---
title: "OpenSpec + Superpowers + Cursor 命令级实操调研"
source-type: article
generated: 2026-06-02
generated-by: wiki-research-skill
research-mode: command-level
---

# OpenSpec + Superpowers + Cursor 命令级实操调研

## 调研问题

具体如何实际使用 OpenSpec + Superpowers 结合 Cursor 开发？涉及哪些安装命令、OpenSpec 命令、Cursor 斜杠命令、验证命令和日常操作步骤？

## 核心结论

1. OpenSpec 在 Cursor 中主要提供“规格生命周期”层：初始化后会生成 `openspec/` 目录，并在 Cursor 下安装 `.cursor/skills/openspec-*/SKILL.md` 和 `.cursor/commands/opsx-*.md`，默认 core profile 包含 `propose`、`explore`、`apply`、`sync`、`archive` 五个工作流。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md] 可信度：高。
2. OpenSpec 的推荐 Cursor 工作流是 `propose -> apply -> sync/archive`，扩展工作流可启用 `new`、`continue`、`ff`、`verify`、`bulk-archive`、`onboard`；启用扩展命令需运行 `openspec config profile` 后再运行 `openspec update`。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md] 可信度：高。
3. OpenSpec CLI 的基础安装命令是 `npm install -g @fission-ai/openspec@latest`，项目初始化命令是 `openspec init`；在自动化或避免交互时可使用 `openspec init --tools claude,cursor` 或 `openspec init --tools cursor`。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/cli.md] 可信度：高。
4. Superpowers 在 Cursor 中的官方 README 安装方式是进入 Cursor Agent chat 后运行 `/add-plugin superpowers`，也可在插件市场搜索 `superpowers`；官方 Mintlify 安装页还记录了 `/plugin-add superpowers`、`/plugin-update superpowers` 和 `/plugin-remove superpowers`，说明 Cursor 插件命令语法可能存在版本差异。[来源: https://raw.githubusercontent.com/obra/superpowers/main/README.md；https://obra-superpowers.mintlify.app/installation/cursor] 可信度：中。
5. 两者组合时，OpenSpec 应作为“控制平面”：负责变更 ID、proposal、delta specs、tasks、archive；Superpowers 应作为“执行纪律”：负责 brainstorming、writing-plans、TDD、systematic-debugging、verification-before-completion、code review 等过程。[来源: https://raw.githubusercontent.com/Veath/openspec-spec-driven-superpowers/main/README.md；https://raw.githubusercontent.com/obra/superpowers/main/README.md] 可信度：中。
6. Cursor 本身适合执行代码编辑，但不提供完整规格生命周期、结构化 spec-to-task 追踪或强制规格一致性，因此多会话、多文件、团队或长期功能更需要 OpenSpec 这类外部规格层。[来源: https://www.augmentcode.com/guides/cursor-spec-driven-development] 可信度：中。

## 内容整理

### 1. 工具分工

OpenSpec 负责规格驱动开发的状态资产：`openspec/specs/` 存放当前系统行为的 source of truth，`openspec/changes/` 存放进行中的变更，`openspec/changes/archive/` 存放完成后的归档。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/getting-started.md]

OpenSpec 的每个 change 通常包含：

```text
openspec/changes/<change-id>/
├── proposal.md
├── design.md
├── tasks.md
└── specs/
    └── <capability>/spec.md
```

其中 `proposal.md` 说明 why/what/scope，`specs/` 写 `ADDED`、`MODIFIED`、`REMOVED` delta requirements，`design.md` 记录技术方案，`tasks.md` 记录可勾选实施清单。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/getting-started.md]

Superpowers 负责约束 Cursor 代理行为。官方 README 将基础流程描述为：brainstorming 先澄清设计，writing-plans 拆出足够小的实施计划，subagent-driven-development 或 executing-plans 执行，test-driven-development 强制 RED-GREEN-REFACTOR，requesting-code-review 做任务间审查，finishing-a-development-branch 做收尾验证和分支决策。[来源: https://raw.githubusercontent.com/obra/superpowers/main/README.md]

Cursor 是实际执行环境：通过 Agent chat 输入 OpenSpec slash commands 和普通提示词，让代理读规格、改代码、运行测试、做验证。但 Cursor Rules / Plan Mode 本身不等于完整 SDD 系统，因为它们缺少版本化规格生命周期、强制 phase gate 和 spec-to-code validation。[来源: https://www.augmentcode.com/guides/cursor-spec-driven-development]

### 2. 安装与初始化命令

#### OpenSpec 安装

```bash
npm install -g @fission-ai/openspec@latest
cd your-project
openspec init
```

上述命令来自 OpenSpec 社区指南和多源重复记录；OpenSpec CLI 文档确认 `openspec init` 会初始化项目并配置 AI tool integrations。[来源: https://recca0120.github.io/en/2026/03/08/openspec-sdd；https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/cli.md]

如果希望显式配置 Cursor，推荐使用：

```bash
openspec init --tools cursor
```

如果同一项目同时给 Claude Code 和 Cursor 使用：

```bash
openspec init --tools claude,cursor
```

OpenSpec CLI 文档确认 `--tools` 支持 `cursor`，并可传入逗号分隔工具列表。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/cli.md]

初始化后，Cursor 相关文件路径是：

```text
.cursor/skills/openspec-*/SKILL.md
.cursor/commands/opsx-*.md
```

该路径来自 OpenSpec supported tools 文档。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md]

#### OpenSpec 更新

升级 npm 包后更新项目内指令文件：

```bash
npm update @fission-ai/openspec
openspec update
```

CLI 文档将 `openspec update` 描述为重新生成 AI tool 配置文件，使用当前 profile、workflow selection 和 delivery mode。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/cli.md]

#### Superpowers 安装

Superpowers 官方 README 对 Cursor 的安装方式是：

```text
/add-plugin superpowers
```

操作位置是 Cursor Agent chat，不是普通终端。[来源: https://raw.githubusercontent.com/obra/superpowers/main/README.md]

Superpowers 官方 Mintlify 安装页记录的命令是：

```text
/plugin-add superpowers
```

验证方式：

```text
Do you have superpowers?
```

更新方式：

```text
/plugin-update superpowers
```

卸载方式：

```text
/plugin-remove superpowers
```

由于官方 README 与官方安装页对 Cursor 插件安装命令分别写作 `/add-plugin superpowers` 和 `/plugin-add superpowers`，实际使用时应优先尝试当前 Cursor 插件市场支持的语法；若失败，换另一种，并确认自己在 Cursor Agent chat 中。[来源: https://raw.githubusercontent.com/obra/superpowers/main/README.md；https://obra-superpowers.mintlify.app/installation/cursor]

### 3. OpenSpec 常用终端命令

#### 查看现有工作

```bash
openspec list
openspec list --specs
openspec spec list --long
```

`openspec list` 用于列出 active changes，`openspec list --specs` 或 `openspec spec list --long` 用于查看已有能力规格，适合创建新 change 前避免重复。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md；https://dev.to/webdeveloperhyper/how-to-make-ai-follow-your-instructions-more-for-free-openspec-2c85]

#### 查看详情

```bash
openspec show <change-id>
openspec show <spec-id> --type spec
openspec show <change-id> --json --deltas-only
```

`show` 支持查看 change 或 spec；`--json` 适合代理或脚本解析。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/cli.md；https://dev.to/webdeveloperhyper/how-to-make-ai-follow-your-instructions-more-for-free-openspec-2c85]

#### 验证规格

```bash
openspec validate <change-id> --strict
openspec validate --all
openspec validate --all --json
```

OpenSpec 文档多次强调 proposal 分享或实施前运行 strict validate；`--json` 可用于自动化或 CI。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md；https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/cli.md]

#### 归档

```bash
openspec archive <change-id> --yes
openspec archive <change-id> --skip-specs --yes
```

`archive` 用于完成变更后归档；`--skip-specs` 适用于 tooling-only changes，不更新能力规格；`--yes` 用于跳过确认。[来源: https://docs.runmaestro.ai/openspec-commands；https://dev.to/webdeveloperhyper/how-to-make-ai-follow-your-instructions-more-for-free-openspec-2c85]

#### 启用扩展工作流

```bash
openspec config profile
openspec update
```

OpenSpec 官方命令文档说明默认 profile 为 `core`，如需 `new`、`continue`、`ff`、`verify`、`bulk-archive`、`onboard` 等扩展命令，需要先运行 `openspec config profile` 选择 workflows，然后在项目中运行 `openspec update`。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]

### 4. Cursor 中的 OpenSpec 斜杠命令

OpenSpec 官方 commands 文档给出的默认命令面是 `/opsx:*`。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]

#### 默认 core profile

```text
/opsx:explore [topic]
/opsx:propose [change-name-or-description]
/opsx:apply [change-name]
/opsx:sync [change-name]
/opsx:archive [change-name]
```

用途：

- `/opsx:explore`：需求不清楚时先探索，不创建 artifacts。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]
- `/opsx:propose`：创建 change 并生成 proposal/specs/design/tasks 等规划资产。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]
- `/opsx:apply`：读取 `tasks.md`，逐项实现并勾选任务。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]
- `/opsx:sync`：将 delta specs 合并到主 `openspec/specs/`，但不归档。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]
- `/opsx:archive`：检查 artifact 和 task 状态，必要时同步 specs，然后移动 change 到 archive。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]

#### 扩展 workflow

```text
/opsx:new [change-name] [--schema <schema-name>]
/opsx:continue [change-name]
/opsx:ff [change-name]
/opsx:verify [change-name]
/opsx:bulk-archive [change-names...]
/opsx:onboard
```

用途：

- `/opsx:new`：只创建 change scaffold，适合复杂需求分阶段推进。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]
- `/opsx:continue`：按依赖顺序一次生成一个 artifact，适合每一步人工审查。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]
- `/opsx:ff`：一次性生成所有 planning artifacts，适合清晰的小中型功能。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]
- `/opsx:verify`：检查 completeness、correctness、coherence，报告 CRITICAL/WARNING/SUGGESTION。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]
- `/opsx:bulk-archive`：批量归档多个完成的 changes，并检查 specs 冲突。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]

#### Cursor 命令格式差异

OpenSpec supported tools 文档指出 Cursor 命令文件路径是 `.cursor/commands/opsx-<workflow>.md`。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md]

一些社区页面或 Cursor 论坛示例使用：

```text
/openspec-proposal Add user authentication with 2FA
/openspec-apply add-user-auth
/openspec-archive add-user-auth
```

另一些 OpenSpec 当前文档使用：

```text
/opsx:propose add-user-auth
/opsx:apply add-user-auth
/opsx:archive add-user-auth
```

这说明命令面可能随 OpenSpec 版本、profile、tool adapter 或社区文档版本变化。实际项目中应以 `openspec init` / `openspec update` 在 `.cursor/commands/` 生成的文件为准。[来源: https://forum.cursor.com/t/openspec-lightweight-portable-spec-driven-framework-for-ai-coding-assistants/134052；https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md；https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md]

### 5. 规格内容写法

OpenSpec delta spec 使用明确的操作头：

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

OpenSpec 文档要求每个 requirement 至少包含一个 scenario，便于后续验证与测试。[来源: https://docs.runmaestro.ai/openspec-commands；https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/getting-started.md]

常见创建 proposal 前检查：

```bash
openspec list
openspec list --specs
openspec show <spec-id> --type spec
rg -n "Requirement:|Scenario:" openspec/specs
```

这些检查用于避免重复创建能力、发现并行 change 冲突、定位已有 requirement。[来源: https://dev.to/webdeveloperhyper/how-to-make-ai-follow-your-instructions-more-for-free-openspec-2c85]

### 6. Superpowers 在组合工作流中的实际用法

Superpowers 官方 README 强调技能会自动触发，用户“不需要做特殊事情”，但在 Cursor 中如果技能没有自动触发，可以显式要求，例如：

```text
use the brainstorming skill
use the writing-plans skill
use the test-driven-development skill
use the systematic-debugging skill
use the verification-before-completion skill
```

官方安装页也建议用具体任务测试自动触发：

```text
Let's design a new feature for user profiles
I need to implement authentication middleware
This API endpoint returns 500 errors randomly
```

代理应自动调用 brainstorming、writing-plans 或 systematic-debugging 等对应技能。[来源: https://obra-superpowers.mintlify.app/installation/cursor]

组合 OpenSpec 时，建议映射如下：

| OpenSpec 阶段 | Superpowers 技能 | 目的 |
| --- | --- | --- |
| `/opsx:explore` | brainstorming | 收敛需求、比较方案、避免过早写 proposal |
| `/opsx:propose` 或 `/opsx:new` + `/opsx:continue` | brainstorming / writing-plans | 形成可审查 proposal、design、tasks |
| 人工审查 artifacts | requesting-code-review | 审查规格是否过度、漏测或冲突 |
| `/opsx:apply` | test-driven-development / executing-plans | 按任务和测试驱动实现 |
| bug 阶段 | systematic-debugging | 先定位根因再修复 |
| `/opsx:verify` 或人工验收 | verification-before-completion / requesting-code-review | 对照规格、测试、实现检查一致性 |
| `/opsx:archive` | finishing-a-development-branch | 验证完成、分支/PR/归档收尾 |

该映射部分来自 Veath 的 `openspec-spec-driven-superpowers` README：其明确将 OpenSpec 定位为 control plane，将 superpowers 定位为 working discipline，并将 `review.md`、`plan.md`、`verification.md` 等作为加强工件。[来源: https://raw.githubusercontent.com/Veath/openspec-spec-driven-superpowers/main/README.md]

## 推荐工作流

### A. 一次性项目初始化

1. 确保 Node.js 满足 OpenSpec 要求。一个 OpenSpec 指南写明需要 Node.js 20.19.0+，但该版本要求需以当前 npm 包为准验证。[来源: https://recca0120.github.io/en/2026/03/08/openspec-sdd] 可信度：中。

2. 安装 OpenSpec：

```bash
npm install -g @fission-ai/openspec@latest
```

3. 进入项目：

```bash
cd your-project
```

4. 初始化并选择 Cursor，或非交互初始化：

```bash
openspec init
```

或：

```bash
openspec init --tools cursor
```

5. 安装 Superpowers。打开 Cursor Agent chat，尝试：

```text
/add-plugin superpowers
```

若该命令不可用，按官方安装页尝试：

```text
/plugin-add superpowers
```

6. 新开 Cursor Agent 会话，验证：

```text
Do you have superpowers?
```

7. 查看 OpenSpec 命令是否生成：

```bash
openspec list
openspec list --specs
```

并在项目中确认 `.cursor/commands/opsx-*.md` 与 `.cursor/skills/openspec-*/SKILL.md` 是否存在。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md]

### B. 新功能开发：推荐命令序列

#### 1. 探索需求

在 Cursor Agent chat：

```text
/opsx:explore How should we add two-factor authentication for admin users?
```

或直接显式触发 Superpowers：

```text
use the brainstorming skill. Help me explore how to add two-factor authentication for admin users. Do not write code yet.
```

此阶段不应改代码，目标是梳理现有认证结构、选项、风险和 open questions。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md；https://raw.githubusercontent.com/obra/superpowers/main/README.md]

#### 2. 创建 OpenSpec change

在 Cursor Agent chat：

```text
/opsx:propose add-admin-two-factor-auth
```

如果 Cursor 当前生成的是短横线命令，可尝试项目实际存在的命令，例如：

```text
/opsx-propose add-admin-two-factor-auth
```

或旧文档示例：

```text
/openspec-proposal Add admin two-factor authentication
```

实际以 `.cursor/commands/` 生成文件为准。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md；https://forum.cursor.com/t/openspec-lightweight-portable-spec-driven-framework-for-ai-coding-assistants/134052]

#### 3. 人工审查 artifacts

检查这些文件：

```text
openspec/changes/add-admin-two-factor-auth/proposal.md
openspec/changes/add-admin-two-factor-auth/design.md
openspec/changes/add-admin-two-factor-auth/tasks.md
openspec/changes/add-admin-two-factor-auth/specs/<capability>/spec.md
```

终端验证：

```bash
openspec validate add-admin-two-factor-auth --strict
openspec show add-admin-two-factor-auth
```

审查重点：

- `proposal.md` 是否写清 why、scope、out of scope。
- delta spec 是否用 `ADDED/MODIFIED/REMOVED Requirements`。
- 每个 requirement 是否至少有一个 scenario。
- `tasks.md` 是否绑定测试或验证方式。
- 是否与现有 active changes 冲突，可用 `openspec list` 检查。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md；https://dev.to/webdeveloperhyper/how-to-make-ai-follow-your-instructions-more-for-free-openspec-2c85]

#### 4. 执行实现

在 Cursor Agent chat：

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

该做法把 OpenSpec 的 task checklist 与 Superpowers 的 TDD/verification-before-completion 结合。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md；https://raw.githubusercontent.com/obra/superpowers/main/README.md]

#### 5. 验证

终端验证 OpenSpec 结构：

```bash
openspec validate add-admin-two-factor-auth --strict
```

如果启用扩展工作流，在 Cursor Agent chat：

```text
/opsx:verify add-admin-two-factor-auth
```

同时要求 Superpowers 验证：

```text
use the verification-before-completion skill.
Verify the implementation against openspec/changes/add-admin-two-factor-auth:
- all tasks complete
- all requirements implemented
- all scenarios covered by tests or explicit manual verification
- no out-of-scope behavior added
```

`/opsx:verify` 官方说明会检查 completeness、correctness、coherence，并以 CRITICAL、WARNING、SUGGESTION 分类报告。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]

#### 6. 归档

确认测试和 review 后，在 Cursor Agent chat：

```text
/opsx:archive add-admin-two-factor-auth
```

或终端：

```bash
openspec archive add-admin-two-factor-auth --yes
openspec validate --all
```

归档会把 delta specs 合并进主 `openspec/specs/`，并移动 change 到 `openspec/changes/archive/YYYY-MM-DD-<change-id>/`。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/getting-started.md；https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]

### C. 复杂需求：更稳的扩展流程

先启用扩展工作流：

```bash
openspec config profile
openspec update
```

然后在 Cursor Agent chat：

```text
/opsx:new add-admin-two-factor-auth
/opsx:continue add-admin-two-factor-auth
```

每次 `/opsx:continue` 只生成下一个 artifact，人工审查后再继续。也可以在需求清楚时：

```text
/opsx:ff add-admin-two-factor-auth
```

实现前：

```bash
openspec validate add-admin-two-factor-auth --strict
```

实现后：

```text
/opsx:verify add-admin-two-factor-auth
/opsx:archive add-admin-two-factor-auth
```

该方式适合跨模块、权限、安全、数据库迁移等高风险变更。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]

### D. Bug 修复：不要机械使用完整 proposal

OpenSpec 衍生资料指出，恢复既有预期行为的 bug fix、typo、格式、注释、非破坏性依赖更新、既有行为测试可跳过 proposal。[来源: https://dev.to/webdeveloperhyper/how-to-make-ai-follow-your-instructions-more-for-free-openspec-2c85]

对 bug 更适合：

```text
use the systematic-debugging skill.
Investigate this bug. Do not write a fix until you identify the root cause and reproduce it.
```

如果排查后发现需要改变现有行为、API、schema、安全策略或架构，再创建 OpenSpec change。

## 适用场景

- 多文件、多会话功能：Cursor 单独使用时容易丢失规格上下文，OpenSpec 可提供版本化规格资产。[来源: https://www.augmentcode.com/guides/cursor-spec-driven-development]
- 老项目渐进改造：OpenSpec 的 changes/delta specs 更适合 brownfield iterative changes。[来源: https://docs.runmaestro.ai/openspec-commands]
- 高风险变更：认证、权限、支付、数据迁移、安全策略、API breaking change、架构调整，需要 proposal、scenario、validation 和 archive。[来源: https://dev.to/webdeveloperhyper/how-to-make-ai-follow-your-instructions-more-for-free-openspec-2c85]
- 需要审计和长期维护的项目：OpenSpec archive 保留 why/what/how/tasks，便于后续追溯。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/getting-started.md]
- 希望约束 AI 不跳过测试的团队：Superpowers 官方 README 明确强调 TDD、systematic over ad-hoc、evidence over claims。[来源: https://raw.githubusercontent.com/obra/superpowers/main/README.md]

## 不适用场景

- 单行 CSS、typo、注释、低风险配置修改：OpenSpec proposal 成本高于收益。[来源: https://recca0120.github.io/en/2026/03/08/openspec-sdd]
- 单会话、单文件、强人工实时控制的任务：Cursor alone 足够，规格层可能拖慢速度。[来源: https://www.augmentcode.com/guides/cursor-spec-driven-development]
- 纯 bug fix 且只是恢复已有 spec 行为：可以直接用 systematic-debugging 和测试修复，除非修复改变了行为契约。[来源: https://dev.to/webdeveloperhyper/how-to-make-ai-follow-your-instructions-more-for-free-openspec-2c85]
- 团队不愿维护 archive 和 specs：如果实现后不 sync/archive，OpenSpec 的 source of truth 会漂移。

## 风险与约束

- 命令语法存在版本差异：OpenSpec 当前官方命令参考使用 `/opsx:*`，Cursor 论坛和部分社区资料使用 `/openspec-*`，Superpowers Cursor 安装命令也存在 `/add-plugin` 与 `/plugin-add` 两种写法；应以本地生成文件和当前 Cursor 插件命令为准。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md；https://forum.cursor.com/t/openspec-lightweight-portable-spec-driven-framework-for-ai-coding-assistants/134052；https://raw.githubusercontent.com/obra/superpowers/main/README.md；https://obra-superpowers.mintlify.app/installation/cursor]
- Cursor 不强制 phase gate：即使有 OpenSpec，用户仍需约束代理“未审批 proposal 不准实现”。Cursor 本身不会天然阻止代理越界。[来源: https://www.augmentcode.com/guides/cursor-spec-driven-development]
- Superpowers 与 OpenSpec 不是一个官方一体化产品：Veath 的集成仓库提供 schema 思路，但 star 少、属于社区项目，应作为参考而非标准。[来源: https://raw.githubusercontent.com/Veath/openspec-spec-driven-superpowers/main/README.md]
- 自动验证不等于业务正确：`/opsx:verify` 报告 completeness/correctness/coherence，但不会替代真实测试、代码审查、安全审查和人工产品验收。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]
- 文档和工具变化很快：OpenSpec stars、Superpowers stars、版本号等数字随时间变化，不应作为稳定知识写入；本报告只保留命令和流程层面的可操作事实。

## 来源与可信度

- https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md  
  类型：OpenSpec 官方仓库命令参考。可信度：高。支撑内容：`/opsx:*` 命令、core/expanded profiles、apply/verify/archive 行为。
- https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/cli.md  
  类型：OpenSpec 官方 CLI 参考。可信度：高。支撑内容：`openspec init`、`openspec update`、`--tools cursor`、`validate --json` 等命令。
- https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md  
  类型：OpenSpec 官方支持工具文档。可信度：高。支撑内容：Cursor skills/commands 生成路径、默认 profile、workflow-dependent installation。
- https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/getting-started.md  
  类型：OpenSpec 官方入门文档。可信度：高。支撑内容：目录结构、artifacts、delta specs、archive 行为。
- https://raw.githubusercontent.com/obra/superpowers/main/README.md  
  类型：Superpowers 官方 README。可信度：高。支撑内容：Superpowers 定义、Cursor 安装、基础技能流程、技能列表。
- https://obra-superpowers.mintlify.app/installation/cursor  
  类型：Superpowers 官方风格安装文档。可信度：中。支撑内容：Cursor Agent 安装、验证、更新、卸载、故障排查；与 README 的安装命令有差异。
- https://docs.runmaestro.ai/openspec-commands  
  类型：Maestro 文档，封装 OpenSpec 命令。可信度：中。支撑内容：OpenSpec vs Spec-Kit、proposal/apply/archive、CLI 命令速查。
- https://forum.cursor.com/t/openspec-lightweight-portable-spec-driven-framework-for-ai-coding-assistants/134052  
  类型：Cursor 论坛 OpenSpec 发布帖。可信度：中。支撑内容：Cursor 集成示例、`/openspec-proposal`、`/openspec-apply`、`/openspec-archive` 旧/社区命令面。
- https://recca0120.github.io/en/2026/03/08/openspec-sdd  
  类型：社区技术博客。可信度：中。支撑内容：安装命令、`/opsx:*` 示例、delta spec 说明、扩展命令说明。
- https://www.augmentcode.com/guides/cursor-spec-driven-development  
  类型：厂商技术分析文章。可信度：中。支撑内容：Cursor 在 SDD 中的能力边界和缺口。
- https://raw.githubusercontent.com/Veath/openspec-spec-driven-superpowers/main/README.md  
  类型：社区集成仓库 README。可信度：中偏低。支撑内容：OpenSpec control plane + Superpowers working discipline 的组合模型。
- https://dev.to/webdeveloperhyper/how-to-make-ai-follow-your-instructions-more-for-free-openspec-2c85  
  类型：个人实践文章。可信度：中。支撑内容：OpenSpec 初始化后 AGENTS 指令内容、proposal/implementation/archive 检查清单、命令速查。

## 对于可信度较高的来源逐来源总结

### OpenSpec 官方 commands.md

该来源是 OpenSpec slash commands 的直接参考。它明确默认 core profile 包含 `/opsx:propose`、`/opsx:explore`、`/opsx:apply`、`/opsx:sync`、`/opsx:archive`；扩展 workflow 包含 `/opsx:new`、`/opsx:continue`、`/opsx:ff`、`/opsx:verify`、`/opsx:bulk-archive`、`/opsx:onboard`。它还说明默认 global profile 是 `core`，启用扩展命令需要运行 `openspec config profile` 并在项目中运行 `openspec update`。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]

可入库知识点：OpenSpec slash command reference、OpenSpec expanded workflow、OpenSpec verify workflow。

局限：该文档定义的是 OpenSpec 当前命令参考，但 Cursor 内实际命令显示可能受工具 adapter 和生成文件影响。

### OpenSpec 官方 CLI 文档

该来源定义 `openspec init`、`openspec update`、`openspec list`、`openspec show`、`openspec validate`、`openspec archive` 等终端命令。它明确 `openspec init --tools cursor` 或 `--tools claude,cursor` 可非交互配置工具，并说明初始化后会生成 `openspec/`、`.cursor/skills/`、`.cursor/commands/` 等文件。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/cli.md]

可入库知识点：OpenSpec CLI、OpenSpec Cursor initialization、OpenSpec validation commands。

局限：CLI 文档非常长，本报告只提取与 Cursor + Superpowers 组合相关的命令。

### OpenSpec supported-tools.md

该来源提供 OpenSpec 对 Cursor 的最关键事实：Cursor skills path 是 `.cursor/skills/openspec-*/SKILL.md`，command path 是 `.cursor/commands/opsx-*.md`。它还说明 core profile 默认包括 `propose`、`explore`、`apply`、`sync`、`archive`，扩展 workflow 可通过配置启用。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md]

可入库知识点：OpenSpec supported tools、Cursor OpenSpec command installation paths。

局限：该文档说明文件路径和 profile，不详细说明如何与 Superpowers 协同。

### Superpowers 官方 README

该来源定义 Superpowers 是面向 coding agents 的完整软件开发方法论，基于 composable skills 和初始指令。Cursor 安装方式为在 Cursor Agent chat 运行 `/add-plugin superpowers` 或在插件市场搜索。它列出基本 workflow：brainstorming、using-git-worktrees、writing-plans、subagent-driven-development/executing-plans、test-driven-development、requesting-code-review、finishing-a-development-branch。[来源: https://raw.githubusercontent.com/obra/superpowers/main/README.md]

可入库知识点：Superpowers Cursor installation、Superpowers skills workflow、Superpowers TDD discipline。

局限：README 没有专门说明 OpenSpec 集成方式。

### Superpowers Cursor 安装页

该来源专门说明 Cursor 安装：打开 Agent chat，运行 `/plugin-add superpowers`，用 `Do you have superpowers?` 验证，用 `/plugin-update superpowers` 更新，用 `/plugin-remove superpowers` 卸载。它还提醒 Cursor Agent 和 Cursor Composer 不同，Superpowers 更适合 Agent chat。[来源: https://obra-superpowers.mintlify.app/installation/cursor]

可入库知识点：Superpowers Cursor plugin lifecycle。

局限：与官方 README 中 `/add-plugin superpowers` 命令不一致，因此命令名需标注版本/语法差异。

### OpenSpec getting-started.md

该来源解释 OpenSpec 初始化后的结构、proposal/specs/design/tasks 四类 artifact、delta spec 的 ADDED/MODIFIED/REMOVED 格式，以及 archive 如何把 delta 合并到主 specs 并移动到 archive。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/getting-started.md]

可入库知识点：OpenSpec artifacts、OpenSpec delta specs、OpenSpec archive semantics。

局限：主要是 OpenSpec 内部流程，不覆盖 Superpowers。

### Cursor SDD 分析文章

该来源认为 Cursor 是强执行环境但不是完整 SDD 系统，缺少原生 spec lifecycle management、structured spec-to-task traceability 和 enforcement。它建议单会话任务用 Cursor 即可，多会话功能可叠加 OpenSpec。[来源: https://www.augmentcode.com/guides/cursor-spec-driven-development]

可入库知识点：Cursor 与 SDD 的边界、Cursor + OpenSpec 的适用场景。

局限：该文章来自厂商，有推广自身产品的倾向，需作为分析观点而非中立标准。

### Veath openspec-spec-driven-superpowers README

该来源直接讨论 OpenSpec + superpowers 的组合方式，主张 OpenSpec 是 control plane，superpowers 升级 working discipline，并保留 `/opsx:*` 命令面。它提出 `review.md` 作为 readiness gate、`plan.md` 作为 apply-time execution driver、`verification.md` 作为可选证据。[来源: https://raw.githubusercontent.com/Veath/openspec-spec-driven-superpowers/main/README.md]

可入库知识点：OpenSpec + Superpowers 组合模式、spec-driven-superpowers schema。

局限：这是社区仓库，star 少，不能当作 OpenSpec 或 Superpowers 官方集成标准。

## 矛盾与待验证问题

- Superpowers Cursor 安装命令存在差异：官方 README 写 `/add-plugin superpowers`，官方安装页写 `/plugin-add superpowers`；实际应以当前 Cursor Agent chat 支持的插件命令为准。[来源: https://raw.githubusercontent.com/obra/superpowers/main/README.md；https://obra-superpowers.mintlify.app/installation/cursor]
- OpenSpec Cursor slash command 存在差异：官方 OpenSpec commands 文档写 `/opsx:propose`，Cursor 论坛早期发布帖写 `/openspec-proposal`，supported-tools 文档又显示 Cursor command 文件为 `.cursor/commands/opsx-*.md`；实际应查看本项目生成的 `.cursor/commands/` 文件。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md；https://forum.cursor.com/t/openspec-lightweight-portable-spec-driven-framework-for-ai-coding-assistants/134052；https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md]
- Node.js 20.19.0+ 要求来自社区指南，本报告未从 OpenSpec 官方 README 精读确认，因此标注为中可信度。[来源: https://recca0120.github.io/en/2026/03/08/openspec-sdd]
- OpenSpec、Superpowers 的 stars、版本号、增长速度在不同来源差异大且随时间变化，本报告不将其作为稳定事实。
- Veath 的 `openspec-spec-driven-superpowers` 是很贴近本问题的资料，但属于社区集成方案，不代表官方推荐默认做法。

## 原始证据摘录

> For each selected tool, OpenSpec can install: Skills ... Commands ... Cursor (`cursor`) | `.cursor/skills/openspec-*/SKILL.md` | `.cursor/commands/opsx-.md`。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md]

> The default global profile is `core`. To enable expanded workflow commands, run `openspec config profile`, select workflows, then run `openspec update` in your project。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md]

> Initialize OpenSpec in your project. Creates the folder structure and configures AI tool integrations ... `openspec init --tools claude,cursor`。[来源: https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/cli.md]

> In Cursor Agent chat, install from marketplace: `/add-plugin superpowers`。[来源: https://raw.githubusercontent.com/obra/superpowers/main/README.md]

> In the Agent chat, run the plugin installation command: `/plugin-add superpowers` ... Update to the latest version: `/plugin-update superpowers`。[来源: https://obra-superpowers.mintlify.app/installation/cursor]

> OpenSpec owns the control plane; superpowers upgrades the working discipline。[来源: https://raw.githubusercontent.com/Veath/openspec-spec-driven-superpowers/main/README.md]

> Cursor is a strong execution environment for spec-driven development but a poor SDD system. It can consume specs and generate code from them, but it provides no native spec lifecycle management, no structured spec-to-task traceability, and no enforcement that agents stay aligned to a specification as the codebase evolves。[来源: https://www.augmentcode.com/guides/cursor-spec-driven-development]
