---
title: "CI/CD 失败复盘与处理记录"
kind: source-summary
original-path: "DDC/raw/CICD_FAILURE_SUMMARY.md"
original-url: ""
source-type: project-doc
ingested: 2026-06-08
updated: 2026-06-08
original-date: 2026-06-04
source-quality: high
retention-level: detailed
retained-sections:
  - "failure-symptoms"
  - "root-causes"
  - "commands"
  - "configuration-snippets"
  - "diagnostic-workflow"
  - "fix-commits"
  - "follow-up-recommendations"
omitted-sections: []
pages-created:
  - "[[gitea-actions-expression-compatibility]]"
  - "[[provision-workflow-merge-deduplication]]"
  - "[[uv-sync-python-upper-bound]]"
  - "[[npm-registry-frontend-docker-build]]"
  - "[[gitea-actions-kubectl-install]]"
  - "[[kubernetes-rollout-timeout-diagnostics]]"
  - "[[python-src-layout-docker-pythonpath]]"
pages-updated: []
contradictions-found: []
---

## 核心摘要

本来源记录了 `wdz-demo` 在华拓新项目上线流程完成 provision 后，推送到 `https://git.htzl.com.cn:30000/htzl/wdz-demo` 并多次触发 Gitea Actions `Deploy` workflow 时遇到的 CI/CD 失败。失败类型覆盖 Gitea Actions 表达式兼容性、provision 初始化 workflow 合并冲突、`uv sync` 解释器选择、npm 镜像源缺包、部署 job 缺少 `kubectl`、Kubernetes rollout timeout，以及 Python `src/` 布局容器缺少 `PYTHONPATH`。

该来源包含可复用的错误文本、配置片段、诊断命令、修复提交和后续排查建议，适合作为 CI/CD 故障处理经验的详细来源页。

---

## 失败模式与处理要点

### Gitea Actions 表达式解析异常

共享 workflow 中的表达式：

```yaml
environment: ${{ github.ref_name == 'main' && 'production' || 'staging' }}
```

在 Gitea Actions / act_runner 中被错误格式化为：

```text
%!t(string=production)
```

处理方式是改为项目自定义 `deploy.yaml`，在 shell 中显式计算环境和 namespace：

```bash
environment="production"
namespace="${BASE_NAMESPACE}"
if [ "${GITHUB_REF_NAME}" = "develop" ]; then
  environment="staging"
  namespace="${BASE_NAMESPACE}-staging"
fi
```

相关提交：`30a28ad ci: deduplicate project workflows`。

### provision 初始化 workflow 合并重复

本地仓库已有自定义 workflow，远端 provision 又生成默认 workflow 时，合并初始化历史可能发生同名文件 add/add 冲突。冲突处理不彻底会让 `deploy.yaml`、`pr-check.yaml`、`openhands-resolve.yaml` 出现两个 workflow 拼在同一个文件里的情况。

验证命令：

```bash
rg '^name:' .gitea/workflows
```

期望结果是每个 workflow 文件只有一个顶层 `name:`。相关提交：`30a28ad ci: deduplicate project workflows`。

### `uv sync` 选择 Python 3.14 导致 PyO3 构建失败

错误文本：

```text
error: the configured Python interpreter version (3.14) is newer than
PyO3's maximum supported version (3.13)

pydantic-core (v2.27.2) was included because pydantic depends on pydantic-core
```

原配置仅写：

```toml
requires-python = ">=3.11"
```

修复为：

```toml
requires-python = ">=3.11,<3.14"
```

并新增 `.python-version`：

```text
3.11
```

CI 中显式指定：

```bash
./tools/uv/uv sync --frozen --python 3.11
```

Dockerfile 中显式指定：

```dockerfile
RUN chmod +x /usr/local/bin/uv && uv sync --frozen --no-dev --python 3.11
```

相关提交：`3d0caa3 ci: pin Python version for uv sync`。

### 前端 Docker 构建中 npmmirror 返回 404

错误文本：

```text
npm error 404 Not Found - GET https://cdn.npmmirror.com/packages/electron-to-chromium/1.5.367/...
electron-to-chromium@... is not in this registry
```

原 Dockerfile 强制使用：

```dockerfile
RUN npm config set registry https://registry.npmmirror.com && npm ci
```

修复为：

```dockerfile
RUN npm ci --registry=https://registry.npmjs.org
```

验证命令：

```bash
npm ci --registry=https://registry.npmjs.org
npm run build
```

相关提交：`f3e6247 ci: use npm registry for frontend image build`。

### 部署步骤缺少 `kubectl`

错误文本：

```text
/var/run/act/workflow/7.sh: line 9: kubectl: command not found
Failure - Main Sync APP_ENV to Kubernetes
```

原因是 Gitea Actions runner 的 job 容器没有预装 `kubectl`，但自定义 `deploy.yaml` 直接执行了：

```bash
kubectl create secret ...
kubectl set image ...
kubectl rollout status ...
```

处理方式是在 `Configure kubeconfig` 前增加：

```yaml
- name: Install kubectl
  uses: azure/setup-kubectl@v4
  with:
    version: "v1.30.7"
```

相关提交：`3ab5a33 ci: install kubectl before deploy steps`。

### 后端 Deployment rollout 超时

rollout 超时日志：

```text
deployment.apps/wdz-demo-backend image updated
Waiting for deployment "wdz-demo-backend" rollout to finish:
1 out of 2 new replicas have been updated...
error: timed out waiting for the condition
```

诊断输出显示：

```text
wdz-demo-backend ... CrashLoopBackOff
Last State: Terminated
Exit Code: 1
```

`ci-deployer` ServiceAccount 缺少 `pods/log` 权限时，workflow 无法直接读取容器日志：

```text
cannot get resource "pods/log" in API group "" in the namespace "wdz-demo"
```

失败诊断步骤应在 rollout 失败时输出：

```bash
kubectl get deployment -n "$namespace" -o wide
kubectl get rs -n "$namespace" -o wide
kubectl get pods -n "$namespace" -o wide
kubectl get events -n "$namespace" --sort-by=.lastTimestamp | tail -n 80
kubectl describe deployment ...
kubectl describe pod ...
kubectl logs ... --all-containers --tail=200
kubectl logs ... --all-containers --previous --tail=200
```

相关提交：`48969ab ci: dump Kubernetes diagnostics on deploy failure`。

### Python `src/` 布局容器缺少 `PYTHONPATH`

本地按容器启动方式复现：

```bash
./tools/uv/uv run uvicorn ai_math_question_poc.api.app:create_app --factory --host 127.0.0.1 --port 18000
```

错误：

```text
ModuleNotFoundError: No module named 'ai_math_question_poc'
```

后端代码位于：

```text
src/ai_math_question_poc
```

Dockerfile 只执行：

```dockerfile
COPY src ./src
```

但启动命令是：

```dockerfile
CMD ["uvicorn", "ai_math_question_poc.api.app:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
```

最终修复是在后端 Dockerfile 中补充：

```dockerfile
ENV PYTHONUNBUFFERED=1 \
    UV_CACHE_DIR=/tmp/uv-cache \
    PYTHONPATH=/app/src \
    PATH="/app/.venv/bin:${PATH}"
```

本地验证命令：

```bash
PYTHONPATH=src ./tools/uv/uv run python -c "from ai_math_question_poc.api.app import create_app; print(create_app().title)"
```

输出：

```text
AI Math Question POC
```

相关提交：`8ddda7a ci: set backend Python path in image`。

---

## 对 Wiki 的影响

### 新建的知识点

- [[gitea-actions-expression-compatibility]] — 记录 Gitea Actions / act_runner 对 boolean/string 表达式的兼容性陷阱。
- [[provision-workflow-merge-deduplication]] — 记录 provision 初始化 workflow 与本地 workflow 合并后的去重检查流程。
- [[uv-sync-python-upper-bound]] — 记录 `uv sync` 在 CI 中选择过新 Python 解释器导致 PyO3 构建失败的规避规则。
- [[npm-registry-frontend-docker-build]] — 记录前端 Docker 构建中 npm registry 选择的历史决策。
- [[gitea-actions-kubectl-install]] — 记录 Gitea Actions 部署 job 中显式安装 `kubectl` 的前置步骤。
- [[kubernetes-rollout-timeout-diagnostics]] — 记录 Kubernetes rollout timeout 的 CI 诊断输出流程。
- [[python-src-layout-docker-pythonpath]] — 记录 Python `src/` 布局后端镜像需要设置 `PYTHONPATH=/app/src` 的系统关系。

### 更新的知识点

无。

### 发现的矛盾

无。

---

## 入库保真说明

本次入库保留了原始记录中的失败现象、关键错误文本、根因、修复命令/配置、验证命令、相关提交和后续排查建议。命令、路径、错误信息、配置片段均尽量原样保留到来源页或对应知识点页。

未舍弃主要章节；重复的背景叙述仅在知识点页中压缩为来源说明，完整上下文保留在本来源页。

---

## 关键摘录与原文保真片段

> 当前后端 `CrashLoopBackOff` 的已确认根因是容器缺少 `PYTHONPATH=/app/src`；已通过 Dockerfile 修复。

> 如果再次出现 rollout timeout，优先查看 `Dump Kubernetes diagnostics on deploy failure` 步骤输出。
