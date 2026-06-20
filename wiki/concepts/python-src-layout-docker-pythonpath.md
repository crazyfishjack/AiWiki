---
title: "src-layout Python 后端容器需要设置 PYTHONPATH"
kind: concept
domain: concepts
aliases:
  - "Python src layout PYTHONPATH"
  - "容器 ModuleNotFoundError ai_math_question_poc"
created: 2026-06-08
updated: 2026-06-08
confidence: medium
status: active
sources:
  - "[[sources/cicd-failure-summary]]"
source-count: 1
relations:
  related-to:
    - "[[kubernetes-rollout-timeout-diagnostics]]"
    - "[[uv-sync-python-upper-bound]]"
  is-part-of: []
  depends-on: []
  contradicts: []
  supersedes: []
  derived-from: []
tags: ["CICD失败经验总结"]
---

## 定义

`src-layout` Python 后端容器需要设置 `PYTHONPATH`，是指当业务包位于 `/app/src` 下但启动命令按顶层包名导入时，容器运行环境必须让 Python 能从 `src/` 目录解析业务包。

---

## 失败现象

Kubernetes Deployment rollout 超时后，Pod 表现为 `CrashLoopBackOff`：

```text
wdz-demo-backend ... CrashLoopBackOff
Last State: Terminated
Exit Code: 1
```

本地按容器启动方式复现：

```bash
./tools/uv/uv run uvicorn ai_math_question_poc.api.app:create_app --factory --host 127.0.0.1 --port 18000
```

出现：

```text
ModuleNotFoundError: No module named 'ai_math_question_poc'
```

---

## 根因结构

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

---

## 修复方式

在后端 Dockerfile 中补充：

```dockerfile
ENV PYTHONUNBUFFERED=1 \
    UV_CACHE_DIR=/tmp/uv-cache \
    PYTHONPATH=/app/src \
    PATH="/app/.venv/bin:${PATH}"
```

---

## 验证命令

本地验证：

```bash
PYTHONPATH=src ./tools/uv/uv run python -c "from ai_math_question_poc.api.app import create_app; print(create_app().title)"
```

输出：

```text
AI Math Question POC
```

已验证修复提交：

```text
8ddda7a ci: set backend Python path in image
```

---

## 关联说明

- [[kubernetes-rollout-timeout-diagnostics]] — related-to — rollout timeout 诊断流程定位到的最终根因是容器缺少 `PYTHONPATH=/app/src`。
- [[uv-sync-python-upper-bound]] — related-to — 两者都涉及 Python 后端在 CI 或容器环境中的版本与路径约束。

---

## 来源

- [[sources/cicd-failure-summary]] — 提供 CrashLoopBackOff 现象、复现命令、导入错误、Dockerfile 片段、修复方式和验证命令。
