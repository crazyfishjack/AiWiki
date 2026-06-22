---
title: "调研证据包：招标文件 重点内容 解析 要素提取 阅读 ai提示词 开发"
source-type: article
generated: 2026-06-22
generated-by: wiki-research-skill
research-mode: standard
---

# 调研证据包：招标文件 重点内容 解析 要素提取 阅读 ai提示词 开发

## 调研问题

招标文件 重点内容 解析 要素提取 阅读 ai提示词 开发

## 摘要

本文档是四工具检索生成的证据包草稿，不是最终调研报告。Agent 必须先阅读本证据包，执行下方"AI 综合指令"，生成新的中文综合 raw 报告，然后询问用户是否入库。本证据包保留不删除。

- 发现候选信源：30
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
| exa | 1.00 | Large Language Model for Extracting Complex Contract Information in Industrial Scenes | https://arxiv.org/html/2507.06539v2 |
| exa | 1.00 | ExtractBench: A Benchmark and Evaluation Methodology for Complex Structured Extraction | https://arxiv.org/html/2602.12247 |
| exa | 1.00 | Retrieval Augmented Structured Generation: Business Document Information Extraction As Tool Use | https://arxiv.org/html/2405.20245 |
| exa | 1.00 | Intelligent Processing of Design Notices in Engineering Procurement Construction Projects | https://www.mdpi.com/2075-5309/15/5/805 |
| exa | 1.00 | BenchBench: Benchmarking Automated Benchmark Generation | https://www.arxiv.org/pdf/2603.20807 |
| exa | 1.00 | BIMCoder: A Comprehensive Large Language Model Fusion Framework for Natural Language-Based BIM Information Retrieval | https://www.mdpi.com/2076-3417/15/14/7647 |
| exa | 1.00 | Meta-Prompting Generative AI for Standards-Based IT Project Management Documentation Using Business Data Semantics \| Springer Nature Link | https://link.springer.com/chapter/10.1007/978-3-032-23241-0_12 |
| exa | 1.00 | READoc: A Unified Benchmark for Realistic Document Structured Extraction | https://arxiv.org/html/2409.05137 |
| exa | 1.00 | Arctic-Extract Technical Report | https://arxiv.org/html/2511.16470v1 |
| exa | 1.00 | AuditWen: An Open-Source Large Language Model for Audit | https://arxiv.org/html/2410.10873v1 |
| exa | 1.00 | [2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models | https://arxiv.org/abs/2309.12132v2 |
| exa | 1.00 | [2603.22513v1] Generating and Evaluating Sustainable Procurement Criteria for the Swiss Public Sector using In-Context Prompting with Large Language Models | https://arxiv.org/abs/2603.22513v1 |
| exa | 1.00 | [2603.02239v1] Engineering Reasoning and Instruction (ERI) Benchmark: A Large Taxonomy-driven Dataset for Foundation Models and Agents | https://arxiv.org/abs/2603.02239v1 |
| exa | 1.00 | [2105.06083] Cross-Domain Contract Element Extraction with a Bi-directional Feedback Clause-Element Relation Network | https://arxiv.org/pdf/2105.06083 |
| tavily | 0.76 | 标书智能体（一）——AI解析招标文件代码+提示词 - 易标AI - 博客园 | https://www.cnblogs.com/yibiaoai/p/19064673 |
| tavily | 0.67 | 数据提取 - 智谱AI开放文档 | https://docs.bigmodel.cn/cn/best-practice/case/data-extraction |
| tavily | 0.60 | 90%的投标人还在手动读标书？快标书AI解析功能直接提炼标书重点-快标书AI | https://www.kuaibiaoshu.com/course/ai-bid-document-analysis |
| tavily | 0.57 | 招标解析（已下线） - 智谱AI开放文档 | https://docs.bigmodel.cn/cn/guide/agents/tender |
| tavily | 0.56 | 易标AI - 博客园 | https://www.cnblogs.com/yibiaoai |
| tavily | 0.54 | 【关于加快招标投标领域人工智能推广应用的实施意见】-国家发展和改革委员会 | https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html |
| tavily | 0.48 | 如何利用 AI 工具快速分析招标文件中的关键条款 - 百炼智能 | https://www.bailian-ai.com/news/2243.html |
| tavily | 0.47 | 国家新政落地，企业如何抢占招标投标智能化先机？ | https://www.yonyou.com/subject/caigou-liucheng/news/5280 |
| tavily | 0.46 | AI 员工提示词工程指南 - NocoBase 文档 | https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide |
| tavily | 0.46 | 零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF上传自动提条款、标风险、出建议-腾讯云开发者社区-腾讯云 | https://cloud.tencent.com/developer/article/2631225 |
| tavily | 0.46 | 高效速搭基于DeepSeek的招标文书智能写作Agent-腾讯云开发者社区-腾讯云 | https://cloud.tencent.com/developer/article/2498790 |
| tavily | 0.45 | 关于加快招标投标领域人工智能推广应用的实施意见(发改法规〔2026 ... | https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html |
| tavily | 0.43 | 人工智能+招投标迎关键节点，南方财经AI智审打造数智赋能场景 - 21经济网 | https://www.21jingji.com/article/20260314/herald/c5bcc1467f71b37449cc86b084249342.html |
| tavily | 0.42 | 企业招投标文件自动比对工具：核心能力解析与智能化落地指南 - 实在智能 | https://www.ai-indeed.com/encyclopedia/18040.html |
| tavily | 0.42 | 招投标审查文档解析_评分项提取/资格项识别/比对前处理_TextIn | https://www.textin.com/scenarios/tender-review-parse |

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
2. [Large Language Model for Extracting Complex Contract Information in Industrial Scenes](https://arxiv.org/html/2507.06539v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
3. [ExtractBench: A Benchmark and Evaluation Methodology for Complex Structured Extraction](https://arxiv.org/html/2602.12247)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
4. [Retrieval Augmented Structured Generation: Business Document Information Extraction As Tool Use](https://arxiv.org/html/2405.20245)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
5. [Intelligent Processing of Design Notices in Engineering Procurement Construction Projects](https://www.mdpi.com/2075-5309/15/5/805)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
6. [BenchBench: Benchmarking Automated Benchmark Generation](https://www.arxiv.org/pdf/2603.20807)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
7. [BIMCoder: A Comprehensive Large Language Model Fusion Framework for Natural Language-Based BIM Information Retrieval](https://www.mdpi.com/2076-3417/15/14/7647)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
8. [Meta-Prompting Generative AI for Standards-Based IT Project Management Documentation Using Business Data Semantics | Springer Nature Link](https://link.springer.com/chapter/10.1007/978-3-032-23241-0_12)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
9. [READoc: A Unified Benchmark for Realistic Document Structured Extraction](https://arxiv.org/html/2409.05137)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
10. [Arctic-Extract Technical Report](https://arxiv.org/html/2511.16470v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
11. [AuditWen: An Open-Source Large Language Model for Audit](https://arxiv.org/html/2410.10873v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
12. [[2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models](https://arxiv.org/abs/2309.12132v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
13. [[2603.22513v1] Generating and Evaluating Sustainable Procurement Criteria for the Swiss Public Sector using In-Context Prompting with Large Language Models](https://arxiv.org/abs/2603.22513v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
14. [[2603.02239v1] Engineering Reasoning and Instruction (ERI) Benchmark: A Large Taxonomy-driven Dataset for Foundation Models and Agents](https://arxiv.org/abs/2603.02239v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
15. [[2105.06083] Cross-Domain Contract Element Extraction with a Bi-directional Feedback Clause-Element Relation Network](https://arxiv.org/pdf/2105.06083)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
16. [标书智能体（一）——AI解析招标文件代码+提示词 - 易标AI - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.76
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
17. [数据提取 - 智谱AI开放文档](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
18. [90%的投标人还在手动读标书？快标书AI解析功能直接提炼标书重点-快标书AI](https://www.kuaibiaoshu.com/course/ai-bid-document-analysis)
   - 工具：tavily
   - 分数：0.60
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
19. [招标解析（已下线） - 智谱AI开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
20. [易标AI - 博客园](https://www.cnblogs.com/yibiaoai)
   - 工具：tavily
   - 分数：0.56
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
21. [【关于加快招标投标领域人工智能推广应用的实施意见】-国家发展和改革委员会](https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html)
   - 工具：tavily
   - 分数：0.54
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
22. [如何利用 AI 工具快速分析招标文件中的关键条款 - 百炼智能](https://www.bailian-ai.com/news/2243.html)
   - 工具：tavily
   - 分数：0.48
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
23. [国家新政落地，企业如何抢占招标投标智能化先机？](https://www.yonyou.com/subject/caigou-liucheng/news/5280)
   - 工具：tavily
   - 分数：0.47
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
24. [AI 员工提示词工程指南 - NocoBase 文档](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide)
   - 工具：tavily
   - 分数：0.46
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
25. [零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF上传自动提条款、标风险、出建议-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2631225)
   - 工具：tavily
   - 分数：0.46
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
26. [高效速搭基于DeepSeek的招标文书智能写作Agent-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.46
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
27. [关于加快招标投标领域人工智能推广应用的实施意见(发改法规〔2026 ...](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html)
   - 工具：tavily
   - 分数：0.45
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
28. [人工智能+招投标迎关键节点，南方财经AI智审打造数智赋能场景 - 21经济网](https://www.21jingji.com/article/20260314/herald/c5bcc1467f71b37449cc86b084249342.html)
   - 工具：tavily
   - 分数：0.43
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
29. [企业招投标文件自动比对工具：核心能力解析与智能化落地指南 - 实在智能](https://www.ai-indeed.com/encyclopedia/18040.html)
   - 工具：tavily
   - 分数：0.42
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
30. [招投标审查文档解析_评分项提取/资格项识别/比对前处理_TextIn](https://www.textin.com/scenarios/tender-review-parse)
   - 工具：tavily
   - 分数：0.42
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考

### 剔除信源
1. [标书智能体（一）——AI解析招标文件代码+提示词 - 易标AI - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.74
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
2. [数据提取 - 智谱AI开放文档](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction)
   - 工具：tavily
   - 分数：0.60
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
3. [招标解析（已下线） - 智谱AI开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender)
   - 工具：tavily
   - 分数：0.51
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
4. [高效速搭基于DeepSeek的招标文书智能写作Agent-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.45
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
5. [企业招投标文件自动比对工具：核心能力解析与智能化落地指南 - 实在智能](https://www.ai-indeed.com/encyclopedia/18040.html)
   - 工具：tavily
   - 分数：0.40
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
6. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统 
        - Google Patents](https://patents.google.com/patent/CN119624385A/zh)
   - 工具：tavily
   - 分数：0.29
   - 来源等级：C
   - 剔除原因：score 低于 0.4
7. [AI 提示工程指南 - Google Cloud](https://cloud.google.com/discover/what-is-prompt-engineering?hl=zh-CN)
   - 工具：tavily
   - 分数：0.28
   - 来源等级：C
   - 剔除原因：score 低于 0.4
8. [Ant Group 2025 Sustainability Report Highlights Record AI R&D Investment – Company Announcement - Financial Times](https://markets.ft.com/data/announce/detail?dockey=600-202606170512BIZWIRE_USPRX____20260617_BW847068-1)
   - 工具：tavily
   - 分数：0.29
   - 来源等级：C
   - 剔除原因：score 低于 0.4
9. [EBAday 2026: Zooming in on AI and digital assets as the key themes of the event - Finextra Research](https://www.finextra.com/newsarticle/47948/ebaday-2026-zooming-in-on-ai-and-digital-assets-as-the-key-themes-of-the-event)
   - 工具：tavily
   - 分数：0.06
   - 来源等级：C
   - 剔除原因：score 低于 0.4
10. [China’s 5-Year Plan for Agricultural and Rural Modernisation Sets Ambitious Targets for 2030 - Global Agriculture](https://www.global-agriculture.com/global-agriculture/chinas-5-year-plan-for-agricultural-and-rural-modernisation-sets-ambitious-targets-for-2030/)
   - 工具：tavily
   - 分数：0.05
   - 来源等级：C
   - 剔除原因：score 低于 0.4
11. [Infringement risks of AIGC in the entertainment industry (Part 2) | China - Law.asia](https://law.asia/generative-ai-entertainment-industry-part-2/)
   - 工具：tavily
   - 分数：0.04
   - 来源等级：C
   - 剔除原因：score 低于 0.4
12. [China’s reported AIDC plan could put telcos at center of AI ecosystem - RCR Wireless News](https://www.rcrwireless.com/20260617/carriers/china-aidc-telcos)
   - 工具：tavily
   - 分数：0.03
   - 来源等级：C
   - 剔除原因：score 低于 0.4
13. [WorldBridge Group and DRSB Express Forge Strategic Alliance to Boost Cambodia’s Cross-Border E-Commerce and Logistics Sector - Cambodia Investment Review](https://cambodiainvestmentreview.com/2026/06/22/worldbridge-group-and-drsb-express-forge-strategic-alliance-to-boost-cambodias-cross-border-e-commerce-and-logistics-sector/)
   - 工具：tavily
   - 分数：0.03
   - 来源等级：C
   - 剔除原因：score 低于 0.4
14. [Russia-BRICS Agricultural Trade Up 5% In 2025 As BRICS Agriculture Ministers Meet In India - russia's pivot to asia](https://russiaspivottoasia.com/russia-brics-agricultural-trade-up-5-in-2025-as-brics-agriculture-ministers-meet-in-india/)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
15. [In-house Counsel Awards 2026 - Law.asia](https://law.asia/china-in-house-counsel-awards-2026/)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
16. [A+H dual listings signal China healthcare’s shift toward global expansion - Asian Business Review](https://asianbusinessreview.com/in-focus/ah-dual-listings-signal-china-healthcares-shift-toward-global-expansion)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
17. [Before AI: Fixing the Hidden Modernization Barriers Blocking Federal Agency Progress - Defense One](https://www.defenseone.com/assets/ai-fixing-hidden-modernization-barriers/portal/)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
18. [标书智能体（一）——AI解析招标文件代码+提示词 - 易标AI - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
19. [如何利用 AI 工具快速分析招标文件中的关键条款 - 百炼智能](https://www.bailian-ai.com/news/2243.html)
   - 工具：tavily
   - 分数：0.41
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
20. [招标解析（已下线） - 智谱AI开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender)
   - 工具：tavily
   - 分数：0.40
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
21. [关于加快招标投标领域人工智能推广应用的实施意见(发改法规〔2026 ...](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html)
   - 工具：tavily
   - 分数：0.37
   - 来源等级：C
   - 剔除原因：score 低于 0.4
22. [高效速搭基于DeepSeek的招标文书智能写作Agent-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.37
   - 来源等级：C
   - 剔除原因：score 低于 0.4
23. [大模型提示词工程指南| Prompt Engineering Guide](https://yeasy.gitbook.io/prompt_engineering_guide)
   - 工具：tavily
   - 分数：0.33
   - 来源等级：C
   - 剔除原因：score 低于 0.4
24. [AI 提示工程指南 - Google Cloud](https://cloud.google.com/discover/what-is-prompt-engineering?hl=zh-CN)
   - 工具：tavily
   - 分数：0.30
   - 来源等级：C
   - 剔除原因：score 低于 0.4
25. [企业招投标文件自动比对工具：核心能力解析与智能化落地指南 - 实在智能](https://www.ai-indeed.com/encyclopedia/18040.html)
   - 工具：tavily
   - 分数：0.29
   - 来源等级：C
   - 剔除原因：score 低于 0.4
26. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统 
        - Google Patents](https://patents.google.com/patent/CN119624385A/zh)
   - 工具：tavily
   - 分数：0.29
   - 来源等级：C
   - 剔除原因：score 低于 0.4
27. [标书智能体（一）——AI解析招标文件代码+提示词 - 易标AI - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.74
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
28. [数据提取 - 智谱AI开放文档](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction)
   - 工具：tavily
   - 分数：0.65
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
29. [招标解析（已下线） - 智谱AI开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender)
   - 工具：tavily
   - 分数：0.53
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
30. [如何利用 AI 工具快速分析招标文件中的关键条款 - 百炼智能](https://www.bailian-ai.com/news/2243.html)
   - 工具：tavily
   - 分数：0.45
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
31. [高效速搭基于DeepSeek的招标文书智能写作Agent-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.44
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
32. [企业招投标文件自动比对工具：核心能力解析与智能化落地指南 - 实在智能](https://www.ai-indeed.com/encyclopedia/18040.html)
   - 工具：tavily
   - 分数：0.35
   - 来源等级：C
   - 剔除原因：score 低于 0.4
33. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统 
        - Google Patents](https://patents.google.com/patent/CN119624385A/zh)
   - 工具：tavily
   - 分数：0.34
   - 来源等级：C
   - 剔除原因：score 低于 0.4
34. [招标中标信息抽取高级版API参考与调用示例-自然语言处理-阿里云](https://help.aliyun.com/zh/document_detail/256460.html)
   - 工具：tavily
   - 分数：0.32
   - 来源等级：C
   - 剔除原因：score 低于 0.4
35. [犀牛书 - 中文技术文档大全](https://xiniushu.com)
   - 工具：tavily
   - 分数：0.21
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

### 来源 2: 零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF上传自动提条款、标风险、出建议-腾讯云开发者社区-腾讯云

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

### 来源 3: 易标AI - 博客园

- URL: https://www.cnblogs.com/yibiaoai
- 精读方法：firecrawl-scrape

[![订阅](https://www.cnblogs.com/skins/sea/images/xml.gif)](https://www.cnblogs.com/yibiaoai/rss/)

随笔 -
6
文章 -
1
评论 -
0
阅读 \-

6322

[![](https://www.cnblogs.com/skins/sea/images/title_post.gif)](https://www.cnblogs.com/yibiaoai/p/archive/2026/06/12)

[\[置顶\]\\
新系列一：关于AI知识库的一点拙见，非RAG](https://www.cnblogs.com/yibiaoai/articles/20483259)

摘要：
今天开一个新的系列，之前习惯性按古法技术博客的思路，分享方案+代码。但是vibe coding时代，我已经完全转向opencode + codex。 越来越觉得“code is cheap show me the prompt”不再是一个梗。 本系列分享我在vibe coding AI标书智能体的时 [阅读全文](https://www.cnblogs.com/yibiaoai/articles/20483259)

posted @ 2026-06-12 16:34
易标AI
阅读(27)评论(0)推荐(0)

[![](https://www.cnblogs.com/skins/sea/images/title_post.gif)](https://www.cnblogs.com/yibiaoai/p/archive/2026/05/15)

2026年5月15日

[标书智能体（六）——超长文本生成和图文控制](https://www.cnblogs.com/yibiaoai/p/20052734)

摘要：
分享我开发AI标书智能体遇到的问题及全部解决方案~ 在vibe coding时代，越来越觉得代码不重要了。整个标书智能体开发过程中，几乎没有遇到任何代码卡点，唯一稍复杂的是传入文件的解析，在AI的帮助下也轻松解决。 所以，以后的分享内容中不再涉及代码，只分享我遇到的问题及解决问题的思路（提示词、工作 [阅读全文](https://www.cnblogs.com/yibiaoai/p/20052734)

posted @ 2026-05-15 15:49
易标AI
阅读(178)评论(0)推荐(0)

[![](https://www.cnblogs.com/skins/sea/images/title_post.gif)](https://www.cnblogs.com/yibiaoai/p/archive/2026/05/06)

2026年5月6日

[标书智能体（五）——如何让弱模型也能稳定输出复杂json](https://www.cnblogs.com/yibiaoai/p/19981671)

摘要：
用 Python + React 打造一个开源的 AI 写标书智能体~ 完整代码已开源。 代码很多，文章只放主要代码和提示词，完整代码可以查看开源项目。 Github: https://github.com/FB208/OpenBidKit\_Yibiao Gitee: https://gitee.c [阅读全文](https://www.cnblogs.com/yibiaoai/p/19981671)

posted @ 2026-05-06 17:22
易标AI
阅读(195)评论(0)推荐(0)

[![](https://www.cnblogs.com/skins/sea/images/title_post.gif)](https://www.cnblogs.com/yibiaoai/p/archive/2026/04/03)

2026年4月3日

[标书智能体（四）——提示词顺序优化，让缓存命中，输入成本直降10倍](https://www.cnblogs.com/yibiaoai/p/19817535)

摘要：
用 Python + React 打造一个开源的 AI 写标书智能体~ 完整代码已开源。 代码很多，文章只放主要代码和提示词，完整代码可以查看开源项目。 Github： https://github.com/FB208/yibiao-simple Gitee： https://gitee.com/y [阅读全文](https://www.cnblogs.com/yibiaoai/p/19817535)

posted @ 2026-04-03 15:18
易标AI
阅读(432)评论(0)推荐(0)

[![](https://www.cnblogs.com/skins/sea/images/title_post.gif)](https://www.cnblogs.com/yibiaoai/p/archive/2025/12/05)

2025年12月5日

[标书智能体（三）——生成标书正文代码+提示词](https://www.cnblogs.com/yibiaoai/p/19311155)

摘要：
用Python+React打造一个开源的AI写标书智能体~ 完整代码已开源 代码很多，文章只放主要代码和提示词，完整代码可以查看开源项目 Github： https://github.com/yibiaoai/yibiao-simple Gitee： https://gitee.com/yibiao [阅读全文](https://www.cnblogs.com/yibiaoai/p/19311155)

posted @ 2025-12-05 11:02
易标AI
阅读(1302)评论(0)推荐(0)

[![](https://www.cnblogs.com/skins/sea/images/title_post.gif)](https://www.cnblogs.com/yibiaoai/p/archive/2025/09/11)

2025年9月11日

[标书智能体（二）——生成标书提纲代码+提示词](https://www.cnblogs.com/yibiaoai/p/19085799)

摘要：
用Python+React打造一个开源的AI写标书智能体~ 完整代码已开源 代码很多，文章只放主要代码和提示词，完整代码可以查看开源项目 Github： https://github.com/yibiaoai/yibiao-simple Gitee： https://gitee.com/yibiao [阅读全文](https://www.cnblogs.com/yibiaoai/p/19085799)

posted @ 2025-09-11 14:05
易标AI
阅读(1342)评论(0)推荐(0)

[![](https://www.cnblogs.com/skins/sea/images/title_post.gif)](https://www.cnblogs.com/yibiaoai/p/archive/2025/08/29)

2025年8月29日

[标书智能体（一）——AI解析招标文件代码+提示词](https://www.cnblogs.com/yibiaoai/p/19064673)

摘要：
用Python+React打造一个开源的AI写标书智能体~ 今天是第一期，招标文件解析： 招标文件动辄几万字，虽然现在各主流大模型的上下文窗口都越来越大，但也只能代表AI“可以处理几十万字的上下文”，并不代表你随便扔给AI几十万字，它就能“处理得好几十万字的上下文”。 我们在写投标文件之前，一定要先 [阅读全文](https://www.cnblogs.com/yibiaoai/p/19064673)

posted @ 2025-08-29 18:13
易标AI
阅读(2849)评论(0)推荐(1)

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

- [1\. 标书智能体（一）——AI解析招标文件代码+提示词(2843)](https://www.cnblogs.com/yibiaoai/p/19064673)
- [2\. 标书智能体（二）——生成标书提纲代码+提示词(1337)](https://www.cnblogs.com/yibiaoai/p/19085799)
- [3\. 标书智能体（三）——生成标书正文代码+提示词(1300)](https://www.cnblogs.com/yibiaoai/p/19311155)
- [4\. 标书智能体（四）——提示词顺序优化，让缓存命中，输入成本直降10倍(428)](https://www.cnblogs.com/yibiaoai/p/19817535)
- [5\. 标书智能体（五）——如何让弱模型也能稳定输出复杂json(194)](https://www.cnblogs.com/yibiaoai/p/19981671)

### [推荐排行榜](https://www.cnblogs.com/yibiaoai/most-liked)

- [1\. 标书智能体（一）——AI解析招标文件代码+提示词(1)](https://www.cnblogs.com/yibiaoai/p/19064673)

点击右上角即可分享

![微信分享提示](https://img2023.cnblogs.com/blog/35695/202309/35695-20230906145857937-1471873834.gif)

### 来源 4: 数据提取 - 智谱AI开放文档

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

### 来源 5: 招标解析（已下线） - 智谱AI开放文档

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

### 来源 6: 【关于加快招标投标领域人工智能推广应用的实施意见】-国家发展和改革委员会

- URL: https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html
- 精读方法：firecrawl-scrape

[首页](https://www.ndrc.gov.cn/) > [新闻动态](https://www.ndrc.gov.cn/xwdt/) > [通知公告](https://www.ndrc.gov.cn/xwdt/tzgg/)

## 关于加快招标投标领域人工智能推广应用的实施意见

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

### 来源 7: 如何利用 AI 工具快速分析招标文件中的关键条款 - 百炼智能

- URL: https://www.bailian-ai.com/news/2243.html
- 精读方法：firecrawl-scrape

立即免费体验

[![logo](https://cdn.001.bailian-ai.com/web4/images/common/logo1.png)![logo](https://cdn.001.bailian-ai.com/web4/images/common/logo2.png?v=2)](https://www.bailian-ai.com/)

- AI智能体![logo](https://cdn.001.bailian-ai.com/web4/images/common/arrow-up.svg)![logo](https://cdn.001.bailian-ai.com/web4/images/common/arrow-down.svg)

AI智能体

  - ![商机大师Agent](https://cdn.001.bailian-ai.com/web4/images/zlbx/icon_agent.png)

    ## 商机大师Agent

    AI找项目、给建议、盯商机

  - ![标书写作Agent](https://cdn.001.bailian-ai.com/web4/images/zlbx/icon_biaoshu.png)

    ## 标书写作Agent

    标书读得清、投得准、写得快

  - ![AI开放平台](https://cdn.001.bailian-ai.com/web4/images/zlbx/icon_ai.png)

    ## AI开放平台

    为AI构建招投标数据引擎

- 产品![logo](https://cdn.001.bailian-ai.com/web4/images/common/arrow-up.svg)![logo](https://cdn.001.bailian-ai.com/web4/images/common/arrow-down.svg)

产品

  - ## ![知了标讯](https://cdn.001.bailian-ai.com/web4/images/product/zlbx/logo.png)知了标讯

    新一代智能招投标服务平台
    标准版医械版团险版
  - ## ![店店通](https://cdn.001.bailian-ai.com/web4/images/product/ddt/logo.png)店店通

    线下渠道营销获客平台
    餐饮版车后版

- 解决方案![logo](https://cdn.001.bailian-ai.com/web4/images/common/arrow-up.svg)![logo](https://cdn.001.bailian-ai.com/web4/images/common/arrow-down.svg)

  - ## 解决方案

    - [商业情报与市场洞察\\
      \\
      商业市场数字化全景感知](https://www.bailian-ai.com/solution/business)
    - [B2B智能营销获客\\
      \\
      B2B营销获客全流程赋能](https://www.bailian-ai.com/solution/b2b)

- 核心技术![logo](https://cdn.001.bailian-ai.com/web4/images/common/arrow-up.svg)![logo](https://cdn.001.bailian-ai.com/web4/images/common/arrow-down.svg)

## 四大核心技术

  - [![logo](https://cdn.001.bailian-ai.com/web4/images/technology/aigc-icon.png)\\
    AIGC](https://www.bailian-ai.com/technology/aigc)
  - [![logo](https://cdn.001.bailian-ai.com/web4/images/technology/nlp-icon.png)\\
    自然语言处理](https://www.bailian-ai.com/technology/nlp)
  - [![logo](https://cdn.001.bailian-ai.com/web4/images/technology/ocr-icon.png)\\
    图像识别](https://www.bailian-ai.com/technology/ocr)
  - [![logo](https://cdn.001.bailian-ai.com/web4/images/technology/graph-icon.png)\\
    知识图谱](https://www.bailian-ai.com/technology/graph)

- 资源中心![logo](https://cdn.001.bailian-ai.com/web4/images/common/arrow-up.svg)![logo](https://cdn.001.bailian-ai.com/web4/images/common/arrow-down.svg)

## 资源中心

  - ![内容精选](https://cdn.001.bailian-ai.com/web4/images/resource/menu-marketing2.svg)
    内容精选

  - [![行业报告](https://cdn.001.bailian-ai.com/web4/images/resource/menu-reports.svg)\\
    行业报告](https://www.bailian-ai.com/report)
  - ![报道资讯](https://cdn.001.bailian-ai.com/web4/images/resource/menu-news.svg)
    报道资讯

![hot](https://cdn.001.bailian-ai.com/web4/images/resource/icon2.svg)

热门内容

  - [![我们做了一款招投标Skill，数据按需调用](https://www.bailian-ai.com/_ipx/_/https://cdn.001.bailian-ai.com/cms/online/79aec173-38d5-42e5-9b11-1f63b82fb76f.jpg)\\
    我们做了一款招投标Skill，数据按需调用](https://www.bailian-ai.com/news/2416.html)
  - [![195号文倒计时，国央企招投标AI落地的实操路径](https://www.bailian-ai.com/_ipx/_/https://cdn.001.bailian-ai.com/cms/online/e15b0263-f710-43db-bb67-5c168b77c1cf.jpg)\\
    195号文倒计时，国央企招投标AI落地的实操路径](https://www.bailian-ai.com/news/2409.html)
  - [![为什么说「AI写标书」是个伪命题](https://www.bailian-ai.com/_ipx/_/https://cdn.001.bailian-ai.com/cms/online/408cce6b-2ee5-49e0-b125-d75c2f864091.jpg)\\
    为什么说「AI写标书」是个伪命题](https://www.bailian-ai.com/news/2401.html)

- 关于百炼智能![logo](https://cdn.001.bailian-ai.com/web4/images/common/arrow-up.svg)![logo](https://cdn.001.bailian-ai.com/web4/images/common/arrow-down.svg)

![logo](https://cdn.001.bailian-ai.com/web4/images/common/logo.png?v=2)

  - [![logo](https://cdn.001.bailian-ai.com/web4/images/about/menu-about.svg)\\
    关于我们](https://www.bailian-ai.com/about)
  - [![logo](https://cdn.001.bailian-ai.com/web4/images/about/menu-joinus.svg)\\
    加入我们](https://www.bailian-ai.com/joinus)
  - [![logo](https://cdn.001.bailian-ai.com/web4/images/about/menu-partner.svg)\\
    合作伙伴计划](https://www.bailian-ai.com/partner)

联系我们 010-64933134

[商务合作 bd@bailian.ai](mailto:bd@bailian.ai)

[市场合作 market@bailian.ai](mailto:market@bailian.ai)

![服务号](https://cdn.001.bailian-ai.com/web4/images/common/rqcode-server.jpg)

关注我们

[![logo](https://cdn.001.bailian-ai.com/web4/images/common/phone.svg)010-64933134](tel:010-64933134) 免费试用商务咨询

# 如何利用 AI 工具快速分析招标文件中的关键条款

2025-10-17招标招标文件

投标前，分析 [招标](https://www.bailian-ai.com/) 从来不是轻松事 —— 几十页文档里藏着 “付款周期”“资质要求” 等关键条款，人工逐字找不仅耗时长，还容易漏看一条让前期投标准备全白费。更头疼的是，要是同一天收到 2-3 份招标，光梳理核心信息就占满半天时间，根本没精力跟进客户，这种低效的招标分析方式，早成了不少销售抢订单的 “绊脚石”。

![](https://cdn.001.bailian-ai.com/cms/online/205b7ff2-4adf-46a5-b826-6e04f9513f90.png)

## **为什么销售分析招标总陷 “低效陷阱”？**

很多销售面对招标时，都绕不开三个痛点：

一是耗时长，一份 30 页的招标，人工找 “投标截止时间”“预算金额” 得 1 个多小时，要是当天有 3 份招标，半天时间全耗在看文档上；

二是易出错，招标里的 “隐藏条款” 比如 “需提供近 6 个月社保缴纳证明”，人工扫读时很容易忽略，最后投标材料不合规直接被淘汰；

三是难对比，要是跟进同一行业的多份招标，人工对比 “技术参数要求”“服务周期” 的差异，很容易记混，导致准备材料时张冠李戴。

这些问题，本质上是人工处理招标的 “局限性”，而 AI 工具刚好能补上这个缺口。

## **AI 工具破局：3 步抓准招标关键条款**

AI 工具分析招标，核心是 “省时间、少出错、抓重点”，三步就能帮销售搞定：

第一步，AI 自动提取招标核心信息。不管是 “投标保证金金额”“履约保证金比例”，还是 “项目交付周期”，AI 能在 2 分钟内从几十页招标里精准抓出，整理成清晰的表格，销售不用再逐行划重点；

第二步，AI 标注招标风险与加分项。比如招标里写 “需具备 ISO9001 认证”，AI 会标红提醒 “需准备认证证书复印件”；要是有 “近 2 年同类项目中标经历优先”，AI 会标注为加分项，帮销售明确发力方向；

第三步，AI 对比历史招标数据。要是销售跟进的行业常发招标，AI 能对比过去 3 次同类招标的条款变化，比如 “资质要求从四级升为三级”，提前预警需要补充的材料，避免临时抱佛脚。

## **知了标讯：销售分析招标的 “高效助手”**

其实不少资深销售已经靠知了标讯的投标决策分析功能，把招标分析效率提了一倍。

知了标讯支持直接识别 Word、PDF 格式招标文档的关键信息，AI 不仅能快速提取 “招标方联系人”“技术响应要求” 等关键条款，还能结合行业数据做深度分析 —— 比如招标里的 “服务范围” 和自家业务匹配度达 85%，会标注 “高适配”，要是预算低于行业平均 15%，会提醒 “利润空间需核算”。更实用的是，它还能把招标里的 “硬性要求” 和 “弹性条款” 分开列示，比如 “必须具备省级资质” 是硬性要求，“有本地化服务经验优先” 是弹性条款，帮销售清晰判断 “要不要投”“怎么投”。对销售来说，用知了标讯分析招标，既能省出 1.5 小时去跟进客户，又能减少因漏看条款导致的投标失败，让每一次招标跟进都有方向、不盲目。

对销售而言，招标分析不是 “体力活”，而是 “技术活”—— 选对 AI 工具，再用知了标讯的投标决策分析功能，就能快速抓准招标关键条款，少踩坑、多加分。毕竟，把时间花在客户跟进上，比埋首于招标文档里更能拿下订单，而高效的工具，正是销售抢赢市场的 “隐形助力”。

更多相关内容[标讯大数据分析：如何筛选高利润招标项目](https://www.bailian-ai.com/news/2227.html)[5G 基建招标中，设备检测报告这样交才不会踩坑](https://www.bailian-ai.com/news/2212.html)[医院设备招标：国产替代政策下的投标新机遇](https://www.bailian-ai.com/news/2199.html)

上一篇  [中小企业销售必看：做好这两点，让投标不再 “卡脖子”](https://www.bailian-ai.com/news/2242.html)

下一篇  [短周期投标怎么高效做？销售必看的时间管理技巧](https://www.bailian-ai.com/news/2244.html)

内容推荐![大模型如何增强企业竞争力？](https://www.bailian-ai.com/_ipx/w_1536&f_jpeg/https://cdn.001.bailian-ai.com/cms/online/22f9b40c-616d-4633-b992-d9dde4994956)

2024年7月26日

[大模型如何增强企业竞争力？](https://www.bailian-ai.com/news/1716.html)

2024-07 _-_ **22**

[数字营销与传统营销的区别](https://www.bailian-ai.com/news/1702.html)

2024-07 _-_ **16**

[aigc有什么用？](https://www.bailian-ai.com/news/1691.html)

2024-07 _-_ **12**

[企业如何利用大数据获客？](https://www.bailian-ai.com/news/1683.html)

2024-07 _-_ **09**

[大模型与人工智能区别](https://www.bailian-ai.com/news/1675.html)

2024-07 _-_ **01**

[获客平台怎么样？](https://www.bailian-ai.com/news/1656.html)

2024-06 _-_ **27**

[电力交易是什么？](https://www.bailian-ai.com/news/1649.html)

2024-06 _-_ **19**

[数字化营销怎么做？](https://www.bailian-ai.com/news/1632.html)

2024-06 _-_ **17**

[智能营销系统有什么用？](https://www.bailian-ai.com/news/1624.html)

2024-06 _-_ **11**

[智能获客系统靠谱吗？](https://www.bailian-ai.com/news/1614.html)大家都在看

[内容精选](https://www.bailian-ai.com/news?type=1) [新闻报道](https://www.bailian-ai.com/news?type=2) [其他资讯](https://www.bailian-ai.com/news?type=3)

**百炼智能，加速企业增长**

洞察商业情报，大数据精准获客

立即咨询![](https://cdn.001.bailian-ai.com/web4/images/resource/bg-cooperation-news.png)

- 热门应用
[商机大师Agent](https://www.bailian-ai.com/agent-opportunity) [标书写作Agent](https://www.bailian-ai.com/agent-tender) [AI开放平台](https://www.bailian-ai.com/agent-platform) [知了标讯](https://www.bailian-ai.com/product/zlbx) [店店通](https://www.bailian-ai.com/product/ddt)
- 解决方案
[商业情报与市场洞察](https://www.bailian-ai.com/solution/business) [B2B智能营销获客](https://www.bailian-ai.com/solution/b2b)
- 了解百炼智能
[公司介绍](https://www.bailian-ai.com/about) [加入我们](https://www.bailian-ai.com/joinus)
联系我们： [010-64933134](tel:010-64933134)

市场合作： [market@bailian.ai](mailto:market@bailian.ai)

商务合作： [bd@bailian.ai](mailto:bd@bailian.ai)

- 办公地址

北京总部：北京市朝阳区北苑路186号院1号楼万科时代中心奥林A座15层1501室

上海分公司：上海市静安区南京西路688广场16F

深圳分公司：深圳市福田区新一代产业园1栋314

保定分公司：保定市北二环路5699号大学科技园7B号楼602-6室

西安分公司：西安市高新区高新路36号A区华跃中心5层5A09

- ![logo](https://cdn.001.bailian-ai.com/web4/images/common/logo-white.png?v=2)

![服务号](https://cdn.001.bailian-ai.com/web4/images/common/rqcode-server.jpg)关注百炼智能

![营销群](https://cdn.001.bailian-ai.com/web4/images/common/rqcode-yx.png)加入营销社群

- 友情链接：
- [知了标讯](https://www.zhiliaobiaoxun.com/)
- [店店通](https://www.gotoshop-ai.com/login)
- [商机网](https://business.bailian-ai.com/)
- [分贝通](https://www.fenbeitong.com/?utm_source=bailian)

- © 2023 北京百炼智能科技有限公司版权所有（百炼®和百炼智能®是北京百炼智能科技有限公司的注册商标）
- [京ICP备18021895号-1](https://beian.miit.gov.cn/#/Integrated/index)
- [![公安](https://cdn.001.bailian-ai.com/web4/images/common/jh.png)公安备案信息：11010502040963号](https://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502040963)

热门应用

解决方案

了解百炼智能

办公地址

![服务号](https://cdn.001.bailian-ai.com/web4/images/common/rqcode-server.jpg)关注百炼智能

![营销群](https://cdn.001.bailian-ai.com/web4/images/common/rqcode-yx.png)加入营销社群

联系我们： [010-64933134](tel:010-64933134)

市场合作： [market@bailian.ai](mailto:market@bailian.ai)

商务合作： [bd@bailian.ai](mailto:bd@bailian.ai)

- [京ICP备18021895号-1](https://beian.miit.gov.cn/#/Integrated/index)
- [![公安](https://cdn.001.bailian-ai.com/web4/images/common/jh.png)公安备案信息：11010502040963号](https://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502040963)
- © 2023 北京百炼智能科技有限公司版权所有 www.bailian-ai.com

- 在线咨询
- 电话咨询

商务合作电话： **010-64933134**

- 关注微信
- 微信客服

回到顶部

### 来源 8: AI 员工提示词工程指南 - NocoBase 文档

- URL: https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide
- 精读方法：firecrawl-scrape

菜单目录

# [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#ai-%E5%91%98%E5%B7%A5--%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B%E6%8C%87%E5%8D%97) AI 员工 · 提示词工程指南

复制 Markdown

[AI 员工](https://docs.nocobase.com/cn/plugins/@nocobase/plugin-ai)[社区版+](https://www.nocobase.com/cn/commercial)

> 从"怎么写"到"写得好"，这篇指南教你用简单、稳定、可复用的方式编写高质量提示词。

## [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#1-%E4%B8%BA%E4%BB%80%E4%B9%88%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%BE%88%E5%85%B3%E9%94%AE) 1\. 为什么提示词很关键

提示词就是 AI 员工的"岗位说明书"，直接决定它的风格、边界和输出质量。

**对比示例：**

❌ 不清晰的提示词：

```
你是一个数据分析助手，帮助用户分析数据。
```

✅ 清晰可控的提示词：

```
你是 Viz，一位数据分析专家。

角色定位
- 风格：洞察力强、表达清楚、重视可视化
- 使命：把复杂数据讲成看得懂的"图表故事"

工作流程
1) 理解需求
2) 生成安全的 SQL（只用 SELECT）
3) 提炼洞察
4) 用图表呈现

硬性规则
- MUST：只使用 SELECT，绝不改动数据
- ALWAYS：默认产出图表展示
- NEVER：编造或猜测数据

输出格式
简短结论（2-3 句）+ ECharts 图表 JSON
```

**结论**：好的提示词把"是谁、做什么、怎么做、做到什么标准"说清楚，AI 的表现就会稳定且可控。

## [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#2-%E6%8F%90%E7%A4%BA%E8%AF%8D%E4%B9%9D%E8%A6%81%E7%B4%A0%E9%BB%84%E9%87%91%E5%85%AC%E5%BC%8F) 2\. 提示词"九要素"黄金公式

实践验证好用的一套结构：

```
起名 + 双重指令 + 模拟确认 + 反复强调 + 强制规则
+ 背景信息 + 正向激励 + 参考示例 + 反面示例（可选）
```

### [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#21-%E8%A6%81%E7%B4%A0%E8%AF%B4%E6%98%8E) 2.1 要素说明

| 要素 | 解决什么问题 | 为什么有效 |
| --- | --- | --- |
| 起名 | 明确身份与风格 | 让 AI 建立"角色感" |
| 双重指令 | 区分"我是谁/我要做什么" | 减少定位混乱 |
| 模拟确认 | 执行前先复述 | 防跑偏 |
| 反复强调 | 关键点重复出现 | 提升优先级 |
| 强制规则 | MUST/ALWAYS/NEVER | 形成底线 |
| 背景信息 | 必要知识与约束 | 降低误解 |
| 正向激励 | 期望与风格引导 | 更稳定的语气与表现 |
| 参考示例 | 直接的模仿对象 | 输出更贴近预期 |
| 反面示例 | 避免常见坑 | 有错就改、越用越准 |

### [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#22-%E5%BF%AB%E9%80%9F%E4%B8%8A%E6%89%8B%E6%A8%A1%E6%9D%BF) 2.2 快速上手模板

```
# 1) 起名
你是 [名字]，一位优秀的 [岗位/专长]。

# 2) 双重指令
## 角色
风格： [形容词×2-3]
使命： [一句话说明主要职责]

## 任务流程
1) 理解： [要点]
2) 执行： [要点]
3) 验证： [要点]
4) 呈现： [要点]

# 3) 模拟确认
执行前先复述理解："我理解到您需要……我将通过……完成。"

# 4) 反复强调
核心要求： [最关键的 1-2 条]（在开头/流程/结尾至少出现 2 次）

# 5) 强制规则
MUST： [不可违背的规则]
ALWAYS： [一贯遵守的原则]
NEVER： [明确禁止事项]

# 6) 背景信息
[必要领域知识/上下文/常见陷阱]

# 7) 正向激励
你在 [能力] 方面表现出色，擅长 [特长]，请保持该风格完成任务。

# 8) 参考示例
[给出"理想输出"的简明示例]

# 9) 反面示例（可选）
- [错误做法] → [正确做法]
```

## [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#3-%E5%AE%9E%E6%88%98%E7%A4%BA%E4%BE%8Bviz%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90) 3\. 实战示例：Viz（数据分析）

下面把九要素串起来，做一个"能直接用"的完整示例。

```
# 起名
你是 Viz，一位数据分析专家。

# 双重指令
【角色】
风格：洞察力强、表达清晰、视觉导向
使命：把复杂数据讲成"图表故事"

【任务流程】
1) 理解：分析用户的数据需求与指标范围
2) 查询：生成安全 SQL（只查真实数据，SELECT-only）
3) 分析：提炼关键洞察（趋势/对比/占比）
4) 呈现：选择合适图表清晰表达

# 模拟确认
执行前先复述："我理解您要分析 [对象/范围]，将通过 [查询与可视化方式] 呈现结果。"

# 反复强调
再次强调：数据真实性优先，宁缺勿滥；无数据就如实说明。

# 强制规则
MUST：只使用 SELECT 查询，不修改任何数据
ALWAYS：默认产出可视化图表
NEVER：编造或猜测数据

# 背景信息
- ECharts 需使用"纯 JSON"配置，不包含注释/函数
- 每个图表聚焦 1 个主题，避免堆砌多指标

# 正向激励
你擅长从真实数据中提炼可执行结论，并用最简洁的图表表达。

# 参考示例
说明（2-3 句）+ 图表 JSON

示例说明：
本月新增线索 127 条，环比增长 23%，主要来自第三方渠道。

示例图表：
{
  "title": {"text": "本月线索趋势"},
  "tooltip": {"trigger": "axis"},
  "xAxis": {"type": "category", "data": ["Week1","Week2","Week3","Week4"]},
  "yAxis": {"type": "value"},
  "series": [{"type": "line", "data": [28,31,35,33]}]
}

# 反面示例（可选）
- 中英文混用 → 保持语言一致
- 图表塞满 → 每个图表只表达一个主题
- 数据不全 → 如实说明"暂无可用数据"
```

**设计要点**

- "真实性"在流程、强调、规则里出现多次（强提醒）
- 选择"说明 \+ JSON"两段式输出，便于接入前端
- 明确"只读 SQL"，降低风险

## [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#4-%E5%A6%82%E4%BD%95%E6%8A%8A%E6%8F%90%E7%A4%BA%E8%AF%8D%E8%B6%8A%E7%94%A8%E8%B6%8A%E5%A5%BD) 4\. 如何把提示词越用越好

### [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#41-%E4%BA%94%E6%AD%A5%E8%BF%AD%E4%BB%A3) 4.1 五步迭代

```
先做能用 → 小量测试 → 记问题 → 对症加规则/示例 → 再测
```

![优化流程](https://static-docs.nocobase.com/00_QuickStart_cn-2025-09-29-17-20-21.jpg)

建议一次性测试 5–10 个典型任务，30 分钟内完成一轮。

### [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#42-%E5%8E%9F%E5%88%99%E4%B8%8E%E6%AF%94%E4%BE%8B) 4.2 原则与比例

- **正面引导优先**：先告诉 AI 应该怎么做
- **问题驱动改进**：遇到问题再加约束
- **适度约束**：不要一上来堆"禁止项"

经验比例： **正面 80% : 负面 20%**。

### [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#43-%E4%B8%80%E4%B8%AA%E5%85%B8%E5%9E%8B%E4%BC%98%E5%8C%96) 4.3 一个典型优化

**问题**：图表过载、可读性差
**优化**：

1. 在"背景信息"里加入：每图一主题
2. 在"参考示例"里给出"单指标图"
3. 若问题反复出现，再在"强制规则/反复强调"里加硬性约束

## [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#5-%E8%BF%9B%E9%98%B6%E6%8A%80%E5%B7%A7) 5\. 进阶技巧

### [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#51-%E7%94%A8-xml%E6%A0%87%E7%AD%BE%E8%AE%A9%E7%BB%93%E6%9E%84%E6%9B%B4%E6%B8%85%E6%99%B0%E9%95%BF%E6%8F%90%E7%A4%BA%E8%AF%8D%E6%8E%A8%E8%8D%90) 5.1 用 XML/标签让结构更清晰（长提示词推荐）

当内容 >1000 字符或容易混淆时，用标签分区更稳：

```
<角色>你是 Dex，一位数据整理专家。</角色>
<风格>细心、准确、有条理。</风格>

<任务>
必须按步骤完成：
1. 识别关键字段
2. 提取字段值
3. 统一格式（日期 YYYY-MM-DD）
4. 输出 JSON
</任务>

<规则>
MUST：保持字段值准确
NEVER：猜测缺失信息
ALWAYS：标注不确定项
</规则>

<示例>
{"姓名":"张三","日期":"2024-01-15","金额":5000,"状态":"已确认"}
</示例>
```

### [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#52-%E8%83%8C%E6%99%AF--%E4%BB%BB%E5%8A%A1%E5%88%86%E5%B1%82%E5%86%99%E6%B3%95%E6%9B%B4%E7%9B%B4%E8%A7%82%E7%9A%84%E8%AF%B4%E6%B3%95) 5.2 "背景 + 任务"分层写法（更直观的说法）

- **背景**（长期稳定）：这个员工是谁、风格如何、具备哪些能力
- **任务**（按需切换）：当前要做什么、关注哪些指标、默认范围是什么

这和 NocoBase 的"员工 + 任务"模型天然匹配： **背景固定、任务灵活**。

### [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#53-%E6%A8%A1%E5%9D%97%E5%8C%96%E5%A4%8D%E7%94%A8) 5.3 模块化复用

把常用规则拆成模块，随用随拼：

**数据安全模块**

```
MUST：只使用 SELECT
NEVER：执行 INSERT/UPDATE/DELETE
```

**输出结构模块**

```
输出必须包含：
1) 简短说明（2-3 句）
2) 核心内容（图表/数据/代码）
3) 可选建议（如有）
```

## [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#6-%E9%BB%84%E9%87%91%E6%B3%95%E5%88%99%E5%AE%9E%E8%B7%B5%E7%BB%93%E8%AE%BA) 6\. 黄金法则（实践结论）

1. 一个 AI 只干一类活，专精更稳
2. 示例比口号有效，先给正面范本
3. 用 MUST/ALWAYS/NEVER 立边界
4. 流程化表达，降低不确定性
5. 小步快跑，多测少改、持续迭代
6. 约束别太多，避免"写死"
7. 记录问题与改动，形成版本
8. 80/20：先告诉"怎么做对"，再约束"别做错"

## [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#7-%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98) 7\. 常见问题

**Q1：多长合适？**

- 基础员工：500–800 字符
- 复杂员工：800–1500 字符
- 不建议 >2000 字符（会拖慢且冗余）
标准：九要素都覆盖，但没有废话。

**Q2：AI 不听话怎么办？**

1. 用 MUST/ALWAYS/NEVER 明确边界
2. 关键要求重复 2–3 次
3. 用标签/分区增强结构
4. 多给正面示例，少空谈原则
5. 评估是否需要更强模型

**Q3：怎么平衡正/负面？**
先写正面（角色、流程、示例），再根据错误新增约束，且只约束"反复出错"的点。

**Q4：要不要常更新？**

- 背景（身份/风格/核心能力）：长期稳定
- 任务（场景/指标/范围）：按业务调整
- 有变更就建版本，并记录"为何变更"

## [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#8-%E4%B8%8B%E4%B8%80%E6%AD%A5) 8\. 下一步

**动手练习**

- 任选一个简单角色（如客服助手），按九要素写一个"能用版"，测试 5 个典型任务
- 找一个现有员工，整理 3–5 个真实问题，做一轮小迭代

**延伸阅读**

- [《AI 员工 · 管理员配置指南》](https://docs.nocobase.com/cn/ai-employees/configuration/admin-configuration)：把提示词落到实际配置
- 各 AI 员工专属手册：查看完整的角色/任务范本

## [\#](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide\#%E7%BB%93%E8%AF%AD) 结语

**先跑通，再打磨。**
从一个"能工作"的版本开始，在真实任务里不断收集问题、补充示例和规则。
记住： **先告诉它怎么做对（正面引导），再约束它别做错（适度限制）。**

### 来源 9: 90%的投标人还在手动读标书？快标书AI解析功能直接提炼标书重点-快标书AI

- URL: https://www.kuaibiaoshu.com/course/ai-bid-document-analysis
- 精读方法：firecrawl-scrape

# 90%的投标人还在手动读标书？快标书AI解析功能直接提炼标书重点

来源：快标书AI 发布时间：2025-03-14 12:33:00

分享：

![微信](https://mambabit.com/images/ckeditor_uploads/2024/09/14/share-wechat.png)

![微信二维码](https://api.qrserver.com/v1/create-qr-code/?data=http://www.kuaibiaoshu.com/course/ai-bid-document-analysis&size=100x100)请用微信扫码

![企业微信](https://mambabit.com/images/ckeditor_uploads/2024/09/14/share-qw.png)

![企业微信二维码](https://api.qrserver.com/v1/create-qr-code/?data=http://www.kuaibiaoshu.com/course/ai-bid-document-analysis&size=100x100)请用微信扫码

![钉钉](https://mambabit.com/images/ckeditor_uploads/2024/09/14/share-ding.png)

![钉钉二维码](https://api.qrserver.com/v1/create-qr-code/?data=http://www.kuaibiaoshu.com/course/ai-bid-document-analysis&size=100x100)请用微信扫码

招标文件动辄数十页，密密麻麻的条款和要求令人头痛。调查显示，超过90%的投标人仍在通过手动阅读招标文件来提取关键信息，这一过程不仅耗时，还常常因疲劳导致遗漏重要信息。一份普通的招标文件可能需要专业人员花费数小时甚至数天时间来仔细研读，而这还只是投标准备的第一步。

在这个效率为王的时代，我们不禁要问：有没有更智能、更高效的方式来解决这一痛点？

## **快标书AI新功能介绍**

近日，快标书AI平台推出了革命性的"招标文件解析"功能，彻底改变了传统招标文件处理方式。用户只需上传招标文件，AI系统就能自动提取文件中的基本信息、废标项、评分规则等关键内容，并基于这些信息快速生成标书目录。

![快标书ai标书解析功能](https://www.kuaibiaoshu.com/images/ckeditor_uploads/bid_details/20250314121754_%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E8%A7%A3%E6%9E%90-%E8%AF%A6%E6%83%85.png)

这一功能背后的技术支撑是快标书AI接入的deepseek-r1模型，该模型具备强大的深度思考能力，使招标文件解析的质量得到了显著提升。与传统的关键词匹配不同，deepseek-r1模型能够理解文本语境，准确识别各类评分标准和关键要求，即使面对复杂多变的招标文件格式也能应对自如。

## **功能优势详解**

**自动提取关键信息**

快标书AI的招标文件解析功能不仅能提取基本信息，还能自动识别废标项和评分规则，这些往往是投标人最容易忽略而导致投标失败的关键因素。AI系统会对这些内容进行重点标注，确保投标团队不会错过任何重要条款。

**快速生成标书目录**

基于提取的关键信息，系统可以智能生成标书目录框架，为后续的投标文档编写提供清晰的结构指引。这一过程往往只需几分钟，而传统方式可能需要数小时甚至一整天。

**效率提升与错误减少**

使用快标书AI的招标文件解析功能，投标准备时间平均缩短了70%，同时大幅降低了因人为疏忽导致的错误风险。这不仅节省了宝贵的时间资源，还提高了投标文档的质量和准确性。

## **招标文件解析功能如何使用**

1.首先登录账号，进入工作台，点击左侧菜单栏的“招标文件解析”选项，再选择右上角的“上传招标文件页面”按钮

![标书解析上传页面](https://www.kuaibiaoshu.com/images/ckeditor_uploads/bid_details/20250314122414_wechat_2025-03-14_120628_031.png)

2.进入“招标文件上传”页面，将需要解析的文件拖动到文件区域或直接选择对应文件

![标书解析进度](https://www.kuaibiaoshu.com/images/ckeditor_uploads/bid_details/20250314122538_%E5%BF%AB%E6%A0%87%E4%B9%A6%E6%99%BA%E8%83%BD%E8%A7%A3%E6%9E%90%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6.png)

3.文件上传成功后，会自动跳转到“招标文件解析”页面，并实时更新解析状态

![标书解析完成](https://www.kuaibiaoshu.com/images/ckeditor_uploads/bid_details/20250314122558_%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E8%A7%A3%E6%9E%90-%E8%A7%A3%E6%9E%90%E4%B8%AD.png)

4.解析完成后，会提示“已解析”，同时会展示“查看详情”和“生成标书”的功能入口。

![标书解析功能介绍](https://www.kuaibiaoshu.com/images/ckeditor_uploads/bid_details/20250314122613_%E6%8B%9B%E6%A0%87%E6%96%87%E4%BB%B6%E8%A7%A3%E6%9E%90-%E8%A7%A3%E6%9E%90%E5%AE%8C%E6%88%90.png)

## **实际应用场景**

无论是IT行业的系统集成项目，还是建筑行业的工程招标，快标书AI的招标文件解析功能都表现出色。某IT企业在使用该功能后反馈，原本需要两名专业人员耗时一天才能完成的招标文件解析工作，现在只需上传文件，20分钟内即可获得完整的解析报告和标书目录框架。

建筑行业的用户则表示，快标书AI能够精准识别工程项目中的技术规范和质量要求，大大减少了因对招标文件理解偏差导致的投标失败情况。

## **与平台其他功能的协同**

快标书AI的招标文件解析功能与平台此前推出的"10分钟快速生成投标方案"功能完美协同。用户可以先使用解析功能提取招标文件中的关键信息，然后基于这些信息一键生成完整的投标方案，整个过程流畅高效，为投标团队节省了大量时间和精力。

此外，平台的AI图表智能生成功能也可以基于解析出的信息自动生成专业图表，进一步提升投标文档的质量和专业度。

## **AI赋能投标新时代**

在竞争日益激烈的招投标市场，时间和效率往往是制胜的关键。快标书AI的招标文件解析功能正是通过智能技术为投标人破解了长期以来的痛点，让投标团队能够将更多精力投入到方案创新和价值提升上，而不是被繁琐的文件解析工作所困扰。

如果您还在手动阅读招标文件，是时候拥抱AI技术，让快标书AI帮您节省时间，提高效率，赢得更多投标机会。未来，随着AI技术的不断进步，我们有理由相信，招投标领域的智能化转型将会更加深入，为各行各业带来更多可能性。

### 来源 10: A Large Language Model-based Framework for Semi-Structured Tender Document Retrieval-Augmented Generation

- URL: https://arxiv.org/html/2410.09077v1
- 精读方法：jina-readerlm-academic

```markdown
## Introduction

### Background

Large Language Models (LLMs) have been widely adopted in many applications due to their impressive capabilities. However, these models often struggle with tasks involving structured information, such as document retrieval and formatting. This paper introduces a framework designed to leverage LLMs for the generation of semi-structured tender documents, addressing the challenge of obtaining accurate and relevant tender documents.

### Research Goals

The primary goal is to develop a method for generating semi-structured tender documents using LLMs while maintaining the integrity of the tender content. Specifically:

1. **Document Retrieval**: Utilize LLMs to extract relevant information from existing tender documents.
2. **Template Filling**: Modify extracted templates to match the new requirements provided by the purchaser.
3. **Modifications with Procurement Knowledge Base**: Incorporate additional knowledge from a procurement knowledge base to ensure consistency and completeness.

### Methodological Approach

#### Template Retrieval Module

This module aims to identify and retrieve relevant tender documents from the repository based on user-provided input. It employs a combination of semantic search algorithms and embeddings to accurately locate documents that align with the user's specifications.

#### Template Filling Module

Once a template is identified, this module uses LLMs to fill out the template with appropriate details based on the user's requirements.

#### Modifications with Procurement Knowledge Base

This component integrates additional knowledge from a procurement knowledge base to ensure that the generated document adheres to industry standards and best practices.

### Evaluation Steps

After generating a draft document, we conduct rigorous evaluations against several criteria:

1. **Paragraph Score**: Measures how well the generated document matches the original paragraph structure.
2. **Table Score**: Evaluates whether the generated document correctly formats tables according to specified rules.
3. **Overall Score**: Comb


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
