# CI/CD 失败复盘与处理记录

_最后更新：2026-06-04_

## 背景

项目 `wdz-demo` 通过华拓新项目上线流程完成 provision 后，我们将当前代码推送到新仓库：

```text
https://git.htzl.com.cn:30000/htzl/wdz-demo
```

随后多次触发 Gitea Actions 的 `Deploy` workflow。过程中连续遇到几类 CI/CD 失败，下面记录每次失败的现象、根因、修复办法和后续建议。

## 1. 共享 deploy workflow 表达式解析异常

### 现象

日志中出现：

```text
expression '${{ github.ref_name == 'main' && 'production' || 'staging' }}'
evaluated to '%!t(string=production)'
Job 'Build & Push → Harbor' failed
```

### 根因

provision 默认生成的 `deploy.yaml` 调用了共享 workflow：

```yaml
uses: htzl/htzl-ai-context/.gitea/workflows/ci/deploy-python-fastapi.yaml@main
```

其中 `environment` 使用了 Gitea/act_runner 对 boolean/string 表达式兼容性不好的写法：

```yaml
environment: ${{ github.ref_name == 'main' && 'production' || 'staging' }}
```

act_runner 将表达式错误格式化成：

```text
%!t(string=production)
```

这是 Gitea Actions / act_runner 对表达式求值的兼容性问题，不是应用代码问题。

### 处理

改为项目自定义 `deploy.yaml`，不再使用该共享 deploy caller 的 `environment` 表达式，而是在 shell 中计算部署变量：

```bash
environment="production"
namespace="${BASE_NAMESPACE}"
if [ "${GITHUB_REF_NAME}" = "develop" ]; then
  environment="staging"
  namespace="${BASE_NAMESPACE}-staging"
fi
```

相关提交：

```text
30a28ad ci: deduplicate project workflows
```

## 2. 合并 provision 初始化历史后 workflow 内容重复

### 现象

`deploy.yaml`、`pr-check.yaml`、`openhands-resolve.yaml` 中出现重复 YAML 内容，等价于两个 workflow 拼在同一个文件里。

### 根因

本地仓库先有自定义 workflow，远端 `htzl/wdz-demo` provision 也生成了一套默认 workflow。合并远端初始化历史时，同名文件发生 add/add 冲突。解决冲突后，部分文件保留了重复内容。

### 处理

清理重复内容，确保每个 workflow 文件只有一个顶层 `name:`：

```text
.gitea/workflows/deploy.yaml
.gitea/workflows/pr-check.yaml
.gitea/workflows/openhands-resolve.yaml
```

并确认：

```bash
rg '^name:' .gitea/workflows
```

结果每个文件只出现一次。

相关提交：

```text
30a28ad ci: deduplicate project workflows
```

## 3. `uv sync` 选择 Python 3.14 导致 PyO3 构建失败

### 现象

CI 后端检查失败：

```text
error: the configured Python interpreter version (3.14) is newer than
PyO3's maximum supported version (3.13)

pydantic-core (v2.27.2) was included because pydantic depends on pydantic-core
```

### 根因

`pyproject.toml` 原本只写了：

```toml
requires-python = ">=3.11"
```

CI runner 中 `uv sync --frozen` 会选择最新兼容解释器，结果选中了 Python 3.14。当前 `pydantic-core` 依赖 PyO3，而该版本 PyO3 最高支持 Python 3.13，因此构建失败。

### 处理

显式锁定 Python 版本范围，并让本地、CI、Docker 构建保持一致。

修改 `pyproject.toml`：

```toml
requires-python = ">=3.11,<3.14"
```

新增 `.python-version`：

```text
3.11
```

CI 中显式指定：

```bash
./tools/uv/uv sync --frozen --python 3.11
```

Dockerfile 中也显式指定：

```dockerfile
RUN chmod +x /usr/local/bin/uv && uv sync --frozen --no-dev --python 3.11
```

相关提交：

```text
3d0caa3 ci: pin Python version for uv sync
```

## 4. 前端 Docker 构建中 `npmmirror` 返回 404

### 现象

前端镜像构建失败：

```text
npm error 404 Not Found - GET https://cdn.npmmirror.com/packages/electron-to-chromium/1.5.367/...
electron-to-chromium@... is not in this registry
```

### 根因

`frontend/Dockerfile` 原本强制使用：

```dockerfile
RUN npm config set registry https://registry.npmmirror.com && npm ci
```

但 `package-lock.json` 锁定的 `electron-to-chromium@1.5.367` 在 `npmmirror` 当前不可用，导致 `npm ci` 失败。

本地验证 npm 官方 registry 可正常获取该包。

### 处理

改为在 Docker 构建中使用 npm 官方 registry：

```dockerfile
RUN npm ci --registry=https://registry.npmjs.org
```

验证命令：

```bash
npm ci --registry=https://registry.npmjs.org
npm run build
```

相关提交：

```text
f3e6247 ci: use npm registry for frontend image build
```

## 5. 部署步骤缺少 `kubectl`

### 现象

部署阶段失败：

```text
/var/run/act/workflow/7.sh: line 9: kubectl: command not found
Failure - Main Sync APP_ENV to Kubernetes
```

### 根因

自定义 `deploy.yaml` 中直接执行了：

```bash
kubectl create secret ...
kubectl set image ...
kubectl rollout status ...
```

但 Gitea Actions runner 的 job 容器并没有预装 `kubectl`。

### 处理

在 `Configure kubeconfig` 之前增加安装步骤：

```yaml
- name: Install kubectl
  uses: azure/setup-kubectl@v4
  with:
    version: "v1.30.7"
```

相关提交：

```text
3ab5a33 ci: install kubectl before deploy steps
```

## 6. 后端 Deployment rollout 超时

### 现象

部署阶段失败：

```text
deployment.apps/wdz-demo-backend image updated
Waiting for deployment "wdz-demo-backend" rollout to finish:
1 out of 2 new replicas have been updated...
error: timed out waiting for the condition
```

### 诊断过程

这说明镜像已经成功更新到 Kubernetes Deployment，但新 Pod 没有在超时时间内全部 Ready。诊断步骤打印出：

```text
wdz-demo-backend ... CrashLoopBackOff
Last State: Terminated
Exit Code: 1
```

这说明后端容器已经成功拉取并启动过，但进程很快退出。CI 使用的 `ci-deployer` ServiceAccount 没有 `pods/log` 权限，所以 workflow 无法直接读取容器日志：

```text
cannot get resource "pods/log" in API group "" in the namespace "wdz-demo"
```

随后在本地按容器启动方式复现：

```bash
./tools/uv/uv run uvicorn ai_math_question_poc.api.app:create_app --factory --host 127.0.0.1 --port 18000
```

出现：

```text
ModuleNotFoundError: No module named 'ai_math_question_poc'
```

### 最终根因

后端代码位于：

```text
src/ai_math_question_poc
```

Dockerfile 中只执行了：

```dockerfile
COPY src ./src
```

但容器启动命令是：

```dockerfile
CMD ["uvicorn", "ai_math_question_poc.api.app:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
```

容器运行时没有设置 `PYTHONPATH=/app/src`，Python 无法从 `src/` 目录找到 `ai_math_question_poc` 包，导致 Uvicorn 启动即退出，Kubernetes 看到的结果就是 `CrashLoopBackOff`。

### 处理

没有继续猜测具体原因，而是在 `deploy.yaml` 中新增失败诊断步骤，rollout 失败时自动打印：

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

相关提交：

```text
48969ab ci: dump Kubernetes diagnostics on deploy failure
```

下一次 rollout 失败时，CI 日志会直接包含 Pod events 和容器日志，可以继续定位真实原因。

### 最终修复

在后端 Dockerfile 中补充：

```dockerfile
ENV PYTHONUNBUFFERED=1 \
    UV_CACHE_DIR=/tmp/uv-cache \
    PYTHONPATH=/app/src \
    PATH="/app/.venv/bin:${PATH}"
```

本地验证：

```bash
PYTHONPATH=src ./tools/uv/uv run python -c "from ai_math_question_poc.api.app import create_app; print(create_app().title)"
```

输出：

```text
AI Math Question POC
```

相关提交：

```text
8ddda7a ci: set backend Python path in image
```

## 当前状态

已推送到 `htzl/wdz-demo` 的主要 CI/CD 修复提交：

```text
30a28ad ci: deduplicate project workflows
3d0caa3 ci: pin Python version for uv sync
f3e6247 ci: use npm registry for frontend image build
3ab5a33 ci: install kubectl before deploy steps
48969ab ci: dump Kubernetes diagnostics on deploy failure
8ddda7a ci: set backend Python path in image
```

当前后端 `CrashLoopBackOff` 的已确认根因是容器缺少 `PYTHONPATH=/app/src`；已通过 Dockerfile 修复。

## 后续建议

1. 如果再次出现 rollout timeout，优先查看 `Dump Kubernetes diagnostics on deploy failure` 步骤输出。
2. 如果 Pod 是 `CrashLoopBackOff`，优先检查 Python import path、启动命令、环境变量和容器日志。
3. 如果 Pod 是 `ImagePullBackOff`，检查 Harbor 镜像 tag、`harbor-pull-secret` 和 namespace。
4. 如果 readiness probe 失败，检查 Deployment probe path 是否为 `/health`，以及容器是否监听 `8000`。
5. 后续可以把项目部署流程逐步改回公司共享 workflow，但要避开 act_runner 表达式兼容问题，或等待共享 workflow 适配 string input。
