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

- 发现候选信源：39
- 精读信源数量：10
- 精读成功数量：9
- 精读失败数量：1

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
| exa | 1.00 | React-ing to Grace Hopper 200 Five Open-Weights Coding Models, One React Native App, One GH200, One Weekend or: why SWE-Bench rankings mispredicted which model actually shipped | https://arxiv.org/html/2604.17187 |
| exa | 1.00 | DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models | https://arxiv.org/html/2512.02556v1 |
| exa | 1.00 | CodegenBench: Can LLMs Write Efficient Code Across Architectures? | https://arxiv.org/html/2606.04023v1 |
| exa | 1.00 | Frontier Coding Agents Use Metaprogramming to Adapt to Unfamiliar Programming Languages | https://arxiv.org/html/2606.10933v1 |
| exa | 1.00 | Qwen3-Coder-Next Technical Report | https://arxiv.org/html/2603.00729v1 |
| exa | 1.00 | ProjDevBench: Benchmarking AI Coding Agents on End-to-End Project Development | https://www.arxiv.org/pdf/2602.01655 |
| exa | 1.00 | Consistency Amplifies: How Behavioral Variance Shapes Agent Accuracy | https://www.arxiv.org/pdf/2603.25764 |
| exa | 1.00 | GLM-5: from Vibe Coding to Agentic Engineering | https://arxiv.org/html/2602.15763v1 |
| exa | 1.00 | Qwen3 Technical Report | https://arxiv.org/html/2505.09388 |
| exa | 1.00 | Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems | https://arxiv.org/html/2506.17208v1 |
| exa | 1.00 | SWE-bench Goes Live! | https://arxiv.org/html/2505.23419 |
| exa | 1.00 | LIVECODEBENCH: | https://openreview.net/pdf?id=chfJJYC3iL |
| exa | 1.00 | Multi-LCB: Extending LiveCodeBench to Multiple Programming Languages | https://arxiv.org/html/2606.20517 |
| tavily | 0.82 | 2026年全网最全大模型API横评：Claude / GPT / Gemini等八大厂商20+主流模型 \| 七牛云 | https://news.qiniu.com/archives/1774508972073 |
| tavily | 0.81 | 2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云 | https://cloud.tencent.com/developer/article/2670420 |
| tavily | 0.79 | 国产模型与海外模型的Coding 能力对比：2026 年程序员该如何选择 | https://segmentfault.com/a/1190000047817400 |
| tavily | 0.78 | 国产三大模型深度对比：性能与性价比深度解析，2026年4月21日_人工智能_weixin_56622231-AtomGit开源社区 | https://gitcode.csdn.net/69e7629e54b52172bc6b4930.html |
| tavily | 0.77 | 2026年全网最全大模型API横评：Claude / GPT / Gemini 等8 大厂商 ... | https://segmentfault.com/a/1190000047676047 |
| tavily | 0.77 | 大模型代码编程能力评测排行榜 | https://www.datalearner.com/leaderboards/category/code |
| tavily | 0.76 | SWE-rebench 2026年1月：GLM-5，MiniMax M2.5，Qwen3-Coder-Next，Opus 4.6，Codex性能 : r/LocalLLaMA | https://www.reddit.com/r/LocalLLaMA/comments/1r3weq3/swerebench_jan_2026_glm5_minimax_m25?tl=zh-hans |
| tavily | 0.74 | 国产开源大模型2026 全景：Qwen3.6 / GLM-5.1 / Kimi K2.6 ... - OfoxAI | https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026 |
| tavily | 0.74 | SWE-bench February 2026 leaderboard update | https://simonwillison.net/2026/Feb/19/swe-bench |
| tavily | 0.73 | 大模型套餐深度分析：国内外主流平台全景对比- SkySeraph - 博客园 | https://www.cnblogs.com/skyseraph/p/19966095 |
| tavily | 0.73 | 国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏 | https://zhuanlan.zhihu.com/p/670574382 |
| tavily | 0.72 | 2026年6月主流大模型Coding能力深度对比：GPT ... - AtomGit开源社区 | https://gitcode.csdn.net/6a22fa2710ee7a33f278289f.html |
| tavily | 0.71 | SWE-bench Verified - Vals AI | https://vals.ai/benchmarks/swebench |
| tavily | 0.71 | Best LLMs for coding: 2026 roundup - Fireworks AI | https://fireworks.ai/blog/best-llms-for-coding |
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
2. [React-ing to Grace Hopper 200 Five Open-Weights Coding Models, One React Native App, One GH200, One Weekend or: why SWE-Bench rankings mispredicted which model actually shipped](https://arxiv.org/html/2604.17187v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
3. [React-ing to Grace Hopper 200 Five Open-Weights Coding Models, One React Native App, One GH200, One Weekend or: why SWE-Bench rankings mispredicted which model actually shipped](https://arxiv.org/html/2604.17187)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
4. [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://arxiv.org/html/2512.02556v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
5. [CodegenBench: Can LLMs Write Efficient Code Across Architectures?](https://arxiv.org/html/2606.04023v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
6. [Frontier Coding Agents Use Metaprogramming to Adapt to Unfamiliar Programming Languages](https://arxiv.org/html/2606.10933v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
7. [Qwen3-Coder-Next Technical Report](https://arxiv.org/html/2603.00729v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
8. [ProjDevBench: Benchmarking AI Coding Agents on End-to-End Project Development](https://www.arxiv.org/pdf/2602.01655)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
9. [Consistency Amplifies: How Behavioral Variance Shapes Agent Accuracy](https://www.arxiv.org/pdf/2603.25764)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
10. [GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/html/2602.15763v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
11. [Qwen3 Technical Report](https://arxiv.org/html/2505.09388)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
12. [Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems](https://arxiv.org/html/2506.17208v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
13. [SWE-bench Goes Live!](https://arxiv.org/html/2505.23419)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
14. [LIVECODEBENCH:](https://openreview.net/pdf?id=chfJJYC3iL)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
15. [Multi-LCB: Extending LiveCodeBench to Multiple Programming Languages](https://arxiv.org/html/2606.20517)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
16. [2026年全网最全大模型API横评：Claude / GPT / Gemini等八大厂商20+主流模型 | 七牛云](https://news.qiniu.com/archives/1774508972073)
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
18. [国产模型与海外模型的Coding 能力对比：2026 年程序员该如何选择](https://segmentfault.com/a/1190000047817400)
   - 工具：tavily
   - 分数：0.79
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
19. [国产三大模型深度对比：性能与性价比深度解析，2026年4月21日_人工智能_weixin_56622231-AtomGit开源社区](https://gitcode.csdn.net/69e7629e54b52172bc6b4930.html)
   - 工具：tavily
   - 分数：0.78
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
20. [2026年全网最全大模型API横评：Claude / GPT / Gemini 等8 大厂商 ...](https://segmentfault.com/a/1190000047676047)
   - 工具：tavily
   - 分数：0.77
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
21. [大模型代码编程能力评测排行榜](https://www.datalearner.com/leaderboards/category/code)
   - 工具：tavily
   - 分数：0.77
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
22. [SWE-rebench 2026年1月：GLM-5，MiniMax M2.5，Qwen3-Coder-Next，Opus 4.6，Codex性能 : r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1r3weq3/swerebench_jan_2026_glm5_minimax_m25?tl=zh-hans)
   - 工具：tavily
   - 分数：0.76
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
23. [国产开源大模型2026 全景：Qwen3.6 / GLM-5.1 / Kimi K2.6 ... - OfoxAI](https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026)
   - 工具：tavily
   - 分数：0.74
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
24. [SWE-bench February 2026 leaderboard update](https://simonwillison.net/2026/Feb/19/swe-bench)
   - 工具：tavily
   - 分数：0.74
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
25. [大模型套餐深度分析：国内外主流平台全景对比- SkySeraph - 博客园](https://www.cnblogs.com/skyseraph/p/19966095)
   - 工具：tavily
   - 分数：0.73
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
26. [国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏](https://zhuanlan.zhihu.com/p/670574382)
   - 工具：tavily
   - 分数：0.73
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
27. [2026年6月主流大模型Coding能力深度对比：GPT ... - AtomGit开源社区](https://gitcode.csdn.net/6a22fa2710ee7a33f278289f.html)
   - 工具：tavily
   - 分数：0.72
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
28. [SWE-bench Verified - Vals AI](https://vals.ai/benchmarks/swebench)
   - 工具：tavily
   - 分数：0.71
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
29. [Best LLMs for coding: 2026 roundup - Fireworks AI](https://fireworks.ai/blog/best-llms-for-coding)
   - 工具：tavily
   - 分数：0.71
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
31. [国产模型大比拼，谁是最佳AI编程模型？MiniMax-M3、Qwen-3.7-Max](https://www.youtube.com/watch?v=yt2uKtkN3Wk)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
32. [Which LLM to Choose in 2026? Selection Guide + Benchmarks](https://iternal.ai/llm-selection-guide)
   - 工具：tavily
   - 分数：0.65
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
33. [AI 大模型中文网 - 探索顶尖人工智能模型](https://aimodels.p2hp.com)
   - 工具：tavily
   - 分数：0.62
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
34. [Best LLMs for Coding in 2026: SWE-bench, HumanEval ... - Onyx AI](https://onyx.app/insights/best-llms-for-coding-2026)
   - 工具：tavily
   - 分数：0.62
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
35. [SWE-bench Pro Leaderboard (2026): Every Model Score, Claude ...](https://www.morphllm.com/swe-bench-pro)
   - 工具：tavily
   - 分数：0.61
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
36. [SWE-bench + - OpenLM.ai](https://openlm.ai/swe-bench)
   - 工具：tavily
   - 分数：0.61
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
37. [LLM Rank - 大型语言模型评测及排行榜](https://llmrank.cn)
   - 工具：tavily
   - 分数：0.60
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
38. [SWE-bench Verified - Epoch AI](https://epoch.ai/benchmarks/swe-bench-verified)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
39. [SWE-bench Leaderboards](https://www.swebench.com)
   - 工具：tavily
   - 分数：0.51
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
2. [国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏](https://zhuanlan.zhihu.com/p/670574382)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
3. [大模型代码编程能力评测排行榜](https://www.datalearner.com/leaderboards/category/code)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
4. [SWE-bench Verified - Vals AI](https://vals.ai/benchmarks/swebench)
   - 工具：tavily
   - 分数：0.60
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
5. [国产模型大比拼，谁是最佳AI编程模型？MiniMax-M3、Qwen-3.7-Max](https://www.youtube.com/watch?v=yt2uKtkN3Wk)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
6. [BRIDGE: benchmarking large language models for understanding real-world clinical practice texts - Nature](https://www.nature.com/articles/s41551-026-01719-2)
   - 工具：tavily
   - 分数：0.29
   - 来源等级：A
   - 剔除原因：score 低于 0.4
7. [Big Tech’s AI Datacenter Investments Might Be In Big Trouble - Forbes](https://www.forbes.com/sites/amirhusain/2026/06/17/big-techs-ai-datacenter-investments-might-be-in-big-trouble/)
   - 工具：tavily
   - 分数：0.17
   - 来源等级：C
   - 剔除原因：score 低于 0.4
8. [China isn’t trying to beat the U.S. at AI — it’s playing a completely different game - fortune.com](https://fortune.com/2026/06/16/china-ai-deepseek-open-source-efficiency-global-expansion-strategy/)
   - 工具：tavily
   - 分数：0.16
   - 来源等级：C
   - 剔除原因：score 低于 0.4
9. [New AI optimization framework beats Claude Code and Codex by 2.5x on the same compute budget - VentureBeat](https://venturebeat.com/orchestration/new-ai-optimization-framework-beats-claude-code-and-codex-by-2-5x-on-the-same-compute-budget)
   - 工具：tavily
   - 分数：0.15
   - 来源等级：C
   - 剔除原因：score 低于 0.4
10. [Claude Makes More Money Per User Than Market Leader ChatGPT Report Finds - Forbes](https://www.forbes.com/sites/siladityaray/2026/06/16/claude-makes-more-money-per-user-than-market-leader-chatgpt-report-finds/)
   - 工具：tavily
   - 分数：0.11
   - 来源等级：C
   - 剔除原因：score 低于 0.4
11. [NVIDIA GB300 Dominates Agentic AI Workloads With 20x Performance Leap Over Hopper As Rubin Nears Launch - Wccftech](https://wccftech.com/nvidia-gb300-dominates-agentic-ai-workloads-20x-performance-leap-over-hopper/)
   - 工具：tavily
   - 分数：0.03
   - 来源等级：C
   - 剔除原因：score 低于 0.4
12. [Most people use Ollama or llama.cpp for local LLMs, but these are the tools I switch to when it gets serious - XDA](https://www.xda-developers.com/most-people-ollama-llama-cpp-local-llms-tool-serious/)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
13. [New OpenAI Method Forecasts AI Risks Before Deployment - BankInfoSecurity](https://www.bankinfosecurity.com/new-openai-method-forecasts-ai-risks-before-deployment-a-32021)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
14. [Companies spent months pushing workers to use AI more. Now the token Hunger Games could be coming. - Business Insider](https://www.businessinsider.com/ai-token-economy-spending-workplace-budgets-usage-caps-software-engineer-2026-6)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
15. [An optimization-driven hierarchical deep learning approach using the Gray Langurs algorithm for data-driven seismic activity prediction - Nature](https://www.nature.com/articles/s41598-026-56169-2)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：A
   - 剔除原因：score 低于 0.4
16. [2026年全网最全大模型API横评：Claude / GPT / Gemini等八大厂商20+主流模型 | 七牛云](https://news.qiniu.com/archives/1774508972073)
   - 工具：tavily
   - 分数：0.78
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
17. [2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云](https://cloud.tencent.com/developer/article/2670420)
   - 工具：tavily
   - 分数：0.77
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
18. [国产三大模型深度对比：性能与性价比深度解析，2026年4月21日_人工智能_weixin_56622231-AtomGit开源社区](https://gitcode.csdn.net/69e7629e54b52172bc6b4930.html)
   - 工具：tavily
   - 分数：0.73
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
19. [大模型代码编程能力评测排行榜](https://www.datalearner.com/leaderboards/category/code)
   - 工具：tavily
   - 分数：0.71
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
20. [国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏](https://zhuanlan.zhihu.com/p/670574382)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
21. [2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云](https://cloud.tencent.com/developer/article/2670420)
   - 工具：tavily
   - 分数：0.78
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
22. [国产开源大模型2026 全景：Qwen3.6 / GLM-5.1 / Kimi K2.6 ... - OfoxAI](https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026)
   - 工具：tavily
   - 分数：0.71
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
23. [大模型代码编程能力评测排行榜](https://www.datalearner.com/leaderboards/category/code)
   - 工具：tavily
   - 分数：0.72
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
24. [国内外知名大模型及应用——模型/应用维度（2026/06/17） - 知乎专栏](https://zhuanlan.zhihu.com/p/670574382)
   - 工具：tavily
   - 分数：0.72
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
25. [SWE-bench Verified - Vals AI](https://vals.ai/benchmarks/swebench)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
26. [LLM Rank - 大型语言模型评测及排行榜](https://llmrank.cn)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果

## 完整精读结果

### 来源 1: 2026年全网最全大模型API横评：Claude / GPT / Gemini等八大厂商20+主流模型 | 七牛云

- URL: https://news.qiniu.com/archives/1774508972073
- 精读方法：firecrawl-scrape

# 502 Bad Gateway

* * *

openresty

### 来源 2: 国产开源大模型2026 全景：Qwen3.6 / GLM-5.1 / Kimi K2.6 ... - OfoxAI

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

### 来源 3: 大模型套餐深度分析：国内外主流平台全景对比- SkySeraph - 博客园

- URL: https://www.cnblogs.com/skyseraph/p/19966095
- 精读方法：firecrawl-scrape

[![Fork me on GitHub](https://camo.githubusercontent.com/365986a132ccd6a44c23a9169022c0b5c890c387/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f7265645f6161303030302e706e67)](https://github.com/skyseraph)

# [大模型套餐深度分析：国内外主流平台全景对比](https://www.cnblogs.com/skyseraph/p/19966095 "发布于 2026-05-02 13:27")

> 作者：skyseraph
>
> 日期：2026-04-30
>
> 原始链接： [llm](https://skyseraph.github.io/posts/2026/llm)
>
> 公众号： [llm](https://mp.weixin.qq.com/s/yKGL9JAL7Q-Vc9zmSIuS0Q)
>
> 数据截至 2026-05-01

* * *

## 一、全局概览：两条赛道，一场博弈

大模型套餐市场分化为两种范式：

- **按量计费（API）**：以 token 为单位付费，适合开发者，成本透明
- **订阅制（Consumer）**：月付/年付，固定费用解锁配额，适合个人和非技术用户

**2026 年最显著的趋势：国产模型在 token 使用量上已全面超越美国。**

据 OpenRouter 数据，2026 年 3 月 30 日至 4 月 5 日一周内，中国模型处理 **12.96 万亿 tokens**，美国模型仅 **3.03 万亿 tokens**。全球 token 消耗量前六名 **全部来自中国**。

* * *

## 二、全球 Token 使用量排行榜

> 数据来源： [OpenRouter Rankings](https://openrouter.ai/rankings) · [OpenRouter 2025 State of AI](https://openrouter.ai/state-of-ai)

| 排名 | 模型 | 厂商 | 周 Token 量（估算） | 主要优势 |
| --- | --- | --- | --- | --- |
| 1 | MiMo-V2.5-Pro | 小米 | ~4.79T | 1T 参数 MoE，1M 上下文 |
| 2 | Kimi K2.6 | Moonshot AI | ~1.4T | 编码榜第一，256K 上下文 |
| 3 | DeepSeek-V4-Flash | DeepSeek | 高 | 极低成本，1M 上下文 |
| 4 | Qwen 系列 | 阿里巴巴 | 高 | 多尺寸覆盖，开源生态 |
| 5 | GLM-5 | 智谱 Z.AI | 中高 | 国内首个上市大模型公司旗舰 |
| 6 | Claude Sonnet 4.6 | Anthropic | 中 | SWE-bench 标杆，综合能力领先 |
| 7 | Gemini 3.1 Flash | Google | 中 | 速度快，价格低，多模态 |
| 8 | GPT-5.5 | OpenAI | 中 | 生态最广，品牌溢价高 |
| 9 | MiniMax-M2.5 | MiniMax | 中 | 音视频多模态领先 |
| 10 | Grok 4 | xAI | 低中 | 实时 X 数据，推理强 |

**关键数据**

| 时间 | 中国模型 | 美国模型 | 全球总量 |
| --- | --- | --- | --- |
| 2025-05（首次超越） | 4.12 万亿 | 2.94 万亿 | — |
| 2026-03-30 ~ 04-05 | **12.96 万亿** | 3.03 万亿 | **27 万亿** |

> 中国模型在 OpenRouter 平台占比从 2025 年初 <2% 升至 2026 年 Q2 **>45%**。DeepSeek 开源份额从 ~80% 降至 ~40%，被 Qwen、MiMo 分流。

* * *

## 三、国内 TOP 5 大模型套餐

### 3.1 DeepSeek

**官网**： [chat.deepseek.com](https://chat.deepseek.com/) · **API 文档**： [api-docs.deepseek.com](https://api-docs.deepseek.com/) · **主体**：深度求索（杭州）

DeepSeek 以极低 API 价格和顶级推理能力著称，颠覆美国主导的定价体系。

#### 用户端

| 套餐 | 价格 | 说明 |
| --- | --- | --- |
| 免费版 | ¥0 | 全部功能，含 DeepSeek-V4-Flash 和深度思考 |
| 订阅制 | 无 | 官方不提供消费者月付套餐 |

> 差异化策略：超低 API 价格服务开发者，消费端完全免费获客。

#### API 计费（/1M tokens）

| 模型 | 输入 | 缓存命中 | 输出 | 上下文 |
| --- | --- | --- | --- | --- |
| DeepSeek-V4-Flash | $0.14 | $0.0028 | $0.28 | 1M |
| DeepSeek-V4-Pro（折扣 75%） | $0.435 | $0.003625 | $0.87 | 1M |
| DeepSeek-V4-Pro（原价） | ~$1.74 | — | ~$3.48 | 1M |
| DeepSeek-V3（旧） | ~$0.20 | — | — | 128K |

> 75% 折扣有效期至 2026-05-05 15:59 UTC，来源： [The Next Web](https://thenextweb.com/news/deepseek-v4-pro-price-cut-75-percent)

**优点**：免费版功能完整 · API 价格全球最低之一（比 GPT-5.5 便宜 35-100x）· 开源可本地部署

**缺点**：无消费者订阅套餐 · 高峰期偶发不稳定 · 无多模态 · 实时信息有限

* * *

### 3.2 Kimi（Moonshot AI）

**官网**： [kimi.moonshot.cn](https://kimi.moonshot.cn/)（国内）/ [kimi.com](https://www.kimi.com/)（国际）· **主体**：月之暗面（北京）

超长上下文见长（最高 200 万字），知识工作者首选。

#### 用户端

| 套餐 | 月付 | 年付 | 主要权益 |
| --- | --- | --- | --- |
| Free | $0 | $0 | 基础对话，有每日限额 |
| 标准套餐 | ~$19 | 更优惠 | 更高频次，优先响应 |
| 高级套餐 | 多档位 | 最高省 $480 | 全部功能，最高配额 |

> 国内版（人民币）：¥0 – ¥399，以 kimi.moonshot.cn 页面为准。

#### Kimi Code 开发者套餐

- 输出速度：最高 **100 tokens/s**
- 5 小时 token 配额，约 300–1,200 次 API 调用
- 最大并发： **30**

#### API 计费

| 模型 | 输入/1M | 输出/1M | 上下文 |
| --- | --- | --- | --- |
| Kimi K2.6 | $0.60 | $2.50 | 256K |

> 比 GPT-5.4 便宜 4-17x，比 Claude Sonnet 4.6 便宜 5-6x。

**优点**：超长上下文（国内最高 2M）· 文档解析强（PDF/Word/Excel）· 编码能力全球前列

**缺点**：免费版限额严格 · 套餐描述不透明，需登录查看 · 多模态能力较弱

* * *

### 3.3 智谱清言 / GLM（Z.AI）

**官网**： [chatglm.cn](https://chatglm.cn/) · **开发者平台**： [bigmodel.cn](https://bigmodel.cn/) / [docs.z.ai](https://docs.z.ai/) · **主体**：智谱 AI（北京），国内首家上市 AI 大模型公司

GLM-5 于 2026 年 2 月发布，性能达全球前列。

#### 用户端

| 套餐 | 价格 | 说明 |
| --- | --- | --- |
| 免费版 | ¥0 | 基础对话 |
| 会员版 | 官网为准 | 更高配额，优先 GLM-5 |
| GLM Coding Plan | **$18/月** | 支持 Claude Code、Cursor、Cline |

> 面向开发者，性价比最高的 Claude-alternative 订阅之一。来源： [GLM Coding Plan 2026](https://truescho.com/en/blog/glm-coding-plan-zai-2026)

#### API 计费

| 模型 | 输入/1M | 输出/1M | 上下文 |
| --- | --- | --- | --- |
| GLM-5 | $1.00 | $0.20 | 200K |
| GLM-5-Code | $1.20–$5.00 | $0.30 | 128K |
| GLM-4.7 | $0.60 | — | — |
| GLM-4.5 系列 | 低成本 | — | — |

**优点**：国内合规性最强 · GLM-5 性能全球前列 · Coding Plan 对开发工具支持度高 · 企业级服务体系完整

**缺点**：消费端套餐不透明 · API 价格高于 DeepSeek · 国际化知名度低 · 低档套餐联网受限

* * *

### 3.4 MiniMax

**官网（海螺 AI）**： [hailuoai.com](https://hailuoai.com/) · **开发者平台**： [platform.minimaxi.com](https://platform.minimaxi.com/) · **主体**：MiniMax（上海）

音视频多模态能力著称，MiniMax-M2.5 开源运行成本约 **$1/小时**。

#### 用户端

| 套餐 | 价格 | 说明 |
| --- | --- | --- |
| 免费版 | ¥0 | 基础对话，图像生成有限额 |
| 会员版 | 官网为准 | 更高配额，AI 视频生成 |

> 以音视频内容创作为核心卖点，适合创意工作者。

#### API 计费

| 模型 | 输入/1M | 上下文 | 参数 |
| --- | --- | --- | --- |
| MiniMax-M2.5 | ~$0.30 | 200K | 230B（10B active MoE） |

**优点**：音频合成（TTS）和视频生成能力领先 · MoE 架构运行成本极低 · 多模态综合

**缺点**：纯文本能力略弱于 DeepSeek/Kimi · 品牌知名度低 · 套餐信息更新不及时

* * *

### 3.5 小米 MiMo

**官网**： [mimo.mi.com](https://mimo.mi.com/) · **主体**：小米集团

2026 年 token 用量增速最快，V2.5-Pro 以 1.02T 参数 MoE 架构登顶 OpenRouter 周度用量第一。

#### 用户端（TokenPlan）

| 套餐 | 月付 | 说明 |
| --- | --- | --- |
| 入门档 | **¥39/月** | 88% 首购折扣，轻度使用 |
| 进阶档 | 多档位 | 月付/年付，积分制 |
| 企业档 | 定制 | 专属资源，高并发 |

> TokenPlan 积分制比传统按次计费更灵活。API 完全兼容 OpenAI 和 Claude 格式。

#### API 计费

| 模型 | 输入/1M | 上下文 | 特点 |
| --- | --- | --- | --- |
| MiMo-V2-Pro | $1.00 | 1M | SWE-Bench 78% |
| MiMo-V2.5-Pro | $1.00 | 1M | OpenRouter 用量第一 |
| MiMo-V2-Flash | 免费（限额） | — | 开源轻量 |

**优点**：OpenRouter 用量全球第一（~4.79T）· API 价格极具竞争力 · 1M 超长上下文 · TokenPlan 灵活

**缺点**：品牌积累时间短 · 消费端产品体验待完善 · 主要优势集中在 API

* * *

## 四、海外 TOP 5 大模型套餐

### 4.1 ChatGPT（OpenAI）

**官网**： [chatgpt.com](https://chatgpt.com/) · **定价**： [openai.com/chatgpt/pricing](https://openai.com/chatgpt/pricing/)

全球用户量最大，2026 年 4 月推出 GPT-5.5，套餐扩展至六档。

#### 订阅套餐

| 套餐 | 月付 | 年付 | 主要功能 |
| --- | --- | --- | --- |
| Free | $0 | $0 | GPT-4o-mini，有限额，无图像生成 |
| Go | ~$8 | — | 轻量付费，休闲用户 |
| **Plus** | **$20** | — | GPT-5.5，扩展图像生成，优先响应 |
| Pro（低档） | **$100** | — | 更高配额，高级推理模型 |
| Pro（高档） | **$200** | — | 近无限制，全模型访问 |
| Business | **$20/seat** | 年付 | 管理后台，SAML SSO，数据隐私 |
| Enterprise | 定制 | 定制 | 500+ 人团队，最高合规 |

> 2026-04 更新：Business 降至 $20/seat；Pro 新增 $100 入门档；GPT-5.5 成为 Plus 及以上默认模型。

#### API 计费

| 模型 | 输入/1M | 输出/1M |
| --- | --- | --- |
| GPT-5.5 | $1.75 | $14.00 |
| GPT-5 mini | $0.25 | $2.00 |
| GPT-5 nano | $0.05 | $0.40 |

**优点**：全球用户量最大，生态最完善（插件、GPT Store）· 套餐灵活，$8 覆盖轻度用户 · GPT-5.5 综合能力强

**缺点**：$200 Pro 性价比争议大 · API 价格偏高 · 国内需FQ · Plus 高峰期降速

* * *

### 4.2 Claude（Anthropic）

**官网**： [claude.ai](https://claude.ai/) · **定价**： [anthropic.com/pricing](https://anthropic.com/pricing)

代码能力和安全性著称，Claude Code 是 SWE-bench 评分最高工具（~80.9%）。

#### 订阅套餐

| 套餐 | 月付 | 主要功能 |
| --- | --- | --- |
| Free | $0 | 基础对话，无 Claude Code |
| **Pro** | **$20** | 标准配额，含 Claude Code |
| Max 5x | **$100** | Pro 的 5 倍配额 |
| Max 20x | **$200** | Pro 的 20 倍，Opus 4.6，1M 上下文 |
| Team | **$25–30/seat** | 最少 2 人，协作，Cowork（2026-01 上线） |
| Enterprise | 定制 | 高合规，专属支持 |

#### API 计费

| 模型 | 输入/1M | 输出/1M | 上下文 |
| --- | --- | --- | --- |
| Claude Opus 4.6 | $5.00 | $25.00 | 1M |
| Claude Sonnet 4.6 | $3.00 | $15.00 | 200K |
| Claude Haiku 4.5 | $1.00 | $5.00 | 200K |

**优点**：SWE-bench 最高分 · Claude Code 最强终端编码代理 · Max 套餐对重度用户友好

**缺点**：中文处理弱于国产模型 · $200 Max 价高 · Team 最少 2 人起 · 国内需FQ

* * *

### 4.3 Gemini（Google）

**官网**： [gemini.google.com](https://gemini.google.com/) · **定价**： [one.google.com/about/ai-premium](https://one.google.com/about/ai-premium)

I/O 2025 重组为三档，并入 Google One 生态，捆绑 YouTube Premium + 2TB 存储。

#### 订阅套餐

| 套餐 | 月付 | 主要功能 |
| --- | --- | --- |
| Free | $0 | 基础版，有限额 |
| Google AI Plus | **$7.99** | 入门付费，扩展访问 |
| **Google AI Pro** | **$19.99** | Gemini 3.1 Pro，2M 上下文，2TB 存储，Deep Research，NotebookLM+ |
| Google AI Ultra | **$249.99** | 最高配额，Veo 3.1 视频生成，Google Home 集成 |

> 首月免费试用（新用户）。Google AI Pro = 原 Gemini Advanced / Google One AI Premium。

#### API 计费

| 模型 | 输入/1M | 输出/1M | 上下文 |
| --- | --- | --- | --- |
| Gemini 2.5 Pro | $1.25 | $5.00 | 2M |
| Gemini 3 Flash | $0.50 | $3.00 | 1M |
| Gemini 3.1 Flash Lite | $0.25 | $1.50 | — |

**优点**：$19.99 捆绑 2TB + YouTube Premium，综合性价比最高 · 2M 上下文最长 · Google Workspace 深度集成

**缺点**：$249.99 Ultra 定价激进 · 代码能力不及 Claude · 产品线频繁改名（Bard→Gemini→Google AI）

* * *

### 4.4 Grok（xAI）

**官网**： [grok.com](https://grok.com/) · **定价**： [grok.com/pricing](https://grok.com/pricing)

实时访问 X（Twitter）平台数据，Grok 4 推理能力突出。

#### 独立套餐

| 套餐 | 月付 | 主要功能 |
| --- | --- | --- |
| Free | $0 | 实时 X，Aurora 图像，6 秒视频，语音，Grok 3/4 有限访问 |
| SuperGrok Lite | **$10** | 扩展限额 |
| SuperGrok | **$30** | 720p HD 视频，30 秒短片，4 个专家 AI 代理 |
| SuperGrok Heavy | **$300** | 最高配额，全模型访问 |

#### X 捆绑套餐

| 套餐 | 月付 | 年付 | Grok 权益 |
| --- | --- | --- | --- |
| X Basic | $3 | $32 | 基础访问 |
| X Premium | $8 | $84 | 中等访问 |
| X Premium+ | $40 | $395 | 完整权益 |

> 企业版：Grok Business $30/seat/月起；SuperGrok Heavy Business $300/seat/月

**优点**：实时 X 数据独家优势 · Free 档功能慷慨（含视频）· $10 Lite 性价比最高入门

**缺点**：$300 Heavy 价格虚高 · 与 X 强绑定 · 多模态不及 GPT-5.5/Gemini

* * *

### 4.5 Perplexity AI

**官网**： [perplexity.ai](https://www.perplexity.ai/) · **定价**： [perplexity.ai/pro](https://www.perplexity.ai/pro)

"AI 搜索引擎"定位，实时联网 + 引用溯源，研究型用户首选。

#### 订阅套餐

| 套餐 | 月付 | 年付 | 主要功能 |
| --- | --- | --- | --- |
| Free | $0 | $0 | 基础搜索，有限 Pro 次数 |
| **Pro** | **$20** | **$200**（≈$16.7/月） | 无限 Pro 搜索，可选 GPT/Claude/Gemini，文件上传，API 积分 |
| Enterprise | 定制 | 定制 | SSO，数据隐私，团队管理 |

**优点**：实时联网，所有答案可溯源 · Pro 可切换后端模型 · 年付 $200 是 $20 档最实惠 · 学术研究首选

**缺点**：搜索为核心，代码/创作非强项 · 依赖第三方模型 · Enterprise 价格不透明

* * *

## 五、横向对比总表

### 5.1 消费者订阅套餐

| 平台 | 免费档 | 入门付费 | 主力 | 旗舰 |
| --- | --- | --- | --- | --- |
| DeepSeek | ✅ 功能完整 | 无 | 无 | 无 |
| Kimi | ✅ 有限额 | — | ~$19/月 | 多档 |
| 智谱清言 | ✅ | — | 官网查看 | — |
| MiniMax（海螺） | ✅ | — | 官网查看 | — |
| MiMo | ✅ | **¥39/月** | 多档 | 企业定制 |
| ChatGPT | ✅ | $8（Go） | **$20（Plus）** | $100–200（Pro） |
| Claude | ✅ | — | **$20（Pro）** | $100–200（Max） |
| Gemini | ✅ | $7.99 | **$19.99** | $249.99 |
| Grok | ✅ 功能全 | $10（Lite） | $30 | $300 |
| Perplexity | ✅ | — | **$20** | — |

### 5.2 API 价格对比（/1M tokens）

| 模型 | 输入 | 输出 | 上下文 | 性价比 |
| --- | --- | --- | --- | --- |
| DeepSeek-V4-Flash | **$0.14** | **$0.28** | 1M | ⭐⭐⭐⭐⭐ |
| MiniMax-M2.5 | $0.30 | — | 200K | ⭐⭐⭐⭐⭐ |
| Gemini 3.1 Flash Lite | $0.25 | $1.50 | — | ⭐⭐⭐⭐⭐ |
| Kimi K2.6 | $0.60 | $2.50 | 256K | ⭐⭐⭐⭐ |
| GLM-5 | $1.00 | $0.20 | 200K | ⭐⭐⭐⭐ |
| MiMo-V2.5-Pro | $1.00 | — | 1M | ⭐⭐⭐⭐ |
| DeepSeek-V4-Pro（折扣） | $0.435 | $0.87 | 1M | ⭐⭐⭐⭐ |
| Gemini 2.5 Pro | $1.25 | $5.00 | 2M | ⭐⭐⭐⭐ |
| GPT-5 mini | $0.25 | $2.00 | — | ⭐⭐⭐ |
| Claude Haiku 4.5 | $1.00 | $5.00 | 200K | ⭐⭐⭐ |
| Claude Sonnet 4.6 | $3.00 | $15.00 | 200K | ⭐⭐⭐ |
| Claude Opus 4.6 | $5.00 | $25.00 | 1M | ⭐⭐ |
| GPT-5.5 | $1.75 | $14.00 | — | ⭐⭐ |

### 5.3 功能维度对比

| 功能 | DeepSeek | Kimi | GLM | MiniMax | MiMo | ChatGPT | Claude | Gemini | Grok | Perplexity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 超长上下文（>200K） | ✅1M | ✅2M | ✅200K | ✅200K | ✅1M | ✅部分 | ✅1M | ✅2M | ❌ | ❌ |
| 实时联网搜索 | 有限 | ✅ | ✅ | 有限 | 有限 | ✅ | 有限 | ✅ | ✅X | ✅ |
| 图像生成 | ❌ | 有限 | ✅ | ✅ | 有限 | ✅ | ❌ | ✅ | ✅ | ❌ |
| 视频生成 | ❌ | 有限 | ❌ | ✅ | ❌ | ❌ | ❌ | ✅Veo | ✅ | ❌ |
| 语音模式 | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| 代码能力 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| 中文优化 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| 国内可用 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 开源 | ✅ | ❌ | ✅部分 | ✅部分 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

* * *

## 六、隐性成本与弊端

### 6.1 通用陷阱

- **"无限制"水分**：所有套餐都有隐性 Rate Limit，高峰期降速。建议实测高峰期响应再决定。
- **上下文窗口 ≠ 有效理解**：模型在超长文档的"中间遗忘"现象仍存在，实际可靠长度远低于技术上限。
- **年付退款风险**：通常不支持中途退款，模型迭代快，建议先月付观察 1-2 个月再年付。

### 6.2 国内平台弊端

| 平台 | 主要弊端 |
| --- | --- |
| **DeepSeek** | 无订阅制，无多模态；高峰期服务器繁忙；对话历史同步弱 |
| **Kimi** | 免费额消耗快；付费档不透明需登录查看；长文档摘要偶发幻觉 |
| **GLM** | 消费端套餐模糊；API 价格偏高；中文开发环境适配有限 |
| **MiniMax** | 文字能力不及 DeepSeek/Kimi；多模态积分制实际花费高于预期 |
| **MiMo** | 消费端产品不成熟；TokenPlan 积分制理解门槛高 |

### 6.3 海外平台弊端

| 平台 | 主要弊端 |
| --- | --- |
| **ChatGPT Plus（$20）** | 高峰期仍降速；对话记忆弱；国内需FQ+境外支付 |
| **ChatGPT Pro（$200）** | 性价比争议大，$100 新档覆盖大部分场景 |
| **Claude Pro（$20）** | 有每日上限，重度用户易触顶 |
| **Claude Max（$100–200）** | 价高；无法图像/视频；国内无法访问 |
| **Gemini Pro（$19.99）** | Ultra $249.99 定价过高；产品多次改名影响信任 |
| **Grok SuperGrok（$30）** | 依赖 X 生态；$300 Heavy 虚高 |
| **Perplexity Pro（$20）** | 不适合创作/代码；稳定性依赖第三方 |

* * *

## 七、选型建议

### 场景 → 推荐

| 场景 | 首选 | 备选 |
| --- | --- | --- |
| 个人日常（国内，0 成本） | DeepSeek 免费 | Kimi 免费 |
| 个人日常（海外，$20） | Claude Pro | ChatGPT Plus |
| 超长文档分析 | Kimi 付费 | Gemini Pro |
| AI 编码代理 | Claude Max | DeepSeek API + Claude Code |
| 极致低成本 API | DeepSeek-V4-Flash | MiniMax-M2.5 |
| 研究/实时搜索 | Perplexity Pro | Kimi + 联网 |
| 音视频创作 | MiniMax 会员 | Gemini Pro（Veo） |
| 舆情监控 | Grok SuperGrok | Perplexity Pro |
| 企业级（国内合规） | 智谱 GLM 企业版 | DeepSeek API 私有化 |
| 企业级（海外） | Claude Enterprise | ChatGPT Enterprise |

### 一句话总结

| 需求 | 推荐 |
| --- | --- |
| 免费用，功能完整 | **DeepSeek**（国内） |
| $20 最优性价比 | **Claude Pro** / **Gemini AI Pro** |
| 极致低成本 API | **DeepSeek-V4-Flash**（$0.14/1M） |
| 最强代码能力 | **Claude + Claude Code** |
| 超大上下文 | **Kimi**（2M）/ **Gemini 2.5 Pro**（2M） |
| 实时信息搜索 | **Perplexity Pro** |
| Token 用量增速最快 | **MiMo**（OpenRouter 第一） |

* * *

## 八、参考资料

**Token 使用量**

- [OpenRouter Rankings](https://openrouter.ai/rankings)
- [OpenRouter 2025 State of AI Report](https://openrouter.ai/state-of-ai)
- [Global Times - Chinese AI Models Take Top Six](https://www.globaltimes.cn/page/202604/1358300.shtml)
- [KuCoin - China Weekly Usage Surpasses US](https://www.kucoin.com/news/flash/china-s-ai-large-models-weekly-usage-surpasses-u-s-for-fifth-consecutive-week)
- [People's Daily - Chinese AI Models Gain Global Use](http://english.people.com.cn/n3/2026/0408/c98649-20444434.html)

**国内平台定价**

- [DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing)
- [DeepSeek V4-Pro 75% Price Cut](https://thenextweb.com/news/deepseek-v4-pro-price-cut-75-percent)
- [Kimi Membership Pricing](https://www.kimi.com/help/membership/membership-pricing)
- [Kimi K2.6 API Pricing](https://www.kimi.com/resources/kimi-k2-6-pricing)
- [Z.AI Developer Docs - Pricing](https://docs.z.ai/guides/overview/pricing)
- [GLM Coding Plan 2026](https://truescho.com/en/blog/glm-coding-plan-zai-2026)
- [MiniMax-M2.5 on HuggingFace](https://huggingface.co/blog/mlabonne/minimax-m25)
- [Xiaomi MiMo TokenPlan](https://www.gizchina.com/ai/xiaomi-launches-mimo-large-model-with-tokenplan-pricing-starting-at-39-yuan)

**海外平台定价**

- [ChatGPT Pricing 2026](https://fritz.ai/chatgpt-pricing/)
- [OpenAI 官方定价](https://openai.com/chatgpt/pricing/)
- [Claude AI Pricing 2026](https://truescho.com/en/blog/claude-ai-pricing-2026)
- [Anthropic 官方定价](https://anthropic.com/pricing)
- [Gemini Pricing](https://www.screenapp.io/blog/gemini-pricing)
- [Grok Pricing Guide 2026](https://grokipediawiki.com/grokipedia/grok-pricing-guide/)
- [AI Cloud Subscriptions 2026](https://jamesm.blog/ai/ai-cloud-subscriptions/)
- [AI API Pricing Comparison 2026](https://intuitionlabs.ai/articles/ai-api-pricing-comparison-grok-gemini-openai-claude)

![image](https://img2024.cnblogs.com/blog/137896/202605/137896-20260502131529523-237688711.png)

本文来自博客园，作者： [SkySeraph](https://www.cnblogs.com/skyseraph/)，转载请注明原文链接： [https://www.cnblogs.com/skyseraph/p/19966095](https://www.cnblogs.com/skyseraph/p/19966095)

posted @
2026-05-02 13:27 [SkySeraph](https://www.cnblogs.com/skyseraph)
阅读(1810)
评论(1)

收藏 [举报](https://report.cnblogs.com/?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fskyseraph%2Fp%2F19966095&targetId=19966095&targetType=0)

[刷新页面](https://www.cnblogs.com/skyseraph/p/19966095#) [返回顶部](https://www.cnblogs.com/skyseraph/p/19966095#top)

登录后才能查看或发表评论，立即 登录 或者
[逛逛](https://www.cnblogs.com/) 博客园首页

[![](https://img2024.cnblogs.com/blog/35695/202512/35695-20251201125434258-461912837.webp)](https://www.trae.com.cn/?utm_source=advertising&utm_medium=cnblogs_ug_cpa&utm_term=hw_trae_cnblogs)

### 公告

点击右上角即可分享

![微信分享提示](https://img2023.cnblogs.com/blog/35695/202309/35695-20230906145857937-1471873834.gif)

### 来源 4: 大模型代码编程能力评测排行榜

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

### 来源 5: 2026年全网最全大模型API横评：Claude / GPT / Gemini 等8 大厂商 ...

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

### 来源 6: 2026 年AI 编程实测：6 款顶流大模型对比，效率直接翻倍！ - 腾讯云

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

### 来源 7: SWE-rebench 2026年1月：GLM-5，MiniMax M2.5，Qwen3-Coder-Next，Opus 4.6，Codex性能 : r/LocalLLaMA

- URL: https://www.reddit.com/r/LocalLLaMA/comments/1r3weq3/swerebench_jan_2026_glm5_minimax_m25?tl=zh-hans
- 精读方法：failed

精读失败：403 Client Error: Forbidden for url: https://api.firecrawl.dev/v2/scrape

### 来源 8: Qwen3-Coder-Next Technical Report

- URL: https://www.arxiv.org/pdf/2603.00729
- 精读方法：jina-readerlm-academic

```markdown
The provided draft Markdown does not match the content of the original HTML, which only contains a head tag with no actual body content. Therefore, there is nothing to extract or refine further into Markdown beyond the title "Your Title" if one were present.
```

### 来源 9: SWE-bench Goes Live!

- URL: https://arxiv.org/html/2505.23419
- 精读方法：jina-readerlm-academic

```markdown
## Table of Contents

1. [Introduction](https://arxiv.org/html/2505.23419#S1)
   - [Related Work](https://arxiv.org/html/2505.23419v2#S2)

### 1. Introduction

Large language models (LLMs) have revolutionized software engineering, enabling advanced code generation and issue resolution tasks. SWE-bench, a benchmark series focusing on code-related tasks, has gained widespread attention for its comprehensive evaluation framework.

#### Related Work

**Coding Benchmarks**

- **Austin, Jacob**, et al. Program synthesis with large language models. arXiv preprint arXiv:2108.07732 (2021).
- **Tworek, Augustus**, et al. Evaluating large language models trained on code. Advances in Neural Information Processing Systems (NeurIPS), pp. 31–53 (2023).

**Coding Agents**

- **Yang, John**, et al. Swe-agent: Agent-computer interfaces enable automated software engineering. Advances in Neural Information Processing Systems (NeurIPS), pp. 50528–50652 (2024).

**Web**

- **Flask**, et al. Flask: A Python web framework for rapid application development and deployment. BSD-3-Clause (2019).
- **Twinbox**, et al. Beetbox: A fast and secure database backend for SQLite databases using Twisted tornado framework for asynchronous network operations and Django ORM for object-oriented modeling of relational data structures.

#### Appendix B Task Formulation

![Image 1: Refer to caption](https://arxiv.org/html/2505.23419/v1/x6.png)

The issue-resolving task requires the model to generate a patch that addresses a given issue, with its correctness evaluated through test execution.

#### Appendix C Performance vs Repository Difficulty

![Image 2: Refer to caption](https://arxiv.org/html/2505.23419/v1/x7.png)

Resolved rate in relation to the number of files and lines of code of a repository.

#### Appendix D Dataset Fields

| Field | Type | Description |
| --- | --- | --- |
| base\_commit | str | The commit on which the pull request is based, representing the repository state before the issue is resolved. |
| patch | str | Gold patch proposed by the pull request, in .diff format. |
| test\_patch | str | Modifications to the test suite proposed by the pull request that are typically used to check whether the issue has been resolved. |
| problem\_statement | str | Issue description text, typically describing the bug or requested feature, used as the task problem statement. |
| FAIL\_TO\_PASS | List\[str\] | Test cases that are expected to successfully transition from failing to passing are used to evaluate the correctness of the patch. |
| PASS\_TO\_PASS | List\[str\] | Test cases that are already passing prior to applying the gold patch. A correct patch shouldn’t introduce regression failures in these tests. |

#### Appendix E Experimental Setup Details

##### Hyperparameters used in the experiments.

For OpenHands, we set a maximum of 60 iterations per instance, with the LLM configured to use a temperature of 0.0 and a top-p value of 1.0 as default.

For SWE-agent, we limit the number of LLM calls to 100 per instance, with the temperature set to 0.0 and top-p to 1.0.

For Agentless, both the number of localization samples and repair samples are set to 1, corresponding to a single rollout.

##### Random seed in subset splitting.

The only stochastic component in this work arises during the sampling of the lite subset, where we set the random seed to 42.

##### Computational resources.

All LLM calls in this work are made through official APIs.
```

### 来源 10: Qwen3 Technical Report

- URL: https://arxiv.org/html/2505.09388
- 精读方法：jina-readerlm-academic

```markdown
# Qwen3 Technical Report

## Abstract

In this work, we present Qwen3, the latest version of the Qwen model family. Qwen3 comprises a series of large language models (LLMs) designed to advance performance, efficiency, and multilingual capabilities. The Qwen3 series includes models of both dense and Mixture-of-Expert (MoE) architectures, with parameter scales ranging from 0.6 to 235 billion. A key innovation in Qwen3 is the integration of thinking mode (for complex, multi-step reasoning) and non-thinking mode (for rapid, context-driven responses) into a unified framework. This eliminates the need to switch between different models—such as chat-optimized models (e.g., GPT-4o) and dedicated reasoning models (e.g., QwQ-32B)—and enables dynamic mode switching based on user queries or chat templates. Meanwhile, Qwen3 introduces a thinking budget mechanism, allowing users to allocate computational resources adaptively during inference, thereby balancing latency and performance based on task complexity. Moreover, by leveraging the knowledge from the flagship models, we significantly reduce the computational resources required to build smaller-scale models, while ensuring their highly competitive performance. Empirical evaluations demonstrate that Qwen3 achieves state-of-the-art results across diverse benchmarks, including tasks in code generation, mathematical reasoning, agent tasks, etc., competitive against larger MoE models and proprietary models. Compared to its predecessor Qwen2.5, Qwen3 expands multilingual support from 29 to 119 languages and dialects, enhancing global accessibility through improved cross-lingual understanding and generation capabilities.

To facilitate reproducibility and community-driven research and development, all Qwen3 models are publicly accessible under Apache 2.0.

## Introduction

The pursuit of artificial general intelligence (AGI) or artificial super intelligence (ASI) has long been a goal for humanity. Recent advancements in large foundation models, e.g., GPT-4o (<span id="S4.SS1.p1.1.1" class="ltx_text ltx_font_bold">gpt4o</span>) , Claude 3.7 (<span id="S4.SS1.p1.1.2" class="ltx_text ltx_font_bold">claude3.7</span>) , Gemini 2.5 (<span id="S4.SS1.p1.1.3" class="ltx_text ltx_font_bold">gemini2.5</span>) , DeepSeek-V3 (<span id="S4.SS1.p1.1.4" class="ltx_Text ltx_font_bold">deepseekv3</span>) , Llama-4 (<span id="S4.SS1.p1.1.5" class="ltx_Text ltx_font_bold">llama4</span>) , and Qwen2.5 (<span id="S4.SS1.p1.1.6" class="ltx_Text ltx_font_bold">qwen2.5</span>) , have demonstrated significant progress toward this objective.

These models are trained on vast datasets spanning trillions of tokens across diverse domains and tasks, effectively distilling human knowledge and capabilities into their parameters.

Notably, an increasing number of top-tier models (<span id="S4.SS1.p2." class="ltx_text ltx_framed ltx_framed_underline">[doremi](https://arxiv.org/pdf/2009/06878.pdf); <span id="S4.SS1.p2." class="ltx_text ltx_framed ltx_framed_underline">doge](https://arxiv.org/pdf/2009/06878.pdf); <span id="S4.SS1.p2." class="ltx_text ltx_framed ltx_framed_underline">regmix](https://arxiv.org/pdf/2009/06878.pdf)) have emerged as part of a growing open-source community focused on improving foundation models.

While most state-of-the-art models remain proprietary:

*   **Open Source Models:** [Claude 3](https://www.anthropic.com/news/pricing)
*   [Gemma-3](https://ai.meta.com/blog/introducing-gemma/)
*   [Llama-3](https://blog.google/technology/developers/google-gemini-update-new-language-models-and-developer-tools/)
*   [DeepSeek-V3](https://platform


## 跨源矛盾检测结论

### 检测范围
- 已精读来源数量：9 个
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
