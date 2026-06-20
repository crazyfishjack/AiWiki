---
title: "provision 初始化 workflow 合并去重规则"
kind: workflow
domain: workflows
aliases:
  - "workflow add/add 冲突去重"
  - "Gitea workflow 合并去重"
created: 2026-06-08
updated: 2026-06-08
confidence: medium
status: active
sources:
  - "[[sources/cicd-failure-summary]]"
source-count: 1
relations:
  related-to:
    - "[[gitea-actions-expression-compatibility]]"
  is-part-of: []
  depends-on: []
  contradicts: []
  supersedes: []
  derived-from: []
tags: ["CICD失败经验总结"]
---

## 定义

provision 初始化 workflow 合并去重规则，是指本地已有 workflow 与远端 provision 默认 workflow 合并后，必须检查并清理同名文件重复内容，确保每个 workflow 文件只有一个顶层 `name:`。

---

## 触发场景

`wdz-demo` 本地仓库先有自定义 workflow，远端 `htzl/wdz-demo` provision 也生成了一套默认 workflow。合并远端初始化历史时，同名文件发生 add/add 冲突。解决冲突后，部分文件保留了重复内容，等价于两个 workflow 拼在同一个文件里。

受影响文件：

```text
.gitea/workflows/deploy.yaml
.gitea/workflows/pr-check.yaml
.gitea/workflows/openhands-resolve.yaml
```

---

## 检查流程

清理重复 YAML 内容后，用下面命令确认每个 workflow 文件只有一个顶层 `name:`：

```bash
rg '^name:' .gitea/workflows
```

如果某个 workflow 文件出现多个 `name:`，优先检查是否把本地自定义 workflow 和 provision 默认 workflow 都保留在同一文件中。

---

## 验证结果

已验证修复提交：

```text
30a28ad ci: deduplicate project workflows
```

验证结果是每个 workflow 文件只出现一次 `name:`。

---

## 关联说明

- [[gitea-actions-expression-compatibility]] — related-to — 两者都来自 provision 后对 Gitea deploy workflow 的修复。

---

## 来源

- [[sources/cicd-failure-summary]] — 提供重复 workflow 现象、根因、受影响文件、验证命令和修复提交。
