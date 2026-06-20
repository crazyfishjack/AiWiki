---
title: "Superpowers"
kind: tool
domain: tools
aliases: ["Superpowers", "Cursor Superpowers", "Agent Skills"]
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
    - "[[openspec]]"
    - "[[openspec-superpowers-cursor-workflow]]"
  is-part-of: []
  depends-on: []
  contradicts: []
  supersedes: []
  derived-from: []
tags: ["ai-coding", "cursor", "workflow"]
---

## 定义

Superpowers 是一套用于约束 AI 编程代理开发行为的软件开发工作流技能集合，可在 Cursor 中引导代理执行头脑风暴、计划、测试驱动开发、调试、代码审查等任务。

---

## 详细说明

在本次调研中，Superpowers 被定位为“开发行为纪律”层。它并不主要解决需求规格的长期归档问题，而是让 Cursor 代理在实现过程中遵守更明确的工程步骤，例如先规划、再实现、按 TDD 循环推进、系统化调试和执行代码审查。

与 OpenSpec 相比，Superpowers 更关注“怎么做”。它适合把已经明确的规格或任务拆成可执行步骤，并要求 Cursor 在每一步中保留验证动作，降低代理跳过测试、直接改主流程或一次性大改的风险。

命令级调研补充了官方安装来源：在 Cursor 中应打开 Agent chat，通过插件市场安装 Superpowers。官方 README 记录的命令是 `/add-plugin superpowers`，官方安装页记录的命令是 `/plugin-add superpowers`，因此实际操作时应以当前 Cursor Agent 支持的插件语法为准；安装后可用 `Do you have superpowers?` 验证，官方安装页还记录了 `/plugin-update superpowers` 和 `/plugin-remove superpowers`。

Superpowers 在组合工作流中的常见技能包括 `brainstorming`、`writing-plans`、`test-driven-development`、`systematic-debugging`、`verification-before-completion`、`requesting-code-review`、`receiving-code-review`、`subagent-driven-development` 和 `finishing-a-development-branch`。当自动触发不明显时，可在 Cursor 中显式要求“use the brainstorming skill”或“use the systematic-debugging skill”。

Superpowers 的 Cursor 插件生命周期应在 Agent chat 中处理，而不是普通终端。官方安装页还提示 Cursor Agent 与 Cursor Composer 存在使用位置差异，因此验证安装时应新开 Agent 会话并询问 `Do you have superpowers?`；若插件命令不可用，应优先确认当前会话类型和 Cursor 支持的插件命令语法。

---

## 关键要点

- Superpowers 的核心价值是约束 Cursor 代理的工程执行节奏。
- Superpowers 常见技能覆盖规划、TDD、调试、子代理并行和代码审查等开发环节。
- Superpowers 适合与 OpenSpec 搭配：OpenSpec 给出规格边界，Superpowers 驱动实现过程。
- Cursor Agent 中可通过插件市场安装 Superpowers，但 `/add-plugin superpowers` 与 `/plugin-add superpowers` 两种写法需按当前 Cursor 版本复核。
- 安装后可用 `Do you have superpowers?` 验证是否生效。
- 插件更新和卸载可参考 `/plugin-update superpowers`、`/plugin-remove superpowers`，但同样应以当前 Cursor 插件命令面为准。

---

## 关联说明

- [[openspec]] — related-to — 两者常被组合用于 AI 编程工作流，但分别解决开发行为纪律和规格管理问题。
- [[openspec-superpowers-cursor-workflow]] — related-to — 该工作流以 Superpowers 作为 Cursor 代理执行约束层。

---

## 来源

- [[sources/2026-06-02-openspec-superpower-cursor-research]] — 提供 Superpowers 的定位、技能范围和安装细节待验证问题。
- [[sources/2026-06-02-openspec-superpowers-cursor-command-workflow-research]] — 提供 Superpowers 在 Cursor Agent 中的插件安装、验证、更新和技能触发方式。
