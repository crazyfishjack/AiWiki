---
title: "OpenSpec"
kind: tool
domain: tools
aliases: ["OpenSpec", "Spec-Driven Development", "SDD"]
created: 2026-06-02
updated: 2026-06-02
confidence: medium
status: active
sources:
  - "[[sources/2026-06-02-openspec-superpower-cursor-research]]"
  - "[[sources/2026-06-02-openspec-superpowers-cursor-command-workflow-research]]"
source-count: 2
relations:
  related-to:
    - "[[superpowers]]"
    - "[[openspec-superpowers-cursor-workflow]]"
  is-part-of: []
  depends-on: []
  contradicts: []
  supersedes: []
  derived-from: []
tags: ["ai-coding", "sdd", "workflow"]
---

## 定义

OpenSpec 是一种面向 AI 辅助开发的轻量级规格驱动开发工具或框架，用于把模糊需求转化为可审查、可执行、可归档的规格和变更记录。

---

## 详细说明

在本次调研中，OpenSpec 被定位为“规格与变更管理”层。它的价值不在于直接替代编码代理，而在于让编码代理在动手前先围绕 proposal、tasks、spec delta 和 archive 等结构化材料对齐“为什么改、改什么、不改什么”。

与只在聊天窗口中描述需求相比，OpenSpec 更强调将需求、任务、规格增量和历史决策落到磁盘中，使后续迭代可以追溯。该机制适合需求容易漂移、涉及跨模块协作或需要审计历史决策的项目。

命令级调研补充了 OpenSpec 官方文档支撑：基础安装通常使用 `npm install -g @fission-ai/openspec@latest`，项目初始化使用 `openspec init`；若要非交互配置 Cursor，可使用 `openspec init --tools cursor`。初始化后，Cursor 相关文件会落在 `.cursor/skills/openspec-*/SKILL.md` 与 `.cursor/commands/opsx-*.md`。

OpenSpec 的常用终端命令包括 `openspec list`、`openspec list --specs`、`openspec show <item>`、`openspec validate <change-id> --strict` 和 `openspec archive <change-id> --yes`。在 Cursor 中，当前官方命令参考以 `/opsx:*` 为主，默认 core profile 包含 `/opsx:explore`、`/opsx:propose`、`/opsx:apply`、`/opsx:sync` 和 `/opsx:archive`；扩展工作流可通过 `openspec config profile` 后运行 `openspec update` 启用 `/opsx:verify`、`/opsx:continue` 等命令。

OpenSpec 的变更资产通常位于 `openspec/changes/<change-id>/`，包含 `proposal.md`、`design.md`、`tasks.md` 和 `specs/<capability>/spec.md`；当前系统行为的主规格位于 `openspec/specs/`，完成后的变更归档到 `openspec/changes/archive/`。delta spec 使用 `ADDED Requirements`、`MODIFIED Requirements`、`REMOVED Requirements` 等操作头，每个 requirement 至少应包含一个 scenario，以便后续验证和测试对齐。

---

## 关键要点

- OpenSpec 的核心价值是把模糊需求变成可审查的规格资产。
- OpenSpec 更适合约束“做什么、为什么做”，而不是约束编码代理的每一步工程动作。
- OpenSpec 的 archive / 归档思路适合保留长期项目中的设计理由和变更历史。
- 在 Cursor 中，OpenSpec 默认生成 `.cursor/skills/` 和 `.cursor/commands/` 下的技能与命令文件。
- 常用命令链是 `openspec init --tools cursor`、`/opsx:propose`、`/opsx:apply`、`openspec validate <change-id> --strict`、`/opsx:archive`。
- proposal 前可用 `openspec list`、`openspec list --specs`、`openspec show <spec-id> --type spec` 和 `rg -n "Requirement:|Scenario:" openspec/specs` 检查现有能力与潜在冲突。
- OpenSpec 对小型一次性改动可能带来额外流程成本。

---

## 关联说明

- [[superpowers]] — related-to — 两者常被组合用于 AI 编程工作流，但分别约束规格管理和开发行为纪律。
- [[openspec-superpowers-cursor-workflow]] — related-to — 该工作流以 OpenSpec 作为规格和变更管理层。

---

## 来源

- [[sources/2026-06-02-openspec-superpower-cursor-research]] — 提供 OpenSpec 的定位、工作流价值和待验证问题。
- [[sources/2026-06-02-openspec-superpowers-cursor-command-workflow-research]] — 提供 OpenSpec 官方命令、Cursor 初始化路径、CLI 验证和归档命令。
