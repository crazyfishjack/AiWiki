---
title: "调研证据包：投标助手招标文件解析场景下的 LLM 提示词设计：多任务拆解、结构化输出、少样本示例与幻觉防控"
source-type: article
generated: 2026-06-21
generated-by: wiki-research-skill
research-mode: standard
---

# 调研证据包：投标助手招标文件解析场景下的 LLM 提示词设计：多任务拆解、结构化输出、少样本示例与幻觉防控

## 调研问题

投标助手招标文件解析场景下的 LLM 提示词设计：多任务拆解、结构化输出、少样本示例与幻觉防控

## 摘要

本文档是四工具检索生成的证据包草稿，不是最终调研报告。Agent 必须先阅读本证据包，执行下方"AI 综合指令"，生成新的中文综合 raw 报告，然后询问用户是否入库。本证据包保留不删除。

- 发现候选信源：25
- 精读信源数量：10
- 精读成功数量：10
- 精读失败数量：0

## AI 综合指令（Agent 必须执行）

请基于本文档的候选信源和完整精读结果生成最终中文调研报告。最终报告必须编写为一个新的 raw Markdown 文件，并删除本文档这个证据包。最终报告必须满足：

1. 删除本“AI 综合指令”占位说明，保留必要原始证据摘录。
2. 用中文输出，不要只粘贴网页摘录。
3. 每条关键事实后标注 `[来源: URL]`。
4. 每条核心结论标注可信度：高 / 中 / 低。
5. 显式列出跨源矛盾、证据不足和待验证问题。
6. 不得把无 URL 支撑的内容写成事实；如确需提及，标注“未验证”。
7. 若本文档中的高可信来源精读失败、正文为空、明显不完整或只有导航/付费墙内容，必须二次精读；否则优先使用证据包中的完整精读结果。
8. 必须包含 `## 对于可信度较高的来源逐来源总结`，逐篇整理高可信来源的核心内容、可用事实、局限和适合入库的知识点。
9. 对重要来源进行完整性检查：若本文档精读结果不足以覆盖正文，应重新读取或抓取该来源全文后再生成最终报告，不得只依赖不完整内容。
10. 必须保留 `## 信源质量门控记录`，列出保留信源、剔除信源、来源等级、保留/剔除原因和后续处理。
11. 必须保留 `## 跨源矛盾检测结论`，逐项检测核心数字、日期、功能描述、因果判断、市场/公司事实。
12. 入库到 `wiki/sources/` 时，来源等级按 A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low` 映射。

最终报告结构必须包含：

- `## 核心结论`：3-7 条可复用结论，每条带来源和可信度。
- `## 内容整理`：保留所有有用的信息，系统化，结构清晰，逻辑正确。
- `## 推荐工作流`：说明如何组合使用这些工具，明确 Cursor 中的执行步骤。
- `## 适用场景`：列出适合采用该方法的项目类型。
- `## 不适用场景`：说明何时会过度工程或不值得引入。
- `## 风险与约束`：列出衔接点、上下文、测试、规格漂移等风险。
- `## 信源质量门控记录`：记录门控规则、保留信源、剔除信源和 A/B/C/D 来源等级。
- `## 来源与可信度`：逐项列出关键来源、来源类型、可信度和支撑内容。
- `## 对于可信度较高的来源逐来源总结`：逐篇整理高可信来源正文，不只提取少量核心结论。
- `## 跨源矛盾检测结论`：说明检测范围、检测结果和所有矛盾项；未发现矛盾也必须明确写出。
- `## 矛盾与待验证问题`：保留冲突或证据不足处。
- `## 原始证据摘录`：保留支持结论的必要摘录或完整证据片段。

本证据包默认保存完整精读结果，不对 Firecrawl/Jina 正文做字符截断。若配置关闭全文证据模式，才会回退为摘录模式。
- 证据包全文模式：true
- 兼容摘录上限：2000 字符（仅在全文模式关闭时使用）
- 若某来源精读失败、正文为空、疑似反爬/付费墙/导航页或工具返回明显不完整，Agent 必须二次精读或标注不可验证。

## 候选信源

| 工具 | 分数 | 标题 | URL |
|------|-------|-------|-----|
| exa | 1.00 |  | https://arxiv.org/pdf/2603.23482 |
| exa | 1.00 | PEER: Expertizing Domain-Specific Tasks with a Multi-Agent Framework and Tuning Methods | https://www.arxiv.org/pdf/2407.06985v4 |
| exa | 1.00 | BIM-GPT: a Prompt-Based Virtual Assistant Framework for BIM Information Retrieval | https://arxiv.org/pdf/2304.09333 |
| exa | 1.00 | A Large Language Model-based Framework for Semi-Structured Tender Document Retrieval-Augmented Generation | https://arxiv.org/html/2410.09077v1 |
| exa | 1.00 |  | https://arxiv.org/pdf/2410.09077 |
| exa | 1.00 | Large Language Models for Structured Information Processing in Construction and Facility Management | https://www.mdpi.com/2079-9292/14/20/4106 |
| exa | 1.00 | From Large Language Model Predicates to Logic Tensor Networks: Neurosymbolic Offer Validation in Regulated Procurement | https://arxiv.org/html/2604.05539 |
| exa | 1.00 | Large Language Model for Extracting Complex Contract Information in Industrial Scenes | https://arxiv.org/html/2507.06539v2 |
| exa | 1.00 | Automated multi-label classification of risk clauses in construction contracts using GPT-driven data augmentation - ScienceDirect | https://www.sciencedirect.com/science/article/pii/S0926580525006399 |
| exa | 1.00 | Knowledge-Driven Hallucination in Large Language Models: An Empirical Study on Process ModelingThe Version of Record of this contribution will be published in the proceedings of the 2nd International Workshop on Generative AI for Process Mi | https://arxiv.org/pdf/2509.15336 |
| exa | 1.00 | DOCUEVAL: An LLM-based AI Engineering Tool for Building Customisable Document Evaluation Workflows | https://arxiv.org/pdf/2511.05496 |
| exa | 1.00 | LLM-as-Judge Framework for Evaluating Tone-Induced Hallucination in Vision-Language Models | https://arxiv.org/html/2604.18803v3 |
| exa | 1.00 | Tone Matters: The Impact of Linguistic Tone on Hallucination in VLMs | https://arxiv.org/html/2601.06460 |
| exa | 1.00 | [2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models | https://arxiv.org/abs/2309.12132v2 |
| exa | 1.00 | A Search for Prompts: Generating Structured Answers from Contracts | https://arxiv.org/html/2310.10141v1 |
| tavily | 0.62 | prompt提示词和prompt-engineering提示词工程基础学习 - 九卷 - 博客园 | https://www.cnblogs.com/jiujuan/p/19855636 |
| tavily | 0.54 | 提示工程（prompt engineering)：技术分类与提示词调优看这篇就够了 - 文章 - 开发者社区 - 火山引擎 | https://developer.volcengine.com/articles/7387978567193526308 |
| tavily | 0.53 | 激发LLM涌现——提示工程 - 李乾坤的博客 | https://qiankunli.github.io/2023/10/29/llm_prompt.html |
| tavily | 0.52 | modelscope-classroom/LLM-tutorial/C.提示词工程-prompt engineering.md at main · modelscope/modelscope-classroom · GitHub | https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md |
| tavily | 0.48 | 提示词工程（Prompt Engineering） \| ZHANG RONG | https://zr9558.com/2025/05/28/prompt-engineering |
| tavily | 0.48 | 文生文Prompt指南 - 阿里云帮助文档 | https://help.aliyun.com/zh/model-studio/prompt-engineering-guide |
| tavily | 0.46 | 附录 A - 高级提示工程技术 \| Jimmy Song | https://jimmysong.io/zh/book/agentic-design-patterns/appendix-a-advanced-prompting-techniques |
| tavily | 0.45 | 充分释放大模型的潜力——提示词工程的16 种方式 - AWS | https://aws.amazon.com/cn/blogs/china/sixteen-ways-of-prompt-engineering |
| tavily | 0.43 | 高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云 | https://cloud.tencent.com/developer/article/2498790 |
| tavily | 0.42 | Prompt工程指南 - 华东师范大学开发者平台 | https://developer.ecnu.edu.cn/vitepress/llm/prompts.html |

## 信源质量门控记录

### 门控规则
- Tavily score < 0.4：剔除
- 已知低质域名：剔除
- 重复 URL：合并保留最高分结果
- Exa 学术/语义结果：默认保留，但进入来源等级评估
- C/D 级来源不得作为唯一结论依据
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`

### 保留信源
1. [https://arxiv.org/pdf/2603.23482](https://arxiv.org/pdf/2603.23482)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
2. [PEER: Expertizing Domain-Specific Tasks with a Multi-Agent Framework and Tuning Methods](https://www.arxiv.org/pdf/2407.06985v4)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
3. [BIM-GPT: a Prompt-Based Virtual Assistant Framework for BIM Information Retrieval](https://arxiv.org/pdf/2304.09333)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
4. [A Large Language Model-based Framework for Semi-Structured Tender Document Retrieval-Augmented Generation](https://arxiv.org/html/2410.09077v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
5. [https://arxiv.org/pdf/2410.09077](https://arxiv.org/pdf/2410.09077)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
6. [Large Language Models for Structured Information Processing in Construction and Facility Management](https://www.mdpi.com/2079-9292/14/20/4106)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
7. [From Large Language Model Predicates to Logic Tensor Networks: Neurosymbolic Offer Validation in Regulated Procurement](https://arxiv.org/html/2604.05539)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
8. [Large Language Model for Extracting Complex Contract Information in Industrial Scenes](https://arxiv.org/html/2507.06539v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
9. [Automated multi-label classification of risk clauses in construction contracts using GPT-driven data augmentation - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0926580525006399)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
10. [Knowledge-Driven Hallucination in Large Language Models: An Empirical Study on Process ModelingThe Version of Record of this contribution will be published in the proceedings of the 2nd International Workshop on Generative AI for Process Mining (GenAI4PM 2025). This preprint has not undergone peer review or any post-submission improvements or corrections.](https://arxiv.org/pdf/2509.15336)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
11. [DOCUEVAL: An LLM-based AI Engineering Tool for Building Customisable Document Evaluation Workflows](https://arxiv.org/pdf/2511.05496)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
12. [LLM-as-Judge Framework for Evaluating Tone-Induced Hallucination in Vision-Language Models](https://arxiv.org/html/2604.18803v3)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
13. [Tone Matters: The Impact of Linguistic Tone on Hallucination in VLMs](https://arxiv.org/html/2601.06460)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
14. [[2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models](https://arxiv.org/abs/2309.12132v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
15. [A Search for Prompts: Generating Structured Answers from Contracts](https://arxiv.org/html/2310.10141v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
16. [prompt提示词和prompt-engineering提示词工程基础学习 - 九卷 - 博客园](https://www.cnblogs.com/jiujuan/p/19855636)
   - 工具：tavily
   - 分数：0.62
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
17. [提示工程（prompt engineering)：技术分类与提示词调优看这篇就够了 - 文章 - 开发者社区 - 火山引擎](https://developer.volcengine.com/articles/7387978567193526308)
   - 工具：tavily
   - 分数：0.54
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
18. [激发LLM涌现——提示工程 - 李乾坤的博客](https://qiankunli.github.io/2023/10/29/llm_prompt.html)
   - 工具：tavily
   - 分数：0.53
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
19. [modelscope-classroom/LLM-tutorial/C.提示词工程-prompt engineering.md at main · modelscope/modelscope-classroom · GitHub](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md)
   - 工具：tavily
   - 分数：0.52
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
20. [提示词工程（Prompt Engineering） | ZHANG RONG](https://zr9558.com/2025/05/28/prompt-engineering)
   - 工具：tavily
   - 分数：0.48
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
21. [文生文Prompt指南 - 阿里云帮助文档](https://help.aliyun.com/zh/model-studio/prompt-engineering-guide)
   - 工具：tavily
   - 分数：0.48
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
22. [附录 A - 高级提示工程技术 | Jimmy Song](https://jimmysong.io/zh/book/agentic-design-patterns/appendix-a-advanced-prompting-techniques)
   - 工具：tavily
   - 分数：0.46
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
23. [充分释放大模型的潜力——提示词工程的16 种方式 - AWS](https://aws.amazon.com/cn/blogs/china/sixteen-ways-of-prompt-engineering)
   - 工具：tavily
   - 分数：0.45
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
24. [高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.43
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
25. [Prompt工程指南 - 华东师范大学开发者平台](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html)
   - 工具：tavily
   - 分数：0.42
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读

### 剔除信源
1. [[PDF] 目录](https://assets.jimmysong.io/books/agentic-design-patterns-zh-20251208.pdf)
   - 工具：tavily
   - 分数：0.34
   - 来源等级：C
   - 剔除原因：score 低于 0.4
2. [南京招标投标协会](http://www.njzbtb.com/Info.aspx?ClassCode=011014002&InforGuid=20250324112556f51f8a48-a1c6-46df-87c7-3a0e6c130db8)
   - 工具：tavily
   - 分数：0.33
   - 来源等级：C
   - 剔除原因：score 低于 0.4
3. [少样本提示 | Prompt Engineering Guide<!-- -->](https://www.promptingguide.ai/zh/techniques/fewshot)
   - 工具：tavily
   - 分数：0.31
   - 来源等级：C
   - 剔除原因：score 低于 0.4
4. [什么是思维链 (CoT) 提示？ | Ultralytics](https://www.ultralytics.com/zh/glossary/chain-of-thought-prompting)
   - 工具：tavily
   - 分数：0.26
   - 来源等级：C
   - 剔除原因：score 低于 0.4
5. [文生文Prompt指南 - 阿里云帮助文档](https://help.aliyun.com/zh/model-studio/prompt-engineering-guide)
   - 工具：tavily
   - 分数：0.40
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
6. [C.提示词工程-prompt engineering.md - GitHub](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md)
   - 工具：tavily
   - 分数：0.46
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
7. [激发LLM涌现——提示工程 - 李乾坤的博客](https://qiankunli.github.io/2023/10/29/llm_prompt.html)
   - 工具：tavily
   - 分数：0.40
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
8. [充分释放大模型的潜力——提示词工程的16 种方式 - AWS](https://aws.amazon.com/cn/blogs/china/sixteen-ways-of-prompt-engineering)
   - 工具：tavily
   - 分数：0.40
   - 来源等级：C
   - 剔除原因：score 低于 0.4
9. [Prompt Engineering 教學：系統化提示設計完全指南](https://www.meta-intelligence.tech/insight-prompt-engineering)
   - 工具：tavily
   - 分数：0.38
   - 来源等级：C
   - 剔除原因：score 低于 0.4
10. [链式提示](https://www.promptingguide.ai/zh/techniques/prompt_chaining)
   - 工具：tavily
   - 分数：0.34
   - 来源等级：C
   - 剔除原因：score 低于 0.4
11. [工程技术提示语 - Microsoft Foundry | Microsoft Learn](https://learn.microsoft.com/zh-cn/azure/foundry/openai/concepts/prompt-engineering)
   - 工具：tavily
   - 分数：0.30
   - 来源等级：C
   - 剔除原因：score 低于 0.4
12. [2.5 智能体提示词工程| 智能体AI 权威指南| Agentic AI Guide](https://yeasy.gitbook.io/agentic_ai_guide/di-yi-bu-fen-dan-ti-zhi-neng-jia-gou/02_reasoning/2.5_prompt_engineering)
   - 工具：tavily
   - 分数：0.22
   - 来源等级：C
   - 剔除原因：score 低于 0.4
13. [China isn’t trying to beat the U.S. at AI — it’s playing a completely different game - fortune.com](https://fortune.com/2026/06/16/china-ai-deepseek-open-source-efficiency-global-expansion-strategy/)
   - 工具：tavily
   - 分数：0.17
   - 来源等级：C
   - 剔除原因：score 低于 0.4
14. [Machine learning-assisted high-speed combinatorial optimization with Ising machines for dynamically changing problems - Nature](https://www.nature.com/articles/s41467-026-73725-6)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：A
   - 剔除原因：score 低于 0.4
15. [Google DeepMind unveils a plan to protect itself from its own rogue AI agents - Fortune](https://fortune.com/2026/06/18/google-deepmind-unveils-plan-to-protect-itself-from-its-own-rogue-ai-agents/)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
16. [New AI optimization framework beats Claude Code and Codex by 2.5x on the same compute budget - VentureBeat](https://venturebeat.com/orchestration/new-ai-optimization-framework-beats-claude-code-and-codex-by-2-5x-on-the-same-compute-budget)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
17. [Ant Group 2025 Sustainability Report Highlights Record AI R&D Investment – Company Announcement - Financial Times](https://markets.ft.com/data/announce/detail?dockey=600-202606170512BIZWIRE_USPRX____20260617_BW847068-1)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
18. [From camera clarity to collision avoidance: What ‘AI in mining’ actually looks like in 2026 - Mining Technology](https://www.mining-technology.com/sponsored/from-camera-clarity-to-collision-avoidance-what-ai-in-mining-actually-looks-like-in-2026/)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
19. [Deep learning-based pattern classification for embroidery in Asia: evidence from Kazakh and Kyrgyz patterns - Nature](https://www.nature.com/articles/s40494-026-02714-1)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：A
   - 剔除原因：score 低于 0.4
20. [EBAday 2026: Zooming in on AI and digital assets as the key themes of the event - Finextra Research](https://www.finextra.com/newsarticle/47948/ebaday-2026-zooming-in-on-ai-and-digital-assets-as-the-key-themes-of-the-event)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
21. [The $250 Million Lesson: How Apple Changed the Way It Showcased AI at the Developers Conference - آي-فون إسلام](https://iphoneislam.com/language/en/2026/06/the-250-million-lesson-how-apple-changed-the-way-it-showcased-ai-at-the-developers-conference/168178)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
22. [12 creative campaigns to know about today - Ad Age](https://adage.com/creativity/work/aa-creative-ads-today-claires-doordash-hersheys-orkin-pedigree-postmates-smithsonian-zillow/)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
23. [激发LLM涌现——提示工程 - 李乾坤的博客](https://qiankunli.github.io/2023/10/29/llm_prompt.html)
   - 工具：tavily
   - 分数：0.44
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
24. [modelscope-classroom/LLM-tutorial/C.提示词工程-prompt engineering.md at main · modelscope/modelscope-classroom · GitHub](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md)
   - 工具：tavily
   - 分数：0.48
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
25. [充分释放大模型的潜力——提示词工程的16 种方式 - AWS](https://aws.amazon.com/cn/blogs/china/sixteen-ways-of-prompt-engineering)
   - 工具：tavily
   - 分数：0.43
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
26. [文生文Prompt指南 - 阿里云帮助文档](https://help.aliyun.com/zh/model-studio/prompt-engineering-guide)
   - 工具：tavily
   - 分数：0.42
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
27. [高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.39
   - 来源等级：C
   - 剔除原因：score 低于 0.4
28. [少样本提示 | Prompt Engineering Guide<!-- -->](https://www.promptingguide.ai/zh/techniques/fewshot)
   - 工具：tavily
   - 分数：0.36
   - 来源等级：C
   - 剔除原因：score 低于 0.4
29. [南京招标投标协会](http://www.njzbtb.com/Info.aspx?ClassCode=011014002&InforGuid=20250324112556f51f8a48-a1c6-46df-87c7-3a0e6c130db8)
   - 工具：tavily
   - 分数：0.34
   - 来源等级：C
   - 剔除原因：score 低于 0.4
30. [2.5 智能体提示词工程 | 智能体AI 权威指南 | Agentic AI Guide](https://yeasy.gitbook.io/agentic_ai_guide/di-yi-bu-fen-dan-ti-zhi-neng-jia-gou/02_reasoning/2.5_prompt_engineering)
   - 工具：tavily
   - 分数：0.28
   - 来源等级：C
   - 剔除原因：score 低于 0.4
31. [C.提示词工程-prompt engineering.md - GitHub](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md)
   - 工具：tavily
   - 分数：0.45
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
32. [文生文Prompt指南 - 阿里云帮助文档](https://help.aliyun.com/zh/model-studio/prompt-engineering-guide)
   - 工具：tavily
   - 分数：0.43
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
33. [充分释放大模型的潜力——提示词工程的16 种方式 - AWS](https://aws.amazon.com/cn/blogs/china/sixteen-ways-of-prompt-engineering)
   - 工具：tavily
   - 分数：0.43
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
34. [[PDF] 大模型上下文工程指南](https://www.cdut.edu.cn/__local/4/A7/81/EA807C0CAAAF77FDAC03EC61C0B_FF6614F6_68E2A6.pdf)
   - 工具：tavily
   - 分数：0.39
   - 来源等级：C
   - 剔除原因：score 低于 0.4
35. [高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.38
   - 来源等级：C
   - 剔除原因：score 低于 0.4
36. [[PDF] 大语言模型检索增强生成优化技术研究综述](http://cjc.ict.ac.cn/online/onlinepaper/008_yl-2026227143149.pdf)
   - 工具：tavily
   - 分数：0.35
   - 来源等级：C
   - 剔除原因：score 低于 0.4
37. [[PDF] Agentic Design Patterns - Jimmy Song](https://assets.jimmysong.io/books/agentic-design-patterns-zh-20251011.pdf)
   - 工具：tavily
   - 分数：0.30
   - 来源等级：C
   - 剔除原因：score 低于 0.4
38. [[PDF] 面向工程审计行业的DeepSeek 大模型应用指南](https://sea.nau.edu.cn/_upload/article/files/9f/48/0664056241d39174c060c10d3ec7/84a746e6-c8d1-4869-bd9e-246aa117040f.pdf)
   - 工具：tavily
   - 分数：0.25
   - 来源等级：C
   - 剔除原因：score 低于 0.4
39. [生成式人工智能技术在招标采购行业的应用及趋势2025-03-24](http://www.njzbtb.com/Info.aspx?ClassCode=011014002&InforGuid=20250324112556f51f8a48-a1c6-46df-87c7-3a0e6c130db8)
   - 工具：tavily
   - 分数：0.24
   - 来源等级：C
   - 剔除原因：score 低于 0.4
40. [2.5 智能体提示词工程| 智能体AI 权威指南| Agentic AI Guide](https://yeasy.gitbook.io/agentic_ai_guide/di-yi-bu-fen-dan-ti-zhi-neng-jia-gou/02_reasoning/2.5_prompt_engineering)
   - 工具：tavily
   - 分数：0.23
   - 来源等级：C
   - 剔除原因：score 低于 0.4

## 完整精读结果

### 来源 1: 提示工程（prompt engineering)：技术分类与提示词调优看这篇就够了 - 文章 - 开发者社区 - 火山引擎

- URL: https://developer.volcengine.com/articles/7387978567193526308
- 精读方法：firecrawl-scrape

[![](https://lf3-static.bytednsdoc.com/obj/eden-cn/nulopslf/developer/community_logo.svg)](https://developer.volcengine.com/)

[文档](https://www.volcengine.com/docs) [备案](https://www.volcengine.com/beian) [控制台](https://console.volcengine.com/home)

[登录](https://console.volcengine.com/auth/login?redirectURI=https%3A%2F%2Fdeveloper.volcengine.com%2Farticles%2F7387978567193526308) [免费开始使用](https://console.volcengine.com/auth/signup?redirectURI=https%3A%2F%2Fdeveloper.volcengine.com%2Farticles%2F7387978567193526308)

[免费注册](https://console.volcengine.com/auth/signup?redirectURI=https%3A%2F%2Fdeveloper.volcengine.com%2Farticles%2F7387978567193526308) [登录](https://console.volcengine.com/auth/login?redirectURI=https%3A%2F%2Fdeveloper.volcengine.com%2Farticles%2F7387978567193526308)

![](<Base64-Image-Removed>)

[首页](https://developer.volcengine.com/) [![AI 大模型体验中心](<Base64-Image-Removed>)![AI 大模型体验中心](<Base64-Image-Removed>)AI 大模型体验中心](https://exp.volcengine.com/) [![动手实验室](<Base64-Image-Removed>)![动手实验室](<Base64-Image-Removed>)动手实验室](https://developer.volcengine.com/handsonlab) [![Agent 评测集](<Base64-Image-Removed>)![Agent 评测集](<Base64-Image-Removed>)Agent 评测集](https://developer.volcengine.com/evaluation-set) [![AI 案例广场](<Base64-Image-Removed>)![AI 案例广场](<Base64-Image-Removed>)AI 案例广场](https://developer.volcengine.com/aigcplaza) [火山杯大赛](https://developer.volcengine.com/competition) [学习中心](https://developer.volcengine.com/learning)

社区

![](<Base64-Image-Removed>)

去发布

2026春季Force火热报名中！

立即报名

![](<Base64-Image-Removed>)

[首页](https://developer.volcengine.com/) [![AI 大模型体验中心](<Base64-Image-Removed>)![AI 大模型体验中心](<Base64-Image-Removed>)AI 大模型体验中心](https://exp.volcengine.com/) [![动手实验室](<Base64-Image-Removed>)![动手实验室](<Base64-Image-Removed>)动手实验室](https://developer.volcengine.com/handsonlab) [![Agent 评测集](<Base64-Image-Removed>)![Agent 评测集](<Base64-Image-Removed>)Agent 评测集](https://developer.volcengine.com/evaluation-set) [![AI 案例广场](<Base64-Image-Removed>)![AI 案例广场](<Base64-Image-Removed>)AI 案例广场](https://developer.volcengine.com/aigcplaza) [学习中心](https://developer.volcengine.com/learning)

社区

提示工程（prompt engineering)：技术分类与提示词调优看这篇就够了

前言

01如何训练提示词模型来生成爆款文案

02翻译时如何用好提示词来告别机翻感

提示工程： 技术分类与提示调优

常见规则

分类

单一提示技术

多重提示技术

定向刺激提示（DSP）

结合外部工具的大型语言模型框架

提示调整和评估

总结

声明

References

评论区

# 提示工程（prompt engineering)：技术分类与提示词调优看这篇就够了

[![山行AI](https://p26-passport.byteacctimg.com/img/user-avatar/531574f0b34bc77490a4eb54a48325f8~300x300.image)\\
\\
山行AI](https://developer.volcengine.com/user/2417169195086699)

2024-07-04

[技术](https://developer.volcengine.com/articles?category=7311217583025717258)

技术

![](https://portal.volccdn.com/obj/volcfe-scm/deploy/volc_developer_/42325/static/image/rec-product.424eb1f0.png)

多云安全平台

[了解详情](https://www.volcengine.com/product/cspm?utm_campaign=20241107&utm_content=allproduct&utm_medium=in_banner&utm_source=community&utm_term=guanggaowei)

火山引擎旗下多云安全管理平台，统一管理资产、服务、事件、身份四个安全要素，为企业提供一站式安全运营、安全运维、安全数据共享能力。

前言

在人工智能盛起的当下，出现了一个新兴的行业——提示工程(prompt engineering)。提示词，简言之，就是我们和AI说的话。在人机交互模式下，一个好的提示词，往往能产生事半功倍的效果。文本领域，好的提示词往往能超越RAG/Agent所能发挥的能力；图片对应的视觉领域，好的提示词往往能产生更好地图片/视觉效果。

在山行AI的视频号上有两个关于提示词的视频很好地说明了这一点，感兴趣的小伙伴不妨一观（顺便帮忙点个关注❤️-\_-❤️，很分感谢～)：

PS：可能看了本文之后，你对于提示词的理解就能超过别人很多啦～

### 01如何训练提示词模型来生成爆款文案

### 02翻译时如何用好提示词来告别机翻感

提示工程：
技术分类与提示调优

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/51008da902ae479798ebd729803a7c91~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=ZPA6eveBkUGsGOeT6I3KFCQ%2BAUk%3D)

作为一个新兴的研究领域，提示工程(prompt engineering)缺乏明确的技术分类。当你浏览不同的文章和网站讨论这些技术时，你会发现它们各不相同且缺乏结构。由于这种混乱，从业者往往只坚持使用最简单的方法。在这篇文章中，我提出了一个对提示工程技术的概览和清晰的分类，这将帮助你把握它们的概念并在你的应用程序中有效使用它们。此外，我还将讨论将提示工程作为一个涉及提示调整(prompt tuning)和评估的数据科学过程。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/3ad692aa51cc4799b03bf1e60d103e8f~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=ESNjUsvnxjJ6xsrUsOJnB6Qo1dw%3D)

尽管许多研究者付出了努力，大型语言模型仍然面临一些问题。它们的主要陷阱有：

• **引用资源。** 大型语言模型（LLMs）可以生成看似非常可信并引用外部资源的内容，但重要的是要记住，它们不能引用资源，它们既没有访问互联网的权限，
• **偏见。** LLMs在它们的回应中可能表现出偏见，常常生成刻板印象或有偏见的内容，
• **幻觉。** 当LLMs被问到它们不知道答案的问题时，有时可以“幻觉”或生成虚假信息，
• **数学和常识问题。** 尽管它们有先进的能力，LLMs常常在解决即使是最简单的数学或常识问题时遇到困难，
• **提示劫持** 。LLMs可以被用户操纵或“黑客攻击”，以忽略开发者的指令并生成特定内容。

大多数的提示工程技术解决了两个问题：幻觉和解决数学及常识任务。有特定的技术旨在减轻提示劫持，但这是一个单独讨论的话题。

**常见规则**

在讨论具体技术之前，让我们谈谈提示的常见规则，这将帮助你写出清晰和具体的指令：

1.准确地说明要做什么（写作、总结、提取信息），
2.避免说明不要做什么，而是说明要做什么，
3.具体一点：不要说“用几句话”，而是说“用2-3句话”，
4.添加标签或分隔符来构造提示，
5.如果需要，要求结构化输出（JSON、HTML），
6.要求模型验证是否满足条件（例如，“如果你不知道答案，就说‘没有信息’”），
7.要求模型先解释然后再提供答案（否则模型可能试图为错误的答案辩解）。

分类

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/51008da902ae479798ebd729803a7c91~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=ZPA6eveBkUGsGOeT6I3KFCQ%2BAUk%3D)

目前的大多数技术可以分为三组：

• **单一提示技术** 旨在优化对一个提示的响应，
•接下来是 **结合几个提示** 的技术。它们的共同理念是多次查询模型（或多个模型）以解决任务，
•最后，有一组方法将大型语言模型 **与外部工具结合** 使用。

单一提示技术

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/4f5cdf4652e844d5b59dc07fb120ca36~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=QI9XZuwfAll0GdO5L8UBsZopRJ0%3D)

哪些技术旨在通过单个提示解决你的任务？

•零次学习（Zero-Shot），
•少次学习（Few-Shot），
•思维链（Chain of Thought），
•程序辅助语言（Program Aided Language）。

我们来逐一研究它们。

**零次提示（Zero-Shot Prompting）**

这是最简单的技术，使用自然语言指令。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/ae3795f8ab214f85b046b90d71aa468a~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=tQBTQDint19V48eQf9cYpl%2BPpbE%3D)

单次学习。示例来自 promptingguide.ai\[1\]

**少次提示（Few-Shot Prompting）**

大型语言模型（LLMs）在单次学习方面表现非常出色，但它们仍可能在复杂的任务上失败。少次学习的理念是向模型演示带有正确答案的类似任务（Brown et al. (2020)\[2\]）。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/8d594e060a934d97a94af472e80143d9~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=CyVWprgvUj%2FFy5cyNBhoiOH09ZA%3D)

少次学习。示例来自 promptingguide.ai\[3\]

在 Min et al. (2022)\[4\] 的论文中，研究表明在一系列分类和多选任务中，示范中标签的不正确几乎不会影响性能。相反，确保示范提供标签空间的少数几个示例、输入测试的分布以及序列的整体格式是至关重要的。

**思维链提示（Chain of Thought Prompting, CoT）**

思维链提示通过中间推理步骤实现复杂的推理能力。这项技术的目标是使模型迭代并对每一步进行推理。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/194e954356d649a4acf188c3998e7910~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=MfgCTaQtmjF3uT6TGzYqynjLnzA%3D)

零次学习、少次学习和思维链提示技术。示例来自 Kojima et al. (2022)\[5\]。

思维链提示可以与零次学习或少次学习一起使用。零次思维链提示的概念是建议模型一步一步地思考，以得出解决方案。这种方法的作者(Kojima et al. (2022)\[6\])展示了零次思维链提示在算术、符号和其他逻辑推理任务上的性能显著超过了零次学习的大型语言模型（LLM）的表现。

如果你选择少次思维链提示，你必须确保有包含解释的多样化示例(Wei et al. (2022)\[7\])。这种方法在算术、常识和符号推理任务上具有惊人的实证增益。

**程序辅助的语言模型（Program-Aided Language Models, PAL）**

程序辅助的语言模型是一种扩展思维链提示的方法，通过将解释扩展为带有代码的自然语言(Gao et al. (2022)\[8\])。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/3feb9ffc98a44963b6302e59c84d17de~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=m0bE77tCFnpk8FylAgzSw8kORYA%3D)

程序辅助语言提示。示例来自 Gao et al. (2022)\[9\]。

这一技术可以使用 LangChain PALChain\[10\] 类来实施。

多重提示技术

下一组提示基于结合一个或几个模型的提示的不同策略：

1. **投票。** 这个想法是通过投票得到正确答案。技术：自我一致性。
2. **分而治之。** 这组提示基于将复杂任务分解为几个提示。技术：方向刺激、生成知识、提示链、表格链和由少到多的提示。
3. **自我评估。** 这种方法建议在框架中加入检查输出是否符合指示的步骤。技术：反思、思维树。

**自我一致性（Self Consistency, SC）**

自我一致性基于这样的直觉：“一个复杂的推理问题通常有多种不同的思考方式，导致其唯一正确的答案”（Wang et al. (2022)\[11\]）。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/28bb5e6014fc42fd8fe8051eb697ad74~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=5R2eU3cx1Btwjg6y6gBCl3FPJyQ%3D)

它多次提出相同的思维链提示，从而生成一组多样化的推理路径，然后通过应用投票选择最一致的答案。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/423b09ce8c934e6d80261e481b2aab6b~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=Kajkyo8k2UedR%2Bgxm7Wk2UW8FU4%3D)

自我一致性提示技术示例，源自Wang et al. (2022)\[12\]

在Wang et al. (2022)\[13\]的研究中，应用自我一致性技术对算术和常识任务的提升，在常见基准测试中为4%–18%。

## 定向刺激提示（DSP）

结合提示的下一个概念是“分而治之”。在DSP中，我们有两个步骤：生成刺激（例如，关键词）并使用它们来提高响应的质量。

定向刺激提示在Li et al. (2023)\[14\]提出，用于摘要生成、对话响应生成和思维链推理任务。它包含两个模型：

•训练一个小型可调策略语言模型（LM）来生成刺激（提示），
•使用一个黑盒冻结的大型语言模型（LM）根据问题和上一步的刺激生成摘要。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/76888ea1469c4e378589ee7c5159f4f6~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=lWGNMIuxY5%2FX4NxdMyhtnY0m27c%3D)

策略模型可以通过使用标记数据的监督式微调和基于大型语言模型（LLM）输出的离线或在线奖励进行强化学习来进行优化，例如：

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/01805de402654954a5d477d712d9f532~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=r2ub2IV6bOE62aRsfsDzNjA0%2BZY%3D)

DSP框架 Li et al. (2023)\[15\] 我们学习一个小型的可调策略模型来生成定向刺激（在这种情况下是关键词），它为大型语言模型（LLM）提供了针对特定输入的指导，以达到预期的目标。

**生成知识提示（GK）**

在“分而治之”概念下的下一个提示技术是在 Liu et al. (2022)\[16\] 提出的生成知识。其思想是先使用一个单独的提示来生成知识，然后利用这些知识来获得更好的响应。

生成知识提示包括两个阶段：

• **知识生成** ：使用少量样本演示从语言模型中生成与问题相关的知识陈述，
• **知识整合** ：使用第二个语言模型与每个知识陈述一起进行预测，然后选择最高置信度的预测。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/3e6e8602cb0344839ac60eec116a5729~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=RFa4wxmp7%2F%2Bbj9oqXiTe7aNj9yk%3D)

这种方法不需要对知识整合的特定任务的监督，也不需要访问结构化的知识库，但它提高了大型、最先进模型在常识推理任务上的性能。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/2847ef91adda497db61169885c697c11~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=7WaPlVVHoZdBGOup0IJ7h65Nv%2Fk%3D)

来自 Liu et al. (2022)\[17\] 的知识生成小样本提示示例，用于QASC

**提示链接**

提示链接是一种简单而强大的技术，你应该将任务分解为子问题，并依次用这些子问题提示模型。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/16b7ca461d344dccbfdac26a99ca0e28~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=Vo6yK%2BoVS%2FdmcSXrfSOo2rP%2Bnc0%3D)

提示链接对于完成一个大型语言模型（LLM）可能难以应对的复杂任务非常有用，特别是当这些任务伴随着非常详细的提示时。它还有助于提高大型语言模型应用的透明度，增强可控性和可靠性。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/72c26744365c44e392fbb72ff905a8a9~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=PEgq3boZRMw0u1dQ7aeIH6572TE%3D)

提示链接示例来自 txt.cohere.com\[18\]

**从简到繁的提示**

从简到繁的提示方法更进了一步，增加了一个步骤，即模型需要决定如何将你的任务分解成子问题。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/b67dab1b0d404855adca9c32372e2432~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=VBNDHFLL5OONnnp5bLMmfd%2FDmAI%3D)

Zhou et al. (2022)\[19\] 中的实验结果揭示，从简到繁的提示方法在与符号操作、组合泛化和数学推理相关的任务上表现良好。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/e495939122cc4f07a1f11bcca3d76db9~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=ifneLqZMLyMR22cAwJG0fldktfI%3D)

Zhou et al. (2022)\[20\] 中的从简到繁提示的例子

**连锁表格提示**

在最近的研究 (Wang et al. (2024)\[21\]) 中提出了一种新方法，其中表格数据被明确用作推理链中的中间思考的代理。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/b93e3d15eb034b979e91aee9ca8d9bb0~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=8JHTrZp7stMdiCvHWTyvNc7W%2F1A%3D)

该算法包括两个步骤的循环：

1. **动态规划** ，在此过程中，大型语言模型（LLM）根据输入查询和以前操作的历史（操作链）从操作池中抽取下一个操作，
2. **参数生成** ，涉及使用大型语言模型（LLM）为上一步骤选定的操作生成参数（例如新的列名），并应用编程语言来执行操作并创建相应的中间表格。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/aca147a03c824170b484d74088e17f87~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=sOCetV7H3sKjgsb9j4nRWRFvBJ4%3D)

来自Wang et al. (2024)\[22\]的连锁思考提示的示例和比较。

接下来的两种方法实现了自检（Self-Check）的概念 —— 框架中有一个步骤来检查解决方案。连锁表格（Cgain-of-Table）实现的示例可以在此链接\[23\]找到。

**思维树（Tree of Thoughts，ToT）**

思维树在连锁思考方法的基础上进行泛化，允许模型探索多个推理步骤并自我评估选择。

要实现ToT技术，我们必须决定四个问题：

1.如何将中间过程分解为思考步骤，
2.如何从每个状态生成潜在的思考点，
3.如何启发式地评估状态（使用状态评估提示），
4.使用什么搜索算法（Yao et al. (2023)\[24\]）。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/9cf93e71705747edbbd139a40f840513~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=83tGdlnDR9QD2EHke%2Bhys1A4NKg%3D)

**输入提示** 必须包括解决问题的中间步骤的描述，以及抽取的思考点或关于生成它们的指令。 **状态评估提示** 必须提供关于选择哪些提示进行下一步的指令。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/6a57fd4627d1419da2b761a43237a62d~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=VpFH%2FrP%2BJM5ogxuLCRBvAKsYG18%3D)

【思维树在24点游戏中的例子】摘自Yao et al. (2023)\[25\]

Yao et al. (2023)\[26\]的实验显示，对于需要复杂规划或搜索的任务，思维树技术（ToT）非常成功。LangChain 实现了思维树技术，在 langchain\_experimental.tot.base.ToTChain 类\[27\]中有所体现。

**反思**

反思是一个通过语言反馈加强语言代理的框架。反思代理通过对任务反馈信号进行口头反思，然后在情节记忆缓冲区中保持自己的反思文本，以在后续试验中促进更好的决策（Shinn et al. (2023)\[28\]）。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/d2c5072a9bd94be7830ed46bb5ca64cb~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=0KV4Xu3q9kvpfBGzAjRVopNJuZI%3D)

来自 Shinn et al. (2023)\[29\] 的反思框架图解

反思框架由三个不同的模型组成：

• **执行者（Actor）** ：一个基于状态观察生成文本和行动的大型语言模型（使用CoT和ReAct技术），
• **评估者（Evaluator）** ：一个对执行者产生的输出进行评分的大型语言模型，
• **自我反思（Self-Reflection）** ：一个生成口头强化提示以协助执行者自我提升的大型语言模型。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/8b426035493048dca7fa970206d847cb~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=6qnkxUvH6DLCL1gYHLtwJbtaXaI%3D)

来自 Shinn et al. (2023)\[30\] 的不同任务中的反思示例

反思在需要顺序决策、编程、语言推理的任务中表现良好。

请通过此链接\[31\]查看实现。

结合外部工具的大型语言模型框架

在本节中，我将介绍两种方法 —— 检索增强生成和ReAct。

**检索增强生成（Retrieval-Augmented Generation, RAG）**

RAG将信息检索组件与文本生成模型结合起来：

• **检索** 。在检索步骤中，系统通常使用向量搜索寻找可能回答问题的相关文档，
• **生成** 。接下来，将相关文档作为上下文连同初始问题传递给一个大型语言模型（Lewis et al. (2021)\[32\]）。

在大多数情况下，使用RAG-序列方法，意味着我们检索 **k** 篇文档，并使用它们生成回答用户查询的所有输出标记。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/f1cf2dee1615484e862d495037282155~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=oxyI6TBv450W2MwOHg6Cqqix0MU%3D)

在RAG中，语言模型可以进行微调，但实际上这种做法很少见，因为预训练的大型语言模型已经足够好，可以直接使用，而自行进行微调成本过高。此外，RAG中的内部知识可以以高效的方式修改，而无需重新训练整个模型。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/5aad88bd88c64d40865ecfb03a523b32~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=1LCkqlJi07%2FiTQVoBPlVFVzdEh0%3D)

RAG生成的响应更具事实性、具体性和多样性，有助于提高事实验证的结果。

**ReAct**

Yao等人（2022）\[33\] 提出了一个名为ReAct的框架，其中大型语言模型被用来以交错的方式生成 **推理迹象** 和 **任务特定** 的行动：推理迹象帮助模型引导、跟踪和更新行动计划，以及处理异常，而行动则使其能够与外部来源（如知识库或环境）接口并收集额外信息。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/17994a26018744a2aceb0a08f3d7d802~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=RcDLZJB0xSuPvoyiuwAi%2Bk6yaog%3D)

ReAct框架可以选择一个可用的工具（例如搜索引擎、计算器、SQL代理），应用它并分析结果以决定下一步行动。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/4c44e4810956453ca0207c66b129f4db~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=zlJI0mubDEf8Ji8Q%2FmeahhBmoFI%3D)

ReAct案例（引自Yao等人（2022年）\[34\]）

通过与简单的Wikipedia API交互，ReAct解决了在连贯思维推理中普遍存在的幻觉和错误传播问题，并生成了类似人类解决任务的轨迹，这些轨迹比没有推理痕迹的基线模型更易于解释（Yao等人（2022年）\[35\]）。

查看Langchain工具实现的ReAct案例\[36\]。

提示调整和评估

选择提示工程技术在很大程度上取决于您的LLM的应用和可用资源。如果您曾经尝试过提示，您知道大型语言模型对人类生成的提示中最微小的变化非常敏感，这些提示往往是次优的且通常具有主观性。

无论您选择哪种提示技术，如果您正在构建一个应用程序，将提示工程视为一个数据科学过程是非常重要的。这意味着创建一个测试集，选择指标，调整提示，并评估其对测试集的影响。

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/c8fa26bae682400ebaee99bb30d2b7d5~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=O3dwueDaaaBjXxsfRvK3KnNxfRM%3D)

测试提示的指标在很大程度上将取决于应用程序，但以下是一些指南（来自数据科学峰会2023\[37\]）：

![picture.image](https://p6-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/19fb1b142cdf4cc4b668e9cd4d375417~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782119126&x-signature=Q15%2By4TaaI1yocanbeoA%2FxyhFjE%3D)

测试提示的指标（摘自数据科学峰会2023\[38\]）

1. **忠实度和相关性** ：•生成答案的事实准确性如何，•生成答案与问题的相关性如何。
2. **检索** — 主要用于RAG和ReAct管道，但也可以应用于生成的知识及方向性刺激提示：•精确度 — 检索到的文档的相关性有多高，•召回率 — 是否检索到了所有相关文档。
3. **内部思考** ：•代理和工具选择的准确性 — 用于ReAct，•工具参数提取 — 是否从上下文中正确检索到参数，并进行了恰当的转换 — 用于ReAct，•在长轮对话中记住事实 — 用于ReAct，•正确的逻辑步骤 — 用于ReAct和思维链提示。
4. **非功能性** ：•答案的风格和语调，•缺乏偏见，•合规和安全检查，•提示注入测试。

根据您的用例，选择指标并跟踪提示更改对测试集的影响，确保任何更改不会降低响应的质量。

总结

我不敢说已经涵盖了所有现有技术 — 它们太多了，不久的将来有人可能会出版一本完整的教科书。但如果你读到这里，你会注意到所有技术的概念都相当普遍且直观。我可以将所有写好提示的规则总结为一个简短的清单：

1.清晰而准确，以便模型不必猜测你的意图，
2.使用分隔符或标签增加结构，
3.通过展示示例和添加解释来帮助模型，
4.要求模型迭代思考，解释其解决方案，
5.如果提示复杂，考虑将其分解为子任务，
6.尝试多次询问相同的提示，
7.考虑增加模型自检的步骤，
8.如有需要，将您的LLM与外部工具结合使用，
9.将提示调整视为一个迭代且需要评估的数据科学过程。

就是这样！感谢您阅读到这里，祝您提示愉快！

声明

本文由山行翻译整理自： [https://medium.com/@kate.ruksha/prompt-engineering-classification-of-techniques-and-prompt-tuning-6d4247b9b64c，如果对您有帮助，请帮忙点赞、关注、收藏，谢谢～](https://medium.com/@kate.ruksha/prompt-engineering-classification-of-techniques-and-prompt-tuning-6d4247b9b64c%EF%BC%8C%E5%A6%82%E6%9E%9C%E5%AF%B9%E6%82%A8%E6%9C%89%E5%B8%AE%E5%8A%A9%EF%BC%8C%E8%AF%B7%E5%B8%AE%E5%BF%99%E7%82%B9%E8%B5%9E%E3%80%81%E5%85%B3%E6%B3%A8%E3%80%81%E6%94%B6%E8%97%8F%EF%BC%8C%E8%B0%A2%E8%B0%A2%EF%BD%9E)

### References

`[1]` promptingguide.ai: _[https://www.promptingguide.ai/techniques/fewshot](https://www.promptingguide.ai/techniques/fewshot)_

`[2]` Brown et al. (2020): _[https://arxiv.org/abs/2005.14165](https://arxiv.org/abs/2005.14165)_

`[3]` promptingguide.ai: _[https://www.promptingguide.ai/techniques/fewshot](https://www.promptingguide.ai/techniques/fewshot)_

`[4]` Min et al. (2022): _[https://arxiv.org/abs/2202.12837](https://arxiv.org/abs/2202.12837)_

`[5]` Kojima et al. (2022): _[https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)_

`[6]` Kojima et al. (2022): _[https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)_

`[7]` Wei et al. (2022): _[https://arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903)_

`[8]` Gao et al. (2022): _[https://arxiv.org/abs/2211.10435](https://arxiv.org/abs/2211.10435)_

`[9]` Gao et al. (2022): _[https://arxiv.org/abs/2211.10435](https://arxiv.org/abs/2211.10435)_

`[10]` LangChain PALChain: _[https://api.python.langchain.com/en/latest/pal\\\_chain/langchain\\\_experimental.pal\\\_chain.base.PALChain.html](https://api.python.langchain.com/en/latest/pal%5C_chain/langchain%5C_experimental.pal%5C_chain.base.PALChain.html)_

`[11]` Wang et al. (2022): _[https://arxiv.org/abs/2203.11171](https://arxiv.org/abs/2203.11171)_

`[12]` Wang et al. (2022): _[https://arxiv.org/abs/2203.11171](https://arxiv.org/abs/2203.11171)_

`[13]` Wang et al. (2022): _[https://arxiv.org/abs/2203.11171](https://arxiv.org/abs/2203.11171)_

`[14]` Li et al. (2023): _[https://arxiv.org/abs/2302.11520](https://arxiv.org/abs/2302.11520)_

`[15]` Li et al. (2023): _[https://arxiv.org/abs/2302.11520](https://arxiv.org/abs/2302.11520)_

`[16]` Liu et al. (2022): _[https://arxiv.org/pdf/2110.08387.pdf](https://arxiv.org/pdf/2110.08387.pdf)_

`[17]` Liu et al. (2022): _[https://arxiv.org/pdf/2110.08387.pdf](https://arxiv.org/pdf/2110.08387.pdf)_

`[18]` txt.cohere.com: _[https://txt.cohere.com/chaining-prompts/](https://txt.cohere.com/chaining-prompts/)_

`[19]` Zhou et al. (2022): _[https://arxiv.org/pdf/2205.10625.pdf](https://arxiv.org/pdf/2205.10625.pdf)_

`[20]` Zhou et al. (2022): _[https://arxiv.org/pdf/2205.10625.pdf](https://arxiv.org/pdf/2205.10625.pdf)_

`[21]` Wang et al. (2024): _[https://arxiv.org/pdf/2401.04398.pdf](https://arxiv.org/pdf/2401.04398.pdf)_

`[22]` Wang et al. (2024): _[https://arxiv.org/pdf/2401.04398.pdf](https://arxiv.org/pdf/2401.04398.pdf)_

`[23]` 此链接: _[https://github.com/run-llama/llama-hub/blob/main/llama\\\_hub/llama\\\_packs/tables/chain\\\_of\\\_table/chain\\\_of\\\_table.ipynb](https://github.com/run-llama/llama-hub/blob/main/llama%5C_hub/llama%5C_packs/tables/chain%5C_of%5C_table/chain%5C_of%5C_table.ipynb)_

`[24]` Yao et al. (2023): _[https://arxiv.org/abs/2305.10601](https://arxiv.org/abs/2305.10601)_

`[25]` Yao et al. (2023): _[https://arxiv.org/abs/2305.10601](https://arxiv.org/abs/2305.10601)_

`[26]` Yao et al. (2023): _[https://arxiv.org/abs/2305.10601](https://arxiv.org/abs/2305.10601)_

`[27]` langchain\_experimental.tot.base.ToTChain 类: _[https://api.python.langchain.com/en/latest/tot/langchain\\\_experimental.tot.base.ToTChain.html](https://api.python.langchain.com/en/latest/tot/langchain%5C_experimental.tot.base.ToTChain.html)_

`[28]` Shinn et al. (2023): _[https://arxiv.org/pdf/2303.11366.pdf](https://arxiv.org/pdf/2303.11366.pdf)_

`[29]` Shinn et al. (2023): _[https://arxiv.org/pdf/2303.11366.pdf](https://arxiv.org/pdf/2303.11366.pdf)_

`[30]` Shinn et al. (2023): _[https://arxiv.org/pdf/2303.11366.pdf](https://arxiv.org/pdf/2303.11366.pdf)_

`[31]` 此链接: _[https://github.com/noahshinn/reflexion](https://github.com/noahshinn/reflexion)_

`[32]` Lewis et al. (2021): _[https://arxiv.org/pdf/2005.11401.pdf](https://arxiv.org/pdf/2005.11401.pdf)_

`[33]` Yao等人（2022）: _[https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)_

`[34]` Yao等人（2022年）: _[https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)_

`[35]` Yao等人（2022年）: _[https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)_

`[36]` ReAct案例: _[https://python.langchain.com/docs/modules/agents/agent\\\_types/react/](https://python.langchain.com/docs/modules/agents/agent%5C_types/react/)_

`[37]` 数据科学峰会2023: _[http://dssconf.pl/](http://dssconf.pl/)_

`[38]` 数据科学峰会2023: _[http://dssconf.pl/](http://dssconf.pl/)_

1279

0

0

0

点赞评论收藏分享

关于作者

[![山行AI](https://p26-passport.byteacctimg.com/img/user-avatar/531574f0b34bc77490a4eb54a48325f8~300x300.image)](https://developer.volcengine.com/user/2417169195086699)

[山行AI](https://developer.volcengine.com/user/2417169195086699)

关注

关于作者

[![山行AI](https://p26-passport.byteacctimg.com/img/user-avatar/531574f0b34bc77490a4eb54a48325f8~300x300.image)](https://developer.volcengine.com/user/2417169195086699)

[山行AI](https://developer.volcengine.com/user/2417169195086699)

文章

200K

获赞

3

收藏

6

关注

[QuantDinger—开源的本地量化平台](https://developer.volcengine.com/articles/7591389863157432370) [为claude code创建skills](https://developer.volcengine.com/articles/7587309078734389298) [如何使用BMad 打造AI超级个体](https://developer.volcengine.com/articles/7582491269004918803)

相关资源

字节跳动 NoSQL 的实践与探索

随着 NoSQL 的蓬勃发展越来越多的数据存储在了 NoSQL 系统中，并且 NoSQL 和 RDBMS 的界限越来越模糊，各种不同的专用 NoSQL 系统不停涌现，各具特色，形态不一。本次主要分享字节跳动内部和火山引擎 NoSQL 的实践，希望能够给大家一定的启发。

点击下载

相关产品

多云安全平台

火山引擎旗下多云安全管理平台，统一管理资产、服务、事件、身份四个安全要素，为企业提供一站式安全运营、安全运维、安全数据共享能力。

[了解详情](https://www.volcengine.com/product/cspm?utm_campaign=20241107&utm_content=allproduct&utm_medium=in_banner&utm_source=community&utm_term=guanggaowei)

大数据文件存储

大数据文件存储，支持HDFS语义，提供数据加速，多模式支持等能力

[了解详情](https://www.volcengine.com/product/cfs?utm_campaign=20241107&utm_content=allproduct&utm_medium=in_banner&utm_source=community&utm_term=guanggaowei)

混合云 veStack

基于云原生的自研混合云平台，与火山引擎公有云采用统一架构，高效智能

[了解详情](https://www.volcengine.com/product/veStack?utm_campaign=20241107&utm_content=allproduct&utm_medium=in_banner&utm_source=community&utm_term=guanggaowei)

推荐阅读

[影刀RPA完全指南：应用发布与分享流程——发版→分享→市场→客户使用\\
\\
2026-06-13](https://developer.volcengine.com/articles/7650830404576149558) [2026 免费行情数据 API 接入指南（Python/Java）\\
\\
2026-06-09](https://developer.volcengine.com/articles/7649579685030854665) [影刀RPA进阶教程：魔法指令3.0完整指南——对话式生成流程与免写XPath\\
\\
2026-06-14](https://developer.volcengine.com/articles/7650936211049021476) [2026酒店智能化趋势：AI+IoT+节能三大方向\\
\\
2026-06-11](https://developer.volcengine.com/articles/7649829194016227347) [基于行情 API 实现加密货币 24 小时涨跌幅实时采集（Python 实战）\\
\\
2026-06-11](https://developer.volcengine.com/articles/7650010044805120050)

评论

未登录

看完啦，登录分享一下感受吧～

暂无评论

售前客服

售后客服

购买咨询

业务咨询

### 来源 2: prompt提示词和prompt-engineering提示词工程基础学习 - 九卷 - 博客园

- URL: https://www.cnblogs.com/jiujuan/p/19855636
- 精读方法：firecrawl-scrape

# [prompt提示词和prompt-engineering提示词工程基础学习](https://www.cnblogs.com/jiujuan/p/19855636 "发布于 2026-04-12 15:58")

[合集 \- AI.大模型(8)](https://www.cnblogs.com/jiujuan/collections/25687)

[1.普通人财富积累的逻辑路径是什么？有哪些阶段？每个有什么困难困难？... ... AI大模型DeepSeek R1的震惊回答！2025-02-18](https://www.cnblogs.com/jiujuan/p/18717541) [2.LLM 大模型发展简史2025-03-05](https://www.cnblogs.com/jiujuan/p/18752957) [3.LLM大模型技术基础知识学习04-01](https://www.cnblogs.com/jiujuan/p/19808460) [4.LLM大模型中AI-Agent智能体应用开发相关知识介绍04-10](https://www.cnblogs.com/jiujuan/p/19848128)

5.prompt提示词和prompt-engineering提示词工程基础学习04-12

[6.AI Agent上下文工程(context engineering)知识学习总结04-12](https://www.cnblogs.com/jiujuan/p/19855674) [7.LLM大模型技术相关的40个重要概念解释04-12](https://www.cnblogs.com/jiujuan/p/19855730) [8.100多行代码实现一个最简单的Agent(用ReAct)04-13](https://www.cnblogs.com/jiujuan/p/19859793)

收起

LLM大模型和Agent应用开发相关文章合集：

> [https://github.com/jiujuan/llm-agent-notebook](https://github.com/jiujuan/llm-agent-notebook)

## 一、什么是提示词 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#1708857053)

### 提示词是什么 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#1975321777)

提示词（Prompt）是人与大语言模型（LLM）进行沟通的桥梁和纽带。简单来说，提示词就是我们向 LLM 大模型输入的文本内容，告诉大模型我们要它做什么的具体指令。

在技术层面来看，提示词是触发模型生成响应的输入信息，它决定了模型输出的方向、质量和准确性。

要理解提示词的概念，可以将其比喻为一位知识渊博的专家（LLM大模型）请教问题，这位专家读过海量的书籍和资料，掌握了广泛的知识，但如果你不清晰地表达自己的问题，专家也很难给出准确的答案。提示词就是这个“表达问题”的过程——你表达得越清晰、越具体，获得的答案就越符合预期。

从技术角度分析，提示词的核心作用在于引导模型的注意力机制。大模型的 Transformer 架构中的注意力机制会让模型关注输入文本中与其当前处理位置相关的内容。当我们输入提示词时，模型会分析提示词中每个部分与最终输出的关联程度，从而决定生成什么样的内容。因此，提示词的质量直接决定了模型能否准确理解用户的意图，并生成有用的响应。

总而言之，提示词（Prompt） 是驱动 LLM 生成内容的唯一输入信号，LLM 的所有输出都严格基于提示词的上下文进行生成。

### 提示词与LLM的关系 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#1186722173)

提示词与 LLM 之间存在着一种共生依存的关系。一方面，LLM 的强大能力为提示词提供了发挥作用的舞台——正是由于模型经过了大规模预训练和微调，才能够理解各种形式的提示词并做出合理响应。另一方面，提示词的存在使得用户能够有效地调用 LLM 的能力，而无需关心模型内部的复杂机制。

这种关系可以类比为软件界面与程序功能的关系。就像图形用户界面（GUI）让用户能够通过点击按钮来操作复杂的程序一样，提示词充当了用户与LLM交互的界面角色。用户通过精心设计的提示词，可以引导模型完成从简单的问答到复杂的推理、从文本生成到代码编写等各种任务，而无需了解模型内部机制是如何工作的。这给普通用户的使用带来了极大方便。

提示词在 LLM 应用中的地位至关重要，这主要体现在三个方面：

- 第一，提示词是用户控制模型行为的唯一方式——模型的所有输出都是对提示词的响应，用户无法直接修改模型的内部参数。

- 第二，提示词的设计直接影响输出质量——同一个模型，给出不同的提示词可能产生截然不同的结果。

- 第三，提示词工程已经成为使用 LLM 的关键技能——掌握提示词工程可以让用户以极低的成本获得高质量的输出。

### 提示词工作原理 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#3526949303)

理解提示词的工作原理需要了解 LLM 的核心工作机制。LLM 本质上是基于概率的文本生成系统，它会对给定的输入序列预测下一个最可能出现的词，然后把这个词添加到序列末尾，继续预测下一个词，如此循环直到生成完整的回答。

当我们输入提示词时，这个过程就开始了。模型首先将提示词分词转换为 Token 序列，然后通过嵌入层将每个 Token 转换为向量表示。这些向量进入 Transformer 架构的处理流程，注意力机制会根据当前正在生成的位置，计算对输入序列中各个部分的关注程度，从而决定下一个词应该是什么。

提示词设计的关键在于影响这个注意力分配的过程。通过在提示词中强调某些信息、提供具体的格式要求、或者设定特定的上下文， 用户可以引导模型的注意力更多地集中在相关的内容上，从而影响输出结果。这就像是在给模型提供线索，帮助它更好地理解用户的意图并生成符合期望的回答。

上面解释比较技术性，下面给一个比较白话的解释：

> LLM 是基于海量文本预训练的自回归生成式模型，核心能力是根据输入的上下文，预测并生成最合理的下一个文本最小单位（Token），它的所有知识与能力都固化在预训练后的模型权重中，无自主意识，所有输出完全由输入的提示词驱动。

## 二、提示词的基本构成 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#3153814848)

### 提示词要素基本构成 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#2956126714)

提示词包含以下基本要素：

**指令**：想要模型执行的特定任务或指令。

**上下文**：包含外部信息或额外的上下文信息，引导语言模型更好地响应。

**输入数据**：用户输入的内容或问题。

**输出指示**：指定输出的类型或格式。

除了上面所提出的，所有能影响模型输出的输入内容，除背景上下文、核心指令、输入、输出外，还包括角色设定、参考资料、少样本示例、约束条件等全部前置输入文本。

### 指令：告诉模型做什么 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#4086498418)

指令（Instruction）是提示词中最核心的部分，它明确告诉模型用户希望完成什么任务。指令应该是清晰、具体、可执行的，让模型能够准确理解用户的期望。

你可以使用命令来指示模型执行各种简单任务，例如“写入”、“分类”、“总结”、“翻译”、“排序”等，从而为各种简单任务设计有效的提示。

指令的设计需要遵循几个原则：

- 首先，指令要明确具体。与其说“写一首诗”，不如说“写一首关于春天的七言绝句，要求押韵且意境优美”。

- 其次，指令要包含任务的关键要素，包括任务类型、具体要求、限制条件等。

- 第三，指令应该使用简洁的语言，避免可能引起歧义的表达。

常见的指令类型包括：

- **生成指令**（如“写一篇关于...的文章”）

- **分析指令**（如“分析这段话的情感倾向”）

- **转换指令**（如“把以下中文翻译成英文”）

- **总结指令**（如“用一句话概括以下内容”）

- **推理指令**（如“根据以下信息推理出正确答案”）

等等指令。

要写出合适的指令，还需要进行大量实验以找出最有效的方法。以不同的关键词（keywords），上下文（contexts）和数据（data）试验不同的指令（instruction），看看什么样是最适合你特定用例和任务的。通常，上下文越具体和跟任务越相关则效果越好。

### 上下文：提供背景信息 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#3977477749)

上下文（Context）为模型提供了理解任务所需的背景信息。好的上下文帮助模型在特定的领域或场景中给出更准确、更相关的回答。

上下文的作用体现在多个层面。

- 领域背景：可以帮助模型使用正确的专业术语和表达方式——例如，在医学问答中提供相关的病例信息，可以帮助模型做出更准确的诊断建议。

- 对话历史：让模型能够理解多轮对话的连贯性——在聊天场景中，模型需要知道之前讨论了什么，才能做出恰当的回应。

- 参考材料：可以为模型提供具体的信息来源——在问答时提供相关的文档片段，可以提高答案的准确性。

上下文并非越多越好。过长的上下文会增加模型的计算负担，可能导致关键信息被稀释，而且可能触发模型的懒政——模型可能过于依赖上下文而减少了自己的推理。因此，上下文应该经过精心筛选，只保留与当前任务最相关的信息。

### 输入数据：需要处理的内容 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#2078381797)

输入数据（Input Data）是提示词中需要模型处理的具体内容。这部分内容可能是需要翻译的文本、等待分析的数据、等待修改的代码，或者是任何需要模型进行处理的对象。输入数据的呈现方式会影响处理效果。

- 格式清晰：输入数据格式清晰更容易被模型正确理解——例如，将需要分析的文章段落用引号括起来，将需要翻译的句子单独放置。

- 结构化：数据结构化呈现可以帮助模型更好地理解复杂信息——如使用列表、表格等形式来组织数据。

- 标识边界：输入数据的边界也很重要——可以使用“以下是需要处理的内容：”、“输入：”等提示词来明确区分输入数据和其他部分。

### 输出格式：期望的响应形式 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#1377724315)

输出格式（Output Format）指定了用户期望的响应形式和结构。虽然这是可选项，但明确输出格式可以大大提高结果的可用性。

常见的输出格式包括：

- 纯文本，如“用简洁的语言回答”

- 结构化文本，如“以JSON格式输出”

- 列表形式，如“以 bullet point 形式列出”

- 代码块，如“用Python代码实现”

- 表格，如“以表格形式呈现对比信息”

等等输出格式。

指定输出格式的典型表达包括：“请用以下JSON格式输出”、“请分点列出”、“请用不超过100字概括”等。

通过这种方式，用户可以省去后续处理的麻烦，直接获得格式规范的输出。

## 三、提示词技术 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#2876910816)

### 零样本提示 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#1641165541)

零样本提示（Zero-shot Prompting）是指在不提供任何示例的情况下，直接要求模型完成某个任务。这种方式完全依赖模型从预训练中学到的知识来理解和执行任务。

零样本提示的典型形式是直接给出任务描述和输入，

例 1：

> 把以下句子翻译成英文：“我爱学习人工智能。”

模型需要依靠其预训练阶段学到的语言知识和翻译能力来完成这个任务。

例 2：

> 将文本分类为中性、负面或正面。
>
> 文本：我认为这次假期还可以。
>
> 情感：

输出：

> 中性

在上面的提示词中，我们没有向模型提供任何示例——这就是零样本能力。

零样本提示的优点是简洁直接，适用于任务简单明确、模型熟悉的场景。GPT-4 等大型模型在许多任务上即使没有示例也能表现良好，这得益于其海量预训练数据中包含的各种语言现象和任务模式。

然而，零样本提示也有局限性。对于复杂任务或特殊格式要求，模型可能无法准确理解用户的期望，导致输出不符合要求。此外，某些特定领域的任务可能需要模型具备专门的领域知识，而这些知识可能不在模型的覆盖范围内。

### 单样本和少样本提示 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#3857486551)

#### 单样本和少样本提示介绍 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#3362429564)

单样本提示（One-shot Prompting）提供一个示例，帮助模型理解任务的期望形式。少样本提示（Few-shot Prompting）则提供多个示例（通常2-5个），让模型更好地把握任务规律。

单样本One-shot提示给 1 个输入→输出，让模型模仿格式 / 逻辑。适合简单任务。

> 任务：把口语转成书面语。
>
> 示例：
>
> 输入：这东西挺好用的
>
> 输出：该产品使用效果良好
>
> 输入：我觉得这个方案还行
>
> 输出：

少样本Few-shot提示的典型结构包括：任务描述、一个或多个输入-输出示例、以及需要模型处理的实际输入。

例子：

```yaml
Copy
任务：判断评论的情感是正面还是负面

示例1：
评论：这部电影太精彩了，我看得热泪盈眶
情感：正面

示例2：
评论：服务态度太差了，等了一个小时还没人接待
情感：负面

请判断以下评论的情感：
评论：商品质量还可以，就是物流太慢了
情感：
```

少样本提示的作用机制在于通过示例提供任务模式的直观展示。模型可以通过分析示例，学习到输入与输出之间的对应关系，从而在新任务上做出更准确的预测。

这种方式特别适合以下场景：任务格式特殊复杂、输出有特定的结构要求、需要模型遵循特定的领域规范等。

#### **少样本提示Few-shot要点** [\#](https://www.cnblogs.com/jiujuan/p/19855636\#3698916934)

要有效使用 Few-shot 提示词，需要注意以下几个技术要点：

- 示例的质量：这个至关重要。示例应该具有代表性和准确性，能够清晰地展示任务的正确处理方式。避免使用有错误或歧义的示例，因为模型可能会学习到这些示例的不良模式。

- 示例的数量：这个需要权衡。一般来说，2-5 个示例可以满足大多数任务的需求。过多的示例可能导致上下文过长，增加计算成本且可能稀释关键信息；但对于复杂任务或需要模型学习多种模式的情况，增加示例数量可能会有帮助。

- 示例的多样性：这个也需要考虑。如果任务涉及多种不同的情况，提供涵盖各种情况的示例可以帮助模型全面理解任务。例如，在情感分析任务中，提供包含不同表达方式（直接表达、讽刺表达、含蓄表达等）的示例，可以提高模型处理各类文本的能力。

- 示例的顺序：这个同样有影响。研究表明，将示例按照“从简单到复杂”的顺序排列，通常能让模型更好地理解任务要求。此外，将最终需要处理的任务紧跟在示例后面，可以确保模型集中注意力在最关键的内容上。

#### 少样本提示限制 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#3315161853)

以下例子来自： [https://www.promptingguide.ai/zh/techniques/fewshot](https://www.promptingguide.ai/zh/techniques/fewshot)

标准的少样本提示对许多任务都有效，但仍然不是一种完美的技术，特别是在处理更复杂的推理任务时。让我们演示为什么会这样。您是否还记得之前提供的任务：

> 这组数字中的奇数加起来是一个偶数：15、32、5、13、82、7、1。
>
> A：

如果我们再试一次，模型输出如下：

> 是的，这组数字中的奇数加起来是107，是一个偶数。

这不是正确的答案，这不仅突显了这些系统的局限性，而且需要更高级的提示工程。

让我们尝试添加一些示例，看看少样本提示是否可以改善结果。

_提示：_

> 这组数字中的奇数加起来是一个偶数：4、8、9、15、12、2、1。
>
> A：答案是False。
>
> 这组数字中的奇数加起来是一个偶数：17、10、19、4、8、12、24。
>
> A：答案是True。
>
> 这组数字中的奇数加起来是一个偶数：16、11、14、4、8、13、24。
>
> A：答案是True。
>
> 这组数字中的奇数加起来是一个偶数：17、9、10、12、13、4、2。
>
> A：答案是False。
>
> 这组数字中的奇数加起来是一个偶数：15、32、5、13、82、7、1。
>
> A：

_输出：_

> 答案是True。

这没用。似乎少样本提示不足以获得这种类型的推理问题的可靠响应。上面的示例提供了任务的基本信息。如果您仔细观察，我们引入的任务类型涉及几个更多的推理步骤。换句话说，如果我们将问题分解成步骤并向模型演示，这可能会有所帮助。思维链（CoT）提示出现了，以解决更复杂的算术、常识和符号推理任务。以更技巧方式来写提示词，处理更复杂的任务。这就涉及到提示词工程。

## 四、提示词工程 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#530351949)

### 什么是提示词工程 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#3916502644)

提示词工程（Prompt Engineering）是指设计和优化提示词，以提高 LLM 输出质量的一系列技术和方法。它涵盖了从基础的提示词撰写到高级的提示词优化策略的全过程。

提示词工程的重要性源于 LLM 的一个关键特性： **模型对提示词非常敏感**。

同一个任务，使用不同的提示词设计可能产生差异巨大的结果。一个精心设计的提示词可以让模型准确理解任务要求并给出高质量回答，而一个模糊或不当的提示词则可能导致模型产生无意义或错误的输出。因此，掌握提示词工程技能是有效使用 LLM 的关键。

提示词工程既是一门科学，也是一门艺术。从科学角度，它有一定的原则和技巧可以遵循；从艺术角度，优秀的提示词设计往往需要创造力和对任务特性的深入理解。随着 LLM 技术的不断发展，提示词工程已经成为人工智能领域的一个重要分支，出现了专门从事这项工作的提示词工程师职位。

### 提示词工程的核心组成 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#2705903136)

提示词工程包含多个核心组成部分，每个部分都有其特定的作用和设计原则。

**任务分析** ：提示词工程的第一步。在设计提示词之前，需要深入理解任务的本质：任务的目标是什么？需要什么样的输入？期望什么样的输出？有什么特殊的约束条件？只有清晰定义任务，才能设计出有效的提示词。

**提示词设计** ：将任务转化为具体提示词的过程。这需要考虑如何清晰地表达指令、如何提供必要的上下文、如何组织提示词的结构等。好的提示词设计应该做到：指令明确无歧义、上下文相关且适量、格式规范便于理解。

**迭代优化**：提示词工程的核心环节。初次设计的提示词往往不能达到最佳效果，需要通过反复测试和改进来优化。这一过程通常包括：分析模型输出的不足、理解问题产生的根源、调整提示词的相应部分、再次测试验证效果。

**技巧应用**：涉及各种具体的提示词优化技术。

这些提示词优化技术包括：

- 思维链提示词（CoT，Chain of Thought）
- 自我一致性提示词（Self-Consistency）
- 生成知识提示词（Generated Knowledge）
- 思维树提示词（ToT，Tree of Thoughts）
- 链式提示词（Prompt Chaining）
- 自动推理并使用工具（ART，Automatic Reasoning and Tool-use）
- 检索增强生成（RAG，Retrieval Augmented Generation）

等等，每种技巧都有其适用的场景和独特的优势。更多提示词技术详情请看这里 [promptingguide.ai的提示词技术讲解](https://www.promptingguide.ai/zh/techniques)。

## 五、高级提示词技术 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#1956271334)

下面说明一下几种高级提示词。

### 思维链提示词 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#1882247195)

思维链提示（CoT，Chain of Thought），它是一种重要的提示技巧，它是一种通过在提示词中引导模型展示其推理过程来提升推理能力的提示技术。

具体做法是在提示词中加入“让我们一步步思考”或“请解释你的推理过程”等引导语。研究表明，思维链提示可以显著提升模型在数学题、逻辑推理等需要多步思考的任务上的表现，通过显式地展示推理步骤，使模型能够进行更加准确、更加连贯的多步骤推理。

![思维链提示词](https://img2024.cnblogs.com/blog/650581/202604/650581-20260412155727238-343690009.png)

(图片来源： [Wei等人（2022）](https://arxiv.org/abs/2201.11903))

在 [Wei等人（2022）](https://arxiv.org/abs/2201.11903) 中引入的链式思考（CoT）提示通过中间推理步骤实现了复杂的推理能力。您可以将其与少样本提示相结合，以获得更好的结果，以便在回答之前进行推理的更复杂的任务。

从技术角度分析，思维链提示之所以有效，涉及到几个重要的机制。

- 首先，通过要求模型分解问题为多个子问题，每个子问题的难度相对降低，模型在每一步只需要关注一个具体的推理任务。

- 其次，中间的推理步骤为模型提供了“检查点”，可以在每一步验证推理的正确性，及时发现和纠正错误。

- 第三，推理步骤的存在使得整个思考过程更加透明，便于人类理解和干预。

思维链提示技术的使用场景在数学问题求解、逻辑推理类问题、代码调试和程序分析任务、复杂问题的拆解和分析、需要解释说明的教育类任务等等一些场景中。

**数学推理例子**

```yaml
Copy
问题：小明有23个苹果，小红给了他15个苹果，然后又送走了8个苹果。小明现在有多少个苹果？

使用思维链提示：
请逐步计算，每一步都展示出来。

步骤1：首先，小明原来有23个苹果
步骤2：小红给了他15个苹果，所以23 + 15 = 38个
步骤3：然后他又送走了8个苹果，所以38 - 8 = 30个
步骤4：因此，小明现在有30个苹果

答案：30个
```

这个例子展示了思维链提示的基本形式：通过将计算过程分解为多个明确的步骤，使推理过程透明化、可验证。

**实际应用示例：商业分析**

思维链提示还可以用于复杂的分析和决策场景：

```yaml
Copy
问题：某电商公司考虑是否要在下个季度推出会员订阅服务。请分析应该考虑哪些因素并给出建议。

使用思维链提示：
请系统性地分析这个问题。

第一步：明确问题核心
需要评估的是：是否应该推出会员订阅服务，以及如何推出。

第二步：识别利益相关方
- 客户：订阅服务的直接消费者
- 公司：服务的提供方，需要评估投入产出
- 竞争对手：可能的市场反应

第三步：分析有利因素
1. 客户留存：订阅模式可以提高客户粘性
2. 稳定收入：形成可预测的现金流
3. 数据价值：深入了解客户偏好

第四步：分析风险和挑战
1. 初期投入：需要开发订阅系统、制定定价策略
2. 用户接受度：客户是否愿意为订阅付费
3. 竞争对手反应：可能引发价格战

第五步：综合评估
权衡利弊，基于公司的具体情况给出建议。

建议：建议采用渐进式策略...（此处省略具体建议内容）
```

### 自我一致性提示词 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#1707680038)

自我一致性提示（Self-Consistency）由 [Wang等人（2022）](https://arxiv.org/pdf/2203.11171.pdf) 提出，自我一致性旨在“替换链式思维提示中使用的天真贪婪解码方法”。其想法是通过少样本 CoT 采样多个不同的推理路径，并使用生成结果选择最一致的答案。

它是继思维链提示之后出现的又一项重要的提示技术。它的核心思想建立在这样一个观察之上：对于同一个问题，模型在多次推理过程中可能会产生不同的结果，但正确的推理路径往往会产生最一致的答案。

通过让模型生成多个不同的推理路径，然后选择其中最一致的答案，自我一致性提示可以显著提高最终结果的可靠性。

自我一致性提示的工作原理可以类比为集思广益的投票过程。想象一个陪审团在做出裁决时，每个陪审员独立思考问题，然后大家一起讨论，最终选择最被广泛认可的裁决。自我一致性提示正是将这种集体智慧的机制引入到了单个AI模型的推理过程中——模型扮演着多个“陪审员”的角色，每个“陪审员”可能走不同的推理路径，但最终通过投票选出最一致的答案。

它使用一般场景有：

- 没有唯一标准答案的开放式问题，例如，问答系统、写作辅助、创意生成等任务，答案的正确性可能存在多种合理的解释
- 需要减少幻觉产生的场景，对自我一致性提示有强烈需求。LLM 有时会产生看似合理但实际错误的信息，这种现象被称为幻觉。通过让模型生成多个答案并选择最一致的，可以一定程度上抑制幻觉的影响——因为真正的知识通常会在多次推理中保持一致，而幻觉往往是不一致的。
- 复杂推理任务，自我一致性提示的另一重要应用领域。特别是数学证明、逻辑分析等需要严格推理的任务，单次推理可能因为某个环节的错误导致整个答案错误。通过多路径推理，可以从多个角度验证推理的正确性，提高最终答案的可靠性。
- 专家系统和决策支持类应用，也可以从自我一致性提示中受益。在医疗诊断、法律分析、金融预测等专业领域，多个独立的推理路径可以提供相互验证，提高决策的可信度。

**逻辑推理应用示例**

考虑一个复杂的逻辑推理问题：

```yaml
Copy
问题：如果明天不下雨，我就去爬山。如果我去爬山，我就会锻炼身体。如果我锻炼身体，我就会保持健康。请问在什么情况下我会保持健康？

使用自我一致性提示进行多路径推理：

推理路径1（正向分析）：
条件：明天不下雨
推论1：不去爬山 → 不锻炼身体 → 不会保持健康
等等，这个推理有误...

重新分析：
如果明天下雨 → 不去爬山 → 不锻炼身体 → 不保持健康
如果明天不下雨 → 去爬山 → 锻炼身体 → 保持健康
答案：明天下雨时我不会保持健康，明天不下雨时我会保持健康

推理路径2（逆向分析）：
目标：保持健康
反向条件：锻炼身体
反向条件：去爬山
反向条件：明天不下雨

因此：只有明天下雨时我才不会保持健康，明天不下雨时我会保持健康

推理路径3（条件分析）：
保持健康的充分条件链：不下雨 → 爬山 → 锻炼 → 健康
逆否命题：不健康 → 不锻炼 → 不爬山 → 下雨

综合结论：明天不下雨是我保持健康的充分条件

一致性分析：所有推理路径都指向相同结论

最终输出：只要明天不下雨，我就会保持健康。
```

### 链式提示词 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#2759080427)

链式提示词（Prompt Chaining），又称提示链，是一种将复杂任务分解为多个简单子任务，然后通过一系列相互关联的提示词逐步引导LLM 完成整个任务的技术。其核心思想是分而治之——与其让模型一次性完成一个复杂的任务，不如让它一步步来，每一步专注于一个具体的子任务。

链式提示的工作原理类似于工厂的生产流水线。在工厂里，一个复杂产品的制造会被分解为多个简单的工序，每个工序负责特定的步骤，最终所有工序的成果组合在一起形成完整的产品。类似地，链式提示将复杂任务分解为多个简单的“步骤”，每个步骤由一个提示词驱动，模型在该提示词的引导下完成特定的处理，然后将结果传递给下一步。

它的适用场景：

- 文档处理与分析是链式提示的典型应用场景。例如，一篇长文的摘要、提取关键信息、多维度分析等任务，都可以分解为“读取内容”、“识别主题”、“提取关键点”、“组织输出”等多个步骤。每个步骤由独立的提示词处理，最终组合成完整的分析报告。
- 多阶段写作任务同样适合使用链式提示。写一篇完整的商业提案可能包括“确定核心主题”、“设计文章结构”、“撰写各部分内容”、“审核与修改”等阶段。通过链式提示，模型可以在每个阶段聚焦于特定目标，产出的内容更加连贯、专业。
- 需要严格遵循流程的任务。例如，代码审查可能需要“检查语法错误”、“检查逻辑问题”、“检查安全漏洞”、“检查性能问题”等多个环节。链式提示确保每个环节都被系统性地处理，不会遗漏。
- 需要整合多种能力或信息来源的任务。例如，一个综合性的市场分析报告可能需要整合财务数据、行业趋势、竞争对手信息等多个来源的数据。链式提示可以将不同来源的数据处理分配给不同的步骤，最后统一整合。

**例子说明**

假设我们需要模型帮助我们分析和评估一家公司的财务状况。这个任务过于复杂，直接用一个提示词很难达到理想效果。使用链式提示词，我们可以将其分解为以下步骤：

**第一步：提取财务数据**

```bash
Copy
提示词1：
请从以下文本中提取关键的财务数据，包括：年收入、净利润、总资产、负债总额、现金流。请以结构化的格式输出，如果某项数据不存在，请标注"未提供"。

财务报告文本：
[此处提供财务报告内容]
```

**第二步：计算财务比率**

```css
Copy
提示词2：
基于以下财务数据，计算以下财务比率：资产负债率、净利润率、毛利率、流动比率。每个比率请给出计算过程和结果。

财务数据：
[引用第一步的输出]
```

**第三步：分析与评估**

```css
Copy
提示词3：
基于以下财务比率，对公司的财务状况进行分析。请从盈利能力、偿债能力、运营效率三个维度进行评估，并指出需要注意的风险点。

财务比率：
[引用第二步的输出]
```

一步一步来分析公司财务状况。

## 六、参考 [\#](https://www.cnblogs.com/jiujuan/p/19855636\#4196361461)

- [Prompt Engineering Guide](https://www.promptingguide.ai/zh) 提示词工程指南

- [https://www.promptingguide.ai/zh/techniques/zeroshot](https://www.promptingguide.ai/zh/techniques/zeroshot) 零样板提示词学习

- [https://arxiv.org/pdf/2109.01652.pdf](https://arxiv.org/pdf/2109.01652.pdf) 指令调整已被证明可以改善零样本学习

- [https://www.promptingguide.ai/zh/techniques/cot](https://www.promptingguide.ai/zh/techniques/cot) 链式思考（CoT，Chain-of-Thought）提示

- [https://arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903) 思维链 CoT

- [https://www.promptingguide.ai/zh/techniques/consistency](https://www.promptingguide.ai/zh/techniques/consistency) 自我一致性提示词

- [https://www.promptingguide.ai/zh/techniques/prompt\_chaining](https://www.promptingguide.ai/zh/techniques/prompt_chaining) 链式提示词

作者：九卷 (公众号：九卷沉思录)

出处： [https://www.cnblogs.com/jiujuan/p/19855636](https://www.cnblogs.com/jiujuan/p/19855636)

版权：本文采用「 [署名-非商业性使用-相同方式共享 by nc nd 4.0 国际](https://creativecommons.org/licenses/by-nc-nd/4.0/)」知识共享许可协议进行许可。

【升认知赚好钱】

合集:
[AI.大模型](https://www.cnblogs.com/jiujuan/collections/25687)

分类:
[AI-大模型](https://www.cnblogs.com/jiujuan/category/2447815.html)

标签:
[AI](https://www.cnblogs.com/jiujuan/tag/AI/), [提示词](https://www.cnblogs.com/jiujuan/tag/%E6%8F%90%E7%A4%BA%E8%AF%8D/), [prompt](https://www.cnblogs.com/jiujuan/tag/prompt/)

免责声明：本内容来自平台创作者，博客园系信息发布平台，仅提供信息存储空间服务。

好文要顶关注我收藏该文微信分享

[![](https://pic.cnblogs.com/face/650581/20190630002924.png)](https://home.cnblogs.com/u/jiujuan/)

[九卷](https://home.cnblogs.com/u/jiujuan/)

[粉丝 \- 289](https://home.cnblogs.com/u/jiujuan/followers/) [关注 \- 166](https://home.cnblogs.com/u/jiujuan/followees/)

+加关注

0

0

[«](https://www.cnblogs.com/jiujuan/p/19848128) 上一篇： [LLM大模型中AI-Agent智能体应用开发相关知识介绍](https://www.cnblogs.com/jiujuan/p/19848128 "发布于 2026-04-10 17:40")

[»](https://www.cnblogs.com/jiujuan/p/19855674) 下一篇： [AI Agent上下文工程(context engineering)知识学习总结](https://www.cnblogs.com/jiujuan/p/19855674 "发布于 2026-04-12 16:07")

posted @
2026-04-12 15:58 [九卷](https://www.cnblogs.com/jiujuan)
阅读(190)
评论(0)

收藏 [举报](https://report.cnblogs.com/?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fjiujuan%2Fp%2F19855636&targetId=19855636&targetType=0)

[刷新页面](https://www.cnblogs.com/jiujuan/p/19855636#) [返回顶部](https://www.cnblogs.com/jiujuan/p/19855636#top)

登录后才能查看或发表评论，立即 登录 或者
[逛逛](https://www.cnblogs.com/) 博客园首页

[【推荐】 凌霞 618 年中大促，Halo 与 1Panel 产品全线半价，叠加满减！](https://www.cnblogs.com/cmt/p/20552787)

[【推荐】HarmonyOS 6.1.0 创新特性“悬浮页签+沉浸光感”精品文章专题](https://harmonyos.cnblogs.com/p/28310)

[【推荐】科研领域的连接者艾思科蓝，一站式科研学术服务数字化平台](https://ais.cn/u/QjqYJr)

[![](https://img2024.cnblogs.com/blog/35695/202606/35695-20260609221536870-1777800795.webp)](https://www.volcengine.com/activity/codingplan?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=cnblogs)

- [让 Agent 在对话中成长：自进化机制的五层实现](https://www.cnblogs.com/zhayujie/p/20523587/self-evolution)
- [代码之外：一个技术人的职场困境与自我和解](https://www.cnblogs.com/charlee44/p/20296178)
- [贩卖焦虑的时代，我终于接住了真实的焦虑](https://www.cnblogs.com/ZyCoder/p/20176104)
- [工良吐槽篇：万字长文细说 AI 落地之笑谈](https://www.cnblogs.com/whuanle/p/20088309)
- [代码是 AI 写的，生产事故谁背锅？](https://www.cnblogs.com/Zhang-Xiang/p/20028472)

- 2025-04-12
[有哪些「低级苦」和「高级苦」（认知成长）](https://www.cnblogs.com/jiujuan/p/18806965)
- 2023-04-12
[Go微服务框架go-kratos实战学习08：负载均衡基本使用](https://www.cnblogs.com/jiujuan/p/17311134.html)
- 2022-04-12
[golang常用库包：Go依赖注入(DI)工具-wire使用](https://www.cnblogs.com/jiujuan/p/16136633.html)

### 公告

行万里路，破九卷书(公号: 九卷沉思录)

**Email: jiujuanfeng@163.com**

昵称：
[九卷](https://home.cnblogs.com/u/jiujuan/)

园龄：
[11年11个月](https://home.cnblogs.com/u/jiujuan/ "入园时间：2014-07-14")

粉丝：
[289](https://home.cnblogs.com/u/jiujuan/followers/)

关注：
[166](https://home.cnblogs.com/u/jiujuan/followees/)

+加关注

### [我的标签](https://www.cnblogs.com/jiujuan/tag/)

- [go(85)](https://www.cnblogs.com/jiujuan/tag/go/)
- [架构(38)](https://www.cnblogs.com/jiujuan/tag/%E6%9E%B6%E6%9E%84/)
- [微服务(36)](https://www.cnblogs.com/jiujuan/tag/%E5%BE%AE%E6%9C%8D%E5%8A%A1/)
- [golang(33)](https://www.cnblogs.com/jiujuan/tag/golang/)
- [redis(27)](https://www.cnblogs.com/jiujuan/tag/redis/)
- [管理(21)](https://www.cnblogs.com/jiujuan/tag/%E7%AE%A1%E7%90%86/)
- [原理(21)](https://www.cnblogs.com/jiujuan/tag/%E5%8E%9F%E7%90%86/)
- [linux(19)](https://www.cnblogs.com/jiujuan/tag/linux/)
- [读书(15)](https://www.cnblogs.com/jiujuan/tag/%E8%AF%BB%E4%B9%A6/)
- [微服务架构(15)](https://www.cnblogs.com/jiujuan/tag/%E5%BE%AE%E6%9C%8D%E5%8A%A1%E6%9E%B6%E6%9E%84/)
- [更多](https://www.cnblogs.com/jiujuan/tag/)

### 积分与排名

- 积分 \-
496714

- 排名 \-
1542

### 合集

- [职业发展(6)](https://www.cnblogs.com/jiujuan/collections/16082)
- [敏捷开发(13)](https://www.cnblogs.com/jiujuan/collections/23133)
- [管理(22)](https://www.cnblogs.com/jiujuan/collections/25481)
- [AI.大模型(8)](https://www.cnblogs.com/jiujuan/collections/25687)
- [创业与商业(6)](https://www.cnblogs.com/jiujuan/collections/25720)
- [微服务架构(31)](https://www.cnblogs.com/jiujuan/collections/27118)
- [九卷启示录.认知成长.方法论(16)](https://www.cnblogs.com/jiujuan/collections/27432)

### [随笔分类](https://www.cnblogs.com/jiujuan/post-categories)

- [\[00\]产品-业务-管理(69)](https://www.cnblogs.com/jiujuan/category/1212400.html)
- [\[01\]Golang(78)](https://www.cnblogs.com/jiujuan/category/622746.html)
- [\[01\]架构-分布式-微服务(55)](https://www.cnblogs.com/jiujuan/category/1211896.html)
- [\[01-1\]深入理解Golang语言(11)](https://www.cnblogs.com/jiujuan/category/1691617.html)
- [\[01-2\]Java(4)](https://www.cnblogs.com/jiujuan/category/1777252.html)
- [\[01-3\]C-Python(5)](https://www.cnblogs.com/jiujuan/category/595467.html)
- [\[02\]redis-memcached(23)](https://www.cnblogs.com/jiujuan/category/1211181.html)
- [\[02-1\]mysql(10)](https://www.cnblogs.com/jiujuan/category/594968.html)
- [\[03\]多读一本书(19)](https://www.cnblogs.com/jiujuan/category/1930519.html)
- [\[04\]php(15)](https://www.cnblogs.com/jiujuan/category/594967.html)
- [\[04-1\]docker-k8s云原生(4)](https://www.cnblogs.com/jiujuan/category/1857746.html)
- [\[04-2\]consul-etcd(5)](https://www.cnblogs.com/jiujuan/category/1421685.html)
- [\[04-3\]消息队列-Elasticsearch(8)](https://www.cnblogs.com/jiujuan/category/1216450.html)
- [\[05\]linux内核-网络(24)](https://www.cnblogs.com/jiujuan/category/595798.html)
- [\[05-1\]协议-tcp/ip-rpc(9)](https://www.cnblogs.com/jiujuan/category/1220217.html)
- [\[05-2\]数据结构-算法(4)](https://www.cnblogs.com/jiujuan/category/594972.html)
- [\[05-3\]设计模式(7)](https://www.cnblogs.com/jiujuan/category/1384651.html)
- [\[05-4\]nginx(5)](https://www.cnblogs.com/jiujuan/category/594969.html)
- [\[06\]职业发展/生涯(13)](https://www.cnblogs.com/jiujuan/category/1489563.html)
- [AI-大模型(7)](https://www.cnblogs.com/jiujuan/category/2447815.html)
- [数字化(转型/产业)(4)](https://www.cnblogs.com/jiujuan/category/2297416.html)
- 更多

### 随笔档案

- [2026年4月(10)](https://www.cnblogs.com/jiujuan/p/archive/2026/04)
- [2026年3月(3)](https://www.cnblogs.com/jiujuan/p/archive/2026/03)
- [2026年1月(1)](https://www.cnblogs.com/jiujuan/p/archive/2026/01)
- [2025年12月(2)](https://www.cnblogs.com/jiujuan/p/archive/2025/12)
- [2025年10月(1)](https://www.cnblogs.com/jiujuan/p/archive/2025/10)
- [2025年9月(1)](https://www.cnblogs.com/jiujuan/p/archive/2025/09)
- [2025年8月(1)](https://www.cnblogs.com/jiujuan/p/archive/2025/08)
- [2025年7月(3)](https://www.cnblogs.com/jiujuan/p/archive/2025/07)
- [2025年6月(2)](https://www.cnblogs.com/jiujuan/p/archive/2025/06)
- [2025年4月(3)](https://www.cnblogs.com/jiujuan/p/archive/2025/04)
- [2025年3月(4)](https://www.cnblogs.com/jiujuan/p/archive/2025/03)
- [2025年2月(4)](https://www.cnblogs.com/jiujuan/p/archive/2025/02)
- [2025年1月(2)](https://www.cnblogs.com/jiujuan/p/archive/2025/01)
- [2024年12月(4)](https://www.cnblogs.com/jiujuan/p/archive/2024/12)
- [2024年11月(4)](https://www.cnblogs.com/jiujuan/p/archive/2024/11)
- [2024年10月(1)](https://www.cnblogs.com/jiujuan/p/archive/2024/10)
- [2024年9月(1)](https://www.cnblogs.com/jiujuan/p/archive/2024/09)
- [2024年5月(3)](https://www.cnblogs.com/jiujuan/p/archive/2024/05)
- [2024年4月(1)](https://www.cnblogs.com/jiujuan/p/archive/2024/04)
- [2024年2月(2)](https://www.cnblogs.com/jiujuan/p/archive/2024/02)
- [2023年7月(2)](https://www.cnblogs.com/jiujuan/p/archive/2023/07)
- [2023年6月(1)](https://www.cnblogs.com/jiujuan/p/archive/2023/06)
- [2023年5月(5)](https://www.cnblogs.com/jiujuan/p/archive/2023/05)
- [2023年4月(6)](https://www.cnblogs.com/jiujuan/p/archive/2023/04)
- [2023年3月(9)](https://www.cnblogs.com/jiujuan/p/archive/2023/03)
- [2023年2月(4)](https://www.cnblogs.com/jiujuan/p/archive/2023/02)
- [2023年1月(1)](https://www.cnblogs.com/jiujuan/p/archive/2023/01)
- [2022年11月(3)](https://www.cnblogs.com/jiujuan/p/archive/2022/11)
- [2022年10月(5)](https://www.cnblogs.com/jiujuan/p/archive/2022/10)
- [2022年9月(4)](https://www.cnblogs.com/jiujuan/p/archive/2022/09)
- [2022年8月(4)](https://www.cnblogs.com/jiujuan/p/archive/2022/08)
- [2022年7月(1)](https://www.cnblogs.com/jiujuan/p/archive/2022/07)
- [2022年6月(4)](https://www.cnblogs.com/jiujuan/p/archive/2022/06)
- [2022年5月(5)](https://www.cnblogs.com/jiujuan/p/archive/2022/05)
- [2022年4月(5)](https://www.cnblogs.com/jiujuan/p/archive/2022/04)
- [2022年3月(3)](https://www.cnblogs.com/jiujuan/p/archive/2022/03)
- [2022年2月(1)](https://www.cnblogs.com/jiujuan/p/archive/2022/02)
- [2022年1月(3)](https://www.cnblogs.com/jiujuan/p/archive/2022/01)
- [2021年12月(1)](https://www.cnblogs.com/jiujuan/p/archive/2021/12)
- [2021年11月(2)](https://www.cnblogs.com/jiujuan/p/archive/2021/11)
- [2021年10月(1)](https://www.cnblogs.com/jiujuan/p/archive/2021/10)
- [2021年8月(1)](https://www.cnblogs.com/jiujuan/p/archive/2021/08)
- [2021年7月(3)](https://www.cnblogs.com/jiujuan/p/archive/2021/07)
- [2021年4月(2)](https://www.cnblogs.com/jiujuan/p/archive/2021/04)
- [2021年3月(3)](https://www.cnblogs.com/jiujuan/p/archive/2021/03)
- [2021年2月(1)](https://www.cnblogs.com/jiujuan/p/archive/2021/02)
- [2021年1月(1)](https://www.cnblogs.com/jiujuan/p/archive/2021/01)
- [2020年11月(3)](https://www.cnblogs.com/jiujuan/p/archive/2020/11)
- [2020年10月(8)](https://www.cnblogs.com/jiujuan/p/archive/2020/10)
- [2020年9月(3)](https://www.cnblogs.com/jiujuan/p/archive/2020/09)
- [2020年8月(3)](https://www.cnblogs.com/jiujuan/p/archive/2020/08)
- [2020年7月(10)](https://www.cnblogs.com/jiujuan/p/archive/2020/07)
- [2020年6月(2)](https://www.cnblogs.com/jiujuan/p/archive/2020/06)
- [2020年5月(1)](https://www.cnblogs.com/jiujuan/p/archive/2020/05)
- [2020年4月(3)](https://www.cnblogs.com/jiujuan/p/archive/2020/04)
- [2020年3月(2)](https://www.cnblogs.com/jiujuan/p/archive/2020/03)
- [2020年2月(2)](https://www.cnblogs.com/jiujuan/p/archive/2020/02)
- [2020年1月(2)](https://www.cnblogs.com/jiujuan/p/archive/2020/01)
- [2019年12月(2)](https://www.cnblogs.com/jiujuan/p/archive/2019/12)
- [2019年11月(8)](https://www.cnblogs.com/jiujuan/p/archive/2019/11)
- [2019年10月(2)](https://www.cnblogs.com/jiujuan/p/archive/2019/10)
- [2019年9月(3)](https://www.cnblogs.com/jiujuan/p/archive/2019/09)
- [2019年8月(3)](https://www.cnblogs.com/jiujuan/p/archive/2019/08)
- [2019年7月(3)](https://www.cnblogs.com/jiujuan/p/archive/2019/07)
- [2019年6月(4)](https://www.cnblogs.com/jiujuan/p/archive/2019/06)
- [2019年5月(2)](https://www.cnblogs.com/jiujuan/p/archive/2019/05)
- [2019年4月(8)](https://www.cnblogs.com/jiujuan/p/archive/2019/04)
- [2019年3月(4)](https://www.cnblogs.com/jiujuan/p/archive/2019/03)
- [2019年2月(5)](https://www.cnblogs.com/jiujuan/p/archive/2019/02)
- [2018年12月(1)](https://www.cnblogs.com/jiujuan/p/archive/2018/12)
- [2018年11月(1)](https://www.cnblogs.com/jiujuan/p/archive/2018/11)
- [2018年10月(2)](https://www.cnblogs.com/jiujuan/p/archive/2018/10)
- [2018年9月(2)](https://www.cnblogs.com/jiujuan/p/archive/2018/09)
- [2018年8月(2)](https://www.cnblogs.com/jiujuan/p/archive/2018/08)
- [2018年7月(2)](https://www.cnblogs.com/jiujuan/p/archive/2018/07)
- [2018年6月(5)](https://www.cnblogs.com/jiujuan/p/archive/2018/06)
- [2018年5月(3)](https://www.cnblogs.com/jiujuan/p/archive/2018/05)
- [2018年3月(2)](https://www.cnblogs.com/jiujuan/p/archive/2018/03)
- [2017年12月(2)](https://www.cnblogs.com/jiujuan/p/archive/2017/12)
- [2017年11月(3)](https://www.cnblogs.com/jiujuan/p/archive/2017/11)
- [2017年10月(3)](https://www.cnblogs.com/jiujuan/p/archive/2017/10)
- [2017年9月(1)](https://www.cnblogs.com/jiujuan/p/archive/2017/09)
- [2017年8月(2)](https://www.cnblogs.com/jiujuan/p/archive/2017/08)
- [2017年7月(2)](https://www.cnblogs.com/jiujuan/p/archive/2017/07)
- [2017年6月(6)](https://www.cnblogs.com/jiujuan/p/archive/2017/06)
- [2017年5月(8)](https://www.cnblogs.com/jiujuan/p/archive/2017/05)
- [2017年4月(4)](https://www.cnblogs.com/jiujuan/p/archive/2017/04)
- [2017年3月(5)](https://www.cnblogs.com/jiujuan/p/archive/2017/03)
- [2016年10月(1)](https://www.cnblogs.com/jiujuan/p/archive/2016/10)
- [2016年8月(7)](https://www.cnblogs.com/jiujuan/p/archive/2016/08)
- [2016年7月(4)](https://www.cnblogs.com/jiujuan/p/archive/2016/07)
- [2016年6月(3)](https://www.cnblogs.com/jiujuan/p/archive/2016/06)
- [2016年5月(4)](https://www.cnblogs.com/jiujuan/p/archive/2016/05)
- [2016年4月(1)](https://www.cnblogs.com/jiujuan/p/archive/2016/04)
- [2016年3月(3)](https://www.cnblogs.com/jiujuan/p/archive/2016/03)
- [2015年11月(4)](https://www.cnblogs.com/jiujuan/p/archive/2015/11)
- [2015年10月(4)](https://www.cnblogs.com/jiujuan/p/archive/2015/10)
- [2015年9月(1)](https://www.cnblogs.com/jiujuan/p/archive/2015/09)
- [2015年6月(1)](https://www.cnblogs.com/jiujuan/p/archive/2015/06)
- [2015年5月(3)](https://www.cnblogs.com/jiujuan/p/archive/2015/05)
- [2015年4月(1)](https://www.cnblogs.com/jiujuan/p/archive/2015/04)
- [2015年1月(2)](https://www.cnblogs.com/jiujuan/p/archive/2015/01)
- [2014年10月(4)](https://www.cnblogs.com/jiujuan/p/archive/2014/10)
- [2014年9月(1)](https://www.cnblogs.com/jiujuan/p/archive/2014/09)
- [2014年8月(2)](https://www.cnblogs.com/jiujuan/p/archive/2014/08)
- [2014年7月(5)](https://www.cnblogs.com/jiujuan/p/archive/2014/07)
- 更多

### [阅读排行榜](https://www.cnblogs.com/jiujuan/most-viewed)

- [1\. golang常用库：字段参数验证库-validator使用(59111)](https://www.cnblogs.com/jiujuan/p/13823864.html)
- [2\. tcpdump高级过滤(58663)](https://www.cnblogs.com/jiujuan/p/9017495.html)
- [3\. php中的匿名函数和闭包(closure)(28146)](https://www.cnblogs.com/jiujuan/p/3894578.html)
- [4\. golang 中 channel 的详细使用、使用注意事项及死锁分析(27705)](https://www.cnblogs.com/jiujuan/p/16014608.html)
- [5\. golang常用库包：log日志记录-uber的Go日志库zap使用详解(22241)](https://www.cnblogs.com/jiujuan/p/17304844.html)

### [推荐排行榜](https://www.cnblogs.com/jiujuan/most-liked)

- [1\. 小公司需要使用微服务架构吗？(32)](https://www.cnblogs.com/jiujuan/p/17116605.html)
- [2\. 全面了解事务、分布式事务理论及其实现方案(22)](https://www.cnblogs.com/jiujuan/p/17542160.html)
- [3\. 软件产品开发中常见的10个问题及处理方法(21)](https://www.cnblogs.com/jiujuan/p/18794416)
- [4\. 程序员怎么做沟通？聊一聊程序员沟通相关的问题(18)](https://www.cnblogs.com/jiujuan/p/18029741)
- [5\. 技术管理：搭建团队研发管理体系的一个框架概述(14)](https://www.cnblogs.com/jiujuan/p/19291044)

点击右上角即可分享

![微信分享提示](https://img2023.cnblogs.com/blog/35695/202309/35695-20230906145857937-1471873834.gif)

[Fork me on GitHub](https://github.com/jiujuan "Fork me on GitHub")

CONTENTS

✕

- 1\. 一、什么是提示词
- 1.1. 提示词是什么
- 1.2. 提示词与LLM的关系
- 1.3. 提示词工作原理
- 2\. 二、提示词的基本构成
- 2.1. 提示词要素基本构成
- 2.2. 指令：告诉模型做什么
- 2.3. 上下文：提供背景信息
- 2.4. 输入数据：需要处理的内容
- 2.5. 输出格式：期望的响应形式
- 3\. 三、提示词技术
- 3.1. 零样本提示
- 3.2. 单样本和少样本提示
- 3.2.1. 单样本和少样本提示介绍
- 3.2.2. 少样本提示Few-shot要点
- 3.2.3. 少样本提示限制
- 4\. 四、提示词工程
- 4.1. 什么是提示词工程
- 4.2. 提示词工程的核心组成
- 5\. 五、高级提示词技术
- 5.1. 思维链提示词
- 5.2. 自我一致性提示词
- 5.3. 链式提示词
- 6\. 六、参考

![](<Base64-Image-Removed>)

[Previous image](https://www.cnblogs.com/jiujuan/p/19855636)[Next image](https://www.cnblogs.com/jiujuan/p/19855636)

### 来源 3: 高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云

- URL: https://cloud.tencent.com/developer/article/2498790
- 精读方法：firecrawl-scrape

[fanstuck](https://cloud.tencent.com/developer/user/9822651)

## 高效速搭基于DeepSeek的招标文书智能写作Agent

原创

关注作者

[_腾讯云_](https://cloud.tencent.com/?from=20060&from_column=20060)

[_开发者社区_](https://cloud.tencent.com/developer)

[文档](https://cloud.tencent.com/document/product?from=20702&from_column=20702) [建议反馈](https://cloud.tencent.com/voc/?from=20703&from_column=20703) [控制台](https://console.cloud.tencent.com/?from=20063&from_column=20063)

登录/注册

[首页](https://cloud.tencent.com/developer)

学习

活动

专区

圈层

工具

[MCP广场![](https://qccommunity.qcloudimg.com/image/new.png)](https://cloud.tencent.com/developer/mcp)

文章/答案/技术大牛搜索

搜索关闭

发布

fanstuck

[社区首页](https://cloud.tencent.com/developer) > [专栏](https://cloud.tencent.com/developer/column) >高效速搭基于DeepSeek的招标文书智能写作Agent

# 高效速搭基于DeepSeek的招标文书智能写作Agent

原创

发布于 2025-02-23 08:46:00

发布于 2025-02-23 08:46:00

6.2K0

举报

文章被收录于专栏：[人工智能项目落地实战](https://cloud.tencent.com/developer/column/104618)人工智能项目落地实战

## **高效速搭基于DeepSeek的招标文书智能写作Agent**

## **前言**

如果你一直在跟着博主的脚步探索AI大模型的相关内容，从最初的大模型Prompt工程解析，到实际的开发部署，再到深入NL2SQL、知识图谱大模型和ChatBI等更高阶应用，应该已经感受到了我们一步一个脚印，从迈过一道道技术难关，到搭建起属于自己的技术桥梁的过程。如今，我们或许对大模型的开发已经有些轻车熟路，但也必须承认，技术的迭代速度实在太快了。要想跟上AI技术发展的步伐，把最新的人工智能技术融入现有业务和应用场景才是我们追求的最终目标。

随着AI技术的飞速发展，传统的招标文书写作方式面临着诸多挑战，尤其是在效率、准确性和一致性方面。如何利用AI技术有效应对这些挑战，提升写作效率，已经成为我们追求的目标之一。

![](https://developer.qcloudimg.com/http-save/yehe-9822651/1cfdd4fd8777ea39c6f212ee068ce05c.gif)

那么为什么今天要写这篇文章呢？因为在招标文书的写作过程中，我们往往需要面对大量的标准化内容和复杂的格式要求。如何在短时间内生成符合需求的高质量文书，成为了许多企业亟需解决的问题。AI技术，特别是基于DeepSeek的大模型，正是解决这一难题的关键。通过智能写作Agent，我们不仅能有效提升文书生成的速度，还能确保文书内容的精准性和专业性。

好了，不再赘述，让我们直接进入今天的主题。我将通过通俗易懂的语言为大家详细解读如何基于DeepSeek快速搭建招标文书智能写作Agent，助力提高招标文书的编写效率。有更多感悟以及有关大模型的相关想法可随时联系博主深层讨论，我是Fanstuck，致力于将复杂的技术知识以易懂的方式传递给读者，热衷于分享最新的行业动向和技术趋势。如果你对大模型的创新应用、AI技术发展以及实际落地实践感兴趣，那么请关注Fanstuck。

## **一、 引言**

### **1.1 传统招标文书写作的挑战**

招标文书的写作一直是一个让许多人感到头痛的工作。首先， **格式要求繁琐** 是一个普遍问题。招标文书通常需要遵循一套严格的格式，不同的部分要求不同的排版、字体和段落设置。每个细节都需要小心处理，否则文书就会显得不够专业。这些格式要求往往要求写作者在文书初稿完成后还要反复修改和调整。

其次， **信息量庞大且复杂**。一个典型的招标文书包含的内容非常多，比如项目背景、投标要求、评标标准、合同条款等。这些内容需要被精确地描述出来，同时避免冗长和重复。为了确保准确无误，每一项内容都需要反复核对，这就大大增加了写作的难度和时间。

最后， **时间紧迫** 也是招标文书写作中的常见问题。许多招标项目的时间表都非常紧张，文书通常需要在极短的时间内完成。尤其是涉及到多个部门或团队的协作时，时间的压力更是倍增。由于工作量大，且要求高，写作者常常面临着无法在规定时间内完成任务的困境。

![](https://developer.qcloudimg.com/http-save/yehe-9822651/9dbcc1a43fb0cf453fa76cef53b9c2d6.png)

### **1.2 市场上的痛点**

在招标文书的实际操作中，这些挑战变得尤为明显，尤其是当面对 **大规模招标项目** 时。随着项目规模的扩大，文书的复杂度和工作量也随之增加。传统的人工写作方法在这种情况下往往难以应对，出现了以下几个痛点：

- **效率低下**：招标文书的写作往往需要多次修改与反馈，而每一轮修改都可能导致进度拖慢。特别是当需要与多个团队进行协作时，沟通与协调就变得尤为繁琐，整体效率受限。
- **易出错**：在频繁修改和调整的过程中，人工写作不可避免地会出现错误。这些错误可能是格式不一致、内容重复，或者在细节上的疏漏。而这些看似不起眼的小错误，往往会影响文书的整体质量，甚至影响项目的评审结果。
- **文档一致性差**：招标文书通常由多个团队成员共同编写，然而每个人的写作风格和表达方式不同，这导致文档整体的一致性差，甚至会出现前后内容矛盾的情况。

这些问题不仅增加了企业的成本，也降低了招标文书的质量，进而影响到企业的竞争力。因此，提升招标文书写作效率、减少错误和确保文档质量，已经成为摆在我们面前的紧迫任务。

从最早的“模板式填充”到如今的“大模型文本生成”，生成式AI为高效撰写各类文档提供了更多可能。然而，大多数通用型大模型（例如一些热门英文模型）在应对专业领域尤其是中文招标文书时，往往会出现：

1. **缺乏中文领域的专业优化**：生成结果存在词汇、格式或专业度上的不足。
2. **对标书写作这种强格式化需求应对不足**：不够灵活或格式不够精准。
3. **难以在复杂环境中落地**：如大模型需要大量算力或商业化部署尚不成熟，令企业望而却步。

那么如今通过生成式人工智能我们又能结合招标文书写作业务，带给我们什么新的启发呢？

![](https://developer.qcloudimg.com/http-save/yehe-9822651/903aa878cfc2cf95d88a9830295ec337.png)

### **1.3 AI辅助写作的优势**

要真正理解AI如何在招标文书写作中提供帮助，我们首先需要明确哪些环节是AI可以介入的。在招标文书的撰写过程中，很多环节都可以通过AI进行优化，从而提高写作效率和文档质量。

#### **1.3.1 挖掘AI介入的场景**

![](https://developer.qcloudimg.com/http-save/yehe-9822651/4e2989e7ca7af3d4837d4013f5bccd44.png)

**自动化内容生成**：许多招标文书包含大量标准化的内容，如项目介绍、公司资质、投标要求等。AI 可以根据项目基本信息，自动生成这些标准化部分的初步草稿。比如，当招标文书需要介绍某公司背景时，AI 可以根据提供的公司信息，快速生成符合格式的公司介绍段落，极大地节省了人工编写时间。此外，对于招标项目的技术方案描述，AI 能依据过往类似项目的成功案例和当前项目的特殊需求，生成针对性的技术路线阐述，让技术方案的起草更高效。

**信息提取与整合**：在招标文书中，很多内容涉及到多个来源的整合。比如评标标准、招标要求等需要从招标文件、法律法规、历史项目等多个渠道中提取并整合相关信息。AI 可以通过 [自然语言处理](https://cloud.tencent.com/developer/techpedia/1502?from_column=20065&from=20065) 技术，从大量的文本中快速提取出关键信息，自动填充到文书中，减少人工查找与整理的工作量。同时，AI 还能从行业动态资讯中提取最新的政策导向和市场趋势，融入到招标文书里，使招标内容更贴合当下形势。

**格式校对与一致性检查**：招标文书的格式要求非常严格，尤其是对于多个章节、表格、标题等的统一排版。AI 可以自动检查文书的格式是否符合要求，包括字体、标题级别、表格布局等。同时，AI 还可以确保文档的风格一致，避免不同部分的写作风格不统一，减少人为错误。AI 还能对文档中的图表编号、交叉引用等进行智能检查与修正，保证文档的严谨性。

**多轮反馈与内容优化**：招标文书的写作过程中，经常需要多次修改和反馈。AI 可以根据用户的反馈，快速生成修改后的文书内容，并进行内容优化。例如，在修改一部分条款时，AI 能够在保证其他部分一致性的基础上，迅速调整相关内容，提高修改效率。当客户提出更注重成本控制的反馈时，AI 不仅能修改预算相关条款，还能联动修改与之相关的成本效益分析部分，使整个文书逻辑更连贯。

**风险评估与预警**：AI 可通过分析过往招标项目的风险案例和当前市场环境，对招标文书中的潜在风险进行评估。如评估合同条款中可能存在的法律风险、项目实施过程中的进度风险等，并给出相应的预警和应对建议，帮助招标方提前规避风险。

**智能问答与辅助决策**：在招标文书撰写过程中，工作人员可能会遇到各种问题，如某项法规的具体要求、某类项目的常见评标指标等。AI 可以作为智能问答助手，实时解答这些问题，为决策提供参考依据，助力工作人员做出更合理的决策。

#### **1.3.2 传统写作 vs AI辅助写作**

传统的招标文书写作与AI辅助写作有着显著的区别。传统写作往往依赖人工进行文书撰写、修改和校对，而AI辅助写作则通过自动化和智能化技术提供支持。下面通过一张对比表格来清晰展示两者在多个方面的差异：

| 方面 | 传统写作 | AI辅助写作 |
| --- | --- | --- |
| 写作效率 | 人工编写文书需要大量时间，尤其是重复性的部分（如标准化内容）需要反复编写和修改。 | AI可以快速生成标准化内容，自动填充模板，大幅节省写作时间。 |
| 错误率 | 容易出现人为错误，如格式不统一、信息遗漏、内容重复等。 | AI根据统一的模板和规则生成内容，减少人为错误，确保准确性。 |
| 一致性 | 多人参与时，风格和格式容易不一致，文档中的部分内容可能会相互矛盾。 | AI保持统一风格和格式，确保文档内容的一致性和规范性。 |
| 时间压力 | 在紧迫的时间限制下，可能会导致文书质量下降，无法完成细致的修改。 | AI能够迅速响应需求变动，并根据反馈进行快速修改，减少时间压力。 |
| 多轮修改 | 修改过程繁琐，通常需要多个团队反复协作和沟通，效率低下。 | AI可以根据反馈快速调整内容，确保多轮修改顺畅且高效。 |
| 信息整合 | 需要手动查找和整合大量的资料，容易出现遗漏或重复。 | AI能够自动提取、整合关键信息，快速填充并生成文书内容。 |
| 适应需求变动 | 对于需求的变动反应迟缓，修改过程往往需要大量人工干预。 | AI可以根据新的输入和反馈迅速调整文书内容，灵活应对需求变动。 |
| 文档格式校对 | 需要人工检查格式、字体、排版等，易出现漏检或格式不一致的问题。 | AI可以自动检查文档格式，确保每个部分符合要求，并统一风格。 |

那么到现在我们已经清楚了目前市面上存在的痛点挑战和了解了AI辅助写作的优势，但是我们应该采取哪些技术实现AI辅助标书写作呢？接下来一章我们就开始阐述技术如何实现。

## **二、智能写作Agent的引入**

### **2.1什么是 AI Agent？**

![](https://developer.qcloudimg.com/http-save/yehe-9822651/4ea320c45b0be84d46410d230d226a2c.png)

AI Agent，即人工智能智能体，是一种能够感知其所处环境，并根据环境信息自主采取行动以实现特定目标的计算系统。从本质上讲，AI Agent 具备自主性、反应性、主动性和社会性这四大核心特点。

自主性使其能够在没有人类直接干预的情况下，基于自身内置的算法和规则，独立地做出决策并执行相应行动。例如，在自动驾驶领域的 AI Agent，能根据路况、交通信号等实时信息，自主决定车辆的行驶速度、方向和刹车时机 。反应性则体现在 AI Agent 可以及时感知环境变化，并迅速做出与之对应的反应。以智能安防系统中的 AI Agent 为例，一旦检测到异常的入侵行为，它能立即触发警报并通知相关人员。

主动性意味着 AI Agent 不仅仅是被动地对环境刺激做出反应，还能主动地采取行动以实现目标。比如智能客服 AI Agent，除了回答用户的提问，还能主动询问用户是否需要进一步的帮助，推荐相关产品或服务。而社会性则表现在 AI Agent 可以与其他智能体或人类进行交互协作，共同完成复杂任务。在智能工厂中，不同的 AI Agent 可以协同工作，完成生产线上的各种工序。

与传统 AI 相比，AI Agent 具有更强的适应性和灵活性。传统 AI 通常是针对特定任务进行设计和训练的，如图像识别、语音识别等，缺乏对复杂动态环境的自主应对能力。而 AI Agent 能够在不同的环境条件下，根据目标灵活调整策略，具有更广泛的应用前景。

在招标文书写作领域，AI Agent 的应用潜力巨大。它可以深入理解招标要求，自动收集和整理相关信息，结合丰富的行业知识和写作经验，快速生成高质量的招标文书。通过对大量历史招标文书和行业标准的学习，AI Agent 能够精准把握不同类型招标文书的写作规范和重点，避免人为疏忽和错误，大大提高写作效率和质量。

### **2.2 招标文书智能写作 Agent**

简单来说，它是一个可以自动生成招标文书的智能系统。想象一下，当你要进行一个大型建筑项目的招标时，只需将项目的基本信息，如项目规模、预期工期、建筑类型等输入到这个智能系统中，它就能迅速根据这些信息，结合自身学习到的知识，快速生成符合要求的招标文书初稿。而且，它不会固步自封，会在不断的使用过程中，根据用户的反馈和新的数据，持续学习、优化，就像一位经验越来越丰富的写手，文书质量和生成效率也会越来越高。

#### **2.2.1 自动分析招标文件要求，生成结构化内容**

在传统的招标文书写作中，文书的每一部分都需要手动输入并确保信息的准确性和一致性。这往往需要大量的时间和精力，尤其是在处理那些标准化和重复性较高的内容时。而智能写作Agent则能够自动化地生成这些内容，大大节省了时间，并减少了人为疏漏。

假设某企业需要为一个关于“城市基础设施建设”的招标项目编写文书。传统写作中，编写人员需要从项目的背景、目标、招标要求等信息中提取出关键信息，逐条手动编写。而智能Agent则可以通过输入一些基本的项目数据，自动生成项目概述部分的内容。

例如，智能Agent在获取到以下关键信息后：

- 项目名称：城市基础设施建设
- 项目目标：提升城市交通流畅度、减少交通拥堵
- 招标要求：项目需符合国家环保和城市建设规范

Agent可以自动生成如下内容：

> **项目概述**：本项目旨在通过提升城市基础设施建设，改善交通流畅度，减少交通拥堵，推动城市可持续发展。投标方需要遵守国家相关环保法规，并确保项目符合城市建设规范，确保高效施工与资金使用。

![](https://developer.qcloudimg.com/http-save/yehe-9822651/369a4950deea5961238b37d76636288f.png)

这种自动化生成的内容确保了格式的统一，同时也能根据实际情况进行快速修改和调整。

#### **2.2.2 根据不同需求和客户特点，智能修改和调整文书中的条款与措辞**

不同的招标项目可能涉及不同的行业、领域和客户需求，而每一份招标文书都需要根据这些特定要求进行调整。传统写作中，修改和定制文书内容常常需要耗费大量的时间和精力。智能写作Agent则能够根据投标项目的特点，自动修改和调整文书中的条款与措辞，使其更加符合具体的需求。

例如，某项目要求投标方提供符合环保合规性的证明。智能Agent可以根据招标文件中的相关条款，自动调整文书中关于环保合规的描述，并根据不同项目的标准，提供不同的措辞。如果项目要求对环保合规性进行严格审查，智能Agent能够根据具体的环保法律要求，调整文书中的措辞，使之符合最新的环保标准。

![](https://developer.qcloudimg.com/http-save/yehe-9822651/0fc333f5ded7c3b69021e5d2e551fc73.png)

另外，如果客户要求的技术规范更加严格，智能Agent也能够自动根据客户需求，调整技术方案部分的细节。例如，当客户要求在招标文书中加入“高效能绿色材料”条款时，智能Agent会自动更新文书中的相关部分，并生成符合要求的描述。

#### **2.2.3 提供文书写作的实时建议与反馈，确保内容质量和符合标准**

传统写作中，完成初稿后往往需要多次修改和校对，这不仅耗时，还容易出现遗漏。智能写作Agent的另一大优势是能够提供实时的写作建议与反馈。在写作过程中，智能Agent能够自动检测文书中的潜在问题，并根据已知的标准提供修改建议。

在编写合同条款时，智能Agent能够实时检测条款中的措辞是否规范、是否符合最新的法律法规或行业标准。例如，当写作者编写“违约责任”条款时，智能Agent会检查是否符合相关法律法规，并提醒写作者对措辞进行修改。例如，如果发现“违约方应支付合同总额的10%作为赔偿”的表述不符合法律要求，智能Agent会建议改为“违约方应支付合同总额的10%，并按实际损失进行赔偿”。除此之外，通过联网搜索功能和知识库能力，可以实时反馈优化了合同条款中的法律措辞，确保文书符合当地最新的政策要求。通过这一过程，企业不仅提高了写作效率，还确保了招标文书的合规性和高质量。

![](https://developer.qcloudimg.com/http-save/yehe-9822651/b5eaaa326bd13cd20244636f9aa1a62d.png)

## **三、为什么选择DeepSeek作为写作大模型**

DeepSeek在中文语义理解精准度达99.7%，远高于OpenAI的92%，且兼容方言及行业术语。。它在中文文本生成上具备优异表现，同时兼顾“规则化”与“非规则化”两种需求，使得招标文书写作可以又快又准。选择DeepSeek作为核心技术底座，源于其在中文场景的 **三重差异化优势**（数据来源：深度求索2024年技术白皮书）：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/139fbb4ef7d1456b144bce14513e6930.png)

- **领域知识增强**：DeepSeek采用了 **稀疏注意力机制** 和 **混合专家架构（MoE）**，这些技术使得模型在处理大量数据时不仅更精准，而且大大降低了计算资源的消耗。例如，DeepSeek-V3通过仅使用10%的参数量就能达到GPT-4的80%性能。这就像你把一台强大的计算机压缩到更小的体积，仍能保持较强的运算能力。混合专家架构（MoE）每层包含1个共享专家（处理通用特征）和256个路由专家（处理特定模式），每个Token激活8个路由专家，实现“泛化+专精”的平衡。传统方法依赖辅助损失函数平衡负载，而DeepSeek通过动态偏置调整专家利用率，避免额外损失干扰训练目标。例如，在训练中实时监测专家负载，动态调整路由策略，使专家利用率差异小于5%。
- **训练数据与效率**：DeepSeek的训练策略也相当创新。它采用了较少的数据，通过精确的训练过程，达到了与其他万亿参数模型相当的效果。举个例子，DeepSeek-R1在处理金融领域的推理任务时，能快速解析股市行情、政策变动等复杂因素，生成高效的决策建议。相比之下，GPT-4需要更大的数据集和更多的计算资源才能完成类似的任务。DeepSeek-R1在多模态能力方面也有所突破，能够处理复杂的数学和编程任务，展现出强大的推理和生成能力。在AIME 2024等基准测试中，DeepSeek-R1的蒸馏模型在数学和编程任务上取得了优异的成绩。

DeepSeek-R1 在后训练阶段大规模使用了强化学习技术，在仅有极少标注数据的情况下，极大提升了模型推理能力。在数学、代码、自然语言推理等任务上，性能比肩 OpenAI o1 正式版。

![](https://developer.qcloudimg.com/http-save/yehe-9822651/0be9204d476646290ddfa42737566cf0.png)

### **3.1.对标书行业术语的精准捕捉**

招标文书写作并非简单的文字罗列，而是往往需要恰当地使用各种专业词汇和术语。例如，“投标响应”“资质证明”“技术规范”等关键词在不同标书中出现的语义背景可能略有差异。DeepSeek的预训练语料库覆盖了广泛的公开可用文本，包括技术、科学、法律和商业等领域的内容。但实际测试使用下来，能达到较多场景业务语料的捕捉：

- **多义词区分**：如“响应”在技术方案中指向“功能响应速度”，在商务条款中指向“招标要求响应程度”；
- **行业特异性**：建筑行业的“工程量清单计价规范”与医疗行业的“医疗器械注册证编号”精准对应；
- **法规联动**：自动关联“《政府采购法》第二十二条”与“供应商资格条件”的强制性表述。

| 类别 | 典型术语 |
| --- | --- |
| 法律条款 | 不可抗力条款、知识产权归属、履约保证金 |
| 技术规范 | 国标GB/T 19001-2016、非标设备参数、验收测试标准（FAT/SAT） |
| 商务流程 | 投标截止时间、唱标记录、评标委员会组成 |

虽然标书相关的术语可能包含在通用商业或法律文本中，但DeepSeek并未专门披露其训练数据的细分类别。因此，无法确认标书行业术语是否被明确包含。建议通过实际应用场景测试模型表现，若需更高专业度，可考虑基于领域数据进行微调。对于关键任务，建议结合人工审核以确保准确性。

### **3.2 对招标方隐含需求的上下文推理**

招标单位常常不会在招标文件中把所有期望都直白地列出，而是通过条款、评分细则甚至语气暗示来传达一些潜在诉求，如对项目周期的优先考虑、对技术创新的偏好、对维护与售后的严格要求等。传统的自动写作工具只能照搬已有模板，难以真正理解这些隐含信息。而DeepSeek通过Transformer的多头注意力机制和大规模上下文建模能力，能在阅读或获取需求描述时捕捉到背后的深层次动机，并在生成“技术方案”或“项目亮点”段落时，主动强调满足这类隐含需求的要点——从而让标书更具说服力。

**上下文感知的术语生成**

动态术语适配： 通过注意力机制优化，模型能够根据上下文动态调整术语使用。例如：

- 当输入提示包含“EPC总承包项目”时，自动触发关联术语：

代码语言：javascript

AI代码解释

复制

```javascript

```

- 在“技术方案”章节生成时，优先使用“技术参数偏离表”“实施方案拓扑图”等组合术语，而非孤立词汇。

错误修正案例： 某招标文件要求供应商提供“ISO 9001质量管理体系认证”，若用户误写为“ISO 9000”，模型将自动触发纠错机制：

代码语言：javascript

AI代码解释

复制

```javascript

```

如果招标文件中提到“工期紧张”“需与其他承建方协同”，DeepSeek会在技术方案或项目管理计划中突出“多方同步”“资源调配灵活性”的内容，并在排期表中体现对工期的优先安排，真正让投标文件“对症下药”。

### **3.3规则化与非规则化内容的融合生成**

相比规则化条款，像“技术解决方案”“项目背景分析”以及“服务承诺”这类内容更具弹性。编写者往往需要在满足基本要求的前提下尽可能突出自身优势，让评审方快速get到项目的独特价值。DeepSeek在此环节的作用尤为明显：

- 灵活表达：得益于大模型对丰富词汇和句式结构的掌握，DeepSeek可以在保持核心信息不变的前提下，灵活变换说服性语言、展现项目卖点。
- 多样化生成：若用户对初版文本不满意，可以在prompt中补充新的提示或期望风格，让DeepSeek再生成一版不同的表达方案。例如，希望突出“节能减排”，就可在提示中加上“请在本段突出环保可持续优势”之类指令，模型便能在新一轮生成中更加聚焦这方面亮点。

### **3.4格式控制能力**

在招标文书里，文字本身固然重要，然而“如何呈现”同样关键。评审人员通常在审阅标书时，对清晰的标题结构、图表插入、要点突出都有较高要求。一旦格式出现混乱或章节编号不对应，往往会给人留下“不专业”的印象。

#### **3.4.1 支持Markdown / LaTeX等格式输出**

不少企业或机构在撰写招标文档时，习惯先用Markdown或LaTeX做初步排版，再导出成Word、PDF或HTML。DeepSeek在接收带有格式指令的prompt时，可以按照相应的语法规则生成带标题、列表、表格、引用等格式的文本。这样一来，就能大大降低后续在排版或转换环节的人工工作量。

- 以Markdown形式生成二级标题“2.1 技术方案”或在文中插入表格，DeepSeek能精准处理如“\|列1\|列2\|”之类的表格语法。
- 若需要在LaTeX格式标书中插入公式或图表引用，模型也能按照`\begin{table} ... \end{table}`、`\label{fig:xxx}`的方式进行排版。

#### **3.4.2 多段落协同生成与逻辑一致性**

招标文书通常不止一个独立章节，比如“技术方案”和“实施计划”就存在较强的互相呼应关系。如果在“技术方案”里承诺要采用某种技术架构，那么在“实施计划”部分便要有与之相匹配的时间安排、资源调度说明。一旦前后不一致，很容易在评审时被扣分。

- **上下文信息全局掌控**：DeepSeek在调用时，可将已生成的文本或项目概要以上下文形式输入，让模型在输出后续章节时自动保证逻辑匹配。
- **自动衔接与引用**：例如“在上一节提到的Docker容器部署方案”这类衔接句，DeepSeek能自然地插入到新生成的文本中，体现出前后内容是一个整体方案。

很多用户在实际使用过程中，习惯先让DeepSeek逐个生成各章节的主体内容，然后做一次整体复审。如果发现某些段落与前文描述不符，就将这些关键信息再次输入模型进行“二次校验生成”，从而让全篇文档的风格与内容更协调。

## **四、基于腾讯云智能体开发平台 LKE的DeepSeek私有知识库搭建与RA** G增强

此项目将根据腾讯云智能体开发平台 LKE开源于GitHub和腾讯云文档中心以及腾讯云社区，首先项目思路和架构分为两个方案，分别对应不同读者学习实践，面向两个主体群体，因此采取的策略也不同。如果对开发不是很熟悉，又想快速实践落地大模型DeepSeek+私有数据库GAG增强，那么首推LKE平台来部署。如果是开发者，那么我这边将根据第三方原子开发能力，在服务器上面进行架构搭建，会很好理解。

### **4.1 基于腾讯云智能体开发平台LK** E实现

因涉及到私有化知识库搭建和模型部署这些技术较深的技术栈，化繁为简使用腾讯云智能体开发平台 LKE就可以很好快速实现项目的落地。首先我介绍一下LKE：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/2204d12bfbc2bae6191c87e79f5f0e0b.png)

腾讯云智能体开发平台（LLM Knowledge Engine）简单来说就是AI Agent [低代码平台](https://cloud.tencent.com/product/weda?from_column=20065&from=20065)，提供多种应用开发方式，能完成企业级Agent、RAG、工作流应用创建及发布，预置优质官方插件，助力企业降低大模型应用落地门槛，高效打造效果佳、有价值的大模型应用。在项目初期验证场景上面很实用，能快速反馈问题并调整方案。

打开腾讯云智能体开发平台，进入到应用管理，然后创建应用：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/c537e2205837b68e02508f440afa0de3.png)

然后我们就能看到AI Agent页面：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/d708fc0b4e20e16595fd7ec23c8ab08e.png)

#### **4.1.1模型配置**

我们先具体来了解如何利用低代码平台搭建一个相对功能完善且效果较好的AI Agent。腾讯云智能体开发平台目前已接入精调知识大模型、混元大模型、行业大模型、DeepSeek 等十余种模型，各模型详情及适用场景如下：

| 模型名称 | 最大输入 | 最大输出 | 场景描述 |
| --- | --- | --- | --- |
| 精调知识大模型高级版 | 7k | 1～4k | 适用于企业知识问答场景，支持图文表答案关联输出、数学计算、逻辑推理、表格问答等复杂场景 |
| 精调知识大模型标准版 | 7k | 1～4k | 适用于企业知识问答场景，性价比高，支持图文关联输出 |
| 混元大模型高级版 | 28k | 4k | 万亿级参数，支持复杂指令和推理，具备数学能力，适用于多语言翻译、金融法律医疗等领域 |
| 混元大模型标准版 | 30k | 2k | MOE-32k 性价比高，适合长文本输入处理 |
| 混元大模型Turbo版 | 28k | 4k | 使用混合专家模型（MoE），推理效率快，效果强 |
| 混元大模型长文本版 | 250k | 6k | 支持长文本，MOE-256k 在长度和效果上突破 |
| 混元大模型角色扮演版 | 28k | 4k | 结合角色扮演数据集增训，适合角色扮演场景 |
| 金融行业大模型标准版 | 7k | 1～4k | 针对金融领域问答，适用于投资、金融产品问答 |
| 教育行业大模型标准版 | 7k | 1～4k | 适用于英语口语对话练习和教案场景，支持语法分析、教材课后对话练习等 |
| 教育行业大模型高级版 | 7k | 1～4k | 深度训练，提升英语口语自然度和任务遵循度，支持丰富教案生成 |
| 医学行业大模型标准版 | 3.4k | 500 | 适用于医学知识问答、电子病历生成等医疗领域应用 |
| DeepSeek-R1 | 32k | - | 强化学习驱动的推理模型，适用于数学、代码、推理任务 |
| DeepSeek-V3 | 32k | - | 6710亿参数的MoE模型，优化推理和训练效率 |

根据需要选择模型，这里我们使用DeepSeek-R1来进行部署验证：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/1c8ce3472cdcbc786e5c14c9e2e0c4c5.png)

其中关于上下文联动功能可以根据业务场景自动调整，比如我只做一次性问答模块，就用不着上下文关联，关闭就可以节省tokens。

- 上下文改写：开启开关后，可结合上下文 [内容识别](https://cloud.tencent.com/developer/techpedia/1056?from_column=20065&from=20065) 指代对象或省略词，改写本轮问句并生成连贯答案。
- 上下文记忆轮数：设置输入给大模型作为 prompt 的上下文对话历史轮数。轮数越多，多轮对话的相关性越高，但消耗的 token 也越多。

开通腾讯云智能体开发平台服务即获赠累计50万 tokens 的免费调用额度，有效期2个月；以资源包的形式发放到腾讯云账号中，优先扣除。（模型通用）。

![](https://developer.qcloudimg.com/http-save/yehe-9822651/afb5409fe0c7d39ed734d32191a4d7a2.png)

其中对于模型的高级设置需要根据实际业务情况来调整：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/a5bedca8bf960ecb6c536e9a8021b167.png)

我们需要先明白温度和top p这两个参数的概念：

- 温度：调高温度会使得模型的输出更多样性和随机性，适用于创造性要求高的场景，如诗歌创作。反之，降低温度会使得输出的内容更遵循指令，适用于确定性要求高的场景，如代码生成。
- Top P：Top P 为累计概率，模型在生成输出时，会从概率最高的词汇开始选择，直到词汇总概率累计达到 Top P 值。可以限制模型只选择这些高概率的词汇，从而控制输出内容的多样性。取值越大，生成内容的多样性越强。

涉及到容错率相当低的审核效验场景，此时温度推荐为0.2以下，也就是适应政务这块，如果是娱乐创作，则可以适当调高。Top P可能大家有点难理解，我这里做个案例：

假设模型生成下一个词时，有 “苹果”“香蕉”“橙子”“草莓” 等一系列候选词，每个词都有对应的生成概率。

当设定 Top P 值为 0.8 时，模型会从概率最高的词开始累加概率。比如 “苹果” 概率是 0.3，“香蕉” 概率是 0.25，“橙子” 概率是 0.15 ，“草莓” 概率是 0.1，这几个词概率依次累加，“苹果”+“香蕉” 概率为 0.55，再加上 “橙子” 时，累计概率达到 0.7 ，还未达到 0.8，继续加上 “草莓”，累计概率达到 0.8 ，此时就停止累加。

最终，模型只会从 “苹果”“香蕉”“橙子”“草莓” 这几个词中选择下一个生成的词，而不会考虑其他概率更低的词 。这样就通过 Top P 值限制了模型选词的范围，从而一定程度上控制了输出内容的多样性。如果将 Top P 值设得更大，比如 0.95，那就会纳入更多概率相对没那么高的词，生成内容的多样性也就更强。

#### **4.1.2角色指令**

也就是我们说的Prompt工程，关于Prompt工程博主撰写的详细的专栏从入门到精通 [Prompt工程师上手指南](https://cloud.tencent.com/developer/column/104616?from_column=20421&from=20421)，专栏内容循序渐进，从基础原理和入门实践讲起。对于初学者，能轻松理解基础概念，为后续学习筑牢根基；有经验的开发者，则可直接跳转到主流策略、引导策略、RAG（检索增强生成）、思维树（ToT）与避免幻觉（Hallucination）等策略章节，获取前沿高阶技术经验：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/90f0315d6bb75337a7465635768b1ff1.png)

再次我就不做过多介绍Prompt，感兴趣的朋友去看本人专栏即可，关于Prompt的写作我这边先给出大家可作参考：

代码语言：javascript

AI代码解释

复制

```javascript

```

**优化亮点解析**

1. **角色权威性构建**：通过添加专业资质编号、知识库版本等细节，增强AI的专业可信度。
2. **结构化示例驱动**：在关键部分嵌入标准模板，引导AI按规范格式输出。
3. **动态风险管控**：引入自动标注系统和法律条款校验机制，降低合规风险。
4. **量化指标体系**：将主观描述转化为可测量的评分模型，提升评标标准的客观性。
5. **交互式澄清机制**：通过选择题式提问解决用户需求模糊的问题，符合反向提问技巧。

建议在实际测试中重点关注：

1. 使用链式验证方法：让AI先输出大纲框架，经用户确认后再填充细节。
2. 启用版本对比功能：保存每次修改记录，方便追溯条款变更过程。
3. 集成法规数据库：对接政府采购网API实时获取最新政策依据。

如需进一步调优，可参考针对性地添加"避免法律术语堆砌""关键条款重复强调"等细化要求。

#### **4.1.3欢迎语**

可以编写引导语，填写欢迎语后，会在客户侧首页展示欢迎语内容，比如：

代码语言：javascript

AI代码解释

复制

```javascript

```

![](https://developer.qcloudimg.com/http-save/yehe-9822651/87b66be8b7a55f759ed7003d622f7bcb.png)

#### **4.1.4知识库**

在页面知识库看到我们可以根据文档来上传知识，点击知识管理我们可以更好处理知识库中的数据。

![](https://developer.qcloudimg.com/http-save/yehe-9822651/02b2daf902fe12edbfa763be54a8c69d.png)

![](https://developer.qcloudimg.com/http-save/yehe-9822651/e7c722adc0ad4d706410345ab34a5fd6.png)

##### **网页导入**

其中网页导入可以需要输入备案和企业主体一致的网址，比如我们想要获取中华人民共和国招标投标法，只需要获取到有关该律法的网站URL，输入即可获取文档：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/b1a97c560835dfabf347a77e9dc3bbfb.png)

而且支持直接修改并且可保存为文档：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/ac6d269762ba9aa1606352687c1e930b.png)

等待解析完即可。

##### **文件导入**

文件导入也十分简单方便。

![](https://developer.qcloudimg.com/http-save/yehe-9822651/a001e11696b21b012572794fa78fbc09.png)

**导入本地文档条件：**

- 支持 pdf、doc、docx、ppt、pptx 格式，大小限制：200MB。
- 支持 xlsx、xls、md、txt、csv 格式，大小限制：20MB。
- 支持导入带文字的图片，包括 png、jpg、jpeg 格式，大小限制：50MB，长宽比不超过1:7。
- 表格文件（ xlsx、xls、csv 格式）最大支持1万行、100列数据，建议一个 sheet 只存放一张表格，表格中出现全空行数据将影响问答效果。
- 支持批量导入文档。

##### **知识库设置**

需要主要的是知识库设置：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/9c162a56b55e5c78275d4a0e32d41852.png)

首先是知识库检索范围设置：知识库检索范围设置用于配置 API 参数和标签名称的映射关系，实现不同身份用户提问检索不同的知识范围的场景。

##### **如何选择“且”与“或”**

**设置选择 API 参数为“且”**

传入多个参数映射多个标签时，会检索 **同时包含多个标签的知识** 以及未打标签的知识。

以上诉案例为例，最终结果：检索 “用户身份” 为 “内部员工” 且 “部门” 为 “产品部” 的知识，以及未打标签的知识。

**设置选择 API 参数为“或”**

传入多个参数映射多个标签时，会检索 **包含任意标签的知识** 以及未打标签的知识。

以上诉案例为例，最终结果：检索 “用户身份” 为 “内部员工” 的知识、 “部门” 为 “产品部” 的知识、以及未打标签的知识。

基于此我们可以配置不同的地区适配地域化差距更大的律法类目，实现差异化管理地方数据类目：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/bc3617829b4d0a404bea0e0ff0b94aa0.png)

##### **文档召回**

- **文档召回数量**：指系统在处理用户问题等请求时，从知识库中检索并返回的相关文档的数量。比设置为 4，意味着系统会找出最相关的 4 篇文档，为后续生成答案等操作提供信息支撑。
- **文档检索匹配度**：用于衡量用户输入与知识库中文档之间的匹配程度的阈值。像设置为 0.2，当某个文档与用户输入的匹配度达到或超过 0.2 时，才会被作为相关文档召回。这一设置可控制召回文档的精准度，数值越高，召回的文档越贴合用户输入。

这里还有更高阶的用法，也就是将文档切分为chunk，这里暂时不清楚腾讯云是否做了文档切分，这里我做较为专业细致的解读：

首先我们需要明确RAG的大致过程：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/214a752a061f338a644602d6f3e61372.png)

根据上图我们可以了解prompt是一个其实是一个智能组合拼装的过程，也就是和我们私域数据(向量编码)进行向量检索之后拼装为prompt，而这个过程是可以将其拼装成适合模型输入的Prompt。

一般来说有两种策略：“按召回数量”和“智能拼装”。“按召回数量”，用户可以精确控制从知识库中召回的信息chunk数量，满足对输入信息量和结构有明确要求的场景。“智能拼装”，能够根据用户设定的Prompt长度和chunk长度，智能地计算并召回最合适的chunk组合，以最大化利用输入空间，确保信息的完整性和输入效率。这两种策略为用户提供了根据不同任务需求灵活选择的机会，从而优化模型的输入质量和性能表现：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/edebaf632ffaef8cc92c7730133c8cb8.png)

这里就不开展过多，大家感兴趣的话可以去阅读博主的另一篇讲解RAG框架的文章： [检索增强生成(RAG)策略下的Prompt](https://cloud.tencent.com/developer/article/2391688?from_column=20421&from=20421)

#### **4.1.5联网搜索**

表面上也就是可以通过联网搜索到一些知识可以使用，许多人对该功能开发其实比较短浅，但是我们可以有更高阶的用法，比如我想实时去解读一份招标文件，但是目前我们又拿不到元件，就可以直接输入URL解读，在一些实时流场景很有用：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/cad6d9956360b75d38058cdcacf5bf87.png)

#### **4.1.6工作流**

大模型工作流是指基于大型语言模型构建的一套自动化流程，用于完成特定的任务。适用于需要结合大模型执行高确定性的业务逻辑的流程型应用，如可执行不同任务的智能助理工作流、自动化分析会议记录工作流等。

![](https://developer.qcloudimg.com/http-save/yehe-9822651/a0b2d28bc054da36945eece81f2f796a.png)

这里和AWSL是不一样的概念，以免大家混淆，这里普及一下AWSL智能体编排是指支持自定义智能体执行逻辑，编排主题为智能体，如智能体节点、智能体组及节点等，可快速实现复杂多智能体协同的逻辑设计和业务效果验证。适用于需要处理大量数据、进行复杂计算或执行多任务处理的场景。例如，在金融领域，可通过智能体编排搭建支持风险评估、投资组合优化、研报分析多种复杂能力的智能投顾系统。

![](https://developer.qcloudimg.com/http-save/yehe-9822651/76c5df8253e39da491cadaf4e5f67000.png)

根据标书写作业务来说，一般用户通常进行上传文件(多为PDF格式)之后，就开始询问或者直接让写作了，通过工作流编排我们能够缩短大模型解读文件时间，比如：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/fdfacf910f06f79705ee65ff3bae6e2e.png)

我们先对PDF的相关解析，统一归为文本数据类型，再将关键文本信息传入到我们之前的大模型中：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/d812aa8c1561ef7e033308a99bbbd33b.png)

然后我们还可以上传相关未整理的文件输入，利用数据格式清洗大模型帮我们规范化文件

![](https://developer.qcloudimg.com/http-save/yehe-9822651/6f7cbbcb4c4c56c963c470fa69cef702.png)

，再根据输出的文件检索相关政策，传入到大模型中：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/b4e22046b1c9037768eb8f62725accfc.png)

之后调试就可以验证并且看到全部工作流过程，方便我们进行调试和纠错：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/852feaa33b90f587f6fc3b6908204f73.png)

#### **4.1.7输出配置**

![](https://developer.qcloudimg.com/http-save/yehe-9822651/7e3d2f86017c4c80859f8629e85d9269.png)

大模型的输出方式有“流式”和“非流式”，必要时需要区分场景选择不同的输出方式对客户体验感有不同的策略。

![](https://developer.qcloudimg.com/http-save/yehe-9822651/38b3a0c928e8412c9174cbab8bd5de96.png)

- 流式适合实时性高的场景。
- 非流式适合需要高连贯性和格式化的任务。
- 选择方式需根据具体需求权衡。

关于智能回复所有问题和对知识来源以外的问题按填写内容回复也有不同的策略问题：

![](https://developer.qcloudimg.com/http-save/yehe-9822651/53be1f3c80a58e2aaf99d099777d0e7a.png)

那么到现在我们招标文书智能写作Agent就已经完成了。

## **五、总结与展望**

传统招标文书写作不仅面临繁琐的格式要求、信息复杂、时间紧迫等问题，还容易产生低效和高错误率。而智能写作Agent通过结合AI技术，为招标文书的写作提供了革命性的解决方案。智能写作Agent还能够根据不同的需求和客户特点，自动修改和调整文书中的条款和措辞。例如，在招标项目中，涉及到环保合规性、技术规范等要求时，Agent能够灵活调整内容，确保文书符合项目和客户的最新要求。这种灵活性和精准度是传统人工写作无法比拟的。

随着人工智能技术的不断进步，招标文书写作智能化的未来前景广阔。未来，智能写作Agent将更加智能和精细化，为招标文书的写作带来更大的变革。未来，AI不仅能生成文本内容，还能结合图表、图像等多模态信息，生成更丰富的招标文书。例如，AI可以根据项目需求自动插入相关的工程图纸、数据图表等，确保文书内容既有详细的文字描述，又能通过图形化展示关键数据和方案。多模态的文书生成将提高文书的可读性和信息传递效果，进一步提升招标文书的质量和专业性。

总的来说，智能写作Agent正在推动招标文书写作从传统人工操作向智能化、自动化的方向发展。随着AI技术的不断进步，未来智能写作Agent将变得更加智能、高效和定制化，进一步解放人力资源，提升招标文书写作的质量和效率。

原创声明：本文系作者授权腾讯云开发者社区发表，未经许可，不得转载。

如有侵权，请联系 [cloudcommunity@tencent.com](mailto:cloudcommunity@tencent.com) 删除。

[腾讯云大模型知识引擎xDeepSeek](https://cloud.tencent.com/developer/tag/18111)

[LLM](https://cloud.tencent.com/developer/tag/17917)

[腾讯云智能体开发平台](https://cloud.tencent.com/developer/tag/18050)

[DeepSeek](https://cloud.tencent.com/developer/tag/18107)

原创声明：本文系作者授权腾讯云开发者社区发表，未经许可，不得转载。

如有侵权，请联系 [cloudcommunity@tencent.com](mailto:cloudcommunity@tencent.com) 删除。

[腾讯云大模型知识引擎xDeepSeek](https://cloud.tencent.com/developer/tag/18111)

[LLM](https://cloud.tencent.com/developer/tag/17917)

[腾讯云智能体开发平台](https://cloud.tencent.com/developer/tag/18050)

[DeepSeek](https://cloud.tencent.com/developer/tag/18107)

评论

登录后参与评论

0 条评论

热度

最新

登录 后参与评论

推荐阅读

目录

- 高效速搭基于DeepSeek的招标文书智能写作Agent

- 前言

- 一、 引言

  - 1.1 传统招标文书写作的挑战

  - 1.2 市场上的痛点

  - 1.3 AI辅助写作的优势

    - 1.3.1 挖掘AI介入的场景

    - 1.3.2 传统写作 vs AI辅助写作

- 二、智能写作Agent的引入

  - 2.1什么是 AI Agent？

  - 2.2 招标文书智能写作 Agent

    - 2.2.1 自动分析招标文件要求，生成结构化内容

    - 2.2.2 根据不同需求和客户特点，智能修改和调整文书中的条款与措辞

    - 2.2.3 提供文书写作的实时建议与反馈，确保内容质量和符合标准

- 三、为什么选择DeepSeek作为写作大模型

  - 3.1.对标书行业术语的精准捕捉

  - 3.2 对招标方隐含需求的上下文推理

  - 3.3规则化与非规则化内容的融合生成

  - 3.4格式控制能力

    - 3.4.1 支持Markdown / LaTeX等格式输出

    - 3.4.2 多段落协同生成与逻辑一致性

- 四、基于腾讯云智能体开发平台 LKE的DeepSeek私有知识库搭建与RAG增强
  - 4.1 基于腾讯云智能体开发平台LKE实现

    - 4.1.1模型配置

    - 4.1.2角色指令

    - 4.1.3欢迎语

    - 4.1.4知识库

    - 4.1.5联网搜索

    - 4.1.6工作流

    - 4.1.7输出配置

- 五、总结与展望

相关产品与服务

腾讯云智能体开发平台

腾讯云智能体开发平台（Tencent Cloud Agent Development Platform，Tencent Cloud ADP），是基于大模型的智能体构建平台。提供LLM+RAG、Workflow、Multi-agent等多种智能体开发框架，助力企业能够结合专属数据，更高效地搭建稳定、安全、符合业务需求的智能体。

[产品介绍](https://cloud.tencent.com/product/adp?from=21341&from_column=21341)

[2026年中大促 \| AI 领航 智绘未来](https://cloud.tencent.com/act/pro/warmup-202606?from=21344&from_column=21344)

领券

- ### 社区

  - [技术文章](https://cloud.tencent.com/developer/column)
  - [技术问答](https://cloud.tencent.com/developer/ask)
  - [技术沙龙](https://cloud.tencent.com/developer/salon)
  - [技术视频](https://cloud.tencent.com/developer/video)
  - [学习中心](https://cloud.tencent.com/developer/learning)
  - [技术百科](https://cloud.tencent.com/developer/techpedia)
  - [技术专区](https://cloud.tencent.com/developer/zone/list)

- ### 活动

  - [自媒体同步曝光计划](https://cloud.tencent.com/developer/support-plan)
  - [邀请作者入驻](https://cloud.tencent.com/developer/support-plan-invitation)
  - [自荐上首页](https://cloud.tencent.com/developer/article/1535830)
  - [技术竞赛](https://cloud.tencent.com/developer/competition)

- ### 圈层

  - [腾讯云最具价值专家](https://cloud.tencent.com/tvp)
  - [腾讯云架构师技术同盟](https://cloud.tencent.com/developer/program/tm)
  - [腾讯云创作之星](https://cloud.tencent.com/developer/program/tci)
  - [腾讯云TDP](https://cloud.tencent.com/developer/program/tdp)

- ### 关于

  - [社区规范](https://cloud.tencent.com/developer/article/1006434)
  - [免责声明](https://cloud.tencent.com/developer/article/1006435)
  - [联系我们](mailto:cloudcommunity@tencent.com)
  - [友情链接](https://cloud.tencent.com/developer/friendlink)
  - [MCP广场开源版权声明](https://cloud.tencent.com/developer/article/2537547)

### 腾讯云开发者

![扫码关注腾讯云开发者](https://qcloudimg.tencent-cloud.cn/raw/a8907230cd5be483497c7e90b061b861.png?imageView2/2/w/200)

扫码关注腾讯云开发者

领取腾讯云代金券

### 热门产品

- [域名注册](https://cloud.tencent.com/product/domain?from=20064&from_column=20064)
- [云服务器](https://cloud.tencent.com/product/cvm?from=20064&from_column=20064)
- [区块链服务](https://cloud.tencent.com/product/tbaas?from=20064&from_column=20064)
- [消息队列](https://cloud.tencent.com/product/message-queue-catalog?from=20064&from_column=20064)
- [网络加速](https://cloud.tencent.com/product/ecdn?from=20064&from_column=20064)
- [云数据库](https://cloud.tencent.com/product/tencentdb-catalog?from=20064&from_column=20064)
- [域名解析](https://cloud.tencent.com/product/dns?from=20064&from_column=20064)
- [云存储](https://cloud.tencent.com/product/cos?from=20064&from_column=20064)
- [视频直播](https://cloud.tencent.com/product/css?from=20064&from_column=20064)

### 热门推荐

- [人脸识别](https://cloud.tencent.com/product/facerecognition?from=20064&from_column=20064)
- [腾讯会议](https://cloud.tencent.com/product/tm?from=20064&from_column=20064)
- [企业云](https://cloud.tencent.com/act/pro/enterprise2022?from=20064&from_column=20064)
- [CDN加速](https://cloud.tencent.com/product/cdn?from=20064&from_column=20064)
- [视频通话](https://cloud.tencent.com/product/trtc?from=20064&from_column=20064)
- [图像分析](https://cloud.tencent.com/product/imagerecognition?from=20064&from_column=20064)
- [MySQL 数据库](https://cloud.tencent.com/product/cdb?from=20064&from_column=20064)
- [SSL 证书](https://cloud.tencent.com/product/ssl?from=20064&from_column=20064)
- [语音识别](https://cloud.tencent.com/product/asr?from=20064&from_column=20064)

### 更多推荐

- [数据安全](https://cloud.tencent.com/solution/data_protection?from=20064&from_column=20064)
- [负载均衡](https://cloud.tencent.com/product/clb?from=20064&from_column=20064)
- [短信](https://cloud.tencent.com/product/sms?from=20064&from_column=20064)
- [文字识别](https://cloud.tencent.com/product/ocr?from=20064&from_column=20064)
- [云点播](https://cloud.tencent.com/product/vod?from=20064&from_column=20064)
- [大数据](https://cloud.tencent.com/product/bigdata-class?from=20064&from_column=20064)
- [小程序开发](https://cloud.tencent.com/solution/la?from=20064&from_column=20064)
- [网站监控](https://cloud.tencent.com/product/tcop?from=20064&from_column=20064)
- [数据迁移](https://cloud.tencent.com/product/cdm?from=20064&from_column=20064)

Copyright © 2013 - 2026 Tencent Cloud. All Rights Reserved. 腾讯云 版权所有

[深圳市腾讯计算机系统有限公司](https://qcloudimg.tencent-cloud.cn/raw/986376a919726e0c35e96b311f54184d.jpg) ICP备案/许可证号： [粤B2-20090059](https://beian.miit.gov.cn/#/Integrated/index)![](https://qcloudimg.tencent-cloud.cn/raw/eed02831a0e201b8d794c8282c40cf2e.png) [粤公网安备44030502008569号](https://beian.mps.gov.cn/#/query/webSearch?code=44030502008569)

[腾讯云计算（北京）有限责任公司](https://qcloudimg.tencent-cloud.cn/raw/a2390663ee4a95ceeead8fdc34d4b207.jpg) 京ICP证150476号 \|  [京ICP备11018762号](https://beian.miit.gov.cn/#/Integrated/index)

[问题归档](https://cloud.tencent.com/developer/ask/archives.html) [专栏文章](https://cloud.tencent.com/developer/column/archives.html) [快讯文章归档](https://cloud.tencent.com/developer/news/archives.html) [关键词归档](https://cloud.tencent.com/developer/information/all.html) [开发者手册归档](https://cloud.tencent.com/developer/devdocs/archives.html) [开发者手册 Section 归档](https://cloud.tencent.com/developer/devdocs/sections_p1.html)

Copyright © 2013 - 2026 Tencent Cloud.

All Rights Reserved. 腾讯云 版权所有

登录 后参与评论

目录

000

推荐

[首页](https://cloud.tencent.com/developer)

[MCP广场![](https://qccommunity.qcloudimg.com/image/new.png)](https://cloud.tencent.com/developer/mcp)

[返回腾讯云官网](https://cloud.tencent.com/?from=20060&from_column=20060)

[首页](https://cloud.tencent.com/developer)

[MCP广场![](https://qccommunity.qcloudimg.com/image/new.png)](https://cloud.tencent.com/developer/mcp)

[返回腾讯云官网](https://cloud.tencent.com/?from=20060&from_column=20060)

### 来源 4: https://arxiv.org/pdf/2603.23482

- URL: https://arxiv.org/pdf/2603.23482
- 精读方法：jina-readerlm-academic

```markdown
The provided draft Markdown does not match the content of the original HTML, which only contains a head tag with no actual body content. Therefore, there is nothing to extract or refine further into Markdown beyond the title "Your Title" if one were present.
```

### 来源 5: modelscope-classroom/LLM-tutorial/C.提示词工程-prompt engineering.md at main · modelscope/modelscope-classroom · GitHub

- URL: https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md
- 精读方法：firecrawl-scrape

[Skip to content](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md) to refresh your session.Dismiss alert

{{ message }}

[modelscope](https://github.com/modelscope)/ **[modelscope-classroom](https://github.com/modelscope/modelscope-classroom)** Public

- [Notifications](https://github.com/login?return_to=%2Fmodelscope%2Fmodelscope-classroom) You must be signed in to change notification settings
- [Fork\\
173](https://github.com/login?return_to=%2Fmodelscope%2Fmodelscope-classroom)
- [Star\\
1.4k](https://github.com/login?return_to=%2Fmodelscope%2Fmodelscope-classroom)

## Collapse file tree

## Files

main

Search this repository(forward slash)` forward slash/`

/

# C.提示词工程-prompt engineering.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

[![lecepin](https://avatars.githubusercontent.com/u/11046969?v=4&size=40)](https://github.com/lecepin)[lecepin](https://github.com/modelscope/modelscope-classroom/commits?author=lecepin)

[Update C.提示词工程-prompt engineering.md](https://github.com/modelscope/modelscope-classroom/commit/417587912ed481d0c5c16042a540e6b4f3633c4c)

2 years agoOct 14, 2024

[4175879](https://github.com/modelscope/modelscope-classroom/commit/417587912ed481d0c5c16042a540e6b4f3633c4c) · 2 years agoOct 14, 2024

## History

[History](https://github.com/modelscope/modelscope-classroom/commits/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md)

Open commit details

[View commit history for this file.](https://github.com/modelscope/modelscope-classroom/commits/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md) History

209 lines (120 loc) · 25.8 KB

/

# C.提示词工程-prompt engineering.md

Copy path

Top

## File metadata and controls

- Preview

- Code

- Blame

209 lines (120 loc) · 25.8 KB

[Raw](https://github.com/modelscope/modelscope-classroom/raw/refs/heads/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# 提示词工程-prompt engineering

[Permalink: 提示词工程-prompt engineering](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-promptengineering)

**引言**

前一天我们讲到：prompt（提示词）是我们和LLM互动最常用的方式，我们提供给LLM的Prompt作为模型的输入，并希望LLM反馈我们期待的结果。

虽然LLM的功能非常强大，但LLM对提示词（prompt）也非常敏感。这使得提示词工程成为一项需要培养的重要技能。

本节课将会给大家介绍提示词设计的一些技术，

使用环境： [https://modelscope.cn/studios/qwen/Qwen-72B-Chat-Demo](https://modelscope.cn/studios/qwen/Qwen-72B-Chat-Demo/summary)

**让我们从一个问题开始：**

最近尝试部署了qwen模型，我想固定它的输出，比如说“请走向公园。这句话我的目的地是？”，然后让它回答“公园”，但是模型会回答其他无关的字，写了提示词也没有解决，这是有办法固定的吗？我在尝试用RLHF微调，不知道有没有用。（from 知乎网友）

我们可以带着这个问题进入到本节课。

**LLM的超参配置**

LLM提供了一些参数可以影响输出结果的创造力和确定性。

在每个步骤中，LLM 会生成一个最有可能出现的token列表以及其对应的概率列表。根据 `top_p` 值，概率较低的token将被排除在概率列表之外，并且从剩余候选项中随机选择一个token（使用 `temperature` 来调整）。

简单来说：`top_p` 参数控制着生成文本时所使用词汇范围大小，而 `temperature` 参数则决定了在这个范围内文本生成时是否具有随机性。当温度接近 0 时，则会得到几乎是确定性结果。

**prompt engineering**

提示工程（Prompt Engineering）是一项通过优化提示词（Prompt）和生成策略，从而获得更好的模型返回结果的工程技术。总体而言，其实现逻辑如下：

[![image](https://github.com/modelscope/modelscope-classroom/raw/main/LLM-tutorial/resources/f2ff219f-a539-4a8c-bd7d-63b73fa67510.png)](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/resources/f2ff219f-a539-4a8c-bd7d-63b73fa67510.png)

（注：示例图来自Cohere官网）

简单而言，大模型的运行机制是“下一个字词预测”。用户输入的prompt即为大模型所获得上下文，大模型将根据用户的输入进行续写，返回结果。因此，输入的prompt的质量将极大地影响模型的返回结果的质量和对用户需求的满足程度，总的原则是“用户表达的需求越清晰，模型更有可能返回更高质量的结果”。

通常情况下，每条信息都会有一个角色（role）和内容（content）：

- 系统角色（system）用来向语言模型传达开发者定义好的核心指令。

- 用户角色（user）则代表着用户自己输入或者产生出来的信息。

- 助手角色（assistant）则是由语言模型自动生成并回复出来。

**System message系统指令**

system message系统指令为用户提供了一个易组织、上下文稳定的控制AI助手行为的方式，可以从多种角度定制属于你自己的AI助手。系统指令允许用户在一定范围内规定LLM的风格和任务，使其更具可定性和适应各种用例。大部分LLM模型的系统指令System message的权重强化高于人工输入的prompt，并在多轮对话中保持稳定，您可以使用系统消息来描述助手的个性，定义模型应该回答和不应该回答的内容，以及定义模型响应的格式。

默认的System message：You are a helpful assistant.

下面是一些system message的使用示例：

| 行业 | 角色 | system message |
| --- | --- | --- |
| 娱乐 | 二次元女生 | 你是二次元女生，喜欢使用颜文字，请用二次元可爱语气和我说话 |
| 教育 | 数学老师 | 您是一名数学导师，帮助各个级别的学生理解和解决数学问题。提供从基础算术到高级微积分等一系列主题的分步解释和指导。使用清晰的语言使复杂的概念更容易理解。 |
| 工作 | python数据分析师 | 1. 你会数学解题；2. 你会数据分析和可视化；3. 用户上传文件时，你必须先了解文件内容再进行下一步操作；4. 调用工具前你需要说明理由；Think step by step |
| 娱乐 | 喜剧演员 | 您是一位单口喜剧演员，用您的智慧和幽默来娱乐用户。分享笑话、有趣的故事和幽默的生活观察，同时根据用户的喜好和情感调整您的风格和内容。鼓励欢笑和轻松，同时保持尊重和包容的语气。 |
| 生活 | 小红书文案 | 你是一名小红书文案助手，擅长使用Emoji风格编辑文案。每篇文案包含引入入胜的标题、每个段落开始和结尾均为Emoji表情结尾，并保持原文的意思。 |
| 出行 | 旅行规划师 | 您是一名旅行规划师，通过提供有关目的地、住宿、景点和交通选项的信息来帮助用户制定旅行计划。根据用户的喜好、预算和旅行目标提供量身定制的建议，并分享实用技巧，帮助他们度过一次难忘而愉快的旅行。 |
| 文学 | 文言文大师 | 你是文言文大师，擅长翻译文本为为文言文。 |

System message可以被广泛应用在：

角色扮演：在系统指令中告诉千问你需要它扮演的角色，即可沉浸式和该角色对话交流

语言风格：简单调整LLM的语言风格

任务设定：比如旅行规划，小红书文案助手这样的专项任务处理

System message也可以被用于规定LLM的答复范围，并设定具体的行为。

| 行业 | 角色 | system message |
| --- | --- | --- |
| 教育 | 深度学习老师 | 你是一名深度学习的老师，可以回答深度学习领域相关的问题，提供有关机器学习概念、技术和最佳实践的全面信息。提供有关实施机器学习算法、选择适当的工具和框架以及构建端到端机器学习项目的分步指导。说明：1. 仅回答深度学习领域的知识 2. 如果不确定答案，你可以回答我不知道，并建议用户访问模型开源社区： [www.modelscope.cn](http://www.modelscope.cn/) |

[![image](https://github.com/modelscope/modelscope-classroom/raw/main/LLM-tutorial/resources/cbff2729-261a-4d61-bc92-5c5acf6e2655.png)](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/resources/cbff2729-261a-4d61-bc92-5c5acf6e2655.png)

[![image](https://github.com/modelscope/modelscope-classroom/raw/main/LLM-tutorial/resources/b055e8d5-c7e5-40c9-b9cc-33b274d156cb.png)](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/resources/b055e8d5-c7e5-40c9-b9cc-33b274d156cb.png)

**注意：** 即便我们在system message里面规范了模型回答，也不能保障请求一定会满足，但是好的system message设计可以增加特定结果的可能性，以及得到LLM更加符合要求的答复。

**用户提示词（user prompt）**

### 指令

[Permalink: 指令](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#%E6%8C%87%E4%BB%A4)

指令是最常用的提示组件，主要功能是向模型说明要执行的操作。虽然概念简单，但是实践中仍然比较复杂，下面是简单和详细的一些指令例子，详细、明确的指导比模糊不清的提示能够产生更好的效果：

| **指令类型** | **prompt** | **Completion** |
| --- | --- | --- |
| 简单指令 | 简要介绍一下阿里巴巴。 | 阿里巴巴集团是一家中国跨国科技公司，成立于1999年。阿里巴巴的业务覆盖了电子商务、零售、金融、物流、云计算、数字娱乐、医疗等多个领域，旗下拥有淘宝、天猫、菜鸟网络、阿里云、优酷等知名品牌。 阿里巴巴集团的愿景是让世界各地的企业都能够平等地进行贸易，让小企业通过数字化技术实现更好的发展。阿里巴巴秉持开放、合作、共赢的理念，致力于打造一个开放、包容、公平的数字经济生态系统，为全球数字经济的发展做出贡献。 阿里巴巴在科技创新和社会责任方面也做出了很多努力。阿里巴巴达摩院是阿里巴巴集团的全球科研机构，致力于推动科技创新和技术进步。阿里巴巴还积极参与公益事业，发起了“阿里巴巴公益基金会”等多个公益项目，致力于推动社会进步和可持续发展。 |
| 详细指令 | 简要介绍一下阿里巴巴， 包含以下内容： \\* 阿里巴巴的创始人姓名 \\* 阿里巴巴的使命 \\* 阿里巴巴的积极的前景 | 阿里巴巴（Alibaba）是一家总部位于中国杭州的全球领先的电子商务和科技公司，成立于1999年。阿里巴巴的创始人是马云和他的团队。阿里巴巴的使命是让世界各地的企业都能够平等地进行贸易，让小企业通过数字化技术实现更好的发展。阿里巴巴的愿景是打造一个开放、包容、公平的数字经济生态系统，为全球数十亿消费者和数百万企业提供服务，推动全球经济可持续发展。 阿里巴巴在过去二十年间迅速发展壮大，已经成为全球领先的电子商务和科技公司之一，业务涉及电子商务、金融、物流、云计算等多个领域。阿里巴巴的旗舰业务包括淘宝、天猫、支付宝、菜鸟网络等，这些业务已经成为中国和全球数亿消费者和企业不可或缺的生活和工作平台。 阿里巴巴在技术创新和社会责任方面也做出了很多努力。阿里巴巴达摩院是阿里巴巴集团的全球科研机构，致力于推动科技创新和技术进步。阿里巴巴还积极参与公益事业，发起了“阿里巴巴公益基金会”等多个公益项目，致力于推动社会进步和可持续发展。 总之，阿里巴巴是一家充满活力和创新精神的公司，其使命和愿景备受赞誉，未来发展前景十分积极。 |

### 主要内容

[Permalink: 主要内容](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#%E4%B8%BB%E8%A6%81%E5%86%85%E5%AE%B9)

主要内容是指模型正在处理的文本内容。 主要内容通常与指令一起使用。 下面会从翻译，摘要等场景来示例：

| **prompt** | **completion** |
| --- | --- |
| 今天天气真好！ 翻译为英文： | The weather is really nice today! |
| 5月1日，福建三明一游乐场内，一位女演员在进行高空表演走钢丝的时候，由于失误发生了意外，女子直接被挂在半空，此事引发大量网友关注。 2日，事发游乐场工作人员回应：女演员在进行高空表演时，被防坠落的装置卡住了，事情发生后，迅速安排救援人员进行救援，/n  女演员在空中挂了一二十分钟后被救下来了，没有生命危险。因为安全保护措施太多了，起到了反作用。 一句话总结这个新闻： | 游乐场高空表演意外，女演员被挂半空，经过20分钟救援后获救。 |

### 少样本学习

[Permalink: 少样本学习](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#%E5%B0%91%E6%A0%B7%E6%9C%AC%E5%AD%A6%E4%B9%A0)

好的prompt也经常包含一些示例样本（单样本或者少样本）学习，指的是需要加入一些示例的输入和输出对。

| prompt | completion |
| --- | --- |
| 新闻标题： **中国足球艰难前行** 主题： | 中国足球正面临艰难的时期，但也有许多积极的发展和进步。中国足协在2023年亚洲杯预选赛中成功晋级，这是中国足球历史上的一次重大突破。此外，中国足球也在加强青训体系建设，培养更多优秀的年轻球员。尽管中国足球面临着许多挑战，但我们相信，在全社会的支持下，中国足球未来会变得更加强大。 |
| 新闻标题：中国足球艰难前行 主题：足球 新闻标题：中美纪念“乒乓外交”50周年 主题：乒乓球 新闻标题：广东队加冕中国篮球比赛“11冠王” 主题： | 篮球 |

通过少样本学习，模型从猜测应该如何生成，而变得清楚的学习了按照示例生成，充分的演示了模型的能力，不需要通过专门的训练，通过少样本学习，也可以生成正确的答案。

### 更加明确的提示

[Permalink: 更加明确的提示](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#%E6%9B%B4%E5%8A%A0%E6%98%8E%E7%A1%AE%E7%9A%84%E6%8F%90%E7%A4%BA)

充当模型输出的快速启动，帮助模型固定所需要的输出。可以作为模型生成的前缀，也可以引导模型一步一步的按照要求思考并给出答案。

| prompt | completion |
| --- | --- |
| 做一杯茶是非常简单的! 第一步，您需要烧开水，然后，你需要准备一个杯子，并在里面放一个茶包, 当水沸腾后，就可以把水倒在茶包上了，现在我们可以坐一会儿等着茶充分的泡开，几分钟后，我们可以吧茶包拿走并丢弃，按照喜好，可以加牛奶，就会成为一杯奶茶，或者什么都不加，然后，你就可以想用你的茶了。 总结上述文本： | 制作一杯茶是非常简单的。首先，你需要烧开水。然后，准备一个杯子，放入茶包，并将沸水倒在茶包上。等待几分钟后，取出茶包并丢弃。最后，你可以加入牛奶，调制成奶茶，或者不加牛奶，直接饮用。 |
| 下面你将读到一段输入文本。如果他包含了一系列的指令, 按照如下格式重写这些指令： 第一步 - … 第二步 - … … 第N步 - … 做一杯茶是非常简单的! 第一步，您需要烧开水，然后，你需要准备一个杯子，并在里面放一个茶包, 当水沸腾后，就可以把水倒在茶包上了，现在我们可以坐一会儿等着茶充分的泡开，几分钟后，我们可以吧茶包拿走并丢弃，按照喜好，可以加牛奶，就会成为一杯奶茶，或者什么都不加，然后，你就可以想用你的茶了。 总结上述文本，按照如上格式分步骤展现出来： | 第一步：烧开水。  第二步：准备一个杯子，放入一个茶包。  第三步：当水沸腾时，将水倒在茶包上。  第四步：坐等茶泡开，几分钟后取出茶包并丢弃。  第五步：按喜好加入牛奶或不加，即可享用茶。 |

### 善用分隔符

[Permalink: 善用分隔符](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#%E5%96%84%E7%94%A8%E5%88%86%E9%9A%94%E7%AC%A6)

使用清晰的提示语法（包括标点符号、标题和节标记）有助于传达意图，并且通常使输出更易于解析。

在下面的示例中，`---`在不同的信息源或步骤之间添加了分隔符（在本例中）。这允许使用`---`作为生成的停止条件。此外，章节标题或特殊变量以大写形式呈现以区分它们。

| prompt | completion |
| --- | --- |
| 您将阅读一篇新闻，然后给这篇新闻取一个标题。 \-\-\- 据中国地震台网消息，1月3日18时08分，福建漳州市华安县发生3.5级地震，震源深度13千米。消息一出，厦门等多地网友纷纷表示有明显震感。 地震发生后，华安县地震局立即启动地震应急预案，加强对地震灾情的调查和监测。目前尚未收到地震造成人员伤亡或财产损失的报告。 网友们纷纷在社交媒体上分享自己的地震体验，有人称自己办公桌晃动，有人说家中的摆设受到了影响。地震引发了不少人的关注和讨论。 地震作为一种自然现象，时常发生。但也提醒我们要时刻保持警惕，加强地震知识的学习，做好地震应急预案，确保自身和家人的安全。 --- | 福建华安发生3.5级地震，厦门等地有震感，暂无伤亡报告 |

### 思维链提示

[Permalink: 思维链提示](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#%E6%80%9D%E7%BB%B4%E9%93%BE%E6%8F%90%E7%A4%BA)

这是任务分解（step by step）技术的一种展现，在这种方法中，模型逐步进行思考，并呈现出涉及的步骤，这样做可以降低结果的不准确的可能性，并对模型响应的可解释性有很大的帮助。

| prompt | completion |
| --- | --- |
| 给咖啡店做一个面向年轻人的菜单，在给出最终答案之前，请在回复中采用step by step的方式 | 设计一个面向年轻人的咖啡店菜单需要考虑以下几个步骤： Step 1：确定核心产品 首先，我们需要确定咖啡店的核心产品。对于年轻人来说，除了经典的拿铁、美式和卡布奇诺之外，我们还可以加入一些新颖、富有创意的咖啡饮品，如冷萃咖啡、氮气咖啡、抹茶拿铁、燕麦奶咖啡 等。 Step 2：添加特色饮品 考虑到年轻人追求新潮和个性化的特点，可以设计一些具有特色的饮品，例如季节限定款(比如冬季的热巧克力、夏季的水果冰咖)，或是网红饮品(如独角兽拉花咖啡、脏脏咖啡) Step 3：轻食搭配 为了满足年轻人健康饮食的需求，我们可以提供一系列轻食选项，包括各种口味的三明治、沙拉、燕麦碗、烤面包、蛋糕甜点以及无糖或低糖的选择。同时，也可以推出一些流行的美食趋势，比如 avocado toast(牛油果吐司)、acai bowl(阿萨伊果冻碗) 等。 Step 4：创新元素与互动体验 为了让年轻人感受到咖啡店的独特氛围，可以在菜单上添加一些互动性元素，比如自选配料区，顾客可以根据个人喜好自行调配咖啡、冰淇淋或者果汁； 或者推出DIY饮品， 让顾客亲手制作自己的专属咖啡。 Step 5：呈现方式与视觉效果 最后，菜单的设计应具有吸引力且符合年轻人审美，可以使用简洁明快、色彩鲜明的设计风格，并配以精美诱人的饮品图片。此外，菜单上的文字描述要充满趣味性和互动感，引起年轻消费者的兴 趣。 综上所述，一个面向年轻人的咖啡店菜单示例可能如下： ---咖啡--- 1.经典系列： \* 拿铁 \* 美式 \* 卡布奇诺 \* 冷萃咖啡 \* 氮气咖啡 2.创意特饮： \* 抹茶拿铁 \* 燕麦奶咖啡 \* 夏日限定：芒果冰咖 \* 季节限定：冬日热巧克力 \* 网红推荐：独角兽拉花咖啡 ---轻食--- 1.早餐精选： \* 香脆培根鸡蛋三明治 \* 牛油果吐司 \* 自制麦片酸奶杯 2.快餐简餐： \* 凯撒沙拉 \* 超级食物蔬沙拉 \* 烤鸡肉蔬菜卷 3.甜品诱惑： \* 巧克力慕斯蛋糕 \* 柠檬挞 \* 无糖酸奶蓝莓派 ---互动体验--- 1.DIY咖啡：选择您喜欢的咖啡底料+任意配料(蜂蜜、焦糖酱、奶油、巧克力粉等) 2.果汁吧：挑选新鲜水果现场榨汁，自由搭配您的专属果汁 请注意，以上只是一个示例，具体菜单内容还需根据目标客群的口味、消费水平及地域文化等因素进行调整。 |

### 对输出格式的明确要求

[Permalink: 对输出格式的明确要求](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#%E5%AF%B9%E8%BE%93%E5%87%BA%E6%A0%BC%E5%BC%8F%E7%9A%84%E6%98%8E%E7%A1%AE%E8%A6%81%E6%B1%82)

| prompt | completion |
| --- | --- |
| 给我推荐2本科幻小说，包含作者，出版时间，推荐理由，请用json格式回答 | 当然，以下是两本科幻小说的推荐信息，格式化为JSON： \`\`\`json \[   {     "书名": "基地",     "作者": "艾萨克·阿西莫夫",     "出版时间": "1951年",     "推荐理由": "《基地》是科幻文学史上的里程碑之作，它构建了一个庞大的银河帝国背景，通过心理史学这一概念，探索了文明兴衰的宏观历史进程以及个体在其中的角色。阿西莫夫以其深邃的想象力和精妙的故事架构，开创了“基地系列”，对后世科幻作品产生了深远影响。"   },   {     "书名": "三体",     "作者": "刘慈欣",     "出版时间": "2006年5月（第一部）",     "推荐理由": "《三体》是中国科幻作家刘慈欣创作的一部硬科幻巨著，该系列凭借其独特的宇宙观、丰富的科学理论基础和紧张刺激的情节赢得了全球读者的喜爱。作品深度探讨了人类文明与外星文明的碰撞、科技发展对人类社会的影响以及宇宙生存法则等主题，荣获雨果奖最佳长篇小说奖，标志着中国科幻小说在世界范围内的重大突破。"   } \] \`\`\` |

**最佳实践案例**

## Agent场景，使用prompt实现agent create

[Permalink: Agent场景，使用prompt实现agent create](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#agent%E5%9C%BA%E6%99%AF%E4%BD%BF%E7%94%A8prompt%E5%AE%9E%E7%8E%B0agentcreate)

[https://github.com/modelscope/modelscope-agent/blob/master/apps/agentfabric/builder\_prompt\_zh.py](https://github.com/modelscope/modelscope-agent/blob/master/apps/agentfabric/builder_prompt_zh.py)

| system message | prompt |
| --- | --- |
| You are a helpful assistant. | 你现在要扮演一个制造AI角色（AI-Agent）的AI助手（QwenBuilder）。 你需要和用户进行对话，明确用户对AI-Agent的要求。并根据已有信息和你的联想能力，尽可能填充完整的配置文件： 配置文件为json格式： {"name": "... # AI-Agent的名字", "description": "... # 对AI-Agent的要求，简单描述", "instructions": "... \ # 分点描述对AI-Agent的具体功能要求，尽量详细一些，类型是一个字符串数组，起始为\[\]", "prompt\_recommend": \ "... # 推荐的用户将对AI-Agent说的指令，用于指导用户使用AI-Agent，类型是一个字符串数组，请尽可能补充4句左右，\ 起始为\["你可以做什么？"\]", "logo\_prompt": "... # 画AI-Agent的logo的指令，不需要画logo或不需要更新logo时可以为空，类型是string"} 在接下来的对话中，请在回答时严格使用如下格式，先作出回复，再生成配置文件，不要回复其他任何内容： Answer: ... # 你希望对用户说的话，用于询问用户对AI-Agent的要求，不要重复确认用户已经提出的要求，而应该拓展出新的角度来询问用户，尽量细节和丰富，禁止为空 Config: ... # 生成的配置文件，严格按照以上json格式 RichConfig: ... # 格式和核心内容和Config相同，但是保证name和description不为空；instructions需要在Config的基础上扩充字数，\ 使指令更加详尽，如果用户给出了详细指令，请完全保留；补充prompt\_recommend，并保证prompt\_recommend是推荐的用户将对AI-Agent\ 说的指令。请注意从用户的视角来描述prompt\_recommend、description和instructions。 一个优秀的RichConfig样例如下： {"name": "小红书文案生成助手", "description": "一个专为小红书用户设计的文案生成助手。", "instructions": "1. 理解并回应用户的指令；\ 2. 根据用户的需求生成高质量的小红书风格文案；3. 使用表情提升文本丰富度", "prompt\_recommend": \["你可以帮我生成一段关于旅行的文案吗？", \ "你会写什么样的文案？", "可以推荐一个小红书文案模版吗？"\], "logo\_prompt": "一个写作助手logo，包含一只羽毛钢笔"} 明白了请说“好的。”， 不要说其他的。 |

## Agent场景，使用system message+prompt实现function call

[Permalink: Agent场景，使用system message+prompt实现function call ](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#agent%E5%9C%BA%E6%99%AF%E4%BD%BF%E7%94%A8systemmessageprompt%E5%AE%9E%E7%8E%B0functioncall)

大部分模型将agent的配置在系统提示中配置，比如函数的参数定义和描述，不同模型的函数调用略有不同，

| system message | prompt |
| --- | --- |
| Answer the following questions as best as you can. You have access to the following tools: \[     {         "name": "get\_current\_weather",         "description": "Get the current weather in a given location",         "parameters": {             "type": "object",             "properties": {                 "location": {                     "type": "string",                     "description": "The city and state, e.g. San Francisco, CA",                 },                 "unit": {"type": "string"},             },             "required": \["location"\],         },     } \] | 今天北京的天气怎么样？ |
| 你是一位智能AI助手，你连接着一台电脑，但请注意不能联网。在使用Python解决任务时，你可以运行代码并得到结果，如果运行结果有错误，你需要尽可能对代码进行改进。你可以处理用户上传到电脑上的文件，文件默认存储路径是/mnt/data/。 | 根据我上传的表格文件，分析数据，并绘制年度收入折线图 |

# 写好Prompt的一些原则总结

[Permalink: 写好Prompt的一些原则总结](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#%E5%86%99%E5%A5%BDprompt%E7%9A%84%E4%B8%80%E4%BA%9B%E5%8E%9F%E5%88%99%E6%80%BB%E7%BB%93)

最核心的写一条好prompt的原则就是尽可能清晰、明确地表达你的需求（类比产品经理向程序员提需求）。细分下来，具体原则包括：

- **清晰的指令：** 足够清晰明确地说明你希望模型为你返回什么，最后更加细致地说明需求，避免模糊表达。

- **提供上下文和例子：** 给出较为充分的上下文信息，让模型更好地理解相关背景。如果能够提供示例，模型能表现更好（类似传统LLM中的in-context learning）。

- **善用符号和语法：** 使用清晰的标点符号，标题，标记有助于转达意图，并使输出更加容易被解析

- **让模型一步一步的思考：** 在这种方法中，模型逐步进行思考，并呈现出涉及的步骤，这样做可以降低结果的不准确的可能性，并对模型响应的可解释性有很大的帮助。

- **激励模型反思和给出思路：** 可以在prompt中用一些措辞激励模型给出理由，这样有助于我们更好地分析模型生成结果，同时，思维过程的生成，也有助于其生成更高质量的结果。

- **给容错空间：** 如模型无法完成指定的任务，给模型提供一个备用路径，比如针对文本提问，可以加入如果答案不存在，则回复“无答案”

- **让模型给出信息来源：** 在模型结合搜索或者外部知识库时，要求模型提供他的答案的信息来源，可以帮助LLM的答案减少捏造，并获取到最新的信息。

# 优质的提示词典型框架

[Permalink: 优质的提示词典型框架](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#%E4%BC%98%E8%B4%A8%E7%9A%84%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%85%B8%E5%9E%8B%E6%A1%86%E6%9E%B6)

优质的prompt千变万化，但遵循上述原则，我们总结出一个比较实用的框架，可以帮助用户更高概率从通义千问中收获更高质量的模型生成结果。使用LLM时，建议包含如下内容：

- system message：你希望大模型扮演什么角色，来解决你当前的问题。大模型具有较强的角色扮演能力，相比直接回答往往表现更好。system message中也可以规定大模型的回答范围。

- prompt
  - 指令：明确说明你希望大模型做什么事情，不要含糊其辞。

  - 例子：如果可能，提供尽可能丰富的例子信息。

  - 原因：详细解释你希望模型做这件事情的原因、动机、希望的结果等，这样大模型能更好地理解你的想法，执行需求。

  - step by step：对于复杂任务，让大模型一步一步的思考，可以给出更加合理的答案。

  - 对于输出格式的形容：对于部分场景，明确大模型输出格式的要求，可以更好的获取到更加结构化，适合系统调用的答案。

# 课后实践

[Permalink: 课后实践](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#%E8%AF%BE%E5%90%8E%E5%AE%9E%E8%B7%B5)

在游戏中学会prompt engineering，通关

### [**https://modelscope.cn/studios/LLMRiddles/LLMRiddles/summary**](https://modelscope.cn/studios/LLMRiddles/LLMRiddles/summary)

[Permalink: https://modelscope.cn/studios/LLMRiddles/LLMRiddles/summary](https://github.com/modelscope/modelscope-classroom/blob/main/LLM-tutorial/C.%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-prompt%20engineering.md#httpsmodelscopecnstudiosllmriddlesllmriddlessummary)

You can’t perform that action at this time.

### 来源 6: 附录 A - 高级提示工程技术 | Jimmy Song

- URL: https://jimmysong.io/zh/book/agentic-design-patterns/appendix-a-advanced-prompting-techniques
- 精读方法：firecrawl-scrape

[跳转到主要内容](https://jimmysong.io/zh/book/agentic-design-patterns/appendix-a-advanced-prompting-techniques/#main-content) [跳转到导航](https://jimmysong.io/zh/book/agentic-design-patterns/appendix-a-advanced-prompting-techniques/#navigation) [跳转到页脚](https://jimmysong.io/zh/book/agentic-design-patterns/appendix-a-advanced-prompting-techniques/#site-footer)

# 附录 A - 高级提示工程技术

内容导航

图书内部搜索...

## 提示工程简介

提示（Prompting）是与语言模型交互的主要接口，通过精心设计输入来引导模型生成期望的输出。提示工程包括结构化请求、提供相关上下文、指定输出格式，以及展示期望的响应类型。设计良好的提示能最大化模型潜力，获得准确、相关且富有创造性的回复；而设计不当则可能导致模糊、无关或错误的输出。

提示工程的目标是持续获得高质量的模型响应。这要求理解模型的能力与局限，并有效传达意图。提示工程是一门与 AI 沟通的专业技能，需要不断学习如何更好地指令模型。

本附录详细介绍了超越基础交互的多种提示技术，涵盖复杂请求结构化、增强模型推理能力、控制输出格式、集成外部信息等方法。这些技术适用于从简单聊天机器人到复杂多智能体系统的开发，可显著提升智能体应用的性能与可靠性。

智能体模式，即智能系统的架构结构，在主章节中有详细阐述。这些模式定义了智能体如何规划、使用工具、管理记忆和协作。智能体系统的效能依赖于其与语言模型的高质量交互。

## 核心提示原则

高效提示的核心原则：

提示工程的有效性依赖于一系列基本原则，适用于各种模型和任务复杂度。掌握这些原则是持续获得有用、准确响应的关键。

**清晰与具体**：指令必须明确、具体。语言模型依赖模式识别，歧义会导致意外响应。需明确定义任务、期望输出格式及限制条件，避免模糊或假设。提示不清会导致输出不准确，影响结果质量。

**简洁**：在保证具体性的前提下，指令应简明扼要。冗余或复杂句式会干扰模型理解。提示应简洁明了，避免复杂语言和多余信息。使用直接表达和主动动词，如：Act、Analyze、Categorize、Classify、Contrast、Compare、Create、Describe、Define、Evaluate、Extract、Find、Generate、Identify、List、Measure、Organize、Parse、Pick、Predict、Provide、Rank、Recommend、Return、Retrieve、Rewrite、Select、Show、Sort、Summarize、Translate、Write。

**动词使用**：动词选择是提示工程的重要工具。动作动词明确期望操作。例如，“Summarize the following text”比“Think about summarizing this”更有效。精准动词能激活模型相关训练

#### 训练（Training）

使用数据集调整模型参数的过程，使模型能够学习数据中的模式。

数据和处理流程。

**正面指令优于约束**：正面指令通常比负面约束更有效。明确期望行为优于强调不希望的行为。约束适用于安全或格式要求，但过度依赖会让模型聚焦于规避而非目标。正面指令更符合人类指导习惯，减少混淆。

**实验与迭代**：提示工程是一个迭代过程。找到最优提示需多次尝试。起草、测试、分析输出、发现不足并优化提示。模型参数和措辞微调会影响结果。记录尝试过程有助于学习和改进。持续实验和迭代是实现理想效果的必经之路。

这些原则是与语言模型高效沟通的基础。通过优先考虑清晰、简洁、动作动词、正面指令和迭代，建立了应用更高级提示技术的坚实框架。

## 基础提示技术

在核心原则基础上，基础提示技术通过不同信息或示例引导模型响应。这些方法是提示工程的起点，适用于广泛场景。

### 零样本提示（Zero-Shot Prompting）

零样本提示是最基础的提示方式，仅提供任务描述和输入数据，无需示例。模型完全依赖预训练知识理解任务并生成响应。

- **适用场景**：模型训练中常见的任务，如简单问答、文本补全、基础摘要，通常零样本即可满足。
- **示例**：

将以下英文句子翻译成法语：‘Hello, how are you?’

### 单样本提示（One-Shot Prompting）

单样本提示在正式任务前提供一个输入 \- 输出示例，帮助模型理解期望模式。适用于输出格式或风格特殊的任务。

- **适用场景**：当期望输出结构或风格较为特殊时，单样本能显著提升效果。

- **示例**：

将以下英文句子翻译成西班牙语：

English: ‘Thank you.’

Spanish: ‘Gracias.’

English: ‘Please.’

Spanish:

### 少样本提示（Few-Shot Prompting）

少样本提示提供 3-5 组输入 - 输出示例，展示更清晰的期望模式，提升模型对新输入的泛化能力。

- **适用场景**：当任务需遵循特定格式、风格或有细微变化时，少样本提示尤为有效。适合分类、结构化数据抽取、特定风格文本生成等。示例数量可根据任务复杂度和模型 Token

#### Token

大模型处理文本的基本单位，可以是单词、词子或字符。

限制调整。

- **示例质量与多样性**：示例需准确、具代表性，覆盖可能的变体或边界情况。高质量示例至关重要，错误示例会误导模型。多样化示例有助于模型泛化。

- **分类任务示例顺序**：分类任务中，建议混合不同类别示例顺序，避免模型过拟合特定序列。

- **“多样本”学习演进**：现代 LLM

#### LLM（大语言模型）

一种能够理解和生成人类语言的深度学习算法。

如 Gemini 支持更长上下文，可在提示中包含大量示例，提升复杂任务表现。

- **示例**：

请将以下电影评论情感分类为 POSITIVE、NEUTRAL 或 NEGATIVE：

评论：“The acting was superb and the story was engaging.”

情感：POSITIVE

评论：“It was okay, nothing special.”

情感：NEUTRAL

评论：“I found the plot confusing and the characters unlikable.”

情感：NEGATIVE

评论：“The visuals were stunning, but the dialogue was weak.”

情感：

合理选择零样本、单样本和少样本提示技术，并精心设计和组织示例，是提升智能体系统有效性的关键。这些基础方法是多种提示策略的根基。

## 提示结构化

除了提供示例，提示结构化对于引导模型至关重要。结构化提示通过不同部分（如指令、上下文、示例）清晰分隔信息，帮助模型正确解析并理解每段文本的角色。

### 系统提示（System Prompting）

系统提示用于设定模型整体行为和交互目的，定义规则、角色或风格。与具体用户查询不同，系统提示为模型响应提供基础指导，影响语气、风格和整体策略。可用于安全和毒性控制，如要求保持礼貌用语。

系统提示可通过 LLM 自动优化，如 Vertex AI Prompt

#### Prompt（提示词）

输入给 AI 模型的指令或文本。

Optimizer，基于用户指标和目标数据迭代提升提示效果。

- **示例**：

你是一名友好且无害的 AI 助手。所有回复需礼貌且信息丰富，不生成有害、偏见或不当内容。

### 角色提示（Role Prompting）

角色提示为模型分配特定身份或角色，结合系统或上下文提示，要求模型采用该角色的知识、语气和风格。例如，“Act as a travel guide”或“你是一名资深数据分析师”，可提升输出的专业性和相关性。角色风格也可指定，如“幽默且励志”。

- **示例**：

作为一名资深旅行博主，写一段关于罗马最佳隐藏景点的精彩短文。

### 分隔符使用

有效提示需清晰区分指令、上下文、示例和输入。可用三重反引号（\`\`\`）、XML 标签（、）、或标记（—）分隔各部分，减少模型误解。

- **示例**：

请总结以下文章，重点关注作者主要观点。\[插入文章全文\]

## 上下文工程

上下文工程区别于静态系统提示，动态提供任务和对话所需背景信息，帮助模型理解细节、回忆历史、整合相关内容，提升响应的相关性和连贯性。包括历史对话、检索文档（如 RAG

#### RAG（检索增强生成）

通过检索外部知识并与生成模型结合，提升回答准确性与可追溯性的方法。

）、或操作参数。例如，讨论日本旅行时，要求推荐东京适合家庭的三项活动，利用已有对话上下文。智能体系统中，上下文工程是记忆持久化、决策和多任务协作的核心。动态上下文管道让智能体能持续目标、调整策略、与其他智能体或工具协作，实现长期自主性。该方法强调模型输出质量更多依赖于上下文丰富度，而非模型架构，是提示工程向多层信息扩展的重要演进。

主要层次包括：

- **系统提示**：定义 AI 操作参数的基础指令（如“你是一名技术写手，语气需正式且精准”）。
- **外部数据**：
  - **检索文档**：主动从知识库获取信息（如技术规格）。
  - **工具输出**：AI 调用外部 API 获取实时数据（如查询日程）。
- **隐式数据**：如用户身份、交互历史、环境状态。集成隐式上下文需注意隐私和伦理，企业、医疗、金融等领域需严格治理。

核心原则是：即使模型再先进，若缺乏丰富或合理的环境视角，表现也会受限。上下文工程将任务从简单问答转变为为智能体构建全面操作视图。例如，集成用户日程（工具输出）、邮件收件人关系（隐式数据）、会议记录（检索文档），让模型生成高度相关、个性化、实用的输出。工程实践包括构建数据管道、反馈循环持续优化上下文质量。

可用如 Google Vertex AI Prompt Optimizer 等自动化工具，基于样例输入和指标系统性优化提示和系统指令，实现大规模反馈循环。优化器可根据样例、系统指令和模板自动改进上下文输入，为复杂上下文工程提供结构化方法。

这种结构化方法让 AI 系统从简单工具升级为具备情境感知的智能体，强调智能体“知道什么、何时知道、如何使用”，确保模型全面理解用户意图、历史和环境。上下文工程是将无状态聊天机器人转变为高能力、情境感知系统的关键方法。

## 结构化输出

提示目标常常不仅是获得自由文本，还需提取或生成特定格式（如 JSON、XML、CSV、Markdown 表格）的结构化信息。明确要求输出格式并提供示例或 Schema，可引导模型生成易于后续处理的结构化响应。请求 JSON 对象有助于限制幻觉，便于数据抽取和管道集成。建议在非创意任务中多尝试不同输出格式。

- **示例**：

从下文提取信息，并以 JSON 对象返回，包含"name"、“address”、“phone\_number"字段。

文本：“Contact John Smith at 123 Main St, Anytown, CA or call (555) 123-4567.”

结构化提示、角色分配、上下文信息、分隔符和结构化输出的有效结合，显著提升与语言模型交互的清晰度、可控性和实用性，为可靠智能体系统开发奠定基础。结构化输出是构建模型输出可作为后续系统输入的关键。

**利用 Pydantic 实现面向对象封装**：通过 LLM 生成的数据填充 Pydantic 对象，是强制结构化输出和提升互操作性的有效方法。Pydantic 是 Python 的数据校验和配置管理

#### 配置管理（Configuration Management）

管理系统配置的过程，包括创建、更新和维护配置文件。

库，支持类型注解。定义 Pydantic 模型后，可直接用 model\_validate\_json 方法解析 LLM 输出的 JSON 字符串，实现解析和校验一步到位。

📄
Pydantic 结构化输出示例

[下载文件](https://jimmysong.io/zh/book/agentic-design-patterns/appendix-a-advanced-prompting-techniques/appendix-a-structured-output.py "下载文件")

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>``` | ```python<br>from pydantic import BaseModel, EmailStr, Field, ValidationError<br>from typing import List, Optional<br>from datetime import date<br># --- Pydantic 模型定义 ---<br>class User(BaseModel):<br>   name: str = Field(..., description="用户全名")<br>   email: EmailStr = Field(..., description="用户邮箱")<br>   date_of_birth: Optional[date] = Field(None, description="出生日期")<br>   interests: List[str] = Field(default_factory=list, description="兴趣列表")<br># --- 假设 LLM 输出 ---<br>llm_output_json = """<br>{<br>   "name": "Alice Wonderland",<br>   "email": "alice.w@example.com",<br>   "date_of_birth": "1995-07-21",<br>   "interests": [<br>       "自然语言处理",<br>       "Python 编程",<br>       "园艺"<br>   ]<br>}<br>"""<br># --- 解析与校验 ---<br>try:<br>   user_object = User.model_validate_json(llm_output_json)<br>   print("成功创建 User 对象！")<br>   print(f"姓名：{user_object.name}")<br>   print(f"邮箱：{user_object.email}")<br>   print(f"出生日期：{user_object.date_of_birth}")<br>   print(f"首个兴趣：{user_object.interests[0]}")<br>   print(f"date_of_birth 类型：{type(user_object.date_of_birth)}")<br>except ValidationError as e:<br>   print("LLM 输出 JSON 校验失败。")<br>   print(e)<br>``` |

上述代码演示了如何用 Pydantic 定义数据模型并校验 JSON 数据。模型字段包含类型注解和描述，解析 LLM 输出时自动校验类型并转换为 Python 对象。异常处理可捕获格式或类型错误。

对于 XML 数据，可用 xmltodict 库将 XML 转为字典，再传递给 Pydantic 模型解析。通过 Field 别名可映射 XML 结构到对象字段。

此方法确保 LLM 组件与系统其他部分的互操作性。LLM 输出封装为 Pydantic 对象后，可安全传递给函数、API 或数据管道，保证数据结构和类型一致。系统边界采用“解析而非校验”原则，提升应用健壮性和可维护性。

结构化提示、角色分配、上下文信息、分隔符和结构化输出的有效结合，显著提升与语言模型交互的清晰度、可控性和实用性，为可靠智能体系统开发奠定基础。结构化输出是构建模型输出可作为后续系统输入的关键。

提示结构化 除了示例，结构化提示通过不同部分（如指令、上下文、示例）清晰分隔信息，帮助模型正确解析并理解每段文本的角色。

## 推理与思考过程技术

大语言模型擅长模式识别和文本生成，但在复杂多步推理任务上仍有挑战。本节介绍提升模型推理能力的技术，鼓励模型显式展示思考过程，提升逻辑推理、数学计算和规划能力。

### 思维链（Chain of Thought, CoT）

思维链提示通过要求模型生成中间推理步骤，提升其推理能力。与直接请求结果不同，CoT

#### CoT（思维链）

Chain of Thought，通过生成一系列中间推理步骤来提高大模型复杂推理能力的提示技术。

提示要求模型“逐步思考”，模拟人类分解问题的过程。

CoT 能显著提升模型在计算或逻辑推理任务上的准确率。主要有两种变体：

- **零样本 CoT**：仅在提示中加入“让我们一步一步思考”等语句，无需示例。许多任务中，这种简单补充即可显著提升模型表现。

  - **示例**：

    一列火车以每小时 60 英里速度行驶，路程 240 英里，旅程耗时多久？让我们一步一步思考。
- **少样本 CoT**：结合少样本提示，提供多个输入、推理过程和最终输出示例，帮助模型学习推理结构，提升复杂任务表现。

  - **示例**：

    Q: 三个连续整数之和为 36，求这三个数？

    A: 设第一个数为 x，第二个为 x+1，第三个为 x+2，总和为 3x+3=36，解得 x=11，三个数为 11、12、13。

    Q: Sarah 有 5 个苹果，又买了 8 个，吃掉 3 个，还剩多少？让我们一步一步思考。

    A: Sarah 初有 5 个苹果，买 8 个后共 13 个，吃掉 3 个剩 10 个。答案是 10。

CoT 优点是易于实现，对现成 LLM 效果显著，无需微调。输出可解释性强，有助于理解和调试。CoT 还能提升不同模型版本间的提示健壮性。缺点是输出长度增加，消耗更多 Token。最佳实践包括将最终答案置于推理步骤之后，单一答案任务建议温度设为 0（贪婪解码）。

### 自洽性（Self-Consistency）

自洽性技术在 CoT 基础上，通过生成多条推理路径并选取最一致答案，提升推理可靠性。

主要步骤：

1. **生成多样推理路径**：同一提示多次发送给 LLM，设置较高温度，鼓励模型探索不同推理方式。
2. **提取答案**：从每条推理路径中提取最终答案。
3. **多数投票**：选取出现频率最高的答案作为最终结果。

该方法提升了多路径任务的准确性和一致性，但需多次运行模型，计算和成本较高。

- **示例**：
  - _提示_：“‘所有鸟都会飞’这个说法对吗？请解释。”
  - _模型 1_：多数鸟会飞，结论为 True。
  - _模型 2_：企鹅和鸵鸟不会飞，结论为 False。
  - _模型 3_：一般鸟会飞，简要提及例外，结论为 True。
  - _自洽性结果_：多数为 True，最终答案为 True。（更复杂方法可权衡推理质量）

### 反思提示（Step-Back Prompting）

反思提示先要求模型考虑与任务相关的通用原则或概念，再解决具体问题。这样能激活模型背景知识，提升推理深度和准确性，减少表面因素影响。先考虑一般因素有助于生成更具洞察力的输出，鼓励批判性思考和知识应用。

- **示例**：
  - _提示 1_：“优秀侦探小说的关键要素有哪些？”
  - _模型响应 1_：列举红鲱鱼、动机、主角缺陷、逻辑线索、圆满结局等。
  - _提示 2_：“结合上述要素，写一个小镇新侦探小说的情节概要。”

### 思维树（Tree of Thoughts, ToT）

思维树是 CoT 的进阶技术，让模型并行探索多条推理路径。每个节点代表一个“思考”，可从节点分支探索不同方案。

ToT 适合需探索、回溯或多方案评估的复杂问题。虽然实现更复杂、计算量更大，但能在需要深度探索的任务上获得更优结果。智能体可在“思维树”中尝试不同分支，纠正初始错误。

- **示例**：如“为故事设计三个不同结局”，ToT 可让模型从关键转折点并行生成多种剧情分支，而非线性续写。

这些推理与思考技术是构建能处理复杂认知任务智能体的关键。通过提示模型显式推理、考虑多角度或抽象原则，可显著提升智能体系统的复杂任务能力。

## 行动与交互技术

智能体不仅能生成文本，还能主动与环境交互，包括调用工具、执行外部函数、参与观察 \- 推理 \- 行动循环。本节介绍支持主动行为的提示技术。

### 工具使用 / 函数调用

智能体关键能力之一是调用外部工具或函数，执行超出自身能力的操作，如网页搜索、数据库访问、发送邮件、计算、API 交互。有效提示需设计模型何时、如何使用工具。

现代模型常针对“函数调用”或“工具使用”微调，能理解工具描述及参数。收到请求后，模型判断是否需用工具，选择合适工具并格式化参数。模型本身不执行工具，而是生成结构化输出（如 JSON），由智能体系统执行工具并将结果反馈给模型，持续交互。

- **示例**：

你可使用天气工具“get\_current\_weather”，参数为城市名（字符串）。

用户：伦敦现在天气如何？

  - _期望模型输出（函数调用）_：

    {

    “tool\_code”: “get\_current\_weather”,

    “tool\_name”: “get\_current\_weather”,

    “parameters”: {

    “city”: “London”

    }

    }

### ReAct (Reason & Act)

ReAct

#### ReAct

Reasoning + Acting，结合推理和行动的智能体框架。

即“推理与行动”，结合 CoT 推理与工具使用，模拟人类思考与行动交替过程。

ReAct 流程：

1. **思考**：模型生成当前理解和计划。
2. **行动**：根据思考决定执行工具操作，输出工具名和参数。
3. **观察**：系统执行工具并将结果反馈给模型。
4. 循环进行，模型基于最新观察生成新思考，继续行动，直至任务完成并输出最终答案。

这种交替思考与行动让智能体能动态获取信息、响应工具输出、优化策略，适合需与动态环境或外部知识交互的任务。

- **示例（ReAct 流程）**：

用户：法国首都及当前人口是多少？

思考：用户需两项信息：法国首都和人口。可用搜索工具查询。先确认首都。

行动：Search({“query”: “capital of France”})

观察：Paris

思考：首都是 Paris，接下来查人口。

行动：Search({“query”: “current population of Paris”})

观察：2023 年人口约 210 万。

思考：已获得全部信息，可回复用户。

最终答案：法国首都是巴黎，2023 年人口约 210 万。

这些技术是构建能主动获取信息、执行任务、与外部系统交互智能体的基础。

## 高级技术

除基础、结构化和推理模式外，还有多种高级提示技术可进一步提升智能体系统能力和效率，包括自动优化提示、集成外部知识、根据用户特征定制响应等。

### 自动提示工程（APE）

自动提示工程（APE）利用语言模型自动生成、评估和优化提示，减少人工设计负担，提升模型表现。

基本思路是用“元模型”根据任务描述生成多个候选提示，通过输出质量（如 BLEU、ROUGE 或人工评估）筛选最佳提示，并进一步优化。用 LLM 生成用户查询变体训练聊天机器人即为一例。

程序化提示优化（如 DSPy 框架）将提示视为可自动优化的模块，采用数据驱动方法：

1. **高质量数据集（Goldset）**：包含代表性输入输出对，定义任务成功标准。
2. **目标函数（评分指标）**：自动评估模型输出与标准输出的质量。

优化器（如贝叶斯优化）系统性优化提示，主要策略：

- **少样本示例优化**：自动从 Goldset 采样不同示例组合，测试并选出最有效示例集。
- **指令优化**：用 LLM 元模型自动迭代修改提示文本，调整措辞、语气或结构，寻找得分最高的表达方式。

目标是最大化目标函数得分，实现提示自动“训练”，持续接近高质量标准。两种策略结合，可同时优化指令和示例，获得针对特定任务的高效提示。

### 迭代提示 / 精炼

该技术从简单提示开始，根据模型初始响应不断优化。分析不足，调整提示，反复迭代，直至满意。

- **示例**：
  - _尝试 1_：“为新型咖啡机写产品描述。”（结果太泛）
  - _尝试 2_：“突出速度和易清洁。”（结果更好但细节不足）
  - _尝试 3_：“为‘SpeedClean Coffee Pro’写描述，强调 2 分钟冲泡和自清洁，面向忙碌职场人士。”（结果接近理想）

### 负面示例

虽然“正面指令优于约束”原则普遍适用，但在某些场景下，负面示例有助于明确边界或防止错误输出。

- **示例**：

生成巴黎热门景点列表，不包含埃菲尔铁塔。

错误示例：

输入：列举巴黎地标。

输出：埃菲尔铁塔、卢浮宫、圣母院。

### 类比使用

用类比帮助模型理解任务或输出，适用于创意或复杂角色说明。

- **示例**：

作为“数据厨师”，用原材料（数据点）烹制“总结菜肴”（报告），突出关键风味（趋势），面向商务受众。

### 分解认知 / 任务拆分

复杂任务可拆分为多个子任务，分别提示模型，最后合并结果。类似提示链和规划，但强调问题分解。

- **示例**：写研究论文：
  - 提示 1：“生成 AI 影响就业市场论文详细大纲。”
  - 提示 2：“根据大纲写引言。”
  - 提示 3：“写‘对白领影响’章节。”（其他章节同理）
  - 提示 N：“合并各章节并写结论。”

### 检索增强生成（RAG）

RAG 通过检索外部知识库信息，增强模型上下文，提升响应的准确性和时效性。用户提问时，系统先检索相关文档，将结果作为上下文加入提示，模型据此生成基于事实的回复，减少幻觉，支持动态或专有信息，是智能体系统关键模式。

- **示例**：
  - _用户查询_：“Python 库‘X’最新版本有哪些新功能？”
  - _系统操作_：检索文档数据库。
  - _LLM 提示_：“根据以下文档片段：\[插入检索内容\]，请说明 Python 库‘X’的新功能。”

### 用户画像模式（Persona Pattern）

角色提示为模型分配身份，用户画像则描述目标用户或受众，帮助模型调整语言、复杂度、语气和信息类型。

- **示例**：

你需向高中生解释量子物理，受众无相关基础，要求简单明了并用类比。

解释量子物理：\[插入请求\]

这些高级技术为提示工程师提供更多工具，优化模型行为、集成外部信息、定制智能体系统交互。

### Google Gems 使用

Google AI“Gems”是 Gemini 架构下的用户可配置特性，每个 Gem 是专用 AI 实例，针对特定任务定制。用户通过指令集定义 Gem 用途、响应风格和知识领域，模型在整个会话中始终遵循这些指令。

可创建专用智能体，如仅引用特定库的代码解释器、只生成摘要的分析助手、遵循特定风格的翻译器等。Gem 为 AI 建立持久、任务专用上下文，避免重复设定，提高效率和一致性，实现细粒度、持久化用户指令。

![图 1：Google Gem 使用示例](https://assets.jimmysong.io/images/book/agentic-design-patterns/appendix-a-advanced-prompting-techniques/f1.webp)图 1：Google Gem 使用示例

## 用 LLM 优化提示（元方法）

前述多种提示技术强调清晰、结构和上下文，但优化过程常需多次迭代。能否利用 LLM 自身帮助我们改进提示？这就是“元提示”——AI 辅助优化与 AI 交互的指令。

这种方法让 AI 成为提示工程的协作伙伴。实际操作时，可将现有提示、任务描述及当前输出（及不足之处）提供给 LLM，要求其分析并提出改进建议。

如 Gemini 等模型能分析提示中的歧义、缺乏具体性或表达低效，建议加入分隔符、明确输出格式、指定角色或补充少样本示例。

元提示优势包括：

- **加速迭代**：比纯人工试错更快获得优化建议。
- **发现盲点**：LLM 能发现提示中被忽略的歧义或误解。
- **学习机会**：通过 LLM 建议提升自身提示工程技能。
- **可扩展性**：可自动化部分提示优化，适合大规模场景。

需注意 LLM 建议并非总是完美，仍需评估和测试，但为优化提供了强大起点。

- **示例元提示**：

分析以下提示，提出改进建议，使其能稳定提取新闻主旨和关键实体（人物、组织、地点）。当前提示有时遗漏实体或主题。

现有提示：

“Summarize the main points and list important names and places from this article: \[insert article text\]”

改进建议：

此例展示了用 LLM 批判和优化提示的元级交互，是构建高效智能体系统的有力工具。

## 特定任务提示

部分任务需专门提示策略，尤其是代码和多模态输入领域。

### 代码提示

LLM（尤其是代码数据训练的模型）是开发者强大助手。代码提示包括生成、解释、翻译、调试代码等多种场景：

- **生成代码**：根据功能描述生成代码片段或函数。
  - **示例**：“写一个 Python 函数，输入数字列表，返回平均值。”
- **解释代码**：输入代码片段，要求模型逐行或总结解释。
  - **示例**：“解释以下 JavaScript 代码：\[插入代码\]。”
- **代码翻译**：要求模型将代码从一种语言翻译为另一种。
  - **示例**：“将以下 Java 代码翻译为 C++：\[插入代码\]。”
- **调试与评审**：输入有错误或需优化的代码，要求模型找出问题、建议修复或重构。
  - **示例**：“以下 Python 代码报‘NameError’，原因及修复方法？\[插入代码和报错\]。”

高效代码提示需提供足够上下文，明确语言和版本，清楚描述功能或问题。

### 多模态提示

随着模型支持多模态（文本、图片、音频、视频等），提示技术也在发展。多模态提示即用多种输入格式引导模型。

- **示例**：输入流程图图片并要求模型解释流程（图片 \+ 文本提示）；或输入图片要求模型生成描述性标题（图片 \+ 文本提示→文本输出）。

多模态能力提升后，提示技术将进一步发展以充分利用多种输入输出。

## 最佳实践与实验

提示工程是一门持续学习和实验的技能，以下最佳实践值得强调：

- **提供示例**：一/少样本示例是最有效的引导方式。
- **设计简洁**：提示应简明清晰，避免术语和复杂表达。
- **明确输出要求**：清楚定义期望格式、长度、风格和内容。
- **优先正面指令**：专注于告诉模型“做什么”而非“不做什么”。
- **控制最大 Token 长度**：用模型参数或提示指令管理输出长度。
- **提示变量化**：应用场景下用变量提升提示复用性，避免硬编码。
- **尝试不同输入格式和风格**：测试不同表达方式和语气，寻找最佳效果。
- **分类任务示例顺序随机化**：防止模型过拟合特定类别顺序。
- **适应模型更新**：模型不断升级，需测试并调整现有提示。
- **尝试不同输出格式**：尤其非创意任务，尝试 JSON、XML 等结构化输出。
- **与他人协作实验**：团队合作能带来更多有效提示。
- **CoT 最佳实践**：如答案置于推理后，单一答案任务温度设为 0。
- **记录提示尝试**：结构化记录提示、配置和结果，便于追踪和优化。
- **提示代码化管理**：应用集成时将提示存于独立文件，便于维护和版本控制。
- **自动化测试与评估**：生产系统需自动化测试和评估，确保提示泛化能力。

提示工程技能需不断实践。应用上述原则和技术，系统化实验和记录，可显著提升智能体系统开发能力。

## 总结

本附录系统介绍了提示工程，将其提升为一门工程学科，而非简单提问。核心在于将通用语言模型转变为专用、可靠、高效的工具。基础原则如清晰、简洁和迭代，是与 AI 高效沟通的基石，能减少自然语言歧义，提升模型输出确定性。零样本、单样本和少样本提示是通过示例展示期望行为的主要方法，强力塑造模型响应风格、语气和格式。结构化提示、角色分配和分隔符为模型控制提供了架构层。

在智能体系统开发中，这些技术尤为重要，为复杂多步操作提供可靠性和可控性。智能体要能有效规划和执行任务，需用思维链、思维树等高级推理模式，将复杂目标分解为可管理子任务。系统可靠性依赖于各组件输出的可预测性，因此请求结构化数据并用 Pydantic 等工具校验，是实现自动化的必要条件。否则，智能体内部认知组件无法可靠通信，自动化流程易出错。结构化和推理技术将模型的概率文本生成转化为智能体的确定性认知引擎。

此外，这些提示赋予智能体感知和行动能力，连接数字思维与现实世界。ReAct 和原生函数调用是智能体的“手”，可用工具、查询 API、操作数据；RAG 和上下文工程是智能体的“感官”，主动检索实时知识，确保决策基于最新事实，避免模型受限于静态训练数据。掌握全方位提示技术，是将通用语言模型升级为具备自主性、感知力和智能的智能体系统的关键。

## 参考文献

以下资源可供深入学习提示工程技术：

- [Prompt Engineering - kaggle.com](https://www.kaggle.com/whitepaper-prompt-engineering)
- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models - arxiv.org](https://arxiv.org/abs/2201.11903)
- [Self-Consistency Improves Chain of Thought Reasoning in Language Models - arxiv.org](https://arxiv.org/pdf/2203.11171)
- [ReAct: Synergizing Reasoning and Acting in Language Models - arxiv.org](https://arxiv.org/abs/2210.03629)
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models - arxiv.org](https://arxiv.org/pdf/2305.10601)
- [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models - arxiv.org](https://arxiv.org/abs/2310.06117)
- [DSPy: Programming—not prompting—Foundation Models - github.com](https://github.com/stanfordnlp/dspy)

[上一页FAQ](https://jimmysong.io/zh/book/agentic-design-patterns/faq/)

[下一页附录 B - 智能体交互：从 GUI 到现实世界环境](https://jimmysong.io/zh/book/agentic-design-patterns/appendix-b-ai-agentic-interactions/)

创建于 2025/09/11
更新于 2025/10/11
10584 字
阅读约 22 分钟

提交勘误/建议

加载评论中...0

giscus

正在加载评论……

### 来源 7: 激发LLM涌现——提示工程 - 李乾坤的博客

- URL: https://qiankunli.github.io/2023/10/29/llm_prompt.html
- 精读方法：firecrawl-scrape

- [什么是Prompt](https://qiankunli.github.io/2023/10/29/llm_prompt.html#%E4%BB%80%E4%B9%88%E6%98%AFprompt)
- [如何写好Prompt——结构化](https://qiankunli.github.io/2023/10/29/llm_prompt.html#%E5%A6%82%E4%BD%95%E5%86%99%E5%A5%BDprompt%E7%BB%93%E6%9E%84%E5%8C%96)
- [自动化提示词工程](https://qiankunli.github.io/2023/10/29/llm_prompt.html#%E8%87%AA%E5%8A%A8%E5%8C%96%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B)
- [工程示例](https://qiankunli.github.io/2023/10/29/llm_prompt.html#%E5%B7%A5%E7%A8%8B%E7%A4%BA%E4%BE%8B)
  - [不同角色的Prompt](https://qiankunli.github.io/2023/10/29/llm_prompt.html#%E4%B8%8D%E5%90%8C%E8%A7%92%E8%89%B2%E7%9A%84prompt)
  - [代码示例](https://qiankunli.github.io/2023/10/29/llm_prompt.html#%E4%BB%A3%E7%A0%81%E7%A4%BA%E4%BE%8B)
- [Prompt 能力有上限嘛？](https://qiankunli.github.io/2023/10/29/llm_prompt.html#prompt-%E8%83%BD%E5%8A%9B%E6%9C%89%E4%B8%8A%E9%99%90%E5%98%9B)
- [0706Prompt也是一种代码](https://qiankunli.github.io/2023/10/29/llm_prompt.html#0706prompt%E4%B9%9F%E6%98%AF%E4%B8%80%E7%A7%8D%E4%BB%A3%E7%A0%81)
- [其它](https://qiankunli.github.io/2023/10/29/llm_prompt.html#%E5%85%B6%E5%AE%83)

## 什么是Prompt [Permalink](https://qiankunli.github.io/2023/10/29/llm_prompt.html\#%E4%BB%80%E4%B9%88%E6%98%AFprompt "Permalink")

Prompt是运行在 LLM 上的程序。

由于LLMs的文本到文本格式，它们能够用单个模型解决各种各样的任务。这种能力最初是通过GPT-2和GPT-3等模型的zero-shot和few-shot学习来证明的。然而，当经过微调以符合人类偏好和指令时，大语言模型变得更加引人注目，使流行的生成应用程序成为可能，例如编码助手，信息搜索对话助理，基于聊天的搜索引擎体验。在此过程中，我们也见证了一个新的互补领域的发展——prompt工程。在高层次上，大语言模型的操作方式是：将文本(即prompt)作为输入，生成文本输出，从中我们可以提取有用的东西(例如，分类，摘要，翻译等)。这种方法的灵活性是有益的。然而，与此同时，我们必须确定如何正确地构造我们的输入prompt，使LLM最有可能产生期望的输出。

大语言模型自 GPT-2 以来就一直具备的一种能力，那就是通过与用户交互和提示语进行上下文学习（In-context Learning）。在 GPT-2 中，提示语主要被用来向模型传递“指令”信息，使模型了解其正在进行的任务。而在 GPT-3 之后，提示语的内容逐渐演变成为了包含“示例”和“指令”的形式。其中，“示例”部分负责为模型提供任务场景的相关样例，帮助其掌握其中的规律；而“指令”部分被沿用下来，目的仍然是让模型明确自己的任务目标。因此，提示语工程的本质其实是一种试图充分利用大语言模型上下文学习能力的方法。通过最佳的格式和最有效的示例及指令为模型提供指导，使其能更好地理解和解决给定问题。

[一文详解Prompt学习和微调（Prompt Learning & Prompt Tuning）](https://zhuanlan.zhihu.com/p/620222350)

1. 过去许多机器学习方法是基于全监督学习（fully supervised learning）的。由于监督学习需要大量的数据学习性能优异的模型，而在 NLP 中大规模训练数据（指为特定任务而标注好的数据）是不足的，因此在深度学习出现之前研究者通常聚焦于 **特征工程**（feature engineering），即利用领域知识从数据中提取好的特征；
2. 在深度学习出现之后, 由于特征可以从数据中习得，因此研究者转向了 **结构工程**（architecture engineering），即通过通过设计一个合适的网络结构来把归纳偏置（inductive bias）引入模型中，从而有利于学习好的特征。
3. 在 2017-2019 年，NLP 模型开始转向一个新的模式（BERT），即预训练 + 微调（pre-train and fine-tune）。在这个模式中, 先用一个固定的结构预训练一个语言模型（language model, LM），预训练的方式就是让模型补全上下文（比如完形填空）。由于预训练不需要专家知识，因此可以在网络上搜集的大规模文本上直接进行训练。然后这个 LM 通过引入额外的参数或微调来适应到下游任务上。此时研究者转向了 **目标工程**（objective engineering），即为预训练任务和微调任务设计更好的目标函数。
4. 在做 objective engineering 的过程中，研究者发现 **让下游任务的目标与预训练的目标对齐是有好处的**（预训练是文字接龙，就把目标任务也改为文字接龙的形式，预训练是文字填空，就把目标任务也改为文字填空）。因此下游任务通过引入文本提示符（textual prompt），把原来的任务目标重构为与预训练模型一致的填空题。比如一个输入 “I missed the bus today.” 的重构：

1. 情感预测任务。输入：“I missed the bus today.I felt so\_\_\_.” 其中 “I felt so” 就是提示词（prompt），然后使用 LM 用一个表示情感的词填空。
2. 翻译任务。输入：“English:I missed the bus today. French: \_\_\_.” 其中 “English:” 和 “French:” 就是提示词，然后使用 LM 应该再空位填入相应的法语句子。
5. 我们发现用不同的 prompt 加到相同的输入上，就能实现不同的任务，从而使得下游任务可以很好的对齐到预训练任务上，实现更好的预测效果。后来研究者发现，在同一个任务上使用不同的 prompt，预测效果也会有显著差异，因此现在有许多研究开始聚焦于 **prompt engineering**。

GPT-3论文定义：如果需要（基于梯度下降为主的算法）对模型参数进行更新，就是fine-tune。如果不需要修改模型和参数，只要给模型一些提示和样例，就让模型复合我们的一些要求完成一些任务就叫in-context learning，后面大家开始叫prompt。GPT 模型可以使用prompt 和 fine tune两种方式进行训练和使用，取决于具体的应用场景和任务需求。prompt 是第一种针对GPT 模型的特殊训练方式， **不需要大量数据，不需要对模型参数进行改动，也就意味着可以不部署模型，而是接入公开的大预言模型服务（MaaS）**。缺点是，模型生成的内容受限于提示信息，不能够完全发挥模型的潜力。PS：即便是AGI，你也得在具体提问上需要告诉模型任务是什么。

[我对Prompt Engineering的理解](https://mp.weixin.qq.com/s/fLtYMwqefoDSeypOuY8bUA)“提示工程（Prompt Engineering）” 这一概念源于语言模型的发展，它描述了如何有效地 **利用提示从语言模型中提取信息** 的过程，包括选择合适的词汇、语法、上下文和主题等元素。 PS：准备样本 ==> 准备提示。 **提示词的本质就是收窄范围**。p(input)=output，为了让模型输出期待的output，找到合适的input。

1. 在语言模型中，“提示” 是用户提供给模型的输入。在 ChatGPT 中，它可以理解为你输入文本框的文字。然后，语言模型根据你的提示 “推断” 出一个 “补全”。
2. “提示工程” 是利用提示作为一种从模型中提取所需信息的方法。这种方法很有吸引力，因为你不需要大量的离线训练数据集，不需要离线访问模型，而且对于非工程师来说也很直观。提示只是调整模型的一种方式。
3. “提示工程” 是一种更严谨的领域， **旨在利用提示作为一种为实际应用构建可靠功能的方法**。它与 ChatGPT 式的提示有所不同，因为通过提示工程生成的提示通常用于在高频、多样化的场景中反复使用， **以便为应用程序可靠地解决特定问题**。

[五万字综述！Prompt Tuning：深度解读一种新的微调范式](https://mp.weixin.qq.com/s/-lfq63NrsqUgmvYNzogCew)

1. Prompt-Tuning自从GPT-3被提出以来，从传统的离散、连续的Prompt的构建、走向面向超大规模模型的In-Context Learning、Instruction-tuning和Chain-of-Thought。
2. 自从GPT、EMLO、BERT的相继提出，以Pre-training + Fine-tuning 的模式在诸多自然语言处理（NLP）任务中被广泛使用，其先在Pre-training阶段通过一个模型在大规模无监督语料上预先训练一个 预训练语言模型（Pre-trained Language Model，PLM） ，然后在Fine-tuning阶段基于训练好的语言模型在具体的下游任务上再次进行 微调（Fine-tuning） ，以获得适应下游任务的模型。这种模式在诸多任务的表现上超越了传统的监督学习方法，不论在工业生产、科研创新还是竞赛中均作为新的主流方式。然而，这套模式也存在着一些问题。例如，在大多数的下游任务微调时， **下游任务的目标与预训练的目标差距过大 导致提升效果不明显，微调过程中依赖大量的监督语料** 等。
3. 至此，以GPT-3、PET为首提出一种基于预训练语言模型的新的微调范式——Prompt-Tuning ，其旨在 **通过添加模板的方法来避免引入额外的参数**，从而让语言模型可以在小样本（Few-shot）或零样本（Zero-shot）场景下达到理想的效果。
4. 以二分类的情感分析作为例子，给定一个句子`[CLS] I like the Disney films very much. [SEP]`
1. 传统的Fine-tuning方法是将其通过BERT的Transformer获得 `[CLS]`表征之后再喂入新增加的MLP分类器进行二分类，预测该句子是积极的（positive）还是消极的（negative），因此需要一定量的训练数据来训练。
2. Prompt-Tuning则执行如下步骤：
      1. 构建模板（Template Construction） ：通过人工定义、自动搜索、文本生成等方法，生成与给定句子相关的一个含有`[MASK]`标记的模板。例如`It was [MASK]`，并拼接到原始的文本中，获得Prompt-Tuning的输入：`[CLS] I like the Disney films very much. [SEP] It was [MASK]. [SEP]`。将其喂入BERT模型中，并复用预训练好的MLM分类器，即可直接得到`[MASK]`预测的各个token的概率分布；
      2. 标签词映射（Label Word Verbalizer） ：因为`[MASK]`部分我们只对部分词感兴趣，因此需要建立一个映射关系。例如如果`[MASK]`预测的词是“great”，则认为是positive类，如果是“terrible”，则认为是negative类。
3. 不同的句子应该有不同的template和label word，没错，因为每个句子可能期望预测出来的label word都不同，因此如何最大化的寻找当前任务更加合适的template和label word是Prompt-tuning非常重要的挑战。
4. 其实我们可以理解，引入的模板和标签词本质上也属于一种数据增强，通过添加提示的方式引入先验知识。
5. GPT-3开创性提出 in-context learning 概念，即无须修改模型即可实现few-shot/zero-shot learning。同时引入了demonstrate learning，即让模型知道与标签相似的语义描述，提升推理能力。
1. In-context Learning ：是Prompt的前身。其通过从训练集中挑选一些样本作为任务的提示提示（Natural Language Prompt），来实现免参数更新的模型预测；
2. Demonstration Learning ：添加一些新的文本作为提示。例如在对“I like the Disney film. It was \[MASK\]”进行情感分析时，可以拼接一些相似场景的ground-truth文本“I like the book, it was great.”、“The music is boring. It is terrible for me.”等。此时模型在根据新添加的两个样例句子就可以“照葫芦画瓢”式地预测结果了。

[ChatGPT Prompt工程：设计、实践与思考](https://mp.weixin.qq.com/s/AizUBFssilX2S9aRfuz3_g) 未细读。

[关于AI未来，我有十二条自用的思考Prompt分享](https://mp.weixin.qq.com/s/7eah_qMhol4EBwrz1bzxeA)

[AI大模型如何在行业实际落地：企业对话场景拥抱大模型之路](https://qiankunli.github.io/2023/10/29/AI%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%A6%82%E4%BD%95%E5%9C%A8%E8%A1%8C%E4%B8%9A%E5%AE%9E%E9%99%85%E8%90%BD%E5%9C%B0%EF%BC%9A%E4%BC%81%E4%B8%9A%E5%AF%B9%E8%AF%9D%E5%9C%BA%E6%99%AF%E6%8B%A5%E6%8A%B1%E5%A4%A7%E6%A8%A1%E5%9E%8B%E4%B9%8B%E8%B7%AF)

1. 提示工程主要是为了解决预训练语言模型训练过程的任务和实际业务的任务之间不一致的问题。通过提示语，可以让预训练语言模型理解当前任务的类型，从而可以更好地完成任务。随着 NLP 技术的飞速发展，现在的提示工程已变得更为复杂， **提示语通常包含任务指令、任务目标、行为约束、输出规范、资源清单、样例展示和思维能力提示等要素**。给每个任务找到合适的提示语还是一个很大的挑战。不同的任务需要差异化的 Prompt 模版（PromptTemplate），从指令设计、样例选择、样例的顺序以及推理过程等细节进行 prompt 的优化微调，每一个环节都可能影响到 Prompt 在实际应用的场景效果。测试结果显示，在意图识别上，不同的 Prompt 的准确率能达到 2%~80% 的巨大差距。
2. Prompt 工程可能是暂时的一个中间过程。只是说， **现在大模型的能力还没有达到基于人工设定的复杂任务目标去自主性进行任务分解，然后根据这些任务转化成一种它可以直接解决的细粒度的自然语言任务**。现在大模型需要中间的提示工程师帮助它理解任务，然后转化成它可以直接执行的自然语言任务，这中间是一个适配的过程”。未来随着大模型的能力向更高层级提升，会覆盖掉现有的 Prompt 工程。

## 如何写好Prompt——结构化 [Permalink](https://qiankunli.github.io/2023/10/29/llm_prompt.html\#%E5%A6%82%E4%BD%95%E5%86%99%E5%A5%BDprompt%E7%BB%93%E6%9E%84%E5%8C%96 "Permalink")

为模型增加外部记忆，在提示词中引入一些领域知识，帮助模型提升回答质量。只需给予大模型详细的指令，清晰表达任务约束或规范，超大模型就能够按指令要求地完成任务。

[人人都需要掌握的Prompt Engineering技巧](https://mp.weixin.qq.com/s/JvoBOzdHmagLXiT2k1nYPQ) 对于一些复杂的问题，Prompt写得好不好，直接影响着大模型给出答案的正确与否。本质上， **LLM是一个概率模型，它只是在给定的信息的前提下，给出概率最大的结果，它并不保证结果的合理性和正确性**。要让LLM给出的结果尽可能地合理、正确，这是我们使用LLM的人的职责。

![](https://qiankunli.github.io/public/upload/machine/prompt_principle.jpg)

AI界的大佬 — Andrew NG推出过一个Prompt Engineering的短课程《ChatGPT Prompt Engineering for Developers》，提到写好Prompt的一些基本理念。PS： **ICL给示范/示例，CoT给思路**，老师教学也是这么搞的。

1. 明确、具体是关键。我们发给LLM的批令，越明确、越具体，对于LLM越友好。
    ![](https://qiankunli.github.io/public/upload/machine/prompt_tips.jpg)
2. 另一种视角：立角色 \+ 述问题 \+ 定目标 \+ 补要求。
3. ICIO： Instruction（指令） + Context（上下文/背景）+ Input Data（输入数据）+ Output Indicator（输出指示器）
4. 给LLM更多的时间去思考。通过Prompt Engineering 的方式，把LLM的“慢思考”调动起来。
1. 一个简单的技巧是在你的Prompt后面，加上这样一句话“Let’s think step by step”。这句话会引导LLM，会去分步骤思考，效果会比不加这句话要好。
2. CoT(Chain-of-Thought) 在Prompt中加入一些例子，让LLM照着例子进行推理、思考。注意，CoT是LLM足够大（参数足够多，通常是在1000亿参数）时才涌现出来的能力。因此，在一些不够大的LLM上，CoT的效果并不明显。此外，在Prompt中加入的示例不是1条，而是多条。具体要考虑解决的问题类型，以及Prompt的长度（因为LLM的Prompt长度通常都是有长度限制的）。
5. Self-Consistency技术：利用CoT Prompting技巧，写好Prompt；不要让LLM只生成最合适的唯一一个结果，而是利用LLM结果的多样性，生成多种不同推理路径所得的结果的集合；从结果集合中投票选择，选出投票最多的结果，做为最终的答案。
6. 从易至难技术：Least-to-Most，CoT的特点是同类型问题的迁移思考，因此，如果给的例子是比较简单的问题，而给的问题却是难度大很多的问题，这时候CoT的效果就不尽如人意。LtM(Least-to-Most)主是为了解决CoT这种从易到难的迁移能力不足而诞生的。LtM的核心思想是：教LLM把复杂问题，拆解成一系列的简单问题，通过解决这一系列的简单问题，来最终得到复杂问题的结果。LtM的过程包含两个阶段：
1. 分解阶段：把复杂问题分解成一系列的简单子问题。这个阶段的Prompt中要包含分解问题的示例，要和分解的问题；
2. 解决子问题阶段：这个阶段的Prompt中包含三部分内容：一是完整的LtM的例子；二是已解决的子问题及其答案列表；三是接下来要解答的子问题。
7. TOT就是让LM对输入prompt不直接输出最终结果，而是输出递进的中间结果，然后将可能的中间结果维护成树状结构，并利用LM对树上的中间结果进行打分，通过某种search方法，搜索出分数更高的叶子节点，作为最终的回复。
8. 在优化提示词过程中，需要人工学习上一轮大模型判断错误例子的数据特征，如果人工再去浏览上千字的对话文本费时费力，这里可以做一个简化操作，就是让大模型不仅输出是否合规的结论， **还要输出判定的依据**，这样我们在人工浏览时可以根据大模型给出的依据快速定位到这些原文中的片段，而不用通读全文，只需分析这些片段的数据特征即可。PS：你认为llm为何错了不重要，llm认为自己为何错了才重要。

[构建高性能 Prompt 之路——结构化 Prompt](https://zhuanlan.zhihu.com/p/647134737)

[GPT Prompt编写的艺术：如何提高AI模型的表现力](https://mp.weixin.qq.com/s/N8XnSSdXlIITSig5z1oZCw) 目标、问题、上下文、要求，针对各个场景罗列了写prompt 的具体技巧和案例。

目前网上已经有不少 prompt 优化工具，比如 chatgpt 的插件中就有一个不错的工具 prompt perfect，能够 **基于用户给的 prompt 进行优化**，再喂给 chatgpt 进行提问

![](https://qiankunli.github.io/public/upload/machine/prompt_perfect.jpg)

https://prompt.always200.com/

## 自动化提示词工程 [Permalink](https://qiankunli.github.io/2023/10/29/llm_prompt.html\#%E8%87%AA%E5%8A%A8%E5%8C%96%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B "Permalink")

APE就是利用LLM来自动化地帮助我们生成提示词。那么问题来了，我们怎么知道LLM生成的提示词好不好呢？它有没有满足我们的要求呢？因此，为了使用APE，我们必须要指定一个明确的metric。基于这个metric，我们能够自动化地评测当前所生成的提示词，它的性能表现达到什么程度了。

1. 定义metric并不是一件容易的事。DSPy框架为此提供了一些常见的metric。
2. 有了metric，那么它具体是在什么数据集上进行评测呢？为此，我们还需要提供一个标注好的数据集 (labelled dataset)。当然，在实际使用时，这个数据集会被划分为训练集、验证集、测试集。
3. APE是一个不断迭代的过程。每生成一个新版的prompt，它就会根据metric，在数据集上进行评测得到一个分数（score）。只要新版prompt比旧版本的prompt能够取得更高的分数，APE就可以不断重复这个过程，从而得到越来越好的prompt。
4. 在迭代的开始，我们还需要提供一个初始的提示词 (initial prompt)，作为优化迭代的起点。另外，由于在APE中提示词是由LLM生成的，因此我们还需要一个为了生成新提示词而使用的提示词，称为meta-prompt。

## 工程示例 [Permalink](https://qiankunli.github.io/2023/10/29/llm_prompt.html\#%E5%B7%A5%E7%A8%8B%E7%A4%BA%E4%BE%8B "Permalink")

通过增强大语言模型输入的质量，来提升生成内容质量。

[硬核Prompt赏析：HuggingGPT告诉你Prompt可以有多“工程”](https://mp.weixin.qq.com/s/Cu2BpzWOuphrVsZ69JR9Hw) 值得细读。

### 不同角色的Prompt [Permalink](https://qiankunli.github.io/2023/10/29/llm_prompt.html\#%E4%B8%8D%E5%90%8C%E8%A7%92%E8%89%B2%E7%9A%84prompt "Permalink")

System message 在大模型内部是每次加在了用户输入的前面。在 OpenAI 的大模型设计的时候，有三种不同的 message 类型，分别是System Message、Assistant Message 以及 User Message，这三者是有明显区别的。其中 User Message 最好理解，就是我们用户写的信息，Assistant Message 就是大模型写的信息，而 System Message 则是对大模型的角色进行定义，并输入一些基础的指令，包括大模型的身份、一些用于提高安全性的指令。

1. System Message 和 User Message 的不同之处就是，System Message 一般都是出现在输入的开始，根据大模型注意力机制的公式，在开始和结尾处的文字更容易被重视。因此，在这些地方出现的内容，更容易被大模型识别和理解。所以，一个完整的提示词，或者多轮对话的场景一般是按照下面的流程去拼接和组装提示词的：`System Message、User Message、Assistant Message、User Message 。。。、Assistant Message`，在这种对话下，Assistant Message 主要是向大模型展示他历史聊天记录的内容，并告知大模型其中的哪些内容是由用户的输入生成的。按照这种模式进行训练和微调的大模型就会意识到，那些内容并不是用户真实的输入，而是一个聊天对话的历史信息，这样大模型就不仅能理解历史的信息，还能更好的回答你接下来的问题。
2. 为什么 System Message 并不和 User Message 合并在一起呢？我们在微调的时候，可以定义不同的消息类型，去避免一些提示词注入和攻击的问题。这个时候，只需要在 System Message 中定义好大模型的角色，而将其他内容放在 User Message 中，就可以避免一些简单的提示词攻击和泄露的情况。而且当我们做成应用的时候，System Message 是对用户不可见的，在这个地方定义的规则、角色由于得到了充分的训练，就具有最高的优先级。大模型就会在很大概率上遵循这个定义，而不是随着用户输入的改变而输出一些违背开发者原来意思的内容。当然，指定 System Message 并不能完全的抵御外来的攻击，之前 GPT4 还是出现过 System Prompt 被套出来的情况，这种情况下，就需要对用户输入的内容或者大模型输出的内容进行二次校验或许是一个更好的方案。

### 代码示例 [Permalink](https://qiankunli.github.io/2023/10/29/llm_prompt.html\#%E4%BB%A3%E7%A0%81%E7%A4%BA%E4%BE%8B "Permalink")

零样本

```
from langchain import PromptTemplate
template = "What is a good name for a company that makes {product}?"
prompt = PromptTemplate(
    input_variables=["product"],
    template=template,
)
prompt.format(product="colorful socks")
```

小样本

```
from langchain import PromptTemplate, FewShotPromptTemplate
examples = [\
    {"word": "happy", "antonym": "sad"},\
    {"word": "tall", "antonym": "short"},\
]
example_template = """
Word: {word}
Antonym: {antonym}\n
"""
example_prompt = PromptTemplate(
    input_variables=["word", "antonym"],
    template=example_template,
)
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Give the antonym of every input",
    suffix="Word: {input}\nAntonym:",
    input_variables=["input"],
    example_separator="\n",
)
few_shot_prompt.format(input="big")
```

以上代码将生成一个提示模板，并根据提供的示例和输入组合成以下提示：

```
Give the antonym of every input

Word: happy
Antonym: sad

Word: tall
Antonym: short

Word: big
Antonym:
```

## Prompt 能力有上限嘛？ [Permalink](https://qiankunli.github.io/2023/10/29/llm_prompt.html\#prompt-%E8%83%BD%E5%8A%9B%E6%9C%89%E4%B8%8A%E9%99%90%E5%98%9B "Permalink")

[Prompt工程如此强大，我们还需要模型训练吗？ - 算法小陈的回答 - 知乎](https://www.zhihu.com/question/586331504/answer/3125792161)

1. 在GPT没有爆火之前，一直以来的共识都是：模型的规模越大，模型在下游任务上的能力越多、越强。LLM原始训练目标是为了生成自然、连贯的文本，因为其本身接受了大量的文本进行预训练，因此根据提示补全和创造文本就是模型的原生能力。不过，仅仅能进行文本创造，并不足以让大语言模型掀起新的一轮技术革命，引爆这一轮技术革命的真正原因是：大语言模型的 **涌现能力**。针对这些在小模型上没有出现，但是在大模型上出现的不可预测的能力，就被称为涌现能力，换句话说：所谓涌现能力（EmergentCapabilities），指的是 **模型在没有针对特定任务进行训练的情况下，仍然能够在合理提示下处理这些任务的能力**，有时也可以将涌现能力理解为模型潜力，巨大的技术潜力，是LLM爆火的根本原因。
2. 激发大型语言模型的涌现能力有两种方法：提示工程（prompt engineering）和微调（fine-tuning）。对于这两种方法各自有各自使用的应用场景， **提示工程解决的问题，往往不会用微调（如小语义空间内的推理问题），微调通常用于解决那些无法通过特征工程解决的问题**。它们更多的时候是作为上下游技术关系，例如要进行本地知识库的定制化问答，最好的方法就是借助提示工程进行数据标注，然后再利用标注好的数据进行微调。
3. 相比模型的原生能力，模型的涌现能力是非常不稳定的，要利用提示工程和微调技术来引导和激发模型的涌现能力，难度很大。在不修改模型本身参数（微调）的情况下，模型涌现能力极度依赖对模型的提示过程，即对同样一个模型，不同的提示方法将获得质量完全不同的结果。
4. 对于提示工程来说，其侧重点是要解决复杂语义理解问题，而要验证模型是否具备这种能力，可以观察模型是否能解决复杂逻辑推理问题。
1. ‘text-davinci-003’在Zero-shot的情况下，逻辑推理能力较弱，只能围绕相对简单的、只有线性运算过程的推理问题进行很好的解答。 **四个经典推理问题只能答对一个**。如何加强模型的逻辑处理能力？
2. One-shot & Few-shot提示学习法。通过输入一些类似问题和问题答案，让模型参考学习，并在同一个prompt的末尾提出新的问题，依次提升模型的推理能力。虽然无法确定模型预测过程发生了何种变化，Few-shot提示方法能够一定程度提高模型推理能力，但提升的幅度有限，对于稍微复杂些的推理问题，模型仍然无法做出准确的回答。 **四个经典推理问题答对二个**。
3. Few-shot有非常多的变种方法，其中一类非常重要的变种方法就是围绕提示的示例进行修改，即在示例中不仅提供问题+答案，同时还会增加一些辅助思考和判断的“提示”。Zero-shot-CoT是在Few-shot思想下，一种更好的提示方法。它借助思维链（也被称为思考链，Chain of Thought，CoT）提示法来解决这个问题。一种非常简单而有效的方式是：在提示词尾部追加一句“Let’s think step by step”，即可大幅提高模型推理能力。 **四个经典推理问题答对三个**。
4. Zero-shot-CoT是零样本提示的情况下通过修改提示词后缀激发模型的思维链，而Few-shot-CoT则是通过编写思维链样本作为提示词，让模型学会思维链的推导方式，从而更好的完成推导任务。相比于Few-shot，Few-shot-CoT的不同之处只是在于需要在提示样本中不仅给出问题的答案、还同时需要给出问题推导的过程（即思维链），从而让模型学到思维链的推导过程，并将其应用到新的问题中。
5. 在谷歌大脑提出的CoT被实际验证能够大幅提升大语言模型的推理能力不久，来自谷歌大脑的另一个团队在此基础上提出了一种名为Least-to-Most（LtM）的提示方法，初衷是为了解决CoT提示方法泛化能力不足的问题——即通过人工编写的思维链提示样本可能并不能够很好的迁移到别的问题当中去，导致“新的问题”无法使用“老的模板”进行解决。即然要找到更加普适的解决问题的流程会非常复杂，那能否“千人千面”让大模型自己找到解决当前问题的思维链呢？基于这个思路开发了一种全新的提示流程，即先通过提示过程让模型找到解决该问题必须要分步解决哪几个问题，然后再通过依次解决这些问题来解决最原始的问题。而整个依次回答问题的过程，其实就可以看成是CoT的过程，只不过LtM会要求模型根据每个不同的问题，单独生成解决问题的链路，以此做到解决问题流程的“千人千面”，从而能够更加精准的解决复杂推理问题。而整个过程问题的由少变多，则是LEAST-TO-MOST一词的来源。通过提示模板“To solve \_\_, we need ti first solve:”来引导模型创建子问题，然后先解决这个子问题，之后将原问题、子问题和问题和答案三部分都作为prompt输入给大语言模型，让其对原始问题进行回答。所以，LtM的核心并不仅仅在于引导模型拆分问题，还在于及时将子问题的问题和答案回传给模型，以便更好的围绕原始问题进行回答。 **四个经典推理问题答对四个**。

## 0706Prompt也是一种代码 [Permalink](https://qiankunli.github.io/2023/10/29/llm_prompt.html\#0706prompt%E4%B9%9F%E6%98%AF%E4%B8%80%E7%A7%8D%E4%BB%A3%E7%A0%81 "Permalink")

首先Prompt和代码都是人工可读的，甚至Prompt的可读范围是更大的，因为它使用自然语言，不需要读者学习对应的编程语言语法。 **Prompt也跟代码一样应该进行版本控制，记录变更历史**。

[用系统架构思维，告别“意大利面条式”系统提示词](https://mp.weixin.qq.com/s/_dfHk0IjYsYkDvIxZ02Rmw) 让我们来看一下其中一些规则的片段：

```
...
- 相比不提供，Dia 应更倾向于提供‘简单回答’……
- 如果你的回应中将包含项目符号或编号列表，则不要包含‘简单回答’……
- 当用户寻求生活帮助或进行休闲对话时，绝不要使用‘简单回答’。

- ……应包含尽可能多的‘问 Dia’超链接，就像维基百科页面那样……
- 绝不要在实际的URL或域名上使用‘问 Dia’超链接……

- 图片可以紧跟在‘简单回答’之后出现
- 图片可以在标题之后出现
- 图片不能出现在段落之后
- 对于这些主题或话题，Dia 绝不能显示图片：编码、天气状况……
- 当基于 `<pdf-content>` 或 `<image-description>` 中的任何内容生成回应时，你绝不能包含任何图片或媒体……
...
```

这东西要怎么维护？这不就是一份注定要变成“技术屎山”的设计文档吗？这种“规则清单式”的设计模式并非个例，它在工程实践中必然会导致三大困境：

1. 规则打架，行为摇摆不定：让我们聚焦于simple answer（简单回答）的规则。它同时存在“应尽可能包含”、“列表内容不包含”、“休闲对话不包含”等多条互斥的条件。现在，如果用户用一种休闲的口吻询问一个可以被列表回答的问题，模型应该遵循哪条规则？由于缺乏一个清晰的决策仲裁机制，模型的行为可能变得不可预测。它到底会做什么，更像是在“猜”，而不是在遵循一个确定的逻辑。
2. 越改越乱，最终没人敢动：现在，假设产品经理要求“在所有标题后都不能加图片”。你必须在海量的文本中找到所有与“图片位置”相关的规则，并小心翼翼地修改它们，同时祈祷这个修改不会与某个关于“列表”或“简单回答”的规则产生新的冲突。这种维护方式，就像在修改一个没有变量、没有模块的老旧代码库。所有逻辑都耦合在一起，任何微小的改动都可能引发雪崩效应。久而久之，提示词变得像“叠叠乐”高塔，摇摇欲坠，没人再敢轻易触碰。
3. 响应像“开盲盒”，核心价值被稀释：Dia 的一个核心价值是“通过视觉元素提升体验”。然而，关于何时显示、何时禁止显示图片的规则被分散在各处，甚至有一条基于上下文（如`<pdf-content>`）的最高优先级禁令。模型有限的“注意力”被大量琐碎的规则所稀释，导致其在判断是否应该插入图片时，可能会因为一条次要规则而忽略了其核心的“视觉化”价值。最终的响应效果就像在“开盲盒”，时好时坏，无法稳定地传递产品的核心价值。

问题的根源，并非某条规则写得不好，而是这种“规则清单”式的设计模式本身存在结构性缺陷。它把一个本应有机的、智能的系统，降维成了一堆离散、扁平的指令。如果我们继续扮演“规则的管理者”，就永远无法摆脱上述困境。我们必须进行一次彻底的思维范式转换：停止堆砌规则，开始构建系统。运用「系统架构思维」进行设计，摒弃“头痛医头，脚痛医脚”的线性修补模式，当应用于提示词设计时，系统思维的核心在于：

1. 关联性认知：系统中任何一条要素的价值，都体现在与其他要素的互动中。单一要素是孤立的，只有当它被置于一个完整的决策框架中时，其真正的作用才能稳定发挥。
2. 层次性拆解：将一个复杂的、庞大的系统，分解为可管理的、功能独立的子系统。这正是我们将一个巨大的提示词拆解为不同功能模块的理论基础。
3. 动态性适应：系统需要根据环境变化（如用户输入的变化）调整其行为，并通过反馈机制实现持续优化。一个设计良好的提示词系统，应该能根据不同的对话场景，动态调用不同的功能模块和行为逻辑。

系统架构思维：构建智能体的“蓝图”，这份蓝图通过回答三个核心问题，来确保系统的所有组件都能协同工作，达成最终目标：

1. 我是谁？ -\> 角色定位：定义系统的身份、服务主体与边界。
2. 我该做什么？-\> 目标定义：建立系统的核心使命与价值主张。
3. 我该怎么做？ -\> 能力与流程：规划系统实现目标的具体路径和方法。

基于系统架构思维，我们构建了一个由四个核心层级组成的、高度结构化的提示词设计框架。这四层从内到外，从核心到边界，共同定义了一个健壮、可维护的智能体系统。它们分别是：

1. 第一层：核心定义: 定义系统的内核——我是谁，我为何存在？
1. 角色建模。一个清晰的角色设定，是解决“规则打架”问题的最高仲裁者。当多条规则冲突时，AI可以回归其核心“人格”来做出最符合其身份的决策。
2. 目标定义。它清晰地定义了“做什么”和“不做什么”，是所有功能模块的最终归宿。通过明确核心价值，可以有效应对“核心价值被稀释”的问题。
2. 第二层：交互接口: 定义系统与外部世界的沟通方式——我如何感知世界，又如何被世界感知？
1. 输入规范。这是系统的“数据接入层” (Data Ingestion Layer)。它负责将外部世界的混乱信息，结构化地提供给内部处理模块。
2. 输出规格。这是系统的“表示层” (Presentation Layer)。它应独立于内部逻辑，专门负责定义最终交付物的结构、格式和布局。将“思考什么”与“如何呈现”分离，是解决“越改越乱”问题的核心手段。
3. 第三层：内部处理: 定义系统的“思考”与“行动”逻辑——我如何一步步完成任务？
1. 能力拆解。将AI需要具备的所有能力，拆解成一个个高内聚、低耦合的“技能模块”。每个模块只负责一件事情。
2. 流程设计。如果说能力是静态的技能，那么流程就是动态的行动剧本。它定义了AI在接收到用户请求后，如何按顺序、有逻辑地调用各个“能力模块”，最终完成任务。一个清晰的流程，能为AI的行为提供可预测的路径，从而解决“响应像开盲盒”的问题。
4. 第四层：全局约束: 定义系统不可逾越的边界——我绝对不能做什么？这是系统的“安全护栏”，定义了AI在任何情况下都不能逾越的红线。它拥有最高的执行优先级。
1. 硬性规则。绝对不能违反的指令，通常涉及安全、伦理、法律等方面（例如：“绝不能在基于`<pdf-content>`的上下文中包含任何外部媒体”）。
2. 求助机制。当遇到无法处理的情况或功能不支持时的固定行为模式（例如：“当被要求执行编码任务时，礼貌地拒绝并解释自己是对话AI”）。

## 其它 [Permalink](https://qiankunli.github.io/2023/10/29/llm_prompt.html\#%E5%85%B6%E5%AE%83 "Permalink")

**与其给语言模型告诉他什么做错了，不如告诉他怎么做是对的**。有人研究过使用语言模型要怎么样比较有效，有一个发现就是与其告诉语言模型不要做什么，不如告诉他要做什么。如果你希望它文章写短一点，你要直接跟它说写短一点，不要告诉它不要写太长。让它不要写太长，它不一定听得懂，叫它写短一点，比较直接，它反而比较听得懂。

少量的业务知识，比如只是几百几千的内容，给到足够上下文是成本最低，性价比最高的方案。微调且无法快速适应业务知识变化，对于我们的大部分场景是投入产出比非常低的事情。

预训练+微调范式主要是让预训练语言模型去适配下游任务，通过 **引入下游任务的loss**，让模型在具体任务上继续训练，以便在下游任务上取得较好的成绩。在这个过程中，语言模型会遗忘预训练过程中学到的知识，造成模型泛化性和鲁棒性的丢失，仅能保留某个任务或者某个数据的信息。而且随着语言模型的逐渐变大，模型本身已经存储了大量的知识，因为具体的下游任务微调导致原本模型能力丧失，是大家不愿意看到的。因此预训练+提示+预测的范式成为LLM主流使用方法，该模式 **让下游任务去适配预训练语言模型**，通过对下游任务的重构，让下游任务符合模型预训练过程，消除预训练任务与下游任务之间的差异，使得下游任务在少样本甚至零样本上可以获得较好的成绩，提高模型的泛化性和鲁棒性。具体而言，提示学习是在原始输入文本上附加额外的提示信息作为新的输入，将下游的预测任务转化为语言模型任务，并将语言模型的预测结果转化为原本下游任务的预测结果。以情感分析任务为例

1. 原始任务 input=“我爱中国”，output=正向/负向
2. 提示学习 input=“我爱中国，这句话的情感为{mask}”，output=mask值，再将mask值映射到情感标签上。

#### 留下评论

```
An error occurred

URI_TOO_LONG

iad1::
```

## 猜您还喜欢

## [从长期回报、Credit Assignment 到 PPO](https://qiankunli.github.io/2026/04/06/rl-mainline.html)

2026/04/06

5 分钟阅读

## [Code Agent](https://qiankunli.github.io/2026/04/04/code_agent.html)

2026/04/04

4 分钟阅读

简介（未完成）

## [Long-horizon Agent](https://qiankunli.github.io/2026/02/16/long_horizon.html)

2026/02/16

3 分钟阅读

简介（未完成）

## [next prompt工程——skill](https://qiankunli.github.io/2026/02/07/skill.html)

2026/02/07

3 分钟阅读

简介

输入您要搜索的关键词...

### 来源 8: 文生文Prompt指南 - 阿里云帮助文档

- URL: https://help.aliyun.com/zh/model-studio/prompt-engineering-guide
- 精读方法：firecrawl-scrape

[官方文档](https://help.aliyun.com/zh)

[有奖调研](https://survey.aliyun.com/apps/zhiliao/u72JLBHwp?ID=XX&WAY=1)

输入文档关键字查找

人工智能与机器学习

人工智能平台

- [人工智能平台 PAI](https://help.aliyun.com/zh/pai/)
- [智能计算灵骏](https://help.aliyun.com/zh/product/435019.html)

模型平台与服务

- [大模型服务平台百炼](https://help.aliyun.com/zh/model-studio/)
- [向量检索服务 DashVector](https://help.aliyun.com/zh/product/2510217.html)

智能搜索与推荐

- [智能推荐 AIRec](https://help.aliyun.com/zh/airec/)
- [智能开放搜索 OpenSearch](https://help.aliyun.com/zh/open-search/)
- [AI 原生搜索 CleverSee](https://help.aliyun.com/zh/product/3037946.html)

视觉智能

- [文字识别](https://help.aliyun.com/zh/ocr/)
- [视觉智能开放平台](https://help.aliyun.com/zh/viapi/)
- [图像搜索](https://help.aliyun.com/zh/image-search/)
- [智能视觉生产（文档停止维护）](https://help.aliyun.com/zh/product/133692.html)

自然语言处理

- [自然语言处理](https://help.aliyun.com/zh/product/60058.html)
- [地址标准化](https://help.aliyun.com/zh/address-purification/)
- [机器翻译](https://help.aliyun.com/zh/machine-translation/)
- [文档智能](https://help.aliyun.com/zh/document-mind/)

智能语音交互

- [智能语音交互](https://help.aliyun.com/zh/isi/)

决策智能

- [优化求解器](https://help.aliyun.com/zh/optimization-solver/)

AI应用

- [数知地球 AI Earth](https://help.aliyun.com/zh/product/127787.html)
- [虚拟数字人](https://help.aliyun.com/zh/avatar/)
- [工作学习 AI 助手通义听悟](https://help.aliyun.com/zh/tingwu/)
- [角色对话智能体通义星尘](https://help.aliyun.com/zh/product/2861601.html)
- [企业 Agent 应用平台](https://help.aliyun.com/zh/product/2987146.html)
- [Agent 观测与优化 AgentLoop](https://help.aliyun.com/zh/product/3033820.html)
- [电商经营助手](https://help.aliyun.com/zh/product/3037945.html)

行业智能

- [交通云控平台](https://help.aliyun.com/zh/ctcc/)
- [工业大脑](https://help.aliyun.com/zh/industrial-intelligence/)
- [自动驾驶云开发平台](https://help.aliyun.com/zh/acdp/)
- [城市视觉智能引擎](https://help.aliyun.com/zh/product/129238.html)
- [基因分析平台](https://help.aliyun.com/zh/genomics/)
- [智慧教育平台](https://help.aliyun.com/zh/product/2627602.html)
- [智能科教内容生成平台](https://help.aliyun.com/zh/product/2846391.html)

智能客服

- [云联络中心](https://help.aliyun.com/zh/ccs/)
- [智能对话机器人](https://help.aliyun.com/zh/beebot/)
- [智能外呼机器人](https://help.aliyun.com/zh/outboundbot/)
- [智能对话分析](https://help.aliyun.com/zh/sca/)
- [客服工作台](https://help.aliyun.com/zh/product/55138.html)
- [新零售智能助理（文档停止维护）](https://help.aliyun.com/zh/retailbot/)
- [智能双录质检](https://help.aliyun.com/zh/svqa/)
- [服务数字员工](https://help.aliyun.com/zh/product/3020463.html)

计算

云服务器

- [云服务器 ECS](https://help.aliyun.com/zh/ecs/)
- [GPU云服务器](https://help.aliyun.com/zh/egs/)
- [轻量应用服务器](https://help.aliyun.com/zh/simple-application-server/)
- [弹性容器实例](https://help.aliyun.com/zh/eci/)
- [专有宿主机](https://help.aliyun.com/zh/dedicated-host/)
- [云虚拟主机](https://help.aliyun.com/zh/cloud-web-hosting/)
- [计算巢服务](https://help.aliyun.com/zh/compute-nest/)
- [弹性加速计算实例（文档停止维护）](https://help.aliyun.com/zh/eais/)
- [云盒](https://help.aliyun.com/zh/cloud-box/)
- [弹性伸缩](https://help.aliyun.com/zh/auto-scaling/)

高性能计算

- [弹性高性能计算](https://help.aliyun.com/zh/e-hpc/)
- [批量计算（文档停止维护）](https://help.aliyun.com/zh/batchcompute/)

Serverless

- [函数计算](https://help.aliyun.com/zh/functioncompute/)
- [Serverless 应用引擎](https://help.aliyun.com/zh/sae/)

操作系统

- [Alibaba Cloud Linux](https://help.aliyun.com/zh/alinux/)

边缘计算

- [边缘节点服务 ENS](https://help.aliyun.com/zh/ens/)
- [边缘网络加速](https://help.aliyun.com/zh/ena/)
- [视图计算](https://help.aliyun.com/zh/vecs/)

无影

- [无影云电脑企业版](https://help.aliyun.com/zh/wuying-workspace/)
- [无影云电脑个人版](https://help.aliyun.com/zh/edsp/)
- [无影云应用](https://help.aliyun.com/zh/wuying-appstreaming/)
- [无影终端](https://help.aliyun.com/zh/wtc/)
- [无影云手机](https://help.aliyun.com/zh/ecp/)
- [无影 Agent 开发套件 AgentBay](https://help.aliyun.com/zh/agentbay/)

异构计算服务

- [真武 PPU 云服务](https://help.aliyun.com/zh/product/2864431.html)

容器

容器服务

- [容器服务 Kubernetes 版 ACK](https://help.aliyun.com/zh/ack/)
- [容器计算服务](https://help.aliyun.com/zh/cs/)
- [服务网格](https://help.aliyun.com/zh/asm/)
- [弹性容器实例](https://help.aliyun.com/zh/eci/)
- [容器镜像服务](https://help.aliyun.com/zh/acr/)

存储

基础存储服务

- [对象存储](https://help.aliyun.com/zh/oss/)
- [文件存储NAS](https://help.aliyun.com/zh/nas/)
- [文件存储 CPFS](https://help.aliyun.com/zh/cpfs/)
- [文件存储HDFS版](https://help.aliyun.com/zh/hdfs/)
- [表格存储 Tablestore](https://help.aliyun.com/zh/tablestore/)
- [数据库文件存储（文档停止维护）](https://help.aliyun.com/zh/dbfs/)
- [存储容量单位包](https://help.aliyun.com/zh/scu/)

存储数据服务

- [日志服务](https://help.aliyun.com/zh/sls/)
- [云备份](https://help.aliyun.com/zh/cloud-backup/)
- [数据灾备中心](https://help.aliyun.com/zh/bdrc/)
- [智能媒体管理](https://help.aliyun.com/zh/imm/)
- [网盘与相册服务](https://help.aliyun.com/zh/pds/)

数据迁移与工具

- [闪电立方](https://help.aliyun.com/zh/data-transport/)
- [云存储网关](https://help.aliyun.com/zh/csg/)
- [在线迁移服务](https://help.aliyun.com/zh/data-online-migration/)

混合云存储

- [混合云存储](https://help.aliyun.com/zh/hcs/)
- [混合云容灾服务](https://help.aliyun.com/zh/hdr/)

网络与CDN

云上网络

- [负载均衡](https://help.aliyun.com/zh/slb/)
- [弹性公网IP](https://help.aliyun.com/zh/eip/)
- [任播弹性公网IP](https://help.aliyun.com/zh/anycast-eip/)
- [云数据传输](https://help.aliyun.com/zh/cdt/)
- [共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/)
- [共享流量包](https://help.aliyun.com/zh/dtp/)
- [专有网络VPC](https://help.aliyun.com/zh/vpc/)
- [NAT网关](https://help.aliyun.com/zh/nat-gateway/)
- [私网连接](https://help.aliyun.com/zh/privatelink/)
- [云解析 PrivateZone](https://help.aliyun.com/zh/product/64583.html)
- [网络智能服务](https://help.aliyun.com/zh/nis/)
- [IPv6 网关](https://help.aliyun.com/zh/ipv6-gateway/)

跨地域网络

- [云企业网](https://help.aliyun.com/zh/cen/)
- [全球加速](https://help.aliyun.com/zh/ga/)

混合云网络

- [VPN网关](https://help.aliyun.com/zh/vpn/)
- [智能接入网关](https://help.aliyun.com/zh/sag/)
- [高速通道](https://help.aliyun.com/zh/express-connect/)
- [云连接器](https://help.aliyun.com/zh/cloud-connector/)
- [5G高速上云服务（文档停止维护）](https://help.aliyun.com/zh/5gcc/)

CDN

- [CDN](https://help.aliyun.com/zh/cdn/)
- [边缘安全加速](https://help.aliyun.com/zh/edge-security-acceleration/)

产品选型与组网设计

- [网络服务选型指南](https://help.aliyun.com/zh/product/2838866.html)
- [云网络规划设计](https://help.aliyun.com/zh/cloud-network-well-architected-design/)

安全

云安全

- [DDoS防护](https://help.aliyun.com/zh/anti-ddos/)
- [Web应用防火墙](https://help.aliyun.com/zh/waf/)
- [云防火墙](https://help.aliyun.com/zh/cloud-firewall/)
- [云安全中心](https://help.aliyun.com/zh/security-center/)
- [办公安全平台](https://help.aliyun.com/zh/sase/)

数据安全

- [数字证书管理服务（原SSL证书）](https://help.aliyun.com/zh/ssl-certificate/)
- [密钥管理服务](https://help.aliyun.com/zh/kms/)
- [数据安全中心](https://help.aliyun.com/zh/dsc/)
- [蚂蚁隐私计算服务平台](https://help.aliyun.com/zh/product/356643.html)
- [AI 数智鉴密](https://help.aliyun.com/zh/product/3034792.html)

身份安全

- [应用身份服务 (IDaaS)](https://help.aliyun.com/zh/idaas/)
- [访问控制](https://help.aliyun.com/zh/ram/)
- [运维安全中心（堡垒机）](https://help.aliyun.com/zh/bh/)

业务安全

- [实人认证](https://help.aliyun.com/zh/id-verification/)
- [风险识别](https://help.aliyun.com/zh/fraud-detection/)
- [AI 安全护栏](https://help.aliyun.com/zh/product/28415.html)
- [跨链数据连接服务](https://help.aliyun.com/zh/product/169830.html)
- [验证码](https://help.aliyun.com/zh/captcha/)
- [区块链服务](https://help.aliyun.com/zh/product/84950.html)
- [分布式数字身份](https://help.aliyun.com/zh/product/165833.html)

安全服务

- [安全管家](https://help.aliyun.com/zh/mss/)

中间件

微服务工具与平台

- [微服务引擎](https://help.aliyun.com/zh/mse/)
- [企业级分布式应用服务](https://help.aliyun.com/zh/edas/)
- [应用高可用服务](https://help.aliyun.com/zh/ahas/)
- [服务网格](https://help.aliyun.com/zh/asm/)
- [分布式任务调度](https://help.aliyun.com/zh/schedulerx/)
- [全局事务服务 （文档停止维护）](https://help.aliyun.com/zh/product/48444.html)
- [金融分布式架构](https://help.aliyun.com/zh/product/130189.html)
- [SOFAStack API 统一网关](https://help.aliyun.com/zh/sofa-apigateway/)

云消息队列

- [云消息队列 RocketMQ 版](https://help.aliyun.com/zh/apsaramq-for-rocketmq/)
- [云消息队列 Kafka 版](https://help.aliyun.com/zh/apsaramq-for-kafka/)
- [云消息队列 RabbitMQ 版](https://help.aliyun.com/zh/apsaramq-for-rabbitmq/)
- [云消息队列 MQTT 版](https://help.aliyun.com/zh/apsaramq-for-mqtt/)
- [轻量消息队列（原 MNS）](https://help.aliyun.com/zh/mns/)

应用集成

- [API 网关](https://help.aliyun.com/zh/api-gateway/)
- [云工作流](https://help.aliyun.com/zh/product/113549.html)
- [事件总线](https://help.aliyun.com/zh/eventbridge/)
- [多智能体治理与协作平台 AgentTeams](https://help.aliyun.com/zh/product/3034770.html)

云原生可观测

- [应用实时监控服务](https://help.aliyun.com/zh/arms/)
- [可观测监控 Prometheus 版](https://help.aliyun.com/zh/prometheus/)
- [可观测可视化 Grafana 版](https://help.aliyun.com/zh/grafana/)
- [可观测链路 OpenTelemetry 版](https://help.aliyun.com/zh/opentelemetry/)
- [性能测试](https://help.aliyun.com/zh/pts/)
- [全域智能运维平台 STAROps](https://help.aliyun.com/zh/product/3027368.html)

数据库

瑶池数据库

- [瑶池控制台](https://help.aliyun.com/zh/product/2842933.html)

关系型数据库

- [云原生数据库 PolarDB](https://help.aliyun.com/zh/polardb/)
- [云数据库 RDS](https://help.aliyun.com/zh/rds/)
- [云数据库 OceanBase 版（文档停止维护）](https://help.aliyun.com/zh/product/26458.html)

NoSQL 数据库

- [云数据库 Tair（兼容 Redis®）](https://help.aliyun.com/zh/redis/)
- [云原生多模数据库 Lindorm](https://help.aliyun.com/zh/lindorm/)
- [云数据库 MongoDB 版](https://help.aliyun.com/zh/mongodb/)
- [时间序列数据库 TSDB](https://help.aliyun.com/zh/product/54825.html)
- [图数据库](https://help.aliyun.com/zh/gdb/)
- [云数据库 Memcache 版](https://help.aliyun.com/zh/memcache/)
- [云数据库Cassandra版（文档停止维护）](https://help.aliyun.com/zh/product/126560.html)
- [云数据库HBase版](https://help.aliyun.com/zh/hbase/)

数据库平台与服务

- [云数据库专属集群](https://help.aliyun.com/zh/product/156215.html)

数据仓库

- [云原生数据仓库AnalyticDB](https://help.aliyun.com/zh/analyticdb/)
- [云数据库 ClickHouse](https://help.aliyun.com/zh/clickhouse/)
- [云数据库 SelectDB 版](https://help.aliyun.com/zh/selectdb/)

数据库管理工具

- [数据管理 DMS](https://help.aliyun.com/zh/dms/)
- [数据传输服务](https://help.aliyun.com/zh/dts/)
- [数据库自治服务](https://help.aliyun.com/zh/das/)
- [数据库和应用迁移](https://help.aliyun.com/zh/product/53556.html)
- [数据库网关 （文档停止维护）](https://help.aliyun.com/zh/product/117995.html)

从这里开始

[新手指南](https://help.aliyun.com/zh/product/47310.html)

[云采用框架](https://help.aliyun.com/zh/caf/)

[卓越架构](https://help.aliyun.com/zh/product/2362200.html)

[阿里云安全指南](https://help.aliyun.com/zh/acsg/)

大数据计算

数据计算与分析

- [云原生大数据计算服务 MaxCompute](https://help.aliyun.com/zh/maxcompute/)
- [实时数仓 Hologres](https://help.aliyun.com/zh/hologres/)
- [实时计算 Flink版](https://help.aliyun.com/zh/flink/)
- [检索分析服务 Elasticsearch版](https://help.aliyun.com/zh/es/)
- [向量检索服务 Milvus 版](https://help.aliyun.com/zh/milvus/)
- [图计算服务 GraphCompute](https://help.aliyun.com/zh/graph-compute/)
- [Cloudera CDP 企业数据云平台](https://help.aliyun.com/zh/cdp/)

数据湖

- [开源大数据平台 E-MapReduce](https://help.aliyun.com/zh/emr/)
- [数据湖构建](https://help.aliyun.com/zh/dlf/)

数据应用与可视化

- [DataV数据可视化](https://help.aliyun.com/zh/datav/)
- [智能商业分析 Quick BI](https://help.aliyun.com/zh/quick-bi/)
- [智能用户增长](https://help.aliyun.com/zh/product/132007.html)
- [全域采集与增长分析](https://help.aliyun.com/zh/product/194063.html)

数据开发与服务

- [大数据开发治理平台 DataWorks](https://help.aliyun.com/zh/dataworks/)
- [数据总线 DataHub](https://help.aliyun.com/zh/datahub/)
- [大数据专家服务](https://help.aliyun.com/zh/bigdata-expert-service/)
- [数据资源平台（文档停止维护）](https://help.aliyun.com/zh/drp/)
- [智能数据建设与治理 Dataphin](https://help.aliyun.com/zh/dataphin/)

媒体服务

视频服务

- [视频直播](https://help.aliyun.com/zh/live/)
- [视频点播](https://help.aliyun.com/zh/vod/)
- [音视频通信](https://help.aliyun.com/zh/product/61399.html)

媒体处理与内容生产

- [智能媒体服务](https://help.aliyun.com/zh/ims/)
- [媒体处理](https://help.aliyun.com/zh/mps/)

媒体开发服务

- [音视频终端 SDK](https://help.aliyun.com/zh/apsara-video-sdk/)

企业服务与云通信

企业云服务

- [云采销（文档停止维护）](https://help.aliyun.com/zh/csp/)
- [能耗宝](https://help.aliyun.com/zh/energy-expert/)
- [场景金融链接器](https://help.aliyun.com/zh/sfc/)
- [云行情](https://help.aliyun.com/zh/cloudquotation/)
- [营销引擎](https://help.aliyun.com/zh/me/)
- [企业商城 LinkedMall](https://help.aliyun.com/zh/linkedmall/)
- [移动研发平台](https://help.aliyun.com/zh/product/434086.html)
- [多端低代码开发平台魔笔](https://help.aliyun.com/zh/mobi/)
- [云原生应用组装平台 BizWorks](https://help.aliyun.com/zh/bizworks/)
- [机器人流程自动化](https://help.aliyun.com/zh/rpa/)
- [云渲染（文档停止维护）](https://help.aliyun.com/zh/gcs/)
- [Salesforce on Alibaba Cloud](https://help.aliyun.com/zh/sfoa/)
- [信息查询服务](https://help.aliyun.com/zh/product/2837261.html)
- [云游戏平台（文档停止维护）](https://help.aliyun.com/zh/product/171674.html)

企业基础服务

- [云市场](https://help.aliyun.com/zh/marketplace/)

企业办公协同

- [专有钉钉（文档停止维护）](https://help.aliyun.com/zh/product/150643.html)
- [钉钉会议](https://help.aliyun.com/zh/product/139635.html)
- [阿里邮箱](https://help.aliyun.com/zh/product/35466.html)
- [邮件推送](https://help.aliyun.com/zh/direct-mail/)
- [智能邮件营销服务](https://help.aliyun.com/zh/sendify/)
- [宜搭](https://help.aliyun.com/zh/product/429784.html)

云通信

- [短信服务](https://help.aliyun.com/zh/sms/)
- [语音服务](https://help.aliyun.com/zh/vms/)
- [号码隐私保护](https://help.aliyun.com/zh/pnp/)
- [号码认证服务](https://help.aliyun.com/zh/pnvs/)
- [号码百科](https://help.aliyun.com/zh/cpns/)
- [智能联络中心](https://help.aliyun.com/zh/aiccs/)
- [Chat App 消息服务](https://help.aliyun.com/zh/chatapp/)

域名与网站

域名与备案服务

- [域名](https://help.aliyun.com/zh/dws/)
- [备案](https://help.aliyun.com/zh/icp-filing/)
- [云解析DNS](https://help.aliyun.com/zh/dns/)
- [AI 建站万小智](https://help.aliyun.com/zh/product/3039206.html)

知识产权服务

- [商标服务](https://help.aliyun.com/zh/trademark/)
- [知识产权服务](https://help.aliyun.com/zh/copyright-and-patent-service/)

终端用户计算

无影

- [无影云电脑企业版](https://help.aliyun.com/zh/wuying-workspace/)
- [无影云电脑个人版](https://help.aliyun.com/zh/edsp/)
- [无影云应用](https://help.aliyun.com/zh/wuying-appstreaming/)
- [无影终端](https://help.aliyun.com/zh/wtc/)
- [无影云手机](https://help.aliyun.com/zh/ecp/)
- [无影 Agent 开发套件 AgentBay](https://help.aliyun.com/zh/agentbay/)

JVS智能体套件

- [JVS 智能体套件](https://help.aliyun.com/zh/jvs/)

物联网

物联网云服务

- [物联网无线连接服务](https://help.aliyun.com/zh/iotmcp/)
- [物联网平台（文档停止维护）](https://help.aliyun.com/zh/iot/)
- [物联网智能视频服务（文档停止维护）](https://help.aliyun.com/zh/linkvisual/)
- [IoT设备身份认证（文档停止维护）](https://help.aliyun.com/zh/iot-device-id/)
- [IoT安全运营中心（文档停止维护）](https://help.aliyun.com/zh/soc/)
- [物联网络管理平台](https://help.aliyun.com/zh/link-wan/)
- [物联网应用开发](https://help.aliyun.com/zh/iot-studio/)

设备端服务

- [物联网边缘计算（文档停止维护）](https://help.aliyun.com/zh/iot-edge/)

行业物联网

- [云投屏（文档停止维护）](https://help.aliyun.com/zh/cloud-display/)
- [生活物联网平台（飞燕平台）](https://help.aliyun.com/zh/product/123207.html)
- [云价签 （文档停止维护）](https://help.aliyun.com/zh/cloudesl/)
- [工业互联网平台（文档停止维护）](https://help.aliyun.com/zh/iiot/)

开发工具

API 与工具

- [云命令行](https://help.aliyun.com/zh/cloud-shell/)
- [OpenAPI Explorer](https://help.aliyun.com/zh/openapi/)
- [阿里云SDK](https://help.aliyun.com/zh/sdk/)
- [阿里云CLI](https://help.aliyun.com/zh/cli/)
- [资源编排](https://help.aliyun.com/zh/ros/)
- [云控制API](https://help.aliyun.com/zh/cloud-control-api/)
- [Node.js 性能平台](https://help.aliyun.com/zh/nodejs/)
- [Terraform](https://help.aliyun.com/zh/terraform/)
- [Pulumi](https://help.aliyun.com/zh/pulumi/)
- [Ansible](https://help.aliyun.com/zh/ansible/)
- [云插件](https://help.aliyun.com/zh/product/29966.html)
- [云 Skills 门户](https://help.aliyun.com/zh/skillsportal/)

云效DevOps

- [云效](https://help.aliyun.com/zh/yunxiao/)
- [Qoder CN 系列](https://help.aliyun.com/zh/lingma/)

开发与运维

- [移动研发平台](https://help.aliyun.com/zh/product/434086.html)
- [多端低代码开发平台魔笔](https://help.aliyun.com/zh/mobi/)
- [云原生应用组装平台 BizWorks](https://help.aliyun.com/zh/bizworks/)
- [API 网关](https://help.aliyun.com/zh/api-gateway/)
- [移动开发平台 mPaaS](https://help.aliyun.com/zh/product/49548.html)

Serverless

计算

- [函数计算](https://help.aliyun.com/zh/functioncompute/)
- [Serverless 应用引擎](https://help.aliyun.com/zh/sae/)

应用集成

- [云原生应用开发平台](https://help.aliyun.com/zh/cap/)
- [云工作流](https://help.aliyun.com/zh/product/113549.html)
- [事件总线](https://help.aliyun.com/zh/eventbridge/)
- [轻量消息队列（原 MNS）](https://help.aliyun.com/zh/mns/)

专有云

[飞天企业版](https://help.aliyun.com/apsara/enterprise.html)

迁移与运维管理

运维与监控

- [日志服务](https://help.aliyun.com/zh/sls/)
- [应用实时监控服务](https://help.aliyun.com/zh/arms/)
- [可观测监控 Prometheus 版](https://help.aliyun.com/zh/prometheus/)
- [可观测可视化 Grafana 版](https://help.aliyun.com/zh/grafana/)
- [可观测链路 OpenTelemetry 版](https://help.aliyun.com/zh/opentelemetry/)
- [系统运维管理](https://help.aliyun.com/zh/oos/)
- [云监控](https://help.aliyun.com/zh/cms/)
- [云网管](https://help.aliyun.com/zh/cmn/)
- [运维事件中心](https://help.aliyun.com/zh/oic/)
- [智能顾问](https://help.aliyun.com/zh/product/65862.html)
- [应用诊断分析平台](https://help.aliyun.com/zh/atp/)

云管理

- [云治理中心](https://help.aliyun.com/zh/cgc/)
- [操作审计](https://help.aliyun.com/zh/actiontrail/)
- [配置审计](https://help.aliyun.com/zh/product/127306.html)
- [访问控制](https://help.aliyun.com/zh/ram/)
- [智能体身份 Agent Identity](https://help.aliyun.com/zh/agentidentity/)
- [资源管理](https://help.aliyun.com/zh/resource-management/)
- [配额中心](https://help.aliyun.com/zh/quota-center/)
- [云速搭](https://help.aliyun.com/zh/cadt/)
- [服务目录](https://help.aliyun.com/zh/service-catalog/)
- [云SSO](https://help.aliyun.com/zh/cloudsso/)

备份与迁移

- [云备份](https://help.aliyun.com/zh/cloud-backup/)
- [数据管理 DMS](https://help.aliyun.com/zh/dms/)
- [数据传输服务](https://help.aliyun.com/zh/dts/)
- [搬站上云](https://help.aliyun.com/zh/cmh/)
- [服务器迁移中心](https://help.aliyun.com/zh/smc/)

解决方案

[专属钉钉](https://help.aliyun.com/zh/product/157323.html)

[阿里云电子政务云](https://help.aliyun.com/zh/govcloud/)

[MindSphere on Alibaba Cloud](https://help.aliyun.com/zh/mdsp/)

[SAP 解决方案](https://help.aliyun.com/zh/sap-solution/)

[无影标品解决方案](https://help.aliyun.com/zh/product/2536540.html)

[金融云](https://help.aliyun.com/zh/product/29849.html)

[阿里云集成转售解决方案](https://help.aliyun.com/zh/product/90850.html)

[数据湖 OpenLake](https://help.aliyun.com/zh/openlake/)

支持与服务

[管理控制台](https://help.aliyun.com/zh/management-console/)

[账号中心](https://help.aliyun.com/zh/account/)

[工单系统API](https://help.aliyun.com/zh/product/163246.html)

[支持与服务](https://help.aliyun.com/zh/product/44216.html)

[法律声明](https://help.aliyun.com/zh/product/67275.html)

[阿里云健康看板](https://help.aliyun.com/zh/product/2636617.html)

[费用与成本](https://help.aliyun.com/zh/user-center/)

更多

[阿里云App](https://help.aliyun.com/zh/product/48842.html)

[云大使推荐返现](https://help.aliyun.com/zh/product/122614.html)

[阿里云认证](https://help.aliyun.com/zh/product/32348.html)

[Data Exchange](https://help.aliyun.com/zh/product/2655805.html)

提示（Prompt）是您输入给大模型（LLM）的文本信息，用于明确地告诉模型您想要解决的问题或完成的任务，也是大语言模型理解用户需求并生成相关、准确回答或内容的基础。 为了帮助您更高效地使用 LLM ，本教程为您提供一系列实用的技巧，帮助您设计和优化 Prompt。

## 设计 **Prompt**

### **构建清晰明确的 Prompt**

想象一下，如果您在给一个同事指派工作任务时，只给了一句话来描述需求，他的任务完成效果可能很难达到您的预期。但如果您提供了明确的目的、建议的思考方向和执行策略等更多参考信息，他更有可能以高标准完成任务。

使用 LLM 也一样，您的任务描述（Prompt）越清晰、具体、没有歧义，LLM 的表现越能符合您的期望。

**说明**

构建一个清晰具体的 Prompt 是充分发挥大模型能力的最重要一步。

| **模糊的 Prompt** | **清晰具体的 Prompt** |
| --- | --- |

|     |     |
| --- | --- |
| **模糊的 Prompt** | **清晰具体的 Prompt** |
| 我想推广公司的新产品。我的公司名为阿里云百炼，新产品名为 Zephyr Z9，是一款轻薄便携的手机。帮我创建一条微博帖子。 | 请为我司“阿里云百炼”最新推出的“Zephyr Z9”轻薄便携手机设计一条吸引眼球的微博推广帖。<br>内容需彰显Zephyr Z9的独特卖点，如极致轻薄设计、高性能配置及用户便利性，同时融入创意元素以提升观众兴趣和互动意愿。<br>记得提及阿里云百炼品牌声誉，激发受众好奇心，引导他们探索更多产品信息或直接进行购买。<br>贴文应简洁有力，符合微博平台的风格与字数限制，适宜社交媒体传播。 |
| 你是一位资深PHP编程专家，现在接到一个明确的开发任务。诉求是：${require}。请使用PHP语言详细描述一种实现该诉求的算法或方法，并考虑在实现过程中可能遇到的边界情况和错误处理，以及如何通过高效且安全的代码来满足此需求。 | 作为一位经验丰富的PHP编程专家，您面临的具体开发任务为：${require}。<br>请运用您的专业知识，详细阐述一种利用PHP实现该任务需求的高效算法或方法论。<br>在您的描述中，请务必涵盖以下几点：<br>\- 具体实现步骤，包括必要的函数、类及数据结构的选择与设计。<br>\- 边界条件分析，识别并解释潜在的边缘案例及如何妥善处理这些情况。<br>\- 错误处理机制，描述如何在代码中实施健壮的错误检测与异常处理逻辑，以确保程序稳定性。<br>\- 安全性考量，讨论可能的安全威胁及推荐的防范措施，确保代码执行过程中的数据安全与隐私保护。<br>\- 性能优化建议，提出提高代码执行效率的方法，包括但不限于算法优化、资源管理和缓存策略。<br>请确保您的解答不仅技术准确，而且条理清晰、易于理解，以便其他开发者能够快速掌握并应用于实际项目中。 |

阿里云百炼提供了Prompt一键优化工具，您可以在 **[Prompt](https://bailian.console.aliyun.com/?tab=app#/component-manage/prompt)** 页面点击 **自动优化** 尝试该工具。该工具能针对输入的提示（Prompt）进行 **自动扩写和细节添加**，推荐您先将 Prompt经过优化工具扩写改进，再接着阅读和体验其他优化技巧。

> Prompt优化功能通过调用大模型实现，需要消耗一定量的Token，按照模型推理费用计费。

### **使用 Prompt 框架**

为了系统化地向 LLM 提供明确背景和目的，这里推荐您使用 **Prompt 框架** 规范化您的 Prompt。该框架用于帮助您方便、快速地设计 Prompt 结构。该模板充分考虑了会影响 LLM 输出有效性和相关性的各个方面，能显著提升模型表现。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5435758771/CAEQTxiBgMCWop6QjxkiIGI2YWU1YzhjYzRiMjQ3NDU5NGY1YTQ2OWUyNDQzMmE54577910_20240815141024.521.svg)

其内容组成为：（当您不确定如何编写框架各元素的具体内容，不妨将一些关键词交给阿里云百炼 Prompt 优化工具进行扩写。）

- **背景：** 介绍与任务紧密相关的背景信息。这一环节有助于LLM深入理解讨论的具体环境，从而保证其生成内容与话题高度相关。

- **目的：** 明确指出您期望LLM完成的具体任务。通过设定清晰、精确的目标指令，可引导LLM聚焦于实现既定任务，提升输出的有效性。

- **风格：** 指定您希望 LLM 输出的写作风格，可以是某个具体名人、具体流派或者某类专家的写作风格。

- **语气：** 定义输出内容应有的语气，比如正式、诙谐、温馨、关怀等，以便适应不同的使用场景和使用目的。

- **受众：** 明确指出内容面向的读者群体，无论是专业人士、入门学习者还是儿童等，这样LLM就能调整语言和内容深度，使之更加贴合受众需求。

- **输出：** 规定输出内容的具体形式，确保LLM提供的成果能直接满足后续应用的需求，比如列表、JSON数据格式、专业分析报告等形式。

|  | **未使用 Prompt 框架** | **使用 Prompt 框架** |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |
|  | **未使用 Prompt 框架** | **使用 Prompt 框架** |
| Prompt | 我想推广公司的新产品。我的公司名为阿里云百炼，新产品名为 Zephyr Z9，是一款轻薄便携的手机。帮我创建一条微博帖子，简洁而深具影响力。 | #背景#<br>我想为公司的新产品做广告。我公司的名字叫阿里云百炼，产品叫阿里云百炼 Zephyr Z9，是一款轻薄便携的手机。<br>#目的#<br>为我创建一个微博帖子（限制：500字），旨在让人们有兴趣点击产品链接购买。<br>#风格#<br>遵循黑米等成功公司为类似产品做广告的写作风格。<br>#语气#<br>有说服力<br>#受众#<br>我公司在微博上的受众通常是年轻一辈人。定制你的帖子，保证喜欢数码产品的人能快速关注到你的帖子。<br>#输出#<br>微博上的帖子，简洁而有影响力。 |
| 输出 | 【轻启未来，风起云涌】<br>![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850289.png)阿里云百炼新品，Zephyr Z9震撼上市！![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850290.png)<br>![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850311.png)携手Zephyr Z9，让科技与轻盈同行。这不仅是一部手机，它是你探索世界的轻便伴侣。厚度挑战极限，设计引领风尚，Z9在手中，灵感随时迸发。<br>![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850323.png)超越想象的性能，搭载极速处理器，流畅如风，无论是工作狂飙还是游戏征途，Zephyr Z9都是你的首选座驾。续航强劲，让每一份热情持续燃烧！<br>![image](<Base64-Image-Removed>)捕捉生活每一刻，Z9相机创新升级，夜景、人像、广角，每一拍都是封面大片，让美好记忆永不褪色。<br>Trees 轻薄，重在体验。#百炼ZephyrZ9# ，为不凡而生，为你而来。立即拥抱未来，开启属于你的轻盈科技时代！<br>官方网站：\[www.bailian.com/Z9\] (请替换为实际网址）<br>#轻薄旗舰 #科技新风尚 #掌中艺术品 | ![image](<Base64-Image-Removed>)【独家揭秘】阿里云百炼Zephyr Z9，轻薄界的颠覆者来了！<br>在这个快节奏的时代，每克重量都是对自由的负担。百炼深谙此道，匠心打造了Zephyr Z9——一款专为追求极致轻盈与强大性能平衡的你而生的手机！悬浮般的手感，一触难忘！![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>)【超薄设计，尽在掌握】<br>Zephyr Z9以其令人惊叹的纤薄机身，重新定义了“轻薄”。仅X.Xmm的厚度，轻松滑入口袋，是你日常出行的完美伴侣。携带它，就像带着未来穿梭于都市丛林！![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>)【顶尖配置，性能怪兽】<br>别看它轻，内核全是硬实力！搭载最新的XXXX处理器，流畅度爆表，无论是多任务处理还是大型游戏，Z9都能游刃有余，让你时刻处于科技最前沿。![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>)【摄影大师，记录生活】<br>配备XXMP超感光镜头，夜晚也清晰。AI智能场景识别，让每一张照片都堪比大片。用Zephyr Z9，记录每一个不凡瞬间，让你的朋友圈从此与众不同。![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>)【续航无忧，能量满满】<br>小身材，大能量！Zephyr Z9内置高效能电池，搭配XXX快充技术，片刻充电，长久陪伴。告别电量焦虑，你的创意和灵感不再受限。⚡<br>![image](<Base64-Image-Removed>)【限时福利，不容错过】<br>前100名通过链接购机的用户，将享受神秘大礼包！包含定制保护壳、XXX会员年卡等多重好礼，只为尊贵的你！![image](<Base64-Image-Removed>)<br>立刻行动，让百炼Zephyr Z9成为你探索世界的全新伙伴！点击下方链接，开启轻盈新纪元！![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>)\[立即抢购百炼Zephyr Z9\] \[产品链接\]<br>#百炼ZephyrZ9 #轻薄旗舰 #科技美学 #数码潮流 #性能怪兽 |

在未使用 Prompt 框架时，LLM 输出虽表现尚可，但显得过于泛化，缺乏必要的细节和针对特定群体的吸引力。而在使用 Prompt 框架时，框架不仅提醒您考虑需求的其它方面，特别是一般 Prompt 中缺少的风格、语气和受众，还帮助 LLM 生成更针对年轻群体、细节更多、语言表达更加富有张力的输出。

**说明**

Prompt 框架在实践中有非常多的种类，您可以根据您的任务需求增减其结构组成。当然您也可以在后续章节观察到本教程对该 Prompt 框架的灵活运用。

## 优化 **Prompt**

### **技巧一：为模型提供输出样例**

在 Prompt 中提供您期望的输出示例，可以让 LLM “模仿”我们所要求的规范、格式、概念、文法、语气进行输出。同时，提供样例可以让大模型多次输出的结果更一致，从而稳定模型表现。

|  | **未添加样例** | **添加样例** |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |
|  | **未添加样例** | **添加样例** |
| Prompt | #背景#<br>你很擅长编写小红书种草笔记，喜欢增加丰富的emoji元素。<br>#目的#<br>请生成一篇小红书种草笔记，推广强森吹风机。吹风机的优点是：体积小、高颜值、风力大、干的快、智能控温不伤发。<br>#受众#<br>喜欢追求时尚的年轻人，尤其是年轻女性<br>#输出#<br>小红书文章格式，充满emoji元素，简洁但内容充实 | #背景#<br>你很擅长编写小红书种草笔记，喜欢增加丰富的emoji元素。<br>#目的#<br>请生成一篇小红书种草笔记，推广强森吹风机。吹风机的优点是：体积小、高颜值、风力大、干得快、智能控温不伤发。<br>#受众#<br>喜欢追求时尚的年轻人，尤其是年轻女性<br>#输出#<br>小红书文章格式，充满emoji元素，简洁但内容充实<br>#语气与风格#<br>1. 我亲测过+n种好物+谁适合谁受益 这个秘诀让你的话语超有信服力！ 比如：亲自尝试了很多美白神器，终于挖到宝！仅俩月，肌肤变得嫩滑透亮，自我感觉飘飘欲仙~ 此法特为想大晒体验的小伙伴们量身定制，还能精准安利，助人避坑！<br>   <br>2. 难题出没+揭秘原因+终极解药 这公式助你条理清晰地分享，内容价值爆棚！ 案例：渴望秀发如丝？揭秘时刻来啦！原来我一直遗漏关键一步，直到遇见它！换用这款洗发水，秀发显著改善，光泽get！ 此法逻辑严密，不仅分享秘籍，还引导读者找到问题破解之道。<br>   <br>3. 独到见解+深度剖析+巧妙推荐 这公式帮你自然流露心声，还能温馨种草！ 示例：我觉得每个女孩都该有份挚爱，生活因此而精彩。手帐成了我的小确幸，每当提笔，幸福指数飙升！ 它助你畅所欲言，同时不经意间传递心头好，双赢策略！<br>   <br>4. 亲身经历+成果展示 这公式让你的情感表达鲜活又感人！ 场景：回想起夏夜海边的蚊灾，满身红包的绝望，直到遇见救星！现在，光滑肌肤让我裙摆飞扬，自信回归！ 它让你的故事活灵活现，分享喜悦与感恩之情，触动人心！ |
| 输出 | 标题：![image](<Base64-Image-Removed>)强森小巧魔力风机，速干护发新宠儿![image](<Base64-Image-Removed>)<br>正文：<br>Hey宝贝们！今天要给你们种草一颗美发界的璀璨新星![image](<Base64-Image-Removed>) —— 强森吹风机！它不仅仅是个工具，简直是随身携带的美发沙龙![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>)体积小巧，旅行必备 ![image](<Base64-Image-Removed>)<br>首先，它的迷你身材直接击中我心！旅行包包再满也能轻松塞进，不占空间，随时随地凹造型![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>) 高颜值，时尚出街 ![image](<Base64-Image-Removed>)<br>看这设计，简直就是艺术品呀！无论是极简白还是高级粉，拿在手里就是街头最靓的崽！手机？不，这是我的新时尚配饰![image](<Base64-Image-Removed>)![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>)风力强劲，速干神器 ![image](<Base64-Image-Removed>)<br>别看它小，风力可一点都不含糊！早上赶时间？强森帮你5分钟搞定出门发型，效率MAX！![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>)干得快，还护发 ![image](<Base64-Image-Removed>)<br>智能控温技术，温柔呵护你的每一根秀发。告别热损伤，只留下柔顺光泽，每次吹发都像做了次沙龙护理～![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>)智能控温，细心之选 ![image](<Base64-Image-Removed>)<br>懂你的不只是风力，还有温度。根据发质自动调节最适宜的热量，守护秀发健康，长期使用也不怕伤发![image](<Base64-Image-Removed>)<br>总之，强森吹风机就是那个能让你爱不释手的小可爱！赶紧加入购物车，给你的美丽加速吧！![image](<Base64-Image-Removed>)<br>#强森吹风机 #美发达人 #快速护发秘籍<br>标记你的朋友，让她们也来感受这份轻巧与高效吧！![image](<Base64-Image-Removed>)<br>记得，爱护自己从“头”开始，强森与你一起，绽放自信光彩！![image](<Base64-Image-Removed>) | ![image](<Base64-Image-Removed>)吹风机也能成为美发时尚单品？强森小钢炮告诉你答案！![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>)自从我用了![image](<Base64-Image-Removed>)强森吹风机![image](<Base64-Image-Removed>)，不仅旅行包轻便多了![image](<Base64-Image-Removed>)，每次吹发都变成享受时光![image](<Base64-Image-Removed>)！用了几次后，朋友们都夸我发质看起来好了不止一个度，就像刚从沙龙出来的样子![image](<Base64-Image-Removed>)。它绝对是短途出游或宿舍生活的完美伴侣哦！适合所有追求高效护发的宝贝们～![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>)面对湿漉漉的长发瀑布，每次都得耗时半小时以上？![image](<Base64-Image-Removed>)别怕，强森智能控温科技来了![image](<Base64-Image-Removed>)！它能迅速吹干每一根发丝，而且风力强劲却不伤发，秘密就在于它能智能调节温度，保护你的秀发不受热损伤![image](<Base64-Image-Removed>)。从此，快速出门不再是梦！<br>![image](<Base64-Image-Removed>)我一直认为，好的造型工具是美丽态度的体现![image](<Base64-Image-Removed>)。强森这枚高颜值吹风机不单是个工具，更是梳妆台上的一件艺术品![image](<Base64-Image-Removed>)。每次用它吹发，都像是在进行一场个人风格的仪式感升级。不妨也给自己来点这样的小奢侈，毕竟，美好的一天从头开始嘛！![image](<Base64-Image-Removed>)<br>![image](<Base64-Image-Removed>)记得那次临时接到晚宴邀请![image](<Base64-Image-Removed>)，急匆匆从健身房出来，头发还滴着汗。正当焦虑之际，幸好有强森吹风机紧急救援！我迅速将湿润的乱发吹整得服服帖帖，走进宴会厅的那一刻，自信满满![image](<Base64-Image-Removed>)，好像刚做完高级沙龙护理似的。多亏了这小巧却强大的美发神器，我的美丽不再受限于时间！![image](<Base64-Image-Removed>)<br>快来把这吹风机界的时尚小钢炮加入购物车吧！![image](<Base64-Image-Removed>)让我们一起做个风一样的女子，优雅又效率，从头开始闪耀每一天！![image](<Base64-Image-Removed>)<br>#强森吹风机 #高颜值美发神器 #智能护发新体验 #速干不伤发 #时尚必备 |

观察输出时，您可以发现，LLM 学习了样例的要求并针对性地生成了符合格式要求的种草文。

### 技巧二：设定完成任务的步骤

对于许多复杂任务，提醒 LLM 如何完成任务是非常必要的。

#### **提供任务步骤来完成数学题**

数学题：

又到了周日，小明像以往一样去爷爷奶奶家玩，小明于早上八点整步行出发，已知小明每分钟行走50米，走了12分钟后，小明的父亲发现小明忘记带作业了，于是便骑车去追小明，已知小明的爸爸每分钟骑行200米，等到追上小明后，爸爸决定骑车带上小明，已知小明坐自行车的路程是走路路程的5倍，请问，小明和他爸爸几点到爷爷家的呢？（小明8点36分到爷爷家）

Prompt（通过添加`#任务步骤#`告诉 LLM 如何完成任务）：

```plaintext
#背景#
又到了周日，小明像以往一样去爷爷奶奶家玩，小明于早上八点整步行出发，已知小明每分钟行走50米，
走了12分钟后，小明的父亲发现小明忘记带作业了，于是便骑车去追小明，已知小明的爸爸每分钟骑行200米，
等到追上小明后，爸爸决定骑车带上小明，已知小明坐自行车的路程是走路路程的5倍，
#目的#
小明什么时候到爷爷家？
#任务步骤#
1. 先计算小明被爸爸追上时的时间和移动的距离。
2. 再计算小明去爷爷家剩余的距离和需要的时间。
3. 最后计算小明到爷爷家的时间。
```

**Output（LLM 清晰地从提示词中获取到了任务步骤，并基于规定的步骤生成了正确结果）：**

```plaintext
要解答这个问题，我们首先需要根据给定的信息分步骤来解决。

步骤1: 计算小明被爸爸追上时的时间和移动的距离
小明每分钟行走50米。
爸爸出发时（即小明走了12分钟后），小明已经走了 12×50=600 米。
从这一刻起，小明继续以每分钟50米的速度前进，而爸爸则以每分钟200米的速度追赶。
设从小明父亲开始追赶直到追上小明所需时间为 t分钟，则有方程：[200t = 50t + 600] （左边是爸爸的总行程，右边是小明在相同时间内走过的距离加上初始的600米领先）
解这个方程得：[150t = 600] [t = 4] 分钟。这意味着爸爸用了4分钟就追上了小明。
在这4分钟里，小明又走了 4×50=200 米。
因此，当爸爸追上小明时，小明总共走了 600+200=800 米。
步骤2: 计算小明去爷爷家剩余的距离和需要的时间
根据题意，“小明坐自行车的路程是走路路程的5倍”，这里可以理解为从爸爸追上小明的地方到爷爷家的路程是之前步行路程(800米)的5倍，即 800×5=4000 米。
由于之后是骑车前往，速度为每分钟200米，因此到达爷爷家还需要时间 4000/200=20 分钟。
步骤3: 最后计算小明到爷爷家的时间
小明于早上八点整出发。
到爸爸追上他时，共过去了 12+4=16 分钟。
再加上骑车前往爷爷家所需的20分钟，总共耗时 16+20=36 分钟。
因此，小明将在出发后的第36分钟到达爷爷家，即早上 8:00+36 分钟 = 8:36 到达爷爷家。
```

### 技巧三： **使用分隔符号区分单元**

在构建复杂的 Prompt 时，采用特定的分隔符来界定不同内容单元是极为关键的，这一做法显著增强了 LLM 对 Prompt 正确解析的能力。随着任务复杂度的增加，合理利用分隔符越能提升 LLM 的表现。

分隔符的选择应着眼于那些在自然语言文本中罕见的、独特的字符组合，例如：`###`、`===`、`>>>`等。这些特殊符号序列并无固定规则，关键在于其辨识度高，确保模型能够明确区分这些符号是作为内容区域的界限标识，而非文本中的普通标点或语法组成部分。

|  | **未使用分隔符** | **使用分隔符** |
| --- | --- | --- |

|     |     |     |
| --- | --- | --- |
|  | **未使用分隔符** | **使用分隔符** |
| Prompt | 请简短总结以下影评。<br>曾经意气风发的张志强在生活的重压下，中年“失速”偏离了原本的生活轨迹，一时意气用事的决定，让他瞬间从家人的“小骄傲”变成了社会的“边角料”。然而，他未曾料到，这仅是他中年人生道路上的起点。接连不断的变故如疾风骤雨般袭来，迫使他不得不重新面对自我。当生活的重担真正压肩，他选择成为一名快递员，从新的起点重新出发，穿梭于都市大街小巷的高志垒在路上结识了一众志同道合的伙伴。在共度的时光里他深切的体会到了人间的冷暖真情，逐渐在这条充满磨砺的“逆行道”中找回曾经丢失的勇气与信念，重新定义人生新的方向。 | 请简短总结以下影评。<br>###<br>曾经意气风发的张志强在生活的重压下，中年“失速”偏离了原本的生活轨迹，一时意气用事的决定，让他瞬间从家人的“小骄傲”变成了社会的“边角料”。<br>###<br>然而，他未曾料到，这仅是他中年人生道路上的起点。接连不断的变故如疾风骤雨般袭来，迫使他不得不重新面对自我。<br>当生活的重担真正压肩，他选择成为一名快递员，从新的起点重新出发，穿梭于都市大街小巷的高志垒在路上结识了一众志同道合的伙伴。<br>###<br>在共度的时光里他深切的体会到了人间的冷暖真情，逐渐在这条充满磨砺的“逆行道”中找回曾经丢失的勇气与信念，重新定义人生新的方向。<br>### |
| 输出 | 电影讲述了一个中年危机故事，主角张志强因生活压力偏离正常生活轨道，经历一系列挑战后，他成为一名快递员，在新朋友的帮助下重拾勇气与信念，找到了生活的新方向。影片展现了逆境中的成长与自我救赎。 | 主人公张志强中年遭遇生活困境，一次冲动的决定使他社会地位骤降。<br>随后，面对重重挑战，他担任快递员重新起步，在此过程中与同行建立深厚情谊，并在磨难中找回勇气和信念。<br>最终，在艰难和挑战中，为自己的人生找到了新的意义和方向。 |

您可以在输出中发现明显差别，在使用了分隔符的输出中， **LLM 不仅理解了三段话的逻辑关系，还正确识别了分隔符，并根据分隔符的段落生成了三段强相关的总结。**

### 技巧四： **引导模型“思考”**

对于逻辑推理和语境学习的复杂任务来说，简单的 Prompt 技巧可能无法满足任务需求。但您可以通过 **引导模型生成推理过程** 或 **帮助模型拆解复杂任务并逐步推理** 的方式，让模型在生成推理结果前生成更多的推理依据，从而提升模型在复杂问题上的表现。

这里为您先介绍 **思维链（Chain of Thought，COT）**，它是一种使用起来较为简单的引导方法，但能够显著提高大模型在复杂场景下的推理能力。

任务目的： **解析一个复杂的 JSON 结构体**

```json
#背景#
JSON 输入：
{"web-app": {
  "servlet": [\
    {\
      "servlet-name": "cofaxEmail",\
      "servlet-class": "org.cofax.cds.EmailServlet",\
      "init-param": {\
      "mailHost": "mail1",\
      "mailHostOverride": "mail2"}},\
    {\
      "servlet-name": "cofaxTools",\
      "servlet-class": "org.cofax.cms.CofaxToolsServlet",\
      "init-param": {\
        "templatePath": "toolstemplates/",\
        "log": 1,\
        "logLocation": "/usr/local/tomcat/logs/CofaxTools.log",\
        "logMaxSize": ""}}],
  "servlet-mapping": {
    "cofaxEmail": "/cofaxutil/aemail/*",
    "cofaxTools": "/tools/*"},

  "taglib": {
    "taglib-uri": "cofax.tld",
    "taglib-location": "/WEB-INF/tlds/cofax.tld"}}}

#目的#
根据 JSON 判断是否完全符合以下要求：
1. 是否每个 servlet 都有 init-param
2. 是不是 servlet-mapping 中元素都在 servlet 中都有匹配
3. servlet 的 cofaxTools 中有三个以“log” 开头的参数，且 “log” 参数小于 10
```

| **不使用思维链** | **使用思维链** |
| --- | --- |

|     |     |
| --- | --- |
| **不使用思维链** | **使用思维链** |
| ```plaintext<br>#输出#<br>如果全部符合要求，只输出 "符合要求"，否则只输出 "不符合要求"。<br>``` | ```plaintext<br>#输出#<br>先输出针对各要求的思考判断过程。<br>如果全部符合要求，再输出 "符合要求"，否则输出 "不符合要求"。<br>``` |
| 不符合要求 | 首先，我们来逐步分析给定的JSON数据，以判断它是否符合所有提到的要求。<br>#### **思考过程**<br>1. **检查每个servlet是否有init-param**<br>   <br>   <br>   - `cofaxEmail`servlet 有`init-param`，包含 "mailHost" 和 "mailHostOverride"。<br>     <br>   - `cofaxTools`servlet 也有`init-param`，包含 "templatePath", "log", "logLocation", 和 "logMaxSize"。<br>     <br>**结论**：每个servlet都有`init-param`，满足要求1。<br>2. **检查servlet-mapping中的元素是否都在servlet中有匹配**<br>   <br>   <br>   - `servlet-mapping`中有两个元素：`cofaxEmail`和`cofaxTools`。<br>     <br>   - `servlet`定义中也正好有这两个servlet名称的定义：`cofaxEmail`和`cofaxTools`。<br>     <br>**结论**：`servlet-mapping` 中的所有元素都能在 `servlet` 中找到匹配，满足要求2。<br>3. **检查cofaxTools servlet中是否有三个以"log"开头的参数，且"log"参数小于10**<br>   <br>   <br>   - `cofaxTools`servlet 的`init-param`中以 "log" 开头的参数有："log"（值为1），"logLocation"（值为"/usr/local/tomcat/logs/CofaxTools.log"），和理论上应该计算在内的"logMaxSize"（尽管它的值为空，但题目似乎更关注前缀而非值的内容）。<br>     <br>   - 其中 "log" 的值为1，确实小于10。<br>     <br>**结论**：虽然关于"logMaxSize"是否算作以"log"开头的有效参数可能有歧义（因为它没有实际数值），但基于最直接的解读，我们可以认为是满足了至少存在三个以"log"开头的参数这一条件，且明确指定的"log"参数值为1，小于10，因此大体上满足要求3，尽管"logMaxSize"的处理依据具体情况可能有所不同。<br>#### **输出**<br>基于以上分析，虽然关于"logMaxSize"的处理可能存在解释空间，但主要条件基本得到满足。因此，如果对"logMaxSize"不作严格要求（比如，不强制要求它必须有一个有效数值且小于10），则可以认为整体 **符合要求**。如果有对"logMaxSize"的具体数值要求，则需要进一步澄清后决定。但在标准解读下，答案应为：“符合要求”。 |

除了思维链，启发 LLM 进行“思考”的实用方法还有 **提示链（Prompt Chaining）**。提示链通过多轮对话，引导 LLM “思考” 方向，让 LLM 从简单任务开始，沿着设计好的“思考”方向逐步完成一个复杂推理。

提示链虽然相对思维链来说构建模式更加复杂，但 **模型表现更好，准确率更高**。它非常适合逻辑复杂但能按照固定模式拆解的困难任务。

#### **提示链（Prompt Chaining）引导样例**

数学题：

又到了周日，小明像以往一样去爷爷奶奶家玩，小明于早上八点整步行出发，已知小明每分钟行走50米，走了12分钟后，小明的父亲发现小明忘记带作业了，于是便骑车去追小明，已知小明的爸爸每分钟骑行200米，等到追上小明后，爸爸决定骑车带上小明，已知小明坐自行车的路程是走路路程的5倍，请问，小明和他爸爸几点到爷爷家的呢？（小明8点36分到爷爷家）

第一轮输入（数学题 \+ 第一个简单问题）：

```plaintext
#背景#
又到了周日，小明像以往一样去爷爷奶奶家玩，小明于早上八点整步行出发，已知小明每分钟行走50米，
走了12分钟后，小明的父亲发现小明忘记带作业了，于是便骑车去追小明，已知小明的爸爸每分钟骑行200米，
等到追上小明后，爸爸决定骑车带上小明，已知小明坐自行车的路程是走路路程的5倍，

#目的#
计算小明什么时候被他爸爸追上，追上时走了多远？
```

**Output 1（LLM 对第一个简单问题的回答）：**

```plaintext
首先，我们计算小明在被父亲追上之前走了多远。
小明的速度是每分钟50米，他已经走了12分钟，因此他已经走过的距离是：
50 米/分钟 × 12 分钟 = 600 米
接下来，我们计算父亲开始追赶小明时两者的相对速度。父亲的骑行速度是每分钟200米，而小明继续以每分钟50米的速度步行。因此，父亲相对于小明的速度是：
200 米/分钟 − 50 米/分钟 = 150 米/分钟
为了追上小明，父亲需要覆盖小明最初12分钟所行走的600米距离。以150米/分钟的相对速度，父亲追上小明所需的时间是：
600 米 / 150 米/分钟 = 4 分钟
这意味着父亲在开始追赶后的4分钟追上了小明，从父亲开始追赶算起，总共用了12分钟（小明已经走了的时间）+ 4分钟（父亲追赶的时间）= 16分钟。
现在，我们要计算小明被追上时共走了多远。小明在最初的12分钟内走了600米，从父亲开始追赶的4分钟里，小明又走了：
50 米/分钟 × 4 分钟 = 200 米
所以，小明被追上时总共走了：
600 米 + 200 米 = 800 米
综上所述，小明在早上8点16分被他爸爸追上，此时他已经走了800米。
```

第二轮输入（第二个问题，问题逐渐深入）：

```plaintext
#目的#
计算小明还要坐多远自行车才能到爷爷家？
```

**Output 2（LLM 对第二个问题的回答）：**

```plaintext
根据题目，小明坐自行车的路程是他走路路程的5倍。小明被追上时已经走了800米，那么他坐自行车的路程将是：
800 米 × 5 = 4000 米
```

第三轮输入（最后的复杂问题）：

```plaintext
#目的#
小明什么时候到爷爷家？
```

**Output 3（通过前面多个问题的引导得到了正确的结果）：**

```plaintext
要计算小明什么时候到爷爷家，我们需先确定小明坐上自行车后的行进时间。
小明坐自行车的总路程是4000米，他父亲的骑行速度是每分钟200米。因此，小明坐自行车所需的时间是：
4000  米 / 200  米/分钟 = 20  分钟
小明从出发到被追上已经过去了16分钟（即8:00出发，8:16被追上），加上坐自行车的20分钟，总共用时为：
16 分钟 + 20 分钟 = 36 分钟
所以，小明在早上8点出发后，将在36分钟后到达爷爷家，即：
8:00 AM + 36  分钟 = 8:36  AM
因此，小明将在上午8点36分到达爷爷家。
```

引导 LLM “思考”的方法还有很多种，比如：思维树（Tree of Thoughts, ToT)、Boosting of Thoughts 等。

## Prompt 测试与迭代

生成最优 prompt 是一个高度实验性的过程，需要不断尝试和调整各种方法。整个 prompt 工程的优化过程可概括如下：

![image](<Base64-Image-Removed>)

此外，值得注意的是，除了精心设计的 prompt 外，用户提供的反馈和修正也是获取模型最佳输出的关键因素之一。即使在 prompt 优化完成后，持续地在线上环境中接收反馈并作出相应调整，才能使模型更好地理解和满足用户需求。

## Prompt 优化案例：跨国公司 AI 助手稳定地输出多语言内容

问题背景：用户反馈 qwen-turbo 无法稳定地用英文回答英文问题。

优化点有：

1. 将“语言”替换为“语种”。因为“语言”这个词有歧义，不一定代指的是英语、法语，也可以是书面语言、口头语言。语种就没有这个歧义。

2. 优化前 Prompt 结构较为松散，而且`## 限制`部分内容过于冗余。因此使用本教程提供的 Prompt 框架重新排版并将`## 限制`部分的内容拆分到正确的位置。

3. `${documents}`部分是一段很长的话，放在某句话中并不合适。应该使用分隔符标记切分出来，作为一个重要的内容块。

| **优化前 Prompt** | **优化后 Prompt** |
| --- | --- |

|     |     |
| --- | --- |
| **优化前 Prompt** | **优化后 Prompt** |
| \# 角色<br>你是一位高效的HR AI助手，专门负责解答公司内部关于政策、考勤制度、年假安排等相关问题。你具备快速准确地解析公司政策文档的能力，并能够为同事提供清晰简洁的说明。<br>\## 技能<br>\### 技能1: 政策解析<br>\- \*\*任务\*\*：准确解读公司政策文档，为同事提供清晰、简洁的政策说明。<br>\- 快速定位到相关政策条款，解答具体的政策执行细节。<br>\- 确保解释的内容易于理解且符合公司的官方规定。<br>\### 技能2: 考勤答疑<br>\- 解答与员工考勤相关的所有疑问，包括打卡规则、迟到早退处理、请假流程等。<br>\- 提供具体的考勤操作指南和特殊情况处理建议。<br>\### 技能3: 年假管理咨询<br>\- 详细解释年假申请条件、累积规则、有效期及审批流程。<br>\- 协助计算员工的年假余额，提供休假规划建议。<br>\## 工具与资源<br>\- \*\*知识库访问\*\*：直接引用和解析\`${documents}\`中的公司政策文档和相关规章制度，确保答案的权威性和时效性。<br>\- 如果提出的问题是英文，请用你理解的中文含义去检索知识库，最后再使用英文回复（请注意回复内容中的标点符号统一为英文格式！尤其字符 U+2019 "’"，请替换为“'” ）。<br>\## 限制<br>\- 要求回答内容仅使用标准 ASCII 字符集，不要出现中文引号、全角逗号及其他全角标点符号！！！<br>\- 使用与用户提问相同的语种回复，例如用户使用中文，回答中文，用户使用英文，回答英文。<br>\- 仅限于解答公司政策、考勤制度、年假等人力资源管理范畴内的问题。<br>\- 不涉及个人隐私数据的查询，保护员工信息安全。<br>\- 当遇到知识库未涵盖或不明确的问题时，需指引询问者联系人力资源部门获取进一步的帮助。 | #背景#<br>你是一位跨国公司的高效的HR AI助手，专门负责解答公司内部关于公司政策解析、考勤答疑、年假管理咨询的问题。你具备快速准确地解析公司政策文档的能力。以下为公司政策文档：<br>======<br>\`${documents}\`<br>======<br>#目的#<br>1. 用户的问题仅限于公司政策解析、考勤答疑、年假管理咨询三类范畴。<br>   <br>2. 当问题在范畴内但知识库未涵盖或不明确时，指引用户联系人力资源部门获取进一步的帮助。<br>   <br>3. 三类问题按照以下要求进行回答：<br>   1. 政策解析<br>      1. 准确解读公司政策文档，为用户提供清晰、简洁的政策说明。<br>         <br>      2. 快速定位到相关政策条款，解答具体的政策执行细节。<br>         <br>      3. 确保解释的内容易于理解且符合公司的官方规定。<br>   2. 考勤答疑<br>      <br>      \- 解答与员工考勤相关的所有疑问，包括打卡规则、迟到早退处理、请假流程等。<br>      <br>      \- 提供具体的考勤操作指南和特殊情况处理建议。<br>      <br>   3. 年假管理咨询<br>      <br>       \- 详细解释年假申请条件、累积规则、有效期及审批流程。<br>      <br>      \- 协助计算员工的年假余额，提供休假规划建议。<br>4. 不涉及个人隐私数据的查询，保护员工信息安全。<br>   <br>#多语言要求#<br>\- 如果提出的问题不是中文，用问题的中文含义去检索知识库。<br>\- 知识库检索出来的内容在输出时也要转换为问题的语种。<br>#输出#<br>1\. 仅使用标准 ASCII 字符集输出回答。<br>2\. 输出的内容语种为用户输入的语种。 |

## Prompt 优化案例：从对话中提取多维度分析结果并输出 JSON

在客服质检、销售分析等业务场景中，常需要从一段对话中同时提取多个维度的分析结果，并以结构化的 JSON 格式输出，以便后续系统处理。以下案例展示如何通过精心设计的 Prompt 实现这一目标。

优化点有：

1. **任务指令**：明确告诉模型需要做什么，用指令形式而非联想形式描述任务，减少模型理解的层数。

2. **回答格式**：指定 JSON 格式模板，让模型严格按照结构化格式输出，有效减少幻觉。

3. **注意事项**：提出对模型的明确要求与限制，如"准确性优先""不能更改原文"等，进一步约束模型行为。

4. **输出示例**：提供符合格式要求的样例数据，是避免模型产生幻觉的最有效方式。

| **优化前 Prompt** | **优化后 Prompt** |
| --- | --- |

|     |     |
| --- | --- |
| **优化前 Prompt** | **优化后 Prompt** |
| 请帮我分析以下电话销售对话中的这些问题：沟通不足、关键信息、客户关注点、需求急迫度、影响成交的因素、客户满意度。<br>（用户对话内容） | 任务指令：根据用户提供的对话内容，回答最后提出的问题。每个问题的回答应首先直接给出答案，然后列出支持该答案的依据；如果问题比较复杂，则根据对话内容分点描述。<br>回答格式：请按照以下 JSON 格式组织答案：<br>```json<br>[<br> {"question": "问题1", "answer": ["答案", "依据一", "依据二"]},<br> {"question": "问题2", "answer": ["答案", "依据一", "依据二"]}<br>]<br>```<br>注意事项：<br>1\. 仔细阅读并理解用户提供的所有信息。<br>2\. 明确区分出用户提出的每一个独立问题。<br>3\. 确保输出的 JSON 格式正确无误，最后仅输出 JSON 内容。<br>4\. 准确性优先，列出依据时不能更改原文。<br>示例：（提供符合格式的样例数据）<br>（用户对话内容 \+ 问题列表） |

在优化前的 Prompt 中，模型可能以自由文本形式输出分析结果，格式不统一，难以被后续系统解析。而优化后的 Prompt 通过 **任务指令 \+ 格式模板 \+ 注意事项 \+ 示例** 四要素的组合，让模型能够准确识别所有问题并以规范的 JSON 格式输出，每个问题都附带来自原文的依据，便于自动化处理和质量追溯。

**说明**

当需要模型输出结构化数据时，提供明确的格式模板和符合格式的示例数据是最有效的优化手段。同时，使用"准确性优先""不能更改原文"等限制性指令，可以有效减少模型的幻觉现象。

该文章对您有帮助吗？

反馈

- 本页导读 （1）

设计 Prompt

构建清晰明确的 Prompt

使用 Prompt 框架

优化 Prompt

技巧一：为模型提供输出样例

技巧二：设定完成任务的步骤

技巧三：使用分隔符号区分单元

技巧四：引导模型“思考”

Prompt 测试与迭代

Prompt 优化案例：跨国公司 AI 助手稳定地输出多语言内容

Prompt 优化案例：从对话中提取多维度分析结果并输出 JSON

### [大模型](https://www.aliyun.com/product/tongyi)

一站式为企业和开发者提供大模型能力体系，大模型原生应用以及最佳解决方案，助力云上开发者轻松完成 AI 落地。

[**AI 体验馆** \\
免费体验前沿 AI 应用和最新通义系列大模型，开启智能创新](https://www.aliyun.com/exp/)

[**大模型服务平台百炼** \\
为企业打造的大模型服务与应用开发平台](https://www.aliyun.com/product/bailian)

#### 大模型

[**Qwen3.7-Max _HOT_** \\
智能体时代全能旗舰模型](https://bailian.console.aliyun.com/cn-beijing/?tab=model#/model-market/detail/qwen3.7-max?serviceSite=asia-pacific-china) [**Qwen3.7-Plus _NEW_** \\
能看、能想、能动手的多模态智能体模型](https://bailian.console.aliyun.com/cn-beijing?tab=model#/model-market/detail/qwen3.7-plus?serviceSite=asia-pacific-china) [**Qwen3.5-LiveTranslate** \\
低延迟音色克隆同传模型](https://pre-bailian.console.aliyun.com/cn-beijing?tab=model#/model-market/detail/qwen3.5-livetranslate-flash-realtime?serviceSite=asia-pacific-china)

[**HappyHorse-1.0-T2V _NEW_** \\
文生视频，精准理解语义，细节丰富画质流畅](https://bailian.console.aliyun.com/cn-beijing/?tab=model#/model-market/detail/happyhorse-1.0-t2v?serviceSite=asia-pacific-china) [**HappyHorse-1.0-I2V _NEW_** \\
图生视频，流畅自然，细节丰富](https://bailian.console.aliyun.com/cn-beijing/?tab=model#/model-market/detail/happyhorse-1.0-i2v?serviceSite=asia-pacific-china) [**Qwen3-VL-Plus** \\
视觉 Coding、空间感知、多模态思考等全面升级](https://bailian.console.aliyun.com/?tab=model#/efm/model_experience_center/vision?currentTab=imageComprehend&modelId=qwen3-vl-plus)

[**Wan2.7-Image** \\
全新图像生成与编辑模型](https://bailian.console.aliyun.com/cn-beijing/?tab=model#/model-market/detail/wan2.7-image) [**Wan2.7-Video** \\
全新视频生成模型，超强编辑能力](https://bailian.console.aliyun.com/cn-beijing/?tab=model#/model-market/detail/wan2.7-videoedit) [**Fun-ASR** \\
支持中英文自由切换，具备更强的噪声鲁棒性](https://bailian.console.aliyun.com/?tab=model#/efm/model_experience_center/voice?currentTab=voiceAsr&modelId=fun-asr-realtime)

[**Deepseek-v4-pro** \\
旗舰 MoE 大模型，百万上下文与顶尖推理能力](https://bailian.console.aliyun.com/cn-beijing/?tab=model#/model-market/detail/deepseek-v4-pro?serviceSite=asia-pacific-china) [**GLM-5.2** \\
1M上下文，专为长程任务能力而生](https://bailian.console.aliyun.com/cn-beijing?tab=model#/efm/model_experience_center/text?modelId=glm-5.2) [**MiniMax-M2.7** \\
自主构建复杂 Agent 架构，驾驭高难度生产力任务](https://bailian.console.aliyun.com/cn-beijing/?tab=model#/model-market/detail/MiniMax%2FMiniMax-M2.7?serviceSite=asia-pacific-china)

#### [大模型服务](https://bailian.console.aliyun.com/?tab=model\#/model-market)

[**大模型服务平台百炼-Token Plan** \\
面向企业和开发者打造的多模态 AI 订阅服务](https://bailian.console.aliyun.com/cn-beijing/?tab=plan#/efm/subscription/overview) [**大模型服务平台百炼-应用模版** \\
丰富多元化的应用模版和解决方案](https://bailian.console.aliyun.com/?tab=app#/app-market/newTemplate) [**大模型服务平台百炼-微调与部署** \\
一站式大模型服务平台，支持界面化微调与部署](https://bailian.console.aliyun.com/?tab=model#/efm/model_manager)

#### [AI 应用构建](https://bailian.console.aliyun.com/?tab=app\#/app-center)

[**大模型服务平台百炼 \- 模型体验** \\
在线体验全尺寸、多种模态的模型效果](https://bailian.console.aliyun.com/?tab=demohouse#/experience/llm) [**大模型服务平台百炼-智能体** \\
灵活可视化地构建企业级 Agent](https://bailian.console.aliyun.com/?tab=app#/app-center) [**人工智能平台 PAI** \\
AI Native 的算法工程平台，一站式完成建模、训练、推理服务部署](https://www.aliyun.com/product/bigdata/learn)

#### 大模型原生应用

[**Qoder _HOT_** \\
面向真实软件的智能体编程平台](https://www.aliyun.com/product/qoder) [**通义听悟** \\
智能会议助手，实时转写会议记录，支持搜索定位](https://tongyi.aliyun.com/tingwu) [**通义晓蜜** \\
智能客服平台，对话机器人、对话分析、智能外呼](https://tongyi.aliyun.com/xiaomi)

[**通义灵码** \\
智能编码助手，支持企业专属部署](https://www.aliyun.com/product/lingma) [**大模型服务平台百炼 \- 全妙** \\
多模态内容创作工具，已接入 DeepSeek](https://bailian.aliyun.com/quanmiao?from=bailian#/home) [**大模型服务平台百炼 \- 法睿** \\
法律智能助手，支持合同审查、法律咨询与检索、智能阅卷等](https://tongyi.aliyun.com/farui/home)

#### 大模型解决方案

[**快速部署 Dify，高效搭建 AI 应用** \\
依托云原生高可用架构,实现Dify私有化部署](https://www.aliyun.com/solution/tech-solution/rapidly-deploy-dify-to-accelerate-ai-application-development) [**10 分钟在聊天系统中增加一个 AI 助手** \\
在企业官网、通讯软件中为客户提供 AI 客服](https://www.aliyun.com/solution/tech-solution/build-a-chatbot-for-your-website-or-chat-system)

[**10分钟微调：让0.6B模型媲美235B模型** \\
用1%尺寸在特定领域达到大模型90%以上效果](https://www.aliyun.com/solution/tech-solution/qwen3-distill) [**即刻拥有 DeepSeek-R1 满血版** \\
多种方案随心选，轻松解锁专属 DeepSeek](https://www.aliyun.com/solution/tech-solution/deepseek-r1-for-platforms)

[**多模态数据信息提取** \\
从文本、图片、视频中提取结构化的属性信息](https://www.aliyun.com/solution/tech-solution/information-extraction) [**超强辅助，Bolt.diy 一步搞定创意建站** \\
通过自然语言交互简化开发流程,全栈开发支持](https://www.aliyun.com/solution/tech-solution/bolt-diy)

[**与 AI 智能体进行实时音视频通话** \\
构建支持视频理解的 AI 音视频实时通话应用](https://www.aliyun.com/solution/tech-solution/real-time-interaction) [**构建大模型应用的安全防护体系** \\
通过阿里云安全产品对 AI 应用进行安全防护](https://www.aliyun.com/solution/tech-solution/build-large-model-application-security-system)

### [产品](https://www.aliyun.com/product/list)

精选产品 [人工智能与机器学习](https://ai.aliyun.com/) [计算](https://www.aliyun.com/product/list/ecs) [容器](https://www.aliyun.com/product/aliware/containerservice) [存储](https://www.aliyun.com/storage/storage?spm=5176.19720258.J_2686872250.30.3f0e4ff6AwBQKs) [网络与CDN](https://www.aliyun.com/product/network/network) [安全](https://www.aliyun.com/product/list/security) [中间件](https://www.aliyun.com/product/list/aliware) [数据库](https://www.aliyun.com/product/outline/index?spm=5176.19720258.J_2686872250.45.3f0e4ff6AwBQKs) [大数据计算](https://www.aliyun.com/product/bigdata/apsarabigdata) 媒体服务 [企业服务与云通信](https://www.aliyun.com/product/list/ent-cmc) 域名与网站终端用户计算Serverless [开发工具](https://www.aliyun.com/product/list/developertools) [迁移与运维管理](https://www.aliyun.com/product/list/operation-mainenance) [专有云](https://apsara-stack.aliyun.com/)

#### 精选产品

[**大模型服务平台百炼 _大模型_** \\
大模型服务与应用平台](https://www.aliyun.com/product/bailian) [**千问大模型 _大模型_** \\
多元化、高性能、安全可靠的大模型服务](https://www.aliyun.com/product/tongyi) [**无影云电脑** \\
随时随地安全接入的云上超级电脑](https://www.aliyun.com/product/ecs/gws) [**短信服务** \\
国内短信简单易用，安全可靠，秒级触达，全球覆盖200+国家和地区。](https://www.aliyun.com/product/sms) [**云原生大数据计算服务 MaxCompute** \\
面向分析的企业级SaaS模式云数据仓库](https://www.aliyun.com/product/maxcompute)

[**域名与网站** \\
提供智能易用的域名与建站服务](https://wanwang.aliyun.com/) [**对象存储 OSS** \\
稳定、安全、高性价比、高性能的云存储服务](https://www.aliyun.com/product/oss) [**人工智能平台 PAI _大模型_** \\
一站式AI开发、训练和推理服务](https://www.aliyun.com/product/bigdata/learn) [**云原生数据库 PolarDB** \\
100%兼容MySQL、PostgreSQL，兼容Oracle，支持集中和分布式](https://www.aliyun.com/product/polardb) [**容器服务 Kubernetes 版 ACK** \\
提供一站式管理容器应用的 K8s 服务](https://www.aliyun.com/product/kubernetes)

[**云服务器 ECS** \\
安全可靠、弹性可伸缩的云计算服务](https://www.aliyun.com/product/ecs) [**云数据库 RDS** \\
全托管，含MySQL、PostgreSQL、SQL Server、MariaDB多引擎](https://www.aliyun.com/product/rds) [**Qoder** \\
面向真实软件的智能体编程平台](https://www.aliyun.com/product/qoder) [**大数据开发治理平台 DataWorks** \\
Data Agent 驱动的一站式 Data+AI 开发治理平台](https://www.aliyun.com/product/dide) [**云防火墙** \\
云原生的云上边界网络安全防护产品](https://www.aliyun.com/product/cfw)

[**轻量应用服务器** \\
快速构建应用程序和网站，即刻迈出上云第一步](https://www.aliyun.com/product/swas) [**数字证书管理服务（原SSL证书）** \\
实现全站 HTTPS，呈现可信的 Web 访问](https://www.aliyun.com/product/cas) [**云解析DNS** \\
覆盖公网/内网、递归/权威、移动APP等全场景解析服务](https://www.aliyun.com/product/dns) [**Qoder CN** \\
基于通义大模型，支持代码智能生成、研发智能问答](https://www.aliyun.com/product/lingma)

### [解决方案](https://www.aliyun.com/solution/tech-solution/)

精选解决方案 [AI](https://www.aliyun.com/solution/tech-solution/ai) 互联网应用开发大数据现代化应用安全网络可观测上云与迁云 [企业出海](https://www.aliyun.com/goglobal) 政企业务

#### 精选解决方案

[**HappyHorse 打造一站式影视创作平台 _NEW_** \\
可视化编排打通从文字构思到成片全链路闭环](https://www.aliyun.com/solution/tech-solution/infinite-canvas) [**Claude Code + GStack 打造工程团队** \\
安装技能 GStack，拥有专属 AI 工程团队](https://www.aliyun.com/solution/tech-solution/gstack) [**自然语言编程：人人都能做 Web 开发** \\
自然语言驱动的沉浸式在线编程应用](https://www.aliyun.com/solution/tech-solution/web-vibe-coding) [**10 分钟在聊天系统中增加一个 AI 助手** \\
在企业官网、通讯软件中为客户提供 AI 客服](https://www.aliyun.com/solution/tech-solution/build-a-chatbot-for-your-website-or-chat-system)

[**Hermes Agent，打造自进化智能体 _NEW_** \\
自主进化，持久记忆，越用越聪明](https://www.aliyun.com/solution/tech-solution/hermes-agent) [**5 分钟轻松部署专属 QwenPaw _HOT_** \\
从聊天伙伴进化为能主动干活的本地数字员工](https://www.aliyun.com/solution/tech-solution/copaw) [**深度研究：生成你的独家洞察报告** \\
智能生成洞察、分析等深度研究与决策报告](https://www.aliyun.com/solution/tech-solution/deep-research) [**高效搭建 AI 智能体与工作流应用** \\
通过阿里云百炼高效搭建AI应用,助力高效开发](https://www.aliyun.com/solution/tech-solution/build-ai-applications-based-on-alibaba-cloud-model-studio)

[**基于 Spark 和 PyTorch 的模型训练方案** \\
Serverless 分布式 AI 训练平台,突破算力运维与成本瓶颈](https://www.aliyun.com/solution/tech-solution/spark-ai-train) [**极速搭建专属 SBTI 测评网站** \\
快来测试全新SBTI人格画像](https://www.aliyun.com/solution/tech-solution/sbti) [**快速拥有专属 OpenClaw _HOT_** \\
让AI从“聊天伙伴”进化为能干活的“数字员工”](https://www.aliyun.com/solution/tech-solution/clawdbot) [**低代码高效构建企业门户网站** \\
以可视化方式快速构建移动和 PC 门户网站](https://www.aliyun.com/solution/tech-solution/build-a-website)

[**基于 Hologres 的广告创投一体化 _HOT_** \\
Hologres 助力游戏广告，自动增效省资源](https://www.aliyun.com/solution/tech-solution/hologres-ai-function) [**效率翻倍，一句话生成专业 PPT** \\
输入一句话想法, 轻松生成专业的 PPT](https://www.aliyun.com/solution/tech-solution/vibe-ppt) [**漫剧工坊：一站式动画创作平台** \\
快速生产连贯的高质量长漫剧](https://www.aliyun.com/solution/tech-solution/use-bailian-to-intelligently-create-comics) [**10 分钟搭建微信、支付宝小程序** \\
高效部署网站，快速应用到小程序](https://www.aliyun.com/solution/tech-solution/develop-your-wechat-mini-program-in-10-minutes)

### [权益](https://www.aliyun.com/benefit)

上云优选，普惠好价，为开发者和企业提供多款超值优选上云必备产品；超 140 款免费试用产品；初创企业最高可得 100 万抵扣金。

#### 普惠上云

[**普惠上云 官方力荐** \\
云服务器38元/年起，超值低价云产品抢先购](https://www.aliyun.com/benefit/select/cloud-discount) [**官方推荐返现计划** \\
推荐新用户得奖励，单订单最高返9万](https://dashi.aliyun.com/) [**云工开物** \\
高校专属算力普惠，学生认证享300元代金券](https://university.aliyun.com/)

#### 免费试用

[**解决方案免费试用 新老同享** \\
最高领取价值200元试用点，立即开启云上创新](https://www.aliyun.com/solution/free) [**AI 产品 免费试用** \\
1亿+ 大模型 tokens 和 30+ 款产品免费体验](https://free.aliyun.com/product/ai) [**140+云产品 免费试用** \\
产品新客免费试用，最长12个月](https://free.aliyun.com/) [**大模型ACA认证体验** \\
助力企业全员 AI 认知与能力提升](https://edu.aliyun.com/learning/topic/llm-free-trial)

#### AI 特惠

[**AI 加速季，智惠生产力 _HOT_** \\
Qwen 3.7 限时5折，先用后返最高 200 元](https://www.aliyun.com/activity/hub/ai-innovation) [**智启 AI 普惠权益** \\
至高享 1亿+免费 tokens，加速 Al 应用落地](https://www.aliyun.com/benefit/ai/discount) [**阿里云 OPC 创新助力计划** \\
至高百万元 Token 补贴，加速一人公司成长](https://opc.aliyun.com/) [**阿里云百炼 Token Plan _HOT_** \\
多模型灵活切换，兼容主流 AI 工具，多档套餐选择](https://www.aliyun.com/benefit/scene/tokenplan) [**Qwen3.7-Max 发布，限时5折起 _NEW_** \\
智能体新前沿，让复杂任务更轻松](https://www.aliyun.com/benefit/scene/qwen3) [**Qwen3.7-Plus 发布，限时8折 _NEW_** \\
多模态智能体能力再升级](https://www.aliyun.com/benefit/scene/qwen37plus) [**HappyHorse 系列模型限时 8 折 _NEW_** \\
新一代 AI 视频生成模型](https://www.aliyun.com/benefit/scene/happyhorse)

#### AI 场景体验

[**AI Coding** \\
智能编程，一键开启高性价比 AI 编程新体验](https://www.aliyun.com/benefit/scene/coding) [**AI 电商营销** \\
从图文生成到视频创作，一键激活电商全链路生产力](https://www.aliyun.com/benefit/aiuse/e-commerce) [**AI 广告创作** \\
图文、视频一站生成，高效打造优质广告素材](https://www.aliyun.com/benefit/aiuse/ad) [**AI 建站** \\
0 代码专业建站，无忧落地极速上线](https://www.aliyun.com/benefit/client/website?tid=service-overview) [**AI 短剧/漫剧** \\
AI助力短剧漫剧创作，剧本、分镜、视频高效生成](https://www.aliyun.com/benefit/scene/playlet) [**AI 办公** \\
AI智能应用，一键激活高效办公新体验](https://www.aliyun.com/benefit/aiuse/office) [**智能客服** \\
自动承接线索、识别商机，让客服更高效、服务更出色。](https://www.aliyun.com/benefit/scene/callcenter)

#### AI 活动

[**AI 生产力先锋** \\
先锋实践拓展 AI 生产力的边界](https://www.aliyun.com/activity/ai-seminar/home) [**飞天发布时刻** \\
所见，即是所愿](https://summit.aliyun.com/apsaramoment) [**AI 实训营** \\
从基础到进阶，Agent 创客手把手教你](https://www.aliyun.com/benefit/aihands-on/mainpage)

#### 创新加速

[**上云场景组合购** \\
覆盖90%+业务场景，专享组合折扣价](https://www.aliyun.com/benefit/client/package) [**老友焕新 权益中心** \\
100+款云产品超值低价](https://www.aliyun.com/benefit/client/index)

### [定价](https://www.aliyun.com/price)

提供灵活的计费方式和清晰的计费规则，满足不同的业务场景需求；支持自助估算价格、高效采购；专业的成本管理工具，持续优化云上成本。

[**产品定价** \\
了解云产品的定价详情](https://www.aliyun.com/price/detail) [**云上成本管理** \\
管理和优化成本](https://www.aliyun.com/price/cost-management)

[**价格计算器** \\
自助选配和估算价格](https://www.aliyun.com/price/product) [**价格优势** \\
推动算力普惠，释放技术红利](https://www.aliyun.com/price/advantage)

[**配置报价器** \\
一站式生成采购清单，支持单品或批量购买](https://www.aliyun.com/price/cpq/list)

[![5亿算力补贴](https://img.alicdn.com/imgextra/i2/O1CN01rarnNB1diFke7Rby7_!!6000000003769-0-tps-400-500.jpg)**5亿算力补贴** \\
\\
新迁上云，5亿补贴享不停](https://www.aliyun.com/benefit/scene/subsidy)

### [云市场](https://market.aliyun.com/)

提供与阿里云能力融合和互补的优质伙伴产品和服务，满足企业上云和各类业务应用开发需求。

#### [精选商城](https://market.aliyun.com/xinxuan)

[网站建设](https://market.aliyun.com/xinxuan/webdesign) [多端小程序](https://market.aliyun.com/xinxuan/application/miniapps) [Salesforce 国际版订阅](https://market.aliyun.com/products/56790007/cmfw00037956.html?innerSource=search_salesforce#sku=yuncode3195600001) [友盟天域](https://market.aliyun.com/products/56842011/cmfw00040027.html) [观测云](https://market.aliyun.com/products/56838014/cmgj00053362.html) [Tuya 物联网平台阿里云版](https://www.aliyun.com/research/tuya) [蓝凌 OA](https://market.aliyun.com/xinxuan/lanling-oa) [电子合同](https://market.aliyun.com/xinxuan/wyy-2023) [畅捷通](https://market.aliyun.com/products/56764034/cmgj00042861.html) [Tableau 订阅](https://market.aliyun.com/products/56024006/cmfw00062543.html) [AI空中课堂在线直播课堂（旗舰版）](https://market.aliyun.com/products/201204006/cmgj00070018.html)

#### [生态解决方案](https://market.aliyun.com/industry)

[行业生态解决方案](https://market.aliyun.com/industry) [开发者生态解决方案](https://market.aliyun.com/developer/shouye) [AI 开发和 AI 应用解决方案](https://market.aliyun.com/developer/AIGC)

#### [数据与 API](https://market.aliyun.com/data)

[数据集](https://market.aliyun.com/dataexchange) [手机三要素](https://market.aliyun.com/products?k=%E6%89%8B%E6%9C%BA%E4%B8%89%E8%A6%81%E7%B4%A0&scene=market) [身份实名认证](https://market.aliyun.com/products?k=%E8%BA%AB%E4%BB%BD%E5%AE%9E%E5%90%8D%E8%AE%A4%E8%AF%81&scene=market) [短信](https://market.aliyun.com/products?k=%E7%9F%AD%E4%BF%A1&scene=market) [OCR 文字识别](https://market.aliyun.com/products?k=OCR%E6%96%87%E5%AD%97%E8%AF%86%E5%88%AB&scene=market) [发票查验](https://market.aliyun.com/products?k=%E5%8F%91%E7%A5%A8%E6%9F%A5%E9%AA%8C&scene=market) [天气预报查询](https://market.aliyun.com/products?k=%E5%A4%A9%E6%B0%94%E9%A2%84%E6%8A%A5%E6%9F%A5%E8%AF%A2&scene=market) [快递物流查询](https://market.aliyun.com/products?k=%E5%BF%AB%E9%80%92%E7%89%A9%E6%B5%81%E6%9F%A5%E8%AF%A2&scene=market)

#### [企业应用](https://market.aliyun.com/enterprise)

[ERP](https://market.aliyun.com/products?k=ERP&scene=market) [CRM](https://market.aliyun.com/products?k=CRM&scene=market) [OA 办公系统](https://market.aliyun.com/products?k=OA%E5%8A%9E%E5%85%AC%E7%B3%BB%E7%BB%9F&scene=market) [财税管理](https://market.aliyun.com/products/56764034?page=1&scene=market) [400电话](https://market.aliyun.com/products?k=400%E7%94%B5%E8%AF%9D&scene=market) [广告营销](https://market.aliyun.com/products/56842011?page=1&scene=market)

#### [基础软件](https://market.aliyun.com/software)

[Windows](https://market.aliyun.com/products?k=Windows&scene=market) [宝塔 Linux](https://market.aliyun.com/products?k=%E5%AE%9D%E5%A1%94+Linux&scene=market) [CentOS](https://market.aliyun.com/products?k=CentOS&scene=market) [Docker](https://market.aliyun.com/products?k=Docker&scene=market) [JAVA](https://market.aliyun.com/products?k=JAVA&scene=market) [全能环境](https://market.aliyun.com/products?k=%E5%85%A8%E8%83%BD%E7%8E%AF%E5%A2%83&scene=market) [操作系统](https://market.aliyun.com/products?k=%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F&scene=market) [WordPress](https://market.aliyun.com/products?k=WordPress&scene=market) [Ubuntu](https://market.aliyun.com/products?k=Ubuntu&scene=market) [Red Hat](https://market.aliyun.com/products?k=Red+Hat&scene=market) [SUSE](https://market.aliyun.com/products?k=SUSE&scene=market)

#### [建站小程序](https://market.aliyun.com/jianzhan)

[模板建站](https://market.aliyun.com/products/56598032?page=1&scene=market) [定制建站](https://market.aliyun.com/products/52738005?page=1&scene=market) [模板小程序](https://market.aliyun.com/products/205798005?page=1&scene=market) [定制小程序](https://market.aliyun.com/products/52752001?page=1&scene=market) [APP 开发](https://market.aliyun.com/products/55514022?page=1&scene=market) [建站系统](https://market.aliyun.com/products/57342011?page=1&scene=market)

#### [专业服务](https://market.aliyun.com/service)

[域名](https://market.aliyun.com/products?k=%E5%9F%9F%E5%90%8D&scene=market) [商标](https://market.aliyun.com/products?k=%E5%95%86%E6%A0%87&scene=market) [备案](https://market.aliyun.com/products?k=%E5%A4%87%E6%A1%88&scene=market) [公司注册](https://market.aliyun.com/products?k=%E5%85%AC%E5%8F%B8%E6%B3%A8%E5%86%8C&scene=market) [上云迁移](https://market.aliyun.com/products/52738004?page=1&scene=market) [代维服务](https://market.aliyun.com/products/52732002?page=1&scene=market)

#### [安全](https://market.aliyun.com/security)

[VPN](https://market.aliyun.com/products?k=VPN&scene=market) [SSL 证书](https://market.aliyun.com/products?k=SSL%E8%AF%81%E4%B9%A6&scene=market) [堡垒机](https://market.aliyun.com/products?k=%E5%A0%A1%E5%9E%92%E6%9C%BA&scene=market) [防火墙](https://market.aliyun.com/products?k=%E9%98%B2%E7%81%AB%E5%A2%99&scene=market) [主机安全](https://market.aliyun.com/products?k=%E4%B8%BB%E6%9C%BA%E5%AE%89%E5%85%A8&scene=market)

#### [AI 应用及服务市场](https://market.aliyun.com/common/ai)

[AI 应用](https://market.aliyun.com/products?k=AI%E5%BA%94%E7%94%A8&scene=market) [大模型](https://market.aliyun.com/products?k=%E5%A4%A7%E6%A8%A1%E5%9E%8B&scene=market) [自然语言处理](https://market.aliyun.com/products?k=%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86&scene=market) [数据标注](https://market.aliyun.com/products/201198004?page=1&scene=market) [机器学习](https://market.aliyun.com/products?k=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&scene=market)

### [伙伴](https://partner.aliyun.com/management/v2)

坚持伙伴优先，为伙伴提供产品、销售和服务的商业合作模式；与伙伴紧密合作，共同为客户提供更完备的产品、更完善的服务。

#### 成为销售伙伴

[分销伙伴](https://partner.aliyun.com/programs/reseller_P) [通用与行业 ISV 伙伴](https://partner.aliyun.com/program/ISV_partner) [咨询伙伴](https://partner.aliyun.com/program/consult_partner)

#### 销售伙伴合作计划

[无影生态合作计划](https://partner.aliyun.com/management/epp_wuying) [Salesforce On Alibaba Cloud Consulting Partner 合作计划](https://partner.aliyun.com/program/Salesforce_program) [AI 大模型销售与服务生态合作计划](https://partner.aliyun.com/program/aimsp)

#### 成为产品伙伴

[产品生态集成认证中心](https://partner.aliyun.com/program/PEIC) [产品生态伙伴](https://chanpinshengtai.aliyun.com/partner/partner) [产品生态伙伴工作台](https://aps.aliyun.com/#/)

#### 产品伙伴合作计划

[阿里云 AI 伙伴计划（繁花）](https://chanpinshengtai.aliyun.com/partner/ai) [弹性计算合作计划](https://partner.aliyun.com/program/txjs_program) [云存储合作计划](https://partner.aliyun.com/program/cunchu) [数据库合作计划](https://partner.aliyun.com/program/sjk_program) [云网络合作计划](https://chanpinshengtai.aliyun.com/chanpinpartner/network) [Salesforce On Alibaba Cloud ISV 合作计划](https://partner.aliyun.com/program/Salesforce-ISV)

#### [成为服务伙伴](https://gts.aliyun.com/)

[服务生态伙伴](https://gts.aliyun.com/)

#### 服务伙伴合作计划

[伙伴信用分合作计划](https://www.aliyun.com/gts/msp/Creditscoresystem)

#### 更多支持

[合作伙伴培训与认证](https://edu.aliyun.com/certification/partner) [查询合作伙伴](https://partner.aliyun.com/management/query#/) [登录合作伙伴管理后台](https://account.aliyun.com/login/qr_login.htm?oauth_callback=https://partner.aliyun.com/management/v2)

### [服务](https://www.aliyun.com/service)

提供多样化的支持计划和专家服务，满足上云咨询、迁移上云、云上运维等场景的全链路服务需求。

#### 售前咨询

[在线服务](https://smartservice.console.aliyun.com/pre-sale/chat?entrance=201&referrer=https%3A%2F%2Fwww.aliyun.com%2F%3Fspm%3Da1z2e.12184483.navigationzhcn.dnavigationzhcn6.469d3247dm8YgK)

#### 售后服务

[自助服务](https://smartservice.console.aliyun.com/tourist-self/self-service-center?from=webnav) [在线服务](https://smartservice.console.aliyun.com/service/robot-chat) [工单服务](https://smartservice.console.aliyun.com/service/create-ticket) [短信专区](https://smartservice.console.aliyun.com/tourist-self/self-service-center/topic?topicCode=dysms&from=webnav)

#### 企业增值服务

[企业支持计划](https://www.aliyun.com/service/supportplans) [专家技术服务](https://www.aliyun.com/service/list) [企业增值服务台](https://custservice.console.aliyun.com/value-added/home)

#### 企业成长

[服务实践](https://www.aliyun.com/service/customer-case) [创新中心](https://chuangke.aliyun.com/)

#### [阿里云认证](https://edu.aliyun.com/)

[大模型认证](https://edu.aliyun.com/certification/llm) [全部认证](https://edu.aliyun.com/certification/) [训练营](https://edu.aliyun.com/trainingcamp)

#### 信息公告

[官网公告](https://www.aliyun.com/notice/) [健康状态](https://status.aliyun.com/)

#### [开发者社区](https://developer.aliyun.com/)

[博文](https://developer.aliyun.com/indexFeed/) [问答](https://developer.aliyun.com/ask/) [电子书](https://developer.aliyun.com/ebook/) [镜像站](https://developer.aliyun.com/mirror/)

#### 我要反馈

[我要建议](https://www.aliyun.com/connect/home) [我要投诉](https://www.aliyun.com/complaint)

### [了解阿里云](https://www.aliyun.com/about)

作为全球领先的全栈人工智能服务商，阿里云坚持让计算成为公共服务，助力全球客户加速价值创新。

#### [为什么选择阿里云](https://www.aliyun.com/why-us)

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing) [技术领先](https://www.aliyun.com/why-us/leading-technology) [稳定可靠](https://www.aliyun.com/why-us/reliability) [安全合规](https://www.aliyun.com/why-us/security-compliance) [分析师报告](https://www.aliyun.com/analyst-reports) [研究报告与白皮书](https://www.aliyun.com/reports)

#### [天池大赛](https://tianchi.aliyun.com/)

[AI 算法大赛](https://tianchi.aliyun.com/competition/algorithmList/) [云开发大赛](https://tianchi.aliyun.com/competition/programList) [入门学习赛](https://tianchi.aliyun.com/competition/coupleList)

#### 最佳实践

[云上春晚](https://www.aliyun.com/about/gala) [云上奥运之旅](https://www.aliyun.com/about/games) [云栖战略参考](https://www.aliyun.com/about/magazines) [云上的中国](https://www.aliyun.com/about/ysdzg) [看见新力量](https://startup.aliyun.com/special/seenewpower) [金融模力时刻](https://summit.aliyun.com/market/financial-agent) [客户案例](https://www.aliyun.com/customer-stories/customer-case-index)

#### 市场活动

[2026 阿里云峰会](https://summit.aliyun.com/2026) [阿里云中企出海大会](https://summit.aliyun.com/go-global) [云栖大会](https://yunqi.aliyun.com/) [活动全景](https://www.aliyun.com/about/events)

#### 魔搭 ModelScope

[魔搭 ModelScope](https://modelscope.cn/home)

#### 高校合作

[云工开物](https://university.aliyun.com/) [科研合作](https://university.aliyun.com/activity/air)

#### [加入我们](https://careers.aliyun.com/)

[Careers](https://careers.aliyun.com/en/home) [社会招聘](https://careers.aliyun.com/off-campus/home) [校园招聘](https://careers.aliyun.com/campus/home)

### 阿里云中国站

www.aliyun.com

简体中文

English [**阿里云国际站** \\
www.alibabacloud.com](https://www.alibabacloud.com/)

### 联系我们

4008013260 [售前咨询](https://smartservice.console.aliyun.com/pre-sale/chat?entrance=201&referrer=https%3A%2F%2Fhelp.aliyun.com%2Fzh%2Fmodel-studio%2Fprompt-engineering-guide) [售后在线](https://smartservice.console.aliyun.com/service/robot-chat?entrance=201&referrer=https%3A%2F%2Fhelp.aliyun.com%2Fzh%2Fmodel-studio%2Fprompt-engineering-guide)

### 其他服务

[我要建议](https://www.aliyun.com/connect/home) [我要投诉](https://www.aliyun.com/complaint)

![登录插画](https://img.alicdn.com/imgextra/i2/O1CN015QIT9m1FmmyUntYlQ_!!6000000000530-2-tps-320-200.png)

登录以查看您的控制台资源

管理云资源

状态一览

快捷访问

[快捷注册](https://account.aliyun.com/register/qr_register.htm?oauth_callback=https%3A%2F%2Fhelp.aliyun.com%2Fzh%2Fmodel-studio%2Fprompt-engineering-guide) [登录阿里云](https://account.aliyun.com/login/login.htm?oauth_callback=https%3A%2F%2Fhelp.aliyun.com%2Fzh%2Fmodel-studio%2Fprompt-engineering-guide)

### 来源 9: 充分释放大模型的潜力——提示词工程的16 种方式 - AWS

- URL: https://aws.amazon.com/cn/blogs/china/sixteen-ways-of-prompt-engineering
- 精读方法：firecrawl-scrape

## 选择您的 Cookie 首选项

我们使用必要 Cookie 和类似工具提供我们的网站和服务。我们使用性能 Cookie 收集匿名统计数据，以便我们可以了解客户如何使用我们的网站并进行改进。必要 Cookie 无法停用，但您可以单击“自定义”或“拒绝”来拒绝性能 Cookie。

如果您同意，AWS 和经批准的第三方还将使用 Cookie 提供有用的网站功能、记住您的首选项并显示相关内容，包括相关广告。要接受或拒绝所有非必要 Cookie，请单击“接受”或“拒绝”。要做出更详细的选择，请单击“自定义”。

接受拒绝自定义

## 自定义 Cookie 首选项

Cookie 及类似工具(统称为“Cookie”)的用途包括以下几种。

### 关键

关键 Cookie 对我们提供网站和服务来说绝对必要，不可将其禁用。关键 Cookie 通常是根据您在网站上的操作(例如，设置您的隐私首选项，登录或填写表格)来设置的。

### 性能

性能 Cookie 可为我们提供有关客户使用网站情况的匿名统计信息，以便我们改善用户的网站体验及网站性能。经批准的第三方可为我们执行分析，但不可将数据用于其自身目的。

允许

### 功能

功能 Cookie 有助于我们提供有用的网站功能，记住您的首选项及显示有针对性的内容。经批准的第三方可对功能 Cookie 进行设置以提供某些网站功能。如果您不允许功能 Cookie，则某些或所有这些服务可能无法正常提供。

允许

### 广告

广告 Cookie 可由我们或我们的广告合作伙伴通过我们的网站进行设置，有助于我们推送有针对性的营销内容。如果您不允许广告 Cookie，则您所接收到的广告的针对性将会有所降低。

允许

阻止某些类型的 Cookie 的话，可能会影响到您的网站体验。您可以随时单击此网站页脚中的 Cookie 首选项来对您的 Cookie 首选项进行更改。要了解有关我们及经批准的第三方如何在网站上使用 Cookie 的更多信息，请阅读 [AWS Cookie 声明。](https://aws.amazon.com/legal/cookies/)

取消保存首选项

## 您的隐私选择

我们会在 AWS 网站和其他资产上展示与您的兴趣相关的广告，包括跨情境行为广告。跨情境行为广告使用来自一个网站或应用程序的数据，在另一个公司的网站或应用程序上向您投放广告。

若要不允许基于 Cookie 或类似技术的 AWS 跨情境行为广告，请选择下面的“不允许”和“保存隐私选择”，或访问启用了法律认可的拒绝信号的 AWS 网站（如全球隐私控制）。如果您删除 Cookie 或使用其他浏览器或设备访问此网站，则需要再次做出选择。有关 Cookie 以及我们如何使用的更多信息，请阅读我们的 [AWS Cookie 通知](https://aws.amazon.com/legal/cookies/)。

允许不允许

若要不允许所有其他 AWS 跨情境行为广告，请 [通过电子邮件填写此表单](https://pulse.aws/application/ZRPLWLL6?p=0)。

如需进一步了解 AWS 如何处理您的信息，请阅读 [AWS 隐私声明](https://aws.amazon.com/privacy/)。

取消保存隐私选择

## 无法保存 Cookie 首选项

我们目前只会存储基本 Cookie，因为我们无法保存您的 Cookie 首选项。

如果您想要更改 Cookie 首选项，请稍后使用 AWS 控制台页脚中的链接重试，如果问题仍然存在，请联系技术支持。

关闭

 [Skip to Main Content](https://aws.amazon.com/cn/blogs/china/sixteen-ways-of-prompt-engineering/#aws-page-content-main)

## [亚马逊AWS官方博客](https://aws.amazon.com/cn/blogs/china/)

# 充分释放大模型的潜力——提示词工程的 16 种方式

## 概述

**预训练**、 **微调** 和 **提示词工程** 是大型语言模型（LLM）生成质量优化的三种关键手段，各自具有不同的特点和优势。

**预训练** 是 LLM 发展的基石，通过在大规模无标注语料库上进行自监督学习，赋予模型通用的语言理解和生成能力。这种自然语言的通用知识为后续的微调和提示词工程奠定了坚实基础。

**微调则** 是利用有标注的任务数据，对预训练模型进行进一步调整和优化，使其更好地适应特定的下游任务。微调的优势在于可以充分利用监督信号，提高模型在特定领域的生成质量。但同时也存在过度微调导致过拟合、灾难性遗忘等潜在风险。

与之不同， **提示词工程** 无需对模型参数进行更新，而是通过设计合理的提示，激发预训练模型中蕴含的知识，从而在下游任务中获得良好的生成质量。这种方式更加高效灵活，避免了微调可能带来的问题。但提示词的设计质量对模型表现影响重大，需要更多研究来探索通用有效的提示设计范式。

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering1.png) |

接下来，本文将重点讨论提示词工程技术。文章将介绍提示词工程的基本原理、设计方法，以及在不同任务场景下的应用实践，旨在为读者提供全面的理解和借鉴。同时也会分析提示词工程当前面临的挑战和发展方向，为后续研究指明路径。

## 提示词工程的分类

提示词工程的分类方法很多，本文将根据提示词工程技术发展演进路径，将类型分为：直接提示（Prompt）、链式提示（Chain）、图谱提示（Graph）、生成类提示（Generate）、集成式提示（Integrate） 五种。

### 直接提示（Prompt）

这种直接的提示词的方式侧重点在于通过特定的指令设计，来提示模型产生更好的输出。主要方法包括：

Zero-shot（零次提示）、Few shots（少量提示）、Act 、ReAct 和 Directional Stimulus Prompting（方向性刺激提示）。

下面举几个例子，可以帮助大家加深这些方法差别的理解。

|     |     |
| --- | --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering2.png) | 我该怎么表白？ |

|     |     |
| --- | --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering3.png) | 这是几个例子，如何模仿这些例子对她表白？<br><example><br>…..<br></emaple><br><example><br>…..<br></emaple> |

|     |     |
| --- | --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering4.png) | 她喜欢哲学，我该怎么在表白的时候引入相关内容？ |

**Zero Shot**、 **Few Shots** 和 **Act** 这三种偏向直接在问题中精心构造输入的内容。

|     |     |
| --- | --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering5.png) | **初始提示词：**<br>假如我们在圣诞节相遇，<br>该如何把这个场景融入表白中？<br>**反应式提示：**<br>如果她接受了我的表白，<br>下一步该怎么办？ |

而 **ReAct** 这种方式，更加关注外部的信息反馈，根据外部信息反馈后做归因然后再进行响应。

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering6.png) |

**Directional Stimulus Prompting**，是指在提示词中加入一些提示，以限制在特定领域或限定的方向上生成的内容。请看如下例子：

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering7.png) |

方向性刺激提示与标准提示的比较

### 链式提示（Chain）

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering8.png) |

链式提示这种方式关注 LLM 的内部逻辑，比如思维链（Chain of Thought）、多模态思维链、思维树（Tree of Thought）。同时还关注在这个过程中的自洽（Self-consistent）和自我反思（Reflexion）。

在这个过程中，一般会将复杂问题进行拆解，分成多个步骤进行推理。这样做的好处是，可以让 LLM 在推理过程中更容易获得正确的答案。

例如，对于一些早期的大语言模型，我们输入“我有 23 个苹果，吃了 20 个后又买了 6 个，现在还有几个？”，大概率会给出错误答案。但是我们看在 Amazon Bedrock 上 Claude 3 Haiku 的响应，他将问题分解成了多个步骤，然后逐步推理获得了正确答案。

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering9.png) |

这种技术的核心就是在提示过程中表现为顺序的，可解释的，能够清晰地看到思维推理的过程。

Reflexion 顾名思义，是大语言模型对自己生成内容进行反思的一种过程。这种自我反思，会记录本轮的问题和输出的答案并作为记忆（上下文），然后再用大语言模型验证生成内容是否符合“初心”。如果不匹配我们就会让这个过程重复“持续思考”，直到获得理想的答案。

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering10.png) |

Reflexion 流程示意图

下面看一个综合运用了多种链式范式综合案例。

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering11.png) |

基于 Amazon Bedrock 上 LLM 的多 Agent 狼人杀游戏

这是一个基于多 Agent 的 AI 狼人杀游戏，在这个游戏中，多个游戏角色由 LLM 来扮演，主要通过 Claude 3 作为推理和发言的主模型，使用 Llama 3 8B Instruct 和 Mistral 7B Instruct 作为 **Reflexion** 和总结性文字的输出。不同游戏角色拥有不同的个性和记忆，角色会根据自己的记忆和游戏的流程不断去推理谁是地方阵营，并发动投票处决敌方。在每个轮次中，角色会对自己的发言进行自我反省，确定自己的发言是否对自己和己方阵营有利。这样做的好处就是可以避免角色出“昏招”。由于这个反省模型和发言模型不一样，这样也可以避开由于单一模型推理过程中造成的“偏见”的问题。在整个游戏过程中，每个角色都会根据外部的问题和事件，根据自己的 **独有记忆** 和 **共享记忆** 来对外部刺激作出响应。然后将“2 个大脑的声音”进行合理性验证，并得作出动作。这个游戏参考了“斯坦福小镇”的设计思路，对于制作开放式角色具有重要参考作用。

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering12.png) |

游戏主要流程设计

### 谱图提示（Graph）

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering13.png) |

图谱提示和链条提示方式非常相似，都是关注大模型内部结构化的推理过程。但这个过程并不是线性的，而是假定训练过程中隐式地构建了网状或者是图形结构的知识图谱。在用户交互过程中，通过寻找不同知识的连接性和关联性，产生多个维度和更加复杂的非线性答案。

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering14.png) |

在这个范式下我们一般会先通过实体的识别，先找出相关问题的出发点。而这个出发点可能不止一个，然后通过实体关系寻找可能的下一个相关节点的相关信息。然后重复这个过程直到在所有关系或指定的有限关系中找到相关内容，并对问题给出正确的解。这个范式适用于复杂数学问题、人物关系问题、犯罪线索发现等领域。

### 生成类提示（Generate）

生成类提示，主要技术包括 **Automatic Prompt  Engineer** 和 **Generate Knowledge Prompting**。

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering15.png) |

- **Automatic Prompt Engineer** 关注自动化。这个方法让指令生成问题被构建为自然语言合成问题，使用 LLMs 作为黑盒优化问题的解决方案来生成和搜索候选解。第一步选择一个语言模型用作推理，该模型接收输出数据以生成任务的指令候选项。这些候选解将指导搜索过程。使用大语言模型作为打分模型，然后根据计算的评估分数选择最合适的指令。

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering16.png) |

- **Generate Knowledge Prompting** 关注内容生成。这种技术的特点是利用语言模型已有的知识进行与问题相关的知识片段的生成，以帮助模型做出更准确的预测。

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering17.png) |

无论是哪种技术，都是利用 LLM 内部的知识来迭代补充知识的生成。下面举个例子大家可以对比着看。

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering18.png) |

使用某个大语言模型直接生成结果获得的错误例子

当然这个问题，现在使用更加强大的模型已经能直接获得正确答案。以下是使用 Amazon Bedrock 上 Claude 3 Haiku 的回答：

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering19.png) |

正确响应

虽然这个例子中的问题，Claude 3 Haiku 已经能正确回答。但是在很多场景下我们还是可以通过 **Generate Knowledge Prompting** 技术来提高问题解答的正确率。下面我们看看这一切是如何发生的：

**输入**

|     |
| --- |
| 问题：高尔夫球的一部分是试图获得比其他人更高的得分。是或否？<br>知识：高尔夫球的目标是以最少的杆数打完一组洞。一轮高尔夫球比赛通常包括 18 个洞。每个洞在标准高尔夫球场上一轮只打一次。每个杆计为一分，总杆数用于确定比赛的获胜者。解释和答案： |

**输出**

|     |
| --- |
| 不是，高尔夫球的目标不是获得比其他人更高的得分。相反，目标是以最少的杆数打完一组洞。总杆数用于确定比赛的获胜者，而不是总得分。 |

在实际实施的过程中，我们可能也会碰到一些输出不稳定的情况。具体情况需要根据业务来分析，可以考虑综合运用多种 PE 技术手段进行优化。

### 集成式提示（Integrate）

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering20.png) |

集成式提示，包括 **检索增强生成（** **RAG** **）**、 **自动推理**、 **工具使用**、 **程序辅助语言模型**。这些方式的共性都是大语言模型与外部资源进行交互，从而实现复杂任务，提升答案质量。

下面介绍一个综合应用这些技术的例子，下图是在 **2024** **年亚马逊云科技中国峰会** 上展示的一个 Text2SQL 落地的案例，架构参考下图：

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering21.png) |

Text2SQL 落地案例架构示意图

该解决方案基于自然语言的交互方式，通过意图识别过滤非法输入，用知识库中的查找相似问题并取回 SQL 语句（RAG），利用相似的 SQL 语句通过大语言模型生成目标 SQL 语句，根据 SQL 语句生成动态图表（PLA），还可以生成信息洞察。

## 总结

|     |
| --- |
| ![](https://s3.cn-north-1.amazonaws.com.cn/awschinablog/sixteen-ways-of-prompt-engineering22.png) |

本文一共介绍了 16 种提示词工程的相关技术，分别对应如何构建外部提示，利用内部知识逻辑或者借助外部数据信息，来引导模型产生更加准确的回答。

总的来说，提示词工程是一个充满活力和创新的领域，为大型语言模型的应用开辟了广阔的前景。通过不断探索和优化提示词的设计方法，我们能够最大限度地发挥模型的潜能，提高生成质量和任务适用性。未来，提示词工程必将与其他人工智能技术相互融合，为构建更加智能、高效和人性化的人机交互系统重要力量。

## 参考链接

[Prompt Engineering Guide](https://www.promptingguide.ai/)

## 本篇作者

### 来源 10: Prompt工程指南 - 华东师范大学开发者平台

- URL: https://developer.ecnu.edu.cn/vitepress/llm/prompts.html
- 精读方法：firecrawl-scrape

[Skip to content](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html#VPContent)

页面导航

# Prompt工程指南 [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#prompt%E5%B7%A5%E7%A8%8B%E6%8C%87%E5%8D%97)

您可以在 [https://chat.ecnu.edu.cn/html/#/app-center](https://chat.ecnu.edu.cn/html/#/app-center) 的 **效率辅助** 中，使用 **提示词生成器** 来快速的扩展生成详细的提示词。

## 什么是Prompt 工程 [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#%E4%BB%80%E4%B9%88%E6%98%AFprompt-%E5%B7%A5%E7%A8%8B)

提示词（Prompt）是一种指令、疑问或陈述，旨在指导或指示语言模型产生特定的文本回应。提示词是用户与语言模型互动的起始点，它清晰地表达了用户的意图，并且希望模型以有价值和相关的方式作出反应。通过精心构思的Prompt，我们能够指导大型语言模型（LLM）更准确地把握用户的意图，产生更精确、有用的答复。

在与大型模型互动时，由于用户可能缺乏经验或模型之间存在差异，可能会遇到不合适的提示词（Prompt）问题。因此，需要通过提示词工程，让用户能够引导模型的输出，产生相关性高、精确且高质量的文本。这与机器学习的过程相似，需要进行反复的迭代。

让我们以一个教育领域的实际场景为例，设想我们的目标是让模型创作一篇关于现代教育技术的文章。一开始，我们可能只给出一个简单的提示词：“创作一篇关于现代教育技术的文章。” 但模型可能只会提供一些泛泛的信息，缺乏深度或专业性。通过提示词工程的迭代过程，我们会逐步改进提示词。

例如，我们首先可能会尝试明确指定一些关键词：“以在线学习平台为焦点，创作一篇现代教育技术文章。” 这样，模型更有可能产生与在线学习平台相关的深入内容。在评估模型的输出时，我们可能发现某些内容仍然不够精确或不符合我们的期望。因此，在下一步迭代中，我们可以进一步细化提示词：“以在线学习平台为焦点，探讨其在提升教育公平性中的作用，创作一篇深入的教育技术报道。”

通过这种反复的迭代过程，我们不仅让模型更准确地理解我们的需求，也提升了生成内容的相关性和质量。这个案例展示了提示词工程的迭代过程，通过调整指令和任务描述，逐步优化模型的输出，使其更能满足特定场景的需求。

## 如何编写 Prompt [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#%E5%A6%82%E4%BD%95%E7%BC%96%E5%86%99-prompt)

### **Prompt 主要构成要素** [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#prompt-%E4%B8%BB%E8%A6%81%E6%9E%84%E6%88%90%E8%A6%81%E7%B4%A0)

- **引导语或指示语**：告诉模型您希望它执行哪种类型的任务，比如回答问题、提出建议、创作文本等。
- **上下文信息**：提供足够的背景信息，以便模型能够更好地理解和处理请求。上下文信息可能包括具体情境、相关数据、历史对话信息等内容。
- **任务描述**：明确地描述你期望模型执行的任务。它可以是一个问题、一个命令性语句或者是一个场景描述。
- **输出格式指示**：如果您对输出结果有特定的格式要求，应在prompt中说明。比如，您可以指定输出应该是列表形式、一段连贯的文本还是一系列步骤等。
- **限制条件**：设置一些约束条件，指导模型避免某些类型的回答或者引导模型产生特定风格的内容。例如，可以限制回答的字数、要求避免使用专业术语等。
- **样例输出**：提供一个或多个例子可以帮助LLM理解所期望的输出类型和质量。
- **结束语**：如果有必要，可以使用结束语来标示prompt的结束，尤其是在连续的对话或者交互中。

> 这些要素并不是每个prompt都必须包含的，但根据特定的需求和上下文，合适地结合这些要素可以提高LLM生成的文本质量和相关性。

## Prompt 设计方法 [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#prompt-%E8%AE%BE%E8%AE%A1%E6%96%B9%E6%B3%95)

#### **①明确的任务指示** [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#_1%E6%98%8E%E7%A1%AE%E7%9A%84%E4%BB%BB%E5%8A%A1%E6%8C%87%E7%A4%BA)

a. Prompt应该清晰地定义你希望LLM完成的任务，内容要尽可能清晰、具体，避免出现歧义。

| **任务指示不明确的prompt** | **指示明确的prompt** |
| --- | --- |
| 我想知道如何提高学生的学习成绩。 | 请列出五种有效的学习方法，并解释每种方法如何帮助学生提高学习成绩。 |
| 给我一些关于课堂管理的建议。 | 请列出五个课堂管理技巧，并详细说明每个技巧如何在实际教学中应用。 |

b. 指定完成任务的步骤：如果有明确的步骤，通过指定完成任务需要的步骤，可以帮助LLM遵循正确的操作流程，从而更精确地生成回应。

| **无任务完成步骤的prompt** | **有任务完成步骤的prompt** |
| --- | --- |
| 写一篇关于如何提高学生学习成绩的文章。 | 为了写一篇关于如何提高学生学习成绩的文章，请遵循以下步骤：1\. 定义学习成绩并解释其重要性。2. 列出影响学习成绩的主要因素。3. 讨论不同学习方法的优缺点。4. 提出具体的提高学习成绩的策略和方法。 |
| 帮我设计一节课的教学计划。 | 为了设计一节课的教学计划，请按照以下步骤：1\. 确定课程目标和学习目标。2. 选择合适的教学材料和资源。3. 制定详细的教学流程和时间安排。4. 设计评估和反馈机制。5. 准备补充活动和作业。请根据这些步骤提供一个完整的教学计划。 |

#### **②提供充分的上下文信息** [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#_2%E6%8F%90%E4%BE%9B%E5%85%85%E5%88%86%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87%E4%BF%A1%E6%81%AF)

a. 提供背景信息或具体情境，帮助LLM更好地理解任务。

| **无具体情景** | **有具体情景** |
| --- | --- |
| 请阐述量子物理的基本原理及其在解释微观粒子行为中的核心作用，并举例说明量子力学中体现其非经典性的奇特现象。 | 在高年级物理课程中，学生们正在探索微观世界的行为规律。现在，请详细解释一下量子物理这一理论是如何描述和理解原子、分子等微观粒子的运动状态以及相互作用，并给出一个或两个著名的量子力学现象作为例子来帮助他们深入理解这一概念。 |
| 解释课堂管理的策略。 | 在一次教师培训工作坊上，教师们希望学习有效的课堂管理策略。请详细解释五个课堂管理技巧，并说明每个技巧在实际教学中的应用实例。 |

b. 角色指定： 指定模型应扮演的角色，这有助于设定LLM回答的特定的语气和风格。

| **无角色指定** | **有角色指定** |
| --- | --- |
| 解释如何使用布卢姆分类法进行教学评估。 | 作为教育专家，向一组新教师解释如何在教学评估中有效使用布卢姆分类法，详细说明各个层级的应用方法和实际案例。 |
| 描述学术诚信的重要性。 | 以大学教授的身份，向一群新生讲述学术诚信的重要性，解释违反学术诚信的后果，并提供保持学术诚信的具体建议。 |

c. 提供一些参考信息：对于一些涉及到专业知识的问题，在prompt里提供相关的专业参考资料能够增强模型。

对于该问题背景和上下文的理解，有助于减少错误或不准确信息（即“幻觉”）的生成，提高回答的质量和准确性。这种参考内容可能包括专业术语解析、行业标准、理论依据、实际案例或研究数据等。

| **无参考信息** | **有参考信息** |
| --- | --- |
| 解释如何实施项目式学习。 | 请根据《项目式学习：让学生成为学习的主人》一书的内容，解释如何在课堂上实施项目式学习。参考书籍章节如下：·章节1：项目式学习的基本概念；·章节2：设计有效的项目。 |
| 描述如何进行基于探究的科学教学。 | 请根据《探究式科学教学手册》中关于科学探究的原则和步骤，详细描述如何在课堂中实施基于探究的科学教学。参考手册内容如下：·手册部分：探究的五个基本步骤；·具体实例：应用探究式教学的案例分析。 |

#### **③利用分隔符** [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#_3%E5%88%A9%E7%94%A8%E5%88%86%E9%9A%94%E7%AC%A6)

分隔符的应用能有效地划分输入prompt的多个段落，这样做可以显著提升LLM对每一部分的识别和理解能力。

| **无分隔符** | **有分隔符** |
| --- | --- |
| 请分析以下学生反馈的情感倾向："这门课程非常有趣，但有时候作业太多了，让我感到压力很大。" | \`\`\`请分析以下学生反馈的情感倾向：\`\`\`\`\`\`学生反馈："这门课程非常有趣，但有时候作业太多了，让我感到压力很大。" |
| 请对以下教师的教学反思进行摘要，分析教学效果，并提取所有重要改进建议。反思内容：“在这学期的教学中，我尝试了新的教学方法，学生们的参与度有所提高，但在掌握基础知识方面还有待加强。未来我计划增加更多基础知识的练习，并定期进行小测验以检验学生的掌握情况。” | 请对提供的教学反思内容进行以下分析：\- 文本摘要：提供反思内容的简短摘要。\- 教学效果分析：评价教学方法的效果。\- 重要改进建议：列出反思中提到的所有改进建议。教学反思内容：“在这学期的教学中，我尝试了新的教学方法，学生们的参与度有所提高，但在掌握基础知识方面还有待加强。未来我计划增加更多基础知识的练习，并定期进行小测验以检验学生的掌握情况。” |

#### **④使用固定格式** [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#_4%E4%BD%BF%E7%94%A8%E5%9B%BA%E5%AE%9A%E6%A0%BC%E5%BC%8F)

如果你需要LLM生成或处理一系列相似的信息，提供一个明确的格式可以增加效率和一致性。例如：

```
请针对以下三门课程：数学，物理，化学，提供每门课程的最新教学资源。格式如下：课程 - 资源名称 - 主要内容。
```

#### ⑤ **提供示例** [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#_5%E6%8F%90%E4%BE%9B%E7%A4%BA%E4%BE%8B)

**a. 给出输出示例**：提供一个示例将有助于LLM理解期望的结果。特别是在有特定的输出格式要求时，给出示例有助于LLM遵循输出要求。

```
请根据以下格式给我推荐三本教育相关的书籍：
书名：[书名]
作者：[作者]
出版年份：[年份]
简短描述：[描述]
示例输出：
书名：《教育心理学》
作者：安妮塔·伍尔福克
出版年份：2010
简短描述：这本书详细介绍了教育心理学的基本理论和实际应用，为教师提供了有价值的教学指导。
```

**b. 给出任务样例**：该方法也称为小样本学习（few-shotlearning），是指在训练模型时仅使用极少量的样本数据进行学习和推理的任务。给出任务相关的样例可以带来如下优势：

- 直观展示：样例提供了一个直观的输出模板，帮助模型理解任务的具体要求。
- 减少误解：通过样例，模型可以更准确地把握用户的意图，减少对指令的误解。
- 提高一致性：样例确保了输出的一致性，使得模型生成的回答遵循相同的格式和风格。
- 简化指令：有时候，一个简单的样例比复杂的指令更容易被模型理解和执行。

| **无任务样例的prompt** | **有任务样例的prompt** |
| --- | --- |
| 请将以下学生反馈分类为积极、中性或消极。反馈内容：\[用户提供的反馈内容\] | 请根据以下样例将学生反馈分类为积极、中性或消极：样例1：反馈内容：这门课非常有趣，我学到了很多新知识。分类：积极 样例2：反馈内容：这门课有时很无聊，但内容还是很有用的。分类：中性 现在，请对以下学生反馈进行分类：反馈内容：\[用户提供的反馈内容\] |

#### ⑥ **让模型进行思考再回答** [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#_6%E8%AE%A9%E6%A8%A1%E5%9E%8B%E8%BF%9B%E8%A1%8C%E6%80%9D%E8%80%83%E5%86%8D%E5%9B%9E%E7%AD%94)

又名思维链（Chain-of-thought）prompting，目的是引导LLM逐步展示其解决问题或推理的逻辑步骤，而不仅仅是直接给出最终答案。通常的方法是：在提出问题后，在prompt的最开始或者结尾部分加上类似“让我们一步一步思考”或“逐步分析”("Let's think step by step.")的语句来引导模型先给出思考过程，再给出答案。

**以解决数学题为例**： 一个正方形和一个等边三角形的周长相等。如果正方形边长是4厘米，求等边三角形的边长。

**Prompt:**

```
一个正方形和一个等边三角形的周长相等。如果正方形的边长是4厘米，求等边三角形的边长。让我们一步一步思考。
```

**Response：**

```
首先，我们来计算正方形的周长。正方形的周长等于四条边之和，因为正方形的四条边都相等，所以：周长 = 4 * 边长 周长 = 4 * 4厘米周长 = 16厘米由于题目中说这个正方形和等边三角形的周长相等，所以等边三角形的周长也是16厘米。对于等边三角形来说，周长等于三条边之和，而等边三角形的三条边也都相等，所以：周长 = 3 * 边长 16厘米 = 3 * 边长现在我们解这个方程，得到等边三角形的边长：边长 = 周长 / 3 边长 = 16厘米 / 3边长 = 5.333...厘米所以，等边三角形的边长大约是5.33厘米（保留到小数点后两位）。
```

采用这种方法，大型语言模型（LLM）不仅提供了答案，还展示了其思考过程，使得最终的解答更加清晰和易于理解。在处理那些需要分步解答或需要明确展示思考路径的复杂问题时，推荐采用思维链（Chain of Thought, CoT）提示法。适用的常见场景包括但不限于以下几个方面：

1. 数学题目解答：比如，解决代数、几何、统计学中的难题，模型需要逐一展示每一步的计算过程和思考逻辑。
2. 逻辑推理：包括演绎推理和归纳推理，模型需要逐步展示得出结论的推导过程。
3. 复杂问答系统：处理那些需要深入理解文本内容并进行综合分析才能回答的问题，例如因果推理、情境分析等。
4. 编程问题解答：在缺乏代码执行环境的情况下，让模型使用自然语言来描述解决编程问题的具体步骤。
5. 教育辅导与学习支持：模拟教学过程，逐步阐释解题方法，帮助学生掌握问题背后的逻辑。
6. 专业领域决策支持：在法律、医学、工程等专业领域，模型通过逐步分析案例背景、相关法规或专业知识来提供决策建议。
7. 多步骤决策游戏策略：在棋类游戏或其他需要多步规划的情境中，利用CoT技术展示每一步决策的依据和整体战略设计。

### **组合使用多种prompting技巧** [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#%E7%BB%84%E5%90%88%E4%BD%BF%E7%94%A8%E5%A4%9A%E7%A7%8Dprompting%E6%8A%80%E5%B7%A7)

以上多种写prompt的技巧可以组合使用。下面是一个组合使用 **背景信息** \+ **引导语或指示语** \+ **输出格式指示** \+ **样例输出** 的例子：

## 例子 [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#%E4%BE%8B%E5%AD%90)

**Prompt**

```
请以教育专家的身份，总结出三种提高课堂互动的方法。请按照以下格式提供建议：

- 方法名称：[方法名称]
- 具体步骤：[具体步骤]
- 应用实例：[应用实例]

示例：

- 方法名称：小组讨论
- 具体步骤：
  1. 将学生分成小组，每组4-5人。
  2. 提出一个讨论问题或主题。
  3. 让每个小组讨论并记录他们的观点。
  4. 每个小组派代表在全班分享讨论结果。
- 应用实例：在历史课上，教师让学生讨论某一历史事件的原因和影响，每个小组分享他们的见解。

现在，请你总结出三种提高课堂互动的方法。
```

**Response**

```
- 方法名称：角色扮演
- 具体步骤：
  1. 为学生分配不同的角色，与课程主题相关。
  2. 提供角色背景和情境。
  3. 让学生在角色扮演中互动，讨论或解决问题。
  4. 进行角色扮演后的反思和讨论。
- 应用实例：在英语课上，教师让学生扮演不同职业的人物，进行模拟面试，增强口语表达能力。
- 方法名称：即时反馈
- 具体步骤：
  1. 使用学生响应系统（如投票器或在线问卷）。
  2. 在课堂上提出问题，学生即时作答。
  3. 实时展示统计结果并进行讨论。
  4. 根据反馈调整教学进度和内容。
- 应用实例：在数学课上，教师使用在线投票系统，让学生即时回答问题，了解学生对新概念的掌握情况。
- 方法名称：游戏化教学
- 具体步骤：
  1. 设计与课程内容相关的游戏或竞赛。
  2. 设定游戏规则和奖励机制。
  3. 组织学生参与游戏，在竞争中学习。
  4. 总结游戏结果，回顾知识点。
- 应用实例：在生物课上，教师设计了一个“生物知识竞赛”，通过问答和小游戏，复习重要的生物学概念和术语。
```

通过这种方式，LLM能够提供更具体、详细和有用的建议，帮助教师有效地提高课堂互动。

## 其他注意点 [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#%E5%85%B6%E4%BB%96%E6%B3%A8%E6%84%8F%E7%82%B9)

在进行以上 prompt 工程时，为了寻找比较满意效果的 prompt ，还可以注意以下几点：

#### 1\. 多提供关键词 [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#_1-%E5%A4%9A%E6%8F%90%E4%BE%9B%E5%85%B3%E9%94%AE%E8%AF%8D)

关键词能够和指令提示相结合，以创建更具体和有针对性的生成文本。

**示例：**

**Prompt：**

```
你是一位数学老师，请根据我提供的主题，为六年级学生设计一个与主题相关的数学问题，要求包含题干、步骤和答案。题干和步骤应满足以下四个要求：

1. 题目难度适中，符合六年级学生的认知水平；
2. 题干必须清晰简洁；
3. 步骤详细，有助于学生理解解题思路；
4. 答案准确无误。

接下来我将提供给你我的主题：分数加减法。
```

**Response：**

```
题干：某班同学在一次数学竞赛中，有5名同学的得分分别为4/5、3/4、7/8、2/3和5/6，求这5名同学的总得分。 步骤：

1. 将所有分数化为相同的分母；
2. 将分数相加；
3. 将结果化简。 答案：471/120
```

#### 2\. 把事情说详细 [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#_2-%E6%8A%8A%E4%BA%8B%E6%83%85%E8%AF%B4%E8%AF%A6%E7%BB%86)

在工作中，往往也是上级安排的命令和要求越详细，我们完成的工作才能越加符合他们的预期。在训练大模型时亦是如此，将要点都详细的告诉大模型往往效果会更好。

参照上一个 prompt 中，我们给出了非常详细且严格的题目格式要求，从而限制大模型的输出内容。

#### 3\. 指定输出长度 [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#_3-%E6%8C%87%E5%AE%9A%E8%BE%93%E5%87%BA%E9%95%BF%E5%BA%A6)

在生成文本时，若我们需要限定字数，此时需要告诉大模型相关信息，避免生成字数过少或过多。

**示例：**

**Prompt：**

```
请用200字左右总结以下内容：学生在课堂上的表现是老师评价学生的重要依据之一。课堂表现不仅反映学生的学习态度和能力，还能揭示他们的兴趣和特长。通过观察学生在课堂上的表现，老师可以更好地了解学生的需求，从而有针对性地进行教学调整。同时，积极的课堂表现有助于学生建立自信，提高学习效果。因此，课堂表现是学生综合素质评价的重要方面。
```

**Response：**

```
学生的课堂表现是老师评价的重要依据，反映了学生的学习态度、能力、兴趣和特长。通过观察课堂表现，老师可以了解学生需求，进行教学调整，帮助学生建立自信，提高学习效果。因此，课堂表现对学生综合素质评价至关重要。
```

#### 4\. 长文本用总结 [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#_4-%E9%95%BF%E6%96%87%E6%9C%AC%E7%94%A8%E6%80%BB%E7%BB%93)

在我们输入一段很长文本给大模型时，由于字数限制大模型可能无法全部读取，此时我们能将全篇文本进行分段，将前面内容让大模型总结从而将总结的内容衔接后面的内容，达到层层递进理解的效果。

**示例：**

假设我们有一篇长篇教育研究论文，总字数超过了大模型一次性处理的限制。我们可以将论文分成若干段落，每次输入一个段落给大模型。比如：

**Prompt：**

```
请帮我总结三引号中的内容，要求简要概括要点。'''在一个小学生课堂上，老师通过游戏方式教授数学知识，学生们表现出极大的兴趣和积极性。'''
```

**Response：**

```
老师通过游戏方式教授数学，小学生们表现出极大的兴趣和积极性。
```

接着，我们将上一段的总结和下一段输入给大模型：

**Prompt：**

```
请帮我总结三引号中的内容，要求简要概括要点。'''老师通过游戏方式教授数学，小学生们表现出极大的兴趣和积极性。这样的教学方式不仅激发了学生的学习热情，还提高了他们的数学成绩。'''
```

**Response：**

```
老师通过游戏教学方式激发了学生的学习热情，提高了他们的数学成绩。
```

这样逐步输入并总结，大模型能够逐渐理解并保持对整个长文本的准确理解。

#### 5.COSTAR框架 [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#_5-costar%E6%A1%86%E6%9E%B6)

CO-STAR 框架，由新加坡政府科技局数据科学与 AI 团队创立，是一个实用的提示构建工具，他的结构如下所示：

- (C) 上下文：为任务提供背景信息 通过为大语言模型（LLM）提供详细的背景信息，可以帮助它精确理解讨论的具体场景，确保提供的反馈具有相关性。
- (O) 目标：明确你要求大语言模型完成的任务 清晰地界定任务目标，可以使大语言模型更专注地调整其回应，以实现这一具体目标。
- (S) 风格：明确你期望的写作风格 你可以指定一个特定的著名人物或某个行业专家的写作风格，如商业分析师或 CEO。这将指导大语言模型以一种符合你需求的方式和词汇选择进行回应。
- (T) 语气：设置回应的情感调 设定适当的语气，确保大语言模型的回应能够与预期的情感或情绪背景相协调。可能的语气包括正式、幽默、富有同情心等。
- (A) 受众：识别目标受众 针对特定受众定制大语言模型的回应，无论是领域内的专家、初学者还是儿童，都能确保内容在特定上下文中适当且容易理解。
- (R) 响应：规定输出的格式 确定输出格式是为了确保大语言模型按照你的具体需求进行输出，便于执行下游任务。常见的格式包括列表、JSON 格式的数据、专业报告等。对于大部分需要程序化处理大语言模型输出的应用来说，JSON 格式是理想的选择。

以下是一个示例

```
标题：【小龙虾节盛宴即将开启，邀您共享美食狂欢！】
(C) 上下文：随着夏季的到来，为了丰富大家的餐饮生活，我们的校园食堂特别策划了一场别开生面的小龙虾节。此次活动旨在为师生们提供一个品尝美味、放松心情的好去处，同时也是庆祝学期过半，给大家带来一次味蕾的享受和精神的放松。
(O) 目标：本文旨在宣传食堂小龙虾节的活动详情，包括活动时间、地点、特色菜品以及参与方式等，吸引广大师生前来参加，体验这一独特的美食盛宴。
(S) 风格：文章采用轻松活泼的风格撰写，以吸引年轻群体的注意力，同时穿插一些趣味元素和小龙虾小知识，增加阅读趣味性。
(T) 语气：整个文章保持积极向上、诱人食欲的语气，通过形象生动的描写和热情洋溢的文字，传递出一种欢乐和期待的氛围。
(A) 受众：主要面向学校师生，同时也欢迎校外美食爱好者参与其中，特别是那些对小龙虾情有独钟的朋友们。
(R) 响应：文章结构清晰，先介绍活动背景和目的，再详细介绍活动内容和亮点，最后以参与方式和期待语作为总结。
```

#### 6\. 图像生成模型 Prompt 工程 [​](https://developer.ecnu.edu.cn/vitepress/llm/prompts.html\#_6-%E5%9B%BE%E5%83%8F%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B-prompt-%E5%B7%A5%E7%A8%8B)

**使用结构化的提示语**：在使用图像生成工具时，应采用精确、具体的视觉描述而非抽象概念。明确、清晰的结构化提示词可以帮助文生图应用创造出更高质量的图像。

- 主体: 人、动物、建筑、课堂、实验等
- 媒介: 照片、绘画、插图、雕塑、涂鸦、图表、报告等
- 环境: 竹林、荷塘、沙漠、月球上、水下、实验室、操场、图书馆等
- 光线: 自然光、体积光、霓虹灯、工作室灯等
- 颜色: 单色、复色、彩虹色、柔和色等
- 情绪 : 开心、生气、悲伤、惊讶、兴奋、专注、好奇、困惑等
- 活动：奔跑、翻滚、讨论、实验、阅读等
- 构图/角度: 肖像、特写、侧脸图、航拍图等


## 跨源矛盾检测结论

### 检测范围
- 已精读来源数量：10 个
- 检测对象：核心数字、日期、功能描述、因果判断、市场/公司事实
- 检测时间：2026-06-21

### 检测结果
结论：待 Agent 基于精读全文检测。最终报告必须替换为以下二选一：

结论：未检测到跨源矛盾，可进入综合阶段。

或：

结论：检测到 X 处跨源矛盾，综合输出时必须保留双方表述，不得静默合并。

### 矛盾项 1：[简短标题]
- 矛盾描述：[具体什么矛盾]
- 来源 A：[URL]
  - 原文引用：“……”
  - 来源等级：A / B / C / D
  - 发布时间 / 数据日期：YYYY-MM-DD
- 来源 B：[URL]
  - 原文引用：“……”
  - 来源等级：A / B / C / D
  - 发布时间 / 数据日期：YYYY-MM-DD
- 初步判断：
  - 倾向：[来源 A / 来源 B / 暂不倾向]
  - 理由：[官方一手来源优先 / 数据更新 / 方法更透明 / 与中文本地来源一致]
- 综合输出要求：
  - 必须写成“来源 A 说 X，来源 B 说 Y，建议人工核实”
  - 禁止取平均值、合并成第三种说法、只保留其中一方
## 矛盾与不确定性

- 脚本不会自动裁决跨源矛盾。Agent 编译最终报告时，必须比较数字、日期、因果关系和产品能力声明。
- 本证据包中没有 URL 支撑的说法都应视为未验证，不得作为事实写入最终调研报告或 Wiki。

## 工具运行记录

- 候选信源超过 15 个，已使用 Jina Reranker 精选。

## 入库提醒

只有在 Agent 已完成新的中文综合 raw 报告并删除本证据包后，才能询问用户是否入库。若用户确认，按完整 `SCHEMA.md` Ingest 工作流执行。
