---
title: "调研证据包：ai投标 投标助手 招标文件解析 ai解析 解析提示词 ai拆分招标文件"
source-type: article
generated: 2026-06-21
generated-by: wiki-research-skill
research-mode: standard
---

# 调研证据包：ai投标 投标助手 招标文件解析 ai解析 解析提示词 ai拆分招标文件

## 调研问题

ai投标 投标助手 招标文件解析 ai解析 解析提示词 ai拆分招标文件

## 摘要

本文档是四工具检索生成的证据包草稿，不是最终调研报告。Agent 必须先阅读本证据包，执行下方"AI 综合指令"，生成新的中文综合 raw 报告，然后询问用户是否入库。本证据包保留不删除。

- 发现候选信源：32
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
| exa | 1.00 | A Large Language Model-based Framework for Semi-Structured Tender Document Retrieval-Augmented Generation | https://arxiv.org/html/2410.09077v1 |
| exa | 1.00 | [2603.22513v1] Generating and Evaluating Sustainable Procurement Criteria for the Swiss Public Sector using In-Context Prompting with Large Language Models | https://arxiv.org/abs/2603.22513v1 |
| exa | 1.00 | Exploring Information Retrieval Landscapes: An | https://arxiv.org/pdf/2409.08479 |
| exa | 1.00 | DocSplit: A Comprehensive Benchmark Dataset and Evaluation Approach for Document Packet Recognition and Splitting | https://arxiv.org/html/2602.15958 |
| exa | 1.00 | Uni-Parser Technical Report | https://arxiv.org/abs/2512.15098v1 |
| exa | 1.00 | [2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models | https://arxiv.org/abs/2309.12132v2 |
| exa | 1.00 | Intelligent Processing of Design Notices in Engineering Procurement Construction Projects | https://www.mdpi.com/2075-5309/15/5/805 |
| exa | 1.00 | Large Language Model for Extracting Complex Contract Information in Industrial Scenes | https://arxiv.org/html/2507.06539v2 |
| exa | 1.00 | IndustryBench: Probing the Industrial Knowledge Boundaries of LLMs | https://arxiv.org/html/2605.10267v3 |
| exa | 1.00 | AIDABench: AI Data Analytics Benchmark | https://arxiv.org/html/2603.15636v1 |
| exa | 1.00 |  | https://arxiv.org/pdf/2008.02347 |
| exa | 1.00 | Infinity-Parser: Layout-Aware Reinforcement Learning for Scanned Document Parsing | https://arxiv.org/html/2506.03197v1 |
| exa | 1.00 | Logics-Parsing: An End-to-end Document Parsing Model with Layout-centric Reinforcement Learning | https://arxiv.org/html/2509.19760v1 |
| exa | 1.00 | The Measure of All Measures: Quantifying LLM Benchmark Quality \| OpenReview | https://openreview.net/forum?id=HpnGmTIs7Z&referrer=%5Bthe+profile+of+Zhen+Dong%5D%28%2Fprofile%3Fid%3D%7EZhen_Dong3%29 |
| tavily | 0.78 | 标书智能体（一）——AI解析招标文件代码+提示词 - 易标AI - 博客园 | https://www.cnblogs.com/yibiaoai/p/19064673 |
| tavily | 0.68 | AI写标书｜DeepSeek搞不定的投标痛点，被它拿捏了！ - 知乎 | https://zhuanlan.zhihu.com/p/1908566825068913729 |
| tavily | 0.67 | 艾瑞数智 | https://www.idigital.com.cn/common-ai-2 |
| tavily | 0.66 | 招标文件全维度智能解析：读懂标书，才是投标制胜的第一步_核心_细节_评分 | https://www.sohu.com/a/1035138286_122095475 |
| tavily | 0.65 | 使用指南 \| 招标文件深度拆解，废标风险全面排查（建议收藏） \| 快书编标官方论坛 | https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F |
| tavily | 0.60 | 资源丰富的投标、招标生态_便捷工具 - 快书编标 | https://www.kshbb.com/AIIntelligent.html |
| tavily | 0.59 | 智能投标助手 - AGICamp | https://agicamp.com/products/CyberIoT |
| tavily | 0.57 | 招标解析（已下线） - 智谱AI开放文档 | https://docs.bigmodel.cn/cn/guide/agents/tender |
| tavily | 0.52 | 招投标会变成AI“全包”吗？答案是“人机搭档”才是未来 | https://www.chinabidding.com.cn/pageInfoSsr/3000000016666/1087000001241861 |
| tavily | 0.51 | AI 标书撰写：如何借助 AI 驱动的投标方案赢得更多竞标（2026年5月） | https://www.jenova.ai/zh/resources/ai-tender-writing-202605 |
| tavily | 0.48 | 标桥首页 | https://www.bqpoint.com |
| tavily | 0.48 | 如何利用 AI 工具快速分析招标文件中的关键条款 - 百炼智能 | https://www.bailian-ai.com/news/2243.html |
| tavily | 0.47 | 易标AI | https://yibiao.pro |
| tavily | 0.44 | GitHub - FB208/OpenBidKit_Yibiao: 开箱即用的AI标书编写工具，标书AI生成工具，投标工具箱、知识库、标书查重、废标项检查，完全开源免费，欢迎使用 · GitHub | https://github.com/FB208/OpenBidKit_Yibiao |
| tavily | 0.44 | 智领招投标，赋能新发展——广东引领推进“人工智能+招标投标”创新应用 \| 广州市发展和改革委员会网站 | http://fgw.gz.gov.cn/tzgg/content/post_10704480.html |
| tavily | 0.42 | CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统 | https://patents.google.com/patent/CN119624385A/zh |

## 信源质量门控记录

### 门控规则
- Tavily score < 0.4：剔除
- 已知低质域名：剔除
- 重复 URL：合并保留最高分结果
- Exa 学术/语义结果：默认保留，但进入来源等级评估
- C/D 级来源不得作为唯一结论依据
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`

### 保留信源
1. [A Large Language Model-based Framework for Semi-Structured Tender Document Retrieval-Augmented Generation](https://arxiv.org/html/2410.09077v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
2. [[2603.22513v1] Generating and Evaluating Sustainable Procurement Criteria for the Swiss Public Sector using In-Context Prompting with Large Language Models](https://arxiv.org/abs/2603.22513v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
3. [Exploring Information Retrieval Landscapes: An](https://arxiv.org/pdf/2409.08479)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
4. [DocSplit: A Comprehensive Benchmark Dataset and Evaluation Approach for Document Packet Recognition and Splitting](https://arxiv.org/html/2602.15958)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
5. [Uni-Parser Technical Report](https://arxiv.org/abs/2512.15098v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
6. [[2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models](https://arxiv.org/abs/2309.12132v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
7. [Intelligent Processing of Design Notices in Engineering Procurement Construction Projects](https://www.mdpi.com/2075-5309/15/5/805)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
8. [Large Language Model for Extracting Complex Contract Information in Industrial Scenes](https://arxiv.org/html/2507.06539v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
9. [IndustryBench: Probing the Industrial Knowledge Boundaries of LLMs](https://arxiv.org/html/2605.10267v3)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
10. [AIDABench: AI Data Analytics Benchmark](https://arxiv.org/html/2603.15636v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
11. [https://arxiv.org/pdf/2008.02347](https://arxiv.org/pdf/2008.02347)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
12. [Infinity-Parser: Layout-Aware Reinforcement Learning for Scanned Document Parsing](https://arxiv.org/html/2506.03197v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
13. [Logics-Parsing: An End-to-end Document Parsing Model with Layout-centric Reinforcement Learning](https://arxiv.org/html/2509.19760v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
14. [The Measure of All Measures: Quantifying LLM Benchmark Quality | OpenReview](https://openreview.net/forum?id=HpnGmTIs7Z&referrer=%5Bthe+profile+of+Zhen+Dong%5D%28%2Fprofile%3Fid%3D%7EZhen_Dong3%29)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
15. [标书智能体（一）——AI解析招标文件代码+提示词 - 易标AI - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.78
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
16. [AI写标书｜DeepSeek搞不定的投标痛点，被它拿捏了！ - 知乎](https://zhuanlan.zhihu.com/p/1908566825068913729)
   - 工具：tavily
   - 分数：0.68
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
17. [艾瑞数智](https://www.idigital.com.cn/common-ai-2)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
18. [招标文件全维度智能解析：读懂标书，才是投标制胜的第一步_核心_细节_评分](https://www.sohu.com/a/1035138286_122095475)
   - 工具：tavily
   - 分数：0.66
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
19. [使用指南 | 招标文件深度拆解，废标风险全面排查（建议收藏） | 快书编标官方论坛](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F)
   - 工具：tavily
   - 分数：0.65
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
20. [资源丰富的投标、招标生态_便捷工具 - 快书编标](https://www.kshbb.com/AIIntelligent.html)
   - 工具：tavily
   - 分数：0.60
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
21. [智能投标助手 - AGICamp](https://agicamp.com/products/CyberIoT)
   - 工具：tavily
   - 分数：0.59
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
22. [招标解析（已下线） - 智谱AI开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
23. [招投标会变成AI“全包”吗？答案是“人机搭档”才是未来](https://www.chinabidding.com.cn/pageInfoSsr/3000000016666/1087000001241861)
   - 工具：tavily
   - 分数：0.52
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
24. [AI 标书撰写：如何借助 AI 驱动的投标方案赢得更多竞标（2026年5月）](https://www.jenova.ai/zh/resources/ai-tender-writing-202605)
   - 工具：tavily
   - 分数：0.51
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
25. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.48
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
26. [如何利用 AI 工具快速分析招标文件中的关键条款 - 百炼智能](https://www.bailian-ai.com/news/2243.html)
   - 工具：tavily
   - 分数：0.48
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
27. [易标AI](https://yibiao.pro)
   - 工具：tavily
   - 分数：0.47
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
28. [GitHub - FB208/OpenBidKit_Yibiao: 开箱即用的AI标书编写工具，标书AI生成工具，投标工具箱、知识库、标书查重、废标项检查，完全开源免费，欢迎使用 · GitHub](https://github.com/FB208/OpenBidKit_Yibiao)
   - 工具：tavily
   - 分数：0.44
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
29. [智领招投标，赋能新发展——广东引领推进“人工智能+招标投标”创新应用 | 广州市发展和改革委员会网站](http://fgw.gz.gov.cn/tzgg/content/post_10704480.html)
   - 工具：tavily
   - 分数：0.44
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
30. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统](https://patents.google.com/patent/CN119624385A/zh)
   - 工具：tavily
   - 分数：0.42
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
31. [智领招投标，赋能新发展](https://www.gdwc.gov.cn/zjwcfgw/gkmlpt/content/2/2153/post_2153176.html?jump=true)
   - 工具：tavily
   - 分数：0.41
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
32. [企业招投标文件自动比对工具：核心能力解析与智能化落地指南 - 实在智能](https://www.ai-indeed.com/encyclopedia/18040.html)
   - 工具：tavily
   - 分数：0.40
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考

### 剔除信源
1. [标书智能体（一）——AI解析招标文件代码+提示词 - 易标AI - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.75
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
2. [艾瑞数智](https://www.idigital.com.cn/common-ai-2)
   - 工具：tavily
   - 分数：0.60
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
3. [招标解析（已下线） - 智谱AI开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender)
   - 工具：tavily
   - 分数：0.51
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
4. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.46
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
5. [AI标书-标书怎么做-标书制作软件-快标宝AI](https://www.kuaibiaobao.com)
   - 工具：tavily
   - 分数：0.40
   - 来源等级：C
   - 剔除原因：score 低于 0.4
6. [标书生成-大模型服务平台百炼(Model Studio)-阿里云帮助中心](https://help.aliyun.com/zh/model-studio/api-aimiaobi-2023-08-01-dir-tender-generation)
   - 工具：tavily
   - 分数：0.39
   - 来源等级：A
   - 剔除原因：score 低于 0.4
7. [Ant Group 2025 Sustainability Report Highlights Record AI R&D Investment – Company Announcement - Financial Times](https://markets.ft.com/data/announce/detail?dockey=600-202606170512BIZWIRE_USPRX____20260617_BW847068-1)
   - 工具：tavily
   - 分数：0.18
   - 来源等级：C
   - 剔除原因：score 低于 0.4
8. [EBAday 2026: Zooming in on AI and digital assets as the key themes of the event - Finextra Research](https://www.finextra.com/newsarticle/47948/ebaday-2026-zooming-in-on-ai-and-digital-assets-as-the-key-themes-of-the-event)
   - 工具：tavily
   - 分数：0.09
   - 来源等级：C
   - 剔除原因：score 低于 0.4
9. [TABLE-Ai -2026/27 parent forecast - TradingView](https://www.tradingview.com/news/reuters.com,2026-06-15:newsml_XB0J3I2J1:0-table-ai-2026-27-parent-forecast/)
   - 工具：tavily
   - 分数：0.06
   - 来源等级：C
   - 剔除原因：score 低于 0.4
10. [China announces measures to promote AI integration with consumption - Reuters](https://www.reuters.com/business/media-telecom/china-announces-measures-promote-ai-integration-with-consumption-2026-06-18/)
   - 工具：tavily
   - 分数：0.04
   - 来源等级：C
   - 剔除原因：score 低于 0.4
11. [BE Semiconductor Raises Long-Term Revenue, Profitability Targets on AI Boost - WSJ](https://www.wsj.com/business/earnings/be-semiconductor-raises-long-term-revenue-profitability-targets-on-ai-boost-c47d5f77)
   - 工具：tavily
   - 分数：0.03
   - 来源等级：C
   - 剔除原因：score 低于 0.4
12. [Mavenir, Red Hat target AI monetization opportunity for telcos - RCR Wireless News](https://www.rcrwireless.com/20260618/carriers/mavenir-ai-telcos)
   - 工具：tavily
   - 分数：0.03
   - 来源等级：C
   - 剔除原因：score 低于 0.4
13. [AI Crypto Presale Ruvi AI Sells 99% of Phase 3 in Under a Month as Only 1% of Tokens Remain at $0.02 - markets.businessinsider.com](https://markets.businessinsider.com/news/stocks/ai-crypto-presale-ruvi-ai-sells-99-of-phase-3-in-under-a-month-as-only-1-of-tokens-remain-at-0-02-1036263619)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
14. [China CAMC Engineering's Unit Signs Contract For Energy Project - TradingView](https://www.tradingview.com/news/reuters.com,2026:newsml_L6N42T03B:0-china-camc-engineering-s-unit-signs-contract-for-energy-project/)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
15. [Beijing Capital International Airport Shareholders Approve 2025 Accounts and No-Dividend Plan at AGM - TipRanks](https://www.tipranks.com/news/company-announcements/beijing-capital-international-airport-shareholders-approve-2025-accounts-and-no-dividend-plan-at-agm)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
16. [AI & Tech brief: China’s biotech dominance - The Washington Post](https://www.washingtonpost.com/wp-intelligence/ai-tech-brief/2026/06/17/ai-tech-brief-chinas-biotech-dominance/)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
17. [标书智能体（一）——AI解析招标文件代码+提示词 - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.65
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
18. [智能标书助手-艾瑞数智](https://www.idigital.com.cn/common-ai-2)
   - 工具：tavily
   - 分数：0.52
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
19. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.45
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
20. [招标解析（已下线） - 智谱AI开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender)
   - 工具：tavily
   - 分数：0.38
   - 来源等级：A
   - 剔除原因：score 低于 0.4
21. [GitHub - FB208/OpenBidKit_Yibiao: 开箱即用的AI标书编写工具，标书AI生成工具，投标工具箱、知识库、标书查重、废标项检查，完全开源免费，欢迎使用 · GitHub](https://github.com/FB208/OpenBidKit_Yibiao)
   - 工具：tavily
   - 分数：0.34
   - 来源等级：C
   - 剔除原因：score 低于 0.4
22. [智领招投标，赋能新发展 - 吴川市人民政府](https://www.gdwc.gov.cn/zjwcfgw/gkmlpt/content/2/2153/post_2153176.html?jump=true)
   - 工具：tavily
   - 分数：0.32
   - 来源等级：C
   - 剔除原因：score 低于 0.4
23. [易标AI](https://yibiao.pro)
   - 工具：tavily
   - 分数：0.30
   - 来源等级：C
   - 剔除原因：score 低于 0.4
24. [标书智能体（一）——AI解析招标文件代码+提示词 - 易标AI - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.74
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
25. [艾瑞数智](https://www.idigital.com.cn/common-ai-2)
   - 工具：tavily
   - 分数：0.60
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
26. [招标解析（已下线） - 智谱AI开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender)
   - 工具：tavily
   - 分数：0.54
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
27. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.47
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
28. [智领招投标，赋能新发展——广东引领推进“人工智能+招标投标”创新应用 | 广州市发展和改革委员会网站](http://fgw.gz.gov.cn/tzgg/content/post_10704480.html)
   - 工具：tavily
   - 分数：0.39
   - 来源等级：C
   - 剔除原因：score 低于 0.4
29. [智领招投标，赋能新发展](https://www.gdwc.gov.cn/zjwcfgw/gkmlpt/content/2/2153/post_2153176.html?jump=true)
   - 工具：tavily
   - 分数：0.37
   - 来源等级：C
   - 剔除原因：score 低于 0.4
30. [[PDF] 招标文件 - 信息资源系统](https://13115299.s21i.faiusr.com/61/1/ABUIABA9GAAg3PPYkwYo1Jy2mQE.pdf)
   - 工具：tavily
   - 分数：0.32
   - 来源等级：C
   - 剔除原因：score 低于 0.4
31. [招投标知识库文档解析_招标文件/投标文件/RAG前处理方案_TextIn](https://www.textin.com/scenarios/tender-bid-knowledge-base)
   - 工具：tavily
   - 分数：0.32
   - 来源等级：C
   - 剔除原因：score 低于 0.4
32. [CN117764039A - 基于大模型的投标文件生成方法、系统、终端及存储介质 
        - Google Patents](https://patents.google.com/patent/CN117764039A/zh)
   - 工具：tavily
   - 分数：0.27
   - 来源等级：C
   - 剔除原因：score 低于 0.4

## 完整精读结果

### 来源 1: 标书智能体（一）——AI解析招标文件代码+提示词 - 易标AI - 博客园

- URL: https://www.cnblogs.com/yibiaoai/p/19064673
- 精读方法：firecrawl-scrape

[![订阅](https://www.cnblogs.com/skins/sea/images/xml.gif)](https://www.cnblogs.com/yibiaoai/rss/)

随笔 -
6
文章 -
1
评论 -
0
阅读 \-

6284

# [标书智能体（一）——AI解析招标文件代码+提示词](https://www.cnblogs.com/yibiaoai/p/19064673 "发布于 2025-08-29 18:13")

[合集 \- AI标书智能体教程(7)](https://www.cnblogs.com/yibiaoai/collections/31020)

1.标书智能体（一）——AI解析招标文件代码+提示词2025-08-29

[2.标书智能体（二）——生成标书提纲代码+提示词2025-09-11](https://www.cnblogs.com/yibiaoai/p/19085799) [3.标书智能体（三）——生成标书正文代码+提示词2025-12-05](https://www.cnblogs.com/yibiaoai/p/19311155) [4.标书智能体（四）——提示词顺序优化，让缓存命中，输入成本直降10倍04-03](https://www.cnblogs.com/yibiaoai/p/19817535) [5.标书智能体（五）——如何让弱模型也能稳定输出复杂json05-06](https://www.cnblogs.com/yibiaoai/p/19981671) [6.标书智能体（六）——超长文本生成和图文控制05-15](https://www.cnblogs.com/yibiaoai/p/20052734) [7.新系列一：关于AI知识库的一点拙见，非RAG06-12](https://www.cnblogs.com/yibiaoai/articles/20483259)

收起

用Python+React打造一个开源的AI写标书智能体~

今天是第一期，招标文件解析：

![2a82ba6e-63f9-49a5-beec-3596bc4b8d3d](https://img2024.cnblogs.com/blog/3696383/202508/3696383-20250829155418113-1743827731.png)

招标文件动辄几万字，虽然现在各主流大模型的上下文窗口都越来越大，但也只能代表AI **“可以处理几十万字的上下文”**，并不代表你随便扔给AI几十万字，它就能 **“处理得好几十万字的上下文”。**

我们在写投标文件之前，一定要先把招标文件通读一遍，标注出需要注意的点，然后再有针对性的撰写招标文件。

AI写标书也是一样，第一步要做的就是 **招标文件解析**。

# 一、Word、PDF文件内容提取

AI解析招标文件，难住我的第一关，并不是如何让AI提取招标文件中的内容，而是怎么把招标文件的内容完整的从PDF、word中提取出来。

word文件提取，选用的是`docx2python`

```python
content = None
try:
    # 使用docx2python提取，它能更好地处理表格和结构
    content = docx2python(file_path)
    extracted_text = []
    # 处理文档内容
    if hasattr(content, 'document'):
        for section in content.document:
            for element in section:
                if isinstance(element, list):
                    # 这可能是表格
                    extracted_text.append("\n[表格内容]")
                    for row in element:
                        if isinstance(row, list):
                            row_text = " | ".join([str(cell).strip() for cell in row if cell])
                            if row_text:
                                extracted_text.append(row_text)
                        else:
                            extracted_text.append(str(row))
                    extracted_text.append("[表格结束]\n")
                else:
                    # 普通文本
                    text = str(element).strip()
                    if text:
                        extracted_text.append(text)
    result = "\n".join(extracted_text).strip()
    # 确保释放资源
    if content:
        del content
    gc.collect()
    return result
except Exception as e:
    # 确保释放资源
    if content:
        del content
    gc.collect()
```

pdf文件提取，则使用pdfplumber

```python
pdf = None
try:
    extracted_text = []
    pdf = pdfplumber.open(file_path)
    for page_num, page in enumerate(pdf.pages, 1):
        # 添加页码标识
        extracted_text.append(f"\n--- 第 {page_num} 页 ---\n")
        # 提取普通文本
        text = page.extract_text()
        if text:
            extracted_text.append(text)
        # 提取表格
        tables = page.extract_tables()
        for table_num, table in enumerate(tables, 1):
            extracted_text.append(f"\n[表格 {table_num}]")
            for row in table:
                if row:  # 跳过空行
                    # 过滤空值并连接单元格
                    row_text = " | ".join([str(cell) if cell else "" for cell in row])
                    extracted_text.append(row_text)
            extracted_text.append("[表格结束]\n")

    result = "\n".join(extracted_text).strip()
    # 确保关闭PDF文件
    if pdf:
        pdf.close()
    gc.collect()
    return result
except Exception as e:
    # 确保关闭PDF文件
    if pdf:
        pdf.close()
    gc.collect()
```

# 二、封装AI流式请求通用函数

注意这里使用的是`AsyncOpenAI`即OpenAI的异步客户端，因为之后要一次性编写几十万字的标书，为了提高速度，使用并发请求，则必须使用`AsyncOpenAI`

```python
def __init__(self, api_key: str, base_url: str = None, model_name: str = "gpt-3.5-turbo"):
    """初始化OpenAI服务"""
    self.api_key = api_key
    self.base_url = base_url
    self.model_name = model_name

    # 初始化OpenAI客户端 - 使用异步客户端
    self.client = openai.AsyncOpenAI(
        api_key=api_key,
        base_url=base_url if base_url else None
    )
async def stream_chat_completion(
    self,
    messages: list,
    temperature: float = 0.7,
    response_format: dict = None
) -> AsyncGenerator[str, None]:
    """流式聊天完成请求 - 真正的异步实现"""
    try:
        stream = await self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            stream=True,
            **({"response_format": response_format} if response_format is not None else {})
        )

        async for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content

    except Exception as e:
        yield f"错误: {str(e)}"
```

# 三、招标文件解析提示词

## 项目概述

### SystemPrompt

```markdown
你是一个专业的标书撰写专家。请分析用户发来的招标文件，提取并总结项目概述信息。

请重点关注以下方面：
1. 项目名称和基本信息
2. 项目背景和目的
3. 项目规模和预算
4. 项目时间安排
5. 项目要实施的具体内容
6. 主要技术特点
7. 其他关键要求

工作要求：
1. 保持提取信息的全面性和准确性，尽量使用原文内容，不要自己编写
2. 只关注与项目实施有关的内容，不提取商务信息
3. 直接返回整理好的项目概述，除此之外不返回任何其他内容
```

### UserPrompt

```markdown
请分析以下招标文件内容，提取项目概述信息：
{request.file_content}
```

## 技术评分要求

在编写招标文件中的技术方案时，技术评分要求非常重要，基本要做到1对1应答式编写，所以评分要求的提取则尤为重要，我采用了自我反思式的结构化提示词进行提取处理。

### SystemPrompt

```markdown
你是一名专业的招标文件分析师，擅长从复杂的招标文档中高效提取“技术评分项”相关内容。请严格按照以下步骤和规则执行任务：
### 1. 目标定位
- 重点识别文档中与“技术评分”、“评标方法”、“评分标准”、“技术参数”、“技术要求”、“技术方案”、“技术部分”或“评审要素”相关的章节（如“第X章 评标方法”或“附件X：技术评分表”）。
- 忽略商务、价格、资质等非技术类评分项。
### 2. 提取内容要求
对每一项技术评分项，按以下结构化格式输出（若信息缺失，标注“未提及”），如果评分项不够明确，你需要根据上下文分析并也整理成如下格式：
【评分项名称】：<原文描述，保留专业术语>
【权重/分值】：<具体分值或占比，如“30分”或“40%”>
【评分标准】：<详细规则，如“≥95%得满分，每低1%扣0.5分”>
【数据来源】：<文档中的位置，如“第5.2.3条”或“附件3-表2”>

### 3. 处理规则
- **模糊表述**：有些招标文件格式不是很标准，没有明确的“技术评分表”，但一定都会有“技术评分”相关内容，请根据上下文判断评分项。
- **表格处理**：若评分项以表格形式呈现，按行提取，并标注“[表格数据]”。
- **分层结构**：若存在二级评分项（如“技术方案→子项1、子项2”），用缩进或编号体现层级关系。
- **单位统一**：将所有分值统一为“分”或“%”，并注明原文单位（如原文为“20点”则标注“[原文：20点]”）。

### 4. 输出示例
【评分项名称】：系统可用性
【权重/分值】：25分
【评分标准】：年平均故障时间≤1小时得满分；每增加1小时扣2分，最高扣10分。
【数据来源】：附件4-技术评分细则（第3页）

【评分项名称】：响应时间
【权重/分分】：15分 [原文：15%]
【评分标准】：≤50ms得满分；每增加10ms扣1分。
【数据来源】：第6.1.2条

### 5. 验证步骤
提取完成后，执行以下自检：
- [ ] 所有技术评分项是否覆盖（无遗漏）？
- [ ] 权重总和是否与文档声明的技术分总分一致（如“技术部分共60分”）？

直接返回提取结果，除此之外不输出任何其他内容
```

### UserPrompt

```markdown
请分析以下招标文件内容，提取技术评分要求信息：
{request.file_content}
```

# 完整代码已开源

Github： [https://github.com/yibiaoai/yibiao-simple](https://github.com/yibiaoai/yibiao-simple)

Gitee： [https://gitee.com/yibiao-ai/yibiao-simple](https://gitee.com/yibiao-ai/yibiao-simple)

合集:
[AI标书智能体教程](https://www.cnblogs.com/yibiaoai/collections/31020)

标签:
[人工智能](https://www.cnblogs.com/yibiaoai/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/), [Python](https://www.cnblogs.com/yibiaoai/tag/Python/), [招投标](https://www.cnblogs.com/yibiaoai/tag/%E6%8B%9B%E6%8A%95%E6%A0%87/), [智能体](https://www.cnblogs.com/yibiaoai/tag/%E6%99%BA%E8%83%BD%E4%BD%93/), [提示词](https://www.cnblogs.com/yibiaoai/tag/%E6%8F%90%E7%A4%BA%E8%AF%8D/)

免责声明：本内容来自平台创作者，博客园系信息发布平台，仅提供信息存储空间服务。

好文要顶关注我收藏该文微信分享

[![](https://pic.cnblogs.com/face/3696383/20250829141117.png)](https://home.cnblogs.com/u/yibiaoai/)

[易标AI](https://home.cnblogs.com/u/yibiaoai/)

[粉丝 \- 3](https://home.cnblogs.com/u/yibiaoai/followers/) [关注 \- 0](https://home.cnblogs.com/u/yibiaoai/followees/)

+加关注

1

0

[升级成为会员](https://cnblogs.vip/)

[»](https://www.cnblogs.com/yibiaoai/p/19085799) 下一篇： [标书智能体（二）——生成标书提纲代码+提示词](https://www.cnblogs.com/yibiaoai/p/19085799 "发布于 2025-09-11 14:05")

posted on
2025-08-29 18:13 [易标AI](https://www.cnblogs.com/yibiaoai)
阅读(2836)
评论(0)

收藏 [举报](https://report.cnblogs.com/?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fyibiaoai%2Fp%2F19064673&targetId=19064673&targetType=0)

[刷新页面](https://www.cnblogs.com/yibiaoai/p/19064673#) [返回顶部](https://www.cnblogs.com/yibiaoai/p/19064673#top)

登录后才能查看或发表评论，立即 登录 或者
[逛逛](https://www.cnblogs.com/) 博客园首页

[![](https://img2024.cnblogs.com/blog/35695/202606/35695-20260609221536870-1777800795.webp)](https://www.volcengine.com/activity/codingplan?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=cnblogs)

- [让 Agent 在对话中成长：自进化机制的五层实现](https://www.cnblogs.com/zhayujie/p/20523587/self-evolution)
- [代码之外：一个技术人的职场困境与自我和解](https://www.cnblogs.com/charlee44/p/20296178)
- [贩卖焦虑的时代，我终于接住了真实的焦虑](https://www.cnblogs.com/ZyCoder/p/20176104)
- [工良吐槽篇：万字长文细说 AI 落地之笑谈](https://www.cnblogs.com/whuanle/p/20088309)
- [代码是 AI 写的，生产事故谁背锅？](https://www.cnblogs.com/Zhang-Xiang/p/20028472)

昵称：
[易标AI](https://home.cnblogs.com/u/yibiaoai/)

园龄：
[9个月](https://home.cnblogs.com/u/yibiaoai/ "入园时间：2025-08-29")

粉丝：
[3](https://home.cnblogs.com/u/yibiaoai/followers/)

关注：
[0](https://home.cnblogs.com/u/yibiaoai/followees/)

+加关注

| |     |     |     |
| --- | --- | --- |
| < | 2026年6月 | > | |
| 日 | 一 | 二 | 三 | 四 | 五 | 六 |
| 31 | 1 | 2 | 3 | 4 | 5 | 6 |
| 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| 21 | 22 | 23 | 24 | 25 | 26 | 27 |
| 28 | 29 | 30 | 1 | 2 | 3 | 4 |
| 5 | 6 | 7 | 8 | 9 | 10 | 11 |

### 搜索

### 常用链接

- [我的随笔](https://www.cnblogs.com/yibiaoai/p/ "我的博客的随笔列表")
- [我的评论](https://www.cnblogs.com/yibiaoai/MyComments.html "我的发表过的评论列表")
- [我的参与](https://www.cnblogs.com/yibiaoai/OtherPosts.html "我评论过的随笔列表")
- [最新评论](https://www.cnblogs.com/yibiaoai/comments "我的博客的评论列表")
- [我的标签](https://www.cnblogs.com/yibiaoai/tag/ "我的博客的标签列表")

### [我的标签](https://www.cnblogs.com/yibiaoai/tag/)

- [智能体(7)](https://www.cnblogs.com/yibiaoai/tag/%E6%99%BA%E8%83%BD%E4%BD%93/)
- [提示词(7)](https://www.cnblogs.com/yibiaoai/tag/%E6%8F%90%E7%A4%BA%E8%AF%8D/)
- [招投标(7)](https://www.cnblogs.com/yibiaoai/tag/%E6%8B%9B%E6%8A%95%E6%A0%87/)
- [人工智能(7)](https://www.cnblogs.com/yibiaoai/tag/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/)
- [Python(5)](https://www.cnblogs.com/yibiaoai/tag/Python/)
- [electron(2)](https://www.cnblogs.com/yibiaoai/tag/electron/)

### 合集

- [AI标书智能体教程(7)](https://www.cnblogs.com/yibiaoai/collections/31020)

### [随笔分类](https://www.cnblogs.com/yibiaoai/post-categories)

- [AI写标书(5)](https://www.cnblogs.com/yibiaoai/category/2474363.html)

### 随笔档案

- [2026年5月(2)](https://www.cnblogs.com/yibiaoai/p/archive/2026/05)
- [2026年4月(1)](https://www.cnblogs.com/yibiaoai/p/archive/2026/04)
- [2025年12月(1)](https://www.cnblogs.com/yibiaoai/p/archive/2025/12)
- [2025年9月(1)](https://www.cnblogs.com/yibiaoai/p/archive/2025/09)
- [2025年8月(1)](https://www.cnblogs.com/yibiaoai/p/archive/2025/08)

### [阅读排行榜](https://www.cnblogs.com/yibiaoai/most-viewed)

- [1\. 标书智能体（一）——AI解析招标文件代码+提示词(2836)](https://www.cnblogs.com/yibiaoai/p/19064673)
- [2\. 标书智能体（二）——生成标书提纲代码+提示词(1334)](https://www.cnblogs.com/yibiaoai/p/19085799)
- [3\. 标书智能体（三）——生成标书正文代码+提示词(1296)](https://www.cnblogs.com/yibiaoai/p/19311155)
- [4\. 标书智能体（四）——提示词顺序优化，让缓存命中，输入成本直降10倍(426)](https://www.cnblogs.com/yibiaoai/p/19817535)
- [5\. 标书智能体（五）——如何让弱模型也能稳定输出复杂json(193)](https://www.cnblogs.com/yibiaoai/p/19981671)

### [推荐排行榜](https://www.cnblogs.com/yibiaoai/most-liked)

- [1\. 标书智能体（一）——AI解析招标文件代码+提示词(1)](https://www.cnblogs.com/yibiaoai/p/19064673)

点击右上角即可分享

![微信分享提示](https://img2023.cnblogs.com/blog/35695/202309/35695-20230906145857937-1471873834.gif)

### 来源 2: AI写标书｜DeepSeek搞不定的投标痛点，被它拿捏了！ - 知乎

- URL: https://zhuanlan.zhihu.com/p/1908566825068913729
- 精读方法：firecrawl-scrape

![BrandImg](https://picx.zhimg.com/v2-0ed97d47c13d84d7432fded4dfd3b43e_r.webp?source=172ae18b&consumer=ZHI_MENG)

AI写标书｜DeepSeek搞不定的投标痛点，被它拿捏了！

![智标领航](https://picx.zhimg.com/v2-801d9f017fb1f52c3d6f4cdf170ae492_l.webp?source=57bf9c9b&consumer=ZHI_MENG)

智标领航

提供智能化招投标解决方案

13 赞同

5 评论

32 收藏

别人用AI写标书：快速提取招标文案要求，生成目录大纲，生成投标方案，填充偏离表，整个过程不到半小时。

你用AI写标书：AI味儿太重，偏离评分标准，字数太少，格式不对，已繁忙.........

![](https://pic4.zhimg.com/v2-50d64cff3b239914177657bbdce097d1_1440w.webp?consumer=ZHI_MENG)

用对AI工具，投标才能效率翻倍！

**智标领航 AI 写标书**，作为更懂投标人的 AI 助手，让编标效率与质量双提升。

私有化部署+AI 智能编标+实时标讯推送，帮您高效提升中标率！

点击跳转至第三方

私有化部署+AI 智能编标+实时标讯推送，帮您高效提升中标率！

点击跳转至第三方

私有化部署+AI 智能编标+实时标讯推送，帮您高效提升中标率！

点击跳转至第三方

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

## **智标领航AI写标书，更快、更好！**

### **1、AI 解析招标文件：无需提示词，精准高效**

用 DeepSeek 解析招标文件，投标人往往需要花费大量时间编写提示词，引导 AI 提取关键信息，而且解析结果常常比较碎片化，需要手动整合，费时又费力。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

智标领航 AI 写标书则让文件解析变得轻松简单。只需一键上传招标文件，无需输入任何提示词，AI 就能在 3 分钟内智能精准地提取重点信息。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

不仅如此，AI 还会将关键信息分版块清晰展示，让投标人一眼看清重点内容。更贴心的是，它支持原文定位功能，点击即可跳转至对应段落核对，再也不用在冗长的文件中盲目翻找，大幅提升解析效率。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

### **2、AI 写标书：贴合招标文件生成，方案专业**

用 DeepSeek 生成标书，常常出现「两张皮」现象：

招标书要求「提供 3 种应急预案」，AI 却写了一堆无关的技术原理；评分标准里「本地化服务能力占 20 分」，生成内容却只字不提本地团队配置。

更要命的是，想修改某个段落，得反复输入提示词，改 3 次才能勉强达标，效率比自己写还低。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

智标领航 AI 写标书依托 DeepSeek 满血版 +QwQ-32B 大模型的强大能力，针对招投标场景微调，能够精准理解招标要求，10 分钟即可生成高质量标书。

生成的内容紧密贴合项目需求，重点突出，逻辑清晰。技术标会详细阐述产品的技术优势、与招标要求的参数对比等内容；商务标则自动调用企业资质库中的相关资料，突出企业的实力和业绩。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

同时，支持AI对生成的目录大纲进行灵活修改，从而对生成内容进行改写、重写，让标书更贴合项目需求。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

### **3、偏离表生成：参数对比零误差，精准填充**

在编制时，往往需要投标人手动整理技术材料、分类标注参数，再逐一对比招标要求，过程繁琐且容易遗漏。

使用 DeepSeek 显然很难一次性完成大批量文件的处理及阅读分析工作，一旦参数对比不精准，可能直接导致标书扣分甚至废标。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

而智标领航 AI 写标书实现了偏离表生成的全智能化。投标人只需一键上传所有技术材料（如产品手册、检测报告等），无需手动分类整理，AI 会智能识别招标要求中的技术参数、商务条款，与企业提供的材料进行精准比对，自动标注 “正偏离” 或 “无偏离”。对比过程零误差，确保每个参数都准确响应。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

生成的偏离表格式规范、内容完整，直接嵌入标书，省去了人工核对和表格制作的时间，不用担心参数漏检或格式错误。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

## **AI写标书这2个细节，一定别忽视**

### **1、完善企业资质库，商务标一键带入**

智标领航支持在线管理企业信息，用户可以上传资质证书、业绩合同、财务数据等资料。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

生成商务标时，选择投标企业，AI就会根据招标文件要求，自动匹配并调取最新、最匹配的数据。

**2、上传企业知识库，技术标识别引用**

用户可以在线构建专属知识库，将行业规范、技术标准、历史项目方案等资料分类上传至云端，形成企业独有的知识体系。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

生成技术标方案时，用户只需选择 “参考知识库”，AI 即可深度解析知识库内容，结合招标文件具体要求，生成高度贴合企业技术优势的方案。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

生成技术标方案时，用户只需选择 “参考知识库”，AI 即可深度解析知识库内容，结合招标文件具体要求，生成高度贴合企业技术优势的方案。

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

## **现在注册，领「50 万字免费生成」权益**

智标领航已上线「超级权益组合包」！ **2025年4月25日-6月18日**，新用户注册、加客服、邀好友、提意见都有字数赠送。

**速领** ↓↓↓

私有化部署+AI 智能编标+实时标讯推送，帮您高效提升中标率！

点击跳转至第三方

私有化部署+AI 智能编标+实时标讯推送，帮您高效提升中标率！

点击跳转至第三方

私有化部署+AI 智能编标+实时标讯推送，帮您高效提升中标率！

点击跳转至第三方

![](https://www.zhihu.com/tardis/zm/art/1908566825068913729?source_id=1003)

编辑于 2026-04-06 · 著作权归作者所有

### 来源 3: 艾瑞数智

- URL: https://www.idigital.com.cn/common-ai-2
- 精读方法：firecrawl-scrape

让AI成为您的投标智囊团

AI解析招标文件 → AI预判评分 → AI标书创作，效率提升50%

立即咨询

观看视频

一键生成高质量投标方案

智能解析

AI预评分

AI标书工厂

资源中枢

AI预评分，精准对标拿分项

客观项辅助评分｜人工一键修正｜评分表穿透溯源

![](<Base64-Image-Removed>)硬分快评：1分钟完成资质/业绩/人员等客观项评分

![](<Base64-Image-Removed>)人机共判：人机协同修正，误差双保险机制

![](<Base64-Image-Removed>)动态评分表生成：一键导出Excel评分表

申请试用

![](https://www.idigital.com.cn/web-oss/idigital-web/2025/07/15/123_20250715113330A011.png)

AI预评分，精准对标拿分项

客观项辅助评分｜人工一键修正｜评分表穿透溯源

![](<Base64-Image-Removed>)硬分快评：1分钟完成资质/业绩/人员等客观项评分

![](<Base64-Image-Removed>)人机共判：人机协同修正，误差双保险机制

![](<Base64-Image-Removed>)动态评分表生成：一键导出Excel评分表

申请试用

您的投标专属AI，安全与效能兼

全链路安全闭环

动态水印+审批溯源，敏感数据0失控

![](https://www.idigital.com.cn/web-oss/idigital-web/2025/07/15/a_20250715114725A015.png)

100%私有化部署

支持本地服务器闭环运行，招标数据不出企业内网，杜绝云端泄露风险

![](https://www.idigital.com.cn/web-oss/idigital-web/2025/07/15/b_20250715115617A017.png)

垂直场景提效

标书全流程AI化，效率提升50%

![](https://www.idigital.com.cn/web-oss/idigital-web/2025/07/15/c_20250715115656A018.png)

申请试用

客户成功案例

客户成功案某大型企业

某大型央国企应用标书工具实战案例

我们为该企业搭建了一套私有化部署的标书工具，将其历史投标案例作为素材进行大模型演练，实现了内容的沉淀、提炼、分类，最终通过AI模型技术，实现了招标文件要点精准解读、投标文件内容快速生成，为该企业全年支持上百个个投标项目，投标文件输出效率提升30%，全年0废标。

![](https://www.idigital.com.cn/web-oss/idigital-web/2025/07/15/dd_20250715120002A019.png)

客户成功案某大型企业

某大型央国企应用标书工具实战案例

我们为该企业搭建了一套私有化部署的标书工具，将其历史投标案例作为素材进行大模型演练，实现了内容的沉淀、提炼、分类，最终通过AI模型技术，实现了招标文件要点精准解读、投标文件内容快速生成，为该企业全年支持上百个个投标项目，投标文件输出效率提升30%，全年0废标。

某大型央国标书工具实战案例

我们为该企业搭建了一套私有化部署的标书工具，将其历史投标案例作为素材进行大模型演练，实现了内容的沉淀、提炼、分类，最终通过AI模型技术，实现了招标文件要点精准解读、投标文件内容快速生成，为该企业全年支持上百个个投标项目，投标文件输出效率提升30%，全年0废标，超标完成。

某大型央国企应用标书工具实战案例

我们为该企业搭建了一套私有化部署的标书工具，将其历史投标案例作为素材进行大模型演练，实现了内容的沉淀、提炼、分类，最终通过AI模型技术，实现了招标文件要点精准解读、投标文件内容快速生成，为该企业全年支持上百个个投标项目，投标文件输出效率提升30%，全年0废标。

某大型央国标书工具实战案例

我们为该企业搭建了一套私有化部署的标书工具，将其历史投标案例作为素材进行大模型演练，实现了内容的沉淀、提炼、分类，最终通过AI模型技术，实现了招标文件要点精准解读、投标文件内容快速生成，为该企业全年支持上百个个投标项目，投标文件输出效率提升30%，全年0废标，超标完成。

我们想使用cookie 以便更好了解您对本网站的使用情况。这将有助于改善您今后访问本网站的体验。关于cookie 的使用，以及如何撤回或管理您的同意，请详见我们的

[《隐私政策》](https://www.idigital.com.cn/service)

。点击右侧确认按钮，同意cookie 的使用。

确 认

![](https://www.idigital.com.cn/_nuxt/online-service-img.CaMyI5oa.png)

- ![](data:image/svg+xml,%3c?xml%20version=%271.0%27%20encoding=%27UTF-8%27?%3e%3csvg%20version=%271.1%27%20width=%2736px%27%20height=%2736px%27%20viewBox=%270%200%2036.0%2036.0%27%20xmlns=%27http://www.w3.org/2000/svg%27%20xmlns:xlink=%27http://www.w3.org/1999/xlink%27%3e%3cdefs%3e%3cclipPath%20id=%27i0%27%3e%3cpath%20d=%27M1920,0%20L1920,6208%20L0,6208%20L0,0%20L1920,0%20Z%27%3e%3c/path%3e%3c/clipPath%3e%3cclipPath%20id=%27i1%27%3e%3cpath%20d=%27M25.1322635,0%20C27.2705057,0%2029,1.74341267%2029,3.89183958%20L29,16.6279379%20C29,18.772395%2027.2705057,20.513953%2025.1322635,20.513953%20L20.7101907,20.513953%20L20.7100214,20.9658457%20C20.710008,21.0121081%2020.7099949,21.0612386%2020.7099825,21.1129084%20L20.7099805,22.4583922%20C20.7100001,22.5294902%2020.7100236,22.6008244%2020.7100515,22.6720658%20L20.710851,23.6926061%20C20.7109335,23.754695%2020.7110227,23.8150463%2020.7111189,23.8733308%20L20.7117843,24.1956051%20C20.7124155,24.4391131%2020.7132458,24.614503%2020.7143319,24.6806504%20C20.7224525,25.0508152%2020.4756639,25.1586823%2019.8647421,24.6806504%20C19.6102049,24.4805484%2018.6799674,23.7238131%2017.6813037,22.9090456%20L17.0787525,22.4172099%20C15.8766606,21.4355662%2014.7509299,20.513953%2014.7509299,20.513953%20L3.86576294,20.513953%20C1.73162963,20.513953%200,18.772395%200,16.6279704%20L0,3.89183958%20C0,1.74344521%201.73166198,0%203.86576294,0%20Z%20M8.28576513,8.33326463%20C7.14283069,8.33326463%206.21439664,9.26306954%206.21439664,10.4165808%20C6.21439664,11.5701897%207.14283069,12.499897%208.28576513,12.499897%20C9.42873192,12.499897%2010.3571983,11.5701897%2010.3571983,10.4165808%20C10.3571983,9.26310208%209.42869957,8.33326463%208.28576513,8.33326463%20Z%20M14.5000647,8.33326463%20C13.3570979,8.33326463%2012.4286315,9.26306954%2012.4286315,10.4165808%20C12.4286315,11.5701897%2013.3570979,12.499897%2014.5000647,12.499897%20C15.6429668,12.499897%2016.5714979,11.5701897%2016.5714979,10.4165808%20C16.5714979,9.26310208%2015.6429991,8.33326463%2014.5000647,8.33326463%20Z%20M20.7143319,8.33326463%20C19.5714946,8.33326463%2018.6429634,9.26306954%2018.6429634,10.4165808%20C18.6429634,11.5701897%2019.5714946,12.499897%2020.7143319,12.499897%20C21.857234,12.499897%2022.7857975,11.5701897%2022.7857975,10.4165808%20C22.7857975,9.26310208%2021.8572664,8.33326463%2020.7143319,8.33326463%20Z%27%3e%3c/path%3e%3c/clipPath%3e%3c/defs%3e%3cg%20transform=%27translate(-1848.0%20-1211.0)%27%3e%3cg%20clip-path=%27url(%23i0)%27%3e%3cg%20transform=%27translate(1829.0%201114.0)%27%3e%3cg%20transform=%27translate(19.0%2097.0)%27%3e%3cg%20transform=%27translate(4.0%206.0)%27%3e%3cg%20clip-path=%27url(%23i1)%27%3e%3cpolygon%20points=%270,0%2029,0%2029,25%200,25%200,0%27%20stroke=%27none%27%20fill=%27%23CBD3D0%27%3e%3c/polygon%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/svg%3e)
- ![](data:image/svg+xml,%3c?xml%20version=%271.0%27%20encoding=%27UTF-8%27?%3e%3csvg%20version=%271.1%27%20width=%2736px%27%20height=%2736px%27%20viewBox=%270%200%2036.0%2036.0%27%20xmlns=%27http://www.w3.org/2000/svg%27%20xmlns:xlink=%27http://www.w3.org/1999/xlink%27%3e%3cdefs%3e%3cclipPath%20id=%27i0%27%3e%3cpath%20d=%27M1920,0%20L1920,6134%20L0,6134%20L0,0%20L1920,0%20Z%27%3e%3c/path%3e%3c/clipPath%3e%3cclipPath%20id=%27i1%27%3e%3cpath%20d=%27M5.44884772,2.204834%20L10.907988,7.6637174%20C11.5920259,8.34942437%2011.5920259,9.4594008%2010.907988,10.1451078%20L9.66728425,11.3849257%20C8.96545433,12.0867508%209.66399443,14.3593482%2011.6523664,16.3474871%20C13.6407383,18.3356261%2015.9122548,19.035258%2016.614962,18.3325556%20L17.8556657,17.0918604%20C18.5413774,16.4078271%2019.6513615,16.4078271%2020.3370732,17.0918604%20L25.7959941,22.5509631%20C26.4800068,23.2365948%2026.4800068,24.3465023%2025.7959941,25.0321341%20L24.5552904,26.2728293%20C23.638525,27.1895884%2022.4326935,27.747978%2020.9711326,27.932865%20C20.6086831,27.9781613%2020.2437397,28.0005763%2019.8784712,27.9999887%20C18.8147602,27.9999887%2017.6670489,27.8203537%2016.4522252,27.4630808%20C13.1547211,26.4939042%209.68658459,24.3081577%206.68955145,21.3102679%20C3.6925183,18.3123781%201.5058794,14.8453621%200.536696124,11.5476614%20C0.0541880324,9.90473269%20-0.104600968,8.38440407%200.066908711,7.02966227%20C0.251797034,5.56811148%200.810190465,4.36228823%201.72695583,3.44552922%20L2.96765958,2.204834%20C3.6532961,1.52082603%204.76321121,1.52082603%205.44884772,2.204834%20Z%20M16.7706805,8.42190781%20C18.3204189,8.42360005%2019.576308,9.67948052%2019.5780002,11.2292082%20C19.5780002,11.6168156%2019.2637803,11.9310334%2018.8761703,11.9310334%20C18.4885603,11.9310334%2018.1743404,11.6168156%2018.1743404,11.2292082%20C18.1734943,10.4543444%2017.5455497,9.82640414%2016.7706805,9.82555803%20C16.3830705,9.82555803%2016.0688505,9.51134023%2016.0688505,9.12373292%20C16.0688505,8.73612562%2016.3830705,8.42190781%2016.7706805,8.42190781%20Z%20M16.7706805,3.28713486e-06%20C21.2851254,-0.0034402441%2025.3620086,2.69890763%2027.117189,6.85815377%20C27.702579,8.24092655%2028.0028316,9.72763271%2027.9999799,11.2292082%20C27.9999799,11.6168156%2027.6857395,11.9310334%2027.2981295,11.9310334%20C26.9105196,11.9310334%2026.5962996,11.6168156%2026.5962996,11.2292082%20C26.5962996,5.81199572%2022.1879303,1.4036568%2016.7706805,1.4036568%20C16.3830705,1.4036568%2016.0688505,1.08943899%2016.0688505,0.701831689%20C16.0688505,0.314224384%2016.3830705,3.28713486e-06%2016.7706805,3.28713486e-06%20Z%20M16.7706805,4.2109572%20C18.6320492,4.2109572%2020.4171811,4.95037794%2021.7333676,6.26655533%20C23.049554,7.58273271%2023.7889799,9.36785234%2023.7889799,11.2292082%20C23.7889799,11.6168156%2023.4747599,11.9310334%2023.0871499,11.9310334%20C22.6995399,11.9310334%2022.38532,11.6168156%2022.38532,11.2292082%20C22.38532,8.13328225%2019.8666278,5.61460741%2016.7706805,5.61460741%20C16.3830705,5.61460741%2016.0688505,5.30038961%2016.0688505,4.91278231%20C16.0688505,4.525175%2016.3830705,4.2109572%2016.7706805,4.2109572%20Z%27%3e%3c/path%3e%3c/clipPath%3e%3c/defs%3e%3cg%20transform=%27translate(-1848.0%20-1349.0)%27%3e%3cg%20clip-path=%27url(%23i0)%27%3e%3cg%20transform=%27translate(1836.0%201269.0)%27%3e%3cg%20transform=%27translate(12.0%2080.0)%27%3e%3cg%20transform=%27translate(4.0%204.0)%27%3e%3cg%20clip-path=%27url(%23i1)%27%3e%3cpolygon%20points=%27-2.97006258e-17,-5.31476317e-14%2028,-5.31476317e-14%2028,28%20-2.97006258e-17,28%20-2.97006258e-17,-5.31476317e-14%27%20stroke=%27none%27%20fill=%27%23CBD2CF%27%3e%3c/polygon%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/svg%3e)
![](https://www.idigital.com.cn/_nuxt/tel.eUfnVCbI.png)

咨询电话400-026-2099

- ![](data:image/svg+xml,%3c?xml%20version=%271.0%27%20encoding=%27UTF-8%27?%3e%3csvg%20version=%271.1%27%20width=%2736px%27%20height=%2736px%27%20viewBox=%270%200%2036.0%2036.0%27%20xmlns=%27http://www.w3.org/2000/svg%27%20xmlns:xlink=%27http://www.w3.org/1999/xlink%27%3e%3cdefs%3e%3cclipPath%20id=%27i0%27%3e%3cpath%20d=%27M1920,0%20L1920,6134%20L0,6134%20L0,0%20L1920,0%20Z%27%3e%3c/path%3e%3c/clipPath%3e%3cclipPath%20id=%27i1%27%3e%3cpath%20d=%27M21.6803015,8.47366126%20C26.6104931,8.47366126%2031,12.155263%2031,16.6718901%20C31,19.2197117%2029.3591505,21.475575%2027.1567713,23.1768174%20L27.9819556,26%20L24.9724924,24.3032646%20C23.8750723,24.5864592%2022.772962,24.8701189%2021.6803015,24.8701189%20C16.4598431,24.8701189%2012.3482696,21.1963151%2012.3482696,16.6718901%20C12.3482696,12.1552988%2016.4598431,8.47366126%2021.6803015,8.47366126%20Z%20M10.971978,0%20C16.3669439,0%2021.0932018,3.38180963%2022.0426224,7.93359904%20C21.6935728,7.89353614%2021.3417091,7.86670831%2020.9860238,7.86670831%20C15.7741118,7.86670831%2011.657744,11.8721041%2011.6577093,16.8076389%20C11.6577093,17.6283561%2011.7819455,18.4194195%2011.9963017,19.1747483%20C11.657744,19.2021484%2011.3162333,19.2197117%2010.9719433,19.2197117%20C9.60232209,19.2197117%208.50114984,18.9320816%207.12871456,18.6523567%20L3.29309425,20.6327517%20L4.39047966,17.2344161%20C1.64369831,15.2583135%200,12.7104919%200,9.60794214%20C0,4.23293165%204.94064888,0%2010.971978,0%20Z%20M18.6546139,12.9980505%20C18.108301,12.9980505%2017.5572633,13.5649763%2017.5572633,14.1278959%20C17.5572633,14.6987564%2018.108301,15.2583135%2018.6546139,15.2583135%20C19.4846274,15.2583135%2020.0280914,14.6987564%2020.0280914,14.1278959%20C20.0280914,13.5649763%2019.4846274,12.9980505%2018.6546139,12.9980505%20Z%20M24.6898341,12.9980505%20C24.1473081,12.9980505%2023.6000224,13.5649763%2023.6000224,14.1278959%20C23.6000224,14.6987564%2024.1472733,15.2583135%2024.6898341,15.2583135%20C25.5121349,15.2583135%2026.0632074,14.6987564%2026.0632074,14.1278959%20C26.0632074,13.5649763%2025.5121349,12.9980505%2024.6898341,12.9980505%20Z%20M15.0865393,4.80368491%20C14.2641343,4.80368491%2013.4389846,5.36331355%2013.4389846,6.21339823%20C13.4389846,7.06012049%2014.2641343,7.62743979%2015.0865393,7.62743979%20C15.9126269,7.62743979%2016.4598778,7.06004895%2016.4598778,6.21339823%20C16.4598778,5.36327778%2015.9126269,4.80368491%2015.0865393,4.80368491%20Z%20M7.40758601,4.80372068%20C6.58521573,4.80372068%205.75534125,5.36331355%205.75534125,6.213434%20C5.75534125,7.06015626%206.58525048,7.62747556%207.40758601,7.62747556%20C8.22988681,7.62747556%208.77717248,7.06012049%208.77717248,6.213434%20C8.77717248,5.36331355%208.22992155,4.80372068%207.40758601,4.80372068%20Z%27%3e%3c/path%3e%3c/clipPath%3e%3c/defs%3e%3cg%20transform=%27translate(-1848.0%20-1417.0)%27%3e%3cg%20clip-path=%27url(%23i0)%27%3e%3cg%20transform=%27translate(1836.0%201269.0)%27%3e%3cg%20transform=%27translate(12.0%20148.0)%27%3e%3cg%20transform=%27translate(3.0%205.0)%27%3e%3cg%20clip-path=%27url(%23i1)%27%3e%3cpolygon%20points=%270,0%2031,0%2031,26%200,26%200,0%27%20stroke=%27none%27%20fill=%27%23CBD2CF%27%3e%3c/polygon%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/svg%3e)

扫码添加

真人咨询

![](https://www.idigital.com.cn/_nuxt/wechat.DCz33zyI.png)

### 来源 4: 资源丰富的投标、招标生态_便捷工具 - 快书编标

- URL: https://www.kshbb.com/AIIntelligent.html
- 精读方法：failed

精读失败：500 Server Error: Internal Server Error for url: https://api.firecrawl.dev/v2/scrape

### 来源 5: 智能投标助手 - AGICamp

- URL: https://agicamp.com/products/CyberIoT
- 精读方法：firecrawl-scrape

![智能投标助手](https://static001.geekbang.org/infoq/a9/a9ebbd46e3c77bdab1e47818b9fb415e.png)

# 智能投标助手

以最快的速度、最低的成本，生成得分最高的标书！

办公效率文本生成AI Agent

62 喜欢62

52 评论52

11个月前发布

分享

喜欢访问应用

产品概览

## 应用截图

![图片1.png](https://static001.geekbang.org/infoq/f5/f532d95ea24d1b0edad6c2f99baeaf61.png)

1/5

![图片2.png](https://static001.geekbang.org/infoq/a3/a3b5bdb31387b5c656108e4b5f1125db.png)

2/5

![图片3.png](https://static001.geekbang.org/infoq/6e/6e0457e6d4d04e0e150a07dcec1a8c2c.png)

3/5

![图片4.png](https://static001.geekbang.org/infoq/5e/5ee742cd9ba98adc9e901d397b8d15fa.png)

4/5

![图片5.png](https://static001.geekbang.org/infoq/b9/b98bf5e1ed692d971c20628b9748ae6c.png)

5/5

## 使用场景

针对目前企业投标过程中存在的编写时间长、废标风险大、投标决策缺乏量化依据等问题和痛点，利用大模型、Al Agent、RAG等技术研发并推出了智能投标助手。5分钟完成招标文件解析、15分钟完成标书商务卷编制，有效降低废标率。

## 开发者/推荐人

![Jetty](https://static001.geekbang.org/account/avatar/00/41/7b/19/d5f4fae8.jpg)

### Jetty

开发者

## 用户评论 (52)

### 发表评论

0 / 2000登录后发表评论

![Jetty](https://static001.geekbang.org/account/avatar/00/41/7b/19/d5f4fae8.jpg)

#### Jetty

大家好，我是吴佳祺，赛博物联的创始人，也是「智能投标助手」的创造者之一。今天，这个酝酿已久、寄托了我们整个团队心血的产品终于和大家见面了，心情激动也充满期待。

回想过去20年，在To G项目投标工作中的经历，也像许多投标人一样，在“中标率”这座大山前挣扎。招标文件拿到手就头皮发麻——厚厚的PDF里找关键信息像大海捞针；几千页的技术方案、清单、资质材料要整合，效率低下还易出错；合规性检查让人提心吊胆，一个格式错误可能前功尽弃；对标书质量的把控更像“开盲盒”，结果公布前永远充满忐忑... 最痛苦的是最后赶标书，熬通宵、反复核对、心力交瘁。我相信每个投标伙伴都深有体会： **传统投标过程的“苦”和“不确定性”，太消磨人了！​**

​

**时代变了！** 当看到GPT这类大语言模型能像人类一样“读懂”复杂文档并推理、生成，当看到AI能在金融、医学等专业领域发挥强大辅助能力时，我内心是震撼的。微软CEO Satya Nadella 提出：“ **AI是终极的‘放大器’，它不仅能提升生产力，更能释放人类创造力。**” Marc Andreessen 的观点则更为直接：“ **AI不会取代你，但一个会用AI的人会**。”那一刻我无比确信：​ **所有繁琐、高成本、高风险的工作流，都值得用AI重做一遍！而投标，这个对精度、效率和洞察力要求极高，却又严重依赖“人肉堆砌”的场景，正是AI技术该大放光芒的战场！​**

​

于是，我们决定倾力打造「智能投标助手」。它的使命很简单，却很强大： **用最短的时间，最低的成本，写出得分最高的标书！​** ​在AI标书领域，我们不是唯一的，但我们相信，「智能投标助手」是 **真正以AI为核心引擎，融合投标场景，深度Know-How的产品**。我们不只是在工具上加AI功能，而是用AI重构了投标流程的核心环节，让它变得 **更智能、更可靠、更能打硬仗**。

**我们想用AI，成为每个投标人背后坚实的后盾，赋予更强大的竞争力，让每一次投标都掷地有声，让每一份精心准备，都有更大机会获得应有的回报。让中标率，不再是难以捉摸的“玄学”。​**

​

**「智能投标助手」今天正式上线！** 希望它能成为您征战下一个项目时，最可靠、最省心的伙伴！

2 回复

![陈剑](https://static001.geekbang.org/account/avatar/00/39/e7/62/ace7f154.jpg)

#### 陈剑

在哪里下载

0 回复

![Jetty](https://static001.geekbang.org/account/avatar/00/41/7b/19/d5f4fae8.jpg)

Jetty

回复 @陈剑：  您好，关注【赛博物联】公众号，就可以找到啦

0 回复

![Geek_31fb76](https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83errj9iaMOHaUFeukYBovd862BNAMevd4xtibRWicDKoiaa4POhG5kdia1wcEBEEu2CE4NeP6NQs9WFrT3w/132)

#### Geek\_31fb76

请问怎么试用？

0 回复

![Jetty](https://static001.geekbang.org/account/avatar/00/41/7b/19/d5f4fae8.jpg)

Jetty

回复 @Geek\_31fb76：  您好，关注【赛博物联】公众号，就可以找到啦

0 回复

![李深](https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLZp7t4ibWuvEwlpSlEGm3tPmkBsfibhgBOsZN4BoP1xH2wkzhwYVOj2vRmevhR0ObJmqP6chs1wwJA/132)

#### 李深

您好，我是玄同科技的李深。我们公司在做一个人工智能一体机，不知道咱的应用能否上我们的机器。做个生态合作

0 回复

![Jetty](https://static001.geekbang.org/account/avatar/00/41/7b/19/d5f4fae8.jpg)

Jetty

回复 @李深：  您好，可以交流一下，关注【赛博物联】公众号就可以找到我们了

0 回复

![Dora](https://static001.geekbang.org/account/avatar/00/43/d5/88/5b6fdee6.jpg)

#### Dora

请问有生成招标文件的AI吗？

0 回复

![Jetty](https://static001.geekbang.org/account/avatar/00/41/7b/19/d5f4fae8.jpg)

Jetty

回复 @Dora：  已经在研发计划中，敬请关注

0 回复

![Geek_19ed7d](https://static001.geekbang.org/static/time/img/geek_elements/defaultAvatar.jpg)

#### Geek\_19ed7d

😘

0 回复

![796💦](https://static001.geekbang.org/account/avatar/00/43/63/d7/bfaee3d5.jpg)

#### 796💦

这个产品确实是一种全新体验，我自己公司用这个标书解析功能已经离不开了。真的比人工效率高太多，之前可能一天撑死接20份标书，用这个智能解析，就昨天，接了28份，太牛了。

0 回复

![Geek_65269e](https://static001.geekbang.org/static/time/img/geek_elements/defaultAvatar.jpg)

#### Geek\_65269e

非常棒！，，！！超级好用！，，太棒了！，，，！！！！！

0 回复

![yolo](https://static001.geekbang.org/account/avatar/00/15/97/cd/e0c294d9.jpg)

#### yolo

👍👍👍👍👍👍

0 回复

![做一只好玉米](https://static001.geekbang.org/account/avatar/00/2c/ae/d9/7e38d803.jpg)

#### 做一只好玉米

Q确实很好用 效率高多了嘿嘿

0 回复

加载更多评论

### 来源 6: 招标文件全维度智能解析：读懂标书，才是投标制胜的第一步_核心_细节_评分

- URL: https://www.sohu.com/a/1035138286_122095475
- 精读方法：firecrawl-scrape

# 招标文件全维度智能解析：读懂标书，才是投标制胜的第一步

2026-06-11 12:23
来源:
[红点智标](https://www.sohu.com/a/1035138286_122095475?spm=smpc.content-abroad.content.1.1782059419356SgxaFMj)

![](https://statics.itc.cn/mptc-mpfe/img/article/icon_Wechat.png)

[![](https://statics.itc.cn/mptc-mpfe/img/article/icon_Weibo.png)](http://service.weibo.com/share/share.php?url=https%3A%2F%2Fwww.sohu.com%2Fa%2F1035138286_122095475&title=%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E5%85%A8%E7%BB%B4%E5%BA%A6%E6%99%BA%E8%83%BD%E8%A7%A3%E6%9E%90%EF%BC%9A%E8%AF%BB%E6%87%82%E6%A0%87%E4%B9%A6%EF%BC%8C%E6%89%8D%E6%98%AF%E6%8A%95%E6%A0%87%E5%88%B6%E8%83%9C%E7%9A%84%E7%AC%AC%E4%B8%80%E6%AD%A5_%E6%A0%B8%E5%BF%83_%E7%BB%86%E8%8A%82_%E8%AF%84%E5%88%86&searchPic=true&pic=//q5.itc.cn/q_70/images01/20260611/f8c3594fa3f04a50bda384c45d8b30e6.png&appkey=2890110694)[![](https://statics.itc.cn/mptc-mpfe/img/article/icon_Space.png)](http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=https%3A%2F%2Fwww.sohu.com%2Fa%2F1035138286_122095475)

![](https://statics.itc.cn/mptc-mpfe/img/article/icon_Link.png)

链接复制成功

发布于：山西省

很多投标人大破防：明明报价合理、方案扎实、实力在线，最后却莫名废标、无缘中标！说到底，九成投标翻车，都栽在了读不透招标文件上。

投标圈藏着一个致命误区：太多团队本末倒置，把大把时间砸在标书排版、文案润色、报价核算上，却忽略了最关键的前置核心——吃透、拆准招标文件。现在的招标文件动辄几百页，通篇文字堆砌，隐性门槛、暗藏约束、隐形扣分点零散藏在各个角落，根本不会重点标注。纯人工逐页精读，很容易看漏、看错、理解跑偏。往往就是漏掉一条隐性响应要求、疏忽一处评分细则、错过一项资质时限，直接扣分、丢分，甚至直接一票否决废标，熬夜熬出来的标书直接作废，所有心血全部白费！

![文章配图-1](https://q5.itc.cn/q_70/images01/20260611/f8c3594fa3f04a50bda384c45d8b30e6.png)

传统人工读标，早就跟不上现在的投标内卷节奏了！人工核对全靠眼力、靠经验、靠死磕，翻完整本标书耗时耗力，效率低到离谱，容错率还极低。新手看不懂暗藏的隐性条款，老手也难免出现细节疏漏，根本做不到对标书内容无死角拆解。这也是为什么很多团队明明全力备标，却频繁翻车、屡屡落标的核心原因。

针对投标行业这一核心痛点，红点智标AI招标文件全维度智能解析系统强势破局！彻底颠覆传统人工死磕读标的低效模式，用高精度AI智能解析，一键解决读标难、判标乱、细节漏、风险高的各类难题，让投标备标开局即精准、高效不踩坑！

操作超级轻量化，新手零上手压力！只需一键上传招标文件，AI快速完成全文深度拆解、智能筛选、分类规整，秒速提炼全部核心信息，彻底告别人工逐字啃读的繁琐。不同于普通工具的简单文字检索，红点智标主打全维度精细化解析，精准拆分商务评分、技术评分两大核心板块，逐项梳理打分标准、加分亮点与扣分雷区，评分规则清晰可视化，精准拿捏每一个得分点！

不仅如此，系统还能自动抓取核心硬性指标，投标资质、报名时限、响应要求等必备条件一键汇总，同时智能识别、高亮标记人工极易忽略的各类隐性约束条件，完美补齐人工读标盲区。AI全方位无死角拆解、标准化梳理，规避人工主观误判、细节遗漏等问题，从源头杜绝条款错读、信息漏缺、响应不达标等投标翻车风险！

![文章配图-2](https://q4.itc.cn/q_70/images01/20260611/b279b9188c59461d8341e81007626b93.jpeg)

读懂标书，是投标制胜的先决条件！有了红点智标AI助力，不用全员耗时长时间精读标书，快速吃透项目所有规则与要求，精准对标投标标准、补齐响应短板、规避各类雷区，让你的标书完全贴合招标规则、踩准评分要点，投标开局就领先同行一大截！

效率拉满的同时，数据安全也直接拉满！系统支持本地私有化部署，完美适配企业涉密、合规需求。所有标书文件、解析数据、项目核心资料全部本地留存，不上云、不外流，从根源杜绝信息泄露风险，高效赋能的同时牢牢守住数据安全底线，适配各类工程企业、招投标机构使用。

如今投标行业内卷加剧，拼速度、拼细节、拼准确率，已经成为中标突围的关键！红点智标AI全维度标书解析，用智能科技替代人工低效重复劳作，帮企业精准吃透每一条招标条款、把控每一处细节，大幅降低废标概率、升级标书质量、拉升整体中标率，助力各大企业在激烈的投标竞争中轻松突围！

想要解锁智能高效的投标新玩法，告别人工读标踩坑？直接私信咨询，即刻体验！ [返回搜狐，查看更多](https://www.sohu.com/?strategyid=00001&spm=smpc.content-abroad.content.2.1782059419356SgxaFMj "点击进入搜狐首页")

平台声明：该文观点仅代表作者本人，搜狐号系信息发布平台，搜狐仅提供信息存储空间服务。

_首赞_

+1

点赞失败

阅读 ( _4_)

我来说两句

[shine link](https://www.sohu.com/collection/1065) 0人参与，
0条评论

[搜狐“我来说两句” 用户公约](https://www.sohu.com/a/739523038_99975564/?pvid=000115_3w_a)

![默认头像](<Base64-Image-Removed>)点击登录

搜狐小编

发布

推荐阅读

[![文章配图-1](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039064693_121050881?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.1.1782059419356SgxaFMj)

# [1:4惨败！被压着打！五星巴西被打成纸老虎，世界杯五冠王没落了](https://www.sohu.com/a/1039064693_121050881?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.1.1782059419356SgxaFMj)

[![体育知道分子头像](https://p0.itc.cn/c_lfill,w_40,h_40,g_face/mpbp/pro/20220208/01a9fa59148b40b78a87c5e558a8e8ff.jpeg)](https://mp.sohu.com/profile?xpt=ZTg4ZmQ3OTUtNTI0Ni00YWZlLWE1MDgtNTk1ZGE2MDI4MjI4&spm=smpc.content-abroad.fd-d.1.1782059419356SgxaFMj)[体育知道分子](https://mp.sohu.com/profile?xpt=ZTg4ZmQ3OTUtNTI0Ni00YWZlLWE1MDgtNTk1ZGE2MDI4MjI4&spm=smpc.content-abroad.fd-d.1.1782059419356SgxaFMj)·06-19 20:37 [0](https://www.sohu.com/a/1039064693_121050881?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.1.1782059419356SgxaFMj#comment_area)

[![文章配图-2](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1034225456_122406580?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.2.1782059419356SgxaFMj)

# [原来她早已去世！退休5个月在美国儿子家中离世，只留下26字遗言](https://www.sohu.com/a/1034225456_122406580?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.2.1782059419356SgxaFMj)

[![忆禾溪头像](https://q2.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250421/e92ef3c22d604b99969646b4cfdd56a0.png)](https://mp.sohu.com/profile?xpt=MjY3NzMzZDYtOTM3Yy00ZGZjLTg3MTUtM2E5YjYyMTM5YTBl&spm=smpc.content-abroad.fd-d.2.1782059419356SgxaFMj)[忆禾溪](https://mp.sohu.com/profile?xpt=MjY3NzMzZDYtOTM3Yy00ZGZjLTg3MTUtM2E5YjYyMTM5YTBl&spm=smpc.content-abroad.fd-d.2.1782059419356SgxaFMj)·06-09 02:13 [0](https://www.sohu.com/a/1034225456_122406580?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.2.1782059419356SgxaFMj#comment_area)

[![文章配图-3](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039368305_121142409?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.3.1782059419356SgxaFMj)

# [6月21日：美国驻华使馆深夜发了条消息，全网都懵了！因中国不承认双重国籍，入了美国...](https://www.sohu.com/a/1039368305_121142409?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.3.1782059419356SgxaFMj)

[![老虎房车游世界头像](https://p3.itc.cn/c_lfill,w_40,h_40,g_face/mpbp/pro/20220326/fcdcfb539ca84920aa0fac041297a716.jpeg)](https://mp.sohu.com/profile?xpt=NzE2YzhjOWItNjdhMS00MmI0LWI4NTEtNTU0NjM5Y2MwOGRi&spm=smpc.content-abroad.fd-d.3.1782059419356SgxaFMj)[老虎房车游世界](https://mp.sohu.com/profile?xpt=NzE2YzhjOWItNjdhMS00MmI0LWI4NTEtNTU0NjM5Y2MwOGRi&spm=smpc.content-abroad.fd-d.3.1782059419356SgxaFMj)·昨天 17:45 [0](https://www.sohu.com/a/1039368305_121142409?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.3.1782059419356SgxaFMj#comment_area)

[![文章配图-4](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039165729_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.4.1782059419356SgxaFMj)

# [果然被我猜中了！俄罗斯最新版官方地图上，悄悄把“海参崴”“伯力”等8个远东地名，用...](https://www.sohu.com/a/1039165729_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.4.1782059419356SgxaFMj)

[![史韵承传头像](https://q3.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260115/eb2b00ba50da416383dbeb52c0006fc6.jpeg)](https://mp.sohu.com/profile?xpt=YTQ4M2I2YmQtNzc1YS00YWM2LWI1MjQtNGEwN2JiNDgxN2Zh&spm=smpc.content-abroad.fd-d.4.1782059419356SgxaFMj)[史韵承传](https://mp.sohu.com/profile?xpt=YTQ4M2I2YmQtNzc1YS00YWM2LWI1MjQtNGEwN2JiNDgxN2Zh&spm=smpc.content-abroad.fd-d.4.1782059419356SgxaFMj)·昨天 00:00 [0](https://www.sohu.com/a/1039165729_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.4.1782059419356SgxaFMj#comment_area)

[![文章配图-5](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1037489144_120452151?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.6.1782059419356SgxaFMj)

# [两性关系：女性过了45岁后，普遍都是这样的状态](https://www.sohu.com/a/1037489144_120452151?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.6.1782059419356SgxaFMj)

[![娱小慧头像](https://q2.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250601/16f332a57fe5499d9cfd4ec84f9485c6.jpeg)](https://mp.sohu.com/profile?xpt=ZWQ2M2FhYTUtOTZmNy00ZTQ3LTg4OWYtOGYzY2Q3YjdhZjQx&spm=smpc.content-abroad.fd-d.6.1782059419356SgxaFMj)[娱小慧](https://mp.sohu.com/profile?xpt=ZWQ2M2FhYTUtOTZmNy00ZTQ3LTg4OWYtOGYzY2Q3YjdhZjQx&spm=smpc.content-abroad.fd-d.6.1782059419356SgxaFMj)·昨天 11:00 [0](https://www.sohu.com/a/1037489144_120452151?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.6.1782059419356SgxaFMj#comment_area)

[![文章配图-6](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038892072_121165594?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.7.1782059419356SgxaFMj)

# [一丝不挂还不知廉耻！内娱为艺术献身的流氓真相，该打破了](https://www.sohu.com/a/1038892072_121165594?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.7.1782059419356SgxaFMj)

[![叶公说史头像](https://p5.itc.cn/c_lfill,w_40,h_40,g_face/mpbp/pro/20220717/0ea9ba8e56b843088aba96608fa93e81.png)](https://mp.sohu.com/profile?xpt=ODNhZDU5ZGQtNGFkZi00Y2VkLWI0NzEtNWE2ZjY4ODQ5M2I2&spm=smpc.content-abroad.fd-d.7.1782059419356SgxaFMj)[叶公说史](https://mp.sohu.com/profile?xpt=ODNhZDU5ZGQtNGFkZi00Y2VkLWI0NzEtNWE2ZjY4ODQ5M2I2&spm=smpc.content-abroad.fd-d.7.1782059419356SgxaFMj)·06-19 04:27 [0](https://www.sohu.com/a/1038892072_121165594?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.7.1782059419356SgxaFMj#comment_area)

[![文章配图-7](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039260099_122637979?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.8.1782059419356SgxaFMj)

# [水均益在直播间抛出个尖锐问题：“你为啥不去考个教练证？”董路立马反击：“那你考过...](https://www.sohu.com/a/1039260099_122637979?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.8.1782059419356SgxaFMj)

[![阿芜爱体育头像](https://q6.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260209/9b3817aa5bd7450b8706ddc6e18e1e61.png)](https://mp.sohu.com/profile?xpt=MGYxMTBmYmUtNDlkZS00MDVlLWE0MTMtNTczODZiNTY4NTMz&spm=smpc.content-abroad.fd-d.8.1782059419356SgxaFMj)[阿芜爱体育](https://mp.sohu.com/profile?xpt=MGYxMTBmYmUtNDlkZS00MDVlLWE0MTMtNTczODZiNTY4NTMz&spm=smpc.content-abroad.fd-d.8.1782059419356SgxaFMj)·昨天 06:41 [0](https://www.sohu.com/a/1039260099_122637979?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.8.1782059419356SgxaFMj#comment_area)

[![文章配图-8](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039278041_122535601?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.9.1782059419356SgxaFMj)

# [现在的俄罗斯大概率只剩下两条路了：要么低头，把吞进去的地全吐出来，赔到服气；要么...](https://www.sohu.com/a/1039278041_122535601?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.9.1782059419356SgxaFMj)

[![锋火金生头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20251003/062c95d1bcfc48a4a4e302a1c4208f69.jpeg)](https://mp.sohu.com/profile?xpt=ZmExMTRlNjMtMWNmZC00ZDQ2LTgzY2ItZDJjMjY5Mjk0YTli&spm=smpc.content-abroad.fd-d.9.1782059419356SgxaFMj)[锋火金生](https://mp.sohu.com/profile?xpt=ZmExMTRlNjMtMWNmZC00ZDQ2LTgzY2ItZDJjMjY5Mjk0YTli&spm=smpc.content-abroad.fd-d.9.1782059419356SgxaFMj)·昨天 08:15 [0](https://www.sohu.com/a/1039278041_122535601?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.9.1782059419356SgxaFMj#comment_area)

[![文章配图-9](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1037464883_121901820?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.11.1782059419356SgxaFMj)

# [范冰冰为艺术献身的3部经典电影，哪部最令你难忘？](https://www.sohu.com/a/1037464883_121901820?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.11.1782059419356SgxaFMj)

[![小宝说娱头像](https://q0.itc.cn/c_lfill,w_40,h_40,g_face/images03/20241115/dc1577ce01984915ac8978436e3587ea.png)](https://mp.sohu.com/profile?xpt=NDYyMzJmODMtY2E2MC00YmE0LTkzMTAtYmUxNGI1YzdjM2I3&spm=smpc.content-abroad.fd-d.11.1782059419356SgxaFMj)[小宝说娱](https://mp.sohu.com/profile?xpt=NDYyMzJmODMtY2E2MC00YmE0LTkzMTAtYmUxNGI1YzdjM2I3&spm=smpc.content-abroad.fd-d.11.1782059419356SgxaFMj)·06-17 19:15 [0](https://www.sohu.com/a/1037464883_121901820?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.11.1782059419356SgxaFMj#comment_area)

[![文章配图-10](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039173411_121165479?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.12.1782059419356SgxaFMj)

# [表面老艺术家，私下贪财又好色，这几位晚节不保一点都不冤](https://www.sohu.com/a/1039173411_121165479?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.12.1782059419356SgxaFMj)

[![史风头像](https://p2.itc.cn/c_lfill,w_40,h_40,g_face/mpbp/pro/20220714/25ee8c0b187d4957866ad3d6fcd53256.png)](https://mp.sohu.com/profile?xpt=ZmJjYzI4NTQtYzA1MC00ZTgzLWJjNWEtYzM4ZWY2ODljNmRm&spm=smpc.content-abroad.fd-d.12.1782059419356SgxaFMj)[史风](https://mp.sohu.com/profile?xpt=ZmJjYzI4NTQtYzA1MC00ZTgzLWJjNWEtYzM4ZWY2ODljNmRm&spm=smpc.content-abroad.fd-d.12.1782059419356SgxaFMj)·昨天 01:55 [0](https://www.sohu.com/a/1039173411_121165479?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.12.1782059419356SgxaFMj#comment_area)

[![文章配图-11](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039212640_122496491?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.13.1782059419356SgxaFMj)

# [刚制裁菲律宾那个防长特奥多罗没几天，怪事就来了。一些乡镇小卖部、大排档，没人下达...](https://www.sohu.com/a/1039212640_122496491?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.13.1782059419356SgxaFMj)

[![离笙深夜谈头像](https://q5.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250808/fa7bc917de05468dafe0f8a155a7d155.png)](https://mp.sohu.com/profile?xpt=MzY4MTBhNDktOThhOS00M2UxLTk5YTEtMzU3MmYwZGQwOGQx&spm=smpc.content-abroad.fd-d.13.1782059419356SgxaFMj)[离笙深夜谈](https://mp.sohu.com/profile?xpt=MzY4MTBhNDktOThhOS00M2UxLTk5YTEtMzU3MmYwZGQwOGQx&spm=smpc.content-abroad.fd-d.13.1782059419356SgxaFMj)·昨天 03:53 [0](https://www.sohu.com/a/1039212640_122496491?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.13.1782059419356SgxaFMj#comment_area)

[![文章配图-12](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1027882580_122407824?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.14.1782059419356SgxaFMj)

# [两天两架！巴基斯坦中国产战机接连坠毁，这次问题出在哪？](https://www.sohu.com/a/1027882580_122407824?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.14.1782059419356SgxaFMj)

[![科普熊头像](https://q8.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250422/80e83c4876944e15906abece529de58a.png)](https://mp.sohu.com/profile?xpt=MjhiZGIzMDQtYmY5ZS00NTZlLThiZDktZTM3OWYyNjJjZDQx&spm=smpc.content-abroad.fd-d.14.1782059419356SgxaFMj)[科普熊](https://mp.sohu.com/profile?xpt=MjhiZGIzMDQtYmY5ZS00NTZlLThiZDktZTM3OWYyNjJjZDQx&spm=smpc.content-abroad.fd-d.14.1782059419356SgxaFMj)·05-26 04:18 [0](https://www.sohu.com/a/1027882580_122407824?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.14.1782059419356SgxaFMj#comment_area)

[![文章配图-13](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1033286603_121906646?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.16.1782059419356SgxaFMj)

# [一次"交粮"消耗多少体力？相当于跑了多少米，答案来了](https://www.sohu.com/a/1033286603_121906646?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.16.1782059419356SgxaFMj)

[![经方堂泌尿科头像](https://q9.itc.cn/c_lfill,w_40,h_40,g_face/images03/20240619/aa663b16b5a042c0a3a1fbf5483ffdb6.jpeg)](https://mp.sohu.com/profile?xpt=NmFiNTIxMDUtMTYxMy00MjAwLTlkODctYmU5NjkzYjVjN2Ex&spm=smpc.content-abroad.fd-d.16.1782059419356SgxaFMj)[经方堂泌尿科](https://mp.sohu.com/profile?xpt=NmFiNTIxMDUtMTYxMy00MjAwLTlkODctYmU5NjkzYjVjN2Ex&spm=smpc.content-abroad.fd-d.16.1782059419356SgxaFMj)·06-06 23:10 [0](https://www.sohu.com/a/1033286603_121906646?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.16.1782059419356SgxaFMj#comment_area)

[![文章配图-14](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039044526_122489832?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.17.1782059419356SgxaFMj)

# [美国为何禁止种植竹子？终于明白，原来竹子比我们想象的更可怕](https://www.sohu.com/a/1039044526_122489832?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.17.1782059419356SgxaFMj)

[![逍遥侃事儿头像](https://q6.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250728/28ab0f6b520d4c4480b4223dee4eac33.jpeg)](https://mp.sohu.com/profile?xpt=NGQyM2Q3NzUtZGQwYi00Njg0LWFlNjEtNTU5YTY3MjZmZDE4&spm=smpc.content-abroad.fd-d.17.1782059419356SgxaFMj)[逍遥侃事儿](https://mp.sohu.com/profile?xpt=NGQyM2Q3NzUtZGQwYi00Njg0LWFlNjEtNTU5YTY3MjZmZDE4&spm=smpc.content-abroad.fd-d.17.1782059419356SgxaFMj)·06-19 18:38 [0](https://www.sohu.com/a/1039044526_122489832?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.17.1782059419356SgxaFMj#comment_area)

[![文章配图-15](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1032841390_122224259?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.18.1782059419356SgxaFMj)

# [陪玩陪睡已过时？继关晓彤事件、注射不明物后，王源也被曝猛料](https://www.sohu.com/a/1032841390_122224259?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.18.1782059419356SgxaFMj)

[![意挽头像](https://q8.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250116/e804ec225a134523b05e82f0e359e393.png)](https://mp.sohu.com/profile?xpt=MzRmNzA1MGMtMTRjMS00MDNjLWJmMTgtNGEwZDAzZmNiYjEx&spm=smpc.content-abroad.fd-d.18.1782059419356SgxaFMj)[意挽](https://mp.sohu.com/profile?xpt=MzRmNzA1MGMtMTRjMS00MDNjLWJmMTgtNGEwZDAzZmNiYjEx&spm=smpc.content-abroad.fd-d.18.1782059419356SgxaFMj)·06-05 15:33 [0](https://www.sohu.com/a/1032841390_122224259?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.18.1782059419356SgxaFMj#comment_area)

[![文章配图-16](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1035742564_122418959?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.19.1782059419356SgxaFMj)

# [全网喊韦神做2026高考数学卷，他仅一句话，让千万网友闭嘴！](https://www.sohu.com/a/1035742564_122418959?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.19.1782059419356SgxaFMj)

[![不笑风云头像](https://q1.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250507/0bbe6692e0de43d3b4f4dd53425f4d47.png)](https://mp.sohu.com/profile?xpt=YWM3MjY3ZjktZGFmMS00ZjcwLThkNzQtYmI4ZjJjZDgzZmFj&spm=smpc.content-abroad.fd-d.19.1782059419356SgxaFMj)[不笑风云](https://mp.sohu.com/profile?xpt=YWM3MjY3ZjktZGFmMS00ZjcwLThkNzQtYmI4ZjJjZDgzZmFj&spm=smpc.content-abroad.fd-d.19.1782059419356SgxaFMj)·06-12 05:00 [0](https://www.sohu.com/a/1035742564_122418959?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.19.1782059419356SgxaFMj#comment_area)

[![文章配图-17](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038875384_120020443?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.21.1782059419356SgxaFMj)

# [黄色网站为什么能让你免费观看，了解真相后，你还敢继续浏览吗](https://www.sohu.com/a/1038875384_120020443?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.21.1782059419356SgxaFMj)

[![梦新看世界头像](https://p8.itc.cn/c_lfill,w_40,h_40,g_face/images03/20230601/90462a42fa4148df996d2868f4ae54c6.jpeg)](https://mp.sohu.com/profile?xpt=Y2Y0MjBlZDYtMjBlMS00NDIyLTkxZmItMGQ5YzQ2N2U4Y2I0&spm=smpc.content-abroad.fd-d.21.1782059419356SgxaFMj)[梦新看世界](https://mp.sohu.com/profile?xpt=Y2Y0MjBlZDYtMjBlMS00NDIyLTkxZmItMGQ5YzQ2N2U4Y2I0&spm=smpc.content-abroad.fd-d.21.1782059419356SgxaFMj)·06-19 03:38 [0](https://www.sohu.com/a/1038875384_120020443?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.21.1782059419356SgxaFMj#comment_area)

[![文章配图-18](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039604570_122535601?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.22.1782059419356SgxaFMj)

# [蒙古国网友：如果中国不开放领空便于美蒙两国的稀土运输，我们就请求美国驻军，他们立...](https://www.sohu.com/a/1039604570_122535601?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.22.1782059419356SgxaFMj)

[![锋火金生头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20251003/062c95d1bcfc48a4a4e302a1c4208f69.jpeg)](https://mp.sohu.com/profile?xpt=ZmExMTRlNjMtMWNmZC00ZDQ2LTgzY2ItZDJjMjY5Mjk0YTli&spm=smpc.content-abroad.fd-d.22.1782059419356SgxaFMj)[锋火金生](https://mp.sohu.com/profile?xpt=ZmExMTRlNjMtMWNmZC00ZDQ2LTgzY2ItZDJjMjY5Mjk0YTli&spm=smpc.content-abroad.fd-d.22.1782059419356SgxaFMj)·今天 07:12 [0](https://www.sohu.com/a/1039604570_122535601?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.22.1782059419356SgxaFMj#comment_area)

[![文章配图-19](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1036384207_136821?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.23.1782059419356SgxaFMj)

# [大学食堂打饭大姐因身材太好被拍火出圈！网友：学校食堂居然也搞色香味俱全了](https://www.sohu.com/a/1036384207_136821?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.23.1782059419356SgxaFMj)

[![电影世界头像](https://5b0988e595225.cdn.sohucs.com/c_lfill,w_40,h_40,g_face/avatar/picon/2015/01/02/590f009394455a25127190a057a87b27android.png)](https://mp.sohu.com/profile?xpt=OTBEREE5RThERTQyNzBFMDk3MzAxRkQ3MThDMjAyRDhAcXEuc29odS5jb20=&spm=smpc.content-abroad.fd-d.23.1782059419356SgxaFMj)[电影世界](https://mp.sohu.com/profile?xpt=OTBEREE5RThERTQyNzBFMDk3MzAxRkQ3MThDMjAyRDhAcXEuc29odS5jb20=&spm=smpc.content-abroad.fd-d.23.1782059419356SgxaFMj)·06-13 23:01 [0](https://www.sohu.com/a/1036384207_136821?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.23.1782059419356SgxaFMj#comment_area)

[![文章配图-20](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038922799_122637979?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.24.1782059419356SgxaFMj)

# [快讯！没有悬念了！本届世界杯争冠格局已经明朗，冠军基本徘徊在以下四支球队：1、阿根...](https://www.sohu.com/a/1038922799_122637979?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.24.1782059419356SgxaFMj)

[![阿芜爱体育头像](https://q6.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260209/9b3817aa5bd7450b8706ddc6e18e1e61.png)](https://mp.sohu.com/profile?xpt=MGYxMTBmYmUtNDlkZS00MDVlLWE0MTMtNTczODZiNTY4NTMz&spm=smpc.content-abroad.fd-d.24.1782059419356SgxaFMj)[阿芜爱体育](https://mp.sohu.com/profile?xpt=MGYxMTBmYmUtNDlkZS00MDVlLWE0MTMtNTczODZiNTY4NTMz&spm=smpc.content-abroad.fd-d.24.1782059419356SgxaFMj)·06-19 05:29 [0](https://www.sohu.com/a/1038922799_122637979?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.24.1782059419356SgxaFMj#comment_area)

[![文章配图-21](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039432421_120020376?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.26.1782059419356SgxaFMj)

# [女人对你“暴露”这3处，就是想和你在一起，男人别不懂！](https://www.sohu.com/a/1039432421_120020376?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.26.1782059419356SgxaFMj)

[![小布点娱乐头像](https://p8.itc.cn/c_lfill,w_40,h_40,g_face/images03/20230601/ac0e174af0ed4ea4b9f24d6236f79992.jpeg)](https://mp.sohu.com/profile?xpt=ZTU2NzI3ZmUtNjhhMC00Y2FmLWIzNjQtNmE2ZjM3N2Y0MDU1&spm=smpc.content-abroad.fd-d.26.1782059419356SgxaFMj)[小布点娱乐](https://mp.sohu.com/profile?xpt=ZTU2NzI3ZmUtNjhhMC00Y2FmLWIzNjQtNmE2ZjM3N2Y0MDU1&spm=smpc.content-abroad.fd-d.26.1782059419356SgxaFMj)·昨天 22:02 [0](https://www.sohu.com/a/1039432421_120020376?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.26.1782059419356SgxaFMj#comment_area)

[![文章配图-22](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039170063_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.27.1782059419356SgxaFMj)

# [“脸都不要了！”黑龙江教师姚志荣离岗请病假25年未返岗，退休前却发现自己的编制"消失...](https://www.sohu.com/a/1039170063_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.27.1782059419356SgxaFMj)

[![史韵承传头像](https://q3.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260115/eb2b00ba50da416383dbeb52c0006fc6.jpeg)](https://mp.sohu.com/profile?xpt=YTQ4M2I2YmQtNzc1YS00YWM2LWI1MjQtNGEwN2JiNDgxN2Zh&spm=smpc.content-abroad.fd-d.27.1782059419356SgxaFMj)[史韵承传](https://mp.sohu.com/profile?xpt=YTQ4M2I2YmQtNzc1YS00YWM2LWI1MjQtNGEwN2JiNDgxN2Zh&spm=smpc.content-abroad.fd-d.27.1782059419356SgxaFMj)·06-19 23:59 [0](https://www.sohu.com/a/1039170063_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.27.1782059419356SgxaFMj#comment_area)

[![文章配图-23](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039089808_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.28.1782059419356SgxaFMj)

# [江苏南京，一女子没买东西，却收到一个快递，见姓名地址都对得上，就顺手拆开了。里头...](https://www.sohu.com/a/1039089808_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.28.1782059419356SgxaFMj)

[![壮壮科普头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260307/e380ee69319747f39e6c2cbb5d0c75e3.png)](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.28.1782059419356SgxaFMj)[壮壮科普](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.28.1782059419356SgxaFMj)·06-19 21:38 [0](https://www.sohu.com/a/1039089808_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.28.1782059419356SgxaFMj#comment_area)

[![文章配图-24](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038945353_122720060?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.29.1782059419356SgxaFMj)

# [投标人必看：避开串标废标雷区，稳稳拿下中标通知书](https://www.sohu.com/a/1038945353_122720060?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.29.1782059419356SgxaFMj)

[![古德莫宁头像](https://q7.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260415/8c178594b7f24419a59a2b0b824a64c1.jpeg)](https://mp.sohu.com/profile?xpt=NDY4YTYyODgtYTk5Zi00ZjQ4LWE2ZTktNzJiMTQyMjg1MmNi&spm=smpc.content-abroad.fd-d.29.1782059419356SgxaFMj)[古德莫宁](https://mp.sohu.com/profile?xpt=NDY4YTYyODgtYTk5Zi00ZjQ4LWE2ZTktNzJiMTQyMjg1MmNi&spm=smpc.content-abroad.fd-d.29.1782059419356SgxaFMj)·06-19 08:00 [0](https://www.sohu.com/a/1038945353_122720060?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.29.1782059419356SgxaFMj#comment_area)

[![文章配图-25](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039477664_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.31.1782059419356SgxaFMj)

# [蒙古国这位女外长，越了解越觉得有意思。一位内陆国外长，怎么把路走成这样，很多人好...](https://www.sohu.com/a/1039477664_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.31.1782059419356SgxaFMj)

[![壮壮科普头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260307/e380ee69319747f39e6c2cbb5d0c75e3.png)](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.31.1782059419356SgxaFMj)[壮壮科普](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.31.1782059419356SgxaFMj)·昨天 23:40 [0](https://www.sohu.com/a/1039477664_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.31.1782059419356SgxaFMj#comment_area)

[![文章配图-26](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039126780_122310936?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.32.1782059419356SgxaFMj)

# [6月20日：中国已经明确拒绝参加，沙特也不再捧场，王储小萨勒曼早已发现](https://www.sohu.com/a/1039126780_122310936?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.32.1782059419356SgxaFMj)

[![召诚侃娱乐头像](https://q5.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250304/59278fcd3efd4cb5ae90c79a51de7419.jpeg)](https://mp.sohu.com/profile?xpt=YWU5ODBlMDYtY2Y3Zi00NDQ3LTk5ZGEtZjI4NDJmYmJlNTBj&spm=smpc.content-abroad.fd-d.32.1782059419356SgxaFMj)[召诚侃娱乐](https://mp.sohu.com/profile?xpt=YWU5ODBlMDYtY2Y3Zi00NDQ3LTk5ZGEtZjI4NDJmYmJlNTBj&spm=smpc.content-abroad.fd-d.32.1782059419356SgxaFMj)·06-19 23:31 [0](https://www.sohu.com/a/1039126780_122310936?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.32.1782059419356SgxaFMj#comment_area)

[![文章配图-27](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039096452_122615833?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.33.1782059419356SgxaFMj)

# [中国突然宣布对车床、铣床、磨床实施全面出口管制，6月30日正式落地执行，反应最激烈的...](https://www.sohu.com/a/1039096452_122615833?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.33.1782059419356SgxaFMj)

[![国际小表妹头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260112/d519ae1b9f7b45debd18815908a6db2f.jpeg)](https://mp.sohu.com/profile?xpt=Zjc3MTQzMjQtZTExYS00YmZmLWFmNmUtNDliZTVmOTI3NjY4&spm=smpc.content-abroad.fd-d.33.1782059419356SgxaFMj)[国际小表妹](https://mp.sohu.com/profile?xpt=Zjc3MTQzMjQtZTExYS00YmZmLWFmNmUtNDliZTVmOTI3NjY4&spm=smpc.content-abroad.fd-d.33.1782059419356SgxaFMj)·06-19 21:59 [0](https://www.sohu.com/a/1039096452_122615833?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.33.1782059419356SgxaFMj#comment_area)

[![文章配图-28](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039095329_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.34.1782059419356SgxaFMj)

# [他在三年疫情期间趁机牟取“国难财”，通过核酸造假害了无数人，他的结局令人拍手称快...](https://www.sohu.com/a/1039095329_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.34.1782059419356SgxaFMj)

[![壮壮科普头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260307/e380ee69319747f39e6c2cbb5d0c75e3.png)](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.34.1782059419356SgxaFMj)[壮壮科普](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.34.1782059419356SgxaFMj)·06-19 21:50 [0](https://www.sohu.com/a/1039095329_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.34.1782059419356SgxaFMj#comment_area)

[![文章配图-29](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039212666_122496491?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.36.1782059419356SgxaFMj)

# [美国为什么在中国面前越来越没底气？一个刺痛的事实：中国最顶级的头脑去了美国，却纷...](https://www.sohu.com/a/1039212666_122496491?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.36.1782059419356SgxaFMj)

[![离笙深夜谈头像](https://q5.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250808/fa7bc917de05468dafe0f8a155a7d155.png)](https://mp.sohu.com/profile?xpt=MzY4MTBhNDktOThhOS00M2UxLTk5YTEtMzU3MmYwZGQwOGQx&spm=smpc.content-abroad.fd-d.36.1782059419356SgxaFMj)[离笙深夜谈](https://mp.sohu.com/profile?xpt=MzY4MTBhNDktOThhOS00M2UxLTk5YTEtMzU3MmYwZGQwOGQx&spm=smpc.content-abroad.fd-d.36.1782059419356SgxaFMj)·昨天 03:54 [0](https://www.sohu.com/a/1039212666_122496491?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.36.1782059419356SgxaFMj#comment_area)

[![文章配图-30](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038917712_122615833?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.37.1782059419356SgxaFMj)

# [广州白云机场深夜一幕刷屏！一个蓬头垢面的印度人，背包空空如也，躺在地上，周边丢满...](https://www.sohu.com/a/1038917712_122615833?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.37.1782059419356SgxaFMj)

[![国际小表妹头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260112/d519ae1b9f7b45debd18815908a6db2f.jpeg)](https://mp.sohu.com/profile?xpt=Zjc3MTQzMjQtZTExYS00YmZmLWFmNmUtNDliZTVmOTI3NjY4&spm=smpc.content-abroad.fd-d.37.1782059419356SgxaFMj)[国际小表妹](https://mp.sohu.com/profile?xpt=Zjc3MTQzMjQtZTExYS00YmZmLWFmNmUtNDliZTVmOTI3NjY4&spm=smpc.content-abroad.fd-d.37.1782059419356SgxaFMj)·06-19 05:11 [0](https://www.sohu.com/a/1038917712_122615833?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.37.1782059419356SgxaFMj#comment_area)

[![文章配图-31](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1032127509_121133293?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.38.1782059419356SgxaFMj)

# [生理旺盛的女性，大多有这3个特征，超准！](https://www.sohu.com/a/1032127509_121133293?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.38.1782059419356SgxaFMj)

[![婉婉情感疗愈头像](https://q1.itc.cn/c_lfill,w_40,h_40,g_face/images03/20240904/7cfbdbb5665d40b8990f5bc841af9052.jpeg)](https://mp.sohu.com/profile?xpt=NjkxZThjMDAtZWYzOS00ZjNlLTllMTYtNzgwOWMzNTlhN2I3&spm=smpc.content-abroad.fd-d.38.1782059419356SgxaFMj)[婉婉情感疗愈](https://mp.sohu.com/profile?xpt=NjkxZThjMDAtZWYzOS00ZjNlLTllMTYtNzgwOWMzNTlhN2I3&spm=smpc.content-abroad.fd-d.38.1782059419356SgxaFMj)·06-04 10:00 [0](https://www.sohu.com/a/1032127509_121133293?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.38.1782059419356SgxaFMj#comment_area)

[![文章配图-32](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039233461_122617630?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.39.1782059419356SgxaFMj)

# [奉劝所有中国人，要做好心理准备，因为央视已经说出了事实：“日本想打的不是一般小仗...](https://www.sohu.com/a/1039233461_122617630?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.39.1782059419356SgxaFMj)

[![云墨简说头像](https://q9.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260123/b9385b735745443191f6fa86bb1b15f5.jpeg)](https://mp.sohu.com/profile?xpt=NWVjZmM2YmItODIxNi00MzY2LWFhNDktYTNkZGFiMWQzZGFl&spm=smpc.content-abroad.fd-d.39.1782059419356SgxaFMj)[云墨简说](https://mp.sohu.com/profile?xpt=NWVjZmM2YmItODIxNi00MzY2LWFhNDktYTNkZGFiMWQzZGFl&spm=smpc.content-abroad.fd-d.39.1782059419356SgxaFMj)·昨天 04:32 [0](https://www.sohu.com/a/1039233461_122617630?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.39.1782059419356SgxaFMj#comment_area)

[![文章配图-33](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039212883_122496491?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.41.1782059419356SgxaFMj)

# [跪舔“美国空气香甜”的杨舒平，当年父母就坐在台下，如今改名另起名字，竟已举家整体搬迁](https://www.sohu.com/a/1039212883_122496491?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.41.1782059419356SgxaFMj)

[![离笙深夜谈头像](https://q5.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250808/fa7bc917de05468dafe0f8a155a7d155.png)](https://mp.sohu.com/profile?xpt=MzY4MTBhNDktOThhOS00M2UxLTk5YTEtMzU3MmYwZGQwOGQx&spm=smpc.content-abroad.fd-d.41.1782059419356SgxaFMj)[离笙深夜谈](https://mp.sohu.com/profile?xpt=MzY4MTBhNDktOThhOS00M2UxLTk5YTEtMzU3MmYwZGQwOGQx&spm=smpc.content-abroad.fd-d.41.1782059419356SgxaFMj)·昨天 03:55 [0](https://www.sohu.com/a/1039212883_122496491?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.41.1782059419356SgxaFMj#comment_area)

[![文章配图-34](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038865441_120020434?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.42.1782059419356SgxaFMj)

# [适合一个人观看的经典电影免费](https://www.sohu.com/a/1038865441_120020434?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.42.1782059419356SgxaFMj)

[![大马猴说娱乐头像](https://p8.itc.cn/c_lfill,w_40,h_40,g_face/images03/20230601/ae2ede65c41f406c852dd3259c5d75b0.jpeg)](https://mp.sohu.com/profile?xpt=NGEzZWJiYjQtY2MxMS00YWU2LThkNDUtZmUwNjY3ZTUwMDA2&spm=smpc.content-abroad.fd-d.42.1782059419356SgxaFMj)[大马猴说娱乐](https://mp.sohu.com/profile?xpt=NGEzZWJiYjQtY2MxMS00YWU2LThkNDUtZmUwNjY3ZTUwMDA2&spm=smpc.content-abroad.fd-d.42.1782059419356SgxaFMj)·06-19 03:06 [0](https://www.sohu.com/a/1038865441_120020434?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.42.1782059419356SgxaFMj#comment_area)

[![文章配图-35](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038870359_122277364?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.43.1782059419356SgxaFMj)

# [“成人网站”上的女生，到底是怎样被偷拍的？女生一定要小心了！](https://www.sohu.com/a/1038870359_122277364?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.43.1782059419356SgxaFMj)

[![孟鑫看世界头像](https://q3.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250219/7881eb10678d48fe891647fd1a768cda.jpeg)](https://mp.sohu.com/profile?xpt=ODNlOWRlYjEtYTYwMC00ZTYwLWE0NDctOGVkMmJmMTViNmUw&spm=smpc.content-abroad.fd-d.43.1782059419356SgxaFMj)[孟鑫看世界](https://mp.sohu.com/profile?xpt=ODNlOWRlYjEtYTYwMC00ZTYwLWE0NDctOGVkMmJmMTViNmUw&spm=smpc.content-abroad.fd-d.43.1782059419356SgxaFMj)·06-19 03:24 [0](https://www.sohu.com/a/1038870359_122277364?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.43.1782059419356SgxaFMj#comment_area)

[![文章配图-36](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1035179553_122786724?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.44.1782059419356SgxaFMj)

# [同床时身材高大丰满的女人，大多命里带福，这6个特质很明显](https://www.sohu.com/a/1035179553_122786724?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.44.1782059419356SgxaFMj)

[![美美聊情感头像](https://q5.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260509/45dea367d0654cd58249f46aee4ce7a6.jpeg)](https://mp.sohu.com/profile?xpt=MmFmM2RjMTUtMGFiNy00MTliLWJlYjQtODBmODEyNmUxMGE3&spm=smpc.content-abroad.fd-d.44.1782059419356SgxaFMj)[美美聊情感](https://mp.sohu.com/profile?xpt=MmFmM2RjMTUtMGFiNy00MTliLWJlYjQtODBmODEyNmUxMGE3&spm=smpc.content-abroad.fd-d.44.1782059419356SgxaFMj)·06-11 01:44 [0](https://www.sohu.com/a/1035179553_122786724?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.44.1782059419356SgxaFMj#comment_area)

[![文章配图-37](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039103063_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.46.1782059419356SgxaFMj)

# [“人民花不了人民币！”广东广州，一男子拿着几万现金，去银行提前还车贷，柜员先是让...](https://www.sohu.com/a/1039103063_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.46.1782059419356SgxaFMj)

[![壮壮科普头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260307/e380ee69319747f39e6c2cbb5d0c75e3.png)](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.46.1782059419356SgxaFMj)[壮壮科普](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.46.1782059419356SgxaFMj)·06-19 22:00 [0](https://www.sohu.com/a/1039103063_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.46.1782059419356SgxaFMj#comment_area)

[![文章配图-38](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038774108_120020376?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.47.1782059419356SgxaFMj)

# [汤唯在《色戒》中的牺牲，远不止那几个镜头，金星都为她鸣不平](https://www.sohu.com/a/1038774108_120020376?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.47.1782059419356SgxaFMj)

[![小布点娱乐头像](https://p8.itc.cn/c_lfill,w_40,h_40,g_face/images03/20230601/ac0e174af0ed4ea4b9f24d6236f79992.jpeg)](https://mp.sohu.com/profile?xpt=ZTU2NzI3ZmUtNjhhMC00Y2FmLWIzNjQtNmE2ZjM3N2Y0MDU1&spm=smpc.content-abroad.fd-d.47.1782059419356SgxaFMj)[小布点娱乐](https://mp.sohu.com/profile?xpt=ZTU2NzI3ZmUtNjhhMC00Y2FmLWIzNjQtNmE2ZjM3N2Y0MDU1&spm=smpc.content-abroad.fd-d.47.1782059419356SgxaFMj)·06-18 23:01 [0](https://www.sohu.com/a/1038774108_120020376?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.47.1782059419356SgxaFMj#comment_area)

[![文章配图-39](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038886880_122407853?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.48.1782059419356SgxaFMj)

# [本轮房价下跌史上罕见，将成为历史性的国民伤痛！远超想象！](https://www.sohu.com/a/1038886880_122407853?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.48.1782059419356SgxaFMj)

[![奇史妙想家头像](https://q7.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250422/626b0fc708de483cb9b93931bb432ff7.png)](https://mp.sohu.com/profile?xpt=YzFhMGZkNzktYjlmNi00NzI4LTk1YzgtODBiZDE4Y2NhNDZm&spm=smpc.content-abroad.fd-d.48.1782059419356SgxaFMj)[奇史妙想家](https://mp.sohu.com/profile?xpt=YzFhMGZkNzktYjlmNi00NzI4LTk1YzgtODBiZDE4Y2NhNDZm&spm=smpc.content-abroad.fd-d.48.1782059419356SgxaFMj)·06-19 04:10 [0](https://www.sohu.com/a/1038886880_122407853?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.48.1782059419356SgxaFMj#comment_area)

[![文章配图-40](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039161375_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.49.1782059419356SgxaFMj)

# [你敢信吗？G7峰会上发生了这么戏剧性的一幕。欧盟主席冯德莱恩专门掏出来一块磁铁，当...](https://www.sohu.com/a/1039161375_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.49.1782059419356SgxaFMj)

[![史韵承传头像](https://q3.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260115/eb2b00ba50da416383dbeb52c0006fc6.jpeg)](https://mp.sohu.com/profile?xpt=YTQ4M2I2YmQtNzc1YS00YWM2LWI1MjQtNGEwN2JiNDgxN2Zh&spm=smpc.content-abroad.fd-d.49.1782059419356SgxaFMj)[史韵承传](https://mp.sohu.com/profile?xpt=YTQ4M2I2YmQtNzc1YS00YWM2LWI1MjQtNGEwN2JiNDgxN2Zh&spm=smpc.content-abroad.fd-d.49.1782059419356SgxaFMj)·06-19 23:41 [0](https://www.sohu.com/a/1039161375_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.49.1782059419356SgxaFMj#comment_area)

[![文章配图-41](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039603694_122745403?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.51.1782059419356SgxaFMj)

# [女人的8个小秘密，男人越早知道越好](https://www.sohu.com/a/1039603694_122745403?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.51.1782059419356SgxaFMj)

[![凭凭头像](https://q7.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260424/d12e9102fa66462b95fb68ca382d9473.png)](https://mp.sohu.com/profile?xpt=M2E2YTk2YTItZjNmYy00NjE4LWIwNTMtMDI3Nzg2N2Y3Zjhl&spm=smpc.content-abroad.fd-d.51.1782059419356SgxaFMj)[凭凭](https://mp.sohu.com/profile?xpt=M2E2YTk2YTItZjNmYy00NjE4LWIwNTMtMDI3Nzg2N2Y3Zjhl&spm=smpc.content-abroad.fd-d.51.1782059419356SgxaFMj)·今天 06:43 [0](https://www.sohu.com/a/1039603694_122745403?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.51.1782059419356SgxaFMj#comment_area)

[![文章配图-42](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039523119_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.52.1782059419356SgxaFMj)

# [“真是闻所未闻！”自家办丧事大摆三天流水席，席间混进来五个完全陌生的外人，大吃大...](https://www.sohu.com/a/1039523119_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.52.1782059419356SgxaFMj)

[![壮壮科普头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260307/e380ee69319747f39e6c2cbb5d0c75e3.png)](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.52.1782059419356SgxaFMj)[壮壮科普](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.52.1782059419356SgxaFMj)·今天 02:28 [0](https://www.sohu.com/a/1039523119_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.52.1782059419356SgxaFMj#comment_area)

[![文章配图-43](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039260009_100934?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.53.1782059419356SgxaFMj)

# [复旦大学教授王德峰，撕开了中国社会当下最大的遮羞布，振聋发聩？](https://www.sohu.com/a/1039260009_100934?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.53.1782059419356SgxaFMj)

[![校长传媒头像](https://sucimg.itc.cn/avatarimg/2de9c41c7d4c427ca0eda399283849c8_1424609483286)](https://mp.sohu.com/profile?xpt=MTY3ODc1ODExMUBzaW5hLnNvaHUuY29t&spm=smpc.content-abroad.fd-d.53.1782059419356SgxaFMj)[校长传媒](https://mp.sohu.com/profile?xpt=MTY3ODc1ODExMUBzaW5hLnNvaHUuY29t&spm=smpc.content-abroad.fd-d.53.1782059419356SgxaFMj)·昨天 06:33 [0](https://www.sohu.com/a/1039260009_100934?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.53.1782059419356SgxaFMj#comment_area)

[![文章配图-44](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1026254627_122471276?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.54.1782059419356SgxaFMj)

# [卷巨额遗产出逃英国，给杨振宁戴绿帽子，翁帆身上的谣言太离谱了](https://www.sohu.com/a/1026254627_122471276?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.54.1782059419356SgxaFMj)

[![貂蝉科普头像](https://q0.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250707/d163de413cd745e68e5a9c2c06f46ad8.jpeg)](https://mp.sohu.com/profile?xpt=YjQ2N2UwN2EtNGI0Mi00YjQxLTg2YzQtNzA1OWI1NDE0OTVk&spm=smpc.content-abroad.fd-d.54.1782059419356SgxaFMj)[貂蝉科普](https://mp.sohu.com/profile?xpt=YjQ2N2UwN2EtNGI0Mi00YjQxLTg2YzQtNzA1OWI1NDE0OTVk&spm=smpc.content-abroad.fd-d.54.1782059419356SgxaFMj)·05-22 05:06 [0](https://www.sohu.com/a/1026254627_122471276?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.54.1782059419356SgxaFMj#comment_area)

[![文章配图-45](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038170198_122018249?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.56.1782059419356SgxaFMj)

# [保安“立功”了！佛山一餐饮店驱赶躲雨母子，网友：认同他的做法](https://www.sohu.com/a/1038170198_122018249?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.56.1782059419356SgxaFMj)

[![云中浮生头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250917/dd392d8194804adb9b7f2a7c09abc36f.jpeg)](https://mp.sohu.com/profile?xpt=N2I2OGRjMTUtNzRmNy00MWE2LWJlMjgtZDM4NTkxMzgxZmVi&spm=smpc.content-abroad.fd-d.56.1782059419356SgxaFMj)[云中浮生](https://mp.sohu.com/profile?xpt=N2I2OGRjMTUtNzRmNy00MWE2LWJlMjgtZDM4NTkxMzgxZmVi&spm=smpc.content-abroad.fd-d.56.1782059419356SgxaFMj)·06-17 20:19 [0](https://www.sohu.com/a/1038170198_122018249?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.56.1782059419356SgxaFMj#comment_area)

[![文章配图-46](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039187861_122542955?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.57.1782059419356SgxaFMj)

# [一旦台海冲突爆发，西方可冻结3.2万亿中国资产，但中国有1张王牌](https://www.sohu.com/a/1039187861_122542955?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.57.1782059419356SgxaFMj)

[![凯道前进九六甲头像](https://q0.itc.cn/c_lfill,w_40,h_40,g_face/images03/20251017/da54bc65dac94fa287fcd34065670016.png)](https://mp.sohu.com/profile?xpt=NzZhOWNiMjItZTc5OC00OWZmLWE4MjItZDU3MDgxNjc5ZTE0&spm=smpc.content-abroad.fd-d.57.1782059419356SgxaFMj)[凯道前进九六甲](https://mp.sohu.com/profile?xpt=NzZhOWNiMjItZTc5OC00OWZmLWE4MjItZDU3MDgxNjc5ZTE0&spm=smpc.content-abroad.fd-d.57.1782059419356SgxaFMj)·昨天 02:42 [0](https://www.sohu.com/a/1039187861_122542955?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.57.1782059419356SgxaFMj#comment_area)

[![文章配图-47](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039175300_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.58.1782059419356SgxaFMj)

# [明明是强国，为何国足可以这么差？答案不在14亿人里选不出11个会踢球的，而在于那11个...](https://www.sohu.com/a/1039175300_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.58.1782059419356SgxaFMj)

[![史韵承传头像](https://q3.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260115/eb2b00ba50da416383dbeb52c0006fc6.jpeg)](https://mp.sohu.com/profile?xpt=YTQ4M2I2YmQtNzc1YS00YWM2LWI1MjQtNGEwN2JiNDgxN2Zh&spm=smpc.content-abroad.fd-d.58.1782059419356SgxaFMj)[史韵承传](https://mp.sohu.com/profile?xpt=YTQ4M2I2YmQtNzc1YS00YWM2LWI1MjQtNGEwN2JiNDgxN2Zh&spm=smpc.content-abroad.fd-d.58.1782059419356SgxaFMj)·06-19 23:51 [0](https://www.sohu.com/a/1039175300_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.58.1782059419356SgxaFMj#comment_area)

[![文章配图-48](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1036942397_122542758?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.59.1782059419356SgxaFMj)

# [聂海胜妻子：在丈夫上太空前提出离婚，保密生活隐藏了多少辛酸？](https://www.sohu.com/a/1036942397_122542758?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.59.1782059419356SgxaFMj)

[![南书房V头像](https://q1.itc.cn/c_lfill,w_40,h_40,g_face/images03/20251016/177a9ecdb9c8486a950c56b470261c9b.png)](https://mp.sohu.com/profile?xpt=YjJlN2FiZDItZWMwMi00NTM1LWIxZTktNTQxMDY4OWU4MmFh&spm=smpc.content-abroad.fd-d.59.1782059419356SgxaFMj)[南书房V](https://mp.sohu.com/profile?xpt=YjJlN2FiZDItZWMwMi00NTM1LWIxZTktNTQxMDY4OWU4MmFh&spm=smpc.content-abroad.fd-d.59.1782059419356SgxaFMj)·06-15 06:13 [0](https://www.sohu.com/a/1036942397_122542758?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.59.1782059419356SgxaFMj#comment_area)

[![文章配图-49](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039273742_122897878?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.61.1782059419356SgxaFMj)

# [“这就是命啊！”6月2日，海南澄迈，两名渔民出海寻找被冲散的泡沫浮具，在距离岸边大...](https://www.sohu.com/a/1039273742_122897878?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.61.1782059419356SgxaFMj)

[![观察者说案头像](https://q0.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260613/3864ac3aae0142b4b81df3861e969196.jpeg)](https://mp.sohu.com/profile?xpt=YWZmNWE0ZTEtMzE5NS00YmYzLWExZmQtNjJjZTljZGM4NDQ1&spm=smpc.content-abroad.fd-d.61.1782059419356SgxaFMj)[观察者说案](https://mp.sohu.com/profile?xpt=YWZmNWE0ZTEtMzE5NS00YmYzLWExZmQtNjJjZTljZGM4NDQ1&spm=smpc.content-abroad.fd-d.61.1782059419356SgxaFMj)·昨天 07:30 [0](https://www.sohu.com/a/1039273742_122897878?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.61.1782059419356SgxaFMj#comment_area)

[![文章配图-50](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1037005788_100243004?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.62.1782059419356SgxaFMj)

# [两性交往，女人说“我去洗澡了”，其实就是在告诉你这3件事情](https://www.sohu.com/a/1037005788_100243004?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.62.1782059419356SgxaFMj)

[![郝评头像](https://p3.itc.cn/c_lfill,w_40,h_40,g_face/images03/20231221/81f79b9ccac243f68fd059dd12668255.jpeg)](https://mp.sohu.com/profile?xpt=MTAyNjI4NzExMjY5OTQ5NDQwMEBzb2h1LmNvbQ==&spm=smpc.content-abroad.fd-d.62.1782059419356SgxaFMj)[郝评](https://mp.sohu.com/profile?xpt=MTAyNjI4NzExMjY5OTQ5NDQwMEBzb2h1LmNvbQ==&spm=smpc.content-abroad.fd-d.62.1782059419356SgxaFMj)·06-15 09:36 [0](https://www.sohu.com/a/1037005788_100243004?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.62.1782059419356SgxaFMj#comment_area)

[![文章配图-51](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038996190_122481126?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.63.1782059419356SgxaFMj)

# [历史要毁于一旦？蒙古国，正在把中国40年的努力毁掉！](https://www.sohu.com/a/1038996190_122481126?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.63.1782059419356SgxaFMj)

[![热情的逗狐狸头像](https://q9.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250720/a291f2758345459aac1df5e136998bea.png)](https://mp.sohu.com/profile?xpt=MjkyN2U1MzQtZTUzNC00OTUwLTkzMmItMjZhMjdiZjFiZGU3&spm=smpc.content-abroad.fd-d.63.1782059419356SgxaFMj)[热情的逗狐狸](https://mp.sohu.com/profile?xpt=MjkyN2U1MzQtZTUzNC00OTUwLTkzMmItMjZhMjdiZjFiZGU3&spm=smpc.content-abroad.fd-d.63.1782059419356SgxaFMj)·06-19 12:42 [0](https://www.sohu.com/a/1038996190_122481126?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.63.1782059419356SgxaFMj#comment_area)

[![文章配图-52](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038940171_122225755?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.64.1782059419356SgxaFMj)

# [别买了！一级致癌物超标近900倍？医生：这东西再便宜也别往家带](https://www.sohu.com/a/1038940171_122225755?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.64.1782059419356SgxaFMj)

[![心灵书舫头像](https://q5.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250414/2daaa53daa5243e594017ff16984db62.jpeg)](https://mp.sohu.com/profile?xpt=ODdjYzI1ZGItMTM2Zi00OTEwLTkyZjItYTQ1YmI1YmIxZWZl&spm=smpc.content-abroad.fd-d.64.1782059419356SgxaFMj)[心灵书舫](https://mp.sohu.com/profile?xpt=ODdjYzI1ZGItMTM2Zi00OTEwLTkyZjItYTQ1YmI1YmIxZWZl&spm=smpc.content-abroad.fd-d.64.1782059419356SgxaFMj)·06-19 07:03 [0](https://www.sohu.com/a/1038940171_122225755?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.64.1782059419356SgxaFMj#comment_area)

[![文章配图-53](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039652859_122603047?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.66.1782059419356SgxaFMj)

# [免费绿豆汤被一人薅空！顾客嚣张回怼：做不起生意就别免费](https://www.sohu.com/a/1039652859_122603047?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.66.1782059419356SgxaFMj)

[![浠浠说道头像](https://q1.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260116/94376d6ffd4549afa991fbe56bc67d01.jpeg)](https://mp.sohu.com/profile?xpt=MmE3MzgyNWEtNmU3Zi00NDU5LTk4ODgtNTY3MGQ2YjZmYjIy&spm=smpc.content-abroad.fd-d.66.1782059419356SgxaFMj)[浠浠说道](https://mp.sohu.com/profile?xpt=MmE3MzgyNWEtNmU3Zi00NDU5LTk4ODgtNTY3MGQ2YjZmYjIy&spm=smpc.content-abroad.fd-d.66.1782059419356SgxaFMj)·今天 12:06 [0](https://www.sohu.com/a/1039652859_122603047?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.66.1782059419356SgxaFMj#comment_area)

[![文章配图-54](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039071413_122014422?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.67.1782059419356SgxaFMj)

# [中缅重大突破！云南人等了几百年的出海口，这次真的来了](https://www.sohu.com/a/1039071413_122014422?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.67.1782059419356SgxaFMj)

[![新浪财经头像](https://q9.itc.cn/c_lfill,w_40,h_40,g_face/images03/20240801/d3b810733621472dbd9b6aec36b7e92b.png)](https://mp.sohu.com/profile?xpt=ZTliZTM5ZTMtNzAzMi00OTgzLThiNWUtNmEzNmYzZTI3N2I5&spm=smpc.content-abroad.fd-d.67.1782059419356SgxaFMj)[新浪财经](https://mp.sohu.com/profile?xpt=ZTliZTM5ZTMtNzAzMi00OTgzLThiNWUtNmEzNmYzZTI3N2I5&spm=smpc.content-abroad.fd-d.67.1782059419356SgxaFMj)·06-19 20:39 [0](https://www.sohu.com/a/1039071413_122014422?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.67.1782059419356SgxaFMj#comment_area)

[![文章配图-55](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1016216467_122483413?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.68.1782059419356SgxaFMj)

# [为什么天安门不悬挂毛主席的照片，反倒要挂主席的画像？](https://www.sohu.com/a/1016216467_122483413?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.68.1782059419356SgxaFMj)

[![天下有锦头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250720/4cba1898fed84334a369e3029de20272.png)](https://mp.sohu.com/profile?xpt=MTE0NDIyMzEtZDVjOS00OWMwLTkzNmUtMjQ5MTUzYTZlZTRl&spm=smpc.content-abroad.fd-d.68.1782059419356SgxaFMj)[天下有锦](https://mp.sohu.com/profile?xpt=MTE0NDIyMzEtZDVjOS00OWMwLTkzNmUtMjQ5MTUzYTZlZTRl&spm=smpc.content-abroad.fd-d.68.1782059419356SgxaFMj)·04-29 02:13 [0](https://www.sohu.com/a/1016216467_122483413?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.68.1782059419356SgxaFMj#comment_area)

[![文章配图-56](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039353012_122850720?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.69.1782059419356SgxaFMj)

# [当废旧电机堆积如山，如何高效回收铜线并提升价值？聊聊定子扒铜机](https://www.sohu.com/a/1039353012_122850720?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.69.1782059419356SgxaFMj)

[![济宁富矿机械设备头像](https://q7.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260525/5ad41bd37e3b4c92b1dfafe4a3c0d366.png)](https://mp.sohu.com/profile?xpt=MzczY2I2NjYtMmI5MC00OTkwLWEzY2QtODFhMDQzNWQ1MTMx&spm=smpc.content-abroad.fd-d.69.1782059419356SgxaFMj)[济宁富矿机械设备](https://mp.sohu.com/profile?xpt=MzczY2I2NjYtMmI5MC00OTkwLWEzY2QtODFhMDQzNWQ1MTMx&spm=smpc.content-abroad.fd-d.69.1782059419356SgxaFMj)·昨天 15:58 [0](https://www.sohu.com/a/1039353012_122850720?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.69.1782059419356SgxaFMj#comment_area)

[![文章配图-57](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039429005_122380346?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.71.1782059419356SgxaFMj)

# [韩国网友提问，既然中国如此强大，那为什么不敢与韩国开战？](https://www.sohu.com/a/1039429005_122380346?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.71.1782059419356SgxaFMj)

[![纪霏动漫说头像](https://q6.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250401/52a20ddaea27452b8e875744f080e368.jpeg)](https://mp.sohu.com/profile?xpt=MjI3NTA2ODQtODE0Ni00NjY3LWE3ZTUtOThkM2ExNDExMDIw&spm=smpc.content-abroad.fd-d.71.1782059419356SgxaFMj)[纪霏动漫说](https://mp.sohu.com/profile?xpt=MjI3NTA2ODQtODE0Ni00NjY3LWE3ZTUtOThkM2ExNDExMDIw&spm=smpc.content-abroad.fd-d.71.1782059419356SgxaFMj)·今天 00:25 [0](https://www.sohu.com/a/1039429005_122380346?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.71.1782059419356SgxaFMj#comment_area)

[![文章配图-58](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1030595810_122415103?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.72.1782059419356SgxaFMj)

# [善恶终有报！放弃国籍、贬低中国，68岁瘫在轮椅的张铁林活成笑话](https://www.sohu.com/a/1030595810_122415103?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.72.1782059419356SgxaFMj)

[![云梦说娱头像](https://q3.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250430/cd27eeccc0a3423f85b4718fb3c508fa.png)](https://mp.sohu.com/profile?xpt=ODhkYTVkZTYtZWU3ZS00MGM3LWI5ZDctN2E0N2U5ZmU3OTM5&spm=smpc.content-abroad.fd-d.72.1782059419356SgxaFMj)[云梦说娱](https://mp.sohu.com/profile?xpt=ODhkYTVkZTYtZWU3ZS00MGM3LWI5ZDctN2E0N2U5ZmU3OTM5&spm=smpc.content-abroad.fd-d.72.1782059419356SgxaFMj)·06-01 03:57 [0](https://www.sohu.com/a/1030595810_122415103?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.72.1782059419356SgxaFMj#comment_area)

[![文章配图-59](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1026600990_122407939?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.73.1782059419356SgxaFMj)

# [白开水再次被点名！研究发现：喝得越多，肾功能衰竭速度越快？](https://www.sohu.com/a/1026600990_122407939?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.73.1782059419356SgxaFMj)

[![直言说头像](https://q1.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250422/15d137af2cf34cb9b286d309bfe93ae7.png)](https://mp.sohu.com/profile?xpt=MDgxNmYzMzYtMjkwOC00ZjNhLWE4NWYtZDlkNDdiZjkyYjAy&spm=smpc.content-abroad.fd-d.73.1782059419356SgxaFMj)[直言说](https://mp.sohu.com/profile?xpt=MDgxNmYzMzYtMjkwOC00ZjNhLWE4NWYtZDlkNDdiZjkyYjAy&spm=smpc.content-abroad.fd-d.73.1782059419356SgxaFMj)·05-23 02:27 [0](https://www.sohu.com/a/1026600990_122407939?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.73.1782059419356SgxaFMj#comment_area)

[![文章配图-60](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039573212_122496491?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.74.1782059419356SgxaFMj)

# [综合多方传出的信号来看，中国大概率早已推演过俄乌冲突最坏局面，预判到俄罗斯若长期...](https://www.sohu.com/a/1039573212_122496491?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.74.1782059419356SgxaFMj)

[![离笙深夜谈头像](https://q5.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250808/fa7bc917de05468dafe0f8a155a7d155.png)](https://mp.sohu.com/profile?xpt=MzY4MTBhNDktOThhOS00M2UxLTk5YTEtMzU3MmYwZGQwOGQx&spm=smpc.content-abroad.fd-d.74.1782059419356SgxaFMj)[离笙深夜谈](https://mp.sohu.com/profile?xpt=MzY4MTBhNDktOThhOS00M2UxLTk5YTEtMzU3MmYwZGQwOGQx&spm=smpc.content-abroad.fd-d.74.1782059419356SgxaFMj)·今天 05:27 [0](https://www.sohu.com/a/1039573212_122496491?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.74.1782059419356SgxaFMj#comment_area)

[![文章配图-61](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038396125_665455?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.76.1782059419356SgxaFMj)

# [“抬棺送葬”公职人员被处理，乡土人情里没输家](https://www.sohu.com/a/1038396125_665455?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.76.1782059419356SgxaFMj)

[![狐度头像](https://sucimg.itc.cn/avatarimg/1b15a55f73cc4b148bb6a1105a1fdbcb_1530521060287)](http://mp.sohu.com/profile?xpt=bGFubGFuZGUyMkBzb2h1LmNvbQ==&spm=smpc.content-abroad.fd-d.76.1782059419356SgxaFMj)[狐度](http://mp.sohu.com/profile?xpt=bGFubGFuZGUyMkBzb2h1LmNvbQ==&spm=smpc.content-abroad.fd-d.76.1782059419356SgxaFMj)·06-18 03:12 [0](https://www.sohu.com/a/1038396125_665455?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.76.1782059419356SgxaFMj#comment_area)

[![文章配图-62](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038434621_122499133?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.77.1782059419356SgxaFMj)

# [62岁的董事长迎娶26岁的女员工，婚礼现场管59岁的岳父叫爸爸](https://www.sohu.com/a/1038434621_122499133?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.77.1782059419356SgxaFMj)

[![民间故事屋头像](https://q3.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250809/7028ae64a58f499583c121c8347a0a2d.png)](https://mp.sohu.com/profile?xpt=ZDAxYTBjOTUtOGUzYS00MTM2LTg1NTktODhjMTliZDRhMDAy&spm=smpc.content-abroad.fd-d.77.1782059419356SgxaFMj)[民间故事屋](https://mp.sohu.com/profile?xpt=ZDAxYTBjOTUtOGUzYS00MTM2LTg1NTktODhjMTliZDRhMDAy&spm=smpc.content-abroad.fd-d.77.1782059419356SgxaFMj)·06-18 04:08 [0](https://www.sohu.com/a/1038434621_122499133?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.77.1782059419356SgxaFMj#comment_area)

[![文章配图-63](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039265088_122639510?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.78.1782059419356SgxaFMj)

# [北京，男子在家中吃了麻酱拌面，上吐下泻，他及时就医，身体却越来越糟糕，最终离世，...](https://www.sohu.com/a/1039265088_122639510?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.78.1782059419356SgxaFMj)

[![史前记序头像](https://q6.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260213/49e25e06b43c4b5fa6e32cb0115349c8.png)](https://mp.sohu.com/profile?xpt=NmNkYWY1NTctNTkyNC00YWI5LWIwYjgtNjhiYmUxOTYzYTkx&spm=smpc.content-abroad.fd-d.78.1782059419356SgxaFMj)[史前记序](https://mp.sohu.com/profile?xpt=NmNkYWY1NTctNTkyNC00YWI5LWIwYjgtNjhiYmUxOTYzYTkx&spm=smpc.content-abroad.fd-d.78.1782059419356SgxaFMj)·昨天 06:55 [0](https://www.sohu.com/a/1039265088_122639510?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.78.1782059419356SgxaFMj#comment_area)

[![文章配图-64](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039165725_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.79.1782059419356SgxaFMj)

# [折腾几十年又回归老路子，是进步还是倒退？现在不少央企都开始自己组建施工队伍了，不...](https://www.sohu.com/a/1039165725_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.79.1782059419356SgxaFMj)

[![史韵承传头像](https://q3.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260115/eb2b00ba50da416383dbeb52c0006fc6.jpeg)](https://mp.sohu.com/profile?xpt=YTQ4M2I2YmQtNzc1YS00YWM2LWI1MjQtNGEwN2JiNDgxN2Zh&spm=smpc.content-abroad.fd-d.79.1782059419356SgxaFMj)[史韵承传](https://mp.sohu.com/profile?xpt=YTQ4M2I2YmQtNzc1YS00YWM2LWI1MjQtNGEwN2JiNDgxN2Zh&spm=smpc.content-abroad.fd-d.79.1782059419356SgxaFMj)·06-19 23:47 [0](https://www.sohu.com/a/1039165725_122614893?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.79.1782059419356SgxaFMj#comment_area)

[![文章配图-65](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039095279_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.81.1782059419356SgxaFMj)

# [24小时不到，佩泽希齐扬对穆杰塔巴态度大变！从之前6次发声的绝对服从，到现在要和穆...](https://www.sohu.com/a/1039095279_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.81.1782059419356SgxaFMj)

[![壮壮科普头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260307/e380ee69319747f39e6c2cbb5d0c75e3.png)](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.81.1782059419356SgxaFMj)[壮壮科普](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.81.1782059419356SgxaFMj)·06-19 21:48 [0](https://www.sohu.com/a/1039095279_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.81.1782059419356SgxaFMj#comment_area)

[![文章配图-66](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039233603_122617630?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.82.1782059419356SgxaFMj)

# [海外华人发声：现在国家日子好过了，能不能把缅甸、泰国、马来西亚、印尼那边受苦的华...](https://www.sohu.com/a/1039233603_122617630?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.82.1782059419356SgxaFMj)

[![云墨简说头像](https://q9.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260123/b9385b735745443191f6fa86bb1b15f5.jpeg)](https://mp.sohu.com/profile?xpt=NWVjZmM2YmItODIxNi00MzY2LWFhNDktYTNkZGFiMWQzZGFl&spm=smpc.content-abroad.fd-d.82.1782059419356SgxaFMj)[云墨简说](https://mp.sohu.com/profile?xpt=NWVjZmM2YmItODIxNi00MzY2LWFhNDktYTNkZGFiMWQzZGFl&spm=smpc.content-abroad.fd-d.82.1782059419356SgxaFMj)·昨天 04:33 [0](https://www.sohu.com/a/1039233603_122617630?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.82.1782059419356SgxaFMj#comment_area)

[![文章配图-67](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039218621_122542758?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.83.1782059419356SgxaFMj)

# [开国上将视察重庆，看到一剃头匠，激动大喊道：司令，你怎么在这](https://www.sohu.com/a/1039218621_122542758?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.83.1782059419356SgxaFMj)

[![南书房V头像](https://q1.itc.cn/c_lfill,w_40,h_40,g_face/images03/20251016/177a9ecdb9c8486a950c56b470261c9b.png)](https://mp.sohu.com/profile?xpt=YjJlN2FiZDItZWMwMi00NTM1LWIxZTktNTQxMDY4OWU4MmFh&spm=smpc.content-abroad.fd-d.83.1782059419356SgxaFMj)[南书房V](https://mp.sohu.com/profile?xpt=YjJlN2FiZDItZWMwMi00NTM1LWIxZTktNTQxMDY4OWU4MmFh&spm=smpc.content-abroad.fd-d.83.1782059419356SgxaFMj)·昨天 04:12 [0](https://www.sohu.com/a/1039218621_122542758?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.83.1782059419356SgxaFMj#comment_area)

[![文章配图-68](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038993735_122662928?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.84.1782059419356SgxaFMj)

# [6月20日：中国没打一枪一炮，赢得了一场大胜，全世界在看中方不怒自威](https://www.sohu.com/a/1038993735_122662928?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.84.1782059419356SgxaFMj)

[![元槐说历史头像](https://q3.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260313/b118330d60bd48d3a285e919d2d6a375.jpeg)](https://mp.sohu.com/profile?xpt=ODgzNDY1OGYtMTk0NS00YWJjLTg0OTgtOGU4OGI5N2I5Yzgw&spm=smpc.content-abroad.fd-d.84.1782059419356SgxaFMj)[元槐说历史](https://mp.sohu.com/profile?xpt=ODgzNDY1OGYtMTk0NS00YWJjLTg0OTgtOGU4OGI5N2I5Yzgw&spm=smpc.content-abroad.fd-d.84.1782059419356SgxaFMj)·06-19 12:41 [0](https://www.sohu.com/a/1038993735_122662928?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.84.1782059419356SgxaFMj#comment_area)

[![文章配图-69](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1030626805_121125734?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.86.1782059419356SgxaFMj)

# [华中工学院更名为华中理工大学后，为何又改名为华中科技大学呢](https://www.sohu.com/a/1030626805_121125734?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.86.1782059419356SgxaFMj)

[![快活大武汉头像](https://p3.itc.cn/c_lfill,w_40,h_40,g_face/images03/20230322/4d72d51e01c043cfb02ecaa716228923.jpeg)](https://mp.sohu.com/profile?xpt=ZDc4ZWM0OTMtODI2MS00NTQwLTk5M2UtMTk0YmJmNjhlMTg2&spm=smpc.content-abroad.fd-d.86.1782059419356SgxaFMj)[快活大武汉](https://mp.sohu.com/profile?xpt=ZDc4ZWM0OTMtODI2MS00NTQwLTk5M2UtMTk0YmJmNjhlMTg2&spm=smpc.content-abroad.fd-d.86.1782059419356SgxaFMj)·06-01 05:00 [0](https://www.sohu.com/a/1030626805_121125734?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.86.1782059419356SgxaFMj#comment_area)

[![文章配图-70](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038770437_121161793?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.87.1782059419356SgxaFMj)

# [印度街头摆摊的姑娘，所贩卖的东西，为何中国男性不敢直视？](https://www.sohu.com/a/1038770437_121161793?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.87.1782059419356SgxaFMj)

[![冰点历史V头像](https://p6.itc.cn/c_lfill,w_40,h_40,g_face/mpbp/pro/20220708/f3b33e283a314ba598ea84669e219860.png)](https://mp.sohu.com/profile?xpt=YTAxZTcwMmUtZTEzNC00ZTM5LTlhNzgtZmIwNjJiMDFjOTYz&spm=smpc.content-abroad.fd-d.87.1782059419356SgxaFMj)[冰点历史V](https://mp.sohu.com/profile?xpt=YTAxZTcwMmUtZTEzNC00ZTM5LTlhNzgtZmIwNjJiMDFjOTYz&spm=smpc.content-abroad.fd-d.87.1782059419356SgxaFMj)·06-18 22:47 [0](https://www.sohu.com/a/1038770437_121161793?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.87.1782059419356SgxaFMj#comment_area)

[![文章配图-71](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1036795793_122786724?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.88.1782059419356SgxaFMj)

# [高质量的性生活，不在时长，而在于结束后的那个拥抱，太真实了](https://www.sohu.com/a/1036795793_122786724?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.88.1782059419356SgxaFMj)

[![美美聊情感头像](https://q5.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260509/45dea367d0654cd58249f46aee4ce7a6.jpeg)](https://mp.sohu.com/profile?xpt=MmFmM2RjMTUtMGFiNy00MTliLWJlYjQtODBmODEyNmUxMGE3&spm=smpc.content-abroad.fd-d.88.1782059419356SgxaFMj)[美美聊情感](https://mp.sohu.com/profile?xpt=MmFmM2RjMTUtMGFiNy00MTliLWJlYjQtODBmODEyNmUxMGE3&spm=smpc.content-abroad.fd-d.88.1782059419356SgxaFMj)·06-15 01:11 [0](https://www.sohu.com/a/1036795793_122786724?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.88.1782059419356SgxaFMj#comment_area)

[![文章配图-72](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038953910_122639510?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.89.1782059419356SgxaFMj)

# [太不可思议了！河北，一男子来到车旁准备开车，多年养成的习惯让他下意识地绕车走了一...](https://www.sohu.com/a/1038953910_122639510?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.89.1782059419356SgxaFMj)

[![史前记序头像](https://q6.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260213/49e25e06b43c4b5fa6e32cb0115349c8.png)](https://mp.sohu.com/profile?xpt=NmNkYWY1NTctNTkyNC00YWI5LWIwYjgtNjhiYmUxOTYzYTkx&spm=smpc.content-abroad.fd-d.89.1782059419356SgxaFMj)[史前记序](https://mp.sohu.com/profile?xpt=NmNkYWY1NTctNTkyNC00YWI5LWIwYjgtNjhiYmUxOTYzYTkx&spm=smpc.content-abroad.fd-d.89.1782059419356SgxaFMj)·06-19 08:22 [0](https://www.sohu.com/a/1038953910_122639510?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.89.1782059419356SgxaFMj#comment_area)

[![文章配图-73](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1016966632_120452151?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.91.1782059419356SgxaFMj)

# [大胆、半露内裤下乳全显？女性艺人的大胆穿着社会争议与穿衣自由！](https://www.sohu.com/a/1016966632_120452151?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.91.1782059419356SgxaFMj)

[![娱小慧头像](https://q2.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250601/16f332a57fe5499d9cfd4ec84f9485c6.jpeg)](https://mp.sohu.com/profile?xpt=ZWQ2M2FhYTUtOTZmNy00ZTQ3LTg4OWYtOGYzY2Q3YjdhZjQx&spm=smpc.content-abroad.fd-d.91.1782059419356SgxaFMj)[娱小慧](https://mp.sohu.com/profile?xpt=ZWQ2M2FhYTUtOTZmNy00ZTQ3LTg4OWYtOGYzY2Q3YjdhZjQx&spm=smpc.content-abroad.fd-d.91.1782059419356SgxaFMj)·05-05 10:04 [0](https://www.sohu.com/a/1016966632_120452151?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.91.1782059419356SgxaFMj#comment_area)

[![文章配图-74](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038190659_122413?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.92.1782059419356SgxaFMj)

# [徐州市公安局常务副局长李海波，拟任县（市、区）委书记](https://www.sohu.com/a/1038190659_122413?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.92.1782059419356SgxaFMj)

[![鲁网淄博头像](https://p1.itc.cn/c_lfill,w_40,h_40,g_face/images03/20221024/11534711076a45e099c23f12ac40ed7f.jpeg)](https://mp.sohu.com/profile?xpt=MDE2NUZBOEMwRUVERTdGNEJFQTU5QjBFRjRENzMxRDVAcXEuc29odS5jb20=&spm=smpc.content-abroad.fd-d.92.1782059419356SgxaFMj)[鲁网淄博](https://mp.sohu.com/profile?xpt=MDE2NUZBOEMwRUVERTdGNEJFQTU5QjBFRjRENzMxRDVAcXEuc29odS5jb20=&spm=smpc.content-abroad.fd-d.92.1782059419356SgxaFMj)·06-17 20:49 [0](https://www.sohu.com/a/1038190659_122413?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.92.1782059419356SgxaFMj#comment_area)

[![文章配图-75](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039095420_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.93.1782059419356SgxaFMj)

# [韩国瑜正式宣布，6月15日，台湾地区立法机构负责人韩国瑜正式宣布：将于星期天（6月21...](https://www.sohu.com/a/1039095420_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.93.1782059419356SgxaFMj)

[![壮壮科普头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260307/e380ee69319747f39e6c2cbb5d0c75e3.png)](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.93.1782059419356SgxaFMj)[壮壮科普](https://mp.sohu.com/profile?xpt=YWM4NWE4Y2QtZGFlMS00ZmExLWFiMjktZmZhNmMzMjQ0MmY2&spm=smpc.content-abroad.fd-d.93.1782059419356SgxaFMj)·06-19 21:52 [0](https://www.sohu.com/a/1039095420_122480070?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.93.1782059419356SgxaFMj#comment_area)

[![文章配图-76](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039614790_162758?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.94.1782059419356SgxaFMj)

# [抓到就罚！驾驶新规已执行，返程注意](https://www.sohu.com/a/1039614790_162758?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.94.1782059419356SgxaFMj)

[![光明网头像](https://5b0988e595225.cdn.sohucs.com/a_auto,c_lfill,w_40,h_40,g_face/images/20200405/0adfc2b0ff2b45729e9bcc9ac5095baf.jpeg)](https://mp.sohu.com/profile?xpt=c29odXptdGUwb2RlMDJAc29odS5jb20=&spm=smpc.content-abroad.fd-d.94.1782059419356SgxaFMj)[光明网](https://mp.sohu.com/profile?xpt=c29odXptdGUwb2RlMDJAc29odS5jb20=&spm=smpc.content-abroad.fd-d.94.1782059419356SgxaFMj)·今天 07:50 [0](https://www.sohu.com/a/1039614790_162758?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.94.1782059419356SgxaFMj#comment_area)

[![文章配图-77](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1033702242_122471289?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.96.1782059419356SgxaFMj)

# [我56岁已经绝经，和77岁的他出去玩了8天，回来后我果断提出散伙](https://www.sohu.com/a/1033702242_122471289?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.96.1782059419356SgxaFMj)

[![瓜汁橘长Dr头像](https://q4.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250707/e44238c087644e10ba727b7a5a188342.jpeg)](https://mp.sohu.com/profile?xpt=MWE5YTA2OTUtNWZmNS00MDYzLWI5ZGQtZDhjN2U3ZDVmNjRj&spm=smpc.content-abroad.fd-d.96.1782059419356SgxaFMj)[瓜汁橘长Dr](https://mp.sohu.com/profile?xpt=MWE5YTA2OTUtNWZmNS00MDYzLWI5ZGQtZDhjN2U3ZDVmNjRj&spm=smpc.content-abroad.fd-d.96.1782059419356SgxaFMj)·06-08 00:48 [0](https://www.sohu.com/a/1033702242_122471289?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.96.1782059419356SgxaFMj#comment_area)

[![文章配图-78](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038200979_122745403?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.97.1782059419356SgxaFMj)

# [“男人的劲再大，再强壮，女人也不怕你。你征服不了她，别不信”](https://www.sohu.com/a/1038200979_122745403?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.97.1782059419356SgxaFMj)

[![凭凭头像](https://q7.itc.cn/c_lfill,w_40,h_40,g_face/images03/20260424/d12e9102fa66462b95fb68ca382d9473.png)](https://mp.sohu.com/profile?xpt=M2E2YTk2YTItZjNmYy00NjE4LWIwNTMtMDI3Nzg2N2Y3Zjhl&spm=smpc.content-abroad.fd-d.97.1782059419356SgxaFMj)[凭凭](https://mp.sohu.com/profile?xpt=M2E2YTk2YTItZjNmYy00NjE4LWIwNTMtMDI3Nzg2N2Y3Zjhl&spm=smpc.content-abroad.fd-d.97.1782059419356SgxaFMj)·06-17 21:11 [0](https://www.sohu.com/a/1038200979_122745403?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.97.1782059419356SgxaFMj#comment_area)

[![文章配图-79](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1038868979_122499133?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.98.1782059419356SgxaFMj)

# [男子怀疑儿子非亲生，妻子坦言：我认为有90%几率是他的](https://www.sohu.com/a/1038868979_122499133?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.98.1782059419356SgxaFMj)

[![民间故事屋头像](https://q3.itc.cn/c_lfill,w_40,h_40,g_face/images03/20250809/7028ae64a58f499583c121c8347a0a2d.png)](https://mp.sohu.com/profile?xpt=ZDAxYTBjOTUtOGUzYS00MTM2LTg1NTktODhjMTliZDRhMDAy&spm=smpc.content-abroad.fd-d.98.1782059419356SgxaFMj)[民间故事屋](https://mp.sohu.com/profile?xpt=ZDAxYTBjOTUtOGUzYS00MTM2LTg1NTktODhjMTliZDRhMDAy&spm=smpc.content-abroad.fd-d.98.1782059419356SgxaFMj)·06-19 03:19 [0](https://www.sohu.com/a/1038868979_122499133?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.98.1782059419356SgxaFMj#comment_area)

[![文章配图-80](https://statics.itc.cn/web/static/images/pic/preload.png)](https://www.sohu.com/a/1039446122_161795?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.100.1782059419356SgxaFMj)

# [涉事纸尿裤品牌，凌晨晒报告，称已报警](https://www.sohu.com/a/1039446122_161795?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.100.1782059419356SgxaFMj)

[![南方都市报头像](https://p1.itc.cn/c_lfill,w_40,h_40,g_face/mpbp/pro/20210804/de3f7d8e7f424dba9026288279fc625a.jpeg)](https://mp.sohu.com/profile?xpt=c29odXptdGdlZ2Jxc2ZAc29odS5jb20=&spm=smpc.content-abroad.fd-d.100.1782059419356SgxaFMj)[南方都市报](https://mp.sohu.com/profile?xpt=c29odXptdGdlZ2Jxc2ZAc29odS5jb20=&spm=smpc.content-abroad.fd-d.100.1782059419356SgxaFMj)·昨天 22:28 [0](https://www.sohu.com/a/1039446122_161795?scm=10008.1479_13-1479_13-68_68.0-4827002.0-1-0-0-0.0&spm=smpc.content-abroad.fd-d.100.1782059419356SgxaFMj#comment_area)

已经到底了

- ![refresh-icon](<Base64-Image-Removed>)
- [![back-home-icon](https://statics.itc.cn/mptc-mpfe/img/components-pc/logo_sohu.png)\\
\\
返回首页](http://www.sohu.com/?strategyid=24&spm=smpc.content-abroad.fx.1.1782059419356SgxaFMj)
- [![feedback-icon](<Base64-Image-Removed>)\\
\\
举报/反馈](https://www.sohu.com/feedback?articleUrl=https://www.sohu.com/a/1035138286_122095475&spm=smpc.content-abroad.fx.2.1782059419356SgxaFMj)

- ![back-top-icon](https://statics.itc.cn/mptc-mpfe/img/components-pc/icon_Up.png)

### 来源 7: 使用指南 | 招标文件深度拆解，废标风险全面排查（建议收藏） | 快书编标官方论坛

- URL: https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F
- 精读方法：firecrawl-scrape

[Skip to content](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F#content)

[![快书编标](https://www.kshbb.com/bbs/assets/uploads/system/site-logo.png?v=65f957ab081)](https://www.kshbb.com/bbs/ "Brand Logo")[**快书编标官方论坛**](https://www.kshbb.com/bbs/)

1. [Home](https://www.kshbb.com/bbs)
2. [行业资讯与政策解读](https://www.kshbb.com/bbs/category/9/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF%E4%B8%8E%E6%94%BF%E7%AD%96%E8%A7%A3%E8%AF%BB)
3. 使用指南 \| 招标文件深度拆解，废标风险全面排查（建议收藏）

# 使用指南 \| 招标文件深度拆解，废标风险全面排查（建议收藏）

Scheduled
Pinned
Locked
[Moved](https://www.kshbb.com/bbs/category/)[行业资讯与政策解读](https://www.kshbb.com/bbs/category/9/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF%E4%B8%8E%E6%94%BF%E7%AD%96%E8%A7%A3%E8%AF%BB)

1Posts1Posters33Views

![](https://www.kshbb.com/bbs/assets/uploads/files/1779936417519-b15c634e-96f2-4f93-9451-f4a6ab54535d-image.png) ![](https://www.kshbb.com/bbs/assets/uploads/files/1779936435512-204289e7-2a9f-477d-a921-54765507aa61-image.png) ![](https://www.kshbb.com/bbs/assets/uploads/files/1779936456259-9b1f8a0e-a4f4-4ec7-9137-7106a63e445f-image.png) ![](https://www.kshbb.com/bbs/assets/uploads/files/1779936488332-9a325cd8-bc88-49cf-b53d-7937de900a45-image.png) ![](https://www.kshbb.com/bbs/assets/uploads/files/1779936858449-74ee1c97-b855-41eb-8482-4ef423bd649c-image.png) +2

This topic has been deleted. Only users with topic management privileges can see it.

- [![快书产品经理小快](https://www.kshbb.com/bbs/assets/uploads/profile/uid-4/4-profileavatar-1767010016049.png)快Offline](https://www.kshbb.com/bbs/user/%E5%BF%AB%E4%B9%A6%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86%E5%B0%8F%E5%BF%AB)

[![快书产品经理小快](https://www.kshbb.com/bbs/assets/uploads/profile/uid-4/4-profileavatar-1767010016049.png)快Offline](https://www.kshbb.com/bbs/user/%E5%BF%AB%E4%B9%A6%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86%E5%B0%8F%E5%BF%AB)

[快书产品经理小快](https://www.kshbb.com/bbs/user/%E5%BF%AB%E4%B9%A6%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86%E5%B0%8F%E5%BF%AB)

wrote [25 days ago](https://www.kshbb.com/bbs/post/660 "May 27, 2026, 10:56 PM")last edited by

[#1](https://www.kshbb.com/bbs/post/660)

做过标书的人都懂，废标离自己比想象的更近。

![b15c634e-96f2-4f93-9451-f4a6ab54535d-image.png](https://www.kshbb.com/bbs/assets/uploads/files/1779936417519-b15c634e-96f2-4f93-9451-f4a6ab54535d-image.png)

这种事每天都在发生。

为什么标书总在自己“看不见的地方”翻车？

一个人翻阅上百页文件，从文字海洋里捞出这些散落各处的“红线”，本身就近乎不可能完成的任务。

下面教你如何从专业角度解读招标文件，从流程出发，用一套体系化的方法把盲区一一覆盖。

![204289e7-2a9f-477d-a921-54765507aa61-image.png](https://www.kshbb.com/bbs/assets/uploads/files/1779936435512-204289e7-2a9f-477d-a921-54765507aa61-image.png)

## **第一步：抓住拆解的关键动作**

拿到一份招标文件，第一件事不是着急翻模板开写，而是做一次彻底的“文件拆解”。先给所有内容标上三个颜色：

关键要素——什么时间节点？最重要的响应项有哪些？

评分重点——分值权重怎样分布？哪些条款对应高额分数？

废标红线——加粗、带★、写进前附表的条款，必须标红重点对待

很多招标文件会将废标条款分散在多个章节，有的甚至用普通段落陈述，没有任何视觉提示。拆解时要主动建立一份“条款响应矩阵表”，按“条款编号-核心要求-响应措施-责任分配”逐项登记，确保每一处都不遗漏。

在编标过程中还要特别留意：标前会议上发布的《补遗书》《答疑纪要》 ，必须在2小时内嵌入原招标文件并醒目标注“新增/修改内容”，这是很多漏项问题的源头。

## **第二步：如何将拆解落到实处？**

此处需要大家打开word或者WPS

点击快书编标栏里面的“AI过招”，选择招标文件，即可开始解析。

[![9b1f8a0e-a4f4-4ec7-9137-7106a63e445f-image.png](https://www.kshbb.com/bbs/assets/uploads/files/1779936456259-9b1f8a0e-a4f4-4ec7-9137-7106a63e445f-image-resized.png)](https://www.kshbb.com/bbs/assets/uploads/files/1779936456259-9b1f8a0e-a4f4-4ec7-9137-7106a63e445f-image.png)

解析结束后，点击选择具体解析项，查看详细内容，拿捏投标要点与注意事项。

也可右边定位查看原文。

[![9a325cd8-bc88-49cf-b53d-7937de900a45-image.png](https://www.kshbb.com/bbs/assets/uploads/files/1779936488332-9a325cd8-bc88-49cf-b53d-7937de900a45-image-resized.png)](https://www.kshbb.com/bbs/assets/uploads/files/1779936488332-9a325cd8-bc88-49cf-b53d-7937de900a45-image.png)

利用解析出的项目信息可在系统内快速创建新项目，或追加到现有投标项目信息，其项目信息和标书模板会同步保存在项目属性中。

而提取出来的信息：项目信息、标书模板、废标项等都可以在编标时候进行直接的查看和使用。

![74ee1c97-b855-41eb-8482-4ef423bd649c-image.png](https://www.kshbb.com/bbs/assets/uploads/files/1779936858449-74ee1c97-b855-41eb-8482-4ef423bd649c-image.png)

## **一套完整的废标风险防控体系，需要“流程+工具”双轮驱动**

不是让投标人凭空多一步工作，而是用智能手段替代重复劳动、规避人为盲区，让有限的时间和精力——让投标人真正聚焦在技术方案打磨和差异化优势构建上。

AI在招投标领域的应用正在加速落地。国家发展改革委等部委已明确提出，到2026年底，招标文件智能检测、智能辅助评标等重点场景将在部分省市实现全覆盖应用。试点数据显示，智能评标模型已能在近400个项目中，将招标文件的问题条款发现率提升40%以上。

在这个趋势面前，主动拥抱智能化工具，绝不是追求“时髦”，而是在构建实实在在的竞争力。

[1 ReplyLast reply](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F#)

[Reply](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F# "Reply")[Quote](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F# "Quote")

[Upvote post](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F# "Upvote post")[0](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F# "Voters") [Downvote post](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F# "Downvote post")

[Post tools](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F#)

[Reply](https://www.kshbb.com/bbs/compose?tid=445)

- [Reply as topic](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F#)

[Log in to reply](https://www.kshbb.com/bbs/login)

Oldest to Newest

- [Oldest to Newest](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F#)
- [Newest to Oldest](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F#)
- [Most Votes](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F#)

* * *

25 days ago

1/1

May 27, 2026, 10:56 PM

[Unread posts link](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F)

25 days ago

* * *

[1 out of 1](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F#)

- ![快书产品经理小快](https://www.kshbb.com/bbs/assets/uploads/profile/uid-4/4-profileavatar-1767010016049.png)快

[快书产品经理小快](https://www.kshbb.com/bbs/user/%E5%BF%AB%E4%B9%A6%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86%E5%B0%8F%E5%BF%AB)

25 days ago

做过标书的人都懂，废标离自己比想象的更近。

![b15c634e-96f2-4f93-9451-f4a6ab54535d-image.png](https://www.kshbb.com/bbs/assets/uploads/files/1779936417519-b15c634e-96f2-4f93-9451-f4a6ab54535d-image.png)

这种事每天都在发生。

为什么标书总在自己“看不见的地方”翻车？

一个人翻阅上百页文件，从文字海洋里捞出这些散落各处的“红线”，本身就近乎不可能完成的任务。

下面教你如何从专业角度解读招标文件，从流程出发，用一套体系化的方法把盲区一一覆盖。

![204289e7-2a9f-477d-a921-54765507aa61-image.png](https://www.kshbb.com/bbs/assets/uploads/files/1779936435512-204289e7-2a9f-477d-a921-54765507aa61-image.png)

## **第一步：抓住拆解的关键动作**

拿到一份招标文件，第一件事不是着急翻模板开写，而是做一次彻底的“文件拆解”。先给所有内容标上三个颜色：

关键要素——什么时间节点？最重要的响应项有哪些？

评分重点——分值权重怎样分布？哪些条款对应高额分数？

废标红线——加粗、带★、写进前附表的条款，必须标红重点对待

很多招标文件会将废标条款分散在多个章节，有的甚至用普通段落陈述，没有任何视觉提示。拆解时要主动建立一份“条款响应矩阵表”，按“条款编号-核心要求-响应措施-责任分配”逐项登记，确保每一处都不遗漏。

在编标过程中还要特别留意：标前会议上发布的《补遗书》《答疑纪要》 ，必须在2小时内嵌入原招标文件并醒目标注“新增/修改内容”，这是很多漏项问题的源头。

## **第二步：如何将拆解落到实处？**

此处需要大家打开word或者WPS

点击快书编标栏里面的“AI过招”，选择招标文件，即可开始解析。

![9b1f8a0e-a4f4-4ec7-9137-7106a63e445f-image.png](https://www.kshbb.com/bbs/assets/uploads/files/1779936456259-9b1f8a0e-a4f4-4ec7-9137-7106a63e445f-image-resized.png)

解析结束后，点击选择具体解析项，查看详细内容，拿捏投标要点与注意事项。

也可右边定位查看原文。

![9a325cd8-bc88-49cf-b53d-7937de900a45-image.png](https://www.kshbb.com/bbs/assets/uploads/files/1779936488332-9a325cd8-bc88-49cf-b53d-7937de900a45-image-resized.png)

利用解析出的项目信息可在系统内快速创建新项目，或追加到现有投标项目信息，其项目信息和标书模板会同步保存在项目属性中。

而提取出来的信息：项目信息、标书模板、废标项等都可以在编标时候进行直接的查看和使用。

![74ee1c97-b855-41eb-8482-4ef423bd649c-image.png](https://www.kshbb.com/bbs/assets/uploads/files/1779936858449-74ee1c97-b855-41eb-8482-4ef423bd649c-image.png)

## **一套完整的废标风险防控体系，需要“流程+工具”双轮驱动**

不是让投标人凭空多一步工作，而是用智能手段替代重复劳动、规避人为盲区，让有限的时间和精力——让投标人真正聚焦在技术方案打磨和差异化优势构建上。

AI在招投标领域的应用正在加速落地。国家发展改革委等部委已明确提出，到2026年底，招标文件智能检测、智能辅助评标等重点场景将在部分省市实现全覆盖应用。试点数据显示，智能评标模型已能在近400个项目中，将招标文件的问题条款发现率提升40%以上。

在这个趋势面前，主动拥抱智能化工具，绝不是追求“时髦”，而是在构建实实在在的竞争力。

First post

1/1

Last post

Go to my next post

[0](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F#)

- [Categories](https://www.kshbb.com/bbs/categories)
- [Recent](https://www.kshbb.com/bbs/recent)
- [Tags](https://www.kshbb.com/bbs/tags)
- [Popular](https://www.kshbb.com/bbs/popular)
- [Users](https://www.kshbb.com/bbs/users)
- [Groups](https://www.kshbb.com/bbs/groups)

- [Search](https://www.kshbb.com/bbs/topic/445/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97-%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E6%B7%B1%E5%BA%A6%E6%8B%86%E8%A7%A3-%E5%BA%9F%E6%A0%87%E9%A3%8E%E9%99%A9%E5%85%A8%E9%9D%A2%E6%8E%92%E6%9F%A5-%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F# "Search")

[Advanced Search](https://www.kshbb.com/bbs/search "Advanced Search")

Search

Looks like your connection to 快书编标官方论坛 was lost, please wait while we try to reconnect.

### 来源 8: 标桥首页

- URL: https://www.bqpoint.com
- 精读方法：firecrawl-scrape

![](https://www.bqpoint.com/bqindexv3/images/header_logo_img.png)标桥

- 首页
- 服务与产品

[![](https://www.bqpoint.com/bqindexv3/images/new_header/serve_1.png)\\
工作台](https://www.bqpoint.com/bqworkbench/bqindex.html) [![](https://www.bqpoint.com/bqindexv3/images/new_header/serve_2.png)\\
AI编标](https://www.bqpoint.com/AIbianbiao/dist/index.html) [![](https://www.bqpoint.com/bqindexv3/images/new_header/serve_3.png)\\
素材市场](https://www.bqpoint.com/materialmarket/vue/dist/index.html?platform=DesktopApp) [![](https://www.bqpoint.com/bqindexv3/images/new_header/serve_5.png)\\
标讯](https://www.bqpoint.com/epoint-web-micro/frame/pages/iframe/index_iframe?headname=bx) [![](https://www.bqpoint.com/bqindexv3/images/new_header/serve_7.png)\\
标证通](https://epbzt.bqpoint.com/) [![](https://www.bqpoint.com/bqindexv3/images/new_header/serve_9.png)\\
建采通](https://ys.bqpoint.com/) [![](https://www.bqpoint.com/bqindexv3/images/new_header/serve_4.png)\\
标书检查](https://www.bqpoint.com/tool/qingbiaotooldownloadindex.html) [![](https://www.bqpoint.com/bqindexv3/images/new_header/serve_6.png)\\
招标文件解析](https://www.bqpoint.com/bqdesktop/fileanalysis/before_analysis.html?p=prefecturetool) [![](https://www.bqpoint.com/bqindexv3/images/new_header/serve_8.png)\\
模拟开标](https://www.bqpoint.com/bqworkbench/bqindex.html) [![](https://www.bqpoint.com/bqindexv3/images/new_header/qykj.png)\\
企业空间](https://www.bqpoint.com/epoint-web-micro/frame/pages/iframe/index_iframe) [![](https://www.bqpoint.com/bqindexv3/images/new_header/serve_10.png)\\
造价云](https://zjy.epoint.com.cn/ZjyMember/frame/pages/login/memlogin)

- 商城

![](https://www.bqpoint.com/bqindexv3/images/new_header/market_1.png)
软件商城
[![](https://www.bqpoint.com/bqindexv3/images/new_header/market_2.png)\\
积分商城](https://www.bqpoint.com/welfarehtml/welfareindex.html)

- [课堂](https://college.bqpoint.com/)
- [下载](https://download.bqpoint.com/)
- [知道](https://zhidao.bqpoint.com/)
- 开发者平台

[![](https://www.bqpoint.com/bqindexv3/images/new_header/logo_2.png)\\
标桥平台](https://www.bqpoint.com/developerplatform/developerplatform.html) [![](https://www.bqpoint.com/bqindexv3/images/new_header/logo_1.png)\\
造价生态平台](https://www.bqpoint.com/zjindex/developerplatindex.html)

登录 [免费注册](https://www.bqpoint.com/unityuser/pages/login_register/login.html)

您好，[立即充值>>](https://www.bqpoint.com/usercenter2/usercenter2myasset.html)

![](https://www.bqpoint.com/images/per.png)

消息（ [0](https://www.bqpoint.com/usercenter2/usercenter2messagecenter.html)）

[用户中心](https://www.bqpoint.com/usercenter2/usercenter2.html)退出帐号

![](https://download.bqpoint.com/share/f543fdc2-475f-4c1c-8fac-4b651fc21f19/banner.png)

![](https://download.bqpoint.com/share/ffea4deb-3009-40dd-acf2-951c36050301/banenr_1.png)

![](https://download.bqpoint.com/share/f543fdc2-475f-4c1c-8fac-4b651fc21f19/banner.png)

![](https://download.bqpoint.com/share/ffea4deb-3009-40dd-acf2-951c36050301/banenr_1.png)

[AI编标\\
\\
AI深度解析招标文件，自动构建标书框架并生成技术方案初稿。](https://www.bqpoint.com/AIbianbiao/index.html) [标书检查\\
\\
自动检测标书关键指标，确保与招标要求 100%无偏差匹配。](https://www.bqpoint.com/tool/qingbiaotooldownloadindex.html)
招标文件解析

自动生成结构化分析报告，直观呈现关键信息与潜在风险。

[素材市场\\
\\
覆盖100+细分领域、汇聚10万+标书模板、案例及方案。](https://www.bqpoint.com/materialmarket/vue/dist/index.html?platform=DesktopApp)

您是否也面临这样的挑战？

时间紧，任务重

投标任务下达晚，技术标方案编制时间不足，需通宵赶 工，影响方案深度。

内容套用，缺乏针对性

照搬过往案例时，沿用旧版标书格式，与当前招标文件要求脱节，导致丢失高分项。

风险暗藏，防不胜防

依赖人工排查，暗标格式、签章、超链接等细节极易遗漏，随时可能面临废标风险。

一个生态，一个对策

标桥如何全流程赋能您的投标工作

- 标前洞察

洞悉先机，赢在起点

招标文件解析 [标讯](https://www.bqpoint.com/epoint-web-micro/frame/pages/iframe/index_iframe?headname=bx) [建采通](https://ys.bqpoint.com/)

- 智能编制

高效精准，专业呈现

[AI编标](https://www.bqpoint.com/AIbianbiao/index.html) [素材市场](https://www.bqpoint.com/materialmarket/vue/dist/index.html?platform=DesktopApp) [标证通(移动CA)](https://epbzt.bqpoint.com/)

- 智能审查

严控风险，万无一失

[标书检查](https://www.bqpoint.com/tool/qingbiaotooldownloadindex.html) [清标工具](https://www.bqpoint.com/tool/qingbiaotooldownloadindex.html)模拟开标蔓延排版精灵

向AI提问，探索投标智慧

提问

快速提问:

CA驱动登录投标标书

热门问题 [更多](https://www.bqpoint.com/epointknow2/bqepointknowplatform.html)

- 电子交易产品

[如何下载安装标证通电子证书APP？](https://zhidao.bqpoint.com/epointknow2/bqepointknowquestion.html?producttype=1&QuestionGuid=e4bb550d-cf85-4bff-8ca7-8dc6a8ad0235 "如何下载安装标证通电子证书APP？") [【上传投标文件提示http】上传文件卡进度，进度回退](https://zhidao.bqpoint.com/epointknow2/bqepointknowquestion.html?producttype=1&QuestionGuid=27783fc5-9868-439b-ae5e-43f36505a093 "【上传投标文件提示http】上传文件卡进度，进度回退") [内蒙古不同地区办理的CA锁是否通用](https://zhidao.bqpoint.com/epointknow2/bqepointknowquestion.html?producttype=1&QuestionGuid=47b4e170-5631-4b7d-9759-c4a5b1c81a2a "内蒙古不同地区办理的CA锁是否通用")

- 建筑产品

什么是双盲评审？技术标常见问题？投标流程详解？

- 标桥使用问题

[什么是清标工具？](https://zhidao.bqpoint.com/epointknow2/bqepointknowquestion.html?producttype=9&QuestionGuid=ff943f82-9dab-4cce-893e-445e11f66c0d "什么是清标工具？") [如何进行清标？](https://zhidao.bqpoint.com/epointknow2/bqepointknowquestion.html?producttype=9&QuestionGuid=c37f9f17-b61a-49c2-af30-69da2b0cd584 "如何进行清标？") [如何激活清标e卡密码？](https://zhidao.bqpoint.com/epointknow2/bqepointknowquestion.html?producttype=9&QuestionGuid=10b00e3e-ba3f-49f0-939d-075a78cf1605 "如何激活清标e卡密码？")

客户之声

真实用户评价，见证标桥价值，助您在招投标中无往不利

- 提升效率
- 降低风险
- 发现商机

- ![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_4.png)建筑公司项目经理

AI编标太好用了，省时省力，效率直接拉满！

AI编标

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_2.png)资深投标顾问

做标书快多了，终于不用再熬夜赶工了！

工作台

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_1.png)工程投标专员

点一下就排好版了，再也不用费劲调格式。

蔓延排版精灵/云端保排版王/智能排版

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_5.png)招标业务经理

招标文件扔进去，要求马上就明白了，真快！

招标文件解析

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_3.png)投标部门主管

模板库超给力，准备资料比以前快了一大半。

素材市场

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_6.png)项目投标经理

整个投标流程都顺了，软件用着很跟手。

工作台

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_2.png)商务经理

功能都在一块儿，一个平台全搞定，效率绝了。

工作台

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_1.png)团队负责人

团队写标书的速度快得飞起，再也不拖DDL了。

AI编标

- ![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_1.png)招标总监

这清标功能真强，基本不用担心会废标了。

清标工具

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_3.png)法务风控专员

它能自动查合规问题，比我们人工看靠谱多了。

标书检查

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_5.png)标书编制员

格式检查特别细，那些低级错误一个也跑不掉。

智能排版

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_2.png)技术负责人

用它做技术标特别规范，双盲评审心里有底。

智能排版

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_4.png)投标经理

有废标风险会提前预警，我们投标准备踏实多了。

标书检查

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_6.png)项目助理

连隐藏的超链接都能揪出来，再也不怕出错了。

标书检查

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_1.png)商务主管

盖章对不对它能查出来，再也没出过岔子。

标书检查

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_3.png)成本估算师

报价自动检查，好几次都帮我找出了小错误。

清标工具

- ![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_1.png)市场拓展经理

订阅的标讯都挺靠谱，好项目一个也没跑掉。

标讯

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_2.png)商务拓展BD

信息特别全，感觉所有商机都在我手里了。

标讯

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_3.png)销售经理

推送的项目都是我想要的，筛起来效率超高。

标讯

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_4.png)公司总经理

全国信息都有，帮我们拓展外地业务太给力了。

标讯

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_5.png)战略发展总监

市场雷达很灵敏，总能帮我挖到别人不知道的机会。

标讯

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_6.png)客户关系经理

情报拿得比别人都快，我们总能先走一步。

标讯

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_7.png)区域业务负责人

推荐的项目跟我们业务很搭，找项目省事多了。

标讯

![](https://www.bqpoint.com/bqindexv3/images/new_index/client_ico_2.png)销售总监

找商机的速度快多了，我们投标的机会也变多了。

标讯

选择标桥，选择专业与信赖

客户的声音

自从用了标桥，

团队的效率肉眼可见地提升了，

现在有更多时间去打磨方案细节

行业的认可

新点20年行业经验沉淀

新点标证通已接入全国互认APP名录

与全国40+权威CA机构深度合作

数据的承诺

服务全国100万+注册投标用户

平台保障，交易安全可靠

数据更安全

### 来源 9: 招标解析（已下线） - 智谱AI开放文档

- URL: https://docs.bigmodel.cn/cn/guide/agents/tender
- 精读方法：firecrawl-scrape

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.bigmodel.cn/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.bigmodel.cn/cn/guide/agents/tender#content-area)

在招投标领域，时间就是金钱，信息的准确性决定成败。招标解析智能体是一款基于智谱大语言模型的专业级文本分析工具，它能模拟行业专家的阅读和分析能力，自动处理各类招标信息载体。无论是政府公开发布的采购公告，还是企业内部流转的招标文件，本智能体都能提供高效、精准、结构化的信息提取服务，显著降低信息获取成本，提升业务处理效率。

[**详细说明** \\
\\
查看介绍、核心功能、适用场景](https://www.bigmodel.cn/marketplace/agent_detail/839ae790c20e)

[**Agent API 文档** \\
\\
查看完整的 API 文档](https://docs.bigmodel.cn/api-reference/agent-api/%E6%99%BA%E8%83%BD%E4%BD%93%E5%AF%B9%E8%AF%9D)

[**体验中心** \\
\\
点击立即体验](https://www.bigmodel.cn/trialcenter/agent?agentId=bidding_parser_agent)

## [​](https://docs.bigmodel.cn/cn/guide/agents/tender\#%E4%BB%B7%E6%A0%BC)  **价格**

- **按 Token 后付费，5 元/百万 Tokens**
- 计量范围：智能体全任务流节点产生的 Tokens 总数

## [​](https://docs.bigmodel.cn/cn/guide/agents/tender\#%E6%8E%A5%E5%8F%A3%E8%AF%B7%E6%B1%82)  **接口请求**

| 传输方式 | https |
| --- | --- |
| 请求地址 | [https://open.bigmodel.cn/api/v1/agents](https://open.bigmodel.cn/api/v1/agents) |
| 字符编码 | UTF-8 |
| 接口请求格式 | JSON |
| 响应格式 | JSON |
| 接口请求类型 | POST |
| 开发语言 | 任意可发起 http 请求的开发语言 |

## [​](https://docs.bigmodel.cn/cn/guide/agents/tender\#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)  **请求参数**

| 参数名称 | 类型 | 是否必填 | 参数说明 |
| --- | --- | --- | --- |
| agent\_id | String | 是 | 智能体 ID：`bidwin_parser_agent` |
| stream | boolean | 否 | 是否使用流式返回，默认为 `false`，表示非流式输出 |
| messages | List<Object> | 是 | 会话消息体 |
| └─ role | String | 是 | 用户的输入 `role = user` |
| └─ content | List<Object> | 是 | 会话消息体 |
| └─ type | String | 是 | 目前支持内容类型，支持 `text` |
| └─ text | String | 是 | 招标公告HTML文本 |
| custom\_variables | Object | 是 | 智能体扩展参数 |
| └─ custom\_fields | List<Object> | 否 | 自定义字段提取说明，每项是一个键值对，键为字段名，值为提取规则或说明 |

Was this page helpful?

YesNo

Ctrl+I

### 来源 10: AI 标书撰写：如何借助 AI 驱动的投标方案赢得更多竞标（2026年5月）

- URL: https://www.jenova.ai/zh/resources/ai-tender-writing-202605
- 精读方法：firecrawl-scrape

![Jenova - AI 智能体平台](<Base64-Image-Removed>)

试用 Jenova

# **AI 标书撰写：如何借助 AI 驱动的投标方案赢得更多竞标（2026年5月）**

2026-05-19

标书撰写是商业写作中风险最高、也最折磨人的领域之一。一份政府或企业标书可能代表着数百万的合同价值，但响应过程却需要数周的紧张工作：剖析 60-120 页的 ITT 文件，从整个组织收集证据，在巨大的截止日期压力下起草合规且有说服力的回复，并按照精确的规范格式化所有内容。错过一个评估标准，整个投标就会被取消资格。满足了所有标准但未能脱颖而出，你就会输给一个答案让评分小组 _感觉_ 更可信的竞争对手。

到 2026 年，压力进一步加剧。全球 AI 投标书撰写软件市场在 [2025 年的估值为 3.49 亿美元，预计将以 7.1% 的复合年增长率达到 5.61 亿美元](https://www.openpr.com/news/4504877/ai-bid-writing-software-research-cagr-of-7-1-during)。根据 [MyTender.io 的 2026 年行业分析](https://mytender.io/blog/best-tender-writing-ai-software-2026)，72% 的中标团队现在使用 AI 驱动的投标软件——而那些没有使用的组织正日益与那些提案更快、更精良、更精确地符合评估标准的竞争对手竞标。

但 AI 的炒作忽略了一点： **撰写只是投标工作的最后 20%**。正如 [LinkedIn 上的行业专业人士](https://www.linkedin.com/posts/virtualbidteam_ai-trends-in-bid-writing-8-developments-activity-7442229203988713472-KGVS) 有力地指出的那样，投标工作是“情报收集、利益相关者协调、风险解读和战略定位——被包裹在截止日期和合规矩阵中”。那些将标书撰写视为简单内容生成的 AI 工具，产生的提案虽然更整洁、更快速，但 _与其他人完全没有区别_。真正能赢得投标的工具是那些能同时处理战略思考和写作的工具。

[**Jenova 的提案生成器**](https://www.jenova.ai/a/proposal-generator) 正是为应对这一挑战而生——它不是一个起草样板文件的聊天机器人，而是一个投标策略师，能够分析 RFP 要求，构建合规矩阵，制定致胜主题，并生成基于证据、为评估者准备的回复。将它与用于采购方情报的 [**RFP 生成器**](https://www.jenova.ai/a/rfp-generator)、用于最终润色的 [**写作助手**](https://www.jenova.ai/a/writing-assistant) 以及 Jenova 的持久跨会话记忆（在每次投标中都保存着您整个组织的知识库）相结合——您就拥有了 2026 年最完整的 AI 标书撰写系统。

![一位专业的标书撰写人正在笔记本电脑前工作，木制桌子上散布着文件和参考资料，这代表了 AI 增强的标书撰写以及战略思维与高效提案制作之间的平衡](https://autogenai.com/uk/wp-content/uploads/sites/4/2025/02/Enhancing-Work-Life-Balance-for-Bid-Writers-Through-Augmented-Intelligence.jpg)

* * *

## 快速解答：什么是 AI 标书撰写？

AI 标书撰写利用人工智能协助分析、起草、合规性检查以及投标回复和提案的战略定位——帮助投标团队更快地制作更高质量的投标书，同时保持评估者所看重的战略判断力。

- 使用 [**提案生成器**](https://www.jenova.ai/a/proposal-generator) 映射每个评估标准的 **RFP 分析和合规矩阵**
- 从您的组织知识库、案例研究和政策中提取信息的 **基于证据的回复起草**
- **致胜主题制定和竞争定位**，以区别于通用投标书
- 通过 [**RFP 生成器**](https://www.jenova.ai/a/rfp-generator) 了解买方优先事项的 **采购方情报**

* * *

## 问题所在：为什么大多数投标会失败——以及为什么仅靠 AI 无法解决问题

标书撰写过程的弊病是简单的内容生成无法修复的。在将任何 AI 工具应用于您的投标工作流程之前，必须了解这些失败点。

### 时间-质量陷阱

> **一份典型的公共部门 ITT 文件长达 60、80，有时甚至 120 页**——外加规格说明、评估标准、定价表和技术附录。投标团队必须同时处理所有这些信息以及内部证据、政策和回复草稿。 — [行业专业人士，LinkedIn 标书撰写讨论，2026](https://www.linkedin.com/posts/virtualbidteam_ai-trends-in-bid-writing-8-developments-activity-7442229203988713472-KGVS)

大多数投标团队都处于永久性的紧急处理状态。由于多个投标同时进行，每个都需要数周的专注工作，团队之所以偷工减料，不是因为他们能力不足，而是因为他们没有时间。证据收集变得仓促。合规性审查在最后一刻才进行。将中标与合格但普通的投标区分开来的战略定位最先被牺牲，因为它需要最长的时间来制定。

### AI 暴露了早已存在的问题

AI 写作工具的出现并没有解决投标质量危机——它揭示了其真实本质。正如 [投标架构师 David Bouwer](https://www.linkedin.com/posts/virtualbidteam_ai-trends-in-bid-writing-8-developments-activity-7442229203988713472-KGVS) 所观察到的：“AI 并没有让标书撰写变得更好。它暴露了大多数投标书本来就有多薄弱。” 使用 AI 更快地起草投标书的公司发现，他们的提案“更整洁、更精良、更一致——并且与其他人完全没有区别。”

问题从来不仅仅是写作。而是策略——或者说缺乏策略。当每个投标人都能够使用 AI 润色的文稿时，润色的文稿就不再是差异化因素。现在能赢的是：

- **清晰度** — 评估者确切地理解你提供的是什么
- **结构** — 你的答案是围绕它将如何被评分来设计的
- **证据** — 每一项声明都有具体、可验证的证据支持
- **信心** — 评估者觉得“这是我能捍卫的最安全的决定”

### 通用 AI 工具不理解采购背景

> **“大多数用 AI 写标书的人都在使用错误的工具。”** Copilot、ChatGPT 和通用助手是为提高生产力而构建的，而不是为采购。它们不理解评估标准的权重、合规矩阵的构建，或规范背后的政治背景。 — [LinkedIn 标书撰写讨论，2026](https://www.linkedin.com/posts/virtualbidteam_ai-trends-in-bid-writing-8-developments-activity-7442229203988713472-KGVS)

一个被要求“写一份投标回复”的通用聊天机器人生成的文本读起来不错，但得分很低。它不知道问题 4.2 占总评估权重的 15%，因此需要的证据密度是问题 2.1 的三倍。它不理解买方的规范语言揭示了隐藏的优先事项。它无法检测到社会价值部分的权重异常之高——这是一个信号，表明这位特定的评估者非常关心社区影响。

### 碎片化的工具格局

专门的 AI 投标工具已经出现—— [Tenderbolt](https://www.tenderbolt.ai/en/post/tender-software-2026-comparison-top-solutions)、AutogenAI、Bidify 等——但每个工具都只专注于一个狭窄的领域。有些擅长合规性检查但不能起草。另一些起草得很好但不能管理证据库。没有一个能提供覆盖整个投标生命周期的集成工作流程：机会分析 → 合规映射 → 致胜主题制定 → 证据收集 → 回复起草 → 审查 → 最终格式化。

> **94% 的采购主管现在每周都使用生成式 AI 工具**，90% 的采购领导者正在实施或计划在他们的工作流程中实施 AI 智能体。 — [Suplari，2026 年采购趋势](https://suplari.com/blog/key-trends-and-pitfalls-for-procurement)

采购方正在积极采用 AI。那些不具备同等复杂性的投标团队，无异于拿着笔去参加枪战。

* * *

## 为什么 Jenova 的 AI 智能体能赢得投标——而不仅仅是撰写它们

这正是 [**提案生成器**](https://www.jenova.ai/a/proposal-generator) 的用武之地。

通用 AI 撰写内容，专门的投标工具处理流程的片段，而 Jenova 的智能体生态系统则覆盖了从收到 RFP 到最终提交的整个投标生命周期。提案生成器不仅仅是起草回复。它会 _思考如何获胜_——分析评估标准，制定差异化定位，构建合规矩阵，并将每一项声明都建立在您组织的实际证据之上。

|  | 通用 AI (ChatGPT, Copilot) | 专用投标工具 | Jenova 提案生成器 |
| --- | --- | --- | --- |
| **RFP 分析** | 基本总结 | 因工具而异 | 带有评分权重分析的深度评估标准映射 |
| **合规矩阵** | 手动 | 部分工具 | 自动构建矩阵并识别差距 |
| **致胜主题制定** | 不支持 | 很少 | 针对竞争对手原型的战略定位 |
| **证据支撑** | 无 — 随意编造 | 基于库 | 交叉引用您上传的证据、案例研究和政策 |
| **回复起草** | 通用，文笔流畅 | 模板驱动 | 以评估者为中心，为得分优化，有证据支持 |
| **采购背景** | 无 | 有限 | 理解评估方法、买方心理、公共部门框架 |
| **记忆** | 仅限会话 | 基于项目 | 持久跨会话 — 记住过去的每一次投标、案例研究和组织细节 |
| **多模型灵活性** | 锁定一个模型 | 锁定一个模型 | GPT-5.4, Claude Opus 4.6, Gemini 3.1 Pro Preview, xAI, DeepSeek |

### 它像评估者一样阅读 RFP

一个中标团队首先要做的是从评估者的角度阅读招标文件——不仅仅是问了什么，而是 _答案将如何被评分_。提案生成器系统地执行此分析：

> _“这是一份 94 页的 ITT 文件，关于一份托管 IT 服务合同。分析评估标准，确定评分方法，标记任何不寻常的权重，并构建一个将每个强制性要求映射到我们回复部分的合规矩阵。突出显示三个最具影响力的、差异化将至关重要的问题。”_

### 它在动笔之前先构建策略

大多数 AI 投标工具的关键缺陷是缺乏战略层。提案生成器会制定致胜主题——贯穿每个回复的 2-3 个核心信息，将您的组织定位为评估者最安全的选择。它能识别出您的优势与买方优先事项的契合点，竞争对手可能具有优势的地方，以及您需要主动弥补弱点的地方。

### 它将每一项声明都建立在证据之上

2026 年的评估者都经过培训，能够识别 AI 生成的内容。正如 [行业评论](https://www.linkedin.com/posts/virtualbidteam_ai-trends-in-bid-writing-8-developments-activity-7442229203988713472-KGVS) 指出的，“AI 生成的提案有一种质感。经验丰富的评估者已经能察觉到。” 解决方法不是避免使用 AI，而是使用能将每一项声明都建立在具体、可验证的证据之上的 AI。上传您的案例研究、CV、政策、认证和方法论文件，提案生成器会在回复中直接引用它们，而不是凭空生成听起来合理的声明。

### 它在每一次投标中都记得您的组织

Jenova 的持久跨会话记忆意味着提案生成器在每次投标时都不会从零开始。您的组织能力、过去的案例研究、员工 CV、标准方法论描述、政策文件，甚至从以前的投标汇报中学到的经验教训都会被保留并自动应用。第十五次投标将受益于前十四次教会系统的一切。

虽然像 ChatGPT 这样的工具可以起草合理的提案文本，但它们无法将您整个组织的知识库保存在持久记忆中，无法映射评分方法，也无法制定有竞争力的致胜主题。像 Tenderbolt 和 AutogenAI 这样的专用投标平台解决了部分问题，但将您锁定在单一模型和僵化的工作流程中。Jenova 为您提供了高级投标顾问的战略深度和 AI 的速度——跨越任何模型，在您控制的对话式工作流程中。

* * *

## 您可能也会喜欢的相关智能体

### [**RFP 生成器**](https://www.jenova.ai/a/rfp-generator)

如果您在采购方工作——发布招标而不是响应招标——RFP 生成器可以处理需求工程、评估框架设计和文件生成。对于投标团队来说，它同样有价值：了解 RFP 是如何 _构建_ 的，能让您在解读规范语言背后买家真正关心的内容时获得战略优势。

- 需求工程和评估框架构建
- 为投标策略提供信息的采购方情报
- 为任何采购框架生成合规的文件

### [**写作助手**](https://www.jenova.ai/a/writing-assistant)

用于将一份强有力的投标书与一份中标书区分开来的最终润色。在提案生成器处理完策略、合规性和基于证据的起草后，写作助手提供逐行编辑——精简文笔、确保语调一致、消除冗余，并使每个句子都为评估者发挥更大作用。

- 具有精细语调和语域控制的逐行编辑
- 适应正式的采购、技术和高管沟通风格
- 最终提交前审查阶段的理想选择

### [**商业计划书撰写器**](https://www.jenova.ai/a/business-plan-writer)

许多招标——特别是政府合同、社会企业和对初创企业友好的采购框架——需要商业计划书的组成部分：财务模型、市场规模估算、组织能力陈述和增长预测。商业计划书撰写器能以评估者期望的严谨性生成这些元素。

- 用于投标内嵌商业案例的财务建模和市场规模估算
- 战略验证和组织能力叙述
- 以商业深度补充提案回复

### [**PDF 文档生成器**](https://www.jenova.ai/a/pdf-doc-generator)

投标书提交要求精确的格式——页数限制、字体要求、章节编号和专业呈现。PDF 文档生成器将您的最终回复转化为具有自适应专业设计的、可随时提交的文件。

- 创建符合格式要求的专业 PDF
- 匹配采购提交要求的自适应设计
- 可导出用于门户上传或打印提交的文件

* * *

## AI 标书撰写在 Jenova 上的工作原理

### 第 1 步：上传并分析招标文件

打开 [**提案生成器**](https://www.jenova.ai/a/proposal-generator) 并上传完整的 RFP/ITT 包——招标文件、规格说明、评估标准、定价表以及任何买方发布的澄清文件。智能体将阅读整个文件集并生成结构化分析：

> _“分析这份 78 页的设施管理服务 ITT 文件。提取所有评估标准及其权重。识别强制性的通过/失败要求与计分问题。构建一个合规矩阵。标记出规范语言中任何不寻常的要求或隐藏的评估优先事项。”_

### 第 2 步：制定致胜主题和策略

在写下任何回复之前，先确定您的竞争定位。告诉智能体您组织的优势、可能的竞争对手以及与该买方的关系背景：

> _“我们是一家中型 FM 供应商，与两家全国性公司和一家本地专业公司竞争。我们的优势是员工保留率（92%，而行业平均为 74%）、在买方所在地区有强大的社会价值项目，以及在类似合同上超越 KPI 的记录。我们的弱点是我们以前没有与该买方签订过合同。制定三个致胜主题，将我们定位为低风险、高价值的选择。”_

### 第 3 步：上传您的证据库

向智能体提供您的案例研究、员工 CV、方法论文件、政策、认证以及任何表现良好的过往投标回复。持久记忆会在所有会话中保留这一切——您只需上传一次，未来的每一次投标都将受益：

> _“这里有四个来自类似 FM 合同的案例研究（两个 NHS，一个地方当局，一个大学），我们的 TUPE 转移方法论，我们的社会价值政策，以及拟议合同经理和运营总监的 CV。在所有回复中直接引用这些——绝不提出我们无法证明的主张。”_

### 第 4 步：起草为得分优化的回复

智能体起草的回复结构围绕评估者实际评分的方式——以答案开头，用证据支持，并展示对买方具体挑战的理解：

> _“起草对问题 3.2 的回复：‘描述您对此合同的动员和 TUPE 转移方法。’该问题占总分的 15%。使用我们的 TUPE 方法论文件和 NHS Highland 案例研究。回复必须展示对转移期间员工焦虑的理解，并显示具体的缓解措施。最多 1500 字。”_

### 第 5 步：审查、完善和格式化

通过具体反馈对每个回复进行迭代。使用 [**写作助手**](https://www.jenova.ai/a/writing-assistant) 进行最终的文笔润色，使用 [**PDF 文档生成器**](https://www.jenova.ai/a/pdf-doc-generator) 进行提交就绪的格式化。整个过程——从 RFP 分析到格式化的提交——都在一个具有完整上下文保留的单一平台上运行：

> _“动员回复很强，但太长了——在不丢失 NHS Highland 案例研究细节的情况下，将其削减到 1200 字。加强开篇段落——评估者应该在头三句话内就知道我们的关键差异化因素。添加一个 12 周动员计划的可视化时间线。”_

* * *

## 结果与用例

### 📊 与全国性公司竞争的中小企业投标团队

**场景：** 一家拥有 200 名员工的设施管理公司竞标一份价值 400 万英镑的地方当局合同。他们与三家拥有 10 人以上专职投标团队的全国性供应商竞争。他们的“投标团队”是两名运营经理，他们在日常工作之余撰写标书。

**传统方法：** 花费晚上和周末的时间重写去年的投标回复。忽略了新评估标准中的细微差别。提交了一份合规但普通的提案，得分 62/100，而中标者为 78/100。汇报反馈：“缺乏具体证据和差异化。”

**Jenova 解决方案：** 第一天就将 ITT 上传到 [**提案生成器**](https://www.jenova.ai/a/proposal-generator)。一小时内获得合规矩阵和评分分析。制定致胜主题，利用中小企业 92% 的员工保留率和本地优势，对抗全国性公司的规模但距离远的定位。用直接的案例研究参考来起草每一份回复。两位经理将时间花在策略和利益相关者沟通上——AI 负责写作。提交质量与全国性公司的专职投标团队相媲美。总投标准备时间：减少 60%。

### 💼 从每年 5 份扩展到 25 份投标的咨询公司

**场景：** 一家成长中的 IT 咨询公司希望竞标更多的公共部门框架，但如果不雇佣一名全职标书撰写人（薪水 4.5-6.5 万英镑外加管理费用），就无法扩大其投标产出。

**传统方法：** 雇佣一名标书撰写人，他需要三个月时间来了解组织的能力和过往工作。或者外包给投标咨询公司，每份标书费用为 2000-5000 英镑。无论哪种方式，每份投标的成本都使得边际机会不经济。

**Jenova 解决方案：** 在 Jenova 的持久记忆中一次性建立组织的证据库——案例研究、CV、方法论、政策、认证。随后的每一次投标都会自动从该库中提取。提案生成器处理初稿；主题专家审查并增加技术深度；写作助手进行润色。该公司在不增加人手的情况下，将年投标量从 5 份扩大到 25 份。持久记忆意味着第 25 份投标比第 5 份更快、质量更高。

### 📱 独立顾问在移动设备上响应投标

**场景：** 一位自由职业的可持续发展顾问在为客户出差时发现了一个截止日期为 10 天的投标机会。他们无法在办公桌前坐上三天来写回复。

**传统方法：** 放弃这个机会。或者在漫长的工作日后，在酒店房间里尝试写一份仓促的回复。提交一些平庸的东西，然后听天由命。

**Jenova 解决方案：** 在移动设备上打开提案生成器，上传招标文件，在途中收到评估分析。在空闲时间通过语音转文本口述战略输入——组织优势、相关经验、建议方法。智能体起草合规、有证据支持的回复。顾问在晚上用平板电脑审查和编辑。一份专业、有竞争力的投标书在第 8 天发出——没有花一整天坐在办公桌前。

### 🏗️ 应对复杂公共采购的建筑公司

**场景：** 一家建筑公司竞标一份价值 1200 万英镑的学校翻新合同，该合同有一份 120 页的 PQQ/ITT 文件、14 个计分问题、强制性的社会价值承诺和一个演示阶段。投标经理同时还在管理另外两个正在进行的投标。

**传统方法：** 投标经理连续三周每天工作 14 小时。所有三个投标的质量都受到影响。权重为 20% 的社会价值回复最后才写，而且写得很差。提交后汇报显示：“技术方法强，社会价值叙述弱。”

**Jenova 解决方案：** 提案生成器同时映射所有三个投标，识别出可以在哪里交叉引用证据，以及每个投标需要独特定位的地方。对于学校翻新项目，它将 20% 的社会价值权重标记为最高单一问题机会，并首先起草详细回复。 [**RFP 生成器**](https://www.jenova.ai/a/rfp-generator) 提供了关于评估小组可能如何构建评分方法的见解——为回复结构提供信息。三份投标按时提交，每份都具有战略差异化。

* * *

## 常见问题解答

### 什么是 AI 标书撰写？

AI 标书撰写是利用人工智能来协助分析招标文件、构建合规矩阵、制定致胜主题、起草计分回复以及格式化最终提交文件。它不能取代投标策略——它能放大策略。Jenova 的 [**提案生成器**](https://www.jenova.ai/a/proposal-generator) 处理整个投标生命周期：RFP 分析、合规映射、基于证据的起草和竞争定位，其持久记忆能在每一次投标中保留您组织的能力。

### AI 真的能赢得投标，还是只是写得更快？

单靠速度是赢不了投标的。正如 [投标专业人士所观察到的](https://www.linkedin.com/posts/virtualbidteam_ai-trends-in-bid-writing-8-developments-activity-7442229203988713472-KGVS)，缺乏策略、证据和差异化的 AI 润色提案，得分并不比手动编写的通用回复高。当 AI 用于战略分析时，它才能赢得投标——映射评估标准、识别得分机会、将声明建立在具体证据之上，并围绕评估者实际评分的方式构建回复。提案生成器正是为这种深度而构建的，而不仅仅是为了起草速度。

### AI 标书撰写与聘请投标顾问相比如何？

一位高级投标顾问每天的费用在 500-2000 英镑之间，他们带来深厚的采购知识、利益相关者管理能力和战略判断力。对于复杂、高价值的投标，AI 标书撰写无法取代这种专业知识——但它能显著减少合规映射、初稿生成和证据检索所需的时间。对于无法为每次投标都聘请顾问的组织，Jenova 以一小部分成本提供了可扩展到无限并发投标的战略分析和起草能力。

### AI 生成的投标内容会被评估者发现吗？

到 2026 年，经验丰富的评估者越来越能识别出 AI 生成的文稿。解决方法不是避免使用 AI，而是使用能根据 _您_ 的特定证据、案例研究和组织口吻生成内容，而不是通用样板文件的 AI。提案生成器直接引用您上传的文件，生成的回复包含任何通用 AI 工具都无法编造的组织特定细节。结合主题专家的审查，输出的内容读起来像是专业撰写的，而不是机器生成的。

### Jenova 用于标书撰写是免费的吗？

Jenova 提供免费套餐，可以访问提案生成器、RFP 生成器、写作助手和所有其他智能体——无需信用卡。起价为每月 20 美元的付费计划提供扩展使用量、跨 GPT-5.4、Claude Opus 4.6、Gemini 3.1 Pro Preview 等的自定义模型选择。对于处理大量投标的团队来说，跨会话的持久记忆意味着每一次后续投标都能从先前投标中建立的组织知识中受益。

### 我可以为公共部门的投标使用 AI 标书撰写吗？

当然可以。公共部门采购是 AI 标书撰写能提供最大价值的地方——复杂的合规要求、详细的评估标准、严格的格式规则和繁重的证据负担。 [Art of Procurement 的 2026 年报告](https://artofprocurement.com/blog/state-of-ai-in-procurement) 证实，全球 80% 的首席采购官计划在采购工作流程中部署生成式 AI，而 [94% 的采购主管](https://suplari.com/blog/key-trends-and-pitfalls-for-procurement) 已经每周使用 AI 工具。不具备这种复杂性的投标团队正处于日益增长的劣势。

* * *

## 赢得更多投标，减少通宵熬夜

标书撰写的危机从来不在于写作本身。而在于在起草任何文字 _之前_ 必须进行的战略分析、证据收集、合规映射和竞争定位——这些工作手动完成需要数周，而当截止日期堆积时，则被压缩到几天。 [AI 投标书撰写软件市场正在增长到 5.61 亿美元](https://www.openpr.com/news/4504877/ai-bid-writing-software-research-cagr-of-7-1-during)，因为组织已经意识到，输掉投标的成本——在收入、机会、团队倦怠方面——远远超过了智能自动化的成本。

但能赢的工具不是那些写得更快的工具。而是那些 _思考_ 如何获胜的工具——分析评估者如何评分，识别差异化最重要的环节，并将每一项声明都建立在不能被视为 AI 样板文件的证据之上。这就是一份得分 65 的精良提案和一份得分 85 的战略性投标书之间的区别。

立即尝试 [**提案生成器**](https://www.jenova.ai/a/proposal-generator)——上传您的下一份招标文件，在您写下任何回复之前，就能看到完整的评估分析、合规矩阵和致胜主题策略。免费，无需信用卡。

在 [**Jenova**](https://www.jenova.ai/) 探索完整的智能体库。

![Jenova - AI 智能体平台](<Base64-Image-Removed>)

Jenova 是世界上最强大的 AI 智能体平台。访问涵盖各个领域的专家智能体，或在几分钟内创建您自己的智能体。

[在网页上使用 Jenova](https://www.jenova.ai/) [下载 iOS 应用](https://apps.apple.com/app/jenova/id6747692301) [下载 Android 应用](https://play.google.com/store/apps/details?id=ai.jenova.app.prod) [加入 Discord](https://discord.gg/EkYSQUZp4e)

[使用条款](https://www.jenova.ai/terms-of-use)

｜

[使用政策](https://www.jenova.ai/usage-policy)

｜

[隐私政策](https://www.jenova.ai/privacy-policy)

Azeroth Inc. © 2025


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
