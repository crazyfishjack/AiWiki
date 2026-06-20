---
title: "Gitea Actions 表达式 string/boolean 兼容性陷阱"
kind: concept
domain: concepts
aliases:
  - "act_runner 表达式兼容性"
  - "Gitea Actions environment 表达式异常"
created: 2026-06-08
updated: 2026-06-08
confidence: medium
status: active
sources:
  - "[[sources/cicd-failure-summary]]"
source-count: 1
relations:
  related-to:
    - "[[provision-workflow-merge-deduplication]]"
    - "[[gitea-actions-kubectl-install]]"
  is-part-of: []
  depends-on: []
  contradicts: []
  supersedes: []
  derived-from: []
tags: ["CICD失败经验总结"]
---

## 定义

Gitea Actions 表达式 string/boolean 兼容性陷阱，是指 act_runner 在解析类似 GitHub Actions 的三元替代表达式时，可能把字符串结果按布尔格式错误输出，导致共享 workflow 失败。

---

## 触发场景

`wdz-demo` 的 provision 默认 `deploy.yaml` 调用了共享 workflow：

```yaml
uses: htzl/htzl-ai-context/.gitea/workflows/ci/deploy-python-fastapi.yaml@main
```

共享 workflow 中的 `environment` 使用了 Gitea/act_runner 兼容性不稳定的表达式：

```yaml
environment: ${{ github.ref_name == 'main' && 'production' || 'staging' }}
```

运行时日志出现：

```text
expression '${{ github.ref_name == 'main' && 'production' || 'staging' }}'
evaluated to '%!t(string=production)'
Job 'Build & Push → Harbor' failed
```

这不是应用代码问题，而是 Gitea Actions / act_runner 对表达式求值的兼容性问题。

---

## 处理规则

不要在共享 deploy caller 的 `environment` 字段里依赖 `boolean && string || string` 写法。更稳妥的方式是在项目自定义 `deploy.yaml` 的 shell 中显式计算部署变量：

```bash
environment="production"
namespace="${BASE_NAMESPACE}"
if [ "${GITHUB_REF_NAME}" = "develop" ]; then
  environment="staging"
  namespace="${BASE_NAMESPACE}-staging"
fi
```

已验证修复提交：

```text
30a28ad ci: deduplicate project workflows
```

---

## 适用边界

适用于 Gitea Actions / act_runner 环境，尤其是从 GitHub Actions 迁移表达式语法或调用公司共享 workflow 时。若后续共享 workflow 已改为纯 string input 或明确兼容 Gitea Actions，应以新的共享 workflow 实现为准。

---

## 关联说明

- [[provision-workflow-merge-deduplication]] — related-to — 两者都发生在 provision 后的 Gitea workflow 调整阶段。
- [[gitea-actions-kubectl-install]] — related-to — 两者都属于 Gitea Actions 部署 workflow 的运行时兼容与前置条件问题。

---

## 来源

- [[sources/cicd-failure-summary]] — 提供失败日志、共享 workflow 调用方式、规避写法和修复提交。
