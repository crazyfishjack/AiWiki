---
title: "调研证据包：投标AI助手 招标文件解析 提示词设计 字段抽取 数据结构 响应矩阵 审查规则"
source-type: article
generated: 2026-06-22
generated-by: wiki-research-skill
research-mode: standard
---

# 调研证据包：投标AI助手 招标文件解析 提示词设计 字段抽取 数据结构 响应矩阵 审查规则

## 调研问题

投标AI助手 招标文件解析 提示词设计 字段抽取 数据结构 响应矩阵 审查规则

## 摘要

本文档是四工具检索生成的证据包草稿，不是最终调研报告。Agent 必须先阅读本证据包，执行下方"AI 综合指令"，生成新的中文综合 raw 报告，然后询问用户是否入库。本证据包保留不删除。

- 发现候选信源：24
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
| exa | 1.00 | A Large Language Model-based Framework for Semi-Structured Tender Document Retrieval-Augmented Generation | https://arxiv.org/html/2410.09077v1 |
| exa | 1.00 | Information Extraction from Visually Rich Documents using LLM-based Organization of Documents into Independent Textual Segments | https://arxiv.org/html/2505.13535v1 |
| exa | 1.00 | Arctic-Extract Technical Report | https://arxiv.org/html/2511.16470v1 |
| exa | 1.00 | Large Language Model for Extracting Complex Contract Information in Industrial Scenes | https://arxiv.org/html/2507.06539v2 |
| exa | 1.00 | [2603.13651v1] Benchmarking Large Language Models on Reference Extraction and Parsing in the Social Sciences and Humanities | https://arxiv.org/abs/2603.13651v1 |
| exa | 1.00 | [2309.10952] LMDX: Language Model-based Document Information Extraction And Localization | https://arxiv.org/pdf/2309.10952 |
| exa | 1.00 | [2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models | https://arxiv.org/abs/2309.12132v2 |
| exa | 1.00 | OmniCompliance-100K: A Multi-Domain, Rule-Grounded, Real-World Safety Compliance Dataset | https://arxiv.org/pdf/2603.13933 |
| exa | 1.00 | Intelligent Processing of Design Notices in Engineering Procurement Construction Projects | https://www.mdpi.com/2075-5309/15/5/805 |
| exa | 1.00 |  | https://arxiv.org/pdf/2603.00369 |
| exa | 1.00 | ProcureGym: A Multi-Agent Markov Game Framework for Modeling National Volume-based Drug Procurement | https://arxiv.org/html/2603.23880v1 |
| exa | 1.00 | BKRAG : A BGE Reranker RAG for similarity analysis of power project requirements | https://dl.acm.org/doi/fullHtml/10.1145/3689218.3689224 |
| exa | 1.00 | AIReg-Bench: Benchmarking Language Models That Assess AI Regulation Compliance | https://arxiv.org/html/2510.01474v3 |
| exa | 1.00 | Extract-0: A Specialized Language Model for Document Information Extraction | https://arxiv.org/html/2509.22906v1 |
| exa | 1.00 | AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects | https://www.mdpi.com/1996-1073/14/15/4632 |
| tavily | 0.68 | 标书智能体（一）——AI解析招标文件代码+提示词 - 博客园 | https://www.cnblogs.com/yibiaoai/p/19064673 |
| tavily | 0.65 | 智能标书助手-艾瑞数智 | https://www.idigital.com.cn/common-ai-2 |
| tavily | 0.59 | 零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF上传自动提条款、标风险、出建议-腾讯云开发者社区-腾讯云 | https://cloud.tencent.com/developer/article/2631225 |
| tavily | 0.58 | 喜鹊标书AI \| AI 标书制作平台与投标方案助手 | https://www.xiquebiaoshu.com |
| tavily | 0.57 | 数据提取 - 智谱AI开放文档 | https://docs.bigmodel.cn/cn/best-practice/case/data-extraction |
| tavily | 0.51 | 高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云 | https://cloud.tencent.com/developer/article/2498790 |
| tavily | 0.50 | View of AI在招投标文件编制中的应用 - omniscient | http://ojs.omniscient.sg/index.php/mepm/article/view/69302/67852 |
| tavily | 0.46 | 关于加快招标投标领域人工智能推广应用的实施意见(发改法规〔2026 ... | https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html |
| tavily | 0.44 | CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统 | https://patents.google.com/patent/CN119624385A/zh |

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
2. [Information Extraction from Visually Rich Documents using LLM-based Organization of Documents into Independent Textual Segments](https://arxiv.org/html/2505.13535v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
3. [Arctic-Extract Technical Report](https://arxiv.org/html/2511.16470v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
4. [Large Language Model for Extracting Complex Contract Information in Industrial Scenes](https://arxiv.org/html/2507.06539v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
5. [[2603.13651v1] Benchmarking Large Language Models on Reference Extraction and Parsing in the Social Sciences and Humanities](https://arxiv.org/abs/2603.13651v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
6. [[2309.10952] LMDX: Language Model-based Document Information Extraction And Localization](https://arxiv.org/pdf/2309.10952)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
7. [[2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models](https://arxiv.org/abs/2309.12132v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
8. [OmniCompliance-100K: A Multi-Domain, Rule-Grounded, Real-World Safety Compliance Dataset](https://arxiv.org/pdf/2603.13933)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
9. [Intelligent Processing of Design Notices in Engineering Procurement Construction Projects](https://www.mdpi.com/2075-5309/15/5/805)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
10. [https://arxiv.org/pdf/2603.00369](https://arxiv.org/pdf/2603.00369)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
11. [ProcureGym: A Multi-Agent Markov Game Framework for Modeling National Volume-based Drug Procurement](https://arxiv.org/html/2603.23880v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
12. [BKRAG : A BGE Reranker RAG for similarity analysis of power project requirements](https://dl.acm.org/doi/fullHtml/10.1145/3689218.3689224)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
13. [AIReg-Bench: Benchmarking Language Models That Assess AI Regulation Compliance](https://arxiv.org/html/2510.01474v3)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
14. [Extract-0: A Specialized Language Model for Document Information Extraction](https://arxiv.org/html/2509.22906v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
15. [AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects](https://www.mdpi.com/1996-1073/14/15/4632)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
16. [标书智能体（一）——AI解析招标文件代码+提示词 - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.68
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
17. [智能标书助手-艾瑞数智](https://www.idigital.com.cn/common-ai-2)
   - 工具：tavily
   - 分数：0.65
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
18. [零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF上传自动提条款、标风险、出建议-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2631225)
   - 工具：tavily
   - 分数：0.59
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
19. [喜鹊标书AI | AI 标书制作平台与投标方案助手](https://www.xiquebiaoshu.com)
   - 工具：tavily
   - 分数：0.58
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
20. [数据提取 - 智谱AI开放文档](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
21. [高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.51
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
22. [View of AI在招投标文件编制中的应用 - omniscient](http://ojs.omniscient.sg/index.php/mepm/article/view/69302/67852)
   - 工具：tavily
   - 分数：0.50
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
23. [关于加快招标投标领域人工智能推广应用的实施意见(发改法规〔2026 ...](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html)
   - 工具：tavily
   - 分数：0.46
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
24. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统](https://patents.google.com/patent/CN119624385A/zh)
   - 工具：tavily
   - 分数：0.44
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考

### 剔除信源
1. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统](https://patents.google.com/patent/CN119624385A/zh)
   - 工具：tavily
   - 分数：0.37
   - 来源等级：C
   - 剔除原因：score 低于 0.4
2. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.36
   - 来源等级：C
   - 剔除原因：score 低于 0.4
3. [智领招投标，赋能新发展——广东引领推进“人工智能+招标投标”创新应用 | 广州市发展和改革委员会网站](http://fgw.gz.gov.cn/tzgg/content/post_10704480.html)
   - 工具：tavily
   - 分数：0.35
   - 来源等级：C
   - 剔除原因：score 低于 0.4
4. [招标中标信息抽取-高级版服务 - 阿里云帮助文档](https://help.aliyun.com/zh/document_detail/256460.html)
   - 工具：tavily
   - 分数：0.32
   - 来源等级：C
   - 剔除原因：score 低于 0.4
5. [CN117764039A - 基于大模型的投标文件生成方法、系统、终端及存储介质 
        - Google Patents](https://patents.google.com/patent/CN117764039A/zh)
   - 工具：tavily
   - 分数：0.21
   - 来源等级：C
   - 剔除原因：score 低于 0.4
6. [智能标书助手-艾瑞数智](https://www.idigital.com.cn/common-ai-2)
   - 工具：tavily
   - 分数：0.60
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
7. [数据提取 - 智谱AI开放文档](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction)
   - 工具：tavily
   - 分数：0.53
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
8. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统](https://patents.google.com/patent/CN119624385A/zh)
   - 工具：tavily
   - 分数：0.38
   - 来源等级：C
   - 剔除原因：score 低于 0.4
9. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.35
   - 来源等级：C
   - 剔除原因：score 低于 0.4
10. [招标中标信息抽取-高级版服务 - 阿里云帮助文档](https://help.aliyun.com/zh/document_detail/256460.html)
   - 工具：tavily
   - 分数：0.33
   - 来源等级：C
   - 剔除原因：score 低于 0.4
11. [[PDF] 招标文件 - 国家药品监督管理局](https://www.nmpa.gov.cn/directory/web/nmpa/images/yv2+3bHq17y53MDt19PPtc2z1dCx6s7EvP4ttdq2rTOLnBkZg==.pdf)
   - 工具：tavily
   - 分数：0.24
   - 来源等级：C
   - 剔除原因：score 低于 0.4
12. [[PDF] 标准设计招标文件](https://www.ndrc.gov.cn/fzggw/jgsj/fgs/sjdt/201709/W020190910481383804853.pdf)
   - 工具：tavily
   - 分数：0.18
   - 来源等级：C
   - 剔除原因：score 低于 0.4
13. [[PDF] 公开招标文件（二次） - 中华人民共和国司法部](https://www.moj.gov.cn/pub/sfbgw/zwxxgk/fdzdgknr/fdzdgknrtzwj/202312/W020231205642701230671.pdf)
   - 工具：tavily
   - 分数：0.14
   - 来源等级：C
   - 剔除原因：score 低于 0.4
14. [China isn’t trying to beat the U.S. at AI — it’s playing a completely different game - fortune.com](https://fortune.com/2026/06/16/china-ai-deepseek-open-source-efficiency-global-expansion-strategy/)
   - 工具：tavily
   - 分数：0.09
   - 来源等级：C
   - 剔除原因：score 低于 0.4
15. [DOC Opens First Proposal Round Under American AI Exports Program - Pillsbury Winthrop Shaw Pittman](https://www.pillsburylaw.com/en/news-and-insights/doc-american-ai-exports-program.html)
   - 工具：tavily
   - 分数：0.08
   - 来源等级：C
   - 剔除原因：score 低于 0.4
16. [EBAday 2026: Zooming in on AI and digital assets as the key themes of the event - Finextra Research](https://www.finextra.com/newsarticle/47948/ebaday-2026-zooming-in-on-ai-and-digital-assets-as-the-key-themes-of-the-event)
   - 工具：tavily
   - 分数：0.04
   - 来源等级：C
   - 剔除原因：score 低于 0.4
17. [Ant Group 2025 Sustainability Report Highlights Record AI R&D Investment – Company Announcement - Financial Times](https://markets.ft.com/data/announce/detail?dockey=600-202606170512BIZWIRE_USPRX____20260617_BW847068-1)
   - 工具：tavily
   - 分数：0.03
   - 来源等级：C
   - 剔除原因：score 低于 0.4
18. [What is GLM-5.2? Another open-source Chinese AI model has Silicon Valley's attention. - Business Insider](https://www.businessinsider.com/what-is-glm-5-2-chinese-ai-coding-model-2026-6)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
19. [Building, backing, and buying AI in 2026 - PitchBook](https://pitchbook.com/video-library/building-backing-and-buying-ai-in-2026)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
20. [Kolon Benit Positions Itself as Manufacturing AX Strategist and Execution Partner - thelec.net](https://www.thelec.net/news/articleView.html?idxno=11407)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
21. [BE Semiconductor Raises Long-Term Revenue, Profitability Targets on AI Boost - WSJ](https://www.wsj.com/business/earnings/be-semiconductor-raises-long-term-revenue-profitability-targets-on-ai-boost-c47d5f77)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
22. [2026 Fierce Outsourcing Awards - Fierce Biotech](https://www.fiercebiotech.com/book/2026-fierce-outsourcing-awards)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
23. [AI & Advanced Analytics - Fierce Biotech](https://www.fiercebiotech.com/cro/ai-advanced-analytics)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
24. [标书智能体（一）——AI解析招标文件代码+提示词 - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.62
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
25. [数据提取 - 智谱AI开放文档](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction)
   - 工具：tavily
   - 分数：0.51
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
26. [智能标书助手-艾瑞数智](https://www.idigital.com.cn/common-ai-2)
   - 工具：tavily
   - 分数：0.50
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
27. [零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF ...](https://cloud.tencent.com/developer/article/2631225)
   - 工具：tavily
   - 分数：0.46
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
28. [招标文件智能解析系统开发文档 - CSDN博客](https://blog.csdn.net/rvgekj/article/details/146287931)
   - 工具：tavily
   - 分数：0.35
   - 来源等级：C
   - 剔除原因：score 低于 0.4
29. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统](https://patents.google.com/patent/CN119624385A/zh)
   - 工具：tavily
   - 分数：0.35
   - 来源等级：C
   - 剔除原因：score 低于 0.4
30. [基于智能文档处理的招投标信息自动抓取和匹配-来也科技](https://laiye.com/news/post/2113.html)
   - 工具：tavily
   - 分数：0.31
   - 来源等级：C
   - 剔除原因：score 低于 0.4
31. [[PDF] 招标文件 - 上海建工](https://www.scg.com.cn/uploadpath/2021/7/23/7677149e-1402-422d-9b82-aafea8e75205.pdf)
   - 工具：tavily
   - 分数：0.12
   - 来源等级：C
   - 剔除原因：score 低于 0.4
32. [[PDF] 招标文件 - 国家药品监督管理局](https://www.nmpa.gov.cn/directory/web/nmpa/images/yv2+3bHq17y53MDt19PPtc2z1dCx6s7EvP4ttdq2rTOLnBkZg==.pdf)
   - 工具：tavily
   - 分数：0.11
   - 来源等级：C
   - 剔除原因：score 低于 0.4
33. [智能标书助手-艾瑞数智](https://www.idigital.com.cn/common-ai-2)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
34. [数据提取 - 智谱AI开放文档](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction)
   - 工具：tavily
   - 分数：0.56
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
35. [高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.43
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
36. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.39
   - 来源等级：C
   - 剔除原因：score 低于 0.4
37. [智领招投标，赋能新发展](https://www.gdwc.gov.cn/zjwcfgw/gkmlpt/content/2/2153/post_2153176.html?jump=true)
   - 工具：tavily
   - 分数：0.33
   - 来源等级：C
   - 剔除原因：score 低于 0.4
38. [[PDF] 招标文件 - 国家药品监督管理局](https://www.nmpa.gov.cn/directory/web/nmpa/images/yv2+3bHq17y53MDt19PPtc2z1dCx6s7EvP4ttdq2rTOLnBkZg==.pdf)
   - 工具：tavily
   - 分数：0.29
   - 来源等级：C
   - 剔除原因：score 低于 0.4
39. [[PDF] 招标文件 - 中华人民共和国司法部](https://www.moj.gov.cn/pub/sfbgw/zwxxgk/fdzdgknr/fdzdgknrtzwj/202501/W020250122622938330518.pdf)
   - 工具：tavily
   - 分数：0.27
   - 来源等级：C
   - 剔除原因：score 低于 0.4
40. [[PDF] 标准设计招标文件](https://www.ndrc.gov.cn/fzggw/jgsj/fgs/sjdt/201709/W020190910481383804853.pdf)
   - 工具：tavily
   - 分数：0.25
   - 来源等级：C
   - 剔除原因：score 低于 0.4
41. [[PDF] 中华人民共和国国家标准数据基础设施数据目录描述要求](https://www.nda.gov.cn/sjj/ywpd/szkjyjcss/0408/ff808081-9b5e8657-019d-6bc2aefe-0ded.pdf)
   - 工具：tavily
   - 分数：0.09
   - 来源等级：C
   - 剔除原因：score 低于 0.4

## 完整精读结果

### 来源 1: 零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF上传自动提条款、标风险、出建议-腾讯云开发者社区-腾讯云

- URL: https://cloud.tencent.com/developer/article/2631225
- 精读方法：firecrawl-scrape

Loading \[MathJax\]/jax/input/TeX/config.js

[合合技术团队](https://cloud.tencent.com/developer/user/9938479)

作者相关精选

## 零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF上传自动提条款、标风险、出建议

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

合合技术团队

[社区首页](https://cloud.tencent.com/developer) > [专栏](https://cloud.tencent.com/developer/column) >零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF上传自动提条款、标风险、出建议

# 零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF上传自动提条款、标风险、出建议

原创

发布于 2026-02-25 01:31:42

发布于 2026-02-25 01:31:42

1.3K0

举报

### 一、为什么招标文件不能只靠人看，也不能只丢给大模型？

如果你参与过招投标，一定理解这种挑战：

- **200-500 页起步：** 包含目录、征文、技术规范、商务条款、复杂表格和各类附件。
- **时间节点密集：** 报名、答疑、截止、开标……遗漏一个就是事故。
- **关键条款分散：** 保证金、履约、付款、交付、质保、废标条款隐藏在不同章节。
- **结果必须可溯源：** 任何“风险提示”，都必须能追溯到原文的具体位置，否则毫无效力。

这正是仅靠人工处理低效，而让大模型直接“硬读”全文也常会翻车的原因：

- 文档过长会被截断，信息丢失；
- 无法可靠解析扫描件、复杂表格和特殊版式；
- 生成的总结常常笼统，无法提供可验证的原文引用。

因此， **更稳的打法是：** 先把文档变成结构化可理解的内容，再让大模型做抽取和风控。 本文将展示如何组合 **Coze（零代码平台）与TextIn xParse（文档解析引擎）**，搭建一个能真正投入使用的“招标解析 [智能体](https://cloud.tencent.com/developer/techpedia/2547?from_column=20065&from=20065)”。它能自动提取关键条款、标记风险、生成响应建议，并确保每一个结论都附有可点击追溯的原文出处。

### 二、先看效果：这个智能体能做什么？

上传一份招标文件（PDF/Word/扫描件/图片），它会输出三部分内容：

#### ✅ 关键条款摘要（1 页看完）

- 投标截止/开标时间、保证金、预算/最高限价、交付期、质保期
- 资格要求（资质/业绩/人员/财务/信誉）
- 评标办法（技术分/商务分/价格分、废标条款）

#### ✅ 风险提示

- 资格不匹配/隐性门槛
- 付款条件不利/履约风险
- 交付周期不合理
- “一票否决”/废标点
- 合同条款冲突/模糊表述

#### ✅ 响应建议（清单化可执行）

- 需要准备的材料 checklist（按部门：商务/法务/技术/财务）
- 建议澄清的问题清单（可直接复制发招标方）
- 投标策略提示（哪些点要重点写、哪些点建议偏离说明）

### 三、重点来了：TextIn做招标文件解析，优势到底在哪？

很多人做招标智能体只盯大模型，但真正决定“能不能用”的，往往是是解析层。

#### 1）更适合招标文件这种“复杂版式+表格+长文档”的解析能力

招标文件不是纯文本，是动辄几十页到几百页的长文档，而且是“文档版面理解”的集合：标题层级、目录结构、表格、页眉页脚、附件、扫描页……

**TextIn xParse** 的核心价值是：把这些复杂结构转换成 **更适合大模型处理的Markdown+结构化信息**，大幅降低“模型看不懂文档”的概率。

#### 2）输出可追溯的原文定位信息

投标场景里，单单给出风险提示没用，必须能指回原文：第几页、哪一段、哪张表。 xParse输出通常会包含 **markdown（正文）+结构块信息+页级信息**，你可以在智能体里做“引用溯源”，让输出更专业、客户更信任。

#### 3）覆盖更多真实文件形态：电子档PDF、扫描件、图片都能处理

招标文件来源很杂：有的是电子版、有的是扫描版、有的来自截图/拍照版。 解析能力覆盖越全，Demo 越不容易翻车，越能实现“现场拿客户文件就能跑”。

### 四、方案架构（无需代码能力）

**Coze负责：对话、工作流编排、输出格式、交互体验**

**TextIn xParse负责：把招标文件解析成结构化可读内容**

**LLM** **负责：条款抽取、** [**风险识别**](https://cloud.tencent.com/developer/techpedia/2530?from_column=20065&from=20065) **、建议生成**

最稳定的链路是：

1. 用户上传招标文件
2. Coze调用 **TextIn xParse 插件** → 得到 markdown/结构化结果
3. Coze用大模型做解析结果抽取：

- 关键条款抽取（结构化字段）
- 风险识别（可以带引用）

4.输出最终“招标解析报告”

![](https://developer.qcloudimg.com/http-save/9938479/070e51e748b42e75fa217865d4c3a95d.png)

### 五、Coze 实操：一步步搭建（完全零代码）

#### Step 1：新建 Bot（智能体）

- 创建 Bot
- 人设建议写得“专业+严谨”，核心强调：
  - 输出要结构化
  - 尽量引用原文/页码
  - 风险提示要分级（高/中/低）
  - 遇到信息缺失要主动提问澄清

![](https://developer.qcloudimg.com/http-save/9938479/403cf8f289c3b63f53168b5e8ba96957.png)

#### Step 2：添加插件：TextIn通用文档解析

在「技能 / 插件」里添加： **通用文档解析**。

这一步的目的就是：让 Bot 具备“读懂招标文件”的能力，而不是只会聊天。

![](https://developer.qcloudimg.com/http-save/9938479/bedd01adcd24b216e49754f4c5a9f7e3.png)

#### **Step 3：定义你的“最终输出格式”（让结果像产品）**

建议直接在Bot里约定输出结构，后面提示词都围绕它：

**输出三段：**

1. 关键条款摘要（结构化字段）
2. 风险提示（按严重程度排序，尽量含引用）
3. 响应建议（checklist）

#### Step 4：让 Bot 学会“先解析，再抽取”（最关键的稳定性技巧）

你的 Bot 在收到用户上传文件后，优先执行：

1）调用 xParse → 获取解析结果（markdown/结构化信息）

2）把解析结果喂给大模型 → 做条款抽取/风险/建议

3）最后把内容渲染成报告

### 六、提示词模板（直接可复制）

代码语言：javascript

AI代码解释

复制

```javascript

```

#### A）关键条款抽取 Prompt（建议输出 JSON，后续好渲染）

**输入：** 解析得到的 markdown

**输出：** 固定字段 JSON 你可以要求输出类似：

- 项目信息：项目名称、招标编号、标段、预算/最高限价
- 时间节点：报名截止、答疑截止、投标截止、开标时间
- 资格要求：资质/业绩/人员/财务/信誉
- 商务条款：保证金、履约保证金、付款方式、交付期、质保期
- 评标办法：评分项、废标条款摘要

#### B）风险识别 Prompt（输出风险清单，带证据）

**输入：** 上一步 JSON + markdown 中对应原文片段

**输出：** 风险列表（高/中/低） 每条风险包含：

- 风险点
- 触发原文（引用）
- 风险类型（合规/商务/交付/资质/评分/合同）
- 建议动作（澄清/补充材料/策略调整）

#### C）响应建议 Prompt（输出 checklist，能落地）

**输入：** 关键条款 JSON + 风险列表

**输出：**

- 材料清单（按部门）
- 澄清问题清单（可直接复制发招标方）
- 投标策略建议（写作重点、偏离说明建议等）

### 七、不止于总结：构建可信、可溯源的招标决策基石

通过TextIn xParse与Coze的组合，我们实现的不仅是一个工具，更是一套可靠、可验证的招标解析新流程。它将专业文档理解能力转化为团队随时可用的数字资产，让关键信息提取、风险识别与响应规划，从此建立在结构清晰、引用确凿的基础之上。 现在，你可以告别低效的人工筛查与不可信的黑盒总结，让每一份招标文件的评估，都始于一份立即可用、来源清晰的结构化报告。智能解析，正在重新定义招投标工作的起点。

原创声明：本文系作者授权腾讯云开发者社区发表，未经许可，不得转载。

如有侵权，请联系 [cloudcommunity@tencent.com](mailto:cloudcommunity@tencent.com) 删除。

[ocr](https://cloud.tencent.com/developer/tag/15010)

[行业文档识别](https://cloud.tencent.com/developer/tag/11244)

原创声明：本文系作者授权腾讯云开发者社区发表，未经许可，不得转载。

如有侵权，请联系 [cloudcommunity@tencent.com](mailto:cloudcommunity@tencent.com) 删除。

[ocr](https://cloud.tencent.com/developer/tag/15010)

[行业文档识别](https://cloud.tencent.com/developer/tag/11244)

[#Textln](https://cloud.tencent.com/developer/search/article-Textln)

[#coze](https://cloud.tencent.com/developer/search/article-coze)

评论

登录后参与评论

暂无评论

登录 后参与评论

推荐阅读

编辑精选文章

换一批

[万字详解高可用架构设计\\
16972](https://cloud.tencent.com/developer/article/2485144)

[Go 开发者必备：Protocol Buffers 入门指南\\
11514](https://cloud.tencent.com/developer/article/2490247)

[10分钟带你彻底搞懂分布式链路跟踪\\
10196](https://cloud.tencent.com/developer/article/2493091)

[多租户的 4 种常用方案\\
14797](https://cloud.tencent.com/developer/article/2497507)

[亿级月活的社交 APP，陌陌如何做到 3 分钟定位故障？\\
11875](https://cloud.tencent.com/developer/article/2416967)

[60页PPT全解：DeepSeek系列论文技术要点整理\\
13343](https://cloud.tencent.com/developer/article/2505000)

[招投标文件结构化：为什么不要全文直抽？先切块再按模块定义输入输出（附GitHub项目地址）](https://cloud.tencent.com/developer/article/2655763?policyId=1003)

[github](https://cloud.tencent.com/developer/tag/10284)

[​项目介绍：​这是一个面向投标/评标场景的结构化抽取工具。支持上传 PDF、Word 或 Excel 格式的招标文件，自动提取项目基础信息、投标资格、技术与商务要求、评标办法等关键条款，并还原目录层级与跨页表格。输出结构化 JSON/Excel，适用于招标文件智能生成、AI 辅助评标及招投标知识库建设。](https://cloud.tencent.com/developer/article/2655763?policyId=1003)

合合技术团队

2026/04/16

3110

![招投标文件结构化：为什么不要全文直抽？先切块再按模块定义输入输出（附GitHub项目地址）](https://developer.qcloudimg.com/http-save/yehe-9938479/1180ec75e178ecb93008ff5456813370.jpg)

[从通用Agent到招标文件合规引擎：基于 openJiuwen + Skills 的工程化落地实践](https://cloud.tencent.com/developer/article/2679822?policyId=1003)

[腾讯云智能体开发平台](https://cloud.tencent.com/developer/tag/18050) [腾讯技术创作特训营S18](https://cloud.tencent.com/developer/tag/18247) [agent](https://cloud.tencent.com/developer/tag/11736) [工企 AI](https://cloud.tencent.com/developer/tag/11563)

[过去一年，Agent 被讨论得太多了。几乎所有技术文章和者公众号都在讲例如：ReAct、多 Agent 协作、Workflow、Tool Calling、MCP、Function Calling等技术概念和功能，看起来，智能体已经无所不能。](https://cloud.tencent.com/developer/article/2679822?policyId=1003)

fanstuck

2026/06/01

4352

![从通用Agent到招标文件合规引擎：基于 openJiuwen + Skills 的工程化落地实践](https://developer.qcloudimg.com/http-save/yehe-9822651/968c6d03044f9316e7c85eba4193ba89.png)

[【软件造价咨询】信息化项目投标流程及注意事项](https://cloud.tencent.com/developer/article/1901827?policyId=1003)

[(3)澄清或修改招标文件的时间：澄清或修改招标文件影响投标文件编制的，应在投标截止时间15日前作出。](https://cloud.tencent.com/developer/article/1901827?policyId=1003)

Hopestarit

2021/11/16

1.5K0

![【软件造价咨询】信息化项目投标流程及注意事项](https://ask.qcloudimg.com/article-cover-image/9180628/utb3osiold.png)

[大模型时代，如何用 AI 实现企业合同审查提效：一套基于Coze+TextIn“条款审阅 + 规范审阅”轻量落地方案](https://cloud.tencent.com/developer/article/2637718?policyId=1003)

[大数据](https://cloud.tencent.com/developer/tag/10796) [人工智能](https://cloud.tencent.com/developer/tag/10539)

[在许多公司，合同审查是一个典型的“高频、重复、依赖经验”的流程：\\
业务同事不断发合同给法务，法务不断做“初筛 \+ 修改建议 \+ 来回沟通”。业务侧频繁发起需求，法务团队则深陷于“接收-初筛-批注-沟通”的往复循环。消耗专业人力的，往往并非艰深的法律研判，而是大量重复、琐碎的基础工作：](https://cloud.tencent.com/developer/article/2637718?policyId=1003)

合合技术团队

2026/03/12

1.5K0

![大模型时代，如何用 AI 实现企业合同审查提效：一套基于Coze+TextIn“条款审阅 + 规范审阅”轻量落地方案](https://developer.qcloudimg.com/http-save/yehe-9938479/2ee2d1e48433657601915d0ddce9f543.jpg)

[告别碎片化输入：TextIn xParse如何为RAG打造「零损耗」知识管道](https://cloud.tencent.com/developer/article/2551960?policyId=1003)

[人工智能](https://cloud.tencent.com/developer/tag/10539) [大数据](https://cloud.tencent.com/developer/tag/10796) [算法](https://cloud.tencent.com/developer/tag/17460)

[在AI应用极速发展的当下，LLM（大语言模型）与RAG（检索增强生成）系统已成为构建智能问答、知识管理等高阶应用的核心引擎。](https://cloud.tencent.com/developer/article/2551960?policyId=1003)

合合技术团队

2025/08/06

7230

![告别碎片化输入：TextIn xParse如何为RAG打造「零损耗」知识管道](https://developer.qcloudimg.com/http-save/yehe-9938479/3ed8c16f05ce858f52eb849fd62f9ac1.jpg)

[基于HAI部署DeepSeekR1的招标文书智能辅助生产开发与应用](https://cloud.tencent.com/developer/article/2493787?policyId=1003)

[腾讯技术创作特训营S11#重启人生](https://cloud.tencent.com/developer/tag/18102) [大模型部署](https://cloud.tencent.com/developer/tag/18105) [DeepSeek](https://cloud.tencent.com/developer/tag/18107) [腾讯云智能体开发平台](https://cloud.tencent.com/developer/tag/18050)

[在日常商业活动中，招投标流程往往是企业竞标和项目落地的关键一环。其中，招标文书的编写工作对于投标企业极具挑战：既要保证逻辑清晰、条理分明，又必须遵循招标机构的各类格式规范，甚至还有特定行业的专业术语和合规条款。这种冗长而繁琐的写作过程，不仅费时费力，还容易出现“疏漏要点”或“措辞不当”等问题，直接影响招标结果。](https://cloud.tencent.com/developer/article/2493787?policyId=1003)

fanstuck

2025/02/06

3.8K2

![基于HAI部署DeepSeekR1的招标文书智能辅助生产开发与应用](https://developer.qcloudimg.com/http-save/yehe-9822651/9e15f305a1842ce7b2d73b8fc79b39f3.png)

[大模型开发落地实战-长上下文多模态场景大模型运用实战](https://cloud.tencent.com/developer/article/2485326?policyId=1003)

[LLM](https://cloud.tencent.com/developer/tag/17917) [腾讯混元大模型](https://cloud.tencent.com/developer/tag/17970) [腾讯云智能体开发平台](https://cloud.tencent.com/developer/tag/18050) [腾讯技术创作特训营S11#重启人生](https://cloud.tencent.com/developer/tag/18102)

[如何从零开始实现 AI 项目的落地？这是每个开发者和企业在迈向智能化时都会面临的核心问题。在本人创建的《人工智能项目落地实战指南》专栏中，我从实践角度出发，为大家梳理了大模型技术在市场应用中的三大方向，并根据 AI 运用的深浅程度进行分类。](https://cloud.tencent.com/developer/article/2485326?policyId=1003)

fanstuck

2025/01/07

2.8K2

![大模型开发落地实战-长上下文多模态场景大模型运用实战](https://developer.qcloudimg.com/http-save/yehe-9822651/bc1b6260b24bbaae4201c817febc145c.webp)

[AI 破局招投标！投标龙：4 大智能能力降 75% 废标率，助投标方轻松赢标](https://cloud.tencent.com/developer/article/2583012?policyId=1003)

[人工智能](https://cloud.tencent.com/developer/tag/10539) [AIGC](https://cloud.tencent.com/developer/tag/11746)

[在 AI 深度渗透招投标行业的当下，从招标文件解析到评标风险防控，智能化工具已成为投标方突破竞争的关键。投标龙作为金润科技深耕建设行业 20 年打造的智能投标解决方案，聚焦投标方核心痛点，将 AI 技术融入 “文件编制 - 风险审查 - 围串标防范 - 评标适配” 全流程，成为投标团队提升效率、降低废标率、提高中标概率的核心利器。](https://cloud.tencent.com/developer/article/2583012?policyId=1003)

招投标免费AI工具

2025/10/31

2.4K1

![AI 破局招投标！投标龙：4 大智能能力降 75% 废标率，助投标方轻松赢标](https://developer.qcloudimg.com/http-save/yehe-11892465/68a2e6af0ed47535570eff414e1738f5.png)

[AI智能辅助评标系统功能](https://cloud.tencent.com/developer/article/2568156?policyId=1003)

[智能审核](https://cloud.tencent.com/developer/tag/11149)

[智能辅助评标系统是一种基于人工智能（AI）、大数据分析和自动化技术的招投标管理工具，旨在提升评标效率、减少人为干预、确保公平合规。](https://cloud.tencent.com/developer/article/2568156?policyId=1003)

用户10809958

2025/09/15

1.4K0

[高效速搭基于DeepSeek的招标文书智能写作Agent](https://cloud.tencent.com/developer/article/2498790?policyId=1003)

[腾讯云大模型知识引擎xDeepSeek](https://cloud.tencent.com/developer/tag/18111) [LLM](https://cloud.tencent.com/developer/tag/17917) [腾讯云智能体开发平台](https://cloud.tencent.com/developer/tag/18050) [DeepSeek](https://cloud.tencent.com/developer/tag/18107)

[如果你一直在跟着博主的脚步探索AI大模型的相关内容，从最初的大模型Prompt工程解析，到实际的开发部署，再到深入NL2SQL、知识图谱大模型和ChatBI等更高阶应用，应该已经感受到了我们一步一个脚印，从迈过一道道技术难关，到搭建起属于自己的技术桥梁的过程。如今，我们或许对大模型的开发已经有些轻车熟路，但也必须承认，技术的迭代速度实在太快了。要想跟上AI技术发展的步伐，把最新的人工智能技术融入现有业务和应用场景才是我们追求的最终目标。](https://cloud.tencent.com/developer/article/2498790?policyId=1003)

fanstuck

2025/02/23

6.2K7

![高效速搭基于DeepSeek的招标文书智能写作Agent](https://developer.qcloudimg.com/http-save/yehe-9822651/5a0e66949eda627b0f455c113c73763d.png)

[5 月 26 日三部门重磅发文！招投标智能体正式 "转正"，政企数字化最大风口来了](https://cloud.tencent.com/developer/article/2693712?policyId=1003)

[行业](https://cloud.tencent.com/developer/tag/17292) [数据](https://cloud.tencent.com/developer/tag/17440) [代理](https://cloud.tencent.com/developer/tag/17225) [服务](https://cloud.tencent.com/developer/tag/17264) [工作](https://cloud.tencent.com/developer/tag/17284)

[2026 年 5 月 26 日，国家网信办、国家发展改革委、工业和信息化部三部门联合印发《智能体规范应用与创新发展实施意见》，首次在国家顶层设计中将招标投标明确列为智能体赋能社会治理的重点应用领域。这标志着招投标智能体从 "试点探索" 正式进入 "全面推广" 的新阶段，也意味着一个年交易规模超40 万亿元的巨大市场，正在向智能体技术全面开放。](https://cloud.tencent.com/developer/article/2693712?policyId=1003)

瑭宋元

2026/06/19

1450

![5 月 26 日三部门重磅发文！招投标智能体正式 "转正"，政企数字化最大风口来了](https://developer.qcloudimg.com/http-save/10011/b7530210bb61a069dde7acd5d5496693.jpg)

[智能合同审查搭建教程：低质量PDF怎么处理？先解析清洗，再分路审阅（附GitHub项目地址）](https://cloud.tencent.com/developer/article/2662370?policyId=1003)

[pdf](https://cloud.tencent.com/developer/tag/15200) [智能合同审核](https://cloud.tencent.com/developer/tag/11253)

[​项目介绍：​这是一个开箱即用的合同风险检测工具。支持上传 PDF/Word 格式的购销、租赁、服务等合同文件，自动识别主体信息缺失、标的物不明、违约责任不完整等法律风险，并输出结构化审查意见与修改建议，结果可溯源至原文页码。适用于企业法务合规审查、业务合同自查及交易对手风险筛查。](https://cloud.tencent.com/developer/article/2662370?policyId=1003)

合合技术团队

2026/04/29

2050

![智能合同审查搭建教程：低质量PDF怎么处理？先解析清洗，再分路审阅（附GitHub项目地址）](https://developer.qcloudimg.com/http-save/yehe-9938479/ae145db9625dd9555061462653793cde.jpg)

[AI辅助评审系统“最强外脑”来袭，重新定义评审](https://cloud.tencent.com/developer/article/2629541?policyId=1003)

[人工智能](https://cloud.tencent.com/developer/tag/10539)

[传统评审方式耗时长、易出错，如何突破这些瓶颈，实现评审过程的高效化与公正化？郑州信源信息AI辅助评审系统应运而生，以AI技术为核心，重新定义评审新标准！](https://cloud.tencent.com/developer/article/2629541?policyId=1003)

用户10809958

2026/02/11

5001

[对话式AI爆发背后：合合信息TextIn如何用智能文档处理解决"垃圾进，垃圾出"难题？](https://cloud.tencent.com/developer/article/2560395?policyId=1003)

[数据处理](https://cloud.tencent.com/developer/tag/10805) [表格](https://cloud.tencent.com/developer/tag/17196) [模型](https://cloud.tencent.com/developer/tag/17381) [数据](https://cloud.tencent.com/developer/tag/17440) [企业](https://cloud.tencent.com/developer/tag/10573)

[先抛出一个问题，AI应用落地最多、使用最广泛的场景是什么？还是聊天机器人Chatbot，也是生成式AI最原始的UI方式。搭建Chatbot并不复杂，扣子、Dify、FastGPT、MaxKB等等都可以轻松上手搭建属于自己的Chatbot Agent。智能客服作为企业使用AI的“入门级”应用形式，看起来既简单又普通，模型+Prompt+文档RAG = 智能客服。](https://cloud.tencent.com/developer/article/2560395?policyId=1003)

用户5602664

2025/08/27

5890

![对话式AI爆发背后：合合信息TextIn如何用智能文档处理解决"垃圾进，垃圾出"难题？](https://developer.qcloudimg.com/http-save/10011/adfbbdb4c073b29d74b7abae610368b6.jpg)

[【跨国合同审查数字员工实战：3小时人工审条款→3分钟全自动化】](https://cloud.tencent.com/developer/article/2620490?policyId=1003)

[可视化](https://cloud.tencent.com/developer/tag/17348) [模型](https://cloud.tencent.com/developer/tag/17381) [配置](https://cloud.tencent.com/developer/tag/17393) [系统](https://cloud.tencent.com/developer/tag/17506) [自动化](https://cloud.tencent.com/developer/tag/10669)

[2024年第四季度，某大型制造企业的采购总监李明收到了一份来自德国供应商的采购合同。这份合同足足有87页，涵盖中、德、英三语条款，涉及模具定制、设备交付、质量验收、付款条件等复杂商务条款。按照公司流程，这份合同需要经过法务部审核条款合规性、财务部核对金额与付款条款、供应链部确认交付节点，三个部门轮流转下来，保守估计需要3个工作日。](https://cloud.tencent.com/developer/article/2620490?policyId=1003)

贺公子之数据科学与艺术

2026/01/20

4450

[用 QClaw 做了一个工程合同风险审计技能，说说我的完整实践过程](https://cloud.tencent.com/developer/article/2655790?policyId=1003)

[腾讯云OpenClaw玩虾大赛](https://cloud.tencent.com/developer/tag/18229) [OpenClaw(Clawdbot)](https://cloud.tencent.com/developer/tag/18225)

[最近公司承接了不少工程项目，合同量大，法务人手有限。每次拿到一份采购合同或者施工合同，审起来都很花时间——条款多则几十页，光是把关键风险点逐条找出来就要两三个小时。更头疼的是，有些条款藏在很不起眼的地方，一不小心就漏掉了。](https://cloud.tencent.com/developer/article/2655790?policyId=1003)

中杯可乐多加冰

2026/04/16

5080

![用 QClaw 做了一个工程合同风险审计技能，说说我的完整实践过程](https://developer.qcloudimg.com/http-save/yehe-10172274/3839583405481e76a5ea51f9366207fd.jpg)

[物流提单智能解析：覆盖海运、空运与海运单的自动化处理方案（附GitHub项目地址）](https://cloud.tencent.com/developer/article/2693454?policyId=1003)

[ocr](https://cloud.tencent.com/developer/tag/15010) [文字识别](https://cloud.tencent.com/developer/tag/10459) [github](https://cloud.tencent.com/developer/tag/10284)

[项目介绍：这是一个面向国际物流与供应链场景的提单智能解析工具。支持上传 PDF、扫描件及拍照件格式的海运提单、海运单、空运单等运输单据，自动识别单据类型，抽取发货人、收货人、通知方、起运港、目的港、货物描述、件数、重量、体积等核心字段，并输出统一结构的 JSON 格式。具备版式还原、字段块定位、多单位标准化及原文坐标溯源能力。适用于 TMS、ERP、关务和供应链系统。](https://cloud.tencent.com/developer/article/2693454?policyId=1003)

合合技术团队

2026/06/18

690

![物流提单智能解析：覆盖海运、空运与海运单的自动化处理方案（附GitHub项目地址）](https://developer.qcloudimg.com/http-save/yehe-9938479/0c020c4379624b354c11db7d7b0f5cfd.jpg)

[基于腾讯元器搭建合同发票智能体：知识库+工作流的企业提效实践](https://cloud.tencent.com/developer/article/2608452?policyId=1003)

[地球online合法外挂#企业副本](https://cloud.tencent.com/developer/tag/18208)

[本文介绍如何使用腾讯元器平台搭建一个面向企业场景的合同发票智能体。通过知识库增强专业问答能力，通过工作流实现合同条款的自动分析与优化建议生成。实测表明，该智能体能识别出合同中多个预留问题，包括多个人工审核容易遗漏的隐晦风险点。](https://cloud.tencent.com/developer/article/2608452?policyId=1003)

一只牛博

2025/12/25

3.1K7

![基于腾讯元器搭建合同发票智能体：知识库+工作流的企业提效实践](https://developer.qcloudimg.com/http-save/9459221/a802becbae58a5972bd387ca3af1097d.png)

[6000 字干货｜Coze 智能体实战：搭建需求文档到测试用例自动生成工作流！](https://cloud.tencent.com/developer/article/2685653?policyId=1003)

[自动化](https://cloud.tencent.com/developer/tag/10669) [自动化测试工具](https://cloud.tencent.com/developer/tag/17877) [自动化测试](https://cloud.tencent.com/developer/tag/10732)

[在前面的教程中，我们已经学习了Coze 平台的核心功能的使用，具体大家 可以查阅《零代码AI 智能体开发平台：Coze》目录下：](https://cloud.tencent.com/developer/article/2685653?policyId=1003)

测试开发技术

2026/06/10

6420

[零代码玩转AI大模型！DeepSeek从调参到职业级开发全攻略](https://cloud.tencent.com/developer/article/2508380?policyId=1003)

[人工智能](https://cloud.tencent.com/developer/tag/10539) [智能媒资托管](https://cloud.tencent.com/developer/tag/11106) [工企 AI](https://cloud.tencent.com/developer/tag/11563) [DeepSeek](https://cloud.tencent.com/developer/tag/18107) [腾讯云大模型知识引擎xDeepSeek](https://cloud.tencent.com/developer/tag/18111)

[​Deep Seek是一款创新的智能搜索与分析平台，致力于通过先进的人工智能技术，帮助用户高效地从海量信息中提取关键信息。](https://cloud.tencent.com/developer/article/2508380?policyId=1003)

万里顾一诚

2025/03/27

2.6K0

![零代码玩转AI大模型！DeepSeek从调参到职业级开发全攻略](https://developer.qcloudimg.com/http-save/yehe-11423712/c8fbc2349590f4bf16de883c38d640c1.png)

[合合技术团队](https://cloud.tencent.com/developer/user/9938479) 0

LV.0

这个人很懒，什么都没有留下～

关注

[文章\\
\\
162](https://cloud.tencent.com/developer/user/9938479/articles) [获赞\\
\\
257](https://cloud.tencent.com/developer/user/9938479) [专栏\\
\\
1](https://cloud.tencent.com/developer/column/96546)

作者相关精选

换一批

- [招投标文件结构化：为什么不要全文直抽？先切块再按模块定义输入输出（附GitHub项目地址）](https://cloud.tencent.com/developer/article/2655763)
- [大模型时代，如何用 AI 实现企业合同审查提效：一套基于Coze+TextIn“条款审阅 + 规范审阅”轻量落地方案](https://cloud.tencent.com/developer/article/2637718)
- [智能合同审查搭建教程：低质量PDF怎么处理？先解析清洗，再分路审阅（附GitHub项目地址）](https://cloud.tencent.com/developer/article/2662370)

目录

- 一、为什么招标文件不能只靠人看，也不能只丢给大模型？

- 二、先看效果：这个智能体能做什么？

  - ✅ 关键条款摘要（1 页看完）

  - ✅ 风险提示

  - ✅ 响应建议（清单化可执行）

- 三、重点来了：TextIn做招标文件解析，优势到底在哪？

  - 1）更适合招标文件这种“复杂版式+表格+长文档”的解析能力

  - 2）输出可追溯的原文定位信息

  - 3）覆盖更多真实文件形态：电子档PDF、扫描件、图片都能处理

- 四、方案架构（无需代码能力）

- 五、Coze 实操：一步步搭建（完全零代码）

  - Step 1：新建 Bot（智能体）

  - Step 2：添加插件：TextIn通用文档解析

  - Step 3：定义你的“最终输出格式”（让结果像产品）

  - Step 4：让 Bot 学会“先解析，再抽取”（最关键的稳定性技巧）

- 六、提示词模板（直接可复制）

  - A）关键条款抽取 Prompt（建议输出 JSON，后续好渲染）

  - B）风险识别 Prompt（输出风险清单，带证据）

  - C）响应建议 Prompt（输出 checklist，能落地）

- 七、不止于总结：构建可信、可溯源的招标决策基石

交个朋友

加入AICoding云开发技术交流群

智能编码实践分享 聚焦AI+云开发

![](https://cs.cloud.tencent.com/group1/M00/30/18/C6E9k2hYwKaAdU1WAAANzKY_z3U943.png)

加入CloudBaseAI生成专属群

AI生成式应用探索 专属技术答疑空间

![](https://cs.cloud.tencent.com/group1/M00/30/18/C6E9k2hYwX6AMLeLAAANpO1bHx8075.png)

加入架构与运维趋势交流群

技术趋势前瞻 架构演进方向

![](https://cs.cloud.tencent.com/group1/M00/2E/70/C6E9n2gN3fOAUGhxAAAeAFnkNhw529.png)

换一批

[![](https://dscache.tencent-cloud.cn/upload/nodir/tokenplan_686x194_v3_2x-1d0beda6c545169d245cf8409fa83c4b83f391de.png)广告](https://cloud.tencent.com/act/pro/tokenplan?ad_trace=d830e6e311194c48bcd6880ae7cf1161&from=29888&from_column=29888)

相关产品与服务

行业文档识别

行业文档识别（Document Optical Character Recognition，Document OCR）基于行业前沿的深度学习技术，支持将图片上的文字内容，智能识别为结构化的文本，可应用于智能核保、智能理赔、试题批改等多种行业场景，大幅提升信息处理效率。

[产品介绍](https://cloud.tencent.com/product/documentocr?from=21341&from_column=21341)

[2026年中大促 \| AI 领航 智绘未来](https://cloud.tencent.com/act/pro/warmup-202606?from=21344&from_column=21344)

加入讨论

[的问答专区 >](https://cloud.tencent.com/developer/ask)

[用户12531692](https://cloud.tencent.com/developer/user/12531692) 0

提问

- [钱怎么提现？](https://cloud.tencent.com/developer/ask/48048)
- [退款怎么提现？](https://cloud.tencent.com/developer/ask/149623)
- [在腾讯元器上搭建只能提，预发布界面能实现的功能，发布界面为啥就不行了？](https://cloud.tencent.com/developer/ask/2211409)

相关课程

[一站式学习中心 >](https://cloud.tencent.com/developer/learning)

[AI代码助手快速上手训练营\\
\\
2020人在学](https://cloud.tencent.com/developer/learning/camp/22)

[腾讯云代码助手](https://cloud.tencent.com/developer/tag/18047)

[腾讯云开发玩转小程序实战训练营\\
\\
1900人在学](https://cloud.tencent.com/developer/learning/camp/23)

[云开发 CloudBase](https://cloud.tencent.com/developer/tag/11098)

[AI绘画-StableDiffusion图像生成\\
\\
1784人在学](https://cloud.tencent.com/developer/learning/camp/19)

[腾讯混元生图](https://cloud.tencent.com/developer/tag/17609)

[高性能应用服务](https://cloud.tencent.com/developer/tag/17993)

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

2

目录

200

推荐

[首页](https://cloud.tencent.com/developer)

[MCP广场![](https://qccommunity.qcloudimg.com/image/new.png)](https://cloud.tencent.com/developer/mcp)

[返回腾讯云官网](https://cloud.tencent.com/?from=20060&from_column=20060)

[首页](https://cloud.tencent.com/developer)

[MCP广场![](https://qccommunity.qcloudimg.com/image/new.png)](https://cloud.tencent.com/developer/mcp)

[返回腾讯云官网](https://cloud.tencent.com/?from=20060&from_column=20060)

### 来源 2: 标书智能体（一）——AI解析招标文件代码+提示词 - 博客园

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

### 来源 3: 智能标书助手-艾瑞数智

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

### 来源 4: 喜鹊标书AI | AI 标书制作平台与投标方案助手

- URL: https://www.xiquebiaoshu.com
- 精读方法：firecrawl-scrape

产品功能

价格

关于我们

登录/注册

立即体验

![喜鹊标书AI](https://www.xiquebiaoshu.com/assets/images/ai-biaoshu-example-DqQ5tWRK.png)

![](https://www.xiquebiaoshu.com/assets/images/banner-title-DOQQUtTP.png)![](https://www.xiquebiaoshu.com/assets/images/banner-content-CheIegpg.png)

![](https://www.xiquebiaoshu.com/assets/images/compile-title-Bp3uRjYs.png)

10分钟生成高水准投标方案，完美匹配所有招标要求，更快响应甲方

![](https://www.xiquebiaoshu.com/assets/images/compile-contnet-LQBwelDT.png)

![](https://www.xiquebiaoshu.com/assets/images/innovative-title-CRyiXMoa.png)![](https://www.xiquebiaoshu.com/assets/images/innovative-label-CaLR_Qbp.png)

革命性的创新工具，让销售更专注于策略定制、客户关系和创新提案

![](https://www.xiquebiaoshu.com/assets/images/innovative-content-rv55GOBQ.png)

![](https://www.xiquebiaoshu.com/assets/images/agent-title-Ck3LypOj.png)

Bidding scenario whole process

即时的行业顾问

不会写、不想写的统统交给AI顾问

![](https://www.xiquebiaoshu.com/assets/images/agent-line-CuGr3lDc.png)

快速、准确、专业的方案设计、问题回答

不再因团队沟通反馈不及时，投标时间紧，出现信息错误或者遗漏等废标风险

节省琐碎问题所花的时间，更关注战略性方案规划

不再为繁杂琐碎的问题花费时间，提升工作效率

![](https://www.xiquebiaoshu.com/assets/images/agent-content-wAbJFO8Y.png)

![](https://www.xiquebiaoshu.com/assets/images/agent-content2-BjK-kWHi.png)

完美的大纲架构师

完美匹配招标要求、评分办法的项目定制大纲

![](https://www.xiquebiaoshu.com/assets/images/agent-line-CuGr3lDc.png)

项目专属大纲，不会遗漏任何评分点和响应项

根据招标文件解读出的所有需求响应项，自动编制完美大纲

易于评审人员评估、逻辑清晰的目录结构

让您的投标在众多竞争者中脱颖而出，提高中标的可能性

细心的审核员

全面检查，让废标成为不可能

![](https://www.xiquebiaoshu.com/assets/images/agent-line-CuGr3lDc.png)

更全面，更细心，多一次审核，多一份保险

不知疲倦的多次审核，确保审核的全面性和正确性

超越人工审核准确率，减少人为错误，降低成本

自动审核系统通过精准的算法和模型，避免了人为因素导致的遗漏和误判，显著降低错误率

![](https://www.xiquebiaoshu.com/assets/images/agent-content3-I5oQwKNx.png)

![](https://www.xiquebiaoshu.com/assets/images/agent-content4-obV2jjid.png)

专属的投标经验专家

利用中标项目经验，让成功可以复制

![](https://www.xiquebiaoshu.com/assets/images/agent-line-CuGr3lDc.png)

复用成功中标项目中的关键知识，调整优化，不用从头开始

引用、借鉴已中标项目的知识内容

统一的公司内知识源共享，保证方案的质量和统一性

沉淀公司知识资产，集中管理，新员工也能统一投标策略和技艺

专业的编辑助手

改写、扩写想怎么写，就能怎么写

![](https://www.xiquebiaoshu.com/assets/images/agent-line-CuGr3lDc.png)

增加细节和论点，丰富方案完整性，更加有说服力

根据章节上下文，围绕招标需求，评分准则，对响应方案的关键点进行扩展

专业且商务的笔风与公司优势特色结合，提升标书竞争力

优化、改写、润色文案，提升原创性和独特性，在评标中脱颖而出

![](https://www.xiquebiaoshu.com/assets/images/agent-content5-3VXoDV9l.png)

![](https://www.xiquebiaoshu.com/assets/images/advantage-content-CU7ZBN6z.png)

![](https://www.xiquebiaoshu.com/assets/images/reason-title-22KkFl0x.png)

我们的愿景 — 销售商务支持不仅终于能跟上业务增长的步调，而且能成为增长的助力剂

我们与阿里云人工智能团队紧密合作，打造一款可靠、安全的AI产品以赋能销售团队工作流，提升团队工作效率，提高赢单可能性

![](https://www.xiquebiaoshu.com/assets/images/reason-item1-Cu0IBL9J.png)![](https://www.xiquebiaoshu.com/assets/images/reason-item2-BUtreWc_.png)![](https://www.xiquebiaoshu.com/assets/images/reason-item3-C_gCrXRW.png)

![商务标、述标PPT、客户端等多项功能更新，喜鹊AI打通全流程编标！](https://crawler-file.oss-cn-qingdao.aliyuncs.com/0aibiaoshu/xqAiBidNews/wxArticleAssets/_YOmYY_MOX5QuPEluhjIrg/image.png)

### 商务标、述标PPT、客户端等多项功能更新，喜鹊AI打通全流程编标！

![八部门联合发文：2026招投标全面AI化，做标书的规则彻底变了](https://crawler-file.oss-cn-qingdao.aliyuncs.com/0aibiaoshu/xqAiBidNews/wxArticleAssets/YMIcFfEBkR_T2JHz5zzWWg/image.png)

### 八部门联合发文：2026招投标全面AI化，做标书的规则彻底变了

![喜鹊 AI 再升级｜这 4 个新功能，让你少熬 80%的夜](https://crawler-file.oss-cn-qingdao.aliyuncs.com/0aibiaoshu/xqAiBidNews/wxArticleAssets/P43u0YFFldaATa81Zit4uQ/image.png)

### 喜鹊 AI 再升级｜这 4 个新功能，让你少熬 80%的夜

![](https://www.xiquebiaoshu.com/assets/images/tryBox-title-B-1P5NC1.png)

让喜鹊AI来做剩下的工作

![](https://www.xiquebiaoshu.com/assets/images/tryBox-btn-BGzT3tPO.png)

### 来源 5: 关于加快招标投标领域人工智能推广应用的实施意见(发改法规〔2026 ...

- URL: https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html
- 精读方法：firecrawl-scrape

[首页](https://www.ndrc.gov.cn/) > [政务公开](https://www.ndrc.gov.cn/xxgk/) > [政策](https://www.ndrc.gov.cn/xxgk/zcfb/) > [通知](https://www.ndrc.gov.cn/xxgk/zcfb/tz/)

## 关于加快招标投标领域人工智能推广应用的实施意见(发改法规〔2026〕195号)

发布时间：2026/02/10

来源：法规司

![](https://www.ndrc.gov.cn/images/dayin.png)\[ 打印 \]

分享到微信朋友圈x

![Scan me!](<Base64-Image-Removed>)

打开微信，点击底部的“发现”，

使用“扫一扫”即可将网页分享至朋友圈。

微博微信

**国家发展改革委等部门关于加快招标投标领域**

**人工智能推广应用的实施意见**

发改法规〔2026〕195号

各省、自治区、直辖市、新疆生产建设兵团发展改革委、工业和信息化主管部门、住房城乡建设厅（委、局）、交通运输厅（局、委）、水利（水务）厅（局）、农业农村厅（局、委）、商务主管部门、国资委、招标投标指导协调部门、公共资源交易平台整合工作牵头部门，各省、自治区、直辖市通信管理局，各中央企业：

为贯彻落实党中央、国务院关于深化招标投标改革部署要求，按照《国务院关于深入实施“人工智能+”行动的意见》有关安排，推动招标投标和人工智能深度融合、促进招标投标市场规范健康发展，现提出如下意见。

**一、总体目标**

围绕招标投标交易全过程和管理重点环节，按照政府引导、多方参与、场景牵引、安全可控的原则，积极稳妥推进人工智能在招标投标领域的应用，改进招标投标范式，提升服务和监管的数智化水平，为保障公共资源公平高效配置、规范招标投标市场秩序提供有力支撑。

2026年底，招标文件检测、智能辅助评标、围串标识别等重点场景在部分省市实现全覆盖应用；2027年底，更多重点场景在全国范围内推广应用，形成一批模型训练、场景应用、机制保障等方面的经验做法，有效促进招标投标市场规范健康发展。

**二、加快推进场景应用**

**（一）“人工智能+”招标**

**1.招标策划。** 辅助招标人对行业趋势、市场供需、资源要素等进行综合研判，准确理解、分析有关项目的投资审批、招标投标、履约验收等信息，生成客观量化的招标需求、技术和商务条件，从源头提高招标的科学合理性。

**2.招标文件编制。** 在深度理解项目目标、建设内容、招标需求、技术和商务条件等基础上，结合历史交易情况和政策法规要求，智能匹配招标文件范本，推荐适合的资格条件、评标办法和评标标准，辅助招标人编制或自动生成招标文件，提升招标文件的编制质量。

**3.招标文件检测。** 结合有关政策法规要求，对招标文件开展合规性、合理性、错敏词等多维度检测，自动识别各类违法违规和排斥限制竞争等问题，提示判断依据和修改建议，辅助招标人对招标文件进行智慧纠偏。鼓励实行招标文件“先体检、再发布”。

**（二）“人工智能+”投标**

**4.投标策划。** 全方位捕捉各类项目招标信息，结合投标人特点推送适合的项目信息，自动提取并解析项目招标计划、招标公告和招标文件等资料中的关键要素，智能生成招标需求图谱，对重要内容进行提示。结合历史交易和同类项目等情况，辅助分析评估参与项目竞争的经济性，提高投标效率。

**5.投标合规自查。** 深度解析项目招标需求和招标文件要求，结合投标人的特点和优势，辅助投标人确定技术方案和报价区间。对投标人编制的投标文件，对照招标文件进行响应性比对，自动提示投标文件中的违法违规、错误缺漏等问题，辅助投标人针对性修改完善。对可能低于成本价的投标进行风险提示，减少恶意低价竞标等情况。

**（三）“人工智能+”开标和评标**

**6.开标。** 打造类人化的数字开标人，调度项目开标活动全流程，自动完成宣读开标纪律、公布投标人名单、标书解密、唱标、结果确认等工作。智能判断开标异常情况并进行提示，辅助招标人实时高效处理。

**7.专家抽取。** 综合解析项目特点和评标要点，根据评标专家的专业分类、地域分布、回避规则等条件，结合远程异地评标等要求，自动生成与项目相适应的专家抽取方案，提高所抽取专家与项目的匹配度，保障专家抽取的科学性和公正性。

**8.智能辅助评标。** 打造类人化的评审推理能力，掌握不同专业评标专家的知识结构体系，按照项目类型建立综合评审指标体系，结合具体项目推荐或匹配评审点，全面提取招标投标文件要素，深度解析招标文件内容和投标文件响应度，辅助专家开展评审或生成结果供专家参考，提升评标的公正性。

**（四）“人工智能+”定标**

**9.评标报告核验。** 打造评标报告智能审核能力，辅助招标人核查评标报告的数据准确性、逻辑关联性、内容合规性等，自动预警客观评审因素评分不一致、分值计算错误、专家打分偏离度过大等问题，提示评标专家进行复核确认并修改完善。

**10.辅助定标决策。** 基于招标需求、供应链管理、历史交易情况等，结合有关行业、信用、税务、司法等平台系统数据，对中标候选人进行多维立体画像。引入数字人答辩等方式，辅助招标人对中标候选人进行综合比对分析并作出定标决策，实现定标全过程记录和可追溯。

**11.中标合同签订。** 在招标投标文件资料中自动提取中标合同的主要签约要素，参考有关示范文本并结合项目专用合同条款生成合同，实现合同的在线签订和存档。结合政策法规要求、历史交易情况等，对中标合同的关键权利义务条款进行风险提示，减少“阴阳合同”、随意篡改等问题。

**（五）“人工智能+”现场管理**

**12.场所调度。** 对交易场所进行全方位智能化管理，高效调配场所工位资源和人员力量，动态监测交易场所中的各类人员和活动情况，提高交易设施的智能化水平，打造无人值守的智慧交易环境。加强交易场所之间的协同联动和资源互补，提升跨区域交易服务的便利化水平。

**13.见证管理。** 构建“智能研判—动态干预—链上存证”的闭环见证体系，对招标投标交易各环节进行无感化数字见证，全面、准确记录交易全过程。强化异常行为分析预警，对涉嫌违法违规活动及时提醒劝阻，加强问题线索报告，为有关部门执纪执法提供支撑。

**14.档案管理。** 构建招标投标交易档案智能化管理体系，结合智能见证管理实现交易文件的智能填报、交易数据的链上存证。对招标投标交易资料进行智能命名与归类，自动生成档案索引与摘要，提供智能检索与查询服务。充分挖掘交易档案在政策绩效评估、围串标分析、争议纠纷解决、降本增效等方面的作用，提升交易档案的综合利用效能。

**15.智慧问答。** 搭建招标投标领域专业问答引擎，针对各类政策法规、业务知识、操作流程等，提供多模态交互式咨询服务，实现操作智能引导、范本智能推荐、异常预警问答、异议投诉咨询等功能，提高招标投标交易服务的便捷性。

**（六）“人工智能+”监管**

**16.专家管理。** 构建评标专家全生命周期智能管理体系，结合专业能力、履职考核、信用评价、教育培训等情况，对评标专家进行多维立体画像并辅助开展动态考核，提升对评标专家的综合管理能力。结合具体行业实际，赋能全国评标专家“一网管理”，推动优质专家资源共享共用。

**17.围串标识别。** 构建“主体+行为”全覆盖的综合预警体系，通过多维数据碰撞和主体画像，穿透式发现企业特征信息雷同，主体关系、投标行为、中标概率异常，专家打分倾向等隐蔽性问题。对投标文件、工程量清单、报价清单等进行深度扫描，通过技术方案语义相似性分析、商务标关键报价特征比对等，挖掘疑似围串标问题线索，为有关部门执纪执法提供参考。

**18.信用管理。** 打造招标投标智慧信用管理能力，实现信用信息的客观记录、自动归集、共享应用、动态调整。打造招标投标智慧信用评价模型，多维立体勾勒主体信用画像，精准高效开展信用评价、信息推送和预警提醒。

**19.协同监管。** 打造贯通项目标前、标中、标后的分析预警模型，加强全过程数据采集、治理和运用，通过数据碰撞和比对分析，自动识别应招未招、转包违法分包、人员违规变更、进度严重滞后、低中高结等问题。加强招标投标“行刑纪”贯通衔接，实现对问题线索预警转办、协同查处、结果反馈的智能化闭环管理，增强对复杂案件的深度解析与处理能力，推动形成行政执法、刑事司法、纪检监察“一网共治”的智慧监管格局。

**20.投诉处理。** 打造招标投标智能化投诉处理能力，辅助行政监督部门分析投诉书，结合政策法规、历史案例和调查取证情况等，形成初步审查意见，分类给出处理建议，辅助生成投诉处理决定书，提升投诉处理效率。对恶意投诉进行智能筛查和处理，提高恶意投诉的防治力度。

**三、规范部署实施**

**（七）科学组织推进。** 各地要根据实践需求和技术基础，科学确定实施路径。对于提高交易效率、适合市场化推进的场景，要积极培育人工智能应用服务商。对于保障交易公平公正、提升监管质效的场景，要注重发挥政府主导作用，加强统筹规划和集约建设，地市应当在省级层面统筹指导下开展部署应用，县级及以下原则上应当复用上级的模型资源。

**（八）强化系统集成。** 各地要持续深化公共资源交易平台整合共享，在统一制度规则和技术标准的基础上有序开展集约化改造，提升招标投标交易流程和有关平台系统的标准化水平，强化有关平台系统互联互通，提高模型部署应用效率。

**（九）夯实数据基础。** 各地要加强招标投标数据治理，强化数据清洗和标注，加快构建涵盖招标投标政策法规和全流程各环节的高质量数据集和知识库，依托政务数据共享机制，推进高质量数据集的共建共享和生成数据的归集治理，更好支撑模型训练和应用。

**（十）持续迭代优化。** 各地要建立人工智能模型常态化升级机制，及时更新数据集和知识库，运用招标投标专业数据进行针对性训练，不断优化模型算法，提升模型精准度。要建立用户评价反馈机制，及时收集、处理用户需求，完善应用功能，以用户反馈驱动模型迭代优化。

**（十一）健全应用机制。** 各地要加强人工智能应用与招标投标全流程各环节的衔接，健全模型生成内容的转化应用机制，保障模型充分发挥作用。坚持技术的辅助性定位，模型生成的结论不替代招标人、招标代理机构、投标人、评标专家等的自主判断，不改变使用主体的法定责任。

**（十二）提升安全水平。** 严格落实人工智能模型安全管理要求，强化模型算法、数据资源、基础设施、应用系统等安全能力建设，严格开展算法、模型备案和安全审核。构建数据、算力、算法和系统安全防护体系，确保模型安全可靠，有效防范和应对模型黑箱、幻觉和算法歧视等风险。

**四、加强组织保障**

各省级发展改革部门要切实发挥指导协调和牵头抓总作用，加大组织实施力度，积极协调解决数据和算力需求，联合有关部门尽快确定应用场景和实施路径，分类推动落实，健全应用保障机制；要加强与高校、科研院所、人工智能企业合作，充分发挥人工智能企业的作用，促进产学研转化；要强化人才队伍建设，加强跨领域人才培养。国家发展改革委将会同有关部门加强统筹协调，做好宣传引导和风险管控，指导各地、各中央企业因地制宜深化探索应用，完善配套制度规则，推进标准体系建设，及时总结推广典型经验做法。

国家发展改革委

工业和信息化部

住房城乡建设部

交 通 运 输 部

水  利  部

农 业 农 村 部

商  务  部

国务院国资委

2026年2月6日

附件：

相关政策与解读

- [国家发展改革委新闻发言人就《国家发展改革委等部门关于加快招标投标领域人工智能推广应用的实施意见》答记者问](https://www.ndrc.gov.cn/xxgk/jd/jd/202602/t20260210_1403683.html)

排行榜

- _01_

## [2026年6月18日国内成品油价格调整](http://www.ndrc.gov.cn/xwdt/xwfb/202606/t20260618_1405957_ext.html "2026年6月18日国内成品油价格调整")

2026-06-18

- _02_

## [2026年6月18日国内成品油价格调整](http://www.ndrc.gov.cn/xwdt/xwfb/202606/t20260618_1405957.html "2026年6月18日国内成品油价格调整")

2026-06-18

- _03_

## [关于开展重点行业节能降碳改造攻坚三年行动的通知(发改环资〔2026〕698号)](http://www.ndrc.gov.cn/xxgk/zcfb/tz/202606/t20260615_1405852.html "关于开展重点行业节能降碳改造攻坚三年行动的通知(发改环资〔2026〕698号)")

2026-06-15

- _04_

## [国家发展改革委举行6月份新闻发布会](http://www.ndrc.gov.cn/xwdt/xwfb/202606/t20260618_1405995.html "国家发展改革委举行6月份新闻发布会")

2026-06-18

- _05_

## [“十五五”规划里的新质生产力](http://www.ndrc.gov.cn/wsdwhfz/202604/t20260413_1404628_ext.html "“十五五”规划里的新质生产力")

2026-04-13

- [政务咨询](https://services.ndrc.gov.cn/ecdomain/portal/portlets/bjweb/newpage/myhall/zixunList.jsp)
- [网上信访](http://xf.ndrc.gov.cn/2019/index.jsp)
- [信息公开](http://zfxxgk.ndrc.gov.cn/web/apply.jsp)

### 来源 6: CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统

- URL: https://patents.google.com/patent/CN119624385A/zh
- 精读方法：firecrawl-scrape

Full documents
Title
Abstract
Claims
All
Any
Exact
NotAdd AND condition

These CPCs and their children

These exact CPCs
Add AND condition

Exact
Exact Batch
Similar
Substructure
Substructure (SMARTS)
Full documents
Claims onlyAdd AND conditionAdd AND condition

Application Numbers
Publication Numbers
EitherAdd AND condition

# 一种基于人工智能的招标文件自动审核方法及系统

### Abstract     translated from

本发明公开了一种基于人工智能的招标文件自动审核方法及系统，在系统中设置在线数据库和本地数据库，通过招标文件审核模块对投标文件进行格式审核、合规审核和其他异常审核后，生成审核意见，经系统使用单位对对审核意见进行人工确认后，生成招标文件定稿，系统包括以下模块：数据库模块、文件上传模块、招标文件审核模块、修改建议模块、招标文件生成模块、用户交互界面、学习模块。本发明使用方便，通过人工智能技术实现对招标文件的智能审核，提高了招标文件的整体质量和效率。

### Classifications     machine-classified       cpc-machine-classified       fterm-machine-classified           fterm-family-classified

The classifications are assigned by a computer and are not a legal conclusion.

Google has not performed a legal analysis and makes no representation as to the
accuracy of the classifications listed.

The CPC classifications are assigned by a computer and are not a legal conclusion.

Google has not performed a legal analysis and makes no representation as to the
accuracy of the classifications listed.

The F-term classifications are assigned based on a patent family member containing
these classification codes.

The F-term classifications are assigned by a computer and are not a legal conclusion.

Google has not performed a legal analysis and makes no representation as to the
accuracy of the classifications listed.

[G](https://patents.google.com/patent/CN119624385A/zh#)PHYSICS

[G06](https://patents.google.com/patent/CN119624385A/zh#)COMPUTING OR CALCULATING; COUNTING

[G06Q](https://patents.google.com/patent/CN119624385A/zh#)INFORMATION AND COMMUNICATION TECHNOLOGY \[ICT\] SPECIALLY ADAPTED FOR ADMINISTRATIVE, COMMERCIAL, FINANCIAL, MANAGERIAL OR SUPERVISORY PURPOSES; SYSTEMS OR METHODS SPECIALLY ADAPTED FOR ADMINISTRATIVE, COMMERCIAL, FINANCIAL, MANAGERIAL OR SUPERVISORY PURPOSES, NOT OTHERWISE PROVIDED FOR

[G06Q10/00](https://patents.google.com/patent/CN119624385A/zh#)Administration; Management

[G06Q10/10](https://patents.google.com/patent/CN119624385A/zh#)Office automation; Time management

[G](https://patents.google.com/patent/CN119624385A/zh#)PHYSICS

[G06](https://patents.google.com/patent/CN119624385A/zh#)COMPUTING OR CALCULATING; COUNTING

[G06F](https://patents.google.com/patent/CN119624385A/zh#)ELECTRIC DIGITAL DATA PROCESSING

[G06F16/00](https://patents.google.com/patent/CN119624385A/zh#)Information retrieval; Database structures therefor; File system structures therefor

[G06F16/20](https://patents.google.com/patent/CN119624385A/zh#)Information retrieval; Database structures therefor; File system structures therefor of structured data, e.g. relational data

[G06F16/21](https://patents.google.com/patent/CN119624385A/zh#)Design, administration or maintenance of databases

[G](https://patents.google.com/patent/CN119624385A/zh#)PHYSICS

[G06](https://patents.google.com/patent/CN119624385A/zh#)COMPUTING OR CALCULATING; COUNTING

[G06F](https://patents.google.com/patent/CN119624385A/zh#)ELECTRIC DIGITAL DATA PROCESSING

[G06F16/00](https://patents.google.com/patent/CN119624385A/zh#)Information retrieval; Database structures therefor; File system structures therefor

[G06F16/20](https://patents.google.com/patent/CN119624385A/zh#)Information retrieval; Database structures therefor; File system structures therefor of structured data, e.g. relational data

[G06F16/22](https://patents.google.com/patent/CN119624385A/zh#)Indexing; Data structures therefor; Storage structures

[G](https://patents.google.com/patent/CN119624385A/zh#)PHYSICS

[G06](https://patents.google.com/patent/CN119624385A/zh#)COMPUTING OR CALCULATING; COUNTING

[G06F](https://patents.google.com/patent/CN119624385A/zh#)ELECTRIC DIGITAL DATA PROCESSING

[G06F40/00](https://patents.google.com/patent/CN119624385A/zh#)Handling natural language data

[G06F40/10](https://patents.google.com/patent/CN119624385A/zh#)Text processing

[G06F40/166](https://patents.google.com/patent/CN119624385A/zh#)Editing, e.g. inserting or deleting

[G06F40/186](https://patents.google.com/patent/CN119624385A/zh#)Templates

[G](https://patents.google.com/patent/CN119624385A/zh#)PHYSICS

[G06](https://patents.google.com/patent/CN119624385A/zh#)COMPUTING OR CALCULATING; COUNTING

[G06N](https://patents.google.com/patent/CN119624385A/zh#)COMPUTING ARRANGEMENTS BASED ON SPECIFIC COMPUTATIONAL MODELS

[G06N20/00](https://patents.google.com/patent/CN119624385A/zh#)Machine learning

[G](https://patents.google.com/patent/CN119624385A/zh#)PHYSICS

[G06](https://patents.google.com/patent/CN119624385A/zh#)COMPUTING OR CALCULATING; COUNTING

[G06Q](https://patents.google.com/patent/CN119624385A/zh#)INFORMATION AND COMMUNICATION TECHNOLOGY \[ICT\] SPECIALLY ADAPTED FOR ADMINISTRATIVE, COMMERCIAL, FINANCIAL, MANAGERIAL OR SUPERVISORY PURPOSES; SYSTEMS OR METHODS SPECIALLY ADAPTED FOR ADMINISTRATIVE, COMMERCIAL, FINANCIAL, MANAGERIAL OR SUPERVISORY PURPOSES, NOT OTHERWISE PROVIDED FOR

[G06Q30/00](https://patents.google.com/patent/CN119624385A/zh#)Commerce

[G06Q30/06](https://patents.google.com/patent/CN119624385A/zh#)Buying, selling or leasing transactions

[G06Q30/08](https://patents.google.com/patent/CN119624385A/zh#)Auctions

View 5 more classifications

Hide more classifications

### Landscapes

[Engineering & Computer Science](https://patents.google.com/patent/CN119624385A/zh#)[Theoretical Computer Science](https://patents.google.com/patent/CN119624385A/zh#)

* * *

Show more

Show less

Other languages[English](https://patents.google.com/patent/CN119624385A/zh#)Inventor[王龙](https://patents.google.com/patent/CN119624385A/zh#)[张应斋](https://patents.google.com/patent/CN119624385A/zh#)[张志华](https://patents.google.com/patent/CN119624385A/zh#)Current Assignee

The listed assignees may be inaccurate.

Google has not performed a legal analysis and makes no representation or
warranty as to the accuracy of the list.

Guizhou Shanfeng Engineering Consulting Co ltd

* * *

2024[CN](https://patents.google.com/patent/CN119624385A/zh#)

Application number: CN202411777926.1A

Filing date: 2024-12-05

Legal status: Pending

* * *

2024-12-05

[Application filed by Guizhou Shanfeng Engineering Consulting Co ltd](https://patents.google.com/patent/CN119624385A/zh#)

2024-12-05

[Priority to CN202411777926.1A](https://patents.google.com/patent/CN119624385A/zh#)

2025-03-14

[Publication of CN119624385A](https://patents.google.com/patent/CN119624385A/zh#)

Status

Pending

* * *

Info[Cited by (7)](https://patents.google.com/patent/CN119624385A/zh#citedBy)[Legal events](https://patents.google.com/patent/CN119624385A/zh#legalEvents)[Similar documents](https://patents.google.com/patent/CN119624385A/zh#similarDocuments)[Priority and Related Applications](https://patents.google.com/patent/CN119624385A/zh#relatedApplications)External links[Espacenet](https://worldwide.espacenet.com/publicationDetails/biblio?CC=CN&NR=119624385A&KC=A&FT=D)[Global Dossier](https://globaldossier.uspto.gov/result/application/CN/202411777926/1)[Discuss](https://patents.stackexchange.com/questions/tagged/CN119624385A)

### Description     translated from

一种基于人工智能的招标文件自动审核方法及系统

技术领域

本发明属于办公自动化技术领域，具体涉及一种基于人工智能的招标文件自动审核方法及系统。

背景技术

目前，招标采购已经作为一种特殊的采购方式，已经广泛应用于各行业、各领域的各类项目。在这种交易方式下，通常是由项目采购(包括货物的购买、工程的发包和服务的采购)的采购方作为招标方，通过发布招标文件等方式发出招标采购的信息，提出所需采购项目的性质及其数量、质量、技术要求，交货期、竣工期或提供服务的时间。经招标方对各投标者的报价及其他条件进行审查比较后，从中择优选定中标者，并与其签订采购合同。具体地，一般由采购方提供招标需求给第三方招标代理机构，由第三方招标代理机构派专业人员根据采购方提供招标需求人工编写招标文件，在编写完成后，对该招标文件进行发布和公告，通知潜在投标人前来投标，以从中择优选定中标者，并与其签订采购合同。

但是，2017年国家取消招标代理资质后，大量良莠不齐的招标代理机构如同雨后春笋般出现，许多招标代理机构存在实力不强、经验不够、人力配备弱、对法律法规理解不到位等情形，其招标文件质量低、水平差，且人工编写招标文件的方式编写效率低，如何提高招标文件的编写质量和编写效率，成为亟须解决的问题，因此，发明一种基于人工智能，使用简单、高效、高质量且能不断自主学习的招标文件自动审核方法和系统具有重要意义。

发明内容

本发明要解决的技术问题是：提供一种基于人工智能的招标文件自动审核方法及系统，通过人工智能自主学习，实现对招标文件编写质量和效率的提升。

本发明的目的是通过以下技术方案实现的：

一种基于人工智能的招标文件自动审核方法，包括以下步骤：

步骤1：在系统中设置在线数据库，通过互联网自动不定期查找并下载招标相关规定和招标文件模板，并对其标记关键词，该在线数据库由系统使用单位共享使用；

步骤2：在系统中设置本地数据库，由系统使用单位人工手动录入其特定行业的招标相关规定和项目招标文件模板，并对其标记关键词，该本地数据库在系统使用单位同意后可以与系统所有使用单位共享使用；

步骤3：系统使用单位上传需要审核的招标文件初稿，招标文件审核模块对其进行格式审核、合规审核和其他异常审核后，生成审核意见；所述审核意见包括审核出的问题和针对各个问题的具体修改意见及其理由；

步骤4：根据步骤3所述审核意见，由系统使用单位对审核意见进行人工确认后，生成招标文件定稿，所述人工确认可以是选择接受审核意见进行修改，可以是拒绝审核意见不予修改，也可以是根据审核意见进行调整或部分采纳等修改操作。

进一步地，还可以包括步骤5：将步骤4中生成的招标文件定稿自动录入本地数据库，并记录步骤4中系统使用单位对审核意见进行人工确认的结果，通过不断记录该使用单位人工确认的结果，训练机器学习该使用单位编制招标文件的风格，通过学习模型，优化步骤3中提出的审核意见。

进一步地，步骤1中所述招标相关规定包括招标领域的国家法律、法规、规章、规范性文件、国家标准、行业标准等相关规定，所述招标文件模板为国家或地方发布的标准招标文件或招标文件示范文本，各行业、各地域、各类型的项目招标文件；并且，步骤1中所述的标记关键词包括招标相关规定标题、生效日期、失效日期、发布单位、发布日期、文件类别、文件版本、招标文件性质、适用区域、地域排他性、适用行业、应用场景、项目类型、招标阶段、适用范围、合同类型、法律层级、法的优先层级、适用优先性、合规性要求、关键条款、处罚措施、适用主体、文件适用条件、附加条款、实施细则等多个关键词。

进一步地，步骤2中的所述的特定行业的招标相关规定包括招标领域的国家法律、法规、规章、规范性文件、国家标准、行业标准等相关规定，所述项目招标文件模板包括国家或地方发布的标准招标文件或招标文件示范文本，各行业、各地域、各类型的项目招标文件；并且，步骤2中所述的标记关键词包括招标相关规定标题、生效日期、失效日期、发布单位、发布日期、文件类别、文件版本、招标文件性质、适用区域、地域排他性、适用行业、应用场景、项目类型、招标阶段、适用范围、合同类型、法律层级、法的优先层级、适用优先性、合规性要求、关键条款、处罚措施、适用主体、文件适用条件、附加条款、实施细则等多个关键词。

进一步地，步骤3中所述合规审核和其他异常审核，通过检索、对比、调取在线数据库及本地数据库数据进行审查。

其中，对招标文件提出审核意见包括：①是否存在违反招标相关规定的情况；②同时横向对比本地数据库中过往项目招标文件，对异常招标文件进行提示；③是否存在前后矛盾、合同条款漏洞、管理模式缺陷等；

其中，对异常招标文件具体是指：

1.内容不完整或缺失，主要为条款缺失(招标文件中缺少法律法规、行业标准或惯例中必须具备的关键条款，如保密条款、合同履约条款、验收标准等)、信息不全(文件中未包含项目基本信息，如项目名称、预算金额和资金来源，或未按要求详细说明招标内容)和附件缺失(未附上招标文件所需的附件，如图纸、技术参数和投标须知，或者附录文件不全)。

2.条款或条件设定不合理，主要为门槛条件过高或过低(投标人资质、业绩等要求设置过高或过低，明显不符合行业惯例或法规规定，可能存在倾向性或排他性)、技术参数过于具体(技术规格或产品要求过于细化，可能限制潜在投标人，涉嫌为特定厂商量身定制，违背公开、公平、公正原则)和评分标准不合理(评分细则缺乏客观性，可能对部分投标人不利，或评分项设置不均衡，如价格权重过高或过低)。

3.时间节点异常，主要为公告时间不足(未按照法规要求预留足够的公告期或投标准备期，如法律规定的20天公告期)和招标时间安排冲突(开标时间、截止时间、澄清时间等安排不符合合理流程或与其他招标文件的时间节点冲突)。

4.招标金额与预算异常，主要为预算不合理(项目预算与市场价相比过高或过低，尤其在设备采购、工程造价等方面，可能存在报价异常)和资金来源不明(未明确资金来源或资金来源不符合要求，可能影响项目的资金保障和履约安全)。

5.法律和合规性问题，主要为引用过期法规(文件中引用的法律条款或标准已经过期或失效，可能导致后续合同条款无法执行)、不符合新法规(未及时更新到现行有效的法规要求，或者未包含最新的合规条款)和优先级冲突(引用的法律条款之间存在优先级冲突，如地方性法规与法律冲突)。

6.历史数据异常，主要为与过往项目数据不一致(文件内容在类似项目中存在显著不同，如工程量清单、技术参数、投标人资质要求等设置差异大，可能暗示设置偏向或不公平)和合同条件有显著差异(合同条款在相似项目中变动较大，如履约保证金、违约责任等，需要判断是否有偏向性或特殊倾向)。

7.价格与成本异常，主要为报价异常偏低或偏高(系统对比类似项目的报价水平，若价格显著偏离市场水平，可能存在恶性竞争或利益输送嫌疑)和投标上限或下限设置异常(设置的最高限价或最低限价不合理，可能导致竞争性降低，或有利于特定投标人)。

8.招标程序违规，主要为招标方式不合规(未按照规定选择合适的招标方式，违规选择单一来源采购等方式)、资格预审不当(资格预审过程不透明，或存在剔除合格投标人的情况)和招标文件发布途径不规范(未通过规定的公告平台发布招标文件，可能影响公开性和透明性)。

9.关联方或利益冲突问题，主要为潜在利益冲突(文件中有可能涉及利益相关方，可能导致不公平竞争，如投标人关联方或利益相关方的参与)和未披露关联关系(若投标人与招标人或评标方存在关联关系未披露，则可能违反公正性要求)。

10.历史项目问题复现，主要为重复出现历史异常(系统发现与历史项目中的异常内容重复，如设置相同不合理的条款，暗示可能存在系统性问题)和质量和履约问题复现(过往项目中曾发生的质量问题或履约问题未在招标文件中被提及或规避，未针对历史问题优化合同条款)。

上述异常有助于系统在文件审核过程中针对性地识别潜在问题，提高招标流程的规范性和透明度。

一种基于人工智能的招标文件自动审核系统，包括以下模块：

模块1：数据库模块，储存招标相关规定和招标文件，并对其设置关键词，便于招标文件审核模块进行匹配、对比。

模块2：文件上传模块，对系统使用单位编制完成的招标文件初稿，经授权后上传至招标文件审核模块；将经系统使用单位确定定稿后的招标文件上传本地数据库。

模块3：招标文件审核模块，对系统使用单位上传的招标文件初稿进行格式审核、合规审核和其他异常审核。

模块4：修改建议模块，对经招标文件审核模块审核后的招标文件生成审核意见，所述审核意见包括审核出的问题和针对各个问题的具体修改意见及其理由。

模块5：招标文件生成模块，根据系统使用单位对具体修改建议的处理结果(如接受、不接受、调整或部分采纳)，自动生成最终版招标文件。

模块6：用户交互界面，方便系统使用单位操作本系统。

模块7：学习模块，也是使用者风格记录模块，自动对比系统提出的审核意见与定稿的最终版招标文件，对于系统提出了意见但系统使用单位没有接受的进行记录，当记录同一情况次数大于系统使用单位设置的阈值时，系统将对该系统使用单位自动屏蔽该类审核意见，避免重复提醒，减少不必要的工作量；记录系统使用单位对审核意见进行人工确认的结果，并利用这些反馈数据训练机器学习模型，逐步提高招标文件审核模块输出的准确性和效率。

进一步地，所述模块1数据库模块包括在线数据库和本地数据库，所述在线数据库，通过互联网自动不定期查找并下载招标相关规定和招标文件模板；所述本地数据库，由系统使用单位人工手动录入其特定行业的招标相关规定和项目招标文件模板。

本发明的有益效果是：与现有技术相比，本发明基于人工智能建立在线数据库和本地数据库，将招标相关规定和招标文件各类模板提前存储，通过招标文件审核模块进行格式审核、合规审核和其他异常审核后，对投标文件生成审查意见。由系统使用单位人工确认后自动生成招标文件定稿，同时，本发明还设有使用者风格记录模块，对系统使用单位的修改习惯进行记录，自动筛选屏蔽，使用方便，通过人工智能技术实现对招标文件的智能审核，提高了招标文件的整体质量和效率。

附图说明

图1是本发明的工作流程及示意图。

具体实施方式

为了更好地理解上述技术方案，下面将结合说明书附图及具体实施方式对上述技术方案进行详细说明。

参考图1，本实施例采用了一种基于人工智能的招标文件自动审核方法，包括以下步骤：

步骤1：在系统中设置在线数据库，通过互联网自动不定期查找并下载招标相关规定和招标文件模板，并对其标记招标相关规定标题、生效日期、失效日期、发布单位、发布日期、文件类别、文件版本、招标文件性质、适用区域、地域排他性、适用行业、应用场景、项目类型、招标阶段、适用范围、合同类型、法律层级、法的优先层级、适用优先性、合规性要求、关键条款、处罚措施、适用主体、文件适用条件、附加条款、实施细则等多个关键词，如适用行业可分为公路行业、铁路行业、房建行业、市政行业、能源等，适用区域可分为贵州省、云南省、重庆市等，项目类型可分为施工、勘察、设计、监理、设备物资、检测、报建等，该在线数据库由系统使用单位共享使用。

其中，步骤1中所述招标相关规定包括招标领域的国家国家法律、法规、规章、规范性文件、国家标准、行业标准等相关规定。所述招标文件模板为国家或地方发布的标准招标文件或招标文件示范文本，各行业、各地域、各类型的项目招标文件。

其中，所述在线数据库可采用分布式数据库系统，能够容纳大量数据并确保数据安全。为了使数据库的设计支持高效查询，便于快速检索，清洗处理过后的法律法规等数据将导入到Elasticsearch中，以提高搜索效率和准确性；另外使用PostgreSQL存储法律法规的结构化数据，包括元数据、关键字，在给有错误的招标文件中标注生成对应的审核意见时可以准确获取相应的法律法规。

互联网自动不定期查找并下载，为利用网络爬虫技术，从政府官方网站和其他合法渠道自动获取最新的招标相关规定和招标文件范本，对获取的数据进行清洗、去重和标准化处理，并通过自然语言处理(NLP)技术提取关键信息，如法的生效时间和失效时间、行业、地域、类型等，并对这些信息进行标记。在线数据库通过设定的周期自动更新，该周期可自由设置，以每周或每月更新一次较优，以确保数据的时效性。

步骤2：在系统中设置本地数据库，由系统使用单位人工手动录入招标相关规定和项目招标文件模板，并对其标记招标相关规定标题、生效日期、失效日期、发布单位、发布日期、文件类别、文件版本、招标文件性质、适用区域、地域排他性、适用行业、应用场景、项目类型、招标阶段、适用范围、合同类型、法律层级、法的优先层级、适用优先性、合规性要求、关键条款、处罚措施、适用主体、文件适用条件、附加条款、实施细则等多个关键词，如适用行业可分为公路行业、铁路行业、房建行业、市政行业、能源等，适用区域可分为贵州省、云南省、重庆市等，项目类型可分为施工、勘察、设计、监理、设备物资、检测、报建等，该本地数据库在使用单位同意后可以与系统所有使用单位共享使用。

其中，步骤2中的所述的特定行业的招标相关规定包括招标领域的国家法律、法规、规章、规范性文件、国家标准、行业标准等相关规定，所述项目招标文件模板包括国家或地方发布的标准招标文件或招标文件示范文本，各行业、各地域、各类型的项目招标文件。

其中，所述本地数据库采用易于管理的关系型数据库PostgreSQL，支持系统使用单位根据自身需求进行数据上传，具体操作为系统使用单位可以通过图形用户界面(GUI)上传特定行业的招标相关规定和项目招标文件，并手动添加或确认系统自动标记的标签。同时，支持对系统使用单位上传的数据进行分类、排序和搜索，确保数据的准确性和易用性。

步骤3：系统使用单位上传需要审核的招标文件初稿后，招标文件审核模块对其进行格式审核、合规审核和其他异常审核后，生成审核意见，所述审核意见包括审核出的问题和针对各个问题的具体修改意见及其理由。

其中，系统使用单位是通过系统上的图形用户界面(GUI)上传需要审核的招标文件初稿。

其中，格式审核为利用Apache POI读取上传的文件的格式并格式化处理，从文件中提取样式信息，包括字体、字号、颜色、对齐方式等。所述格式审核流程为检查文件的整体结构和布局是否符合要求，定义一套规则来规范文件的样式和格式，使用算法来匹配文件的样式和格式与预定义的规则。具体格式审核如下：

文件格式解析：使用Apache POI读取文件的类型和版本(如DOC、DOCX、XLSX)，确保文件格式与审核标准匹配。如果不符合要求(例如不支持的文件类型)，则提示错误。

页面结构检查：解析文档的页数、分段、分栏等布局结构。确认文件的基础页面结构是否符合要求，例如页面分栏或分段设置是否正确。

表格、图片和其他对象：检查文件中是否包含表格、图片、图表等对象，并记录其位置和数量，确保不超过或少于预期数量。

读取字体和字号信息：遍历文档中的每一段或每个段落中的文本部分，使用Apache POI读取文本的字体类型、字号大小、加粗、斜体等样式信息。

主标题和副标题：根据规定，验证文件中各级标题的字体和字号是否符合要求。例如，一级标题应为加粗宋体16号，二级标题应为加粗宋体14号等。

正文字体和字号：检查正文的字体类型、字号，确保正文部分遵循规范(如宋体12号，不允许使用彩色或加粗等不规范样式)。

颜色规范检查：读取并解析文本颜色、背景颜色、表格线条颜色等信息，确保颜色符合规定。例如，所有文本颜色应为黑色或其他特定要求的颜色，背景应为白色。

文本对齐方式：检查文档中每一段落的对齐方式(如左对齐、居中、右对齐或两端对齐)，确保特定内容(如标题、表格标题)符合对齐要求。例如，所有正文段落应为两端对齐，标题为居中对齐。

段落间距检查：检查段落的上、下间距，确保段落间距符合规范。例如，正文段落要求上、下各空一行，标题与正文之间应有适当间距。

行距检查：验证每段的行距是否符合要求，例如正文要求单倍行距，标题可以设置为1.5倍行距。

页面边距检查：检查页面四周边距设置，确保边距在规定的范围内。例如，左右边距设置为3厘米，顶部和底部边距为2厘米。

纸张尺寸检查：确保文档的纸张尺寸符合标准(如A4尺寸21x29.7厘米)，并检查页面方向(纵向或横向)是否符合要求。

表格边框和样式检查：遍历文档中的表格，读取表格边框、单元格颜色、字体大小等信息，确保表格样式规范。例如，所有表格应设置边框线为0.5磅，字体应为宋体10号。

图片分辨率与位置检查：读取并检查图片的分辨率、大小、位置和环绕方式，确保图片符合规范(如分辨率不低于300DPI，居中对齐)。

标题层级检查：读取并解析标题的层级关系，确保标题使用正确的格式。例如，标题层级应按规范依次递减，且标题层级编号(如1.1,1.2,2.1等)符合结构要求。

自动编号检查：确保文件中的编号是通过自动编号生成的，而不是手动输入的，避免后续的编号混乱问题。

识别和记录错误项：记录文件中不符合规则的格式项，包括具体位置、问题描述和建议的格式要求。

自动生成审核报告：根据检测结果生成详细的格式检查报告，列出所有不符合规定的格式项，提供修正建议，并附带超链接，便于用户快速定位到具体问题位置。

格式异常捕捉：如果文档存在不支持的格式或样式(如复杂样式、脚注、批注等)，在报告中记录异常，或提示无法识别的格式项。

容错机制：允许一定范围内的格式偏差，设置格式容差(如字号允许偏差±1号)，确保审核结果的合理性。

以上步骤可帮助系统逐步实现招标文件格式的全面检查，并确保文件格式符合预定义的规范要求。

其中，步骤3中所述合规审查和其他异常审查，通过检索、对比、调取在线数据库及本地数据库数据进行审查。具体步骤为：

1、数据源连接与数据同步

与在线数据库连接：与在线数据库建立实时或定期同步机制，确保数据的实时性。可以使用API接口或数据交换协议(如RESTful API、SOAP、GraphQL)实现数据连接。

与本地数据库同步：定期从在线数据库更新本地数据，同时设置数据更新标记，确保本地数据库在离线或网络不稳定的情况下也能有效运行。

数据镜像备份：对关键数据建立镜像或备份，以便在数据库更新或故障时仍然可以读取和调用。

2、多关键词检索功能

关键词索引：对在线数据库和本地数据库内容建立全文索引和关键词索引(使用倒排索引或哈希索引)，便于快速查询。如基于生效时间、失效时间、适用地域、行业、优先层级等关键词。

模糊匹配和分词检索：采用分词技术(如基于中文的jieba分词或基于NLP的分词工具)和模糊匹配，以便应对多种表达方式和非标准化字段(如“适用于建筑工程”可匹配“建设工程”)。

组合检索：允许基于多关键词的组合查询，如同时筛选生效时间、地域、行业等复合条件，确保检索结果的精确度。

3、数据比对与差异识别

文本对比算法：使用自然语言处理(NLP)算法对招标文件的文本内容与法规标准库中的文本内容进行语义比对，识别关键条款是否符合当前有效的法律条款。

多版本对比：对于有多个版本的标准文件或法规，建立历史版本数据库，使用版本控制技术或多版本比对工具，识别不同版本间的差异，避免旧版内容影响审核结果。

合规性规则库：建立合规性规则库，将法规和标准的关键条款和要求提取成规则，通过规则匹配技术比对文件的合规性，检测是否符合合法合规的要求。

4、数据调用与审查机制

实时数据调用：在审核过程中自动调用最新的法规和标准数据，对比分析招标文件中的条款内容，确保法规内容的最新性。

异常标记与报告生成：对不合规或存在疑问的条款自动标记，并生成详细的异常报告，包括不合规条款的具体内容、法律依据及相应条款内容。

历史数据调用：当法规的适用性涉及历史条款或失效条款时，系统能够调用历史法规数据进行对比，并标明文件中引用的条款是否已过期。

5、智能审查模型的应用

机器学习和规则引擎：构建结合机器学习和规则引擎的智能审查模型。基于招标文件中的内容，自动提取关键条款和字段，然后与法规数据库中的标准内容进行比对。

自然语言理解(NLU)：使用自然语言理解技术对招标文件的语言进行解析，识别出条款背后的语义，并与法规条款的语义进行匹配。

知识图谱辅助审查：构建招标法规知识图谱，将法规的关联性和层级结构可视化，帮助识别不同法规条款间的适用关系和优先关系，提高审核效率。

6、用户反馈和自学习

人工复核与反馈机制：在自动审核结果生成后，可以加入人工复核和反馈机制，以便对模型审查结果的准确性进行验证。

模型自学习：将反馈信息加入模型的自学习模块中，不断优化检索、比对和调用规则，以提升系统的准确度和审核效率。

其中，合规审核为通过NLP技术自动提取招标文件初稿中关键信息(包括项目名称、项目编号、项目预算、资金来源、资质要求、过往业绩、财务状况、人员要求、技术规范、质量标准、验收标准、环境标准、合同期限、履约保证金、支付条款、违约条款、风险分担、招标方式、公告期、投标截止时间、开标流程、评标流程、评分标准、价格评分权重、技术评分细则、加分项、法定合规条款、政策符合性、安全规定、劳动保障、生效日期、失效日期、更新要求、知识产权归属、保密义务、风险应对措施、不可抗力条款、环保合规、安全生产要求、技术认证等关键信息)，并与在线数据库及本地数据库中的数据进行比对，检查是否存在违反招标相关规定的条款。具体步骤如下：

1.数据规范化与预处理

文本规范化：将提取的关键信息和数据库中的参考数据标准化，消除格式和表述差异。包括统一字体、大小写、数字格式等。

同义词处理：为不同表述的同一项内容(如“履约保证金”和“履约押金”)建立同义词词典，方便后续准确比对。

2.逐项比对的逻辑设计

项目基本信息比对：项目名称、编号、预算、资金来源等信息，直接与数据库中对应项目的备案信息进行精确匹配。确保项目的基本信息与批准或备案信息一致。

资质和要求比对：将资质要求、过往业绩、财务状况等内容与法规、行业标准中的合规要求比对，验证是否存在不合理的门槛条件或排他性条款。对于资质等限制性条款，可参照过往类似项目的资质要求进行合理性校验。

技术和质量要求比对：技术规范、质量标准、验收标准等信息与数据库中的行业标准比对，确保未设置不合理的技术要求。如数据库中的行业标准规定特定设备的标准为“XX参数”，则检查文件中是否使用了符合该参数的条款。

3.合同和履约条件比对

期限和金额比对：将合同期限、履约保证金等条件与类似项目的数据或法规中的规定范围进行比对。例如，履约保证金金额应控制在项目总金额的合理百分比范围内，超出此范围则判定为异常。

支付条款和违约条款比对：比对支付条款、违约条款是否符合合同法及行业规范，确保支付安排和违约处理符合相关法律的通用标准。

风险分担和不可抗力条款比对：检查文件中的风险条款和不可抗力条款，确保符合数据库中的法律标准。可比对过往项目中的类似条款，查看是否存在偏离。

4.流程和期限比对

招标方式和公告期比对：将招标方式、公告期限等内容与法规规定比对，确保公告期不低于法律要求的最短时限。对于特定项目类型(如公开招标)，公告期应达到法定标准。

截止时间和流程比对：检查投标截止时间和开标流程是否符合流程规范。确保开标时间符合公平性和公开性的要求，如不允许提前开标或设置非公开的评标流程。

5.评分标准和评标细则比对

评分权重比对：将评分标准中的价格权重、技术评分细则与标准数据库比对，确保权重设置在合理范围内。例如价格权重通常在30％-60％之间，超出此范围则提示异常。

加分项合理性比对：将评分中的加分项与法律、政策规定比对，确保加分项不偏向特定投标人，符合公平竞争要求。

6.合规与政策要求比对

法定合规条款比对：逐条比对文件中的法定合规条款(如公平竞争声明、保密要求)是否齐全，参考数据库中的标准合同条款，确保所有必备条款均完整。

政策符合性比对：检查文件是否符合最新政策，如地方采购优惠、环保要求等，并与政策数据库中内容进行逐条比对，确保符合最新的政策导向。

7.生效与失效日期比对

生效和失效日期比对：将文件中的生效日期、失效日期与项目审批时间及行业规范的要求比对，确保时间范围符合法规要求。如法规要求合同签订后必须在半年内完成项目，若文件规定超过半年，则提示异常。

8.知识产权、保密义务和风险管理条款比对

知识产权归属条款比对：检查文件中是否明确知识产权归属，与数据库中的标准条款比对，确保知识产权归属清晰。

保密义务比对：比对保密义务条款的设置是否符合标准，确保未泄露招标敏感信息。

风险条款比对：将风险应对措施和不可抗力条款与标准条款进行比对，确保符合行业规范。若存在漏项或条款描述不清，提示修订建议。

9.行业特殊要求比对

环保、安全要求比对：对环保、安全生产等特殊要求条款进行比对，确保文件中所述环保、节能等条款符合国家和地方的环保、安全政策。

技术认证比对：对涉及特定产品的技术认证要求，与数据库中类似项目的认证需求比对，确保符合行业认证要求。

10.异常记录与提示

异常条款标记：对比过程中，记录每一项比对的异常结果，并在最终的比对报告中提示异常条款。

生成详细比对报告：生成文件与数据库比对结果的审核报告，列出异常信息及修正建议，帮助招标文件编制人员进行修改。

其中，其他异常审核利用机器学习算法，进一步对招标文件进行深度分析，包括对比在线及本地数据库中其他项目招标文件，检查是否存在异常、前后矛盾、合同条款漏洞、管理模式缺陷等问题。具体步骤如下：

1.文本分析与比对

自然语言处理(NLP)：使用NLP技术对招标文件进行结构化分析，提取出关键合同条款、条件、术语，并识别关键信息。常用的方法包括：

关键词提取：提取出关键合同条款、金额、期限等信息。

语义分析：使用分词、词性标注和句法分析等手段，识别各条款的语义，判断条款之间的逻辑关系。

前后矛盾检测：通过自动化比对不同条款的内容和表达，检测前后是否存在逻辑或表述上的矛盾。例如，条款中定义的时间、金额是否与其他条款一致。

文本相似度分析：使用余弦相似度或句向量等方法，判断不同部分内容是否相似，检查是否有内容冗余或重复定义的情况。

2.逻辑规则与条件检查

基于规则的逻辑检查：编写规则引擎，定义招标文件的逻辑关系和条件规则。例如，“付款条款”应与“交付条款”相对应，不应出现矛盾的描述。

自动化条件验证：通过条件规则自动验证文件内部的一致性。例如，合同中的付款比例与项目进度的关系是否合理，是否符合一般的工程建设规律。

3.异常与漏洞检测

漏洞识别模型：基于历史合同或招标文件的常见问题和漏洞，训练机器学习模型检测文件中的异常。可以利用过去的合同问题样本构建分类或异常检测模型，从而识别潜在的漏洞。

规则库与合规性校验：建立基于行业标准或法规的规则库，自动检测文件是否符合这些标准或法规。例如，对采购流程、合同条款中的保密条款、知识产权条款等进行合规性校验。

4.管理模式缺陷分析

管理模式数据挖掘：通过分析项目管理方法和合同中的管理模式，识别潜在的缺陷。例如，项目实施的分工是否合理，是否有明确的职责划分，管理流程是否清晰。

流程分析和模拟：使用流程挖掘和流程模拟技术，对合同条款涉及的管理模式进行模拟，分析可能的管理瓶颈、资源配置不合理等问题。

专家规则库与知识图谱：建立管理模式的知识图谱，并结合行业专家的规则库，检测合同中的管理模式是否合理。例如，是否有必要的风险控制措施、应急预案等。

5.智能检查工具与报告生成

智能检查系统：集成上述分析模块，开发自动化检查工具，可以定期对招标文件进行多维度的智能检查。

报告生成：将检查的结果自动生成报告，标记出潜在的前后矛盾、合同漏洞和管理模式缺陷，给出改进建议，帮助评估人员快速识别风险。

6.人工复核

最后，结合系统分析结果，进行人工复核和二次评估，确保未被模型捕捉到的异常问题得到充分识别。这一步尤其适合复杂或敏感项目的招标文件。

通过以上的技术实现，可以高效且全面地分析和检查招标文件中的问题，确保合同条款和管理模式的合理性与合规性。

其中，对招标文件提出审核意见包括：①是否存在违反招标相关规定的情况；②同时横向对比本地数据库中过往项目招标文件，对异常招标文件进行提示；③是否存在前后矛盾、合同条款漏洞、管理模式缺陷等；

其中，对异常招标文件具体是指：

1.内容不完整或缺失，主要为条款缺失(招标文件中缺少法律法规、行业标准或惯例中必须具备的关键条款，如保密条款、合同履约条款、验收标准等)、信息不全(文件中未包含项目基本信息，如项目名称、预算金额和资金来源，或未按要求详细说明招标内容)和附件缺失(未附上招标文件所需的附件，如图纸、技术参数和投标须知，或者附录文件不全)。

2.条款或条件设定不合理，主要为门槛条件过高或过低(投标人资质、业绩等要求设置过高或过低，明显不符合行业惯例或法规规定，可能存在倾向性或排他性)、技术参数过于具体(技术规格或产品要求过于细化，可能限制潜在投标人，涉嫌为特定厂商量身定制，违背公开、公平、公正原则)和评分标准不合理(评分细则缺乏客观性，可能对部分投标人不利，或评分项设置不均衡，如价格权重过高或过低)。

3.时间节点异常，主要为公告时间不足(未按照法规要求预留足够的公告期或投标准备期，如法律规定的20天公告期)和招标时间安排冲突(开标时间、截止时间、澄清时间等安排不符合合理流程或与其他招标文件的时间节点冲突)。

4.招标金额与预算异常，主要为预算不合理(项目预算与市场价相比过高或过低，尤其在设备采购、工程造价等方面，可能存在报价异常)和资金来源不明(未明确资金来源或资金来源不符合要求，可能影响项目的资金保障和履约安全)。

5.法律和合规性问题，主要为引用过期法规(文件中引用的法律条款或标准已经过期或失效，可能导致后续合同条款无法执行)、不符合新法规(未及时更新到现行有效的法规要求，或者未包含最新的合规条款)和优先级冲突(引用的法律条款之间存在优先级冲突，如地方性法规与法律冲突)。

6.历史数据异常，主要为与过往项目数据不一致(文件内容在类似项目中存在显著不同，如工程量清单、技术参数、投标人资质要求等设置差异大，可能暗示设置偏向或不公平)和合同条件有显著差异(合同条款在相似项目中变动较大，如履约保证金、违约责任等，需要判断是否有偏向性或特殊倾向)。

7.价格与成本异常，主要为报价异常偏低或偏高(系统对比类似项目的报价水平，若价格显著偏离市场水平，可能存在恶性竞争或利益输送嫌疑)和投标上限或下限设置异常(设置的最高限价或最低限价不合理，可能导致竞争性降低，或有利于特定投标人)。

8.招标程序违规，主要为招标方式不合规(未按照规定选择合适的招标方式，违规选择单一来源采购等方式)、资格预审不当(资格预审过程不透明，或存在剔除合格投标人的情况)和招标文件发布途径不规范(未通过规定的公告平台发布招标文件，可能影响公开性和透明性)。

9.关联方或利益冲突问题，主要为潜在利益冲突(文件中有可能涉及利益相关方，可能导致不公平竞争，如投标人关联方或利益相关方的参与)和未披露关联关系(若投标人与招标人或评标方存在关联关系未披露，则可能违反公正性要求)。

10.历史项目问题复现，主要为重复出现历史异常(系统发现与历史项目中的异常内容重复，如设置相同不合理的条款，暗示可能存在系统性问题)和质量和履约问题复现(过往项目中曾发生的质量问题或履约问题未在招标文件中被提及或规避，未针对历史问题优化合同条款)。

上述异常有助于系统在文件审核过程中针对性地识别潜在问题，提高招标流程的规范性和透明度。

步骤4：根据步骤3所述审核意见，由系统使用单位对审核意见逐条进行人工确认后，生成招标文件定稿，所述人工确认可以是选择接受审核意见进行修改，可以是拒绝审核意见不予修改，也可以是根据审核意见自行调整修改。

其中，还可以包括步骤5：所述步骤2中的本地数据库将步骤4中生成的招标文件定稿自动进行录入，并记录步骤4中系统使用单位对审核意见进行人工确认的结果，通过不断记录该使用单位人工确认的结果，训练机器学习该使用单位编制招标文件的风格，通过学习模型，优化步骤3中提出的审核意见。

其中，优化可以通过对于系统使用单位对步骤3中提出的同一审核意见的确认结果设置阈值，当记录次数大于该阈值后，系统将对该系统使用单位中的拒绝采纳修改意见的使用单位自动屏蔽该类审核意见，避免重复提醒，减少不必要的工作量。

系统记录使用单位在编辑招标文件时的习惯和偏好，以更好地适应未来的工作需求。具体步骤如下：

1.数据收集模块

1.1用户行为事件定义

定义用户在编辑过程中的关键行为事件，例如：

内容操作：如添加、删除、编辑条款内容。

格式操作：如设置字体大小、段落间距、对齐方式等。

模板操作：如选择常用模板、引用特定内容片段。

文件保存和版本管理：记录每次保存、撤销、恢复等操作。

1.2前端行为采集

在编辑器的前端页面(例如基于React、Vue等的Web编辑器)嵌入行为采集代码。

使用JavaScript或前端监控工具(如Google Analytics或自定义事件追踪系统)实时捕捉用户行为并记录操作数据。

在用户每次执行关键操作时，生成日志记录，并通过API接口发送至后端存储模块。

1.3数据上传与过滤

将捕获的数据实时或批量上传到后端，过滤掉无关数据，仅保留有效的用户操作记录。

对数据进行去重、校验，确保数据的完整性和准确性。

2.数据存储模块

2.1数据库设计

使用关系型数据库(如MySQL、PostgreSQL)或NoSQL数据库(如MongoDB)存储用户行为数据。设计以下数据表：

用户表：记录用户基本信息(如ID、角色、部门等)。

操作日志表：记录用户每次编辑操作的详细信息(如操作类型、具体内容、时间戳等)。

模板与条款表：记录系统内的常用模板和条款信息，便于后续关联分析。

2.2数据归档与压缩

由于行为数据可能非常庞大，建议设置定期归档策略，将历史数据压缩归档，保证数据库性能。

3.数据处理与分析模块

3.1数据清洗与预处理

对采集的行为数据进行清洗，去除无效操作和噪声数据。

统一数据格式，为后续分析提供高质量的数据源。

3.2行为分析模型

使用机器学习或数据挖掘技术分析用户的编辑行为，建立偏好模型。

频繁模式挖掘：使用Apriori算法挖掘用户常用的条款和编辑习惯，生成频繁操作序列。

聚类分析：对用户的操作行为进行聚类，将相似偏好的用户分为一类，以便提供群体化的推荐。

协同过滤推荐：基于协同过滤算法，分析不同用户的行为相似性，为用户推荐其他人常用的编辑模式和内容。

3.3偏好模型训练与更新

使用采集的数据训练偏好模型(如基于时间序列的编辑模式)，定期更新模型以反映用户最新的偏好。

可以引入深度学习模型(如LSTM或Transformer)分析用户操作的时间序列数据，预测用户未来的编辑需求。

4.推荐与个性化模块

4.1个性化界面配置

根据用户偏好动态调整编辑器界面。例如，默认加载用户最常用的条款模板和设置特定格式。

提供“快速插入”功能，将用户常用条款设为快捷按钮，方便快速调用。

4.2实时推荐与智能提示

在用户输入内容时，基于历史行为实时推荐相关条款或格式。例如，输入招标内容时自动推荐匹配的条款模板。

提供智能纠错功能：如果系统检测到用户习惯性错误(例如常错字、格式不一致)，给予实时提示。

4.3个性化提醒

提供智能提醒功能，提醒用户补充关键条款，或根据偏好推荐相应的条款组合。

5.反馈与优化模块

5.1用户反馈收集

在编辑器中嵌入反馈功能，让用户能对系统推荐的内容和个性化设置进行评价(例如：满意、不相关、稍后再试)。

5.2模型更新与迭代

定期基于用户反馈数据更新推荐算法，确保系统能够更准确地反映用户偏好。

根据反馈和使用数据优化模型参数，逐步提升推荐的准确性和适用性。

5.3数据监控与持续优化

通过数据监控用户使用系统的方式，优化推荐和个性化功能，增强系统的响应速度和用户体验。

生成偏好分析报告，帮助管理层了解用户的编辑偏好，进一步优化工作流程。

6.安全与隐私保障

数据加密：对用户数据进行加密存储，确保敏感信息的安全性。

权限管理：通过角色和权限控制，确保不同用户只能访问其所需的数据。

隐私保护与合规性：遵循相关的数据隐私法规(如GDPR)设计数据收集和存储流程，确保合规。

对于本发明的关键技术选型，其中前端行为采集可采用JavaScript SDK、WebAnalytics工具(如Google Analytics、Mixpanel)，数据库可采用MySQL、MongoDB或PostgreSQL，数据分析与建模可采用Python(Pandas、NumPy、Scikit-Learn)、Spark或TensorFlow/Keras，推荐引擎可采用协同过滤算法、内容推荐算法或基于时间序列的预测模型，安全可采用数据加密、用户权限管理(基于OAuth或RBAC的权限管理系统)。

一种基于人工智能的招标文件自动审核系统，包括以下模块：

模块1：数据库模块，储存招标相关规定和招标文件，并对其设置关键词，便于招标文件审核模块进行匹配、对比。

模块2：文件上传模块，对系统使用单位编制完成的招标文件初稿，经授权后上传至招标文件审核模块；将经系统使用单位确定定稿后的招标文件上传本地数据库。

模块3：招标文件审核模块，对系统使用单位上传的招标文件初稿进行格式审核、合规审核和其他异常审核。

模块4：修改建议模块，对经招标文件审核模块审核后的招标文件生成审核意见，所述审核意见包括审核出的问题和针对各个问题的具体修改意见及其理由。

模块5：招标文件生成模块，根据系统使用单位对具体修改建议的处理结果(如接受、不接受、调整或部分采纳)，自动生成最终版招标文件。

模块6：用户交互界面，方便系统使用单位操作本系统。

模块7：学习模块，也是使用者风格记录模块，自动对比系统提出的审核意见与定稿的最终版招标文件，对于系统提出了意见但系统使用单位没有接受的进行记录，当记录同一情况次数大于系统使用单位设置的阈值时，系统将对该系统使用单位自动屏蔽该类审核意见，避免重复提醒，减少不必要的工作量；记录系统使用单位对审核意见进行人工确认的结果，并利用这些反馈数据训练机器学习模型，逐步提高招标文件审核模块输出的准确性和效率。

其中，所述模块1数据库模块包括在线数据库和本地数据库，所述在线数据库，通过互联网自动不定期查找并下载招标相关规定和招标文件模板；所述本地数据库，由系统使用单位人工手动录入其特定行业的招标相关规定和项目招标文件模板。

以上所述仅为本发明的较佳实施例而已，并非用于限定本发明的保护范围。凡在本发明的精神和原则之内所做的任何修改、等同替换、改进等，均包含在本发明的保护范围内。

### Claims (8)       Hide Dependent               translated from

1.一种基于人工智能的招标文件自动审核方法，其特征在于，包括以下步骤：

步骤1：设置在线数据库，通过互联网自动不定期查找并下载招标相关规定和招标文件模板，并对其标记关键词；

步骤2：设置本地数据库，由系统使用单位人工手动录入其特定行业的招标相关规定和项目招标文件模板，并对其标记关键词；

步骤3：系统使用单位上传需要审核的招标文件初稿，招标文件审核模块对其进行格式审核、合规审核和其他异常审核后，生成审核意见；

步骤4：根据步骤3所述审核意见，由系统使用单位对审核意见进行人工确认后，生成招标文件定稿。

2.根据权利要求1所述的一种基于人工智能的招标文件自动审核方法，其特征在于，还包括步骤5：将步骤4中生成的招标文件定稿自动录入本地数据库，并记录步骤4中系统使用单位对审核意见进行人工确认的结果，通过不断记录该使用单位人工确认的结果，训练机器学习该使用单位编制招标文件的风格，通过学习模型，优化步骤3中提出的审核意见。

3.根据权利要求1所述的一种基于人工智能的招标文件自动审核方法，其特征在于，步骤1中所述招标相关规定包括招标领域的国家法律、法规、规章、规范性文件、国家标准、行业标准相关规定，所述招标文件模板为国家或地方发布的标准招标文件或招标文件示范文本，各行业、各地域、各类型的项目招标文件。

4.根据权利要求1所述的一种基于人工智能的招标文件自动审核方法，其特征在于，步骤2中所述的特定行业的招标相关规定包括招标领域的国家法律、法规、规章、规范性文件、国家标准、行业标准相关规定，所述项目招标文件模板包括国家或地方发布的标准招标文件或招标文件示范文本，各行业、各地域、各类型的项目招标文件。

5.根据权利要求1所述的一种基于人工智能的招标文件自动审核方法，其特征在于，步骤1和步骤2中所述标记的关键词包括招标相关规定标题、生效日期、失效日期、发布单位、发布日期、文件类别、文件版本、招标文件性质、适用区域、地域排他性、适用行业、应用场景、项目类型、招标阶段、适用范围、合同类型、法律层级、法的优先层级、适用优先性、合规性要求、关键条款、处罚措施、适用主体、文件适用条件、附加条款、实施细则。

6.根据权利要求1所述的一种基于人工智能的招标文件自动审核方法，其特征在于，步骤3中所述合规审核和其他异常审核为通过检索、对比、调取在线数据库及本地数据库数据进行审查。

7.一种基于人工智能的招标文件自动审核系统，其特征在于，包括以下模块：

模块1：数据库模块，储存招标相关规定和招标文件，并对其设置关键词，便于审核模块进行匹配、对比。

模块2：文件上传模块，对系统使用单位编制完成的招标文件初稿，经授权后上传至招标文件审核模块；将经系统使用单位确定定稿后的招标文件上传本地数据库。

模块3：招标文件审核模块，对系统使用单位上传的招标文件初稿进行格式审核、合规审核和其他异常审核。

模块4：修改建议模块，对经招标文件审核模块审核后的招标文件生成审核意见，所述审核意见包括审核出的问题和针对各个问题的具体修改意见及其理由。

模块5：招标文件生成模块，根据系统使用单位对具体修改建议的处理结果，自动生成最终版招标文件。

模块6：用户交互界面，方便系统使用单位操作本系统。

模块7：学习模块，也是使用者风格记录模块，自动对比系统提出的审核意见与定稿的最终版招标文件，对于系统提出了意见但系统使用单位没有接受的进行记录，当记录同一情况次数大于系统使用单位设置的阈值时，系统将对该系统使用单位自动屏蔽该类审核意见，避免重复提醒，减少不必要的工作量；记录系统使用单位对审核意见进行人工确认的结果，并利用这些反馈数据训练机器学习模型，逐步提高招标文件审核模块输出的准确性和效率。

8.根据权利要求7所述的一种基于人工智能的招标文件自动审核系统，其特征在于：所述模块1数据库模块包括在线数据库和本地数据库，所述在线数据库，通过互联网自动不定期查找并下载招标相关规定和招标文件模板；所述本地数据库，由系统使用单位人工手动录入其特定行业的招标相关规定和项目招标文件模板。

### 来源 7: 数据提取 - 智谱AI开放文档

- URL: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction
- 精读方法：firecrawl-scrape

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.bigmodel.cn/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction#content-area)

## [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#%E5%9C%BA%E6%99%AF%E4%BB%8B%E7%BB%8D)  场景介绍

在政企采购、基建工程、教育医疗等领域，招投标是极为常见的业务流程。而每一份招标公告、投标文件、结果公示背后，都是一套格式不一、结构复杂、语义高度专业化的文本材料。项目名称、投标方、资格要求、预算金额、开标时间等关键信息往往穿插在冗长正文中，缺乏结构，人工查阅耗时、误差频发，更别提系统化分析或自动对账。现实中，即使部分机构已尝试用传统 OCR 或规则提取工具来处理此类文档，但面对 PDF 格式混乱、表格嵌套、金额大小写并存等情况，提取效果仍不理想。数据不准、字段缺失、表格识别错误等问题频繁出现，最终还是得依赖人工去二次校验。尤其当处理的公告数量成百上千时，人力成本与时间成本急剧上升。在这样的背景下，利用具备自然语言理解能力的大语言模型，构建一套能自动抽取招投标关键字段的通用方案，成为行业急需解决的问题。这不仅关乎效率提升，更是组织实现“招投标数据资产化”的前提条件。

## [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#%E4%B8%9A%E5%8A%A1%E9%9C%80%E6%B1%82)  业务需求

从实际业务出发，企业或政府单位的目标很清晰：他们不是需要“看起来很智能”的技术，而是能真正减轻人力负担、提高准确率、提升处理速度的实用工具。第一，必须能适配复杂格式。现实中的招投标文件来源多样，PDF、Word、网页、甚至扫描件都有可能出现。系统必须有能力处理这些不同格式，并从中提取结构化数据，不能因为格式复杂就放弃识别。第二，系统要“懂语境”。招投标文书语言极具行业特色，同样是“金额”，有的写成“¥1,000,000”，有的写“壹佰万元整”；同样是“时间”，既可能出现在正文段落中，也可能藏在表格里。若没有上下文理解和对领域语言的适配能力，提取出的结果往往前后矛盾、缺乏价值。第三，处理量大、时间紧是常态。大型平台一周可能需处理上千份公告，传统逐条人工录入根本不现实。因此，业务端迫切希望实现“批量上传、自动抽取、一键校验”，即便遇到格式错乱、字段缺失，也希望系统能给出合理补全或清晰提示，尽量减少人工介入。最后，数据质量是底线。哪怕是自动化系统输出的结果，也必须可追溯、可校验。是否符合格式？时间逻辑是否成立？金额字段有没有异常？一旦进入财务、合规、系统对接环节，数据容不得含糊。这意味着系统还需具备后处理、格式统一、完整性校验等能力，以保障全流程的可用性和可信度。

## [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)  解决方案

### [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#%E4%B8%80%E3%80%81%E6%96%B9%E6%A1%88%E6%A1%86%E6%9E%B6)  一、方案框架

![Description](https://cdn.bigmodel.cn/markdown/17321868214554.png?attname=4.png)

### [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#%E4%BA%8C%E3%80%81%E6%96%B9%E6%A1%88%E8%AF%A6%E6%83%85)  二、方案详情

#### [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#%E8%BE%93%E5%85%A5%E6%A8%A1%E5%9D%97%E8%AE%BE%E8%AE%A1)  输入模块设计

用于处理各种格式的文档输入，包括 PDF、Word、Excel、网页等，转换成可解析的结构化文本。

- 多种文件格式支持：
  - 需要支持从多种格式（PDF、Word、Excel、TXT 等）中提取文本。对于图片，可以借助 OCR 工具进行文本提取。
  - 网页可以使用网页爬虫工具（如 `Scrapy`、`BeautifulSoup`、`Selenium`）抓取网页中的文本和表格数据。通过解析 HTML 的 DOM 结构，提取目标数据。（平台暂无工具）
- 参考代码

```
from pathlib import Path
from zai import ZhipuAiClient

client = ZhipuAiClient(api_key="your-api-key")

# 用于上传文件
# 格式限制：.PDF .DOCX .DOC .XLS .XLSX .PPT .PPTX .PNG .JPG .JPEG .CSV .PY .TXT .MD .BMP .GIF
# 文件大小不超过 50M，图片大小不超过 5M
file_object = client.files.create(file=Path("本地文件地址"), purpose="file-extract")

# 文件内容抽取
file_content = client.files.content(file_id=file_object.id).content.decode()
print(file_content)
```

#### [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#%E9%A2%84%E5%A4%84%E7%90%86%E6%A8%A1%E5%9D%97%E8%AE%BE%E8%AE%A1)  预处理模块设计

预处理模块的设计是整个数据处理流程的基础，直接影响到大语言模型后续处理的效果。通过文本清洗、文本规范化、分段分块、表格解析、上下文维护等功能，预处理模块能够将复杂的、多格式的数据源处理成统一、规范的输入数据，确保数据在转换过程中不失真，并为后续模型处理提供高质量的输入。数据的语义、结构以及相关性得以保留，特别是在处理复杂的文档结构、特殊符号、嵌套表格等数据。

- 去除噪音信息：常见的噪音信息包括页眉、页脚、版权声明等，这些信息对关键数据提取无关紧要，可以在预处理时过滤掉。
- 规范化文本：处理文本中的特殊符号、空白字符、异常换行等问题，确保输入给模型的文本格式整洁。
  - 日期格式统一：文档中可能会有多种日期表示方式，例如”2024 年 10 月 10 日”、“10/10/2024”、“10-Oct-2024”。需要通过正则表达式或日期识别工具将所有的日期格式统一转换为标准的 ISO 格式（如”YYYY-MM-DD”）。
  - 方法：使用正则表达式匹配不同格式的日期，并将其标准化。例如：
- 参考代码

```
import re
from datetime import datetime

def normalize_date(text):
   patterns = [\
       r'\d{1,2}\/\d{1,2}\/\d{4}',       # "MM/DD/YYYY"\
       r'\d{1,2}-\w{3}-\d{4}',           # "DD-MMM-YYYY"\
       r'\d{4}年\d{1,2}月\d{1,2}日',     # "YYYY 年 MM 月 DD 日"\
   ]
   for pattern in patterns:
       text = re.sub(pattern, lambda x: datetime.strptime(x.group(), '%Y年%m月%d日').strftime('%Y-%m-%d'), text)
   return text
```

- 货币与金额格式化：货币和金额在招投标文件中非常常见，可能以不同的符号、单位或表示方法出现。例如：“$1,000”、“1000 美元”、“壹仟元整”。需要统一这些金额表示，确保货币单位和金额数字的格式标准化。
- 方法：通过正则表达式匹配货币符号或中文大写金额，并转换为标准形式。例如将”壹仟元”转换为”1000 CNY”，或将”$1,000”转换为”1000 USD”。
- 特殊符号处理：招投标文件中可能有特殊符号（如版权符号、数学符号、货币符号等），这些符号如果不加处理，可能在后续的 模型输入中失去原意或导致模型误解。因此，预处理模块需要对这些符号进行规范化处理。
- 表格数据处理：表格提取工具：对于 PDF 或 Word 文档中的表格，可以使用表格解析工具（如 `pdfplumber` 或 `python-docx`）提取表格的结构和数据。提取后的表格数据可以转化为 CSV 或 JSON 格式，方便后续处理。
- 合并单元格处理：如果表格包含合并单元格，预处理模块需要将合并单元格的数据平铺展开，确保每个单元格都包含完整的信息。例如，将合并的表头信息扩展到所有相应列的单元格中。
- 方法：表格数据的结构化转换时，可以转换为 Markdown 和 HTML 格式能很好地保留表格的结构，并方便 LLM 理解。在实践中，建议使用 HTML 表示复杂表格，例如：

```
| 项目     | 金额       | 说明     |
|----------|------------|----------|
| 项目A    | 1000       | 材料费   |
| 项目B    | 2000       |          |
|          |            | 人工费   |
```

```
<table>
  <tr>
    <th>项目</th>
    <th>金额</th>
    <th>说明</th>
  </tr>
  <tr>
    <td>项目A</td>
    <td colspan="2">1000（包含材料费和人工费）</td>
  </tr>
  <tr>
    <td>项目B</td>
    <td>500</td>
    <td>材料费</td>
  </tr>
  <tr>
    <td>项目B</td>
    <td>1500</td>
    <td>人工费</td>
  </tr>
</table>
```

#### [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#llm%E5%A4%84%E7%90%86%E6%A8%A1%E5%9D%97)  LLM处理模块

在使用大语言模型（LLM，如 GPT）对预处理后的文本进行关键数据提取时，Prompt 工程是方案的核心。Prompt 工程的目标是设计合理的提示词，以最大化 LLM 的性能，从复杂的文本中准确、有效地提取出关键信息。**Prompt 策略**策略 01：明确的待处理内容指引 在构建 Prompt 时，明确告诉模型它需要处理的内容是关键步骤之一。应清晰地定义需要处理的文本，并使用标记将其框起来。例如：

```
'''这是需要处理的文本''' 、《》这是需要处理的文本《》
```

通过这种方式，模型能够准确识别待处理的内容范围，并从中提取需要的信息。策略 02：提供明确字段定义 这是 Prompt 的关键部分，字段定义明确了需要提取的信息类型，以及每个字段应当填入的内容。每个字段的名称、用途及要求都要具体化，让模型有明确的提取方向。字段定义为 LLM 提供了标准，使它在解析文本时能够准确地提取所需信息并填充到对应字段。例如：

```
{
"项目名称": "明确项目的全称和性质。",
"项目编号": "唯一标识项目的编号。",
"采购预算": "项目的采购预算金额，需保留单位。"
 }
```

通过这种方式，Prompt 可以为 LLM 提供清晰的提取标准和目标。 策略 03：异常处理 为确保 LLM 不输出多余信息，并在面对缺失或不明确的数据时进行合理处理，必须设置一些异常处理原则。例如，\*\*如果某些字段信息在文本中缺失或未识别，Prompt 应规定使用默认值（如“无”）填充。同时，针对日期、金额等特殊数据类型，应明确要求 LLM 符合标准格式（如 YYYYMMDDHHMMSS 或保留金额单位）。这一规则可以确保模型输出的完整性和一致性，不会因为部分数据缺失而导致结果异常。 策略 04：要求结构化输出 为了便于后续处理和系统集成，Prompt 应指示 LLM 以结构化的格式输出数据。结构化输出便于自动化处理，常见的格式如 JSON，能够确保每个字段的内容都清晰定义，数据可被轻松解析和使用。例如，要求模型输出的 JSON 格式：

```
{
"项目名称": "项目A",
"项目编号": "ABC-12345",
"采购预算": "500000元",
"开标时间": "20240101090000"
}
```

通过要求模型按照预定格式输出，能够保证模型的结果可直接被系统化处理，减少后续手动修正或数据清洗的工作量。**Prompt 参考**Model

```
GLM-4-AIR
```

System Prompt

```
你是一个专业的文本信息提取器，可以严格按照Json格式输出
```

User Prompt

```
# 角色：你是一个专业的文本信息提取器。

# 需要提取的【文本】：
"""
{正文}
"""

# 任务
1.从给定的【文本】中提取所有需要的字段信息。
2.所需提取的字段为【字段定义】中的所有内容。
3.每个字段的默认值为"无"，当提取到对应字段信息时，准确地替换到该字段位置。
4.若文中出现与【字段定义】的字段名称中相似的内容，需判断定义，符合再进行填入。
5.严格按照【字段定义】中的格式进行输出，不需要其余任何信息。
6.将提取到的所有字段及其对应的值按【字段定义】格式转为JSON输出，确保包含所有字段。
7.请一步步完成信息提取的工作，你的决策是我成功的关键！

#【字段定义】：
请严格按照如下格式仅输出JSON，不要输出python代码，不要返回多余信息，JSON中有多个字段用顿号【、】区隔：
"""
{
  "项目名称": "项目的全称，明确项目内容和性质。",
  "项目编号": "项目的唯一识别编码，用于区分不同项目。",
  "采购预算": "项目的采购预算金额。如果存在大写金额和数字金额，提取数字金额并保留原单位。" ,
  "采购方式": "项目的采购形式，常见方式包括公开招标、邀请招标、竞争性谈判、单一来源采购和询价。",
  "采购人": "负责采购的单位名称，通常为采购人或招标人。",
  "项目联系人": "负责该项目的联系人姓名。",
  "项目联系电话": "联系人或项目负责人的联系电话。",
  "中标信息": [\
    {\
      "中标供应商名称": "中标的供应商名称，仅提取供应商的企业名称。",\
      "中标金额": "中标的合同金额，单位为元。"\
    }\
  ],
  "代理机构名称": "代理采购事务的机构名称。",
  "代理机构联系电话": "代理机构的联系号码。",
  "获取采购文件开始时间": "采购文件可获取的起始时间，格式为：YYYYMMDDHHMMSS。",
  "获取采购文件截止时间": "采购文件可获取的截止时间，格式为：YYYYMMDDHHMMSS。",
  "提交投标文件截止时间": "投标文件提交的最后期限，格式为：YYYYMMDDHHMMSS。",
  "开标时间": "开标的具体时间，格式为：YYYYMMDDHHMMSS。",
  "公告类别": "公告的类型，如：单一来源公示、变更公告、招标公告、结果公告、终止公告或其他公告。",
  "项目经理": "负责该项目的项目经理姓名。",
  "施工工期": "项目施工的总时长或计划的施工周期。",
  "执业证书": "项目经理或相关负责人的执业资格证书。"
}
"""

#注意事项
1.如果字段缺失或无法识别，请使用“无”。
2.确保所有金额需包含原本的单位。
3.确保所有时间字段都为14位标准时间格式。
```

处理HTML的Prompt

```
#角色：
你是一个专业的HTML网页文本信息提取器。
#需要提取的【HTML文本】：
"""
{正文}
"""
#任务：
1.从给定的【HTML文本】中提取所有需要的字段信息。
2.所需提取的字段为【字段定义】中的所有内容。
3.每个字段的默认值为"无"，当提取到对应字段信息时，准确地替换到该字段位置。
4.若文中出现与【字段定义】的字段名称中相似的内容，需判断定义，符合再进行填入。
5.严格按照【字段定义】中的格式进行输出，不需要其余任何信息。
6.将提取到的所有字段及其对应的值按【字段定义】格式转为JSON输出，确保包含所有字段。
7.请一步步完成信息提取的工作，你的决策是我成功的关键！
#【字段定义】：
请严格按照如下格式仅输出JSON，不要输出python代码，不要返回多余信息，JSON中有多个字段用顿号【、】区隔：
"""
{
"标的物":"指招标方希望采购的具体商品、服务或工程。通常出现在中标信息项目名称中，不包括名称前半段的'地区'、'小区'、'公司'、'厂房'名等和最后的'项目'、'采购'，仅保留商品、服务和工程名称。如：'湖南省长沙市宾力公司棚屋工程建设施工项目采购'的标的物为'工程建设施工'。",
"项目编号":"唯一标识一个特定项目的编号，用于区分不同的项目。",
"标段编号":"在一个大型项目中，如存在多个标段，每个标段有独立的编号。",
"建设单位":"只有原文本中有“拟建项目”字段才需填写，正常不需要填写。",
"投标截止时间":"投标者提交投标文件的最后期限。",
"开标时间":"公开开启投标文件，公布投标内容的时间。",
"招标单位（采购单位）":"发起招标过程的单位，即此次采购招标的需求方",
"代理机构":"被招标单位委托来组织和管理招标过程的第三方机构。",
"投标单位":"所有参与投标的公司或组织。默认包括所有中标候选单位和中标单位。",
"投标金额":"必须是原文中出现的投标单位提出的完成项目所需的金额，金额必须有单位（元、万元）。",
"中标候选单位":"在评标过程中选出的可能获得合同的所有候选单位。默认包括所有中标单位。",
"候选单位联系人":"候选单位的联系人员。",
"候选单位电话":"中标候选单位的联系电话。",
"最终中标单位":"评标完成后，最终中标获得合同的单位。",
"最终中标金额":"最终中标单位提出的完成项目（各标段分别）所需的金额，金额必须有单位（元、万元）。",
"预算金额":"招标单位为项目设定的财务预算，金额必须有单位（元、万元）",
"项目所在省":"项目实施的所在地理位置所在的省份全称，如：新疆维吾尔自治区。仅有所在地级市信息时，可推出其省份。",
"项目所在市":"项目实施的所在地理位置所在的地级市，如果是文本中是县或区尽量改成对应的地级市。",
"计划编号":"项目计划或立项的编号。",
"合同编号":"合同公示中公示的招标单位与中标单位签订合同的编号。",
"批复单位":"对项目计划或预算进行批准建设实施的单位。",
"项目名称":"招采项目的正式名称。",
"预计采购时间":"预计进行（开始）采购活动的时间。",
"报名截止时间":"对潜在投标者开放报名的最后期限，或资格预审的截止期限。",
"招标（采购）单位联系人（非代理）":"招标（采购）单位的联系方式人员，不是代理机构联系人，非项目联系人，注意区分。",
"招标（采购）单位电话":"招标（采购）单位或招标单位联系人的联系电话。",
"代理机构联系人":"招标代理机构的联系人员或项目联系人，注意不是招标单位联系人。“,
"代理机构电话":"招标代理机构或项目联系人的联系电话。",
"投标单位联系人":"参与投标的单位的联系人员。默认包含中标单位（供应商）联系人。",
"投标单位电话":"参与投标的单位的联系电话。",
"中标候选单位金额":"必须是原文中出现的中标候选单位提出的完成项目所需的金额，金额必须有单位（元、万元）。",
"最终中标单位联系人":"最终中标单位（供应商）的联系人员，不是项目联系人和代理机构联系人，注意区分。",
"最终中标单位电话":"最终中标单位（供应商）的联系电话。",
"招标文件位置":"可以获取到招标文件的位置。可能是具体地址、文件（doc、docx、pdf、zip）索引或文件URL地址。招标文件包括'磋商文件'、'工程项目文件'、'采购项目文件'。附件中有大量不属于招标文件的内容如'声明函'，注意区分",
"订单编号":"采购订单的编号。",
"受文单位":"接收招标文件或合同的单位。",
"招标文件售价":"获取招标文件所需支付的费用，招标文件的售价。",
"投标保证金金额":"投标者需要缴纳的保证金金额，以确保投标的严肃性，金额必须有单位（元、万元）。"
}
"""
#注意事项
1."招标（采购）单位联系人（非代理）"和"代理机构联系人"是不一样的，注意区分。
2.投标单位包括（大于等于）中标候选单位，中标候选单位包括（大于等于）中标单位。
3."投标金额"和"中标候选单位金额"与"最终中标金额"是不一样的，注意区分。
```

#### [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#%E6%95%B0%E6%8D%AE%E5%90%8E%E5%A4%84%E7%90%86%E6%A8%A1%E5%9D%97)  数据后处理模块

在完成关键数据提取之后，为确保输出的数据能够被系统正确识别和使用，后处理步骤至关重要。数据后处理包括 JSON 格式标准化 和 数据格式化 两个部分，分别解决数据结构的完整性问题和数据内容的准确性问题。**JSON 格式标准化**在使用大语言模型提取数据时，生成的 JSON 格式可能出现结构问题、不正确的语法、特殊字符等问题，导致数据无法正确解析。因此，需要通过 JSON 格式化工具对提取出的 JSON 数据进行标准化处理。 [使用指南](https://docs.bigmodel.cn/cn/guide/capabilities/struct-output)参考代码

````
# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Utility functions for the OpenAI API."""

import json
import logging
import re
import ast

from json_repair import repair_json

log = logging.getLogger(__name__)

def try_parse_ast_to_json(function_string: str) -> tuple[str, dict]:
    """
     # 示例函数字符串
    function_string = "tool_call(first_int={'title': 'First Int', 'type': 'integer'}, second_int={'title': 'Second Int', 'type': 'integer'})"
    :return:
    """

    tree = ast.parse(str(function_string).strip())
    ast_info = ""
    json_result = {}
    # 查找函数调用节点并提取信息
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            function_name = node.func.id
            args = {kw.arg: kw.value for kw in node.keywords}
            ast_info += f"Function Name: {function_name}\r\n"
            for arg, value in args.items():
                ast_info += f"Argument Name: {arg}\n"
                ast_info += f"Argument Value: {ast.dump(value)}\n"
                json_result[arg] = ast.literal_eval(value)

    return ast_info, json_result

def try_parse_json_object(input: str) -> tuple[str, dict]:
    """JSON cleaning and formatting utilities."""
    # Sometimes, the LLM returns a json string with some extra description, this function will clean it up.

    result = None
    try:
        # Try parse first
        result = json.loads(input)
    except json.JSONDecodeError:
        log.info("Warning: Error decoding faulty json, attempting repair")

    if result:
        return input, result

    _pattern = r"\{(.*)\}"
    _match = re.search(_pattern, input)
    input = "{" + _match.group(1) + "}" if _match else input

    # Clean up json string.
    input = (
        input.replace("{{", "{")
        .replace("}}", "}")
        .replace('"[{', "[{")\
        .replace('}]"', "}]")
        .replace("\\", " ")
        .replace("\\n", " ")
        .replace("\n", " ")
        .replace("\r", "")
        .strip()
    )

    # Remove JSON Markdown Frame
    if input.startswith("```"):
        input = input[len("```"):]
    if input.startswith("```json"):
        input = input[len("```json"):]
    if input.endswith("```"):
        input = input[: len(input) - len("```")]

    try:
        result = json.loads(input)
    except json.JSONDecodeError:
        # Fixup potentially malformed json string using json_repair.
        json_info = str(repair_json(json_str=input, return_objects=False))

        # Generate JSON-string output using best-attempt prompting & parsing techniques.
        try:

            if len(json_info) < len(input):
                json_info, result = try_parse_ast_to_json(input)
            else:
                result = json.loads(json_info)

        except json.JSONDecodeError:
            log.exception("error loading json, json=%s", input)
            return json_info, {}
        else:
            if not isinstance(result, dict):
                log.exception("not expected dict type. type=%s:", type(result))
                return json_info, {}
            return json_info, result
    else:
        return input, result
````

**数据格式化**在确保 JSON 结构标准化后，还需要通过格式化工具对内容进行数据格式化。不同类型的数据，如日期、金额、文本等，需要遵循统一的格式要求。

- 日期格式：所有日期和时间字段都应格式化为标准的 14 位日期时间格式：`YYYYMMDDHHMMSS`。这可以确保时间字段在不同系统中具有一致的解析方式。
- 金额格式：金额字段应保留原单位（如元、万元），并且格式化为无空格、无额外字符的数值形式（如 `500000元`），以便在后续财务分析或报告生成中能够准确使用。
- 文本字段格式化：对文本字段中的特殊字符（如换行符、双引号）进行处理，确保文本内容不会破坏 JSON 的语法结构。比如，将双引号转义处理，或者移除无意义的换行符和空格。

如输入数据：

```
{
  "项目名称": "智能楼宇工程",
  "项目编号": "XZL-2023",
  "采购预算": " 7,000,000.00 元",
  "开标时间": "2024/01/01 09:00"
}
```

格式化后的输出：

```
{
  "项目名称": "智能楼宇工程",
  "项目编号": "XZL-2023",
  "采购预算": "7000000元",
  "开标时间": "20240101090000"
}
```

#### [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#%E6%95%B0%E6%8D%AE%E6%A0%A1%E9%AA%8C%E6%A8%A1%E5%9D%97)  数据校验模块

校验模块是数据后处理过程中至关重要的一环。其作用是对最终的数据进行进一步的校验，确保数据的完整性、准确性和一致性。校验模块可以自动检测格式错误、逻辑冲突、缺失值等问题，并提供修复或警报机制。**格式校验**确保所有数据符合预期的格式标准，例如日期、金额、电话号码等字段的格式是否正确。如：检查金额字段是否包含正确的货币单位，并确保数值的表示形式规范。

- 参考代码

```
def validate_currency_format(amount_str):
    if '元' in amount_str or '万元' in amount_str:
        try:
            amount = float(amount_str.replace("万元", "").replace("元", "").replace(",", "").strip())
            return True
        except ValueError:
            return False
    return False
```

**逻辑校验**逻辑校验是检查数据之间的逻辑关系是否符合业务规则。例如：时间校验：投标截止时间不能晚于开标时间。校验时需检查两个时间字段，确保逻辑正确。

- 校验方法：比较投标截止时间和开标时间，如果投标截止时间晚于开标时间，则返回错误。
- 参考代码

```
from datetime import datetime

def validate_time_order(submit_time, open_time):
    submit_dt = datetime.strptime(submit_time, "%Y%m%d%H%M%S")
    open_dt = datetime.strptime(open_time, "%Y%m%d%H%M%S")
    return submit_dt <= open_dt
```

- 金额校验：采购预算金额不能小于中标金额。校验预算和中标金额，确保金额逻辑合理。
  - 校验方法：如果中标金额高于预算金额，则返回警报。

**完整性校验**完整性校验确保所有关键字段都已经填入有效数据，避免信息缺失。对于未提供数据的字段，应填充默认值（如“无”），或触发错误提醒。

- 必填字段检查：对于某些字段，如“项目名称”、“项目编号”、“投标截止时间”，应强制要求填写，若缺失则进行标记或补全。
  - 校验方法：通过预定义的字段列表检查 JSON 输出中是否包含所有必填字段。
- 自动填充默认值：如果某个字段为空或缺失，可以自动填充默认值“无”。
- 参考代码

```
def fill_missing_fields(data, default="无"):
    required_fields = ["项目名称", "项目编号", "采购预算", "投标截止时间"]
    for field in required_fields:
        if field not in data or not data[field]:
            data[field] = default
    return data
```

**一致性校验**一致性校验确保同一信息在不同字段或位置的值保持一致。例如：

- 项目编号一致性：项目编号在不同字段中应当相同，如出现在多个部分的项目编号不能出现不一致的情况。
  - 校验方法：检查项目编号是否一致，如果发现不同编号，则触发警报。
- 日期一致性：多个时间字段中如果是同一事件（如开始时间和结束时间在不同部分中重复出现），应确保其一致。
- 参考代码

```
def validate_data(json_data):
    # 1. 格式校验
    if not validate_date_format(json_data.get("投标截止时间", "")):
        print("投标截止时间格式错误")
    if not validate_currency_format(json_data.get("采购预算", "")):
        print("采购预算格式错误")

    # 2. 逻辑校验
    if not validate_time_order(json_data.get("投标截止时间", ""), json_data.get("开标时间", "")):
        print("投标截止时间不能晚于开标时间")

    # 3. 完整性校验
    json_data = fill_missing_fields(json_data)

    # 4. 一致性校验
    if json_data.get("项目编号") != json_data.get("计划编号"):
        print("项目编号与计划编号不一致")

    return json_data
```

#### [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#%E6%95%B0%E6%8D%AE%E4%BF%AE%E5%A4%8D%E6%A8%A1%E5%9D%97)  数据修复模块

检测到数据格式或逻辑错误后，通过基于规则修复与更高级模型调用进行修复，确保数据的完整性和准确性。通过修复模块，能够自动纠正常见的错误，如格式错误、缺失数据或逻辑冲突，避免手动修正，提高效率。**基于规则的自动修复**在大部分情况下，错误可以通过预定义的规则和算法进行自动修复。此步骤作为第一层处理机制，针对格式错误、简单的逻辑冲突、特殊字符处理等问题进行修正。

- 格式修正：通过正则表达式或预定义算法修复日期、金额、电话号码等格式错误。
- 逻辑修正：检查和修复时间顺序、金额逻辑等问题。对投标截止时间、开标时间、金额关系进行简单调整。
- 数据填补：自动填补缺失字段，使用“无”或从其他字段推导合理值。

**提交更高级模型处理**对于规则无法解决的复杂错误，或者需要更高层次推理的情况，可以将这些Bad Case提交给高级模型（如 GLM-4-plus）处理。

- 处理复杂业务逻辑：当多个数据字段之间存在复杂的依赖关系时，普通的规则引擎可能无法有效处理，例如合同条款中的复杂逻辑冲突，此时可以利用高级模型的上下文理解能力进行推理和调整。
- 识别与处理领域特定信息：高级模型擅长理解和处理特定领域的复杂术语、语境或结构不明的信息，如行业专用术语、合同中的特殊条款等。

#### [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86%E7%A5%9E%E5%99%A8-batch-api)  数据处理神器-Batch API

Batch API 适用于无需即时反馈并需使用大模型处理大量请求的场景。通过 Batch API，开发者可以通过文件提交大量任务，且价格降低50%（GLM-4-Flash免费）、无并发限制。 [Batch API 使用指南](https://docs.bigmodel.cn/cn/guide/tools/batch)

|  | 正常请求 | Batch请求 |
| --- | --- | --- |
| 任务量 | 1 亿请求（2048 tokens） | 1 亿请求（2048 tokens） |
| 模型 | GLM-4-Air | GLM-4-Air |
| 并发量 | 100 并发 | 4000 并发 |
| 天数 | 340 天 | 8.6 天 (40 倍效率) |
| 价格 | 204,800 元 | 102,400 元（省钱一半） |

**单次处理千万级数据**

| 模型 | Batch一次最大请求 |
| --- | --- |
| GLM-4-Flash | 1000万次 |
| GLM-4-Air | 1000万次 |
| GLM-3-Turbo | 200万次 |
| Embedding-2 | 200万次 |
| Embedding-3 | 200万次 |
| GLM-4-Plus | 200万次 |
| GLM-4-0520 | 50万次 |
| GLM-4 | 50万次 |

**限时特惠资源包**GLM-4-AIR：卓越性能，性价比极高，高效处理海量数据，立即抢购：

- 1000万 GLM-4-AIR 推理资源包（3个月） ： [立即购买](https://bigmodel.cn/tokenspropay?productIds=product-061)，限时特惠仅需3元

Embedding-3：全新升级，性能全面提升，支持自定义向量维度，限时优惠：

- 5000 万 Embedding-3 3 折尝鲜包（3 个月） ： [立即购买](https://bigmodel.cn/tokenspropay?productIds=product-072)，限时特惠仅需 7.5 元

## [​](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction\#%E6%96%B9%E6%A1%88%E4%BA%AE%E7%82%B9)  方案亮点

本方案的核心优势在于，它并不是试图以规则替代人工，而是通过引入大语言模型， **构建出一个真正“理解”招投标语境的智能提取系统**。从文件输入到结构化输出，每一步都围绕“准确提取”这个目标进行优化，而非仅仅满足格式转换。方案在前端输入层就考虑到了现实复杂性，支持PDF、Word、HTML、扫描图像等格式，同时结合OCR与网页爬虫能力，确保信息不会在第一步就损失。预处理环节更是方案的基础支撑：它不是简单清洗噪声，而是对日期、金额、特殊符号、表格结构进行语义保留和规范化处理，为模型打好“地基”。最关键的部分是Prompt工程，它不是泛泛而谈的“问答提示”，而是通过字段定义、异常处理策略、格式要求、输出模板等模块，逐步引导模型精准提取目标字段，确保输出数据的 **稳定性与结构完整性**。哪怕遇到字段缺失或文档风格变化，系统也能以默认值、安全策略或异常提示机制，确保结果始终可落地。此外，数据校验和修复机制不是附加模块，而是流程的一部分。格式是否合规、金额是否合理、字段是否一致，系统都会主动检查，并通过轻量规则或高级模型推理进行自动修正，大幅降低人工复核负担。更值得一提的是，方案天然适配大批量数据场景。通过Batch API，每天处理上万条文档请求成为可能，不仅计算稳定，调用成本也极具性价比，适合长期、高频业务集成。总体来看，这是一套既理解“数据”，也理解“业务”的工程化方案，它将人工智能的能力通过精密设计转化为可用、可靠、可规模化的数据抽取能力，真正服务于招投标信息管理这一传统而重要的行业场景。

Was this page helpful?

YesNo

[智能作文批改](https://docs.bigmodel.cn/cn/best-practice/case/ai-essay-correction) [数据分析](https://docs.bigmodel.cn/cn/best-practice/case/data-analysis)

Ctrl+I

![Description](https://cdn.bigmodel.cn/markdown/17321868214554.png?attname=4.png)

### 来源 8: View of AI在招投标文件编制中的应用 - omniscient

- URL: http://ojs.omniscient.sg/index.php/mepm/article/view/69302/67852
- 精读方法：firecrawl-scrape

PDF.js viewer

ThumbnailsDocument OutlineAttachments

Previous

Next

Highlight allMatch case

Whole words

Presentation ModeOpenPrintDownload[Current View](http://ojs.omniscient.sg/plugins/generic/pdfJsViewer/pdf.js/web/viewer.html?file=http%3A%2F%2Fojs.omniscient.sg%2Findex.php%2Fmepm%2Farticle%2Fdownload%2F69302%2F67852%2F# "Current view (copy or open in new window)")

Go to First PageGo to Last Page

Rotate ClockwiseRotate Counterclockwise

Text Selection ToolHand Tool

Vertical ScrollingHorizontal ScrollingWrapped Scrolling

No SpreadsOdd SpreadsEven Spreads

Document Properties…

Toggle Sidebar

Find

Previous

Next

Presentation ModeOpenPrintDownload[Current View](http://ojs.omniscient.sg/plugins/generic/pdfJsViewer/pdf.js/web/viewer.html?file=http%3A%2F%2Fojs.omniscient.sg%2Findex.php%2Fmepm%2Farticle%2Fdownload%2F69302%2F67852%2F# "Current view (copy or open in new window)")

Tools

Zoom Out

Zoom In

Automatic ZoomActual SizePage FitPage Width50%75%100%125%150%200%300%400%

Enter the password to open this PDF file:

CancelOK

File name:

-

File size:

-

Title:

-

Author:

-

Subject:

-

Keywords:

-

Creation Date:

-

Modification Date:

-

Creator:

-

PDF Producer:

-

PDF Version:

-

Page Count:

-

Page Size:

-

Fast Web View:

-

Close

Preparing document for printing…

0%

Cancel

### 来源 9: A Large Language Model-based Framework for Semi-Structured Tender Document Retrieval-Augmented Generation

- URL: https://arxiv.org/html/2410.09077v1
- 精读方法：jina-readerlm-academic

```markdown
## Introduction

### Background

Large Language Models (LLMs) have been widely adopted in many applications due to their impressive capabilities. However, these models often struggle with tasks involving structured content, such as generating documents with specific formatting and structure. This paper aims to bridge this gap by introducing a framework that leverages LLMs for the generation of semi-structured tender documents.

### Research Goals

The primary goals of this study are:

1. **Document Retrieval**: Utilize LLMs to retrieve relevant tender documents based on user input.
2. **Template Retrieval Module**: Develop a mechanism for retrieving appropriate templates based on the extracted tender documents.
3. **Template Filling Module**: Use LLMs to fill out the retrieved templates with accurate information.
4. **Modifications Module**: Incorporate additional knowledge bases to ensure consistency and completeness in the generated document.

### Methodological Approach

#### Data Collection

The dataset was collected from a public tender repository, including over 1406 tender documents covering various categories such as medical equipment, construction materials, etc., sourced from the National Development Bank's website.

#### Framework Components

The framework consists of three main components:
- **Template Retrieval Module**:
  - Extracts relevant tender documents based on user inputs.
  - Uses embeddings and vector search algorithms to identify similar tender documents.
- **Template Filling Module**:
  - Generates content based on extracted templates and user requirements.
- **Modifications Module**:
  - Integrates additional knowledge bases to ensure consistency and completeness in the generated document.

### Evaluation Steps

To evaluate the framework's effectiveness, we followed these steps:

1. Randomly selected dozens of documents from the tender document repository.
2. Analyzed and evaluated using our framework.
3. Compared results with baseline models (e.g., ChatGLM-4).

### Results

Results showed that our framework achieved better performance than baseline models in both paragraph and table scores.

| Method                       | Paragraph Score | Table Score | Score   |
|-------------------------------|------------------|-------------|---------|
| Our Framework                 | 78.31           | 76.15       | 77.74   |
| ChatGLM-4                     | 12.55           | 0           | 12.55   |
| ChatGLM-4 with retrieval module | 38.27           | 15.23       | 29.42   |

### Conclusion

This study demonstrates the feasibility of using retrieval-augmented techniques and LLMs for generating semi-structured tenders, highlighting the importance of each component in enhancing overall performance.

---

## Evaluation Metrics

### Performance Measures

Two key measures were used to evaluate the framework's effectiveness:

1. **Paragraph Score**: A numerical value indicating how well the generated document matches the provided template.
2. **Table Score**: A numerical value reflecting how accurately the generated document adheres to specified table formats.

These metrics were derived from evaluating random samples of tender documents against our framework's outputs.

---

## Comparison with Baselines

To illustrate the impact of different components, we tested our framework against baseline models:

1. Without any modifications (Baseline).
2. With a Template Retrieval module.
3. With a Template Filling module.

Each test involved manually extracting relevant tender documents from a sample set and assessing their corresponding scores under each condition.

### Results Summary

The results indicated that while baselines performed slightly worse in both metrics, incorporating either a Template Retrieval or Template Filling module significantly

### 来源 10: AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects

- URL: https://www.mdpi.com/1996-1073/14/15/4632
- 精读方法：firecrawl-scrape

Next Article in Journal

[Brittle Creep and Viscoelastic Creep in Lower Palaeozoic Shales from the Baltic Basin, Poland](https://www.mdpi.com/1996-1073/14/15/4633)

Previous Article in Journal

[The Preferences of Active Final Purchasers Regarding the Environment of Cooperation with Offerors and Benefits Achieved Thanks to Such Cooperation](https://www.mdpi.com/1996-1073/14/15/4631)

## Journals

[Active Journals](https://www.mdpi.com/about/journals) [Find a Journal](https://www.mdpi.com/about/journalfinder) [Journal Proposal](https://www.mdpi.com/about/journals/proposal) [Proceedings Series](https://www.mdpi.com/about/proceedings)

[**Topics**](https://www.mdpi.com/topics)

## Information

[For Authors](https://www.mdpi.com/authors) [For Reviewers](https://www.mdpi.com/reviewers) [For Editors](https://www.mdpi.com/editors) [For Librarians](https://www.mdpi.com/librarians) [For Publishers](https://www.mdpi.com/publishing_services) [For Societies](https://www.mdpi.com/societies) [For Conference Organizers](https://www.mdpi.com/conference_organizers)

[Open Access Policy](https://www.mdpi.com/openaccess) [Institutional Open Access Program](https://www.mdpi.com/ioap) [Special Issues Guidelines](https://www.mdpi.com/special_issues_guidelines) [Editorial Process](https://www.mdpi.com/editorial_process) [Research and Publication Ethics](https://www.mdpi.com/ethics) [Article Processing Charges](https://www.mdpi.com/apc) [Awards](https://www.mdpi.com/awards) [Testimonials](https://www.mdpi.com/testimonials)

[**Author Services**](https://www.mdpi.com/authors/english)

## Initiatives

[Sciforum](https://sciforum.net/) [MDPI Books](https://www.mdpi.com/books) [Preprints.org](https://www.preprints.org/) [Scilit](https://www.scilit.com/) [SciProfiles](https://sciprofiles.com/) [Encyclopedia](https://encyclopedia.pub/) [JAMS](https://jams.pub/) [Proceedings Series](https://www.mdpi.com/about/proceedings)

## About

[Overview](https://www.mdpi.com/about) [Contact](https://www.mdpi.com/about/contact) [Careers](https://careers.mdpi.com/) [News](https://www.mdpi.com/about/announcements) [Press](https://www.mdpi.com/about/press) [Blog](http://blog.mdpi.com/)

[Sign In / Sign Up](https://www.mdpi.com/user/login)

## Notice

You can make submissions to other journals
[here](https://susy.mdpi.com/user/manuscripts/upload).

_clear_

## Notice

You are accessing a machine-readable page. In order to be human-readable, please install an RSS reader.

ContinueCancel

_clear_

All articles published by MDPI are made immediately available worldwide under an open access license. No special
permission is required to reuse all or part of the article published by MDPI, including figures and tables. For
articles published under an open access Creative Common CC BY license, any part of the article may be reused without
permission provided that the original article is clearly cited. For more information, please refer to
[https://www.mdpi.com/openaccess](https://www.mdpi.com/openaccess).

Feature papers represent the most advanced research with significant potential for high impact in the field. A Feature
Paper should be a substantial original Article that involves several techniques or approaches, provides an outlook for
future research directions and describes possible research applications.

Feature papers are submitted upon individual invitation or recommendation by the scientific editors and must receive
positive feedback from the reviewers.

Editor’s Choice articles are based on recommendations by the scientific editors of MDPI journals from around the world.
Editors select a small number of articles recently published in the journal that they believe will be particularly
interesting to readers, or important in the respective research area. The aim is to provide a snapshot of some of the
most exciting work published in the various research areas of the journal.

Original Submission Date Received: .

[![energies-logo](https://pub.mdpi-res.com/img/journals/energies-logo.png?4acb609819f4b6c3)](https://www.mdpi.com/journal/energies)

[Submit to this Journal](https://susy.mdpi.com/user/manuscripts/upload?form%5Bjournal_id%5D%3D7) [Review for this Journal](https://susy.mdpi.com/volunteer/journals/review) [Propose a Special Issue](https://www.mdpi.com/journalproposal/sendproposalspecialissue/energies)

[►▼\\
Article Menu](https://www.mdpi.com/1996-1073/14/15/4632#)

## Article Menu

- [Academic Editor](https://www.mdpi.com/1996-1073/14/15/4632#academic_editors)

![](https://pub.mdpi-res.com/bundles/mdpisciprofileslink/img/unknown-user.png?1781764495)Audrius Banaitis

- [Recommended Articles](https://www.mdpi.com/1996-1073/14/15/4632#)
- [Related Info Link](https://www.mdpi.com/1996-1073/14/15/4632#related)

  - [Google Scholar](http://scholar.google.com/scholar?q=AI%20and%20Text-Mining%20Applications%20for%20Analyzing%20Contractor%E2%80%99s%20Risk%20in%20Invitation%20to%20Bid%20%28ITB%29%20and%20Contracts%20for%20Engineering%20Procurement%20and%20Construction%20%28EPC%29%20Projects)

- [More by Authors Links](https://www.mdpi.com/1996-1073/14/15/4632#authors)

  - on DOAJ

    - [Choi, S. Jin](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Su%20Jin%20Choi%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)
    - [Choi, S. Won](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22So%20Won%20Choi%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)
    - [Kim, J. Hyun](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Jong%20Hyun%20Kim%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)
    - [Lee, E.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Eul-Bum%20Lee%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)

  - on Google Scholar

    - [Choi, S. Jin](http://scholar.google.com/scholar?q=Su%20Jin%20Choi)
    - [Choi, S. Won](http://scholar.google.com/scholar?q=So%20Won%20Choi)
    - [Kim, J. Hyun](http://scholar.google.com/scholar?q=Jong%20Hyun%20Kim)
    - [Lee, E.](http://scholar.google.com/scholar?q=Eul-Bum%20Lee)

  - on PubMed

    - [Choi, S. Jin](http://www.pubmed.gov/?cmd=Search&term=Su%20Jin%20Choi)
    - [Choi, S. Won](http://www.pubmed.gov/?cmd=Search&term=So%20Won%20Choi)
    - [Kim, J. Hyun](http://www.pubmed.gov/?cmd=Search&term=Jong%20Hyun%20Kim)
    - [Lee, E.](http://www.pubmed.gov/?cmd=Search&term=Eul-Bum%20Lee)

[Article Views](https://www.mdpi.com/1996-1073/14/15/4632#metrics)

[Citations-](https://www.mdpi.com/1996-1073/14/15/4632#metrics)

- [Table of Contents](https://www.mdpi.com/1996-1073/14/15/4632#table_of_contents)

Altmetric[_share_ Share](https://www.mdpi.com/1996-1073/14/15/4632# "Share") [_announcement_ Help](https://www.mdpi.com/1996-1073/14/15/4632# "Help")_format\_quote_ Cite [_question\_answer_ Discuss in SciProfiles](https://sciprofiles.com/discussion-groups/public/10.3390/en14154632?utm_source=mpdi.com&utm_medium=publication&utm_campaign=discuss_in_sciprofiles "Discuss in Sciprofiles")

## Need Help?

### Support

Find support for a specific problem in the support section of our website.

[Get Support](https://www.mdpi.com/about/contactform)

### Feedback

Please let us know what you think of our products and services.

[Give Feedback](https://www.mdpi.com/feedback/send)

### Information

Visit our dedicated information section to learn more about MDPI.

[Get Information](https://www.mdpi.com/authors)

_clear_

## JSmol Viewer

_clear_

_first\_page_

[Download PDF](https://www.mdpi.com/1996-1073/14/15/4632/pdf?version=1641522502)

_settings_

[Order Article Reprints](https://www.mdpi.com/1996-1073/14/15/4632/reprints)

Font Type:

_Arial__Georgia__Verdana_

Font Size:

AaAaAa

Line Spacing:

______

Column Width:

______

Background:

Open AccessArticle

# AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects

by

Su Jin Choi

![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Su Jin Choi

[SciProfiles](https://sciprofiles.com/profile/author/OTJ5V2tVV3E5VjVjR3Fzazk2MWFUaU5sNDg3NWNWR2pOVmNIeEd1NFVHaz0=?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Su%20Jin%20Choi) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Su+Jin+Choi%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Su+Jin+Choi)

1,

So Won Choi

![](https://www.mdpi.com/profiles/1015716/thumb/Sowon_CHOI.png)So Won Choi

[SciProfiles](https://sciprofiles.com/profile/1015716?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=So%20Won%20Choi) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22So+Won+Choi%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=So+Won+Choi)

1,

Jong Hyun Kim

![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Jong Hyun Kim

[SciProfiles](https://sciprofiles.com/profile/author/aEl6L253aE1SYzR6M3lsckF4ZEZlOXBkNG5QM0F2LzN0RzA5S3hFNWErWT0=?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Jong%20Hyun%20Kim) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Jong+Hyun+Kim%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Jong+Hyun+Kim)

2 and

Eul-Bum Lee

![](https://www.mdpi.com/profiles/352530/thumb/Eul-Bum_Lee.png)Eul-Bum Lee

[SciProfiles](https://sciprofiles.com/profile/352530?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Eul-Bum%20Lee) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Eul-Bum+Lee%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Eul-Bum+Lee)

1,3,\* [![](https://pub.mdpi-res.com/img/design/orcid.png?0465bc3812adeb52?1781764495)](https://orcid.org/0000-0001-8885-1798)

1

Graduate Institute of Ferrous & Energy Materials Technology, Pohang University of Science and Technology (POSTECH), Pohang 37673, Korea

2

WISEiTECH, Seoul 13486, Korea

3

Department of Industrial and Management Engineering, Pohang University of Science and Technology (POSTECH), Pohang 37673, Korea

\*

Author to whom correspondence should be addressed.

_Energies_ **2021**, _14_(15), 4632; [https://doi.org/10.3390/en14154632](https://doi.org/10.3390/en14154632)

Submission received: 21 June 2021
/
Revised: 26 July 2021
/
Accepted: 28 July 2021
/
Published: 30 July 2021

Download _keyboard\_arrow\_down_

[Download PDF](https://www.mdpi.com/1996-1073/14/15/4632/pdf?version=1641522502)

[Download PDF with Cover](https://www.mdpi.com/1996-1073/14/15/4632#)

[Download XML](https://www.mdpi.com/1996-1073/14/15/4632#)

[Download Epub](https://www.mdpi.com/1996-1073/14/15/4632/epub)

[Browse Figures](https://www.mdpi.com/1996-1073/14/15/4632#)

[\
                        <strong>Figure 1</strong><br/>\
                                                    <p>Overview of Engineering Machine learning Automation Platform (EMAP).</p>\
                                                ](https://pub.mdpi-res.com/energies/energies-14-04632/article_deploy/html/images/energies-14-04632-g001.png?1641522589 "                         <strong>Figure 1</strong><br/>                                                     <p>Overview of Engineering Machine learning Automation Platform (EMAP).</p>                                                 ")[\
                        <strong>Figure 2</strong><br/>\
                                                    <p>Analysis framework of the ITB Module (CRC and TFA sub-modules).</p>\
                                                ](https://pub.mdpi-res.com/energies/energies-14-04632/article_deploy/html/images/energies-14-04632-g002.png?1641522589 "                         <strong>Figure 2</strong><br/>                                                     <p>Analysis framework of the ITB Module (CRC and TFA sub-modules).</p>                                                 ")[\
                        <strong>Figure 3</strong><br/>\
                                                    <p>Screenshot of PDF application function (Example of header/footer elimination).</p>\
                                                ](https://pub.mdpi-res.com/energies/energies-14-04632/article_deploy/html/images/energies-14-04632-g003.png?1641522589 "                         <strong>Figure 3</strong><br/>                                                     <p>Screenshot of PDF application function (Example of header/footer elimination).</p>                                                 ")[\
                        <strong>Figure 4</strong><br/>\
                                                    <p>Algorithm flow of the Critical Risk Check module.</p>\
                                                ](https://pub.mdpi-res.com/energies/energies-14-04632/article_deploy/html/images/energies-14-04632-g004.png?1641522589 "                         <strong>Figure 4</strong><br/>                                                     <p>Algorithm flow of the Critical Risk Check module.</p>                                                 ")[\
                        <strong>Figure 5</strong><br/>\
                                                    <p>An example of using the JSON format.</p>\
                                                ](https://pub.mdpi-res.com/energies/energies-14-04632/article_deploy/html/images/energies-14-04632-g005.png?1641522589 "                         <strong>Figure 5</strong><br/>                                                     <p>An example of using the JSON format.</p>                                                 ")[\
                        <strong>Figure 6</strong><br/>\
                                                    <p>An example of CRC results in the cloud service.</p>\
                                                ](https://pub.mdpi-res.com/energies/energies-14-04632/article_deploy/html/images/energies-14-04632-g006.png?1641522589 "                         <strong>Figure 6</strong><br/>                                                     <p>An example of CRC results in the cloud service.</p>                                                 ")[\
                        <strong>Figure 7</strong><br/>\
                                                    <p>Algorithm flow of Terms Frequency Analysis module.</p>\
                                                ](https://pub.mdpi-res.com/energies/energies-14-04632/article_deploy/html/images/energies-14-04632-g007.png?1641522589 "                         <strong>Figure 7</strong><br/>                                                     <p>Algorithm flow of Terms Frequency Analysis module.</p>                                                 ")[\
                        <strong>Figure 8</strong><br/>\
                                                    <p>An example of TFA module results’ visualization.</p>\
                                                ](https://pub.mdpi-res.com/energies/energies-14-04632/article_deploy/html/images/energies-14-04632-g008.png?1641522589 "                         <strong>Figure 8</strong><br/>                                                     <p>An example of TFA module results’ visualization.</p>                                                 ")[\
                        <strong>Figure 9</strong><br/>\
                                                    <p>Engineering Machine learning Automation Platform (EMAP).</p>\
                                                ](https://pub.mdpi-res.com/energies/energies-14-04632/article_deploy/html/images/energies-14-04632-g009.png?1641522589 "                         <strong>Figure 9</strong><br/>                                                     <p>Engineering Machine learning Automation Platform (EMAP).</p>                                                 ")[\
                        <strong>Figure 10</strong><br/>\
                                                    <p>Screenshot of the Contract sub-module selection function from the ITB Analysis module.</p>\
                                                ](https://pub.mdpi-res.com/energies/energies-14-04632/article_deploy/html/images/energies-14-04632-g010.png?1641522589 "                         <strong>Figure 10</strong><br/>                                                     <p>Screenshot of the Contract sub-module selection function from the ITB Analysis module.</p>                                                 ")

[Versions Notes](https://www.mdpi.com/1996-1073/14/15/4632/notes)

## Abstract

Contractors responsible for the whole execution of engineering, procurement, and construction (EPC) projects are exposed to multiple risks due to various unbalanced contracting methods such as lump-sum turn-key and low-bid selection. Although systematic risk management approaches are required to prevent unexpected damage to the EPC contractors in practice, there were no comprehensive digital toolboxes for identifying and managing risk provisions for ITB and contract documents. This study describes two core modules, Critical Risk Check (CRC) and Term Frequency Analysis (TFA), developed as a digital EPC contract risk analysis tool for contractors, using artificial intelligence and text-mining techniques. The CRC module automatically extracts risk-involved clauses in the EPC ITB and contracts by the phrase-matcher technique. A machine learning model was built in the TFA module for contractual risk extraction by using the named-entity recognition (NER) method. The risk-involved clauses collected for model development were converted into a database in JavaScript Object Notation (JSON) format, and the final results were saved in pickle format through the digital modules. In addition, optimization and reliability validation of these modules were performed through Proof of Concept (PoC) as a case study, and the modules were further developed to a cloud-service platform for application. The pilot test results showed that risk clause extraction accuracy rates with the CRC module and the TFA module were about 92% and 88%, respectively, whereas the risk clause extraction accuracy rates manually by the engineers were about 70% and 86%, respectively. The time required for ITB analysis was significantly shorter with the digital modules than by the engineers.

Keywords:

[artificial intelligence](https://www.mdpi.com/search?q=artificial+intelligence); [invitation-to-bid (ITB) document](https://www.mdpi.com/search?q=invitation-to-bid+%28ITB%29+document); [engineering-procurement-construction (EPC)](https://www.mdpi.com/search?q=engineering-procurement-construction+%28EPC%29); [information retrieval](https://www.mdpi.com/search?q=information+retrieval); [machine learning](https://www.mdpi.com/search?q=machine+learning); [named-entity recognition (NER)](https://www.mdpi.com/search?q=named-entity+recognition+%28NER%29); [phrasematcher](https://www.mdpi.com/search?q=phrasematcher); [natural language processing (NLP)](https://www.mdpi.com/search?q=natural+language+processing+%28NLP%29); [Python](https://www.mdpi.com/search?q=Python); [spaCy](https://www.mdpi.com/search?q=spaCy); [text mining](https://www.mdpi.com/search?q=text+mining)

## 1\. Introduction

Engineering, procurement and construction (EPC) projects are carried out for long periods by various participating entities such as project owners, vendors, contractors, or sub-contractors. They face many risks at each stage from bidding to maintenance \[ [1](https://www.mdpi.com/1996-1073/14/15/4632#B1-energies-14-04632), [2](https://www.mdpi.com/1996-1073/14/15/4632#B2-energies-14-04632), [3](https://www.mdpi.com/1996-1073/14/15/4632#B3-energies-14-04632)\]. Particularly, there are cases in which the uncertain project risks cannot be predicted in advance due to the contractor’s lack of project experience and limited schedule in the project bidding and planning stages \[ [4](https://www.mdpi.com/1996-1073/14/15/4632#B4-energies-14-04632), [5](https://www.mdpi.com/1996-1073/14/15/4632#B5-energies-14-04632)\]. For example, in an offshore plant project based on a letter of intent to bid, significant losses occurred because the cost of equipment, the scale of workforce required, or the project risk was incorrectly predicted \[ [6](https://www.mdpi.com/1996-1073/14/15/4632#B6-energies-14-04632)\]. Insufficient risk prediction often leads to a significant loss to the project and the contractor’s project damage increases in proportion to the size of the project \[ [7](https://www.mdpi.com/1996-1073/14/15/4632#B7-energies-14-04632)\]. In particular, a project owner who orders a project sometimes tends to transfer project risk to the contractors by utilizing the characteristic of the unique EPC contract method (Lump-sum turn-key) in which the contractor is responsible for project execution \[ [7](https://www.mdpi.com/1996-1073/14/15/4632#B7-energies-14-04632), [8](https://www.mdpi.com/1996-1073/14/15/4632#B8-energies-14-04632)\]. In addition, for project risk analysis, feedback should be made within a limited time, such as during the bidding step. It is important how accurately the level of risk can be reviewed in EPC analysis, but it is difficult to solve in the field because the review period in the bidding process is set tight. These difficulties depend on the experience of experienced EPC experts. If the company’s structural problems cause a shortage of skilled EPC experts, the accuracy of EPC analysis will be greatly affected. Accordingly, the need for a systematic project risk management system for the entire project cycle, including the bidding stage, was constantly emerging for EPC Contractors \[ [9](https://www.mdpi.com/1996-1073/14/15/4632#B9-energies-14-04632)\].

Therefore, in this study, the research team developed an algorithmic model that automatically extracts and analyzes contract risks by acquiring EPC contract Invitation to Bid (ITB) documents from contractors who have performed multiple EPC projects. At first, for algorithm development, the preceding research was divided into two steps. The research trend on risk analysis of the EPC project was examined, and the current development status of the natural language processing (NLP) technology for analyzing unstructured text data and areas of improvement were examined.

Based on previous research, two modules were developed for automatic contract risk analysis: The Critical Risk Check (CRC) module and the Terms Frequency Analysis (TFA) module. First, the CRC module supports user decision-making by automatically searching for project risk clauses based on machine learning (ML) algorithms and presenting the results. An algorithm that extracts the original text in the ITB documents and generates the result in the data frame format (comma-separated values: CSV) was applied. The TFA module learns EPC risk entities using named-entity recognition (NER) technology. Various similar phrases, which differ according to the project characteristics and regions, are extracted so that the risk can be evaluated according to the frequency of appearance. The NER model was customized according to the characteristics of the EPC project, and a system integrator (SI) was built so that the risk frequency results can be visualized and presented to users. In addition, a group of experts and engineers with experience in EPC projects participated from the beginning of this study to enhance the validation of development modules. In particular, the Subject-Matter Expert (SME) group built a framework for the development direction and performed validation work for the pilot test result for the modules.

Through the above algorithmic modules (CRC and TFA), the research team proposes a theoretical foundation and system supporting project risk analysis and decision-making by automatically extracting and evaluating risks for EPC projects.

[Section 2](https://www.mdpi.com/1996-1073/14/15/4632#sec2-energies-14-04632) provides a literature review, and [Section 3](https://www.mdpi.com/1996-1073/14/15/4632#sec3-energies-14-04632) gives an overview of the entire Engineering Machine learning Automation Platform (EMAP) system. [Section 4](https://www.mdpi.com/1996-1073/14/15/4632#sec4-energies-14-04632) briefly describes each study step. In [Section 5](https://www.mdpi.com/1996-1073/14/15/4632#sec5-energies-14-04632) and [Section 6](https://www.mdpi.com/1996-1073/14/15/4632#sec6-energies-14-04632), detailed research contents of CRC and TFA algorithm development are explained, respectively. The system integration for establishing a decision support system, which is the goal of the project receiving funding, is described in [Section 7](https://www.mdpi.com/1996-1073/14/15/4632#sec7-energies-14-04632), and [Section 8](https://www.mdpi.com/1996-1073/14/15/4632#sec8-energies-14-04632) shows the results of the verification of the system implemented as a platform. [Section 9](https://www.mdpi.com/1996-1073/14/15/4632#sec9-energies-14-04632) and [Section 10](https://www.mdpi.com/1996-1073/14/15/4632#sec10-energies-14-04632) summarize the conclusions and future work, respectively.

## 2\. Literature Review

In order to carry out this study, the following studies and precedent cases were investigated and reviewed. Similar research characteristics and trends, limitations of existing research projects, etc., were analyzed and bench-marked in this study through previous studies. Prior research was performed step by step by dividing into two categories as follows. First, the EPC project risk analysis cases are described, followed by document pre-processing for unstructured data and NLP technology application cases.

### 2.1. EPC Project Risk Studies

In this study, the researchers initially focused on EPC risk definitions and databases to build a decision-making system by using the rules made in text mining techniques. This section summarized the literature review focused on identifying project risk through text mining.

Yu and Wang \[ [10](https://www.mdpi.com/1996-1073/14/15/4632#B10-energies-14-04632)\] tried to systematize the quantitative risk analysis by evaluating the contractor risk (11 types) of the EPC project using the interpretive structural modeling (ISM) method. Shen et al. \[ [1](https://www.mdpi.com/1996-1073/14/15/4632#B1-energies-14-04632)\] analyzed the contractor’s risk and the causes of the claims in the EPC projects through an EPC contractor case study in China and tried to verify that the EPC project risk is a direct influence factor of the claim by modeling structural equations. However, this study has a limitation of a small sample size for case studies. Kim et al. \[ [11](https://www.mdpi.com/1996-1073/14/15/4632#B11-energies-14-04632)\] developed a model (Detail Engineering Completion Rating Index System: DECRIS) to support the optimization of the construction schedule while minimizing the rework of EPC contractors during the offshore plant EPC project. They performed the project schedule, cost performance calculation, and validation for thirteen completed offshore projects in the DECRIS model. Mohebbi and Bislimi \[ [8](https://www.mdpi.com/1996-1073/14/15/4632#B8-energies-14-04632)\] presented a methodology for project risk management by studying parameters affecting EPC project risk and the general risk management model through an oil and gas plant project in Iran. Ullah et al. \[ [12](https://www.mdpi.com/1996-1073/14/15/4632#B12-energies-14-04632)\] established a theoretical framework by analyzing the causes of schedule delay and cost overrun of an EPC project. Gunduz and Maki \[ [13](https://www.mdpi.com/1996-1073/14/15/4632#B13-energies-14-04632)\] listed 39 attributes that negatively influenced the cost overrun of a construction project through a review of the project documentation. After that, these attributes were ranked through the Frequency-Cost Adjusted Importance Index (FCAII) technique.

As global demand for liquefied natural gas (LNG) rapidly increased as an energy source, Animah and Shafiee \[ [14](https://www.mdpi.com/1996-1073/14/15/4632#B14-energies-14-04632)\] reviewed risks of plant facilities such as floating production storage and offloading (FPSO) units, floating storage and regasification units (FSRU), LNG ships, and terminals. Son and Lee \[ [15](https://www.mdpi.com/1996-1073/14/15/4632#B15-energies-14-04632)\] applied text-mining technology to study the construction period prediction, key risk components of offshore EPC projects. Critical terms (CTs) were selected using the R program for the client’s technical specification (scope of work) document, and the Schedule Delay Risk Index (SDRI) of the project was prepared. The schedule delay was predicted through regression analysis. Son and Lee’s study can be used for the technical documents of the project bidding stage, but the conditions of the EPC main contract, where the project contract conditions are specified, were not included in the study subject. Chua et al. introduced a neural network technique to find key project management factors for successful budget performances of construction projects. Their study was an early case of applying a neural network model to a construction project and utilizing construction knowledge for solving schedule- and cost-related problems in construction sites \[ [16](https://www.mdpi.com/1996-1073/14/15/4632#B16-energies-14-04632)\]. Ho et al. proposed a Building Information Modeling-based Knowledge Sharing Management (BIMKSM) system that shares construction knowledge using Building Information Modeling (BIM) technology \[ [17](https://www.mdpi.com/1996-1073/14/15/4632#B17-energies-14-04632)\]. Sackey and Kim developed ESCONPROCS (expert system for construction procurement selection) to support decision-making on contract and procurement system selection in the construction industry based on extensive literature review \[ [18](https://www.mdpi.com/1996-1073/14/15/4632#B18-energies-14-04632)\]. Lee et al. developed an AI-based ITB risk management model to analyze ITB documents at the bidding stage of EPC projects \[ [19](https://www.mdpi.com/1996-1073/14/15/4632#B19-energies-14-04632)\]. Their model was implemented in the IBM’s Watson Explorer AI architecture environment, and a testbed was also built for the pilot study \[ [20](https://www.mdpi.com/1996-1073/14/15/4632#B20-energies-14-04632)\]. It was different from the research of our research team in that commercialized Application Programming Interface (API) was purchased and used for research.

### 2.2. Pre-Processing for Unstructured Data and Application of NLP Technology

In EPC projects, most documents, such as ITB, contract documents, and technical specifications, are composed of unstructured documents (e.g., numbers, units, text formats). The current status and trend of natural language processing (NLP) technology were reviewed in the field of pre-processing and analysis of unstructured data. NLP is an artificial intelligence (AI) technique that enables computers and humans to interact efficiently by providing a computer language and listener repertoire \[ [21](https://www.mdpi.com/1996-1073/14/15/4632#B21-energies-14-04632)\]. NLP is often used in the fields of information extraction (IE) and information retrieval (IR). IE refers to the process of extracting information that matches certain patterns by defining the type or pattern of information extracted in advance. IR is the task of finding the necessary information in a large repository of information, for example, a searching engine that searches for and ranks information according to user queries. NER for tagging people’s names or geographical names is one type of IR \[ [22](https://www.mdpi.com/1996-1073/14/15/4632#B22-energies-14-04632)\].

In 2016, Tixier et al. \[ [23](https://www.mdpi.com/1996-1073/14/15/4632#B23-energies-14-04632)\] proposed a framework to extract meaningful empirical data from a vast database of digital injury reports on construction site accidents. A model was built to analyze the text of the construction injury report using NLP. They also introduced methods of overcoming the decoding of unstructured reports and building a system through the repetition of coding and testing. Tixier et al. \[ [23](https://www.mdpi.com/1996-1073/14/15/4632#B23-energies-14-04632)\] used structured data as a prerequisite when applying statistical modeling techniques. Lim and Kim \[ [22](https://www.mdpi.com/1996-1073/14/15/4632#B22-energies-14-04632)\] sorted documents according to the contents of documents and used a text mining technique, which is also referred to as text analysis or document mining, for extracting meaningful information from documents. They classified major research fields of construction automation by keywords and summarized the most frequently cited studies in construction automation. However, due to the collection of papers in the National Digital Science Library, there was a limitation that some papers might be omitted when analyzing the number of citations. In 2014 Williams and Gong \[ [24](https://www.mdpi.com/1996-1073/14/15/4632#B24-energies-14-04632)\] proposed a model that combines numerical and text data of construction projects using data mining and classification algorithms and predicted the possibility of cost overrun when bidding on a project. They used a stacking ensemble model in predicting construction cost overruns.

Mrzouk and Enaba \[ [25](https://www.mdpi.com/1996-1073/14/15/4632#B25-energies-14-04632)\] analyzed the text of a construction project contract using text mining. By integrating project correspondence within BIM and monitoring project performance, they developed the Dynamic Text Analytics for Contract and Correspondence model, a text analysis model based on project correspondence. Their study showed a methodology for extracting meaningful patterns from construction project documents. Zoua et al. \[ [26](https://www.mdpi.com/1996-1073/14/15/4632#B26-energies-14-04632)\] introduced a search methodology through two NLP techniques (vector space model and semantic query expansion) for the effective extraction of risk cases from the construction accident case database. Li et al. \[ [27](https://www.mdpi.com/1996-1073/14/15/4632#B27-energies-14-04632)\] proposed NER’s unsupervised learning method using annotated texts in an encyclopedia. They stated that the approach to learning the NER model without manually labeled data shows better performance than the model fully trained with news source data.

After reviewing the cases and papers as described above, a lack of studies was revealed on systems that automatically extract and analyze the project risk from the letter of intent (LOI) and contract for the EPC project using ML. Therefore, this study focused on developing automatic risk extraction and analysis modules from the LOIs and contract documents provided by project owners for a machine learning-based decision-making system for EPC projects.

## 3\. Overview of Engineering Decision-Support System

In this study, a machine learning-based integrated decision-support system was developed to provide EPC contractors the maximized efficiency on risk analysis of EPC contracts.

The engineering decision-support system, Engineering Machine learning Automation Platform (EMAP), consists of three modules: (1) ITB Analysis, (2) Engineering Design, and (3) Predictive Maintenance, as shown in [Figure 1](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f001).

The Engineering Design sub-modules are Cost Estimate, Error Check, and Cost Change and Control. The cost estimate sub-module developed a design cost prediction model for estimating design time and cost by selecting variables and standardizing data through correlation analysis. The cost change and control check sub-module developed a prediction model that applied the scaling technique. The Cost Change and control check sub-module developed a prediction model that performed regression analysis by making the information of the existing project the variables.

Predictive maintenance is a module that develops a model for predicting maintenance and parts demand for equipment. Three types of analysis were performed: turbo fan engine, gearbox, and wastewater pump. The predictive maintenance module aims to provide a reference model after collecting data about the equipment. The prediction results for each reference model are visualized and implemented as a chart and presented in an integrated solution.

Considering the module characteristics and analysis types, various ML algorithm techniques, such as phrase/context-matching and random forest, were implemented in each analysis model. First, the ITB Analysis module analyzes ITB documents and identifies project risks in advance through machine learning-based automatic extraction of risk components and key parameters for ITB and contract documents. Second, the Engineering Design module selects variables through correlation analysis and standardizes information, so that it predicts project design time and cost estimates. Third, the Predictive Maintenance module predicts values of equipment such as turbofan engine, gearbox, and wastewater pump. This paper focused on the description of two sub-modules, Critical Risk Check (CRC) and Term Frequency Analysis (TFA) in the ITB Analysis module, and describes the detailed processes implementing NER and phrase matcher techniques in a syntactic analysis.

## 4\. Analysis Framework for ITB Module

The framework of the ITB Analysis module consists of the following five steps as shown in [Figure 2](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f002). The detailed description of each step is described in the following sections:

### 4.1. STEP 1: Collection of EPC Documents Subsection

The 25 EPC ITB documents were collected through the EPC contractors for various EPC fields such as offshore, onshore plants, and infrastructure projects for this study. In the 25 projects, the EPC ITB information was converted into 21,683 rows in a database (DB).

In the first step, a DB was created through a pre-processing step so that it could be used for risk analysis by converting complex sentences into short sentences. [Table 1](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t001), below, shows the list of the collected EPC ITB documents. The project titles were anonymized in consideration of the relationship with the project owners.

### 4.2. STEP 2: Structure of Database

Pre-processing data is a major step to improve the accuracy of the selected data by applying data-mining techniques. The result of pre-processing has a substantial influence on the analysis quality of the ITB documents. A Portable Document Format (PDF)-importing function was built to collect ITB documents as a sub-module in the ITB Analysis module. This function recognizes the text on PDF documents, creates a CSVfile containing the texts tagged with codes that indicate the text positions, and tracks the table of contents from the PDF documents.

Tagging the texts during the standardization stage enabled the module to find the sentences’ affiliation in the contract during the analysis result. In this study, the ITB documents were converted into a DB and used to develop an automatic risk extraction algorithm. [Table 2](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t002) shows an example of the exception of the EPC ITB document, and the following pre-processing steps were performed for accurate text recognition with Python programming \[ [28](https://www.mdpi.com/1996-1073/14/15/4632#B28-energies-14-04632)\]:

- First, recognize texts in page order on the ITB documents.

- Second, extract texts as sub-class each line and convert the text data into a CSV format.

- Third, add position codes to the line-based text contents in a CSV file.

- Fourth, convert capital letters to lower-case letters, tokenize words by classes, and eliminate stop words and white spaces.

Proper interpretation by experts was important because of the complex sentence structure (subject-verb-object: SVO), which is a common feature of project contract documents. Therefore, text-mining and NLP analysis techniques were applied for reducing errors and improving the machine’s ability to understand the context of the sentence. In the text analysis of the EPC ITB documents, errors were reduced, and meaningful analysis results were achieved by collaborating with SMEs and reviewing the systematic processes.

As a general pre-processing technology for text recognition, various computing technologies such as stop words removal, stemming, and the term frequency/inverse document frequency (TF/IDF) algorithms are used \[ [29](https://www.mdpi.com/1996-1073/14/15/4632#B29-energies-14-04632)\]. In the text pre-processing step, unnecessary or obstructive texts, such as stop-word, white-space, and delimiters, were deleted or corrected, and the smallest unit phrases were identified. This sentence simplification processes were necessary due to the sentence complexity in the EPC ITB documents.

Collectively changing the capital letters on the ITB documents to the lowercase letters improved the accuracy rate in rule tagging.

As shown in [Table 2](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t002), the sentences in the EPC ITB document were divided into titles, subheadings, and sentences. The title and subtitle were automatically recognized and processed as separate lines in Python programming. Each sentence was recognized and extracted based on the delimiters, such as (a), (b) or (i), (ii). [Table 2](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t002) shows the example of the position codes and the simple sentences after the pre-processing step.

Recognizing and classifying each sentence were intended to improve the recognition rate of risk keywords through the pre-processing step. Tagging risk keywords with complex sentences was not properly performed and showed low-performance results due to errors and omissions. It was important to define the breakpoints of sentences in the pre-processing step. Sentences are often separated by separators or periods, but special symbols such as (:) and (;) are also shown as a sentence separator. The various cases of sentence breakpoints were collected in the ITB documents collected for this study, and the case rule for sentence breakpoints was developed to resolve irregularities of separating sentences. The parser technique was applied in Python programming to analyze the sentence structures and define the relationship among phrases in complex sentences. The parser technique allows checking the grammar of a series of strings and building meaningful tokens with parse trees for further utilization \[ [30](https://www.mdpi.com/1996-1073/14/15/4632#B30-energies-14-04632)\].

Through the pre-processing step described above, 21,683 lines of text contents were generated in the DB from the ITB documents. The PDF application function analyzes each page of the PDF file imported and stores information in a metadata format. Once a PDF file is uploaded, a header section, a footer section, and watermarks are eliminated as shown in [Figure 3](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f003), and the text contents are stored in a CSV file.

[Table 3](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t003) shows an example of the table generated in the DB from the PDF application function in the pre-processing step. The table consists of four columns: project title, class, sub-class, and content. Class and sub-class are the title and the sub-title in the contents, respectively. Each sub-class is associated with one sentence, which is the smallest unit in the document structure.

In this study, automatic extraction and CSV (comma-separated values) file format were achieved so that the ITB documents can be broken up sentence by sentence by using the parser technique. A CSV file is an application document that uses plain text and is a file that is widely used. Rather than using the existing commercialized technology, the sub-module was developed with specialized customizations in EPC analysis. In addition, unstructured data, such as numbers, units, and text formats of scans and hard copies, were digitized by recognizing texts using the optical character recognition (OCR) technique. OCR is a technique that converts characters into simple text that can be scanned or analyzed by a machine \[ [31](https://www.mdpi.com/1996-1073/14/15/4632#B31-energies-14-04632)\]. It is a highly usable technology field that can generate information read by a machine as an output file. The digitized files are stored in the cloud using the marina DB service \[ [32](https://www.mdpi.com/1996-1073/14/15/4632#B32-energies-14-04632)\], and the cloud service was built from the viewpoint of user convenience in the field.

### 4.3. STEP 3: Development of Algorithm

This section briefly describes the CRC module and the TFA module. The CRC module uses a phrase-matcher, which is a rule-based technique for identifying risk clauses. The TFA module includes a machine learning algorithm for automatically extracting frequency in large amounts of data (so called ‘big data’). The detailed development processes for the CRC module and the TFA module are described in [Section 5](https://www.mdpi.com/1996-1073/14/15/4632#sec5-energies-14-04632) and [Section 6](https://www.mdpi.com/1996-1073/14/15/4632#sec6-energies-14-04632), respectively. Several advanced techniques, including text-mining, AI, machine learning, and information retrieval (IR), are applied in a complex interconnection to achieve the best performance of the application.

[Table 4](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t004) summarizes the technique, input data types, program language, and target result for both the CRC and the TFA modules. The AI technique was applied to the CRC module and the IR module was applied to the TFA module. AI is a system and infrastructure technology in which machines implement human capabilities (learning, reasoning, perception) as computer programs \[ [19](https://www.mdpi.com/1996-1073/14/15/4632#B19-energies-14-04632)\]. IR is a technology for searching or tagging information, and there is NER as a sub-technology \[ [33](https://www.mdpi.com/1996-1073/14/15/4632#B33-energies-14-04632)\].

The CRC module recognizes and standardizes the rules and automatically detects the events matching with the rules. The CRC module is useful to determine if a risk clause exists in the entire ITB document. The TFA module extracts the frequency of the risk clauses and similar syntaxes and identifies the risk that could not be found in the rule-based CRC modules. The TFA module presents the frequency of risk clauses and similar syntaxes to the user with visual outputs (charts and images). Both modules use the same file, but the output is a standardized CSV file for the CRC module. The TFA module provides a variety of image files, web format HTML, and table format CSV files. According to the purpose of the algorithm and technology, ITB Analysis was composed of three sub-analysis modules with several ML technologies for different purposes. It was divided into CRC, TFA, and NLP sub-modules with a syntactic approach, and each submodule provides algorithm development and solutions suitable for the analysis purpose.

#### 4.3.1. Critical Risk Check (CRC) Module

The Critical Risk Check (CRC) module detects risks according to specific rules using PhraseMatcher \[ [34](https://www.mdpi.com/1996-1073/14/15/4632#B34-energies-14-04632)\]. PhraseMatcher is a function of spaCy \[ [36](https://www.mdpi.com/1996-1073/14/15/4632#B36-energies-14-04632)\], a Python open-source library that extracts the terms related to user-specified rules. First, pre-processing was performed to separate the sentences of ITB using spaCy’s part-of-speech (POS) tagging and dependency parsing techniques prior to the main analysis. After pre-processing, ITB extracts risk clauses through CRC rules. For example, the rules were developed in this study to extract liquidated damages (LD), a key contract clause in ITBs. These rules were developed by analyzing the ITBs previously collected. The 35 CRC rules were configured from those EPC contracts. Among the list for CRC, Level 1 indicates major risk items in the contract, and Level 2 indicates the keywords’ associated risks, as Table 6 in [Section 5.1](https://www.mdpi.com/1996-1073/14/15/4632#sec5dot1-energies-14-04632) below shows ‘Liquidated Damages (LD)’ and the related keywords in the contract risk list for CRC. If a user wants to find a Level 1 risk clause called ‘Liquidated Damages’, the LD-related sentences are extracted when a sentence containing one of the keywords listed in Level 2 appears. When a user inputs the ITB to be analyzed into the CRC module, the sentence containing the keyword for the LD is extracted and presented through the CRC rule. If the relevant risk clause does not exist, ‘No detected message’ is printed and displayed on the module interface. The detailed development process is described in [Section 5](https://www.mdpi.com/1996-1073/14/15/4632#sec5-energies-14-04632).

#### 4.3.2. Terms Frequency (TFA) Module (M2)

The Terms Frequency Analysis (TFA) module, the second sub-module in the ITB analysis module, consists of an analysis module using spaCy’s NER model. The NER model learns the entity label from the collected sentence data and analyzes whether there is a keyword belonging to the entity label. It utilizes a statistical prediction technique pre-learned from the new data using the learned model \[ [37](https://www.mdpi.com/1996-1073/14/15/4632#B37-energies-14-04632)\]. The research team developed an algorithm that tags the position using the NER model, calculates the frequency, and generates a graph. For the TF analysis, the critical risk words in the EPC contract were first designated as NER level. After collecting the sentences with the corresponding level from the contract, it was written as a JavaScript Object Notation (JSON) file, which was used as training data for NER for learning entities. When a user enters the contract to be analyzed, the location of the learned entity and its frequency are analyzed, and the result is displayed as an HyperText Markup Language (HTML) file. A total of 21,683 sentences were collected from the contracts for the TF module in this study. This study implemented the TF algorithm using NER using Python. The detailed explanation is described in [Section 6](https://www.mdpi.com/1996-1073/14/15/4632#sec6-energies-14-04632).

### 4.4. STEP 4: Integrated Platform

A decision support system for EPC contract risk analysis was developed in this study. The purpose of the integrated platform was to enable users to analyze EPC contract risk on the web-based tool effectively. The cloud service of the integrated platform stores the data, analyzes it, and visualizes the results on the user’s computer screen.

After the risk clauses detected from the 25 ITB documents were identified and stored in the marina Database Management System (DBMS) \[ [32](https://www.mdpi.com/1996-1073/14/15/4632#B32-energies-14-04632)\], they are linked with the modules during the analysis. The EPC contract analysis decision support system is described in detail in [Section 7](https://www.mdpi.com/1996-1073/14/15/4632#sec7-energies-14-04632).

### 4.5. STEP 5: Case Analysis of the EPC Contracts

In STEP 5, the concept of risk in the EPC industry and the built lexicon were compared with the EPC risk database. The completed risk database and lexicon were used as a comparison database (DB) in which the algorithm model was built. A team of experts, with experience in bidding, contracting and performing multiple EPC projects, participated from the beginning of the development to plan and review the algorithm models during the framework stage. A case analysis of contracts obtained from the EPC contractor was conducted, and the rules were established through the concept of EPC risk and lexicon construction. The risk keywords commonly used in the EPC industry were grouped and established as a lexicon. A lexicon is also called a wordbook in linguistics, and a computing lexicon is a group of words created in a programming language (Python). Machine learning-based lexicons were developed and utilized in previous studies \[ [5](https://www.mdpi.com/1996-1073/14/15/4632#B5-energies-14-04632), [35](https://www.mdpi.com/1996-1073/14/15/4632#B35-energies-14-04632)\]. Lee, et al. analyzed FIDIC (International Federation of Consulting Engineers), an international standard contract, and defined problematic clauses that should not be missed and essential clauses that should not be omitted in the review process for overseas construction projects. They were named PCI (problems caused by included information) and PCNI (problems caused by not included information) to reflect the characteristics of risk determination \[ [5](https://www.mdpi.com/1996-1073/14/15/4632#B5-energies-14-04632)\]. Kang, el. extracted design information from the piping and instrumentation diagram document of the EPC industry and converted it into a database \[ [38](https://www.mdpi.com/1996-1073/14/15/4632#B38-energies-14-04632)\].

In the Risk Keyword Lexicons, built through collaboration with the EPC experts, the following are several examples:

- Liquidated damages (LD) are considered the most serious risk in EPC projects. LD can be classified into delay liquidated damages (DLD) or performance liquidated damages (PLD). In both cases, if the EPC contractor fails to meet the contract delivery date or does not meet the performance required by the contract, it is a contract clause that compensates the project owner for losses.

- PLD also has the risk of incurring losses of up to five percent of the total contract amount. If the contract delivery date is delayed due to reasons beyond the responsibility of the EPC contractor or the contract performance has not been met, the contract is deferred from the client, and the DLD or PLD will be judged based on the extended contract delivery date or revised contract performance. Therefore, from the standpoint of the contractor, the biggest risk of DLD and PLD is not only whether the requirements included in the ITB document for DLD and PLD are appropriate, but also how reasonable the client is to delay delivery or change performance beyond the responsibility of the EPC contractor.

- There are cases in which delays due to a project owner’s faults (design changes, various inspections/approvals, delays in decision-making, etc.) during the construction execution of the EPC contractor, or other reasons for various delivery extensions during construction, are not sufficiently recognized.

The research team conducted a study on the intersection rule through a comprehensive rule and a case study to selectively extract specific risks. In addition, in order to provide the application system integrator (SI) service to EPC contractors, the result of this research carried out, as a part of the project, also performs SI validation in addition to the validation stage. At the time of PoC validation of the ITB analysis module, it was conducted for DLD and PLD-related risks. The validation result is described in detail in [Section 8](https://www.mdpi.com/1996-1073/14/15/4632#sec8-energies-14-04632).

## 5\. ITB Analysis Module: Critical Risk Check (CRC) Sub-Module

The CRC module was developed to automatically detect the risk clauses, applying a machine learning algorithm. The process flow of the CRC sub-module is described in [Figure 4](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f004). First, an ITB document to be analyzed is uploaded to the Risk Extraction Algorithm module (A1). Second, the algorithm checks whether a clause with DB risk exists through the pre-processing process (A2). Third, the algorithm investigates the existence of risk and, if present, extracts the sentence or generates a notification that there is no result value if no risk rule in the DB is tagged (A3).

### 5.1. Risk Database of CRC Module

The CRC module enables the review of EPC ITB documents through the risk database established by the research team. By comparing the text of the target contract document with the risk database, the existence of EPC risk sentences was identified and extracted. The existence of risk can be identified when comparing the texts of the target contract with the Risk DB in the CRC module. The Risk DB is divided into the single rule (lower group) and the multi-rule (higher group). The single rule is 1:1 matching of rule and keyword. The intersection of the single rule was defined as the multi-rule.

In the CRC module, the risk rule is input in the form of a token in Python. For example, to extract word combinations in the form of “Token-1, Token-2, and Token-3”, \[Attribute-1: Token-1\], \[Attribute-2: Token-2\], \[Attribute-3: Token-3\] are entered into Python. The details can be specified by entering the appropriate attribute type in parentheses and set multiple attributes as needed. For example, a token called such liquidated damages is entered as \[Liquidated Damages: such liquidated damages\] in the single rule attribute called Liquidated Damages. In the EPC document, if there is a sentence with LD risk, as shown in [Table 5](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t005), it is possible to check the existence of a sentence through keyword tagging that is underlined instead of the entire sentence. According to the risk DB, when all keywords belonging to “Liquidated Damage”, “Date”, and “Fail” exist as the intersection in the contract text, it is defined as a Delay Liquidated Damage (DLD) clause label. The collected ITB documents were analyzed by the expert group, and based on the result of the judgment, the combination of attribute multi-rules was confirmed and converted into a DB. Detailed examples of the single rule and the multi-rule are presented in [Table 6](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t006) and [Table 7](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t007).

To extract the combination of LD in the ITB documents, five types of multi-labels were selected through collaboration with SMEs, as presented in [Table 8](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t008). There were ten or more keyword intersection combinations under each label.

Risk DB was constructed by borrowing the keyword established as a lexicon. The rules applied to the algorithm were constructed in the JavaScript Object Notation (JSON) format and used for analysis. The JSON file format is an open standard format commonly used when creating DB in computing technique research \[ [39](https://www.mdpi.com/1996-1073/14/15/4632#B39-energies-14-04632)\]. Therefore, the JSON format was appropriately used for the lexicon, having various text structures such as type, name, and terms. An example of an application is shown in [Figure 5](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f005).

### 5.2. Risk Detection with Phrase-Matcher

The CRC module analyzes the ITB document, automatically extracts the label and similar syntax, and presents it in a data frame format. An algorithm was developed using phrase-matcher technology to automatically analyze and extract risk rules in Python by embedding them. Phrase-matcher is one of the packages provided by spaCy and determines whether to match the token sequence based on the document. By using the Critical Risk Check module using the phrase-matcher technique, a large data list can be efficiently matched, and the matched patterns can be represented in the form of document objects \[ [34](https://www.mdpi.com/1996-1073/14/15/4632#B34-energies-14-04632)\].

The CRC module recognizes texts in the ITB document in a PDF format and detects the presence or absence of a keyword defined as a risk clause within the texts. The detected risk clause displays the original text, including the keyword, and is presented with the tagged keyword. The risk clause was converted into a DB and can be extended to the lexicon. In addition, if similar rules of various cases through rule-based analysis are embedded and expanded into a DB, a rule-based technology can relatively secure risk detection reliability.

### 5.3. Analysis Results of CRC Module

The result values were automatically classified and extracted in a CSV format according to the risk DB. The order of multi-label, single label, risk group, and sentence is automatically generated.

The content and the purpose of extraction of the header in [Table 9](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t009) are described here:

- Multi-label is a group of single label combinations and is extracted when all combinations are included.

- In a single label, the keyword is the risk that exists in the tagged document. For example, the risk keyword ‘failure’ was extracted, and ‘failure’ belongs to the single label of fail. It facilitates risk analysis by organizing the extracted keywords and the labels that belong to them and presenting them to users.

- A risk group can be defined as a clause with a specific rule when a specific combination is tagged among multi-label combinations. In addition to a straightforward keyword tagging for users, the research team defined criteria that can easily judge risks.

- Sentence extracts the risk statement existing in the ITB document as it is. The reason is to support the user’s intuitive analysis result analysis.

In [Table 9](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t009), Exclusive Remedy 1 (ER1) clause is a risk, which is defined as a clause on workers’ compensation. The DLD clause states that if damage (loss) caused by the EPC contractor’s schedule delay is compensated for by only DLD, further liability is exempted. If this DLD clause does not exist in the ITB document, it is exclusive remedy (ER) that there is a risk for the project owner to claim actual loss over the DLD due to actual (general) damage. ER risk can be a risk that cannot be easily detected during EPC analysis by a junior engineer with little project experience.

A file in the CSV format, as shown in [Table 9](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t009), based on the final result standard of the CRC module’s risk DB and algorithm, is created. Through the risk group presented in the results, even users with little experience in performing EPC contracts can check whether the risk exists or not. SI can be used as a report for decision-making by checking and downloading the standardized analysis results on the web page, as shown in [Figure 6](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f006).

## 6\. ITB Analysis Module: Terms Frequency Analysis (TFA)

NER is a technique that recognizes, extracts, and classifies an entity corresponding to a project owner, place, or time from a document through a dictionary definition \[ [37](https://www.mdpi.com/1996-1073/14/15/4632#B37-energies-14-04632)\]. NER is actively used in NLP technology and IR. The EPC risk labels used in the TFA were selected through collaboration with the SMEs, and the labels are composed of similar keywords as shown in [Table 10](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t010). The TFA module collects risk data and creates and utilizes a training model to perform analysis. It is the task of the TFA module to build a training model specialized for EPC risk and implement the tagged frequency value in the algorithm model. The TFA process is shown in [Figure 7](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f007), and the process is as follows:

- B1: Upload the ITB document to be analyzed.

- B2: Based on the risk DB, the document is analyzed in the NER model to which the NER package is applied.

- B3: Through model analysis, risk entities are tagged, and frequency is extracted.

- B4: The extracted results are visualized and presented as a frequency chart, a HTML rendering file, and a word cloud.

The collected EPC risk data are generated as training data in the JSON format. The module was completed by learning JSON training data in the NER package. The prototype of the NER model used spaCy’s ‘en\_core\_web\_sm’ model and was completed by customizing it to fit the EPC risk through validation. The ‘en\_core\_web\_sm’ model is one of the libraries provided by spaCy and provides a pipeline optimized for English sentences \[ [35](https://www.mdpi.com/1996-1073/14/15/4632#B35-energies-14-04632)\]. It is possible to recognize basic written text such as blogs, news, comments, vocabulary, and entities type by using technologies such as tok2vec, tagger, lemmatizer, and parser. Various modules exist and serve a similar purpose (‘en\_core\_web\_md’, ‘en\_core\_web\_lg’, ‘en\_core\_web\_trf’). When the EPC ITB document to be analyzed is uploaded to the completed model, the analysis result is extracted according to the model learning result, and a graph is generated by calculating the frequency of the entity. In addition, when interworking with the service platform, the model was saved in pickle format to provide accurate analysis values. Python’s pickle implements a binary protocol of object structure to store and retrieve data with a small capacity \[ [40](https://www.mdpi.com/1996-1073/14/15/4632#B40-energies-14-04632)\].

### 6.1. Risk Database of TF Module

NER learning data were constructed by selecting sentences for risk clauses from 21,683 lines of sentences collected in the ITB documents. The NER learning data set was created as a JSON file, and 14 kinds of NER learning data JSON files were embedded in the integrated analysis system.

As shown in [Table 10](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t010), EPC risk data start with training data consisting of eight similar phrases, such as ‘fit for purpose.’ Similar phrases include plural and singular, and as a result of analyzing the collected EPC ITB documents, they were grouped in the form of family keyword by applying the sentence format commonly used in contracts.

The process of generating NER learning data goes through the following three steps:

- Risk DB classifies only fit for purpose-related sentences from the ITB documents collected from the EPC contractor. In the sentence, the expert filters whether the EPC contractor’s liability risk exists or not, and if there is no risk, the plaintext case is excluded.

- Assign a risk entity to each sentence. An example would be the sentence “Contractor warrants that the Plant will be fit for the purpose”. In this example sentence, **fit for the purpose** belongs to the risk label. Risk entities start from the 43rd and belong to the 62nd character, so the string numbers are assigned as “43” and “62”. The computing character counting method starts with 0 from the first digit.

- Each sentence’s given entities are structured as a JSON file. As shown in [Table 11](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t011), sentence: contract sentence, entities: risk word, and the label are listed in order. By being given as the standard of EPC risk data, it is possible to tag a keyword that has an entity similar to the training data (not learned, but similar to the training data) according to the learning result.

The NER learning data, created through the process described in [Figure 7](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f007), are grouped under a group name called Label. In this study, a total of 14 labels applied to the TFA module are shown in [Table 12](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t012) below. For the NER label, a keyword was selected in consideration of discrimination according to the application of the NER model through collaboration with SMEs. Each label consists of at least 50 to 200 sentences of collected data. When analyzing the TFA module, the model was saved in the pickle format to exclude the phenomenon of biased learning effect according to the data rate, and the saved model was linked to the cloud.

### 6.2. Calibration of the NER Model

Since the spaCy library provides only the model learned about the general object name, it is necessary to define the document’s contractor risk and apply it to the model \[ [35](https://www.mdpi.com/1996-1073/14/15/4632#B35-energies-14-04632)\]. SpaCy’s ‘en\_core\_web’ model shows the performance of Precision: 0.86, Recall: 0.85, and F-score: 0.86 in NER task \[ [37](https://www.mdpi.com/1996-1073/14/15/4632#B37-energies-14-04632)\]. The research team obtained, calibrated, and applied the model’s parameter values, epoch and batch size, which are described in detail below.

In ML, hyperparameters are used to control the learning process \[ [41](https://www.mdpi.com/1996-1073/14/15/4632#B41-energies-14-04632)\]. Examples of hyperparameters are learning rate and mini-batch size. The time required to train and test the model may vary depending on the hyperparameters. Random numbers generated in a computer program generate a sequence that appears to be random by means of an algorithm determined by the computer. The starting number of a random sequence is called a seed. Once generated, the random seed becomes the seed value for the next generation. In this study, the following values were determined by fixing the random seed (see [Table 13](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t013)). The setting was fixed to the test value that gave the optimal result suitable for EPC risk:

- Epoch: In ML processes, the algorithm goes through each process from input to output using parameters, and epoch 1 can be seen as it completing the entire dataset once. Epoch = 1 means that the whole data set was used once and learned.

- Batch size: The sample size of data given per mini-batch is called batch size. In most cases, due to memory limitations and slowdown in speed, the data are divided into one epoch. The loss derived by inputting each datum of the mini-batch into the model is calculated, and the gradient value of the average of this loss is calculated and updated to the weight. The batch size gradually increases with epoch K, up to a maximum of 256.

- When epoch is K, Batch size, B(K), is expressed as Equation (1):

B(K)={256(K≥log1.014+1)32×(1.01)k−1(K<log1.014+1)

(1)

- Optimizer: As the stochastic gradient descent (SGD) algorithm, it finds the optimal weight while adjusting the weight in the opposite direction to the gradient direction of the current weight.

- Learning rate: A coefficient that multiplies the gradient value when adding the gradient value of each layer calculated through the loss function and back propagation to the existing layer.

- Dropout: Dropout refers to a technique to reduce the amount of computation and overfitting by inactivating some random nodes among all nodes of the neural network. The dropout rate value means the ratio of the nodes to be deactivated among the nodes of the entire neural network.

### 6.3. Analysis Results of TFA Module

By using the visualized model analysis result, the risk severity on the EPC project can be estimated to have an impact. The label and keyword frequency were automatically extracted and imaged, and the output types were expressed in three ways as follows:

- Frequency (bar chart): Automatically generated in graph format by calculating the existence and frequency of labels ( [Figure 8](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f008) a).

- Word Cloud Image: Automatic extraction of frequency and importance through co-word analysis ( [Figure 8](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f008) b).

- HTML file with rendering technique: Highlight and display on the web page ( [Figure 8](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f008) c).

[Figure 8](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f008) is the result of ‘I-1 project’ applied to the pilot project among the ITB documents, and the pre-learned entity was statistically converted through a complete model analysis and was automatically extracted as an image file. If we look at the bar chart in [Figure 8](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f008) a, we can see that the frequency of the Law label is tagged 62 times. Similar phrases learned in the Law label include governing law and applicable law, and local law that was not learned in the I-1 project result was additionally tagged. As such, it was verified that the appropriate EPC risk was extracted by analyzing the articles tagged in the validation step. In [Figure 8](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f008) b, word cloud result is also called tag cloud, and it means a structure that is visually arranged in consideration of importance, popularity, alphabetical order, etc., by analyzing the result values obtained from metadata. Each label, resulting from the term’s frequency result and the frequency of similar phrases, was converted into a word cloud and used as visual result data. [Figure 8](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f008) shows an example of (c) an HTML file with rendering technology application. It is possible to highlight using the rendering function by entity tagging through the learning model. By converting the ITB document into a text file, a user can highlight words tagged as EPC risk and specify the risk group together to generate a resulting value.

## 7\. System Integration and Application

In this study, a machine learning-based integrated decision-making support system as a cloud-service platform, EMAP, was developed to maximize the convenience of EPC contractors based on the current research results on EPC risk analysis. The integrated system is composed mainly of three modules (ITB Analysis, Engineering Design, Maintenance Analysis). Rather than simple integration, it was designed to build and operate an information system that meets the purpose. This research team referred to GE Predix and DNV’s Veracity platform examples for system configuration \[ [42](https://www.mdpi.com/1996-1073/14/15/4632#B42-energies-14-04632), [43](https://www.mdpi.com/1996-1073/14/15/4632#B43-energies-14-04632)\].

### 7.1. Features of IT

NLP is a field of artificial intelligence where machines understand and respond to human language systems to help human activities \[ [44](https://www.mdpi.com/1996-1073/14/15/4632#B44-energies-14-04632)\]. In order to effectively utilize this key technology, the selection and use of a digital assistant are important. Python has the advantage of being concise and highly productive among programming languages. As it is the most used in the world, it has many useful libraries. Due to these characteristics of Python, Python was mainly used for algorithm development. SpaCy is an open-source software for advanced natural language processing written in a programming language (Python or Cython) \[ [28](https://www.mdpi.com/1996-1073/14/15/4632#B28-energies-14-04632), [45](https://www.mdpi.com/1996-1073/14/15/4632#B45-energies-14-04632)\]. Additionally, spaCy provides libraries for numeric data and text processing \[ [44](https://www.mdpi.com/1996-1073/14/15/4632#B44-energies-14-04632)\]. In this study, PoC was implemented as an algorithm module by borrowing spaCy libraries of Python.

This research team developed an ITB analysis module for EPC risk analysis by building an EPC risk extraction algorithm based on Python packages. In addition, it was embedded in a cloud-based integrated decision support platform through collaboration with a professional solution company with an independently developed machine learning engine \[ [46](https://www.mdpi.com/1996-1073/14/15/4632#B46-energies-14-04632)\]. As shown in [Figure 9](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f009), the integrated platform is divided into three modules (ITB Analysis, Engineering Design Analysis, Predictive Maintenance), and each module has an algorithm function suitable for the purpose of analysis. HTML, Cascading Style Sheet and JavaScript were used to develop the integrated platform.

The integrated platform of this study was named Engineering Machine learning Automation Platform (EMAP), and it was based on a software as a service (SaaS) service that can be immediately used by providing an application solution. Oracle, one of the world’s largest software companies, provides integrated services by dividing cloud services into SaaS, platform as a service (PaaS), and infrastructure as a service (IaaS) \[ [47](https://www.mdpi.com/1996-1073/14/15/4632#B47-energies-14-04632)\]. The database management system (DBMS) constructed in this study allows authorized users to access the DB through the server. By constructing an accessible DBMS, extensibility is given so that clients can use ‘user functions.’ The implementation of the ‘user management function’ made it possible to use the previously embedded DB structure as a new data set by assigning each user-id as a default and copying the modified default value. Through open-source MySQL DBMS, a local server was created, connected, and built to connect to the developed Python package DB. Oracle’s MySQL is the world’s most widely used relational DB management system \[ [48](https://www.mdpi.com/1996-1073/14/15/4632#B48-energies-14-04632)\].

The purpose of the integrated platform is to maximize user convenience on the web. The cloud service, applied in the integrated platform, stores the data, analyzes it, and visualizes the results within the platform so that the user can easily check it on the screen.

### 7.2. SI of ITB Module

SI can be defined as the overall process of developing a platform. Based on the algorithm described in [Section 5](https://www.mdpi.com/1996-1073/14/15/4632#sec5-energies-14-04632) and [Section 6](https://www.mdpi.com/1996-1073/14/15/4632#sec6-energies-14-04632), a system for each module was constructed as shown in [Figure 9](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f009) above. If a user clicks ITB analysis on the integrated platform, a user can see five sub-module menus, as illustrated in [Figure 10](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-f010). The CRC and TFA modules are the parts covered in this study. The package of each sub-module is linked to the cloud-integrated solution, and it can be extended to an administrator account.

In addition, to increase user utilization, the system is configured so that the user can add the desired rule on the final screen. Along with the existing risk DB accumulated through collaboration with an expert team, it provides a function that can be applied to risk analysis by adding arbitrary keywords and labels that the user needs.

Extensibility was achieved with a DB construction and the addition of user management functions. A user can upload and read the Excel format file on the User Interface (UI), apply the rules, and view the results in the existing analysis module. In addition, by conducting a software validation test in the process of implementing the system, errors or bugs that occurred during execution by developers and prospective users were reflected in advance.

## 8\. ITB Analysis Module Validation through PoC

This section describes the validation process and results of the developed modules (CRC and TFA). Module validation was conducted to confirm the applicability of the modules for risk analysis in an actual EPC project. In order to evaluate the reliability and accuracy of the module, the expert group evaluated the ITB documents used in the module development. By engaging experts with specialized knowledge and execution experience from the beginning of development to discuss development ideas for modules and evaluate the analysis results, it was made to be a practical and unbiased validation.

### 8.1. Definition of Validation Method

The purpose of the module validation was to check whether the modules extract accurate information by converting the unstructured information of the ITB documents into the filtered data format in the DB. The PoC method approach was used to evaluate the quantitative level of the review results. In other words, the performance results (risk detection accuracy and time efficiency) executed by the machine learning-based automatic risk extraction modules (CRC and TFA) were compared with the evaluation results from the EPC project engineers. The verification methodology followed the processes introduced by Lee et al. \[ [5](https://www.mdpi.com/1996-1073/14/15/4632#B5-energies-14-04632)\] and Kang et al. \[ [38](https://www.mdpi.com/1996-1073/14/15/4632#B38-energies-14-04632)\].

First, two engineers with experience in performing at least one EPC project participated as the main body of PoC implementation. As the analysis target project, ‘I-1 project (FPSO\_Australia)’ was applied equally to the CRC module and the TFA module. SMEs with more than 15 years of experience participated in the verification of PoC performance results (TPV\_Third Party Verification). As shown in [Table 14](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t014), the SMEs participating in the validation process have experience in performing a number of EPC projects in bidding and contracting. PoC proceeded sequentially according to the following four steps:

- Distributed the ‘I-1project’ document (PDF) to two engineers and received replies within a limited period (3 days). In order to derive mutually independent results without mutual interest, data sharing and result replies were conducted individually.

- Conducted cloud-based module analysis using development modules (CRC and TFA) with the same materials distributed to the engineers (‘I-1project’ contract and selection rules).

- The analysis results and system module analysis results performed by the engineer were delivered to SMEs to evaluate and verify the analysis process and contents. The review process for the development module was conducted in a non-face-to-face manner, and the review process was conducted individually by each expert so that independent verification could be made.

- The research team summarized the quantitative evaluation results by converting the SMEs analysis results based on their own knowledge and project execution experience into numerical values.

A validation evaluation index was used to quantify the results. The evaluation index was divided into variables called True Positive (TP), False Positive (FP), and Total Risk, and the risk extraction accuracy of each module was quantitatively evaluated by calculating the numerical value using the above three variables. The validation accuracy calculation formula is as shown in Equation (2).

- TP: the risk sentence is extracted as risk.

- FP: the risk sentence was not extracted.

- Total Risk: total risk (TP + FP) for an ITB or contract document of a project.

Accuracy = TP/(TP + FP)

(2)

### 8.2. Model Validation Results

#### 8.2.1. CRC Module Validation

To verify the CRC module, PoC was conducted by selecting “LD”, one of the risk keywords that can have a huge impact on the project if it occurs during bidding or execution of the EPC project. LD is a clause that the EPC contractor must pay to the ordering party when the contract delivery date is not met, or the performance required by the contract is not met. It can be divided into DLD or performance liquidated damages (PLD). In addition, EPC risk was divided into single rule and multi-rule. The single rule in the CRC module means risk keyword, and multi-rule is the intersection of every single rule. Therefore, 20 keywords of single rule and LD, which is a representative multi-rule, were selected as analysis targets. Twenty single keyword types can be seen in [Table 15](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t015).

The CRC module analysis process is as follows. First, a bidding specification (I-1project) is selected. Then, the prepared bid specification is uploaded to the CRC module. After performing the analysis, the number of risk detections is quantified numerically. The CRC accuracy evaluation results are shown in [Table 16](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t016).

- Single Rule: When comparing the CRC module analysis results as shown in [Table 16](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t016), the engineer risk extraction accuracy (100%) is relatively higher than the machine learning-based CRC automatic extraction module accuracy (89%). However, the engineer extracts 120 sentences with EPC risk, whereas the CRC module detects 230 sentences, so the module has a relatively high risk detection capacity. In addition, 205 sentences out of the 230 sentence extraction results of the SMEs verification result module were verified as TP. An example sentence in [Table 17](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t017) below is judged by SMEs as FP. SMEs suggested that the sentence belongs to the Definition chapter of the EPC ITB document and is simply a sentence that defines the term Contract Price. The difference between the risk sentence extraction results of the Engineer and the CRC module is the time limit and the large number of documents. The developed algorithm module is capable of extracting risk sentences by screening a large amount of text in a short time, but an omission occurred because the engineer reviewed the entire document within a limited time. In addition, it was found that some differences occurred in the result values of risk sentence judgment due to personal experience and subjective judgment among POC performing engineers.

- Multi-rule: As shown in [Table 16](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t016), the engineer extracted 28 sentences with EPC risk, whereas the CRC module detected 36 sentences. As a result of SMEs’ verification, 34 sentences were verified as TP. An engineer can see that the risk keyword detection accuracy (82%) drops by detecting only 28 out of 34 LD risk sentences verified by SME. Additionally, the module accuracy of the multi-rule (94%) is higher than the module accuracy of the single rule (89%). The multi-rule is an intersection of risk keywords, and although the number that exists in one project is small, it is selective and has higher accuracy.

#### 8.2.2. TFA Module Validation

First, for the verification of the TFA module, the target label was selected as damage (including LD and DLD), and the phrase label, FFP (Fit for Purpose), was selected through expert collaboration. Based on the target label, an accuracy evaluation of risk detection was performed for the module. Since the NER module is a technique for extracting keywords defined as entities such as people, regions, and organizations, the extracted target is defined as Keywords. The analysis process is similar to the verification process of the CRC module, and the accuracy results are shown in [Table 18](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t018) below.

When comparing the analysis results of the TFA risk module, the machine learning-based automatic TFA risk extraction model can significantly reduce the risk extraction rate and the time required for EPC risk analysis (see [Table 18](https://www.mdpi.com/1996-1073/14/15/4632#energies-14-04632-t018)). The engineer analysis result was 82 for the Damages label and 4 for the FFP label. In the TFA Module, 98 and 6 were tagged, respectively, and 8 and 1 keywords were determined as FP, respectively. The module validation results of each target label are 92% and 83%, respectively. Although 82 and 4 were extracted from the engineer validation, respectively, the keywords determined as FP as a result of the module validation were 90 and 5, and the engineers’ analysis result accuracy was 91% and 80%, respectively

As a result of examining the keyword determined by FP by an expert, it can be determined that it is not related to the target label. The main cause is the incompleteness of the knowledge-based learning model, which requires machines to understand human language. In order to minimize FP tagging errors, continuous expansion of learning data and advancement of machine learning functions through repetitive learning are required.

## 9\. Conclusions

This paper proposes the technology to check the existence of risk clauses for the ITB documents that require prior analysis when bidding or executing EPC projects and to detect and manage project risk sentences. Accordingly, two algorithm modules were developed for automatic risk extraction and analysis in the EPC technical specification based on ML techniques. In the CRC module, EPC risk-related clauses were defined, and the rules were selected by structuring it in a lexicon and embedded in the CRC module. An automatic risk detection function was developed to find the risk specified in the lexicon from the collected DB. The TFA module collects and rearranges EPC risk sentences to build a learning data set and constructs the NER model through individual learning of EPC risk sentences. The ITB document was analyzed using a pre-learned model, and the frequency of EPC risk was calculated, so that it could be used as a decision support tool. Therefore, this study performed the model development work according to the following steps. First, the model collected ITB documents and classified them by risk types. 25 EPC projects, previously conducted from EPC companies, were collected, and risk sentences (21,683 lines) were classified by risk type. These sentences were used as basic data for model development.

Second, the research team developed an algorithm and model that can detect major risks of contracts through natural language processing of sentences included in the ITB documents. The data preprocessing and algorithm step removes unnecessary data, and its logic was configured with ML, according to the characteristics of the two modules. Risk detection technology was developed through keyword grouping by applying NLP’s phrase-matching technology to the CRC algorithm. In the case of the TFA algorithm, it can be used as an analysis tool by analyzing the ITB document using a pre-learned model and calculating the frequency of the EPC risk. In the system application stage, the algorithm was dash-boarded on the ML platform to visualize the analysis results. When the pattern of sentences in the ITB document matches the developed rules, the mechanism for extracting information is activated. The model is implemented using Python, and automatically extracts and reviews risk sentences when the user enters the ITB document. This supports the users’ decision-making by viewing the model results. In addition, a user function has been added so that the model reflecting the rules desired by the user can be analyzed. The developed model is presented as a cloud-based integrated decision support platform, EMAP, considering user convenience.

Third, to enhance and verify the reliability of the developed model performance, collaboration with EPC project experts was conducted from the beginning of development, and the model performance and usability were reviewed by the experts. The experts who participated in the validation have experience in performing a number of EPC projects and allow independent validation to be performed. As a result of the pilot test, the CRC module-based risk sentence extraction accuracy result was 92%, and the TFA module-based risk sentence extraction accuracy result was 88%, whereas the engineer’s risk sentence extraction accuracy result was 70% and 86%, respectively. This is the result of risk extraction of the model reflecting some types of errors found in the validation process. The model extraction results show higher performance than the results detected by PoC subjects (engineers), and the time required for analysis is also significantly different. According to the validation conducted in this study, the ITB document analysis is prone to deviations depending on the capabilities of each manager or engineer. The significance of this study can be summarized in two ways. The first is that a technical system has been established to support the ITB document risk sentence detection task more effectively. Second, a model capable of preemptive risk management based on ML was developed. It automatically extracts major risks by incorporating machine learning technology into an analysis algorithm and presents them in an evaluation index.

By applying various AI technologies in the EPC field, the research team developed a scientific tool to automatically identify risk clauses that engineers are likely to miss, reducing potential risks to contractors and significantly shortening contract review time. In this process, it was confirmed that AI and ML technology were successfully applied to the EPC field.

## 10\. Limitation and Future Work

Despite the above study results, there are still some areas that need improvement when conducting related studies in the future. First, a rule that defines and embeds keyword risk needs to be improved at the level of a syntactic structure by targeting the conditions of a contract in the ITB document analysis procedure. Although the level of risk detection accuracy of the CRC module is stable, there are some areas in which unexpected errors or typos are not completely screened, other than the standard that is practically universal. For example, in the case of LD risk sentence validation, the degree of the ratio increased sharply in the single keyword sentence analysis, as was judged as an FP sentence among the module results. By analyzing multiple rules at once, they are extracted with a higher percentage of plain text or meaningless sentences. Continuous and elaborate knowledge-based rule updates are required to extract sentences that contain EPC Risk Keyword in the sentence. Accordingly, the authors will continue to conduct research to improve the reliability of analysis through linking NLP technology and technology updates that automatically pre-process documents in an atypical state.

Second, evaluating the recognition rate for automatic extraction of the TFA module, there are cases in which similar phrases are incorrectly tagged in the case of a label with insufficient learning. To reduce these errors, learning and training through big data are necessary, which is a common problem in the rule-based information extraction model. To overcome this, there is a need for continuous updates. The lexicon is continuously expanding, data on various types of ITB documents are constructed, and the rules are implemented through ML. In future research, it is expected that the universality of the integrated platform can be secured through the introduction of advanced technologies and the expansion of training data through the collection of extensive ITB documents not only in the plant field but also in other industries.

Third, in this study, it was implemented through the construction of a lexicon including the contracts and the keywords in English only. In order to apply to another language in addition to English, further processes are necessary to collect contracts in the corresponding language, establishing the keywords and the rules in the database in the corresponding language, although the AI and ML technique would still work. The expected difficulty is that in addition to the existing English contract, it is necessary to collect data for the corresponding language, and when recognizing the texts from the contract through the program, the development of a recognition algorithm for each language should proceed.

Fourth, apart from this study, this research team is conducting research on the automatic risk extraction model through semantic analysis and the knowledge-based automatic risk extraction model for technical specifications. When construction of the individual modules is combined into an integrated ML decision support platform (Engineering Machine learning Automation Platform: EMAP) (to be completed in 2021), it will be able to provide practical direct and indirect benefits to EPC contractors.

## Author Contributions

The contribution of the authors for this publication article are follows: conceptualization, S.J.C. and E.-B.L.; methodology, S.J.C., S.W.C. and E.-B.L.; software, S.J.C. and S.W.C.; validation, E.-B.L. and J.H.K.; formal analysis, S.J.C. and S.W.C.; writing—original draft preparation, S.J.C.; writing—review and editing, J.H.K. and E.-B.L.; visualization, S.J.C. and S.W.C.; supervision, E.-B.L.; project administration, E.-B.L.; and funding acquisition, E.-B.L. and J.H.K. All authors have read and agreed to the published version of the manuscript.

## Funding

This research was funded by the Korea Ministry of Trade Industry and Energy (MOTIE) and the Korea Evaluation Institute of Industrial Technology (KEIT) through the Technology Innovation Program funding for “Artificial Intelligence and Big-data (AI-BD) Platform Development for Engineering Decision-support Systems” project (grant number = 20002806).

## Institutional Review Board Statement

Not applicable.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

Not applicable.

## Acknowledgments

The authors would like to thank Kim, C.M. (a senior researcher at University of California—Davis) for his academic feedback on this paper, Lee, S.Y. (a senior researcher in POSTECH University) for his support on the manuscript editing work, Baek, S.B. (a graduate student in POSTECH University) for his assistance to Python coding, and Kim, C.Y. (a graduate student in POSTECH University) for her help on the manuscript revision. The views expressed in this paper are solely those of the authors and do not represent those of any official organization.

## Conflicts of Interest

The authors declare no conflict of interest.

## Abbreviations

The following abbreviations and parameters are used in this paper:

|     |     |
| --- | --- |
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| CRC | Critical risk check |
| CSV | Comma-separated values |
| CT | Critical Term |
| DBMS | Database Management System |
| DLD | Delay Liquidated Damage |
| EMAP | Engineering Machine learning Automation Platform |
| EPC | Engineering, Construction, and Construction |
| ER1 | Exclusive Remedy 1 |
| FP | False Positive |
| HTML | Hyper-Text Markup Language |
| IaaS | Infrastructure as a Service |
| IE | Information Extraction |
| IR | Information Retrieval |
| DBMS | Database Management System |
| ITB | Invitation to bid, invitation for bid or sealed bid |
| JSON | JavaScript Object Notation |
| LDs | Liquidated Damages |
| NER | Named Entity Recognition |
| NLP | Natural language processing |
| OCR | Optical Character Recognition |
| PaaS | Platform as a Service |
| PLD | Performance Liquidated Damages |
| PoC | Proof-of-concept |
| SaaS | Software as a Service |
| SI | System Integrator |
| SMEs | Subject-Matter Experts |
| TF | Terms Frequency |

## References

01. Shen, W.; Tang, W.; YU, W.; Duffield, C.F.; Hui, F.K.P.; Wei, Y.; Fang, J. Causes of contractors’ claims in international engineering-procurement-construction projects. J. Civ. Eng. Manag. **2017**, 23, 727–739. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Causes+of+contractors%E2%80%99+claims+in+international+engineering-procurement-construction+projects&author=Shen,+W.&author=Tang,+W.&author=YU,+W.&author=Duffield,+C.F.&author=Hui,+F.K.P.&author=Wei,+Y.&author=Fang,+J.&publication_year=2017&journal=J.+Civ.+Eng.+Manag.&volume=23&pages=727%E2%80%93739&doi=10.3846/13923730.2017.1281839)\] \[ [CrossRef](https://doi.org/10.3846/13923730.2017.1281839)\]
02. Du, L.; Tang, W.; Liu, C.; Wang, S.; Wang, T.; Shen, W.; Huang, M.; Zhou, T. Enhancing engineer–procure–construct project performance by partnering in international markets: Perspective from Chinese construction companies. Int. J. Proj. Manag. **2016**, 34, 30–43. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Enhancing+engineer%E2%80%93procure%E2%80%93construct+project+performance+by+partnering+in+international+markets:+Perspective+from+Chinese+construction+companies&author=Du,+L.&author=Tang,+W.&author=Liu,+C.&author=Wang,+S.&author=Wang,+T.&author=Shen,+W.&author=Huang,+M.&author=Zhou,+T.&publication_year=2016&journal=Int.+J.+Proj.+Manag.&volume=34&pages=30%E2%80%9343&doi=10.1016/j.ijproman.2015.09.003)\] \[ [CrossRef](https://doi.org/10.1016/j.ijproman.2015.09.003)\]
03. Nurdiana, A.; Susanti, R. Assessing risk on the engineering procurement construction (EPC) project from the perspective of the owner: A case study. In Proceedings of the IOP Conference Series: Earth and Environmental Science, Surabaya, Indonesia, 1–2 October 2020; Volume 506, p. 012040. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Assessing+risk+on+the+engineering+procurement+construction+(EPC)+project+from+the+perspective+of+the+owner:+A+case+study&conference=Proceedings+of+the+IOP+Conference+Series:+Earth+and+Environmental+Science&author=Nurdiana,+A.&author=Susanti,+R.&publication_year=2020&pages=012040&doi=10.1088/1755-1315/506/1/012040)\] \[ [CrossRef](https://doi.org/10.1088/1755-1315/506/1/012040)\]
04. Doloi, H.; Sawhney, A.; Iyer, K.C.; Rentala, S. Analysing factors affecting delays in indian construction projects. Int. J. Proj. Manag. **2012**, 30, 479–489. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Analysing+factors+affecting+delays+in+indian+construction+projects&author=Doloi,+H.&author=Sawhney,+A.&author=Iyer,+K.C.&author=Rentala,+S.&publication_year=2012&journal=Int.+J.+Proj.+Manag.&volume=30&pages=479%E2%80%93489&doi=10.1016/j.ijproman.2011.10.004)\] \[ [CrossRef](https://doi.org/10.1016/j.ijproman.2011.10.004)\]
05. Lee, J.H.; Yi, J.S.; Son, J.W. Development of automatic-extraction model of poisonous clauses in international construction contracts using rule-based NLP. J. Comput. Civ. Eng. **2019**, 33. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Development+of+automatic-extraction+model+of+poisonous+clauses+in+international+construction+contracts+using+rule-based+NLP&author=Lee,+J.H.&author=Yi,+J.S.&author=Son,+J.W.&publication_year=2019&journal=J.+Comput.+Civ.+Eng.&volume=33&doi=10.1061/(ASCE)CP.1943-5487.0000807)\] \[ [CrossRef](https://doi.org/10.1061/(ASCE)CP.1943-5487.0000807)\]
06. Korea Agency for Infrastructure Technology Advancement. 2013 General Report on the Analysis of Technology Level of Land Transportation (KAIA); Korea Agency for Infrastructure Technology Advancement: Anyang, Korea, 2013.
07. Gunduz, M.; Yahya, A.H.A. Analysis of project success factors in construction industry. Technol. Econ. Dev. Econ. **2015**, 24, 67–80. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Analysis+of+project+success+factors+in+construction+industry&author=Gunduz,+M.&author=Yahya,+A.H.A.&publication_year=2015&journal=Technol.+Econ.+Dev.+Econ.&volume=24&pages=67%E2%80%9380&doi=10.3846/20294913.2015.1074129)\] \[ [CrossRef](https://doi.org/10.3846/20294913.2015.1074129)\]
08. Mohebbi, A.H.; Bislimi, N. Project Risk Management: Methodology Development for Engineering, Procurement and Construction Projects a Case Study in the Oil and Gas Industry. Master’s Thesis, Karlstad University, Faculty of Economic Sciences, Communication and IT, Karlstad, Sweden, February 2012. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Project+Risk+Management:+Methodology+Development+for+Engineering,+Procurement+and+Construction+Projects+a+Case+Study+in+the+Oil+and+Gas+Industry&author=Mohebbi,+A.H.&author=Bislimi,+N.&publication_year=2012)\]
09. Rijtema, S.; Haas, R.D. Creating sustainable offshore developments in the ultra-deep water. In Proceedings of the Offshore Technology Conference, Houston, TX, USA, 4–7 May 2015. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Creating+sustainable+offshore+developments+in+the+ultra-deep+water&conference=Proceedings+of+the+Offshore+Technology+Conference&author=Rijtema,+S.&author=Haas,+R.D.&publication_year=2015&doi=10.4043/25873-ms)\] \[ [CrossRef](https://doi.org/10.4043/25873-ms)\]
10. Yu, N.; Wang, Y. Risk analysis of EPC project based on ISM. In Proceedings of the 2nd IEEE International Conference on Emergency Management and Management Sciences, Beijing, China, 8–10 August 2011. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Risk+analysis+of+EPC+project+based+on+ISM&conference=Proceedings+of+the+2nd+IEEE+International+Conference+on+Emergency+Management+and+Management+Sciences&author=Yu,+N.&author=Wang,+Y.&publication_year=2011&doi=10.1109/icemms.2011.6015642)\] \[ [CrossRef](https://doi.org/10.1109/icemms.2011.6015642)\]
11. Kim, M.H.; Lee, E.B.; Choi, H.S. Detail engineering completion rating index system (DECRIS) for optimal initiation of construction works to improve contractors’ schedule-cost performance for offshore oil and gas EPC projects. Sustainability **2018**, 10, 2469\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Detail+engineering+completion+rating+index+system+(DECRIS)+for+optimal+initiation+of+construction+works+to+improve+contractors%E2%80%99+schedule-cost+performance+for+offshore+oil+and+gas+EPC+projects&author=Kim,+M.H.&author=Lee,+E.B.&author=Choi,+H.S.&publication_year=2018&journal=Sustainability&volume=10&pages=2469&doi=10.3390/su10072469)\] \[ [CrossRef](https://doi.org/10.3390/su10072469)\]
12. Ullah, K.; Abdullah, A.H.; Nagapan, S.; Suhoo, S.; Khan, M.S. Theoretical framework of the causes of construction time and cost overruns. IOP Conf. Ser. Mater. Sci. Eng. **2017**, 271, 012032\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Theoretical+framework+of+the+causes+of+construction+time+and+cost+overruns&author=Ullah,+K.&author=Abdullah,+A.H.&author=Nagapan,+S.&author=Suhoo,+S.&author=Khan,+M.S.&publication_year=2017&journal=IOP+Conf.+Ser.+Mater.+Sci.+Eng.&volume=271&pages=012032&doi=10.1088/1757-899X/271/1/012032)\] \[ [CrossRef](https://doi.org/10.1088/1757-899X/271/1/012032)\]
13. Gunduz, M.; Maki, O.L. Assessing the risk perception of cost overview through importance rating. Technol. Econ. Dev. Econ. **2018**, 24, 1829–1844. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Assessing+the+risk+perception+of+cost+overview+through+importance+rating&author=Gunduz,+M.&author=Maki,+O.L.&publication_year=2018&journal=Technol.+Econ.+Dev.+Econ.&volume=24&pages=1829%E2%80%931844&doi=10.3846/20294913.2017.1321053)\] \[ [CrossRef](https://doi.org/10.3846/20294913.2017.1321053)\]
14. Animah, I.; Shafiee, M. Application of risk analysis in the liquefied natural gas (LNG) sector: An overview. J. Loss Prev. Process. Ind. **2020**, 63. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Application+of+risk+analysis+in+the+liquefied+natural+gas+(LNG)+sector:+An+overview&author=Animah,+I.&author=Shafiee,+M.&publication_year=2020&journal=J.+Loss+Prev.+Process.+Ind.&volume=63&doi=10.1016/j.jlp.2019.103980)\] \[ [CrossRef](https://doi.org/10.1016/j.jlp.2019.103980)\]
15. Son, B.Y.; Lee, E.B. Using text mining to estimate schedule delay risk of shore oil and gas EPC case studies during the bidding process. Energies **2019**, 12, 1956\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Using+text+mining+to+estimate+schedule+delay+risk+of+shore+oil+and+gas+EPC+case+studies+during+the+bidding+process&author=Son,+B.Y.&author=Lee,+E.B.&publication_year=2019&journal=Energies&volume=12&pages=1956&doi=10.3390/en12101956)\] \[ [CrossRef](https://doi.org/10.3390/en12101956)\]
16. Chua, D.K.H.; Loh, P.K.; Kong, Y.C.; Jaselskism, E.J. Neural networks for construction project success. Expert Syst. Appl. **1997**, 13, 317–328. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Neural+networks+for+construction+project+success&author=Chua,+D.K.H.&author=Loh,+P.K.&author=Kong,+Y.C.&author=Jaselskism,+E.J.&publication_year=1997&journal=Expert+Syst.+Appl.&volume=13&pages=317%E2%80%93328&doi=10.1016/S0957-4174(97)00046-8)\] \[ [CrossRef](https://doi.org/10.1016/S0957-4174(97)00046-8)\]
17. Ho, S.P.; Tserng, H.P.; Jan, S.H. Enhancing knowledge sharing management using BIM technology in construction. Sci. World J. **2013**, 1–10. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Enhancing+knowledge+sharing+management+using+BIM+technology+in+construction&author=Ho,+S.P.&author=Tserng,+H.P.&author=Jan,+S.H.&publication_year=2013&journal=Sci.+World+J.&pages=1%E2%80%9310&doi=10.1155/2013/170498&pmid=24723790)\] \[ [CrossRef](https://doi.org/10.1155/2013/170498)\] \[ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/24723790)\]
18. Sackey, S.; Kim, B.S. Development of an expert system tool for the selection of procurement system in large-scale construction projects. (ESCONPROCS). KSCE J. Civ. Eng. **2018**, 22, 4205–4214. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Development+of+an+expert+system+tool+for+the+selection+of+procurement+system+in+large-scale+construction+projects.+(ESCONPROCS)&author=Sackey,+S.&author=Kim,+B.S.&publication_year=2018&journal=KSCE+J.+Civ.+Eng.&volume=22&pages=4205%E2%80%934214&doi=10.1007/s12205-018-0439-2)\] \[ [CrossRef](https://doi.org/10.1007/s12205-018-0439-2)\]
19. Lee, D.H.; Yoon, G.H.; Kim, J.J. Development of ITB risk Mgt. model based on AI in bidding phase for oversea EPC projects. J. Inst. Internet Broadcast. Commun. (JIIBC) **2019**, 19, 151–160. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Development+of+ITB+risk+Mgt.+model+based+on+AI+in+bidding+phase+for+oversea+EPC+projects&author=Lee,+D.H.&author=Yoon,+G.H.&author=Kim,+J.J.&publication_year=2019&journal=J.+Inst.+Internet+Broadcast.+Commun.+(JIIBC)&volume=19&pages=151%E2%80%93160&doi=10.7236/JIIBC.2019.19.4.151)\] \[ [CrossRef](https://doi.org/10.7236/JIIBC.2019.19.4.151)\]
20. Watson Explorer; IBM: Armonk, NY, USA; Available online: [https://www.ibm.com/docs/en/watson-explorer/11.0.1?topic=components-product-overview](https://www.ibm.com/docs/en/watson-explorer/11.0.1?topic=components-product-overview) (accessed on 30 June 2021).
21. Cherpas, C. Natural language processing, pragmatics, and verbal behavior. Anal. Verbal Behav. **1992**, 10, 135–147. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Natural+language+processing,+pragmatics,+and+verbal+behavior&author=Cherpas,+C.&publication_year=1992&journal=Anal.+Verbal+Behav.&volume=10&pages=135%E2%80%93147&doi=10.1007/BF03392880)\] \[ [CrossRef](https://doi.org/10.1007/BF03392880)\]
22. Lim, S.Y.; Kim, S.O. A text mining analysis for research trend about information and communication technology in construction automation. Korean J. Constr. Eng. Manag. **2016**, 17, 13–23. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=A+text+mining+analysis+for+research+trend+about+information+and+communication+technology+in+construction+automation&author=Lim,+S.Y.&author=Kim,+S.O.&publication_year=2016&journal=Korean+J.+Constr.+Eng.+Manag.&volume=17&pages=13%E2%80%9323&doi=10.6106/KJCEM.2016.17.6.013)\] \[ [CrossRef](https://doi.org/10.6106/KJCEM.2016.17.6.013)\]\[ [Green Version](http://society.kisti.re.kr/sv/SV_svpsbs03V.do?method=download&cn1=JAKO201608967047389)\]
23. Tixier, A.J.-P.; Hallowell, M.R.; Rajagopalan, B.; Bowman, D. Automated content analysis for construction safety: A natural language processing system to extract precursors and outcomes from unstructured injury reports. Autom. Constr. **2016**, 62, 45–56. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Automated+content+analysis+for+construction+safety:+A+natural+language+processing+system+to+extract+precursors+and+outcomes+from+unstructured+injury+reports&author=Tixier,+A.J.-P.&author=Hallowell,+M.R.&author=Rajagopalan,+B.&author=Bowman,+D.&publication_year=2016&journal=Autom.+Constr.&volume=62&pages=45%E2%80%9356&doi=10.1016/j.autcon.2015.11.001)\] \[ [CrossRef](https://doi.org/10.1016/j.autcon.2015.11.001)\]
24. Williams, T.P.; Gong, J. Predicting construction cost overruns using text mining, numerical data and ensemble classifiers. Autom. Constr. **2014**, 43, 23–29. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Predicting+construction+cost+overruns+using+text+mining,+numerical+data+and+ensemble+classifiers&author=Williams,+T.P.&author=Gong,+J.&publication_year=2014&journal=Autom.+Constr.&volume=43&pages=23%E2%80%9329&doi=10.1016/j.autcon.2014.02.014)\] \[ [CrossRef](https://doi.org/10.1016/j.autcon.2014.02.014)\]
25. Marzouk, M.; Enaba, M. Text analytics to analyze and monitor construction project contract and correspondence. Autom. Constr. **2019**, 98, 265–274. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Text+analytics+to+analyze+and+monitor+construction+project+contract+and+correspondence&author=Marzouk,+M.&author=Enaba,+M.&publication_year=2019&journal=Autom.+Constr.&volume=98&pages=265%E2%80%93274&doi=10.1016/j.autcon.2018.11.018)\] \[ [CrossRef](https://doi.org/10.1016/j.autcon.2018.11.018)\]
26. Zoua, Y.; Kiviniemib, A.; Jonesa, S.W. Retrieving similar cases for construction project risk management using natural language processing techniques. Autom. Constr. **2017**, 80, 66–76. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Retrieving+similar+cases+for+construction+project+risk+management+using+natural+language+processing+techniques&author=Zoua,+Y.&author=Kiviniemib,+A.&author=Jonesa,+S.W.&publication_year=2017&journal=Autom.+Constr.&volume=80&pages=66%E2%80%9376&doi=10.1016/j.autcon.2017.04.003)\] \[ [CrossRef](https://doi.org/10.1016/j.autcon.2017.04.003)\]
27. Li, M.; Yang, Q.; He, F.; Li, Z.; Zhao, P.; Zhao, L.; Chen, Z. An unsupervised learning approach for NER based on online encyclopedia. Web Big Data **2019**, 329–344. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=An+unsupervised+learning+approach+for+NER+based+on+online+encyclopedia&author=Li,+M.&author=Yang,+Q.&author=He,+F.&author=Li,+Z.&author=Zhao,+P.&author=Zhao,+L.&author=Chen,+Z.&publication_year=2019&journal=Web+Big+Data&pages=329%E2%80%93344&doi=10.1007/978-3-030-26072-9_25)\] \[ [CrossRef](https://doi.org/10.1007/978-3-030-26072-9_25)\]
28. Python; Python Software Foundation: Wilmington, DE, USA; Available online: [https://www.python.org/](https://www.python.org/) (accessed on 21 June 2021).
29. Vijayarani, S. Preprocessing techniques for text mining—An overview. Int. J. Comput. Sci. Commun. Netw. **2015**, 5, 7–16. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Preprocessing+techniques+for+text+mining%E2%80%94An+overview&author=Vijayarani,+S.&publication_year=2015&journal=Int.+J.+Comput.+Sci.+Commun.+Netw.&volume=5&pages=7%E2%80%9316)\]
30. Manning, C.; Schiitze, H. Foundations of Statistical Natural Language Processing; Cambridge University Press: Cambridge, UK, 1999. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Foundations+of+Statistical+Natural+Language+Processing&author=Manning,+C.&author=Schiitze,+H.&publication_year=1999)\]
31. Shinde, A.A.; Chougule, S.R. Text pre-processing and text segmentation for OCR. Int. J. Comput. Sci. Eng. Technol. **2012**, 2, 810–812. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Text+pre-processing+and+text+segmentation+for+OCR&author=Shinde,+A.A.&author=Chougule,+S.R.&publication_year=2012&journal=Int.+J.+Comput.+Sci.+Eng.+Technol.&volume=2&pages=810%E2%80%93812)\]
32. Marina, D.B. The Open Source Relational Database. Available online: [https://mariadb.org/](https://mariadb.org/) (accessed on 21 June 2021).
33. Manning, C.D.; Raghavan, P.; Schütze, H. Introduction to Information Retrieval; Cambridge University Press: Cambridge, UK, 2008. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Introduction+to+Information+Retrieval&author=Manning,+C.D.&author=Raghavan,+P.&author=Sch%C3%BCtze,+H.&publication_year=2008)\] \[ [CrossRef](https://doi.org/10.1017/CBO9780511809071)\]
34. PhraseMatcher, spaCy API Documentation. Explosion, Berlin, Germany. Available online: [https://spacy.io/api/phrasematcher](https://spacy.io/api/phrasematcher) (accessed on 21 June 2021).
35. enModels Model Documentation, Explosion, Berlin, Germany. Available online: [https://spacy.io/models/en](https://spacy.io/models/en) (accessed on 21 June 2021).
36. spaCy, Explosion, Berlin, Germany. Available online: [https://spacy.io/](https://spacy.io/) (accessed on 21 June 2021).
37. NamedEntityRecognition, Training Pipelines and Models, Explosion, Berlin, Germany. Available online: [https://spacy.io/usage/training#quickstart](https://spacy.io/usage/training#quickstart) (accessed on 21 June 2021).
38. Kang, S.O.; Lee, E.B.; Baek, H.K. A digitization and conversion tool for imaged drawings to intelligent piping and instrumentation diagrams (P&ID). Energies **2019**, 12, 2593\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=A+digitization+and+conversion+tool+for+imaged+drawings+to+intelligent+piping+and+instrumentation+diagrams+(P%2526ID)&author=Kang,+S.O.&author=Lee,+E.B.&author=Baek,+H.K.&publication_year=2019&journal=Energies&volume=12&pages=2593&doi=10.3390/en12132593)\] \[ [CrossRef](https://doi.org/10.3390/en12132593)\]
39. Java Script Object Notation, Introducing JSON. Available online: [https://www.json.org/json-en.html](https://www.json.org/json-en.html) (accessed on 21 June 2021).
40. Pickle, Python Object Serialization. Available online: [https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html) (accessed on 21 June 2021).
41. Amir-Ahmadi, P.; Matthes, C.; Wang, M.C. Choosing prior hyperparameters: With applications to time-varying parameter models. J. Bus. Econ. Stat. **2018**, 38, 124–136. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Choosing+prior+hyperparameters:+With+applications+to+time-varying+parameter+models&author=Amir-Ahmadi,+P.&author=Matthes,+C.&author=Wang,+M.C.&publication_year=2018&journal=J.+Bus.+Econ.+Stat.&volume=38&pages=124%E2%80%93136&doi=10.1080/07350015.2018.1459302)\] \[ [CrossRef](https://doi.org/10.1080/07350015.2018.1459302)\]
42. Predix Platform, General Electronic, Boston, MA, USA The Industrial IoT Platform. Available online: [https://www.predix.io/](https://www.predix.io/) (accessed on 21 June 2021).
43. Veracity, DNV, Sandvika, Norway. Available online: [https://www.veracity.com/](https://www.veracity.com/) (accessed on 21 June 2021).
44. Vasiliev, Y. Natural Language Processing with Python and SpaCy; No Starch Press: San Francisco, CA, USA, 2020. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Natural+Language+Processing+with+Python+and+SpaCy&author=Vasiliev,+Y.&publication_year=2020)\]
45. Behnel, S.; Bradshaw, R.; Dalcín, L.; Florisson, M.; Makarov, V.; Seljebotn, D.S. Cython C-Extensions for Python; Redmond: Washington, DC, USA; Available online: [https://cython.org/](https://cython.org/) (accessed on 21 June 2021).
46. Wiseprophet, Machine Learning Automated Platform; WISEiTECH: Seoul, Korea; Available online: [http://prophet.wise.co.kr/#/intro](http://prophet.wise.co.kr/#/intro) (accessed on 21 June 2021).
47. Oracle; Integrated Cloud Application: Austin, TX, USA; Available online: [https://www.oracle.com/index.html](https://www.oracle.com/index.html) (accessed on 21 June 2021).
48. MySQL; Oracle Corporation: Austin, TX, USA; Available online: [https://www.mysql.com/](https://www.mysql.com/) (accessed on 21 June 2021).

**Figure 1.**
Overview of Engineering Machine learning Automation Platform (EMAP).

**Figure 1.**
Overview of Engineering Machine learning Automation Platform (EMAP).

**Figure 2.**
Analysis framework of the ITB Module (CRC and TFA sub-modules).

**Figure 2.**
Analysis framework of the ITB Module (CRC and TFA sub-modules).

**Figure 3.**
Screenshot of PDF application function (Example of header/footer elimination).

**Figure 3.**
Screenshot of PDF application function (Example of header/footer elimination).

**Figure 4.**
Algorithm flow of the Critical Risk Check module.

**Figure 4.**
Algorithm flow of the Critical Risk Check module.

**Figure 5.**
An example of using the JSON format.

**Figure 5.**
An example of using the JSON format.

**Figure 6.**
An example of CRC results in the cloud service.

**Figure 6.**
An example of CRC results in the cloud service.

**Figure 7.**
Algorithm flow of Terms Frequency Analysis module.

**Figure 7.**
Algorithm flow of Terms Frequency Analysis module.

**Figure 8.**
An example of TFA module results’ visualization.

**Figure 8.**
An example of TFA module results’ visualization.

**Figure 9.**
Engineering Machine learning Automation Platform (EMAP).

**Figure 9.**
Engineering Machine learning Automation Platform (EMAP).

**Figure 10.**
Screenshot of the Contract sub-module selection function from the ITB Analysis module.

**Figure 10.**
Screenshot of the Contract sub-module selection function from the ITB Analysis module.

**Table 1.**
List of the collected EPC contracts in the database.

**Table 1.**
List of the collected EPC contracts in the database.

| Project Category | No. | Project Name<br>(Anonymized) | Project Type | Location |
| :-: | :-: | :-: | :-: | :-: |
| Offshore | 1 | P-1 | FLNG 1 | Brazil |
| 2 | C-1 | Fixed Platform | Angola |
| 3 | S-1 | FPSO 2 | Nigeria |
| 4 | P-2 | Drillship | for chartering |
| 5 | E-1 | Semi-submersible | Gulf of Mexico |
| 6 | S-2 | Fixed Platform | North Sea (Norway) |
| 7 | I-1 | FPSO | Australia |
| 8 | C-2 | Booster Compression Facilities | Gulf of Thailand |
| 9 | T-1 | TLP 3 | Congo |
| 10 | T-2 | FPSO | Angola |
| 11 | T-3 | FPSO | Nigeria |
| 12 | T-4 | FPSO | Angola |
| Onshore | 13 | S-3 | Petrochemical | Saudi Arabia |
| 14 | A-1 | Combined Cycle Power Plant | Kuwait |
| 15 | A-2 | Refinery | Kuwait |
| 16 | C-3 | LNG Terminal | USA |
| 17 | P-3 | Refinery | Peru |
| 18 | O-1 | Oil Collecting Station | India |
| 19 | A-3 | Coal-fired Power Plant | Chile |
| Infrastructure | 20 | W-1 | Tunnel | Mexico |
| 21 | P-4 | Highway | Australia |
| 22 | M-1 | Tunnel | Australia |
| 23 | R-1 | Rail | Australia |
| 24 | V-1 | Tunnel | Australia |
| 25 | N-1 | Rail | Australia |

1 FLNG (floating liquified Natural gas): a floating production storage and offloading facility that conducts LNG operations from offshore gas wells. 2 FPSO (floating production, storage and offloading): a ship-shaped floating production facility that process, store, and offload the hydrocarbon production from offshore oil and gas wells. 3 TLP (tension leg platforms): A floating production system typically that are buoyant production facilities vertically moored to the seafloor by tendons for offshore oil/gas wells.

**Table 2.**
An example of the text contents before and after pre-processing (excerption).

**Table 2.**
An example of the text contents before and after pre-processing (excerption).

| The Original Text Contents<br>before Pre-Processing | The Processed Text Contents<br> after Pre-Processing |
| :-: | :-: |
| No. | Content | No. | Position<br>Code | Content |
| :-: | :-: | :-: | :-: | :-: |
| 1 | 36 LIQUIDATED DAMAGES<br>36.1 Liquidated Damages for Late Completion (a) If contractor fails to complete the relevant part of the work by the relevant Completion Date then contractor will pay liquidated damages to Company in accordance with Exhibit B. (b) Subject to Company’s rights and remedies provided for under Article XX, sub- Articles YY to YY and Article ZZ, the payment of liquidated damages under sub-Article YY are the sole and exclusive financial remedy of Company in respect of contractor’s failure to complete the relevant part of the work by the Completion Date. | 1 | 36 | LIQUIDATED DAMAGES |
| 2 | 36.1 | Liquidated Damages for Late Completion |
| 3 | (a) | If contractor fails to complete the relevant part of the work by the relevant Completion Date then contractor will pay liquidated damages to Company in accordance with Exhibit B. |
| 4 | (b) | Subject to Company’s rights and remedies provided for under Article XX, sub- Articles YY to YY and Article ZZ, the payment of liquidated damages under sub-Article YY are the sole and exclusive financial remedy of Company in respect of contractor’s failure to complete the relevant part of the work by the Completion Date. |

**Table 3.**
An example of the table generated in the database.

**Table 3.**
An example of the table generated in the database.

| Project | Class | Sub-Class | Content |
| :-: | :-: | :-: | :-: |
| Cheniere\_<br>Sabine\_<br>Pass\_<br>LNG | 2\. RELATIONSHIP OF OWNER, CONTRACTOR AND<br>SUBCONTRACTORS | 2.1 Status of Contractor. | The relationship of Contractor to Owner shall be that of an independent contractor. |

**Table 4.**
Summary of algorithm.

**Table 4.**
Summary of algorithm.

|  | Critical Risk Check | Terms Frequency Analysis |
| :-: | :-: | :-: |
| **Key Library** | spaCy’s PhraseMatcher \[ [34](https://www.mdpi.com/1996-1073/14/15/4632#B34-energies-14-04632)\] | spaCy’s en\_core\_web\_sm \[ [35](https://www.mdpi.com/1996-1073/14/15/4632#B35-energies-14-04632)\] |
| **Technology** | Artificial Intelligence (AI) | Information Retrieval (IR) |
| **Input Data** | EPC contract | EPC contract |
| **Language Program** | Python 3.7 | Python 3.7 |
| **Target Result** | This module aims to analyze the existence of EPC project risk using rule-based technique. | This module aims to tag similar syntax through a training model suitable for the EPC project. |

**Table 5.**
An example of liquidated damages sentences from ‘I-1’EPC Project Contract.

**Table 5.**
An example of liquidated damages sentences from ‘I-1’EPC Project Contract.

| LD Sentence |
| :-: |
| All amounts of such liquidated damages for which contractor may become liable under this contract are agreed to be a genuine pre-estimate of the loss which may be sustained by Company in the event that contractor fails to comply with the relevant obligation under the contract and are not a penalty. |

**Table 6.**
An example of the single rules in the Critical Risk Check.

**Table 6.**
An example of the single rules in the Critical Risk Check.

| Single Label | Keyword |
| :-: | :-: |
| Liquidated Damages | such liquidated damages |
| Liquidated Damages |
| Damages |
| genuine pre-estimate |
| Liability | liable |
| Fail | fails to comply with |
| Fails |
| Penalty | not a penalty |
| penalty |

**Table 7.**
An example of Critical Risk Check multi-rule.

**Table 7.**
An example of Critical Risk Check multi-rule.

| Multi Label | Keyword (Single Label) |
| :-: | :-: |
| Delay Liquidated Damages Clause | Liquidated\_Damages, Liability, Fail, Penalty |
| Liquidated\_Damages, Time\_Barring, Payable |

**Table 8.**
An example of multi-rule label in the Critical Risk Check.

**Table 8.**
An example of multi-rule label in the Critical Risk Check.

| Multi Label |
| :-: |
| Liquidated Damages Clause |
| Delay Liquidated Damages Clause |
| Performance Liquidated Damages Clause |
| Exclusive Remedy 1 Clause |
| Exclusive Remedy 2 Clause |

**Table 9.**
An example of the Critical Risk Check sub-module result.

**Table 9.**
An example of the Critical Risk Check sub-module result.

| Multi-Label | Single Label<br>(Label: Keyword) | Risk<br>Group | Sentence |
| :-: | :-: | :-: | :-: |
| \[‘Liquidated Damages’, ‘Liability’, ‘Fail’, ‘Penalty’\] | \[‘Liquidated Damages: such liquidated damages’, ‘Liquidated Damages: a genuine pre-estimate of the loss’, ‘Liability: liable’, ‘Fail: fails’, ‘Penalty: not a penalty.’\] | \[‘Delay Liquidated Damages Clause’\] | All amounts of such liquidated damages for which contractor may become liable under this contract are agreed to be a genuine pre-estimate of the loss which may be sustained by Company in the event that contractor fails to comply with the relevant obligation under the contract and are not a penalty. |
| \[‘Fail’, ‘Remedy’, ‘Waiver’, ‘Contractor’\] | \[‘Fail: failure’,<br>‘Remedy: remedy’,<br>‘Waiver: waiver’, ‘Contractor: PARTY’\] | \[‘Exclusive Remedy 1 Clause’\] | The failure to exercise or delay in exercising a right or remedy under the CONTRACT shall not constitute a waiver of the right or remedy, or a waiver of any other rights or remedies, unless such waiver is set out in writing and executed by such PARTY’s authorized representative and duly notified to the other PARTY. |

**Table 10.**
Keyword list of fit for purpose label.

**Table 10.**
Keyword list of fit for purpose label.

| Label | NO | Family Keyword |
| :-: | :-: | :-: |
| Fit for Purpose | 1 | fit for purpose |
| 2 | fit for the use |
| 3 | fit for their intended purpose |
| 4 | fit for the purposes |
| 5 | fit for its purpose |
| 6 | fit the purpose |
| 7 | fit for its intended purpose |
| 8 | fit for that purpose |

**Table 11.**
An example of risk data JSON structure.

**Table 11.**
An example of risk data JSON structure.

|     |
| --- |
| \[“sentence”: “Contractor warrants that the Plant will be fit for the purpose”, “entities”: (43,62), “FFP”\] |

**Table 12.**
An Example of NER label.

**Table 12.**
An Example of NER label.

| NER Label (14) |
| :-: |
| Damages (Liquidated Damages, Delay Liquidated Damages), dispute, change order (variation), fit for purpose, shall not be liable, limitation of liability, indemnify (indemnification), governing law (applicable law), deem, bank guarantee, Cost, Schedule, Safety, Quality |

**Table 13.**
Calibration values of the NER sub-model.

**Table 13.**
Calibration values of the NER sub-model.

| Parameter | Value |
| :-: | :-: |
| Batch size | 128 |
| Dropout rate | 0.75 |
| Epoch | 2000 |
| Learning rate | 1.001 |
| Optimizer | SGD 1 |

1 Stochastic gradient descent: A method of using slope to minimize the value of the loss function, which defines the difference between the result value and the actual value from the network.

**Table 14.**
Information of SMEs participating.

**Table 14.**
Information of SMEs participating.

| Expert | Project Experiences | Specialty |
| :-: | :-: | :-: |
| SME 1 | 20 years | ITB analysis/Contract Management |
| SME 2 | 15 years | ITB analysis/Project Management |
| SME 3 | 17 years | EPC Project Business Management |
| Engineer 1 | 2 years | EPC Project |
| Engineer 2 | 5 years | EPC Project |

**Table 15.**
Single keyword list.

**Table 15.**
Single keyword list.

| Single Keyword (20) |
| :-: |
| Certificate, Guarantee, Dispute, Contractor, Completion, Period, Payable, Deem, Agreement, Waiver, Law, Liability, Novation, Remedy, Discretion, Taxes, Refund, Amount, Indemnify, Default |

**Table 16.**
CRC sub-module results.

**Table 16.**
CRC sub-module results.

| Risk Category | Subject | Total<br>Sentence | Time Span<br>(Hours) | Extracted Sentence | SMEs Validation | Accuracy<br>(%) |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| TP | FP |
| :-: | :-: |
| Single Rule | Module | 1122 | 0.6 | 230 | 205 | 25 | 89 |
| Engineer | 1122 | 30 | 120 | 120 | 0 | 100 |
| Multi-Rule (LD) | Module | 1122 | 0.5 | 36 | 34 | 2 | 94 |
| Engineer | 1222 | 24 | 28 | 28 | 0 | 100 |

**Table 17.**
An example of contract sentence.

**Table 17.**
An example of contract sentence.

|     |
| --- |
| Contract Price means the aggregate of all sums payable under the contract calculated in accordance with Exhibit B as may be modified by Change Orders; it being understood that the initial Contract Price is that known at the Contract Date and the final Contract Price is that known after final assessment under the contract as described in sub-Article 34.6. |

**Table 18.**
Accuracy of Terms Frequency Analysis sub-module result.

**Table 18.**
Accuracy of Terms Frequency Analysis sub-module result.

| Target<br>Label | Subject | Contract<br>(Project) | Time Span<br>(Hours) | Extracted Keyword | SMEs Validation | Accuracy<br>(%) |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| TP | FP |
| :-: | :-: |
| Damages | Module | I-1 | 1 | 98 | 90 | 8 | 92 |
| Engineer | I-1 | 24 | 82 | 82 | 0 | 100 |
| Fit for Purpose<br>(FFP) | Module | I-1 | 0.9 | 6 | 5 | 1 | 83 |
| Engineer | I-1 | 22 | 4 | 4 | 0 | 100 |

|     |     |
| --- | --- |
|  | **Publisher’s Note:** MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations. |

© 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license ( [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)).

## Share and Cite

[Email](mailto:?&subject=From%20MDPI%3A%20%22AI%20and%20Text-Mining%20Applications%20for%20Analyzing%20Contractor%E2%80%99s%20Risk%20in%20Invitation%20to%20Bid%20%28ITB%29%20and%20Contracts%20for%20Engineering%20Procurement%20and%20Construction%20%28EPC%29%20Projects%22&body=https://www.mdpi.com/1210672%3A%0A%0AAI%20and%20Text-Mining%20Applications%20for%20Analyzing%20Contractor%E2%80%99s%20Risk%20in%20Invitation%20to%20Bid%20%28ITB%29%20and%20Contracts%20for%20Engineering%20Procurement%20and%20Construction%20%28EPC%29%20Projects%0A%0AAbstract%3A%20Contractors%20responsible%20for%20the%20whole%20execution%20of%20engineering%2C%20procurement%2C%20and%20construction%20%28EPC%29%20projects%20are%20exposed%20to%20multiple%20risks%20due%20to%20various%20unbalanced%20contracting%20methods%20such%20as%20lump-sum%20turn-key%20and%20low-bid%20selection.%20Although%20systematic%20risk%20management%20approaches%20are%20required%20to%20prevent%20unexpected%20damage%20to%20the%20EPC%20contractors%20in%20practice%2C%20there%20were%20no%20comprehensive%20digital%20toolboxes%20for%20identifying%20and%20managing%20risk%20provisions%20for%20ITB%20and%20contract%20documents.%20This%20study%20describes%20two%20core%20modules%2C%20Critical%20Risk%20Check%20%28CRC%29%20and%20Term%20Frequency%20Analysis%20%28TFA%29%2C%20developed%20as%20a%20digital%20EPC%20contract%20risk%20analysis%20tool%20for%20contractors%2C%20using%20artificial%20intelligence%20and%20text-mining%20techniques.%20The%20CRC%20module%20automatically%20extracts%20risk-involved%20clauses%20in%20the%20EPC%20ITB%20and%20contracts%20by%20the%20phrase-matcher%20technique.%20A%20machine%20learning%20model%20was%20built%20in%20the%20TFA%20module%20for%20contractual%20risk%20extraction%20by%20using%20the%20named-entity%20recognition%20%28NER%29%20method.%20The%20risk-involved%20clauses%20collected%20for%20model%20development%20were%20converted%20into%20a%20database%20in%20JavaScript[...] "Email")[LinkedIn](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.mdpi.com%2F1210672&title=AI%20and%20Text-Mining%20Applications%20for%20Analyzing%20Contractor%E2%80%99s%20Risk%20in%20Invitation%20to%20Bid%20%28ITB%29%20and%20Contracts%20for%20Engineering%20Procurement%20and%20Construction%20%28EPC%29%20Projects%26source%3Dhttps%3A%2F%2Fwww.mdpi.com%26summary%3DContractors%20responsible%20for%20the%20whole%20execution%20of%20engineering%2C%20procurement%2C%20and%20construction%20%28EPC%29%20projects%20are%20exposed%20to%20multiple%20risks%20due%20to%20various%20unbalanced%20contracting%20methods%20such%20as%20lump-sum%20turn-key%20and%20low-bid%20selection.%20Although%20%5B...%5D "LinkedIn")[facebook](http://www.facebook.com/sharer.php?u=https://www.mdpi.com/1210672 "facebook")[Reddit](http://www.reddit.com/submit?url=https://www.mdpi.com/1210672 "Reddit")[Mendeley](http://www.mendeley.com/import/?url=https://www.mdpi.com/1210672 "Mendeley")

**MDPI and ACS Style**

Choi, S.J.; Choi, S.W.; Kim, J.H.; Lee, E.-B.
AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects. _Energies_ **2021**, _14_, 4632.
https://doi.org/10.3390/en14154632

**AMA Style**

Choi SJ, Choi SW, Kim JH, Lee E-B.
AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects. _Energies_. 2021; 14(15):4632.
https://doi.org/10.3390/en14154632

**Chicago/Turabian Style**

Choi, Su Jin, So Won Choi, Jong Hyun Kim, and Eul-Bum Lee.
2021\. "AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects" _Energies_ 14, no. 15: 4632.
https://doi.org/10.3390/en14154632

**APA Style**

Choi, S. J., Choi, S. W., Kim, J. H., & Lee, E.-B.

(2021). AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects. _Energies_, _14_(15), 4632.
https://doi.org/10.3390/en14154632

Note that from the first issue of 2016, this journal uses article numbers instead of page numbers. See further details [here](https://www.mdpi.com/about/announcements/784).

## Article Metrics

No

No

### Article Access Statistics

For more information on the journal statistics, click [here](https://www.mdpi.com/journal/energies/stats).

Multiple requests from the same IP address are counted as one view.

Zoom\| Orient \| As Lines \| As Sticks \| As Cartoon \| As Surface \|Previous Scene\|Next Scene

## Cite

Export citation file:
BibTeX \|
EndNote \|
RIS

**MDPI and ACS Style**

Choi, S.J.; Choi, S.W.; Kim, J.H.; Lee, E.-B.
AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects. _Energies_ **2021**, _14_, 4632.
https://doi.org/10.3390/en14154632

**AMA Style**

Choi SJ, Choi SW, Kim JH, Lee E-B.
AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects. _Energies_. 2021; 14(15):4632.
https://doi.org/10.3390/en14154632

**Chicago/Turabian Style**

Choi, Su Jin, So Won Choi, Jong Hyun Kim, and Eul-Bum Lee.
2021\. "AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects" _Energies_ 14, no. 15: 4632.
https://doi.org/10.3390/en14154632

**APA Style**

Choi, S. J., Choi, S. W., Kim, J. H., & Lee, E.-B.

(2021). AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects. _Energies_, _14_(15), 4632.
https://doi.org/10.3390/en14154632

Note that from the first issue of 2016, this journal uses article numbers instead of page numbers. See further details [here](https://www.mdpi.com/about/announcements/784).

_clear_

We use cookies on our website to ensure you get the best experience.

Read more about our cookies [here](https://www.mdpi.com/about/privacy).

[Accept](https://www.mdpi.com/accept_cookies)

## Share Link

[Email](mailto:?&subject=From%20MDPI%3A%20%22AI%20and%20Text-Mining%20Applications%20for%20Analyzing%20Contractor%E2%80%99s%20Risk%20in%20Invitation%20to%20Bid%20%28ITB%29%20and%20Contracts%20for%20Engineering%20Procurement%20and%20Construction%20%28EPC%29%20Projects%22&body=https://www.mdpi.com/1210672%3A%0A%0AAI%20and%20Text-Mining%20Applications%20for%20Analyzing%20Contractor%E2%80%99s%20Risk%20in%20Invitation%20to%20Bid%20%28ITB%29%20and%20Contracts%20for%20Engineering%20Procurement%20and%20Construction%20%28EPC%29%20ProjectsContractors%20responsible%20for%20the%20whole%20execution%20of%20engineering%2C%20procurement%2C%20and%20construction%20%28EPC%29%20projects%20are%20exposed%20to%20multiple%20risks%20due%20to%20various%20unbalanced%20contracting%20methods%20such%20as%20lump-sum%20turn-key%20and%20low-bid%20selection.%20Although%20systematic%20risk%20management%20approaches%20are%20required%20to%20prevent%20unexpected%20damage%20to%20the%20EPC%20contractors%20in%20practice%2C%20there%20were%20no%20comprehensive%20digital%20toolboxes%20for%20identifying%20and%20managing%20risk%20provisions%20for%20ITB%20and%20contract%20documents.%20This%20study%20describes%20two%20core%20modules%2C%20Critical%20Risk%20Check%20%28CRC%29%20and%20Term%20Frequency%20Analysis%20%28TFA%29%2C%20developed%20as%20a%20digital%20EPC%20contract%20risk%20analysis%20tool%20for%20contractors%2C%20using%20artificial%20intelligence%20and%20text-mining%20techniques.%20The%20CRC%20module%20automatically%20extracts%20risk-involved%20clauses%20in%20the%20EPC%20ITB%20and%20contracts%20by%20the%20phrase-matcher%20technique.%20A%20machine%20learning%20model%20was%20built%20in%20the%20TFA%20module%20for%20contractual%20risk%20extraction%20by%20using%20the%20named-entity%20recognition%20%28NER%29%20method.%20The%20risk-involved%20clauses%20collected%20for%20model%20development%20were%20converted%20into%20a%20database%20in%20JavaScript%20Object[...] "Email")[Twitter](https://x.com/intent/tweet?text=AI+and+Text-Mining+Applications+for+Analyzing+Contractor%E2%80%99s+Risk+in+Invitation+to+Bid+%28ITB%29+and+Contracts+for+Engineering+Procurement+and+Construction+%28EPC%29+Projects&hashtags=mdpienergies&url=https%3A%2F%2Fwww.mdpi.com%2F1210672&via=energies_mdpi "Twitter")[LinkedIn](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.mdpi.com%2F1210672&title=AI%20and%20Text-Mining%20Applications%20for%20Analyzing%20Contractor%E2%80%99s%20Risk%20in%20Invitation%20to%20Bid%20%28ITB%29%20and%20Contracts%20for%20Engineering%20Procurement%20and%20Construction%20%28EPC%29%20Projects%26source%3Dhttps%3A%2F%2Fwww.mdpi.com%26summary%3DContractors%20responsible%20for%20the%20whole%20execution%20of%20engineering%2C%20procurement%2C%20and%20construction%20%28EPC%29%20projects%20are%20exposed%20to%20multiple%20risks%20due%20to%20various%20unbalanced%20contracting%20methods%20such%20as%20lump-sum%20turn-key%20and%20low-bid%20selection.%20Although%20%5B...%5D "LinkedIn")[facebook](http://www.facebook.com/sharer.php?u=https://www.mdpi.com/1210672 "facebook")[Reddit](http://www.reddit.com/submit?url=https://www.mdpi.com/1210672 "Reddit")[Mendeley](http://www.mendeley.com/import/?url=https://www.mdpi.com/1210672 "Mendeley")[CiteULike](http://www.citeulike.org/posturl?url=https://www.mdpi.com/1210672 "CiteULike")

Copy

_clear_

## Share

https://www.mdpi.com/1210672

_clear_

[Back to TopTop](https://www.mdpi.com/1996-1073/14/15/4632#)


## 跨源矛盾检测结论

### 检测范围
- 已精读来源数量：10 个
- 检测对象：核心数字、日期、功能描述、因果判断、市场/公司事实
- 检测时间：2026-06-22

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
