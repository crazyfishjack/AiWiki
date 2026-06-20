---
title: "uv sync 需要限制 Python 上界以避开 PyO3 构建失败"
kind: workflow
domain: workflows
aliases:
  - "uv sync Python 3.14 PyO3 失败"
  - "PyO3 maximum supported version"
created: 2026-06-08
updated: 2026-06-08
confidence: medium
status: active
sources:
  - "[[sources/cicd-failure-summary]]"
source-count: 1
relations:
  related-to:
    - "[[npm-registry-frontend-docker-build]]"
    - "[[python-src-layout-docker-pythonpath]]"
  is-part-of: []
  depends-on: []
  contradicts: []
  supersedes: []
  derived-from: []
tags: ["CICD失败经验总结"]
---

## 定义

`uv sync` Python 上界约束，是指在 CI、Docker 和本地开发环境中显式限制 Python 版本范围，避免 `uv sync --frozen` 选择过新的解释器并触发 PyO3 依赖构建失败。

---

## 失败现象

CI 后端检查失败，错误文本为：

```text
error: the configured Python interpreter version (3.14) is newer than
PyO3's maximum supported version (3.13)

pydantic-core (v2.27.2) was included because pydantic depends on pydantic-core
```

原始 `pyproject.toml` 只写了：

```toml
requires-python = ">=3.11"
```

CI runner 中 `uv sync --frozen` 会选择最新兼容解释器，因此选中了 Python 3.14。当前 `pydantic-core` 依赖 PyO3，而该版本 PyO3 最高支持 Python 3.13，最终导致构建失败。

---

## 修复流程

在 `pyproject.toml` 中显式锁定 Python 版本范围：

```toml
requires-python = ">=3.11,<3.14"
```

新增 `.python-version`：

```text
3.11
```

CI 中显式指定 Python 版本：

```bash
./tools/uv/uv sync --frozen --python 3.11
```

Dockerfile 中也显式指定：

```dockerfile
RUN chmod +x /usr/local/bin/uv && uv sync --frozen --no-dev --python 3.11
```

---

## 决策规则

只写 `requires-python = ">=3.11"` 对 CI 来说过于宽松。只要依赖中包含 PyO3、Rust 扩展或尚未支持最新 Python 的二进制构建链路，就应同步约束：

- `pyproject.toml` 的 `requires-python`
- `.python-version`
- CI 中的 `uv sync --python`
- Dockerfile 中的 `uv sync --python`

---

## 验证结果

已验证修复提交：

```text
3d0caa3 ci: pin Python version for uv sync
```

---

## 关联说明

- [[npm-registry-frontend-docker-build]] — related-to — 两者都是 Docker/CI 构建阶段的依赖解析失败经验。
- [[python-src-layout-docker-pythonpath]] — related-to — 两者都涉及 Python 后端在 CI 或容器环境中的运行时约束。

---

## 来源

- [[sources/cicd-failure-summary]] — 提供错误文本、根因、配置改动、CI/Docker 命令和修复提交。
