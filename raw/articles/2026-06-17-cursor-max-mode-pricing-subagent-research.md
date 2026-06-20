---
title: "Cursor Max 模式、Token 定价与 Subagent 行为调研"
source-type: article
generated: 2026-06-17
generated-by: wiki-research-skill
research-mode: standard
---

# Cursor Max 模式、Token 定价与 Subagent 行为调研

## 核心结论

1. Cursor Max Mode 的核心作用是把上下文窗口扩展到模型支持的最大范围，让模型能看到更多代码和对话上下文；它不是单纯“更聪明按钮”，主要收益来自更大的上下文，主要成本来自更多输入 token。[来源: https://cursor.com/help/ai-features/max-mode] 可信度：高。
2. 在当前个人套餐上，Max Mode 按所选模型的 API token 价格计费；Teams 的非 Auto 请求还会叠加 Cursor Token Rate；旧版 request-based 套餐上 Max Mode 会增加 20% surcharge。[来源: https://cursor.com/docs/models-and-pricing；https://cursor.com/help/models-and-usage/usage-limits] 可信度：高。
3. “消耗相同 token 是否价格相同”不能一概而论：如果是同一模型、同一 token 类型、同一套餐规则、同一上下文计价档位，通常按同一 per-token rate；但部分模型在长上下文或超过 200k 输入 token 时存在 2x input pricing，而 Teams/旧套餐也有额外规则。[来源: https://cursor.com/docs/models-and-pricing] 可信度：高。
4. Max Mode 通常会让一次请求消耗更多 token，因为它会发送更大的上下文；所以即使 per-token 单价相同，总费用也往往更高。[来源: https://cursor.com/help/ai-features/max-mode] 可信度：高。
5. Cursor Agent 可以根据任务复杂度自动启动 subagent；subagent 有独立上下文窗口并独立消耗 token。官方明确提示：并行运行多个 subagent 会近似按多个上下文分别消耗 token，五个 subagent 大致可能接近单 agent 的五倍 token。[来源: https://cursor.com/docs/subagents] 可信度：高。
6. 对本地/编辑器内 subagent，官方没有证据表明“主界面关闭 Max 后，主 agent 会仅因任务复杂就悄悄给 subagent 自动打开 Max”。官方写法更接近：自定义 subagent 默认继承父 agent 模型，或使用指定模型；如果指定模型需要 Max Mode 但未启用，Cursor 会回退到兼容模型。[来源: https://cursor.com/docs/subagents；https://cursor.com/help/models-and-usage/available-models.md] 可信度：高。
7. Cloud Agents 是例外：官方明确说 Cloud Agents 使用一组选定模型，并且始终运行在 Max Mode，没有关闭 Max Mode 的开关；Cloud Agents 按所选模型 API pricing 计费。[来源: https://cursor.com/docs/cloud-agent] 可信度：高。

## 内容整理

### Max Mode 与非 Max Mode 的区别

Max Mode 是 Cursor 中的模型上下文扩展模式。开启后，Cursor 会把上下文窗口扩展到模型支持的最大范围，让模型能处理更大的代码库上下文、跨大文件修改和复杂项目推理。[来源: https://cursor.com/help/ai-features/max-mode]

非 Max Mode 使用默认上下文窗口。Cursor 官方帮助页称，Max Mode 对上下文窗口大于默认约 200k tokens 的模型最有影响；对多数普通编码任务，默认上下文窗口通常已经足够。[来源: https://cursor.com/help/ai-features/max-mode]

启用方式有两类：

- 在 chat 或 agent 面板的模型选择器中打开 Max Mode；该设置是全局设置，会跨对话保持。[来源: https://cursor.com/help/ai-features/max-mode]
- CLI 中可以使用 `/max-mode [on|off]` 切换支持 Max Mode 的模型。[来源: https://cursor.com/docs/cli/reference/slash-commands]

部分模型是 Max Mode-only，选择这些模型时会自动启用 Max Mode。[来源: https://cursor.com/help/ai-features/max-mode]

### Cursor 当前计费池

Cursor 当前个人套餐将用量分为两个池：

- Auto + Composer：Auto 或 Composer 2.5 选中时使用，面向日常 agentic coding，价格更低，Auto 由 Cursor 平衡智能、成本和可靠性。[来源: https://cursor.com/docs/models-and-pricing]
- API：手动选择具体模型或使用 Premium routing 时，按该模型 API 价格消耗 API pool。[来源: https://cursor.com/docs/models-and-pricing]

官方套餐说明：

- Pro：$20/mo，包含 $20 API usage，加上 generous Auto and Composer usage。[来源: https://cursor.com/docs/models-and-pricing；https://cursor.com/help/models-and-usage/usage-limits]
- Pro Plus：$60/mo，包含 $70 API usage，加上 generous Auto and Composer usage。[来源: https://cursor.com/docs/models-and-pricing；https://cursor.com/help/models-and-usage/usage-limits]
- Ultra：$200/mo，包含 $400 API usage，加上 generous Auto and Composer usage。[来源: https://cursor.com/docs/models-and-pricing；https://cursor.com/help/models-and-usage/usage-limits]

Auto 的官方固定 token 价格：

- Input + Cache Write：$1.25 / 1M tokens。[来源: https://cursor.com/docs/models-and-pricing]
- Output：$6.00 / 1M tokens。[来源: https://cursor.com/docs/models-and-pricing]
- Cache Read：$0.25 / 1M tokens。[来源: https://cursor.com/docs/models-and-pricing]

API pool 的价格取决于模型。示例：

- Claude 4.6 Sonnet：Input $3 / 1M，Cache write $3.75 / 1M，Cache read $0.3 / 1M，Output $15 / 1M；备注为 request-based plans 需要 Max Mode，Max Mode up to 1M tokens at same per-token rates，无 long-context surcharge。[来源: https://cursor.com/docs/models-and-pricing]
- GPT-5.5：Input $5 / 1M，Cache read $0.5 / 1M，Output $30 / 1M；备注为 request-based plans 需要 Max Mode，Long context Max Mode 支持 up to 1M tokens with 2x input pricing。[来源: https://cursor.com/docs/models-and-pricing]
- GPT-5.4：Input $2.5 / 1M，Cache read $0.25 / 1M，Output $15 / 1M；备注为 Long context Max Mode supports up to 1M tokens with 2x input pricing。[来源: https://cursor.com/docs/models-and-pricing]
- Grok 4.20：Input $2 / 1M，Cache read $0.2 / 1M，Output $6 / 1M；备注为 input exceeds 200k tokens 时成本 2x。[来源: https://cursor.com/docs/models-and-pricing]

### 同样 token 下是否价格相同

需要分层判断。

第一层：同一模型、同一 token 类型、同一套餐规则、同一上下文计价档位。若这些条件完全相同，则按同一 per-token rate 计费。Cursor 官方对多个 Claude 模型备注“Up to 1M tokens in Max Mode at the same per-token rates (no long-context surcharge)”。[来源: https://cursor.com/docs/models-and-pricing]

第二层：Max Mode 与非 Max Mode 总价。即使 per-token 单价相同，Max Mode 由于上下文更大，通常会发送更多 input tokens，因此单次请求可能消耗更多预算。[来源: https://cursor.com/help/ai-features/max-mode]

第三层：部分模型存在长上下文额外规则。Cursor 官方模型表中，Claude 4 Sonnet 1M 写明 input exceeds 200k tokens 时成本 2x；GPT-5.4 与 GPT-5.5 写明 Long context Max Mode supports up to 1M tokens with 2x input pricing；Grok 4.20 也写明 input exceeds 200k tokens 时成本 2x。[来源: https://cursor.com/docs/models-and-pricing]

第四层：套餐差异。当前个人套餐 Max Mode 按模型 API rate；Teams 非 Auto agent 请求会叠加 Cursor Token Rate $0.25 / 1M tokens；旧版 request-based 套餐 Max Mode 增加 20% surcharge。[来源: https://cursor.com/docs/models-and-pricing；https://cursor.com/help/models-and-usage/usage-limits]

因此，最准确的回答是：同 token 不必然同价。只有在模型、token 类型、计费池、套餐、长上下文档位完全一致时才可视为同价；否则可能不同。

### Subagent 与 Max Mode 的关系

Cursor subagent 是父 agent 可委托的专用 AI assistant。每个 subagent 有自己的上下文窗口，处理特定任务后把结果返回父 agent。[来源: https://cursor.com/docs/subagents]

Cursor built-in subagents 包括 Explore、Bash、Browser，分别处理代码库搜索分析、shell 命令序列、浏览器/MCP 操作。它们会自动处理上下文重、输出噪声大的任务。[来源: https://cursor.com/docs/subagents]

Cursor Agent 可以基于任务复杂度和范围、custom subagent description、当前上下文和工具自动委派 subagent。[来源: https://cursor.com/docs/subagents]

模型选择规则：

- Built-in subagents 会根据 subtask 自动选择模型。[来源: https://cursor.com/help/models-and-usage/available-models.md]
- Custom subagents 默认 `model: inherit`，使用父 agent 的模型；也可在 YAML frontmatter 里指定具体模型 ID。[来源: https://cursor.com/docs/subagents]
- Cursor 会尽量遵守 subagent 的 `model` 字段，但如果团队管理员禁用模型、模型需要 Max Mode 而用户未启用 Max Mode、或当前套餐不可用，Cursor 会回退到兼容模型。[来源: https://cursor.com/docs/subagents]
- 官方 FAQ 还说明：旧版 request-based plans 且未启用 Max Mode 时，subagents 会使用 Composer regardless of any `model` configuration；如果团队管理员阻止 Composer，request-based plans 的 subagents 只能在 Max Mode 中运行；usage-based plans and Max Mode will default to the parent model。[来源: https://cursor.com/docs/subagents]

这意味着：本地 subagent 可能与主 agent 使用不同模型，尤其 built-in subagent 会自动选模型；但官方没有说“主界面关闭 Max 后，本地 subagent 会因为任务复杂自动打开 Max”。官方明确写法反而是：指定模型需要 Max Mode 而未启用时会 fallback 到兼容模型。[来源: https://cursor.com/docs/subagents]

### Cloud Agents 例外

Cloud Agents 与本地 subagent/本地 agent 不同。官方 Cloud Agents 文档明确写道：Cloud Agents use a curated selection of models that always run in Max Mode；There is no toggle to turn Max Mode off for Cloud Agents。[来源: https://cursor.com/docs/cloud-agent]

Cloud Agents 的 Billing 章节写明：Cloud Agents are charged at API pricing for the selected model，并且首次使用时会要求设置 spend limit。[来源: https://cursor.com/docs/cloud-agent]

因此，如果用户把任务交给 Cloud Agents，即使本地 chat 的 Max Mode 关闭，Cloud Agents 仍会以 Max Mode 运行。这是官方确认的例外。

## 推荐工作流

1. 默认使用 Auto 或 Composer 处理日常编辑、短上下文问答、局部 bugfix。Auto/Composer 使用单独用量池，适合成本敏感的日常工作。[来源: https://cursor.com/docs/models-and-pricing；https://cursor.com/help/models-and-usage/available-models.md]
2. 只有当任务需要跨大文件、大量上下文或复杂架构推理时，手动打开 Max Mode。Cursor 官方也建议 watching usage carefully 时应 selectively use Max Mode。[来源: https://cursor.com/help/ai-features/max-mode]
3. 在模型选择器确认当前模型是否为 Max Mode-only；如果是，选择它可能自动启用 Max Mode。[来源: https://cursor.com/help/ai-features/max-mode]
4. 处理复杂任务前先看 `cursor.com/dashboard` 的 Usage；任务完成后复查用量和 token breakdown。[来源: https://cursor.com/help/models-and-usage/usage-limits]
5. 使用自定义 subagent 时，优先显式写 `model: inherit`，避免不必要的昂贵模型覆盖；只有确有需要时才指定昂贵模型。[来源: https://cursor.com/docs/subagents]
6. 需要高并发 subagent 时，先预估 token 成本。官方说明每个 subagent 独立消耗 token，五个并行 subagent 可能接近五倍 token。[来源: https://cursor.com/docs/subagents]
7. 若使用 Cloud Agents，默认按 Max Mode + API pricing 思维预算，并设置 spend limit。[来源: https://cursor.com/docs/cloud-agent]

## 适用场景

- 大型代码库中跨目录、跨模块理解和修改，需要模型看到更多上下文。[来源: https://cursor.com/help/ai-features/max-mode]
- 复杂多步骤任务，需要 subagent 分担探索、shell、浏览器或验证工作，且用户能接受额外 token 消耗。[来源: https://cursor.com/docs/subagents]
- 云端长跑任务、自动化或并行任务，且用户愿意按 Cloud Agents 的 Max Mode/API pricing 预算。[来源: https://cursor.com/docs/cloud-agent]

## 不适用场景

- 单文件小改、局部重命名、短问题问答。Cursor 官方称多数 coding tasks 默认上下文窗口工作良好。[来源: https://cursor.com/help/ai-features/max-mode]
- 成本敏感且不需要长上下文的日常任务，应优先 Auto/Composer。[来源: https://cursor.com/docs/models-and-pricing]
- 简单任务不适合拆成 subagent。官方说明 subagent 对简单任务可能更慢，因为它启动新上下文并独立收集上下文。[来源: https://cursor.com/docs/subagents]

## 风险与约束

- Max Mode 不是固定“贵 20%”。当前个人套餐按 API rate，旧版 request-based plans 才有 20% surcharge，Teams 有 Cursor Token Rate；部分长上下文模型还有 2x input pricing。[来源: https://cursor.com/docs/models-and-pricing；https://cursor.com/help/models-and-usage/usage-limits]
- Max Mode 的主要费用风险是上下文扩大导致 input tokens 增加，而不是一定存在单独加价。[来源: https://cursor.com/help/ai-features/max-mode]
- Subagents 独立消耗 token，并行越多越容易放大成本。[来源: https://cursor.com/docs/subagents]
- Built-in subagents 会自动选择模型，custom subagents 默认继承父模型；若成本异常，应检查 usage dashboard 的 request-level 模型和成本。[来源: https://cursor.com/help/models-and-usage/available-models.md；https://cursor.com/docs/models-and-pricing]
- Cloud Agents 始终 Max Mode，没有关闭开关，不能按本地 Max Mode 开关来推断成本。[来源: https://cursor.com/docs/cloud-agent]

## 信源质量门控记录

### 门控规则

- 优先保留 Cursor 官方文档、官方帮助页、官方定价页。
- 对搜索分数低但主题关键的官方页面，人工恢复并精读；官方定价页不能因 Tavily score 低于 0.4 而剔除。
- 二手定价解读文章仅作背景，不作为核心结论唯一依据。
- 学术论文候选虽然来源等级高，但多数与 Cursor Max Mode 定价问题不直接相关，剔除为主题不相关。
- C/D 级来源不得作为唯一结论依据。
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`。

### 保留信源

1. [Models & Pricing | Cursor Docs](https://cursor.com/docs/models-and-pricing)
   - 工具：WebFetch / WebSearch
   - 分数：官方关键来源，人工保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方定价、模型价格、Max Mode、套餐、Cursor Token Rate 的一手来源
   - 后续处理：进入精读
2. [Max Mode | Cursor Docs](https://cursor.com/help/ai-features/max-mode)
   - 工具：WebFetch / WebSearch
   - 分数：官方关键来源
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方解释 Max Mode 启用方式、作用、计费影响和使用建议
   - 后续处理：进入精读
3. [Usage and limits | Cursor Docs](https://cursor.com/help/models-and-usage/usage-limits)
   - 工具：WebFetch / WebSearch
   - 分数：官方关键来源
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方解释套餐 usage budget、dashboard、Max Mode 在当前个人套餐和旧套餐上的计费
   - 后续处理：进入精读
4. [Subagents | Cursor Docs](https://cursor.com/docs/subagents)
   - 工具：WebFetch / WebSearch
   - 分数：官方关键来源
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方解释 subagent 自动委派、模型继承/覆盖、Max Mode required 时 fallback、token/cost considerations
   - 后续处理：进入精读
5. [Available models | Cursor Docs](https://cursor.com/help/models-and-usage/available-models.md)
   - 工具：WebFetch / WebSearch
   - 分数：官方关键来源
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方解释模型切换、Auto/Premium、subagents 使用什么模型
   - 后续处理：进入精读
6. [Cloud Agents | Cursor Docs](https://cursor.com/docs/cloud-agent)
   - 工具：WebFetch / WebSearch
   - 分数：官方关键来源
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方确认 Cloud Agents 始终 Max Mode、无法关闭、按 API pricing 计费
   - 后续处理：进入精读
7. [Agent mode | Cursor Docs](https://cursor.com/help/ai-features/agent)
   - 工具：WebFetch / WebSearch
   - 分数：官方补充来源
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方确认 Agent 可委托 subagents
   - 后续处理：进入精读
8. [What is multi-agent coding? | Cursor Docs](https://cursor.com/help/ai-features/multi-agent)
   - 工具：WebFetch / WebSearch
   - 分数：官方补充来源
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方解释 multi-agent 与 subagent 的基础定义
   - 后续处理：进入精读

### 剔除信源

1. arXiv 学术论文候选，如 `Token Is All You Price`、`AOrchestra`、`Recursive Agent Harnesses` 等
   - 工具：Exa
   - 分数：Exa 默认高分
   - 来源等级：A
   - 剔除原因：与 Cursor 产品 Max Mode 定价规则不直接相关，不能回答产品计费问题
2. 二手博客和社区解读，如 CloudZero、Verdent、Medium、Appscribed、Finout
   - 工具：WebSearch / Tavily
   - 来源等级：C
   - 剔除原因：可能有实用背景，但当前官方文档已直接覆盖核心事实；不作为核心结论依据
3. 中文搬运/聚合文章，如掘金、53AI、第三方中文文档镜像
   - 工具：Tavily
   - 来源等级：C/D
   - 剔除原因：存在过时、搬运、非官方和转述风险；只在官方不可用时作线索

## 来源与可信度

- https://cursor.com/docs/models-and-pricing — 官方模型与定价页。可信度：高。支撑计费池、模型价格、Max Mode 计费、Teams Cursor Token Rate、套餐 included usage。
- https://cursor.com/help/ai-features/max-mode — 官方 Max Mode 帮助页。可信度：高。支撑 Max Mode 定义、启用方式、全局开关、Max-only 模型、使用建议。
- https://cursor.com/help/models-and-usage/usage-limits — 官方用量与限制页。可信度：高。支撑各套餐 API usage、usage dashboard、limit 后处理、Max Mode 当前/旧套餐计费。
- https://cursor.com/docs/subagents — 官方 subagent 参考。可信度：高。支撑自动委派、model inherit/override、fallback 规则、token/cost considerations。
- https://cursor.com/help/models-and-usage/available-models.md — 官方模型可用性页。可信度：高。支撑 built-in/custom subagents 的模型选择说明。
- https://cursor.com/docs/cloud-agent — 官方 Cloud Agents 页。可信度：高。支撑 Cloud Agents 始终 Max Mode、无法关闭、API pricing 计费。
- https://cursor.com/help/ai-features/agent — 官方 Agent mode 帮助页。可信度：高。支撑 Agent 可委托 subagents。
- https://cursor.com/help/ai-features/multi-agent — 官方 multi-agent 帮助页。可信度：高。支撑 subagent 基础定义和多 agent 运行方式。

## 对于可信度较高的来源逐来源总结

### Models & Pricing | Cursor Docs

该页面是本次调研最关键的计费依据。它说明 Cursor 个人套餐有两个 usage pools：Auto + Composer 和 API。Auto + Composer 面向低成本日常 agentic coding；API pool 用于手动选择具体模型或 Premium routing，并按模型 API rate 计费。[来源: https://cursor.com/docs/models-and-pricing]

该页面还列出模型级 per-token 价格，区分 input、cache write、cache read、output。模型备注中直接影响 Max Mode 成本的关键信息包括：部分 Claude 模型在 Max Mode up to 1M tokens 时保持 same per-token rates、no long-context surcharge；部分模型如 GPT-5.4/GPT-5.5 的 Long context Max Mode 存在 2x input pricing；部分模型在 input exceeds 200k tokens 时成本 2x。[来源: https://cursor.com/docs/models-and-pricing]

该页面还说明个人套餐包含 API usage：Pro $20、Pro Plus $70、Ultra $400；超过 included monthly usage 后可启用 on-demand usage 或升级套餐；on-demand usage 按 same API rates 月结，Requests are never downgraded in quality or speed。[来源: https://cursor.com/docs/models-and-pricing]

适合入库的知识点：Cursor usage pools、Cursor API pool、Cursor Auto pricing、Cursor Max Mode pricing、Cursor Token Rate、Cursor subagent cost budgeting。

### Max Mode | Cursor Docs

该页面定义 Max Mode：把 context window 扩展到模型支持的最大值，使模型对代码库有更深入理解，适合大型文件和复杂项目的准确编辑。[来源: https://cursor.com/help/ai-features/max-mode]

该页面说明启用方式：在 chat 或 agent panel 的 model selector 中打开 Max Mode。它是 global setting，跨 conversations 保持。部分 Max Mode-only 模型在被选择时会自动启用。[来源: https://cursor.com/help/ai-features/max-mode]

该页面说明 Max Mode 对用量影响：Max Mode uses token-based pricing，因此单个 request 可能显著消耗更多 usage budget。当前个人套餐按模型 API rate；Teams 非 Auto 请求包含 Cursor Token Rate；旧版 request-based plans 增加 20% surcharge。[来源: https://cursor.com/help/ai-features/max-mode]

适合入库的知识点：Cursor Max Mode definition、Max Mode enablement、Max Mode cost risk、Max-only models。

### Usage and limits | Cursor Docs

该页面确认每个 Cursor plan 包含 monthly budget of API usage charged at model provider prices，另外有 generous Auto and Composer usage。它列出 Pro、Pro Plus、Ultra 的 API agent usage 分别为 $20、$70、$400。[来源: https://cursor.com/help/models-and-usage/usage-limits]

该页面强调 model selection affects how quickly included usage is consumed，并可在 dashboard 查看 usage 和 token breakdowns。达到 usage limit 后，用户会在 editor 中看到通知，可启用 usage-based pricing 或升级套餐。[来源: https://cursor.com/help/models-and-usage/usage-limits]

适合入库的知识点：Cursor usage dashboard、Cursor monthly usage reset、Cursor usage-based pricing。

### Subagents | Cursor Docs

该页面定义 subagents：由 Cursor agent 委托的专用 AI assistants，各自运行在独立 context window，完成任务后把结果返回 parent agent。它们用于拆分复杂任务、并行工作和保存主对话上下文。[来源: https://cursor.com/docs/subagents]

该页面说明 Agent 可以自动使用 subagent：当 Agent 遇到 complex task 时，可以自动启动 subagent。自动委派基于 task complexity and scope、custom subagent descriptions、current context and available tools。[来源: https://cursor.com/docs/subagents]

模型规则方面，该页面说明 custom subagent 的 `model` 默认为 `inherit`，使用父 agent 模型；也可指定具体模型 ID。Cursor 会遵守该字段，除非模型被团队管理员禁用、模型需要 Max Mode 而未启用、或套餐不可用；这些情况下会 fallback 到 compatible model。[来源: https://cursor.com/docs/subagents]

成本方面，该页面明确指出 subagents consume tokens independently。每个 subagent 有自己的 context window 和 token usage；running five subagents in parallel uses roughly five times the tokens of a single agent。[来源: https://cursor.com/docs/subagents]

适合入库的知识点：Cursor subagent model inheritance、subagent automatic delegation、subagent token cost、subagent fallback rules。

### Available models | Cursor Docs

该页面说明 Cursor 模型选择会跨 conversations 保持；Auto 会根据 intelligence、cost、reliability 平衡选模型；Premium 会为复杂任务选择最强模型，并按所选模型 API rate 计费。[来源: https://cursor.com/help/models-and-usage/available-models.md]

该页面直接回答“subagents 使用什么模型”：built-in subagents, including Explore, Bash, Browser, select their model automatically based on the subtask；custom subagents default to `inherit`，也可在 YAML frontmatter 的 `model` 字段覆盖。[来源: https://cursor.com/help/models-and-usage/available-models.md]

适合入库的知识点：Cursor built-in subagent model selection、Cursor custom subagent model override。

### Cloud Agents | Cursor Docs

该页面说明 Cloud Agents 是运行在云端隔离 VM 中的 agents，可在云端并行执行任务，不需要本地机器联网。[来源: https://cursor.com/docs/cloud-agent]

模型章节直接说明：Cloud Agents use a curated selection of models that always run in Max Mode；There is no toggle to turn Max Mode off for Cloud Agents。[来源: https://cursor.com/docs/cloud-agent]

Billing 章节说明 Cloud Agents are charged at API pricing for the selected model，首次使用时会要求设置 spend limit。[来源: https://cursor.com/docs/cloud-agent]

适合入库的知识点：Cursor Cloud Agents Max Mode、Cloud Agents billing、Cloud Agents spend limit。

## 跨源矛盾检测结论

### 检测范围

- 已精读来源数量：8 个官方 Cursor 来源。
- 检测对象：Max Mode 定义、启用方式、套餐价格、API usage、per-token pricing、Teams/旧套餐差异、subagent 模型选择、Cloud Agents Max Mode 行为。
- 检测时间：2026-06-17。

### 检测结果

结论：核心官方来源之间未检测到直接矛盾，但存在需要分场景解释的差异项。

### 差异项 1：Max-only 模型自动启用 Max vs subagent 模型需要 Max 但未启用时 fallback

- 来源 A：https://cursor.com/help/ai-features/max-mode
  - 表述：Some models are Max Mode-only and enable it automatically when selected.
  - 来源等级：A
- 来源 B：https://cursor.com/docs/subagents
  - 表述：Cursor honors subagent `model` unless Max Mode required and you don't have it enabled; in these cases Cursor falls back to a compatible model.
  - 来源等级：A
- 初步判断：不视为矛盾。来源 A 描述用户在模型选择器中选择 Max-only 模型的行为；来源 B 描述 subagent frontmatter 指定模型但 Max Mode 未启用时的 fallback 行为。
- 综合输出要求：回答时区分“用户选择模型”和“subagent 配置模型”两个场景。

### 差异项 2：同 token 同价 vs 长上下文 2x input pricing

- 来源 A：https://cursor.com/docs/models-and-pricing
  - 表述：部分 Claude 模型备注 Max Mode up to 1M tokens at same per-token rates (no long-context surcharge)。
  - 来源等级：A
- 来源 B：https://cursor.com/docs/models-and-pricing
  - 表述：GPT-5.4/GPT-5.5 Long context (Max Mode) supports up to 1M tokens with 2x input pricing；部分模型 input exceeds 200k tokens 时成本 2x。
  - 来源等级：A
- 初步判断：不是跨源矛盾，而是模型级规则不同。
- 综合输出要求：禁止把“Max Mode 同 token 同价”写成通用结论，必须限定到具体模型和计价档位。

## 矛盾与待验证问题

- 官方文档没有直接说明 built-in subagents 自动选模型时是否可能选择一个会导致 Max Mode 的模型；但 subagent 文档明确说模型需要 Max Mode 而未启用时会 fallback，Cloud Agents 另有始终 Max Mode 规则。结论应写为：本地 subagent 自动打开 Max 的说法未被官方证实；Cloud Agents 始终 Max 已被官方证实。[来源: https://cursor.com/docs/subagents；https://cursor.com/docs/cloud-agent]
- 官方文档未给出每次 subagent 调用在 usage dashboard 中展示的字段细节；但 Models & Pricing 页说明 usage page 可在 request level 查看 cost and model selection。建议实际排查时以 dashboard 为准。[来源: https://cursor.com/docs/models-and-pricing]
- 具体模型价格会随 Cursor 和模型供应商更新而变动；入库后应定期复核 `Models & Pricing` 官方页。[来源: https://cursor.com/docs/models-and-pricing]

## 原始证据摘录

> Max Mode extends the context window to the maximum a model supports, giving it a deeper understanding of your codebase for more accurate edits across large files and complex projects. [来源: https://cursor.com/help/ai-features/max-mode]

> Open the model selector in your chat or agent panel and toggle Max Mode on. It's a global setting that stays on across conversations. Some models are Max Mode-only and enable it automatically when selected. [来源: https://cursor.com/help/ai-features/max-mode]

> Max Mode uses token-based pricing, so a single request can use significantly more of your usage budget than a normal request. [来源: https://cursor.com/help/ai-features/max-mode]

> On current individual plans, Max Mode is billed at the model's API rate. On Teams plans, non-Auto requests include the Cursor Token Rate. On legacy request-based plans, Max Mode adds a 20% surcharge. [来源: https://cursor.com/help/ai-features/max-mode]

> When you select a specific model (or use Premium routing), usage is drawn from the API pool at that model's API rate. [来源: https://cursor.com/docs/models-and-pricing]

> Cursor Token Rate: On Teams plans, non-Auto agent requests include a Cursor Token Rate of $0.25 per million tokens. [来源: https://cursor.com/docs/models-and-pricing]

> Subagents consume tokens independently — Each subagent has its own context window and token usage. Running five subagents in parallel uses roughly five times the tokens of a single agent. [来源: https://cursor.com/docs/subagents]

> Built-in subagents (Explore, Bash, Browser) select their model automatically based on the subtask. Custom subagents default to `inherit`, which uses the parent agent's model. [来源: https://cursor.com/help/models-and-usage/available-models.md]

> Cursor honors the `model` field in your subagent frontmatter unless one of these conditions applies: Team admin restrictions; Max Mode required — The model requires Max Mode and you don't have it enabled; Plan limitations. In these cases, Cursor falls back to a compatible model. [来源: https://cursor.com/docs/subagents]

> Cloud Agents use a curated selection of models that always run in Max Mode. There is no toggle to turn Max Mode off for Cloud Agents. [来源: https://cursor.com/docs/cloud-agent]

> Cloud Agents are charged at API pricing for the selected model. You'll be asked to set a spend limit when you first start using them. [来源: https://cursor.com/docs/cloud-agent]
