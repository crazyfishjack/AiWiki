---
title: "调研证据包：Qwen Kimi GPT GLM Claude DeepSeek 大模型能力对比 SWE-bench HumanEval LiveCodeBench 代码能力跑分 2026"
source-type: article
generated: 2026-06-20
generated-by: wiki-research-skill
research-mode: standard
---

# 调研证据包：Qwen Kimi GPT GLM Claude DeepSeek 大模型能力对比 SWE-bench HumanEval LiveCodeBench 代码能力跑分 2026

## 调研问题

Qwen Kimi GPT GLM Claude DeepSeek 大模型能力对比 SWE-bench HumanEval LiveCodeBench 代码能力跑分 2026

## 摘要

本文档是四工具检索生成的证据包草稿，不是最终调研报告。Agent 必须先阅读本证据包，执行下方"AI 综合指令"，生成新的中文综合 raw 报告，然后询问用户是否入库。本证据包保留不删除。

- 发现候选信源：47
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
| exa | 1.00 | Qwen3-Coder-Next Technical Report | https://www.arxiv.org/pdf/2603.00729 |
| exa | 1.00 | React-ing to Grace Hopper 200 Five Open-Weights Coding Models, One React Native App, One GH200, One Weekend or: why SWE-Bench rankings mispredicted which model actually shipped | https://arxiv.org/html/2604.17187v1 |
| exa | 1.00 | Kimi K2.5: Visual Agentic Intelligence | https://arxiv.org/html/2602.02276 |
| exa | 1.00 | Consistency Amplifies: How Behavioral Variance Shapes Agent Accuracy | https://www.arxiv.org/pdf/2603.25764 |
| exa | 1.00 | Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks | https://arxiv.org/html/2606.12344v1 |
| exa | 1.00 | SWE-Compass: Towards Unified Evaluation of Agentic Coding Abilities for Large Language Models | https://arxiv.org/html/2511.05459v3 |
| exa | 1.00 | An Execution-Verified Multi-Language Benchmark for Code Semantic Reasoning | https://arxiv.org/html/2605.11006v1 |
| exa | 1.00 | Qwen3-Coder-Next Technical Report | https://arxiv.org/html/2603.00729v1 |
| exa | 1.00 | Qwen3.5-Omni Technical Report | https://arxiv.org/pdf/2604.15804 |
| exa | 1.00 | LiveOIBench: Can Large Language Models Outperform Human Contestants in Informatics Olympiads? | https://arxiv.org/pdf/2510.09595 |
| exa | 1.00 | LiveCodeBench Pro: How Do Olympiad Medalists Judge LLMs in Competitive Programming? | https://openreview.net/pdf?id=U5RIVFtat1 |
| exa | 1.00 | DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence | https://arxiv.org/pdf/2406.11931v1 |
| exa | 1.00 | GLM-5: from Vibe Coding to Agentic Engineering | https://arxiv.org/pdf/2602.15763v1 |
| exa | 1.00 | Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents | https://arxiv.org/html/2509.23045v2 |
| exa | 1.00 | LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code | https://arxiv.org/html/2403.07974 |
| tavily | 0.97 | 大模型代码编程能力评测排行榜 | https://www.datalearner.com/leaderboards/category/code |
| tavily | 0.97 | 2026 AI编程能力评测：八大模型全面对比 - UniFuncs | https://unifuncs.com/s/RYSb15zp |
| tavily | 0.97 | Best LLMs for Coding in 2026: SWE-bench, HumanEval ... - Onyx AI | https://onyx.app/insights/best-llms-for-coding-2026 |
| tavily | 0.96 | 2026 年最佳开源编程大模型：开发者指南 | https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm |
| tavily | 0.96 | 国产模型与海外模型的Coding 能力对比：2026 年程序员该如何选择 | https://segmentfault.com/a/1190000047817400 |
| tavily | 0.96 | 国产三大模型深度对比：性能与性价比深度解析，2026年4月21日 | https://gitcode.csdn.net/69e7629e54b52172bc6b4930.html |
| tavily | 0.96 | SWE-bench Verified - Vals AI | https://vals.ai/benchmarks/swebench |
| tavily | 0.95 | DeepSeek V4 RAG Benchmark with Milvus vs GPT-5.5 and Qwen  - Milvus Blog | https://milvus.io/zh/blog/deepseek-v4-vs-gpt-55-vs-qwen36-which-model-should-you-use.md |
| tavily | 0.95 | Big Tech’s AI Datacenter Investments Might Be In Big Trouble - Forbes | https://www.forbes.com/sites/amirhusain/2026/06/17/big-techs-ai-datacenter-investments-might-be-in-big-trouble/ |
| tavily | 0.95 | Top 7 LLMs for Coding in 2026 (SWE-bench, LiveCodeBench, Terminal-Bench) - Tech Jacks Solutions | https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding |
| tavily | 0.95 | 2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云 | https://cloud.tencent.com/developer/article/2670420 |
| tavily | 0.95 | 2026 AI大模型全景对比\|GPT vs Claude vs Gemini vs DeepSeek,到底 ... | https://k.sina.com.cn/article_7857201856_1d45362c001906zvc0.html?from=tech |
| tavily | 0.94 | AI 大模型对比 2026 年中版：blog080 写完两个多月，模型层换了一轮 \| 陈广亮的技术博客 | https://chenguangliang.com/posts/blog166_ai-models-mid-2026-update |
| tavily | 0.94 | 国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏 | https://zhuanlan.zhihu.com/p/670574382 |
| tavily | 0.94 | 7 Best LLMs for Coding in April 2026 \| Blaxel Blog | https://blaxel.ai/blog/best-llm-for-coding |

## 信源质量门控记录

### 门控规则
- Tavily score < 0.4：剔除
- 已知低质域名：剔除
- 重复 URL：合并保留最高分结果
- Exa 学术/语义结果：默认保留，但进入来源等级评估
- C/D 级来源不得作为唯一结论依据
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`

### 保留信源
1. [Qwen3-Coder-Next Technical Report](https://www.arxiv.org/pdf/2603.00729)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
2. [React-ing to Grace Hopper 200 Five Open-Weights Coding Models, One React Native App, One GH200, One Weekend or: why SWE-Bench rankings mispredicted which model actually shipped](https://arxiv.org/html/2604.17187v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
3. [Kimi K2.5: Visual Agentic Intelligence](https://arxiv.org/html/2602.02276)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
4. [Consistency Amplifies: How Behavioral Variance Shapes Agent Accuracy](https://www.arxiv.org/pdf/2603.25764)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
5. [Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks](https://arxiv.org/html/2606.12344v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
6. [SWE-Compass: Towards Unified Evaluation of Agentic Coding Abilities for Large Language Models](https://arxiv.org/html/2511.05459v3)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
7. [An Execution-Verified Multi-Language Benchmark for Code Semantic Reasoning](https://arxiv.org/html/2605.11006v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
8. [Qwen3-Coder-Next Technical Report](https://arxiv.org/html/2603.00729v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
9. [Qwen3.5-Omni Technical Report](https://arxiv.org/pdf/2604.15804)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
10. [LiveOIBench: Can Large Language Models Outperform Human Contestants in Informatics Olympiads?](https://arxiv.org/pdf/2510.09595)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
11. [LiveCodeBench Pro: How Do Olympiad Medalists Judge LLMs in Competitive Programming?](https://openreview.net/pdf?id=U5RIVFtat1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
12. [DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence](https://arxiv.org/pdf/2406.11931v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
13. [GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/pdf/2602.15763v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
14. [Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents](https://arxiv.org/html/2509.23045v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
15. [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://arxiv.org/html/2403.07974)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
16. [大模型代码编程能力评测排行榜](https://www.datalearner.com/leaderboards/category/code)
   - 工具：tavily
   - 分数：0.97
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
17. [2026 AI编程能力评测：八大模型全面对比 - UniFuncs](https://unifuncs.com/s/RYSb15zp)
   - 工具：tavily
   - 分数：0.97
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
18. [Best LLMs for Coding in 2026: SWE-bench, HumanEval ... - Onyx AI](https://onyx.app/insights/best-llms-for-coding-2026)
   - 工具：tavily
   - 分数：0.97
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
19. [2026 年最佳开源编程大模型：开发者指南](https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm)
   - 工具：tavily
   - 分数：0.96
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 技术文档
   - 后续处理：进入精读
20. [国产模型与海外模型的Coding 能力对比：2026 年程序员该如何选择](https://segmentfault.com/a/1190000047817400)
   - 工具：tavily
   - 分数：0.96
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
21. [国产三大模型深度对比：性能与性价比深度解析，2026年4月21日](https://gitcode.csdn.net/69e7629e54b52172bc6b4930.html)
   - 工具：tavily
   - 分数：0.96
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
22. [SWE-bench Verified - Vals AI](https://vals.ai/benchmarks/swebench)
   - 工具：tavily
   - 分数：0.96
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
23. [DeepSeek V4 RAG Benchmark with Milvus vs GPT-5.5 and Qwen
 - Milvus Blog](https://milvus.io/zh/blog/deepseek-v4-vs-gpt-55-vs-qwen36-which-model-should-you-use.md)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
24. [Big Tech’s AI Datacenter Investments Might Be In Big Trouble - Forbes](https://www.forbes.com/sites/amirhusain/2026/06/17/big-techs-ai-datacenter-investments-might-be-in-big-trouble/)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
25. [Top 7 LLMs for Coding in 2026 (SWE-bench, LiveCodeBench, Terminal-Bench) - Tech Jacks Solutions](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
26. [2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云](https://cloud.tencent.com/developer/article/2670420)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
27. [2026 AI大模型全景对比|GPT vs Claude vs Gemini vs DeepSeek,到底 ...](https://k.sina.com.cn/article_7857201856_1d45362c001906zvc0.html?from=tech)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
28. [AI 大模型对比 2026 年中版：blog080 写完两个多月，模型层换了一轮 | 陈广亮的技术博客](https://chenguangliang.com/posts/blog166_ai-models-mid-2026-update)
   - 工具：tavily
   - 分数：0.94
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
29. [国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏](https://zhuanlan.zhihu.com/p/670574382)
   - 工具：tavily
   - 分数：0.94
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
30. [7 Best LLMs for Coding in April 2026 | Blaxel Blog](https://blaxel.ai/blog/best-llm-for-coding)
   - 工具：tavily
   - 分数：0.94
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
31. [2026年全网最全大模型API横评：Claude / GPT / Gemini 等8 大厂商 ...](https://segmentfault.com/a/1190000047676047)
   - 工具：tavily
   - 分数：0.94
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
32. [BRIDGE: benchmarking large language models for understanding real-world clinical practice texts - Nature](https://www.nature.com/articles/s41551-026-01719-2)
   - 工具：tavily
   - 分数：0.94
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
33. [Breakdown: Kimi K2, DeepSeek-R1, Qwen3 (+Coder), and GLM-4.5](https://www.turingpost.com/p/chinesemodels)
   - 工具：tavily
   - 分数：0.94
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
34. [SWE-bench Leaderboards](https://www.swebench.com)
   - 工具：tavily
   - 分数：0.94
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
35. [New AI optimization framework beats Claude Code and Codex by 2.5x on the same compute budget - VentureBeat](https://venturebeat.com/orchestration/new-ai-optimization-framework-beats-claude-code-and-codex-by-2-5x-on-the-same-compute-budget)
   - 工具：tavily
   - 分数：0.94
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
36. [Best LLMs for coding: 2026 roundup - Fireworks AI](https://fireworks.ai/blog/best-llms-for-coding)
   - 工具：tavily
   - 分数：0.94
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
37. [国产大模型编码能力实测(GLM 5.1、Kimi K2.6、Mimo v2.5 Pro 和 DeepSeek V4 Pro) | blog-website](https://owent.net/2026/2607.html)
   - 工具：tavily
   - 分数：0.93
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
38. [国产开源大模型2026 全景：Qwen3.6 / GLM-5.1 / Kimi K2.6 ... - OfoxAI](https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026)
   - 工具：tavily
   - 分数：0.93
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
39. [2026年6月主流大模型Coding能力深度对比：GPT ... - AtomGit开源社区](https://gitcode.csdn.net/6a22fa2710ee7a33f278289f.html)
   - 工具：tavily
   - 分数：0.93
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
40. [大模型之家2026年5月热力榜：当“能干多久”取代“能跑多高” - 澎湃新闻](https://m.thepaper.cn/newsDetail_forward_33291314)
   - 工具：tavily
   - 分数：0.93
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
41. [Claude Makes More Money Per User Than Market Leader ChatGPT Report Finds - Forbes](https://www.forbes.com/sites/siladityaray/2026/06/16/claude-makes-more-money-per-user-than-market-leader-chatgpt-report-finds/)
   - 工具：tavily
   - 分数：0.92
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
42. [China isn’t trying to beat the U.S. at AI — it’s playing a completely different game - fortune.com](https://fortune.com/2026/06/16/china-ai-deepseek-open-source-efficiency-global-expansion-strategy/)
   - 工具：tavily
   - 分数：0.92
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
43. [ASD draws a hard line on developers lacking security skills - iTnews](https://www.itnews.com.au/news/asd-draws-a-hard-line-on-developers-lacking-security-skills-626728?utm_source=feed&utm_medium=rss&utm_campaign=iTnews+Technology+feed)
   - 工具：tavily
   - 分数：0.90
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
44. [Study finds LLMs reproduce antisemitic stereotypes - Let's Data Science](https://letsdatascience.com/news/study-finds-llms-reproduce-antisemitic-stereotypes-07bad08c)
   - 工具：tavily
   - 分数：0.88
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
45. [New OpenAI Method Forecasts AI Risks Before Deployment - BankInfoSecurity](https://www.bankinfosecurity.com/new-openai-method-forecasts-ai-risks-before-deployment-a-32021)
   - 工具：tavily
   - 分数：0.85
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
46. [An optimization-driven hierarchical deep learning approach using the Gray Langurs algorithm for data-driven seismic activity prediction - Nature](https://www.nature.com/articles/s41598-026-56169-2)
   - 工具：tavily
   - 分数：0.83
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
47. [NVIDIA GB300 Dominates Agentic AI Workloads With 20x Performance Leap Over Hopper As Rubin Nears Launch - Wccftech](https://wccftech.com/nvidia-gb300-dominates-agentic-ai-workloads-20x-performance-leap-over-hopper/)
   - 工具：tavily
   - 分数：0.83
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读

### 剔除信源
1. [大模型代码编程能力评测排行榜](https://www.datalearner.com/leaderboards/category/code)
   - 工具：tavily
   - 分数：0.96
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
2. [2026 AI编程能力评测：八大模型全面对比 - UniFuncs](https://unifuncs.com/s/RYSb15zp)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
3. [2026 年最佳开源编程大模型：开发者指南](https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
4. [国产三大模型深度对比：性能与性价比深度解析，2026年4月21日](https://gitcode.csdn.net/69e7629e54b52172bc6b4930.html)
   - 工具：tavily
   - 分数：0.94
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
5. [国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏](https://zhuanlan.zhihu.com/p/670574382)
   - 工具：tavily
   - 分数：0.92
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
6. [2026 年最佳开源编程大模型：开发者指南](https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
7. [国产模型与海外模型的Coding 能力对比：2026 年程序员该如何选择](https://segmentfault.com/a/1190000047817400)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
8. [国产三大模型深度对比：性能与性价比深度解析，2026年4月21日](https://gitcode.csdn.net/69e7629e54b52172bc6b4930.html)
   - 工具：tavily
   - 分数：0.93
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
9. [SWE-bench Leaderboards](https://www.swebench.com)
   - 工具：tavily
   - 分数：0.93
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
10. [大模型代码编程能力评测排行榜](https://www.datalearner.com/leaderboards/category/code)
   - 工具：tavily
   - 分数：0.96
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
11. [2026 AI编程能力评测：八大模型全面对比 - UniFuncs](https://unifuncs.com/s/RYSb15zp)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
12. [2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云](https://cloud.tencent.com/developer/article/2670420)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
13. [国产模型与海外模型的Coding 能力对比：2026 年程序员该如何选择](https://segmentfault.com/a/1190000047817400)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
14. [2026 年最佳开源编程大模型：开发者指南](https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm)
   - 工具：tavily
   - 分数：0.95
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
15. [2026 AI大模型全景对比|GPT vs Claude vs Gemini vs DeepSeek,到底 ...](https://k.sina.com.cn/article_7857201856_1d45362c001906zvc0.html?from=tech)
   - 工具：tavily
   - 分数：0.94
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
16. [国产三大模型深度对比：性能与性价比深度解析，2026年4月21日](https://gitcode.csdn.net/69e7629e54b52172bc6b4930.html)
   - 工具：tavily
   - 分数：0.94
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
17. [大模型之家2026年5月热力榜：当“能干多久”取代“能跑多高” - 澎湃新闻](https://m.thepaper.cn/newsDetail_forward_33291314)
   - 工具：tavily
   - 分数：0.92
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
18. [国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏](https://zhuanlan.zhihu.com/p/670574382)
   - 工具：tavily
   - 分数：0.92
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果

## 完整精读结果

### 来源 1: 大模型代码编程能力评测排行榜

- URL: https://www.datalearner.com/leaderboards/category/code
- 精读方法：firecrawl-scrape

截至 2026年6月，本页覆盖 SWE-bench Verified, LiveCodeBench, SWE-Bench Pro - Public, SWE-bench Multilingual 等评测基准，聚焦 **大模型代码编程能力评测排行榜** 方向的模型对比。

点击模型名称可进入详情页查看上下文长度、许可方式与 API 价格。数据口径说明见 [数据方法论](https://www.datalearner.com/about/data-methodology)。

## 代码能力参考综合排名

目前没有一个被普遍认可的代码能力综合排行榜。SWE-bench、HumanEval 等静态基准可以衡量特定技能，但容易被针对性优化（"刷榜"）。为此我们选取了两个切入角度不同的人类偏好参考榜单并列展示：LMArena Coding Arena 通过匿名盲测评测通用编程能力（调试、算法实现、代码生成等）；DesignArena Code Category 专注评测具有视觉呈现效果的前端代码生成（网站、UI 组件、游戏等），两者方法论相同但考察场景各异，结合参考效果最佳。

### LMArena Coding Arena

[完整排名](https://www.datalearner.com/leaderboards/external/text-generation-coding)

基于真实开发者提交的通用编程任务（调试、算法、代码生成）进行匿名 A/B 盲测投票，Elo 算法动态排名。

数据更新于2026-06-16

#模型Elo

1

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Claude Fable 5](https://www.datalearner.com/ai-models/pretrained-models/claude-fable-5) Anthropic

1563

2

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Opus 4.7 (thinking)](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-7) Anthropic

1553

3

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Claude Opus 4.6 (thinking)](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-6) Anthropic

1551

4

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Opus 4.7](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-7) Anthropic

1549

5

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Claude Opus 4.6](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-6) Anthropic

1548

6

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Claude Opus 4.8 (thinking)](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-8) Anthropic

1541

7

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Claude Opus 4.8](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-8) Anthropic

1540

8

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Claude Opus 4 (thinking-32k)](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4) Anthropic

1530

9

智

[GLM 5.1](https://www.datalearner.com/ai-models/pretrained-models/glm-5-1) 智谱AI

1529

10

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Claude Sonnet 4.6](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4-6) Anthropic

1527

来源： [LMArena](https://arena.ai/leaderboard/coding)

### DesignArena Code Category

[完整排名](https://www.datalearner.com/leaderboards/external/arcada-code)

基于 Arcada Labs 平台，对视觉前端代码任务（网站、UI 组件、游戏、数据可视化等）进行匿名投票，Bradley-Terry 模型动态排名。

数据更新于2026-06-19

#模型Elo

1

智

[GLM-5.2](https://www.datalearner.com/ai-models/pretrained-models/glm-5-2) 智谱AI

1360

2

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Claude Fable 5](https://www.datalearner.com/ai-models/pretrained-models/claude-fable-5) Anthropic

1350

3

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Claude Opus 4.6](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-6) Anthropic

1341

4

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Opus 4.7 (thinking)](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-7) Anthropic

1337

5

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Claude Opus 4.6 (thinking)](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-6) Anthropic

1336

6

智

[GLM 5.1](https://www.datalearner.com/ai-models/pretrained-models/glm-5-1) 智谱AI

1332

7

![Moonshot AI](https://www.datalearner.com/resources/ai-org-logo/9898984c-ed92-456e-9f5c-6f127142ba87.jpeg)

[Kimi K2.6](https://www.datalearner.com/ai-models/pretrained-models/kimi-k2-6) Moonshot AI

1328

8

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Opus 4.7](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-7) Anthropic

1325

9

![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)

[Claude Sonnet 4.6](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4-6) Anthropic

1325

10

智

[GLM-5-Turbo](https://www.datalearner.com/ai-models/pretrained-models/glm-5-turbo) 智谱AI

1322

来源： [DesignArena](https://www.designarena.ai/leaderboard/code)

基准评测

[SWE-bench Verified](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified) [LiveCodeBench](https://www.datalearner.com/leaderboards/category/code?benchmark=LiveCodeBench) [SWE-Bench Pro - Public](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-Bench+Pro+-+Public) [SWE-bench Multilingual](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Multilingual)

[更多评测](https://www.datalearner.com/benchmarks)

参数规模: [全部](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified) [3B及以下](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&modelSize=3b) [7B](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&modelSize=7b) [13B](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&modelSize=13b) [34B](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&modelSize=34b) [65B](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&modelSize=65b) [100B及以上](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&modelSize=100b)

模型类型: [全部](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified) [推理大模型](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&modelType=reasoningLLM) [基座大模型](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&modelType=foundationLLM) [指令优化/聊天优化大模型](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&modelType=chatLLM) [编程大模型](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&modelType=coderLLM)

开源： [全部](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified) [开源](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&licenseType=open) [闭源](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&licenseType=closed)

来源： [全部](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified) [国产模型](https://www.datalearner.com/leaderboards/category/code?benchmark=SWE-bench+Verified&isChina=1)

模型发布时间截止:

最新

[当前 SOTA\\
\\
![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)\\
\\
Claude Fable 5\\
\\
Anthropic\\
\\
95.00SWE-bench Verified\\
\\
查看详情](https://www.datalearner.com/ai-models/pretrained-models/claude-fable-5) [最佳开源\\
\\
![DeepSeek-AI](https://www.datalearner.com/resources/ai-org-logo/7e535e25-299b-437c-8412-baf2988b671d.jpeg)\\
\\
DeepSeek-V4-Pro\\
\\
DeepSeek-AI\\
\\
80.60SWE-bench Verified−14.40\\
\\
查看详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro) [最佳国产\\
\\
![DeepSeek-AI](https://www.datalearner.com/resources/ai-org-logo/7e535e25-299b-437c-8412-baf2988b671d.jpeg)\\
\\
DeepSeek-V4-Pro\\
\\
DeepSeek-AI\\
\\
80.60SWE-bench Verified−14.40\\
\\
查看详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro)

### 大模型性能评测结果

数据来源：DataLearnerAI

点击任意行查看模型详情；勾选左侧可对比最多 4 个模型。

|  | 排名 | 模型 | SWE-benchVerified [查看 SWE-bench Verified 评测详情](https://www.datalearner.com/benchmarks/SWE-bench-Verified "查看 SWE-bench Verified 评测详情") | LiveCodeBench [查看 LiveCodeBench 评测详情](https://www.datalearner.com/benchmarks/LiveCodeBench "查看 LiveCodeBench 评测详情") | SWE-Bench ProPublic [查看 SWE-Bench Pro - Public 评测详情](https://www.datalearner.com/benchmarks/SWE-Bench-Pro---Public "查看 SWE-Bench Pro - Public 评测详情") | SWE-bench Multilingual [查看 SWE-bench Multilingual 评测详情](https://www.datalearner.com/benchmarks/SWE-bench-Multilingual "查看 SWE-bench Multilingual 评测详情") | 开源情况 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Claude Fable 5](https://www.datalearner.com/ai-models/pretrained-models/claude-fable-5) <br>深度思考模式工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 95.00 | — | 80.30 | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-fable-5 "查看 Claude Fable 5 详情") |
|  |  | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Claude Fable 5](https://www.datalearner.com/ai-models/pretrained-models/claude-fable-5) <br>开启思考工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 95.00 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-fable-5 "查看 Claude Fable 5 详情") |
|  |  | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Claude Mythos Preview](https://www.datalearner.com/ai-models/pretrained-models/claude-mythos-preview) <br>扩展思考工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 93.90 | — | 77.80 | 87.30 | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-mythos-preview "查看 Claude Mythos Preview 详情") |
|  | 4 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Claude Opus 4.8](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-8) <br>扩展思考工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 88.60 | — | 69.20 | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-8 "查看 Claude Opus 4.8 详情") |
|  | 5 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Opus 4.7](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-7) <br>扩展思考工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 87.60 | — | 64.30 | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-7 "查看 Opus 4.7 详情") |
|  | 6 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Claude Sonnet 4.5](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4_5) <br>并行 · 开启思考工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 82.00 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4_5 "查看 Claude Sonnet 4.5 详情") |
|  | 7 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Claude Sonnet 5](https://www.datalearner.com/ai-models/pretrained-models/claude-5-sonnet) <br>并行 · 开启思考<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 82.00 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-5-sonnet "查看 Claude Sonnet 5 详情") |
|  | 8 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Opus 4.5](https://www.datalearner.com/ai-models/pretrained-models/anthropic-claude-opus-4-5) <br>扩展思考工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 80.90 | 87.00 | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/anthropic-claude-opus-4-5 "查看 Opus 4.5 详情") |
|  | 9 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Claude Opus 4.6](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-6) <br>扩展思考工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 80.84 | — | — | 72.00 | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-6 "查看 Claude Opus 4.6 详情") |
|  | 10 | [![Google Deep Mind](https://www.datalearner.com/resources/ai-org-logo/89eb72da-11bf-4473-81ae-6b74117ec8a9.png)](https://www.datalearner.com/ai-organizations/deep-mind "查看 Google Deep Mind 机构详情") <br>[Gemini 3.1 Pro Preview](https://www.datalearner.com/ai-models/pretrained-models/gemini-3-1-pro-preview) <br>开启思考工具<br>[Google Deep Mind](https://www.datalearner.com/ai-organizations/deep-mind "查看 Google Deep Mind 机构详情") | 80.60 | 91.70 | 54.20 | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/gemini-3-1-pro-preview "查看 Gemini 3.1 Pro Preview 详情") |
|  | 11 | [![DeepSeek-AI](https://www.datalearner.com/resources/ai-org-logo/7e535e25-299b-437c-8412-baf2988b671d.jpeg)](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") <br>[DeepSeek-V4-Pro](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro) <br>思考水平 · 极高工具<br>[DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") | 80.60 | — | 55.40 | 76.20 | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro "查看 DeepSeek-V4-Pro 详情") |
|  | 12 | [![阿里巴巴](https://www.datalearner.com/resources/ai-org-logo/aed962c6-d9e3-4413-ae3f-72b9b95a3996.webp)](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") <br>[Qwen3.7-Max-Preview](https://www.datalearner.com/ai-models/pretrained-models/qwen3-7-max-preview) <br>开启思考工具<br>[阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") | 80.40 | — | 60.60 | 78.30 | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-7-max-preview "查看 Qwen3.7-Max-Preview 详情") |
|  | 13 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Claude Sonnet 4](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4) <br>并行 · 开启思考工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 80.20 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4 "查看 Claude Sonnet 4 详情") |
|  | 14 | [![MiniMaxAI](https://www.datalearner.com/resources/ai-org-logo/24cc0de4-ed5f-442f-9796-bfdb7a94eaba.jpeg)](https://www.datalearner.com/ai-organizations/MiniMaxAI "查看 MiniMaxAI 机构详情") <br>[MiniMax M2.5](https://www.datalearner.com/ai-models/pretrained-models/minimax-m2-5) <br>开启思考工具<br>[MiniMaxAI](https://www.datalearner.com/ai-organizations/MiniMaxAI "查看 MiniMaxAI 机构详情") | 80.20 | — | 55.40 | — | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/minimax-m2-5 "查看 MiniMax M2.5 详情") |
|  | 15 | [![Moonshot AI](https://www.datalearner.com/resources/ai-org-logo/9898984c-ed92-456e-9f5c-6f127142ba87.jpeg)](https://www.datalearner.com/ai-organizations/Moonshot-AI "查看 Moonshot AI 机构详情") <br>[Kimi K2.6](https://www.datalearner.com/ai-models/pretrained-models/kimi-k2-6) <br>开启思考工具<br>[Moonshot AI](https://www.datalearner.com/ai-organizations/Moonshot-AI "查看 Moonshot AI 机构详情") | 80.20 | — | 58.60 | 76.70 | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/kimi-k2-6 "查看 Kimi K2.6 详情") |
|  | 16 | [![OpenAI](https://www.datalearner.com/resources/ai-org-logo/20b18263-07f8-44e6-b375-0fbb4530a9b3.png)](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") <br>[GPT-5.2](https://www.datalearner.com/ai-models/pretrained-models/openai-gpt-5-2) <br>思考水平 · 极高工具<br>[OpenAI](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") | 80.00 | — | 55.60 | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/openai-gpt-5-2 "查看 GPT-5.2 详情") |
|  | 17 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Claude Sonnet 4.6](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4-6) <br>开启思考<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 79.60 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4-6 "查看 Claude Sonnet 4.6 详情") |
|  | 18 | [![DeepSeek-AI](https://www.datalearner.com/resources/ai-org-logo/7e535e25-299b-437c-8412-baf2988b671d.jpeg)](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") <br>[DeepSeek-V4-Pro](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro) <br>开启思考工具<br>[DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") | 79.40 | — | 54.40 | 74.10 | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro "查看 DeepSeek-V4-Pro 详情") |
|  | 19 | [![DeepSeek-AI](https://www.datalearner.com/resources/ai-org-logo/7e535e25-299b-437c-8412-baf2988b671d.jpeg)](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") <br>[DeepSeek-V4-Flash](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-flash) <br>思考水平 · 极高工具<br>[DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") | 79.00 | — | 52.60 | 73.30 | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-flash "查看 DeepSeek-V4-Flash 详情") |
|  | 20 | [![阿里巴巴](https://www.datalearner.com/resources/ai-org-logo/aed962c6-d9e3-4413-ae3f-72b9b95a3996.webp)](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") <br>[Qwen 3.6 Plus Preview](https://www.datalearner.com/ai-models/pretrained-models/qwen-3.6-plus-preview) <br>开启思考工具<br>[阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") | 78.80 | — | 56.60 | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/qwen-3.6-plus-preview "查看 Qwen 3.6 Plus Preview 详情") |
|  | 21 | [![阿里巴巴](https://www.datalearner.com/resources/ai-org-logo/aed962c6-d9e3-4413-ae3f-72b9b95a3996.webp)](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") <br>[Qwen3.6-Max-Preview](https://www.datalearner.com/ai-models/pretrained-models/qwen3-6-max-preview) <br>开启思考工具<br>[阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") | 78.80 | — | 56.60 | 73.80 | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-6-max-preview "查看 Qwen3.6-Max-Preview 详情") |
|  | 22 | [![DeepSeek-AI](https://www.datalearner.com/resources/ai-org-logo/7e535e25-299b-437c-8412-baf2988b671d.jpeg)](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") <br>[DeepSeek-V4-Flash](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-flash) <br>开启思考工具<br>[DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") | 78.60 | — | 52.30 | 70.20 | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-flash "查看 DeepSeek-V4-Flash 详情") |
|  | 23 | [![智谱AI](https://www.datalearner.com/resources/ai-org-logo/b67aa2ce-ba23-4309-9fc7-67f4ecaf5d2a.png)](https://www.datalearner.com/ai-organizations/zhipu-ai "查看 智谱AI 机构详情") <br>[GLM-5](https://www.datalearner.com/ai-models/pretrained-models/glm-5) <br>开启思考<br>[智谱AI](https://www.datalearner.com/ai-organizations/zhipu-ai "查看 智谱AI 机构详情") | 77.80 | — | — | — | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/glm-5 "查看 GLM-5 详情") |
|  | 24 | [![Facebook AI研究实验室](https://www.datalearner.com/resources/ai-org-logo/f92e60c3-c65b-4e77-afcc-38181a2512a1.png)](https://www.datalearner.com/ai-organizations/fair "查看 Facebook AI研究实验室 机构详情") <br>[Muse Spark](https://www.datalearner.com/ai-models/pretrained-models/muse-spark) <br>开启思考工具<br>[Facebook AI研究实验室](https://www.datalearner.com/ai-organizations/fair "查看 Facebook AI研究实验室 机构详情") | 77.40 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/muse-spark "查看 Muse Spark 详情") |
|  | 25 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Claude Sonnet 4.5](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4_5) <br>开启思考工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 77.20 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4_5 "查看 Claude Sonnet 4.5 详情") |
|  | 26 | [![阿里巴巴](https://www.datalearner.com/resources/ai-org-logo/aed962c6-d9e3-4413-ae3f-72b9b95a3996.webp)](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") <br>[Qwen3.6-27B](https://www.datalearner.com/ai-models/pretrained-models/qwen3-6-27b) <br>开启思考工具<br>[阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") | 77.20 | — | 53.50 | 71.30 | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-6-27b "查看 Qwen3.6-27B 详情") |
|  | 27 | [![OpenAI](https://www.datalearner.com/resources/ai-org-logo/20b18263-07f8-44e6-b375-0fbb4530a9b3.png)](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") <br>[GPT-5.1-Codex-Max](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-1-codex-max) <br>思考水平 · 高工具<br>[OpenAI](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") | 76.80 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-1-codex-max "查看 GPT-5.1-Codex-Max 详情") |
|  | 28 | [![Moonshot AI](https://www.datalearner.com/resources/ai-org-logo/9898984c-ed92-456e-9f5c-6f127142ba87.jpeg)](https://www.datalearner.com/ai-organizations/Moonshot-AI "查看 Moonshot AI 机构详情") <br>[Kimi K2.5](https://www.datalearner.com/ai-models/pretrained-models/kimi-k2-5) <br>开启思考工具<br>[Moonshot AI](https://www.datalearner.com/ai-organizations/Moonshot-AI "查看 Moonshot AI 机构详情") | 76.80 | — | 50.70 | — | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/kimi-k2-5 "查看 Kimi K2.5 详情") |
|  | 29 | [![阿里巴巴](https://www.datalearner.com/resources/ai-org-logo/aed962c6-d9e3-4413-ae3f-72b9b95a3996.webp)](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") <br>[Qwen3.5-397B-A17B](https://www.datalearner.com/ai-models/pretrained-models/qwen3-5-397b-a17b) <br>开启思考工具<br>[阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") | 76.40 | — | — | — | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-5-397b-a17b "查看 Qwen3.5-397B-A17B 详情") |
|  | 30 | [![OpenAI](https://www.datalearner.com/resources/ai-org-logo/20b18263-07f8-44e6-b375-0fbb4530a9b3.png)](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") <br>[GPT-5.1](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-1-reasoning) <br>思考水平 · 高<br>[OpenAI](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") | 76.30 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-1-reasoning "查看 GPT-5.1 详情") |
|  | 31 | [![OpenAI](https://www.datalearner.com/resources/ai-org-logo/20b18263-07f8-44e6-b375-0fbb4530a9b3.png)](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") <br>[GPT-5.1](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-1-reasoning) <br>开启思考工具<br>[OpenAI](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") | 76.30 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-1-reasoning "查看 GPT-5.1 详情") |
|  | 32 | [![Google Deep Mind](https://www.datalearner.com/resources/ai-org-logo/89eb72da-11bf-4473-81ae-6b74117ec8a9.png)](https://www.datalearner.com/ai-organizations/deep-mind "查看 Google Deep Mind 机构详情") <br>[Gemini 3.0 Pro (Preview 11-2025)](https://www.datalearner.com/ai-models/pretrained-models/gemini-3-0-pro-preview-11-2025) <br>开启思考<br>[Google Deep Mind](https://www.datalearner.com/ai-organizations/deep-mind "查看 Google Deep Mind 机构详情") | 76.20 | 92.00 | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/gemini-3-0-pro-preview-11-2025 "查看 Gemini 3.0 Pro (Preview 11-2025) 详情") |
|  | 33 | [![阿里巴巴](https://www.datalearner.com/resources/ai-org-logo/aed962c6-d9e3-4413-ae3f-72b9b95a3996.webp)](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") <br>[Qwen3-Max-Thinking](https://www.datalearner.com/ai-models/pretrained-models/qwen3-max) <br>开启思考<br>[阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") | 75.30 | 85.90 | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-max "查看 Qwen3-Max-Thinking 详情") |
|  | 34 | [![OpenAI](https://www.datalearner.com/resources/ai-org-logo/20b18263-07f8-44e6-b375-0fbb4530a9b3.png)](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") <br>[o3-pro](https://www.datalearner.com/ai-models/pretrained-models/o3-pro) <br>思考水平 · 高<br>[OpenAI](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") | 75.00 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/o3-pro "查看 o3-pro 详情") |
|  | 35 | [![MiniMaxAI](https://www.datalearner.com/resources/ai-org-logo/24cc0de4-ed5f-442f-9796-bfdb7a94eaba.jpeg)](https://www.datalearner.com/ai-organizations/MiniMaxAI "查看 MiniMaxAI 机构详情") <br>[M2.1](https://www.datalearner.com/ai-models/pretrained-models/minimax-m2-1-preview) <br>开启思考<br>[MiniMaxAI](https://www.datalearner.com/ai-organizations/MiniMaxAI "查看 MiniMaxAI 机构详情") | 74.80 | — | — | — | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/minimax-m2-1-preview "查看 M2.1 详情") |
|  | 36 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Opus 4.1](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4_1) <br>扩展思考工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 74.50 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4_1 "查看 Opus 4.1 详情") |
|  | 37 | [![OpenAI](https://www.datalearner.com/resources/ai-org-logo/20b18263-07f8-44e6-b375-0fbb4530a9b3.png)](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") <br>[GPT-5 Codex](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-codex) <br>思考水平 · 高<br>[OpenAI](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") | 74.50 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-codex "查看 GPT-5 Codex 详情") |
|  | 38 | [![StepFunAI](https://www.datalearner.com/resources/ai-org-logo/485fed6f-5ec6-44a5-b60c-b12d22059a54.png)](https://www.datalearner.com/ai-organizations/StepFunAI "查看 StepFunAI 机构详情") <br>[Step 3.5 Flash](https://www.datalearner.com/ai-models/pretrained-models/stepfun-flash-3-5) <br>开启思考<br>[StepFunAI](https://www.datalearner.com/ai-organizations/StepFunAI "查看 StepFunAI 机构详情") | 74.40 | 86.40 | — | — | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/stepfun-flash-3-5 "查看 Step 3.5 Flash 详情") |
|  | 39 | [![智谱AI](https://www.datalearner.com/resources/ai-org-logo/b67aa2ce-ba23-4309-9fc7-67f4ecaf5d2a.png)](https://www.datalearner.com/ai-organizations/zhipu-ai "查看 智谱AI 机构详情") <br>[GLM-4.7](https://www.datalearner.com/ai-models/pretrained-models/glm-4-7) <br>开启思考工具<br>[智谱AI](https://www.datalearner.com/ai-organizations/zhipu-ai "查看 智谱AI 机构详情") | 73.80 | — | 40.60 | — | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/glm-4-7 "查看 GLM-4.7 详情") |
|  | 40 | [![DeepSeek-AI](https://www.datalearner.com/resources/ai-org-logo/7e535e25-299b-437c-8412-baf2988b671d.jpeg)](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") <br>[DeepSeek-V4-Flash](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-flash) <br>常规模式工具<br>[DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") | 73.70 | — | 49.10 | 69.70 | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-flash "查看 DeepSeek-V4-Flash 详情") |
|  | 41 | [![DeepSeek-AI](https://www.datalearner.com/resources/ai-org-logo/7e535e25-299b-437c-8412-baf2988b671d.jpeg)](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") <br>[DeepSeek-V4-Pro](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro) <br>常规模式工具<br>[DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") | 73.60 | — | 52.10 | 69.80 | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro "查看 DeepSeek-V4-Pro 详情") |
|  | 42 | [![xAI](https://www.datalearner.com/resources/ai-org-logo/6b25b544-b32c-4002-a138-0613936c8576.svg)](https://www.datalearner.com/ai-organizations/xAI "查看 xAI 机构详情") <br>[Grok 4 Heavy](https://www.datalearner.com/ai-models/pretrained-models/grok-4-heavy) <br>并行 · 开启思考工具<br>[xAI](https://www.datalearner.com/ai-organizations/xAI "查看 xAI 机构详情") | 73.50 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/grok-4-heavy "查看 Grok 4 Heavy 详情") |
|  | 43 | [![阿里巴巴](https://www.datalearner.com/resources/ai-org-logo/aed962c6-d9e3-4413-ae3f-72b9b95a3996.webp)](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") <br>[Qwen3.6-35B-A3B](https://www.datalearner.com/ai-models/pretrained-models/qwen3-6-35b-a3b) <br>开启思考<br>[阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") | 73.40 | 80.40 | 49.50 | 67.20 | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-6-35b-a3b "查看 Qwen3.6-35B-A3B 详情") |
|  | 44 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Haiku 4.5](https://www.datalearner.com/ai-models/pretrained-models/claude-haiku-4-5) <br>开启思考工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 73.30 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-haiku-4-5 "查看 Haiku 4.5 详情") |
|  | 45 | [![DeepSeek-AI](https://www.datalearner.com/resources/ai-org-logo/7e535e25-299b-437c-8412-baf2988b671d.jpeg)](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") <br>[DeepSeek V3.2](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v3-2) <br>开启思考工具<br>[DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI "查看 DeepSeek-AI 机构详情") | 73.10 | — | — | — | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v3-2 "查看 DeepSeek V3.2 详情") |
|  | 46 | [![OpenAI](https://www.datalearner.com/resources/ai-org-logo/20b18263-07f8-44e6-b375-0fbb4530a9b3.png)](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") <br>[GPT-5](https://www.datalearner.com/ai-models/pretrained-models/gpt-5) <br>思考水平 · 高<br>[OpenAI](https://www.datalearner.com/ai-organizations/open-ai "查看 OpenAI 机构详情") | 72.80 | — | 36.30 | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/gpt-5 "查看 GPT-5 详情") |
|  | 47 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Claude Sonnet 4](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4) <br>开启思考工具<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 72.70 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4 "查看 Claude Sonnet 4 详情") |
|  | 48 | [![Anthropic](https://www.datalearner.com/resources/ai-org-logo/3be5750e-ead8-4a60-a00f-8b7afddf2ad8.webp)](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") <br>[Claude Opus 4](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4)<br>[Anthropic](https://www.datalearner.com/ai-organizations/anthropic "查看 Anthropic 机构详情") | 72.50 | 56.60 | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4 "查看 Claude Opus 4 详情") |
|  | 49 | [![阿里巴巴](https://www.datalearner.com/resources/ai-org-logo/aed962c6-d9e3-4413-ae3f-72b9b95a3996.webp)](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") <br>[Qwen3.5-27B](https://www.datalearner.com/ai-models/pretrained-models/qwen3-5-27b-dense) <br>开启思考<br>[阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba "查看 阿里巴巴 机构详情") | 72.40 | — | — | — | 免费商用 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-5-27b-dense "查看 Qwen3.5-27B 详情") |
|  | 50 | [![xAI](https://www.datalearner.com/resources/ai-org-logo/6b25b544-b32c-4002-a138-0613936c8576.svg)](https://www.datalearner.com/ai-organizations/xAI "查看 xAI 机构详情") <br>[Grok 4 Code](https://www.datalearner.com/ai-models/pretrained-models/grok-4-code)<br>[xAI](https://www.datalearner.com/ai-organizations/xAI "查看 xAI 机构详情") | 72.00 | — | — | — | 闭源 | [详情详情](https://www.datalearner.com/ai-models/pretrained-models/grok-4-code "查看 Grok 4 Code 详情") |

[Claude Fable 5](https://www.datalearner.com/ai-models/pretrained-models/claude-fable-5) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

深度思考模式工具

[查看 Claude Fable 5 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-fable-5)

SWE-bench Verified95.00

LiveCodeBench—

SWE-Bench Pro - Public80.30

SWE-bench Multilingual—

闭源

[Claude Fable 5](https://www.datalearner.com/ai-models/pretrained-models/claude-fable-5) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

开启思考工具

[查看 Claude Fable 5 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-fable-5)

SWE-bench Verified95.00

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

[Claude Mythos Preview](https://www.datalearner.com/ai-models/pretrained-models/claude-mythos-preview) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

扩展思考工具

[查看 Claude Mythos Preview 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-mythos-preview)

SWE-bench Verified93.90

LiveCodeBench—

SWE-Bench Pro - Public77.80

SWE-bench Multilingual87.30

闭源

4

[Claude Opus 4.8](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-8) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

扩展思考工具

[查看 Claude Opus 4.8 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-8)

SWE-bench Verified88.60

LiveCodeBench—

SWE-Bench Pro - Public69.20

SWE-bench Multilingual—

闭源

5

[Opus 4.7](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-7) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

扩展思考工具

[查看 Opus 4.7 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-7)

SWE-bench Verified87.60

LiveCodeBench—

SWE-Bench Pro - Public64.30

SWE-bench Multilingual—

闭源

6

[Claude Sonnet 4.5](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4_5) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

并行 · 开启思考工具

[查看 Claude Sonnet 4.5 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4_5)

SWE-bench Verified82.00

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

7

[Claude Sonnet 5](https://www.datalearner.com/ai-models/pretrained-models/claude-5-sonnet) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

并行 · 开启思考

[查看 Claude Sonnet 5 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-5-sonnet)

SWE-bench Verified82.00

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

8

[Opus 4.5](https://www.datalearner.com/ai-models/pretrained-models/anthropic-claude-opus-4-5) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

扩展思考工具

[查看 Opus 4.5 详情](https://www.datalearner.com/ai-models/pretrained-models/anthropic-claude-opus-4-5)

SWE-bench Verified80.90

LiveCodeBench87.00

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

9

[Claude Opus 4.6](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-6) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

扩展思考工具

[查看 Claude Opus 4.6 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4-6)

SWE-bench Verified80.84

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual72.00

闭源

10

[Gemini 3.1 Pro Preview](https://www.datalearner.com/ai-models/pretrained-models/gemini-3-1-pro-preview) [Google Deep Mind](https://www.datalearner.com/ai-organizations/deep-mind)

开启思考工具

[查看 Gemini 3.1 Pro Preview 详情](https://www.datalearner.com/ai-models/pretrained-models/gemini-3-1-pro-preview)

SWE-bench Verified80.60

LiveCodeBench91.70

SWE-Bench Pro - Public54.20

SWE-bench Multilingual—

闭源

11

[DeepSeek-V4-Pro](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro) [DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI)

思考水平 · 极高工具

[查看 DeepSeek-V4-Pro 详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro)

SWE-bench Verified80.60

LiveCodeBench—

SWE-Bench Pro - Public55.40

SWE-bench Multilingual76.20

免费商用

12

[Qwen3.7-Max-Preview](https://www.datalearner.com/ai-models/pretrained-models/qwen3-7-max-preview) [阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba)

开启思考工具

[查看 Qwen3.7-Max-Preview 详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-7-max-preview)

SWE-bench Verified80.40

LiveCodeBench—

SWE-Bench Pro - Public60.60

SWE-bench Multilingual78.30

闭源

13

[Claude Sonnet 4](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

并行 · 开启思考工具

[查看 Claude Sonnet 4 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4)

SWE-bench Verified80.20

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

14

[MiniMax M2.5](https://www.datalearner.com/ai-models/pretrained-models/minimax-m2-5) [MiniMaxAI](https://www.datalearner.com/ai-organizations/MiniMaxAI)

开启思考工具

[查看 MiniMax M2.5 详情](https://www.datalearner.com/ai-models/pretrained-models/minimax-m2-5)

SWE-bench Verified80.20

LiveCodeBench—

SWE-Bench Pro - Public55.40

SWE-bench Multilingual—

免费商用

15

[Kimi K2.6](https://www.datalearner.com/ai-models/pretrained-models/kimi-k2-6) [Moonshot AI](https://www.datalearner.com/ai-organizations/Moonshot-AI)

开启思考工具

[查看 Kimi K2.6 详情](https://www.datalearner.com/ai-models/pretrained-models/kimi-k2-6)

SWE-bench Verified80.20

LiveCodeBench—

SWE-Bench Pro - Public58.60

SWE-bench Multilingual76.70

免费商用

16

[GPT-5.2](https://www.datalearner.com/ai-models/pretrained-models/openai-gpt-5-2) [OpenAI](https://www.datalearner.com/ai-organizations/open-ai)

思考水平 · 极高工具

[查看 GPT-5.2 详情](https://www.datalearner.com/ai-models/pretrained-models/openai-gpt-5-2)

SWE-bench Verified80.00

LiveCodeBench—

SWE-Bench Pro - Public55.60

SWE-bench Multilingual—

闭源

17

[Claude Sonnet 4.6](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4-6) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

开启思考

[查看 Claude Sonnet 4.6 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4-6)

SWE-bench Verified79.60

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

18

[DeepSeek-V4-Pro](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro) [DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI)

开启思考工具

[查看 DeepSeek-V4-Pro 详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro)

SWE-bench Verified79.40

LiveCodeBench—

SWE-Bench Pro - Public54.40

SWE-bench Multilingual74.10

免费商用

19

[DeepSeek-V4-Flash](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-flash) [DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI)

思考水平 · 极高工具

[查看 DeepSeek-V4-Flash 详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-flash)

SWE-bench Verified79.00

LiveCodeBench—

SWE-Bench Pro - Public52.60

SWE-bench Multilingual73.30

免费商用

20

[Qwen 3.6 Plus Preview](https://www.datalearner.com/ai-models/pretrained-models/qwen-3.6-plus-preview) [阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba)

开启思考工具

[查看 Qwen 3.6 Plus Preview 详情](https://www.datalearner.com/ai-models/pretrained-models/qwen-3.6-plus-preview)

SWE-bench Verified78.80

LiveCodeBench—

SWE-Bench Pro - Public56.60

SWE-bench Multilingual—

闭源

21

[Qwen3.6-Max-Preview](https://www.datalearner.com/ai-models/pretrained-models/qwen3-6-max-preview) [阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba)

开启思考工具

[查看 Qwen3.6-Max-Preview 详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-6-max-preview)

SWE-bench Verified78.80

LiveCodeBench—

SWE-Bench Pro - Public56.60

SWE-bench Multilingual73.80

闭源

22

[DeepSeek-V4-Flash](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-flash) [DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI)

开启思考工具

[查看 DeepSeek-V4-Flash 详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-flash)

SWE-bench Verified78.60

LiveCodeBench—

SWE-Bench Pro - Public52.30

SWE-bench Multilingual70.20

免费商用

23

[GLM-5](https://www.datalearner.com/ai-models/pretrained-models/glm-5) [智谱AI](https://www.datalearner.com/ai-organizations/zhipu-ai)

开启思考

[查看 GLM-5 详情](https://www.datalearner.com/ai-models/pretrained-models/glm-5)

SWE-bench Verified77.80

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

免费商用

24

[Muse Spark](https://www.datalearner.com/ai-models/pretrained-models/muse-spark) [Facebook AI研究实验室](https://www.datalearner.com/ai-organizations/fair)

开启思考工具

[查看 Muse Spark 详情](https://www.datalearner.com/ai-models/pretrained-models/muse-spark)

SWE-bench Verified77.40

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

25

[Claude Sonnet 4.5](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4_5) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

开启思考工具

[查看 Claude Sonnet 4.5 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4_5)

SWE-bench Verified77.20

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

26

[Qwen3.6-27B](https://www.datalearner.com/ai-models/pretrained-models/qwen3-6-27b) [阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba)

开启思考工具

[查看 Qwen3.6-27B 详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-6-27b)

SWE-bench Verified77.20

LiveCodeBench—

SWE-Bench Pro - Public53.50

SWE-bench Multilingual71.30

免费商用

27

[GPT-5.1-Codex-Max](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-1-codex-max) [OpenAI](https://www.datalearner.com/ai-organizations/open-ai)

思考水平 · 高工具

[查看 GPT-5.1-Codex-Max 详情](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-1-codex-max)

SWE-bench Verified76.80

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

28

[Kimi K2.5](https://www.datalearner.com/ai-models/pretrained-models/kimi-k2-5) [Moonshot AI](https://www.datalearner.com/ai-organizations/Moonshot-AI)

开启思考工具

[查看 Kimi K2.5 详情](https://www.datalearner.com/ai-models/pretrained-models/kimi-k2-5)

SWE-bench Verified76.80

LiveCodeBench—

SWE-Bench Pro - Public50.70

SWE-bench Multilingual—

免费商用

29

[Qwen3.5-397B-A17B](https://www.datalearner.com/ai-models/pretrained-models/qwen3-5-397b-a17b) [阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba)

开启思考工具

[查看 Qwen3.5-397B-A17B 详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-5-397b-a17b)

SWE-bench Verified76.40

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

免费商用

30

[GPT-5.1](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-1-reasoning) [OpenAI](https://www.datalearner.com/ai-organizations/open-ai)

思考水平 · 高

[查看 GPT-5.1 详情](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-1-reasoning)

SWE-bench Verified76.30

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

31

[GPT-5.1](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-1-reasoning) [OpenAI](https://www.datalearner.com/ai-organizations/open-ai)

开启思考工具

[查看 GPT-5.1 详情](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-1-reasoning)

SWE-bench Verified76.30

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

32

[Gemini 3.0 Pro (Preview 11-2025)](https://www.datalearner.com/ai-models/pretrained-models/gemini-3-0-pro-preview-11-2025) [Google Deep Mind](https://www.datalearner.com/ai-organizations/deep-mind)

开启思考

[查看 Gemini 3.0 Pro (Preview 11-2025) 详情](https://www.datalearner.com/ai-models/pretrained-models/gemini-3-0-pro-preview-11-2025)

SWE-bench Verified76.20

LiveCodeBench92.00

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

33

[Qwen3-Max-Thinking](https://www.datalearner.com/ai-models/pretrained-models/qwen3-max) [阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba)

开启思考

[查看 Qwen3-Max-Thinking 详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-max)

SWE-bench Verified75.30

LiveCodeBench85.90

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

34

[o3-pro](https://www.datalearner.com/ai-models/pretrained-models/o3-pro) [OpenAI](https://www.datalearner.com/ai-organizations/open-ai)

思考水平 · 高

[查看 o3-pro 详情](https://www.datalearner.com/ai-models/pretrained-models/o3-pro)

SWE-bench Verified75.00

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

35

[M2.1](https://www.datalearner.com/ai-models/pretrained-models/minimax-m2-1-preview) [MiniMaxAI](https://www.datalearner.com/ai-organizations/MiniMaxAI)

开启思考

[查看 M2.1 详情](https://www.datalearner.com/ai-models/pretrained-models/minimax-m2-1-preview)

SWE-bench Verified74.80

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

免费商用

36

[Opus 4.1](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4_1) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

扩展思考工具

[查看 Opus 4.1 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4_1)

SWE-bench Verified74.50

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

37

[GPT-5 Codex](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-codex) [OpenAI](https://www.datalearner.com/ai-organizations/open-ai)

思考水平 · 高

[查看 GPT-5 Codex 详情](https://www.datalearner.com/ai-models/pretrained-models/gpt-5-codex)

SWE-bench Verified74.50

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

38

[Step 3.5 Flash](https://www.datalearner.com/ai-models/pretrained-models/stepfun-flash-3-5) [StepFunAI](https://www.datalearner.com/ai-organizations/StepFunAI)

开启思考

[查看 Step 3.5 Flash 详情](https://www.datalearner.com/ai-models/pretrained-models/stepfun-flash-3-5)

SWE-bench Verified74.40

LiveCodeBench86.40

SWE-Bench Pro - Public—

SWE-bench Multilingual—

免费商用

39

[GLM-4.7](https://www.datalearner.com/ai-models/pretrained-models/glm-4-7) [智谱AI](https://www.datalearner.com/ai-organizations/zhipu-ai)

开启思考工具

[查看 GLM-4.7 详情](https://www.datalearner.com/ai-models/pretrained-models/glm-4-7)

SWE-bench Verified73.80

LiveCodeBench—

SWE-Bench Pro - Public40.60

SWE-bench Multilingual—

免费商用

40

[DeepSeek-V4-Flash](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-flash) [DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI)

常规模式工具

[查看 DeepSeek-V4-Flash 详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-flash)

SWE-bench Verified73.70

LiveCodeBench—

SWE-Bench Pro - Public49.10

SWE-bench Multilingual69.70

免费商用

41

[DeepSeek-V4-Pro](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro) [DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI)

常规模式工具

[查看 DeepSeek-V4-Pro 详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v4-pro)

SWE-bench Verified73.60

LiveCodeBench—

SWE-Bench Pro - Public52.10

SWE-bench Multilingual69.80

免费商用

42

[Grok 4 Heavy](https://www.datalearner.com/ai-models/pretrained-models/grok-4-heavy) [xAI](https://www.datalearner.com/ai-organizations/xAI)

并行 · 开启思考工具

[查看 Grok 4 Heavy 详情](https://www.datalearner.com/ai-models/pretrained-models/grok-4-heavy)

SWE-bench Verified73.50

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

43

[Qwen3.6-35B-A3B](https://www.datalearner.com/ai-models/pretrained-models/qwen3-6-35b-a3b) [阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba)

开启思考

[查看 Qwen3.6-35B-A3B 详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-6-35b-a3b)

SWE-bench Verified73.40

LiveCodeBench80.40

SWE-Bench Pro - Public49.50

SWE-bench Multilingual67.20

免费商用

44

[Haiku 4.5](https://www.datalearner.com/ai-models/pretrained-models/claude-haiku-4-5) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

开启思考工具

[查看 Haiku 4.5 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-haiku-4-5)

SWE-bench Verified73.30

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

45

[DeepSeek V3.2](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v3-2) [DeepSeek-AI](https://www.datalearner.com/ai-organizations/DeepSeek-AI)

开启思考工具

[查看 DeepSeek V3.2 详情](https://www.datalearner.com/ai-models/pretrained-models/deepseek-v3-2)

SWE-bench Verified73.10

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

免费商用

46

[GPT-5](https://www.datalearner.com/ai-models/pretrained-models/gpt-5) [OpenAI](https://www.datalearner.com/ai-organizations/open-ai)

思考水平 · 高

[查看 GPT-5 详情](https://www.datalearner.com/ai-models/pretrained-models/gpt-5)

SWE-bench Verified72.80

LiveCodeBench—

SWE-Bench Pro - Public36.30

SWE-bench Multilingual—

闭源

47

[Claude Sonnet 4](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

开启思考工具

[查看 Claude Sonnet 4 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-sonnet-4)

SWE-bench Verified72.70

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

48

[Claude Opus 4](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4) [Anthropic](https://www.datalearner.com/ai-organizations/anthropic)

[查看 Claude Opus 4 详情](https://www.datalearner.com/ai-models/pretrained-models/claude-opus-4)

SWE-bench Verified72.50

LiveCodeBench56.60

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

49

[Qwen3.5-27B](https://www.datalearner.com/ai-models/pretrained-models/qwen3-5-27b-dense) [阿里巴巴](https://www.datalearner.com/ai-organizations/alibaba)

开启思考

[查看 Qwen3.5-27B 详情](https://www.datalearner.com/ai-models/pretrained-models/qwen3-5-27b-dense)

SWE-bench Verified72.40

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

免费商用

50

[Grok 4 Code](https://www.datalearner.com/ai-models/pretrained-models/grok-4-code) [xAI](https://www.datalearner.com/ai-organizations/xAI)

[查看 Grok 4 Code 详情](https://www.datalearner.com/ai-models/pretrained-models/grok-4-code)

SWE-bench Verified72.00

LiveCodeBench—

SWE-Bench Pro - Public—

SWE-bench Multilingual—

闭源

排序：SWE-bench VerifiedLiveCodeBenchSWE-Bench Pro - PublicSWE-bench Multilingual重置

勾选左侧复选框，可同时对比 2-4 个模型

已显示 50 / 211 个模型加载更多 [查看 SWE-bench Verified 基准测试完整页面](https://www.datalearner.com/benchmarks/SWE-bench%20Verified)

### 来源 2: Best LLMs for Coding in 2026: SWE-bench, HumanEval ... - Onyx AI

- URL: https://onyx.app/insights/best-llms-for-coding-2026
- 精读方法：firecrawl-scrape

[All Insights](https://onyx.app/insights)

AI Tools11 min readPublished May 7, 2026

# Best LLMs for Coding in 2026

![Roshan Desai](https://onyx.app/_next/image?url=%2Favatars%2Frd-ghibli-pfp.png&w=64&q=75)

By Roshan Desai

The model that writes the cleanest function isn't necessarily the best one for shipping features. Generating code from a description and fixing bugs in a real codebase are different skills, and the best model for each is not always the same. This guide focuses on the coding models in the [Onyx Coding LLM Leaderboard](https://onyx.app/best-llm-for-coding), updated March 12, 2026. In that dataset, Claude Opus 4.6 leads on autonomous bug-fixing, GPT-5.4 leads on agentic terminal tasks, Kimi K2.5 and GLM-5 are the strongest open-source options, and MiniMax M2.5 or Step-3.5-Flash stand out when API cost matters.

**How this guide is sourced:** Coding benchmark, pricing, and license data comes from the Onyx Coding LLM Leaderboard. The recommendations in each review are editorial guidance based on that dataset.

* * *

> **TL;DR:** For serious software engineering, **Claude Opus 4.6** leads on autonomous bug-fixing with 80.8% SWE-bench. For agentic coding and terminal tasks, **GPT-5.4** leads with 75.1% Terminal-Bench and 75% OSWorld-Verified, the strongest agentic profile in this dataset. If cost is the constraint, **MiniMax M2.5** matches frontier-level bug-fixing at $0.30/M, and **Step-3.5-Flash** goes even lower at $0.10/M. For open-source, **Kimi K2.5** leads on code generation under an MIT license, while **GLM-5** is the strongest open-weight model for fixing real bugs.

* * *

## What Makes an LLM Good at Coding?

Not all coding tasks are the same, and different models are optimized for different ones.

Writing a function from a description is easy for almost every modern LLM. Navigating an unfamiliar 50,000-line codebase, finding where a bug originates, and writing a fix that doesn't break three other things: that's much harder, and that's what separates the top models from the rest.

The four benchmarks in this guide each test something different:

- **SWE-bench Verified**: The closest thing to a real-world software engineering test. Models are given an actual GitHub issue and must fix it autonomously. This is the benchmark that matters most for teams building coding agents or using AI for production engineering work.
- **HumanEval**: Tests how well a model writes code from a description. Almost every frontier model now scores above 90%, so it's more useful for evaluating open-source and smaller models than for differentiating the top tier.
- **LiveCodeBench**: Competitive programming problems from LeetCode and Codeforces, updated monthly. Strong scores here indicate a model handles novel algorithmic challenges well. Useful for algorithm implementation and competitive programming, less relevant for most production software work.
- **Terminal-Bench**: Tests whether a model can autonomously complete tasks in a real terminal: running commands, reading output, adjusting its approach. This is the best proxy for how well a model works as an autonomous coding agent.

A model that excels on HumanEval but has a low SWE-bench score is a good autocomplete tool. A model that leads on SWE-bench and Terminal-Bench is what you want for serious engineering work.

* * *

## What Is Onyx?

[Onyx](https://onyx.app/) is an open-source AI platform that connects LLMs to company knowledge, tools, and workflows. For coding teams, Onyx is useful when model evaluation needs to extend beyond code generation benchmarks into real engineering context: design docs, tickets, pull requests, Slack discussions, runbooks, and source repositories.

A coding model can write code. A workplace AI platform helps the model find the right context before it writes. Onyx supports that layer with connectors, permission-aware search, agents, deep research, and model flexibility across hosted and self-hosted LLMs.

## Best Coding LLMs 2026: Full Comparison Table

| Model | Provider | SWE-bench | HumanEval | LiveCode | Terminal-Bench | API Cost (per 1M in/out) | License |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Claude Opus 4.6** | Anthropic | **80.8%** | 95.0% | 76.0% | 65.4% | $15 / $75 | Proprietary |
| **GPT-5.4** | OpenAI | N/A† | N/A | N/A | **75.1%** | $2.50 / $15 | Proprietary |
| **MiniMax M2.5** | MiniMax | 80.2% | 89.6% | 65.0% | 42.2% | $0.30 / $1.20 | API |
| **Claude Sonnet 4.6** | Anthropic | 79.6% | 92.1% | 72.4% | 59.1% | $3 / $15 | Proprietary |
| **Gemini 3.1 Pro** | Google | 78.0% | 93.0% | 81.3% | 56.2% | $2 / $12 | Proprietary |
| **GLM-5** | Zhipu AI | 77.8% | 90.0% | 52.0% | 56.2% | Free API | MIT |
| **Kimi K2.5** | Moonshot | 76.8% | **99.0%** | 85.0% | 50.8% | Free API | MIT |
| **Qwen 3.5** | Qwen | 76.4% | N/A | 83.6% | 52.5% | Free API | Apache 2.0 |
| **Step-3.5-Flash** | Stepfun | 74.4% | 81.1% | **86.4%** | 51.0% | $0.10 / $0.30 | API |
| **MiMo-V2-Flash** | Xiaomi | 73.4% | 84.8% | 80.6% | 38.5% | Free API | MIT |

_† SWE-bench Verified not yet published for GPT-5.4. SWE-bench Pro = 57.7%._

_Source: [Onyx Coding LLM Leaderboard](https://onyx.app/best-llm-for-coding), last updated March 12, 2026._

* * *

## Coding LLMs at a Glance

**Best at fixing real bugs:** Claude Opus 4.6, MiniMax M2.5, Claude Sonnet 4.6, Gemini 3.1 Pro, GLM-5

**Best code generation:** Kimi K2.5, Claude Opus 4.6, GPT-5.4, Gemini 3.1 Pro, Claude Sonnet 4.6

**Best for competitive programming:** Step-3.5-Flash, Kimi K2.5, Qwen 3.5, Gemini 3.1 Pro, GPT-5.4

**Best for agentic coding:** GPT-5.4, Claude Opus 4.6, Claude Sonnet 4.6, GLM-5, Gemini 3.1 Pro

**Best reasoning for coding tasks:** GPT-5.4, Claude Opus 4.6, Gemini 3.1 Pro, Claude Sonnet 4.6

**Best open-source:** GLM-5, Kimi K2.5, Qwen 3.5, MiMo-V2-Flash

**Best budget API:** MiniMax M2.5 at $0.30/M, Step-3.5-Flash at $0.10/M

* * *

## Top Coding LLMs: Detailed Reviews

### 1\. Claude Opus 4.6 (Anthropic)

Claude Opus 4.6 scores 80.8% on SWE-bench Verified, 95.0% on HumanEval, 76.0% on LiveCodeBench, 65.4% on Terminal-Bench, and costs $15 / $75 per 1M input/output tokens. Use it when you are optimizing for maximum success rate on difficult software-engineering tasks, particularly where autonomous bug-fixing quality is the top priority.

### 2\. GPT-5.4 (OpenAI)

GPT-5.4 leads this dataset on agentic tasks: 75.1% Terminal-Bench, 75% OSWorld-Verified, and 82.7% BrowseComp. It also scores 92.8% on GPQA Diamond, showing strong reasoning alongside its agentic performance. SWE-bench Verified hasn't been published yet (SWE-bench Pro is 57.7%), and it costs $2.50 / $15 per 1M input/output tokens. Choose GPT-5.4 when agentic coding, terminal task automation, or computer control are the primary use case.

### 3\. MiniMax M2.5 (MiniMax)

MiniMax M2.5 scores 80.2% on SWE-bench Verified, 89.6% on HumanEval, 65.0% on LiveCodeBench, 42.2% on Terminal-Bench, and costs $0.30 / $1.20 per 1M input/output tokens. It is the first model to evaluate when software-engineering throughput per dollar matters more than terminal-agent performance.

### 4\. Claude Sonnet 4.6 (Anthropic)

Claude Sonnet 4.6 scores 79.6% on SWE-bench Verified, 92.1% on HumanEval, 72.4% on LiveCodeBench, 59.1% on Terminal-Bench, and costs $3 / $15 per 1M input/output tokens. Pick it when you want Anthropic compatibility and strong coding performance without stepping up to Opus pricing.

### 5\. Gemini 3.1 Pro (Google)

Gemini 3.1 Pro scores 78.0% on SWE-bench Verified, 93.0% on HumanEval, 81.3% on LiveCodeBench, 56.2% on Terminal-Bench, and costs $2 / $12 per 1M input/output tokens. Start with Gemini 3.1 Pro when you want strong coding coverage and the lowest proprietary API price among frontier models, especially for code generation and algorithm-heavy tasks.

### 6\. GLM-5 (Zhipu AI, MIT)

GLM-5 scores 77.8% on SWE-bench Verified, 90.0% on HumanEval, 52.0% on LiveCodeBench, 56.2% on Terminal-Bench, and is MIT-licensed with a free API option. It is the best fit in this ranking when you need MIT licensing and want a model optimized for practical software-engineering workflows.

### 7\. Kimi K2.5 (Moonshot, MIT License)

Kimi K2.5 scores 76.8% on SWE-bench Verified, 99.0% on HumanEval, 85.0% on LiveCodeBench, 50.8% on Terminal-Bench, and is MIT-licensed with a free API option. Choose Kimi K2.5 when code generation and algorithmic problem solving matter more than terminal-agent performance.

### 8\. Qwen 3.5 (Alibaba, Apache 2.0)

Qwen 3.5 scores 76.4% on SWE-bench Verified, 83.6% on LiveCodeBench, 52.5% on Terminal-Bench, and is Apache 2.0 licensed with a free API option. HumanEval is not listed in this snapshot. Qwen 3.5 is the strongest option here when Apache licensing and competitive-programming-style coding are the key requirements.

### 9\. Step-3.5-Flash (Stepfun)

Step-3.5-Flash scores 74.4% on SWE-bench Verified, 81.1% on HumanEval, 86.4% on LiveCodeBench, 51.0% on Terminal-Bench, and costs $0.10 / $0.30 per 1M input/output tokens. Use it when algorithmic coding volume is high and price sensitivity outweighs the need for the strongest end-to-end engineering model.

### 10\. MiMo-V2-Flash (Xiaomi, MIT)

MiMo-V2-Flash scores 73.4% on SWE-bench Verified, 84.8% on HumanEval, 80.6% on LiveCodeBench, 38.5% on Terminal-Bench, and is MIT-licensed with a free API option. It is a balanced MIT-licensed option when you want broadly decent coding performance without targeting a specialized winner.

* * *

## Coding LLM Cost Comparison

At 10 million output tokens per month (a typical usage level for a 50-person engineering team using AI coding assistance):

| Model | Monthly API Cost | SWE-bench | Notes |
| --- | --- | --- | --- |
| Claude Opus 4.6 | ~$750,000 | 80.8% | Highest SWE-bench, highest cost |
| Claude Sonnet 4.6 | ~$150,000 | 79.6% | Best Anthropic value |
| GPT-5.4 | ~$150,000 | N/A† | Best Terminal-Bench, strongest agentic use |
| Gemini 3.1 Pro | ~$100,000 | 78.0% | Cheapest frontier proprietary model |
| MiniMax M2.5 | ~$12,000 | 80.2% | Best value in the frontier tier |
| Step-3.5-Flash | ~$3,000 | 74.4% | Cheapest option with 74%+ SWE-bench |
| Kimi K2.5 | Free in this snapshot | 76.8% | MIT licensed, listed with free API |
| GLM-5 | Free in this snapshot | 77.8% | MIT licensed, listed with free API |

* * *

## How to Choose the Best Coding LLM

| Your Situation | Best Choice |
| --- | --- |
| Highest SWE-bench, cost not a constraint | **Claude Opus 4.6** |
| Best agentic coding and terminal tasks | **GPT-5.4** (75.1% Terminal-Bench, 75% OSWorld) |
| Best frontier performance per dollar | **MiniMax M2.5** ($0.30/M input, 80.2% SWE-bench) |
| Cheapest API with high LiveCodeBench | **Step-3.5-Flash** ($0.10/M, 86.4% LiveCode) |
| Best open-source, MIT license | **Kimi K2.5** (99% HumanEval) or **GLM-5** (77.8% SWE-bench) |
| Apache 2.0, open weights | **Qwen 3.5** (83.6% LiveCode) |
| Anthropic ecosystem, cost-optimized | **Claude Sonnet 4.6** (79.6% SWE-bench, $15/M out) |
| Frontier coding at reasonable API cost | **Gemini 3.1 Pro** ($2/M) or **Claude Sonnet 4.6** ($3/M) |

* * *

## Recommended Coding LLM Setup

| Engineering use case | Recommended setup | Why |
| --- | --- | --- |
| Individual coding assistant | Claude, GPT, Gemini, or a coding-focused open model in the IDE | Fastest feedback loop for code generation |
| Team knowledge search | Onyx connected to GitHub, Jira, Confluence, Slack, and runbooks | Helps models answer with project context |
| Autonomous engineering agents | Frontier coding model plus sandboxed terminal environment | Stronger fit for bug fixing and terminal tasks |
| Regulated engineering org | Self-hosted model + Onyx self-hosted + source permissions | Keeps code and internal docs inside controlled infrastructure |

Benchmarks tell you which models are strong. The production setup determines whether those models can safely use your team's actual engineering context.

## Frequently Asked Questions

### What is the best LLM for coding in 2026?

In this leaderboard snapshot, Claude Opus 4.6 has the strongest autonomous bug-fixing performance at 80.8% SWE-bench. GPT-5.4 leads on Terminal-Bench (75.1%) and OSWorld-Verified (75%), making it the best pick for agentic coding workflows. MiniMax M2.5 is notable for price-performance on SWE-bench. For open-source options, Kimi K2.5 and GLM-5 are the leading choices in this dataset.

### What is SWE-bench Verified?

SWE-bench Verified is a benchmark where models are given real GitHub issues from popular Python projects and must autonomously write a code patch that makes the project's existing tests pass. Unlike HumanEval, which tests function-level code generation, SWE-bench tests the ability to understand entire codebases, locate relevant files, and write correct diffs. A score above 75% is considered frontier-level as of 2026.

### Is Claude better than GPT for coding?

On SWE-bench Verified, Claude Opus 4.6 (80.8%) leads among models with published scores. On Terminal-Bench, GPT-5.4 (75.1%) leads Claude Opus 4.6 (65.4%) by a significant margin, making it the better choice for autonomous coding agents and terminal workflows. The right pick depends on whether you are optimizing for bug-fixing accuracy or agentic task completion.

### What is the best open-source model for coding?

In this leaderboard snapshot, Kimi K2.5 and GLM-5 are the strongest open-source coding models. Kimi K2.5 leads on code generation with 99% HumanEval and 85% LiveCodeBench under an MIT license. GLM-5 is the better pick for fixing real bugs, with 77.8% SWE-bench and strong terminal performance, also MIT-licensed. Qwen 3.5 is the top Apache 2.0 option if you need that specific license. All three offer free API access in this snapshot.

Related Insights

[AI ToolsEnterprise Search\\
\\
22 min read\\
\\
Best Enterprise RAG Platforms for 2026: A Buyer's Guide\\
\\
Compare 11 enterprise RAG platforms across architecture, connectors, deployment, security, and pricing. Includes turnkey, cloud, and open-source options with current 2026 pricing and analyst data.\\
\\
![Roshan Desai](https://onyx.app/_next/image?url=%2Favatars%2Frd-ghibli-pfp.png&w=48&q=75)\\
\\
Roshan Desai\\
\\
May 8, 2026](https://onyx.app/insights/enterprise-rag-platforms-2026) [AI Tools\\
\\
11 min read\\
\\
Best Open Source LLMs in 2026\\
\\
Compare 10 open-source and open-weight language models in Onyx's March 12, 2026 leaderboard snapshot. Benchmark data, license types, and API availability for Kimi K2.5, GLM-5, DeepSeek V3.2, Qwen 3.5, GPT-oss 120B, and more.\\
\\
![Roshan Desai](https://onyx.app/_next/image?url=%2Favatars%2Frd-ghibli-pfp.png&w=48&q=75)\\
\\
Roshan Desai\\
\\
May 5, 2026](https://onyx.app/insights/best-open-source-llms-2026) [AI Tools\\
\\
10 min read\\
\\
Best LLMs in 2026\\
\\
Compare leading large language models in Onyx's leaderboard snapshot. Benchmark data for Claude Opus 4.6, GPT-5.4, Gemini 3.1 Pro, Kimi K2.5, GLM-5, and more across SWE-bench, GPQA Diamond, and AIME.\\
\\
![Roshan Desai](https://onyx.app/_next/image?url=%2Favatars%2Frd-ghibli-pfp.png&w=48&q=75)\\
\\
Roshan Desai\\
\\
May 4, 2026](https://onyx.app/insights/best-llms-2026)

Best LLMs for Coding in 2026: SWE-bench, HumanEval, and LiveCode Rankings \| Onyx AI

Cookies Notice

This website utilizes third-party website tracking technologies such as cookies to enable essential functionalities as well as continually improve our services.

[Privacy Policy](https://onyx.app/legal/privacy-policy)

![Logo](<Base64-Image-Removed>)

### 来源 3: Top 7 LLMs for Coding in 2026 (SWE-bench, LiveCodeBench, Terminal-Bench) - Tech Jacks Solutions

- URL: https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding
- 精读方法：firecrawl-scrape

#### Gallery

#### Contacts

405 W. Greenlawn Ave Lansing, Michigan 48910

contact@techjacksolutions.com

+1-616-320-4064

[Twitter](https://x.com/GoTechJacks)[Facebook-f](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#)[Pinterest-p](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#)[Instagram](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#)

[Full Rankings](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-ranking) [How We Ranked](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-methodology) [1\. Claude Opus 4.6](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-opus) [2\. Gemini 3.1 Pro](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-gemini) [3\. MiniMax M2.5](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-minimax) [4\. GLM-5](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-glm) [5\. Kimi K2.5](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-kimi) [6\. Qwen 3.5-plus](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-qwen) [7\. GPT-5.3 Codex](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-codex) [Reading the Scores](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-caveats) [FAQ](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-faq)

Light / Dark

Rankings

# Top 7 LLMs for Coding in 2026 (SWE-bench, LiveCodeBench, Terminal-Bench)

We ranked the seven strongest coding models of early 2026 primarily by SWE-bench Verified, the most contamination-resistant agentic coding benchmark, with LiveCodeBench and Terminal-Bench 2.0 as secondary axes. Every score below is labeled as vendor-reported or independently measured, and the numbers reflect February to March 2026 snapshots that will shift over time.

80.8

SWE-bench Verified leader (Claude Opus 4.6)

Anthropic + Onyx, Feb-Mar 2026

83.6

LiveCodeBench leader (Qwen 3.5-plus)

Onyx independent tracker

77.3

Terminal-Bench 2.0 leader (GPT-5.3 Codex)

Independent, agentic shell tasks

7

Models ranked on shared axes

Verified Feb-Mar 2026

* * *

## The Full Rankings

This table covers all seven models at a glance. Click any model name to jump to its detailed breakdown below, or sort by any column to re-rank on a different axis. The Source column flags whether the figures are independently measured or include vendor-reported numbers. Scores are SWE-bench Verified percent, LiveCodeBench percent, and Terminal-Bench 2.0 percent.

| \# ↕ | Model ↕ | Org ↕ | SWE-bench Verified ↕ | LiveCodeBench ↕ | Terminal-Bench 2.0 ↕ | Source ↕ |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [Claude Opus 4.6](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-opus) | Anthropic | 80.8SWE lead | 76.0 | 65.4 | Vendor + Independent |
| 2 | [Gemini 3.1 Pro](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-gemini) | Google | 80.6 | 81.3 | 68.5 | Independent |
| 3 | [MiniMax M2.5](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-minimax) | MiniMax | 80.2 | 65.0 | 42.2 | Vendor + Independent |
| 4 | [GLM-5](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-glm) | Zhipu AI | 77.8 | 52.0 | 56.2 | Independent |
| 5 | [Kimi K2.5](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-kimi) | Moonshot AI | 76.8 | 85.0 | Not reported | Independent |
| 6 | [Qwen 3.5-plus](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-qwen) | Alibaba | 76.4 | 83.6LCB lead | 52.5 | Independent |
| 7 | [GPT-5.3 Codex](https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding/#section-codex) | OpenAI | Not independently reported (SWE-bench Pro 56.8) | 71.0 | 77.3Term lead | Independent |

_Sortable: click "SWE-bench Verified", "LiveCodeBench", or "Terminal-Bench 2.0" to re-rank. The two rows without an independent SWE-bench Verified figure sort to the bottom of that column._

* * *

## How We Ranked These Models

Methodology

Ranked primarily by SWE-bench Verified (real GitHub issues, contamination-resistant), with LiveCodeBench and Terminal-Bench 2.0 as secondary axes, as of February to March 2026. SWE-bench scores depend on the agentic scaffold. Vendor-reported versus independent is labeled. Saturated benchmarks such as HumanEval and GSM8K are excluded.

Where a model lacks an independently reported SWE-bench Verified score, we say so rather than substitute a different benchmark and treat it as equivalent. GPT-5.3 Codex is placed at the bottom of the primary axis for this reason and is included on the strength of its independent Terminal-Bench 2.0 result.

The three benchmarks measure different things, and a model can lead one while trailing another:

- **SWE-bench Verified** runs a model inside an agent harness against human-validated GitHub issues. It is the closest public proxy for "can this fix a real bug in a real repository," which is why it is our primary axis.
- **LiveCodeBench** uses a rolling set of recent competitive-programming problems collected after model training cutoffs, making it among the most contamination-resistant trackers for algorithmic coding.
- **Terminal-Bench 2.0** measures agentic shell and tool-use competence: navigating a filesystem, running commands, and completing multi-step terminal tasks.

Sources include independent trackers (Onyx AI, LLM-Stats, Artificial Analysis) and the public SWE-bench, LiveCodeBench, and Terminal-Bench leaderboards, cross-checked against vendor technical reports where independent figures were unavailable. Saturated benchmarks like HumanEval (above 93 percent across the field) and GSM8K (around 99 percent) are excluded because they no longer separate frontier models.

* * *

## 1\. Claude Opus 4.6 (Anthropic)

#1Claude Opus 4.6Anthropic

Claude Opus 4.6 takes the top spot on our primary axis with the highest SWE-bench Verified score in the group at 80.8 percent. The gap over second place is small, well within scaffold-driven noise, but Opus has been the most consistent performer across independent harnesses on real repository fixes. Its Terminal-Bench 2.0 result of 65.4 is mid-pack, and its LiveCodeBench figure of 76.0 trails the algorithmic specialists, so it is a strong generalist rather than a category winner everywhere.

80.8

SWE-bench Verified

76.0

LiveCodeBench

65.4

Terminal-Bench 2.0

**Best for:** Teams that want the most reliable agentic bug-fixing and refactoring across real codebases, especially when paired with a strong scaffold such as Claude Code.

**How to read this:** The SWE-bench Verified figure blends an Anthropic-reported result with an independent Onyx measurement. The lead over Gemini 3.1 Pro and MiniMax M2.5 is a fraction of a point, so treat the top three as effectively tied on this axis.

_Read more: [What Is Claude AI?](https://techjacksolutions.com/ai-tools/anthropic-claude/what-is-claude-ai/)_

* * *

## 2\. Gemini 3.1 Pro (Google)

#2Gemini 3.1 ProGoogle

Gemini 3.1 Pro is arguably the strongest all-rounder on this list. Its independent SWE-bench Verified result of 80.6 is statistically level with the leader, and it pairs that with a much higher LiveCodeBench score of 81.3 and the second-best Terminal-Bench 2.0 figure at 68.5. If you want one model that is competitive on real bug-fixing, algorithmic problems, and terminal agents at once, Gemini 3.1 Pro has the most balanced profile here.

80.6

SWE-bench Verified

81.3

LiveCodeBench

68.5

Terminal-Bench 2.0

**Best for:** Developers who want the most balanced single model across all three axes, particularly those already working in the Google ecosystem.

**How to read this:** All three figures here are independently measured (Onyx and officechai), which makes this one of the more defensible profiles in the group. The SWE-bench gap to rank one is two-tenths of a point.

_Read more: [What Is Google Gemini?](https://techjacksolutions.com/ai-tools/google-gemini/what-is-google-gemini/)_

* * *

## 3\. MiniMax M2.5 (MiniMax)

#3MiniMax M2.5MiniMax

MiniMax M2.5 rounds out the top tier on SWE-bench Verified at 80.2 percent, a genuinely strong result for real-repository bug fixing. The catch is that its strength is narrow: its LiveCodeBench score of 65.0 and especially its Terminal-Bench 2.0 result of 42.2 are the weakest agentic-terminal figure in the group. It is a focused repository-fixing model more than a do-everything coding assistant.

80.2

SWE-bench Verified

65.0

LiveCodeBench

42.2

Terminal-Bench 2.0

**Best for:** Pipelines focused tightly on resolving GitHub-style issues where terminal-agent breadth is less important than raw patch accuracy.

**How to read this:** The headline SWE-bench number blends a MiniMax-reported figure with an independent Onyx measurement. The low Terminal-Bench 2.0 result is a real gap, not noise, so do not assume top-three SWE-bench standing carries over to terminal agents.

* * *

## 4\. GLM-5 (Zhipu AI)

#4GLM-5Zhipu AI

GLM-5 posts a solid independent SWE-bench Verified score of 77.8, landing just below the top tier. Its Terminal-Bench 2.0 result of 56.2 is respectable, sitting between the leaders and the weaker terminal performers. The soft spot is LiveCodeBench at 52.0, the lowest algorithmic score here, which suggests it is more comfortable with applied repository work than with competitive-style problems.

77.8

SWE-bench Verified

52.0

LiveCodeBench

56.2

Terminal-Bench 2.0

**Best for:** Teams wanting a capable, independently benchmarked option for applied coding and terminal tasks without paying frontier-flagship prices.

**How to read this:** All three figures are independently sourced. The weak LiveCodeBench result means GLM-5 is a poorer fit for algorithm-heavy or competitive-programming workloads.

* * *

## 5\. Kimi K2.5 (Moonshot AI)

#5Kimi K2.5Moonshot AI

Kimi K2.5 is a study in why the primary axis matters. Its independent LiveCodeBench score of 85.0 is the highest algorithmic figure on this entire list, yet its SWE-bench Verified result of 76.8 places it fifth on our real-repository axis. No Terminal-Bench 2.0 figure has been independently reported for it. If competitive-style problem solving is your priority, Kimi punches well above its overall rank.

76.8

SWE-bench Verified

85.0

LiveCodeBench

Not reported

Terminal-Bench 2.0

**Best for:** Algorithmic and competitive-programming work, where its category-leading LiveCodeBench score is the most relevant signal.

**How to read this:** Ranked fifth because our primary axis is SWE-bench Verified, not LiveCodeBench. The missing Terminal-Bench 2.0 figure means its agentic-terminal competence is unverified here.

* * *

## 6\. Qwen 3.5-plus (Alibaba)

#6Qwen 3.5-plusAlibaba

Qwen 3.5-plus holds the LiveCodeBench crown among models with a full score set at 83.6 percent, edging out Gemini on that axis. Its SWE-bench Verified result of 76.4 is solid but places it sixth on our primary measure, and its Terminal-Bench 2.0 figure of 52.5 sits mid-table. Like Kimi, it is a reminder that a high algorithmic score does not automatically translate into top real-repository performance.

76.4

SWE-bench Verified

83.6

LiveCodeBench

52.5

Terminal-Bench 2.0

**Best for:** Algorithmic workloads where it leads LiveCodeBench among full-profile models, with an active open ecosystem behind it.

**How to read this:** All figures are independently sourced. Its sixth-place SWE-bench standing means it is a weaker pick for autonomous repository bug-fixing than the top three.

* * *

## 7\. GPT-5.3 Codex (OpenAI)

#7GPT-5.3 CodexOpenAI

GPT-5.3 Codex is the hardest model to place, which is exactly why it ranks seventh on a SWE-bench-first list. It has no independently reported SWE-bench Verified score; the closest public figure is SWE-bench Pro at 56.8, a harder and different benchmark that cannot be compared directly to the Verified numbers above. Where it clearly excels is agentic terminal work: it leads the group on Terminal-Bench 2.0 at 77.3, with a respectable LiveCodeBench result of 71.0.

Pro 56.8

SWE-bench Verified n/a

71.0

LiveCodeBench

77.3

Terminal-Bench 2.0

**Best for:** Agentic terminal and tool-use workflows, where its category-leading Terminal-Bench 2.0 score is the most relevant benchmark.

**How to read this:** Ranked last on the primary axis only because no comparable SWE-bench Verified figure exists, not because it is a weak coder. The SWE-bench Pro 56.8 number is a different, tougher benchmark and is shown for context, not as a Verified-equivalent score.

_Read more: [What Is ChatGPT?](https://techjacksolutions.com/ai-tools/chatgpt/what-is-chatgpt/)_

* * *

## Reading the Scores: Three Things That Change the Ranking

Benchmark tables look authoritative, but coding scores carry caveats that can flip a ranking. Keep these three in mind before you treat any number as settled.

Scores are scaffold-dependent

SWE-bench Verified and Terminal-Bench 2.0 run a model inside an agent harness. The same model can score noticeably higher or lower depending on the scaffold, for example Claude Code versus a generic Codex-style CLI. Read every figure as a model-plus-scaffold result, not pure model capability.

Saturated benchmarks are excluded

HumanEval (above 93 percent across the field) and GSM8K (around 99 percent) are saturated and contamination-prone, so they no longer separate frontier models. We exclude them from ranking. If a comparison leans on those numbers, treat its conclusions with caution.

Some standings are still pending

Newer releases such as DeepSeek V4-Pro and Kimi K2.6 lack public, independently reported coding benchmarks at the time of writing. We do not rank what we cannot verify. The table will be revised when contamination-resistant scores are published, rather than filled in with estimates.

The practical takeaway: the top three on SWE-bench Verified are effectively tied, so pick based on your actual workload. Choose for real-repository bug fixing on the SWE-bench axis, for algorithmic problems on LiveCodeBench, and for terminal-agent tasks on Terminal-Bench 2.0. Then verify current standings yourself, because these are February to March 2026 snapshots and the leaderboards move.

* * *

## Frequently Asked Questions

### What is the best LLM for coding in 2026?

By SWE-bench Verified, the most contamination-resistant agentic coding benchmark, Claude Opus 4.6 leads at 80.8 percent, with Gemini 3.1 Pro at 80.6 and MiniMax M2.5 at 80.2 close behind. That top three is effectively tied. The right model depends on your task: Qwen 3.5-plus leads LiveCodeBench (83.6) among full-profile models for competitive-style problems, and GPT-5.3 Codex leads Terminal-Bench 2.0 (77.3) for shell and tool-use work.

### Why is SWE-bench Verified used as the primary ranking signal?

SWE-bench Verified draws from real, human-validated GitHub issues, so it measures whether a model can resolve genuine software bugs rather than recite memorized answers. It is more contamination-resistant than saturated benchmarks like HumanEval (above 93 percent) and GSM8K (around 99 percent), which we exclude. The main caveat is that SWE-bench scores depend on the agentic scaffold used to run the model.

### What does scaffold-dependent mean for these scores?

Agentic coding benchmarks run a model inside a harness that plans, edits files, runs tests, and retries. The same model can score noticeably higher or lower depending on the scaffold, for example Claude Code versus a generic Codex-style CLI. Compare scores as model-plus-scaffold results, not pure model capability, and treat small gaps between top models as noise.

### Why is GPT-5.3 Codex ranked seventh if it leads Terminal-Bench?

Our primary ranking axis is SWE-bench Verified, and GPT-5.3 Codex has no independently reported Verified score at the time of writing. Its available figure is SWE-bench Pro at 56.8, a harder and different benchmark that cannot be placed on the same axis as the others. It still leads Terminal-Bench 2.0 at 77.3, which is why it earns a spot on the list.

### Where do DeepSeek and Kimi fit in this ranking?

Kimi K2.5 is included at rank five, and it actually leads LiveCodeBench at 85.0. Newer releases such as DeepSeek V4-Pro and Kimi K2.6 lack public, independently reported coding benchmarks at the time of writing, so we do not rank them. We will revise the table once contamination-resistant scores are published rather than estimate placements.

* * *

## Video Resources

[SWE-bench Verified Explained\\
\\
YouTube Search\\
\\
How the real-GitHub-issue benchmark works and why scaffolds matter](https://www.youtube.com/results?search_query=SWE-bench+Verified+explained+LLM+coding+benchmark) [Best LLMs for Coding in 2026 Compared\\
\\
YouTube Search\\
\\
Hands-on comparisons of frontier coding models across tasks](https://www.youtube.com/results?search_query=best+LLM+for+coding+2026+benchmark+comparison) [LiveCodeBench and Terminal-Bench Walkthrough\\
\\
YouTube Search\\
\\
What the secondary axes measure and how to read agentic scores](https://www.youtube.com/results?search_query=LiveCodeBench+Terminal-Bench+agentic+coding+benchmark)

Related Reading

[Ranking\\
Top 10 Open-Weight LLMs\\
\\
The open-weight leaderboard ranked by Arena Elo, with restrictive licenses flagged.](https://techjacksolutions.com/ai-tools/rankings/top-open-weight-llms/) [Ranking\\
Top 8 Cheapest Frontier AI APIs\\
\\
Price per 1M tokens at frontier capability, with the cost-versus-capability tradeoff.](https://techjacksolutions.com/ai-tools/rankings/cheapest-frontier-ai-apis/) [Ranking\\
Top 6 LLMs by Context Window\\
\\
Advertised maximum versus RULER-effective context, and why models use only 50 to 65 percent.](https://techjacksolutions.com/ai-tools/rankings/llms-by-context-window/) [Breakdown\\
The LLM Benchmark Landscape\\
\\
What MMLU-Pro, SWE-bench, GPQA, and Arena Elo actually measure, and how to read them.](https://techjacksolutions.com/ai-tools/meta-llama/llm-benchmark-landscape/)

### Go Deeper

Resources from across Tech Jacks Solutions

[AI Tools Hub\\
\\
Vendor breakdowns, comparisons, and rankings across the AI tooling landscape](https://techjacksolutions.com/ai-tools/) [Prompt Engineering Library\\
\\
Prompting techniques that get better code out of any model](https://techjacksolutions.com/prompt-engineering-library/) [AI Career Paths\\
\\
Roles that work with these models and tools daily](https://techjacksolutions.com/tech-jobs-career-hub/) [AI Glossary\\
\\
Definitions for benchmark and model terms used in this article](https://techjacksolutions.com/ai-glossary/)

Ranked from SWE-bench Verified, LiveCodeBench, and independent trackers, data as of Feb-Mar 2026. Scores shift; verify current standings.

Claude and Claude Opus are trademarks of Anthropic. Gemini is a trademark of Google LLC. GPT and Codex are trademarks of OpenAI. MiniMax is a trademark of MiniMax. GLM is a trademark of Zhipu AI. Kimi is a trademark of Moonshot AI. Qwen is a trademark of Alibaba Group. SWE-bench, LiveCodeBench, and Terminal-Bench are the property of their respective maintainers. All other trademarks belong to their respective owners. Tech Jacks Solutions is not affiliated with or endorsed by any of the organizations mentioned.

Before You Use AI

Your Privacy

Coding assistants process your source code and prompts on remote servers unless you run an open-weight model locally. Free and consumer tiers often retain inputs and may use them for training, while commercial API and enterprise tiers generally do not. Before pasting proprietary code, internal repositories, or secrets into any model from Anthropic, Google, OpenAI, Alibaba, MiniMax, Zhipu, or Moonshot, review that vendor's data retention and training policy and prefer enterprise or zero-retention tiers for sensitive work.

[Anthropic Privacy Policy](https://www.anthropic.com/privacy) [Google Privacy Policy](https://policies.google.com/privacy) [OpenAI Privacy Policy](https://openai.com/policies/privacy-policy)

Mental Health & AI Dependency

Coding models are designed to be helpful and always available, which can quietly erode the practice of reasoning through problems yourself. Notice when you reach for a model to avoid thinking versus to accelerate work you understand, and keep building your own debugging and design judgment. If you or someone you know is experiencing a mental health crisis:

- **988 Suicide & Crisis Lifeline** \-\- Call or text 988 (US)
- **SAMHSA Helpline** \-\- 1-800-662-4357
- **Crisis Text Line** \-\- Text HOME to 741741

AI systems can produce plausible-sounding but incorrect guidance. For mental health, medical, legal, or financial decisions, always consult a qualified professional.

[NIST AI Risk Framework](https://airc.nist.gov/Home)

Your Rights & Our Transparency

Under GDPR and CCPA, you have the right to access, correct, and delete the personal data an AI provider holds about you, and each vendor has its own process for exercising those rights. Tech Jacks Solutions maintains editorial independence. This ranking was not sponsored, reviewed, or approved by any vendor listed, and we receive no affiliate commissions from the models covered. Rankings reflect independent benchmark trackers and public leaderboards, with vendor-reported figures labeled as such. The EU AI Act classifies general-purpose AI systems under Article 52 transparency obligations.

[AI Governance Hub](https://techjacksolutions.com/ai-governance-hub/) [EU AI Act Overview](https://techjacksolutions.com/eu-ai-act/) [Cybersecurity News Center](https://techjacksolutions.com/cybersecurity-news-center/)

**We value your privacy**

We use cookies for analytics and advertising. [Privacy Policy](https://techjacksolutions.com/privacy-policy/) · [Cookie Policy](https://techjacksolutions.com/cookie-policy/)

Show details

**Strictly Necessary** Always active

Essential for the site to function. Can't be turned off.

**Analytics**

Helps us understand which pages are visited and how users navigate. Aggregated and anonymous via Google Analytics.

**Advertising**

Measures campaign performance via Google Ads. May share data with Google for ad personalization.

Accept AllAnalytics OnlyReject Non-Essential

### 来源 4: Kimi K2.5: Visual Agentic Intelligence

- URL: https://arxiv.org/html/2602.02276
- 精读方法：jina-readerlm-academic

```markdown
### Table 4: Benchmarks

#### Reasoning Benchmarks

- **HLE-Full**: 30.1%
- **AIME 2025**: 96.1%
- **HMMT Feb 2025**: 95.4%
- **GPQA-Diamond**: 87.6%

#### LongBench v2

- **WideSearch**: 79.0%
- **DeepSearchQA**: 35.4%
- **FinSearchComp T2&T3**: 49.7%

#### Computer Use Capability

- **Seal-QA**: Raising the bar for reasoning in search-augmented language models
- **PaperBench**: Evaluating AI's ability to replicate AI research
```

### 来源 5: 2026 AI编程能力评测：八大模型全面对比 - UniFuncs

- URL: https://unifuncs.com/s/RYSb15zp
- 精读方法：firecrawl-scrape

![logo](https://s.unifuncs.com/_next/image?url=%2Fdeepsearch%2Flogo.png&w=640&q=75)

新的搜索

通过API将深度搜索接入到您的系统

我 \- 03-01 08:57

GLM-5, QWen-3.5 Plus, Deepseek V3.2，Kimi K2.5, Seed-2-Code,Minimax M2.5, Opus 4.6, gpt-5.3-codex 这几个模型在编程能力上的客观评价。

最后一定要列表进行总结。

复制

标准深搜 03-01 08:57

推理完成

让我分析一下这个用户查询：

用户想要对以下8个AI模型的编程能力进行客观评价：

1. GLM-5
2. QWen-3.5 Plus
3. Deepseek V3.2
4. Kimi K2.5
5. Seed-2-Code
6. Minimax M2.5
7. Opus 4.6
8. gpt-5.3-codex

这些模型看起来都是代码编程相关的AI模型，有些可能是知名模型的新版本（如GPT系列），有些可能是我还不熟悉的新模型。

根据系统要求，我需要：

1. 首先理解用户需求：用户想要这些模型在编程能力上的客观评价，最后要列表总结
2. 这是技术评估类查询，时效性要求高（AI模型更新很快）
3. 我需要搜索每个模型的具体信息、评测结果、性能对比等
4. 最后需要结构化呈现，用表格或列表总结

让我先规划搜索策略：

首先，我需要识别这些模型：

- GLM-5：可能是智谱AI的GLM系列最新版本
- QWen-3.5 Plus：可能是阿里通义千问的版本
- Deepseek V3.2：深度求索的模型
- Kimi K2.5：Moonshot AI的Kimi系列
- Seed-2-Code：这可能是某个公司的代码模型
- Minimax M2.5：Minimax的模型
- Opus 4.6：可能是Anthropic的Claude Opus系列
- gpt-5.3-codex：OpenAI的GPT系列代码模型

我需要：

1. 确认这些模型是否真实存在（避免幻觉）
2. 获取它们的最新编程能力评测数据
3. 找到权威的对比评测（如HumanEval、MBPP等标准基准）
4. 收集各模型的特点、优势、局限

让我设计搜索关键词：

初步搜索策略：

- 搜索AI编程模型2025-2026最新评测（因为现在是2026年3月）
- 搜索各个模型的具体信息（确认存在性）
- 搜索编程能力基准测试对比

我需要并行调用搜索来获取信息。让我先进行基础搜索：

搜索关键词设计：

1. "AI编程模型2026最新评测" - 获取整体趋势和权威评测
2. "GLM-5 编程能力 评测"
3. "QWen-3.5 Plus code generation benchmark"
4. "Deepseek V3.2 programming performance"
5. "Kimi K2.5 code ability"
6. "Seed-2-Code model evaluation"
7. "Minimax M2.5 programming benchmark"
8. "Claude Opus 4.6 coding"
9. "GPT-5.3 Codex performance"

让我开始执行搜索。

我来帮您对这些AI编程模型进行深度搜索和客观评价。让我先分析查询需求并制定搜索策略。

## 🎯 查询需求分析

**核心需求：**

- 对8个AI模型的编程能力进行 **客观、基于实证** 的评价
- 需要覆盖：代码生成、算法能力、调试能力、多语言支持等维度
- 最终需要 **结构化列表总结** （便于对比）

**信息维度规划：**

1. **模型存在性验证** ：确认这些模型是否真实存在及版本准确性
2. **权威基准测试** ：HumanEval、MBPP、SWE-bench等标准编程评测
3. **性能对比数据** ：pass@k、准确率等量化指标
4. **特点与局限** ：各模型的专长领域、支持语言、实际应用表现
5. **时效性要求** ：AI模型更新快，必须优先2025-2026年最新数据

## 🔍 搜索策略设计

让我从多个角度并行搜索，确保信息全面性和可靠性：

AI编程模型2026最新评测 HumanEval MBPP benchmark

GLM-5 智谱AI 编程能力 代码生成评测

QWen-3.5 Plus 通义千问 编程 benchmark 2025 2026

Deepseek V3.2 深度求索 编程性能 代码能力

Kimi K2.5 Moonshot AI 编程能力评测

Seed-2-Code model evaluation programming

Minimax M2.5 programming benchmark code

Claude Opus 4.6 Anthropic coding performance 2026

GPT-5.3 Codex OpenAI programming benchmark 2025 2026

推理完成

搜索结果已经返回了很多信息。让我分析一下当前的状态：

1. 我已经执行了多个搜索查询，获取了关于这些模型的大量信息
2. 大部分搜索都返回了相关的结果，时效性也很好（2026年的信息）
3. 但是，我注意到搜索结果中有一些需要验证的问题：
   - 有些模型名称可能需要确认（比如"gpt-5.3-codex"是否准确）
   - 需要阅读详细内容来确认这些模型的编程能力具体表现
   - 需要获取具体的基准测试数据

让我先总结一下从搜索结果中获得的关键信息：

**Kimi K2.5** (Moonshot AI):

- 2026年1月27日发布
- 视觉编程能力强
- 在HLE全集50.2%，BrowseComp 74.9%
- 接近Claude Opus 4.5的编码能力
- SWE-Bench Verified 77.8% (与GLM-5相同)

**GLM-5** (智谱AI):

- 2026年2月发布
- SWE-Bench Verified 77.8%
- 744B参数MoE架构
- 在Artificial Analysis榜单全球第四、开源第一
- 文本/代码竞技场与Claude Opus等商业模型同档

**Minimax M2.5** :

- 2026年2月12日发布
- SWE-Bench Verified 80.2%
- 230B参数MoE，激活10B
- 成本较低
- 在多语言编程方面表现突出

**GPT-5.3-Codex** (OpenAI):

- 2026年2月5日发布
- Terminal-Bench 2.0: 77.3%
- SWE-Bench Pro: 领先
- 25% faster than predecessor
- 在终端/CLI任务上表现突出

**Claude Opus 4.6** (Anthropic):

- 2026年2月5日发布
- SWE-Bench Verified: 81.42%
- Terminal-Bench 2.0: 65.4%
- OSWorld: 72.7%
- 200K context (1M beta)
- 在计算机使用/GUI方面领先

**Deepseek V3.2** :

- 2025年12月1日发布
- 性能对标GPT-5
- 推理能力大幅增强
- 编程能力显著提升
- 有V3.2-Speciale版本

**QWen-3.5 Plus** (阿里通义千问):

- 2026年2月发布
- 397B总参数，激活170B
- 开源模型
- 性能媲美Gemini 3 Pro
- 对中文注释、国内开发文档理解好

**Seed-2-Code** (字节跳动):

- 需要进一步验证具体信息
- 有Seed2.0系列和专门的Code模型
- 支持200+编程语言

现在我需要更深入地阅读一些关键来源来获取确切的编程能力评测数据，特别是：

1. OpenAI官方关于GPT-5.3-Codex的详细评测
2. Anthropic关于Claude Opus 4.6的技术规格
3. 智谱AI关于GLM-5的完整技术报告
4. Minimax M2.5的详细编程基准数据
5. Kimi K2.5的编程能力详细评测
6. Deepseek V3.2的编程基准数据
7. QWen-3.5 Plus的编程能力具体表现
8. Seed-2-Code的具体评测数据

让我选择最权威的来源进行深度阅读。

[GPT-5.3-Codex programming benchmark SWE-Bench Terminal-Bench performance evaluation](https://openai.com/index/introducing-gpt-5-3-codex/ "GPT-5.3-Codex 正式登场 | OpenAI")

[Claude Opus 4.6 coding benchmark SWE-Bench Terminal-Bench performance evaluation](https://www.anthropic.com/news/claude-opus-4-6 "Claude Opus 4.6 \ Anthropic")

[GLM-5 SWE-Bench Verified 77.8% programming benchmark technical report](https://zhuanlan.zhihu.com/p/2009393352567697921 "智谱新年的第一篇论文：GLM-5 技术报告解读来了！ - 知乎")

[Minimax M2.5 SWE-Bench Verified 80.2% programming benchmark performance](https://www.minimax.io/news/minimax-m25 "MiniMax M2.5: Built for Real-World Productivity. - MiniMax News | MiniMax")

[Kimi K2.5 programming benchmark SWE-Bench coding performance evaluation](https://news.qq.com/rain/a/20260127A051UK00 "Kimi K2.5 正式发布：代码能力再次强悍升级，全球最强开源视觉智能体!_腾讯新闻")

[Qwen3.5-Plus programming benchmark HumanEval MBPP code generation performance](https://www.ithome.com/0/922/114.htm "阿里除夕夜炸场：“开源旗舰”Qwen3.5 发布，登顶全球最强开源模型 - IT之家")

[DeepSeek V3.2 programming benchmark code generation performance evaluation](https://api-docs.deepseek.com/zh-cn/news/news251201 "DeepSeek V3.2 正式版：强化 Agent 能力，融入思考推理 | DeepSeek API Docs")

[Seed-Coder ByteDance programming benchmark code generation performance](https://bytedance-seed-coder.github.io/ "Seed-Coder")

推理完成

好的，我已经从深度阅读中获得了很多关键信息。现在让我整理一下：

**已获取的确切数据：**

1. **Kimi K2.5** (Moonshot AI):
   - SWE-bench Verified: 76.8%
   - MMMU Pro: 78.5%
   - VideoMMMU: 86.6%
   - HLE全集: 50.2%
   - BrowseComp: 74.9%
   - 发布时间：2026年1月27日
2. **GLM-5** (智谱AI):
   - SWE-bench Verified: 77.8%
   - BrowseComp: 75.9%
   - Artificial Analysis Intelligence Index: 50分
   - 发布时间：2026年2月
3. **Minimax M2.5** :
   - SWE-Bench Verified: 80.2%
   - Multi-SWE-Bench: 51.3%
   - BrowseComp: 76.3%
   - 比M2.1快37%
   - 与Claude Opus 4.6速度相当
   - 发布时间：2026年2月12日
4. **GPT-5.3-Codex** (OpenAI):
   - SWE-Bench Pro: 顶尖水平（未提供具体数字）
   - Terminal-Bench 2.0: 创纪录（未提供具体数字）
   - Token消耗比以往任何模型都少
   - 发布时间：2026年2月5日
5. **Claude Opus 4.6** (Anthropic):
   - SWE-bench Verified: 81.42%
   - Terminal-Bench 2.0: 领先所有模型
   - BrowseComp: 领先
   - GDPval-AA: 比GPT-5.2高144 Elo，比Opus 4.5高190 Elo
   - 发布时间：2026年2月5日
6. **Deepseek V3.2** :
   - 性能对标GPT-5
   - ICPC World Finals 2025金牌（人类第二名水平）
   - 编程能力显著提升
   - 发布时间：2025年12月1日
7. **QWen-3.5 Plus** (阿里):
   - MMLU-Pro: 87.8分，超越GPT-5.2
   - GPQA: 88.4分，高于Claude 4.5
   - IFBench: 76.5分，刷新所有模型纪录
   - Browsecomp: 超越Gemini 3 Pro
   - 总参数397B，激活170B
   - 发布时间：2026年2月16日
8. **Seed-Coder** (字节跳动):
   - 8B参数规模
   - SWE-bench Verified: 未提供具体数字，但说在~8B模型中最佳
   - Multi-SWE-bench mini: 表现优异
   - IOI'2024: 超越QwQ-32B和DeepSeek-R1
   - Codeforces: ELO评分与o1-mini相当

我还需要补充一些信息：

1. Deepseek V3.2的具体编程基准数据
2. QWen-3.5 Plus的具体编程基准数据（HumanEval, MBPP等）
3. 是否还有其他相关的编程基准测试对比

让我再搜索一些具体的编程基准测试数据，特别是这些模型在HumanEval、MBPP等经典基准上的表现。

[GPT-5.3-Codex specific benchmark scores Terminal-Bench 2.0 SWE-Bench Pro exact numbers](https://www.morphllm.com/best-ai-model-for-coding "Best AI Model for Coding 2026: Codex 5.3 vs Opus 4.6 vs Gemini vs DeepSeek | Morph")

[Kimi K2.5 detailed benchmark scores SWE-bench Verified MMMU Pro coding evaluation](https://zhuanlan.zhihu.com/p/2001617342354974091 "Kimi K2.5开箱评测：性能数据亮眼，但实测体验真的如此吗？ - 知乎")

[Qwen3.5-Plus HumanEval MBPP coding benchmark scores performance](https://juejin.cn/post/7609481369001115667 "2026 Q1 AI 编程大模型横评与订阅指南2026 Q1 AI 编程大模型横评与订阅指南 进入 2026 年，AI - 掘金")

[DeepSeek V3.2 programming benchmark scores SWE-Bench code generation](https://zhuanlan.zhihu.com/p/1979096243872477619 "DeepSeek-V3.2 正式发布：开源模型的“反击时刻”，Speciale 版比肩 GPT-5 - 知乎")

[2026 AI coding models benchmark comparison HumanEval MBPP SWE-Bench](https://adg.csdn.net/694cf0c65b9f5f31781a9408.html "国内编程大模型哪家强？2025年最新排行榜与深度解析_人工智能_i建模-火山引擎 ADG 社区")

推理完成

让我回顾一下当前的情况：

用户要求对8个AI模型的编程能力进行客观评价，并最后用列表总结。这8个模型是：

1. GLM-5
2. QWen-3.5 Plus
3. Deepseek V3.2
4. Kimi K2.5
5. Seed-2-Code
6. Minimax M2.5
7. Opus 4.6
8. gpt-5.3-codex

我已经完成了大量的搜索和深度阅读，获取了以下关键信息：

**已获取的确切编程基准数据：**

1. **Claude Opus 4.6** (Anthropic):
   - SWE-bench Verified: 81.42%
   - Terminal-Bench 2.0: 领先（但具体数字未提供，根据另一来源65.4%可能是Sonnet 4.6的数据）
   - 上下文窗口: 200K (1M beta)
   - 发布日期: 2026年2月5日
2. **GPT-5.3-Codex** (OpenAI):
   - SWE-Bench Pro: 顶尖水平（具体未提供，但~80%）
   - Terminal-Bench 2.0: 77.3%
   - 上下文窗口: 256K tokens
   - Token效率: 比前代少2-4倍
   - 速度: 比前代快25%
   - 发布日期: 2026年2月5日
3. **Minimax M2.5** :
   - SWE-Bench Verified: 80.2%
   - Multi-SWE-Bench: 51.3%
   - BrowseComp: 76.3%
   - 速度: 比M2.1快37%，与Claude Opus 4.6相当
   - 上下文窗口: 未明确，但提到204K
   - 发布日期: 2026年2月12日
4. **GLM-5** (智谱AI):
   - SWE-bench Verified: 77.8%
   - BrowseComp: 75.9%
   - Artificial Analysis Intelligence Index: 50分
   - LiveCodeBench Pro: ~2650 (ELO评分)
   - 上下文窗口: 128K
   - 发布日期: 2026年2月
5. **Kimi K2.5** (Moonshot AI):
   - SWE-bench Verified: 76.8%（来源1），77.8%（其他来源可能）
   - MMMU Pro: 78.5%
   - VideoMMMU: 86.6%
   - HLE全集: 50.2%
   - BrowseComp: 74.9%
   - 发布日期: 2026年1月27日
6. **QWen-3.5 Plus** (阿里通义千问):
   - SWE-bench Verified: 70.6%（根据2026 Q1横评）
   - LiveCodeBench Pro: ~2580 (ELO评分)
   - 上下文窗口: 128K
   - 总参数: 397B，激活170B
   - 发布日期: 2026年2月16日
   - 多模态能力突出
7. **Deepseek V3.2** (深度求索):
   - LiveCodeBench: 标准版83.3%，Speciale版88.7%
   - GPT-5 High: 84.5%
   - Gemini-3.0 Pro: 90.7%
   - Codeforces评分: Speciale版2701分
   - ICPC World Finals 2025: 金牌（人类第二名水平）
   - 发布日期: 2025年12月1日
8. **Seed-Coder** (字节跳动):
   - 参数规模: 8B
   - SWE-bench Verified: 未提供具体数字，但表示在~8B模型中最佳
   - Multi-SWE-bench mini: 表现优异
   - IOI'2024: 超越QwQ-32B和DeepSeek-R1
   - Codeforces: ELO评分与o1-mini相当
   - 主要针对小参数模型优化

我注意到这些模型在SWE-bench Verified和LiveCodeBench等关键编程基准上呈现出明显的能力梯队。顶级模型如Claude Opus 4.6和GPT-5.3-Codex表现突出，而Minimax M2.5和GLM-5紧随其后。不同模型在特定领域如多模态、小参数优化等方面各有特色。

关于"Opus 4.6"，搜索结果显示这确实是Anthropic的模型，但用户可能期望看到具体的能力对比。我需要进一步确认这个版本的具体细节，特别是在编程能力上的实际表现。

对于"gpt-5.3-codex"，目前搜索结果显示OpenAI的GPT-5.3-Codex确实存在，这验证了用户查询的准确性。

接下来我将聚焦于整理现有数据，检查是否有遗漏的关键信息，特别是Seed-2-Code的具体性能指标和深度seek V3.2的SWE-bench Verified数据。同时，我将确保所有数据都有可靠来源支持。

现在让我补充一些关键信息，特别是确认所有模型的存在性和版本准确性：

"Opus 4.6" Anthropic official model 2026

"GPT-5.3 Codex" OpenAI official 2026

"Seed-2-Code" ByteDance Doubao programming model

推理完成

好的，让我整理一下目前的发现：

## 模型存在性验证

1. **GLM-5** ✅ \- 智谱AI的旗舰模型，2026年2月发布，真实存在
2. **QWen-3.5 Plus** ✅ \- 阿里通义千问的模型，2026年2月16日发布，真实存在
3. **Deepseek V3.2** ✅ \- 深度求索的模型，2025年12月1日发布，真实存在
4. **Kimi K2.5** ✅ \- Moonshot AI的模型，2026年1月27日发布，真实存在
5. **Seed-2-Code** ✅ \- 字节跳动的模型，2026年2月发布，是Seed 2系列中的Code版本，真实存在
6. **Minimax M2.5** ✅ \- MiniMax的模型，2026年2月12日发布，真实存在
7. **Opus 4.6** ✅ \- Anthropic的Claude Opus 4.6，2026年2月5日发布，真实存在
8. **gpt-5.3-codex** ✅ \- OpenAI的GPT-5.3-Codex，2026年2月5日发布，真实存在

所有模型都是真实存在的，发布时间都在2025-2026年，都是最新的模型。

## 编程能力数据汇总

现在让我基于已收集的信息，整理各模型的编程能力数据。我注意到有些模型在某些基准测试上的数据不完整，我需要诚实地指出这一点。

### 已确认的编程基准数据

**SWE-bench Verified** (修复真实GitHub仓库bug的能力):

- Claude Opus 4.6: 81.42% 182

- Minimax M2.5: 80.2% 185

- GPT-5.3-Codex: ~80% (约等) 190

- GLM-5: 77.8% 183

- Kimi K2.5: 76.8% 178

- Qwen3.5-Plus: 70.6% 189

- Deepseek V3.2: 标准版SWE-Verified数据未直接给出，但提到大幅缩短与闭源模型差距186

**Terminal-Bench 2.0** (终端操作技能):

- GPT-5.3-Codex: 77.3% 190
- Claude Opus 4.6: 65.4% 190

**LiveCodeBench / Codeforces** (算法竞赛能力):

- Deepseek V3.2-Speciale: LiveCodeBench 88.7, Codeforces 2701分186
- GPT-5.3-Codex: LiveCodeBench 2887 (推测) 189
- Gemini 3.1 Pro: LiveCodeBench 2887 189
- Claude Opus 4.6: LiveCodeBench ~2850 189
- Minimax M2.5: LiveCodeBench ~2720 189
- GLM-5: LiveCodeBench ~2650 189
- Qwen3.5-Plus: LiveCodeBench ~2580 189

**Multi-SWE-bench** (多语言编程):

- Minimax M2.5: 51.3% 185

**BrowseComp** (信息搜索与整合):

- GLM-5: 75.9% 183
- Minimax M2.5: 76.3% 185
- Kimi K2.5: 74.9% 178

**其他维度:**

- Kimi K2.5: MMMU Pro 78.5%, VideoMMMU 86.6% 178
- Qwen3.5-Plus: 在MMLU-Pro、GPQA等通用基准上有高分，但编程专项相对较弱180

**上下文窗口大小:**

- Claude Opus 4.6: 200K (1M beta) 182
- GPT-5.3-Codex: 256K 190
- Minimax M2.5: 204K 189
- GLM-5: 128K 183
- Qwen3.5-Plus: 128K 189

## 信息缺口识别

我发现以下信息缺失或不完整：

1. Deepseek V3.2 的 SWE-bench Verified 具体分数
2. Seed-Coder (8B参数) 的 SWE-bench Verified 具体分数
3. 部分模型在 HumanEval、MBPP 等经典基准上的表现
4. 各模型的多语言编程支持细节
5. 更详细的成本效益对比

但是，根据系统要求，我不应该过度搜索。目前我已经有了足够的权威数据来给出一个相对全面的评价。主要权威来源包括：

- OpenAI官方发布
- Anthropic官方发布
- MiniMax官方发布
- 智谱AI官方技术报告
- Moonshot AI官方发布
- 第三方评测（如Morph、2026 Q1横评等）

## 验证需求

我需要验证以下几点：

1. 所有数据是否都有可靠来源？
   - SWE-bench Verified数据：大部分有明确来源
   - 其他基准：部分来自第三方评测，需要标注置信度
2. 是否存在矛盾信息？
   - Kimi K2.5的SWE-bench Verified：腾讯新闻说是76.8%，但其他来源有说77.8%（可能与GLM-5相同）。我需要采用最权威的来源。腾讯新闻引用的是官方数据，应该以76.8%为准。
3. 时效性：所有数据都是2026年1-2月的最新数据，符合要求。

现在我可以开始准备最终报告了。根据要求，我需要：

1. 先进行简要的需求分析和搜索策略说明
2. 呈现核心发现
3. 用列表进行总结对比
4. 标注置信度和来源
5. 使用emoji增强表达
6. 保持客观、批判性思维

让我开始撰写最终回答。

基于已获取的权威信息，我现在可以为您提供这8个AI模型编程能力的客观评价。

## 🎯 需求分析与搜索策略

**核心需求识别：**

- 对8个指定模型进行 **编程能力** 的客观、实证评价
- 需要覆盖代码生成、工程任务解决、算法能力等多个维度
- 最终要求 **结构化列表总结** （便于对比）

**信息维度规划：**

1. **模型真实性验证** ：确认所有模型存在且版本准确 ✅
2. **权威基准测试** ：SWE-bench Verified（真实GitHub问题修复）、Terminal-Bench 2.0（终端操作）、LiveCodeBench（算法竞赛）等
3. **量化性能数据** ：Pass@k、准确率、ELO评分等
4. **时效性保证** ：所有数据均为2025-2026年最新发布（2026年3月1日当前）
5. **多源交叉验证** ：官方发布 \+ 第三方评测

* * *

## 📊 核心发现总结

### 🔝 第一梯队：编程能力顶尖（SWE-bench > 80%）

| 模型 | SWE-bench Verified | Terminal-Bench 2.0 | LiveCodeBench | 核心优势 |
| --- | --- | --- | --- | --- |
| **Claude Opus 4.6** | **81.42%** 🥇 | 65.4% | ~2850 | 多文件重构、长上下文(1M)、深度推理 |
| **Minimax M2.5** | **80.2%** 🥈 | - | ~2720 | 速度最快（37%提升）、成本效益高 |
| **GPT-5.3-Codex** | ~80% | **77.3%** 🥇 | ~2887 | **终端操作最强** 、Token效率高2-4倍 |
| **Deepseek V3.2-Speciale** | - | - | **2887** 🥇 | **算法竞赛最强** 、Codeforces 2701分 |

### 🥈 第二梯队：编程能力优秀（SWE-bench 75-80%）

| 模型 | SWE-bench Verified | 核心特点 |
| --- | --- | --- |
| **GLM-5** | **77.8%** | 开源模型最高、Agentic Engineering领先 |
| **Kimi K2.5** | **76.8%** | 视觉编程能力突出、智能体集群 |
| **Claude Sonnet 4.6** | 79.6% | 性价比高、Opus 4.6的90%能力 |

### 🥉 第三梯队：编程能力良好（SWE-bench < 75%）

| 模型 | SWE-bench Verified | 核心特点 |
| --- | --- | --- |
| **Qwen3.5-Plus** | **70.6%** | 中文技术栈理解领先、多模态支持 |
| **Deepseek V3.2** 标准版 | 约66-70% | 性价比极高、开源生态丰富 |

### 🔧 专业编程模型（小参数优化）

| 模型 | 参数规模 | 特点 |
| --- | --- | --- |
| **Seed-Coder** | **8B** | 小模型SOTA、SWE-bench Verified在8B级最佳 |

* * *

## 📋 详细评价报告

### 1️⃣ **Claude Opus 4.6** (Anthropic) 🏆

**发布时间：** 2026年2月5日182

**核心编程能力：**

- 🎯 **SWE-bench Verified: 81.42%**
- 当前所有模型最高分182
- 💻 **Terminal-Bench 2.0: 65.4%**
- 终端操作能力强劲190
- 🧠 **推理深度** ：在GPQA Diamond、MMLU Pro等推理基准领先182
- 📜 **上下文窗口** ：200K标准，1M beta - 支持超大型项目182

**独特优势：**

- ✅多文件重构能力最强，可处理10+文件的复杂修改190
- ✅ 意图理解能力突出，能处理模糊需求190
- ✅ 代码审查能力强，提供深度架构洞察190
- ✅ 在真实软件工程任务中表现最稳定

**局限：**

- ⚠️ Token消耗较大（思考过程长）190
- ⚠️ 响应速度相对较慢190
- 💰 价格较高：$5/$25 per million tokens190

**适用场景：** 大型项目架构设计、复杂系统重构、深度代码审查

* * *

### 2️⃣ **GPT-5.3-Codex** (OpenAI) 🚀

**发布时间：** 2026年2月5日184

**核心编程能力：**

- 🎯 **SWE-Bench Pro: 顶尖水平** （未公开具体数字）184
- 💻 **Terminal-Bench 2.0: 77.3%** \- **当前最高** 🥇190
- ⚡ **效率优势** ：Token消耗比以往少2-4倍190
- 🚀 **速度提升** ：比前代快25%190

**独特优势：**

- ✅ **终端/CLI操作能力最强** ，适合DevOps和CI/CD工作流190
- ✅ Token效率极高，构建更多内容成本更低184
- ✅ 算法优化、性能调优能力强190
- ✅ 执行速度快，适合自动化任务190
- ✅ 更愿意直接执行，不需要详细规格说明190

**局限：**

- ⚠️ 上下文窗口256K，小于Claude Opus 4.6的1M190
- ⚠️ 长上下文推理能力相对较弱190
- 💰 价格：$6/$30 per million tokens190

**适用场景：** 终端自动化、DevOps任务、性能优化、快速原型开发

* * *

### 3️⃣ **Minimax M2.5** (MiniMax) ⚡

**发布时间：** 2026年2月12日185

**核心编程能力：**

- 🎯 **SWE-bench Verified: 80.2%**
- 仅次于Claude Opus 4.6🥈185
- 🌍 **Multi-SWE-bench: 51.3%**
- **多语言编程能力行业第一** 185
- 🔍 **BrowseComp: 76.3%** \- 信息搜索能力强185
- ⚡ **效率提升** ：比M2.1快37%，与Claude Opus 4.6相当185

**独特优势：**

- ✅ **architect-thinking能力** ：编码前会主动分解和规划项目结构、UI设计185
- ✅ 支持10+编程语言（Go, C, C++, TypeScript, Rust, Python, Java, JS等）185
- ✅ 全栈开发能力：从0-1设计到90-100代码审查全覆盖185
- ✅ 成本效益极高：任务成本仅为Claude Opus 4.6的10%185
- ✅ 推理速度100 tokens/sec，接近其他模型的2倍185

**局限：**

- ⚠️ 在某些复杂任务上稳定性待提升185

**适用场景：** 全栈开发、多语言项目、成本敏感的生产环境

* * *

### 4️⃣ **GLM-5** (智谱AI) 🇨🇳

**发布时间：** 2026年2月183

**核心编程能力：**

- 🎯 **SWE-bench Verified: 77.8%**
- **开源模型最高** 🥇183
- 🔍 **BrowseComp: 75.9%** \- 信息搜索能力突出183
- 📊 **Artificial Analysis Index: 50分**
- 开源模型首次达到此水平183
- 🏆 **LMArena排名** ：全球第四、开源第一54

**独特优势：**

- ✅ **Agentic Engineering能力** ：从"写代码"到"独立完成工程任务"183
- ✅ **Slime框架** ：异步RL训练，解决Agent任务效率瓶颈183
- ✅ **DSA稀疏注意力** ：DeepSeek技术融入，长上下文处理能力强183
- ✅ **国产芯片适配** ：原生支持华为昇腾、摩尔线程等七大国产平台183
- ✅ 成本大幅降低，部署显存占用降60%180

**局限：**

- ⚠️ 上下文窗口128K，小于顶级竞品183

**适用场景：** 企业级私有化部署、AI编程助手、自主工程任务

* * *

### 5️⃣ **Kimi K2.5** (Moonshot AI) 👁️

**发布时间：** 2026年1月27日178

**核心编程能力：**

- 🎯 **SWE-bench Verified: 76.8%** 178
- 👁️ **Coding with Vision** ：视觉编程能力突出187
- 🤖 **Agent Swarm** ：支持100个子智能体并行工作178
- 📊 **MMMU Pro: 78.5%** , **VideoMMMU: 86.6%** 178

**独特优势：**

- ✅ **视觉编程SOTA** ：根据图片/视频直接生成代码、界面178
- ✅ **智能体蜂群架构** ：自动创建并行子代理，提高效率178
- ✅ 前端界面还原能力强，包含交互式布局与动画178
- ✅ 支持视觉调试（基于截图/视频进行代码修正）178

**局限：**

- ⚠️ 复杂交互生成与高保真动效复刻存在局限187
- ⚠️ Agent Swarm整体效率与输出稳定性待提升187
- 💰 定价较高：$0.6/$3 per million tokens187

**适用场景：** 前端开发、UI/UX设计、视觉转代码、多任务并行处理

* * *

### 6️⃣ **Claude Sonnet 4.6** (Anthropic) 💎

**发布时间：** 2026年2月17日192

**核心编程能力：**

- 🎯 **SWE-bench Verified: 79.6%**
- 接近Opus 4.6水平189
- 💻 **LiveCodeBench: ~2780** 189

**独特优势：**

- ✅ **性价比极高** ：达到Opus 4.6约90%能力，速度快3倍189
- ✅ 综合评分与Opus差距小，价格优势明显189

**适用场景：** 日常编程主力、预算有限但需要高质量输出的场景

* * *

### 7️⃣ **Qwen3.5-Plus** (阿里通义千问) 🇨🇳🌏

**发布时间：** 2026年2月16日180

**核心编程能力：**

- 🎯 **SWE-bench Verified: 70.6%**
- 中等水平189
- 🧮 **LiveCodeBench: ~2580** 189
- 📚 **中文技术栈理解** ： **国内开发文档（小程序、微信支付API）理解独步天下** 189

**独特优势：**

- ✅ **中文注释与国内文档理解领先** ，适合中国开发者189
- ✅多模态支持完善，总参数397B（激活仅170B）180
- ✅ 部署显存占用降60%，推理效率提升19倍180
- ✅ 价格优势：$0.11/$0.28 per million tokens189

**局限：**

- ⚠️编程基准分数相对较低（70.6%）189
- ⚠️ 复杂工程任务能力不如顶级模型189

**适用场景：** 中文技术栈开发、小程序/应用开发、成本敏感项目

* * *

### 8️⃣ **Deepseek V3.2** (深度求索) 🧠

**发布时间：** 2025年12月1日186

**核心编程能力：**

- 🏆 **LiveCodeBench: 标准版83.3%, Speciale版88.7%** 186
- ⚔️ **ICPC World Finals 2025: 金牌** （人类第2名水平）186
- 💪 **Codeforces: Speciale版2701分**
- 超越绝大多数人类程序员186
- 🎯 **SWE-Verified** ：标准版大幅缩短与闭源模型差距186

**独特优势：**

- ✅ **算法竞赛能力极强** ，LiveCodeBench达88.7%186
- ✅ **"Thinking in Tool-Use"** ：工具使用中的思考，避免思维断层186
- ✅ 动态策略管理长任务：自动总结或丢弃非必要历史186
- ✅ **极致性价比** ：成本仅为同类模型的1/10186
- ✅ 开源生态丰富，API接口完善186

**局限：**

- ⚠️ SWE-bench Verified具体分数未公开186
- ⚠️ 工程任务综合能力略逊于顶级闭源模型186

**适用场景：** 算法竞赛训练、数学推理、成本敏感的开源项目

* * *

### 9️⃣ **Seed-Coder** (字节跳动) 🔬

**发布时间：** 2026年2月181

**核心编程能力：**

- 📊 **参数规模：8B** \- 轻量化设计181
- 🏆 **SWE-bench Verified** ：在~8B模型中 **最佳** 181
- 🌍 **Multi-SWE-bench mini** ：表现优异181
- 🧮 **IOI'2024** ：超越QwQ-32B和DeepSeek-R1181
- ⚔️ **Codeforces** ：ELO评分与o1-mini相当181

**独特优势：**

- ✅ **参数效率极高** ：8B模型达到百亿级模型性能181
- ✅ **数据管道透明** ：完全开源代码数据筛选方法181
- ✅ 支持base、instruct、reasoning三种变体181
- ✅ 推理能力在8B级模型中顶尖181

**局限：**

- ⚠️ 绝对能力受限于参数规模（8B）
- ⚠️ 复杂大型项目处理能力不如大模型181

**适用场景：** 边缘部署、移动端应用、轻量级代码助手、研究用途

* * *

## 🏅 编程能力综合排行榜（2026年3月）

基于SWE-bench Verified（最权威的编程基准）排序：

| 排名 | 模型 | SWE-bench Verified | 综合评级 | 核心优势领域 |
| --- | --- | --- | --- | --- |
| 🥇 1 | Claude Opus 4.6 | **81.42%** | 🌟🌟🌟🌟🌟 | 工程任务、长上下文、架构设计 |
| 🥈 2 | Minimax M2.5 | **80.2%** | 🌟🌟🌟🌟🌟 | 全栈开发、多语言、速度/成本 |
| 🥉 3 | GPT-5.3-Codex | **~80%** | 🌟🌟🌟🌟🌟 | 终端操作、Token效率、自动化 |
| 4 | GLM-5 | **77.8%** | 🌟🌟🌟🌟 | Agent工程、开源最佳、国产化 |
| 5 | Kimi K2.5 | **76.8%** | 🌟🌟🌟🌟 | 视觉编程、智能体集群 |
| 6 | Claude Sonnet 4.6 | **79.6%** | 🌟🌟🌟🌟 | 性价比、综合能力强 |
| 7 | Qwen3.5-Plus | **70.6%** | 🌟🌟🌟 | 中文文档、多模态、成本低 |
| 8 | Deepseek V3.2-Speciale | N/A | 🌟🌟🌟 | 算法竞赛、推理能力 |
| 9 | Seed-Coder (8B) | N/A | 🌟🌟 | 小参数优化、轻量化 |

**注：** Deepseek V3.2和Seed-Coder因未公开SWE-bench Verified具体分数，按其他基准表现评估。

* * *

## 🔍 关键洞察与建议

### 📈 趋势观察1\. **性能趋同化** ：顶级模型（Claude Opus 4.6, GPT-5.3-Codex, Minimax M2.5）在SWE-bench上差距仅1.3个百分点，进入"后基准时代"190

2. **Agent能力成为新战场** ：从"写代码"到"独立完成工程任务"（Agentic Engineering）是核心方向183

3. **成本效率革命** ：Minimax M2.5任务成本仅为Claude的10%185，Deepseek V3.2成本为同类1/10186

4. **国产模型崛起** ：GLM-5开源第一、Kimi K2.5视觉编程领先、Qwen中文优化，与国际巨头差距快速缩小

### 💡 选型建议

**🏢 企业级生产环境：**

- 首选： **Claude Opus 4.6** （最稳定可靠）
- 备选： **Minimax M2.5** （性价比极高）

**💰 成本敏感项目：**

- 首选： **Deepseek V3.2** （开源+低成本）
- 备选： **Qwen3.5-Plus** （中文优化+低价）

**🎨 前端/视觉开发：**

- 首选： **Kimi K2.5** （视觉编程SOTA）

**🤖 算法/竞赛：**

- 首选： **Deepseek V3.2-Speciale** （ICPC金牌水平）

**📱 边缘/轻量部署：**

- 首选： **Seed-Coder 8B** （小参数最优）

**🔒 国产化要求：**

- 首选： **GLM-5** （国产芯片适配+开源）

**⚡ 自动化/DevOps：**

- 首选： **GPT-5.3-Codex** （终端操作最强）

* * *

## ⚠️ 置信度与局限性说明

### ✅ 高置信度信息（来源：官方发布/权威评测）

- Claude Opus 4.6的SWE-bench 81.42%（Anthropic官方）182
- Minimax M2.5的SWE-bench 80.2%（MiniMax官方）185
- GLM-5的SWE-bench 77.8%（智谱技术报告）183
- Kimi K2.5的SWE-bench 76.8%（Moonshot官方）178
- GPT-5.3-Codex的Terminal-Bench 77.3%（OpenAI官方）190

### 🔍 中等置信度信息（来源：第三方评测）

- Qwen3.5-Plus的SWE-bench 70.6%（2026 Q1横评）189
- 各模型的LiveCodeBench ELO评分189
- Kimi K2.5的MMMU Pro 78.5%（腾讯新闻）178

### ❓ 信息不足

- Deepseek V3.2的SWE-bench Verified具体分数
- Seed-Coder的SWE-bench Verified具体分数
- 各模型在HumanEval、MBPP等经典基准上的具体表现
- 长期稳定性与可靠性数据

* * *

## 📝 最终总结

这8个模型代表了2026年AI编程能力的最高水平， **Claude Opus 4.6** 、 **Minimax M2.5** 和 **GPT-5.3-Codex** 三强鼎立，编程能力都在SWE-bench 80%左右，处于第一梯队。 **GLM-5** 和 **Kimi K2.5** 作为开源和视觉编程的代表紧随其后。选择哪个模型取决于您的 **具体场景、预算和技术栈** ——没有万能的最优解，只有最适合的解决方案。

**关键建议：** 在实际项目中，建议进行小规模POC测试，根据您的特定工作流和代码base选择最匹配的模型。

分叉会话新的搜索

5

Go

内容由AI生成，请仔细甄别

### 来源 6: SWE-bench Verified - Vals AI

- URL: https://vals.ai/benchmarks/swebench
- 精读方法：firecrawl-scrape

Coding

SWE-bench Verified

# SWE-bench Verified

Academic

Updated: 6/17/2026

Solving production software engineering tasks

![](https://www.vals.ai/Logos/Vals.svg)![](https://www.vals.ai/Logos/Vals-dark.svg)

View:All Models

Harness:All harnesses

Task:Overall

Systems (64)

Harness

Score

Cost/Test

Latency

[1\\
\\
![Anthropic](https://www.vals.ai/model_providers/icons/Anthropic.svg)\\
\\
Claude Fable 5\\
\\
![Mini-SWE-agent](https://www.vals.ai/harnesses/icons/Mini-SWE-agent.svg)Mini-SWE-agent\\
\\
95.00%± 0.98\\
\\
$2.05\\
\\
356.18s](https://www.vals.ai/models/anthropic_claude-fable-5)

[2\\
\\
![Anthropic](https://www.vals.ai/model_providers/icons/Anthropic.svg)\\
\\
Claude Opus 4.8\\
\\
![Mini-SWE-agent](https://www.vals.ai/harnesses/icons/Mini-SWE-agent.svg)Mini-SWE-agent\\
\\
88.60%± 1.42\\
\\
$1.92\\
\\
566.95s](https://www.vals.ai/models/anthropic_claude-opus-4-8)

[3\\
\\
![Anthropic](https://www.vals.ai/model_providers/icons/Anthropic.svg)\\
\\
Claude Opus 4.8\\
\\
![Claude Code](https://www.vals.ai/model_providers/icons/Anthropic.svg)Claude Code\\
\\
85.80%± 1.56\\
\\
$0.67\\
\\
135.40s](https://www.vals.ai/models/anthropic_claude-opus-4-8-claude-code)

[4\\
\\
![zAI](https://www.vals.ai/model_providers/icons/zAI.svg)\\
\\
GLM 5.2\\
\\
![Mini-SWE-agent](https://www.vals.ai/harnesses/icons/Mini-SWE-agent.svg)Mini-SWE-agent\\
\\
82.80%± 1.69\\
\\
$0.71\\
\\
669.67s](https://www.vals.ai/models/zai_glm-5.2)

[5\\
\\
![OpenAI](https://www.vals.ai/model_providers/icons/OpenAI.svg)\\
\\
GPT 5.5\\
\\
![Mini-SWE-agent](https://www.vals.ai/harnesses/icons/Mini-SWE-agent.svg)Mini-SWE-agent\\
\\
82.60%± 1.70\\
\\
$1.36\\
\\
426.43s](https://www.vals.ai/models/openai_gpt-5.5)

[6\\
\\
![Anthropic](https://www.vals.ai/model_providers/icons/Anthropic.svg)\\
\\
Claude Opus 4.7\\
\\
![Mini-SWE-agent](https://www.vals.ai/harnesses/icons/Mini-SWE-agent.svg)Mini-SWE-agent\\
\\
82.00%± 1.72\\
\\
$2.42\\
\\
441.99s](https://www.vals.ai/models/anthropic_claude-opus-4-7)

[7\\
\\
![Cursor](https://www.vals.ai/model_providers/icons/Cursor.svg)\\
\\
Composer 2.5\\
\\
![Cursor CLI](https://www.vals.ai/model_providers/icons/Cursor.svg)Cursor CLI\\
\\
79.60%± 1.80\\
\\
N/A\\
\\
N/A](https://www.vals.ai/models/cursor_composer-2.5)

[8\\
\\
![Google](https://www.vals.ai/model_providers/icons/Google.svg)\\
\\
Gemini 3.5 Flash\\
\\
![Mini-SWE-agent](https://www.vals.ai/harnesses/icons/Mini-SWE-agent.svg)Mini-SWE-agent\\
\\
78.80%± 1.83\\
\\
$0.95\\
\\
254.13s](https://www.vals.ai/models/google_gemini-3.5-flash)

[9\\
\\
![Google](https://www.vals.ai/model_providers/icons/Google.svg)\\
\\
Gemini 3.1 Pro Preview (02/26)\\
\\
![Mini-SWE-agent](https://www.vals.ai/harnesses/icons/Mini-SWE-agent.svg)Mini-SWE-agent\\
\\
78.80%± 1.83\\
\\
$0.78\\
\\
312.26s](https://www.vals.ai/models/google_gemini-3.1-pro-preview)

[10\\
\\
![OpenAI](https://www.vals.ai/model_providers/icons/OpenAI.svg)\\
\\
GPT 5.4 (xhigh)\\
\\
![Mini-SWE-agent](https://www.vals.ai/harnesses/icons/Mini-SWE-agent.svg)Mini-SWE-agent\\
\\
78.20%± 1.85\\
\\
$0.80\\
\\
307.12s](https://www.vals.ai/models/openai_gpt-5.4-2026-03-05)

See 54 more models

Best Performing

Highest accuracy on this benchmark.

Best Budget

Highest accuracy² / avg token cost among the top 7 models.

Best Speed

Highest accuracy² / latency among the top 7 models.

## Key Takeaways

- [Claude Fable 5](https://www.vals.ai/models/anthropic_claude-fable-5) leads with a performance of 95.00%, achieving the best accuracy on SWE-bench Verified. [Claude Opus 4.8](https://www.vals.ai/models/anthropic_claude-opus-4-8) follows at 88.60%.

- [GPT 5.5](https://www.vals.ai/models/openai_gpt-5.5) comes in third with 82.60%, followed by [Claude Opus 4.7](https://www.vals.ai/models/anthropic_claude-opus-4-7) at 82.00% and [Gemini 3.5 Flash](https://www.vals.ai/models/google_gemini-3.5-flash) at 78.80%.

Resolution Rate by Task Difficulty

Model

<15 min

194 tasks

15m–1h

261 tasks

1–4 hr

42 tasks

>4 hr

3 tasks

GPT 5.5

92%

81%

50%

67%

Claude Opus 4.7

90%

79%

64%

67%

Composer 2.5

87%

79%

52%

67%

Gemini 3.1 Pro Preview (02/26)

89%

78%

43%

33%

Claude Opus 4.6 (Thinking)

90%

75%

43%

33%

GPT 5.4 (xhigh)

88%

76%

50%

0%

GPT 5.3 Codex

90%

73%

55%

33%

Claude Sonnet 4.6

87%

75%

50%

33%

DeepSeek V4

88%

76%

45%

0%

Claude Opus 4.5 (Thinking)

88%

75%

40%

0%

Gemini 3 Pro (11/25)

88%

74%

43%

33%

GLM 5.1

89%

73%

45%

33%

Kimi K2.6

88%

74%

40%

0%

GPT 5.2

89%

72%

38%

33%

Gemini 3 Flash (12/25)

88%

72%

38%

33%

MiniMax-M2.1

86%

73%

40%

33%

Muse Spark

85%

73%

40%

0%

MiniMax-M2.5

87%

71%

38%

33%

MiniMax-M2.7

86%

72%

31%

33%

GPT 5.4 Mini

86%

71%

33%

0%

GPT 5.5

Claude Opus 4.7

Composer 2.5

Gemini 3.1 Pro Preview (02/26)

Claude Opus 4.6 (Thinking)

GPT 5.4 (xhigh)

GPT 5.3 Codex

Claude Sonnet 4.6

DeepSeek V4

Claude Opus 4.5 (Thinking)

Gemini 3 Pro (11/25)

GLM 5.1

Kimi K2.6

GPT 5.2

Gemini 3 Flash (12/25)

MiniMax-M2.1

Muse Spark

MiniMax-M2.5

MiniMax-M2.7

GPT 5.4 Mini

GPT 5.2 Codex

Grok 4.20 (Reasoning)

Grok 4.3

GLM 5

Qwen 3.5 Plus

Qwen 3.6 27B

Claude Sonnet 4.5 (Thinking)

Kimi K2.5

GPT 5.1

GPT 5.4 Nano

GLM 4.7

GPT 5

DeepSeek V3.2 (Thinking)

Claude Haiku 4.5 (Thinking)

Qwen 3.5 Flash

Gemini 3.1 Flash Lite Preview

Devstral 2

GPT 5 Mini

Kimi K2 Thinking

Grok 4

Gemini 2.5 Pro

Grok 4 Fast (Reasoning)

Grok 4.1 Fast (Reasoning)

Mistral Large 3

GPT OSS 120B

Command A

* * *

## Background

SWE-bench, introduced by Jimenez et al. in their seminal paper [“Can Language Models Resolve Real-World GitHub Issues?”](https://arxiv.org/pdf/2310.06770), has emerged as a prominent benchmark for evaluating Large Language Models (LLMs) in software engineering contexts.

The benchmark comprises 500 tasks, each executed within an isolated Docker container. These tasks represent real-world GitHub issues from various repositories. Models must generate a “patch” to resolve each issue. The success of a model’s solution is determined by running unit tests against the generated patch.

A notable complexity of SWE-bench lies in its dual evaluation of both the agentic harness and the underlying foundation model. This leads to different methodologies adopted by foundation model labs when they report their results. Additionally, the benchmark’s computational requirements make it resource-intensive to reproduce results.

To enable fair and consistent comparisons across foundation models, we use a minimal bash-tool-only agent harness. Models are given a single tool — bash — and must navigate, search, edit, and solve tasks using standard command-line tools. This puts the evaluation burden squarely on the model rather than the harness.

* * *

## Results

SWE-bench

Overall

Cost / Test

Accuracy

Alibaba

Anthropic

Cohere

Cursor

DeepSeek

Google

Meta

MiniMax

Mistral

Moonshot AI

NVIDIA

OpenAI

Poolside

xAI

Xiaomi

zAI

Models that perform well on SWE-bench Verified tend to be proficient with bash and standard command-line tools for code navigation and editing.

There is also a clear trend that closed-source models perform better on SWE-bench Verified than open-source models. The clearest performance differences appear among tasks that take between 15 minutes and 1 hour to complete.
Models that perform well on these tasks tend to score higher overall on the benchmark.

y axis:Accuracy

Claude Fable 5

Show Average

### Tool Use

All models are given a single tool: bash. Models must use standard command-line tools (grep, find, sed, etc.) to navigate codebases, search for relevant files, and apply edits. This means tool usage differences between models reflect their command-line fluency and problem-solving strategy rather than how they interact with specialized harness tooling.

* * *

## Methodology

We use a minimal bash-tool-only agent harness, [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent), for all evaluations. Models are given a single tool — bash — and a system prompt describing the task. They must use standard command-line tools to navigate the codebase, identify the relevant code, and produce a patch.

We use the SWE-bench Verified subset of the dataset. SWE-bench Verified is a human-validated section of the SWE-bench dataset released by OpenAI in August 2024. Each task in the split has been carefully reviewed and validated by human experts, resulting in a curated set of 500 high-quality test cases from the original benchmark. You can find more information about the Verified split of the dataset [here](https://openai.com/index/introducing-swe-bench-verified/).

All models have access to the same tool to ensure a fair, apples-to-apples comparison. Models are run with the default configuration given by the provider, except for the max token limit, which is always set to the highest value possible.

All experiments are run on isolated cloud sandboxes. Latency is calculated starting from the first step the model takes within each task.

It may be possible to build better harnesses for a given model. However, our aim is to adopt a fair framework with which to evaluate all models.

### 来源 7: 2026 年最佳开源编程大模型：开发者指南

- URL: https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm
- 精读方法：firecrawl-scrape

[模型](https://www.atlascloud.ai/zh/models)

[探索](https://www.atlascloud.ai/zh/models/explore)

[价格](https://www.atlascloud.ai/zh/pricing/models)

[开发者](https://www.atlascloud.ai/zh/developer)

[企业](https://www.atlascloud.ai/zh/enterprise)

[联系](https://www.atlascloud.ai/zh/contact) [登录](https://www.atlascloud.ai/zh/login?redirect_url=%2Fblog%2Fguides%2Fcoding-plan-best-open-source-coding-llm)

模型

[图视频模型](https://www.atlascloud.ai/zh/models) [LLM](https://www.atlascloud.ai/zh/models/list/llm)

探索

[画廊](https://www.atlascloud.ai/zh/models/explore) [AI 视频与图像](https://www.atlascloud.ai/zh/models) [LLM](https://www.atlascloud.ai/zh/models/list/llm) [音频](https://www.atlascloud.ai/zh/models?type=Text-To-Speech) [3D](https://www.atlascloud.ai/zh/models?type=Text-to-3D,Image-to-3D) [工作流](https://www.atlascloud.ai/zh/console/workflow)

[价格](https://www.atlascloud.ai/zh/pricing/models)

开发者

[文档](https://www.atlascloud.ai/docs/zh) [Coding Plan](https://www.atlascloud.ai/zh/coding-plan) [MCP & CLINEW](https://www.atlascloud.ai/zh/cli)

[企业](https://www.atlascloud.ai/zh/enterprise)

[登录](https://www.atlascloud.ai/zh/login?redirect_url=%2Fblog%2Fguides%2Fcoding-plan-best-open-source-coding-llm) [联系](https://www.atlascloud.ai/zh/contact)

中国人工智能实验室已经悄然构建出目前市面上最强的一批开源编程模型。对于那些只关注 Anthropic 和 OpenAI 市场动态的开发者来说，DeepSeek、Moonshot（月之暗面）、Zhipu（智谱 AI）、MiniMax 和 Alibaba（阿里巴巴）所提供的模型矩阵之丰富，确实令人惊喜。

在 2026 年，我们需要探讨的不再是这些模型“好不好”，而是哪一个模型适合哪种工作负载、大规模运行的成本如何，以及如何将它们接入你现有的工具链中。本指南涵盖了这三个方面：实验室背景概况、完整规格与成本对照表、实用用例路由指南，以及 Claude Code、Codex 和 OpenClaw 的配置方案。

![icons of open source llm](https://static.atlascloud.ai/uploads/icons_of_open_source_llm_8649b37e3d.jpg)

## 为什么 **最强开源编程大模型 (LLM)** 正受到高度关注

转折点出现在 2024 年 12 月发布的 DeepSeek V3。它在 HumanEval 上得分 89.1%，在 SWE-bench Verified 上得分 42.0%，在当时与 Claude 3.5 Sonnet 和 GPT-4o 旗鼓相当。尽管它是开源的，并采用了在每次前向传播中仅激活 6710 亿参数中 370 亿参数的混合专家（MoE）架构（ [DeepSeek-V3 技术报告](https://github.com/deepseek-ai/DeepSeek-V3)，2024 年 12 月）。该架构所带来的高效率，解释了为何其推理成本能显著降低。

这一结果将开发者的目光引向了更广阔的中国开源生态系统。事实证明，DeepSeek 并非孤例。Moonshot AI 的 Kimi K2 系列一直在长文本基准测试中保持领先；阿里巴巴的 Qwen2.5-Coder 系列在代码专用排行榜上位居前列；智谱 AI 的 GLM-5 系列则能够输出精准的结构化数据，这对智能体（Agentic）工作流至关重要。

对开发者而言，实际意义在于：现在有五家独立的实验室提供能够胜任生产级编程工作负载的模型，它们不仅拥有开放权重或商用 API 接口，而且使用成本远低于那些私有替代方案。

## 打造最强开源编程大模型的实验室

### DeepSeek：以编程为先的设计与 MoE 效率

DeepSeek AI 成立于 2023 年，由幻方量化（一家中国量化对冲基金）提供支持，从创立之初就将编程能力作为模型的核心。DeepSeek-Coder 是最早引起开源社区高度关注的专用代码生成模型之一。V3 和 V4 系列在保持强劲编程基准表现的同时，将能力拓展到了通用推理领域。

理解 MoE 架构对理解其定价至关重要。通过每个 Token 只激活一小部分参数，其单次请求的计算成本远低于同等质量的稠密模型。这种效率优势直接体现在 API 定价上，这正是 DeepSeek V4 Flash 能够以每千 Token 0.23 个积分的输入价格运行，且在处理简单任务时质量丝毫不减的原因。

### Moonshot AI (Kimi)、Zhipu AI (GLM)、MiniMax 和 Alibaba (Qwen)

**Moonshot AI**（2023 年成立于北京）凭借长上下文推理能力确立了口碑。Kimi K2 系列具备 262K 的上下文窗口，专为文档密集型和代码密集型任务而设计，尤其适合在单次调用中处理大型代码库。

**Zhipu AI**（2019 年成立于北京，源自清华大学 KEG 实验室）是中国老牌 AI 公司之一。GLM 系列已迭代五代，每一代都在提升结构化输出的可靠性和指令遵循能力。GLM-5.1 体现了其在精准任务执行方面多年的对齐优化成果。

**MiniMax**（成立于 2021 年）从多模态领域跨入编程模型，推出了 M2 系列。MiniMax M2.5 和 M2.7 在成本与质量之间找到了极佳的平衡，精准填补了中端市场。

**阿里巴巴 Qwen 团队** 基于其强大的编程模型谱系构建了 Qwen3.6-plus。该系列在多语言代码生成方面表现持续稳健，且 256K+ 的上下文窗口处于当前可选方案的第一梯队（ [QwenLM GitHub](https://github.com/QwenLM/Qwen)，2025）。

## 最强开源编程大模型对比：上下文、成本与规格

以下是按输入价格排序的当前模型完整对照表，以便直观了解成本结构：

| 模型 | 实验室 | 上下文 | 输入费率 | 输出费率 | 缓存写入 | 较官方优惠 |
| --- | --- | --- | --- | --- | --- | --- |
| DeepSeek V4 Flash | DeepSeek AI | 1M | 0.23 | 0.46 | 0.046 | -50% |
| DeepSeek V3.2 | DeepSeek AI | 160K | 0.42 | 0.62 | 0.193 | -55% |
| MiniMax M2.5 | MiniMax | 200K | 0.65 | 2.18 | 0.109 | -45% |
| Kimi K2.5 | Moonshot AI | 262K | 1.09 | 5.45 | 0.182 | -45% |
| Kimi K2.6 | Moonshot AI | 262K | 1.72 | 7.26 | 0.290 | -45% |
| GLM-5 | Zhipu AI | 200K | 1.82 | 5.81 | 0.363 | -45% |
| MiniMax M2.7 | MiniMax | 200K | 2.36 | 4.00 | 0.109 | -45% |
| GLM-5.1 | Zhipu AI | 200K | 2.54 | 7.99 | 0.472 | -45% |
| DeepSeek V4 Pro | DeepSeek AI | 1M | 2.87 | 5.75 | 0.231 | -50% |
| Qwen3.6-plus | Alibaba | 256K+ | 3.30 | 9.90 | 0.660 | -50% |

_费率单位为每 1,000 Token 的积分数。“较官方优惠”指与该模型官方 API 直接定价相比的节省幅度。_

几点观察：首先，同属一家实验室的 DeepSeek V4 Flash（输入 0.23）与 V4 Pro（输入 2.87），两者在同一模型家族中，最低端与最高端 tier 的成本差距竟达 12.5 倍。其次，Kimi K2.5 以 1.09 的输入价格提供了 262K 的上下文窗口，属于高性价比的中端选择，无需承担 V4 Pro 的高额开销。第三，Qwen3.6-plus 的输出费率达到 9.90，是该组中最高的，这暗示了其设计更倾向于生成更长、更详尽的代码补全。

## 各类中国开源编程大模型的最佳适用场景

这是本指南的实战部分。上述费率决定了你在执行智能体编程会话时的路由选择。

**轻量级及后台任务：DeepSeek V4 Flash**

适用于文档字符串（docstrings）、变量重命名、简单补全、格式转换以及编程智能体在后台自动调用的所有辅助请求。输入 0.23 和输出 0.46 的费率使其成为该组中性价比最高的选择。当 Claude Code 将后台任务路由至 Haiku 模型槽位时，切换到 DeepSeek V4 Flash 可在不影响主会话性能的情况下大幅降低背景噪音的开销。

**兼顾成本与性能：DeepSeek V3.2 和 MiniMax M2.5**

DeepSeek V3.2 在 160K 上下文窗口下以 55% 的官方折扣提供了 V3 架构的性能。对于希望获得稳健编程能力但又不想承担 V4 Pro 全价的开发者，V3.2 是务实的选择。MiniMax M2.5（输入 0.65）提供了类似的定位，并支持 200K 窗口，适合上下文需求大于极致成本优化的场景。

**长上下文工作负载：Kimi K2.5 和 K2.6**

两款 Kimi 模型均支持 262K 的上下文窗口。对于需要传入大型代码库、分析长会话记录或进行需要完整上下文的多文件重构任务，Kimi K2.5（输入 1.09）可以在不支付旗舰模型价格的前提下提供大窗口支持。K2.6（输入 1.72）则在上下文优势的基础上提升了性能，适合更注重质量的场景。

**结构化输出与指令精准度：GLM-5 和 GLM-5.1**

智谱 AI 的 GLM 模型在指令遵从性上表现卓越。对于需要可靠结构化输出的流水线（如特定的 JSON 模式、格式化的代码片段、一致的 API 响应格式），建议在这些任务上对比测试 GLM-5（1.82）和 GLM-5.1（2.54）。其较高的输出费率反映了它们更倾向于生成详尽、细致的输出。

**旗舰级推理：DeepSeek V4 Pro 和 Qwen3.6-plus**

对于复杂的架构决策、多系统交互调试，或是首轮生成质量至关重要（避免因初稿质量差导致昂贵的重试循环）的任务，V4 Pro 和 Qwen3.6-plus 是首选。V4 Pro 的 1M 上下文窗口是其核心卖点；Qwen3.6-plus 则在 DeepSeek 家族之外提供了 256K+ 的高端选项。

### 模型路由：最被低估的开源编程 LLM 策略

对于使用这些国产开源编程大模型的开发者而言，最高效的优化手段并非仅仅选择单一模型，而是根据会话中的任务类型将请求路由到不同层级的模型中。

考虑一个典型的智能体编程会话：制定方案（复杂，需要 V4 Pro）、编写核心算法（复杂，V4 Pro）、生成测试用例（中等负载，MiniMax M2.5 或 Kimi K2.5）、为新函数编写文档字符串（轻量级，V4 Flash）、运行文件读取观察（轻量级，V4 Flash）。如果你全程使用 V4 Pro，那么上述每一个辅助步骤的成本都比必要的多花费 12.5 倍。

计算结果非常直接。假设一次会话中 50 次 API 调用里有 60% 是简单任务（平均 2,000 输入 + 500 输出 Token）。若在 V4 Flash 上运行：

- 成本：30 次调用 × (2,000 × 0.23 + 500 × 0.46) = 30 × (460 + 230) = **20,700 积分**

若全部在 V4 Pro 上运行：

- 成本：30 次调用 × (2,000 × 2.87 + 500 × 5.75) = 30 × (5,740 + 2,875) = **258,450 积分**

仅这 30 次调用，差价就高达 12.5 倍。模型路由的效益显而易见。

## 如何为你的工作流选择最强的开源编程大模型

以下是适用于大多数开发者场景的决策树：

**你需要最大化的单次请求上下文**：DeepSeek V4 Pro (1M) 或 Qwen3.6-plus (256K+)。两者均能处理大型代码库输入，无需分块。

**成本是首要限制**：简单任务选择 DeepSeek V4 Flash，中等复杂度工作选择 DeepSeek V3.2 或 MiniMax M2.5。

**你需要可靠的结构化输出**：从 GLM-5.1 开始尝试，并根据你的具体模式要求进行验证。

**你正在构建多步智能体流水线**：按步骤复杂度进行路由。辅助步骤使用 Flash，中等推理步骤使用 Kimi K2.5 或 GLM-5，规划与调试步骤使用 V4 Pro。

**你需要首选一个模型进行测试**：DeepSeek V4 Pro 是开发者首次评估国产 LLM 的自然首选。它有详尽的文档、在 ( [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)) 上拥有广泛的社区支持，并提供旗舰级的编程质量。

现实中的难点：高效地在模型间路由需要它们都在同一个 API Key 和 Base URL 之下。维护十个独立的 API 账户是不现实的。这正是统一网关解决的问题：一个端点，一个密钥，模型选择仅作为一个参数。

## 在编程工具中运行最强开源编程大模型

[Atlas Cloud Coding Plan](https://www.atlascloud.ai/console/coding-plan) 将本指南提到的所有十款模型集成在一个 API Key 和 Base URL 下，价格较官方 API 费率低 45-55%。各主流编程工具的设置方法如下。

**Base URL 注意事项（避免调试困扰）**：Claude Code 使用 [https://api.atlascloud.ai](https://api.atlascloud.ai/) 且不带 /v1 后缀。所有其他工具（Codex, OpenClaw, OpenCode, Cursor）均使用带有 /v1 后缀的 [https://api.atlascloud.ai/v1](https://api.atlascloud.ai/v1)。此处弄错会导致认证错误，且不会直接指向原因。

**Claude Code** (~/.claude/settings.json, macOS/Linux):

```plaintext
plaintextCopy
1{
2  "env": {
3    "ANTHROPIC_AUTH_TOKEN": "your-atlas-api-key",
4    "ANTHROPIC_BASE_URL": "https://api.atlascloud.ai",
5    "ANTHROPIC_MODEL": "deepseek-ai/deepseek-v4-pro",
6    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-ai/deepseek-v4-flash",
7    "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-ai/deepseek-v4-pro",
8    "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS": "1"
9  }
10}
```

ANTHROPIC\_DEFAULT\_HAIKU\_MODEL 字段映射到 Claude Code 的后台任务槽位。将其设置为 DeepSeek V4 Flash，意味着所有自动辅助调用（文件读取、状态检查、观察）都将使用性价比最高的模型，而主提示词使用 V4 Pro。无需任何路由逻辑，即可实现自动模型路由。

若要将 GLM-5.1 替换为 V4 Pro，只需将两个 Sonnet/main 字段中的 deepseek-ai/deepseek-v4-pro 修改为 zai-org/glm-5.1 即可。

**Codex** (~/.codex/config.toml + ~/.codex/auth.json):

```plaintext
plaintextCopy
1model_provider = "atlas_coding_plan"
2model = "deepseek-ai/deepseek-v4-pro"
3
4[model_providers.atlas_coding_plan]
5name = "atlascloud"
6base_url = "https://api.atlascloud.ai/v1"
7wire_api = "chat"
8requires_openai_auth = true
```

```plaintext
plaintextCopy
1{
2  "OPENAI_API_KEY": "your-atlas-api-key"
3}
```

**OpenClaw**：运行 openclaw onboard，选择 QuickStart，然后选择 Custom Provider。输入 [https://api.atlascloud.ai/v1](https://api.atlascloud.ai/v1) 作为 Base URL，粘贴密钥，然后输入模型 ID（如 moonshotai/kimi-k2.5）并选择 OpenAI 兼容协议。

在这些设置中切换模型仅需一行更改。无论选择哪个模型，API Key 和 Base URL 均保持不变。

![split-screen terminal showing settings json](https://static.atlascloud.ai/uploads/split_screen_terminal_showing_settings_json_4362ca8c94.jpg)

## 最强开源编程大模型：常见问题解答

**DeepSeek 真的是最强的开源编程大模型吗？**

对于大多数初学者，基于社区普及度、基准测试表现以及 1M 上下文窗口与价格优势的结合，DeepSeek V4 Pro 是自然首选。但“最强”很大程度上取决于任务类型。对于长文本任务，Kimi K2.5 或 K2.6 在低费率下提供了 262K 上下文；对于结构化输出任务，GLM-5.1 值得测试。结论是，“最强”取决于你的具体开发场景。

**这些模型在编程表现上与 Claude Sonnet 或 GPT-4o 相比如何？**

在标准编程基准测试中，顶级开源模型与美国私有模型之间的差距自 2024 年以来已大幅缩小。DeepSeek V3 在发布时已在多个基准测试中与 Claude 3.5 Sonnet 持平。私有模型目前的优势仍在于更细腻的指令解释能力，以及那些得益于大规模 RLHF 调优的任务。对于绝大多数代码生成、重构和调试任务，开发者感受到的实际差异微乎其微。

**我可以在同一个流水线中使用多个开源编程模型吗？**

可以。当所有模型通过网关共享同一个 Base URL 和 API Key 时，你可以在每次请求中指定不同的模型 ID。这意味着你可以在一个自动化工作流中，针对不同步骤分别使用 DeepSeek V4 Flash、Kimi K2.5 和 V4 Pro，而无需管理多个账户或认证环境。

**如果我从未用过开源 LLM，我该先尝试哪一个？**

从 DeepSeek V4 Pro 开始。它拥有最丰富的文档、最广泛的社区讨论以及最明确的性能特征。一旦你在实际任务中建立了基准，就可以在上下文密集型步骤上测试 Kimi K2.5，在后台辅助调用上测试 DeepSeek V4 Flash。两者之间的成本差将直观展示模型路由是否适合你的工作流。

**在企业环境中使用开源 LLM 是否安全？**

这取决于你的部署模式。对于通过第三方网关进行的 API 访问，需遵循该网关的数据处理政策。而可自托管的开放权重模型让你对代码的流向拥有完全控制权。r/LocalLLaMA 社区对此已有深入讨论，共识是 API 的使用需遵循与任何第三方 API 相同的安全审计标准，无需将其视为特殊关注类别。

## 关于最强开源编程大模型的总结

目前已有五家实验室发布了能够胜任重要生产级编程任务的模型，它们在成本和能力范围内提供了足够广的选择空间。盲目使用单一模型选择方案会让你蒙受额外的成本损耗。

实战手册：选择一个能让你通过单一密钥访问所有模型的网关，以 DeepSeek V4 Pro 建立基准，然后利用上述路由指南将简单任务转移到更廉价的层级。对于大多数执行智能体编程会话的开发者而言，单靠这一项路由优化就能在不改变输出质量的前提下显著降低开销。

_模型规格与费率参考截至 2026 年 5 月的 Atlas Cloud Coding Plan 文档。DeepSeek V3 基准数据来自 2024 年 12 月的 DeepSeek-V3 技术报告。费率可能会有所变动；在进行结算决策前，请务必与各服务商核对最新数据。_

分享

[Share on Twitter](https://twitter.com/intent/tweet?text=DeepSeek%E3%80%81Kimi%E3%80%81GLM%E3%80%81MiniMax%E3%80%81Qwen%EF%BC%9A2026%20%E5%B9%B4%E6%9C%80%E4%BD%B3%E5%BC%80%E6%BA%90%E7%BC%96%E7%A8%8B%E5%A4%A7%E6%A8%A1%E5%9E%8B%E6%8E%92%E5%90%8D&url=https%3A%2F%2Fwww.atlascloud.ai%2Fzh%2Fblog%2Fguides%2Fcoding-plan-best-open-source-coding-llm)[Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.atlascloud.ai%2Fzh%2Fblog%2Fguides%2Fcoding-plan-best-open-source-coding-llm)[Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.atlascloud.ai%2Fzh%2Fblog%2Fguides%2Fcoding-plan-best-open-source-coding-llm)

[返回列表](https://www.atlascloud.ai/zh/blog)

### 最新模型

[![Kling V3.0 Turbo Image-to-Video](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodels%2Fb5d5fb88-7124-4756-bd8a-413084831e8c.png&w=3840&q=75)\\
\\
NEW\\
\\
图生视频\\
\\
TURBO\\
\\
![brand logo](https://www.atlascloud.ai/icons/brands/kling-color.svg)\\
\\
**Kling V3.0 Turbo Image-to-Video** \\
\\
Kling V3.0 Turbo Image-to-Video transforms static images into dynamic cinematic videos using MVL technology. Supports first/last frame control and audio generation.\\
\\
From$0.112/秒\\
\\
$0.095/秒\\
\\
-15%\\
\\
试用](https://www.atlascloud.ai/zh/models/kwaivgi/kling-v3.0-turbo/image-to-video)

[![Kling V3.0 Turbo Text-to-Video](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodels%2F8791fc65-ec9b-431f-9fdd-12e064beea88.png&w=3840&q=75)\\
\\
NEW\\
\\
文生视频\\
\\
TURBO\\
\\
![brand logo](https://www.atlascloud.ai/icons/brands/kling-color.svg)\\
\\
**Kling V3.0 Turbo Text-to-Video** \\
\\
Kling V3.0 Turbo Text-to-Video generates dynamic cinematic videos from text prompts using MVL technology. Supports first/last frame control and audio generation.\\
\\
From$0.112/秒\\
\\
$0.095/秒\\
\\
-15%\\
\\
试用](https://www.atlascloud.ai/zh/models/kwaivgi/kling-v3.0-turbo/text-to-video)

[![Kling Video O3 4K Image-to-Video](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodels%2F4b899852-8ca9-42a8-a627-ac5ffa8a4520.png&w=3840&q=75)\\
\\
NEW\\
\\
图生视频\\
\\
![brand logo](https://www.atlascloud.ai/icons/brands/kling-color.svg)\\
\\
**Kling Video O3 4K Image-to-Video** \\
\\
Kling Omni Video O3 (4K) Image-to-Video transforms static images into dynamic cinematic videos using MVL technology. Supports first/last frame control and audio generation.\\
\\
From$0.42/秒\\
\\
$0.357/秒\\
\\
-15%\\
\\
试用](https://www.atlascloud.ai/zh/models/kwaivgi/kling-video-o3-4k/image-to-video)

[![Kling Video O3 4K Text-to-Video](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodels%2F23828fc3-3a1d-40bb-b67b-0fda360d3a68.png&w=3840&q=75)\\
\\
NEW\\
\\
文生视频\\
\\
![brand logo](https://www.atlascloud.ai/icons/brands/kling-color.svg)\\
\\
**Kling Video O3 4K Text-to-Video** \\
\\
Kling Omni Video O3 (4K) is Kuaishou advanced unified multi-modal video model with MVL (Multi-modal Visual Language) technology. Generates high-quality videos from text prompts with natural motion and audio generation support.\\
\\
From$0.42/秒\\
\\
$0.357/秒\\
\\
-15%\\
\\
试用](https://www.atlascloud.ai/zh/models/kwaivgi/kling-video-o3-4k/text-to-video)

### 相关文章

[![DeepSeek V4: Release Date, Announcement, and What to Expect in 2026](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Flarge_Group_1312320279_1_f8086d9b65.png&w=3840&q=75)News\\
\\
**DeepSeek V4: Release Date, Announcement, and What to Expect in 2026** \\
\\
January 24, 2026](https://www.atlascloud.ai/zh/news/DeepSeek-V4-Expect-in-2026)

[![Kling 3.0 Turbo and Omni: What Launched on June 17, 2026](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmedium_cov22_a4fc155fdb.png&w=3840&q=75)Blog\\
\\
**Kling 3.0 Turbo and Omni: What Launched on June 17, 2026** \\
\\
Atlas CloudJune 16, 2026](https://www.atlascloud.ai/zh/blog/guides/kling-3.0-turbo-kling-omni)

[![Kling AI NSFW Policy 2026: What's Allowed and Blocked](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fcov3_dcd8a0d799.png&w=3840&q=75)Blog\\
\\
**Kling AI NSFW Policy 2026: What's Allowed and Blocked** \\
\\
Atlas CloudJune 14, 2026](https://www.atlascloud.ai/zh/blog/guides/kling-ai-nsfw-policy)

[![How to Use the Gemini Omni Flash API for Video Generation (2026)](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fcov4_178d42e5b1.png&w=3840&q=75)Blog\\
\\
**How to Use the Gemini Omni Flash API for Video Generation (2026)** \\
\\
Atlas CloudJune 14, 2026](https://www.atlascloud.ai/zh/blog/guides/how-to-use-gemini-omni-api)

[![DeepSeek V4 Is Coming to Atlas Cloud: What We Know About the Next-Generation AI Model](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Flarge_New_3_7ca8eea5e9.png&w=3840&q=75)News\\
\\
**DeepSeek V4 Is Coming to Atlas Cloud: What We Know About the Next-Generation AI Model** \\
\\
Atlas CloudJanuary 22, 2026](https://www.atlascloud.ai/zh/news/deepseek-v4-is-coming)

[![Kling AI Video Length Limit: Maximum Duration by Version and Plan (2026)](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fcov2_ea276d0af8.png&w=3840&q=75)Blog\\
\\
**Kling AI Video Length Limit: Maximum Duration by Version and Plan (2026)** \\
\\
Atlas CloudJune 15, 2026](https://www.atlascloud.ai/zh/blog/guides/kling-ai-video-length-limit)

## 一个 API，畅享全模态 AI。

[探索全部模型](https://www.atlascloud.ai/zh/event/claim-model-rewards)

![Atlas Logo](https://www.atlascloud.ai/logo.svg)

产品

[图像模型](https://www.atlascloud.ai/zh/models?type=Text-to-Image,Image-to-Image) [视频模型](https://www.atlascloud.ai/zh/models?type=Text-to-Video,Image-to-Video) [大语言模型](https://www.atlascloud.ai/zh/models/list/llm)

模型

[Seedance 2.0](https://www.atlascloud.ai/zh/seedance-2) [Kling 3.0](https://www.atlascloud.ai/zh/models/kling-v3) [Nano Banana Pro](https://www.atlascloud.ai/zh/models/nanobanana) [GPT Image 2](https://www.atlascloud.ai/zh/models/gpt-image-2) [DeepSeek](https://www.atlascloud.ai/zh/models/deepseek) [GLM](https://www.atlascloud.ai/zh/models/glm) [探索更多](https://www.atlascloud.ai/zh/models/explore)

资源

[价格](https://www.atlascloud.ai/zh/pricing/models) [文档](https://www.atlascloud.ai/docs/zh) [提示词中心](https://www.atlascloud.ai/prompts-hub/) [按需 GPU](https://www.atlascloud.ai/zh/gpus) [裸金属服务器](https://www.atlascloud.ai/zh/bare-metal) [Serverless](https://www.atlascloud.ai/zh/serverless)

公司

[博客](https://www.atlascloud.ai/zh/blog) [关于我们](https://www.atlascloud.ai/zh/about) [联系我们](https://www.atlascloud.ai/zh/contact)

关注我们

[Linkedin](https://www.linkedin.com/company/atlas-cloudai/) [Discord](https://discord.gg/kUCbEZn8js) [X](https://x.com/atlas_cloud_ai) [Github](https://github.com/AtlasCloudAI) [Reddit](https://www.reddit.com/r/AtlasCloudAI/) [Youtube](https://www.youtube.com/@AtlasCloudAI)

![AICPA SOC Certification](https://www.atlascloud.ai/_next/image?url=%2Fimages%2Fhome%2Ffooter%2Fcert-1.png&w=128&q=75)![AICPA SOC 2 Certification](https://www.atlascloud.ai/_next/image?url=%2Fimages%2Fhome%2Ffooter%2Fcert-2.png&w=128&q=75)![HIPAA Compliant](https://www.atlascloud.ai/_next/image?url=%2Fimages%2Fhome%2Ffooter%2Fcert-3.png&w=384&q=75)

SOC I & II CERTIFIED \| HIPAA COMPLIANT

© 2026 Atlas Cloud [所有系统运行正常](https://atlascloud.instatus.com/)

[隐私与条款](https://www.atlascloud.ai/zh/privacy) \| [使用政策](https://www.atlascloud.ai/zh/acceptable-use) \| [数据删除政策](https://www.atlascloud.ai/zh/data-deletion-policy) \| [数据留存](https://www.atlascloud.ai/zh/data-retention)

### Join our Discord community

Join the Discord community for the latest model updates, prompts, and support.

Join Now！

[Popular AI Models](https://www.atlascloud.ai/zh/models)

[Seedance 2.0](https://www.atlascloud.ai/zh/models/seedance2)![hot](https://www.atlascloud.ai/images/navbar-icons/hot-icon.svg)[GPT Image 2](https://www.atlascloud.ai/zh/models/gpt-image-2)[Nano Banana 2](https://www.atlascloud.ai/zh/models/nanobanana-2)[Kling v3](https://www.atlascloud.ai/zh/models/kling-v3)[Seedream 5.0](https://www.atlascloud.ai/zh/models/seedream-5)[Veo 3.1](https://www.atlascloud.ai/zh/models/veo-3.1)

[AI Video API](https://www.atlascloud.ai/zh/models?type=Text-to-Video,Image-to-Video)

[Seedance 2.0](https://www.atlascloud.ai/zh/models/seedance2)[Veo 3.1](https://www.atlascloud.ai/zh/models/veo-3.1)[Kling v3](https://www.atlascloud.ai/zh/models/kling-v3)[Sora 2](https://www.atlascloud.ai/zh/models/sora-2)[Wan2.7](https://www.atlascloud.ai/zh/models/wan2.7)[PixVerse](https://www.atlascloud.ai/zh/models/pixverse)[Vidu](https://www.atlascloud.ai/zh/models/vidu)[Ltx-2](https://www.atlascloud.ai/zh/models/ltx2)

[AI Image API](https://www.atlascloud.ai/zh/models?type=Text-to-Image,Image-to-Image)

[Nano Banana 2](https://www.atlascloud.ai/zh/models/nanobanana-2)[GPT Image 2](https://www.atlascloud.ai/zh/models/gpt-image-2)[Seedream 5.0](https://www.atlascloud.ai/zh/models/seedream-5)[Qwen Image](https://www.atlascloud.ai/zh/models/qwen-image)[Flux.2](https://www.atlascloud.ai/zh/models/flux)[Image tools](https://www.atlascloud.ai/zh/models/image-video-tools)

[LLM API](https://www.atlascloud.ai/zh/models/list/llm)

[DeepSeek](https://www.atlascloud.ai/zh/models/deepseek)[Qwen](https://www.atlascloud.ai/zh/models/qwen)[Grok](https://www.atlascloud.ai/zh/models/grok)[Z.ai](https://www.atlascloud.ai/zh/models/glm)[Moonshot](https://www.atlascloud.ai/zh/models/kimi)[MiniMax](https://www.atlascloud.ai/zh/models/minimax-m2.1)[Kat](https://www.atlascloud.ai/zh/models/kwaipilot/kat-coder-pro-v2)[OpenAI](https://www.atlascloud.ai/zh/models/chatgpt)[Anthropic](https://www.atlascloud.ai/zh/models/anthropic)

[探索全部模型](https://www.atlascloud.ai/zh/models)

Popular AI Models [查看更多](https://www.atlascloud.ai/zh/models)

[![Seedance 2.0 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F95e2160e-febc-4c37-84c4-0a36d007c3f1.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/bytedance-color.svg)Seedance 2.0\\
\\
Seedance 2.0（by Bytedance） is a multimodal video generation model that redefines "controllable creation," moving beyond the limitations of text or start/end frames. It supports quad-modal inputs—text, image, video, and audio—and introduces an industry-leading "Universal Reference" system. By precisely replicating the composition, camera movement, and character actions from reference assets, Seedance 2.0 solves critical issues with character consistency and physical coherence, empowering creators to act as true "directors" with deep control over their output.](https://www.atlascloud.ai/zh/models/seedance2) [![Grok-Imagine Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F376e7c88-24bb-4a21-9d2c-103af17d04bb.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/grok.png)Grok-Imagine\\
\\
Grok Imagine Image Quality is xAI's latest AI image generation model, delivering studio-grade visuals with up to 2K resolution and razor-sharp detail. It offers best-in-class text rendering across multiple languages, photorealistic outputs with natural lighting, rich textures, and believable physics, plus tighter prompt following and image editing with reference inputs for precise creative control. Ideal for hero images, ad creatives, product renders, and brand-grade visuals.](https://www.atlascloud.ai/zh/models/grok-imagine-models) [![Gemini Omni](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F43cd4205-d5d4-46c0-8442-d87fb6af6ff9.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/gemini-color.svg)Gemini Omni\\
\\
Gemini Omni (by Google DeepMind) is a video generation and editing model launched on May 20, 2026 at Google I/O that redefines the standard for "reasoning-driven creation," built specifically to solve the core challenge of AI video: making output that actually understands what you mean, not just what you type. \\
\\
It fuses Gemini's reasoning engine with generative capability, accepting any mix of images, text, video, and audio to produce consistent, knowledge-grounded output. Unlike models that start from scratch each time, Omni lets you edit through natural conversation — swapping objects, rewriting scenes, shifting styles — while keeping physics, characters, and continuity intact across every turn.](https://www.atlascloud.ai/zh/models/gemini-omni) [![GPT Image 2 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F793e3c5c-b633-4e78-baa4-fbd7654b349f.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/openai.svg)GPT Image 2\\
\\
GPT Image 2 is a state-of-the-art multimodal foundation model engineered for exceptional text-to-image generation with unprecedented photorealism and creative versatility. Developed by OpenAI as the evolution of the DALL-E lineage, it transforms detailed natural language descriptions into hyper-realistic imagery at up to 4K resolution. With proprietary "Neural Rendering Engine" technology for precise visual control, GPT Image 2 delivers studio-quality results with accurate anatomy, lighting, and composition—making it the premier AI tool for professional creators, enterprises, and developers demanding production-ready visual assets.](https://www.atlascloud.ai/zh/models/gpt-image-2) [![MAI Image 2.5 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F3280dbc2-9f28-43f8-ba46-2d113ae08057.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/microsoft-color.svg)MAI\\
\\
MAI-Image-2.5 是 Microsoft 最新推出的逼真图像生成与编辑模型系列，专为商业设计、产品摄影和品牌级内容创作而打造。提供用于文本生成图像和图像编辑的 standard 和 Flash 变体，以极具竞争力的价格（每张图像起价 0.03 美元）提供同类最佳的 Arena ELO 得分。凭借精准的文本渲染、手术刀级的编辑能力以及自然的人像生成，MAI-Image-2.5 专为需要生产级质量视觉效果且无需承担后期处理开销的团队而设计。](https://www.atlascloud.ai/zh/models/mai-image-2.5) [![Wan 2.7 Models ](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F9c805eb7-989a-4d83-84e5-f7aa494bdd1e.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/qwen-color.svg)Wan 2.7\\
\\
Launching this March, Wan2.7 is the latest powerhouse in the Qwen ecosystem, delivering a massive upgrade in visual fidelity, audio synchronization, and motion consistency over version 2.6. This all-in-one AI video generator supports advanced features like first-and-last frame control, 3x3 grid synthesis, and instruction-based video editing. Outperforming competitors like Jimeng, Wan2.7 offers superior flexibility with support for real-person image inputs, up to five video references, and 1080P high-definition outputs spanning 2 to 15 seconds, making it the premier choice for professional digital storytelling and high-end content marketing.](https://www.atlascloud.ai/zh/models/wan2.7) [![Nano Banana 2 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Ff76d5d1c-0478-4566-9ff7-9a107f244d45.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/gemini-color.svg)Nano Banana 2\\
\\
Nano Banana 2 (by Google), is a generative image model that perfectly balances lightning-fast rendering with exceptional visual quality. With an improved price-performance ratio, it achieves breakthrough micro-detail depiction, accurate native text rendering, and complex physical structure reconstruction. It serves as a highly efficient, commercial-grade visual production tool for developers, marketing teams, and content creators.](https://www.atlascloud.ai/zh/models/nanobanana-2) [![Hunyuan 3D Generation Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F2399af50-a0d4-4cbd-a194-ab7b3cd789ae.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/hunyuan-color.svg)Hunyuan 3D\\
\\
Hunyuan3D is a state-of-the-art 3D generative foundation model from Tencent that turns text prompts and single images into high-quality, textured 3D meshes. Built on a two-stage pipeline—Hunyuan3D-DiT for shape generation via flow-matching diffusion and Hunyuan3D-Paint for multi-view texture synthesis—it produces clean geometry with full PBR materials ready for game engines, AR/VR, 3D printing, and DCC tools. Available in Pro (up to 1.5M faces, 4K PBR textures) and Rapid (2–3 minute lightweight generation) tiers, with both Text-to-3D and Image-to-3D entry points, Hunyuan3D is the premier AI 3D toolkit for game developers, e-commerce teams, and 3D content studios. Generations start at $0.02 each.](https://www.atlascloud.ai/zh/models/hunyuan-3d) [![Midjourney Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F8985bbfd-0cd3-4b90-9912-6090fb37bda8.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/midjourney.svg)Midjourney\\
\\
Midjourney is a proprietary AI image and video generation platform developed by Midjourney, Inc. (San Francisco). Founded in 2021 by David Holz, it has become the aesthetic gold standard in generative AI — transforming text prompts into cinematic, painterly visuals at native 2K resolution. The latest V8.1 architecture, rebuilt from scratch on GPU-native PyTorch, delivers 4–5× faster generation, true 2048×2048 output without upscaling artifacts, and a signature visual style that remains unmatched by competitors. With the addition of Video V1, Midjourney extends its aesthetic into motion — animating still images into atmospheric 5-second cinematic clips. From brand campaigns to film pre-visualization to game concept art, Midjourney is the premier AI creative tool for professionals who demand both speed and artistry.](https://www.atlascloud.ai/zh/models/midjourney) [![PixVerse Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Fa833da45-430e-45ed-9906-8084d76850d4.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/pixverse-color.svg)PixVerse\\
\\
PixVerse, developed by AISphere, is a video generation model series built around one idea: giving creators director-level control over every frame. V6 is the flagship generation model, covering text-to-video, image-to-video, reference-to-video, start-and-end frame control, and video extension in a single cohesive pipeline. C1 takes a different approach — it is a storyboard-native model designed for multi-shot narrative production, where scene continuity and visual consistency across clips matter as much as individual frame quality. Both series are available on Atlas Cloud, starting from $0.025 per second, with no infrastructure setup required.](https://www.atlascloud.ai/zh/models/pixverse) [![Veo 3.1 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Fc356abb6-a5c9-4f69-926d-268fe857832a.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/gemini-color.svg)Veo 3.1\\
\\
Google DeepMind’s Veo 3.1 represents a paradigm shift in AI video generation, empowering creators with director-level narrative control and cinematic-grade audio quality that seamlessly integrates with its enhanced visual realism. By bridging the gap between imaginative concepts and photorealistic execution, this advanced model offers a transformative solution for a wide range of application scenarios, from professional filmmaking and high-end advertising to immersive digital content creation.](https://www.atlascloud.ai/zh/models/veo-3.1) [![Seed 3D Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F2875b575-5865-44a4-a982-db777842c093.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/bytedance-color.svg)Seed 3D\\
\\
Seed3D V2.0 is ByteDance's second-generation 3D generation foundation model, released April 23, 2026. It transforms single images, video, or text into production-ready 3D assets — complete with full PBR material maps (albedo, normal, metallic, roughness) and simulation-compatible formats. Powered by a coarse-to-fine two-stage Diffusion Transformer and unified PBR pipeline, it achieved a 92.8% win rate over Tripo 3.0 in blind evaluations by 60 professional 3D modelers — covering everything from game assets and e-commerce AR previews to robotics simulation via URDF output.](https://www.atlascloud.ai/zh/models/seed-3d) [![Seedream 5.0 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Fda8e3ea6-1a1b-4166-8a37-14b956761219.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/bytedance-color.svg)Seedream 5.0\\
\\
Seedream 5.0, developed by ByteDance’s Jimeng AI, is a high-performance AI image generation model that integrates real-time search with intelligent reasoning. Purpose-built for time-sensitive content and complex visual logic, it excels at professional infographics, architectural design, and UI assistance. By blending live web insights with creative precision, Seedream 5.0 empowers commercial branding and marketing with a seamless, logic-driven workflow that turns sophisticated data into stunning, high-fidelity visuals.](https://www.atlascloud.ai/zh/models/seedream-5) [![Kling 3.0 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F676705d5-2beb-46e5-8148-362a76c07d3c.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/kling-color.svg)Kling 3.0\\
\\
Kuaishou’s flagship video generation suite, Kling 3.0, features two powerhouse models—Kling 3.0 (Upgraded from Kling 2.6) and Kling 3.0 Omni (Kling O3, Upgraded from Kling O1)—both offering high-fidelity native audio integration. While Kling 3.0 excels in intelligent cinematic storytelling, multilingual lip-syncing, and precision text rendering, Kling O3 sets a new standard for professional-grade subject consistency by supporting custom subjects and voice clones derived from video or image inputs. Together, these models provide a comprehensive solution tailored for cinematic narratives, global marketing campaigns, social media content, and digital skit production.](https://www.atlascloud.ai/zh/models/kling-v3) [![Seedream 4.5 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Fa7146f15-6aae-48e5-aec3-7dc6df27b8b5.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/bytedance-color.svg)Seedream 4.5\\
\\
Seedream 4.5, developed by ByteDance’s Jimeng AI, is a versatile, high-fidelity model that unifies creative generation with precise image editing. Engineered for professional consistency and intricate text rendering, it excels at multi-subject fusion, brand identity, and high-resolution marketing assets. By bridging spatial logic with artistic control, Seedream 4.5 empowers designers with a seamless, instruction-driven workflow that transforms complex concepts into polished, commercial-grade visuals.](https://www.atlascloud.ai/zh/models/seedream-4.5) [![Vidu Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F39ce054c-dc09-4da7-bd6f-64f0d5d158ff.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/vidu-color.svg)Vidu\\
\\
Vidu, a joint innovation by Shengshu AI and Tsinghua University, is a high-performance video model powered by the original U-ViT architecture that blends Diffusion and Transformer technologies. It delivers long-form, highly consistent, and dynamic video content tailored for professional filmmaking, animation design, and creative advertising. By streamlining high-end visual production, Vidu empowers creators to transform complex ideas into cinematic reality with unprecedented efficiency.](https://www.atlascloud.ai/zh/models/vidu) [![Qwen Image Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Ff46fba52-2578-4390-a2a4-779aeb59ecbf.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/qwen-color.svg)Qwen Image\\
\\
Qwen Image 2.0 is Alibaba Cloud's latest image generation model series from the Tongyi Qianwen family, comprising 4 models optimized for different use cases. This series delivers professional-grade image generation and editing capabilities with exceptional cost-performance ratio, supporting up to 2K resolution output and demonstrating outstanding performance in prompt adherence, detail rendering, and style consistency. Whether for text-to-image or image-to-image tasks, Qwen Image 2.0 provides developers, marketing teams, and content creators with efficient and reliable visual content production solutions.\\
The series includes two tiers: Standard and Professional. The Standard edition is ideal for daily content production and cost-effective batch image generation, while the Professional edition delivers the highest quality visual output, designed for professional production workflows with stringent image quality requirements.\\
Qwen-Image, a lightweight 7B foundation model by Alibaba, transforms long-form prompts up to 1,000 tokens into stunning native 2K (2048x2048) resolution images. It excels in Chinese text rendering, accurately handling complex layouts and classical scripts, making it the premier AI tool for high-end graphic design and cross-cultural content creation.](https://www.atlascloud.ai/zh/models/qwen-image) [![Happy Horse 1.0](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F47fa27ae-4d6f-4fa4-8f4f-c4f95ac5d960.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/happyhorse.svg)Happy Horse 1.0\\
\\
HappyHorse-1.0 is a unified multimodal AI video generation model that climbed to the top of the Artificial Analysis Video Arena blind-test leaderboard for both text-to-video and image-to-video generation. CNBC Alibaba Group confirmed ownership of HappyHorse, developed under its Alibaba Token Hub (ATH) business unit, where it leads benchmarks outperforming ByteDance's Seedance 2.0 and others. Caixin Global Led by Zhang Di — the former VP of Kuaishou who architected Kling AI — the 15-billion parameter model generates 1080p video with synchronized audio in a single pass using a unified transformer architecture that bypasses the multi-stage pipelines used by every major competitor.](https://www.atlascloud.ai/zh/models/happyhorse) [![Nano Banana Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F74b8012a-1e04-4e1e-b910-8e115ba4c285.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/gemini-color.svg)Nano Banana\\
\\
Google’s Nano Banana (Gemini 3 Image) series, featuring both standard and Pro models, combines deep semantic understanding with seamless integration for precise detail control. While the standard version delivers high-quality 1K outputs, Nano Banana Pro elevates professional workflows with versatile 1K/2K/4K resolution options with higher quality, making it the ideal solution for any creative or commercial application.](https://www.atlascloud.ai/zh/models/nanobanana) [![Hailuo Video Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F2a98d8ad-58a9-46fd-84e2-3a067ff2542c.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/minimax-color.svg)Hailuo Video\\
\\
MiniMax Hailuo 视频模型提供原生 1080p (Pro) 和 768p (Standard) 的文生视频与图生视频功能，具备强大的指令遵循能力以及逼真、符合物理规律的运动表现。](https://www.atlascloud.ai/zh/models/hailuo) [![Wan 2.6 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F0a2b5a2a-6fda-4364-851b-078a9e3027de.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/qwen-color.svg)Wan 2.6\\
\\
Wan 2.6 is a next-generation AI video generation model from Alibaba’s Tongyi Lab, designed for professional-quality, multimodal video creation. It combines advanced narrative understanding, multi-shot storytelling, and native audio–visual synchronization to produce smooth 1080p videos up to 15 s long from text and reference inputs. Wan 2.6 also supports character consistency and role-guided generation, enabling creators to turn scripts into cohesive scenes with seamless motion and lip syncing. Its efficiency and rich creative control make it ideal for short films, advertising, social media content, and automated video workflows.](https://www.atlascloud.ai/zh/models/wan2.6) [![Flux.2 Image Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Fc6023d0c-a14c-451f-bd35-cfc0058e36f8.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/flux.png)Flux.2 Image\\
\\
Developed by Black Forest Labs, FLUX.2 is a powerhouse 32-billion parameter rectified flow Transformer model that redefines creative workflows by unifying AI image generation, editing, and composition. It transforms complex text prompts into high-fidelity visuals while offering integrated tools for professional-grade editing at resolutions up to 2K, providing a streamlined, all-in-one solution for digital artists and designers seeking unmatched precision and scalability in their visual content creation.](https://www.atlascloud.ai/zh/models/flux) [![GPT Image Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Ff810a4ef-4e44-410e-a5ef-91f481b914a5.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/openai.svg)GPT Image\\
\\
The GPT Image Family is OpenAI's latest suite of multimodal image generation and editing models, built on the powerful GPT architecture. This family includes three tiers — GPT Image-1, GPT Image-1.5, and GPT Image-1 Mini — each available in both Text-to-Image and Image-to-Image variants. Combining GPT's world-class language understanding with DALL·E-class visual synthesis, these models deliver exceptional prompt adherence, photorealistic rendering, and creative versatility across illustration, photography, design, and visualization tasks.\\
The series offers flexible pricing and quality tiers to match any workflow — from rapid prototyping and high-volume content production to professional-grade final deliverables. Whether you need ultra-fast iterations at minimal cost or maximum quality for brand campaigns, the GPT Image Family has a solution tailored to your needs.](https://www.atlascloud.ai/zh/models/gpt-image) [![Seedance 1.5 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F43469c91-ae52-4602-8581-087f74889134.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/bytedance-color.svg)Seedance 1.5\\
\\
ByteDance’s Seedance 1.5 Pro is a powerful AI video generation model that seamlessly integrates native audio with film-grade cinematography. Engineered for emotional storytelling and superior visual quality, it enables creators to produce immersive, narrative-driven content for professional filmmaking and advertising, setting a new standard for artistic precision and production efficiency.](https://www.atlascloud.ai/zh/models/seedance1.5) [![ERNIE Image Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F5d9fea6f-c26d-423b-9f5a-14c465901787.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/wenxin-color.svg)ERNIE Image\\
\\
ERNIE-Image is an open-weight text-to-image model developed by the ERNIE-Image Team at Baidu, built on a single-stream Diffusion Transformer (DiT) with 8B parameters and paired with a lightweight Prompt Enhancer that rewrites short prompts into richer, more structured descriptions before passing them to the diffusion backbone. NYU Shanghai RITS Released on April 15, 2026 under the Apache 2.0 license, it transforms natural language descriptions into detailed imagery with particular strength in text rendering and structured layout generation. ERNIE-Image is designed not only for strong visual quality, but for controllability in practical generation scenarios where accurate content realization matters as much as aesthetics — making it well-suited for commercial posters, comics, multi-panel layouts, and other content creation tasks that require both visual quality and precise control.](https://www.atlascloud.ai/zh/models/ERNIE-Image) [![Ltx-2 Video Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Fa94acd8a-3e80-444c-a96e-a458d7ac0ea2.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/lightricks.png)Ltx-2 Video\\
\\
LTX-2 is a complete AI creative engine. Built for real production workflows, it delivers synchronized audio and video generation, 4K video at 48 fps, multiple performance modes, and radical efficiency, all with the openness and accessibility of running on consumer-grade GPUs.](https://www.atlascloud.ai/zh/models/ltx2) [![Sora 2 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F9a795bd8-d8a1-40c6-9c48-f8e41d78d47f.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/openai.svg)Sora 2\\
\\
OpenAI’s Sora 2 is a groundbreaking video generation model that redefines digital realism through enhanced physical accuracy and precise creative control. By introducing seamless audio-video synchronization, Sora 2 transitions AI-generated video from experimental concepts into a truly practical production tool for the modern creator. Whether crafting high-impact e-commerce advertisements, engaging social media content, or cinematic sequences for filmmaking, Sora 2 provides a robust and reliable engine that streamlines high-quality visual storytelling for professional workflows.](https://www.atlascloud.ai/zh/models/sora-2) [![Seedream 4 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F5f04e578-0512-4f6b-bdae-bf0cbb882a64.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/bytedance-color.svg)Seedream 4\\
\\
Seedream v4, a cutting-edge image generation model by ByteDance, redefines creative workflows by combining lightning-fast inference speeds with breathtaking 4K high-definition output. Beyond its raw performance, the model leverages advanced knowledge and reasoning to interpret complex prompts with precision, enabling seamless prompt-based editing and a vast spectrum of versatile artistic styles that make it the ultimate solution for professional design, content creation, and digital marketing.](https://www.atlascloud.ai/zh/models/seedream-4) [![Imagen Image Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F18d662e0-6ddc-40a5-a233-06bf8d8d7dec.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/gemini-color.svg)Imagen Image\\
\\
Imagen is Google’s diffusion-based image generation family, designed for photorealism, creativity, and scalable content workflows. With options from fast inference to ultra-high fidelity, Imagen balances speed, detail, and enterprise reliability.](https://www.atlascloud.ai/zh/models/Imagen) [![Photon Image Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F9484e64c-ffef-4320-aaa3-4e878e02e852.png&w=3840&q=75)\\
\\
Photon Image\\
\\
Photon (by Luma Labs) is a universal image generation model built for visual excellence, leveraging an advanced diffusion transformer architecture. Renowned for its deep understanding of lighting physics and superior text rendering capabilities, it accurately captures complex prompt intentions to instantly generate high-fidelity images that blend cinematic realism with artistic beauty. Photon is designed to empower artists, designers, and brands with a fast, intelligent, and highly controllable creative engine, significantly shortening the path from inspiration to final image.](https://www.atlascloud.ai/zh/models/photon) [![Seedance Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Fd6317de4-ab4e-47d9-afb2-a9234d9aa030.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/bytedance-color.svg)Seedance\\
\\
Seedance is ByteDance’s family of video generation models, built for speed, realism, and scale. Available in Lite and Pro versions across 480p, 720p, and 1080p, Seedance transforms text and images into smooth, cinematic video on Atlas Cloud.](https://www.atlascloud.ai/zh/models/seedance) [![Ideogram Image Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Fc41ed6bf-482c-48c5-b49e-252aa91700b3.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/ideogram.png)Ideogram Image\\
\\
Ideogram (by Ideogram AI) is an image generation model that redefines the standard for "text-visual fusion," designed specifically to solve text rendering challenges in AI art. It features industry-leading typography control and semantic understanding, perfectly blending accurate spelling, diverse fonts, and design-forward visuals. Unlike generic models, Ideogram produces highly finished commercial designs like posters, logos, and T-shirt graphics, making it the ultimate "what you see is what you get" tool for designers and marketers.](https://www.atlascloud.ai/zh/models/ideogram) [![Van Video Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F3d434ac4-0bcb-4064-9110-ba7d7f990094.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/qwen-color.svg)Van Video\\
\\
Built on the Wan 2.5 and 2.6 frameworks, Van Model is a flagship AI video series that delivers superior high-resolution outputs with unmatched creative freedom. By blending cinematic 3D VAE visuals with Flow Matching dynamics, it leverages proprietary compute distillation to offer ultra-fast inference speeds at a fraction of the cost, making it the premier engine for scalable, high-frequency video production on a budget.](https://www.atlascloud.ai/zh/models/van) [![Hidream Image Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Fb4b04be3-5001-4690-a4cc-6f12fb3d8b1a.png&w=3840&q=75)\\
\\
Hidream Image\\
\\
HiDream is a foundation image generation model built on a proprietary billion-scale parameter architecture, designed specifically for "precision and control" in professional creation. Fusing deep semantic understanding with exceptional visual rendering, it accurately captures nuances in both Chinese and English prompts to generate rigorously composed, cinematically lit visuals. HiDream bridges the gap between imagination and execution, offering an integrated solution for generation and intelligent editing to streamline visual production for e-commerce, advertising, and game art.](https://www.atlascloud.ai/zh/models/hidream) [![Seedance 2.1 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Ff93eb5af-17d1-4ef8-9596-5b5bc070dafb.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/bytedance-color.svg)Seedance 2.1\\
\\
Seedance 2.1 即将发布！](https://www.atlascloud.ai/zh/models/seedance-2.1) [![Wan 2.5 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Faf16bb4e-96ac-4491-b119-1e19e9ef9773.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/qwen-color.svg)Wan 2.5\\
\\
Wan 2.5 is Alibaba’s state-of-the-art multimodal video generation model, capable of producing high-fidelity, audio-synchronized videos from text or images. It delivers realistic motion, natural lighting, and strong prompt alignment across 480p to 1080p outputs—ideal for creative and production-grade workflows.](https://www.atlascloud.ai/zh/models/wan2.5) [![Kling Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Fea286b45-3623-4ad2-998e-4196a6b89cab.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/kling-color.svg)Kling\\
\\
Kling AI is a text-to-video model developed by Kuaishou that creates realistic, high-quality videos from text prompts. It focuses on smooth motion, stable frames, and natural-looking scenes. Kling works well for short videos, ads, and marketing content, helping creators save time and reduce production costs. With strong performance in video consistency and realism, Kling AI is becoming a popular choice in the AI video generation space.](https://www.atlascloud.ai/zh/models/kling) [![Wan 2.2 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Fd7501d5a-58bb-4189-a942-9a6860f13406.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/qwen-color.svg)Wan 2.2\\
\\
Wan 2.2 introduces a Mixture-of-Experts (MoE) architecture that enables greater capacity and finer motion control without higher inference cost, supporting both text-to-video and image-to-video generation with high visual fidelity, smooth motion, and cinematic realism optimized for real-world GPU deployment.](https://www.atlascloud.ai/zh/models/wan) [![Seedance 2.0 Mini Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F515923d3-efa9-45bf-9a0c-0700de1e26dc.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/bytedance-color.svg)Seedance 2.0 Mini\\
\\
Seedance 2.0 Mini 将 ByteDance 的多模态视频生成技术引入到对速度和成本要求极高的工作流中。它以更轻量的占用空间提供 Seedance 2.0 的核心能力——更快的生成速度、更低的单条视频成本，并且使用您现有的同款 API 集成。对于运行高吞吐量流水线或进行大规模原型设计的团队来说，Mini 是最实用的默认选择。](https://www.atlascloud.ai/zh/models/seedance-2.0-mini) [![Recraft Image Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F07b17e93-fb31-4dca-872a-64a1a336b40a.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/recraft.png)Recraft Image\\
\\
The Recraft model family is a premier AI design engine engineered for professional-grade visual creation, distinguished by its superior prompt intelligence and innate aesthetic precision. Renowned for industry-leading vector generation and breathtakingly lifelike photorealism, these models empower creators to generate high-fidelity mockups and custom brand assets with unmatched accuracy. By seamlessly bridging the gap between conceptual prompts and production-ready visuals, Recraft serves as a versatile technical foundation for high-end, scalable creative workflows.](https://www.atlascloud.ai/zh/models/recraft) [![Tools](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2F940555e7-ba39-4b07-a0a4-8151a6934e7d.png&w=3840&q=75)\\
\\
Tools\\
\\
Open, advanced large-scale image generative models that power high-fidelity creation and editing with modular APIs, reproducible training, built-in safety guardrails, and elastic, production-grade inference at scale.](https://www.atlascloud.ai/zh/models/image-video-tools) [![Veo 3 Models](https://www.atlascloud.ai/_next/image?url=https%3A%2F%2Fstatic.atlascloud.ai%2Fuploads%2Fmodel-families%2Fd219b426-378e-4635-b827-83447ceaeb40.png&w=3840&q=75)\\
\\
![](https://www.atlascloud.ai/icons/brands/gemini-color.svg)Veo 3\\
\\
Veo is Google’s generative video model family, designed to produce cinematic-quality clips with natural motion, creative styles, and integrated audio. With options from fast, iterative variants to high-fidelity production outputs, Veo enables seamless text-to-video and image-to-video creation.](https://www.atlascloud.ai/zh/models/veo)

[![](https://www.atlascloud.ai/images/nav-dropdown/icons/gallery.svg)画廊从社区的精彩创作中汲取灵感](https://www.atlascloud.ai/zh/models/explore) [![](https://www.atlascloud.ai/images/nav-dropdown/icons/ai-video-image.svg)AI 视频与图像一键将文字化作惊艳视觉](https://www.atlascloud.ai/zh/models) [![](https://www.atlascloud.ai/images/nav-dropdown/icons/llm.svg)LLM读懂你每个想法的智慧大脑](https://www.atlascloud.ai/zh/models/list/llm) [![](https://www.atlascloud.ai/images/nav-dropdown/icons/audio.svg)音频几秒钟生成完美人声](https://www.atlascloud.ai/zh/models?type=Text-To-Speech) [![](https://www.atlascloud.ai/images/nav-dropdown/icons/3d.svg)3D打造你的专属世界](https://www.atlascloud.ai/zh/models?type=Text-to-3D,Image-to-3D) [![](https://www.atlascloud.ai/images/nav-dropdown/icons/workflow.svg)工作流让专业视频创作更高效顺畅](https://www.atlascloud.ai/zh/console/workflow)

[![](https://www.atlascloud.ai/images/nav-dropdown/icons/docs.svg)文档![](https://www.atlascloud.ai/images/nav-dropdown/icons/arrow-outward.svg)快速上手、玩转平台的入门指南](https://www.atlascloud.ai/docs/zh) [![](https://www.atlascloud.ai/images/nav-dropdown/icons/coding-plan.svg)Coding Plan持续畅享编码算力，激发无限创意](https://www.atlascloud.ai/zh/coding-plan) [![](https://www.atlascloud.ai/images/nav-dropdown/icons/code-blocks.svg)MCP & CLINEW万物互联，无缝集成](https://www.atlascloud.ai/zh/cli)

### 来源 8: LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code

- URL: https://arxiv.org/html/2403.07974
- 精读方法：jina-readerlm-academic

```markdown
# LiveCodeBench: Holistic and Contamination-Free Evaluation of Large Language Models for Code

## Abstract

Large Language Models (LLMs) applied to code-related applications have emerged as a prominent field, attracting significant interest from both academia and industry. However, as new and improved LLMs are developed, existing benchmarks remain insufficient for assessing their capabilities. In this work, we propose **LiveCodeBench**, a comprehensive and contamination-free evaluation of LLMs for code, which integrates various scenarios beyond code generation to capture broader coding abilities.

## Introduction

### Overview

**LiveCodeBench** is a holistic evaluation framework designed to assess the capabilities of LLMs in various areas of code-related tasks. It encompasses four primary scenarios: code generation, self-repair, code execution, and test output prediction. Each scenario addresses different aspects of programming:

- **Code Generation**: Generates correct programs from natural language descriptions.
- **Self-Repair**: Corrects mistakes made by the model during generation.
- **Code Execution**: Executes the generated program to validate correctness.
- **Test Output Prediction**: Predicts the expected output based on input.

### Key Features

#### Data Collection

**Data Collection:** Collects problems from competitions across three platforms: LeetCode, AtCoder, and CodeForces. Problems are sourced from publicly visible portions of these platforms, avoiding paywall or interaction with websites.

#### Problem Curves

**Problem Curves:** The distribution of problem lengths and execution steps is shown in Figures 8(a) and 8(b).

#### Filtering Criteria

**Filtering Criteria:** Programs are filtered based on length (between 100 and 500 characters), syntax errors (no syntax errors), import statements included (necessary imports included), compilation time (length ≤ 3 seconds), runtime conditions (true division, integer operations with at least one argument ≥ 3, string or list operations with at least one argument ≥ 3), finish running in 2 seconds, "reasonable" number of steps (≤ 1000 Python bytecode operations).

#### Dataset Statistics

**Dataset Statistics:** As mentioned in Figure 9(a), the final benchmark consists of 479 samples from 85 distinct problems. The statistics for programs in our dataset are shown in Figure A2.

## Appendix A Dataset

### License

Similar to Hendrycks et al. ([2021](https://arxiv.org/html/2403.07974v2#bib.bib20)), we scrape only the problem statements, ground-truth solutions, and test cases from competition websites – LeetCode, AtCoder, and CodeForces. Further, we only scrape publicly visible portions of websites, avoiding any data collection that might be pay-walled or require login or interaction with the website.

| Model ID | Short Name | Approximate Cutoff Date | Link |
| --- | --- | --- | --- |
| deepseek-ai/deepseek-coder-33b-instruct | DSCoder-33b-Ins | 08/30/2023 | [deepseek-coder-33b-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-33b-instruct) |
| deepseek-ai/deepseek-coder-6.7b-instruct | DSCoder-6.7b-Ins | 08/30/2023 | [deepseek-coder-6.7b-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct) |
| deepseek-ai/deepseek-coder-1.3b-in

### 来源 9: Qwen3-Coder-Next Technical Report

- URL: https://www.arxiv.org/pdf/2603.00729
- 精读方法：jina-readerlm-academic

```markdown
The provided draft Markdown does not match the content of the original HTML, which only contains a head tag with no actual body content. Therefore, there is nothing to extract or refine further into Markdown beyond the title "Your Title" if one were present.
```

### 来源 10: SWE-Compass: Towards Unified Evaluation of Agentic Coding Abilities for Large Language Models

- URL: https://arxiv.org/html/2511.05459v3
- 精读方法：jina-readerlm-academic

```markdown
# SWE-Compass: Towards Unified Evaluation of Agentic Coding Abilities for Large Language Models

## Abstract

Evaluating large language models (LLMs) for software engineering has been limited by narrow task coverage, language bias, and insufficient alignment with real-world developer workflows. Existing benchmarks often focus on algorithmic problems or Python-centric bug fixing, leaving critical dimensions of software engineering underexplored. To address these gaps, we introduce **SWE-Compass**, a comprehensive benchmark that unifies heterogeneous code-related evaluations into a structured and production-aligned framework. SWE-Compass spans 8 task types, 8 programming scenarios, and 10 programming languages, combining broad coverage with rigorous evaluation fidelity. Each instance is paired with executable environments and reproducible tests, enabling fair comparison across prompting and agent-based methods under controlled budgets. Importantly, SWE-Compass is built upon four design principles: (i) real-world alignment, ensuring data originates from genuine developer interactions; (ii) comprehensive coverage across diverse tasks and languages; (iii) systematic taxonomy, providing structured labeling and balanced distributions; and (iv) evaluation fidelity, guaranteeing that all instances are executable and verifiable. Together, these principles yield a benchmark that reflects the complexity, diversity, and reproducibility demanded by modern software engineering.

## Related Works

### Evaluating LLMs for Software Engineering

Large language models (LLMs) trained on code have rapidly advanced from solving algorithmic puzzles to assisting with production-scale software development. Modern coding LLMs excel at a wide range of programming tasks, including code generation, completion, repair, translation, code comprehension, documentation generation, and cross-language migration. These models demonstrate impressive reasoning capabilities in various aspects:

*   **Code Understanding**: Strong ability to comprehend and reason about code semantics.
*   **Feature Enhancement**: Ability to improve or enhance existing components.
*   **Bug Fixing**: Ability to identify and resolve defects in the code.
*   **Refactoring**: Ability to refactor code without altering external functionality.
*   **Performance Optimization**: Ability to optimize system performance without impacting functionality.
*   **Code Writing**: Ability to write new code snippets efficiently.

However, there remains significant variance in model performance across different categories:
- **Bug Fixing** scores are relatively low due to the difficulty in identifying bugs accurately.
- **Refactoring** scores are higher but still lag behind other tasks like Code Understanding.

### Benchmark Construction

SWE-Compass is constructed from authentic software engineering requirements by collecting high-quality pull requests from GitHub repositories. This process includes:
1.  Filtering out irrelevant content such as comments or unrelated projects.
2.  Extracting relevant PRs based on predefined criteria (e.g., high-star status).
3.  Selecting PRs that contain clear modification semantics (e.g., changes made to specific files).

Each selected PR is then processed through an active learning pipeline for task classification and scenario identification.

#### Standardized Offline Build/Test Commands

To ensure reproducible builds and comparable feedback signals across languages:
- Python: `pytest -q`
- JavaScript/TypeScript: `npm ci && npm test --run`
- Java: `mvn -B -DskipTests=false test`
- Go: `go test ./...`
- Rust: `cargo test --locked`
- C/C++: `cmake --build && ctest -j1`

#### Executor Hardening Controls

To minimize offline flakiness and improve determinism:
- Pinned toolchains inside containers.
- Pre-populated offline caches/proxies for pip/pnpm/cargo/Maven/Gradle/go modules.
- Normalization of EOL/encoding (LF/UTF-8).
- Repository navigation pruning by extensions.
- Optional function/class extraction for faster localization.
- Budgets and quotas limiting maximum turns per step.

## Conclusion

We introduced SWE-Compass as a unified benchmark that enables systematic evaluation of large language models across diverse software engineering tasks, scenarios, and languages. By integrating 2000 verified instances derived from real-world GitHub repositories with reproducible execution environments, SWE-Compass provides comprehensive coverage of the software development lifecycle. Our large-scale experiments with ten state-of-the-art LLMs under two agentic frameworks revealed consistent hierarchies of task difficulty across languages and scenarios. Future progress depends less on isolated code generation improvements but more on enhancing requirement grounding, environment reliability, and reasoning consistency.

## Future Works

We see several directions to extend SWE-Compass:
1.  Scale and coverage expansion.
2.


## 跨源矛盾检测结论

### 检测范围
- 已精读来源数量：10 个
- 检测对象：核心数字、日期、功能描述、因果判断、市场/公司事实
- 检测时间：2026-06-20

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
