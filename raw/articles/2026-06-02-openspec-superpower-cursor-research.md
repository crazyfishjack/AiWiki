---
title: "OpenSpec + Superpowers 结合 Cursor 开发的方式"
source-type: article
generated: 2026-06-02
generated-by: wiki-research-skill
research-mode: standard
---

# OpenSpec + Superpowers 结合 Cursor 开发的方式

## 调研问题

如何把 OpenSpec、Superpowers 与 Cursor 组合成一套可执行、可审计、不过度工程的 AI 辅助开发工作流？

## 核心结论

1. OpenSpec 更适合承担“规格与变更管理”角色：它把模糊需求转成 proposal、tasks、spec delta、archive 等结构化资产，用于降低 AI 编码中的需求偏移和历史决策丢失风险。[来源: https://www.cnblogs.com/goloving/p/19671659] 可信度：中。
2. Superpowers 更适合承担“开发行为纪律”角色：它通过可组合 skills 引导 Cursor 代理执行头脑风暴、规划、TDD、系统化调试、子代理并行、代码审查等流程。[来源: https://www.michaelapp.com/posts/2026/2026-03-01-cursor-%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8superpowers] 可信度：中。
3. 二者不是二选一：OpenSpec 约束“做什么、为什么、变更如何归档”，Superpowers 约束“怎么做、按什么工程步骤做”，Cursor 则作为实际执行和代码编辑环境。[来源: https://cloud.tencent.com/developer/article/2649111] 可信度：中。
4. 组合使用的关键价值在复杂或长期项目中更明显，尤其是老项目改造、多人协作、涉及接口/数据库/权限等跨模块变更、需要保留设计决策的项目。[来源: https://cloud.tencent.com/developer/article/2659798] 可信度：中。
5. 这套组合不是“无缝自动串联”的银弹：实战文章明确提到 OpenSpec + Superpowers 的衔接点可能断裂，尤其在规格交接、任务拆分和测试闭环上需要人工复核。[来源: https://cloud.tencent.com/developer/article/2664183] 可信度：中。
6. 对小型一次性脚本、低风险改动或快速原型，OpenSpec + Superpowers + Cursor 三件套可能带来额外文档和流程成本，裸用 Cursor 或只启用少量技能更合适。[来源: https://www.heyuan110.com/zh/posts/ai/2026-04-09-claude-code-openspec-superpowers] 可信度：中。

## 推荐工作流

### 1. 项目初始化：让 Cursor 读懂边界

1. 在 Cursor 中先让代理扫描项目结构、测试命令、代码规范和关键模块，输出简短项目上下文。
2. 安装或启用 Superpowers，使 Cursor 能在合适任务中调用 brainstorming、planning、TDD、debugging、review 等技能。[来源: https://www.michaelapp.com/posts/2026/2026-03-01-cursor-%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8superpowers]
3. 在项目中初始化 OpenSpec，并把规格目录视为后续需求变更的单一真相来源；OpenSpec 的目标是把“凭感觉聊天”转向“基于规范开发”。[来源: https://www.cnblogs.com/goloving/p/19671659]

### 2. 需求阶段：OpenSpec 先锁定“做什么”

1. 对非平凡需求，先让 Cursor 使用 OpenSpec 产出变更提案，说明为什么要改、改什么、不改什么。[来源: https://www.cnblogs.com/goloving/p/19671659]
2. 把验收标准写成可检查条目，尤其是接口契约、数据模型、权限边界、失败场景和兼容性要求。[来源: https://lzw.me/a/ai-coding-sdd-speckit-openspec-cursor.html]
3. 让 Cursor 审查 OpenSpec 提案是否过度实现、是否遗漏测试、是否影响现有规格。[来源: https://cloud.tencent.com/developer/article/2664183]

### 3. 计划阶段：Superpowers 把规格转成执行计划

1. 让 Cursor 基于 OpenSpec 的 proposal、tasks 和 spec delta 生成实施计划。
2. 对大任务使用 Superpowers 的 planning / execution 类技能，将任务拆成小步，并要求每步绑定测试或验证方式。[来源: https://www.michaelapp.com/posts/2026/2026-03-01-cursor-%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8superpowers]
3. 人工确认计划后再允许 Cursor 修改代码；OpenSpec 负责防止目标漂移，Superpowers 负责防止代理跳过工程步骤。[来源: https://www.heyuan110.com/zh/posts/ai/2026-04-09-claude-code-openspec-superpowers]

### 4. 实现阶段：Cursor 执行，Superpowers 约束节奏

1. 在 Cursor Agent 中按计划逐步实现，不要一次性让代理完成整个复杂需求。
2. 对核心逻辑使用 TDD：先让 Cursor 写失败测试，再实现最小代码，再重构。[来源: https://www.michaelapp.com/posts/2026/2026-03-01-cursor-%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8superpowers]
3. 每完成一个任务，要求 Cursor 对照 OpenSpec 的 tasks 和验收标准检查是否满足，不满足时先更新实现或测试，不直接勾选完成。[来源: https://www.cnblogs.com/goloving/p/19671659]

### 5. 验证阶段：把“完成”定义为规格、测试、代码一致

1. 运行项目测试、类型检查、lint 或关键手动验证。
2. 让 Cursor 做一次代码审查，重点检查：是否偏离 OpenSpec、是否跳过测试、是否破坏既有行为、是否引入未声明功能。[来源: https://www.michaelapp.com/posts/2026/2026-03-01-cursor-%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8superpowers]
3. 若实现与规格不一致，优先判断是代码错误还是规格需要调整；规格调整必须回到 OpenSpec 变更流程，而不是只改代码。[来源: https://www.cnblogs.com/goloving/p/19671659]

### 6. 收尾阶段：OpenSpec 归档，保留决策历史

1. 需求完成后，把 OpenSpec 变更归档，保留 proposal、任务、规格增量和设计理由。
2. 对未来维护者重要的决策，要求 Cursor 从 OpenSpec 归档中生成简短开发备注或 ADR。
3. 不建议让 Superpowers 的单次设计文档替代 OpenSpec 归档，因为有资料指出单纯设计文档可能在后续 brainstorming 中被覆盖，而 OpenSpec 的 Delta / Archive 机制更适合保留历史决策。[来源: https://www.heyuan110.com/zh/posts/ai/2026-04-09-claude-code-openspec-superpowers]

## 适用场景

- 中大型功能开发：例如认证、支付、权限、工作流、数据迁移、接口重构等，适合先用 OpenSpec 明确边界，再用 Superpowers 驱动 Cursor 分步实现。[来源: https://cloud.tencent.com/developer/article/2659798]
- 老项目增量改造：老项目常见缺测试、耦合高、注释少的问题，资料建议用 OpenSpec 锁定设计意图，用 Superpowers 约束测试和实现流程。[来源: https://cloud.tencent.com/developer/article/2659798]
- 需要审计的变更：OpenSpec 的提案、任务和归档结构适合保留“为什么这么改”的上下文。[来源: https://www.cnblogs.com/goloving/p/19671659]
- 多轮迭代项目：当早期决策容易被新对话覆盖时，OpenSpec archive 能保留历史变更，Superpowers 则帮助每轮迭代维持执行纪律。[来源: https://www.heyuan110.com/zh/posts/ai/2026-04-09-claude-code-openspec-superpowers]
- 一人团队或小团队高强度交付：资料将 OpenSpec + Superpowers 描述为可帮助架构师或个人开发者从设计到实现闭环的流程组合，但其中“30 分钟搭建完整系统”等效率声明仅来自单篇实践文章，需按项目验证。[来源: https://cloud.tencent.com/developer/article/2660449] 可信度：低。

## 不适用场景

- 一次性脚本、临时数据处理、低风险 UI 文案修改：完整 OpenSpec 流程可能比直接让 Cursor 修改并验证更慢。[来源: https://www.heyuan110.com/zh/posts/ai/2026-04-09-claude-code-openspec-superpowers]
- 需求仍在探索、还没有稳定目标的阶段：过早写完整规格可能导致文档频繁返工；更适合先用 Cursor + Superpowers brainstorming 收敛方向，再进入 OpenSpec。[来源: https://www.michaelapp.com/posts/2026/2026-03-01-cursor-%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8superpowers]
- 没有测试体系的纯实验项目：Superpowers 的 TDD 和 review 流程价值会下降，但也可作为补测试的起点。[来源: https://www.michaelapp.com/posts/2026/2026-03-01-cursor-%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8superpowers]
- 团队不愿维护规格或归档：OpenSpec 的价值依赖规格持续更新，如果实现后不归档、不校验，规格会与代码漂移。[来源: https://www.cnblogs.com/goloving/p/19671659]

## 风险与约束

- 衔接点断裂：OpenSpec 输出的 proposal / tasks 未必能被 Superpowers 自动理解成完整执行计划，实战资料明确指出三处衔接点中有多处可能失败，需要人工复核交接。[来源: https://cloud.tencent.com/developer/article/2664183]
- 规格与代码漂移：如果 Cursor 修改代码后没有回查 OpenSpec，规格会失去单一真相来源的价值。[来源: https://www.cnblogs.com/goloving/p/19671659]
- 流程过重：三件套同时使用会增加前期文档、评审和归档成本，对小改动可能不划算。[来源: https://www.heyuan110.com/zh/posts/ai/2026-04-09-claude-code-openspec-superpowers]
- 测试被形式化满足：Cursor 可能生成看似通过但没有覆盖真实业务风险的测试，因此测试用例需要人工审查验收标准是否覆盖关键路径。[来源: https://cloud.tencent.com/developer/article/2664183]
- 来源质量约束：本次调研主要来源是中文技术博客和社区实践文章，缺少 OpenSpec、Superpowers、Cursor 官方文档的直接精读支撑；因此多数结论应按中等可信度使用。[来源: https://cloud.tencent.com/developer/article/2649111]
- 安装细节不完整：一个 Cursor 安装 Superpowers 的页面在抓取结果中存在命令代码块为空的情况，不能把其中安装命令作为事实引用。[来源: https://www.michaelapp.com/posts/2026/2026-03-01-cursor-%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8superpowers]

## 来源与可信度

- https://www.cnblogs.com/goloving/p/19671659  
  类型：中文技术博客。可信度：中。支撑内容：OpenSpec 的定位、提案-审查-实施-归档流程、需求偏移和审计问题。
- https://lzw.me/a/ai-coding-sdd-speckit-openspec-cursor.html  
  类型：中文技术博客。可信度：中。支撑内容：SDD、Spec-Kit、OpenSpec 在 Cursor 中的应用实践和目录结构概念。
- https://www.michaelapp.com/posts/2026/2026-03-01-cursor-%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8superpowers  
  类型：中文个人博客。可信度：中偏低。支撑内容：Superpowers 在 Cursor 中的定位、技能类别、TDD / debug / review 等流程；安装命令部分抓取不完整，不能引用为空代码块。
- https://cloud.tencent.com/developer/article/2649111  
  类型：腾讯云开发者社区实践文章。可信度：中。支撑内容：OpenSpec 管规格管理，Superpowers 管行为纪律，两者解决不同层面的问题。
- https://cloud.tencent.com/developer/article/2659798  
  类型：腾讯云开发者社区实践文章。可信度：中。支撑内容：老项目、缺测试、前后端耦合等场景下组合使用的价值。
- https://cloud.tencent.com/developer/article/2660449  
  类型：腾讯云开发者社区实践文章。可信度：低到中。支撑内容：一人极简工作流案例；效率数据和“30 分钟”类表述需复测。
- https://cloud.tencent.com/developer/article/2664183  
  类型：腾讯云开发者社区实战复盘。可信度：中。支撑内容：OpenSpec + Superpowers 串联存在衔接点失败，不能假设自动无缝。
- https://www.heyuan110.com/zh/posts/ai/2026-04-09-claude-code-openspec-superpowers  
  类型：中文个人实测文章。可信度：中。支撑内容：三件套的 trade-off、OpenSpec archive 相对普通设计文档的价值、小任务中过度工程风险。

## 矛盾与待验证问题

- “Superpowers GitHub Star 125K”只在腾讯云社区文章中出现，未由本次精读的官方仓库页面验证；该数字标注为未验证，不应作为稳定事实写入 Wiki。[来源: https://cloud.tencent.com/developer/article/2649111]
- “OpenSpec npm 包 @fission-ai/openspec v1.2.0”只在腾讯云社区文章中出现，未由 npm 或官方仓库验证；该版本号标注为未验证。[来源: https://cloud.tencent.com/developer/article/2649111]
- “30 分钟从零搭出带 CRUD、数据库、单元测试的可用系统”来自单篇实践文章，可能受项目规模、模板、模型能力和作者环境影响，不能泛化为通用能力。[来源: https://cloud.tencent.com/developer/article/2660449]
- Superpowers 在 Cursor 中的推荐安装路径需要进一步用官方仓库或 Cursor 扩展市场验证；本次抓取的安装文章存在空代码块，不能确认完整命令。[来源: https://www.michaelapp.com/posts/2026/2026-03-01-cursor-%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8superpowers]
- OpenSpec 与 Superpowers 的名称在社区文章中有时与 Claude Code、Spec-Kit、Cursor 混合讨论，具体命令、目录和插件能力可能随版本变化，需要以当前项目实际安装版本复核。[来源: https://lzw.me/a/ai-coding-sdd-speckit-openspec-cursor.html]

## 原始证据摘录

> OpenSpec 是面向 AI 智能体的轻量级规范驱动开发框架，通过“提案-审查-实施-归档”工作流，解决 AI 编程中的需求偏移与不可预测性问题。[来源: https://www.cnblogs.com/goloving/p/19671659]

> OpenSpec 的表格化说明中将“需求不明确”对应到 proposal.md，将“AI 过度实现”对应到 tasks.md，将“规范缺失”对应到 specs/，将“变更难追溯”对应到 changes/archive/。[来源: https://www.cnblogs.com/goloving/p/19671659]

> Superpowers 是一个为 Cursor 设计的软件开发工作流系统，提供头脑风暴、测试驱动开发、系统化调试、编写和执行计划、子代理驱动开发、Git Worktrees、代码审查工作流、自定义技能创建等能力。[来源: https://www.michaelapp.com/posts/2026/2026-03-01-cursor-%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8superpowers]

> 社区对 OpenSpec 与 Superpowers 的分工概括为：一个管行为纪律，一个管规格管理；它们解决的是不同层面的问题。[来源: https://cloud.tencent.com/developer/article/2649111]

> 实战复盘文章声明其内容基于 OpenSpec 和 Superpowers 的源码分析及实际操作验证，并提示配置模板和参数建议需以业务数据和环境测试为准。[来源: https://cloud.tencent.com/developer/article/2664183]

> 三件套取舍文章把常见问题拆为“AI 做的不是你想要的”“AI 跳过测试直接写代码”“多次迭代后早期决策被盖掉”，并认为这些需要不同层面的工具分别处理。[来源: https://www.heyuan110.com/zh/posts/ai/2026-04-09-claude-code-openspec-superpowers]
