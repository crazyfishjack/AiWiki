---
title: "OpenSpec + Superpowers + Cursor 命令级实操调研"
kind: source-summary
original-path: "raw/articles/2026-06-02-openspec-superpowers-cursor-command-workflow-research.md"
original-url: ""
source-type: article
ingested: 2026-06-02
updated: 2026-06-02
original-date: 2026-06-02
source-quality: high
retention-level: detailed
retained-sections:
  - "core-conclusions"
  - "commands"
  - "cursor-slash-commands"
  - "workflow"
  - "examples"
  - "review-checklists"
  - "risks"
  - "source-by-source-summary"
  - "contradictions-and-open-questions"
omitted-sections:
  - "stars-count — 数字随时间变化且非本次命令级 SOP 的核心事实"
  - "重复性宣传语 — 无独立复用价值"
pages-created: []
pages-updated:
  - "[[openspec]]"
  - "[[superpowers]]"
  - "[[openspec-superpowers-cursor-workflow]]"
contradictions-found: []
---

## 核心摘要

该调研报告补充了 OpenSpec、Superpowers 与 Cursor 组合使用时的命令级实操信息。报告基于 OpenSpec 官方命令文档、CLI 文档、supported tools 文档、Superpowers 官方 README 和 Cursor 安装页，整理了 OpenSpec 安装、初始化、Cursor 命令生成路径、`/opsx:*` 斜杠命令、`openspec validate` / `archive` 等 CLI 命令，以及 Superpowers 在 Cursor Agent 中的插件安装和验证方式。报告同时标注了命令语法差异，例如 Superpowers 安装命令在不同官方页面中分别写作 `/add-plugin superpowers` 和 `/plugin-add superpowers`。

---

## 可复用事实与命令清单

1. OpenSpec 在 Cursor 中会安装 `.cursor/skills/openspec-*/SKILL.md` 和 `.cursor/commands/opsx-*.md`，默认 core profile 包含 `propose`、`explore`、`apply`、`sync`、`archive`。
2. OpenSpec 的基础安装和初始化命令是 `npm install -g @fission-ai/openspec@latest`、`openspec init`，非交互配置 Cursor 可用 `openspec init --tools cursor`。
3. OpenSpec 的核心 Cursor 斜杠命令是 `/opsx:explore`、`/opsx:propose`、`/opsx:apply`、`/opsx:sync`、`/opsx:archive`，扩展命令包括 `/opsx:verify`、`/opsx:continue` 等。
4. Superpowers 在 Cursor 中通过 Agent chat 的插件市场安装；官方来源存在 `/add-plugin superpowers` 与 `/plugin-add superpowers` 两种写法，实际应以当前 Cursor 支持的插件语法为准。
5. 组合使用时，OpenSpec 适合作为规格和变更控制平面，Superpowers 适合作为 Cursor 代理执行纪律层。
6. Cursor 本身适合执行代码编辑，但不提供完整规格生命周期和强制规格一致性，多会话、多文件或长期功能更需要 OpenSpec 这类外部规格层。

### OpenSpec 安装与初始化

```bash
npm install -g @fission-ai/openspec@latest
cd your-project
openspec init
```

非交互配置 Cursor：

```bash
openspec init --tools cursor
```

同时配置 Claude Code 与 Cursor：

```bash
openspec init --tools claude,cursor
```

升级后刷新项目内指令文件：

```bash
npm update @fission-ai/openspec
openspec update
```

Cursor 相关生成路径：

```text
.cursor/skills/openspec-*/SKILL.md
.cursor/commands/opsx-*.md
```

### OpenSpec CLI

```bash
openspec list
openspec list --specs
openspec spec list --long
openspec show <change-id>
openspec show <spec-id> --type spec
openspec show <change-id> --json --deltas-only
openspec validate <change-id> --strict
openspec validate --all
openspec validate --all --json
openspec archive <change-id> --yes
openspec archive <change-id> --skip-specs --yes
openspec config profile
openspec update
```

### OpenSpec 目录与规格写法

OpenSpec 变更通常围绕 `openspec/changes/<change-id>/` 下的 `proposal.md`、`design.md`、`tasks.md` 和 `specs/<capability>/spec.md` 组织；当前系统行为的 source of truth 存放在 `openspec/specs/`，完成后的变更归档到 `openspec/changes/archive/`。

```text
openspec/changes/<change-id>/
├── proposal.md
├── design.md
├── tasks.md
└── specs/
    └── <capability>/spec.md
```

delta spec 使用明确的操作头，每个 requirement 至少应包含一个 scenario：

```markdown
## ADDED Requirements

### Requirement: New Feature
The system SHALL provide...

#### Scenario: Success case
- **WHEN** user performs action
- **THEN** expected result

## MODIFIED Requirements

### Requirement: Existing Feature
[Complete updated requirement text]

## REMOVED Requirements

### Requirement: Old Feature
**Reason**: [Why removing]
**Migration**: [How to handle]
```

创建 proposal 前可先检查现有能力和并行变更，避免重复或冲突：

```bash
openspec list
openspec list --specs
openspec show <spec-id> --type spec
rg -n "Requirement:|Scenario:" openspec/specs
```

### Cursor 中的 OpenSpec 命令

默认 core profile：

```text
/opsx:explore [topic]
/opsx:propose [change-name-or-description]
/opsx:apply [change-name]
/opsx:sync [change-name]
/opsx:archive [change-name]
```

扩展 workflow：

```text
/opsx:new [change-name] [--schema <schema-name>]
/opsx:continue [change-name]
/opsx:ff [change-name]
/opsx:verify [change-name]
/opsx:bulk-archive [change-names...]
/opsx:onboard
```

旧文档或社区示例中可能出现：

```text
/openspec-proposal Add user authentication with 2FA
/openspec-apply add-user-auth
/openspec-archive add-user-auth
/opsx-propose add-admin-two-factor-auth
```

实际使用时以 `openspec init` / `openspec update` 在 `.cursor/commands/` 生成的命令为准。

### Superpowers Cursor 插件

官方 README 写法：

```text
/add-plugin superpowers
```

官方安装页写法：

```text
/plugin-add superpowers
```

验证、更新、卸载：

```text
Do you have superpowers?
/plugin-update superpowers
/plugin-remove superpowers
```

若技能未自动触发，可显式要求：

```text
use the brainstorming skill
use the writing-plans skill
use the test-driven-development skill
use the systematic-debugging skill
use the verification-before-completion skill
```

---

## 操作流程与示例

### 一次性初始化

1. 安装 OpenSpec：`npm install -g @fission-ai/openspec@latest`。
2. 进入项目目录：`cd your-project`。
3. 初始化并配置 Cursor：`openspec init --tools cursor`。
4. 在 Cursor Agent chat 安装 Superpowers：优先尝试 `/add-plugin superpowers`，失败时尝试 `/plugin-add superpowers`。
5. 新开 Agent 会话并询问：`Do you have superpowers?`。
6. 运行 `openspec list`、`openspec list --specs` 检查项目状态。
7. 确认 `.cursor/commands/opsx-*.md` 与 `.cursor/skills/openspec-*/SKILL.md` 已生成。

### 新功能开发命令链

```text
/opsx:explore How should we add two-factor authentication for admin users?
/opsx:propose add-admin-two-factor-auth
```

审查文件：

```text
openspec/changes/add-admin-two-factor-auth/proposal.md
openspec/changes/add-admin-two-factor-auth/design.md
openspec/changes/add-admin-two-factor-auth/tasks.md
openspec/changes/add-admin-two-factor-auth/specs/<capability>/spec.md
```

验证 proposal：

```bash
openspec validate add-admin-two-factor-auth --strict
openspec show add-admin-two-factor-auth
```

执行实现：

```text
/opsx:apply add-admin-two-factor-auth
```

加强版提示词：

```text
/opsx:apply add-admin-two-factor-auth

Use Superpowers discipline:
- read proposal.md, design.md, tasks.md and spec deltas first
- use test-driven-development for security-critical logic
- complete tasks sequentially
- run relevant tests after each task group
- only check a task when implementation and verification are actually done
- do not implement out-of-scope behavior
```

验证：

```bash
openspec validate add-admin-two-factor-auth --strict
```

```text
/opsx:verify add-admin-two-factor-auth
```

也可要求 Superpowers：

```text
use the verification-before-completion skill.
Verify the implementation against openspec/changes/add-admin-two-factor-auth:
- all tasks complete
- all requirements implemented
- all scenarios covered by tests or explicit manual verification
- no out-of-scope behavior added
```

归档：

```text
/opsx:archive add-admin-two-factor-auth
```

或：

```bash
openspec archive add-admin-two-factor-auth --yes
openspec validate --all
```

### 复杂需求

```bash
openspec config profile
openspec update
```

```text
/opsx:new add-admin-two-factor-auth
/opsx:continue add-admin-two-factor-auth
```

需求清楚时可一次性生成规划工件：

```text
/opsx:ff add-admin-two-factor-auth
```

### Bug 修复

恢复既有预期行为的 bug fix、typo、格式、注释、非破坏性依赖更新、既有行为测试可跳过 OpenSpec proposal。更适合先用：

```text
use the systematic-debugging skill.
Investigate this bug. Do not write a fix until you identify the root cause and reproduce it.
```

如果排查后发现需要改变现有行为、API、schema、安全策略或架构，再创建 OpenSpec change。

---

## 审查清单

创建或实施 OpenSpec change 前应检查：

- `proposal.md` 是否写清 why、scope、out of scope。
- delta spec 是否使用 `ADDED`、`MODIFIED`、`REMOVED` requirements。
- 每个 requirement 是否至少包含一个 scenario。
- `tasks.md` 是否绑定测试或验证方式。
- 是否与现有 active changes 冲突，可用 `openspec list` 检查。
- 实施阶段是否只在验证完成后勾选 task。
- 是否存在 out-of-scope 行为被 Cursor “顺手实现”。

---

## 对 Wiki 的影响

### 新建的知识点

无。

### 更新的知识点

- [[openspec]] — 补充 OpenSpec 的安装、初始化、Cursor 生成路径、CLI 命令、规格资产结构、delta spec 写法和 `/opsx:*` 命令面。
- [[superpowers]] — 补充 Cursor Agent 中的插件安装、验证、更新、卸载命令、Agent chat 使用边界，以及命令语法差异。
- [[openspec-superpowers-cursor-workflow]] — 补充 OpenSpec + Superpowers + Cursor 的命令级实施流程、proposal 前检查、规格资产说明和阶段映射。

### 发现的矛盾

无正式页面矛盾；来源内部记录了两类待验证差异：Superpowers Cursor 安装命令在不同官方页面中分别写作 `/add-plugin superpowers` 与 `/plugin-add superpowers`，OpenSpec Cursor 命令在不同来源中存在 `/opsx:*`、`/opsx-*`、`/openspec-*` 等写法差异。

---

## 来源与可信度索引

- https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md — OpenSpec 官方命令参考。可信度：高。支撑 `/opsx:*`、core/expanded profiles、apply/verify/archive。
- https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/cli.md — OpenSpec 官方 CLI 参考。可信度：高。支撑 `openspec init`、`openspec update`、`--tools cursor`、`validate --json`。
- https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md — OpenSpec 官方支持工具文档。可信度：高。支撑 Cursor skills/commands 生成路径。
- https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/getting-started.md — OpenSpec 官方入门文档。可信度：高。支撑目录结构、artifacts、delta specs、archive 行为。
- https://raw.githubusercontent.com/obra/superpowers/main/README.md — Superpowers 官方 README。可信度：高。支撑 Cursor 安装、基础技能流程、技能列表。
- https://obra-superpowers.mintlify.app/installation/cursor — Superpowers Cursor 安装页。可信度：中。支撑 `/plugin-add`、验证、更新、卸载；与 README 命令写法有差异。
- https://docs.runmaestro.ai/openspec-commands — Maestro 文档。可信度：中。支撑 OpenSpec vs Spec-Kit、proposal/apply/archive、CLI 命令速查。
- https://forum.cursor.com/t/openspec-lightweight-portable-spec-driven-framework-for-ai-coding-assistants/134052 — Cursor 论坛发布帖。可信度：中。支撑旧/社区命令面。
- https://recca0120.github.io/en/2026/03/08/openspec-sdd — 社区技术博客。可信度：中。支撑安装命令、`/opsx:*` 示例、delta spec 说明。
- https://www.augmentcode.com/guides/cursor-spec-driven-development — 厂商分析文章。可信度：中。支撑 Cursor 在 SDD 中的边界与缺口。
- https://raw.githubusercontent.com/Veath/openspec-spec-driven-superpowers/main/README.md — 社区集成仓库 README。可信度：中偏低。支撑 OpenSpec control plane + Superpowers working discipline 模型。
- https://dev.to/webdeveloperhyper/how-to-make-ai-follow-your-instructions-more-for-free-openspec-2c85 — 个人实践文章。可信度：中。支撑 AGENTS 指令内容、proposal/implementation/archive 检查清单。

---

## 对于可信度较高的来源逐来源总结

### OpenSpec 官方 commands.md

该来源是 OpenSpec Cursor slash commands 的直接参考。它确认默认 core profile 包含 `/opsx:propose`、`/opsx:explore`、`/opsx:apply`、`/opsx:sync`、`/opsx:archive`；扩展 workflow 包含 `/opsx:new`、`/opsx:continue`、`/opsx:ff`、`/opsx:verify`、`/opsx:bulk-archive`、`/opsx:onboard`。它还说明默认 global profile 是 `core`，如需扩展命令，应运行 `openspec config profile` 选择 workflows，再在项目中运行 `openspec update`。

- 可入库知识点：OpenSpec slash command reference、OpenSpec expanded workflow、OpenSpec verify workflow。
- 局限：它定义当前 OpenSpec 命令参考，但 Cursor 内实际命令仍受本地生成文件、profile 和 tool adapter 影响。

### OpenSpec 官方 CLI 文档

该来源定义 `openspec init`、`openspec update`、`openspec list`、`openspec show`、`openspec validate`、`openspec archive` 等终端命令。它确认 `openspec init --tools cursor` 或 `openspec init --tools claude,cursor` 可非交互配置工具，并说明初始化后会生成 `openspec/`、`.cursor/skills/`、`.cursor/commands/` 等文件。

- 可入库知识点：OpenSpec CLI、OpenSpec Cursor initialization、OpenSpec validation commands。
- 局限：CLI 文档范围较广，本来源页只保留与 Cursor + Superpowers 组合相关的命令。

### OpenSpec supported-tools.md

该来源提供 OpenSpec 对 Cursor 的关键事实：Cursor skills path 是 `.cursor/skills/openspec-*/SKILL.md`，command path 是 `.cursor/commands/opsx-*.md`。它还说明 core profile 默认包括 `propose`、`explore`、`apply`、`sync`、`archive`，扩展 workflow 可通过配置启用。

- 可入库知识点：OpenSpec supported tools、Cursor OpenSpec command installation paths。
- 局限：该文档说明文件路径和 profile，不详细说明如何与 Superpowers 协同。

### OpenSpec getting-started.md

该来源解释 OpenSpec 初始化后的结构、proposal/specs/design/tasks 四类 artifact、delta spec 的 `ADDED` / `MODIFIED` / `REMOVED` 格式，以及 archive 如何把 delta 合并到主 specs 并移动到 archive。

- 可入库知识点：OpenSpec artifacts、OpenSpec delta specs、OpenSpec archive semantics。
- 局限：主要覆盖 OpenSpec 内部流程，不覆盖 Superpowers。

### Superpowers 官方 README

该来源定义 Superpowers 是面向 coding agents 的软件开发方法论，基于 composable skills 和初始指令。Cursor 安装方式为在 Cursor Agent chat 运行 `/add-plugin superpowers` 或在插件市场搜索。它列出基本 workflow：brainstorming、using-git-worktrees、writing-plans、subagent-driven-development / executing-plans、test-driven-development、requesting-code-review、finishing-a-development-branch。

- 可入库知识点：Superpowers Cursor installation、Superpowers skills workflow、Superpowers TDD discipline。
- 局限：README 没有专门说明 OpenSpec 集成方式。

### Superpowers Cursor 安装页

该来源专门说明 Cursor 安装：打开 Agent chat，运行 `/plugin-add superpowers`，用 `Do you have superpowers?` 验证，用 `/plugin-update superpowers` 更新，用 `/plugin-remove superpowers` 卸载。它还提醒 Cursor Agent 和 Cursor Composer 不同，Superpowers 更适合 Agent chat。

- 可入库知识点：Superpowers Cursor plugin lifecycle、Agent chat 使用位置。
- 局限：与官方 README 中 `/add-plugin superpowers` 命令不一致，因此命令名需要保留版本/语法差异。

### Cursor SDD 分析文章

该来源认为 Cursor 是强执行环境但不是完整 SDD 系统，缺少原生 spec lifecycle management、structured spec-to-task traceability 和 enforcement。它建议单会话任务用 Cursor 即可，多会话功能可叠加 OpenSpec。

- 可入库知识点：Cursor 与 SDD 的边界、Cursor + OpenSpec 的适用场景。
- 局限：该文章来自厂商，有推广自身产品的倾向，应作为分析观点而非中立标准。

### Veath openspec-spec-driven-superpowers README

该来源直接讨论 OpenSpec + Superpowers 的组合方式，主张 OpenSpec 是 control plane，Superpowers 升级 working discipline，并保留 `/opsx:*` 命令面。它提出 `review.md` 作为 readiness gate、`plan.md` 作为 apply-time execution driver、`verification.md` 作为可选证据。

- 可入库知识点：OpenSpec + Superpowers 组合模式、spec-driven-superpowers schema。
- 局限：这是社区仓库，不代表 OpenSpec 或 Superpowers 官方集成标准。

---

## 矛盾、版本差异与待验证项

- Superpowers Cursor 安装命令存在差异：官方 README 写 `/add-plugin superpowers`，官方安装页写 `/plugin-add superpowers`；实际应以当前 Cursor Agent chat 支持的插件命令为准。
- OpenSpec Cursor slash command 存在差异：官方 commands 文档写 `/opsx:propose`，Cursor 论坛早期发布帖写 `/openspec-proposal`，supported-tools 文档显示 Cursor command 文件为 `.cursor/commands/opsx-*.md`。
- Node.js 20.19.0+ 要求来自社区指南，未在本次入库中作为高置信官方事实使用。
- OpenSpec、Superpowers 的 stars、版本号、增长速度等数字随时间变化，不作为稳定知识写入知识页。
- Veath 的 `openspec-spec-driven-superpowers` 贴近本主题，但属于社区集成方案，不代表官方默认做法。

---

## 入库保真说明

- 已保留：核心结论、OpenSpec 安装/初始化命令、CLI 命令、Cursor slash commands、Superpowers 插件命令、显式技能触发示例、新功能开发流程、复杂需求路径、Bug 修复路径、审查清单、来源可信度索引、命令差异和待验证项。
- 已转换：raw 中的长篇推荐工作流被拆成「操作流程与示例」；逐来源总结已补录为独立章节，保留各来源的可用事实、局限和入库知识点。
- 未保留：stars 数、版本号等易过时数字；重复性宣传语；与本命令级 SOP 无直接关系的扩展阅读标题。
- 完整原文：`raw/articles/2026-06-02-openspec-superpowers-cursor-command-workflow-research.md`。

---

## 关键摘录与原文保真片段

> For each selected tool, OpenSpec can install: Skills ... Commands ... Cursor (`cursor`) | `.cursor/skills/openspec-*/SKILL.md` | `.cursor/commands/opsx-.md`。

> The default global profile is `core`. To enable expanded workflow commands, run `openspec config profile`, select workflows, then run `openspec update` in your project。

> In Cursor Agent chat, install from marketplace: `/add-plugin superpowers`。

> In the Agent chat, run the plugin installation command: `/plugin-add superpowers` ... Update to the latest version: `/plugin-update superpowers`。
