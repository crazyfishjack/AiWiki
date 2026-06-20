---
title: "OpenSpec + Superpowers + Cursor 开发工作流"
kind: workflow
domain: workflows
aliases: ["OpenSpec Superpowers Cursor workflow", "OpenSpec + Superpowers 工作流"]
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
    - "[[superpowers]]"
  is-part-of: []
  depends-on:
    - "[[openspec]]"
    - "[[superpowers]]"
  contradicts: []
  supersedes: []
  derived-from: []
tags: ["ai-coding", "cursor", "sdd"]
---

## 定义

OpenSpec + Superpowers + Cursor 开发工作流是一种将规格驱动、代理行为约束和 IDE 内代码执行结合起来的 AI 辅助开发方法：OpenSpec 管理需求和变更，Superpowers 约束实现步骤，Cursor 负责读取上下文、编辑代码和执行验证。

---

## 分层职责

该工作流适合在 Cursor 中处理复杂或长期演进的开发任务。三者分工如下：

- [[openspec]] 管“做什么、为什么、如何归档”：负责 change id、proposal、delta specs、design、tasks、sync 和 archive。
- [[superpowers]] 管“怎么做、如何验证”：负责 brainstorming、writing-plans、test-driven-development、systematic-debugging、verification-before-completion、code review 等执行纪律。
- Cursor 管实际执行：读取项目上下文、编辑代码、运行测试、执行 OpenSpec 斜杠命令和 Superpowers 技能。

该组合不是自动无缝串联的银弹。OpenSpec 输出的规格和 Superpowers 的执行步骤之间可能出现交接断裂，测试也可能被形式化满足，因此需要人工复核规格、任务、测试和代码是否一致。

---

## 一次性初始化

安装并初始化 OpenSpec：

```bash
npm install -g @fission-ai/openspec@latest
cd your-project
openspec init --tools cursor
```

如果同一项目同时给 Claude Code 和 Cursor 使用：

```bash
openspec init --tools claude,cursor
```

升级 OpenSpec 后刷新项目内指令文件：

```bash
npm update @fission-ai/openspec
openspec update
```

初始化后应能看到：

```text
.cursor/skills/openspec-*/SKILL.md
.cursor/commands/opsx-*.md
```

在 Cursor Agent chat 安装 Superpowers。官方来源存在两种写法，优先按当前 Cursor 支持的插件语法执行：

```text
/add-plugin superpowers
/plugin-add superpowers
```

安装后验证：

```text
Do you have superpowers?
```

---

## 常用命令

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
```

### Cursor 斜杠命令

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

启用扩展 workflow：

```bash
openspec config profile
openspec update
```

命令语法可能随 Cursor/OpenSpec 版本变化。实际应以 `.cursor/commands/` 生成文件和 Cursor Agent 插件语法为准。

---

## OpenSpec 规格资产

创建 change 后，应重点审查以下文件：

```text
openspec/changes/<change-id>/
├── proposal.md
├── design.md
├── tasks.md
└── specs/
    └── <capability>/spec.md
```

其中 `proposal.md` 说明 why、what、scope 和 out of scope，`tasks.md` 记录实施清单，`specs/<capability>/spec.md` 记录 delta requirements。delta spec 使用 `ADDED Requirements`、`MODIFIED Requirements`、`REMOVED Requirements` 等操作头，每个 requirement 至少应包含一个 scenario。

proposal 前可先检查现有能力与并行变更：

```bash
openspec list
openspec list --specs
openspec show <spec-id> --type spec
rg -n "Requirement:|Scenario:" openspec/specs
```

---

## 新功能开发 SOP

### 1. 探索需求

需求不清晰时，先探索，不写代码：

```text
/opsx:explore How should we add two-factor authentication for admin users?
```

或显式触发 Superpowers：

```text
use the brainstorming skill. Help me explore how to add two-factor authentication for admin users. Do not write code yet.
```

### 2. 创建 OpenSpec change

```text
/opsx:propose add-admin-two-factor-auth
```

创建后检查这些文件：

```text
openspec/changes/add-admin-two-factor-auth/proposal.md
openspec/changes/add-admin-two-factor-auth/design.md
openspec/changes/add-admin-two-factor-auth/tasks.md
openspec/changes/add-admin-two-factor-auth/specs/<capability>/spec.md
```

### 3. 审查 proposal 和 spec

```bash
openspec validate add-admin-two-factor-auth --strict
openspec show add-admin-two-factor-auth
```

审查清单：

- `proposal.md` 是否写清 why、scope、out of scope。
- delta spec 是否使用 `ADDED`、`MODIFIED`、`REMOVED` requirements。
- 每个 requirement 是否至少包含一个 scenario。
- `tasks.md` 是否绑定测试或验证方式。
- 是否与现有 active changes 冲突，可用 `openspec list` 检查。

### 4. 执行实现

```text
/opsx:apply add-admin-two-factor-auth
```

推荐加强提示词：

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

### 5. 验证

```bash
openspec validate add-admin-two-factor-auth --strict
```

如果启用扩展 workflow：

```text
/opsx:verify add-admin-two-factor-auth
```

也可显式要求 Superpowers 验证：

```text
use the verification-before-completion skill.
Verify the implementation against openspec/changes/add-admin-two-factor-auth:
- all tasks complete
- all requirements implemented
- all scenarios covered by tests or explicit manual verification
- no out-of-scope behavior added
```

### 6. 归档

```text
/opsx:archive add-admin-two-factor-auth
```

或终端执行：

```bash
openspec archive add-admin-two-factor-auth --yes
openspec validate --all
```

归档会把 delta specs 合并进主 `openspec/specs/`，并移动 change 到 `openspec/changes/archive/YYYY-MM-DD-<change-id>/`。

---

## 复杂需求路径

复杂、高风险或需要逐步审查的需求，不建议一次性 `/opsx:propose` 后直接实现。可启用扩展 workflow：

```bash
openspec config profile
openspec update
```

然后分阶段创建工件：

```text
/opsx:new add-admin-two-factor-auth
/opsx:continue add-admin-two-factor-auth
```

如果需求已经非常清楚，可使用：

```text
/opsx:ff add-admin-two-factor-auth
```

---

## Bug 修复路径

恢复既有预期行为的 bug fix、typo、格式、注释、非破坏性依赖更新、既有行为测试，不一定需要完整 OpenSpec proposal。

推荐先用 Superpowers 调试纪律：

```text
use the systematic-debugging skill.
Investigate this bug. Do not write a fix until you identify the root cause and reproduce it.
```

如果排查后发现需要改变现有行为、API、schema、安全策略或架构，再创建 OpenSpec change。

---

## OpenSpec 与 Superpowers 阶段映射

| OpenSpec 阶段 | Superpowers 技能 | 目的 |
| --- | --- | --- |
| `/opsx:explore` | `brainstorming` | 收敛需求、比较方案、避免过早写 proposal |
| `/opsx:propose` 或 `/opsx:new` + `/opsx:continue` | `brainstorming` / `writing-plans` | 形成可审查 proposal、design、tasks |
| 人工审查 artifacts | `requesting-code-review` | 审查规格是否过度、漏测或冲突 |
| `/opsx:apply` | `test-driven-development` / `executing-plans` | 按任务和测试驱动实现 |
| bug 阶段 | `systematic-debugging` | 先定位根因再修复 |
| `/opsx:verify` 或人工验收 | `verification-before-completion` / `requesting-code-review` | 对照规格、测试、实现检查一致性 |
| `/opsx:archive` | `finishing-a-development-branch` | 验证完成、分支/PR/归档收尾 |

---

## 适用边界

适合：

- 老项目渐进改造。
- 多文件、多会话功能。
- 认证、权限、支付、数据迁移、安全策略、API breaking change、架构调整。
- 需要审计和长期维护的项目。
- 希望约束 Cursor 不跳过测试和审查的团队。

不适合：

- 单行 CSS、typo、注释、低风险配置修改。
- 单会话、单文件、强人工实时控制的任务。
- 纯 bug fix 且只是恢复已有 spec 行为。
- 团队不愿维护 archive 和 specs 的项目。

---

## 风险与约束

- Cursor 不强制 phase gate，即使有 OpenSpec，也需要人工要求“proposal 未审批不准实现”。
- `/opsx:verify` 不等于业务正确、安全正确或产品验收通过，仍需真实测试和代码审查。
- OpenSpec 与 Superpowers 不是一个官方一体化产品；社区集成方案可参考，但不代表官方默认做法。
- 命令语法可能随版本变化，优先看本项目 `.cursor/commands/` 和 Cursor 插件市场当前语法。
- stars、版本号、增长速度等数字易过时，不应作为稳定事实引用。

---

## 入库保真说明

- 已保留：安装命令、初始化命令、CLI 命令、Cursor 斜杠命令、插件安装差异、功能开发 SOP、复杂需求路径、Bug 修复路径、审查清单、验证提示词、阶段映射、适用边界和风险。
- 已转换：raw 中逐来源总结压缩为来源页的来源索引；本页仅保留对执行工作流直接有用的结论。
- 未保留：stars 数、版本号等易过时数字；重复性宣传语；与命令级执行无直接关系的扩展阅读标题。

---

## 关联说明

- [[openspec]] — depends-on — 该工作流依赖 OpenSpec 提供规格、任务和归档机制。
- [[superpowers]] — depends-on — 该工作流依赖 Superpowers 约束 Cursor 代理的计划、TDD、调试和评审步骤。
- [[openspec]] — related-to — OpenSpec 是该组合中负责规格驱动开发的工具。
- [[superpowers]] — related-to — Superpowers 是该组合中负责行为纪律的工具集合。

---

## 来源

- [[sources/2026-06-02-openspec-superpower-cursor-research]] — 提供推荐工作流、适用场景、不适用场景和风险约束。
- [[sources/2026-06-02-openspec-superpowers-cursor-command-workflow-research]] — 提供安装、初始化、OpenSpec CLI、Cursor 斜杠命令、Superpowers 插件命令和组合执行顺序。
