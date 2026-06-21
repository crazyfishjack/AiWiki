---
title: "调研证据包：Qwen全系列 Kimi全系列 GPT全系列 GLM全系列 Claude全系列 DeepSeek全系列 大模型能力对比 代码跑分 HumanEval MBPP LiveCodeBench SWE-bench 2026年最新"
source-type: article
generated: 2026-06-21
generated-by: wiki-research-skill
research-mode: standard
---

# 调研证据包：Qwen全系列 Kimi全系列 GPT全系列 GLM全系列 Claude全系列 DeepSeek全系列 大模型能力对比 代码跑分 HumanEval MBPP LiveCodeBench SWE-bench 2026年最新

## 调研问题

Qwen全系列 Kimi全系列 GPT全系列 GLM全系列 Claude全系列 DeepSeek全系列 大模型能力对比 代码跑分 HumanEval MBPP LiveCodeBench SWE-bench 2026年最新

## 摘要

本文档是四工具检索生成的证据包草稿，不是最终调研报告。Agent 必须先阅读本证据包，执行下方"AI 综合指令"，生成新的中文综合 raw 报告，然后询问用户是否入库。本证据包保留不删除。

- 发现候选信源：43
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
| exa | 1.00 | Qwen3.5-Omni Technical Report | https://arxiv.org/html/2604.15804 |
| exa | 1.00 | Qwen3 Technical Report | https://arxiv.org/html/2505.09388 |
| exa | 1.00 | OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation | https://arxiv.org/pdf/2604.10866 |
| exa | 1.00 | Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks | https://arxiv.org/html/2606.12344 |
| exa | 1.00 | The Growing Pains of Frontier Models: When Leaderboards Stop Separating and What to Measure Next | https://arxiv.org/html/2605.18840v1 |
| exa | 1.00 |  | https://www.arxiv.org/pdf/2604.08064 |
| exa | 1.00 | React-ing to Grace Hopper 200 Five Open-Weights Coding Models, One React Native App, One GH200, One Weekend or: why SWE-Bench rankings mispredicted which model actually shipped | https://arxiv.org/html/2604.17187v1 |
| exa | 1.00 | GLM-5: from Vibe Coding to Agentic Engineering | https://arxiv.org/html/2602.15763v1 |
| exa | 1.00 | Towards Comprehensive Benchmarking Infrastructure for LLMs In Software Engineering | https://arxiv.org/html/2601.21070 |
| exa | 1.00 | Quantifying the Capability Boundary of DeepSeek Models: An Application-Driven Performance Analysis | https://arxiv.org/html/2502.11164 |
| exa | 1.00 | Meta-analysis of large language models: benchmarking DeepSeek-R1 against ChatGPT, Gemini, Qwen, and LLaMA \| Journal of Big Data \| Springer Nature Link | https://link.springer.com/article/10.1186/s40537-025-01330-3 |
| exa | 1.00 | The ATOM Report: Measuring the Open Language Model Ecosystem | https://arxiv.org/html/2604.07190 |
| exa | 1.00 | Configuration Over Selection: Hyperparameter Sensitivity Exceeds Model Differences in Open-Source LLMs for RTL Generation | https://arxiv.org/pdf/2604.17102 |
| exa | 1.00 | Unified Deployment-Aware Evaluation of Open Reasoning Language Models | https://www.arxiv.org/pdf/2604.07035 |
| tavily | 0.82 | 2026 AI编程能力评测：八大模型全面对比 - U深搜 | https://unifuncs.com/s/RYSb15zp |
| tavily | 0.81 | 2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云 | https://cloud.tencent.com/developer/article/2670420 |
| tavily | 0.81 | 2026年全网最全大模型API横评：Claude / GPT / Gemini等八大厂商 ... | https://news.qiniu.com/archives/1774508972073 |
| tavily | 0.80 | 2026年全网最全大模型API横评：Claude / GPT / Gemini 等8 大厂商 ... | https://segmentfault.com/a/1190000047676047 |
| tavily | 0.80 | 国产模型与海外模型的Coding 能力对比：2026 年程序员该如何选择 | https://segmentfault.com/a/1190000047817400 |
| tavily | 0.79 | 2026 農曆新年，中國開源大模型集體爆發 — Kimi、Qwen、GLM、MiniMax 怎麼選？ | https://ai-coding.wiselychen.com/china-ai-models-2026-lunar-new-year-comparison |
| tavily | 0.78 | 国产三大模型深度对比：性能与性价比深度解析，2026年4月21日 | https://gitcode.csdn.net/69e7629e54b52172bc6b4930.html |
| tavily | 0.77 | 大模型代码编程能力评测排行榜 | https://www.datalearner.com/leaderboards/category/code |
| tavily | 0.76 | 国产开源大模型 2026 全景：Qwen3.6 / GLM-5.1 / Kimi K2.6 / DeepSeek V4 / MiniMax M2.7 五雄并起 | https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026 |
| tavily | 0.75 | 国内外知名大模型及应用——模型/应用维度（2026/06/17） | https://zhuanlan.zhihu.com/p/670574382 |
| tavily | 0.74 | SWE-bench February 2026 leaderboard update | https://simonwillison.net/2026/Feb/19/swe-bench |
| tavily | 0.74 | 大模型之家2026年5月热力榜：当“能干多久”取代“能跑多高” - 澎湃新闻 | https://m.thepaper.cn/newsDetail_forward_33291314 |
| tavily | 0.72 | 2026年全球顶级代码编程大模型深度研究报告：性能、性价比与多模态综合能力全景解析_大数据_yuanmying-DeepSeek技术社区 | https://deepseek.csdn.net/6a0d685d662f9a54cb75db06.html |
| tavily | 0.72 | 国产三巨头谁更强：Kimi K2.6、GLM-5.1、Qwen3.6-Plus | https://deepseek.csdn.net/6a05acca662f9a54cb7480b6.html |
| tavily | 0.71 | 2026 年最佳开源编程大模型：开发者指南 | https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm |

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
2. [Qwen3.5-Omni Technical Report](https://arxiv.org/html/2604.15804)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
3. [Qwen3 Technical Report](https://arxiv.org/html/2505.09388)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
4. [OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation](https://arxiv.org/pdf/2604.10866)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
5. [Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks](https://arxiv.org/html/2606.12344)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
6. [The Growing Pains of Frontier Models: When Leaderboards Stop Separating and What to Measure Next](https://arxiv.org/html/2605.18840v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
7. [https://www.arxiv.org/pdf/2604.08064](https://www.arxiv.org/pdf/2604.08064)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
8. [React-ing to Grace Hopper 200 Five Open-Weights Coding Models, One React Native App, One GH200, One Weekend or: why SWE-Bench rankings mispredicted which model actually shipped](https://arxiv.org/html/2604.17187v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
9. [GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/html/2602.15763v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
10. [Towards Comprehensive Benchmarking Infrastructure for LLMs In Software Engineering](https://arxiv.org/html/2601.21070)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
11. [Quantifying the Capability Boundary of DeepSeek Models: An Application-Driven Performance Analysis](https://arxiv.org/html/2502.11164)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
12. [Meta-analysis of large language models: benchmarking DeepSeek-R1 against ChatGPT, Gemini, Qwen, and LLaMA | Journal of Big Data | Springer Nature Link](https://link.springer.com/article/10.1186/s40537-025-01330-3)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
13. [The ATOM Report: Measuring the Open Language Model Ecosystem](https://arxiv.org/html/2604.07190)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
14. [Configuration Over Selection: Hyperparameter Sensitivity Exceeds Model Differences in Open-Source LLMs for RTL Generation](https://arxiv.org/pdf/2604.17102)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
15. [Unified Deployment-Aware Evaluation of Open Reasoning Language Models](https://www.arxiv.org/pdf/2604.07035)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
16. [2026 AI编程能力评测：八大模型全面对比 - U深搜](https://unifuncs.com/s/RYSb15zp)
   - 工具：tavily
   - 分数：0.82
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
17. [2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云](https://cloud.tencent.com/developer/article/2670420)
   - 工具：tavily
   - 分数：0.81
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
18. [2026年全网最全大模型API横评：Claude / GPT / Gemini等八大厂商 ...](https://news.qiniu.com/archives/1774508972073)
   - 工具：tavily
   - 分数：0.81
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
19. [2026年全网最全大模型API横评：Claude / GPT / Gemini 等8 大厂商 ...](https://segmentfault.com/a/1190000047676047)
   - 工具：tavily
   - 分数：0.80
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
20. [国产模型与海外模型的Coding 能力对比：2026 年程序员该如何选择](https://segmentfault.com/a/1190000047817400)
   - 工具：tavily
   - 分数：0.80
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
21. [2026 農曆新年，中國開源大模型集體爆發 — Kimi、Qwen、GLM、MiniMax 怎麼選？](https://ai-coding.wiselychen.com/china-ai-models-2026-lunar-new-year-comparison)
   - 工具：tavily
   - 分数：0.79
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
22. [国产三大模型深度对比：性能与性价比深度解析，2026年4月21日](https://gitcode.csdn.net/69e7629e54b52172bc6b4930.html)
   - 工具：tavily
   - 分数：0.78
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
23. [大模型代码编程能力评测排行榜](https://www.datalearner.com/leaderboards/category/code)
   - 工具：tavily
   - 分数：0.77
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
24. [国产开源大模型 2026 全景：Qwen3.6 / GLM-5.1 / Kimi K2.6 / DeepSeek V4 / MiniMax M2.7 五雄并起](https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026)
   - 工具：tavily
   - 分数：0.76
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
25. [国内外知名大模型及应用——模型/应用维度（2026/06/17）](https://zhuanlan.zhihu.com/p/670574382)
   - 工具：tavily
   - 分数：0.75
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
26. [SWE-bench February 2026 leaderboard update](https://simonwillison.net/2026/Feb/19/swe-bench)
   - 工具：tavily
   - 分数：0.74
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
27. [大模型之家2026年5月热力榜：当“能干多久”取代“能跑多高” - 澎湃新闻](https://m.thepaper.cn/newsDetail_forward_33291314)
   - 工具：tavily
   - 分数：0.74
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
28. [2026年全球顶级代码编程大模型深度研究报告：性能、性价比与多模态综合能力全景解析_大数据_yuanmying-DeepSeek技术社区](https://deepseek.csdn.net/6a0d685d662f9a54cb75db06.html)
   - 工具：tavily
   - 分数：0.72
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
29. [国产三巨头谁更强：Kimi K2.6、GLM-5.1、Qwen3.6-Plus](https://deepseek.csdn.net/6a05acca662f9a54cb7480b6.html)
   - 工具：tavily
   - 分数：0.72
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
30. [2026 年最佳开源编程大模型：开发者指南](https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm)
   - 工具：tavily
   - 分数：0.71
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 技术文档
   - 后续处理：进入精读
31. [大模型套餐深度分析：国内外主流平台全景对比- SkySeraph - 博客园](https://www.cnblogs.com/skyseraph/p/19966095)
   - 工具：tavily
   - 分数：0.71
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
32. [Best LLMs for coding: 2026 roundup - Fireworks AI](https://fireworks.ai/blog/best-llms-for-coding)
   - 工具：tavily
   - 分数：0.71
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
33. [【2025年度】编程大模型对比与总结-CSDN博客](https://blog.csdn.net/qq_44810930/article/details/157262891)
   - 工具：tavily
   - 分数：0.69
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
34. [SuperCLUE中文大模型测评基准-AI评测榜单](https://www.superclueai.com)
   - 工具：tavily
   - 分数：0.66
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
35. [知识 - 大模型测评完全指南：2026 年主流 LLM 评测体系、榜单解读与选型建议 - 个人文章 - SegmentFault 思否](https://segmentfault.com/a/1190000047645758)
   - 工具：tavily
   - 分数：0.64
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
36. [Kimi K2.6 vs GLM 5.1 vs Qwen 3.6 Plus vs MiniMax M2.7: Which Open Source Model Wins for Coding in 2026 - Atlas Cloud Blog](https://www.atlascloud.ai/blog/guides/kimi-k2-6-vs-glm-5-1-vs-qwen-3-6-plus-vs-minimax-m2-7-coding-2026)
   - 工具：tavily
   - 分数：0.63
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 技术文档
   - 后续处理：进入精读
37. [Best LLMs for Coding in 2026: SWE-bench, HumanEval ... - Onyx AI](https://onyx.app/insights/best-llms-for-coding-2026)
   - 工具：tavily
   - 分数：0.62
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
38. [SWE-bench Verified - Vals AI](https://vals.ai/benchmarks/swebench)
   - 工具：tavily
   - 分数：0.60
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
39. [各厂家Coding Plan 实际价值对比 - GitHub](https://github.com/mahonzhan/awesome-coding-plan)
   - 工具：tavily
   - 分数：0.59
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
40. [AI大模型列表- 评测结果、参数与价格汇总](https://www.datalearner.com/ai-models/pretrained-models)
   - 工具：tavily
   - 分数：0.58
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
41. [大模型 LLM 架构对比，DeepSeek、Llama、Qwen、Kimi、Mistral、Gemma-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2551575)
   - 工具：tavily
   - 分数：0.54
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
42. [LLM Rank - 大型语言模型评测及排行榜](https://llmrank.cn)
   - 工具：tavily
   - 分数：0.51
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
43. [国产AI编程冲上全球第二！实测五大模型，谁才是Vibe Coding神器](https://www.ifanr.com/1667180)
   - 工具：tavily
   - 分数：0.47
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考

### 剔除信源
1. [2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云](https://cloud.tencent.com/developer/article/2670420)
   - 工具：tavily
   - 分数：0.76
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
2. [国产三大模型深度对比：性能与性价比深度解析，2026年4月21日](https://gitcode.csdn.net/69e7629e54b52172bc6b4930.html)
   - 工具：tavily
   - 分数：0.73
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
3. [国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏](https://zhuanlan.zhihu.com/p/670574382)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
4. [大模型代码编程能力评测排行榜](https://www.datalearner.com/leaderboards/category/code)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
5. [2026 AI编程能力评测：八大模型全面对比 - UniFuncs](https://unifuncs.com/s/RYSb15zp)
   - 工具：tavily
   - 分数：0.80
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
6. [2026 年 AI 编程实测：6 款顶流大模型对比，效率直接翻倍！-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2670420)
   - 工具：tavily
   - 分数：0.76
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
7. [国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏](https://zhuanlan.zhihu.com/p/670574382)
   - 工具：tavily
   - 分数：0.73
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
8. [大模型代码编程能力评测排行榜 - SWE-Bench / LiveCodeBench / SWE-Bench Pro【2026年6月更新】- 实时数据与场景解读 | DataLearnerAI](https://www.datalearner.com/leaderboards/category/code)
   - 工具：tavily
   - 分数：0.72
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
9. [2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云](https://cloud.tencent.com/developer/article/2670420)
   - 工具：tavily
   - 分数：0.77
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
10. [2026年全网最全大模型API横评：Claude / GPT / Gemini等八大厂商 ...](https://news.qiniu.com/archives/1774508972073)
   - 工具：tavily
   - 分数：0.77
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
11. [国产三大模型深度对比：性能与性价比深度解析，2026年4月21日](https://gitcode.csdn.net/69e7629e54b52172bc6b4930.html)
   - 工具：tavily
   - 分数：0.74
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
12. [国产开源大模型2026 全景：Qwen3.6 / GLM-5.1 / Kimi K2.6 ... - OfoxAI](https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026)
   - 工具：tavily
   - 分数：0.72
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
13. [大模型代码编程能力评测排行榜](https://www.datalearner.com/leaderboards/category/code)
   - 工具：tavily
   - 分数：0.71
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
14. [国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏](https://zhuanlan.zhihu.com/p/670574382)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
15. [人工智能 - 2026年全网最全大模型API横评：Claude / GPT / Gemini 等8 大厂商 20+ 主流模型 - 个人文章 - SegmentFault 思否](https://segmentfault.com/a/1190000047676047)
   - 工具：tavily
   - 分数：0.78
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
16. [2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云](https://cloud.tencent.com/developer/article/2670420)
   - 工具：tavily
   - 分数：0.78
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
17. [国产开源大模型2026 全景：Qwen3.6 / GLM-5.1 / Kimi K2.6 ... - OfoxAI](https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026)
   - 工具：tavily
   - 分数：0.74
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
18. [大模型代码编程能力评测排行榜](https://www.datalearner.com/leaderboards/category/code)
   - 工具：tavily
   - 分数：0.72
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
19. [国产三巨头谁更强：Kimi K2.6、GLM-5.1、Qwen3.6-Plus](https://deepseek.csdn.net/6a05acca662f9a54cb7480b6.html)
   - 工具：tavily
   - 分数：0.71
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
20. [国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏](https://zhuanlan.zhihu.com/p/670574382)
   - 工具：tavily
   - 分数：0.72
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
21. [2026 年最佳开源编程大模型：开发者指南](https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
22. [各厂家Coding Plan 实际价值对比 - GitHub](https://github.com/mahonzhan/awesome-coding-plan)
   - 工具：tavily
   - 分数：0.58
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果

## 完整精读结果

### 来源 1: 国产开源大模型 2026 全景：Qwen3.6 / GLM-5.1 / Kimi K2.6 / DeepSeek V4 / MiniMax M2.7 五雄并起

- URL: https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026
- 精读方法：firecrawl-scrape

![国产开源大模型 2026 全景：Qwen3.6 / GLM-5.1 / Kimi K2.6 / DeepSeek V4 / MiniMax M2.7 五雄并起](https://ofox.ai/blog/_assets/zh-open-source-llm-china-roundup-2026-hero.DkZOf6qp_1iO9Qe.webp)

May 25, 2026

model-comparisonopen-sourcechina-guideqwenglm

# 国产开源大模型 2026 全景：Qwen3.6 / GLM-5.1 / Kimi K2.6 / DeepSeek V4 / MiniMax M2.7 五雄并起

**TL;DR** — 2026 年 4 月，中国五家头部厂商在一个月内集中发布新一代大模型，其中 GLM-5.1、Kimi K2.6、Qwen3.6 系列（开源版）走开源权重路线，DeepSeek V4 Preview 和 MiniMax M2.7 走 API 优先。这不是巧合：开源国产首次同时在编程（GLM-5.1 达 Claude Opus 4.6 的 94.6%）、Agent（Kimi K2.6 SWE-Bench Pro 58.6%）、长上下文（Qwen3.6-Plus 1M tokens 默认）三条线上挑战闭源旗舰。本文按场景拆五雄定位。

## 一周时间表：4 月发生的事按日列出来

- **4 月 2 日** — 阿里发布 Qwen3.6-Plus，1M token 上下文默认开启，闭源 API
- **4 月 7 日** — 智谱开源 GLM-5.1，MIT 协议，编程能力达 Claude Opus 4.6 的 94.6%
- **4 月 16 日** — 阿里把 Qwen3.6-35B-A3B 以 Apache 2.0 放上 Hugging Face
- **4 月 20 日** — Moonshot 开源 Kimi K2.6（1T MoE / 32B active）；同日阿里发 Qwen3.6-Max-Preview
- **4 月 22 日** — Qwen3.6-27B 跟进开源
- **4 月 24 日** — DeepSeek V4 Preview 上线，V4-Pro 1.6T total / 49B active，V4-Flash 284B / 13B active

MiniMax M2.7 早一个多月（3 月 18 日）上线，但 4 月的对比叙事离不开它，因此一并纳入。

## 五雄速览表

| 模型 | 厂商 | 发布日 | 总参数 / 激活 | 上下文 | 协议 / 开源 | 一句话定位 |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3.6-Plus | 阿里 | 2026-04-02 | 未公开 | 1M | 闭源 API | 长上下文工程 Agent |
| Qwen3.6-Max-Preview | 阿里 | 2026-04-20 | 未公开 | 260K | 闭源 API | 旗舰 benchmark 冠军 |
| Qwen3.6-35B-A3B | 阿里 | 2026-04-16 | 35B / 3B（MoE） | 256K | Apache 2.0 | 中等推理成本社区款 |
| Qwen3.6-27B | 阿里 | 2026-04-22 | 27B（稠密） | 256K | Apache 2.0 | 单卡可跑入门款 |
| GLM-5.1 | 智谱（Z.ai） | 2026-04-07 | 未完全披露 | 200K | MIT 开源 | 编程接近 Claude Opus |
| Kimi K2.6 | Moonshot | 2026-04-20 | 1T / 32B（MoE） | 256K | Modified MIT | Agent Swarm 多步编排 |
| DeepSeek V4-Pro | DeepSeek | 2026-04-24 | 1.6T / 49B（MoE） | 1M | 闭源 API（预览） | 综合旗舰 |
| DeepSeek V4-Flash | DeepSeek | 2026-04-24 | 284B / 13B（MoE） | 1M | 闭源 API（预览） | 低延迟高吞吐 |
| MiniMax M2.7 | MiniMax | 2026-03-18 | 230B / 10B（MoE） | 200K | 半开放 API | 性价比之王 |

下面按厂商拆。

## Qwen3.6 系列：阿里”全栈打法”，闭源做企业，开源养社区

Qwen3.6 的关键不是某一个模型，而是阿里用一套品牌名同时打了四张牌。4 月 2 日先放出闭源的 Qwen3.6-Plus，主打企业级 agentic 编码和 1M token 默认上下文，直接对标 Claude Sonnet 4.6 的 repo 级理解能力；4 月 16 日和 22 日分别放出 Qwen3.6-35B-A3B（MoE，3B 激活）和 Qwen3.6-27B（稠密），都是 Apache 2.0；4 月 20 日 Qwen3.6-Max-Preview 上线，260K 上下文，在 SWE-bench Pro、Terminal-Bench 2.0、SciCode 等六个 agentic 编码 benchmark 拿第一。

这套打法的含义：阿里把”商业产品 \+ 社区开源”分了赛道。要 SLA、要 1M 上下文、要企业部署找 Plus / Max；要本地跑、要研究、要二次微调拉 35B-A3B / 27B。两条路共用 Qwen3 tokenizer 和工具调用格式，意味着从开源切到闭源不用重写 prompt。

如果只关注 Qwen3 API 的接入流程，已经写过 [通义千问 Qwen API 接入指南](https://ofox.ai/zh/blog/qwen-api-guide-qwen3-max-qwen3-6-2026)，本文不重复。

## GLM-5.1：把 Claude Opus 4.6 编程性能逼到 94.6%，还全华为昇腾训练

GLM-5.1 这一代最具公关效应的事实有两个：编程能力达到 Claude Opus 4.6 的 94.6%（智谱官方与 WaveSpeed、DigitalApplied 测试一致），以及训练算力全程华为昇腾，没有 NVIDIA 卡参与。MIT 协议开源，商用零限制。

放在国产开源谱系里看，GLM-5.1 把开源和闭源的最大差距压到了一个相当窄的带宽。Claude Opus 4.6 当前的 API 单价远高于 GLM-5.1 在云厂商上的价格。对于编程为主、能容忍 4 个百分点差距的团队，GLM-5.1 是真的可以替代闭源旗舰的。

关于 GLM-5 系列的 API 接入和具体定价，详见 [GLM-5 API 接入完全指南](https://ofox.ai/zh/blog/glm-5-api-guide-coding-agent-2026)。GLM-5.1 的 API 路径和 GLM-5 完全一致，只需要把 model 字段换成 `glm-5.1` 即可。

## Kimi K2.6：1T MoE 加上 Agent Swarm，把”开源 Agent”推到能交付完整产物

Kimi K2.6 不是一个对话模型，是一个原生 Agent 平台。Moonshot 在 4 月 20 日把它以 Modified MIT 开源：1T 总参数，32B 激活，原生多模态，自带 Agent Swarm 编排能力，可以同时调度 300 个领域子代理，在一次自主运行中执行最多 4000 步协调动作。

Agent Swarm 这一层是真正的代差。“模型会调工具”K2.5 就有了，K2.6 的差别是能把一个复杂任务拆成并行子任务，再把子任务结果合成一份成品。官方演示给的是三类完整交付物：研究报告、可运行网站、数据电子表格。

跑分上，K2.6 在 SWE-Bench Pro 拿到 58.6%，与 GPT-5.5 持平；Humanity’s Last Exam（带工具）拿到 54.0%，超过 Claude Opus 4.6；token 单价大约只有 GPT-5.5 的五分之一。

要看 K2.5 的编程实测和 Agent Swarm 实际用法可以参考 [Kimi K2.5 编程能力实测](https://ofox.ai/zh/blog/kimi-k2-5-coding-capability-benchmark-2026) 和 [Kimi K2.5 Agent Swarm + 多模态 API 实战](https://ofox.ai/zh/blog/kimi-k2-5-agent-swarm-multimodal-api-guide-2026)，K2.6 是同一套 API，差别在模型 ID。

## DeepSeek V4 Preview：1.6T + 284B 双线策略，1M 上下文默认开启

DeepSeek 4 月 24 日上线 V4 Preview，几乎每个维度都重写了：参数量、注意力架构、训练方法。两个变体 deepseek-v4-pro（1.6T 总 / 49B 激活）和 deepseek-v4-flash（284B 总 / 13B 激活）同时开放 API，1M 上下文，384K 最大输出。

Pro 走复杂推理、agentic 编码、长上下文工程，Flash 走延迟敏感场景。值得注意的过渡安排：旧的 `deepseek-chat` 和 `deepseek-reasoner` 在 7 月 24 日下线，向后兼容期被映射到 deepseek-v4-flash 的非思考 / 思考模式上。

这是一个对国内开发者影响最大的发布。DeepSeek 一直是性价比标杆，V4 把价格带保持住的同时把上下文拉到了 1M。这是闭源旗舰里第一家把 1M 默认开启、而不是按溢价档收费的。

具体接入参数和迁移注意事项见 [DeepSeek V4 API 接入指南](https://ofox.ai/zh/blog/deepseek-v4-api-guide-2026)。

## MiniMax M2.7：用 10B 激活拿到接近 GLM-5.1 的成绩

M2.7 不是 4 月发布，是 3 月中旬，但是 4 月所有横评里几乎都被拉来对比。原因很简单：在 Atlas Cloud 的 SWE-Bench Pro 测试里，M2.7 拿到 56.22%，是 GLM-5.1 的 94%；但只激活 10B 参数，单价约为 $0.30 / M 输入 token，大约是 GLM-5.1 的五分之一。

这是一个被低估的事实：MoE 架构走到 M2.7 这一代，激活参数和实际能力的解耦已经相当成熟。十分之一的激活规模拿到九成性能，意味着部署成本曲线被压平。对于跑高并发对话、文档分类、批量数据处理这类不要求极致推理深度的工作负载，M2.7 是当前性价比最高的选择。

关于 M2.7 的具体能力和 TTS / 多模态 API 用法，见 [MiniMax M2.7 编程实测 + TTS 语音 API 实战](https://ofox.ai/zh/blog/minimax-m2-7-coding-tts-practical-guide-2026) 和 [MiniMax 多模态 API 全攻略](https://ofox.ai/zh/blog/minimax-multimodal-api-complete-guide-2026)。

## 怎么选：四个真实场景的对应

不要按”哪个模型最强”选，按你的工作负载选。

**场景一：本地部署 / 私有云推理。** 优先 Qwen3.6-35B-A3B（MoE，3B 激活，单台 80GB 卡可跑）或 Qwen3.6-27B（稠密，更易上量）。如果有更高编程要求且能接受 200B+ 部署成本，自己跑 GLM-5.1 权重。Kimi K2.6 1T MoE 本地跑成本过高，除非有 H100 集群，否则不实际。

**场景二：编程 Agent 为主，调 API。** GLM-5.1 是性价比 + 性能甜点。如果预算允许，Qwen3.6-Plus 因为 1M 默认上下文，在 repo 级理解上更不容易掉精度。Kimi K2.6 适合需要多步骤自主交付的场景（研究 / 自动生成完整代码库）。

**场景三：客服 / 文档处理 / 高并发对话。** MiniMax M2.7 性价比最强。如果想要更稳定的延迟，DeepSeek V4-Flash 是当前所有 API 里 1M 上下文 + 低单价的最佳组合。

**场景四：综合应用，多个工作负载混合。** 没有单一最优解。常见做法是：编程用 GLM-5.1 / Claude Sonnet 4.6，对话用 MiniMax M2.7 或 DeepSeek V4-Flash，长上下文工程用 Qwen3.6-Plus 或 DeepSeek V4-Pro，Agent 编排用 Kimi K2.6。这就引出下一个问题：怎么避免维护五套 SDK。

## 一站式调用：避免五个 Key、五种 SDK、五张账单

五雄并起的副作用是 API 治理变复杂。每家都自定义了一套鉴权头、错误码、SDK 包名，迁移成本会随着模型数量线性涨。OpenAI 兼容的 AI API 聚合平台（如 [ofox.ai](https://ofox.ai/)）的价值在这里：一个 OpenAI 兼容的 endpoint，model 字段换名字就切换模型，结算合并到一张账单，不用为每家维护独立的客户端和监控。

需要做横评、A/B 测试、灰度切流的团队，这种方案的运维成本节省尤其明显。具体的迁移和对比参考 [OpenRouter 替代方案：OfoxAI vs OpenRouter](https://ofox.ai/zh/blog/openrouter-alternative-ofoxai-comparison-migration-2026)。

## 接下来值得关注的几个问题

写到这里，几个真正影响选型的悬念其实还没有答案，留给后续测：

1. **GLM-5.1 在长链路 Agent 任务上的稳定性** — 跑分接近 Claude Opus 4.6 不等于在 1000 步的真实 workflow 里同样稳定，需要在工程环境里跑一段时间才能下结论
2. **Qwen3.6-Plus 1M 上下文的有效衰减点** — 默认 1M 不等于 1M 全部可用，要看在 700K-900K 区间检索准确率掉多少
3. **DeepSeek V4 Preview 转 GA 的定价** — 当前是 preview 价格，正式定价可能调整，迁移规划要预留缓冲
4. **Kimi K2.6 Agent Swarm 的可观测性** — 300 个子代理并行调度的状态追踪和失败回滚目前文档很薄，工程化使用要自己补一层

这五个模型不会有一个”最强”的答案。但 4 月这一波集中发布把开源国产的能力下限抬高了一截。对国内开发者，结果是选型从”挑一个能用的将就”，变成了”按场景挑最合适的”。

* * *

**数据来源**：阿里云博客（Qwen3.6-Plus 发布稿）、Qwen 官方博客（Max-Preview）、Hugging Face Hub（Qwen3.6-35B-A3B / 27B 模型卡）、Z.ai / 智谱 GLM-5.1 开源公告、Hugging Face mlabonne GLM-5 评测、DeepSeek API Docs（V4 Preview 发布公告、changelog）、Moonshot Kimi K2.6 模型页、Atlas Cloud SWE-Bench Pro 横评（MiniMax M2.7）。所有版本号与发布日期截止 2026 年 5 月。

### 相关文章

[![](https://ofox.ai/blog/_assets/zh-qwen3-6-vs-glm-5-1-hero.MnfI3cib_6PTAp.webp)\\
**Qwen3.6 vs GLM-5.1：国产开源权重对决，27B 小钢炮和 754B MoE 谁更适合你（2026）** May 24, 2026](https://ofox.ai/zh/blog/qwen3-6-vs-glm-5-1-open-weight-china-2026/) [![](https://ofox.ai/blog/_assets/zh-qwen3-7-max-coding-hero.C6OaFt6b_1YyC1y.webp)\\
**Qwen3.7-Max 实测：Code Arena 第4、Elo 1541，价格是 Claude Opus 三分之一** May 27, 2026](https://ofox.ai/zh/blog/qwen-3-7-max-bianma-pingce-code-arena-vs-claude-2026/) [![](https://ofox.ai/blog/_assets/zh-china-open-source-llm-flagship-showdown-2026-hero.B-nZLLeY_Z2tOfGH.webp)\\
**国产开源大模型旗舰横评 2026：DeepSeek、Qwen、Kimi 谁是真正的开源王者** May 24, 2026](https://ofox.ai/zh/blog/china-open-source-llm-flagship-showdown-2026/)

[← 返回文章列表](https://ofox.ai/zh/blog/)

### 来源 2: 2026年全网最全大模型API横评：Claude / GPT / Gemini等八大厂商 ...

- URL: https://news.qiniu.com/archives/1774508972073
- 精读方法：firecrawl-scrape

# 502 Bad Gateway

* * *

openresty

### 来源 3: 2026 農曆新年，中國開源大模型集體爆發 — Kimi、Qwen、GLM、MiniMax 怎麼選？

- URL: https://ai-coding.wiselychen.com/china-ai-models-2026-lunar-new-year-comparison
- 精读方法：firecrawl-scrape

**作者：** Wisely Chen
**日期：** 2026 年 2 月
**系列：** AI Agent 完整指南 / IT 架構系列
**關鍵字：** 開源模型比較, Agent 選型, 成本優化, MoE 架構, 中文模型, Benchmark 對比

* * *

## 為什麼要寫這篇

今年農曆新年對中國 AI 產業來說是個分水嶺。

1 月底 Kimi K2.5 發布後，2 月份各大廠商火力全開： **阿里 Qwen3.5**（成本 -60%）、 **智譜 GLM-5**（Intelligence Index 50+）、 **MiniMax M2.5**（速度最快）、 **字節 Seedance 2.0**（影片生成被馬斯克點讚）。

短短一個月內，就像集體按下了「加速鍵」。

但問題隨之而來： **該用誰？**

是用 Kimi K2.5 的 Agent Swarm 做複雜自動化？還是用 Qwen3.5 省一大筆成本？編程應用是選 GLM-5 還是 MiniMax？

所以這篇我不只深入 Kimi K2.5，而是把 **春節檔主角全部拉出來橫向對比**。核心結論是：

**沒有「最好的模型」，只有「最適合場景的模型」。** 開源模型的性價比已經逼近國際頂級閉源模型——但前提是你得懂怎麼選。

* * *

## 30 秒看懂四大主角

| 維度 | Kimi K2.5 | Qwen3.5 | GLM-5 | MiniMax M2.5 |
| --- | --- | --- | --- | --- |
| **總參數** | 1T (MoE) | 397B (MoE) | 744B (MoE) | 230B |
| **激活參數** | 32B (3.2%) | 170B | 400B | - |
| **上下文** | 256K | 256K | 256K | 256K |
| **輸入成本** | $0.60/M | ~$0.20/M | ~$0.30/M | ~$0.15/M |
| **主要優勢** | Agent Swarm + 多模態 | 成本低 60% | 推理能力 | 速度 \+ Tool Calling |
| **開源授權** | Modified MIT | MIT | MIT | MIT |
| **廠商** | Moonshot AI | 阿里巴巴 | 智譜 AI | MiniMax |

一句話版：

- **Kimi K2.5**：100 個子代理同時幹活，看圖看影片，Agent 最強
- **Qwen3.5**：最省錢，成本比前代便宜 60%，企業大規模應用首選
- **GLM-5**：推理最強，Intelligence Index 50+，與 Claude Opus 4.5 持平
- **MiniMax M2.5**：速度最快，Tool Calling 最精準，高吞吐量場景首選

* * *

## Kimi K2.5：Agent Swarm 革命

Kimi K2.5 的詳細技術評估我已經在 [另一篇文章](https://ai-coding.wiselychen.com/kimi-k2-5-agent-swarm-deep-dive-technical-assessment/) 寫過。這裡只講跟其他三個模型比較時的關鍵差異。

### 獨門武器：Agent Swarm

Kimi K2.5 跟其他三個模型最本質的差異，就是 **原生的群體協作能力**。

傳統 Agent 線性執行 50 個子任務要 50 分鐘。Kimi 的編排器（Orchestrator）可以把任務拆成 DAG 圖譜，最多派 **100 個專用子代理** 同時運作，單次任務最高 **1,500 次工具調用**。同樣的 50 個任務，大約 11 分鐘搞定。

BrowseComp 的數據更直接：標準模式 60.6%，開啟 Swarm 模式後飆到 **78.4%**。

### 原生多模態

四個模型裡， **只有 Kimi K2.5 是從第一天就視覺和文本混合訓練的**。集成 4 億參數的 MoonViT 編碼器，不需要把圖片「翻譯」成文字再推理。

VideoMMMU 86.6%，超過 GPT-5.2 的 85.9%。其他三個模型都沒有這個級別的視頻理解能力。

要澄清： **音頻不是 K2.5 的原生能力**，Moonshot AI 有獨立的 Kimi-Audio 模型，App 端是串起來用的。

### 適用場景

複雜 Agent 自動化（情報分析、競爭監控）、視覺編碼（UI 圖轉代碼）、需要多模態的應用。輸入成本 $0.60/M tokens，是 Claude 的 12%。

* * *

## Qwen3.5：成本戰新王者

**發布日期：** 2026 年 2 月 16 日
**廠商：** 阿里巴巴

Qwen3.5 是這個春節檔最有野心的定價殺手。參數量 397B，MoE 架構激活 170B 推理。

### 成本優勢：-60% 怎麼做到的

不是虛假宣傳，而是真實的計算效率提升：

- **FP8 量化 + MoE 優化**：8-bit 低精度和混合專家選擇，推理成本大幅下降
- **吞吐量提升 8 倍**：同樣的 GPU 資源，能處理 8 倍的並發請求
- **API 定價**：輸入成本約 $0.20/1M tokens（Kimi 的三分之一）

對企業來說： **同樣 $10,000 的預算，用 Qwen3.5 能跑 3 倍 Kimi 的工作量，25 倍 Claude 的工作量。**

### Qwen3.5-Coder：編程的本地部署方案

同時發布的 **Qwen3.5-Coder-Next**，233B 參數，每次推理激活約 30B，可在單張 H100 上本地運行。

這意味著：企業可以直接在自己的伺服器上部署，整個代碼審查過程不出海，成本還比 API 便宜 40%。對「數據隱私 + 編碼需求」的場景，這是目前最務實的選擇。

### 適用場景

成本敏感的企業 AI 應用、大規模 RAG（256K context）、長文檔分析、本地部署編程工具。

* * *

## GLM-5：推理能力的天花板

**發布日期：** 2026 年 2 月 11-12 日
**廠商：** 智譜 AI

GLM-5 是春節檔最「硬核」的發布。744B 參數，每次推理激活 400B——激活的參數量比 Qwen3.5 整體激活參數（170B）還多一倍以上。

### Intelligence Index 首次突破 50

智譜公布的 **Intelligence Index**（智力指數），GLM-5 是首款達到 50+ 的開源模型：

- **GLM-5**: 50.2
- **Claude Opus 4.5**: 50.0
- **GPT-5.2**: 49.8

這是 7 個標準化 Benchmark 的加權平均。直白說： **GLM-5 的推理能力已經與國際頂級閉源模型持平。**

### 編程能力

HumanEval 達 92.8%，是四個模型裡代碼生成最強的。LiveCodeBench 89.2%，也是最高。如果你的需求是「寫代碼」而不是「修代碼」，GLM-5 是最佳選擇。

（「修代碼」還是 Claude SWE-Bench 80.9% 最穩。）

### 適用場景

複雜推理任務、編程應用（代碼生成和審查）、需要「不輸國際頂級」的場景。輸入成本約 $0.30/M tokens。

* * *

## MiniMax M2.5：速度和精準的平衡點

**發布日期：** 2026 年 2 月 11-12 日
**廠商：** MiniMax

MiniMax M2.5 是最「低調」卻最「務實」的選擇。參數量只有 230B，遠小於其他三個，卻在實際應用場景上表現出色。

### Tool Calling 最精準

MiniMax 在 **τ-Bench**（Tau-Bench）上獲得 77.2%，超過所有對手。這個測試專門考察模型調用外部工具的能力：理解什麼時候需要調用工具、正確填充參數、根據返回結果推理、處理調用失敗。

在 OpenClaw、Dify、n8n 這類 Agent 框架中， **Tool Calling 的精準度直接決定自動化流程的成功率。**

### 速度和成本

較小的參數量帶來實際好處：

- **吞吐量最高**：同樣硬體下能處理最多的並發請求
- **延遲最低**：首字出現時間最短
- **成本最低**：輸入成本約 $0.15/1M tokens，比 Claude 便宜 33 倍

### 適用場景

高吞吐量 Agent 應用（精準 Tool Calling）、批量處理、成本極限優化、需要低延遲的實時應用。

* * *

## Benchmark 全面對比

| 測試領域 | Benchmark | Kimi K2.5 | GLM-5 | Qwen3.5 | MiniMax M2.5 | GPT-5.2 | Claude Opus |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 代理協同 | HLE-Full (w/ Tools) | **50.2%** | 48.6% | 47.2% | 45.1% | 45.5% | 43.2% |
| 代理搜索 | BrowseComp | **78.4%** | 72.3% | 68.5% | 71.2% | 65.8% | 57.8% |
| Tool Calling | τ-Bench | 74.6% | 76.1% | 74.8% | **77.2%** | 72.3% | 68.9% |
| 程式修復 | SWE-Bench | 76.8% | 77.2% | 75.4% | 71.3% | 80.0% | **80.9%** |
| 代碼生成 | HumanEval | 87.3% | **92.8%** | 89.1% | 85.6% | 90.2% | 88.4% |
| 視覺數學 | MathVision | **84.2%** | 81.5% | 79.8% | 77.2% | 83.0% | N/A |
| 純數學推理 | AIME 2025 | 96.1% | 95.2% | 94.8% | 93.1% | **100%** | 92.8% |
| 長視頻理解 | VideoMMMU | **86.6%** | N/A | N/A | N/A | 85.9% | 82.1% |
| 即時編程 | LiveCodeBench | 85.0% | **89.2%** | 84.5% | 82.1% | 87.3% | 64.0% |
| 中文理解 | CMMLU | 84.5% | **92.1%** | 89.3% | 86.2% | 80.2% | 79.1% |

### 各模型的贏點

- **Kimi K2.5**：Agent 協同、代理搜索、多模態（視覺、視頻）全部第一
- **GLM-5**：代碼生成 92.8%、即時編程 89.2%、中文理解 92.1%，三項第一
- **MiniMax M2.5**：Tool Calling 77.2% 第一，速度和成本最優
- **Qwen3.5**：沒有突出的單項第一，但全面均衡且成本最低

### 「最強」不等於「最適合」

拿 SWE-Bench 來說：

- **Claude 80.9%** — 你負責 Linux 內核補丁，需要接近 100% 正確率，選 Claude
- **GLM-5 77.2%** — 創業公司寫業務邏輯，77% 夠用，而且便宜 17 倍
- **Kimi 76.8%** — 需要邊寫程式邊看設計文檔（多模態），Kimi 是唯一選擇

問題不是「誰最強」，而是「你的場景對什麼最敏感」。

* * *

## 成本對比：這才是企業最關心的

| 模型 | 輸入 ($/1M) | 輸出 ($/1M) | vs Claude 輸入成本 |
| --- | --- | --- | --- |
| **MiniMax M2.5** | ~$0.15 | ~$0.50 | 便宜 33 倍 |
| **Qwen3.5** | ~$0.20 | ~$0.80 | 便宜 25 倍 |
| **GLM-5** | ~$0.30 | ~$1.20 | 便宜 17 倍 |
| **Kimi K2.5** | $0.60 | $2.50 | 便宜 8 倍 |
| GPT-5.2 | $1.25 | $10.00 | 便宜 4 倍 |
| Claude Opus 4.5 | $5.00 | $25.00 | 基準 |

**心得：** 同樣預算，Kimi K2.5 可以跑 8 倍的工作量（vs Claude）。選 MiniMax 或 Qwen，可以跑 25-33 倍。

### 本地部署成本

| 模型 | 激活參數 | GPU 需求 | 月度成本 | 適用場景 |
| --- | --- | --- | --- | --- |
| **Qwen3.5-Coder** | 30B | 1x H100 | ~$2,500 | 編程團隊、數據隱私 |
| **MiniMax M2.5** | - | 1x A100 | ~$1,800 | 高吞吐量應用 |
| **Kimi K2.5** | 32B | 1x H100 | ~$2,500 | Agent Swarm 應用 |
| **GLM-5** | 400B | 2x H100 | ~$5,000 | 推理密集任務 |

如果月流量超過 100M tokens，本地部署反而比 API 便宜。對企業來說，這是分水嶺。

* * *

## 應用場景選型矩陣

| 應用場景 | 首選 | 次選 | 理由 |
| --- | --- | --- | --- |
| **Agent 自動化（複雜）** | Kimi K2.5 | GLM-5 | Agent Swarm 原生並行 |
| **Agent 自動化（簡單高量）** | MiniMax M2.5 | Qwen3.5 | Tool Calling 精準 + 速度快 |
| **編程 \+ 代碼審查** | GLM-5 | Qwen3.5-Coder | HumanEval 92.8% 最高 |
| **長文檔 RAG** | Qwen3.5 | Kimi K2.5 | 成本最低 \+ 256K context |
| **多模態（圖片/影片）** | Kimi K2.5 | — | 唯一原生視頻理解 |
| **極限成本優化** | MiniMax M2.5 | Qwen3.5 | 輸入 $0.15/M |
| **推理能力要求高** | GLM-5 | Kimi K2.5 | Intelligence Index 50+ |
| **本地部署（數據主權）** | Qwen3.5 | GLM-5 | MIT 開源 + 硬體需求低 |

* * *

## 我在 OpenClaw 上的實戰結果

前面都是 Benchmark 數字，這裡是真實場景。我把龍蝦從 Opus 4.6 改成了 Kimi K2.5，跑了幾天。

| 維度 | Opus 4.6 | Kimi K2.5 | 差異 |
| --- | --- | --- | --- |
| 中文理解 | 頂級 | 頂級 | 無差異 |
| 指令精準度 | 頂級 | 接近頂級 | 偶爾漏掉邊界 case |
| 任務完成度 | 95% | 93% | -2%（可接受） |
| 回應速度 | 中等 | 快 | +30% |
| 成本 | 1x | 0.2x | **省 80%** |

**場景 1：50 頁 PDF 結構提取**
Opus 完美無誤，$2.50。Kimi 正確率 97%，$0.25。 **省 10 倍成本。**

**場景 2：500 行 Python 代碼審查**
Opus 找出 8 個問題。Kimi 找出 7 個，漏掉 1 個邊界 case，不影響生產。

**場景 3：複雜商業邏輯系統設計**
Opus 提出 5 個視角。Kimi 提出 4 個，遺漏 1 個。95% 滿足，但不是 100%。

**結論：省 80% 成本換掉 2-3% 的完美度，對 Agent 應用來說是超划算的交易。**

* * *

## 坦白說：選型的三個陷阱

### 陷阱 1：被 Benchmark 蒙騙

GLM-5 Intelligence Index 50.2 和 Claude Opus 50.0， **數字差 0.2，但成本差 17 倍**。別被排名迷惑，看的是應用場景，不是排名。

### 陷阱 2：過度追求「完美」

如果你追求 99.99% 的完美率，別看開源模型。但如果 95-98% 足夠（大多數場景都是），開源模型省下的成本能讓你多試 100 個新 idea。

### 陷阱 3：忽視部署自由度

Qwen3.5 和 GLM-5 都是 MIT 開源。 **部署在自己的伺服器上** = 數據主權 \+ 永遠不怕被廠商漲價。這對企業來說，價值可能超過模型本身的聰明程度。

* * *

## 結語

2026 農曆新年，中國開源大模型集體踏入「成熟期」。

Kimi K2.5、Qwen3.5、GLM-5、MiniMax M2.5 不是競爭關係，而是 **選型關係**。它們分別在不同維度達到頂級：

- **Kimi**：Agent 和多模態
- **Qwen**：成本和部署自由度
- **GLM**：推理能力和中文理解
- **MiniMax**：速度和工具調用

背後的真相是： **參數時代已經過去，MoE（混合專家）時代已經來臨。** 不再拼「總參數」，而是拼「激活效率」和「應用適配度」。

我目前的配置是： **核心 Agent 應用用 Kimi K2.5，高吞吐量任務用 MiniMax M2.5，編程用 GLM-5，成本敏感的企業應用用 Qwen3.5。**

不是備用方案，這就是主力方案。

* * *

## 參考資料

### Kimi K2.5

1. [One Hundred Agents, One Command - Kimi K2.5 Automation](https://medium.com/@cognidownunder/one-hundred-agents-one-command-kimi-k2-5-just-rewrote-the-rules-of-automation-0e9db50bc694)
2. [MoonshotAI/Kimi-K2.5 - GitHub](https://github.com/MoonshotAI/Kimi-K2.5)
3. [Kimi K2.5 Tech Blog - Moonshot AI](https://www.kimi.com/blog/kimi-k2-5.html)
4. [Kimi K2.5 API Quickstart](https://platform.moonshot.ai/docs/guide/kimi-k2-5-quickstart)

### Qwen3.5

1. [通義千問 Qwen3.5 - 阿里巴巴官方](https://www.aliyun.com/product/qwen3)
2. [Qwen3.5 技術報告](https://arxiv.org/abs/2402.xxxx)

### GLM-5

1. [GLM-5 Intelligence Index - 智譜 AI](https://www.zhipu.ai/glm-5)
2. [GLM-5 開源發布 - Hugging Face](https://huggingface.co/THUDM/GLM-5)

### MiniMax

1. [MiniMax M2.5 - MiniMax 官方](https://www.minimaxi.com/models/m2.5)
2. [τ-Bench: Tool Calling Benchmark](https://github.com/minimaxi/tau-bench)

### 綜合對比

1. [大模型 Benchmark 對比 - Artificial Analysis](https://artificialanalysis.ai/models)
2. [中國開源模型春節檔發布總結 \- 知乎專欄](https://zhuanlan.zhihu.com/)
3. [開源 LLM 成本分析報告 - AI Commons](https://aicommons.org/llm-costs-2026)

### OpenClaw 相關

1. [Peter Steinberger OpenClaw 推特推薦](https://x.com/steipete/status/2016260885782622626)
2. [OpenClaw + Kimi K2.5 最佳配置 - APIYi](https://help.apiyi.com/zh-hant/openclaw-kimi-k-2-5)

### 来源 4: 2026 AI编程能力评测：八大模型全面对比 - U深搜

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

### 来源 5: https://www.arxiv.org/pdf/2604.08064

- URL: https://www.arxiv.org/pdf/2604.08064
- 精读方法：jina-readerlm-academic

```markdown
The provided draft Markdown does not match the content of the original HTML, which only contains a head tag with no actual body content. Therefore, there is nothing to extract or refine further into Markdown beyond the title "Your Title" if one were present.
```

### 来源 6: 2026年全网最全大模型API横评：Claude / GPT / Gemini 等8 大厂商 ...

- URL: https://segmentfault.com/a/1190000047676047
- 精读方法：firecrawl-scrape

# [2026年全网最全大模型API横评：Claude / GPT / Gemini 等8 大厂商 20+ 主流模型](https://segmentfault.com/a/1190000047676047)

[![头像](https://avatar-static.segmentfault.com/424/154/4241544123-69a295188caae_huge128)\\
\\
**七牛云行业应用**](https://segmentfault.com/u/shenyongweiwudedahai_ay15n) [3 月 25 日上海](https://segmentfault.com/a/1190000047676047/revision)

阅读 6 分钟

0 [评论](https://segmentfault.com/a/1190000047676047#comment-area)

大模型 API 横评是开发者选型的核心参考。本文覆盖 8 大厂商 20+ 主流模型，从 **价格、上下文窗口、推理能力、编程性能、中文质量、响应速度** 六个维度全面对比，所有数据来自官方文档（截至 2026 年 3 月）。无论你是做 Agent 开发、RAG 系统还是日常代码辅助，读完这篇可以直接做出选型决策。

![](https://segmentfault.com/img/bVdocSC)

* * *

## 一、价格总览：各模型每百万 Token 费用对比

价格是 API 选型第一要素。以下为各厂商旗舰模型和经济型模型的官方定价（2026 年 3 月，单位：美元 / 百万 Token）：

### 国际模型

| 模型 | API ID | 输入价格 | 输出价格 | 上下文窗口 |
| --- | --- | --- | --- | --- |
| Claude Opus 4.6 | `claude-opus-4-6` | $5.00 | $25.00 | 1M tokens |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | $3.00 | $15.00 | 1M tokens |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | $1.00 | $5.00 | 200k tokens |
| GPT-4o | `gpt-4o` | $2.50 | $10.00 | 128k tokens |
| GPT-4.1 | `gpt-4.1` | $2.00 | $8.00 | 1M tokens |
| GPT-4.1 mini | `gpt-4.1-mini` | $0.40 | $1.60 | 1M tokens |
| o3 | `o3` | $10.00 | $40.00 | 200k tokens |
| o4-mini | `o4-mini` | $1.10 | $4.40 | 200k tokens |
| Gemini 2.5 Pro | `gemini-2.5-pro` | $1.25 | $10.00 | 1M tokens |
| Gemini 2.5 Flash | `gemini-2.5-flash` | $0.30 | $2.50 | 1M tokens |
| Gemini 2.5 Flash-Lite | `gemini-2.5-flash-lite` | $0.10 | $0.40 | 1M tokens |

> GPT-4.1 / GPT-4.1 mini 价格来自 OpenAI 官方文档，o3/o4-mini 为推理模型，按思考 token 计费，实际成本受任务复杂度影响。

### 国内模型

| 模型 | API ID | 输入价格 | 输出价格 | 上下文窗口 |
| --- | --- | --- | --- | --- |
| DeepSeek-V3.2 | `deepseek-chat` | $0.28（无缓存）/ $0.028（缓存命中） | $0.42 | 128k tokens |
| DeepSeek-R1（推理） | `deepseek-reasoner` | $0.28（无缓存）/ $0.028（缓存命中） | $0.42 | 128k tokens |
| Qwen3-Max | `qwen3-max` | $0.36–$1.00 | $1.43–$4.01 | 262k tokens |
| Qwen3.5-Plus | `qwen3.5-plus` | $0.12–$0.57 | $0.69–$3.44 | 1M tokens |
| Qwen-Flash | `qwen-flash` | $0.05–$0.25 | $0.40–$2.00 | 1M tokens |
| Kimi K2.5 | `kimi-k2.5` | \[价格待核实：请查阅 platform.moonshot.cn\] | — | 256k tokens |
| MiniMax M2.7 | `minimax-m2.7` | \[价格待核实：请查阅 platform.minimaxi.com\] | — | \[待核实\] |
| GLM-4-Flash | `glm-4-flash` | \[价格待核实：请查阅 open.bigmodel.cn\] | — | 128k tokens |

> DeepSeek 价格来自官方 API 文档（2026年3月），Qwen 价格为国际版 Global 区报价，国内版略有差异。

* * *

## 二、旗舰模型能力横评

### 2.1 编程 / Agent 能力

**代码生成是当前大模型能力分化最明显的维度。**

| 模型 | SWE-bench 得分 | 特色 |
| --- | --- | --- |
| Claude Opus 4.6 | 72.5%（Anthropic 官方，2025年） | Agent 编程行业领先，支持 Computer Use |
| Claude Sonnet 4.6 | 72.7%（Anthropic 官方，2025年） | 性价比旗舰，速度快于 Opus |
| GPT-4.1 | \[数据待核实：建议引用 OpenAI 官方评测\] | 支持 1M 上下文，代码理解增强 |
| DeepSeek-V3.2 | \[数据待核实：建议引用 DeepSeek 官方报告\] | 国内开发者首选，FIM 补全支持 |
| Kimi K2.5 | \[数据待核实\] | 主打 Agentic Coding，支持 thinking 模式 |

> SWE-bench 是业界主流的代码能力评测基准，测试模型在真实 GitHub issue 上的修复成功率。

### 2.2 推理 / 数学能力

各厂商的"推理专用模型"对比：

| 模型 | 推理方式 | 适用场景 |
| --- | --- | --- |
| Claude Opus/Sonnet 4.6 | Extended Thinking（可配置 budget\_tokens） | 数学证明、逻辑推断、多步规划 |
| o3 | 原生 Chain-of-Thought，按思考 token 计费 | 竞赛数学、复杂推理 |
| o4-mini | 轻量推理，成本低于 o3 80% | 日常推理任务 |
| DeepSeek-R1（deepseek-reasoner） | Thinking Mode，最大输出 64k | 学术推理、代码调试 |
| Kimi K2 Thinking | 思维链推理模式 | Agent 场景通用推理 |
| Qwen3-Max | 内置混合推理模式 | 中文技术文档、代码 |

### 2.3 长上下文处理

上下文窗口大小直接决定能处理多长的文档或代码库：

| 等级 | 模型 | 窗口大小 |
| --- | --- | --- |
| 超长（≥1M） | Claude Opus/Sonnet 4.6、GPT-4.1/4.1-mini、Gemini 2.5 Pro/Flash、Qwen3.5-Plus/Qwen-Flash | 1M tokens |
| 长（256k–512k） | Kimi K2.5、Kimi K2-Thinking | 256k tokens |
| 中（128k–262k） | DeepSeek-V3.2/R1、GPT-4o、Qwen3-Max、GLM-4-Flash | 128k–262k tokens |

> **实际建议**：1M 上下文适合整个代码仓库分析；256k 适合长文档问答；128k 满足绝大多数对话场景。

* * *

## 三、价格-性能比分析

![](https://segmentfault.com/img/bVdocSD)

### 极致性价比区（输出 $0.40–$2.50 / MTok）

- **Gemini 2.5 Flash-Lite**（$0.10/$0.40）：最便宜的 1M 上下文模型，适合高并发轻量场景
- **Gemini 2.5 Flash**（$0.30/$2.50）：速度最快之一，1M 窗口，批量处理首选
- **DeepSeek-V3.2**（$0.28/$1.12）：缓存命中后仅 $0.028 输入，国内调用稳定，FIM 补全支持
- **Qwen-Flash**（$0.05–$0.25/$0.40–$2.00）：阿里云生态首选，1M 上下文，中文质量优秀

### 均衡旗舰区（输出 $5–$15 / MTok）

- **Claude Sonnet 4.6**（$3/$15）：SWE-bench 72.7%，1M 上下文，当前综合能力最强的均衡模型之一
- **Gemini 2.5 Pro**（$1.25/$10）：Google 旗舰，多模态能力强，原生工具调用
- **GPT-4.1**（$2/$8）：1M 上下文，代码和指令遵循增强版，比 GPT-4o 便宜

### 顶级旗舰区（输出 $25–$40 / MTok）

- **Claude Opus 4.6**（$5/$25）：Agent 编程和 Computer Use 场景的当前最优模型，128k 最大输出
- **o3**（$10/$40）：推理任务天花板，适合竞赛数学和高难度分析，成本高昂

* * *

## 四、各场景选型建议

| 场景 | 推荐模型 | 理由 |
| --- | --- | --- |
| Agent / 自主编程 | Claude Opus 4.6 / Sonnet 4.6 | SWE-bench 领先，支持 Computer Use |
| 生产环境高并发 | Gemini 2.5 Flash / DeepSeek-V3.2 | 速度快、成本低 |
| 复杂数学推理 | o3 / DeepSeek-R1 | 原生推理链，准确率更高 |
| 超长文档处理 | Claude Sonnet 4.6 / Gemini 2.5 Pro | 1M 窗口，长上下文质量稳定 |
| 国内部署，中文优先 | Qwen3-Max / Kimi K2.5 / DeepSeek-V3.2 | 低延迟接入，中文训练数据充足 |
| 多模态（图像/视频） | Gemini 2.5 Pro / GPT-4o / Kimi K2.5 | 原生多模态架构 |
| 极致成本控制 | Gemini 2.5 Flash-Lite / Qwen-Flash | 输入 $0.05–$0.10，1M 窗口 |
| 角色扮演 / 创意写作 | MiniMax M2-Her / Kimi K2.5 | 专项训练，多轮角色场景 |

* * *

## 五、各家 API 接入方式对比

```
# Claude (Anthropic SDK)
import anthropic
client = anthropic.Anthropic(api_key="YOUR_KEY")
resp = client.messages.create(model="claude-opus-4-6", max_tokens=1024, messages=[...])

# GPT (OpenAI SDK)
from openai import OpenAI
client = OpenAI(api_key="YOUR_KEY")
resp = client.chat.completions.create(model="gpt-4.1", messages=[...])

# DeepSeek (兼容 OpenAI SDK)
client = OpenAI(api_key="YOUR_KEY", base_url="https://api.deepseek.com")
resp = client.chat.completions.create(model="deepseek-chat", messages=[...])

# Qwen (兼容 OpenAI SDK)
client = OpenAI(api_key="YOUR_KEY", base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1")
resp = client.chat.completions.create(model="qwen3-max", messages=[...])

# Kimi (兼容 OpenAI SDK)
client = OpenAI(api_key="YOUR_KEY", base_url="https://api.moonshot.cn/v1")
resp = client.chat.completions.create(model="kimi-k2.5", messages=[...])

# GLM (兼容 OpenAI SDK)
client = OpenAI(api_key="YOUR_KEY", base_url="https://open.bigmodel.cn/api/paas/v4/")
resp = client.chat.completions.create(model="glm-4-flash", messages=[...])
```

**关键结论：DeepSeek、Qwen、Kimi、GLM 均兼容 OpenAI SDK，只需替换 `base_url` 和 `api_key`，迁移成本极低。**

对于需要同时管理多个模型 API Key 的开发场景，可以通过统一推理网关接入，例如七牛云 AI 大模型推理服务兼容 OpenAI/Anthropic 双标准，支持 Claude、DeepSeek、Gemini 等主流模型，切换模型无需修改调用代码。

* * *

## 六、中文能力专项

中文任务性能是国内开发者的核心关切：

| 模型 | 中文训练数据 | 中文推荐场景 |
| --- | --- | --- |
| Qwen3-Max / Qwen3.5-Plus | 阿里云，中文语料丰富 | 中文文档生成、客服、RAG |
| DeepSeek-V3.2 | 国内数据集，中文指令遵循强 | 中文代码注释、技术翻译 |
| Kimi K2.5 | Moonshot，中文长文本优化 | 长文摘要、合同分析 |
| GLM-4-Flash | 清华，中文学术场景 | 知识问答、学术写作辅助 |
| Claude Sonnet 4.6 | 多语言训练，中文质量上升 | 中英文混合任务 |

* * *

## 常见问题

**Q：DeepSeek API 和 Claude API 哪个更适合做 Agent？**

Claude Opus/Sonnet 4.6 在 SWE-bench（72.5%/72.7%）上领先，原生支持 Computer Use 和 Extended Thinking，是当前 Agent 场景的首选。DeepSeek 性价比更高，成本约为 Claude 的 1/10，适合预算有限或高并发 Agent 流水线。两者并不互斥：可以用 DeepSeek 做初步筛选，再用 Claude 处理复杂子任务。

**Q：Gemini 2.5 Flash 和 Claude Haiku 4.5 哪个更划算？**

价格上 Gemini 2.5 Flash 更低（$0.30/$2.50 vs $1.00/$5.00），且同样支持 1M 上下文。Claude Haiku 4.5 上下文窗口为 200k，但在中文任务和指令遵循方面口碑更稳定。实际建议：做 benchmark 跑自己的用例后再决策。

**Q：o3 值得用吗？价格这么高。**

o3（$10/$40 每百万 token）适合有明确的高精度推理需求场景：竞赛数学、代码安全审计、复杂法律分析。日常编程和文本任务用 Claude Sonnet 4.6 或 GPT-4.1 成本低 80% 以上，且实际输出质量差距不显著。

**Q：国内访问哪个模型最稳定？**

DeepSeek（api.deepseek.com）、Qwen（dashscope.aliyuncs.com）、Kimi（api.moonshot.cn）、GLM（open.bigmodel.cn）均提供国内节点，无需代理。Claude 和 GPT 官方 API 需要境外网络，可通过兼容层代理访问。

**Q：如何快速测试多个模型对同一 prompt 的输出质量？**

将 OpenAI SDK 的 `base_url` 配置为多模型推理网关，用相同代码切换 `model` 参数即可对比，无需为每家分别写 SDK 调用逻辑。

* * *

## 总结

![](https://segmentfault.com/img/bVdocSE)

**2026 年大模型 API 格局已高度分化：**

- **能力天花板**：Claude Opus 4.6 和 o3 分别在 Agent 编程和数学推理上领先，但成本高昂
- **均衡旗舰**：Claude Sonnet 4.6、Gemini 2.5 Pro、GPT-4.1 是性价比最高的旗舰选择
- **成本最优**：DeepSeek-V3.2 和 Gemini 2.5 Flash/Flash-Lite 提供最低成本，适合高并发生产环境
- **国内首选**：Qwen3-Max / DeepSeek-V3.2 / Kimi K2.5 兼顾中文质量与访问稳定性

根据 Anthropic、OpenAI、Google、DeepSeek、阿里云官方文档（2026年3月），本文所有价格和参数以官方实时定价为准，建议在正式采购前再次核实最新报价。

**延伸资源：**

- 多模型对比体验： [https://www.qiniu.com/ai/models](https://link.segmentfault.com/?enc=uETebH8bK29V0lbPCOREgA%3D%3D.yoJfLGpvJRF7vcEdn%2BqlBomoYjPhngKTZHUZO%2FrMua4%3D)
- Anthropic 模型文档： [https://platform.claude.com/docs/en/about-claude/models/overview](https://link.segmentfault.com/?enc=%2B6KU2qquvo6B35iL7hi%2FdQ%3D%3D.xRC3mNoJO2SebZVlmQzxxzaIR%2BQR40rFqM7rUYXRnwpzPEWSFBsTrE3iCtiqBCx05I36ky%2FrGWbvMcIPEb2rMVPn%2BmDeS%2Bv7zHwKlsCGI%2Fg%3D)
- DeepSeek API 文档： [https://api-docs.deepseek.com](https://link.segmentfault.com/?enc=p2KsU1eP7uCEnNBnBrAbZw%3D%3D.DImbLsu259D9vvNQ%2FoPABuRFQg4T%2FJ0cstQuhpoUB7E%3D)
- Gemini 定价页： [https://ai.google.dev/gemini-api/docs/pricing](https://link.segmentfault.com/?enc=tLJCTCvLp3hvfy2IBRRm7w%3D%3D.B1pFjdHLXPXJxV8R5Lf3IdBC1LZNQW8%2FSc%2BRYZ2v0lAPzZSnLV5cSF2FOJ2je%2BnQ)

* * *

_本文数据截至 2026 年 3 月，大模型价格变动频繁，建议每季度核对官方最新定价后再做预算规划。_

[人工智能](https://segmentfault.com/t/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD) [llm](https://segmentfault.com/t/llm) [openai](https://segmentfault.com/t/openai) [chatgpt](https://segmentfault.com/t/chatgpt) [claude](https://segmentfault.com/t/claude)

赞收藏

分享

阅读 22.1k [发布于 3 月 25 日](https://segmentfault.com/a/1190000047676047/revision)

举报

* * *

[![头像](https://avatar-static.segmentfault.com/424/154/4241544123-69a295188caae_huge128)](https://segmentfault.com/u/shenyongweiwudedahai_ay15n)

[**七牛云行业应用**](https://segmentfault.com/u/shenyongweiwudedahai_ay15n)

10 声望8 粉丝

关注作者

* * *

« 上一篇

[Claude Code 常见问题解决手册：安装、认证、网络与性能全覆盖（2026年）](https://segmentfault.com/a/1190000047676028)

下一篇 »

[最适配 OpenClaw 的大模型 API 是哪个？四款模型实测对比与选型指南（2026）](https://segmentfault.com/a/1190000047676077)

[一、价格总览：各模型每百万 Token 费用对比](https://segmentfault.com/a/1190000047676047#item-1) [国际模型](https://segmentfault.com/a/1190000047676047#item-1-1) [国内模型](https://segmentfault.com/a/1190000047676047#item-1-2) [二、旗舰模型能力横评](https://segmentfault.com/a/1190000047676047#item-2) [2.1 编程 / Agent 能力](https://segmentfault.com/a/1190000047676047#item-2-3) [2.2 推理 / 数学能力](https://segmentfault.com/a/1190000047676047#item-2-4) [2.3 长上下文处理](https://segmentfault.com/a/1190000047676047#item-2-5) [三、价格-性能比分析](https://segmentfault.com/a/1190000047676047#item-3) [极致性价比区（输出 $0.40–$2.50 / MTok）](https://segmentfault.com/a/1190000047676047#item-3-6) [均衡旗舰区（输出 $5–$15 / MTok）](https://segmentfault.com/a/1190000047676047#item-3-7) [顶级旗舰区（输出 $25–$40 / MTok）](https://segmentfault.com/a/1190000047676047#item-3-8) [四、各场景选型建议](https://segmentfault.com/a/1190000047676047#item-4) [五、各家 API 接入方式对比](https://segmentfault.com/a/1190000047676047#item-5) [六、中文能力专项](https://segmentfault.com/a/1190000047676047#item-6) [常见问题](https://segmentfault.com/a/1190000047676047#item-7) [总结](https://segmentfault.com/a/1190000047676047#item-8)

▲

### 引用和评论

**推荐阅读**

[![头像](https://avatar-static.segmentfault.com/424/154/4241544123-69a295188caae_big64)\\
\\
**Codex 最新更新：支持接入第三方模型，配置一次全端生效** \\
\\
七牛云行业应用](https://segmentfault.com/a/1190000047876848?utm_source=sf-similar-article) [![头像](https://image-static.segmentfault.com/317/931/3179314346-5f61e47221e07)\\
\\
**给 DeepSeek 写了个专属 Agent 框架 Reasonix：85% 缓存命中率是怎么做出来的** \\
\\
谦逊的钥匙\_oQUBJ赞 5阅读 9.1k评论 1](https://segmentfault.com/a/1190000047722418?utm_source=sf-similar-article) [![头像](https://avatar-static.segmentfault.com/291/139/2911397043-69cde2d7cdd60_big64)\\
\\
**AI Agent中6种常用的设计模式** \\
\\
苏三说技术赞 1阅读 5.2k](https://segmentfault.com/a/1190000047703425?utm_source=sf-similar-article) [![头像](https://avatar-static.segmentfault.com/205/718/2057180355-69cdfa184ed1e_big64)\\
\\
**OpenAI vs Anthropic vs Google：2026年AI大模型竞争格局** \\
\\
ViVaAPI赞 1阅读 14.6k](https://segmentfault.com/a/1190000047691901?utm_source=sf-similar-article) [![头像](https://avatar-static.segmentfault.com/424/154/4241544123-69a295188caae_big64)\\
\\
**Codex CLI 国内使用完整教程：从安装到第一个任务（2026 最新版）** \\
\\
七牛云行业应用赞 1阅读 11.7k](https://segmentfault.com/a/1190000047776553?utm_source=sf-similar-article) [![头像](https://avatar-static.segmentfault.com/526/152/52615256-649946e860b48_big64)\\
\\
**OpenAI Codex 安装与使用全指南：API Key 获取与自定义 API 配置与实战排错** \\
\\
uiuihaoAICG阅读 19.9k](https://segmentfault.com/a/1190000047687741?utm_source=sf-similar-article) [![头像](https://avatar-static.segmentfault.com/279/029/2790295347-5c7f8d6242978_big64)\\
\\
**从 OpenClaw 看 Agent 架构设计** \\
\\
vivo互联网技术赞 1阅读 1.8k](https://segmentfault.com/a/1190000047702119?utm_source=sf-similar-article)

**0 条评论**

[得票](https://segmentfault.com/a/1190000047676047?sort=votes) [最新](https://segmentfault.com/a/1190000047676047?sort=newest)

![头像](https://image-static.segmentfault.com/317/931/3179314346-5f61e47221e07)

提交评论

评论支持部分 Markdown 语法：``**粗体** _斜体_ [链接](http://example.com) `代码` - 列表 > 引用``。你还可以使用 `@`来通知其他用户。

![preview](https://segmentfault.com/a/1190000047676047)

![preview](https://segmentfault.com/a/1190000047676047)

### 来源 7: 大模型代码编程能力评测排行榜

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

### 来源 8: OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation

- URL: https://arxiv.org/pdf/2604.10866
- 精读方法：jina-readerlm-academic

```markdown
The provided draft Markdown does not match the content of the original HTML, which only contains a head tag with no actual body content. Therefore, there is nothing to extract or refine further into Markdown beyond the title "Your Title" if one were present.
```

### 来源 9: Qwen3-Coder-Next Technical Report

- URL: https://www.arxiv.org/pdf/2603.00729
- 精读方法：jina-readerlm-academic

```markdown
The provided draft Markdown does not match the content of the original HTML, which only contains a head tag with no actual body content. Therefore, there is nothing to extract or refine further into Markdown beyond the title "Your Title" if one were present.
```

### 来源 10: 2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云

- URL: https://cloud.tencent.com/developer/article/2670420
- 精读方法：firecrawl-scrape

[测试开发技术](https://cloud.tencent.com/developer/user/6490225)

## 2026 年 AI 编程实测：6 款顶流大模型对比，效率直接翻倍！

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

测试开发技术

[社区首页](https://cloud.tencent.com/developer) > [专栏](https://cloud.tencent.com/developer/column) >2026 年 AI 编程实测：6 款顶流大模型对比，效率直接翻倍！

# 2026 年 AI 编程实测：6 款顶流大模型对比，效率直接翻倍！

发布于 2026-05-18 07:34:39

发布于 2026-05-18 07:34:39

5.8K0

举报

文章被收录于专栏：[测试开发技术](https://cloud.tencent.com/developer/column/82746)测试开发技术

![](https://developer.qcloudimg.com/http-save/yehe-6490225/6f8555dbaf0e57caa6227cb765f7d5ca.png)

说实话，2026年的AI编程工具市场，已经卷到让人眼花缭乱。

AI 编程几乎可以说，已进入到了 **全民生产时代**，长上下文、代码工程、 [Agent](https://cloud.tencent.com/developer/techpedia/2493?from_column=20065&from=20065) 自动化、多模态理解全面成熟。每隔几周就有新模型发布，每家都宣称自己是"最强编程模型"。

作为一个每天和代码打交道的知识博主，我深知 **选对工具比追新更重要**。

今天这篇文章，结合自身实测以及 SWE‑bench、LiveCodeBench、ARC‑AGI‑2 等权威榜单相结合，给大家盘一盘程序员最常用的6款AI大模型，以及我的使用建议。

> 本文的对比数据，截止 2026 年 5 月份

### **一、2026年AI编程：神仙打架进入白热化**

先花30秒看懂当前格局。

2026年4-5月，AI大模型行业迎来了 **史上最密集的升级周期**。OpenAI、Anthropic、Google、DeepSeek四大阵营集中发布旗舰模型，百万Token上下文、代码能力、多模态效果全面突破。

- • 国际模型： **Claude 4.7、GPT‑5.5、Gemini 3.1 Pro** 稳坐第一梯队，百万上下文已成标配。
- • 国产模型： **GLM‑5.1、kimi 2.6、DeepSeek V4** 全面逼近甚至超越国际一线，性价比与中文体验碾压级优势。

**核心变化**：不再是 “能不能写代码”，而是 **复杂工程重构、推理深度、工程化落地、超长上下文理解、端到端 Agent 自动化**。

2026 AI 编程模型总览

🌍 国际大模型

🇨🇳 国产大模型

🤖 GPT-5.5 Agent全能战士

👑 Claude Opus 4.7 编程新王

🧠 Gemini 3.1 Pro 推理最强音

💼 Claude Sonnet 4.6 主力均衡

⚡ DeepSeek V4 性价比之王

🔥 GLM-5.1 国模编程标杆

⭐ Qwen3.6-Plus 阿里代码旗舰

🌙 Kimi K2.6 开源多面手

### **二、Claude Opus 4.7 ：编程天花板，登顶全球榜首**

2026 年 4 月 16 日，Anthropic 发布的 Claude Opus 4.7，直接把 AI 编程的 “天花板” 又拉高了一个档次：在全球 AI 模型综合排名中以 1503 分登顶，编程专项评测成绩更是刷新行业纪录。

![](https://developer.qcloudimg.com/http-save/yehe-6490225/06b56e4f628167f5298b96a16bde8f5f.jpg)

Opus 4.7 支持 100 万 Token 上下文窗口 —— 这是什么概念？大约相当于 750 万个英文单词，或是一整套《哈利・波特》系列的 7 倍，意味着你可以直接把一整个代码库丢给它，让它分析跨模块的逻辑漏洞、重构架构，不用再分批次拆解需求。

在 LMArena Coding Arena 盲测中，Claude Opus 4.7 (Thinking) 以 1350 分稳居第一，远超其他竞品。

这次更新聚焦 [**智能体**](https://cloud.tencent.com/developer/techpedia/2547?from_column=20065&from=20065) **编排（Agentic orchestration）**：

- • 接近Opus级别的性能，成本更低
- • 代码质量进一步提升，修复了之前的推理和缓存问题
- • 支持本地应用自主操控，具备代理化编程与高精视觉解析能力

不过，Opus 4.7的价格依然是目前最贵的，1百万Token的输入、输出价格分别是 **5美元、25美元**。但作为编程能力天花板，贵得有道理。如果追求极致代码质量且预算充足，Claude Opus 4.7是目前首选。

**我的建议**：复杂架构设计、跨模块调试、长上下文分析用Opus 4.7；日常编码、简单任务用Sonnet 4.6 或用国产大模型即可。

### **三、GPT-5.5：OpenAI的"Agent全能战士"**

就在 Claude 升级一周后，OpenAI 在 4 月 24 日发布了 GPT-5.5（代号 Spud），它的野心根本不是 “写代码”，而是 “替你完成整个工作流”。

![](https://developer.qcloudimg.com/http-save/yehe-6490225/08c43bcd5c444a3f0b668072b8ae2127.jpg)

**核心改进：从 “写代码” 到 “做任务”**

- • **电脑操控能力**：OSWorld‑Verified 成功率 75%，超人类平均水平 —— 我实测过让它操作 VS Code 调试代码、用 Postman 调用接口、甚至用 Excel 处理数据，它能精准操控鼠标 / 键盘 / 软件，完成从 “写代码” 到 “验证代码效果” 的全流程，这是目前其他模型无法匹敌的。
- • **SWE‑bench Verified 得分 88.7%**：短任务与快速修复能力堪称第一，比如线上 bug 紧急修复，它能在几分钟内定位问题、写出修复代码，甚至给出测试用例。
- • **效率提升**：100 万 Token 上下文 + Codex 加速，生成速度提升 1.5 倍，延迟却没增加，写代码时的 “等待感” 大幅降低。

**我的建议**：OpenAI 的核心优势从来不是 “聊天”，而是 “把 AI 融入工作流的能力”。如果你需要AI不仅能写代码，还能操作软件完成完整任务，GPT-5.5是目前最强选择，当然它的价格也是死贵死贵的。 —— 但个人开发者没必要盲目追，除非你的工作高度依赖 “代码 + 软件操作” 的全流程自动化。

### **四、Gemini 3.1 Pro：推理之王**

谷歌的 Gemini 系列一直主打 “推理”，3.1 Pro 版本更是把这个优势发挥到了极致：在评估全新逻辑模式处理能力的 ARC-AGI-2 基准测试中，它取得 77.1% 的实测得分，是上一代的两倍多。

**核心亮点：推理 \+ 多模态**

- • **逻辑推理无敌**：我用它做过数学建模、算法优化、复杂业务逻辑推导（比如电商订单的分账规则），它能清晰拆解逻辑链，写出的代码几乎没有 “逻辑漏洞”—— 这是很多模型的短板，比如有的模型能写代码，但逻辑绕来绕去，实际运行就出问题。
- • **多模态能力顶尖**：支持文 \+ 图 \+ 音 \+ 视频输入，我曾把一张手绘的架构图丢给它，它能精准理解架构逻辑，生成对应的代码框架；做前端可视化时，它生成的 SVG 动画、交互效果，比其他模型更贴合设计意图，幻觉率也大幅降低。
- • **性价比尚可**：在国际主流模型中，Gemini 3.1 Pro 的价格算是中等，比 Claude 和 GPT 便宜不少，适合有推理需求的场景。

**我的建议**：如果你做的是算法、科研、多模态编程，需要模型进行深度逻辑推理和多模态分析，选它准没错；但如果是纯业务代码开发，它的优势就没那么明显了。

### **五、DeepSeek V4：国产开源的性价比之王**

2026 年 4 月 24 日发布的 DeepSeek V4，是国产大模型对国际阵营的 “强力反击”—— 它用 1% 的成本，实现了顶级模型 90% 的能力，堪称 “行业价格屠夫”。

**核心升级：性能追平，成本腰斩**

- • **架构革命**：1.6 万亿总参数 + 混合注意力栈，既能处理超长上下文，又能控制成本，100 万 Token 全量支持，分析大型代码库毫无压力。
- • **SWE‑bench Verified 得分 80.6%**：在开源 / 开放权重模型中排名顶级，我实测写后端接口、前端组件，它的代码质量和 Claude Sonnet 4.6 几乎持平，甚至中文注释更贴合国内开发者的习惯。

而DeepSeek V4 API价格堪称"行业屠夫"：

| 版本 | 输入价格（缓存命中） | 输出价格 | 备注 |
| --- | --- | --- | --- |
| V4 Flash | $0.0028/MT | $0.28/MT | 日常首选 |
| V4 Pro（5.31前2.5折） | $0.0036/MT | $0.87/MT | 限时优惠 |
| V4 Pro（恢复原价后） | $0.0145/MT | $3.48/MT | 仍极具竞争力 |

对比下来，DeepSeek V4 Pro 优惠价的成本仅为 Claude Sonnet 4.7 的 1/432，GPT-5.5 的 1/360—— 我近一个月的日常编码都用它，每月成本不到 50 元，效率却没降。 **接近顶流性能，但价格仅为零头，个人开发者首选。**

**我的建议**：DeepSeek V4 是我最推荐个人开发者和中小团队用的模型，它让我们看到国产模型的真正价值 —— 不是 “对标国际”，而是 “贴合本土需求”。唯一的小短板是极端复杂的架构设计稍逊于国际顶流，但日常场景完全够用，性价比直接拉满。如果预算敏感，DeepSeek V4是毫无疑问的首选。

### **六、GLM-5.1（智谱）：国模编程能力新标杆**

3 月 28 日，智谱发布 GLM-5.1，距离 5.0 仅一个多月，这次更新看似 “短平快”，却直接把国产模型的编程能力推到了新高度。

![](https://developer.qcloudimg.com/http-save/yehe-6490225/445a9d27f59c9db83b89718c3487b1d2.jpg)

**核心突破：从 “单点强” 到 “全栈能打”**

- • **SWE‑bench Pro 得分 58.4%**：正式超越 Claude Sonnet 4.5 Thinking，成为第一个通过全部测试工程的国产模型 —— 我用它做过一个完整的电商后端项目，从 [数据库](https://cloud.tencent.com/developer/techpedia/1471?from_column=20065&from=20065) 设计、接口开发到联调，它能全程支撑，不再像之前的国产模型那样 “前端行、后端拉胯”。
- • **中文体验拉满**：国内网络稳定、合规友好，对中文需求的理解精准度远超国际模型 —— 比如 “根据中文业务需求写带注释的代码”“适配国内支付接口”，它不用我反复解释，一次就能写对。
- • **稳定性提升**：超长上下文的幻觉问题明显改善，我曾丢给它 50 万行的中文代码库，它分析的逻辑问题准确率超过 90%，比 GLM-5.0 靠谱太多。

**我的建议**：GLM-5.1 是 “国产模型里的全能选手”，适合有一定复杂度的国内项目：比如政企类系统、中文业务场景的全栈开发。它的进步让我觉得，国产模型不再是 “凑数的”，而是能真正解决本土开发者痛点的 —— 网络稳、沟通成本低、适配国内生态，这些都是国际模型比不了的。如果你的项目主要面向国内市场，GLM-5.1 是比国际模型更优的选择。

> **国产编程首选，稳定、好用、不掉链。**

### **七、Kimi 2.6 : 开源多面手**

Kimi 2.6 是国产开源模型里的 “宝藏选手”，虽然在跑分上不如 DeepSeek V4 和 GLM-5.1 亮眼，但胜在 “灵活、可定制”。

且支持 **200万Token** 上下文窗口，是目前公开模型中最长的。

它的核心优势在于开源生态完善：开发者可以基于它的基座模型，根据自己的业务场景做微调 。此外，Kimi 2.6 对中文长文本的理解能力不错，写文档、注释、业务逻辑代码都很顺手，价格也足够亲民。

**我的建议**：如果你需要处理超长的中文文档，或者需要在本地部署AI模型，Kimi 2.6是目前最优选择之一。

### **写在最后**

2026年5月的AI编程战场，已经进入 **白刃战** 阶段。

Anthropic靠Opus 4.7登顶全球编程榜，OpenAI用GPT-5.5的Agent能力开辟新赛道，谷歌在推理上持续深耕，而国产模型则以 **极致性价比** 缩小差距——DeepSeek V4的SWE-bench达80.6%且成本极低，GLM-5.1成为复杂工况下的国产编程主力。

作为一名技术博主，我的感受是： **没有一款模型能通吃所有场景，灵活组合才是正解。**

是

极致编程质量

Agent全能/自动化

科学推理/多模态

否

是

是

否

否

开始选型

预算充足？

主要需求？

Claude Opus 4.7

GPT-5.5

Gemini 3.1 Pro

需要国产？

追求性价比？

DeepSeek V4

GLM-5.1

DeepSeek V4（国际也可用）

我现在的日常workflow：

- • 复杂架构、跨模块调试、安全敏感代码 → **Claude Opus 4.7**
- • 快速编码、简单函数、日常CRUD → **Claude Sonnet 4.6 / DeepSeek V4**
- • 需要操作软件、自动化流程 → **GPT-5.5**
- • 国内项目、中文场景 → **GLM 5.1 /Kimi 2.6 / DeepSeek V4**

**选对工具，编程效率可以翻倍；灵活组合，你才能不被时代甩下。**

本文参与 [腾讯云自媒体同步曝光计划](https://cloud.tencent.com/developer/support-plan)，分享自微信公众号。

原始发表：2026-05-12，如有侵权请联系 [cloudcommunity@tencent.com](mailto:cloudcommunity@tencent.com) 删除

[模型](https://cloud.tencent.com/developer/tag/17381)

[效率](https://cloud.tencent.com/developer/tag/17516)

[开源](https://cloud.tencent.com/developer/tag/10667)

[编程](https://cloud.tencent.com/developer/tag/17183)

[开发者](https://cloud.tencent.com/developer/tag/17341)

本文分享自 测试开发技术 微信公众号，前往查看

如有侵权，请联系 [cloudcommunity@tencent.com](mailto:cloudcommunity@tencent.com) 删除。

本文参与 [腾讯云自媒体同步曝光计划](https://cloud.tencent.com/developer/support-plan)  ，欢迎热爱写作的你一起参与！

[模型](https://cloud.tencent.com/developer/tag/17381)

[效率](https://cloud.tencent.com/developer/tag/17516)

[开源](https://cloud.tencent.com/developer/tag/10667)

[编程](https://cloud.tencent.com/developer/tag/17183)

[开发者](https://cloud.tencent.com/developer/tag/17341)

评论

登录后参与评论

0 条评论

热度

最新

登录 后参与评论

推荐阅读

目录

- 一、2026年AI编程：神仙打架进入白热化

- 二、Claude Opus 4.7 ：编程天花板，登顶全球榜首

- 三、GPT-5.5：OpenAI的"Agent全能战士"

- 四、Gemini 3.1 Pro：推理之王

- 五、DeepSeek V4：国产开源的性价比之王

- 六、GLM-5.1（智谱）：国模编程能力新标杆

- 七、Kimi 2.6 : 开源多面手

- 写在最后

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
