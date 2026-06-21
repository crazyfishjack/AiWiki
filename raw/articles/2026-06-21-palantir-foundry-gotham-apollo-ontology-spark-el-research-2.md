---
title: "调研证据包：Palantir Foundry Gotham Apollo ontology 语义建模 核心产品技术架构 企业数据平台 金融风控政府情报 Spark Elasticsearch 行业对标"
source-type: article
generated: 2026-06-21
generated-by: wiki-research-skill
research-mode: standard
---

# 调研证据包：Palantir Foundry Gotham Apollo ontology 语义建模 核心产品技术架构 企业数据平台 金融风控政府情报 Spark Elasticsearch 行业对标

## 调研问题

Palantir Foundry Gotham Apollo ontology 语义建模 核心产品技术架构 企业数据平台 金融风控政府情报 Spark Elasticsearch 行业对标

## 摘要

本文档是四工具检索生成的证据包草稿，不是最终调研报告。Agent 必须先阅读本证据包，执行下方"AI 综合指令"，生成新的中文综合 raw 报告，然后询问用户是否入库。本证据包保留不删除。

- 发现候选信源：35
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
| exa | 1.00 | Concept-Centric Software Development | https://arxiv.org/html/2304.14975 |
| exa | 1.00 | A Brief Analysis of Palantir Gotham: A Collaborative and Interactive Big Data Visualization Analysis Software Based on Dynamic Ontology \| IEEE Conference Publication \| IEEE Xplore | https://ieeexplore.ieee.org/document/10808897 |
| exa | 1.00 | Data Digitization in Manufacturing Factory Using Palantir Foundry Solution | https://www.mdpi.com/2227-9717/12/12/2816 |
| exa | 1.00 | 𝖠𝗎𝗍𝗈𝖵𝖾𝗋𝗂𝖿𝗂𝖾𝗋: An Agentic Automated Verification Framework Using Large Language Models | https://arxiv.org/html/2604.02617v1 |
| exa | 1.00 | Foundry: a message-oriented, horizontally scalable ETL system for scientific data integration and enhancement | https://pmc.ncbi.nlm.nih.gov/articles/PMC6301337/ |
| exa | 1.00 | Palantir:  a framework for collaborative incident response and investigation | https://dl.acm.org/doi/10.1145/1527017.1527023 |
| exa | 1.00 | [2204.07309] Saga: A Platform for Continuous Construction and Serving of Knowledge At Scale | https://arxiv.org/pdf/2204.07309 |
| exa | 1.00 | OntoKG: Ontology-Oriented Knowledge Graph Construction with Intrinsic-Relational Routing | https://www.arxiv.org/pdf/2604.02618 |
| exa | 1.00 | Ontology-Driven Architecture for Managing Environmental, Social, and Governance Metrics | https://www.mdpi.com/2079-9292/13/9/1719 |
| exa | 1.00 |  | https://openreview.net/pdf?id=Prc8onC-jfq |
| exa | 1.00 | Unifying Ontology Construction and Semantic Alignment for Deterministic Enterprise Reasoning at Scale | https://arxiv.org/html/2604.09608 |
| exa | 1.00 | Unifying Ontology Construction and Semantic Alignment for Deterministic Enterprise Reasoning at Scale | https://arxiv.org/abs/2604.09608v1 |
| exa | 1.00 | Architecture and implementation of the Darmstadt database kernel system | https://dl.acm.org/doi/10.1145/38714.38737 |
| exa | 1.00 |  | https://arxiv.org/pdf/2004.11682 |
| exa | 1.00 |  | http://arxiv.org/pdf/2504.03652 |
| tavily | 0.78 | Palantir 核心技术架构深度研究 - Tech Whims \| 张晓龙 | https://techwhims.com/cn/posts/palantir-core-architecture |
| tavily | 0.73 | 万字解读Palantir产品、技术和架构讨论 - 53AI | https://www.53ai.com/news/Palantir/2025121217384.html |
| tavily | 0.73 | 万字解读Palantir产品、技术和架构讨论 - 53AI | https://www.53ai.com/news/AISaaS/2025121217384.html |
| tavily | 0.70 | Palantir产品套件与平台架构- 53AI-AI知识库 | https://www.53ai.com/news/Palantir/2025122362370.html |
| tavily | 0.69 | [PDF] 相关研究报告北交所研究团队 - i研报 | https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf |
| tavily | 0.69 | 帕兰泰尔- 维基百科，自由的百科全书 | https://zh.wikipedia.org/zh-cn/%E5%B8%95%E8%98%AD%E6%B3%B0%E7%88%BE |
| tavily | 0.69 | 以AI+本体框架整合多源数据，依托4大平台，让Palantir得以发现隐藏 ... | https://www.smartcity.team/investment/companies/palantir |
| tavily | 0.68 | Palantir - 全球大数据与AI领域市值最高的公司-产品核心技术 - 53AI-AI知识库\|企业AI知识库\|大模型知识库\|前线部署工程师\|FDE\|AIHub | https://www.53ai.com/news/knowledgegraph/2025120478305.html |
| tavily | 0.68 | [PDF] Palantir— —深挖政府大数据的神秘独角兽 | https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf |
| tavily | 0.67 | Palantir 产品体系深度解构：Ontology 驱动下的分层架构与模块- 墨天轮 | https://www.modb.pro/db/1930804422725087232 |
| tavily | 0.66 | [PDF] 深度解析Palantir | https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf |
| tavily | 0.63 | Palantir 的“本体工程”的核心思路、技术架构与实践示例 - 博客园 | https://www.cnblogs.com/end/p/19144086 |
| tavily | 0.60 | 平台概览 - Palantir | https://www.palantir.com/docs/zh/foundry/platform-overview/overview |
| tavily | 0.59 | 成功转型800亿美元AI领导者，Palantir做对了什么？ | https://www.secrss.com/articles/71253 |
| tavily | 0.57 | 构建管道• Best practices • 推荐的项目和团队结构 - Palantir | https://www.palantir.com/docs/zh/foundry/building-pipelines/recommended-project-structure |

## 信源质量门控记录

### 门控规则
- Tavily score < 0.4：剔除
- 已知低质域名：剔除
- 重复 URL：合并保留最高分结果
- Exa 学术/语义结果：默认保留，但进入来源等级评估
- C/D 级来源不得作为唯一结论依据
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`

### 保留信源
1. [Concept-Centric Software Development](https://arxiv.org/html/2304.14975)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
2. [A Brief Analysis of Palantir Gotham: A Collaborative and Interactive Big Data Visualization Analysis Software Based on Dynamic Ontology | IEEE Conference Publication | IEEE Xplore](https://ieeexplore.ieee.org/document/10808897)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
3. [Data Digitization in Manufacturing Factory Using Palantir Foundry Solution](https://www.mdpi.com/2227-9717/12/12/2816)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
4. [𝖠𝗎𝗍𝗈𝖵𝖾𝗋𝗂𝖿𝗂𝖾𝗋: An Agentic Automated Verification Framework Using Large Language Models](https://arxiv.org/html/2604.02617v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
5. [Foundry: a message-oriented, horizontally scalable ETL system for scientific data integration and enhancement](https://pmc.ncbi.nlm.nih.gov/articles/PMC6301337/)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
6. [Palantir:  a framework for collaborative incident response and investigation](https://dl.acm.org/doi/10.1145/1527017.1527023)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
7. [[2204.07309] Saga: A Platform for Continuous Construction and Serving of Knowledge At Scale](https://arxiv.org/pdf/2204.07309)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
8. [OntoKG: Ontology-Oriented Knowledge Graph Construction with Intrinsic-Relational Routing](https://www.arxiv.org/pdf/2604.02618)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
9. [Ontology-Driven Architecture for Managing Environmental, Social, and Governance Metrics](https://www.mdpi.com/2079-9292/13/9/1719)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
10. [https://openreview.net/pdf?id=Prc8onC-jfq](https://openreview.net/pdf?id=Prc8onC-jfq)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
11. [Unifying Ontology Construction and Semantic Alignment for Deterministic Enterprise Reasoning at Scale](https://arxiv.org/html/2604.09608)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
12. [Unifying Ontology Construction and Semantic Alignment for Deterministic Enterprise Reasoning at Scale](https://arxiv.org/abs/2604.09608v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
13. [Architecture and implementation of the Darmstadt database kernel system](https://dl.acm.org/doi/10.1145/38714.38737)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
14. [https://arxiv.org/pdf/2004.11682](https://arxiv.org/pdf/2004.11682)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
15. [http://arxiv.org/pdf/2504.03652](http://arxiv.org/pdf/2504.03652)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
16. [Palantir 核心技术架构深度研究 - Tech Whims | 张晓龙](https://techwhims.com/cn/posts/palantir-core-architecture)
   - 工具：tavily
   - 分数：0.78
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
17. [万字解读Palantir产品、技术和架构讨论 - 53AI](https://www.53ai.com/news/Palantir/2025121217384.html)
   - 工具：tavily
   - 分数：0.73
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
18. [万字解读Palantir产品、技术和架构讨论 - 53AI](https://www.53ai.com/news/AISaaS/2025121217384.html)
   - 工具：tavily
   - 分数：0.73
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
19. [Palantir产品套件与平台架构- 53AI-AI知识库](https://www.53ai.com/news/Palantir/2025122362370.html)
   - 工具：tavily
   - 分数：0.70
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
20. [[PDF] 相关研究报告北交所研究团队 - i研报](https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf)
   - 工具：tavily
   - 分数：0.69
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
21. [帕兰泰尔- 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E5%B8%95%E8%98%AD%E6%B3%B0%E7%88%BE)
   - 工具：tavily
   - 分数：0.69
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
22. [以AI+本体框架整合多源数据，依托4大平台，让Palantir得以发现隐藏 ...](https://www.smartcity.team/investment/companies/palantir)
   - 工具：tavily
   - 分数：0.69
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
23. [Palantir - 全球大数据与AI领域市值最高的公司-产品核心技术 - 53AI-AI知识库|企业AI知识库|大模型知识库|前线部署工程师|FDE|AIHub](https://www.53ai.com/news/knowledgegraph/2025120478305.html)
   - 工具：tavily
   - 分数：0.68
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
24. [[PDF] Palantir— —深挖政府大数据的神秘独角兽](https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf)
   - 工具：tavily
   - 分数：0.68
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
25. [Palantir 产品体系深度解构：Ontology 驱动下的分层架构与模块- 墨天轮](https://www.modb.pro/db/1930804422725087232)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
26. [[PDF] 深度解析Palantir](https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf)
   - 工具：tavily
   - 分数：0.66
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
27. [Palantir 的“本体工程”的核心思路、技术架构与实践示例 - 博客园](https://www.cnblogs.com/end/p/19144086)
   - 工具：tavily
   - 分数：0.63
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
28. [平台概览 - Palantir](https://www.palantir.com/docs/zh/foundry/platform-overview/overview)
   - 工具：tavily
   - 分数：0.60
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 技术文档
   - 后续处理：进入精读
29. [成功转型800亿美元AI领导者，Palantir做对了什么？](https://www.secrss.com/articles/71253)
   - 工具：tavily
   - 分数：0.59
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
30. [构建管道• Best practices • 推荐的项目和团队结构 - Palantir](https://www.palantir.com/docs/zh/foundry/building-pipelines/recommended-project-structure)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 技术文档
   - 后续处理：进入精读
31. [Integrated platforms: AIP, Foundry, and Apollo - Palantir](https://palantir.com/docs/foundry/architecture-center/platforms)
   - 工具：tavily
   - 分数：0.54
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 技术文档
   - 后续处理：进入精读
32. [同样是数据智能企业，中国版Palantir的根本不同在这里！ - 同花顺](https://stock.10jqka.com.cn/20260316/c675323641.shtml)
   - 工具：tavily
   - 分数：0.52
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
33. [Ontology design: Best practices • Palantir](https://www.palantir.com/docs/foundry/ontology/ontology-best-practices)
   - 工具：tavily
   - 分数：0.42
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 技术文档
   - 后续处理：进入精读
34. [Palantir Explained: Chief Architect on Foundry in 2022](https://www.youtube.com/watch?v=ZGGRCTTjLfQ)
   - 工具：tavily
   - 分数：0.42
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
35. [Palantir Competitors: Understanding Alternatives to Gotham and ...](https://datawalk.com/palantir-competitors-understanding-alternatives-to-gotham-and-foundry)
   - 工具：tavily
   - 分数：0.40
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考

### 剔除信源
1. [Palantir 核心技术架构深度研究 - Tech Whims | 张晓龙](https://techwhims.com/cn/posts/palantir-core-architecture)
   - 工具：tavily
   - 分数：0.72
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
2. [万字解读Palantir产品、技术和架构讨论 - 53AI](https://www.53ai.com/news/Palantir/2025121217384.html)
   - 工具：tavily
   - 分数：0.68
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
3. [万字解读Palantir产品、技术和架构讨论 - 53AI](https://www.53ai.com/news/AISaaS/2025121217384.html)
   - 工具：tavily
   - 分数：0.68
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
4. [[PDF] 相关研究报告北交所研究团队 - i研报](https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf)
   - 工具：tavily
   - 分数：0.66
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
5. [以AI+本体框架整合多源数据，依托4大平台，让Palantir得以发现隐藏 ...](https://www.smartcity.team/investment/companies/palantir)
   - 工具：tavily
   - 分数：0.64
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
6. [[PDF] 深度解析Palantir](https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf)
   - 工具：tavily
   - 分数：0.56
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
7. [France to ditch Palantir’s AI data tools in favour of domestic provider - The Guardian](https://www.theguardian.com/world/2026/jun/16/france-ai-data-tools-palantir-chapsvision)
   - 工具：tavily
   - 分数：0.15
   - 来源等级：C
   - 剔除原因：score 低于 0.4
8. [SIJE Unveils Agentic AI and 470,000-Class Ontology Supply Chain Platform at VivaTech 2026, Redefining Global Apparel OEM Industry Standards - 에이빙](https://kr.aving.net/news/articleViewAmp.html?idxno=1811717)
   - 工具：tavily
   - 分数：0.07
   - 来源等级：C
   - 剔除原因：score 低于 0.4
9. [How SpaceX’s float could lift the tide for European space tech - PitchBook](https://pitchbook.com/news/articles/how-spacexs-float-could-lift-the-tide-for-european-space-tech)
   - 工具：tavily
   - 分数：0.05
   - 来源等级：C
   - 剔除原因：score 低于 0.4
10. [Your GPUs aren’t the problem: AI’s real bottleneck is data delivery - TechCrunch](https://techcrunch.com/sponsor/f5/your-gpus-arent-the-problem-ais-real-bottleneck-is-data-delivery/)
   - 工具：tavily
   - 分数：0.03
   - 来源等级：C
   - 剔除原因：score 低于 0.4
11. [Top Computer Vision Development Company Options for 2026 - Robotics & Automation News](https://roboticsandautomationnews.com/2026/06/16/top-computer-vision-development-company-options-for-2026/102574/)
   - 工具：tavily
   - 分数：0.03
   - 来源等级：C
   - 剔除原因：score 低于 0.4
12. [Art+AI Fuels Innovation & Entrepreneurship: 2026 Next Generation Philanthropy Leadership Program Opens - Alvinology](https://alvinology.com/2026/06/18/artai-fuels-innovation-entrepreneurship-2026-next-generation-philanthropy-leadership-program-opens-recruitment/)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
13. [2026 Next Generation Philanthropy Leadership Program opens recruitment amid AI advancement wave - Vietnam Investment Review - VIR](https://vir.com.vn/2026-next-generation-philanthropy-leadership-program-opens-recruitment-amid-ai-advancement-wave-155051.html)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
14. [New AI optimization framework beats Claude Code and Codex by 2.5x on the same compute budget - VentureBeat](https://venturebeat.com/orchestration/new-ai-optimization-framework-beats-claude-code-and-codex-by-2-5x-on-the-same-compute-budget)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
15. [Databricks: Artefact Reveals “The Workforce You Won’t Recognize” - EIN Presswire](https://www.einpresswire.com/article/919827936/databricks-artefact-reveals-the-workforce-you-won-t-recognize)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
16. [The AI gamble of mining companies: Valuations enter a phase of differentiation, and it's hard to turn the tide - WEEX](https://www.weex.com/news/detail/the-ai-gamble-of-mining-companies-valuations-enter-a-phase-of-differentiation-and-its-hard-to-turn-the-tide-fglrejwbf21tu7j8w4so3s9b)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
17. [万字解读Palantir产品、技术和架构讨论 - 53AI](https://www.53ai.com/news/AISaaS/2025121217384.html)
   - 工具：tavily
   - 分数：0.70
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
18. [Palantir 核心技术架构深度研究 - Tech Whims | 张晓龙](https://techwhims.com/cn/posts/palantir-core-architecture)
   - 工具：tavily
   - 分数：0.70
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
19. [一文全面解析Palantir产品以及其“本体论”：以AI+本体框架整合多源数据，依托4大平台，让Palantir得以发现隐藏在数据背后的关键关联，构建可演进的闭环决策系统，赋能政府与企业两类客户 – 智慧城市行业分析](https://www.smartcity.team/investment/companies/palantir)
   - 工具：tavily
   - 分数：0.63
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
20. [[PDF] 相关研究报告北交所研究团队 - i研报](https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf)
   - 工具：tavily
   - 分数：0.61
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
21. [[PDF] 深度解析Palantir](https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf)
   - 工具：tavily
   - 分数：0.48
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
22. [平台概览 - Palantir](https://www.palantir.com/docs/zh/foundry/platform-overview/overview)
   - 工具：tavily
   - 分数：0.47
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
23. [Platform overview - Palantir](https://palantir.com/docs/foundry/platform-overview/overview)
   - 工具：tavily
   - 分数：0.37
   - 来源等级：A
   - 剔除原因：score 低于 0.4
24. [Palantir 核心技术架构深度研究 - Tech Whims | 张晓龙](https://techwhims.com/cn/posts/palantir-core-architecture)
   - 工具：tavily
   - 分数：0.73
   - 来源等级：B
   - 剔除原因：重复 URL，已合并到最高分结果
25. [以AI+本体框架整合多源数据，依托4大平台，让Palantir得以发现隐藏 ...](https://www.smartcity.team/investment/companies/palantir)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
26. [万字解读Palantir产品、技术和架构讨论 - 53AI](https://www.53ai.com/news/AISaaS/2025121217384.html)
   - 工具：tavily
   - 分数：0.68
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
27. [[PDF] Palantir— —深挖政府大数据的神秘独角兽](https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf)
   - 工具：tavily
   - 分数：0.64
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
28. [[PDF] 相关研究报告北交所研究团队 - i研报](https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf)
   - 工具：tavily
   - 分数：0.68
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
29. [[PDF] 深度解析Palantir](https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf)
   - 工具：tavily
   - 分数：0.62
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
30. [平台概览 - Palantir](https://www.palantir.com/docs/zh/foundry/platform-overview/overview)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果

## 完整精读结果

### 来源 1: Palantir 核心技术架构深度研究 - Tech Whims | 张晓龙

- URL: https://techwhims.com/cn/posts/palantir-core-architecture
- 精读方法：firecrawl-scrape

# Palantir 核心技术架构深度研究 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#palantir-%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E6%9E%B6%E6%9E%84%E6%B7%B1%E5%BA%A6%E7%A0%94%E7%A9%B6)

> 面向大数据架构师的 Ontology 战略解析

## 引言：为什么数据平台总是「能看不能用」 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#%E5%BC%95%E8%A8%80-%E4%B8%BA%E4%BB%80%E4%B9%88%E6%95%B0%E6%8D%AE%E5%B9%B3%E5%8F%B0%E6%80%BB%E6%98%AF-%E8%83%BD%E7%9C%8B%E4%B8%8D%E8%83%BD%E7%94%A8)

如果你是一位在教育行业负责大数据平台建设的架构师，你大概率经历过以下场景：

- 数据湖建好了，TB 级别的数据存进去了，BI 报表做了几十张，但业务部门还是说「数据没用」
- 分析师每天导出 Excel，手动合并数据，人工做决策
- ERP、CRM、实时传感器、行为日志分布在不同系统，每次要做一个跨系统分析，都要经历痛苦的 ETL 和数据对齐
- AI 模型训好了，却不知道如何让它真正介入业务流程

这不是能力问题，是架构问题。传统大数据平台的逻辑是： **数据→存储→计算→展示**。数据是静态的旁观者，人是决策的主体，工具只是让「看」变得更高效。但看完之后呢？决策和行动仍然在系统之外。

Palantir 的回答是： **把数据变成运营层的数字孪生，让 AI 在治理框架内直接提出操作建议**。

这不是一个简单的「知识图谱」或「数据中台」概念。Palantir 构建的叫 **Ontology**——一个把数据、逻辑、操作、安全统一建模的语义层。本研究深入解析 Ontology 的技术架构，以及它对大数据架构师的借鉴意义。

* * *

## 一、Ontology：不是 Schema，是运营层的数字孪生 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#%E4%B8%80-ontology-%E4%B8%8D%E6%98%AF-schema-%E6%98%AF%E8%BF%90%E8%90%A5%E5%B1%82%E7%9A%84%E6%95%B0%E5%AD%97%E5%AD%AA%E7%94%9F)

### 1.1 传统数仓的问题 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#1-1-%E4%BC%A0%E7%BB%9F%E6%95%B0%E4%BB%93%E7%9A%84%E9%97%AE%E9%A2%98)

传统数据仓库的建模逻辑是 **表（Table）**：

这种建模没问题，但它描述的是 **数据的结构**，不是 **业务的运作方式**。

分析师要回答「华北地区高价值客户最近一单延迟发货的情况」，需要：

1. join orders 和 customers 筛选区域和金额
2. join shipments 找出发货记录
3. 计算延迟天数
4. 导出 Excel 给运营人员
5. 运营人工判断要不要催单、要不要补偿

这个链路中， **数据是「死的」**——它只在人被问到问题时才被唤醒。

### 1.2 Ontology 的思路 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#1-2-ontology-%E7%9A%84%E6%80%9D%E8%B7%AF)

Palantir 的 Ontology 不描述「表」，它描述的是 **可操作的业务对象**：

关键区别在于：

- **传统数仓**：名词（实体）和动词（操作）是分离的，建模是数据驱动的
- **Ontology**：名词和动词一起建模，语义对象本身就是业务流程的抽象

这不是简单的「对象数据库」或「图数据库」。Palantir 的 Ontology 是 **四要素集成**：

| 要素 | 描述 |
| --- | --- |
| **Data** | 从 ERP、CRM、工业数据库、地理空间、实时传感器等异构数据源统一抽象为 objects/properties/links |
| **Logic** | 业务规则、ML 模型、LLM 函数、多步编排统一在 Ontology 内定义 |
| **Action** | 从简单属性更新到复杂多步事务，变更可实时回写到运营系统 |
| **Security** | 行级、列级权限控制，AI agent 继承人类权限或项目权限 |

### 1.3 对大数据架构师的启示 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#1-3-%E5%AF%B9%E5%A4%A7%E6%95%B0%E6%8D%AE%E6%9E%B6%E6%9E%84%E5%B8%88%E7%9A%84%E5%90%AF%E7%A4%BA)

**问题**：你的数仓建模是「面向分析」还是「面向操作」？

大多数数仓是前者。我们建dim\_dim、dim\_fact、dws\_ads 层，目标是让 SQL 查询更快。但业务对象之间的语义关系、操作链路没有被显式建模。

**判断**：如果你负责的数仓主要服务于 BI 报表和 ad-hoc 查询， Ontology 的思路可以帮助你重新审视「语义层」的设计——不只是做一个统一的指标口径，而是思考：

- 业务实体之间的关联关系是否被显式建模为 first-class 概念？
- 是否有统一的「动作」概念，可以对一个业务对象发起操作？
- 数据变更是否能反向回写到业务系统？

这不是让你推翻现有数仓，而是在数仓之上构建一层 **运营语义层**。Palantir 的做法是原生就设计这一层，传统企业则往往需要在这一步做增量。

* * *

## 二、Ontology 底层架构：三层设计与微服务分解 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#%E4%BA%8C-ontology-%E5%BA%95%E5%B1%82%E6%9E%B6%E6%9E%84-%E4%B8%89%E5%B1%82%E8%AE%BE%E8%AE%A1%E4%B8%8E%E5%BE%AE%E6%9C%8D%E5%8A%A1%E5%88%86%E8%A7%A3)

Palantir 官方文档将 Ontology 架构分为三个层次：

### 2.1 Language：建模语义 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#2-1-language-%E5%BB%BA%E6%A8%A1%E8%AF%AD%E4%B9%89)

这一层解决「如何定义业务对象」的问题。Ontology 定义了：

- **Object Types**：语义对象类型（如 Order, Customer, Shipment）
- **Property Types**：属性类型（基础类型 \+ 复杂类型如地理坐标、时间序列）
- **Link Types**：对象之间的关系（对称关系、非对称关系、多重关系）
- **Action Types**：可对对象执行的操作（原子操作、流程化操作）
- **Logic**：业务规则、计算属性、验证逻辑

这些定义通过 SDK（OSDK，Ontology SDK）声明式地描述，形成一套完整的业务语义模型。

### 2.2 Engine：执行层 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#2-2-engine-%E6%89%A7%E8%A1%8C%E5%B1%82)

Engine 层负责高性能执行，包含：

- **高规模 SQL 查询**：对数十亿对象执行复杂过滤、聚合
- **实时状态变更订阅**：客户端可以订阅对象变更事件（类似 WebSocket）
- **原子事务更新**：保证操作的 ACID 语义
- **批量变更与流式处理**：支持 CDC（Change Data Capture）低延迟镜像
- **版本控制**：每个对象变更都有完整的审计日志和版本历史

Engine 层是 Palantir 多年打磨的核心竞争力——它要支撑每天数百万次对象查询和数十万次操作变更。

### 2.3 Toolchain：开发与运维 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#2-3-toolchain-%E5%BC%80%E5%8F%91%E4%B8%8E%E8%BF%90%E7%BB%B4)

- **OSDK**：自动生成 API 网关和多语言 SDK（Python, TypeScript, Java 等）
- **DevOps 工具链**：CI/CD、版本管理、部署流水线
- **IDE 集成**：在 IDE 中实时预览 Ontology 变更的影响

* * *

## 三、OMS 与 OSS：微服务架构拆解 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#%E4%B8%89-oms-%E4%B8%8E-oss-%E5%BE%AE%E6%9C%8D%E5%8A%A1%E6%9E%B6%E6%9E%84%E6%8B%86%E8%A7%A3)

### 3.1 OMS（Ontology Metadata Service） [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#3-1-oms-ontology-metadata-service)

OMS 是 Ontology 的「元数据服务」，负责管理：

- **Object Types 的元数据**：每个对象类型有哪些属性、哪些关联、哪些操作
- **Link Types 的定义**：对象之间的关系规则
- **Action Types 的定义**：操作的结构、参数、权限要求

可以把 OMS 理解为 Ontology 的「schema 注册中心」。它不存储实际的对象数据，只存储「对象的定义」。

**架构意义**：OMS 是典型的元数据层设计，它使得 Ontology 的定义可以独立于数据存储进行变更。这为「版本控制」和「分支治理」提供了技术基础。

### 3.2 OSS（Object Set Service） [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#3-2-oss-object-set-service)

OSS 是 Ontology 的「读取服务」，负责：

- **对象的搜索与过滤**：基于任意属性组合条件查询对象集合
- **聚合计算**：count, sum, avg, group by 等
- **对象加载**：将对象从底层存储加载到客户端内存
- **对象集的动态维护**：支持 Static、Dynamic、Temporary、Permanent 四种对象集类型

**Object Sets 的分类**：

| 类型 | 描述 | 典型场景 |
| --- | --- | --- |
| **Static** | 主键列表，一经创建不变 | 「我关注的 100 个重点客户」 |
| **Dynamic** | 过滤条件，结果随数据自动更新 | 「所有未处理的订单」 |
| **Temporary** | 24 小时过期，适合临时分析 | 一次 ad-hoc 查询的结果集 |
| **Permanent** | 长期保存的对象集 | 业务定义的关键群体 |

OSS 的设计核心是 **高性能读取**。在 V2 架构中，OSS 直接对接底层的 Object Databases（对象数据库），这些数据库分为：

- **V1（Phonograph）**：遗留系统，维护兼容性
- **V2**：新一代对象存储，针对 Ontology 查询模式优化

### 3.3 数据写入：Object Data Funnel [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#3-3-%E6%95%B0%E6%8D%AE%E5%86%99%E5%85%A5-object-data-funnel)

写入流程通过 **Object Data Funnel** 编排：

1. 数据从源系统（ERP, CRM, 传感器）通过 CDC 管道进入
2. 经过清洗、转换、映射到 Ontology 对象模型
3. 写入 Object Databases
4. 触发 OMS 元数据更新和 OSS 缓存刷新

这个流程是实时的，保证 Ontology 中的数据状态与业务系统同步。

### 3.4 对大数据架构师的启示 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#3-4-%E5%AF%B9%E5%A4%A7%E6%95%B0%E6%8D%AE%E6%9E%B6%E6%9E%84%E5%B8%88%E7%9A%84%E5%90%AF%E7%A4%BA)

OMS + OSS 的分离设计，本质上是\*\*「元数据注册」+「数据服务」\*\*的经典架构模式。

**借鉴点**：

- **语义层与服务分离**：你的数据中台是否有一层清晰的「语义定义」服务？还是有定义但散落在各个 BI 工具和代码中？
- **Object Set 即服务**：是否可以把「常用查询」封装为稳定的 API，而非让业务方每次写 SQL？
- **CDC 实时同步**：异构数据源的实时同步是 Ontology 能否「实时」的关键。你们的 ETL 延迟是多少？小时级？分钟级？还是秒级？

**判断**：大多数企业大数据平台的 ETL 是小时级或 T+1 的。如果要构建运营级的语义层，需要重新审视数据同步延迟。

* * *

## 四、AIP：当 AI 遇见 Ontology [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#%E5%9B%9B-aip-%E5%BD%93-ai-%E9%81%87%E8%A7%81-ontology)

### 4.1 传统 RAG 的局限 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#4-1-%E4%BC%A0%E7%BB%9F-rag-%E7%9A%84%E5%B1%80%E9%99%90)

现在业界最火的 AI 应用模式是 **RAG（Retrieval-Augmented Generation）**：

RAG 解决的是「知识获取」问题——让 LLM 能引用企业私有数据。但它有一个根本局限： **LLM 只是「更好地搜索」，它不介入业务操作**。

你问 RAG 系统：「这个订单要不要退款？」，它可以给你一段分析。但它不能帮你执行退款操作。

### 4.2 AIP 的解法 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#4-2-aip-%E7%9A%84%E8%A7%A3%E6%B3%95)

Palantir 的 AIP（AI Platform）让 LLM 在 Ontology 之上运作：

- **AI 不只检索信息，而是在治理框架内对真实业务对象提出操作建议**
- 每个 Action 都有权限校验，AI 的操作建议要经过人工审批
- 审批通过后，操作回写到业务系统（ERP, CRM 等）

**关键概念：Proposal 工作流**

借鉴 Git 的 branching 思想：

1. AI 提议一个操作（如「建议将此订单标记为优先处理」）
2. 提议作为一个「branch」存在，可被 review
3. 人类审批通过后，merge 到主状态
4. 操作执行到业务系统

这套机制解决了 AI 应用的核心难题： **如何在不失去人类控制的前提下，让 AI 介入业务流程？**

### 4.3 AIP 的核心能力 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#4-3-aip-%E7%9A%84%E6%A0%B8%E5%BF%83%E8%83%BD%E5%8A%9B)

| 能力 | 描述 |
| --- | --- |
| **Pipeline Builder** | 用 LLM 对非结构化数据做分类、摘要、实体提取，自动构建数据管道 |
| **Scenario Primitive** | 模拟「假设」场景，如「如果这条生产线调整，对供应链的影响是什么」 |
| **Language Model Service** | 统一接口切换/比较多个 LLM 提供商（OpenAI, Anthropic, 自托管等） |
| **AI Agent** | 自然语言操作 Foundry（创建 pipeline、管理 repo、构建 ontology 对象） |

### 4.4 对大数据架构师的启示 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#4-4-%E5%AF%B9%E5%A4%A7%E6%95%B0%E6%8D%AE%E6%9E%B6%E6%9E%84%E5%B8%88%E7%9A%84%E5%90%AF%E7%A4%BA)

**问题**：你的 AI 能力是否只在「查询」层面，还是已经介入「操作」层面？

**判断**：大多数企业的 AI 应用停留在「问答」——问数据，给分析。但业务真正需要的是「行动」——AI 建议，人审批，自动执行。

**关键区别**：

| 维度 | 传统 RAG | AIP 模式 |
| --- | --- | --- |
| LLM 角色 | 更好的搜索引擎 | 业务决策参与者 |
| 数据交互 | 只读检索 | 读写操作 |
| 权限控制 | 无 | 继承人类权限或项目权限 |
| 变更追溯 | 无 | 完整的 branch/merge 审计 |
| 业务闭环 | 不介入 | 可回写到业务系统 |

**落地建议**：

- 先有清晰的 Ontology（业务对象模型），再做 AI 介入
- AI 操作建议必须有「审批」环节，不能自动执行
- 操作日志要完整保留，支持审计和回滚

* * *

## 五、三大平台：Gotham vs Foundry vs Apollo [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#%E4%BA%94-%E4%B8%89%E5%A4%A7%E5%B9%B3%E5%8F%B0-gotham-vs-foundry-vs-apollo)

Palantir 并不是一个单一产品，而是三个平台的组合：

| 平台 | 定位 | 核心用户 | 特点 |
| --- | --- | --- | --- |
| **Gotham** | 政府与国防 | 情报机构、军队、安全部门 | 高敏感数据处理、跨机构协同、实时态势感知 |
| **Foundry** | 商业企业 | 能源、制造、金融、医疗、零售 | 运营决策平台、数据管道构建、Ontology 驱动的业务应用 |
| **Apollo** | 基础底座 | 上述所有平台 | 持续交付与自动化运维，支撑平台本身的迭代更新 |

### 5.1 Gotham：起源与核心能力 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#5-1-gotham-%E8%B5%B7%E6%BA%90%E4%B8%8E%E6%A0%B8%E5%BF%83%E8%83%BD%E5%8A%9B)

Gotham 是 Palantir 最早的产品，诞生于 2003 年，最初用于反恐情报分析。它的核心特点是：

- **跨源数据融合**：整合情报数据库、通讯记录、地理信息、人员档案
- **实体关联分析**：找出人、组织、地点、事件之间的隐藏关联
- **知识图谱推理**：基于图推理引擎进行多跳查询
- **高安全管控**：分级权限、审计追溯、防止数据泄露

Gotham 在美国政府体系中广泛应用，是 Palantir 最早的营收来源。

### 5.2 Foundry：商业化的 Ontology [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#5-2-foundry-%E5%95%86%E4%B8%9A%E5%8C%96%E7%9A%84-ontology)

Foundry 是 Palantir 将 Gotham 的能力向商业企业输出的产品，也是本文讨论的核心。它的关键演进是：

- **Ontology 原生**：Gotham 是「分析优先」，Foundry 是「操作优先」
- **自服务数据管道**：业务用户可以自己构建数据管道，不需要全依赖数据团队
- **行业模板**：预置行业特定的 Ontology 模型（如制造业的供应链 Ontology、医疗的患者 Ontology）
- **更友好的 UX**：面向商业用户的前端，而不是面向分析师的查询工具

### 5.3 Apollo：持续交付底座 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#5-3-apollo-%E6%8C%81%E7%BB%AD%E4%BA%A4%E4%BB%98%E5%BA%95%E5%BA%A7)

Apollo 是 Palantir 的「运维平台」，它解决的问题是：

- **软件持续更新**：Palantir 产品每周迭代，Apollo 负责将更新自动推送到客户环境
- **环境一致性**：确保每个客户的测试、生产环境版本一致
- **故障自愈**：自动检测和恢复异常组件

你可以把 Apollo 理解为 Palantir 自己的 DevOps 平台，也是它能维持「软件即服务」体验的技术基础。

### 5.4 对大数据架构师的启示 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#5-4-%E5%AF%B9%E5%A4%A7%E6%95%B0%E6%8D%AE%E6%9E%B6%E6%9E%84%E5%B8%88%E7%9A%84%E5%90%AF%E7%A4%BA)

**判断**：你的团队在使用多个「烟囱式」系统吗？

Gotham → Foundry 的演进说明：早期系统往往是「专用的」，后期需要抽象为「通用的 Ontology」。如果你有多个业务系统（ERP, CRM, LMS, 财务系统），它们之间的「语义互通」是问题关键。

**组织启发**：Palantir 的 **FDE（Forward Deployed Engineers）** 模式

Palantir 有一个独特的岗位叫 **FDE**——嵌入客户运营环境的工程师。他们不是远程支持，而是：

- 住在客户现场
- 理解客户的业务流程
- 基于 Ontology 定制开发
- 持续优化客户的运营流程

这不是传统意义上的「实施顾问」或「技术支持」。FDE 是 **既懂技术又懂业务的「驻场架构师」**。

**判断**：你的数据团队是否有人真正「住在」业务一线？还是只在需求井喷时响应？

* * *

## 六、版本控制与分支治理：Ontology 的独特设计 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#%E5%85%AD-%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E4%B8%8E%E5%88%86%E6%94%AF%E6%B2%BB%E7%90%86-ontology-%E7%9A%84%E7%8B%AC%E7%89%B9%E8%AE%BE%E8%AE%A1)

### 6.1 借鉴 Git 的设计哲学 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#6-1-%E5%80%9F%E9%89%B4-git-%E7%9A%84%E8%AE%BE%E8%AE%A1%E5%93%B2%E5%AD%A6)

Ontology 最有特色的设计之一是 **版本控制**：

- 每个 Ontology 变更（新增对象类型、修改属性、调整关系）都有版本记录
- 变更可以开「分支」，在分支上做实验性修改
- 分支可以 review、comment、approve
- 批准后 merge 回主版本

这完全借鉴了 Git 的 branching 思想，但应用在 **业务操作治理** 上。

### 6.2 为什么需要分支治理 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#6-2-%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81%E5%88%86%E6%94%AF%E6%B2%BB%E7%90%86)

传统系统的变更有两种模式：

1. **直接修改**：改错了，撤回难，审计难
2. **审批流**：流程冗长，创新受限

Ontology 的分支治理试图取两者之长：

- **实验自由**：可以在分支上大胆尝试新模型、新逻辑
- **治理可控**：每个分支的变更都有 review 和审批
- **变更可追溯**：所有 merge 记录都在，方便审计和回溯

### 6.3 对大数据架构师的启示 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#6-3-%E5%AF%B9%E5%A4%A7%E6%95%B0%E6%8D%AE%E6%9E%B6%E6%9E%84%E5%B8%88%E7%9A%84%E5%90%AF%E7%A4%BA)

**问题**：你的数据模型变更有版本控制吗？变更有审批流程吗？

大多数数仓的变更是这样管理的：

- 有人改了 dwd 层的表结构
- 下游报表大面积报错
- 追溯不到是谁改的、为什么改

**判断**：引入类似 Git 的分支治理模型，可能让你的数据平台变更更可控。

但要注意：Palantir 的分支治理是针对「业务语义模型」的，不是针对「底层表结构」的。不要把简单问题复杂化。

* * *

## 七、哪些可以借鉴，哪些是 Palantir 特有的 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#%E4%B8%83-%E5%93%AA%E4%BA%9B%E5%8F%AF%E4%BB%A5%E5%80%9F%E9%89%B4-%E5%93%AA%E4%BA%9B%E6%98%AF-palantir-%E7%89%B9%E6%9C%89%E7%9A%84)

### 7.1 可以借鉴的理念 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#7-1-%E5%8F%AF%E4%BB%A5%E5%80%9F%E9%89%B4%E7%9A%84%E7%90%86%E5%BF%B5)

| 理念 | 落地方式 |
| --- | --- |
| **业务对象统一建模** | 在数仓之上构建「语义对象层」，定义核心业务实体的属性、关系、操作 |
| **OMS/OSS 分离** | 设计独立的「元数据服务」和「数据读取服务」，提高架构清晰度 |
| **Object Set API 化** | 将常用查询封装为稳定的 API，减少业务方的 SQL 依赖 |
| **AI 介入操作层** | 设计「AI 建议 → 人工审批 → 自动执行」的闭环 |
| **版本控制治理** | 对核心数据模型和 Ontology 变更引入分支和审批机制 |
| **CDC 实时同步** | 缩短 ETL 延迟，从 T+1 到分钟级甚至秒级 |
| **FDE 驻场模式** | 数据团队派人深入业务一线，而非只在后方支持 |

### 7.2 Palantir 特有的，难以复制 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#7-2-palantir-%E7%89%B9%E6%9C%89%E7%9A%84-%E9%9A%BE%E4%BB%A5%E5%A4%8D%E5%88%B6)

| 特性 | 原因 |
| --- | --- |
| **完整的 Ontology 产品化** | 投入 20 年打磨，不是几个月能赶上 |
| **Gotham/Foundry 双轨产品** | 政府与商业市场分开运营 |
| **FDE 驻场文化** | 需要组织架构配合，不是单纯的技术选型 |
| **高客单价商业模式** | Palantir 软件年费数百万美元，不是所有企业能承受 |
| **全栈自研** | 从底层的对象数据库到上层的 AI Agent，全链路自研 |

### 7.3 务实落地的起点 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#7-3-%E5%8A%A1%E5%AE%9E%E8%90%BD%E5%9C%B0%E7%9A%84%E8%B5%B7%E7%82%B9)

**判断**：不要试图做一个 Palantir 的「精简版」，从最痛的痛点入手：

1. **先解决「数据找不到」**：统一指标口径，提供稳定的对象查询 API
2. **再解决「数据不能用」**：将 AI 能力从「问答」延伸到「操作建议」
3. **最后解决「变更加失控」**：对核心模型变更引入审查机制

* * *

## 八、总结：对大数据架构师的行动建议 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#%E5%85%AB-%E6%80%BB%E7%BB%93-%E5%AF%B9%E5%A4%A7%E6%95%B0%E6%8D%AE%E6%9E%B6%E6%9E%84%E5%B8%88%E7%9A%84%E8%A1%8C%E5%8A%A8%E5%BB%BA%E8%AE%AE)

### 8.1 核心认知 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#8-1-%E6%A0%B8%E5%BF%83%E8%AE%A4%E7%9F%A5)

Palantir 的 Ontology 并不是一个新的「数据库」或「数据中台」，它本质上是一套\*\*「业务语义操作系统」\*\*：

- 数据不只是被查询的对象，而是可以被操作的主体
- AI 不只是回答问题，而是可以提出操作建议
- 变更不只是修改，而是可追溯、可审查、可回滚的治理对象

### 8.2 行动建议 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#8-2-%E8%A1%8C%E5%8A%A8%E5%BB%BA%E8%AE%AE)

| 阶段 | 行动 | 衡量标准 |
| --- | --- | --- |
| **短期（1-3 个月）** | 梳理核心业务对象，识别关键实体及其关系 | 产出核心 Ontology 草图（10-20 个对象类型） |
| **中期（3-6 个月）** | 构建语义 API 层，将常用查询封装为服务 | 业务方通过 API 获取数据的比例超过 50% |
| **长期（6-12 个月）** | 引入 AI 操作建议，试点分支治理 | AI 建议被采纳并执行的操作 > 10 条/周 |

### 8.3 风险提示 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#8-3-%E9%A3%8E%E9%99%A9%E6%8F%90%E7%A4%BA)

- **不要「为了 Ontology 而 Ontology」**：没有明确的业务痛点，不要盲目投入
- **小心过度工程**：Ontology 应该是演进的，不是一步到位的
- **权限和安全是底线**：AI 介入操作必须有完善的权限控制，否则是灾难
- **组织配套是关键**：FDE 模式说明，技术问题往往不是纯技术问题

* * *

## 参考资料 [\#](https://techwhims.com/cn/posts/palantir-core-architecture/\#%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99)

- Palantir 官方 Ontology 架构文档
- Palantir 官方 AIP 产品概述
- 开源书《Palantir Ontology Strategy》: [github.com/Leading-AI-IO/palantir-ontology-strategy](https://github.com/Leading-AI-IO/palantir-ontology-strategy)
- Palantir 财报与产品发布（上市公司公开披露）

### 来源 2: 万字解读Palantir产品、技术和架构讨论 - 53AI

- URL: https://www.53ai.com/news/AISaaS/2025121217384.html
- 精读方法：firecrawl-scrape

- [首页](https://www.53ai.com/)
- 产品服务
- 客户案例
- FDE知识库
- 关于我们

热门场景

工作+AI

业务+AI

AIx业务

[落地咨询](https://www.53ai.com/consulting.html)

[场景共创](https://www.53ai.com/fine-tuning.html)

热门产品

[![53AI Brain](https://static.53ai.com/uploads/20250429/f9ed1b6c2d16a688c5791a0057c2217d.png)\\
\\
53AI Brain \\
\\
让知识在人与AI之间高效流动](https://www.53ai.com/products/53AIBrain) [![53AI Studio](https://static.53ai.com/uploads/20250429/b2cd4330d03bce8eb0eb0332eb2954cd.png)\\
\\
53AI Studio \\
\\
高准确率的企业级智能体开发平台](https://www.53ai.com/products/53AIStudio) [![53AI Hub](https://static.53ai.com/uploads/20250429/94e6d990ee63512db567bc53c113e8bd.png)\\
\\
53AI Hub开源\\
\\
三分钟搭建出独立的企业AI门户](https://www.53ai.com/products/53AIHub) [![53AI Agents](https://static.53ai.com/uploads/20250429/05d03bb026421069826c64e2407ad7ee.png)\\
\\
53AI Agents \\
\\
“AI专家”效率倍增的武器](https://www.53ai.com/products/Agents)

[行业案例](https://www.53ai.com/kehuanli/hangyeanli) [场景案例](https://www.53ai.com/kehuanli/solution)

[前沿技术](https://www.53ai.com/news/qianyanjishu) [Agent框架](https://www.53ai.com/news/agentplatform) [行业应用](https://www.53ai.com/news/hangyeyingyong) [企业落地](https://www.53ai.com/news/qiyejingying)

[公司介绍](https://www.53ai.com/about/introduction) [渠道合作](https://www.53ai.com/about/cooperation)

![FDE知识库](https://static.53ai.com/uploads/20250210/aec076a60258b0cc07078c8ea7dff92c.webp)

FDE知识库

学习大模型的前沿技术与行业落地应用

立即咨询预约演示

[![](https://static.53ai.com/assets/static/images/tab1.png)首页](https://www.53ai.com/) [FDE知识库](https://www.53ai.com/news.html) [前沿技术](https://www.53ai.com/news/qianyanjishu) [Palantir](https://www.53ai.com/news/Palantir)

# 万字解读Palantir产品、技术和架构讨论

发布日期：2025-12-12 07:03:23浏览次数： 6493

作者：信息化与数字化

![](https://static.53ai.com/assets/static/images/detail-icon.png)

微信搜一搜，关注“信息化与数字化”

推荐语

深入剖析Palantir如何颠覆传统企业数据架构，揭秘其"数据即平台"的工程哲学。

核心内容：

1\. Palantir独特的"产品+咨询"混合模式与落地能力

2\. 数据作为一等公民的架构设计与传统ERP的根本差异

3\. 全局可视化系统如何实现战场级的业务决策支持

![](https://static.53ai.com/assets/static/images/avatar.jpg)

杨芳贤

53AI创始人/腾讯云(TVP)最具价值专家

之前也在一些技术交流群里分享过 PDF 版的《Palantir 产品和技术讨论》，但 PDF 的形态实在不太适合讨论。今天就换成文章的方式，把其中的一些思考拿出来分享，如果需要PDF版本的话，也可以线下联系。除了大家常聊的”泡沫“估值和“本体论哲学”，这次更想从工程和架构的角度，看看 Palantir 在技术上到底有哪些内容。全文2万余字，大家可以找自己感兴趣的模块看。![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=129748&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9RZXlERDhoaWFibmh4U2Q4ZjBmRUpENlFyeXNpYTV0aWJMNk9HMjZuU0J5WVZCekNxSENTajFhM2hQWE5YZVZjTFI4Z3VXWlJBWEo5U3RGM2ljQlNaWDhRTWcvNjQwP3d4X2ZtdD1wbmcmYW1w;from=appmsg)

## 第 22章：专题：Palantir产品和技术分析

![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=129748&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9RZXlERDhoaWFibmh4U2Q4ZjBmRUpENlFyeXNpYTV0aWJMNk1iTjJsVjdQZkVEQ2tXSWlhUWNHSktpYXBkTDF5ZXFiaWE3emliQU9HWHYwcXRkQjZGSW8zUlBXancvNjQwP3d4X2ZtdD1wbmcmYW1w;from=appmsg)

### 22.1 对Palantir 的观察观点：

- **落地能力的差异化**：

与各类战略咨询、业务公司或传统数据分析服务相比，Palantir 的突出特点在于更强的落地执行力；而与 Oracle、SAP、Snowflake 等以系统或工具为核心的企业软件公司相比，Palantir 不仅仅提供工具，而是从整体上提供一个全局化的数据分析与决策视角。Palantir 的模式介于“软件公司”和“咨询公司”之间，强调产品平台 + 咨询交付。这种“重交付”模式难以规模化，但形成了与 SaaS 厂商的差异化。

- **应用、数据的关系演变：**

在传统企业信息化中，ERP 等应用是核心，以流程为轴心，把业务固化为系统操作，数据只是随之沉淀的副产品，用于事后统计和审计，本质是“系统先于数据”，应用的边界决定了数据的形态。Palantir 则彻底反转：它把数据提升为一等公民，成为组织的“操作对象”和“统一语境”，而应用只是数据的投影与使用方式。Palantir 将数据构造成跨部门、跨系统的统一底层，应用则像插件挂载其上。这样企业不再依赖僵硬的应用堆叠，而能在同一数据语境下快速衍生业务能力，真正实现数据驱动的敏捷组织。

- **全局可视化：**

Palantir 将抽象的数据与真实业务场景深度结合，让用户获得类似“作战地图”的全局视角。指挥官可以像在沙盘上推演一样制定作战计划，供应链管理者则能如同观察神经网络般实时追踪订单、库存与运输节点的变化。数据不再只是后台的存量资源，而是成为直接驱动认知与行动的前台工具，大幅提升决策的透明度、速度与准确性。相比之下，传统 ERP 系统过于强调对现实业务流程的数字化映射，更多关注信息和数据处理本身，让用户去适应系统；而 Palantir 的设计理念始终围绕用户的全局观，帮助他们以直观方式理解复杂系统并快速行动。

- **语境化可视化**：

Palantir 的另一大价值在于彻底改变了数据的呈现方式。数据不再只是冰冷的表格字段，而是被转化为贴近真实世界的语境：地理全景图展示货物、人员或资产在空间上的实时流动；时间线将复杂事件的发展脉络清晰还原，让用户能够洞察因果链条；关系网络图揭示不同数据实体之间的依赖与作用，帮助发现潜在的风险点或协同机会。通过这种“语境化”的可视化方式，用户不再是孤立地解读数字，而是置身于一个动态的“业务剧场”，能直观感知数据背后的逻辑与趋势，从而在复杂环境中快速形成判断与行动。

- **数据驱动执行：**

Palantir 的核心价值在于将数据分析与决策执行深度耦合，并直接下沉到一线作业场景，而不仅停留在宏观战略层面。在军事领域，它能够让海外作战单元根据实时情报动态调整计划；在商业场景中，则能驱动供应链即时优化，例如让卡车在运输途中临时改派至缺货市场。这样的能力不仅让价值可以被量化与验证，还真正实现了“数据—决策—行动”的闭环。更重要的是，它能够同时赢得一线执行者的高度认可与高层决策者的信任，不仅提升了采购决策的合理性，也为商业合作创造了“价值共创”的模式——Palantir 可以通过帮助客户降本增效来进行成果分成，从而获得远超传统软件许可证的回报。

- **跨层级穿透**：

Palantir 能同时服务战略层、战术层和作业层，从总部的宏观分析，到前线的一线指令，全部基于同一个数据底座与语义体系。这种“全栈穿透”是传统 ERP、BI 难以做到的。相比之下，如果一个业务只能停留在洞察层面而无法驱动执行，其价值往往模糊、变现路径冗长，还需要跨越多个组织层级的审批与推动；而 Palantir 将“洞察”与“行动”打通，从根本上缩短了价值实现的链条。

- **人机协同**：

Palantir 的定位不是替代人，而是强化人机协同。机器负责提供推演、模拟与数据支撑，而最终决策仍由人类承担。这在军事、金融、能源等高风险领域尤为重要。

- **认知锁定：**

Palantir 擅长通过前瞻性的市场叙事（如 Ontology、Operating System for AI、Enterprise Digital Twin），在概念层面占据客户心智，完成认知锁定。一旦客户接受了这种高维度的框架，就很难再回到传统 BI 或 ERP 的思维方式。同时，这类叙事不仅能让资本市场给予更高估值，也能让客户对产品价值的认知大幅提升，从而降低销售成本，实现“认知驱动的市场渗透”。

- **Palantir 与** **知识图谱** **的抽象定位**

  -   Palantir 的底层能力可被视为数据领域的“动态知识图谱”：它将人、物、地点、事件等实体编织成因果与关系网络，形成统一语境，支撑查询、追溯与推理。这种图谱化范式相比传统 BI 更契合情报分析、风险管控、供应链可视化等多实体、多关系场景，尤其在事件溯源和模式发现上具备天然优势。

      不过，它也有边界：知识图谱长于关系建模，却不擅长数值优化（如调度、线性规划），需借助外部算法引擎；在应对实时高频数据流时，也必须依赖额外的流式计算框架。Palantir 的独特之处在于，结合与各类业务系统、数据系统的深度工程化对接，将知识图谱的洞察力与执行力贯通，真正让数据从“认知”走向“行动”。

- **Palantir 特殊经历塑造的技术护城河：**

          Palantir 的护城河与其早期客户类型密切相关。对传统企业而言，数据整合相对可控，只要权限到位，通常能较快完成跨部门打通；但 Palantir 从一开始就服务军队和情报机构，这些环境下的数据极度复杂：既包含庞大的外部实时交互数据，又因保密制度导致内部流通高度受限。在这种高难度挑战下，Palantir 被迫打造出一套完全不同于传统数仓、数据湖和 BI 的新型数据架构体系。

        这一体系的核心，是通过 Ontology 方法论 将业务实体与数据抽象映射起来，使其成为一个“数据操作系统”；并引入了类似 “Git for Data” 的版本化管理能力，支持 时间回溯（Time Travel） 等机制，让用户能够像代码一样追踪、回滚和重现数据全生命周期。这意味着 Palantir 的平台并非把数据处理作为应用的附属功能，而是把数据处理本身提升为一个面向全局的基础生产平台。

          正是在这种背景下，Palantir 不仅成功解决了高复杂度、高敏感度场景中的数据整合难题，也让这一架构具备了迁移到分散、松散数据环境的能力，从而形成独特且难以复制的竞争壁垒。

- **大模型** **时代** **Ontology** **与 AI 的双向融合**

       在 AI 时代，Ontology 与大模型的结合堪称“天生一对”，解决了数据与智能之间的双重难题：

  - **Ontology** **赋能** **大模型**：传统数据库存放的是庞杂的原始信息，量大且精度要求高，大模型难以直接处理。Ontology 能够把这些信息重组为语义化、结构化的知识网络，通过时间、关系、事件等维度压缩与语境化，从而为大模型提供高质量的上下文输入，避免冗余与噪声干扰。

  - **大模型** **加速** **Ontology**：过去 Ontology 的构建依赖专家梳理和人工建模，周期长、成本高。大模型的引入改变了这一过程——它能够基于已有数据快速生成 Ontology 的初始框架或模板，大幅提升知识图谱与指数级图谱的建立效率，让语义层的搭建从“工匠式”转变为“自动化+校准”的范式。

  - **形成智能闭环**：Ontology 提供“可操作的上下文”，大模型则通过理解和推理完成“从数据到行动”的转化。当两者结合，企业不仅能获得智能化的认知，还能推动实时决策与执行闭环，真正让 AI 成为业务系统的操作层，而不是附属分析工具。

    这种双向融合，让 Ontology 不再是静态的知识框架，而成为 AI 时代的动态语境引擎，也为企业级 AI 落地打开了全新的空间。

**Palantir 的重构：**

- 搭建一个类似Palantir 的MVP最少需要哪些组件？大概工作量是怎样的？

- 几乎每一个 Palantir 模块都能找到替代品，但这些替代品往往是单点产品，而 Palantir 的优势在于：

  - 高度集成 —— 地理信息、实时数据、建模、工作流、安全体系在一个平台内无缝协同。

  - 安全与权限体系 —— 军事、情报、政府场景造就了极高门槛。

  - 直达一线执行 —— 很多产品只能“看”，Palantir 能“推演+执行”。

下面这张图可能更好的帮助大家理解Palantir的技术组件有哪些类似的产品：![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=129748&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9RZXlERDhoaWFibmh4U2Q4ZjBmRUpENlFyeXNpYTV0aWJMNmdEQUpPbjZUV3Q4S0ZpYnZPV1F4c3VRRjh3UHZkbnVBVmFpYmRhd2NHM09hT1l1enhZOXpSbUlBLzY0MD93eF9mbXQ9cG5nJmFtcA==;from=appmsg)

|     |     |     |     |
| --- | --- | --- | --- |
| 功能模块 | Palantir 的特色 | 可能的替代品/类似产品 | 差异与门槛 |
| 地图与地理信息可视化 | 深度集成任务数据（战场态势 / 物流线路 / 基础设施），支持多源数据叠加 | Google Earth、ESRI ArcGIS、OpenStreetMap、CesiumJS | Palantir 能将异构数据（传感器、卫星、业务系统）实时叠加并用于决策，而非单纯地理展示 |
| 三维可视化 / 全景推演 | 类似沙盘演练，结合时序和地理空间进行动态模拟 | Cesium、Unity、Unreal Engine、Kepler.gl | 替代品多用于展示或开发，Palantir 强调“决策推演”，并结合权限、安全、实时数据 |
| 数据集成与建模 | 异构数据源快速接入（包括敏感系统、外部 API、实时传感器） | Talend、Informatica、Fivetran、Apache NiFi | Palantir 更关注安全环境和高度复杂的数据权限隔离 |
| 数据自动化工作流 | 工作流引擎驱动数据清洗、处理与触发业务操作 | N8N、Apache Airflow、Prefect | Palantir 强调“与业务执行挂钩”的工作流，而不是单纯 ETL |
| 知识图谱 / 关系建模 | 将人、物、地点、事件串联成图谱，辅助分析因果关系 | Neo4j、TigerGraph、Stardog，IBM I2 | Palantir 优势在于自动化构建、与安全权限体系深度结合 |
| 可视化分析与仪表盘 | 从战略到一线执行的多层级仪表盘 | Tableau、Power BI、Qlik | 传统 BI 偏向于报表，Palantir 注重“可操作的分析”，直接影响决策流 |
| 权限与安全体系 | 细粒度权限控制，支持跨部门、跨级别的共享与隔离 | Okta、SailPoint、Centrify | 在军事/情报级别的复杂安全需求下，Palantir 的设计难以被替代 |
| 实时决策与模拟推演 | 将模型结果直接反馈到一线（如战场部署、供应链调度） | AnyLogic、Simio（仿真工具）、OptaPlanner（约束优化） | 其他工具多停留在建模/模拟，Palantir 强调与现实执行场景直接挂钩 |
| AI/ML 模型集成 | 支持接入第三方模型，或在安全环境中运行 ML 推理 | DataRobot、SageMaker、H2O.ai | Palantir 的优势在于“把模型嵌入到组织的日常工作流中” |
| 协同与审计 | 让多部门基于同一数据环境协作，同时保证可追溯性 | Confluence、Jira、Slack + 数据平台 | 替代方案分散，Palantir 强调统一平台下的“协作 + 审计”能力 |

### 22.2 问题拆解

### 要了解一个大的体系，要从列问题开始。这里先不做解答，把一些跟产品和技术有关的问题先整理出来。

#### 22.2.1 产品与架构定位

- Foundry / Gotham 历来的技术架构演化是怎样的？

- Palantir 的产品定位是 **平台** 还是 **应用**？在客户体系中是取代传统 IT 系统，还是作为补充和“胶水层”？

- Foundry / Gotham 的 **核心技术抽象** 是什么？它是“数据模型”“知识图谱”还是“操作系统”层？

- 与传统 BI、ERP、Data Lake 有什么 **边界与差异**？

- 如果一家企业只用一个超大型 ERP（比如 SAP S/4HANA 或 Oracle Fusion），好像就可以把订单、库存、财务、采购、人力全都放在里面，并且做好抽象分层和解耦，是不是就不需要 Palantir Foundry 这样的产品了？

- 与 Data Lake / Lakehouse（Snowflake、Databricks）的关系是 **竞争** 还是 **上层封装**？

- 与 BI 工具（如 Tableau、PowerBI）的边界是什么？Foundry 提供的可视化是否会逐步侵蚀 BI 工具的角色？

- Palantir 的平台定位是否足够“可插拔”？客户能否只用数据治理或应用构建的子模块，而不是整个平台？

#### **22.2.2** **Ontology** **—— 从哲学到工程化**

- Palantir 为什么强调 Ontology 是 Foundry 的核心卖点？

- Ontology，怎样从抽象哲学到具体的工程落地？

  - Foundry 中的 Ontology 并不是抽象哲学，而是一个 业务实体与关系的统一建模层，它把“数据 → 业务语义 → 应用逻辑”连成一体

- Ontology 是否能直接作为 **应用构建的底层** **DSL**，让低代码/无代码开发更容易？

- Ontology 如何把底层异构数据（表格、日志、传感器流）映射为“订单、车辆、客户、任务”等业务对象？

- Ontology 是如何实现类似 **图数据库/** **知识图谱** 的实体关系，却又能与关系型、列式存储共存？

- 当业务逻辑变化时（比如供应链规则调整），Ontology 如何支持 **版本化演进** 而不破坏历史数据？

- Ontology 和传统的 Schema-on-Read / Schema-on-Write 的根本差异是什么？它解决了哪些痛点？

- 一个典型的跨系统的Ontology定义是什么？是否可以举一个例子么？

- Ontology 相当于“动态、语义化的主数据管理”吗？与 Informatica/Collibra 的差别在哪？

- Ontology 在工程上如何实现 **数据层、语义层、应用层** 的耦合？

- 业务实体的 Ontology 建模是自动生成（AI/规则）还是需要人工主导？

- Foundry 是否允许多套 Ontology 并存？如果允许，如何保证 **跨 Ontology 的互操作性**？

- Ontology 建模能否借助 **AI 自动生成/推荐**？例如自动识别“订单、车辆、用户”并形成初始本体？

* * *

#### 22.2.3 数据层设计

* * *

##### 22.2.3.1 数据接入与存储

- Palantir 如何处理 **异构数据源**？是否支持实时流式数据？

- 从 **数据引入 → 存储 → 使用 → 归档/销毁**，Foundry 是否有端到端的生命周期策略？如何保证历史数据在可追溯的同时不造成安全风险？

- 在大规模数据场景下，Foundry 的存储是否支持 **冷热分层、自动压缩、智能索引**，如何在性能与成本之间平衡？

- 除了关系型与时序数据，Foundry 如何管理 **文档、图像、视频、传感器流等非结构化数据**？是否有统一的索引与检索能力？

* * *

##### 22.2.3.2 数据建模与语义抽象

- Foundry 的 **Ontology（本体）** 是如何抽象的？与传统的 Schema-on-Read / Schema-on-Write 有何不同？

- Foundry 的 Ontology 与传统 \*\*数据目录/元数据管理（如 Collibra、DataHub）\*\*相比，有哪些增强功能？

- 除了传统血缘（Lineage），Foundry 是否支持 **跨多源数据的语义血缘**，从业务语义层追踪数据来历？

* * *

##### 22.2.3.3 数据治理与安全

- 在 Foundry 中，数据血缘、权限控制、审计如何做到 **细粒度**？能否支持 **多租户**？

- 针对机密数据（政府/军工），Palantir 如何实现 **多级安全隔离**？

- 与 Schema-on-Read、Schema-on-Write、Data Lakehouse 的治理模式相比，Foundry 的治理模式有哪些独特优势与局限？

- 在企业数据治理和业务决策中，为什么传统的 Schema-on-Write、Schema-on-Read、Lakehouse 模式不足以满足“ **可追溯、可重现、可合规**”的需求？

* * *

##### 22.2.3.4 协作与 Git for Data 范式

- Palantir Foundry 在数据协作层面是否支持类似 **‘Git for Data’** 的范式？

- “Git for Data”是语义层的（如订单、车辆、客户、任务），还是具体到某个数据表、数据集？

- 数据快照与版本对比的粒度到什么程度（表级、行级、字段级）？

- 在多人同时修改同一数据集时，Foundry 如何避免 **“最后写入覆盖”** 的冲突？

- 是否支持 **Pull Request / Review** 流程，让数据变更先经过审批或校验，再合入主版本？

- 如何在大规模分布式团队中同步数据更改（类似 Git 的分布式克隆/推送模型）？

- 有哪些开源体系（如 LakeFS、DVC），可以部分实现 Foundry 里的 ‘Git for Data’ 模式？

- 地图对象（如道路网络、地理多边形、时序轨迹）在“Git For Data”的模式下，如何优化性能和存储？

* * *

##### 22.2.3.5 时间回溯（Time Travel）

- Palantir Foundry 的 **Time Travel 功能** 带来了哪些独特价值？它在整体架构中扮演怎样的角色，并解决了传统数据平台难以覆盖的哪些痛点？

- Foundry 的 Time Travel 是基于 **全量快照、增量日志（delta log），还是混合模式**？不同选择对存储与检索性能有什么影响？

- 在 TB/PB 级数据规模下，Time Travel 如何实现？如何避免存储膨胀，同时保证历史版本查询的低延迟？

- 当一个关键业务指标在历史版本中被回溯时，Foundry 是否能提供 **全链路的可解释性**（数据来源 → 转换逻辑 → 模型版本 → 决策执行）？

- Time Travel 回溯仅仅是“只读”，还是支持 **沙箱演练**？能否在历史版本上运行新策略，做“假如当时”的模拟？

- Foundry 的地理空间（Geospatial）场景里，地图数据是否支持 Time Travel（时光回溯）？假设在一个战场中，道路被反复毁坏和修复的场景中，如果需要复盘历史上的一个战况。

* * *

##### 22.2.3.6 大规模数据与决策取舍

- 在 PB/TB 级数据场景中，Foundry 是否会因为数据读取或处理时间过长，而选择只用部分数据来支持分析与决策？如果会，系统如何保证这种取舍仍然能支撑“ **足够好**”的决策？

- Foundry 的设计哲学是追求每次都生成“ **最优解**”，还是强调“ **及时、可解释、可落地的足够好决策**”？在哪些场景下，时效性优先于最优性？

- 当使用部分数据做快速决策时，是否能事后通过 **Time Travel 回溯** 或全量重算来校正和优化？

- 在牺牲部分数据完整性的情况下，Foundry 如何保证决策 **可追溯、可审计**，并让客户信任？

* * *

#### 22.2.4 算法与分析引擎

- Palantir 的分析引擎，本质是 算法库、工作流引擎，还是 ML 平台？它的定位和边界是什么？

- Foundry 的算法层与 Ontology 如何耦合？是否能让算法直接 面向业务对象（订单、车辆、客户），而非原始数据表？

- Foundry 内部的数据计算，是基于 分布式引擎（Spark/Flink），还是自研引擎？在哪些环节使用开源，哪些地方深度改造？

- 与 Databricks、Snowflake ML、SageMaker 相比，Foundry 的算法能力 差异化优势体现在哪里？

- 内置算子、数据处理与 ML pipeline 分别依赖哪些语言？（Python、R、SQL、Scala …）它们在平台中的 角色、优势与局限 各是什么？

- Foundry 如何管理 Python 等依赖的 版本升级与兼容性，避免“依赖地狱”？

- 算法是否被抽象为 可组合算子（Operators），支持 DAG 式的流程编排，类似 Spark/Flink？

- 在大规模推理或函数调用下，如何进行 算子级与代码级性能优化？

- 算法与业务场景如何结合？平台如何封装 决策优化、仿真与可视化推演？

- 算法结果是否能直接通过 Ontology 映射为 可视化对象（如车辆调度方案、库存水平），而不仅是抽象指标？

- 在多目标优化（成本、时效、风险）中，Foundry 如何展示 权衡空间（Pareto Frontier），让用户选择不同解？

- 是否提供交互式工具来探索 “解空间”，而不仅仅返回单点解？

- OR-Tools 等优化器如何与 业务对象与流程打通，形成闭环的资源分配与调度？

- 同一用例中，批处理、准实时、交互式分析如何统一调度，避免“为实时牺牲精度”的困境？

- 批处理、流处理与交互式查询如何在 Foundry 内部平衡？是否有一个统一抽象整合不同计算引擎？

- 在实时决策场景（应急调度）中，如何取舍 近似解与最优解？是否提供策略可配置？

- 针对大规模运筹优化（调度、网络优化），Foundry 倾向使用 启发式算法，还是数学规划/商业求解器？

- 在机器学习与 AI 方面，Foundry 是更偏向 AutoML、模型管理，还是聚焦于 数据管道与应用封装？

- Foundry 是否提供 ML/AI SDK，让用户在外部训练模型后无缝接入？

- 对于 TensorFlow / PyTorch / Hugging Face 等生态，Foundry 是否支持 一键部署与集成？

- Foundry 能否承担企业级的 MLOps 平台角色，还是更强调 算法与业务应用的深度耦合？

- Foundry 如何保证算法的 可解释性？是否能将输入、输出、关键变量与中间步骤完整暴露给业务用户？

- 当模型失效或数据漂移时，Foundry 如何触发 自动切换到规则系统或回滚机制？

- 算法层是否提供 监控视图，实时展示数据漂移、模型失效、优化收敛情况？

- 算法层是否支持 假设分析（What-if Analysis），并能在 Ontology 上模拟不同输入条件？

- 假设分析的 性能挑战 如何解决？是否支持近似计算或缓存优化？

- Foundry 的 What-if / Scenario Analysis 与 数字孪生（Digital Twin） 结合时，会遇到哪些工程挑战？

- 在复杂系统（供应链、能源网络、金融市场）中，Foundry 如何支持 多主体建模与博弈论分析？

* * *

#### 22.2.5 应用与场景封装

##### 22.2.5.1 行业模块与复用性

- Palantir 的行业模块是 **通用模板（如供应链、金融、能源）** 还是 **客户定制**？如何平衡“可复用”与“差异化”？

- Palantir 的行业解决方案，是以 **通用模板 \+ 定制化扩展** 的方式交付，还是为核心行业（国防、能源）内置了 **全链路场景封装**？

- Palantir 如何抽象 **跨行业共性的工作流**（如订单履约、调度、风险监控），同时保留行业特有差异？

- Palantir 如何保证 **跨租户复用**？一个行业模板能否被不同客户快速复用？

- 不同行业模块是否包含 **完整功能栈**（业务 KPI、预设算法、可视化组件、地图组件），还是仅仅是 **数据模型骨架**？

- 不同行业，组件配置差异如何体现？其 **定价方式** 是按行业套件、按模块，还是按使用量？

* * *

##### 22.2.5.2 场景化功能封装

- Palantir 是否会在场景封装时，把 **“业务角色 → 数据对象 → 应用界面”** 的映射直接做好？

- Foundry 是否提供类似 **“行业 App Store”** 的模式，让客户快速启用现成的应用？

- 类似 **“地图模块”** 在不同场景下的功能差异：

  - **军事**：卫星态势、战场推演

  - **能源**：管线网络监测

  - **供应链**：仓储选址、线路规划

- 同一个模块在不同行业里是 **裁剪版** 还是 **增强版**？

- Gotham 在安全/反恐场景下，具体的 **工作流与分析能力** 是如何封装的？

- Foundry 在供应链、金融等企业场景中，是否能形成 **行业级标准化模块**，还是必须 **高度定制**？

* * *

##### 22.2.5.3 低代码 / 无代码能力

- Palantir 的 低代码/无代码能力 在实际客户落地中扮演什么角色？面向的是 业务用户 还是 数据科学家？

- Palantir 的低代码 DSL 是否完全内嵌在 Ontology 层，还是允许 用户自定义扩展？

- 无代码应用是否支持 复杂业务逻辑编排，还是仅限于 轻量可视化与交互？

- 无代码组件能否与 Ontology 对象直接绑定（如“订单拖拽 → 自动生成调度分析”）？

- 在客户真实落地中，低代码的 局限性 主要表现在哪些方面？是否会导致 性能瓶颈或灵活性不足？

- 性能上，低代码生成的查询是否等价于专家手写 SQL/Python，还是存在优化差距？

- Palantir 是否允许企业将 自研 UI/组件 与其无代码框架集成？

- 当业务逻辑复杂超出 DSL 表达能力时，低代码与全代码如何无缝切换？

* * *

##### 22.2.5.4 SDK 与生态

- Palantir 是否提供 标准化 SDK / API（Python、Java、REST、GraphQL …），让开发者能把 Foundry 功能嵌入外部系统？

- SDK 的使用门槛与授权模式如何？是 开放生态，还是仅对 付费客户/战略合作伙伴开放？

- SDK的使用是否有收费门槛？

- SDK的主要版本的生命周期是怎样？

- SDK 的覆盖范围到哪一层？是仅限 数据读写，还是涵盖 数据管道编排、权限、模型部署、应用 UI 组件？

* * *

##### 22.2.5.5 定制化与长期演进

- 应用的 定制化开发 是否会导致 “二次开发陷阱”，增加平台长期的维护成本？

- Foundry 如何解决 二次开发的版本依赖和技术债务问题？

- 自动生成的 SQL/Python 代码是否 可追溯并版本化（类似 “Git for Low-code”）？

- 低代码工件是否能“一键转化”为 可编辑的 Python/SQL，实现 低代码与全代码的无缝切换？

- 当 DSL 与代码混用时，Foundry 如何 优化执行计划，避免性能损耗？

- 是否可以把 DSL 与 Python/R 的算子机制统一成 同一 AST 或中间表示，实现 低代码与全代码的同构？

- Palantir 是否探索过通过 LLVM 或 WASM，将 DSL 统一编译到多语言后端（Python、Go、Rust、C++），实现“一套语义，多种运行时”？

#### 22.2.6 系统集成与执行控制

- 系统定位：Palantir 在系统集成层的定位到底是什么？是替代传统中间件/ESB/BPM，还是更专注于“决策中枢 + 调度”的上层编排？若 Foundry 过度下沉到执行层，会否与 SAP/Oracle 的事务边界与控制权产生冲突？

- 与 iPaaS 的关系：Foundry 与现有 iPaaS（MuleSoft、Boomi、Informatica）在客户架构中是竞争还是互补？典型部署中是“Foundry 统一编排 + iPaaS 做连接”，还是相互替换？

- 数据桥接与安全：接入 SAP/Oracle 等核心系统时，Foundry 采用何种“官方/合规”的接入机制？例如 SAP 认证 Add-On 或标准 API 方式。这类“应用层级”的连接如何平衡实时性与对源系统的影响？

- SAP 连接拓扑与模式选择：连接 SAP 时有哪些推荐的架构模式？在不同网络分段/隔离场景下如何落地？

- 批/流一体与 HyperAuto：当需要从 SAP 持续同步时，是否采用流式同步（如基于 SLT），若没有流式条件时如何用“文件/镜像/预过滤抽取”的方式折中？对数据新鲜度与作业可靠性有何影响？

- 写回与一致性模型：业务操作需要回写第三方系统时，首选通过 Ontology Actions 实现（也可经 OSDK 或 API Gateway）。跨系统写回的“事务性”如何保证？是否建立幂等键、重试与补偿策略的标准化？

- 调用与权限边界：Foundry 下发指令时如何避免“超权限”调用？采用 API Key、Service Account 还是零信任的细粒度授权？不同方式对审计、轮换、最小权限落地的影响是什么？

- 跨系统一致性：当 AI 决策串联多个系统（如“库存调拨 → 订单结算 → 财务入账”）时，Foundry 是否内置分布式事务，或推荐 Saga/补偿模式？多步作业的失败域与回滚链路如何建模？

- 不友好系统接入策略：对接口不佳或老旧系统如何接？（直连表、文件/日志批量导入、RPA、定制适配器）的选择准则与风控边界是什么？在何种条件下建议采用影子模式而非直接下发？

- SDK 与标准化集成：是否提供标准 SDK/适配包加速对接主流系统（SAP/Oracle 等），以及统一的“适配层”以降低长尾系统集成成本？

- 速率控制与回压：当 Foundry 对第三方 API 高并发写回时，如何实施限流、熔断、排队与回压，避免拖垮源系统？这些策略与任务编排/重试/补偿如何协同？

- 灰度与沙箱：如何避免“一次性大规模下发”的系统性风险？是否具备从“沙箱推演 → 小流量灰度 → 全量执行”的发布策略？若第三方系统没有沙箱能力，如何以“规则模拟/只读校验”实现等价的安全演练？

- 容器化与可移植性：在本地数据中心或隔离网络中，Foundry 的集成与执行组件是否支持容器化/代理化部署？连接器版本、证书轮换、密钥管理与集中运维如何落地？

- 连接器与源类型版图：除 SAP/Oracle 等业务系统，Foundry 在对象存储、文件系统、JDBC/数据仓库等“数据平面”的连接版图与限制是什么？如何界定 Foundry 与 iPaaS 的边界？

#### 22.2.7 平台工程与架构演进

- Foundry/Gotham的架构是 单体演进 → 微服务 → 容器化 → 云原生，还是直接基于云原生？是否支持 混合云/多云部署？在客户本地数据中心部署时的难点在哪？

- 在业务前线（如海外军事任务）场景下，当敏感数据无法出境时，Foundry/Gotham 是否支持 边缘节点（Edge Node）部署？边缘节点与主节点在 功能覆盖、权限范围、数据处理能力 上如何划分？

- 在弱网或离线环境下，边缘节点能否保持自治运行与决策能力，并在网络恢复后实现与主节点的安全同步？在遇到威胁时候，边缘节点是否可以启用自动销毁的程序？

- 微服务与容器编排：平台是否全面容器化并采用服务网格？跨数百微服务的版本一致性、兼容矩阵、配置漂移如何治理？

- 架构演化与分层：Foundry/Gotham 的“控制平面 vs 数据平面”如何划分？哪些能力在控制平面统一，哪些必须贴近数据/业务落在数据平面？这种分层对发布、扩容、容灾有何影响？

- 发布火车与灰度策略：在多租户、多环境（SaaS、私有云、本地、边缘）下如何实现分批发布、金丝雀、回滚与特性开关的矩阵管理？发布失败域如何最小化？

- 断网/空隔与边缘：在隔离网络、间歇连通或边缘设备上，例如国防军工领域的客户无法实时联网，软件如何脱线接收补丁、验证签名、分段推进并保证状态一致？跨网域的“制品与元数据”搬运如何可控与可追踪？

- 多云与工作负载放置：平台如何做策略驱动的调度（成本、延迟、数据驻留、合规、GPU/CPU 资源）？跨云跨区的数据重力与计算迁移如何权衡？

- 多租户隔离：在“存储、计算、网络、日志、遥测、缓存”各层的隔离边界是什么？如何防止租户间噪声干扰并在共享集群中提供可预期的 SLO？

- 资源与成本工程：是否有统一的成本/容量治理（配额、自动扩缩容、抢占/Spot、冷热层、缓存）？针对大模型/GPU 作业，如何做混部、切片、抢占、批处理窗口的策略优化？

- 数据驻留与地域策略：多国/多地区法规要求下，元数据、日志、模型参数、向量索引等是否都能“就地”驻留？跨区协同时采用联邦/代理/最小可共享哪种模式？

- 技术栈与开源依赖：平台主要采用哪些开源组件（如 Kubernetes、Kafka、Spark/Flink、Arrow、Iceberg、Ray 等）？哪些部分是自研（如 Ontology、Action 引擎、治理/审计框架）？对开源的 **依赖深度** 与 **二次开发程度** 如何？是否存在 **替换/迁移路径**？在技术路线的选择上，是“通用开源 → 平台整合”还是“自研为核心 → 兼容开源”？

- 兼容性与可演化性：平台内Ontology、管道引擎、算子、SDK的版本如何共存？是否支持双写/影子运行以平滑升级复杂依赖？

- 观测与运营闭环：统一的日志、指标、链路追踪如何覆盖“数据 → 算法 → Action 调用 → 外部系统回执”的全链路？SLO/SLA 违约如何自动触发回滚/限流/降级？

- 备份与容灾：RPO/RTO 目标下，跨区多活、冷热备、对象存储快照如何组合？Time Travel 与传统备份/灾备如何分工，避免把回溯误当灾备？

- 工程供给效率：开发者如何获得“一键可复现环境”（模板化 Stack、样板管道、测试数据沙箱、Mock 外部系统）？是否支持预览环境与“变更即验证”的内环路？

- 配置与密钥管理：大规模环境的配置漂移如何检测与收敛？密钥/证书/令牌的轮换、分发、撤销如何自动化且可审计？

- 制品与供应链：平台是否产出可追溯制品（SBOM、签名、来源证明）并在部署端做策略校验？如何在断网环境中仍保持软件供应链的可信？

- 统一 SDK 与“适配层”：对主流系统（SAP/Oracle/数据湖/消息总线）是否提供版本化的标准适配包？长尾系统如何通过低代码适配层接入且在平台升级时不被“拉断”？

- 容量与队列调度：在批处理/流处理/交互式混合负载下，如何做统一排队与优先级，保证在线体验不被批作业“顶爆”？

- AIP 融合下的基础设施升级：引入 LLM/向量检索/代理编排后，平台如何演进GPU 调度、模型缓存、并发限流、提示与上下文缓存？这些能力是平台内建还是托管于外部推理服务？

- 审计与可解释：平台是否能把“谁用什么数据，触发何决策，经由哪些 Action，在哪些系统落地”完整沉淀为可检索的审计图谱？

- 审计粒度与最小解释单元：一次执行的“可解释性”最低需要包含哪些要素（输入快照、版本、规则/模型、外部响应、补偿链）才能满足复盘与合规要求？

- 环境模板与规模复制：是否存在行业/场景级环境蓝图（网络、权限、接入、监控、数据模型的最低集）以周级复制一个新环境？复制过程中的可变参数与不可变基线如何定义？

- 技术债务与退场机制：如何管理跨版本长期兼容带来的技术债？当客户选择退场或迁移时，平台是否提供一键导出/解耦路径避免“不可逆锁定”？

#### 22.2.8 与传统 IT/大厂、市场潜在竞争对手的比较

- 技术边界：Palantir AIP/Foundry 自称“把 AI 与数据与运营打通”，而 Databricks/Snowflake 更偏数据与模型工作负载、SAP/Oracle 更偏应用内嵌 AI。Palantir 的“从数据直达执行”与其他平台“从数据到洞察/从应用到自动化”在职责边界上究竟差在哪里？（能否跨系统下发 Action、是否仅在单一应用内建议/自动化）。

- 语义层 vs 业务模块：Palantir 的 Ontology 强调“把数据、模型、对象、动作”映射到统一的业务语义层；而 SAP/Oracle 的模块化 ERP 以流程/事务边界来组织数据。二者是数据驱动应用 vs 应用驱动数据的根本差异吗？在跨域场景（供应链 + 维护 + 财务）里，哪种语义组织更稳健？

- “企业级 AI 操作系统”的含金量：Palantir 所谓 OS for Enterprise AI 比 Lakehouse AI（Databricks）、Cortex（Snowflake）和 AI ERP（SAP Joule、Dynamics Copilot、Oracle Fusion AI）多出了哪些“能执行”的基础件（如统一动作模型、跨系统编排、可回滚）？又缺哪些“底层”能力（如湖仓原生算子/数据库原语/大规模训练设施）？

- 数据与治理栈对齐：与 Databricks（Unity Catalog/治理）和 Snowflake（原生治理 + Cortex）相比，Palantir 的数据治理、血缘、权限与可解释性覆盖到“动作/执行层”了吗？是否能把“谁在何时用何数据触发何决策并在何系统落地”闭环到同一治理面板？

- 模型路由与嵌入方式：Snowflake Cortex、Databricks Lakehouse AI、SAP Joule、Dynamics Copilot、Oracle Fusion AI 都宣称“内嵌/原生 AI”。Palantir 的多模型路由、BYOM 与业务对象/动作绑定相比之下更强还是更弱？在跨域任务里（如“从告警到工单到备件采购”），谁的端到端更顺滑？

- 执行半径：Palantir 强调“把建议变成执行”。而 SAP/Oracle/微软多在各自应用域内落地自动化；Snowflake/Databricks多停留在数据域。谁更擅长跨系统的可控执行（有无统一 Action/回滚/幂等/审批机制）？失败域如何隔离？

- 行业沉淀 vs 平台中立：Palantir 在国防、能源、制造的行业工作流与语义沉淀，和 SAP/Oracle 的纵深行业 Best Practices、微软/Dynamics 的角色工作台，哪种复用性/迁移性更强？跨行业落地的摩擦系数如何量化（时间、人员、变更成本）？

- 生态策略：SAP/Oracle/微软拥有成熟的 ISV + 实施伙伴生态；Databricks/Snowflake有大量数据/AI 生态。Palantir 是走应用商店/行业模块市场，还是主要靠自交付 + 合作伙伴？生态对规模化复制与客户锁定的影响是什么？

- 锁定机制的差异：传统厂商通过核心流程/主数据/许可实现锁定；数据云通过数据重力/治理体系实现锁定；Palantir 是否通过 Ontology + 应用/动作层形成“语义锁定”？这种锁定对客户是正外部性（减少集成成本）还是负外部性（迁移困难）？

- 云原生与多租隔离：与三大公有云原生 AI/数据平台相比，Palantir 在弹性扩展、资源隔离、多租户治理上是否存在短板或优势？其政府/隔离环境部署与“企业公有云”形态的差异如何影响 TCO 与交付速度？

- 端到端 AI 体验的取舍：Oracle/Fusion、SAP/Joule、Dynamics/Copilot把 AI 嵌入业务流程的“就地体验”很强，但跨系统联动有限；数据云的“数据侧一体化”很强，但“执行侧”薄。Palantir 若走“跨系统 OS”，在体验深度 vs 范围广度上如何选型？

- 成本结构与可持续性：数据云强调计算分离、按需弹性；应用云强调流程价值；Palantir 若承担编排 + 语义 + 执行三层，单位用例的端到端成本是否可控？与“各域原生 AI”（Joule、Copilot、Fusion AI）相比的长期运维负担如何？

- 竞争—协作关系演化：Palantir 会被定义为“上层编排/应用平台”叠加在数据云/应用云之上，还是会与 Lakehouse/数据云、AI ERP 发生直接替代竞争？在客户主架构中如何划清边界以避免“平台内卷”？

- 针对大型企业的落地路径：若客户已深度采用 SAP/Oracle + Snowflake/Databricks + Microsoft Copilot，Palantir 的最小可行切入点是什么（如先做语义层与跨系统编排）？替换路径与共存路径各自的迁移风险与收益模型如何设计？

- “行业云 vs 跨行业基座”的取舍：Palantir 会不会也走“行业云”（国防云、能源云、制造云）来获得复制效率，还是坚持“跨行业基座 + 行业模板”的路径？哪种更利于生态扩展与产品化？

- Palantir目前的产品形态下， 选择与 AWS、Azure、Google Cloud、Oracle 等合作，而不是直接替代，它在生态中的独特定位是什么？其规模增长到什么程度，就可能会跟这些生态链上下游产生竞争？

#### 22.2.9 商业模式与客户价值

- Palantir 的收入模式：订阅制、项目制、还是混合？如何平衡“规模化可复制”与“深度交付”？如何避免被客户视为高级一点的“外包团队”，而是定位为长期战略伙伴？

- Palantir 如何将抽象的“AI驱动决策”量化为客户的 ROI（节约成本、降低风险、提升收入）？

- Palantir 自己在衡量一个客户价值时，ROI 的衡量周期是短期（季度/年度）还是长期（3-5 年）？

- 在客户 ROI 上，它如何证明自己比传统 IT 或咨询更具性价比？

- Palantir 在 **生态合作** 上的策略：是封闭（自研全栈）还是开放（对接 AWS、Azure、GCP、第三方 ML 工具）？

- Palantir 的客户一旦迁移到 Foundry/Gotham，其退出成本体现在哪些层面？（数据模型、工作流、治理体系）

- Palantir 这种“深度绑定”是否会引发客户对锁定风险的担忧？客户被绑架的代价是多大？有没有替代品？

- 在金融、供应链、政府安全等不同行业中，Palantir 的商业模式有何差异？

- 是按照“用户数 / 节点数 / 数据量”收费，还是以“价值分享”方式收费？在不同的阶段是怎样的收费模式？“价值分享”在商业合同上具体怎样设计？

- 当客户在某些场景（如供应链优化节约几亿美元）看到效果后，Palantir 会按 收益比例 或 规模扩展费用 来收取更高的合同金额。但是降本增效总有到极限的一天，如果到时候没有更多的优化空间，Palantir 的“价值分享”收益来自于哪里？是否存在业务上的天花板？

- Palantir 的护城河究竟是：

  - 技术（Ontology、低代码 DSL、封装）

  - 行业 know-how（深耕国防/能源/供应链）

  - 深度交付（强咨询 \+ 长期绑定）  三者哪个才是 不可替代 的？

* * *

#### 22.2.10 Palantir  AIP，AI专题

##### 22.2.10.1 战略定位与生态角色

- Palantir 在 AI 时代的定位：是继续做 数据驱动的企业操作系统，还是转型为 AI 驱动的企业操作系统？

- 在 AI Agent 崛起的背景下，Palantir 会成为 AI Agent 的承载操作系统，还是会被新一代 Agent 平台取代？

- AIP 的战略定位是 Foundry/Gotham 的 AI 插件，还是一个 独立的 AI 原生平台？

- AIP与 Copilot Studio / LangChain Hub， AWS Bedrock / Azure OpenAI，这些的区别？

- AIP 与 OpenAI、Anthropic、Mistral 等 LLM 平台相比，核心差异在哪里？是“行业封装 + 合规治理”，还是在算力、算法层直接竞争？

- AI 时代是否会改变 Palantir 的商业模式？（订阅制 vs AI SaaS + Agent 平台）

##### 22.2.10.2 技术架构与大模型融合

- Palantir 的大模型定位：是作为 嵌入式工具（辅助提升可用性），还是 底层操作引擎（直接驱动 Foundry 工作流）？

- AIP 是否具备 多模型路由能力（根据任务自动选择 GPT、Claude、Mistral、本地模型）？

- 客户能否 部署自有大模型 并与 AIP 无缝对接？调用时的数据是否有外泄风险？

- 在调用 LLM 时，AIP 如何解决企业数据的 语义鸿沟？是否具备自动 Prompt 生成与 Ontology 映射机制？

- AIP 是否采用 短期会话上下文 + 长期知识记忆 的分层架构？是否结合 Vector DB + Ontology Cache？

- 是否区分 自然语言推理（LLM） 与 数值计算/规则引擎，避免 LLM 在金融/国防场景中做错误计算？

##### 22.2.10.3 Ontology 与行业专家壁垒

- Palantir 过去依赖行业专家手工构建 Ontology，这是其壁垒之一。AI 时代是否降低了这道壁垒？

- 大模型能否自动生成行业 Ontology（如供应链、金融风控、国防），并长期维护？

- 如果大模型可以直接从数据库 Schema 和业务日志生成“半自动 Ontology”，Palantir 的行业专家护城河还成立吗？

- Ontology 的价值在于“ **动态演化**”，Palantir 是否能建立 **AI + 人机共建** 的 Ontology 演进体系？

- 如果行业 Ontology 可以被 AI 快速生成，Palantir 如何在 **深度绑定客户业务逻辑** 上保持护城河？

- 大模型调用 Ontology 时，是 **一次性全量挂载**，还是 **按需懒加载 \+ 会话缓存**？

- 是否存在一个全局的 “Ontology-aware System Prompt”，统一指导模型如何解释对象与字段？

- Ontology 是否可以作为训练客户私有模型的数据资产？Palantir 是否提供这种能力？

##### 22.2.10.4 工程化，AI Agent 化与工作流重构

- Ontology 作为记忆层：Palantir 的 Ontology 把业务对象和数据关系建模在一起，它是否天然适合作为 AI Agent 的长期记忆与状态存储？如何处理“会话态 + 持久态”的边界？

- Ontology 的颗粒度：一个 Ontology 需要多大颗粒度、多少层关系，才能既让 AI 灵活调用，又不至于触发 Token 爆炸和性能瓶颈？

- Action 抽象与事务语义：在 Palantir AIP 中，AI 通过 Action 执行业务或系统操作。Action 的最佳抽象层级是“业务级操作”还是“底层系统调用”？是否需要事务特性（前置/后置条件、幂等键、补偿钩子）来保证可靠性？

- 反馈闭环：Agent 在执行 Action 后，如何把结果反馈到 Ontology？Palantir 是否内置了“自我纠错”或“再训练”机制？

- LLM 与 Functions 的分工：Palantir 坚持把数值计算、约束校验放在 Functions，而不是交给大模型。这是否说明在关键行业中，大模型只能做编排，无法替代传统求解器？

- 混合推理与算力分配：AIP 如何在大模型推理（LLM）与传统优化器/仿真器之间做算力分配？在一个决策链路中，哪些环节适合概率推理，哪些必须交给确定性算法？是否有调度器自动做“任务切片”和“算力路由”？

- 推理层路由与模型选择：AIP 是否支持根据任务复杂度与实时性需求，动态选择“小模型处理高频请求，大模型处理复杂问题”？调度策略如何实现？

- 不确定性处理：当 LLM 输出带有概率性时，AIP 如何与传统确定性计算融合？是否存在多路候选计划、再由优化器选优的机制？

- 实时性与流式场景：在高频决策（金融交易、供应链调度）场景下，AIP 如何保证 LLM 推理的延迟不会拖垮整体工作流？

- 上下文缓存与会话态：AIP 是否支持 Context Cache / Session State，避免在长会话或多 Agent 协作中重复加载大规模上下文？

- 流式响应与渐进式结果：在需要人机交互或长链路推理时，AIP 是否支持流式输出中间结果，让用户在等待最终决策前就能获取阶段性反馈？

- Copilot 的查询方式：AIP Copilot 生成查询结果时，是通过 SQL/GraphQL 显式调用 Ontology，还是通过语义向量检索？不同方式在可解释性与性能上差异怎样？

- 跨系统编排能力：AIP Copilot 是否支持跨系统编排（ERP、SCM、IoT、GIS），还是主要局限在 Foundry 内部？

- 插件化生态：AIP 是否支持 “Bring Your Own Tool (BYOTool)” 与 “Bring Your Own Model (BYOM)”，让客户自由集成自有系统与模型？

- Agent 框架的策略：Palantir 会发展自己的 Agent 框架/DSL，还是更多对接 LangChain、AutoGen、Copilot Studio 等第三方生态？

- 行业模块的演变：传统 Foundry 行业模块（地图、KPI、工作流）未来是否会演变为可直接调用的“Agent 角色库”？

- 多 Agent 协作：Palantir 是否支持多个 Agent 基于统一 Ontology 协作？如何避免任务冲突、循环调用或资源死锁？

- 推理链的透明度：AI Agent 在调用 Ontology + Action 时，是否会自动生成可追溯的“推理链路”，帮助用户理解为什么做出某个决策？

- UI 与低代码封装：AIP Copilot 是否能生成可直接运行的 UI（报表、地图、仪表盘），还是只负责数据调用？这对非技术用户的上手有多大帮助？

- 迭代与可演化性：Ontology、Action、Functions 的设计是否支持迭代演化？在 AI Agent 持续学习的情况下，如何避免模型与数据结构“脱节”？

- 自我进化：Ontology与Agent之间是否可以实现相互的自我进化？

##### 22.2.10.5 安全、权限与责任边界

- 最小权限控制：在 AIP 中，Agent 调用 Action 时如何保证最小权限？是否存在类似 RBAC/ABAC 的自动收敛机制？

- 高风险指令的边界：当 Agent 获得执行权（如航班调度、资金调配、军事命令），Palantir 如何设定权限与责任分界？

- 权限体系继承：AIP Copilot 的权限模型是否完全延续 Foundry 的细粒度控制？

- 权限粒度可扩展性：Palantir 的权限可达“对象-属性-操作”级别，在 AI 驱动自动化场景下，这种粒度是否会爆炸式膨胀，最终难以维护？

- 风险拦截机制：是否存在 Policy Engine / 审批环节，用来阻止危险的 AI 指令落地？

- 可追溯性保障：如何确保 AI 输出具备可追溯、可验证、可解释特性？

- 黑箱风险与新护城河：LLM 的概率黑箱属性，是否反而让 Palantir 的合规、审计与安全治理成为新的差异化壁垒？

- 可解释性的最小单元：一次 Action 的解释是仅记录“模型调用日志”，还是包含“业务语义解释 + 数据溯源”？

##### 22.2.10.6 成本与商业模式

- AI Native 的 Palantir 是否会因大规模模型调用增加客户成本？

- Palantir 是否会发展 **轻量推理框架（Distilled Agent / 小模型）** 来降低成本？

- AIP 的定价模式是基于 **调用次数、算力消耗**，还是基于 **场景/用户打包**？如何避免与 LLM API 厂商产生“双重计费”？

- 是否提供 **AI 成本透明化仪表盘**，让客户实时监控 AI 使用成本？

##### 22.2.10.7 未来演进与竞争格局

- 如果未来的 AI 平台天然具备 **数据处理与集成能力**，Palantir 的独特价值还在哪里？

- LLM 的概率模型本质（非逻辑引擎）和上下文窗口限制，是否反而让 Palantir 的 **Ontology 与长期记忆** 成为优势？

- 如果出现 **可解释性更强的 AI**，Palantir 的数据治理价值会被稀释吗？

* * *

### 22.3 参考资料：

### Palantir 并非大模型浪潮下才出现的新玩家，而是经历过多轮业务与架构迭代的老公司。先把这段演化史补齐，才能从那些情绪化的吹捧与质疑中抽身出来，比较冷静地判断它的真实价值。

#### **22.3.1 Palantir Gotham** 架构演化

**初期架构（2008–2014）**

- 部署模式：Gotham 诞生于情报/政府场景（CIA、FBI 等），一开始就是高度封闭、本地化部署的单体/模块化架构。

- 技术栈：大量使用 Java/Scala + 大规模关系数据库（Oracle、Postgres），再配合 Palantir 自研的“数据整合层”和“知识图谱层”。

- 特征：强调 数据集成与图谱搜索，把异构数据源统一到一个 Ontology，再提供高可视化的情报分析工作台。

- 局限：扩展性不足，依赖人工定制 ETL 与工作流，难以快速适配新业务场景，也无法高效跨多客户/多租户交付。

**中期演进（2014–2017）**

- Palantir 面对政府与企业客户同时扩张，开始意识到 Gotham 的 **交付与升级成本过高**。

- 当时的 Gotham 架构逐渐拆分出 **服务化组件**，如数据接入、治理、权限、可视化，但整体仍然是 **较重的应用交付**，而非云原生。

- Palantir 工程团队在内部尝试容器化，但真正的转折点是在 2017 年 **Rubix 项目**：该项目用 Kubernetes 重构了 Palantir 的云基础设施。

**向 Foundry 云原生过渡（2017 之后）**

- Gotham 的很多底层能力（数据建模、图谱、权限体系）被抽象出来，逐渐融入 **Foundry** 的统一平台。

- 随着 **Apollo** 成熟，Palantir 能够在多云环境快速迭代产品，Gotham 也逐渐被“再平台化”为 **Foundry 上的一个垂直应用**（面向政府/情报安全）。

- 今天 Gotham 在架构上不再是独立的单体，今天 Gotham 实际上是 **运行在 Foundry 栈上的一个垂直应用**（Government Vertical），而 Foundry 是底层通用操作系统。

#### **22.3.2 Palantir** 主要的技术特色：

1. **Ontology（业务本体层建模）**

- 把跨系统的数据抽象成业务对象（订单、卡车、患者、任务）与关系。

- 语义层直接面向业务人员，而不是表/字段。

- 核心卖点：让跨系统、跨组织的数据治理与决策更直观、更可协作。

* * *

2. **Git for Data（数据版本化与 Time Travel）**

- 每个数据集、对象、关系、工作流都有不可变版本。

- 支持时光回溯、回滚、分支与合并（类似 Git 但面向数据）。

- 核心价值：可追溯、可重现、可审计。

* * *

3. **细粒度安全与合规体系**

- 行级、列级、对象级权限控制，跨部门/跨组织共享时依然可控。

- 内置审计日志，符合 GDPR、HIPAA、CCPA 等合规要求。

- 核心卖点：高安全环境（军工/政府）到商业场景都能通用。

* * *

4. **数据血缘与语义血缘（Lineage & Semantic Lineage）**

- 不仅能追溯表字段来源，还能追溯业务对象的语义来历。

- 例如：“这个库存数来自哪些仓库传感器 → 哪些订单 → 哪些系统”。

- 核心价值：增强可解释性，支撑风控、合规、审计。

* * *

5. **跨系统数据集成能力**

- 支持结构化（ERP、DB）、非结构化（PDF、图像）、实时流（IoT、Kafka）。

- 提供标准连接器、SDK、自定义适配器，甚至支持 RPA 抓取。

- 核心价值：能在“接口不友好”的环境中，依然打通多源异构数据。

* * *

6. **工作流与 Saga 式补偿机制**

- 支持跨系统编排（Orchestration），自动化数据流和决策执行。

- 通过 Saga 模式实现最终一致性（补偿事务、幂等、重试、死信队列）。

- 核心价值：让数据流不仅能“看”，还能“驱动执行”。

* * *

7. **沙箱与灰度执行机制**

- 支持沙箱演练（基于历史数据回放）、小范围灰度执行、全量推广。

- 可以在 Ontology 对象上模拟业务策略（如改派订单），避免大规模混乱。

- 核心价值：保证高风险环境（军队、供应链）中的安全落地。

* * *

8. **可视化与全局推演能力**

- 内置全景地图、时间轴、关系图谱。

- 不仅是 BI 报表，而是“业务沙盘”，支持作战指挥/供应链调度/应急演练。

- 核心价值：让复杂数据直接对应现实世界，直观驱动决策。

* * *

9. **开放生态与模型集成**

- 支持外部 AI/ML 框架（TensorFlow、PyTorch）、第三方模型（DataRobot、SageMaker）。

- 模型运行在 Foundry 语义层之上，直接作用于业务对象。

- 核心价值：不是替代 AI 平台，而是让 AI 真正进入业务流程。

* * *

10. **全链路协作与审计闭环**

- 开发者、数据科学家、分析师、业务人员可以在同一 Ontology 层协作。

- 每一步操作（数据更新、模型执行、报表生成）都有审计记录。

- 核心价值：在高度复杂的组织环境里，保证 **透明、可控、可信**。

#### **22.3.3 跨系统的Ontology 的例子：**

跨系统的“订单（Order）” Ontology 定义

业务对象（Entities）

01. Order（订单）

    1. 来自 ERP 系统（SAP/Oracle）：订单号、客户 ID、产品、数量、价格、状态。

03. Shipment（运输批次）

    1. 来自 TMS 系统：承运商、卡车/司机、起点、终点、预计到达时间。

05. Inventory（库存）

    1. 来自 WMS 系统：仓库位置、可用库存、批次号。

07. Sensor（传感器数据）

    1. 来自 IoT 系统：温度、湿度、GPS、卡车位置。

09. Customer（客户）

    1. 来自 CRM：客户信息、信用等级、合同条款。

* * *

关系（Relationships）

- Order → Shipment：一个订单可以被分配到多个运输批次（部分发货）。

- Order → Inventory：订单关联仓库库存，用于判断是否可发货。

- Shipment → Sensor：运输批次与卡车 IoT 数据绑定，用于实时监控。

- Order → Customer：订单与客户绑定，支持信用风险控制。

* * *

版本化 & Time Travel

- 订单状态从 _创建 → 已发货 → 在途 → 签收 → 退货_，每个变化在 Ontology 里都有版本号。

- 可以回溯“订单 12345 在 2024/07/01 时，绑定的是哪个仓库、哪个司机、哪辆车”。

* * *

Ontology 带来的统一视图

在传统系统里：

- ERP 只知道订单和合同；

- WMS 只知道库存和出库；

- TMS 只知道卡车和路线；

- IoT 只知道传感器信号。

在 Foundry 的 Ontology 里：  👉 “订单”成为一个统一的业务对象，跨系统的数据都挂载到这个对象上，这样业务人员和决策者不用去查 4 个系统，就能直接看到订单的全景。

#### **22.3.4** Foundry的主要技术栈：

**前端（用户界面层）**

Foundry 的前端本质是一个 **Web 平台**，用户通过浏览器访问，主要技术方向包括：

- **框架与语言**

  - **TypeScript + React** → Foundry 的主要 UI 框架，用于构建工作台、仪表盘、低代码应用界面。

  - **GraphQL / REST** → 与后端的数据查询和交互。

- **可视化与地图**

  - **WebGL** → 浏览器端渲染引擎。

  - **MapboxGL** → 地图与 3D 场景渲染（Foundry 的 Map/Contour 模块基于此）。

  - **D3.js / Highcharts** → 常规 BI 可视化组件。

- **交互体验**

  - 浏览器端低代码工具（App Builder、Workshop），封装了 React + 内部 DSL（领域专用语言）。

  - 多人协作机制类似 Google Docs，前端需支持实时同步与权限控制。

* * *

**后端（应用逻辑与计算层）**

Foundry 的后端是一个 **云原生 \+ 分布式计算** 架构，核心技术栈包括：

- **运行与调度**

  - **Kubernetes** → 统一容器编排平台。

  - **Apollo** → Palantir 自研的持续交付与多云部署系统，确保 Foundry 能在 AWS、Azure、GCP 或本地数据中心一致运行。

- **数据存储与处理**

  - **分布式存储**：对象存储（S3 兼容）、列式存储（Parquet、ORC）

  - **关系数据库**：Postgres、Oracle 等，用于事务型与元数据管理。

  - **分布式计算引擎**：Apache **Spark**（批处理/机器学习）， **Flink**（流处理场景）。

  - **Graph 数据存储**：内部有知识图谱/本体管理，早期 Gotham 用过 Titan/Neo4j 等，Foundry 更可能采用自研或基于分布式 KV。

- **数据治理与权限**

  - 内置 RBAC/ABAC 模型，支持行/列/单元格级别权限。

  - 血缘追踪和审计日志存储，通常用 **Kafka + ElasticSearch** 或自研管道。

* * *

**AI / 数据科学集成**

- **工作台（Code Workbooks）**：

  - 支持 **Python、R、SQL**，直接运行在 Spark 集群或容器沙箱里。

  - 集成 scikit-learn、TensorFlow、PyTorch 等常见库。

- **模型管理**：

  - 内置 MLOps 模块，支持版本控制、实验追踪、模型部署。

  - 与外部 MLflow、SageMaker 有一定程度对接能力。

* * *

**DevOps 与运维**

- **CI/CD**：Apollo + Git 集成。

- **监控**：Prometheus、Grafana、Elastic Stack 结合内部工具。

- **安全合规**：Kubernetes 原生安全策略 + Palantir 自研隔离机制，满足政府/军工客户的多级保密要求。

* * *

**总结**

- **前端**：TypeScript/React + WebGL/MapboxGL + GraphQL

- **后端**：Kubernetes + Apollo + Spark/Flink + 分布式存储（S3/Parquet）+ 强权限治理

- **AI 层**：Python/R/SQL 工作台 + MLOps

- **核心差异点**：不是某个单一技术，而是 **数据本体（Ontology）+ 安全权限体系 + Apollo 多云交付**，这三者形成了 Palantir 的独特技术护城河。

#### **22.3.5** Foundry与传统的MDM的主要差异：

|     |     |     |
| --- | --- | --- |
| 维度 | 传统 MDM（Informatica / Collibra） | Palantir Foundry Ontology |
| 定位 | 数据治理工具（管好 Golden Record、标准化主数据） | 业务语义层 \+ 应用开发基座（建模、可视化、工作流） |
| 数据形态 | 以 表/字段 为核心（Customer 表，Product 表） | 以 对象/关系/动作 为核心（Customer→下单→Order） |
| 集成模式 | ETL/ESB，先抽取清洗再写回 MDM | Schema-on-Read，Ontology 映射到源数据，避免复制 |
| 使用人群 | 数据治理/IT 部门（负责全局主数据） | 一线业务/开发（在 Ontology 上直接构建应用） |
| 更新节奏 | 主数据版本更新较慢（季度/年度） | 动态、可实时更新（支持 Time Travel 和差异对比） |
| 产出 | 干净的数据资产 | 可直接驱动应用的业务模型、图谱、工作流、权限 |
| 扩展性 | 偏治理、目录化 | 内置 DSL，低代码/无代码开发，直接跑应用 |

#### **22.3.6** Foundry 的权限控制体系：

Foundry 的权限体系分为几个粒度：

- **源数据层**：传统的行/列/表权限（类似数据库 ACL）。

- **Ontology 层**：以业务对象为中心（例如 `Order`、`Customer`、`Warehouse`）。

- **属性级别**：某些敏感字段（例如客户身份证号） → “可见/不可见/脱敏”。

- **实例级别（Row-level Security）**：例如“销售 A 只能看到自己负责区域的订单”，通过 Ontology 映射规则实现。

- **操作级别**：不仅是“看”，还能限制“能不能触发某个动作”，例如：

  - 可以查看订单状态

  - 但不能触发“取消订单” 或 “重新分配库存”的操作

**技术实现方式：**

- **Policy-as-Code**：Foundry 提供策略引擎，权限规则可以写成可配置的策略（JSON/YAML/DSL），而不是硬编码。

- **语义绑定**：权限不是绑定在表字段，而是绑定在 Ontology 对象 → 比如“Order.totalAmount 只有经理能看”。

- **动态评估**：规则执行时可以基于上下文，比如 `user.role = manager` 且 `region = APAC` 时放开访问。

- **遮罩/变形**：不是只有“能看/不能看”，还支持“能看但脱敏”，如显示 `****1234` 的银行卡号。

**为什么 Ontology 层的权限更强？**

在 ERP 或数据库里，权限通常是：“这个表谁能看”，“这个字段谁能看”。

但 Foundry Ontology 的权限模型是：

- “谁能看 **订单** 这个对象”

- “能看订单里的哪些属性（如金额、客户地址）”

- “能对订单对象执行哪些动作（取消、修改、审批）”

- “这些权限在不同上下文是否变化（只限自己部门）”

这样权限和 **业务语义** 紧密对齐，而不是死板的表结构。

|     |     |     |
| --- | --- | --- |
| 维度 | 传统数据库 / ERP 权限 | Foundry Ontology 权限 |
| 控制对象 | 表、字段（Column-level Security） | 业务对象（Order、Customer、Asset）、属性（字段）、实例（单条记录）、操作（动作） |
| 粒度 | \- 表级（Table ACL） - 字段级（Column ACL） | \- 对象级（Object-level） - 属性级（Attribute-level） - 实例级（Row-level, Region-level） - 操作级（Action-level） |
| 业务语义 | 权限绑定在表结构上，语义弱 | 权限绑定在 Ontology 对象及关系上，直接映射业务逻辑 |
| 上下文动态性 | 固定规则（谁能看哪个表/字段） | 动态策略：基于用户角色、部门、地域、上下文条件（Policy-as-Code） |
| 操作权限 | 通常只有 CRUD（增删改查） | 可定义“业务动作权限”，如 cancelOrder、approvePayment、rerouteTruck |
| 数据遮罩 | 部分支持（如脱敏视图） | 内置多级遮罩：完全隐藏、部分脱敏（\*\*\*\*1234）、汇总级展示 |
| 跨系统一致性 | 难以统一，不同系统各自实现 | 统一在 Foundry Ontology 层做语义权限管理，跨系统执行一致 |
| 审计能力 | 日志较粗粒度（谁访问了表/字段） | 精细审计：谁在什么上下文下访问了哪个对象的哪个属性、执行了什么操作 |
| 价值定位 | 偏技术安全控制 | 语义安全 / 业务安全控制，更贴近真实世界权限需求 |

#### **22.3.7** Foundry 的前端使用方式

**Web 界面为核心**

    Foundry 提供一整套 **基于浏览器的工作台（Workspaces）**，用户直接通过浏览器访问。

    核心模块包括：

-  Ontology（数据本体建模）：定义业务实体与关系。

-  Data Lineage / Pipeline Studio：拖拽式数据管道编排。

-  Code Workbooks：数据科学家可以直接写 Python、R、SQL，调用 Spark / ML 库。

-  Visualization / Dashboards：BI 风格可视化，内嵌在 Foundry 界面中。

-   App Builder / Workshop：低代码构建行业应用。

**角色驱动的界面**

- 业务人员：通过 Dashboard、Workshop（类似 Power BI / Tableau + 低代码表单）。

- 数据工程师：通过 Pipeline Studio 和 Dataset 浏览器。

- 数据科学家/分析师：通过 Code Workbooks 或与外部 IDE（Jupyter、VSCode）集成。

Foundry 的 3D 地图性能：浏览器端体验

- Palantir Foundry 并没有单独的桌面客户端，它的 2D/3D 地图完全依赖浏览器端的 WebGL 来渲染。对用户来说，打开方式很简单，但这也常常引出一个担心： **只靠浏览器，会不会卡？**

其实能否流畅，取决于几个关键点：

- **硬件加速**：如果浏览器没有开启 GPU 加速，或者显卡驱动不支持 WebGL，那么加载 3D 场景一定会卡顿。这个问题在一些虚拟机或企业锁定环境里尤其常见。

- **数据规模**：地图并不怕“3D”，怕的是“一次性加载太多”。矢量要素过密、点云数据没做抽稀，或者 3D 模型没有分级细节（LOD），都会让前端直接崩溃。

- **网络与传输**：3D 地图的瓦片、纹理和模型体积都很大，如果网络带宽差，表现上就会是卡顿和延迟。

Foundry 的做法是：

- 在浏览器端用 WebGL 进行渲染，但在后端提前做好“切片、抽稀、聚合”，前端拿到的已经是可视化友好的结果。

- 对大数据场景提供分层加载，比如业务人员看到的是简化版的图层，只有在工程师或分析人员需要时，才会加载完整的三维细节。

- 如果前端设备实在跑不动，还有传统的轻量回退模式可以用。

总结一下：Foundry 的 3D 地图性能瓶颈不是“浏览器”，而是 GPU 配置、数据处理和网络环境。在正确的架构下，即便是普通办公电脑，也能流畅跑相当复杂的三维场景。

#### **22.3.8** 将Palantir 的能力抽象为数据模型（Data Model / Ontology）

- **定位**：Palantir 强调“语义层 + 本体（Ontology）”，即用统一的数据模型描述业务世界。一个工厂里的“卡车”“仓库”“订单”“人员”都能抽象成数据对象，并建立关系。

- **扩展能力**：

  - 可以快速复用到不同场景（军事、能源、金融），只需换一套行业语义层。

  - 新数据源接入后，只要映射到统一模型，就能立即参与分析和决策。

- **限制**：

  - 高度依赖 **建模能力和行业理解**，不同客户的语义差异大，实施成本高。

  - 在一些高度动态、非结构化的数据环境（例如社交媒体、非标准 IoT）下，建模难度陡增。

#### **22.3.9** 将Palantir 的能力抽象为知识图谱（Knowledge Graph）

- **定位**：很多人认为 Palantir 的底层更接近知识图谱：把人、物、地点、事件串联起来，形成“因果/关系网络”，支持查询与推理。

- **扩展能力**：

  - 非常适合 **情报分析、风险控制、供应链可视化** 等需要多实体、多关系的场景。

  - 天然支持“事件追溯、可视化、推理”，利于发现隐藏模式。

- **限制**：

  - 图谱模型擅长“关系”，但在 **数值型优化**（如线性规划、调度优化）上能力不足，需要外接算法引擎。

  - 知识图谱本身难以处理 **实时高频数据流**（如传感器毫秒级信号），必须依赖额外的流式计算框架。

#### **22.3.10 抽象为操作系统内核（OS Kernel for Data & Decisions）**

- 定位：Palantir 自己喜欢用“操作系统”来描述——它像是组织的数据内核，外接各种“设备驱动”（业务系统、数据库、API），然后在统一环境里运行“应用”（决策工作流、分析模块）。

- 扩展能力：

  - 具备极强的横向扩展性：理论上任何系统、任何数据都能接入，只要写好“驱动”。

  - 可以形成完整的生态体系（就像操作系统之上跑应用），合作伙伴和客户可以自己开发应用。

- 限制：

  - 复杂度高：操作系统式的抽象需要庞大的权限管理、进程调度、安全体系，这也是 Palantir 实施成本昂贵的原因。

  - 易受锁定效应约束：既然是“OS 内核”，客户一旦上了 Palantir，迁移成本极高，但这同时意味着 Palantir 难以被“轻量化”采用。

#### **22.3.11** Foundry 的端到端数据生命周期管理

① 数据引入（Ingestion）

- Foundry 支持多源数据接入（数据库、API、IoT 流、文件），并在入口就进行权限控制与日志记录。

- 每条数据的来源、时间戳、转换规则都会被自动记录（即所谓的 _lineage_ 数据血缘）。

- 引入时可以配置 合规策略（如 GDPR、HIPAA），对敏感字段自动脱敏或加密。

② 存储（Storage & Modeling）

- 底层可连接客户已有的存储（Snowflake、S3、HDFS 等），Foundry 作为逻辑层而非“霸占数据”。

- 数据存储采用多层抽象：原始层（Raw）、清洗层（Refined）、语义层（Ontology）。

- 每层数据都带有 版本控制（类似 Git for Data），保证修改可回溯。

③ 使用（Usage & Execution）

- 数据被用来驱动分析、可视化、建模和工作流。

- Foundry 提供细粒度权限控制（行级、列级、对象级），确保不同角色只能看到该看到的。

- 所有查询、修改、导出行为都会自动审计，便于事后追溯。

- 历史版本的数据可随时“时光倒流”，保证分析结果的可验证性。

④ 归档/销毁（Archival & Deletion）

- Foundry 支持根据\*\*数据保留策略（Retention Policy）\*\*对过期数据进行归档或彻底删除。

- 归档的数据可转入低成本存储（冷存储/离线仓库），并与权限体系绑定。

- 合规销毁机制：敏感数据在达到合规年限后可强制删除，同时保留“元数据审计记录”，确保历史可追溯但内容已清除。

#### **22.3.12** 如何在“可追溯”与“安全风险”之间平衡

- 可追溯性依赖的是 _元数据和血缘信息_，而不是保留所有原始数据。Foundry 通过“记录操作日志 + 保留数据版本号”，实现溯源。

- 安全性依赖的是 _细粒度权限 \+ 动态加密_：即使数据存在历史版本，也未必能被访问，除非用户权限允许。

- 合规性：Foundry 内置对 GDPR、CCPA、HIPAA 等合规框架的支持，可以自动触发数据过期删除，同时保留“销毁记录”，做到“证明已删”。

- 最小暴露原则：审计和追溯只对谁做了什么操作进行保留，而不一定保留敏感数据本身。

#### **22.3.13** Foundry 的“Git for Data” 与代码 Git 的相似点，以及区别

- 版本化（Versioning）：  每次数据变更都会生成一个版本号，任何分析、建模都基于“某个具体版本”，保证可重现性。

- 不可变快照（Immutable Snapshot）：  历史版本不可修改，只能追加新版本 → 这就是为什么数据血缘可追溯。

- 可回滚（Rollback）：  出错时可以回退到之前的版本，像代码一样切换分支。

- 多人协作（Collaboration）：  不同团队可以在不同分支上清洗/建模数据，最后再合并。

这保证了 Foundry 在大规模协作环境里有“数据的可重复性、可审计性”。

“Git for Data” 与代码 Git 的主要区别：

|     |     |     |
| --- | --- | --- |
| 特点 | 代码 Git | Foundry Git-for-Data |
| 存储对象 | 文本文件（几 KB ~ MB） | 数据集（GB ~ TB 级） |
| 变更方式 | 基于行的差异（diff/patch） | 基于数据块/分区的差异（block/partition delta） |
| 合并逻辑 | 按行合并冲突 | 按数据粒度合并（字段、分区、数据对象），更多自动化 |
| 索引方式 | 文件树 \+ commit | 数据集索引 \+ 时间/版本号 |
| 性能优化 | 面向小文件优化 | 面向大规模分布式存储优化（列存/对象存储 \+ 元数据索引） |

Foundry 不是逐行 diff，而是 **以“数据分块”的方式存储差异**，这在底层实现上更像是 **Delta Lake / Iceberg / Hudi** 这样的数据湖表格格式。

#### **22.3.14** 冗余数据问题怎么解决？

如果真的每次改动都复制整个 TB 级表，确实会爆炸。Foundry 采用了几种手段：

- 增量存储（Delta Storage）

  - 只保存变化的部分（新增/修改/删除的数据块），未变的数据块直接复用。

  - 类似于“写时复制（copy-on-write）”或“快照 + 日志（snapshot + log）”。

- 列存压缩（Columnar Storage + Compression）

  - 数据通常以列式存储，压缩率高；重复字段只存一次。

- 分区化（Partitioning）

  - 大表被切分为分区，改动只影响局部分区，而不是整表。

- 生命周期管理（Retention Policy）

  - 管理员可设定保留策略（如只保留近 6 个月的细粒度版本，老版本只保留关键快照）。

- 冷热分层存储（Hot/Cold Tiering）

  - 常用数据留在热存储（高性能）；老版本归档到冷存储（低成本）。

#### 22.3.15 针对 PB/TB 规模的计算优化

Palantir 在 Foundry 的数据层和计算层做了多层优化：

（1）分层/分级数据架构

冷/热分层：热数据（近期、核心特征）存放在高性能存储中，冷数据放在低成本存储（S3/HDFS）。

分级抽样：系统优先使用最新、关键的样本数据进行推理，必要时再调用全量数据做回溯。

（2）预计算与特征工程

大量分析逻辑在 数据管道中提前计算好特征，下游决策模块直接使用特征表，而不是每次重跑全量数据。

类似于 Materialized View（物化视图），减少重复计算。

（3）增量计算与流式处理

利用 Flink / Kafka / Delta Log 等流处理技术，对新数据进行增量更新，而不是全量重算。

决策层优先基于增量数据和历史缓存合并，保证时效性。

（4）分布式与并行计算

底层依赖 Spark/Flink + Apollo/K8s 调度，能在大规模集群上并行处理。

但会结合 成本优化策略，避免无限扩张算力。

（5）容错与回溯

如果快速决策后发现结果存在偏差，可以利用 Time Travel 回溯，在事后用全量数据重算，再校正或优化策略。

#### 22.3.16 **Palantir Foundry 与 Databricks、Snowflake ML、AWS SageMaker** 在算法与 ML 能力上的核心差异

- Foundry：算法能力 ≈ “够用 + 与业务语义深度融合”。它的独特价值不是“训练得多快”，而是“模型和业务应用怎么真正落地”。算法是 Ontology 的延伸。

- Databricks：算法能力 ≈ “科研级算力 + 湖仓一体”。核心卖点是 大规模训练和实验管理。

- Snowflake ML：算法能力 ≈ “轻量内置 ML”。降低 SQL/BI 用户门槛，但算法能力不算深。

- SageMaker：算法能力 ≈ “工业级 ML 工厂”。全面覆盖 训练-调优-部署-监控，最强的硬核 ML 工程能力。

Palantir Foundry 与 Databricks、Snowflake ML、AWS SageMaker的对标比较：

![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=129748&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9RZXlERDhoaWFibmh4U2Q4ZjBmRUpENlFyeXNpYTV0aWJMNkh3c3ZhU2hpY0c0bFBndFlPUjh4ZGFTQU9ydmNpY1dUUXpCaHRJNEZpYm14M0dhODFhdXlYWUhxUS82NDA/d3hfZm10PXBuZyZhbXA=;from=appmsg)

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| 维度 | Foundry | Databricks | Snowflake ML | SageMaker |
| 训练能力 | 支持外部训练产物接入，本地也可跑常见 Python ML，不是超大规模分布式训练平台 | 原生支持大规模 Spark/Flink 训练，MLflow 实验管理 | 内嵌 AutoML + 轻量模型训练，偏中小规模场景 | 大规模分布式训练、GPU/TPU 调度、自动超参优化 |
| 算法库 | 内置标准算子库（分类、预测、优化），可扩展；强调“与 Ontology 绑定” | 广泛支持开源库（TensorFlow/PyTorch/Scikit-Learn 等），高度自由 | Snowpark ML API，功能相对有限 | 深度支持 TensorFlow、PyTorch、Hugging Face 等框架 |
| 工作流编排 | 算法即节点，可组成 DAG，直接作用于业务对象 | Pipelines + MLflow 实验管理，面向数据科学团队 | SQL/Python 调用，简化工作流 | Step Functions + SageMaker Pipelines，面向 MLOps 工程师 |
| 模型部署 | 模型作为服务封装到 Foundry 内部，直接挂载到业务应用 | 部署到 Databricks Serving 或外部 API | 模型可转化为 SQL UDF/表函数 | 最完善的在线/批量推理服务 |
| 差异化 | 算法与 Ontology 强绑定：结果直接映射到“订单、车辆、库存”等对象 → 更偏应用集成 | 超大规模训练 & 数据湖原生 → 更偏数据科学研究与实验 | 仓库内轻量 ML → 更偏 SQL 用户与数据分析师 | 最强的 ML 工程平台 → 适合全栈 ML/AI 团队 |

[ai+saas](https://www.53ai.com/keyword/ai+saas) [ai saas产品](https://www.53ai.com/keyword/ai%20saas%E4%BA%A7%E5%93%81) [AI+SaaS系统](https://www.53ai.com/keyword/AI+SaaS%E7%B3%BB%E7%BB%9F)

分享：

用微信扫描二维码

用微信扫描二维码

用微信扫描二维码

用微信扫描二维码

53AI，企业落地大模型首选服务商

**产品**：场景落地咨询+大模型应用平台+行业解决方案

**承诺**：免费POC验证，效果达标后再合作。 **零风险落地应用大模型**，已交付160+中大型企业

[上一篇：喜力啤酒如何利用Palantir “快进” 供应链：从被动救火到预知未来](https://www.53ai.com/news/Palantir/2025121296031.html) [下一篇：从 Palantir 到世界大模型：记录、洞察与执行的重构之路](https://www.53ai.com/news/Palantir/2025121159031.html)

[返回列表](https://www.53ai.com/news/Palantir)

相关资讯

[2026-06-20\\
\\
FDE 术语表：30 个词看懂这个行业在说什么](https://www.53ai.com/news/Palantir/2026062029765.html) [2026-06-19\\
\\
决策系统的真正内核：本体模型](https://www.53ai.com/news/Palantir/2026061937529.html) [2026-06-16\\
\\
中国市场FDE是否有机会？](https://www.53ai.com/news/Palantir/2026061690672.html) [2026-06-11\\
\\
AI组织进化：为什么必须先补Palantir本体论这一课](https://www.53ai.com/news/Palantir/2026061116354.html) [2026-06-10\\
\\
硅谷今年最火的岗位 FDE，我们闷头干了三年](https://www.53ai.com/news/Palantir/2026061023150.html) [2026-06-10\\
\\
咨询与软件FDE转型：深度拆解Palantir生态卡位](https://www.53ai.com/news/Palantir/2026061007516.html) [2026-06-09\\
\\
现在流行的本体(Ontology)，是不是就是我们常说的语义层？](https://www.53ai.com/news/Palantir/2026060908627.html) [2026-06-07\\
\\
别把 Palantir 的“本体”做成知识图谱：企业数据架构的务实落地指南](https://www.53ai.com/news/Palantir/2026060746835.html)

[联系获取](https://www.53ai.com/solution.html)

[联系获取](https://www.53ai.com/solution.html)

160+中大型企业正在使用53AI

立即咨询预约演示

[把握AI发展的机遇，共同探索、共同进步\\
\\
2025-01-22](https://www.53ai.com/news/dongtai/2025012294502.html) [如何打造基于GenAI的员工服务机器人\\
\\
2025-01-22](https://www.53ai.com/news/dongtai/2025012234192.html)

[![banner](https://static.53ai.com/uploads/20250611/c637940d8902b253d3264aaf89cd40fc.jpg)](https://hub.53ai.com/)

热点资讯

[Palantir的中国门徒们，走到哪一步了？ \\
\\
2026-04-21](https://www.53ai.com/news/Palantir/2026042180293.html) [Palantir 技术思路与架构发展史：从情报图谱到决策操作系统 \\
\\
2026-04-22](https://www.53ai.com/news/Palantir/2026042265749.html) [FDE：AI时代的职业转型号角已吹响？ \\
\\
2026-05-26](https://www.53ai.com/news/Palantir/2026052650763.html) [当 DeepSeek 遇见 Ontology：企业智能决策的新范式正在出现 \\
\\
2026-05-11](https://www.53ai.com/news/Palantir/2026051197150.html) [硅谷今年最火的岗位 FDE，我们闷头干了三年 \\
\\
2026-06-10](https://www.53ai.com/news/Palantir/2026061023150.html) [吴恩达给正火的 FDE 泼冷水：押注它，不如押注 AI Engineer \\
\\
2026-06-03](https://www.53ai.com/news/Palantir/2026060317459.html) [别把 Palantir 的“本体”做成知识图谱：企业数据架构的务实落地指南 \\
\\
2026-06-07](https://www.53ai.com/news/Palantir/2026060746835.html) [Agentic Ontology：构建企业数字世界 \\
\\
2026-06-04](https://www.53ai.com/news/Palantir/2026060460327.html) [AI组织进化：为什么必须先补Palantir本体论这一课 \\
\\
2026-06-11](https://www.53ai.com/news/Palantir/2026061116354.html) [从PPT到FDE：这是一场咨询人的自我革命 \\
\\
2026-06-05](https://www.53ai.com/news/Palantir/2026060502965.html)

大家都在问

[中国市场FDE是否有机会？ \\
\\
2026-06-16](https://www.53ai.com/news/Palantir/2026061690672.html) [现在流行的本体(Ontology)，是不是就是我们常说的语义层？ \\
\\
2026-06-09](https://www.53ai.com/news/Palantir/2026060908627.html) [FDE：AI时代的职业转型号角已吹响？ \\
\\
2026-05-26](https://www.53ai.com/news/Palantir/2026052650763.html) [Palantir的中国门徒们，走到哪一步了？ \\
\\
2026-04-21](https://www.53ai.com/news/Palantir/2026042180293.html) [本体论思想-抽象建模的本质是什么？ \\
\\
2026-02-05](https://www.53ai.com/news/Palantir/2026020535127.html) [咨询 \| Palantir：我们不想做带着UI的埃森哲；一家咨询公司有望成为Palantir吗？优势和劣势分别在哪里？ \\
\\
2026-01-27](https://www.53ai.com/news/Palantir/2026012743157.html) [Palantir 哪些功能已经被标注为 Sunset（退场）和当前主推的功能是什么？ \\
\\
2026-01-19](https://www.53ai.com/news/Palantir/2026011980765.html) [【深度拆解】Palantir AIP智能体六件套：为何它是企业级Agent的终极形态？ \\
\\
2026-01-08](https://www.53ai.com/news/Palantir/2026010854981.html)

热门标签

[内容创作](https://www.53ai.com/news/neirongchuangzuo) [大模型技术](https://www.53ai.com/news/LargeLanguageModel) [个人提效](https://www.53ai.com/news/gerentixiao) [langchain](https://www.53ai.com/news/langchain) [llamaindex](https://www.53ai.com/news/llamaindex) [多模态技术](https://www.53ai.com/news/MultimodalLargeModel) [RAG技术](https://www.53ai.com/news/RAG) [智能客服](https://www.53ai.com/news/zhinengkefu) [知识图谱](https://www.53ai.com/news/knowledgegraph) [模型微调](https://www.53ai.com/news/finetuning) [RAGFlow](https://www.53ai.com/news/RAGFlow) [coze](https://www.53ai.com/news/coze) [Dify](https://www.53ai.com/news/dify) [Fastgpt](https://www.53ai.com/news/fastgpt) [Bisheng](https://www.53ai.com/news/Bisheng) [Qanything](https://www.53ai.com/news/Qanything) [AI+汽车](https://www.53ai.com/news/AIqiche) [AI+金融](https://www.53ai.com/news/AIjinrong) [AI+工业](https://www.53ai.com/news/AIgongye) [AI+培训](https://www.53ai.com/news/AIpeixun) [AI+SaaS](https://www.53ai.com/news/AISaaS) [Skill](https://www.53ai.com/news/tishicikuangjia) [提示词技巧](https://www.53ai.com/news/tishicijiqiao) [AI+电商](https://www.53ai.com/news/AIdianshang) [AI面试](https://www.53ai.com/news/AImianshi) [数字员工](https://www.53ai.com/news/shuziyuangong) [ChatBI](https://www.53ai.com/news/zhinengbaobiao) [AI知识库](https://www.53ai.com/news/zhishiguanli) [开源大模型](https://www.53ai.com/news/OpenSourceLLM) [智能营销](https://www.53ai.com/news/zhinengyingxiao) [智能硬件](https://www.53ai.com/news/zhinengyingjian) [FDE](https://www.53ai.com/news/zhinenghuagaizao) [AI+医疗](https://www.53ai.com/news/AIyiliao) [MaxKB](https://www.53ai.com/news/MaxKB) [Palantir](https://www.53ai.com/news/Palantir) [Glean](https://www.53ai.com/news/Glean) [Openclaw](https://www.53ai.com/news/Openclaw)

[应聘简历请发送至： ceo@53ai.com](mailto:ceo@53ai.com)

联系我们

售前咨询

[186 6662 7370](tel:18666627370)

预约演示

[185 8882 0121](tel:18588820121)

![](https://static.53ai.com/assets/static/images/loading.svg)

微信扫码

添加专属顾问

回到顶部

![](https://static.53ai.com/assets/static/images/loading.svg)

加载中...

扫码咨询

![](https://www.53ai.com/news/AISaaS/2025121217384.html)

![](https://www.53ai.com/news/AISaaS/2025121217384.html)

[预约演示](https://work.weixin.qq.com/ca/cawcde2599cf74e2d9) [微信咨询](https://work.weixin.qq.com/ca/cawcdefb661890e885) [电话咨询](tel:400-838-1185)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

安全验证

拖动下方拼图完成验证

![close](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

AI生成背景

![success](<Base64-Image-Removed>)

您的速度已超过 99% 的用户

验证错误,请重试

![load error](<Base64-Image-Removed>)

确定

![slider arrow](<Base64-Image-Removed>)![slider arrow](<Base64-Image-Removed>)![slider arrow](<Base64-Image-Removed>)

安全验证

刷新验证码

![refresh](<Base64-Image-Removed>)

反馈

![tip](<Base64-Image-Removed>)

切换无障碍验证

![Barrier-free verification](<Base64-Image-Removed>)

切换常规验证

![switch](<Base64-Image-Removed>)

### 来源 3: 万字解读Palantir产品、技术和架构讨论 - 53AI

- URL: https://www.53ai.com/news/Palantir/2025121217384.html
- 精读方法：firecrawl-scrape

- [首页](https://www.53ai.com/)
- 产品服务
- 客户案例
- FDE知识库
- 关于我们

热门场景

![](https://static.53ai.com/uploads/20240529/f87e241ff2dd3924718463507d38fcd1.png)

工作+AI

![](https://static.53ai.com/uploads/20240529/e3d1b654d90fe4a02dfda2b7bda13b74.png)

业务+AI

![](https://static.53ai.com/uploads/20240529/3294c40ae237a976140829e8c3e481c6.png)

AIx业务

[落地咨询](https://www.53ai.com/consulting.html)

[场景共创](https://www.53ai.com/fine-tuning.html)

热门产品

[![53AI Brain](https://static.53ai.com/uploads/20250429/f9ed1b6c2d16a688c5791a0057c2217d.png)\\
\\
53AI Brain \\
\\
让知识在人与AI之间高效流动](https://www.53ai.com/products/53AIBrain) [![53AI Studio](https://static.53ai.com/uploads/20250429/b2cd4330d03bce8eb0eb0332eb2954cd.png)\\
\\
53AI Studio \\
\\
高准确率的企业级智能体开发平台](https://www.53ai.com/products/53AIStudio) [![53AI Hub](https://static.53ai.com/uploads/20250429/94e6d990ee63512db567bc53c113e8bd.png)\\
\\
53AI Hub开源\\
\\
三分钟搭建出独立的企业AI门户](https://www.53ai.com/products/53AIHub) [![53AI Agents](https://static.53ai.com/uploads/20250429/05d03bb026421069826c64e2407ad7ee.png)\\
\\
53AI Agents \\
\\
“AI专家”效率倍增的武器](https://www.53ai.com/products/Agents)

[行业案例](https://www.53ai.com/kehuanli/hangyeanli) [场景案例](https://www.53ai.com/kehuanli/solution)

[前沿技术](https://www.53ai.com/news/qianyanjishu) [Agent框架](https://www.53ai.com/news/agentplatform) [行业应用](https://www.53ai.com/news/hangyeyingyong) [企业落地](https://www.53ai.com/news/qiyejingying)

[公司介绍](https://www.53ai.com/about/introduction) [渠道合作](https://www.53ai.com/about/cooperation)

![FDE知识库](https://static.53ai.com/uploads/20250210/aec076a60258b0cc07078c8ea7dff92c.webp)

FDE知识库

学习大模型的前沿技术与行业落地应用

立即咨询预约演示

[![](https://static.53ai.com/assets/static/images/tab1.png)首页](https://www.53ai.com/) [FDE知识库](https://www.53ai.com/news.html) [前沿技术](https://www.53ai.com/news/qianyanjishu) [Palantir](https://www.53ai.com/news/Palantir)

# 万字解读Palantir产品、技术和架构讨论

发布日期：2025-12-12 07:03:23浏览次数： 6491

作者：信息化与数字化

![](https://static.53ai.com/assets/static/images/detail-icon.png)

微信搜一搜，关注“信息化与数字化”

推荐语

深入剖析Palantir如何颠覆传统企业数据架构，揭秘其"数据即平台"的工程哲学。

核心内容：

1\. Palantir独特的"产品+咨询"混合模式与落地能力

2\. 数据作为一等公民的架构设计与传统ERP的根本差异

3\. 全局可视化系统如何实现战场级的业务决策支持

![](https://static.53ai.com/assets/static/images/avatar.jpg)

杨芳贤

53AI创始人/腾讯云(TVP)最具价值专家

之前也在一些技术交流群里分享过 PDF 版的《Palantir 产品和技术讨论》，但 PDF 的形态实在不太适合讨论。今天就换成文章的方式，把其中的一些思考拿出来分享，如果需要PDF版本的话，也可以线下联系。除了大家常聊的”泡沫“估值和“本体论哲学”，这次更想从工程和架构的角度，看看 Palantir 在技术上到底有哪些内容。全文2万余字，大家可以找自己感兴趣的模块看。![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=129748&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9RZXlERDhoaWFibmh4U2Q4ZjBmRUpENlFyeXNpYTV0aWJMNk9HMjZuU0J5WVZCekNxSENTajFhM2hQWE5YZVZjTFI4Z3VXWlJBWEo5U3RGM2ljQlNaWDhRTWcvNjQwP3d4X2ZtdD1wbmcmYW1w;from=appmsg)

## 第 22章：专题：Palantir产品和技术分析

![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=129748&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9RZXlERDhoaWFibmh4U2Q4ZjBmRUpENlFyeXNpYTV0aWJMNk1iTjJsVjdQZkVEQ2tXSWlhUWNHSktpYXBkTDF5ZXFiaWE3emliQU9HWHYwcXRkQjZGSW8zUlBXancvNjQwP3d4X2ZtdD1wbmcmYW1w;from=appmsg)

### 22.1 对Palantir 的观察观点：

- **落地能力的差异化**：

与各类战略咨询、业务公司或传统数据分析服务相比，Palantir 的突出特点在于更强的落地执行力；而与 Oracle、SAP、Snowflake 等以系统或工具为核心的企业软件公司相比，Palantir 不仅仅提供工具，而是从整体上提供一个全局化的数据分析与决策视角。Palantir 的模式介于“软件公司”和“咨询公司”之间，强调产品平台 + 咨询交付。这种“重交付”模式难以规模化，但形成了与 SaaS 厂商的差异化。

- **应用、数据的关系演变：**

在传统企业信息化中，ERP 等应用是核心，以流程为轴心，把业务固化为系统操作，数据只是随之沉淀的副产品，用于事后统计和审计，本质是“系统先于数据”，应用的边界决定了数据的形态。Palantir 则彻底反转：它把数据提升为一等公民，成为组织的“操作对象”和“统一语境”，而应用只是数据的投影与使用方式。Palantir 将数据构造成跨部门、跨系统的统一底层，应用则像插件挂载其上。这样企业不再依赖僵硬的应用堆叠，而能在同一数据语境下快速衍生业务能力，真正实现数据驱动的敏捷组织。

- **全局可视化：**

Palantir 将抽象的数据与真实业务场景深度结合，让用户获得类似“作战地图”的全局视角。指挥官可以像在沙盘上推演一样制定作战计划，供应链管理者则能如同观察神经网络般实时追踪订单、库存与运输节点的变化。数据不再只是后台的存量资源，而是成为直接驱动认知与行动的前台工具，大幅提升决策的透明度、速度与准确性。相比之下，传统 ERP 系统过于强调对现实业务流程的数字化映射，更多关注信息和数据处理本身，让用户去适应系统；而 Palantir 的设计理念始终围绕用户的全局观，帮助他们以直观方式理解复杂系统并快速行动。

- **语境化可视化**：

Palantir 的另一大价值在于彻底改变了数据的呈现方式。数据不再只是冰冷的表格字段，而是被转化为贴近真实世界的语境：地理全景图展示货物、人员或资产在空间上的实时流动；时间线将复杂事件的发展脉络清晰还原，让用户能够洞察因果链条；关系网络图揭示不同数据实体之间的依赖与作用，帮助发现潜在的风险点或协同机会。通过这种“语境化”的可视化方式，用户不再是孤立地解读数字，而是置身于一个动态的“业务剧场”，能直观感知数据背后的逻辑与趋势，从而在复杂环境中快速形成判断与行动。

- **数据驱动执行：**

Palantir 的核心价值在于将数据分析与决策执行深度耦合，并直接下沉到一线作业场景，而不仅停留在宏观战略层面。在军事领域，它能够让海外作战单元根据实时情报动态调整计划；在商业场景中，则能驱动供应链即时优化，例如让卡车在运输途中临时改派至缺货市场。这样的能力不仅让价值可以被量化与验证，还真正实现了“数据—决策—行动”的闭环。更重要的是，它能够同时赢得一线执行者的高度认可与高层决策者的信任，不仅提升了采购决策的合理性，也为商业合作创造了“价值共创”的模式——Palantir 可以通过帮助客户降本增效来进行成果分成，从而获得远超传统软件许可证的回报。

- **跨层级穿透**：

Palantir 能同时服务战略层、战术层和作业层，从总部的宏观分析，到前线的一线指令，全部基于同一个数据底座与语义体系。这种“全栈穿透”是传统 ERP、BI 难以做到的。相比之下，如果一个业务只能停留在洞察层面而无法驱动执行，其价值往往模糊、变现路径冗长，还需要跨越多个组织层级的审批与推动；而 Palantir 将“洞察”与“行动”打通，从根本上缩短了价值实现的链条。

- **人机协同**：

Palantir 的定位不是替代人，而是强化人机协同。机器负责提供推演、模拟与数据支撑，而最终决策仍由人类承担。这在军事、金融、能源等高风险领域尤为重要。

- **认知锁定：**

Palantir 擅长通过前瞻性的市场叙事（如 Ontology、Operating System for AI、Enterprise Digital Twin），在概念层面占据客户心智，完成认知锁定。一旦客户接受了这种高维度的框架，就很难再回到传统 BI 或 ERP 的思维方式。同时，这类叙事不仅能让资本市场给予更高估值，也能让客户对产品价值的认知大幅提升，从而降低销售成本，实现“认知驱动的市场渗透”。

- **Palantir 与** **知识图谱** **的抽象定位**

  -   Palantir 的底层能力可被视为数据领域的“动态知识图谱”：它将人、物、地点、事件等实体编织成因果与关系网络，形成统一语境，支撑查询、追溯与推理。这种图谱化范式相比传统 BI 更契合情报分析、风险管控、供应链可视化等多实体、多关系场景，尤其在事件溯源和模式发现上具备天然优势。

      不过，它也有边界：知识图谱长于关系建模，却不擅长数值优化（如调度、线性规划），需借助外部算法引擎；在应对实时高频数据流时，也必须依赖额外的流式计算框架。Palantir 的独特之处在于，结合与各类业务系统、数据系统的深度工程化对接，将知识图谱的洞察力与执行力贯通，真正让数据从“认知”走向“行动”。

- **Palantir 特殊经历塑造的技术护城河：**

          Palantir 的护城河与其早期客户类型密切相关。对传统企业而言，数据整合相对可控，只要权限到位，通常能较快完成跨部门打通；但 Palantir 从一开始就服务军队和情报机构，这些环境下的数据极度复杂：既包含庞大的外部实时交互数据，又因保密制度导致内部流通高度受限。在这种高难度挑战下，Palantir 被迫打造出一套完全不同于传统数仓、数据湖和 BI 的新型数据架构体系。

        这一体系的核心，是通过 Ontology 方法论 将业务实体与数据抽象映射起来，使其成为一个“数据操作系统”；并引入了类似 “Git for Data” 的版本化管理能力，支持 时间回溯（Time Travel） 等机制，让用户能够像代码一样追踪、回滚和重现数据全生命周期。这意味着 Palantir 的平台并非把数据处理作为应用的附属功能，而是把数据处理本身提升为一个面向全局的基础生产平台。

          正是在这种背景下，Palantir 不仅成功解决了高复杂度、高敏感度场景中的数据整合难题，也让这一架构具备了迁移到分散、松散数据环境的能力，从而形成独特且难以复制的竞争壁垒。

- **大模型** **时代** **Ontology** **与 AI 的双向融合**

       在 AI 时代，Ontology 与大模型的结合堪称“天生一对”，解决了数据与智能之间的双重难题：

  - **Ontology** **赋能** **大模型**：传统数据库存放的是庞杂的原始信息，量大且精度要求高，大模型难以直接处理。Ontology 能够把这些信息重组为语义化、结构化的知识网络，通过时间、关系、事件等维度压缩与语境化，从而为大模型提供高质量的上下文输入，避免冗余与噪声干扰。

  - **大模型** **加速** **Ontology**：过去 Ontology 的构建依赖专家梳理和人工建模，周期长、成本高。大模型的引入改变了这一过程——它能够基于已有数据快速生成 Ontology 的初始框架或模板，大幅提升知识图谱与指数级图谱的建立效率，让语义层的搭建从“工匠式”转变为“自动化+校准”的范式。

  - **形成智能闭环**：Ontology 提供“可操作的上下文”，大模型则通过理解和推理完成“从数据到行动”的转化。当两者结合，企业不仅能获得智能化的认知，还能推动实时决策与执行闭环，真正让 AI 成为业务系统的操作层，而不是附属分析工具。

    这种双向融合，让 Ontology 不再是静态的知识框架，而成为 AI 时代的动态语境引擎，也为企业级 AI 落地打开了全新的空间。

**Palantir 的重构：**

- 搭建一个类似Palantir 的MVP最少需要哪些组件？大概工作量是怎样的？

- 几乎每一个 Palantir 模块都能找到替代品，但这些替代品往往是单点产品，而 Palantir 的优势在于：

  - 高度集成 —— 地理信息、实时数据、建模、工作流、安全体系在一个平台内无缝协同。

  - 安全与权限体系 —— 军事、情报、政府场景造就了极高门槛。

  - 直达一线执行 —— 很多产品只能“看”，Palantir 能“推演+执行”。

下面这张图可能更好的帮助大家理解Palantir的技术组件有哪些类似的产品：![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=129748&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9RZXlERDhoaWFibmh4U2Q4ZjBmRUpENlFyeXNpYTV0aWJMNmdEQUpPbjZUV3Q4S0ZpYnZPV1F4c3VRRjh3UHZkbnVBVmFpYmRhd2NHM09hT1l1enhZOXpSbUlBLzY0MD93eF9mbXQ9cG5nJmFtcA==;from=appmsg)

|     |     |     |     |
| --- | --- | --- | --- |
| 功能模块 | Palantir 的特色 | 可能的替代品/类似产品 | 差异与门槛 |
| 地图与地理信息可视化 | 深度集成任务数据（战场态势 / 物流线路 / 基础设施），支持多源数据叠加 | Google Earth、ESRI ArcGIS、OpenStreetMap、CesiumJS | Palantir 能将异构数据（传感器、卫星、业务系统）实时叠加并用于决策，而非单纯地理展示 |
| 三维可视化 / 全景推演 | 类似沙盘演练，结合时序和地理空间进行动态模拟 | Cesium、Unity、Unreal Engine、Kepler.gl | 替代品多用于展示或开发，Palantir 强调“决策推演”，并结合权限、安全、实时数据 |
| 数据集成与建模 | 异构数据源快速接入（包括敏感系统、外部 API、实时传感器） | Talend、Informatica、Fivetran、Apache NiFi | Palantir 更关注安全环境和高度复杂的数据权限隔离 |
| 数据自动化工作流 | 工作流引擎驱动数据清洗、处理与触发业务操作 | N8N、Apache Airflow、Prefect | Palantir 强调“与业务执行挂钩”的工作流，而不是单纯 ETL |
| 知识图谱 / 关系建模 | 将人、物、地点、事件串联成图谱，辅助分析因果关系 | Neo4j、TigerGraph、Stardog，IBM I2 | Palantir 优势在于自动化构建、与安全权限体系深度结合 |
| 可视化分析与仪表盘 | 从战略到一线执行的多层级仪表盘 | Tableau、Power BI、Qlik | 传统 BI 偏向于报表，Palantir 注重“可操作的分析”，直接影响决策流 |
| 权限与安全体系 | 细粒度权限控制，支持跨部门、跨级别的共享与隔离 | Okta、SailPoint、Centrify | 在军事/情报级别的复杂安全需求下，Palantir 的设计难以被替代 |
| 实时决策与模拟推演 | 将模型结果直接反馈到一线（如战场部署、供应链调度） | AnyLogic、Simio（仿真工具）、OptaPlanner（约束优化） | 其他工具多停留在建模/模拟，Palantir 强调与现实执行场景直接挂钩 |
| AI/ML 模型集成 | 支持接入第三方模型，或在安全环境中运行 ML 推理 | DataRobot、SageMaker、H2O.ai | Palantir 的优势在于“把模型嵌入到组织的日常工作流中” |
| 协同与审计 | 让多部门基于同一数据环境协作，同时保证可追溯性 | Confluence、Jira、Slack + 数据平台 | 替代方案分散，Palantir 强调统一平台下的“协作 + 审计”能力 |

### 22.2 问题拆解

### 要了解一个大的体系，要从列问题开始。这里先不做解答，把一些跟产品和技术有关的问题先整理出来。

#### 22.2.1 产品与架构定位

- Foundry / Gotham 历来的技术架构演化是怎样的？

- Palantir 的产品定位是 **平台** 还是 **应用**？在客户体系中是取代传统 IT 系统，还是作为补充和“胶水层”？

- Foundry / Gotham 的 **核心技术抽象** 是什么？它是“数据模型”“知识图谱”还是“操作系统”层？

- 与传统 BI、ERP、Data Lake 有什么 **边界与差异**？

- 如果一家企业只用一个超大型 ERP（比如 SAP S/4HANA 或 Oracle Fusion），好像就可以把订单、库存、财务、采购、人力全都放在里面，并且做好抽象分层和解耦，是不是就不需要 Palantir Foundry 这样的产品了？

- 与 Data Lake / Lakehouse（Snowflake、Databricks）的关系是 **竞争** 还是 **上层封装**？

- 与 BI 工具（如 Tableau、PowerBI）的边界是什么？Foundry 提供的可视化是否会逐步侵蚀 BI 工具的角色？

- Palantir 的平台定位是否足够“可插拔”？客户能否只用数据治理或应用构建的子模块，而不是整个平台？

#### **22.2.2** **Ontology** **—— 从哲学到工程化**

- Palantir 为什么强调 Ontology 是 Foundry 的核心卖点？

- Ontology，怎样从抽象哲学到具体的工程落地？

  - Foundry 中的 Ontology 并不是抽象哲学，而是一个 业务实体与关系的统一建模层，它把“数据 → 业务语义 → 应用逻辑”连成一体

- Ontology 是否能直接作为 **应用构建的底层** **DSL**，让低代码/无代码开发更容易？

- Ontology 如何把底层异构数据（表格、日志、传感器流）映射为“订单、车辆、客户、任务”等业务对象？

- Ontology 是如何实现类似 **图数据库/** **知识图谱** 的实体关系，却又能与关系型、列式存储共存？

- 当业务逻辑变化时（比如供应链规则调整），Ontology 如何支持 **版本化演进** 而不破坏历史数据？

- Ontology 和传统的 Schema-on-Read / Schema-on-Write 的根本差异是什么？它解决了哪些痛点？

- 一个典型的跨系统的Ontology定义是什么？是否可以举一个例子么？

- Ontology 相当于“动态、语义化的主数据管理”吗？与 Informatica/Collibra 的差别在哪？

- Ontology 在工程上如何实现 **数据层、语义层、应用层** 的耦合？

- 业务实体的 Ontology 建模是自动生成（AI/规则）还是需要人工主导？

- Foundry 是否允许多套 Ontology 并存？如果允许，如何保证 **跨 Ontology 的互操作性**？

- Ontology 建模能否借助 **AI 自动生成/推荐**？例如自动识别“订单、车辆、用户”并形成初始本体？

* * *

#### 22.2.3 数据层设计

* * *

##### 22.2.3.1 数据接入与存储

- Palantir 如何处理 **异构数据源**？是否支持实时流式数据？

- 从 **数据引入 → 存储 → 使用 → 归档/销毁**，Foundry 是否有端到端的生命周期策略？如何保证历史数据在可追溯的同时不造成安全风险？

- 在大规模数据场景下，Foundry 的存储是否支持 **冷热分层、自动压缩、智能索引**，如何在性能与成本之间平衡？

- 除了关系型与时序数据，Foundry 如何管理 **文档、图像、视频、传感器流等非结构化数据**？是否有统一的索引与检索能力？

* * *

##### 22.2.3.2 数据建模与语义抽象

- Foundry 的 **Ontology（本体）** 是如何抽象的？与传统的 Schema-on-Read / Schema-on-Write 有何不同？

- Foundry 的 Ontology 与传统 \*\*数据目录/元数据管理（如 Collibra、DataHub）\*\*相比，有哪些增强功能？

- 除了传统血缘（Lineage），Foundry 是否支持 **跨多源数据的语义血缘**，从业务语义层追踪数据来历？

* * *

##### 22.2.3.3 数据治理与安全

- 在 Foundry 中，数据血缘、权限控制、审计如何做到 **细粒度**？能否支持 **多租户**？

- 针对机密数据（政府/军工），Palantir 如何实现 **多级安全隔离**？

- 与 Schema-on-Read、Schema-on-Write、Data Lakehouse 的治理模式相比，Foundry 的治理模式有哪些独特优势与局限？

- 在企业数据治理和业务决策中，为什么传统的 Schema-on-Write、Schema-on-Read、Lakehouse 模式不足以满足“ **可追溯、可重现、可合规**”的需求？

* * *

##### 22.2.3.4 协作与 Git for Data 范式

- Palantir Foundry 在数据协作层面是否支持类似 **‘Git for Data’** 的范式？

- “Git for Data”是语义层的（如订单、车辆、客户、任务），还是具体到某个数据表、数据集？

- 数据快照与版本对比的粒度到什么程度（表级、行级、字段级）？

- 在多人同时修改同一数据集时，Foundry 如何避免 **“最后写入覆盖”** 的冲突？

- 是否支持 **Pull Request / Review** 流程，让数据变更先经过审批或校验，再合入主版本？

- 如何在大规模分布式团队中同步数据更改（类似 Git 的分布式克隆/推送模型）？

- 有哪些开源体系（如 LakeFS、DVC），可以部分实现 Foundry 里的 ‘Git for Data’ 模式？

- 地图对象（如道路网络、地理多边形、时序轨迹）在“Git For Data”的模式下，如何优化性能和存储？

* * *

##### 22.2.3.5 时间回溯（Time Travel）

- Palantir Foundry 的 **Time Travel 功能** 带来了哪些独特价值？它在整体架构中扮演怎样的角色，并解决了传统数据平台难以覆盖的哪些痛点？

- Foundry 的 Time Travel 是基于 **全量快照、增量日志（delta log），还是混合模式**？不同选择对存储与检索性能有什么影响？

- 在 TB/PB 级数据规模下，Time Travel 如何实现？如何避免存储膨胀，同时保证历史版本查询的低延迟？

- 当一个关键业务指标在历史版本中被回溯时，Foundry 是否能提供 **全链路的可解释性**（数据来源 → 转换逻辑 → 模型版本 → 决策执行）？

- Time Travel 回溯仅仅是“只读”，还是支持 **沙箱演练**？能否在历史版本上运行新策略，做“假如当时”的模拟？

- Foundry 的地理空间（Geospatial）场景里，地图数据是否支持 Time Travel（时光回溯）？假设在一个战场中，道路被反复毁坏和修复的场景中，如果需要复盘历史上的一个战况。

* * *

##### 22.2.3.6 大规模数据与决策取舍

- 在 PB/TB 级数据场景中，Foundry 是否会因为数据读取或处理时间过长，而选择只用部分数据来支持分析与决策？如果会，系统如何保证这种取舍仍然能支撑“ **足够好**”的决策？

- Foundry 的设计哲学是追求每次都生成“ **最优解**”，还是强调“ **及时、可解释、可落地的足够好决策**”？在哪些场景下，时效性优先于最优性？

- 当使用部分数据做快速决策时，是否能事后通过 **Time Travel 回溯** 或全量重算来校正和优化？

- 在牺牲部分数据完整性的情况下，Foundry 如何保证决策 **可追溯、可审计**，并让客户信任？

* * *

#### 22.2.4 算法与分析引擎

- Palantir 的分析引擎，本质是 算法库、工作流引擎，还是 ML 平台？它的定位和边界是什么？

- Foundry 的算法层与 Ontology 如何耦合？是否能让算法直接 面向业务对象（订单、车辆、客户），而非原始数据表？

- Foundry 内部的数据计算，是基于 分布式引擎（Spark/Flink），还是自研引擎？在哪些环节使用开源，哪些地方深度改造？

- 与 Databricks、Snowflake ML、SageMaker 相比，Foundry 的算法能力 差异化优势体现在哪里？

- 内置算子、数据处理与 ML pipeline 分别依赖哪些语言？（Python、R、SQL、Scala …）它们在平台中的 角色、优势与局限 各是什么？

- Foundry 如何管理 Python 等依赖的 版本升级与兼容性，避免“依赖地狱”？

- 算法是否被抽象为 可组合算子（Operators），支持 DAG 式的流程编排，类似 Spark/Flink？

- 在大规模推理或函数调用下，如何进行 算子级与代码级性能优化？

- 算法与业务场景如何结合？平台如何封装 决策优化、仿真与可视化推演？

- 算法结果是否能直接通过 Ontology 映射为 可视化对象（如车辆调度方案、库存水平），而不仅是抽象指标？

- 在多目标优化（成本、时效、风险）中，Foundry 如何展示 权衡空间（Pareto Frontier），让用户选择不同解？

- 是否提供交互式工具来探索 “解空间”，而不仅仅返回单点解？

- OR-Tools 等优化器如何与 业务对象与流程打通，形成闭环的资源分配与调度？

- 同一用例中，批处理、准实时、交互式分析如何统一调度，避免“为实时牺牲精度”的困境？

- 批处理、流处理与交互式查询如何在 Foundry 内部平衡？是否有一个统一抽象整合不同计算引擎？

- 在实时决策场景（应急调度）中，如何取舍 近似解与最优解？是否提供策略可配置？

- 针对大规模运筹优化（调度、网络优化），Foundry 倾向使用 启发式算法，还是数学规划/商业求解器？

- 在机器学习与 AI 方面，Foundry 是更偏向 AutoML、模型管理，还是聚焦于 数据管道与应用封装？

- Foundry 是否提供 ML/AI SDK，让用户在外部训练模型后无缝接入？

- 对于 TensorFlow / PyTorch / Hugging Face 等生态，Foundry 是否支持 一键部署与集成？

- Foundry 能否承担企业级的 MLOps 平台角色，还是更强调 算法与业务应用的深度耦合？

- Foundry 如何保证算法的 可解释性？是否能将输入、输出、关键变量与中间步骤完整暴露给业务用户？

- 当模型失效或数据漂移时，Foundry 如何触发 自动切换到规则系统或回滚机制？

- 算法层是否提供 监控视图，实时展示数据漂移、模型失效、优化收敛情况？

- 算法层是否支持 假设分析（What-if Analysis），并能在 Ontology 上模拟不同输入条件？

- 假设分析的 性能挑战 如何解决？是否支持近似计算或缓存优化？

- Foundry 的 What-if / Scenario Analysis 与 数字孪生（Digital Twin） 结合时，会遇到哪些工程挑战？

- 在复杂系统（供应链、能源网络、金融市场）中，Foundry 如何支持 多主体建模与博弈论分析？

* * *

#### 22.2.5 应用与场景封装

##### 22.2.5.1 行业模块与复用性

- Palantir 的行业模块是 **通用模板（如供应链、金融、能源）** 还是 **客户定制**？如何平衡“可复用”与“差异化”？

- Palantir 的行业解决方案，是以 **通用模板 \+ 定制化扩展** 的方式交付，还是为核心行业（国防、能源）内置了 **全链路场景封装**？

- Palantir 如何抽象 **跨行业共性的工作流**（如订单履约、调度、风险监控），同时保留行业特有差异？

- Palantir 如何保证 **跨租户复用**？一个行业模板能否被不同客户快速复用？

- 不同行业模块是否包含 **完整功能栈**（业务 KPI、预设算法、可视化组件、地图组件），还是仅仅是 **数据模型骨架**？

- 不同行业，组件配置差异如何体现？其 **定价方式** 是按行业套件、按模块，还是按使用量？

* * *

##### 22.2.5.2 场景化功能封装

- Palantir 是否会在场景封装时，把 **“业务角色 → 数据对象 → 应用界面”** 的映射直接做好？

- Foundry 是否提供类似 **“行业 App Store”** 的模式，让客户快速启用现成的应用？

- 类似 **“地图模块”** 在不同场景下的功能差异：

  - **军事**：卫星态势、战场推演

  - **能源**：管线网络监测

  - **供应链**：仓储选址、线路规划

- 同一个模块在不同行业里是 **裁剪版** 还是 **增强版**？

- Gotham 在安全/反恐场景下，具体的 **工作流与分析能力** 是如何封装的？

- Foundry 在供应链、金融等企业场景中，是否能形成 **行业级标准化模块**，还是必须 **高度定制**？

* * *

##### 22.2.5.3 低代码 / 无代码能力

- Palantir 的 低代码/无代码能力 在实际客户落地中扮演什么角色？面向的是 业务用户 还是 数据科学家？

- Palantir 的低代码 DSL 是否完全内嵌在 Ontology 层，还是允许 用户自定义扩展？

- 无代码应用是否支持 复杂业务逻辑编排，还是仅限于 轻量可视化与交互？

- 无代码组件能否与 Ontology 对象直接绑定（如“订单拖拽 → 自动生成调度分析”）？

- 在客户真实落地中，低代码的 局限性 主要表现在哪些方面？是否会导致 性能瓶颈或灵活性不足？

- 性能上，低代码生成的查询是否等价于专家手写 SQL/Python，还是存在优化差距？

- Palantir 是否允许企业将 自研 UI/组件 与其无代码框架集成？

- 当业务逻辑复杂超出 DSL 表达能力时，低代码与全代码如何无缝切换？

* * *

##### 22.2.5.4 SDK 与生态

- Palantir 是否提供 标准化 SDK / API（Python、Java、REST、GraphQL …），让开发者能把 Foundry 功能嵌入外部系统？

- SDK 的使用门槛与授权模式如何？是 开放生态，还是仅对 付费客户/战略合作伙伴开放？

- SDK的使用是否有收费门槛？

- SDK的主要版本的生命周期是怎样？

- SDK 的覆盖范围到哪一层？是仅限 数据读写，还是涵盖 数据管道编排、权限、模型部署、应用 UI 组件？

* * *

##### 22.2.5.5 定制化与长期演进

- 应用的 定制化开发 是否会导致 “二次开发陷阱”，增加平台长期的维护成本？

- Foundry 如何解决 二次开发的版本依赖和技术债务问题？

- 自动生成的 SQL/Python 代码是否 可追溯并版本化（类似 “Git for Low-code”）？

- 低代码工件是否能“一键转化”为 可编辑的 Python/SQL，实现 低代码与全代码的无缝切换？

- 当 DSL 与代码混用时，Foundry 如何 优化执行计划，避免性能损耗？

- 是否可以把 DSL 与 Python/R 的算子机制统一成 同一 AST 或中间表示，实现 低代码与全代码的同构？

- Palantir 是否探索过通过 LLVM 或 WASM，将 DSL 统一编译到多语言后端（Python、Go、Rust、C++），实现“一套语义，多种运行时”？

#### 22.2.6 系统集成与执行控制

- 系统定位：Palantir 在系统集成层的定位到底是什么？是替代传统中间件/ESB/BPM，还是更专注于“决策中枢 + 调度”的上层编排？若 Foundry 过度下沉到执行层，会否与 SAP/Oracle 的事务边界与控制权产生冲突？

- 与 iPaaS 的关系：Foundry 与现有 iPaaS（MuleSoft、Boomi、Informatica）在客户架构中是竞争还是互补？典型部署中是“Foundry 统一编排 + iPaaS 做连接”，还是相互替换？

- 数据桥接与安全：接入 SAP/Oracle 等核心系统时，Foundry 采用何种“官方/合规”的接入机制？例如 SAP 认证 Add-On 或标准 API 方式。这类“应用层级”的连接如何平衡实时性与对源系统的影响？

- SAP 连接拓扑与模式选择：连接 SAP 时有哪些推荐的架构模式？在不同网络分段/隔离场景下如何落地？

- 批/流一体与 HyperAuto：当需要从 SAP 持续同步时，是否采用流式同步（如基于 SLT），若没有流式条件时如何用“文件/镜像/预过滤抽取”的方式折中？对数据新鲜度与作业可靠性有何影响？

- 写回与一致性模型：业务操作需要回写第三方系统时，首选通过 Ontology Actions 实现（也可经 OSDK 或 API Gateway）。跨系统写回的“事务性”如何保证？是否建立幂等键、重试与补偿策略的标准化？

- 调用与权限边界：Foundry 下发指令时如何避免“超权限”调用？采用 API Key、Service Account 还是零信任的细粒度授权？不同方式对审计、轮换、最小权限落地的影响是什么？

- 跨系统一致性：当 AI 决策串联多个系统（如“库存调拨 → 订单结算 → 财务入账”）时，Foundry 是否内置分布式事务，或推荐 Saga/补偿模式？多步作业的失败域与回滚链路如何建模？

- 不友好系统接入策略：对接口不佳或老旧系统如何接？（直连表、文件/日志批量导入、RPA、定制适配器）的选择准则与风控边界是什么？在何种条件下建议采用影子模式而非直接下发？

- SDK 与标准化集成：是否提供标准 SDK/适配包加速对接主流系统（SAP/Oracle 等），以及统一的“适配层”以降低长尾系统集成成本？

- 速率控制与回压：当 Foundry 对第三方 API 高并发写回时，如何实施限流、熔断、排队与回压，避免拖垮源系统？这些策略与任务编排/重试/补偿如何协同？

- 灰度与沙箱：如何避免“一次性大规模下发”的系统性风险？是否具备从“沙箱推演 → 小流量灰度 → 全量执行”的发布策略？若第三方系统没有沙箱能力，如何以“规则模拟/只读校验”实现等价的安全演练？

- 容器化与可移植性：在本地数据中心或隔离网络中，Foundry 的集成与执行组件是否支持容器化/代理化部署？连接器版本、证书轮换、密钥管理与集中运维如何落地？

- 连接器与源类型版图：除 SAP/Oracle 等业务系统，Foundry 在对象存储、文件系统、JDBC/数据仓库等“数据平面”的连接版图与限制是什么？如何界定 Foundry 与 iPaaS 的边界？

#### 22.2.7 平台工程与架构演进

- Foundry/Gotham的架构是 单体演进 → 微服务 → 容器化 → 云原生，还是直接基于云原生？是否支持 混合云/多云部署？在客户本地数据中心部署时的难点在哪？

- 在业务前线（如海外军事任务）场景下，当敏感数据无法出境时，Foundry/Gotham 是否支持 边缘节点（Edge Node）部署？边缘节点与主节点在 功能覆盖、权限范围、数据处理能力 上如何划分？

- 在弱网或离线环境下，边缘节点能否保持自治运行与决策能力，并在网络恢复后实现与主节点的安全同步？在遇到威胁时候，边缘节点是否可以启用自动销毁的程序？

- 微服务与容器编排：平台是否全面容器化并采用服务网格？跨数百微服务的版本一致性、兼容矩阵、配置漂移如何治理？

- 架构演化与分层：Foundry/Gotham 的“控制平面 vs 数据平面”如何划分？哪些能力在控制平面统一，哪些必须贴近数据/业务落在数据平面？这种分层对发布、扩容、容灾有何影响？

- 发布火车与灰度策略：在多租户、多环境（SaaS、私有云、本地、边缘）下如何实现分批发布、金丝雀、回滚与特性开关的矩阵管理？发布失败域如何最小化？

- 断网/空隔与边缘：在隔离网络、间歇连通或边缘设备上，例如国防军工领域的客户无法实时联网，软件如何脱线接收补丁、验证签名、分段推进并保证状态一致？跨网域的“制品与元数据”搬运如何可控与可追踪？

- 多云与工作负载放置：平台如何做策略驱动的调度（成本、延迟、数据驻留、合规、GPU/CPU 资源）？跨云跨区的数据重力与计算迁移如何权衡？

- 多租户隔离：在“存储、计算、网络、日志、遥测、缓存”各层的隔离边界是什么？如何防止租户间噪声干扰并在共享集群中提供可预期的 SLO？

- 资源与成本工程：是否有统一的成本/容量治理（配额、自动扩缩容、抢占/Spot、冷热层、缓存）？针对大模型/GPU 作业，如何做混部、切片、抢占、批处理窗口的策略优化？

- 数据驻留与地域策略：多国/多地区法规要求下，元数据、日志、模型参数、向量索引等是否都能“就地”驻留？跨区协同时采用联邦/代理/最小可共享哪种模式？

- 技术栈与开源依赖：平台主要采用哪些开源组件（如 Kubernetes、Kafka、Spark/Flink、Arrow、Iceberg、Ray 等）？哪些部分是自研（如 Ontology、Action 引擎、治理/审计框架）？对开源的 **依赖深度** 与 **二次开发程度** 如何？是否存在 **替换/迁移路径**？在技术路线的选择上，是“通用开源 → 平台整合”还是“自研为核心 → 兼容开源”？

- 兼容性与可演化性：平台内Ontology、管道引擎、算子、SDK的版本如何共存？是否支持双写/影子运行以平滑升级复杂依赖？

- 观测与运营闭环：统一的日志、指标、链路追踪如何覆盖“数据 → 算法 → Action 调用 → 外部系统回执”的全链路？SLO/SLA 违约如何自动触发回滚/限流/降级？

- 备份与容灾：RPO/RTO 目标下，跨区多活、冷热备、对象存储快照如何组合？Time Travel 与传统备份/灾备如何分工，避免把回溯误当灾备？

- 工程供给效率：开发者如何获得“一键可复现环境”（模板化 Stack、样板管道、测试数据沙箱、Mock 外部系统）？是否支持预览环境与“变更即验证”的内环路？

- 配置与密钥管理：大规模环境的配置漂移如何检测与收敛？密钥/证书/令牌的轮换、分发、撤销如何自动化且可审计？

- 制品与供应链：平台是否产出可追溯制品（SBOM、签名、来源证明）并在部署端做策略校验？如何在断网环境中仍保持软件供应链的可信？

- 统一 SDK 与“适配层”：对主流系统（SAP/Oracle/数据湖/消息总线）是否提供版本化的标准适配包？长尾系统如何通过低代码适配层接入且在平台升级时不被“拉断”？

- 容量与队列调度：在批处理/流处理/交互式混合负载下，如何做统一排队与优先级，保证在线体验不被批作业“顶爆”？

- AIP 融合下的基础设施升级：引入 LLM/向量检索/代理编排后，平台如何演进GPU 调度、模型缓存、并发限流、提示与上下文缓存？这些能力是平台内建还是托管于外部推理服务？

- 审计与可解释：平台是否能把“谁用什么数据，触发何决策，经由哪些 Action，在哪些系统落地”完整沉淀为可检索的审计图谱？

- 审计粒度与最小解释单元：一次执行的“可解释性”最低需要包含哪些要素（输入快照、版本、规则/模型、外部响应、补偿链）才能满足复盘与合规要求？

- 环境模板与规模复制：是否存在行业/场景级环境蓝图（网络、权限、接入、监控、数据模型的最低集）以周级复制一个新环境？复制过程中的可变参数与不可变基线如何定义？

- 技术债务与退场机制：如何管理跨版本长期兼容带来的技术债？当客户选择退场或迁移时，平台是否提供一键导出/解耦路径避免“不可逆锁定”？

#### 22.2.8 与传统 IT/大厂、市场潜在竞争对手的比较

- 技术边界：Palantir AIP/Foundry 自称“把 AI 与数据与运营打通”，而 Databricks/Snowflake 更偏数据与模型工作负载、SAP/Oracle 更偏应用内嵌 AI。Palantir 的“从数据直达执行”与其他平台“从数据到洞察/从应用到自动化”在职责边界上究竟差在哪里？（能否跨系统下发 Action、是否仅在单一应用内建议/自动化）。

- 语义层 vs 业务模块：Palantir 的 Ontology 强调“把数据、模型、对象、动作”映射到统一的业务语义层；而 SAP/Oracle 的模块化 ERP 以流程/事务边界来组织数据。二者是数据驱动应用 vs 应用驱动数据的根本差异吗？在跨域场景（供应链 + 维护 + 财务）里，哪种语义组织更稳健？

- “企业级 AI 操作系统”的含金量：Palantir 所谓 OS for Enterprise AI 比 Lakehouse AI（Databricks）、Cortex（Snowflake）和 AI ERP（SAP Joule、Dynamics Copilot、Oracle Fusion AI）多出了哪些“能执行”的基础件（如统一动作模型、跨系统编排、可回滚）？又缺哪些“底层”能力（如湖仓原生算子/数据库原语/大规模训练设施）？

- 数据与治理栈对齐：与 Databricks（Unity Catalog/治理）和 Snowflake（原生治理 + Cortex）相比，Palantir 的数据治理、血缘、权限与可解释性覆盖到“动作/执行层”了吗？是否能把“谁在何时用何数据触发何决策并在何系统落地”闭环到同一治理面板？

- 模型路由与嵌入方式：Snowflake Cortex、Databricks Lakehouse AI、SAP Joule、Dynamics Copilot、Oracle Fusion AI 都宣称“内嵌/原生 AI”。Palantir 的多模型路由、BYOM 与业务对象/动作绑定相比之下更强还是更弱？在跨域任务里（如“从告警到工单到备件采购”），谁的端到端更顺滑？

- 执行半径：Palantir 强调“把建议变成执行”。而 SAP/Oracle/微软多在各自应用域内落地自动化；Snowflake/Databricks多停留在数据域。谁更擅长跨系统的可控执行（有无统一 Action/回滚/幂等/审批机制）？失败域如何隔离？

- 行业沉淀 vs 平台中立：Palantir 在国防、能源、制造的行业工作流与语义沉淀，和 SAP/Oracle 的纵深行业 Best Practices、微软/Dynamics 的角色工作台，哪种复用性/迁移性更强？跨行业落地的摩擦系数如何量化（时间、人员、变更成本）？

- 生态策略：SAP/Oracle/微软拥有成熟的 ISV + 实施伙伴生态；Databricks/Snowflake有大量数据/AI 生态。Palantir 是走应用商店/行业模块市场，还是主要靠自交付 + 合作伙伴？生态对规模化复制与客户锁定的影响是什么？

- 锁定机制的差异：传统厂商通过核心流程/主数据/许可实现锁定；数据云通过数据重力/治理体系实现锁定；Palantir 是否通过 Ontology + 应用/动作层形成“语义锁定”？这种锁定对客户是正外部性（减少集成成本）还是负外部性（迁移困难）？

- 云原生与多租隔离：与三大公有云原生 AI/数据平台相比，Palantir 在弹性扩展、资源隔离、多租户治理上是否存在短板或优势？其政府/隔离环境部署与“企业公有云”形态的差异如何影响 TCO 与交付速度？

- 端到端 AI 体验的取舍：Oracle/Fusion、SAP/Joule、Dynamics/Copilot把 AI 嵌入业务流程的“就地体验”很强，但跨系统联动有限；数据云的“数据侧一体化”很强，但“执行侧”薄。Palantir 若走“跨系统 OS”，在体验深度 vs 范围广度上如何选型？

- 成本结构与可持续性：数据云强调计算分离、按需弹性；应用云强调流程价值；Palantir 若承担编排 + 语义 + 执行三层，单位用例的端到端成本是否可控？与“各域原生 AI”（Joule、Copilot、Fusion AI）相比的长期运维负担如何？

- 竞争—协作关系演化：Palantir 会被定义为“上层编排/应用平台”叠加在数据云/应用云之上，还是会与 Lakehouse/数据云、AI ERP 发生直接替代竞争？在客户主架构中如何划清边界以避免“平台内卷”？

- 针对大型企业的落地路径：若客户已深度采用 SAP/Oracle + Snowflake/Databricks + Microsoft Copilot，Palantir 的最小可行切入点是什么（如先做语义层与跨系统编排）？替换路径与共存路径各自的迁移风险与收益模型如何设计？

- “行业云 vs 跨行业基座”的取舍：Palantir 会不会也走“行业云”（国防云、能源云、制造云）来获得复制效率，还是坚持“跨行业基座 + 行业模板”的路径？哪种更利于生态扩展与产品化？

- Palantir目前的产品形态下， 选择与 AWS、Azure、Google Cloud、Oracle 等合作，而不是直接替代，它在生态中的独特定位是什么？其规模增长到什么程度，就可能会跟这些生态链上下游产生竞争？

#### 22.2.9 商业模式与客户价值

- Palantir 的收入模式：订阅制、项目制、还是混合？如何平衡“规模化可复制”与“深度交付”？如何避免被客户视为高级一点的“外包团队”，而是定位为长期战略伙伴？

- Palantir 如何将抽象的“AI驱动决策”量化为客户的 ROI（节约成本、降低风险、提升收入）？

- Palantir 自己在衡量一个客户价值时，ROI 的衡量周期是短期（季度/年度）还是长期（3-5 年）？

- 在客户 ROI 上，它如何证明自己比传统 IT 或咨询更具性价比？

- Palantir 在 **生态合作** 上的策略：是封闭（自研全栈）还是开放（对接 AWS、Azure、GCP、第三方 ML 工具）？

- Palantir 的客户一旦迁移到 Foundry/Gotham，其退出成本体现在哪些层面？（数据模型、工作流、治理体系）

- Palantir 这种“深度绑定”是否会引发客户对锁定风险的担忧？客户被绑架的代价是多大？有没有替代品？

- 在金融、供应链、政府安全等不同行业中，Palantir 的商业模式有何差异？

- 是按照“用户数 / 节点数 / 数据量”收费，还是以“价值分享”方式收费？在不同的阶段是怎样的收费模式？“价值分享”在商业合同上具体怎样设计？

- 当客户在某些场景（如供应链优化节约几亿美元）看到效果后，Palantir 会按 收益比例 或 规模扩展费用 来收取更高的合同金额。但是降本增效总有到极限的一天，如果到时候没有更多的优化空间，Palantir 的“价值分享”收益来自于哪里？是否存在业务上的天花板？

- Palantir 的护城河究竟是：

  - 技术（Ontology、低代码 DSL、封装）

  - 行业 know-how（深耕国防/能源/供应链）

  - 深度交付（强咨询 \+ 长期绑定）  三者哪个才是 不可替代 的？

* * *

#### 22.2.10 Palantir  AIP，AI专题

##### 22.2.10.1 战略定位与生态角色

- Palantir 在 AI 时代的定位：是继续做 数据驱动的企业操作系统，还是转型为 AI 驱动的企业操作系统？

- 在 AI Agent 崛起的背景下，Palantir 会成为 AI Agent 的承载操作系统，还是会被新一代 Agent 平台取代？

- AIP 的战略定位是 Foundry/Gotham 的 AI 插件，还是一个 独立的 AI 原生平台？

- AIP与 Copilot Studio / LangChain Hub， AWS Bedrock / Azure OpenAI，这些的区别？

- AIP 与 OpenAI、Anthropic、Mistral 等 LLM 平台相比，核心差异在哪里？是“行业封装 + 合规治理”，还是在算力、算法层直接竞争？

- AI 时代是否会改变 Palantir 的商业模式？（订阅制 vs AI SaaS + Agent 平台）

##### 22.2.10.2 技术架构与大模型融合

- Palantir 的大模型定位：是作为 嵌入式工具（辅助提升可用性），还是 底层操作引擎（直接驱动 Foundry 工作流）？

- AIP 是否具备 多模型路由能力（根据任务自动选择 GPT、Claude、Mistral、本地模型）？

- 客户能否 部署自有大模型 并与 AIP 无缝对接？调用时的数据是否有外泄风险？

- 在调用 LLM 时，AIP 如何解决企业数据的 语义鸿沟？是否具备自动 Prompt 生成与 Ontology 映射机制？

- AIP 是否采用 短期会话上下文 + 长期知识记忆 的分层架构？是否结合 Vector DB + Ontology Cache？

- 是否区分 自然语言推理（LLM） 与 数值计算/规则引擎，避免 LLM 在金融/国防场景中做错误计算？

##### 22.2.10.3 Ontology 与行业专家壁垒

- Palantir 过去依赖行业专家手工构建 Ontology，这是其壁垒之一。AI 时代是否降低了这道壁垒？

- 大模型能否自动生成行业 Ontology（如供应链、金融风控、国防），并长期维护？

- 如果大模型可以直接从数据库 Schema 和业务日志生成“半自动 Ontology”，Palantir 的行业专家护城河还成立吗？

- Ontology 的价值在于“ **动态演化**”，Palantir 是否能建立 **AI + 人机共建** 的 Ontology 演进体系？

- 如果行业 Ontology 可以被 AI 快速生成，Palantir 如何在 **深度绑定客户业务逻辑** 上保持护城河？

- 大模型调用 Ontology 时，是 **一次性全量挂载**，还是 **按需懒加载 \+ 会话缓存**？

- 是否存在一个全局的 “Ontology-aware System Prompt”，统一指导模型如何解释对象与字段？

- Ontology 是否可以作为训练客户私有模型的数据资产？Palantir 是否提供这种能力？

##### 22.2.10.4 工程化，AI Agent 化与工作流重构

- Ontology 作为记忆层：Palantir 的 Ontology 把业务对象和数据关系建模在一起，它是否天然适合作为 AI Agent 的长期记忆与状态存储？如何处理“会话态 + 持久态”的边界？

- Ontology 的颗粒度：一个 Ontology 需要多大颗粒度、多少层关系，才能既让 AI 灵活调用，又不至于触发 Token 爆炸和性能瓶颈？

- Action 抽象与事务语义：在 Palantir AIP 中，AI 通过 Action 执行业务或系统操作。Action 的最佳抽象层级是“业务级操作”还是“底层系统调用”？是否需要事务特性（前置/后置条件、幂等键、补偿钩子）来保证可靠性？

- 反馈闭环：Agent 在执行 Action 后，如何把结果反馈到 Ontology？Palantir 是否内置了“自我纠错”或“再训练”机制？

- LLM 与 Functions 的分工：Palantir 坚持把数值计算、约束校验放在 Functions，而不是交给大模型。这是否说明在关键行业中，大模型只能做编排，无法替代传统求解器？

- 混合推理与算力分配：AIP 如何在大模型推理（LLM）与传统优化器/仿真器之间做算力分配？在一个决策链路中，哪些环节适合概率推理，哪些必须交给确定性算法？是否有调度器自动做“任务切片”和“算力路由”？

- 推理层路由与模型选择：AIP 是否支持根据任务复杂度与实时性需求，动态选择“小模型处理高频请求，大模型处理复杂问题”？调度策略如何实现？

- 不确定性处理：当 LLM 输出带有概率性时，AIP 如何与传统确定性计算融合？是否存在多路候选计划、再由优化器选优的机制？

- 实时性与流式场景：在高频决策（金融交易、供应链调度）场景下，AIP 如何保证 LLM 推理的延迟不会拖垮整体工作流？

- 上下文缓存与会话态：AIP 是否支持 Context Cache / Session State，避免在长会话或多 Agent 协作中重复加载大规模上下文？

- 流式响应与渐进式结果：在需要人机交互或长链路推理时，AIP 是否支持流式输出中间结果，让用户在等待最终决策前就能获取阶段性反馈？

- Copilot 的查询方式：AIP Copilot 生成查询结果时，是通过 SQL/GraphQL 显式调用 Ontology，还是通过语义向量检索？不同方式在可解释性与性能上差异怎样？

- 跨系统编排能力：AIP Copilot 是否支持跨系统编排（ERP、SCM、IoT、GIS），还是主要局限在 Foundry 内部？

- 插件化生态：AIP 是否支持 “Bring Your Own Tool (BYOTool)” 与 “Bring Your Own Model (BYOM)”，让客户自由集成自有系统与模型？

- Agent 框架的策略：Palantir 会发展自己的 Agent 框架/DSL，还是更多对接 LangChain、AutoGen、Copilot Studio 等第三方生态？

- 行业模块的演变：传统 Foundry 行业模块（地图、KPI、工作流）未来是否会演变为可直接调用的“Agent 角色库”？

- 多 Agent 协作：Palantir 是否支持多个 Agent 基于统一 Ontology 协作？如何避免任务冲突、循环调用或资源死锁？

- 推理链的透明度：AI Agent 在调用 Ontology + Action 时，是否会自动生成可追溯的“推理链路”，帮助用户理解为什么做出某个决策？

- UI 与低代码封装：AIP Copilot 是否能生成可直接运行的 UI（报表、地图、仪表盘），还是只负责数据调用？这对非技术用户的上手有多大帮助？

- 迭代与可演化性：Ontology、Action、Functions 的设计是否支持迭代演化？在 AI Agent 持续学习的情况下，如何避免模型与数据结构“脱节”？

- 自我进化：Ontology与Agent之间是否可以实现相互的自我进化？

##### 22.2.10.5 安全、权限与责任边界

- 最小权限控制：在 AIP 中，Agent 调用 Action 时如何保证最小权限？是否存在类似 RBAC/ABAC 的自动收敛机制？

- 高风险指令的边界：当 Agent 获得执行权（如航班调度、资金调配、军事命令），Palantir 如何设定权限与责任分界？

- 权限体系继承：AIP Copilot 的权限模型是否完全延续 Foundry 的细粒度控制？

- 权限粒度可扩展性：Palantir 的权限可达“对象-属性-操作”级别，在 AI 驱动自动化场景下，这种粒度是否会爆炸式膨胀，最终难以维护？

- 风险拦截机制：是否存在 Policy Engine / 审批环节，用来阻止危险的 AI 指令落地？

- 可追溯性保障：如何确保 AI 输出具备可追溯、可验证、可解释特性？

- 黑箱风险与新护城河：LLM 的概率黑箱属性，是否反而让 Palantir 的合规、审计与安全治理成为新的差异化壁垒？

- 可解释性的最小单元：一次 Action 的解释是仅记录“模型调用日志”，还是包含“业务语义解释 + 数据溯源”？

##### 22.2.10.6 成本与商业模式

- AI Native 的 Palantir 是否会因大规模模型调用增加客户成本？

- Palantir 是否会发展 **轻量推理框架（Distilled Agent / 小模型）** 来降低成本？

- AIP 的定价模式是基于 **调用次数、算力消耗**，还是基于 **场景/用户打包**？如何避免与 LLM API 厂商产生“双重计费”？

- 是否提供 **AI 成本透明化仪表盘**，让客户实时监控 AI 使用成本？

##### 22.2.10.7 未来演进与竞争格局

- 如果未来的 AI 平台天然具备 **数据处理与集成能力**，Palantir 的独特价值还在哪里？

- LLM 的概率模型本质（非逻辑引擎）和上下文窗口限制，是否反而让 Palantir 的 **Ontology 与长期记忆** 成为优势？

- 如果出现 **可解释性更强的 AI**，Palantir 的数据治理价值会被稀释吗？

* * *

### 22.3 参考资料：

### Palantir 并非大模型浪潮下才出现的新玩家，而是经历过多轮业务与架构迭代的老公司。先把这段演化史补齐，才能从那些情绪化的吹捧与质疑中抽身出来，比较冷静地判断它的真实价值。

#### **22.3.1 Palantir Gotham** 架构演化

**初期架构（2008–2014）**

- 部署模式：Gotham 诞生于情报/政府场景（CIA、FBI 等），一开始就是高度封闭、本地化部署的单体/模块化架构。

- 技术栈：大量使用 Java/Scala + 大规模关系数据库（Oracle、Postgres），再配合 Palantir 自研的“数据整合层”和“知识图谱层”。

- 特征：强调 数据集成与图谱搜索，把异构数据源统一到一个 Ontology，再提供高可视化的情报分析工作台。

- 局限：扩展性不足，依赖人工定制 ETL 与工作流，难以快速适配新业务场景，也无法高效跨多客户/多租户交付。

**中期演进（2014–2017）**

- Palantir 面对政府与企业客户同时扩张，开始意识到 Gotham 的 **交付与升级成本过高**。

- 当时的 Gotham 架构逐渐拆分出 **服务化组件**，如数据接入、治理、权限、可视化，但整体仍然是 **较重的应用交付**，而非云原生。

- Palantir 工程团队在内部尝试容器化，但真正的转折点是在 2017 年 **Rubix 项目**：该项目用 Kubernetes 重构了 Palantir 的云基础设施。

**向 Foundry 云原生过渡（2017 之后）**

- Gotham 的很多底层能力（数据建模、图谱、权限体系）被抽象出来，逐渐融入 **Foundry** 的统一平台。

- 随着 **Apollo** 成熟，Palantir 能够在多云环境快速迭代产品，Gotham 也逐渐被“再平台化”为 **Foundry 上的一个垂直应用**（面向政府/情报安全）。

- 今天 Gotham 在架构上不再是独立的单体，今天 Gotham 实际上是 **运行在 Foundry 栈上的一个垂直应用**（Government Vertical），而 Foundry 是底层通用操作系统。

#### **22.3.2 Palantir** 主要的技术特色：

1. **Ontology（业务本体层建模）**

- 把跨系统的数据抽象成业务对象（订单、卡车、患者、任务）与关系。

- 语义层直接面向业务人员，而不是表/字段。

- 核心卖点：让跨系统、跨组织的数据治理与决策更直观、更可协作。

* * *

2. **Git for Data（数据版本化与 Time Travel）**

- 每个数据集、对象、关系、工作流都有不可变版本。

- 支持时光回溯、回滚、分支与合并（类似 Git 但面向数据）。

- 核心价值：可追溯、可重现、可审计。

* * *

3. **细粒度安全与合规体系**

- 行级、列级、对象级权限控制，跨部门/跨组织共享时依然可控。

- 内置审计日志，符合 GDPR、HIPAA、CCPA 等合规要求。

- 核心卖点：高安全环境（军工/政府）到商业场景都能通用。

* * *

4. **数据血缘与语义血缘（Lineage & Semantic Lineage）**

- 不仅能追溯表字段来源，还能追溯业务对象的语义来历。

- 例如：“这个库存数来自哪些仓库传感器 → 哪些订单 → 哪些系统”。

- 核心价值：增强可解释性，支撑风控、合规、审计。

* * *

5. **跨系统数据集成能力**

- 支持结构化（ERP、DB）、非结构化（PDF、图像）、实时流（IoT、Kafka）。

- 提供标准连接器、SDK、自定义适配器，甚至支持 RPA 抓取。

- 核心价值：能在“接口不友好”的环境中，依然打通多源异构数据。

* * *

6. **工作流与 Saga 式补偿机制**

- 支持跨系统编排（Orchestration），自动化数据流和决策执行。

- 通过 Saga 模式实现最终一致性（补偿事务、幂等、重试、死信队列）。

- 核心价值：让数据流不仅能“看”，还能“驱动执行”。

* * *

7. **沙箱与灰度执行机制**

- 支持沙箱演练（基于历史数据回放）、小范围灰度执行、全量推广。

- 可以在 Ontology 对象上模拟业务策略（如改派订单），避免大规模混乱。

- 核心价值：保证高风险环境（军队、供应链）中的安全落地。

* * *

8. **可视化与全局推演能力**

- 内置全景地图、时间轴、关系图谱。

- 不仅是 BI 报表，而是“业务沙盘”，支持作战指挥/供应链调度/应急演练。

- 核心价值：让复杂数据直接对应现实世界，直观驱动决策。

* * *

9. **开放生态与模型集成**

- 支持外部 AI/ML 框架（TensorFlow、PyTorch）、第三方模型（DataRobot、SageMaker）。

- 模型运行在 Foundry 语义层之上，直接作用于业务对象。

- 核心价值：不是替代 AI 平台，而是让 AI 真正进入业务流程。

* * *

10. **全链路协作与审计闭环**

- 开发者、数据科学家、分析师、业务人员可以在同一 Ontology 层协作。

- 每一步操作（数据更新、模型执行、报表生成）都有审计记录。

- 核心价值：在高度复杂的组织环境里，保证 **透明、可控、可信**。

#### **22.3.3 跨系统的Ontology 的例子：**

跨系统的“订单（Order）” Ontology 定义

业务对象（Entities）

01. Order（订单）

    1. 来自 ERP 系统（SAP/Oracle）：订单号、客户 ID、产品、数量、价格、状态。

03. Shipment（运输批次）

    1. 来自 TMS 系统：承运商、卡车/司机、起点、终点、预计到达时间。

05. Inventory（库存）

    1. 来自 WMS 系统：仓库位置、可用库存、批次号。

07. Sensor（传感器数据）

    1. 来自 IoT 系统：温度、湿度、GPS、卡车位置。

09. Customer（客户）

    1. 来自 CRM：客户信息、信用等级、合同条款。

* * *

关系（Relationships）

- Order → Shipment：一个订单可以被分配到多个运输批次（部分发货）。

- Order → Inventory：订单关联仓库库存，用于判断是否可发货。

- Shipment → Sensor：运输批次与卡车 IoT 数据绑定，用于实时监控。

- Order → Customer：订单与客户绑定，支持信用风险控制。

* * *

版本化 & Time Travel

- 订单状态从 _创建 → 已发货 → 在途 → 签收 → 退货_，每个变化在 Ontology 里都有版本号。

- 可以回溯“订单 12345 在 2024/07/01 时，绑定的是哪个仓库、哪个司机、哪辆车”。

* * *

Ontology 带来的统一视图

在传统系统里：

- ERP 只知道订单和合同；

- WMS 只知道库存和出库；

- TMS 只知道卡车和路线；

- IoT 只知道传感器信号。

在 Foundry 的 Ontology 里：  👉 “订单”成为一个统一的业务对象，跨系统的数据都挂载到这个对象上，这样业务人员和决策者不用去查 4 个系统，就能直接看到订单的全景。

#### **22.3.4** Foundry的主要技术栈：

**前端（用户界面层）**

Foundry 的前端本质是一个 **Web 平台**，用户通过浏览器访问，主要技术方向包括：

- **框架与语言**

  - **TypeScript + React** → Foundry 的主要 UI 框架，用于构建工作台、仪表盘、低代码应用界面。

  - **GraphQL / REST** → 与后端的数据查询和交互。

- **可视化与地图**

  - **WebGL** → 浏览器端渲染引擎。

  - **MapboxGL** → 地图与 3D 场景渲染（Foundry 的 Map/Contour 模块基于此）。

  - **D3.js / Highcharts** → 常规 BI 可视化组件。

- **交互体验**

  - 浏览器端低代码工具（App Builder、Workshop），封装了 React + 内部 DSL（领域专用语言）。

  - 多人协作机制类似 Google Docs，前端需支持实时同步与权限控制。

* * *

**后端（应用逻辑与计算层）**

Foundry 的后端是一个 **云原生 \+ 分布式计算** 架构，核心技术栈包括：

- **运行与调度**

  - **Kubernetes** → 统一容器编排平台。

  - **Apollo** → Palantir 自研的持续交付与多云部署系统，确保 Foundry 能在 AWS、Azure、GCP 或本地数据中心一致运行。

- **数据存储与处理**

  - **分布式存储**：对象存储（S3 兼容）、列式存储（Parquet、ORC）

  - **关系数据库**：Postgres、Oracle 等，用于事务型与元数据管理。

  - **分布式计算引擎**：Apache **Spark**（批处理/机器学习）， **Flink**（流处理场景）。

  - **Graph 数据存储**：内部有知识图谱/本体管理，早期 Gotham 用过 Titan/Neo4j 等，Foundry 更可能采用自研或基于分布式 KV。

- **数据治理与权限**

  - 内置 RBAC/ABAC 模型，支持行/列/单元格级别权限。

  - 血缘追踪和审计日志存储，通常用 **Kafka + ElasticSearch** 或自研管道。

* * *

**AI / 数据科学集成**

- **工作台（Code Workbooks）**：

  - 支持 **Python、R、SQL**，直接运行在 Spark 集群或容器沙箱里。

  - 集成 scikit-learn、TensorFlow、PyTorch 等常见库。

- **模型管理**：

  - 内置 MLOps 模块，支持版本控制、实验追踪、模型部署。

  - 与外部 MLflow、SageMaker 有一定程度对接能力。

* * *

**DevOps 与运维**

- **CI/CD**：Apollo + Git 集成。

- **监控**：Prometheus、Grafana、Elastic Stack 结合内部工具。

- **安全合规**：Kubernetes 原生安全策略 + Palantir 自研隔离机制，满足政府/军工客户的多级保密要求。

* * *

**总结**

- **前端**：TypeScript/React + WebGL/MapboxGL + GraphQL

- **后端**：Kubernetes + Apollo + Spark/Flink + 分布式存储（S3/Parquet）+ 强权限治理

- **AI 层**：Python/R/SQL 工作台 + MLOps

- **核心差异点**：不是某个单一技术，而是 **数据本体（Ontology）+ 安全权限体系 + Apollo 多云交付**，这三者形成了 Palantir 的独特技术护城河。

#### **22.3.5** Foundry与传统的MDM的主要差异：

|     |     |     |
| --- | --- | --- |
| 维度 | 传统 MDM（Informatica / Collibra） | Palantir Foundry Ontology |
| 定位 | 数据治理工具（管好 Golden Record、标准化主数据） | 业务语义层 \+ 应用开发基座（建模、可视化、工作流） |
| 数据形态 | 以 表/字段 为核心（Customer 表，Product 表） | 以 对象/关系/动作 为核心（Customer→下单→Order） |
| 集成模式 | ETL/ESB，先抽取清洗再写回 MDM | Schema-on-Read，Ontology 映射到源数据，避免复制 |
| 使用人群 | 数据治理/IT 部门（负责全局主数据） | 一线业务/开发（在 Ontology 上直接构建应用） |
| 更新节奏 | 主数据版本更新较慢（季度/年度） | 动态、可实时更新（支持 Time Travel 和差异对比） |
| 产出 | 干净的数据资产 | 可直接驱动应用的业务模型、图谱、工作流、权限 |
| 扩展性 | 偏治理、目录化 | 内置 DSL，低代码/无代码开发，直接跑应用 |

#### **22.3.6** Foundry 的权限控制体系：

Foundry 的权限体系分为几个粒度：

- **源数据层**：传统的行/列/表权限（类似数据库 ACL）。

- **Ontology 层**：以业务对象为中心（例如 `Order`、`Customer`、`Warehouse`）。

- **属性级别**：某些敏感字段（例如客户身份证号） → “可见/不可见/脱敏”。

- **实例级别（Row-level Security）**：例如“销售 A 只能看到自己负责区域的订单”，通过 Ontology 映射规则实现。

- **操作级别**：不仅是“看”，还能限制“能不能触发某个动作”，例如：

  - 可以查看订单状态

  - 但不能触发“取消订单” 或 “重新分配库存”的操作

**技术实现方式：**

- **Policy-as-Code**：Foundry 提供策略引擎，权限规则可以写成可配置的策略（JSON/YAML/DSL），而不是硬编码。

- **语义绑定**：权限不是绑定在表字段，而是绑定在 Ontology 对象 → 比如“Order.totalAmount 只有经理能看”。

- **动态评估**：规则执行时可以基于上下文，比如 `user.role = manager` 且 `region = APAC` 时放开访问。

- **遮罩/变形**：不是只有“能看/不能看”，还支持“能看但脱敏”，如显示 `****1234` 的银行卡号。

**为什么 Ontology 层的权限更强？**

在 ERP 或数据库里，权限通常是：“这个表谁能看”，“这个字段谁能看”。

但 Foundry Ontology 的权限模型是：

- “谁能看 **订单** 这个对象”

- “能看订单里的哪些属性（如金额、客户地址）”

- “能对订单对象执行哪些动作（取消、修改、审批）”

- “这些权限在不同上下文是否变化（只限自己部门）”

这样权限和 **业务语义** 紧密对齐，而不是死板的表结构。

|     |     |     |
| --- | --- | --- |
| 维度 | 传统数据库 / ERP 权限 | Foundry Ontology 权限 |
| 控制对象 | 表、字段（Column-level Security） | 业务对象（Order、Customer、Asset）、属性（字段）、实例（单条记录）、操作（动作） |
| 粒度 | \- 表级（Table ACL） - 字段级（Column ACL） | \- 对象级（Object-level） - 属性级（Attribute-level） - 实例级（Row-level, Region-level） - 操作级（Action-level） |
| 业务语义 | 权限绑定在表结构上，语义弱 | 权限绑定在 Ontology 对象及关系上，直接映射业务逻辑 |
| 上下文动态性 | 固定规则（谁能看哪个表/字段） | 动态策略：基于用户角色、部门、地域、上下文条件（Policy-as-Code） |
| 操作权限 | 通常只有 CRUD（增删改查） | 可定义“业务动作权限”，如 cancelOrder、approvePayment、rerouteTruck |
| 数据遮罩 | 部分支持（如脱敏视图） | 内置多级遮罩：完全隐藏、部分脱敏（\*\*\*\*1234）、汇总级展示 |
| 跨系统一致性 | 难以统一，不同系统各自实现 | 统一在 Foundry Ontology 层做语义权限管理，跨系统执行一致 |
| 审计能力 | 日志较粗粒度（谁访问了表/字段） | 精细审计：谁在什么上下文下访问了哪个对象的哪个属性、执行了什么操作 |
| 价值定位 | 偏技术安全控制 | 语义安全 / 业务安全控制，更贴近真实世界权限需求 |

#### **22.3.7** Foundry 的前端使用方式

**Web 界面为核心**

    Foundry 提供一整套 **基于浏览器的工作台（Workspaces）**，用户直接通过浏览器访问。

    核心模块包括：

-  Ontology（数据本体建模）：定义业务实体与关系。

-  Data Lineage / Pipeline Studio：拖拽式数据管道编排。

-  Code Workbooks：数据科学家可以直接写 Python、R、SQL，调用 Spark / ML 库。

-  Visualization / Dashboards：BI 风格可视化，内嵌在 Foundry 界面中。

-   App Builder / Workshop：低代码构建行业应用。

**角色驱动的界面**

- 业务人员：通过 Dashboard、Workshop（类似 Power BI / Tableau + 低代码表单）。

- 数据工程师：通过 Pipeline Studio 和 Dataset 浏览器。

- 数据科学家/分析师：通过 Code Workbooks 或与外部 IDE（Jupyter、VSCode）集成。

Foundry 的 3D 地图性能：浏览器端体验

- Palantir Foundry 并没有单独的桌面客户端，它的 2D/3D 地图完全依赖浏览器端的 WebGL 来渲染。对用户来说，打开方式很简单，但这也常常引出一个担心： **只靠浏览器，会不会卡？**

其实能否流畅，取决于几个关键点：

- **硬件加速**：如果浏览器没有开启 GPU 加速，或者显卡驱动不支持 WebGL，那么加载 3D 场景一定会卡顿。这个问题在一些虚拟机或企业锁定环境里尤其常见。

- **数据规模**：地图并不怕“3D”，怕的是“一次性加载太多”。矢量要素过密、点云数据没做抽稀，或者 3D 模型没有分级细节（LOD），都会让前端直接崩溃。

- **网络与传输**：3D 地图的瓦片、纹理和模型体积都很大，如果网络带宽差，表现上就会是卡顿和延迟。

Foundry 的做法是：

- 在浏览器端用 WebGL 进行渲染，但在后端提前做好“切片、抽稀、聚合”，前端拿到的已经是可视化友好的结果。

- 对大数据场景提供分层加载，比如业务人员看到的是简化版的图层，只有在工程师或分析人员需要时，才会加载完整的三维细节。

- 如果前端设备实在跑不动，还有传统的轻量回退模式可以用。

总结一下：Foundry 的 3D 地图性能瓶颈不是“浏览器”，而是 GPU 配置、数据处理和网络环境。在正确的架构下，即便是普通办公电脑，也能流畅跑相当复杂的三维场景。

#### **22.3.8** 将Palantir 的能力抽象为数据模型（Data Model / Ontology）

- **定位**：Palantir 强调“语义层 + 本体（Ontology）”，即用统一的数据模型描述业务世界。一个工厂里的“卡车”“仓库”“订单”“人员”都能抽象成数据对象，并建立关系。

- **扩展能力**：

  - 可以快速复用到不同场景（军事、能源、金融），只需换一套行业语义层。

  - 新数据源接入后，只要映射到统一模型，就能立即参与分析和决策。

- **限制**：

  - 高度依赖 **建模能力和行业理解**，不同客户的语义差异大，实施成本高。

  - 在一些高度动态、非结构化的数据环境（例如社交媒体、非标准 IoT）下，建模难度陡增。

#### **22.3.9** 将Palantir 的能力抽象为知识图谱（Knowledge Graph）

- **定位**：很多人认为 Palantir 的底层更接近知识图谱：把人、物、地点、事件串联起来，形成“因果/关系网络”，支持查询与推理。

- **扩展能力**：

  - 非常适合 **情报分析、风险控制、供应链可视化** 等需要多实体、多关系的场景。

  - 天然支持“事件追溯、可视化、推理”，利于发现隐藏模式。

- **限制**：

  - 图谱模型擅长“关系”，但在 **数值型优化**（如线性规划、调度优化）上能力不足，需要外接算法引擎。

  - 知识图谱本身难以处理 **实时高频数据流**（如传感器毫秒级信号），必须依赖额外的流式计算框架。

#### **22.3.10 抽象为操作系统内核（OS Kernel for Data & Decisions）**

- 定位：Palantir 自己喜欢用“操作系统”来描述——它像是组织的数据内核，外接各种“设备驱动”（业务系统、数据库、API），然后在统一环境里运行“应用”（决策工作流、分析模块）。

- 扩展能力：

  - 具备极强的横向扩展性：理论上任何系统、任何数据都能接入，只要写好“驱动”。

  - 可以形成完整的生态体系（就像操作系统之上跑应用），合作伙伴和客户可以自己开发应用。

- 限制：

  - 复杂度高：操作系统式的抽象需要庞大的权限管理、进程调度、安全体系，这也是 Palantir 实施成本昂贵的原因。

  - 易受锁定效应约束：既然是“OS 内核”，客户一旦上了 Palantir，迁移成本极高，但这同时意味着 Palantir 难以被“轻量化”采用。

#### **22.3.11** Foundry 的端到端数据生命周期管理

① 数据引入（Ingestion）

- Foundry 支持多源数据接入（数据库、API、IoT 流、文件），并在入口就进行权限控制与日志记录。

- 每条数据的来源、时间戳、转换规则都会被自动记录（即所谓的 _lineage_ 数据血缘）。

- 引入时可以配置 合规策略（如 GDPR、HIPAA），对敏感字段自动脱敏或加密。

② 存储（Storage & Modeling）

- 底层可连接客户已有的存储（Snowflake、S3、HDFS 等），Foundry 作为逻辑层而非“霸占数据”。

- 数据存储采用多层抽象：原始层（Raw）、清洗层（Refined）、语义层（Ontology）。

- 每层数据都带有 版本控制（类似 Git for Data），保证修改可回溯。

③ 使用（Usage & Execution）

- 数据被用来驱动分析、可视化、建模和工作流。

- Foundry 提供细粒度权限控制（行级、列级、对象级），确保不同角色只能看到该看到的。

- 所有查询、修改、导出行为都会自动审计，便于事后追溯。

- 历史版本的数据可随时“时光倒流”，保证分析结果的可验证性。

④ 归档/销毁（Archival & Deletion）

- Foundry 支持根据\*\*数据保留策略（Retention Policy）\*\*对过期数据进行归档或彻底删除。

- 归档的数据可转入低成本存储（冷存储/离线仓库），并与权限体系绑定。

- 合规销毁机制：敏感数据在达到合规年限后可强制删除，同时保留“元数据审计记录”，确保历史可追溯但内容已清除。

#### **22.3.12** 如何在“可追溯”与“安全风险”之间平衡

- 可追溯性依赖的是 _元数据和血缘信息_，而不是保留所有原始数据。Foundry 通过“记录操作日志 + 保留数据版本号”，实现溯源。

- 安全性依赖的是 _细粒度权限 \+ 动态加密_：即使数据存在历史版本，也未必能被访问，除非用户权限允许。

- 合规性：Foundry 内置对 GDPR、CCPA、HIPAA 等合规框架的支持，可以自动触发数据过期删除，同时保留“销毁记录”，做到“证明已删”。

- 最小暴露原则：审计和追溯只对谁做了什么操作进行保留，而不一定保留敏感数据本身。

#### **22.3.13** Foundry 的“Git for Data” 与代码 Git 的相似点，以及区别

- 版本化（Versioning）：  每次数据变更都会生成一个版本号，任何分析、建模都基于“某个具体版本”，保证可重现性。

- 不可变快照（Immutable Snapshot）：  历史版本不可修改，只能追加新版本 → 这就是为什么数据血缘可追溯。

- 可回滚（Rollback）：  出错时可以回退到之前的版本，像代码一样切换分支。

- 多人协作（Collaboration）：  不同团队可以在不同分支上清洗/建模数据，最后再合并。

这保证了 Foundry 在大规模协作环境里有“数据的可重复性、可审计性”。

“Git for Data” 与代码 Git 的主要区别：

|     |     |     |
| --- | --- | --- |
| 特点 | 代码 Git | Foundry Git-for-Data |
| 存储对象 | 文本文件（几 KB ~ MB） | 数据集（GB ~ TB 级） |
| 变更方式 | 基于行的差异（diff/patch） | 基于数据块/分区的差异（block/partition delta） |
| 合并逻辑 | 按行合并冲突 | 按数据粒度合并（字段、分区、数据对象），更多自动化 |
| 索引方式 | 文件树 \+ commit | 数据集索引 \+ 时间/版本号 |
| 性能优化 | 面向小文件优化 | 面向大规模分布式存储优化（列存/对象存储 \+ 元数据索引） |

Foundry 不是逐行 diff，而是 **以“数据分块”的方式存储差异**，这在底层实现上更像是 **Delta Lake / Iceberg / Hudi** 这样的数据湖表格格式。

#### **22.3.14** 冗余数据问题怎么解决？

如果真的每次改动都复制整个 TB 级表，确实会爆炸。Foundry 采用了几种手段：

- 增量存储（Delta Storage）

  - 只保存变化的部分（新增/修改/删除的数据块），未变的数据块直接复用。

  - 类似于“写时复制（copy-on-write）”或“快照 + 日志（snapshot + log）”。

- 列存压缩（Columnar Storage + Compression）

  - 数据通常以列式存储，压缩率高；重复字段只存一次。

- 分区化（Partitioning）

  - 大表被切分为分区，改动只影响局部分区，而不是整表。

- 生命周期管理（Retention Policy）

  - 管理员可设定保留策略（如只保留近 6 个月的细粒度版本，老版本只保留关键快照）。

- 冷热分层存储（Hot/Cold Tiering）

  - 常用数据留在热存储（高性能）；老版本归档到冷存储（低成本）。

#### 22.3.15 针对 PB/TB 规模的计算优化

Palantir 在 Foundry 的数据层和计算层做了多层优化：

（1）分层/分级数据架构

冷/热分层：热数据（近期、核心特征）存放在高性能存储中，冷数据放在低成本存储（S3/HDFS）。

分级抽样：系统优先使用最新、关键的样本数据进行推理，必要时再调用全量数据做回溯。

（2）预计算与特征工程

大量分析逻辑在 数据管道中提前计算好特征，下游决策模块直接使用特征表，而不是每次重跑全量数据。

类似于 Materialized View（物化视图），减少重复计算。

（3）增量计算与流式处理

利用 Flink / Kafka / Delta Log 等流处理技术，对新数据进行增量更新，而不是全量重算。

决策层优先基于增量数据和历史缓存合并，保证时效性。

（4）分布式与并行计算

底层依赖 Spark/Flink + Apollo/K8s 调度，能在大规模集群上并行处理。

但会结合 成本优化策略，避免无限扩张算力。

（5）容错与回溯

如果快速决策后发现结果存在偏差，可以利用 Time Travel 回溯，在事后用全量数据重算，再校正或优化策略。

#### 22.3.16 **Palantir Foundry 与 Databricks、Snowflake ML、AWS SageMaker** 在算法与 ML 能力上的核心差异

- Foundry：算法能力 ≈ “够用 + 与业务语义深度融合”。它的独特价值不是“训练得多快”，而是“模型和业务应用怎么真正落地”。算法是 Ontology 的延伸。

- Databricks：算法能力 ≈ “科研级算力 + 湖仓一体”。核心卖点是 大规模训练和实验管理。

- Snowflake ML：算法能力 ≈ “轻量内置 ML”。降低 SQL/BI 用户门槛，但算法能力不算深。

- SageMaker：算法能力 ≈ “工业级 ML 工厂”。全面覆盖 训练-调优-部署-监控，最强的硬核 ML 工程能力。

Palantir Foundry 与 Databricks、Snowflake ML、AWS SageMaker的对标比较：

![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=129748&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL3N6X21tYml6X3BuZy9RZXlERDhoaWFibmh4U2Q4ZjBmRUpENlFyeXNpYTV0aWJMNkh3c3ZhU2hpY0c0bFBndFlPUjh4ZGFTQU9ydmNpY1dUUXpCaHRJNEZpYm14M0dhODFhdXlYWUhxUS82NDA/d3hfZm10PXBuZyZhbXA=;from=appmsg)

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| 维度 | Foundry | Databricks | Snowflake ML | SageMaker |
| 训练能力 | 支持外部训练产物接入，本地也可跑常见 Python ML，不是超大规模分布式训练平台 | 原生支持大规模 Spark/Flink 训练，MLflow 实验管理 | 内嵌 AutoML + 轻量模型训练，偏中小规模场景 | 大规模分布式训练、GPU/TPU 调度、自动超参优化 |
| 算法库 | 内置标准算子库（分类、预测、优化），可扩展；强调“与 Ontology 绑定” | 广泛支持开源库（TensorFlow/PyTorch/Scikit-Learn 等），高度自由 | Snowpark ML API，功能相对有限 | 深度支持 TensorFlow、PyTorch、Hugging Face 等框架 |
| 工作流编排 | 算法即节点，可组成 DAG，直接作用于业务对象 | Pipelines + MLflow 实验管理，面向数据科学团队 | SQL/Python 调用，简化工作流 | Step Functions + SageMaker Pipelines，面向 MLOps 工程师 |
| 模型部署 | 模型作为服务封装到 Foundry 内部，直接挂载到业务应用 | 部署到 Databricks Serving 或外部 API | 模型可转化为 SQL UDF/表函数 | 最完善的在线/批量推理服务 |
| 差异化 | 算法与 Ontology 强绑定：结果直接映射到“订单、车辆、库存”等对象 → 更偏应用集成 | 超大规模训练 & 数据湖原生 → 更偏数据科学研究与实验 | 仓库内轻量 ML → 更偏 SQL 用户与数据分析师 | 最强的 ML 工程平台 → 适合全栈 ML/AI 团队 |

[ai+saas](https://www.53ai.com/keyword/ai+saas) [ai saas产品](https://www.53ai.com/keyword/ai%20saas%E4%BA%A7%E5%93%81) [AI+SaaS系统](https://www.53ai.com/keyword/AI+SaaS%E7%B3%BB%E7%BB%9F)

分享：

![](https://static.53ai.com/assets/static/images/share_icon_1.png)

用微信扫描二维码

![](https://static.53ai.com/assets/static/images/share_icon_2.png)

用微信扫描二维码

![](https://static.53ai.com/assets/static/images/share_icon_3.png)

用微信扫描二维码

![](https://static.53ai.com/assets/static/images/share_icon_4.png)

用微信扫描二维码

53AI，企业落地大模型首选服务商

**产品**：场景落地咨询+大模型应用平台+行业解决方案

**承诺**：免费POC验证，效果达标后再合作。 **零风险落地应用大模型**，已交付160+中大型企业

[上一篇：喜力啤酒如何利用Palantir “快进” 供应链：从被动救火到预知未来](https://www.53ai.com/news/Palantir/2025121296031.html) [下一篇：从 Palantir 到世界大模型：记录、洞察与执行的重构之路](https://www.53ai.com/news/Palantir/2025121159031.html)

[返回列表](https://www.53ai.com/news/Palantir)

相关资讯

[2026-06-20\\
\\
FDE 术语表：30 个词看懂这个行业在说什么](https://www.53ai.com/news/Palantir/2026062029765.html) [2026-06-19\\
\\
决策系统的真正内核：本体模型](https://www.53ai.com/news/Palantir/2026061937529.html) [2026-06-16\\
\\
中国市场FDE是否有机会？](https://www.53ai.com/news/Palantir/2026061690672.html) [2026-06-11\\
\\
AI组织进化：为什么必须先补Palantir本体论这一课](https://www.53ai.com/news/Palantir/2026061116354.html) [2026-06-10\\
\\
硅谷今年最火的岗位 FDE，我们闷头干了三年](https://www.53ai.com/news/Palantir/2026061023150.html) [2026-06-10\\
\\
咨询与软件FDE转型：深度拆解Palantir生态卡位](https://www.53ai.com/news/Palantir/2026061007516.html) [2026-06-09\\
\\
现在流行的本体(Ontology)，是不是就是我们常说的语义层？](https://www.53ai.com/news/Palantir/2026060908627.html) [2026-06-07\\
\\
别把 Palantir 的“本体”做成知识图谱：企业数据架构的务实落地指南](https://www.53ai.com/news/Palantir/2026060746835.html)

![智能化改造方案](https://static.53ai.com/uploads/20240531/5002026623535870b7a07ff223f9f34a.jpg)![智能化改造方案](https://static.53ai.com/uploads/20240531/5002026623535870b7a07ff223f9f34a.jpg)[联系获取](https://www.53ai.com/solution.html)

![大模型落地应用平台](https://static.53ai.com/uploads/20240529/72a2c0f952f63ef0a546b91beb4bbb32.jpg)![大模型落地应用平台](https://static.53ai.com/uploads/20240530/5002026623535870b7a07ff223f9f34a.jpg)[联系获取](https://www.53ai.com/solution.html)

160+中大型企业正在使用53AI

立即咨询预约演示

[把握AI发展的机遇，共同探索、共同进步\\
\\
2025-01-22](https://www.53ai.com/news/dongtai/2025012294502.html) [如何打造基于GenAI的员工服务机器人\\
\\
2025-01-22](https://www.53ai.com/news/dongtai/2025012234192.html)

[![banner](https://static.53ai.com/uploads/20250611/c637940d8902b253d3264aaf89cd40fc.jpg)](https://hub.53ai.com/)

热点资讯

[Palantir的中国门徒们，走到哪一步了？ \\
\\
2026-04-21](https://www.53ai.com/news/Palantir/2026042180293.html) [Palantir 技术思路与架构发展史：从情报图谱到决策操作系统 \\
\\
2026-04-22](https://www.53ai.com/news/Palantir/2026042265749.html) [FDE：AI时代的职业转型号角已吹响？ \\
\\
2026-05-26](https://www.53ai.com/news/Palantir/2026052650763.html) [当 DeepSeek 遇见 Ontology：企业智能决策的新范式正在出现 \\
\\
2026-05-11](https://www.53ai.com/news/Palantir/2026051197150.html) [硅谷今年最火的岗位 FDE，我们闷头干了三年 \\
\\
2026-06-10](https://www.53ai.com/news/Palantir/2026061023150.html) [吴恩达给正火的 FDE 泼冷水：押注它，不如押注 AI Engineer \\
\\
2026-06-03](https://www.53ai.com/news/Palantir/2026060317459.html) [别把 Palantir 的“本体”做成知识图谱：企业数据架构的务实落地指南 \\
\\
2026-06-07](https://www.53ai.com/news/Palantir/2026060746835.html) [Agentic Ontology：构建企业数字世界 \\
\\
2026-06-04](https://www.53ai.com/news/Palantir/2026060460327.html) [AI组织进化：为什么必须先补Palantir本体论这一课 \\
\\
2026-06-11](https://www.53ai.com/news/Palantir/2026061116354.html) [从PPT到FDE：这是一场咨询人的自我革命 \\
\\
2026-06-05](https://www.53ai.com/news/Palantir/2026060502965.html)

大家都在问

[中国市场FDE是否有机会？ \\
\\
2026-06-16](https://www.53ai.com/news/Palantir/2026061690672.html) [现在流行的本体(Ontology)，是不是就是我们常说的语义层？ \\
\\
2026-06-09](https://www.53ai.com/news/Palantir/2026060908627.html) [FDE：AI时代的职业转型号角已吹响？ \\
\\
2026-05-26](https://www.53ai.com/news/Palantir/2026052650763.html) [Palantir的中国门徒们，走到哪一步了？ \\
\\
2026-04-21](https://www.53ai.com/news/Palantir/2026042180293.html) [本体论思想-抽象建模的本质是什么？ \\
\\
2026-02-05](https://www.53ai.com/news/Palantir/2026020535127.html) [咨询 \| Palantir：我们不想做带着UI的埃森哲；一家咨询公司有望成为Palantir吗？优势和劣势分别在哪里？ \\
\\
2026-01-27](https://www.53ai.com/news/Palantir/2026012743157.html) [Palantir 哪些功能已经被标注为 Sunset（退场）和当前主推的功能是什么？ \\
\\
2026-01-19](https://www.53ai.com/news/Palantir/2026011980765.html) [【深度拆解】Palantir AIP智能体六件套：为何它是企业级Agent的终极形态？ \\
\\
2026-01-08](https://www.53ai.com/news/Palantir/2026010854981.html)

热门标签

[内容创作](https://www.53ai.com/news/neirongchuangzuo) [大模型技术](https://www.53ai.com/news/LargeLanguageModel) [个人提效](https://www.53ai.com/news/gerentixiao) [langchain](https://www.53ai.com/news/langchain) [llamaindex](https://www.53ai.com/news/llamaindex) [多模态技术](https://www.53ai.com/news/MultimodalLargeModel) [RAG技术](https://www.53ai.com/news/RAG) [智能客服](https://www.53ai.com/news/zhinengkefu) [知识图谱](https://www.53ai.com/news/knowledgegraph) [模型微调](https://www.53ai.com/news/finetuning) [RAGFlow](https://www.53ai.com/news/RAGFlow) [coze](https://www.53ai.com/news/coze) [Dify](https://www.53ai.com/news/dify) [Fastgpt](https://www.53ai.com/news/fastgpt) [Bisheng](https://www.53ai.com/news/Bisheng) [Qanything](https://www.53ai.com/news/Qanything) [AI+汽车](https://www.53ai.com/news/AIqiche) [AI+金融](https://www.53ai.com/news/AIjinrong) [AI+工业](https://www.53ai.com/news/AIgongye) [AI+培训](https://www.53ai.com/news/AIpeixun) [AI+SaaS](https://www.53ai.com/news/AISaaS) [Skill](https://www.53ai.com/news/tishicikuangjia) [提示词技巧](https://www.53ai.com/news/tishicijiqiao) [AI+电商](https://www.53ai.com/news/AIdianshang) [AI面试](https://www.53ai.com/news/AImianshi) [数字员工](https://www.53ai.com/news/shuziyuangong) [ChatBI](https://www.53ai.com/news/zhinengbaobiao) [AI知识库](https://www.53ai.com/news/zhishiguanli) [开源大模型](https://www.53ai.com/news/OpenSourceLLM) [智能营销](https://www.53ai.com/news/zhinengyingxiao) [智能硬件](https://www.53ai.com/news/zhinengyingjian) [FDE](https://www.53ai.com/news/zhinenghuagaizao) [AI+医疗](https://www.53ai.com/news/AIyiliao) [MaxKB](https://www.53ai.com/news/MaxKB) [Palantir](https://www.53ai.com/news/Palantir) [Glean](https://www.53ai.com/news/Glean) [Openclaw](https://www.53ai.com/news/Openclaw)

[应聘简历请发送至： ceo@53ai.com](mailto:ceo@53ai.com)

联系我们

售前咨询

[186 6662 7370](tel:18666627370)

预约演示

[185 8882 0121](tel:18588820121)

![](https://static.53ai.com/assets/static/images/loading.svg)

微信扫码

添加专属顾问

回到顶部

![](https://static.53ai.com/assets/static/images/loading.svg)

加载中...

扫码咨询

![](https://www.53ai.com/news/Palantir/2025121217384.html)

![](https://www.53ai.com/news/Palantir/2025121217384.html)

[预约演示](https://work.weixin.qq.com/ca/cawcde2599cf74e2d9) [微信咨询](https://work.weixin.qq.com/ca/cawcdefb661890e885) [电话咨询](tel:400-838-1185)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

安全验证

拖动下方拼图完成验证

![close](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

AI生成背景

![success](<Base64-Image-Removed>)

您的速度已超过 99% 的用户

验证错误,请重试

![load error](<Base64-Image-Removed>)

确定

![slider arrow](<Base64-Image-Removed>)![slider arrow](<Base64-Image-Removed>)![slider arrow](<Base64-Image-Removed>)

安全验证

刷新验证码

![refresh](<Base64-Image-Removed>)

反馈

![tip](<Base64-Image-Removed>)

切换无障碍验证

![Barrier-free verification](<Base64-Image-Removed>)

切换常规验证

![switch](<Base64-Image-Removed>)

### 来源 4: Palantir - 全球大数据与AI领域市值最高的公司-产品核心技术 - 53AI-AI知识库|企业AI知识库|大模型知识库|前线部署工程师|FDE|AIHub

- URL: https://www.53ai.com/news/knowledgegraph/2025120478305.html
- 精读方法：firecrawl-scrape

- [首页](https://www.53ai.com/)
- 产品服务
- 客户案例
- FDE知识库
- 关于我们

热门场景

工作+AI

业务+AI

AIx业务

[落地咨询](https://www.53ai.com/consulting.html)

[场景共创](https://www.53ai.com/fine-tuning.html)

热门产品

[![53AI Brain](https://static.53ai.com/uploads/20250429/f9ed1b6c2d16a688c5791a0057c2217d.png)\\
\\
53AI Brain \\
\\
让知识在人与AI之间高效流动](https://www.53ai.com/products/53AIBrain) [![53AI Studio](https://static.53ai.com/uploads/20250429/b2cd4330d03bce8eb0eb0332eb2954cd.png)\\
\\
53AI Studio \\
\\
高准确率的企业级智能体开发平台](https://www.53ai.com/products/53AIStudio) [![53AI Hub](https://static.53ai.com/uploads/20250429/94e6d990ee63512db567bc53c113e8bd.png)\\
\\
53AI Hub开源\\
\\
三分钟搭建出独立的企业AI门户](https://www.53ai.com/products/53AIHub) [![53AI Agents](https://static.53ai.com/uploads/20250429/05d03bb026421069826c64e2407ad7ee.png)\\
\\
53AI Agents \\
\\
“AI专家”效率倍增的武器](https://www.53ai.com/products/Agents)

[行业案例](https://www.53ai.com/kehuanli/hangyeanli) [场景案例](https://www.53ai.com/kehuanli/solution)

[前沿技术](https://www.53ai.com/news/qianyanjishu) [Agent框架](https://www.53ai.com/news/agentplatform) [行业应用](https://www.53ai.com/news/hangyeyingyong) [企业落地](https://www.53ai.com/news/qiyejingying)

[公司介绍](https://www.53ai.com/about/introduction) [渠道合作](https://www.53ai.com/about/cooperation)

![FDE知识库](https://static.53ai.com/uploads/20250210/aec076a60258b0cc07078c8ea7dff92c.webp)

FDE知识库

学习大模型的前沿技术与行业落地应用

立即咨询预约演示

[![](https://static.53ai.com/assets/static/images/tab1.png)首页](https://www.53ai.com/) [FDE知识库](https://www.53ai.com/news.html) [前沿技术](https://www.53ai.com/news/qianyanjishu) [Palantir](https://www.53ai.com/news/Palantir)

# Palantir - 全球大数据与AI领域市值最高的公司-产品核心技术

发布日期：2025-12-04 15:42:52浏览次数： 3247

作者：数道至简

![](https://static.53ai.com/assets/static/images/detail-icon.png)

微信搜一搜，关注“数道至简”

推荐语

揭秘Palantir如何用数字孪生技术重构企业决策系统，打造全球领先的AI操作系统。

核心内容：

1\. 基于本体(Ontology)驱动的数字孪生平台架构

2\. 数据集成与Pipeline构建的组织数字孪生技术

3\. 面向国防和民用场景的双产品线技术实现

![](https://static.53ai.com/assets/static/images/avatar.jpg)

杨芳贤

53AI创始人/腾讯云(TVP)最具价值专家

## 前两天聊了他们的主要产品，本文主要从产品技术为思路进行整理。

## 一、整体定位：一个面向复杂组织的“决策操作系统”

    Palantir 并非传统意义上的数据平台或 BI 工具，而是一个 **集成数据、模型、应用、AI 与运维的统一操作系统**，其目标是支撑高复杂度、高合规性、高行动导向的企业级决策闭环。该系统以 **Foundry（民用）** 和 **Gotham（国防/情报）** 为两大产品线，共享底层技术栈，但面向不同场景。

**技术本质**：Palantir 构建了一个 **基于本体（Ontology）驱动的、可编程的数字孪生平台**，使得组织能够在其上运行“数据 → 模型 → 决策 → 执行 → 反馈”的完整控制回路。

二、核心技术

### 1\. Ontology：业务语义的操作系统内核

#### 技术实现

- **对象模型抽象层：Ontology 将底层异构数据（关系表、JSON、Parquet、流数据等）映射为**

**类型化的对象（Typed Objects）**，每个对象具有：

  - **Schema（属性定义）**
  - **Relationships（关联关系）**
  - **Permissions（细粒度 ACL）**
  - **Lifecycle Hooks（事件触发器）**

- **对象存储引擎：**

  - **Object Storage V2**（当前主流）：基于分布式列式存储，支持 PB 级对象规模，提供毫秒级点查与高效聚合。
  - 支持 **增量索引更新**（Delta Indexing），确保实时性。
  - 与 **Conjure**（Palantir 自研的 RPC/IDL 框架）深度集成，实现强类型 API。

- **语义一致性保障：**

  - 通过 **Ontology Versioning** 机制，支持对象模型的演进（如新增属性、修改关系），而无需破坏下游依赖。
  - 所有上层应用（包括 AI Agent）通过 **Ontology API** 访问数据，而非直接查询原始表。

#### 技术价值

- **解耦业务逻辑与物理存储：DW/数据湖结构变更不影响上层应用。**
- **LLM 友好性：大模型可通过自然语言理解：**

```
“Flight 405 delayed due to weather”而非 SELECT * FROM flights WHERE id = 'F405'
```

- **权限即代码（Policy-as-Code）：对象级权限策略可随模型一同版本化管理。**

**关键区别**：不同于传统主数据管理（MDM）或知识图谱，Palantir 的 Ontology 是 **可执行的、带权限的、与工作流绑定的运行时语义层**。

**2\. 数据集成与 Pipeline：构建可信的“组织数字孪生”**

#### 核心组件：Foundry Data Lineage & Pipelines

- **Pipeline Builder：**

  - 支持 **声明式（YAML/Conjure） + 可视化拖拽** 混合开发。
  - 底层基于 **Spark / Flink** 引擎，但对用户透明。
  - 每个 pipeline 节点生成 **可追溯的数据血缘**（Data Lineage），精确到字段级别。

- **统一 Schema Registry：**

  - 所有摄入数据必须注册到 **Ontology-aware Schema Registry**，强制语义对齐。
  - 支持 **schema evolution** 与 **backward compatibility** 检查。

- **虚拟化能力（Virtual Datasets）：**

  - 允许在不物理复制数据的前提下，跨源（S3, Snowflake, Kafka, SAP）构建联合视图。
  - 查询时动态下推（Push-down）到源系统，兼顾性能与成本。

#### 技术目标

- 实现 **Single Source of Truth（SSOT）** 的动态构建，而非静态仓库。
- 支撑 **what-if 模拟**：例如在排产系统中，修改“某工厂产能”后，自动重算供应链影响。

**工程亮点**：Pipeline 支持 **branching & rollback**（类似 Git for Data），允许在隔离环境中测试数据变更，再安全上线。

3\. AIP（Artificial Intelligence Platform）：将 LLM 转化为可执行智能体![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=129293&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IYWRONjhBbXpsa05TYVVoSUtXNzJ2UUt2SnZEc3VCNzlGUFJQWGliZFZaTGs2c3RhU1dnajVIOUEyOExEOWg4SjhyY1NSejZvRWd0UnFvWldUVVFHd1EvNjQwP3d4X2ZtdD1wbmcmYW1w;from=appmsg)

    Palantir 的 AI 战略不是“聊天机器人”，而是 **Actionable AI** —— 让模型能 **读、写、调用、执行**。

#### 架构分层

![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=129293&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IYWRONjhBbXpsa05TYVVoSUtXNzJ2UUt2SnZEc3VCN1FYaWFpY0JuaWJuYk9mVURTOWNpY3NSUXJoUWw1b2ZpY1NrNmJldUJYdlpRaWNvUUtmNlRhT1RIVDBzdy82NDA/d3hfZm10PXBuZyZhbXA=;from=appmsg)

#### 关键能力

- **Tool Use with Guardrails：**

  - 每个 AI Agent 只能调用预授权的 **Actions**（如 “update\_inventory\_level”），且受 RBAC 控制。
  - 所有操作留痕，满足审计要求（SOX, HIPAA 等）。

- **RAG on Ontology：**

  - 检索增强生成（RAG）直接基于 Ontology 对象图进行，而非原始文本块。
  - 例如：“找出过去一周延迟的航班及其关联机组” → 自动遍历 `Flight → Crew` 关系。

- **Closed-Loop Learning：**

  - Agent 执行结果（成功/失败）反馈回系统，用于优化提示词（Prompt Tuning）或重训微调模型。

**范式转变**：AIP 不是“AI as Service”，而是 **AI as Integrated Workflow Participant**。

4\. Apollo：面向极端环境的 DevSecOps 操作系统

    Apollo 是 Palantir 能在五角大楼、核电站、跨国药企等严苛场景落地的关键。

#### 架构设计

- **Hub-and-Spoke 模型：**

  - **Apollo Hub：中央控制平面，管理所有环境的期望状态（Desired State）。**

- **Deployment Platforms：轻量代理，部署在目标环境（云、本地、边缘、断网区）。**
- **GitOps 原生：**

  - 所有配置（服务版本、网络策略、密钥）存储于 Git 仓库。
  - 自动同步差异，支持 **canary rollout, blue-green, feature flags**。

- **环境抽象层：**

  - 统一抽象 Kubernetes、VM、裸机甚至嵌入式设备为“Deployment Target”。
  - 在无网络环境下，支持 **air-gapped sync via USB/SD card**（用于军事场景）。

#### 运维能力

- **全栈可观测性：集成日志、指标、追踪，但**

**按 Ontology 对象聚合**（如查看“某订单”的全链路日志）。

- **合规自动化：自动生成 SOC2、FedRAMP 合规报告。**
- **灾难恢复：支持跨地域一键重建整个 Foundry 实例。**

**独特优势**：Apollo 使得 Palantir 能在 **数百个异构客户环境** 中保持平台一致性，这是多数 SaaS 无法做到的。

**四、总结：Palantir 的技术护城河**![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=129293&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IYWRONjhBbXpsa05TYVVoSUtXNzJ2UUt2SnZEc3VCN3RsalBIa0VpYTVwb2pXNUk2eXRsblJlQmNRelRVcU5SZUZqa2J6REJwa2JmdGZIYTdvTEZDaHcvNjQwP3d4X2ZtdD1wbmcmYW1w;from=appmsg)

    Palantir 的真正创新，不在于某项单项技术（如用了 Spark 或 LLM），而在于 **将数据、语义、AI、行动、运维整合为一个可编程、可审计、可演进的操作系统**。这使其在高 stakes（高风险、高价值）决策场景中具备不可替代性。

[知识图谱](https://www.53ai.com/keyword/%E7%9F%A5%E8%AF%86%E5%9B%BE%E8%B0%B1) [知识图谱构建](https://www.53ai.com/keyword/%E7%9F%A5%E8%AF%86%E5%9B%BE%E8%B0%B1%E6%9E%84%E5%BB%BA) [知识图谱可视化](https://www.53ai.com/keyword/%E7%9F%A5%E8%AF%86%E5%9B%BE%E8%B0%B1%E5%8F%AF%E8%A7%86%E5%8C%96)

分享：

用微信扫描二维码

用微信扫描二维码

用微信扫描二维码

用微信扫描二维码

53AI，企业落地大模型首选服务商

**产品**：场景落地咨询+大模型应用平台+行业解决方案

**承诺**：免费POC验证，效果达标后再合作。 **零风险落地应用大模型**，已交付160+中大型企业

[上一篇：Palantir发布新产品Chain Reaction：面向美国人工智能基础设施的操作系统](https://www.53ai.com/news/Palantir/2025120536742.html) [下一篇：详解Palantir中组件、变量、本体之间的铁三角关系](https://www.53ai.com/news/Palantir/2025120483072.html)

[返回列表](https://www.53ai.com/news/Palantir)

相关资讯

[2026-06-20\\
\\
FDE 术语表：30 个词看懂这个行业在说什么](https://www.53ai.com/news/Palantir/2026062029765.html) [2026-06-19\\
\\
决策系统的真正内核：本体模型](https://www.53ai.com/news/Palantir/2026061937529.html) [2026-06-16\\
\\
中国市场FDE是否有机会？](https://www.53ai.com/news/Palantir/2026061690672.html) [2026-06-11\\
\\
AI组织进化：为什么必须先补Palantir本体论这一课](https://www.53ai.com/news/Palantir/2026061116354.html) [2026-06-10\\
\\
硅谷今年最火的岗位 FDE，我们闷头干了三年](https://www.53ai.com/news/Palantir/2026061023150.html) [2026-06-10\\
\\
咨询与软件FDE转型：深度拆解Palantir生态卡位](https://www.53ai.com/news/Palantir/2026061007516.html) [2026-06-09\\
\\
现在流行的本体(Ontology)，是不是就是我们常说的语义层？](https://www.53ai.com/news/Palantir/2026060908627.html) [2026-06-07\\
\\
别把 Palantir 的“本体”做成知识图谱：企业数据架构的务实落地指南](https://www.53ai.com/news/Palantir/2026060746835.html)

[联系获取](https://www.53ai.com/solution.html)

[联系获取](https://www.53ai.com/solution.html)

160+中大型企业正在使用53AI

立即咨询预约演示

[把握AI发展的机遇，共同探索、共同进步\\
\\
2025-01-22](https://www.53ai.com/news/dongtai/2025012294502.html) [如何打造基于GenAI的员工服务机器人\\
\\
2025-01-22](https://www.53ai.com/news/dongtai/2025012234192.html)

[![banner](https://static.53ai.com/uploads/20250611/c637940d8902b253d3264aaf89cd40fc.jpg)](https://hub.53ai.com/)

热点资讯

[Palantir的中国门徒们，走到哪一步了？ \\
\\
2026-04-21](https://www.53ai.com/news/Palantir/2026042180293.html) [Palantir 技术思路与架构发展史：从情报图谱到决策操作系统 \\
\\
2026-04-22](https://www.53ai.com/news/Palantir/2026042265749.html) [FDE：AI时代的职业转型号角已吹响？ \\
\\
2026-05-26](https://www.53ai.com/news/Palantir/2026052650763.html) [当 DeepSeek 遇见 Ontology：企业智能决策的新范式正在出现 \\
\\
2026-05-11](https://www.53ai.com/news/Palantir/2026051197150.html) [硅谷今年最火的岗位 FDE，我们闷头干了三年 \\
\\
2026-06-10](https://www.53ai.com/news/Palantir/2026061023150.html) [吴恩达给正火的 FDE 泼冷水：押注它，不如押注 AI Engineer \\
\\
2026-06-03](https://www.53ai.com/news/Palantir/2026060317459.html) [别把 Palantir 的“本体”做成知识图谱：企业数据架构的务实落地指南 \\
\\
2026-06-07](https://www.53ai.com/news/Palantir/2026060746835.html) [Agentic Ontology：构建企业数字世界 \\
\\
2026-06-04](https://www.53ai.com/news/Palantir/2026060460327.html) [AI组织进化：为什么必须先补Palantir本体论这一课 \\
\\
2026-06-11](https://www.53ai.com/news/Palantir/2026061116354.html) [从PPT到FDE：这是一场咨询人的自我革命 \\
\\
2026-06-05](https://www.53ai.com/news/Palantir/2026060502965.html)

大家都在问

[中国市场FDE是否有机会？ \\
\\
2026-06-16](https://www.53ai.com/news/Palantir/2026061690672.html) [现在流行的本体(Ontology)，是不是就是我们常说的语义层？ \\
\\
2026-06-09](https://www.53ai.com/news/Palantir/2026060908627.html) [FDE：AI时代的职业转型号角已吹响？ \\
\\
2026-05-26](https://www.53ai.com/news/Palantir/2026052650763.html) [Palantir的中国门徒们，走到哪一步了？ \\
\\
2026-04-21](https://www.53ai.com/news/Palantir/2026042180293.html) [本体论思想-抽象建模的本质是什么？ \\
\\
2026-02-05](https://www.53ai.com/news/Palantir/2026020535127.html) [咨询 \| Palantir：我们不想做带着UI的埃森哲；一家咨询公司有望成为Palantir吗？优势和劣势分别在哪里？ \\
\\
2026-01-27](https://www.53ai.com/news/Palantir/2026012743157.html) [Palantir 哪些功能已经被标注为 Sunset（退场）和当前主推的功能是什么？ \\
\\
2026-01-19](https://www.53ai.com/news/Palantir/2026011980765.html) [【深度拆解】Palantir AIP智能体六件套：为何它是企业级Agent的终极形态？ \\
\\
2026-01-08](https://www.53ai.com/news/Palantir/2026010854981.html)

热门标签

[内容创作](https://www.53ai.com/news/neirongchuangzuo) [大模型技术](https://www.53ai.com/news/LargeLanguageModel) [个人提效](https://www.53ai.com/news/gerentixiao) [langchain](https://www.53ai.com/news/langchain) [llamaindex](https://www.53ai.com/news/llamaindex) [多模态技术](https://www.53ai.com/news/MultimodalLargeModel) [RAG技术](https://www.53ai.com/news/RAG) [智能客服](https://www.53ai.com/news/zhinengkefu) [知识图谱](https://www.53ai.com/news/knowledgegraph) [模型微调](https://www.53ai.com/news/finetuning) [RAGFlow](https://www.53ai.com/news/RAGFlow) [coze](https://www.53ai.com/news/coze) [Dify](https://www.53ai.com/news/dify) [Fastgpt](https://www.53ai.com/news/fastgpt) [Bisheng](https://www.53ai.com/news/Bisheng) [Qanything](https://www.53ai.com/news/Qanything) [AI+汽车](https://www.53ai.com/news/AIqiche) [AI+金融](https://www.53ai.com/news/AIjinrong) [AI+工业](https://www.53ai.com/news/AIgongye) [AI+培训](https://www.53ai.com/news/AIpeixun) [AI+SaaS](https://www.53ai.com/news/AISaaS) [Skill](https://www.53ai.com/news/tishicikuangjia) [提示词技巧](https://www.53ai.com/news/tishicijiqiao) [AI+电商](https://www.53ai.com/news/AIdianshang) [AI面试](https://www.53ai.com/news/AImianshi) [数字员工](https://www.53ai.com/news/shuziyuangong) [ChatBI](https://www.53ai.com/news/zhinengbaobiao) [AI知识库](https://www.53ai.com/news/zhishiguanli) [开源大模型](https://www.53ai.com/news/OpenSourceLLM) [智能营销](https://www.53ai.com/news/zhinengyingxiao) [智能硬件](https://www.53ai.com/news/zhinengyingjian) [FDE](https://www.53ai.com/news/zhinenghuagaizao) [AI+医疗](https://www.53ai.com/news/AIyiliao) [MaxKB](https://www.53ai.com/news/MaxKB) [Palantir](https://www.53ai.com/news/Palantir) [Glean](https://www.53ai.com/news/Glean) [Openclaw](https://www.53ai.com/news/Openclaw)

[应聘简历请发送至： ceo@53ai.com](mailto:ceo@53ai.com)

联系我们

售前咨询

[186 6662 7370](tel:18666627370)

预约演示

[185 8882 0121](tel:18588820121)

![](https://static.53ai.com/assets/static/images/loading.svg)

微信扫码

添加专属顾问

回到顶部

![](https://static.53ai.com/assets/static/images/loading.svg)

加载中...

扫码咨询

![](https://www.53ai.com/news/knowledgegraph/2025120478305.html)

![](https://www.53ai.com/news/knowledgegraph/2025120478305.html)

[预约演示](https://work.weixin.qq.com/ca/cawcde2599cf74e2d9) [微信咨询](https://work.weixin.qq.com/ca/cawcdefb661890e885) [电话咨询](tel:400-838-1185)

### 来源 5: Concept-Centric Software Development

- URL: https://arxiv.org/html/2304.14975
- 精读方法：jina-readerlm-academic

```markdown
# Concept-Centric Software Development

## An Experience Report

### Peter Wilczynski, Taylor Gregoire-Wright, Daniel Jackson
#### (2023; 2023-04-28; 2023-08-11; 2023-10-12)

**Authors:**  
* **Peter Wilczynski**
  * Palantir Technologies Inc., Denver CO USA
* **Taylor Gregoire-Wright**
  * Ontologize LLC, Palo Alto CA USA
* **Daniel Jackson**
  * Massachusetts Institute of Technology, Cambridge MA USA

**Dates:**  
* December 2023

---

## Abstract

Developers have long recognized the importance of the concepts underlying the systems they build, and the primary role that concepts play in shaping user experience. To date, however, concepts have tended to be only implicit in software design with development being organized instead around more concrete artifacts (such as wireframes and code modules).

Palantir, a software company whose data analytics products are widely used by major corporations, recently reworked the internal representation of its software development process to bring concepts to the fore, making explicit the concepts underlying its products, including how they are clustered together, used in applications, and governed by teams. With a centralized repository of concepts, engineers are able to align products more closely based on shared concepts, evolve concepts in response to user needs, and communicate more effectively with non-engineering groups within the company.

This paper reports on Palantir's experiences to date, analyzing both successes and challenges, and offers advice to other organizations considering adopting a concept-centric approach to software development.

**Keywords:** concepts, software design, ontology

---

## Introduction

For decades, software engineers have recognized the importance of the concepts that underlie software systems. Without a robust notion of what concepts are and how they might be described and analyzed. The theory of concept design described in _The Essence of Software_ (Jackson \[2021\]) builds on well-established software engineering ideas but also extends them in new directions. In this section:

* Identifies key ideas.
* Describes how EOS can apply to software design.
* Discusses implications for business strategy.

---

## Outline of Concept Design Theory

### Key Ideas

Concept design starts with an idea that many of the essential qualities of a software system follow from functionality. Concepts offer a way to define functionality that is experienced directly by users and aligned with their needs.

Key distinguishing qualities:
* User-facing.
* Functional.
* Behavioral.
* Independent.
* Purposive.
* Valuable.

### Application Examples

Consider the Clip concept (discussed in Section A.0.1):
- User-facing: Encapsulates functionality spanning multiple code modules but is experienced by users as a single unit.
- Functional: Represents functionality without reliance on other concepts.
- Behavioral: Provides dynamic behavior involving multiple objects and encapsulates its own data model.
- Independent: Used across multiple applications without dependence on other concepts.
- Purposive: Addresses user needs for embedding segments within other resources while maintaining linkage between source and destination.
- Valuable: Synthesizes disparate unique insights from various precursor concepts into a unified concept.

---

## Example Concept

### Context

As with all design work, concepts need to be developed pragmatically—the best concepts are practical solutions to specific problems. However, it’s almost impossible for designers to anticipate all interactions and experiences surrounding a concept. Therefore, concept clarification is a common workflow for concept designers.

In 2021:
- Developed generic Clip concept to generalize TextSnippet, MapSlide, GraphSnapshot, VideoClip (see Fig. A.0.1).

Inspired by OpenDoc in the 1990s:
- Purpose: Let users embed segments within another resource while maintaining linkage between source and destination.
- Generalization across static and dynamic clip sources.

Clarification:
- Split into ClipDefinition (clip metadata) and ClipCapture (static snapshot).
- Clarified version control semantics: changes could occur at different levels (clip definition vs clip capture vs source document).

---

## Early Benefits

### Uptake of Concept Entities

Foundry tracks each entity’s users:
| | |
| --- | --- |
| Users | Number |
| Password | About 5% |
| Display Name | About 5% |
| Recent Likes | About 5% |

Organic adoption of concepts has increased over time:
| | |
| --- | --- |
| Users | Number |
| Password | About 5% |
| Display Name | About 5% |
| Recent Likes | About 5% |

### Product Documentation

Organic adoption of product documentation:
| | |
| --- | --- |
| Documents | Number |
| List Literature Review | About 5% |
| Search Lists Results | About 5% |

### Product Manager Career Growth

Improved product

### 来源 6: 以AI+本体框架整合多源数据，依托4大平台，让Palantir得以发现隐藏 ...

- URL: https://www.smartcity.team/investment/companies/palantir
- 精读方法：firecrawl-scrape

![8c581e79b09d74f981fe8b1c6e600361](https://www.smartcity.team/wp-content/uploads/2025/10/8c581e79b09d74f981fe8b1c6e600361.png)

Palantir是全球领先的大数据与AI平台软件提供商，定位为服务于国家级安全机构与全球大型企业的“决策操作系统”供应商。

**公司依托“政府+商业”双轮驱动模式 。**

在政府端，Palantir深度绑定美国国防与情报体系，构筑了稳固的基本盘。

![641-1](https://www.smartcity.team/wp-content/uploads/2025/10/641-1.jpg)

图：Palantir政府客户列表，UBS，AlphaEngine

在商业端，公司凭借Foundry及AIP平台，为能源、金融、制造等关键行业的头部企业提供数字化转型与AI落地解决方案，成为其技术伙伴，展现出更高的增长弹性。

![641](https://www.smartcity.team/wp-content/uploads/2025/10/641.jpg)

图：Palantir商业客户数量，UBS，AlphaEngine

**Palantir由多位背景深厚的硅谷精英共同创立，融合了顶尖的技术专长、敏锐的商业洞察与强大的资本运作能力 。**

Peter Thiel是作为“PayPal黑帮”的灵魂人物，他联合创立了PayPal，并且是Facebook（现Meta）的传奇早期投资人，其投资哲学体现在畅销书《从0到1》中。

他拥有斯坦福大学哲学学士与法学博士学位，为公司注入了深厚的商业与资本基因。

Palantir的CEO Alex Karp是Thiel在斯坦福的室友， 尽管政治立场不同，但还是亲密合作，主要负责公司的日常运营与战略方向，是Palantir对外形象代表。

Stephen Cohen拥有斯坦福大学计算机科学学士学位，具备深厚的技术背景，是公司早期技术研发的核心力量之一。

Palantir的发展历程可清晰地划分为四个阶段，展现了其从政府服务向商业化、平台化及AI化演进的战略路径。

**政务业务奠基期 (2003-2010)**

2003年Peter Thiel等人联合创立Palantir，早期获得CIA旗下风投基金In-Q-Tel的投资，专注于为美国国防与情报部门提供反恐数据分析服务。

2008年，公司推出其首个核心平台Gotham，专为政府客户设计，奠定了其在国防和情报领域的市场地位。

**商业业务起步期 (2011-2016)**

2011年，公司首次将业务拓展至商业领域，与摩根大通合作开发反欺诈解决方案，迈出商业化第一步。

在2014至2015年间，Palantir与英国石油（BP）、空客（Airbus）等行业巨头达成合作，逐步在商业市场建立影响力。

**商业平台规模化期 (2016-2022)**

2016年，Palantir正式推出面向商业客户的Foundry平台，旨在打造企业级“中央操作系统”，标志着商业业务进入规模化阶段。

2020年9月，公司通过直接上市（DPL）的方式在纽约证券交易所挂牌，股票代码为PLTR，显著提升了市场知名度。

2018年推出Apollo平台以优化软件部署，2021年与IBM合作将Foundry整合至其云平台，并成立Palantir Japan拓展亚洲市场。

**AI驱动增长期 (2023-至今)**

2023年4月，Palantir推出人工智能平台（AIP），将生成式AI能力与现有平台深度融合，开启了由AI驱动的新增长周期。

2023年9月，公司被纳入标普500指数，随后转板至纳斯达克并加入纳斯达克100指数，获得了更广泛的投资者关注。

2024年与BP达成AIP合作，2025年与xAI等合作推出金融AI解决方案，AIP的商业化落地成果显著。

## （2）Palantir的四大核心产品

Palantir构建了四大核心产品平台，形成了从底层部署、中层数据融合到上层AI应用的全栈能力，覆盖政府与商业两大领域，其中AIP平台是驱动当前业绩爆发式增长的核心引擎。

![641-2](https://www.smartcity.team/wp-content/uploads/2025/10/641-2.jpg)

图：AlphaEngine Agent制图

**Gotham平台：面向政府客户，尤其专注于国防、情报等高度复杂的决策场景** 。

其核心能力在于整合海量、多源、异构的数据（如卫星、无人机、雷达、人力情报等），通过强大的数据融合与分析能力，帮助用户在看似无关的信息中发现隐藏的模式、线索和关联，为反恐、军事行动、灾难响应等提供关键决策支持。

例如，其深度参与的TITAN智能作战系统，能够为前线和指挥人员提供统一的可视化平台并支持实时协作。

**Foundry平台：面向商业客户，定位为企业的“中央操作系统”** 。

它旨在打破企业内部的数据孤岛，将生产、供应链、销售、财务等所有数据集中到一个统一的平台上。

Foundry提供从数据接入、清洗、建模到可视化、低代码应用开发的全套工具，帮助企业构建其业务的“数字孪生”体。

典型应用如为空客 A350 整合全球生产与供应链数据，打造数字孪生系统，最终使产量提升 33% 。

**Apollo平台：作为Gotham和Foundry的底层技术基座，Apollo是一个软件持续部署与管理平台** 。

其核心价值在于确保Palantir的软件能够在任何环境下（包括公有云、私有云、本地服务器甚至断网的战术边缘环境）稳定运行、无缝更新和统一管理。

Apollo通过单一平台管理所有软件的持续维护和更新，是Palantir实现产品化和规模化交付的关键，支持动态实时数据分析。

**AIP：作为驱动当前业绩增长的核心引擎，旨在将大语言模型安全、有效地整合到Gotham和Foundry平台中** 。

它不仅是一个简单的AI聊天助手，更是一个面向Agent时代的开发与执行环境，包含AIP Assist（界面聊天助手）、AIP Logic（无代码开发环境）和AIP Agent Studio（快速创建智能代理）等核心模块。

AIP的推出极大加速了Palantir的商业化进程，尤其在美国市场，其商业收入增长率因此大幅提升。

## （3）Palantir的核心竞争力与护城河

Palantir的护城河并非单一优势，而是由技术、数据、品牌、模式四大要素交织构成的立体化、自增强体系。

其商业模式常被类比为 “ **微软（技术）+麦肯锡（咨询）**”的结合体 ，形成了难以逾越的综合壁垒。

![641-3](https://www.smartcity.team/wp-content/uploads/2025/10/641-3.jpg)

图：AlphaEngine Agent作图

**技术壁垒：Palantir独特的“本体（Ontology）”构建能力，是区别于其他数据分析公司的根源** 。

所谓“本体”就像是企业内部的“业务地图”， 把公司里的人、机器、订单、仓库、交易等作为一个个不同的“本体”，注明它们之间的关系，比如谁属于谁、谁依赖谁、谁跟谁有流程。

这样一来，不管业务数据多么分散，都能共享同一套“业务语言”。

![641-5](https://www.smartcity.team/wp-content/uploads/2025/10/641-5.jpg)

图：Palantir客户访谈纪要，UBS，AlphaEngine

基于本体规则驱动，Palantir能实现动态的业务孪生建模，有效处理传统系统难以应对的复杂模态数据与深度业务场景需求。

通过高阶实施工程师（FDE）与客户的深度协作，将复杂的业务知识转化为可复用、可迭代的数字资产，为AI决策提供坚实的语义基础。

**数据粘性壁垒：数据粘性是Palantir护城河中最坚固的部分之一，体现为极高的转换成本 。**

Palantir每进入一个新行业，便构建一套新的本体空间。

这些不同行业的本体空间能够相互连接、复用，逐步形成对现实世界的数字孪生建模，即一个庞大的“世界模型”。

随着业务扩张，其护城河呈指数级拓宽，例如在军工领域长达20年的本体积累，短期内无法被复制。

客户数据在经过Palantir平台归一化处理后，深度融入其本体架构。

若客户希望迁移至其他系统，不仅面临巨大的技术挑战，更意味着其沉淀多年的业务逻辑和数字资产将作废，转换成本极高。

![641-6](https://www.smartcity.team/wp-content/uploads/2025/10/641-6.jpg)

图： Palantir客户访谈纪要，UBS，AlphaEngine

**品牌认知壁垒：Palantir的品牌力源自一系列“传奇”案例的背书，构成了强大的认知壁垒**。

从早期协助CIA、在美国追捕本·拉登行动中提供关键情报支持，到破获麦道夫金融诈骗案，再到商业领域帮助空客（Airbus）优化全球供应链，这些高难度、高影响力的标杆案例，为Palantir的实战能力提供了最强有力的证明。

这些成功案例在全球范围内塑造了“最顶尖的政府机构和商业巨头都在使用”的强大品牌势能。

这使其在获取新客户时具备天然的信任优势，显著降低了市场教育成本，并能支撑其高昂的客单价。

**FDE模式壁垒：Palantir独创的交付模式是其区别于传统软件公司的另一大壁垒**。

公司独创“FDE（前线部署工程师）+咨询”的交付模式，将高阶工程师作为核心资产派驻客户现场，深度解决业务问题。

这种模式远超传统软件销售，实现了7天极速POC（概念验证），将获客周期缩短6-12个月，交付效率极高。

通过跨行业的项目交付，Palantir积累了大量可复用的数据、产品模块和行业知识，形成了强大的复利效应。

## （4）Palantir财务数据分析

Palantir在2025年上半年展现出强劲的增长动能与盈利能力。

Q2实现营收10.04亿美元，同比增长48%，环比增长14%。

**业绩增长的核心亮点在于其美国商业业务的爆发式增长** 。

公司Q2美国商业收入达3.06亿美元，同比增长93%，美国政府收入达4.26亿美元，同比增长53%。

**同时，公司的盈利能力也得到显著提升**。Q2 GAAP净利润率达到33%，同比增加12个百分点，显示出公司在规模化扩张的同时，其商业模式的盈利效率正在快速释放。

![641-7](https://www.smartcity.team/wp-content/uploads/2025/10/641-7.jpg)

图：Palantir财务数据，BofA，AlphaEngine

Palantir在2022至2024年间经历了从亏损到盈利、从增速放缓到再次加速的关键性转变，其业绩拐点在2023年确立，核心驱动力为人工智能平台（AIP）的推出与商业化落地。

![641-4](https://www.smartcity.team/wp-content/uploads/2025/10/641-4.jpg)

图：AIP推出的影响，UBS，AlphaEngine

公司在手订单充足，截至Q2公司在手合同价值约22.7亿美元，同比增长 140%，其中美国商务业务合同价值达到8.43 亿美元，同比增长222%，均创公司历史纪录。

**近期Palantir官方上调了2025财年的全年业绩指引，预计全年营收将达到41.42亿至41.5亿美元** ，这意味着同比增长率约为45%，彰显了公司对当前业务增长势头的强烈信心。

分析师普遍对Palantir 2026年的业绩保持乐观。

综合预测显示，预计公司2026年营收将实现超过26%的同比增长，同时净利润增长预计将接近37%，反映出市场对其盈利能力持续改善的预期。

公司管理层为未来五年设定了极具雄心的增长目标。

**其长期愿景是实现10倍的业务增长，使年化营收达到120亿美元的规模，这意味着未来五年的年均复合增长率（CAGR）需高达58%**。

## （5）Palantir的主要竞争对手

Palantir凭借其独特的“本体论”技术路径和“咨询+产品”的深度服务模式，在高端数据分析市场，特别是政府、国防及复杂工业领域，构筑了难以复制的竞争壁垒。

公司的主要竞争对手包括Databricks、C3.AI 、Snowflake、Microsoft、IBM、Accenture、Deloitte等。

![641-8](https://www.smartcity.team/wp-content/uploads/2025/10/641-8.jpg)

![641-11](https://www.smartcity.team/wp-content/uploads/2025/10/641-11.jpg)

图：AlphaEngine Agent制表

Databricks擅长数据仓库/湖和模型训练等计算任务，覆盖超过60%的财富500强企业，应用领域包括流媒体、金融、制造、航空等。

与Palantir主要服务政府、国防等客户不同，Databricks服务广泛商业客户，提供平台级产品，由客户和合作伙伴自主解决业务问题，而不提供端到端的交付能力。

C3.ai 专注于企业级AI部署，目标客户包括国防和企业领域（如美国空军、壳牌公司），与Palantir的客户群体有重叠，但更侧重于AI模型和工具服务， 而非深度行业定制。

Snowflake专注于云数据仓库和数据处理，主要面向商业客户，提供云原生数据仓库服务，但缺乏Palantir在政府和高安全性领域的深度渗透。

![641-10](https://www.smartcity.team/wp-content/uploads/2025/10/641-10.jpg)

图：Palantir客户访谈，UBS，AlphaEngine

IBM、埃森哲、德勤等也与Palantir的业务存在竞争关系，这里不多展开。

## （6）Palantir的催化剂与潜在风险

**首先，美国政府业务作为Palantir的基石，正进入新一轮的加速扩张期 。**

美国陆军的Maven Smart System (MSS)项目合同上限从最初的4.8亿美元大幅提升166%至12.75亿美元，这不仅直接增厚了未来的收入确定性，也反映了美国国防部对其技术的高度认可。

MSS合同在2024-2025年的首年支出已达到约1.85亿美元，合同执行进度远超市场预期，预示着未来四年的年均支出有望达到2.725亿美元，为政府业务的持续高增长提供了坚实基础。

**其次，AIP的快速商业化落地，已成为公司最强劲的增长引擎 。**

在AIP的驱动下，2025年Q2美国商业业务收入实现了93%的惊人同比增长，环比增长20%，证明了AIP在企业市场的强大吸引力和变现能力。

AIP的成功应用吸引了大量新客户，Q2净增客户79家，同比增长103%。客户正从初步的概念验证（POC）阶段快速转向规模化部署，尤其是在医疗、制造和零售等行业。

然后我们来看Palantir面临的主要风险。

**Palantir面临的最大风险是显著的市值高估，其股价已严重透支未来增长预期 。**

当前估值对应2026年预期自由现金流的153倍，远高于软件行业48倍的平均水平。

这种极端估值意味着市场对增长的预期极为苛刻。

**第二，公司的核心技术和产品安全性面临严峻考验**。

近期，其为美军打造的“下一代指挥与控制系统”（NGC2）被内部报告曝光存在“基础安全控制、流程和治理方面的严重缺陷”，系统风险等级被评为“极高”。

该报告严厉指出，系统“无法控制访问权限、无法验证软件安全”，直接引发市场对其技术可靠性的担忧。

此负面事件导致公司股价在2025年10月3日单日大跌7.47%，市值蒸发超330亿美元，并使外界质疑其“硅谷模式”在军事领域的适用性。

**第三，Palantie的国际业务，特别是欧洲市场的持续疲软是公司增长的一大拖累**。

2025年Q2，其国际商业收入同比下滑3%，已连续多个季度呈现负增长。

考虑到欧洲市场在2024年占公司总收入的11%，该区域的持续不振对整体业绩构成显著压力。

此外，国际政府业务的增长动力亦出现放缓迹象，其同比增速已从第一季度的46%下降至第二季度的37%。

本报告由FinGPT Agent辅助生成，报告地址：点击查阅

![641-9](https://www.smartcity.team/wp-content/uploads/2025/10/641-9.jpg)

# Palantir产品体系的复利密码与技术壁垒拆解

来源：中科世通亨奇

当多数科技公司将 “技术壁垒” 等同于 “独家算法” 或 “专利数量” 时，Palantir 给出了另一种答案：真正的壁垒，是能持续解决真实问题的 “体系能力”。这家深耕政企、国防等高壁垒领域的企业，从未陷入 “闭门造产品” 的误区，而是以客户现场为 “实验室”，通过工程师驻场的实战经验沉淀产品模块，实现从 “定制服务” 到 “平台化产品” 的复利增长；更关键的是，它通过 “AI Mesh” 体系将数据整合、决策分析、部署调度、AI 赋能四大能力拧成闭环，形成从数据到决策的全链条支撑，这种 “实战沉淀 + 体系协同” 的组合构筑了对手难以逾越的护城河。

```
 核心观点速览：

产品复利逻辑：Palantir 摒弃传统产品设计模式，派工程师深入客户现场，积累解决实际问题的经验。将重复痛点转化为标准化工具，打造出 Foundry 等核心平台，实现从定制服务到规模化产品的蜕变 。

架构核心形态：旗下 Foundry、Gotham、Apollo、AIP 四大平台以 “APP 集合体” 形式运作，集成众多功能各异的 APP，满足不同行业客户的个性化需求，同时保障体系协同 。

技术壁垒关键：“AI Mesh” 协同闭环体系是 Palantir 的技术护城河。Foundry 整合数据，Gotham 负责决策，Apollo 管理部署，AIP 赋能 AI，四大平台紧密协作，形成完整的从数据到决策的链条，在关键领域优势显著 。
```

* * *

**产品不是设计出来的，是“战地经验”堆出来的复利**

**提到企业软件产品，多数人会想到“需求调研-产品设计-研发落地”的标准化流程，但Palantir 的起点却完全不同——它的产品体系，是工程师在客户现场“摸爬滚打”出来的“经验结晶”，本质是一场持续十余年的“项目交付复利”。**

![640-42](https://www.smartcity.team/wp-content/uploads/2025/10/640-42.png)

2016年的 Palantir，更像一家“带着代码的咨询公司”：前线部署工程师（FDEs）每周3-4天驻扎在客户办公室，从制造工厂的生产线到医疗机构的病房，从情报机构的数据分析室到航空航天的研发中心，亲手帮客户解决最具体的问题。为了整合SAP的数据，他们手动编写大量ETL脚本；为了让客户看懂数据，他们临时开发可视化工具；为了快速搭建应用，他们又琢磨出简易的UI组件。 这些看似“定制化”的琐碎工作，恰恰成了产品复利的起点。当FDEs在不同客户现场遇到重复的痛点——“都需要导入外部数据”“都需要可视化分析”“都需要快速搭应用”，核心产品团队（PD）便将这些“定制解决方案”提炼成标准化工具：数据导入用Magritte，可视化用Contour，搭应用用Workshop。 久而久之，这些工具围绕“整合数据并使其有用”的核心，汇聚成了如今支撑Palantir半壁江山的Foundry平台。

![640-41](https://www.smartcity.team/wp-content/uploads/2025/10/640-41.png)

没有凭空的产品设计，只有对“战地问题”的反复解决与沉淀——这就是Palantir产品体系的复利逻辑：每一个项目都是一次经验积累，每一次积累都为下一个产品模块铺路，最终从“定制服务”蜕变为“平台化产品”，实现从“0到1”再到“1到N”的突破。

* * *

从“定制经验”到“模块化体系”

当“战地经验”被反复提炼、抽象为标准化工具后，Palantir并未止步于单一平台的搭建，而是进一步将核心能力拆解为一个个可灵活组合的“APP”，最终形成Foundry、Gotham、Apollo、AIP四大产品平台。这四大平台并非孤立的“重型软件”，而是以“ **解决具体场景问题**”为核心的“ **APP** **集合体**”——每个平台都围绕特定业务目标，整合了一系列功能明确、可按需调用的APP，既满足不同客户的个性化需求，又保持了体系的协同性与扩展性。 这种“平台+APP”的架构，本质是对客户需求的深度适配：政府客户需要精准的情报分析工具，金融客户需要高效的交易风险监测模块，制造客户需要灵活的生产数据可视化应用，而APP化设计让Palantir能快速调取对应功能，无需为每个客户“从零开发”。

**从具体平台的APP构成来看，各模块的功能定位清晰且互补**

- Foundry：作为面向商业客户的核心，其APP矩阵聚焦“数据价值落地”，涵盖从数据处理到应用开发的全流程。例如，数据整合环节有“Pipeline Builder”“HyperAuto V2”等APP，可自动化完成数据导入、清洗与转换。

![640-53](https://www.smartcity.team/wp-content/uploads/2025/10/640-53.jpeg)

分析环节有“Contour”（点击式表格分析）、“Quiver”（时间序列可视化）、“Code Workbook”（高级代码笔记本）等工具，满足从非技术人员到数据科学家的不同分析需求。

![640-43](https://www.smartcity.team/wp-content/uploads/2025/10/640-43.png)

应用开发环节则有“Workshop”（低代码互动应用搭建）、“Slate”（拖放式响应式应用设计）、“Automate”（流程自动化）等APP，让企业无需专业开发团队，也能快速搭建贴合业务的运营应用。

![640-44](https://www.smartcity.team/wp-content/uploads/2025/10/640-44.png)

此外，“Ontology Manager”（本体管理）“Object Explorer”（对象集搜索分析）“Object Views”（对象浏览挖掘）等本体相关APP，还能帮助用户直观查看数据关联、监控关键业务实体动态，让数据始终与业务逻辑紧密绑定。

![640-45](https://www.smartcity.team/wp-content/uploads/2025/10/640-45.png)

- Gotham：针对情报、国防等复杂场景，其APP模块更侧重“深度关联分析与决策支持”。例如，“链接分析APP”可挖掘人员、地点、事件间的隐藏关系，助力锁定情报线索。

![640-46](https://www.smartcity.team/wp-content/uploads/2025/10/640-46.png)

“地理空间可视化APP”能将多源数据叠加到地图上，直观呈现战场态势或区域风险；“时间轴分析APP”可梳理事件发生顺序，还原案件脉络或战场动态；再搭配“协作工具APP”，支持多部门实时共享分析结果，让决策效率大幅提升，俄乌战争中乌军对战场决策的优化，正是依托这些APP的协同应用。

- Apollo：作为“调度中枢”，其APP体系聚焦“跨环境一致性管理”，核心功能通过轻量化模块实现。例如，“Control Panel”（控制面板APP）可统一管理不同部署环境的版本更新；“资源管理APP”能实时监控服务器、存储等硬件资源占用情况；“安全审计APP”则记录所有部署操作，确保涉密环境下的合规性。这些APP共同支撑了“一次构建，随处部署”的能力，让Palantir产品既能在公有云运行，也能适配企业私有云、甚至离线涉密网络。

-  AIP：作为AI技术的“放大器”，其APP设计围绕“AI与业务流程的融合”展开。“AIP Logic”可编排大模型与本体数据的联动逻辑，让AI理解业务上下文。

![640-48](https://www.smartcity.team/wp-content/uploads/2025/10/640-48.png)

“AIP Assist”能嵌入到Foundry、Gotham的各类应用中，通过自然语言交互帮助用户快速调取数据或分析工具；“AIP Agent Studio”则支持自定义AI代理，满足特定场景的自动化决策需求。更关键的是，这些AI APP并非独立运行，而是能直接调用Foundry的数据源、Gotham的分析模型，让AI能力真正融入业务闭环，而非“悬浮的技术工具”。

* * *

**不是单一产品，而是“AI Mesh”协同闭环**

若只看Foundry、Gotham这些单个产品，或许有人会觉得Palantir与其他企业软件公司并无本质区别。但真正让它在国防、金融、医疗等关键领域难以被替代的，是其背后一套被称为“AI Mesh”的协同作战体系——四大核心组件环环相扣，构筑了从数据底层到决策顶层的完整闭环，这才是Palantir最深的技术护城河。

**四大组件各守其位，又无缝协同。** Palantir的“AI Mesh”体系以四大核心平台为支柱，每个平台都有明确的定位，却又能打破数据与功能的壁垒，形成协同效应。

- Foundry作为数据整合“地基”，打破“数据孤岛”形成统一数据资产库。

- Gotham担当复杂场景“数据大脑”，挖掘数据隐性关联以支撑情报分析、战场指挥等决策。

- Apollo作为“调度中枢”，实现跨环境统一版本管理与运维。

- AIP则是AI能力“放大器”，将大模型与数据源、决策逻辑结合并融入业务流程，四者环环相扣，共同构成从数据底层到决策顶层的完整支撑链条。

![640-47](https://www.smartcity.team/wp-content/uploads/2025/10/640-47.png)

* * *

Palantir的故事或许印证了一个道理：真正有生命力的产品体系，从来不是规划出来的，而是在解决真实问题的过程中“长”出来的；真正的技术壁垒，也不是某一个“黑科技”，而是能将数据、分析、决策、部署拧成一股绳的“协同能力”。 对于想要在复杂领域突围的企业而言，Palantir的启示或许是：与其纠结“如何设计完美产品”，不如先走进客户的“战场”；与其追求“单点技术领先”，不如先搭建“全链条的协同体系”——毕竟，能解决真问题的体系，才是最坚固的壁垒。

* * *

# ![20efb41964068abf05690e91ccbb0aca](https://www.smartcity.team/wp-content/uploads/2025/10/20efb41964068abf05690e91ccbb0aca.png)

**以下来源：公众号（数据人杰森、四时研选）**

# 一、5000字拆解 Palantir 产品与本体论

1. Palantir公司历史回顾
2. 产品矩阵概览
3. 本体论是什么，是独创的吗
4. 是个不折不扣的BI平台
5. 分析与业务动作的联合
6. 对AI的拥抱与FOMO

![640-26](https://www.smartcity.team/wp-content/uploads/2025/10/640-26.png)

Palantir 核心产品 Foundry 中 Ontology 模块

近期本体论一词有点火，本文也来尝试讨论下这个概念以及Palantir公司（以下简称PLTR）基于这个理论构建的数据产品Foundry。

![640-30](https://www.smartcity.team/wp-content/uploads/2025/10/640-30.png)

Palantir数据中台一词在微信指数里的趋势 2024.9 – 2025.9

## 公司历史与股市表现

PLTR ，一家美国公司，成立于2003年（距今22年），早期为政府单位提供大数据解决方案，后期也面向商业企业提供服务，涵盖国防、安全、金融、医疗等领域。 创始人是PayPal黑帮成员之一的彼得·蒂尔。

Palantir 这个名称来源于 J.R.R. 托尔金奇幻史诗巨著《魔戒》中的神奇物品——真知晶球。这是一个人为创造的词汇，大致意为“远见之物”或“能望远者”。

公司2020年上市，2024年度营收在28亿美元规模，人均产值70万美元（公开信息显示员工数量在4000左右），对应的利润为10亿美元左右，当前市盈率（TTM口径）是551。同期Salesforce 跟微软的市盈率分别是34、37。

## 产品功能矩阵概览

PLTR核心产品包括面向商业客户的 **Foundry 平台** 和面向政府客户的 Gotham 平台。官网公开的产品资料主要是Foundry 产品，因此本文的关注重点也是这个产品。

Foundry一词是铸造场的意思。单从名称上看，跟微软的Data Factory 就有一些接近。 在我们翻阅完其200+帮助中心文档后，我们认为这是一个带着一对翅膀的数据中台。

- 左翅膀：在数据分析看板中支持调用外部系统API，实现看数与决策执行的链路联通。
- 右翅膀：更灵活、低门槛的页面定制能力。 比如去修改可视化展现的方式，去定义一个专题的小型业务系统，比如选址。

![640-31](https://www.smartcity.team/wp-content/uploads/2025/10/640-31.png)

Foundry 产品核心模块能力

**20年的项目积累使得Foundry成为一个包罗万象的数据产品套件。**

- Data Connectivity & Integration： 数据连接、集成、处理模块，就是传统的ETL概念；也支持实时数据的接入。支持对接近160多种数据库；为了满足客户需求，还专门开发了与SAP对接的插件。数据存储用了HDFS作为解决方案。 这些处理好的数据，也支持被PowerBI、Tableau进行消费。
- Ontology 本体论： 数字孪生模块，支持基于各类业务系统中的数据表构建逻辑模型，实现与真实世界各类物体（比如机场、航班）、事件（比如航班、延误预警）一一对应。
- Analytic ：分析模块，与常规的BI分析基本一致，也做出了相应的特色，比如支持业务流的展现，与业务系统的一键协同。
- AI Platform：包含基础的AI能力，实现机器学习、预测、策略优化等能力；大模型兴起之后，也新增了各类模型的对接部署、监控、调用能力。
- Market Place ： 应用市场能力，快速获取开箱即用的模板，减少交付实施成本。 也支持一些集团型公司向子公司快速传递数据处理、数据展现资源包。
- Developer Toolchain： 开发者工具链，看名称就不一般。 正是基于此项能力，实现应用层的 Operation 能力，从看数到执行（数据回写Write Back）。
- Security & Governance：安全管控能力，企业级数据软件的必选项。

当然20年的发展历程中也会有些产品模块被淘汰，PLTR也不是一直在做正确的事情：） 有些早期推出的产品模块，也进入了维护期，不再更新。比如报告Report功能（应该是被仪表盘功能取代了），表单填报功能。

## 本体论 Ontology是什么

> Ontology, build and manage your organization’s digital twin.

Palantir Ontology 定位为组织的操作层。Ontology 位于集成到Palantir平台中的数字资产（数据集和模型）之上，并将它们与真实世界的对应物连接起来，从工厂、设备、产品等物理资产到客户订单或金融交易等概念。在许多情况下，Ontology 充当组织的数字孪生体，包含启用各种应用案例所需的语义元素（objects、属性、链接）和动态元素（操作、函数、动态安全机制）。

### 实现真实世界的数字化建模

Ontology具体做了什么事情？ 我们结合航班延误这个场景举例。

- 定义实体类型 Obejct Type
  - 如机场、航班、航线、航空器、延误这些实体
  - 对应数据表里的一行就是 Object 的实例
- 定义Object 的属性
  - 比如机场的名称，机场的缩写，容量大小
- 定义实体类型之间的关系
  - 如一个机场每一天都有很多航班
- 定义实体类型的可操作类型
  - 如可以修改某个航班的执行飞行器（换飞机），修改某个预警事件的严重等级。

这些实体的背后都跟实际的数据一一对应。

![640-27](https://www.smartcity.team/wp-content/uploads/2025/10/640-27.png)

Ontology 建模示例

### 更业务化的数据展现方式

工具型软件产品如何体现业务价值，Foundry提供了一些思路。

#### 维度属性与关系展现

传统的分析系统仅仅考虑了数据表数据的展现，却缺少业务视角的呈现。比如BI产品的可视化类型里有指标卡，可以展现一个总收入；但是基本没有维度属性卡这样的概念，用来展示文本类的信息。比如想展示一个店铺的基础信息， 解决方案可能只有表格； 或者用体验糟糕的方式来拼接出一个文本。

![640-28](https://www.smartcity.team/wp-content/uploads/2025/10/640-28.png)

PLTR Ontology 中对于一个机场的信息展示页面

#### 基于业务流展现数据

如果说Ontology是基于技术视角来描述企业，那么子模块Vertex就是基于Ontology中定义的实体来做业务化呈现。他可以把多个有关系的实体进行串联，用业务流程的思路来进行展现。比如一个机场有对应的航班，能显示航班的状态，并根据配置的阈值进行预警。

对比之下传统的数据平台通常提供的是基于技术视角的数据血缘能力。

![640-29](https://www.smartcity.team/wp-content/uploads/2025/10/640-29.png)

Vertex 功能示例： 机场航班案例

![640-32](https://www.smartcity.team/wp-content/uploads/2025/10/640-32.png)

Vertex 功能示例：电池生产线， 支持查看某设备传感器的温度。

杰森认为这其实应该是业务系统要做的事情？ 比如钢铁生产监控软件，应该默认就包含这些？或许这些老旧的软件的可定制，二次开发能力太弱，以至于后起之秀有了可乘之机。

### 本体论的独创性探讨

有一篇文章提到PLTR的护城河是Ontology（本体论）。 PLTR当下的影响力最强，他们自然而然地成为这个理论的布道者。 如果说产品能力是数字1，那么这个理论就是后面的1个0或者2个0， 也是他们获取超额项目收益的原因所在。

数据行业的长期从业者（有一些喜欢自称数据老兵）大概率不会认为这个本体论是PLTR的原创。成立于1990年之前，在2000年前就上市的独立数据分析软件厂商MicroStrategy（目前也是一家很火的公司，因为他们核心商业模式已经转型到比特币）产品中也践行了这些理念。在他们的设想中，不同环节做不同的事情。

– 业务系统 Source System：把真实世界的业务数字化

– 数据仓库 Data Warehouse： 把业务系统数据处理干净

– 分析系统 BI ：把多个可信赖的数仓数据关联，破除数据孤岛，能够呈现一个单一实体的完整面貌。

在MicroStrategy数据产品中，也支持实体的定义，实体属性的定义、实体之间关系的定义；基于这些定义可以快速在仪表盘上进行数据呈现，之类各类粒度的聚合关联。

![640-33](https://www.smartcity.team/wp-content/uploads/2025/10/640-33.png)

MicroStrategy产品的本体论实践

很巧合的是这两家公司 都挺喜欢用机场、航班这些案例。 或许是搞ToB的人经常飞来飞去，对这个场景最为熟悉，哈哈。

## 不折不扣的分析与展现系统

之所以说Foundry是个不折不扣的分析与展现系统，是因为他足足提供了5款分析工具。

### Quiver

- 支持对Object对象（也就是Ontology建模的劳动成果）与关系进行可视化展现。
- 把基于时间序列的分析做了“提级”，用户体验上会更好，比如预置累计计算、窗口计算能力。
- 提供画布Canvas 与 图形 Graph两种模式，前者就是我们常见的仪表盘；后者更像是一个分析树。

![640-35](https://www.smartcity.team/wp-content/uploads/2025/10/640-35.png)

分析功能Quiver 示例

![640-34](https://www.smartcity.team/wp-content/uploads/2025/10/640-34.png)

Quiver 时间序列分析

### Code Workspaces 代码工作簿

类似Jupyter notebook ，主要用Python来处理、展示数据，并支持处理流的编排。

### Notepad 记事本

是一个富文本编辑器，支持载入其他 Foundry 应用程序的输出结果，如 Contour、Quiver、Code Workbook 和 Object Explorer（建模对象的详情页面）。

![640-34](https://www.smartcity.team/wp-content/uploads/2025/10/640-34.png)

### Fusion

一个以电子表格为驱动的应用，将表格计算与Foundry的Ontology和Object驱动查询系统的强大功能相结合。Excel 是如此的强大，以至于经常得到各种下一代产品都还需要致敬。

### Contour

支持基于表进行数据分析，不一定使用到 Ontology的建模结果（比如是临时导入的Excel分析） ； 也包含相应的数据清理能力（比如合并，过滤等）。

对于更灵活的分析展示需求， Foundry提供了Slate 产品能力 。 开发者可以使用 CSS 自定义应用的风格，更灵活响应个性化的展示需求。按官网介绍，基于 Slate，用户所看到的一切都可以更改，从画布的背景颜色到按钮的字体和边框半径。

其他自动化推送、预警功能作为商业智能软件的基础功能，也没有例外地出现在Foundry产品中。

## 分析与业务动作的联动

> Supercharge your business intelligence (BI) and analytics ecosystem with dynamic, decision-making workflows. Palantir Foundry ensures that your user applications can scale without fracturing your core data and model foundation.

在分析仪表盘功能Quiver中，还支持按钮能力，支持与业务系统的联动。 按钮支持两种模式，分别是 write back 跟 side effect， 前者会等待回写状态，而side effect只是推送一个消息。

关于与业务系统的联动，曾经也有个蛮流行的概念，是反向ETL，就是在数据处理类产品中，支持把数据再回传到业务系统，或者直接利用API去修改业务系统的数据。不少产品提供的解决方案是数据同步，这真的是一个过于技术化的解决方案了。

如果是更复杂的数据展现与业务流程整合需求，就需要借助Workshop模块。这是在Foundry产品中一个灵活的面向对象的应用程序搭建工具，支持将对象、链接和操作编织成用户驱动的工作流，远远超越了仪表盘或被动可视化。

![640-36](https://www.smartcity.team/wp-content/uploads/2025/10/640-36.png)

上图是一个航班预警页面，既有分析看板，也有业务操作流程，比如提升某个预警等级或者降低预警等级。

正是基于Workshop能力，Foundry可以帮助客户快速落地一些专业的数据类产品，比如供应链优化、门店选址等能力；相比单独的分析看板，也能够让数据项目的价值放大，获取高额的商业回报。

### 为什么PLTR没有把手伸进业务系统

定义实体、实体之间的关系并不难，基础的分析系统并不难，难的是面对灵活多变分析需求，后台服务能准确从相应数据源取数并完成计算。

PLTR做了这么多难的事情，为什么没有深入到业务系统的建设中？

或许因为数据系统与业务系统还是存在差异，两者共同点是对实体的清晰定义，而业务系统还需要处理各类规则与策略。 如果要再做一个SAP，他可能还需要20年时间。 这大概也是阿里云这样的厂商降低所谓业务中台优先级的原因。当然如果他做业务系统，应该也是从本体论出发，现有逻辑概念，然后再落地业务系统。

AI时代，大模型具备了Tool Use能力，有能力连接所有数字化工具，完成真实世界里的任务。但是业务系统价值还会继续存在，业务系统中配置的所有限制规则，多人审批策略是 **智能体破坏真实世界前的一道防线**。即使未来AI可以创建业务系统或者智能体Agent本身就是业务系统，但被发现他无法满足人类期待时，他还是会被修正、优化或者推倒重来。

![640-37](https://www.smartcity.team/wp-content/uploads/2025/10/640-37.png)

认证过的Software 是保护真实世界的一道防线

## 对AI的拥抱与FOMO

PLTR早期产品模块里就支持经典的AI功能，包括机器学习、预测与优化等。传言 Palantir 还是当年美军抓本拉登的得力干将。 他通过分析海量的卫星图像，发现在深山的废弃屋舍旁出现了人类垃圾，判断本拉登可能藏匿于此，美军因此得以抓捕本拉登。这里应用的能力是对图片数据的处理与解读，并不是经典的数据分析产品的功能边界。

随着大语言模型的繁荣， 在Foundry诸多产品模块里都支持了大模型帮助用户决策，并提供用户Review后执行相关动作的能力。 比如下图演示了一个供应链管理场景中的调拨策略建议，正等待用户确认。

![640-38](https://www.smartcity.team/wp-content/uploads/2025/10/640-38.png)

Foundry产品中的智能应用——供应链库存调拨

当然这个能力背后需要前置对应的提示词。

![640-39](https://www.smartcity.team/wp-content/uploads/2025/10/640-39.png)

Foundry AIP功能中的提示词示例

能感觉到 PLTR 对于 LLM 跟其他软件厂商一样，都是FOMO的心态，担心错失这样几十年一遇的风口，甚至都上线了跟传统意义理解的数据没有直接关系的功能。

比如AI Thread 功能，该功能支持从一堆PDF里获取洞察，找到答案。 实际应用场景包括从设备技术手册与指南快速查询答案、快速提取并总结情报简报中的关键信息、总结和解读立法文本和政策文件。这类功能与本体论关系目前没有足够信息判断，或许Ontology里的配置可以作为一种知识库成为LLM的输入。

可能也没其他更多可以创新、可以探索的领域，LLM在Foundry产品中也是“无孔不入”。比如在文档型分析报告里，就支持自动进行拼写检查、缩短、修改或翻译文本，同时保留其现有格式。

### Palantir 对于ChatBI的投入

同期Tableau、PowerBI都推出了ChatBI相关功能。可能是自己搜索能力不强，目前没有捕捉到Foundry产品中有类似的功能，期待捕捉到这块信息的读者可以协助纠正。

## 总结

PLTR在传统的BI类、数据开发类产品中提供了两大差异化的能力，值得数据行业从业者的关注。

- **数据分析看板中支持调用外部系统的能力**，实现了看数系统与业务系统的联动，使得数据不再割裂之外，业务流也不再割裂。
- **灵活低门槛的页面定制能力**，是其获得商业化成功（虽然才上市2年，我们姑且称之为成功哈）的一个有利保障；能够实现深度定制化需求的可控成本的交付。

**大而全的产品套件模式还将继续**，包括Palantir的Foundry产品，微软的Data Factory、Databricks 商业化产品套件走的都是这个模式。

**数据中台还重要吗**？杰森认为是的。AI要进入到一个更高的阶段，就更需要直接从物理世界获取更全面、更原始的数据。让AI能更准确地去理解数据，去理解数据背后的真实物理世界。

逻辑层的重要性还是存在。 当一堆系统出现时，而且发现整合不动的时候，更上一层的系统来做逻辑化的建模时机也就到来了。比如出现支付聚合功能，聚合打车功能，这个在AI、LLM时代大概率也会出现，让我们拭目以待。

![640-40](https://www.smartcity.team/wp-content/uploads/2025/10/640-40.png)

通过逻辑层，把繁杂的系统之间交互关系进行简化

衍生阅读：Nabeel S. Qureshi，2015-2023年任职于 Palantir，原文写于2024年10月

# 二、关于 Palantir 的一些思考

原创Qureshi四时研选

_2025年07月17日 11:41_ _广东_

Palantir 纳入标普500指数之后，股价一路飙升，目前市值已超过3500亿美元。风投们也追着前 Palantir 员工，希望能参与他们创办的新公司。

但对于在 Palantir 工作多年、或是已离职的老员工来说，这种热度显得十分怪异。尤其是在 2016 年到 2020 年期间，说你在 Palantir 工作，常常会被人侧目。那时候，外界普遍将 Palantir 看作是间谍科技、NSA 监控的同路人，甚至更糟。公司门口时常有人抗议。即使是那些在道德上并不反对的人，也常常把 Palantir 视为一家假装是软件公司的咨询公司，或者最多也不过是某种精致的“人才套利”机构。

关于 Palantir 这家公司，有太多外人不理解的地方。以下是一位在 Palantir 工作了八年的前员工撰写的回顾。他从亲历者的角度出发，揭示了这家神秘的硅谷公司不为外界所熟知的一面，内容坦率而深刻，值得一读。

## （一）我为什么加入 Palantir

我是在 2015 年夏天加入 Palantir 的，起初是在刚开设的伦敦办公室，后来搬到了硅谷，最终又去了华盛顿特区，担任前线部署工程师（forward deployed engineer）。当时公司大约有1500人，在帕洛阿尔托（总部）、纽约、伦敦和其他几个城市设有办公室。（如今员工数大约4000，总部也迁到了丹佛。）

**我为什么选择加入？**

首先，我想在“难搞”的行业解决真正有意义的问题。我的兴趣领域——出于个人原因——是医疗保健和生物技术，公司在这方面刚刚起步。公司当时声称要进入医疗、航空航天、制造业、网络安全等行业——这些我认为都极为重要，但当时很少有人愿意涉足。那会儿最热门的还是社交网络（Facebook、LinkedIn、Quora 等）和各种消费级应用（Dropbox、Uber、Airbnb），真正愿意面对经济中那些棘手领域的公司少之又少。如果你既想解决这些“硬问题”，又想保有硅谷那种工作文化，当时你几乎只能选择 Palantir。

我的目标是以后自己创业，但在那之前，我希望（1）能在某个行业深入工作一段时间，真正学到些东西；（2）能进入一家美国公司，通过工作拿到绿卡。Palantir 正好满足这两个条件，这就让选择变得很简单。

其次，是人才密度。我当时和几位医疗领域的早期负责人聊过，印象非常深刻。之后又与好几个早期做业务运营和战略的员工交谈过，更是被震撼到了。他们是那种非常强烈、极具竞争心的人，真正的信仰者；是那种奇特而迷人、会在空闲时读哲学、尝试奇怪饮食、为乐趣骑行100英里的人。这种文化，其实是从 PayPal 帮派那里传承下来的。曾在 PayPal 担任早期员工的 Yishan Wong 写过一篇关于“强度”的重要性的文章：

“总体来看，当我开始接触更多创业公司时，我发现 PayPal 的人才水平在硅谷初创公司中并不罕见，但真正的区别可能在于其高层所展现出的那种强度：Peter Thiel 和 Max Levchin 都是极具强度的人——极度好胜、工作极其努力、从不接受失败。我认为，正是这种领导力，能推动一支‘标准’的优秀团队实现非凡的成就，并由此孕育出后续源源不断的成功。”

Palantir 是一个异常“高强度”且古怪的地方。我记得第一次和 Stephen Cohen 交谈时，他办公室的空调设定在华氏60度（约摄氏15.5度），屋里放着几个奇形怪状的设备，用来减少空气中的二氧化碳含量，桌上还放着一大杯冰块。在整个谈话过程中，他一直在嚼冰块。（据说这样对认知能力有好处。）

公司CEO Alex Karp 面试了我，我还与其他领导团队成员交流过。大概不用我多说你也能相信 Karp 有多怪——只要去看一场他的采访就知道了。我不能透露我们具体谈了什么，但他在 2012 年一次采访中展现出的风格，足以让你感受到他的特质：

“我喜欢在对候选人一无所知的情况下见他们：没有简历、没有预先交流、也没有职位描述，就只是我和候选人坐在一个房间里。我会问一个相当随机的问题，那种和他们在 Palantir 实际工作毫无关联的问题。然后我观察他们是如何拆解这个问题的，看他们是否能意识到同一件事可以有很多种不同的理解方式。我喜欢把面试控制在10分钟左右。否则，人们就会进入他们预设好的应答模式，你也就无法真正了解他们是什么样的人了。”

我的面试往往完全与工作或软件无关——有一次我们整整聊了一个小时的维特根斯坦。要知道，Peter Thiel 和 Alex Karp 都是哲学专业出身。当时 Thiel 的讲义刚刚流出，他们讨论莎士比亚、托尔斯泰、吉拉尔（那时还鲜为人知，如今几乎成了陈词滥调）等等。

这种“思想上的宏大”与“极度好胜”的结合对我来说简直是绝配。直到今天，这种氛围仍然很难找到——许多公司模仿了那种“铁血”工作文化，营造出“我们就是科技界的海军陆战队”那种感觉，但真正拥有浓厚思想氛围、能让你参与到一整套深刻理念中的地方却屈指可数。这种氛围是无法“演”的——创始人和早期员工必须是真正有思想、有趣的人。

现在能让我想到、成功兼具这两种特质的公司，主要是 OpenAI 和 Anthropic。它们能吸引顶尖人才，也就毫不意外了。

## （二）前线部署

我加入时，Palantir 的工程师大致分为两类：

1、与客户一线共事的工程师，通常被称为 FDE（前线部署工程师，Forward Deployed Engineers）。

2、在核心产品团队工作的工程师（产品开发，简称 PD），他们很少直接去客户现场。

FDE 通常被要求每周有 3-4 天在客户现场办公，也就是“驻场”，这意味着要频繁出差。对于一家硅谷公司来说，这种工作模式在当时（甚至现在）都非常罕见。

这种模式值得深入探讨，但核心理念是：你必须深入了解某些“困难行业”（比如制造、医疗、情报、航空航天等）中的业务流程，然后基于这种深度理解去设计真正解决问题的软件。接着，PD 工程师会将 FDE 所构建的内容“产品化”，更广义上说，他们会开发出能够帮助 FDE 更高效、更快速开展工作的工具型软件。

Foundry 产品的很多早期形态，就是这样逐步构建起来的：FDE 去客户现场，需要手动完成大量繁杂低效的工作；PD 工程师随后开发出工具，将这些“苦工”自动化。

比如：需要从 SAP 或 AWS 导入数据？用 Magritte（一个数据导入工具）。需要可视化数据？用 Contour（一个点选式的数据可视化工具）。需要快速搭建一个 Web 应用？用 Workshop（一个类似 Retool 的网页应用搭建工具）。

最终，公司围绕“整合数据并使其真正发挥作用”这一宽泛主题，打造出一套非常强大的工具组合。

当时，把这些工具开放给客户使用被认为是一个非常激进的举措——它们其实还没准备好给外人用。但如今，这部分业务已经贡献了公司超过50%的收入，并被命名为 Foundry。从这个角度看，Palantir 实现了一个非常罕见的从“服务公司 → 产品公司”的转型。2016 年时，说它是一家硅谷的服务型公司，其实并不算错；但到了 2024 年，再这么说就完全不准确了。因为公司成功打造出了一套企业级数据平台——这正是早期服务经验转化而来的成果。这种转变也直接体现在毛利率上：2023 年，Palantir 的毛利率高达 80%，这是真正意义上的“软件公司毛利率”。对比一下埃森哲（Accenture），它的毛利率只有 32%。

经济学家 Tyler Cowen 有一句非常精彩的话：“真正稀缺的，是信息背后的语境与洞察（Context is that which is scarce）。”这可以说是 Palantir 模式的根本洞见所在。亲自去客户现场——创业教父 Steve Blank 称之为“走出办公室”（get out of the building）——意味着你能获得他们工作方式中难以言传的隐性知识，而不是企业软件通常所依赖的那种平铺直叙的“需求清单”模式。

Palantir 对此信念到了夸张的程度：时常会接到电话，被要求第二天一早就飞去一个完全陌生的地方。“先上飞机，再问问题”成了公司的文化偏好。这也导致公司长期内差旅开支失控——我们中很多人都成了 United 1K 之类的高级旅客——但也正是这种模式，带来了长达十年的密集学习循环，最终产生了丰厚回报。

我参与的第一个真正客户项目是法国的飞机制造商空中客车（Airbus）。我搬到图卢兹，在他们工厂里跟制造团队一起工作了一年，每周四天，帮助他们定制并部署我们的软件版本。

刚到图卢兹的第一个月，我周末都没法离开这座城市，因为法国空管人员每个周末都罢工。欢迎来到法国（笑）。不过说真的，法国是个好地方，而且空客的飞机确实令人惊叹。这是一家真正以工程为核心的公司。CEO 通常都是航空工程背景出身，而不是 MBA。不像……咳，总之你懂的。

当时空客 CEO 告诉我们，他最大的问题是 A350 机型的产能扩张。于是我们着手开发软件，直接应对这个挑战。我有时候会把它描述为：“造飞机的 Asana”。你要把各种分散的数据源——工单、缺件、质量问题（称为“non-conformities”，即不合规项）——整合在一个清晰的界面中，用户可以勾选任务、查看其他团队在做什么、零件在哪里、进度如何等等。同时，还能搜索（包括模糊/语义搜索）过往的质量问题及其解决方法。

这些功能在软件世界看似基础，但你知道企业软件通常有多糟糕——哪怕只是把这些“最佳实践”的用户界面部署到现实场景中，其影响力也是巨大的。最终，这套系统成功地推动了 A350 的产能提升，实现了 4 倍速增长，同时仍然保持了空客一贯的高质量标准。

这也导致我们开发的软件很难用一句话概括清楚——它不只是一个数据库，也不是个电子表格，而是一个从头到尾解决特定问题的系统，至于能不能推广、是否通用，完全无所谓。你的任务就是把问题解决掉，不用担心“过拟合”；而 PD 工程师的任务，则是把你写的东西进行抽象和产品化，以便未来能在别的客户那里推广使用。

FDE 写的代码以“能跑起来”为目标，讲得委婉一点，就是——会有技术债，也常常会采用临时性或“土法上马”的方案。PD 工程师则写的是那种可扩展性强、适用于多种场景、稳定性高的软件。

Palantir 的一个关键“秘密”是：真正创造持久的企业级价值，需要这两类工程能力同时存在。

FDE（也有人称 BD 工程师）通常具备非常强的“抗压能力”以及嵌入客户组织的社交和政治技巧，能赢得客户信任，同时还有极高的执行速度——你需要在非常短的时间内做出一个“有价值的雏形”，让客户意识到：“哦，这是真的有用的。”

这在当时非常占优势，因为大多数客户对软件外包团队的期待几乎可以说是“笑话级别”的低。他们习惯了 SAP 那种“实施时间按年计算”的瀑布式流程，而外包团队往往只是“安装工”和“培训讲师”。

所以当一群二十几岁的年轻人出现在客户现场，两周内就做出了一个能真正用起来的产品，客户自然会刮目相看。

这种“前线快速打样 \+ 后台系统抽象”的双螺旋模式，构成了 Palantir 强大产品引擎的基础。

客户团队通常很小（4-5人），运转高效、相对自治；同时这样的团队有很多，每个都在快速学习，而核心产品团队的任务就是把这些一线实践提炼出来，构建统一的主平台。

当我们被允许进入一个组织内部工作时，这种模式往往效果很好。障碍主要来自政治因素。每次看到政府又给德勤（Deloitte）一个价值1.1亿美元的合同去开发一个最终无法运行的网站，或者像 healthcare.gov（美国联邦医保网站）那样的灾难性失败，或者旧金山学区（SFUSD）花了4000万美元上线一个照样运行不了的薪资系统时，你看到的其实是：内部政治压倒了实质能力。

你可以再看看 SpaceX 和 NASA 的对比，性质也是一样的。

这个世界需要更多像 SpaceX 和 Palantir这样的公司——它们靠执行力脱颖而出，靠实现目标取胜，而不是靠玩政治游戏、堆砌无用的点状方案来混淆成果。

## （三）隐秘的价值

FDE（前线部署工程师）做的另一件核心工作叫做数据集成（data integration），这个词乍听之下无聊至极，能让人立刻昏昏欲睡。但这件事在当时（乃至现在）都是 Palantir 的核心所在，多年来被外界严重低估。

直到 AI 的兴起，大家才开始逐渐意识到：对于企业来说，拥有干净、结构化、易访问的数据，有多么重要。

用简单的话说，数据集成就是指：(a) 获取企业数据的访问权限，这通常需要和组织内的“数据拥有者”谈判；(b) 对数据进行清洗、转换，使其真正可用；(c) 将数据存放在一个所有人都能访问、使用的地方。

Palantir 主打平台 Foundry 中的大量底层基础软件，其实就是用来让这一流程变得更快、更易操作的工具链。

**那为什么数据集成这么难？**

一方面，是数据格式极为混乱、不适合计算机直接读取：PDF、实验记录本、Excel 表（天哪，真的有无数Excel文件）……格式五花八门。

**但真正的阻碍，其实是组织内部的政治问题：**

某个团队或部门控制着一个关键的数据源，而这个“看门人”角色就是他们存在的根本理由。他们之所以能在企业中维持地位，就是因为自己是这份数据的“唯一通道”，甚至还靠着提供一些分析报告来证明自己的不可替代性。

这种组织内斗常常是最大的阻力，有时还会带来令人哭笑不得的后果——比如一个客户花钱买了一个 8~ 12 周的试点项目，结果我们前 8~11 周都花在争取数据访问权限上，最后一周才匆忙赶出一个能演示的原型系统。

Palantir 早期意识到的另一个“秘诀”是：数据访问的争执有一部分确实是出于真实的数据安全顾虑，而这些问题是可以通过在数据集成层内置安全控制机制来缓解的——覆盖平台的各个层级。这包括基于角色的访问控制、行级策略、安全标记、审计追踪，以及其他许多数据安全功能，而这些功能，许多公司到现在还在努力赶上。

也正因为这些安全机制，Palantir 的系统往往使公司的数据更安全，而不是更不安全。

## （四）关于公司文化的一些注解

整体来说，Palantir 的氛围更像是一个带有救世使命感的“理想主义小教派”，而不是一家传统的软件公司。

但非常重要的一点是，这家公司高度包容甚至鼓励批评——有人给我看过一封邮件，内容是一位入职不久的初级工程师，正在和一位公司董事激烈争论，而且整封邮件被抄送给了全公司（当时约一千人）。

作为一个“理性主义脑袋”的哲学专业出身者，这一点对我来说意义重大——我不是来加入一个盲目崇拜、不能质疑的组织的。

但如果这是一个由持怀疑态度、关心世界走向、愿意就“软件在世界中的意义”展开存在主义式辩论的人所组成的组织——那就很吸引我了。

我不确定现在是否还这样做，但当时新员工入职时，公司会送你一套书：《Impro》（《即兴表演》）、《The Looming Tower》（《通向“9·11”之路》，一本关于 9·11 的书）、《Interviewing Users》（《用户访谈》）、《Getting Things Done》（《搞定》），我还收到了一份早期PDF版的Ray Dalio（瑞·达利欧）的《原则》。

这套书定下了公司的基调。

《The Looming Tower》很容易理解——公司在某种程度上是为了回应 9/11 而创立的，而 Peter Thiel 认为，9/11 之后对公民自由的侵蚀是不可避免的，所以这本书提供了重要的历史背景。

但——为什么会送《Impro》呢？

要成为一名优秀的 FDE（前线部署工程师），你必须具备一种对社交语境极其敏锐的感知能力。你的真正任务，是与企业（或政府）高层建立合作关系并赢得他们的信任，而这通常意味着你必须会“玩政治”。

《Impro》在极客群体中之所以受欢迎，部分原因正是它把社交行为拆解得像机制一样清晰可分析。Palantir 的公司语言里充满了“Impro 式”的表达，比如“casting（角色设定）”就是其中一个例子。

作者 Keith Johnstone 在书中讨论过：同一个演员，只要改变一些肢体语言，就可以表现出“高地位”或“低地位”：说话时头部保持不动，是“高地位”；头左右晃动，是“低地位”；挺胸抬头、双手外露，是“高地位”；含胸缩肩、双手插兜，是“低地位”，诸如此类。

如果你不了解这些社交信号，你很难在客户环境中混得开。这意味着你更难打通客户的数据接口、推动他们使用你的软件，最终就意味着项目失败。

**这也是为什么，许多前 FDE 后来都成了非常优秀的创业者。**

（尽管 Google 员工比 Palantir 多了大约 50 倍，但每一届 Y Combinator（YC）创业营里，Palantir 出身的创始人往往比前 Googler 还多。）

优秀的创始人具备一种本能，能够读懂一个房间的气氛、群体动态和权力结构。

这点虽然不常被谈论，却极为关键：创办公司，其实是一连串谈判的过程——而你必须大多数时候能赢下来。招聘、销售、融资，这些说到底都是谈判，而想成为谈判高手，就必须深刻理解人性和行为。

这正是 Palantir 在 FDE 实践中所教授的能力，而在硅谷其他公司，很难学到这一套。

此外，FDE 还必须具备强大的理解能力。

你对客户越有效，往往就代表你越快掌握他们的语言和业务模式。

比如你在和医院合作，不能只说“我们帮你改善医疗系统”，你得迅速学会讨论病人通量、床位调度、容量管理这些专业术语；如果你接触的是药物研发、健康保险、医学信息系统、癌症免疫疗法等领域，每个行业都有一套专属语言。

**那些做得好的人，通常都是能非常快速掌握行业语言的人。**

在 Tyler Cowen 的《Talent》一书中，我最喜欢的一个观点是：最有才华的人往往会发展出一套属于自己的词汇和思想“梗”（memes），而这些语言符号构成了进入他们所建构的知识世界的入口。

Tyler 自己就是个典范。任何一个 Marginal Revolution（MR）博客的读者都能立刻说出十几个 “Tyler 式表达”——比如：“model this”（建个模型看看）；“context is that which is scarce”（语境是最稀缺的资源）；“solve for the equilibrium”（解出均衡解）；“the great stagnation”（大停滞）……

你也能在其他人身上看到类似的能力：Thiel 是一个，Elon Musk 也是（比如 “多星球物种”、“守护意识之光” 等，都是他的思想梗）。Trump、Yudkowsky、gwern、SSC（Slate Star Codex 博主）、Paul Graham 这些人也都经常创造属于自己的语言系统。事实证明，这种语言创造力其实是一种“影响力”的有效衡量指标。

这个规律同样适用于公司。Palantir 就拥有一整套庞大的术语体系，其中有些甚至晦涩得让人摸不清头脑，以至于“Palantir 到底是干嘛的？”本身都成了网络上的一个梗。

“Ontology（本体论）” 是比较早的一个术语，后来又出现了更多，比如：impl（implementation，即现场项目）、artist’s colony（艺术家群落）、compounding（复利增长）、the 36 chambers（三十六道考验）、dots（数据点 / 洞察）、metabolizing pain（代谢痛苦）、gamma radiation（伽马辐射）…

这些术语，每一个都代表着一套浓缩的理念或实践逻辑。重点并不是解释这些词具体什么意思，而是：如果你在挑选想加入的公司，不妨留意那些拥有自己内部语言体系的组织——这种语言往往能帮你更深刻地思考问题，更快地融入文化，也更容易激发创造力。

提起 Palantir，大多数人第一反应是 Peter Thiel。但其实，很多独特的术语都是由早期员工发明的，尤其是现任公司总裁 Shyam Sankar。

尽管我在公司工作的那段时间，Peter 并未直接参与日常运营，但他对 Palantir 的文化有着深远影响。

我认为，公司里不给员工设定头衔这一点，大概就是来自 Peter Thiel 的理念。

我在 Palantir 工作时，几乎所有人都统一叫做 “Forward Deployed Engineer”（前线部署工程师），除此之外，大概就五六个“总监”（Director）和一个 CEO。偶尔也有人自己编个头衔（我认识一个人就自称是 “Head of Special Situations”，我觉得非常搞笑），但这些新头衔从来没有真正流行起来。

这种做法可以直接追溯到 Peter 的“吉拉尔式”信念：一旦你设立头衔，人们就会开始渴望它们，于是内部就会滋生嫉妒和政治斗争，最终破坏团队的凝聚力。与其如此，不如大家都用同一个头衔，把注意力集中在真正的目标上。

当然，也有很多人批评这种“扁平结构”的管理方式，比如那篇广为引用的《结构缺失的暴政》（The Tyranny of Structurelessness）就很有洞见。而且如今的初创公司似乎早已不流行这种模式了，往往一开始就设立 CEO、COO、副总裁、创始工程师等各种头衔。

但就我个人经历来看，Palantir 的这种方式确实运作得不错。有些人确实更有影响力，但这种影响力通常是建立在某项真正了不起的成果基础上的。更关键的是，没人有权限命令别人做什么。所以，即使某个人很有声望、觉得你的想法很蠢，你也完全可以无视他，继续去构建你认为正确的东西。

而且在公司文化中，这种“我坚持我自己干”反而是被推崇的。公司里就流传着这样的故事：某个工程师不顾总监的意见，坚持自己做了某个项目，结果这个项目后来成了公司的关键基础设施。这类故事常常被拿来作为学习榜样。

当然，这种方式的代价就是：公司常常显得缺乏清晰的战略方向，更像是一个培养皿（Petri dish），聚集了一群聪明人，各自建立自己的“领地”，往不同方向发散。但与此同时，它也极具创造力。Palantir 曾经孕育出很多非常新颖的 UI 概念和产品创意，很多现在才开始出现在别的公司，比如 Hex、Retool、Airflow 等工具的某些核心模块，最早都是在 Palantir 内部开发出来的。

现在 Palantir 正在把同样的创造力应用到 AI 领域——他们为大型企业部署大语言模型所构建的工具系统，也非常强大。

“不设头衔”的文化还带来了另一个现象：公司内部谁“当红”、谁“失势”变动非常快。因为大家的头衔都一样，所以你只能通过别的方式来判断某个人的影响力，比如：“这个人最近和某位总监走得很近”，“这个人正在主导一个看起来很重要的产品项目”，而不是因为他是“某某副总裁”。

这种机制导致公司内部呈现出一种“英雄—废柴”过山车式的循环：某人一段时间内可能风头无两，过几个月又神秘消失，什么项目都不负责了，而且你也永远搞不清到底发生了什么。

## （五）“蝙蝠信号”（Bat-signals）

还有一个我认为源自于 Peter Thiel 的理念，是“人才蝙蝠信号”（talent bat-signals）——这点在我现在自己创办公司（目前还在“隐身模式”）之后才真正体会到：招到优秀的人才真的很难，你必须拥有一些差异化的“人才来源”。

如果你只是和 Facebook、Google 去抢同一批斯坦福计算机系毕业生，那你基本注定会输。所以你需要两件事：1. 一群特别想加入你这家公司的人，而不是随便找份硅谷好工作的；2. 一个能大规模接触到这类人的方式。

Palantir 在这方面就有不少“差异化的人才来源”，构成了它的“招聘 alpha”。

举个例子，在支持国防 / 情报工作还不那么流行的时候，Palantir 就吸引了一批这方面有志向的人。这种筛选机制自然更容易招到中西部或“红州”的聪明工程师，以及很多有能力的前军人、前 CIA / NSA 特工。这些人一方面想为美国效力，另一方面又对在硅谷公司工作的方式很感兴趣。

入职第一天，和我一起参加部门内部培训的还有一个看起来比我年长的人。我随口问他：“你来 Palantir 之前是做什么的？”他面无表情地看着我，说：“我在那个机构（the agency，这里指 CIA）干了 15 年。”

随后我见到了我的第一位直属领导——他是前俄亥俄州 SWAT 特警！同时也是一名退役军人。

有很多这样的人，其中不少非常有才华，而他们大多不会去谷歌。Palantir 是这类人才几乎唯一的“灯塔”，公司在支持军方、表达爱国情怀等方面也一直非常高调——尽管这些在当时非常不受欢迎。这就形成了一种高度有效、独特的“人才信号”。（现在也有了 Anduril，以及一批防务和制造类初创公司。）

第二点是，想加入 Palantir，你得有点“怪”。至少在最初的热潮过去之后是这样，尤其是在特朗普任期内，公司一度被视为“异类”。一方面是公司非常激进地宣传“使命驱动”的理念，在当时并不常见；另一方面，公司也明确表示员工工作时间长、薪资低于市场水平，而且出差频繁。与此同时，因为与政府合作，我们还曾被硅谷的招聘会赶出来。所有这些，都筛选出了特定类型的人才：那些能独立思考、不被负面新闻轻易左右的人。

## （六）道德问题

道德问题是一个非常有趣的话题。Palantir 毫不掩饰地支持西方世界，这种立场我大体上是认同的——我认为，一个更偏向中共或俄罗斯的世界将会是一个糟糕的世界，而这正是当今摆在我们面前的选择。如果你生活在一个自由国家，批评它其实很容易；但如果你曾经历过其他体制，这种批评就不那么轻松了（我有过这类经历——童年时曾在一个压制性的国家生活过几年）。因此，即使有时候不完全认同军方的行为，我也完全不反对公司为军方提供支持。

但军方难道不会有做错的时候吗？当然会——比如我本人就反对伊拉克战争。这正好切中问题的核心：在 Palantir 工作并不是完全“道德正确”，因为我们有时会支持一些我并不认同目标的机构；但也并非完全“不道德”：政府其实也做了很多有益的事情，而通过提供不那么糟糕的软件来帮助他们更高效地完成这些工作，本身就是一件值得尊敬的事。

一种澄清道德问题的方式，是把公司的工作分成三类——这三类划分并不完美，但请先听我说完：

1.道德中立：指的是普通的商业合作，例如为 FedEx、CVS、金融公司、科技公司等提供服务。虽然有些人可能会对此有所保留，但总体来说，大多数人对此类工作不会感到道德困扰。

2.明确是好事：例如，与美国疾控中心（CDC）合作开展抗疫项目；与国家失踪与受虐儿童中心（NCMEC）合作打击儿童色情。这类工作多数人都会认为是有价值且正面的。

3.灰色地带：指那些涉及道德上棘手、复杂抉择的工作，例如医疗保险、移民执法、石油公司、军方、情报机构、警察与犯罪等领域的合作。

每个工程师都会面临一个选择：你可以去做类似 Google 搜索或 Facebook 新闻推送这类的工作，这些基本上是些边际上有益的事情，属于第一类；你也可以选择从事第二类的工作，比如加入 GiveDirectly、OpenPhilanthropy 之类的组织。

而对 Palantir 最常见的批评在于：“你不应该参与第三类事务，因为这可能涉及做出道德上有问题的决定。” 比如 2016 至 2020 年期间的移民执法，就让许多人感到不安。

但在我看来，完全忽视第三类事务、选择抽身不参与，本身也是一种逃避责任的表现。第三类的机构是必须存在的。美国是靠持枪的军人来保卫的；警察必须执法——而且根据我的经验，即使有些人对执法感到道德不适，一旦自己家被偷了也会立刻报警。石油公司必须提供能源，医保公司必须做出艰难的取舍。这些行业确实有不光彩的地方，但我们是否就该完全不参与，把一切都丢给他们自己去处理？

我认为是否要与第三类客户合作，并没有一个放之四海而皆准的答案，必须具体情况具体分析。Palantir 的态度可以概括为：“我们会和大多数第三类机构合作，除非它们明显是在作恶，并相信民主机制终将推动它们走向更好的方向。” 例如：

• 在移民执法方面，Palantir 在特朗普时期退出了与 ERO（执法与遣返行动）的合作，但继续与 HSI（国土安全调查局）合作；

• 公司与大多数第三类机构保持合作，因为它们总体上在为社会做有益的事情，尽管其中也存在问题行为；

虽然我不能披露具体细节，但 Palantir 的软件确实曾在多起恐怖袭击未遂中发挥了阻止作用，我认为仅凭这一点，就足以为这类合作辩护。

这种立场令很多人感到不安，正是因为它意味着你无法保证自己所做的始终是“百分百正确”的事。某种程度上，你得接受历史的不确定性，并且赌自己所参与的是正向多于负向的事；也赌在场比缺席要更好。对我来说，这样的理由足够充分，而其他人可能会选择离开。

当然，这种立场也有风险：它很容易沦为一种“为权力结构背书”的通用借口，说到底你只是助推了现有的系统。这就是为什么需要“具体问题具体分析”——没有通用答案，只能具体判断。就我个人而言，我在 Palantir 大部分时间从事的是医疗健康和生物相关的项目，对我的贡献我感到问心无愧。我相信那些阻止恐袭的人，也对自己的工作感到自豪；在疫情期间负责分发药品的人也是如此。

即使如今风向已变，大家对这类“复杂领域”的参与越来越趋之若鹜，但对技术人员来说，这些问题仍然值得思考。人工智能就是一个很好的例子——许多人对其部署可能带来的后果感到不安，比如用于黑客攻击、深度伪造泛滥、或引发失业等问题。但 AI 也确实带来了巨大的好处。

就像在 Palantir 一样，从事 AI 相关工作大概率不会是“完全正确”或“完全错误”的。完全回避它，或者幻想通过“暂停”来规避问题，并不是最佳方案。即使你不是在 OpenAI 或 Anthropic 工作，如果你具备从事 AI 相关工作的能力，那你可能也应该参与其中。确实有一些明确的方向：做评估、做对齐、增强社会系统的韧性。但我想强调的是，“灰色地带”同样值得介入：比如参与制定 AI 政策，将 AI 应用于医疗等领域。过程会很艰难，但值得深入其中。

我回顾当今 AI 领域最具影响力的那些人，他们几乎全都是“身处局中”的人——要么在 AI 实验室、要么在政府、要么在智库中。我宁愿成为他们中的一员，也不想当一个站在圈外指指点点的人。当然，这其中需要面对很多艰难决策，但至少你在场，当关键时刻发生时，你有机会作出影响——即使有朝一日你选择离开并发出警告。

## （七）接下来去哪？

我仍然看好这家公司吗？是的。

本轮 AI 周期带来的最大生产力提升，将出现在 AI 真正开始为当今时代的大型企业和机构赋能之时——这些行业包括制造业、国防、物流、医疗等。而 Palantir 已经花了十年时间与这些企业深度合作。未来，AI 智能体将驱动许多核心的业务流程，而这些智能体将依赖对关键业务数据的读写权限。花十年时间去整合企业数据，正是将 AI 真正落地到企业应用的关键基础。这个机会巨大无比。

至于我本人，我正在执行期待已久的“宏伟计划”：下一步是创办一家新公司。是的，其中会涉及一些政府相关的内容。团队很棒，而且——我们正在招人。我们甚至偶尔还会讨论维特根斯坦。

_作者：Nabeel S. Qureshi，2015-2023年任职于 Palantir，原文写于2024年10月，由四时研选翻译_

# 三、Palantir估值该怎么看？从盈利模式、护城河到TAM全解析

四时研选、晨星报告

晨星（Morningstar）预计，到2033年，Palantir所能覆盖的潜在市场规模（TAM）将达到1.4万亿美元。

基本情境假设是，Palantir将走出类似Salesforce在2010年代的发展轨迹。Salesforce通过标准化销售流程和整合数据，极大提升了销售效率；而Palantir有望以颠覆性方式革新企业的数据分析流程。

传统模式下数据被收集、分析、呈现后便被丢弃，Palantir则通过创建一种读写循环系统，使软件在与数据交互时不断学习和改进，从而为用户提供清晰的“行动方案”建议，极大提升决策效率，甚至部分替代传统的内部IT团队职能。

晨星指出，Palantir估值的驱动因素在于潜在市场规模预期以及实际渗透能力。尽管对TAM的预期变化可能带来股价大幅波动，但从当前发展阶段来看，公司依然处于有利位置，真正的爆发期或许还未到来。

## 经营战略

Palantir是一家以AI驱动决策优化为核心的软件公司，其关键能力在于：整合全球最复杂的数据集，并构建一个覆盖组织各层、能实时交互与演进的闭环系统。随着时间推移，该系统不断自我学习与演进，推动各行业实现高度自动化、机器学习驱动的业务流程。

其最大的技术优势在于“本体框架”（Ontology Framework）——该架构可帮助客户从海量数据中识别隐藏关联，支持高级决策。Ontology 原为哲学术语，研究“存在的本质与关系”，Palantir借此强调其系统对现实世界复杂性与关联性的高还原能力。正因如此，Palantir具有为任何西方国家企业、政府或军队解决任何问题的潜力。

公司目前拥有两大主要平台：Gotham（主要面向政府与国防客户）和Foundry（服务于商业客户）。Palantir最初专注于国家安全与军事情报，后逐步扩展至企业级解决方案。2023年推出AI平台AIP，作为大型语言模型的调度中枢，大幅降低非技术用户调用AI功能的门槛，推动AI在企业中的普及。

在销售策略方面，Palantir采用“训练营”式销售模式，快速识别客户痛点并部署定制解决方案，极大提高了客户转化效率。其AI平台也因此加速在各行业落地，预示着未来几年将迎来爆发式增长。

## 护城河

虽然AWS、Snowflake和ServiceNow等公司也有数据分析工具，但Palantir最大的不同在于：它不仅分析数据，更帮助客户将数据转化为可执行的解决方案。

其本体框架让Palantir得以发现隐藏在数据背后的关键关联，并构建一个完整的闭环交互系统。

简而言之，**Palantir能采集全形态客户数据：**从结构化数据（以行列存储的表格数据）到非结构化数据（如邮件、报告、IT系统日志或视频/图像等无固定格式的内容），从情报数据（卫星影像、部队调动、犯罪记录、威胁评估）到运营信息（供应链、需求、生产量或产出指标），乃至模拟信号数据（工厂或野外环境中的温度、压力、声响、振动等物理世界参数）。系统通过自动清洗数据、识别关联性，并部署机器学习算法，生成可直接交互和落地执行的业务建议。

与Palantir竞争的通常是企业内部IT部门，因为其核心业务同样涉及数据分析与信息看板构建。但传统的内置IT数据聚合架构往往导致零散拼凑的解决方案：操作笨拙、迭代困难，且扩展成本高昂。

**Palantir本体框架的价值定位在于：**不仅实现数据的组织与可视化，更能生成经过优先级排序的数据资产——这些数据可被快速理解并交互操作，最终实现现实世界的效率提升。无论是聚合传统数据湖、通过分析病患数据提升床位周转率，还是将全球的模拟信号数字化，该公司都在通过数据推动效率提升。这些切实可见的效能提升不断累积，最终转化为客户的转换成本壁垒。

**Palantir的客户粘性极强，**其净收入留存率（NRR）约为120%，高于Snowflake、DataDog和Splunk等同行。自AIP平台发布以来，其NRR更呈现逐季度加速攀升态势，这不仅印证了客户黏性，也反映了其产品渗透率在扩大。客户认可Palantir框架的价值，并持续加大投入，预期这一趋势将延续。

实际上，客户一旦使用Palantir系统，将很难放弃，因为该系统会持续学习和优化，一旦中断将导致效率显著下降。

此外，Palantir客户的平均支出水平极高，每位客户每季度平均花费超过100万美元，且已在数据导入、流程梳理、培训等方面形成沉没成本，进一步加深了客户锁定。

实际案例显示，Tampa综合医院与Palantir合作后，患者平均住院时长减少30%；在军事领域，Palantir系统曾助力发现本·拉登的位置并制定作战计划。当涉及生死攸关的复杂决策时，客户必须选择最强、最可靠的解决方案——这正是Palantir的核心价值。弃用该平台不仅意味着经济损失，更可能造成难以估量的人力代价。

客户增长势头同样令人瞩目。自2023年中触底以来，美国商业客户数量迅猛增长。这一增长得益于新推出的训练营试销售策略，通过高频交互培育潜在客户。签约后，Palantir工程师会深入了解客户数据，量身定制方案，进一步增强用户粘性。这种独特的获客与留存机制，能持续深化与终端用户的合作关系并促进增长。

值得关注的是，公司正通过拓展商业客户实现收入多元化。相比政府合同，商业客户的利润率通常更高。

总体而言，Palantir作为创新型AI公司，擅长从全球最复杂数据中提炼精准解决方案。其产品已深度嵌入各行业关键基础设施，极高的净收入留存率更印证了其护城河优势。

## 估值模型与增长逻辑

Palantir估值的核心逻辑在于其潜在市场规模的扩大与持续渗透能力。晨星预计，到2033年，TAM将达到1.4万亿美元，其中2028–2030年将迎来爆发式增长期，年复合增长率约40%。

乐观情形估计TAM超1.6万亿美元，若未来市场渗透率接近3%，对应估值约为280美元/股。

AI革命才刚刚开始，而Palantir未来可能会像当年的Salesforce一样，成为企业不可或缺的核心系统，只不过其角色从“销售操作平台”转向“决策支持系统”。

未来增长将主要来自商业客户的持续扩张，而现有客户留存率也将继续保持高位。

Palantir正处于毛利率持续改善的周期：自上市以来，Palantir的毛利率从2020年的68% 提高到2024年初的82%。早期毛利率偏低主要因大量股权激励摊销导致。此后，随着营收增速超过运营支出，毛利率持续改善。预计未来10年毛利率将再提升400个基点，主要由于高毛利商业客户占比上升。

不过，在AI计算资源需求不断增长的背景下，云成本上行压力仍在，因此我们对毛利率进一步大幅提升持谨慎态度。

在支出方面，Palantir过去在研发和销售上的投入很大，2023年这两项合计占收入的52%。但营收增长正在逐步超越开支，盈利能力持续增强。训练营式销售策略的推行，不仅提升了客户转化效率，也有效控制了获客成本，进一步提升盈利预期。

## 风险与不确定性

Palantir的最大不确定性在于：其潜在市场规模（TAM）与实际渗透率仍难以精准预估。

其本体框架适用于众多行业，理论上覆盖面广泛，也因此带来了高度增长预期。但这也意味着，任何关于TAM的预期下调，都会带来估值层面的显著波动。

尽管目前尚无公司能在本体框架或AI决策系统方面可与Palantir匹敌，但未来科技巨头（如Google）开发出类似 AI 决策软件的可能性依然存在。一旦发生，将面临激烈竞争与定价压力。

值得注意的是，Palantir 拥有领先市场 10~20 年的技术积累，其基于机器学习的 AI 能力构成了显著壁垒。新进入者若想超越，需要在研发上投入巨额资金，门槛极高。

此外，Palantir处理的多为敏感信息，数据泄露可能引发严重的ESG风险。好在公司目前采用了行业领先的加密技术（Cipher服务），至今未发生重大数据泄露事件。

## 结语

Palantir是一家真正以AI为核心，具备平台化能力与战略价值的公司。凭借其对复杂数据的深度整合、极强的客户粘性、领先的本体框架与AI编排系统，Palantir有望成为未来十年最具代表性的AI企业之一。

当AI革命加速推进，Palantir或许就是那个“看得远、站得稳、跑得快”的“长坡厚雪型公司”。

资料来源：晨星报告

# Palantir的本体论：在数据中寻找意义

Palantir Blog四时研选

_2025年07月30日 17:04_ _广东_

一个高效的数据生态系统，必须融入“本体论”（Ontology）的理念，才能实现可扩展性与可持续性。

## 引言

只要你花一点时间研究 Palantir 及其所构建的软件平台，就一定会遇到一个颇为特别的词：本体论（Ontology）。Palantir 用它的频率之高，甚至可能让人忘了它其实源自一个晦涩的希腊哲学概念。Palantir 用“本体论”一词来描述其所开发的一项关键技术，它使我们能够应对全球组织所面临的各种复杂数据挑战。

Palantir 得出的结论是：一个高效运行、具备扩展能力的数据生态系统，必须包含本体论的理念。这篇文章进一步解释“本体论”在 Palantir 的含义、实际应用方式，以及它为何如此重要。

## 什么是“本体论”（Ontology）？

数据生态系统的核心，在于它如何处理系统中的数据。虽然人们关于数据的问题通常围绕“数据从哪里来？要去往哪里？到达目的地后做什么？谁可以访问，如何访问？”这些“流动性”层面，但实际上，有一个更为关键（却常被忽视）的问题是：数据的意义是什么？

系统中所有类型的数据 —— 原始数据、处理后的数据、运营数据，乃至计算模型生成的任何数据输出 —— 都与回答这个问题息息相关。值得注意的是，数据本身并不天然具备意义；相反，意义是由使用数据生态系统的用户“附加”到数据上的。这听起来像是哲学问题，但实际上，它是任何一个高效数据系统都必须严肃对待的“实践问题”。

本体论，指的是将数据系统性地映射到有意义的语义概念上的过程。 一个有效的本体框架不嵌入数据本身，而是作为一种外部结构，支撑数据集成、应用构建、用户协作及其他各种功能。这种本体论的前提是：数据是“中性的”。虽然数据的结构会影响本体的设计方式，但本体本身应能在不依赖具体数据存在的情况下独立运行。要解释为什么会这样，我们需要进一步理解“本体论”究竟做了什么。

本体论的作用是提供一张“地图”，把数据与意义连接起来 —— 它定义了“什么是有意义的”。 这些“有意义的东西”，就是组织里的名词、动词和形容词。

举个例子：一家银行可能最关心的是一些关键对象或对象类别，比如账户（Accounts）、交易（Transactions）和金融产品（Financial Products）。在本体中，每一个这样的对象类别都需要有相应的定义，同时它们之间也会通过各种“已定义的关系”连接成一个语义网络。每个对象类别定义中，还会包括一系列属性，用来描述这个类别。当一个实际的账户、交易或金融产品以数据的形式出现时，它就会被映射到某一个“对象类别”中，成为一个具体的“实例对象”（instantiated object）。

这些“实例对象”可以被创建或删除，可以彼此连接或断开，它们的属性也可以发生变化。数据科学家的任务，就是在本体框架中建立这些对象类别的定义，以便生成可用于业务系统和操作流程的“实例化对象”。

下图进一步解释了这些抽象概念：

![640-52](https://www.smartcity.team/wp-content/uploads/2025/10/640-52.jpeg)

为了真正实现这种三层抽象结构，本体论不能只是一个“概念”，它必须作为一个服务框架存在，能够把这些概念“运行化”，即：服务于数据流与应用的实际工作流程。

## 为什么“本体论”至关重要？

本体论为数据生态系统中的所有参与者建立了一套共同的语言。 通过这种方式，它统一了各类异构数据源与系统，促成了协同合作和依赖型工作流的构建。本体论对语义进行标准化，并定义了一系列“有意义的类别”，供用户在实现个人或组织目标时加以利用。对象类别（例如：人员、设施、账户、交易、产品、物料、供应商等）不再只是电子表格中的一行行数据，而是任务本身的“语言”。

当相关数据被映射到抽象的“对象类别”中时，数据操作系统的用户就能够自然地理解这些底层对象的意义与作用。这使得应用程序和工作流可以以“面向本体”的方式开发，所需代码量和定制开发的工作大大减少。应用程序因此不再只是处理数据的工具，而是成为一种交互式的界面，使用户能够主动推动业务目标的实现。

从这个角度看，本体论就像连接“数据”与“应用”的组织性纽带。在一个有效的本体体系下，数据集成的工作就变成了：把原始数据映射到既有本体上；而应用开发的工作就变成了：构建用户与本体对象交互的方式。此外，为了在不同应用间实现一致性，一些标准化的业务逻辑也可以直接嵌入本体之中，例如但不限于：安全权限设置、对象聚合与筛选、对象变换、与外部系统的 Webhook 联动，以及各种写回操作。

本体论的引入，可以有效避免“数据集与应用之间的碎片化映射”问题，释放数据科学家与应用开发者的生产力，让他们专注于更具实效性的问题，同时也帮助减少对数据管道与应用程序的运维管理负担。

## 高效“本体服务”的关键要求

1. 本体服务必须实现数据管道与应用程序的解耦。

将数据层与应用层分离，是本体服务的一个核心特征。这种解耦有助于降低每一层的管理复杂度，同时引入标准化的业务逻辑。新增的数据只需映射到一个统一的地方（即本体），而新的应用程序则可以直接利用已有的对象逻辑进行构建，避免重复开发。

2. 本体服务必须提供一个“动态元数据服务”，允许用户创建、定义、修改和废弃本体元素。

所谓“动态元数据服务”（又称“本体语言”Ontology Language），就是定义对象、属性及其关系的地方，并将这些元素关联起来，构建出完整的对象图（Object Graph）。一个有效的本体定义应当具有动态性，能够支持引入新的对象、属性或关系类型，并对现有定义进行修改。对象相关的业务逻辑也应具备动态能力，以便各类应用更容易复用本体中集中定义的标准化协议。

3. 本体服务必须提供“对象集服务”，用于定义如何将对象类别组织成集合，包括聚合、筛选和搜索等能力。

对象不仅是数据的容器，更是语义上的有意义实体。因此，本体服务需要提供机制，使这些语义特征可以被程序化利用。比如，对象集服务能够定义某类对象如何被逻辑性地聚合、筛选或搜索。如果某一类对象可以通过特定的属性或关系来分组，该服务就负责定义这类聚合逻辑。

4. 本体服务必须提供“对象函数服务”，允许对对象类别定义可调用的函数，包括任意逻辑（如机器学习模型等）。

尽管“对象”本身是非常有用的抽象形式，但本体真正的强大之处在于：可以将逻辑嵌入到对象中。如果某段逻辑可以针对一个对象或一组对象运行，就应以“函数”的形式定义它。这个函数可以是简单的，比如计算对象属性的平均值；也可以非常复杂，比如在对象上运行机器学习模型等高级任务。这些函数可以被各类应用调用，并且在多个应用之间保持逻辑的一致性和可复用性。

这一架构的本质，是将“语义”和“逻辑”抽象为统一的结构层，使数据生态具备高度可扩展性、可组合性与协同性。

5. 本体服务必须提供“对象操作服务”，定义对象类成员如何发生变更。

一旦对象被定义为某个“对象类别”的实例，它们在数据生态系统中会经历一系列变化。“对象操作服务”负责规定对象如何发生变化，包括不同类型的变更应遵循的规则与约束。无论是简单地切换某个属性值，还是将多个对象互相关联，这些操作都可以被标准化定义，并在整个企业范围内复用。

6. 本体服务必须具备高性能的对象存储层，以支持实时处理，包括对时间敏感或流式属性的支持。

与大多数数据存储解决方案类似，本体的存储服务也需要围绕特定数据结构进行优化。本体服务应提供一个专门设计的存储层，能够支撑本体架构及其各类子服务的使用，从而为用户提供丰富而流畅的交互体验。特别是那些具有时效性、需要实时响应的对象数据，也应能得到有效支持。

7. 本体服务必须提供“Webhook 服务”，允许将对象数据导出至外部系统，或写回底层数据存储。

尽管本体服务对现代数据生态系统至关重要，但在许多企业中，仍存在无法完全兼容本体架构的遗留系统或单点解决方案。为了实现与这些系统的互通，本体服务必须暴露 Webhook 接口，使对象数据能够重新映射到这些“非本体感知系统”中。即便数据在应用层被更改，也可以继续被这些系统利用。同时，这类服务也支持将应用层产生的数据写回到数据层，确保数据表示与本体表示始终保持一致性。

8. 本体服务必须能与企业安全架构对接，包括对底层数据源的访问授权控制。

在本体架构中实施安全控制的能力，对企业而言具有重大影响。对象及其属性可以根据其所依赖的数据源进行权限控制，同时也可对本体类型和对象上可调用的服务实施安全管理。最关键的是，本体服务将安全策略嵌入其自身逻辑中，这意味着应用开发人员无需单独处理这些安全需求，从而实现更高层级的安全性与标准化。

这部分强调了构建一个企业级、可运行的本体服务体系所必须具备的底层能力：不仅仅是“定义语义”，还必须提供一整套结构化、服务化、安全可控、可与外部集成的技术框架，从而真正支撑数据生态系统的智能化与规模化。

## 结语

本体论是一项关键使能技术，它让数据得以被驾驭，从而助力实现更优的结果、更明智的决策和更高效的运营 —— 同时避免“规模不经济”的陷阱。

我们在上文中阐述了构建一个高效数据生态系统所需的本体服务要求。推动这项能力落地的动因显而易见，且多种多样；但其中最重要的一点是：本体论的存在，使得数据生态系统可以随着时间不断发展演进，持续释放复利价值，而不是在复杂性中日益失控。

_本文来自 Palantir Blog，原标题为 Ontology: Finding meaning in data_

www.smartcity.team

文章标签： [palantir](https://www.smartcity.team/tag/palantir/)

[![](https://www.smartcity.team/wp-content/uploads/2025/07/%E7%9F%A5%E8%AF%86%E6%98%9F%E7%90%83%E4%BA%8C%E7%BB%B4%E7%A0%814.jpg)](https://t.zsxq.com/hCZQu)

声明：转载请注明来源于“智慧城市行业分析(www.smartcity.team)”及相关作者。本站信息除原创外，部分信息来自于互联网，如相关内容涉及到侵害权益，请联系底部联系方式删除。

📚【数字科技人专属福利】创始会员立减 50 元，解锁全行业核心资源！

「数字科技专题研究」知识星球 —— 你的专属行业资料中枢，依托「智慧城市行业分析」专业积淀，精华资料、实时前沿动态、独家方案库，一站式解决你的信息焦虑！

✅ 加入即享 4 大核心价值：

▪ 效率飙升：节省 90% 资料筛选时间，告别大海捞针

▪ 认知升级：吃透 AI、算力、数据智能等前沿领域，快速搭建系统知识框架

▪ 资源链接：与行业从业者直接对接，参与案例共创，拓展优质人脉

▪ 专属服务：有报告文件和方案需求的星友，可以留言，我们将在力所能及的范围内获取或制作相应内容；更鼓励大家打卡、留言、互动互助，共建优质行业社群！

👥 无论你是行业工程师、高校研究者、企业决策者，还是数字科技爱好者，这里都能为你赋能！

🚀 数智引领，穿越周期，相约数字科技下一个十年→ [https://t.zsxq.com/zGWUg](https://t.zsxq.com/Jy0rW)

### 为您推荐

[![](https://www.smartcity.team/wp-content/uploads/2026/05/640-27-300x200.png)](https://www.smartcity.team/investment/companies/gartner_china_ai25/)

## [Gartner中国AI25强企业榜单（Gartner China AI 25）：“AI+制造” 是核心主线，小米小鹏理想蔚来美的比亚迪等在内，综合考量企业CEO的愿景、产品、服务、研发、AI人才、组织架构、创新与研究、生态系统、数据及商业模式等因素确定](https://www.smartcity.team/investment/companies/gartner_china_ai25/)

[![](https://www.smartcity.team/wp-content/uploads/2026/05/640-23-300x200.jpeg)](https://www.smartcity.team/investment/companies/2026_forbes_ai_top50/)

## [2026福布斯中国人工智能科技企业TOP50：呈现”头部集聚、腰部拓宽、长尾涌现”的三层格局，技术层与应用层的企业数量比约为6:4，北上身高度集中](https://www.smartcity.team/investment/companies/2026_forbes_ai_top50/)

[![](https://www.smartcity.team/wp-content/uploads/2026/05/f520f2db6210c102f918a6dd2455da6f-300x200.png)](https://www.smartcity.team/investment/companies/%e5%8d%97%e5%a8%81%e8%bd%af%e4%bb%b62025/)

## [南威软件（603636）2025年新签合同10.20亿元，回款15.89亿元，营收8.39亿元，归属于上市公司股东净利润-4.47亿元；2026年坚持“All in AI”战略不动摇，布局AI健康、AI教育、企业数智化服务等B端、C端创新业务，开辟第二增长曲线](https://www.smartcity.team/investment/companies/%e5%8d%97%e5%a8%81%e8%bd%af%e4%bb%b62025/)

[![](https://www.smartcity.team/wp-content/uploads/2026/01/0c99b891568653a8f976b63f0e4492df-300x200.png)](https://www.smartcity.team/investment/companies/%e5%85%a8%e5%9b%bd%e6%95%b0%e6%8d%ae%e9%9b%86%e5%9b%a2%e5%8f%91%e5%b1%95%e8%93%9d%e7%9a%ae%e4%b9%a62025/)

## [全国数据集团发展蓝皮书（2025）：省级地方数据集团数量为29家，地市级地方数据集团数量为187家，主要围绕区域功能保障、公共数据运营、跨域业务拓展三个核心方向开展业务，核心挑战主要为战略定位抉择、数据资源整合路径以及核心竞争力培育机制三个关键层面](https://www.smartcity.team/investment/companies/%e5%85%a8%e5%9b%bd%e6%95%b0%e6%8d%ae%e9%9b%86%e5%9b%a2%e5%8f%91%e5%b1%95%e8%93%9d%e7%9a%ae%e4%b9%a62025/)

[![](https://www.smartcity.team/wp-content/uploads/2026/01/3eb364390194f6db0ec2c176d276d588-300x200.png)](https://www.smartcity.team/investment/companies/2025%e5%b9%b4%e8%b7%a8%e8%a1%8c%e4%b8%9a%e8%b7%a8%e9%a2%86%e5%9f%9f%e5%b7%a5%e4%b8%9a%e4%ba%92%e8%81%94%e7%bd%91%e5%b9%b3%e5%8f%b0%e5%90%8d%e5%8d%95/)

## [工信部2025年跨行业跨领域工业互联网平台名单公布：47家入选，A级12家，B级34家，C级1家，百度、华润平台未通过（附47家双跨工业互联网全清单）](https://www.smartcity.team/investment/companies/2025%e5%b9%b4%e8%b7%a8%e8%a1%8c%e4%b8%9a%e8%b7%a8%e9%a2%86%e5%9f%9f%e5%b7%a5%e4%b8%9a%e4%ba%92%e8%81%94%e7%bd%91%e5%b9%b3%e5%8f%b0%e5%90%8d%e5%8d%95/)

[![](https://www.smartcity.team/wp-content/uploads/2025/10/640-55-300x200.jpeg)](https://www.smartcity.team/investment/companies/bp2025%e6%95%b0%e5%ad%97%e7%94%9f%e6%80%81500%e5%bc%ba%e6%a6%9c%e5%8d%95/)

## [BP商业伙伴“2025数字生态500强”榜单：营收百强（软通、讯飞、中软国际前三）、市值百强（金山办公、讯飞、360前三）、盈利能力百强（宝信、恒生、广电运通前三）、企业成长百强、行业数智化服务商百强（含金融、能源、政务等细分领域）、信创服务商百强、技术领域服务商、业务维度服务商、概念热点类、2025 数字生态奖项、区域方案商。](https://www.smartcity.team/investment/companies/bp2025%e6%95%b0%e5%ad%97%e7%94%9f%e6%80%81500%e5%bc%ba%e6%a6%9c%e5%8d%95/)

### 发表回复

要发表评论，您必须先 [登录](https://www.smartcity.team/wp-login.php?redirect_to=https%3A%2F%2Fwww.smartcity.team%2Finvestment%2Fcompanies%2Fpalantir%2F)。

[返回顶部](https://www.smartcity.team/investment/companies/palantir/#top "返回顶部")

### 来源 7: Palantir 产品体系深度解构：Ontology 驱动下的分层架构与模块- 墨天轮

- URL: https://www.modb.pro/db/1930804422725087232
- 精读方法：firecrawl-scrape

![暂无图片](https://js-cdn.modb.cc/image/float-thumbupoutline.png)

![暂无图片](https://js-cdn.modb.cc/image/float-star-out.png)

![暂无图片](https://js-cdn.modb.cc/image/float-commentout.png)

微信扫码

复制链接

新浪微博

分享数说

![暂无图片](https://js-cdn.modb.cc/image/float-share.png)

采集到收藏夹

分享到数说

举报

[首页](https://www.modb.pro/) /
Palantir 产品体系深度解构：Ontology 驱动下的分层架构与模块

# Palantir 产品体系深度解构：Ontology 驱动下的分层架构与模块

[大数据和云计算技术](https://www.modb.pro/u/615436) 2025-06-06

8644

# 引言：Palantir 还是比较复杂的，这次继续介绍 Palantir 的产品架构和有哪些模块

# 一、发展历程

Palantir的Ontology的发展历史，并非一蹴而就，它的发展与公司的本身的成长和其核心产品的演进紧密相连。

1. 早期萌芽与核心理念（2003年～2008年）：Ontology这个时候是一个理念，将来自不同来源的、看似孤立的数据点连接起来，形成一个有意义的、可操作的整体视图；这个时期的主要产品是 **Palantir Gotham**，主要服务于政府和情报部门。
2. Ontology的概念明确化与Foundry平台的推出（2016年～现在）：随着Palantir将业务扩展到商业领域，推出了 **Palantir Foundry** 平台，在Foundry中，Ontology变得更加明确和核心，确立了 Object Types、Action Types、Logic。
3. 持续演进与AI的深度融合（2021年～现在）：随着AI的发展，Ontolgoy的价值凸显，它为AI模型提供了一个结构化、有上下文的知识基础，使得AI能够更深刻地理解业务逻辑，并做出更可靠的预测和建议。Palantir推出了 **Palantir AIP**，也是构建在Foundry及其Ontology之上的。 **AIP并不独立存在，AIP融合在Foundry的各个功能模块之中。**

# 二、Palantir 产品架构划分

Palantir 的产品架构可以从不同维度进行理解，但通常可以将其视为一个多层次、模块化的体系。以下是一种常见的理解方式，将 Palantir 的核心能力和产品组件分层：

01. **基础设施与部署层 (Infrastructure & Deployment Layer) - 以 Apollo 为核心代表**

    - **Palantir Apollo:** 这是 Palantir 的持续交付和基础设施管理平台。它自动化了软件的安装、升级、监控和维护，确保了跨不同环境的一致性和弹性。Apollo 使得 Palantir 及其客户能够专注于上层应用的开发和数据分析，而无需过多关注底层基础设施的复杂性。它实现了“一次构建，随处部署”的理念。
    - **底层服务网格 (Underlying Service Mesh):** 由 Apollo 强制执行的一组软件定义原则，确保平台内数百项服务的可用性、冗余和可扩展性。

    - **核心功能：** 这一层关注的是 Palantir 整个软件栈（包括 Foundry、Gotham 以及客户基于它们构建的应用）如何在各种环境中（公有云、私有云、混合云、边缘设备，甚至离线环境）被可靠、安全、持续地部署、管理和更新。
    - **关键组件/产品：**
    - **重要性：** 这是整个 Palantir 产品体系的基石，保证了其核心平台的稳定运行和灵活部署。

04. **数据整合与本体层 (Data Integration & Ontology Layer) - Foundry 和 Gotham 的基础能力**

    - **数据连接器 (Data Connectors):** Palantir 平台内置了大量连接器，可以从各种数据库、文件系统、API、流数据源等获取数据。
    - **数据管道与转换引擎 (Data Pipelines & Transformation Engines):** 工具用于清洗、转换、标准化和丰富数据，例如使用 Spark、Flink 或 Palantir 自研的引擎。
    - **本体构建工具 (Ontology Building Tools):** 允许用户定义对象类型 (Object Types)、属性 (Properties)、链接类型 (Link Types) 和动作类型 (Action Types)，从而构建出能够反映业务逻辑的动态数据模型。

    - **核心功能：** 负责连接、摄取、转换和整合来自客户各种异构数据源的数据。更重要的是，在这一层构建“本体 (Ontology)”，即现实世界实体（如人员、地点、事件、设备、概念等）及其相互关系的数字表示。本体为数据赋予了业务含义和上下文。
    - **关键组件/产品：**
    - **重要性：** 这是将原始数据转化为可用资产的关键步骤，为上层分析和应用提供了统一、有意义的数据基础。

07. **数据分析与应用开发层 (Data Analysis & Application Development Layer) - 以 Foundry 和 Gotham 为核心平台**

    - **Palantir Foundry:** 主要面向企业客户，提供一个开放的、可扩展的环境，用于构建数据驱动的运营应用。它包含：
    - **Palantir Gotham:** 主要面向政府和国防情报客户，专注于复杂情报数据的分析、调查和协作。它包含：

    - **分析工具：** 可视化分析、代码工作簿 (支持 SQL, Python, R 等)、时间序列分析、地理空间分析等。
    - **应用构建器 (Application Builders):** 低代码/无代码工具，用于快速创建面向最终用户的交互式应用和工作流 (例如 Workshop)。
    - **模型集成与开发：** 支持导入、训练、部署和管理机器学习模型。

    - **链接分析 (Link Analysis):** 发现实体间的隐藏关系。
    - **地理空间可视化与分析 (Geospatial Visualization & Analysis):** 在地图上展现和分析数据。
    - **时间轴分析 (Timeline Analysis):** 理解事件的发生顺序和发展。
    - **协作工具 (Collaboration Tools):** 支持多用户共享和分析情报。

    - **核心功能：** 在整合和理解数据的基础上，提供强大的分析工具、应用构建能力和人工智能集成，以解决具体业务问题，支持决策制定。
    - **关键组件/产品：**
    - **重要性：** 这是 Palantir 平台价值实现的核心，用户通过这些工具和平台与数据交互，产生洞察，驱动行动。

12. **人工智能集成层 (Artificial Intelligence Platform - AIP Layer)**

    - **AIP 逻辑 (AIP Logic):** 允许用户编排 LLM 和其他 AI 模型，将其连接到本体数据和操作。
    - **AIP 助手 (AIP Assist):** 在平台应用中嵌入 AI 助手，帮助用户通过自然语言与数据和系统交互。
    - **安全与治理工具：** 确保 AI 的使用符合组织的安全策略和伦理准则，例如对 LLM 的输入输出进行控制和审计。

    - **核心功能：** 将大型语言模型 (LLM) 和其他人工智能能力安全、负责任地集成到 Palantir 的核心平台（Foundry 和 Gotham）及其构建的应用中。AIP 旨在增强数据分析、决策制定和自动化流程的能力。
    - **关键组件/产品：**
    - **重要性：** 这是 Palantir 架构中较新的但战略性的一层，旨在将最新的 AI 技术赋能给所有用户和应用场景，同时保持其一贯强调的安全和治理。

15. **安全与治理层 (Security & Governance Layer) - 贯穿所有层次**

    - **细粒度访问控制 (Granular Access Controls):** 基于角色、数据标记、目的等多维度控制数据和功能的访问权限。
    - **数据血缘与溯源 (Data Lineage & Provenance):** 追踪数据的来源、转换过程和使用情况。
    - **审计日志 (Audit Logging):** 记录所有用户活动和系统操作。
    - **加密 (Encryption):** 数据在传输和存储时都进行加密。
    - **合规性工具 (Compliance Tools):** 帮助满足特定行业或地区的法规要求。

    - **核心功能：** 确保数据在整个生命周期中的安全性、隐私保护和合规性。这不是一个独立的层次，而是渗透到平台架构的每一个组件和操作中。
    - **关键能力：**
    - **重要性：** 对于 Palantir 的核心客户（政府、金融、医疗等）来说，这是至关重要的能力。

**总结来说，Palantir 的产品架构可以被看作是一个从底层基础设施管理 (Apollo)，到中间的数据整合与本体构建，再到上层的分析、应用开发 (Foundry, Gotham) 和 AI 集成 (AIP) 的完整体系，并且在所有层面都嵌入了强大的安全与治理能力。** 这种分层但高度整合的架构使其能够处理端到端的数据价值链，从原始数据到最终决策和行动。

# 三、核心产品模块

- **数据连接与集成**

  - **Pipeline Builder**
  - **HyperAuto V2 V1**
  - **数据源连接器/JDBC**

- **本体**

  - **AIP Logic**

  - **proposal（本体提案）**
  - **Object Types**
  - **Link Types**
  - **Action Types（动作类型）**
  - **function（函数）**
  - **interface（接口）**

  - **Ontology Manager（本体管理器）**
  - **logic（逻辑）**
  - **Object Explorer（对象浏览器）**
  - Object Monitors（对象监视器）
  - Object View（对象视图）
  - Vertex（顶点）
  - process mining（流程挖掘）
  - foundry rules（以前称为Taurus）借助Foundry Rules，用户可以创建规则并将这些规则应用于数据集、Objects和时间序列，以支持多种应用案例，如警报生成或数据分类。
  - Map（地图应用）

- 分析

  - Contour：提供了一个点击式用户界面，用于在大规模表格上执行数据分析
  - Quiver：是一个分析和仪表盘套件，搜索和可视化 时间序列和Object数据，将分析 **搭建和发布** 到参数化的交互式仪表盘中
  - Code Workbook（代码工作簿）：高级版notebook
  - Code Workspaces：将 JupyterLab®、RStudio® Workbench 和 VS Code 第三方 IDE 引入 Palantir Foundry
  - Notepad（记事本）：是一个面向对象的协作富文本编辑器。除了可以添加和格式化文本和图像等内容外，您还可以集成来自其他 Foundry 应用程序的微件，如 Contour、Quiver、Code Workbook 和 Object Explorer
  - Fusion：Foundry 的电子表格应用程序，处于稳定状态，不再更新
  - AIP Threads：是一款通用生产力工具，专为企业用户设计，利用大型语言模型（LLM）的力量帮助用户完成各种任务和临时分析。处于测试阶段

- 应用开发：

  - **workshop：使应用构建者能** 够为操作用户创建互动且高质量的应用程序
  - **slate：能够通过** 拖放界面构建具有自定义设计的动态和响应式应用
  - 本体SDK React应用
  - **automate：自动化应用程序** 允许用户定义条件和效果。条件会被持续检查，当指定条件满足时，效果会自动执行
  - carbon：可以为需要执行关键操作工作流的非技术用户提供专注的体验
  - **AIP Agent Studio**
  - 解决方案设计师
  - 应用案例

- 模型

  - 模型集成
  - 模型开发
  - 模型迁移

- 安全

  - 组织、空间、项目、角色、权限
  - 审批
  - 检查点
  - 密码
  - 敏感数据扫描器
  - 数据生命周期
  - 安全审计

- 管理

  - 账号认证
  - control panel
  - 资源管理
  - Organization settings

![](https://oss-emcsprod-public.modb.pro/image/auto/modb_20250606_867a1649-4278-11f0-9cd2-8ca982f925c1.png)

[大数据](https://www.modb.pro/tag/%E5%A4%A7%E6%95%B0%E6%8D%AE?type=knowledge) [aip](https://www.modb.pro/tag/aip?type=knowledge) [应用架构](https://www.modb.pro/tag/%E5%BA%94%E7%94%A8%E6%9E%B6%E6%9E%84?type=knowledge) [palantir](https://www.modb.pro/tag/palantir?type=knowledge) [用户分析](https://www.modb.pro/tag/%E7%94%A8%E6%88%B7%E5%88%86%E6%9E%90?type=knowledge)

文章转载自 [大数据和云计算技术](http://mp.weixin.qq.com/s?__biz=MzA3ODUxMzQxMA==&mid=2663999309&idx=1&sn=699da00c570200fb544b71550e9243af&chksm=847c5320b30bda36abe73f93b174f6826e9f781cd808f0f3de183dc0d74d976ce2fdd5349d2d#rd)，如果涉嫌侵权，请发送邮件至：contact@modb.pro进行举报，并提供相关证据，一经查实，墨天轮将立刻删除相关内容。

### 评论

### 相关阅读

[从“用AI”到“生于AI”：2026智能原生大会将于6月16日在京启幕\\
\\
大数据技术标准推进委员会\\
\\
64次阅读\\
\\
2026-06-03 10:10:36](https://www.modb.pro/db/2061993923762020352) [欢迎新Buddy：DataBuddy\\
\\
腾讯云大数据\\
\\
36次阅读\\
\\
2026-05-22 10:24:18](https://www.modb.pro/db/2057648714701955072) [TCIceberg 实时入湖：百万级/秒背后的六大技术\\
\\
腾讯云大数据\\
\\
32次阅读\\
\\
2026-05-30 09:28:43](https://www.modb.pro/db/2060533829706801152) [腾讯云与 CCSA TC601 联合发布白皮书，提出 Data+AI 时代大数据平台融合创新演进路径\\
\\
腾讯云大数据\\
\\
29次阅读\\
\\
2026-05-22 10:24:18](https://www.modb.pro/db/2057648718216781824) [腾讯云与CCSA TC601联合发布《大数据平台在DATA+AI时代下的融合创新》\\
\\
大数据技术标准推进委员会\\
\\
25次阅读\\
\\
2026-05-27 08:08:21](https://www.modb.pro/db/2059426443151630336) [收好这份参会指南！明日与腾讯云大数据共同探索Agentic AI浪潮下的企业数智融合新范式\\
\\
腾讯云大数据\\
\\
23次阅读\\
\\
2026-06-05 08:17:20](https://www.modb.pro/db/2062690196253138944) [腾讯云面向Agent升级数据平台：DataBuddy、WeData与AI原生数据底座亮相\\
\\
腾讯云大数据\\
\\
21次阅读\\
\\
2026-06-08 10:34:19](https://www.modb.pro/db/2063811831173570560) [本体技术研讨会成功举办，多行业实践与标准建设同步推进\\
\\
大数据技术标准推进委员会\\
\\
16次阅读\\
\\
2026-05-28 09:44:31](https://www.modb.pro/db/2059813033699008512) [IEEE算电协同国际标准启动会召开，IEEE数字信任标委会加速可信电力应用标准布局\\
\\
大数据技术标准推进委员会\\
\\
16次阅读\\
\\
2026-05-26 09:42:55](https://www.modb.pro/db/2059087855629197312) [一图看懂腾讯云Agent-Ready数据平台\\
\\
腾讯云大数据\\
\\
15次阅读\\
\\
2026-06-08 10:34:20](https://www.modb.pro/db/2063811834508042240)

[朱洁](https://www.modb.pro/u/615436)

关注

[150\\
\\
文章](https://www.modb.pro/u/615436) [12\\
\\
粉丝](https://www.modb.pro/u/615436) [74K+\\
\\
浏览量](https://www.modb.pro/u/615436)

![暂无图片](https://js-cdn.modb.cc/image/svgs/likes.png)

获得了15次点赞

![暂无图片](https://js-cdn.modb.cc/image/svgs/comment.png)

内容获得19次评论

![暂无图片](https://js-cdn.modb.cc/image/svgs/star.png)

获得了11次收藏

热门文章

[Palantir Ontology 核心概念解读\\
\\
2025-06-034269浏览](https://www.modb.pro/db/1929740845025079296) [Palantir ontology 与传统知识图谱区别\\
\\
2025-08-113010浏览](https://www.modb.pro/db/1954726227214872576) [Palantir决策模拟：从Ontology到AIP的What-if推演引擎\\
\\
2025-06-112840浏览](https://www.modb.pro/db/1932616121073545216) [逻辑统一，物理解耦：揭秘Palantir的数据虚拟化引擎\\
\\
2025-06-162652浏览](https://www.modb.pro/db/1934435224495075328) [业务逻辑即工具：Palantir 如何构建安全可靠的企业级 AI 助手\\
\\
2025-07-072570浏览](https://www.modb.pro/db/1942056220555227136)

最新文章

[一年爆卖370亿、利润翻三倍！拆解泡泡玛特的“造富神话”与隐忧\\
\\
2026-06-0816浏览](https://www.modb.pro/db/2063812964487094272) [2026 AI 商业化底牌：是谁赚走了大模型的钱？\\
\\
2026-05-2532浏览](https://www.modb.pro/db/2058734953609912320) [深度拆解：Palantir 业绩狂飙背后的秘密武器——AIP Bootcamp\\
\\
2026-05-11116浏览](https://www.modb.pro/db/2053697205585383424) [软件流水线的瓦解：AI Coding 时代的岗位大洗牌与生存指南\\
\\
2026-05-0640浏览](https://www.modb.pro/db/2051867151997427712) [百万 Token 治不好 AI 的失忆症：大模型时代的“记忆”底牌\\
\\
2026-05-0643浏览](https://www.modb.pro/db/2051867148264497152)

领墨值

有奖问卷

[意见反馈](https://www.modb.pro/datalk/topic/11111)

![暂无图片](https://js-cdn.modb.cc/image/modb666.jpg)

客服小墨

### 来源 8: [PDF] Palantir— —深挖政府大数据的神秘独角兽

- URL: https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf
- 精读方法：firecrawl-scrape

\[Table\_InvestInfo\]
投资评级 优于大市 维持

市场表现

资料来源：海通证券研究所

相关研究
\[Table\_ReportInfo\]

\[Table\_ReportInfo\] 《计算机行业跟踪周报第 228 期：聚焦近期港股和美中概小市值 IT 行业公司表现》
2021.02.23
《从恒生电子投资赢时胜，看金融科技行

《从恒生电子投资赢时胜，看金融科技行业的平台化趋势》2021.02.22
《区块链和人工智能已成为领先金融科

《区块链和人工智能已成为领先金融科技企业技术布局重点》2021.02.21

Tel:(021)23219392

分析师\[Table\_AuthorInfo\]:郑宏达

证书:S0850516050002

分析师:洪琳

Email: [hl11570@htsec.com](mailto:hl11570@htsec.com)

Email: [ycl12224@htsec.com](mailto:ycl12224@htsec.com)

证书:S0850519050002
分析师:黄竞晶

分析师:黄竞晶

分析师:于成龙

证书:S0850518090004

Tel:(021)23154174

海通 AI 产业链深度研究（9）：Palantir—
—深挖政府大数据的神秘独角兽
\[Table\_Summary\]

\[Table\_Summary\]
投资要点：

l 专注政企大数据智能化，神秘独角兽 Palantir 市值已超 500 亿。Palantir 于 2020
年 9 月 30 日于纽交所直接上市（股票代码“PLTR”），截至 2021 年 2 月 19 日，
公司股票涨跌幅达 164%，市值规模超 500 亿美元。Palantir 目前提供十七种行业解决方案，客户行业覆盖军事、警务、金融、制造、网络、医疗健康等多个领域，我们认为该公司业务未来可能继续延伸拓展至其他行业。根据公司招股书，
Palantir 软件在全球商业和政府部门的总潜在市场约为 1190 亿美元。其中，商业领域的 TAM 约为 560 亿美元。政府机构的总潜在市场为 630 亿美元，美国政府部门为 260 亿美元，国际政府部门的 TAM 为 370 亿美元。根据公司 Palantir 年度报告，2020 年公司全年收入为 11 亿美元，同比增长 47％。

l Palantir 美国政府客户粘性高，企业与海外客户存在增长空间。2020 年前三季度，Palantir 政府客户的收入增长了 1.774 亿美元或，较 2019Q3 增长 73％；其中，1.485 亿美元的增长额归属于现有政府客户，主要集中于美国。政府客户与美国本土客户占比较 2019 同期有所提升，最新财报显示，2020 年前三季度，公司收入 55%来自政府机构，而 2019 年该数字为 47%，增长了 8 个百分点。按地区划分，公司收入 51%来自美国客户，而 2019 年该数字为 38%，增长了 13 个百分点。

l Palantir 深挖大数据图分析商业化潜力，利用图分析（graph analytics）技术协助政府与企业解决实际问题。知识图谱的前期应用场景以谷歌、雅虎等为代表，
采用搜索引擎的模式以获取实际知识为目的。近年来，知识图谱的应用扩展至国防、公安、金融、工业、医疗、司法等小规模复杂应用场景。以实体概念为节点
（vertex），以关系为边（edge），知识图谱将实体抽象为顶点，将实体之间的关系抽象为边，通过结构化的形式对知识进行建模和描述，并将知识可视化。细分行业的全新应用场景以及复杂的行业需求向知识图谱企业提出了全新的挑战。

l Palantir 拓展图分析垂直领域行业应用，知识图谱（knowledge graph）技术步入下半场。 Gotham 和 Foundry 两大产品为政府机构和企业提供十多种解决方案，覆盖军事、警务、金融、制造、网络、医疗健康等多个领域。Palantir 利用不同来源的结构化和非结构化数据，将数据之间千丝万缕的联系以可视化图形呈现出来，从而使人脑与大数据分析结合，提升客户的决策洞察力。图分析技术通过帮助客户整理以往看似毫无关系的数据，创造一种可见的并且可加以利用的知识图谱，形成人脑决策和计算机智能共生的大数据分析环境及工具系统。

* * *

目 录

1. 专注政企大数据智能化，神秘独角兽 Palantir 市值超 500 亿 ..... 5
2. Palantir 深挖大数据图分析商业化潜力 ..... 5
   2.1 美国政府官方合作伙伴，逐步拓展至商业领域 ..... 5
   2.2 Gotham 与 Foundry 两大平台为政府与企业提供全栈式服务 ..... 6
3. 疫情加速软件部署，Palantir 收入增速加快 ..... 7
4. 客户商业化三阶段，高粘性留存成为收入增长源动力 ..... 9
   4.1 获客-扩张-留存，长期留存客户收入进一步增加 ..... 9
   4.2 美国政府客户粘性高，企业与海外客户存在增长空间 ..... 9
5. Palantir 开拓垂直领域应用：知识图谱技术进入下半场 ..... 10
   5.1 垂直行业知识图谱应用不断深化 ..... 10
   5.2 Palantir 独树一帜，为各垂直领域提供行业技术解决方案 ..... 11
   5.2.1 以军事国防为例

* * *

图目录

图 1 2010 至 2020 年 Palantir 营业收入及增长率 .....5
图 2 Palantir 公司发展大事记.....6
图 3 2019Q3 和 2020Q3 Palantir 收入变化情况 .....8
图 4 2019Q3 和 2020Q3 Palantir 经营收入（亏损）情况.....8
图 5 2019Q3 和 2020Q3 Palantir 费用细分变化情况 .....8
图 6 2019Q3 和 2020Q3 Palantir 边际贡献率和毛利率 .....8
图 7 2019Q3 和 2020Q3 Palantir 企业与政府客户收入占比 .....10
图 8 2019Q3 和 2020Q3 Palantir 各地区收入占比.....10
图 9 Palantir 软件为多行业提供解决方案 .....11
图 10 Palantir 战场空间感知态势界面图 ..

* * *

行业研究〃信息服务行业

# 表目录

表 1 Palantir Gotham 平台应用程序及模块 ... 7

表 2 Palantir Foundry 平台及应用程序 ... 7

请务必阅读正文之后的信息披露和法律声明

* * *

1. 专注政企大数据智能化，神秘独角兽 Palanti” 市值超
   500 亿

Palantir 于 2020 年 9 月 30 日于纽交所直接上市（股票代码“PLTR”），公司作为美国政府机构的合作伙伴备受关注。截至 2021 年 2 月 19 日，公司股票涨跌幅达 164%，
市值规模已超 500 亿美金。

根据公司官网，Palantir 目前提供十七种行业解决方案。Palantir 服务的客户行业覆盖军事、警务、金融、制造、网络、医疗健康等多个领域，我们认为该公司业务未来可能继续延伸拓展至其他行业。

根据公司招股书，Palantir 软件在全球商业和政府部门的总潜在市场（total
addressable market，TAM）约为 1190 亿美元。其中，商业领域的 TAM 约为 560 亿美元。政府机构（包括美国其盟友以及与自由民主国家持一致价值的其他国家/地区的政府机构）的 TAM 为 630 亿美元，美国政府部门为 260 亿美元，国际政府部门的 TAM 为
370 亿美元。

根据公司 Palantir 年度报告，2020 年公司全年收入为 11 亿美元，同比增长 47％。

图1 2010 至 2020 年 Palantir 营业收入及增长率

从公司的发展历程来看，Palantir 成立于 2003 年，最早负责开发反恐行动中所需的应用软件。2008 年发布了首个数据平台 Palantir Gotham（以下简称“ Gotham”），为情报领域的用户提供服务，帮助客户从纷繁复杂的信息中识别所需的重要情报。美国的国防部门利用该平台调查潜在危险，目前 Gotham 正在美国及其盟国的政府机构中广泛使用。

资料来源：Palantir 招股书，海通证券研究所

2. Palantir 深挖大数据图分析商业化潜力

* * *

行业研究〃信息服务行业

件平台 Palantir Foundry（以下简称“ Foundry”），以应对大公司遇到的一系列常见挑 战。Foundry 不仅正在成为单个机构的中心操作系统，而且也正在成为整个行业的中心 操作系统。2017 年，Palantir 与空中客车公司达成合作伙伴关系，现今已连接了来自全 球一百多家航空公司 9000 余架飞机的航空数据。

\[Table\_Pic 图2 **Palantir** Pe\]公司发展大事记

资料来源：公司招股书，Frorbes，Insider，Quartz，CNBC，海通证券研究所

## Palantir 的图分析技术最早应用于美国政府机构，重要客户包括美国国家安全局

（NSA），美国联邦调查局（FBI），美国中央情报局（CIA）和很多其他的美国反恐和军 事机构。Palantir 曾起诉美国陆军，使 1994 年《联邦采购精简法案》在美军中得以更好 地执行。该法案要求美国联邦政府在尝试自行研究开发软件之前考虑市场上可用的软件， 从而使美军开始购买商业化软件。

根据公司招股书，Palantir 软件在全球商业和政府部门的总潜在市场（total addressable market，TAM）约为 1190 亿美元。其中，商业领域的 TAM 约为 560 亿美 元。政府机构（包括美国其盟友以及与自由民主国家持一致价值的其他国家/地区的政府 机构）的 TAM 为 630 亿美元，美国政府部门为 260 亿美元，国际政府部门的 TAM 为 370 亿美元。

# 2.2 Gotham 与 Foundry 两大平台为政府与企业提供全栈式服务

Palantir 拥有两个软件平台 Gotham 和 Foundry，提供了行业客户运营所需的关键 基础架构。通过从源数据传播到共享分析的细粒度访问控制，Palantir 可保护每个数据， 分析，决策和元数据的安全。每个平台都包含面向用户的应用程序，这些应用程序针对 使用它们的特定行业和部门。

在 Gotham 和 Foundry 中，不同技术能力的用户可以进行有效协作。数据工程师可 以集成新的数据源，分析师可以清理和转换数据，数据科学家可以编写模型，业务用户 可以执行日常工作流，而高级领导者可以制定关键决策。这两个平台既可以单独使用， 也可以捆绑在一起作为统一的生态系统。尽管 Gotham 和 Foundry 在特定功能上有所不 同，两者均为 Palantir 客户提供了中央操作系统。两者在操作方法上保持一致，并且都 可以部署在几乎任何环境中。

请务必阅读正文之后的信息披露和法律声明

* * *

表 1 Palantir Gotham 平台应用程序及模块

| 应用/模块 | 功能 |
| --- | --- |
| Graph | Graph提供了类似于白板的界面，用户可以在图中创建或编辑数据，还可以通过插件进行时间分析，网络分析，识别数据模式。 |
| Gaia | Gaia允许用户通过共享的实时地图跟踪实时数据，以便每个人都可以对相同的信息采取行动。用户可以将对象从其他Gotham应用程序直接拖放到Gaia中，以便协同进行计划和情报收集。 |
| Dossier | Dossier是一个实时协作文档编辑器，用户可以跨团队和组织进行协作，以在Gotham生态系统内创建实时和动态情报产品 |
| Stencil | Stencil是一个结构化的表单输入工具，支持协作数据输入和报告创作，可以执行结构化的内容创建，同时支持自定义的审批流程。 |
| Video | Video是一种允许多种格式的实时和历史视频数据进行交互的应用程序。用户可以查看平台中的视频素材，并使用地理空间信息和基于其他数据源的叠加来增强原始素材，提高态势感知能力和实时决策能力。 |
| Table | Table是一个交互式的自上而下的搜索工具，用于快速检索大量事件型信息。用户可以过滤数十亿条记录，在数据集种发现可疑点并可视化特定结果。 |
| Ava | Ava是一个人工智能系统，可扫描数十亿个数据点，全天候针对数据流进行调查，以帮助国防和情报部门等机构的研究人员识别模式和联系。 |
| Forward | Forward可以在不稳定甚至无信号的网络环境中过提供同步的Gotham服务。一个指挥部的士兵可以使用Forward笔记本电脑在总部和现场人员之间以及与来自世界各地不同指挥部的士兵之间同步数据和分析。 |
| Mobile | Mobile是携载Gotham的移动设备，支持实时和分布式操作。借助Android或iOS设备，用户可以归档现场报告，上传照片和视频，跟指挥中心实时协作，以把控任务运行并对变化的环境做出反应。 |

资料来源：公司招股书、海通证券研究所

表 2 Palantir Foundry 平台及应用程序

| 应用程序 | 功能 |
| --- | --- |
| Monocle | Monocle使用能够使用图形界面访问和管理数据链条，比如访问和管理产业链上下游的各种数据 |
| Contour | Contour支持自上而下对大规模数据进行研究，用户可以在Foundry中过滤、添加以及可视化数据集 |
| Object Explorer | Object Explorer允许用户与表示为对象（如客户、设备或工厂）的数据进行交互，支持搜索索引数据并遍历对象之间的连接 |
| Fusion | Fusion Foundry的电子表格环境，用户可以创建单元格引用和函数，以创建新的数据集或报表 |
| Workshop | Workshop帮助用户在低代码或无代码的环境中构建应用程序，可以动态地构建交互式工作流 |
| Vertex | Vertex使用可以模拟变化并执行假设性分析，帮助机构优化运营 |
| Code Authoring | Code Authoring是为数据工程师设计的一套应用，便于数据工程师在平台上进行开发 |
| Quiver | Quiver是一个多维图表应用程序，用于分析非常大的时间序列数据集，例如来自机器传感器的流式数据 |
| AI/ML | AI/ML将人工智能和机器学习与Foundry平台的核心组件集成，用户可以进行调用以实现各种功能 |
| Code Workbooks | Code Workbooks每个计算步骤都可以保存为Foundry数据集，可供其他应用程序使用以及跨工作簿重用 |
| Reports | Reports允许用户动态发布并实时更新工作及数据 |

资料来源：公司招股书、海通证券研究所

高需求推动公司收入增速加快，20 年前三季度同比增速达 50% 。2020 年前三季度，
公司收入达 7.706 亿美元，与 2019 年前三季度 5.132 亿美元的收入相比，同比增长 50官城不计入股票薪酬，公司经营业绩有显着改善。2020 年前三季度，Palantir 经营亏损约
10 亿美元；若不计入股票薪酬，则实现营业利润 1180 万美元。根据 Yahoo Finance
数据，20201 年 2 月 19 日公司 PS 估值约为 60 倍。

* * *

本次新冠疫情使许多潜在客户意识到，软件应用部署刻不容缓。以往内部软件开发部署的工作可能需要数月甚至数年，现在几天之内就可以准备就绪。因此，客户越来越多地采用 Palantir 的软件并加速与公司签订合同，以适应危机期间的工作状态。

截至第三季度财报发出，新冠疫情疫情并未对 Palantir 的经营业绩造成重大不利影响。针对疫情，Palantir 采取了预防措施，暂停员工和员工的所有不必要的商务旅行，
公司所有主要办事处临时关闭。大多数员工远程工作，差旅和办公室有关的支出有所减少，但是公司软件平台有效运行的能力并未受太大影响。

不计入股票薪酬，Palantir 2020Q3 实现扭亏。公司主要收入方式为销售订阅，若不计入股票薪酬，公司经营业绩有显着改善。2020 年前三季度，Palantir 经营亏损约
10 亿美元；若不计入股票薪酬，则实现营业利润 1180 万美元。

图3 2019Q3 和 2020Q3 Palantir 收入变化情况

资料来源：Palantir 第三季度财报，海通证券研究所

图4 2019Q3 和 2020Q3 Palantir 经营收入（亏损）情况

资料来源：Palantir 第三季度财报书，海通证券研究所

毛利率保持 60% 以上，因上市后员工期权激励费用化，毛利率短期有所下滑。根据第三季度财报， Palantir 2020 年前三季度毛利率比 2019 年前三季度下降了 5％。毛利率下降的主要原因是员工限制性股票满足条件行权带来的处臵费以及优先股转换普通股产生的保证金费用。另外，公司产生了与上市准备活动相关的财务咨询、会计、法律和其他专业服务相关的一般管理费用，共 5620 万美元。若不计入股票薪酬，
Palantir2020 年前三季度毛利率较 2019 年同期增长 8％。

资料来源：Palantir2020Q3 财报，海通证券研究所

图5 2019Q3 和 2020Q3 Palantir 费用细分变化情况

资料来源：Palantir2020Q3 财报，海通证券研究所

* * *

行业研究〃信息服务行业

# 4\. 客户商业化三阶段，高粘性留存成为收入增长源动力

Palantir 将“边际贡献率”（contribution margin）作为公司的重要经营指标。该 指标的定义为“收入减去收入成本（cost of revenue）、营销费用（不包括股票薪酬） 再除以收入”。按边际贡献率指标来看，Palantir 的边际贡献率由 2019 Q3 的 1 6% 上升 至 2020Q3 的 51 % ，实现了三倍的增长。

## 4.1 获客- 扩张- 留存，长期留存客户收入进一步增加

在付费方面，公司将客户分为三个发展阶段：获客（Acquire）、扩张（E xp。 ） 和留存（S cale）。 Palantir 根据每个客户所处的阶段提供相应的服务。

对于获客阶段的客户，Palantir 愿意提供试用以让用户体验到软件所带来的切实便 利，这通常是完全亏损经营。如果在一个日历年结束时，某年客户产生的收入少于 10 万美元，公司则将该类客户定义为“Acquire”阶段。客户可能会因评估软件而支付名 义费用，但对公司绩效没有重大影响。2019 年，处在获客阶段的用户产生了 60 万美元 的收入，产生了 6540 万美元的贡献损失。2020 年前三季度，这些客户产生了 4,110 万 美元的收入，产生了 420 万美元的贡献亏损。

扩张阶段的客户收入的获得说明了公司软件为用户带来了正向的价值和影响。如果 在一个日历年结束时，某客户产生的收入超过 10 万美元并且其帐户年末产生负边际贡 献，则该客户处在“Expand”阶段。2019 年，处于扩张阶段的客户产生了 1.763 亿美 元的收入，边际贡献率为-43％。2020 年前三季度，这些客户创造了 2.544 亿美元的收 入，边际贡献率为 41％。

在留存阶段，公司的收入成本通常会下降，在留存阶段用户的边际贡献率会有所提 高。如果在一个日历年结束时，某客户产生的收入超过 10 万美元并且其帐户年末已确 产生正边际贡献，曾该客户处在“Scale”阶段。2019 年，处于留存阶段的客户产生了

5.657 亿美元的收入，贡献率为 55％。2020 年前三季度，这些客户创造了 4.522 亿美 元的收入，贡献率为 69％。 根据 Palantir 公司三季度财报，随着平台在客户运营中使用量增加，软件为客户提 供的价值也会显著增加。在留存阶段，客户在使用已经安装好的平台系统时会更加自如， 可以基于 Palantir 的运维系统（O&M service）开发自身的软件和应用程序。随着公司 在软件平台部署和管理维护方面越来越高效，长期来看，公司的客户都将逐渐进入留存 阶段。

## 4.2 美国政府客户粘性高，企业与海外客户存在增长空间

根据招股书数据，2019 年 Palantir 53％的收入来自商业客户，47％的收入来自政 府机构；按地区类型划分，Palantir 2019 年 40%的收入来自美国客户，其余 60％来自 国外客户。截至 2019 年底，Palantir 收入排名前 20 位的客户使用该平台的平均年限为

6.6 年。截至 2020Q3，公司预计未来待履约合同年限为 3.6 年。 根据 2020 年第三季度财报数据，截至 2020 年 9 月 30 日，Palantir 拥有 132 个客 户，其中包括各个商业领域的领先公司以及世界各地的政府机构。2020 年前三季度， 公司收入的 45％来自商业客户，而 55％来自政府机构。按地区类型划分，公司收入的 51%来自美国客户，其余 49％来自国外客户。 2020 年前三季度，Palantir 政府客户的收入增长了 1.774 亿美元，较 2019Q3 增长 73％；其中，1.485 亿美元的增长额归属于现有政府客户，主要集中于美国。商业客户 的收入增张了 8000 万美元，较 2019Q3 增长 30％；其中，6,710 万美元的增长额来自请务必阅读正文之后的信息披露和法律声明

* * *

现有客户。

我们认为，Palantir 美国本土政府客户对 Palantir 整体营收的逆势上升产生了积极作用。商业客户与非本土客户占比较 2019 同期有所降低原因可能是受到疫情影响，政府稳定性较商业客户更高，抗击疫情对经济的影响的能力更强。长期来看，政府将仍然是 Palantir 软件应用服务的重点对象，但企业客户与海外客户方面也存在一定空间。

图7 2019Q3 和 2020Q3 Palantir 企业与政府客户收入占比

资料来源：Palantir2020Q3 财报，海通证券研究所

图8 2019Q3 和 2020Q3 Palantir 各地区收入占比

资料来源：Palantir2020Q3 财报，海通证券研究所

5. Palantir 开拓垂直领域应用：知识图谱技术进入下半场

Palantir 为政府与企业服务提供全栈式多场景的技术解决方案。其中，图分析是
Palantir 运用的重要技术之一。知识图谱（Knowledge Graph）的概念由谷歌 2012 年正式提出，旨在搭建更智能的搜索引擎。目前，随着智能信息服务应用的不断发展，知识图谱已被广泛应用于智能搜索、智能问答、个性化推荐、情报分析、反欺诈等领域。

5.1 垂直行业知识图谱应用不断深化

按应用领域划分，知识图谱分为通用知识图谱与行业知识图谱。

行业知识图谱以行业或企业内部的数据为主要来源，通常包含本体工程和规则型知识。知识结构更加复杂，通常要求快速扩大规模，构建行业壁垒。知识抽取的质量要求很高，较多的依靠从企业内部的结构化、非结构化以及半结构化数据进行联合抽取，需要依靠人工进行审核校验，来保证质量。行业知识图谱的应用形式更加全面，除搜索问答外，还包括决策分析、业务管理等，并对推理的要求更高，并有较强的可解释性要求。主要领域有电商、金融、农业、安全、医疗等等。

* * *

行业研究〃信息服务行业

# 5.2 Palantir 独树一臶，为各垂直领域提供行业技术解决方案

根据开发者社区网站掘金，国外图分析商业化的公司包括：Neo4j，TigerGraph， cambridge-intelligence 等，国内涉及图数据库的公司包括：欧若数网（Nebula Graph光称 费马科技（TuGraph）、蚂蚁金服（Geabase）等；然而 Palantir 是目前唯一一家上市公 司，为政府和企业客户提供全栈式多场景的行业技术解决方案。

根据公司官网，Palantir 目前提供十七种行业解决方案。Palantir 服务的客户行业覆 盖军事、警务、金融、制造、网络、医疗健康等多个领域，我们认为公司业务未来可能 继续延伸拓展至其他行业。

图9 **Palantir 软件为多行业提供解决方案**

资料来源：Palantir 公司官网，Palantir 招股书，海通证券研究所

**5.2.1** 以军事国防为例 据腾讯云援引大数据文摘微信公众号，Palantir 为美国军队提供的大数据分析技术 已经深入美国核心情报军事机构，能够指导其人员分析情报、打击目标，再将军事行动 中获得的新情报与现有大数据进行融合更新，极大提高了情报分析和决策指挥能力。 Palantir 将多个军事情报领域的海量数据打通融合，包括非结构化和结构化数据流， 如链接图，电子表格，电话，文档，网络数据，传感器数据，甚至动态视频、图像等。 这整合了美军等多方原本孤立的数据源（如军事情报部门和陆海空、海军陆战队等组织 机构的数据）。 基于通用的大数据融合和可视化分析平台，指挥人员和调度人员能在单一系统内解 决所有问题，包括敌人的活动情报分析（情报报告，事件行为等），关联分析（背景、 关联、跟踪、反应等）和预判决策等。Palantir 基于本体映射的全量多模态数据融合和 协同分析框架，支持对地理空间上分散的人、装备、环境、事件等进行大规模实时监测 和因果分析，以指导复杂战场环境下的军事行动。这些大数据技术已被美国军方广泛运 用于战场态势分析和预测，如定位伊拉克战场可能存在的炸弹或地雷位臵，帮助美军在 巴格达规划一条被袭概率最小的路径，或者分析亚丁湾海盗活动的热点区域。请务必阅读正文之后的信息披露和法律声明

* * *

图10 Palantir 战场空间感知态势界面图

资料来源：腾讯云，大数据文摘，海通证券研究所

图11 Palantir 阿富汗战场的融合分析功能界面图

资料来源：腾讯云，大数据文摘，海通证券研究所

5.2.2 以金融欺诈解决方案为例

Palantir 凭借其为政府服务的影响力，在 2009 年将摩根大通纳入首批非政府客户。后来 Palantir 帮多家银行追回纳斯达克前主席麦道夫庞氏骗局的数十亿美金，名声大振，
其出色的大数据技术获得华尔街金融大鳄们的认可，目前许多银行、保险、对冲基金，
包括美国证券交易委员会都在使用 Palantir 的产品和技术。

反欺诈是金融领域的一项关键业务，信用评级、风险管理、关联交易、洗钱、逃税等都涉及此项分析内容。金融是信息化程度极高的行业，拥有海量的相关数据。Palantir
的平台可将许多孤立的金融环境数据汇集到统一分析系统，通过回归关联建模、频繁项分析和知识图谱、社交网络等机器学习和大数据可视化技术挖掘出有价值的信息。

图12 Palantir 金融反欺诈界面图

资料来源：腾讯云，大数据文摘，海通证券研究所

Palantir 利用大数据图分析技术可将数据间有价值的关联关系深度挖掘出来，形成完整的证据链条，通过间接关联分析解决线索中断的问题。Palantir 通过与美国各州的警队合作，将遍布在城市及乡镇各处卡口、警车上的摄像头拍下的照片及视频入库存储，
与警方的人口数据库、犯罪数据库、DNA 数据库等进行深度融合，提取出如车牌号码、人脸、DNA 及体态等关键信息。这些信息虽然繁琐且表面看起来关联性不强，但其间却蕴藏着各式各样的关系（强、弱；直接、间接等），联系之间更是隐藏着深层的信息。通

资料来源：腾讯云，大数据文摘，公司官网，海通证券研究所

* * *

过预测性警务模型分析历史犯罪数据，还能计算出最有可能在警察下一次执勤时发生犯罪活动的地点。

2011 年，美国海关的一名情报人员在墨西哥被一群毒贩射杀，美国警方随即展开名为 Operation Fallen Hero 的行动，利用 Palantir 大数据技术，在浩瀚的人物、地点以及事件等等元素中间整理出复杂的关系链，同时融合联邦探员自身掌握的信息，如大毒枭们，及其下线的融资渠道以及运毒路线等。通过对与本案相关多源数据关系的可视化展现、交互分析，Palantir 将分散隐蔽的证据有效衔接，筛选排除干扰信息，最终将证据链完整呈现。警方通过资金往来以及人际关系网络分析理清了关键人物以及关键联系，
并确定了主要嫌疑犯，逮捕了 600 多名毒贩和大批毒品武器。

图14 Palantir 锁定嫌疑人分析功能界面图

资料来源：腾讯云，大数据文摘，海通证券研究所

图15 Palantir 其他大数据可视化功能界面图

资料来源：腾讯云，大数据文摘，海通证券研究所

6. 投资建议

我们认为，AI 在政企大数据上的应用深度和广度都在不断提升，如 Palantir 由政府客户开始，将知识图谱能力向多个垂直领域渗透，以平台叠加应用模块的方式使 AI 能力规模化输出，同时使政企客户高留存以保证长期成长性。我们认为，未来通过平台化和标准化应用模块将 AI 能力对 G 端和 B 端输出将加快 AI 商业化落地，打开更大的市场空间。

7. 风险提示

AI 行业落地进展缓慢。

* * *

信息披露

分析师声明

\[Table\_ 郑宏达 Analyst计算机行业 s\]
洪琳 计算机行业

洪琳 计算机行业黄竞晶 计算机行业

黄竞晶 计算机行业于成龙 计算机行业

于成龙 计算机行业

本人具有中国证券业协会授予的证券投资咨询执业资格，以勤勉的职业态度，独立、客观地出具本报告。本报告所采用的数据和信息均来自市场公开信息，本人不保证该等信息的准确性或完整性。分析逻辑基于作者的职业理解，清晰准确地反映了作者的研究观点，
结论不受任何第三方的授意或影响，特此声明。

分析师负责的股票研究范围

\[Table\_Reports\] 重点研究上市公司： 易华录, 四维图新, 佳都科技, 创业慧康, 京北方, 广联达, 用友网络, 金溢科技, 锐明技术, 中控技术, 拉卡拉, 捷顺科技, 恒华科技, 拓尔思, 鼎捷软件, 中电兴发, 航天信息, 优刻得- W, 金山办公, 中望软件, 中孚信息, 万兴科技, 云从科技, 海康威视, 启明星辰, 长亮科技, 金蝶国际, 久远银海, 京东数科, 美亚柏科

| 1.投资评级的比较和评级标准：以报告发布后的6个月内的市场表现为比较标准，报告发布日后6个月内的公司股价（或行业指数）的涨跌幅相对同期市场基准指数的涨跌幅；2.市场基准指数的比较标准：A股市场以海通综指为基准；香港市场以恒生指数为基准；美国市场以标普500或纳斯达克综合指数为基准。 | 类别 | 评级 | 说明 |
| --- | --- | --- | --- |
| 股票投资评级 | 优于大市 | 预期个股相对基准指数涨幅在10%以上; |  |
| 中性 | 预期个股相对基准指数涨幅介于-10%与10%之间; |  |  |
| 弱于大市 | 预期个股相对基准指数涨幅低于-10%及以下; |  |  |
| 无评级 | 对于个股未来6个月市场表现与基准指数相比无明确观点。 |  |  |
| 行业投资评级 | 优于大市 | 预期行业整体回报高于基准指数整体水平10%以上; |  |
| 中性 | 预期行业整体回报介于基准指数整体水平-10%与10%之间; |  |  |
| 弱于大市 | 预期行业整体回报低于基准指数整体水平-10%以下。 |  |  |

法律声明

本报告仅供海通证券股份有限公司（以下简称“本公司”）的客户使用。本公司不会因接收人收到本报告而视其为客户。在任何情况下，
本报告中的信息或所表述的意见并不构成对任何人的投资建议。在任何情况下，本公司不对任何人因使用本报告中的任何内容所引致的任何损失负任何责任。

本报告所载的资料、意见及推测仅反映本公司于发布本报告当日的判断，本报告所指的证券或投资标的的价格、价值及投资收入可能会波动。在不同时期，本公司可发出与本报告所载资料、意见及推测不一致的报告。

市场有风险，投资需谨慎。本报告所载的信息、材料及结论只提供特定客户作参考，不构成投资建议，也没有考虑到个别客户特殊的投资目标、财务状况或需要。客户应考虑本报告中的任何意见或建议是否符合其特定状况。在法律许可的情况下，海通证券及其所属关联机构可能会持有报告中提到的公司所发行的证券并进行交易，还可能为这些公司提供投资银行服务或其他服务。

* * *

\[Table\_PeopleInfo\]
海通证券股份有限公司研究所

路 颖 所长
(021)23219403 [luying@htsec.com](mailto:luying@htsec.com)

高道德 副所长
(021)63411586 [gaodd@htsec.com](mailto:gaodd@htsec.com)

邓 勇 副所长
(021)23219404 [dengyong@htsec.com](mailto:dengyong@htsec.com)

荀玉根 副所长
(021)23219658 [xyg6052@htsec.com](mailto:xyg6052@htsec.com)

(021)23219658 [xyg6052@htsec.com](mailto:xyg6052@htsec.com)

涂力磊 所长助理
(021)23219747 [tll5535@htsec.com](mailto:tll5535@htsec.com)

余文心 所长助理
(0755)82780398 [ywx9461@htsec.com](mailto:ywx9461@htsec.com)

策略研究团队荀玉根(021)23219658 [xyg6052@htsec.com](mailto:xyg6052@htsec.com)

孔维娜(021)23219223 [kongwn@htsec.com](mailto:kongwn@htsec.com)
潘莹练(021)23154122 [pyl10297@htsec.com](mailto:pyl10297@htsec.com)

周 霞(021)23219807 [zx6701@htsec.com](mailto:zx6701@htsec.com)
姜珮珊(021)23154121 [jps10296@htsec.com](mailto:jps10296@htsec.com)
联系人

联系人王巧喆(021)23154142 [wqz12709@htsec.com](mailto:wqz12709@htsec.com)

曾 知(021)23219810 [zz9612@htsec.com](mailto:zz9612@htsec.com)
郑子勋(021)23219733 [zzx12149@htsec.com](mailto:zzx12149@htsec.com)
刘 溢(021)23219748 [ly12337@htsec.com](mailto:ly12337@htsec.com)

张向伟(021)23154141 [zxw10402@htsec.com](mailto:zxw10402@htsec.com)
李姝醒 [lsx11330@htsec.com](mailto:lsx11330@htsec.com)
曾 知(021)23219810 [zz9612@htsec.com](mailto:zz9612@htsec.com)

政策研究团队李明亮(021)23219434 [lml@htsec.com](mailto:lml@htsec.com)

联系人吴信坤 021-23154147 [wxk12750@htsec.com](mailto:wxk12750@htsec.com)

政策研究团队李明亮(021)23219434 [lml@htsec.com](mailto:lml@htsec.com)
吴一萍(021)23219387 [wuyiping@htsec.com](mailto:wuyiping@htsec.com)

朱 蕾(021)23219946 [zl8316@htsec.com](mailto:zl8316@htsec.com)
周洪荣(021)23219953 [zhr8381@htsec.com](mailto:zhr8381@htsec.com)

公用事业吴 杰(021)23154113 [wj10521@htsec.com](mailto:wj10521@htsec.com)

曹雅倩(021)23154145 [cyq12265@htsec.com](mailto:cyq12265@htsec.com)
联系人

联系人房乔华 021-23219807 [fqh12888@htsec.com](mailto:fqh12888@htsec.com)

房乔华 021-23219807 [fqh12888@htsec.com](mailto:fqh12888@htsec.com)
郑 蕾 23963569 [zl12742@htsec.com](mailto:zl12742@htsec.com)

郝艳辉(010)58067906 [hyh11052@htsec.com](mailto:hyh11052@htsec.com)
毛云聪(010)58067907 [myc11153@htsec.com](mailto:myc11153@htsec.com)

梁广楷(010)56760096 [lgk12371@htsec.com](mailto:lgk12371@htsec.com)
孟 陆 86 10 56760096 [ml13172@htsec.com](mailto:ml13172@htsec.com)
周 航(021)23219671 [zh13348@htsec.com](mailto:zh13348@htsec.com)
朱赵明(021)23154120 [zzm12569@htsec.com](mailto:zzm12569@htsec.com)
彭 娉(010)68067998 [pp13606@htsec.com](mailto:pp13606@htsec.com)

陈星光(021)23219104 [cxg11774@htsec.com](mailto:cxg11774@htsec.com)
孙小雯(021)23154120 [sxw10268@htsec.com](mailto:sxw10268@htsec.com)

有色金属行业施 毅(021)23219480 [sy8486@htsec.com](mailto:sy8486@htsec.com)
陈晓航(021)23154392 [cxh11840@htsec.com](mailto:cxh11840@htsec.com)

涂力磊(021)23219747 [tll5535@htsec.com](mailto:tll5535@htsec.com)
谢 盐(021)23219436 [xiey@htsec.com](mailto:xiey@htsec.com)

郑景毅 [zjy12711@htsec.com](mailto:zjy12711@htsec.com)

谢 盐(021)23219436 [xiey@htsec.com](mailto:xiey@htsec.com)
金 晶(021)23154128 [jj10777@htsec.com](mailto:jj10777@htsec.com)

* * *

| 电子行业 | 煤炭行业 |
| --- | --- |
| 周旭辉 [zxh12382@htsec.com](mailto:zxh12382@htsec.com) | 李淼(010)58067998 |
| 联系人 | 戴元灿(021)23154146 |
| 肖隽狮021-23154139 [xjc12802@htsec.com](mailto:xjc12802@htsec.com) | 吴杰(021)23154113王涛(021)23219760 |
| 基础化工行业 | 计算机行业 |
| 刘威(0755)82764281 [lw10053@htsec.com](mailto:lw10053@htsec.com) | 郑宏达(021)23219392 |
| 刘海荣(021)23154130 [lhr10342@htsec.com](mailto:lhr10342@htsec.com) | 杨林(021)23154174 |
| 张翠翠(021)23214397 [zcc11726@htsec.com](mailto:zcc11726@htsec.com) | 于成龙(021)23154174 |
| 孙维容(021)23214931 [swr12178@htsec.com](mailto:swr12178@htsec.com) | 黄竟晶(021)23154131洪琳(021)23154137联系人杨蒙(0755)23617756 |
| 李智(021)23219392 [lz11785@htsec.com](mailto:lz11785@htsec.com) | 交通运输行业 |
| 非银行金融行业 | 虞楠(021)23219382 |
| 孙婷(010)50949926 [st9998@htsec.com](mailto:st9998@htsec.com) | 罗月江(010)567600 |
| 何婷(021)23219634 [ht10515@htsec.com](mailto:ht10515@htsec.com) | 李轩(021)23154652陈宇(021)23219442 |
| 李芳洲(021)23154127 [lfz11585@htsec.com](mailto:lfz11585@htsec.com) |  |
| 联系人任广博(010)56760090 [rgb12695@htsec.com](mailto:rgb12695@htsec.com) |  |
| 建筑建材行业 | 机械行业 |
| 冯晨阳(021)23212081 [fcy10886@htsec.com](mailto:fcy10886@htsec.com) | 佘炜超(021)23219816周丹zd12213@hts |
| 潘莹练(021)23154122 [pyl10297@htsec.com](mailto:pyl10297@htsec.com) | 吉晟(021)23154653赵玥炜(021)23219814联系人赵靖博zjb13572@hts |
| 申浩(021)23154114 [sh12219@htsec.com](mailto:sh12219@htsec.com) |  |
| 颜慧菁 [yhj12866@htsec.com](mailto:yhj12866@htsec.com) |  |
| 建筑工程行业 | 农林牧渔行业 |
| 张欣勏 [zxj12156@htsec.com](mailto:zxj12156@htsec.com) | 丁频(021)23219405陈阳(021)23212041联系人孟亚琦(021)23154396 |
| 军工行业 | 银行行业 |
| 张恒晅 [zhx10170@htsec.com](mailto:zhx10170@htsec.com) | 孙婷(010)50949926解巍巍xww12276@h林加力(021)23154395联系人董栋梁(021)23219356 |
| 张高艳0755-82900489 [zgy13106@htsec.com](mailto:zgy13106@htsec.com) |  |
| 联系人刘砚菲021-2321-4129 [lyf13079@htsec.com](mailto:lyf13079@htsec.com) |  |
| 家电行业 | 进纸轻工行业 |

|  | 电力设备及新能源行业 |  |
| --- | --- | --- |
| [lm10779@htsec.com](mailto:lm10779@htsec.com) | 张一弛(021)23219402 | [zyc9637@htsec.com](mailto:zyc9637@htsec.com) |
| [dyc10422@htsec.com](mailto:dyc10422@htsec.com) | 房青(021)23219692 | [fangq@htsec.com](mailto:fangq@htsec.com) |
| [wj10521@htsec.com](mailto:wj10521@htsec.com) | 曾彪(021)23219418 | [zb10242@htsec.com](mailto:zb10242@htsec.com) |
| [wt12363@htsec.com](mailto:wt12363@htsec.com) | 徐柏乔(021)23219171 | [xbq6583@htsec.com](mailto:xbq6583@htsec.com) |
|  | 通信行业 |  |
| [zhd10834@htsec.com](mailto:zhd10834@htsec.com) | 朱劲松(010)50949926 | [zjs10213@htsec.com](mailto:zjs10213@htsec.com) |
| [yl11036@htsec.com](mailto:yl11036@htsec.com) | 余伟民(010)50949926 | [ywm11574@htsec.com](mailto:ywm11574@htsec.com) |
| [ycl12224@htsec.com](mailto:ycl12224@htsec.com) | 张峥青(021)23219383 | [zzq11650@htsec.com](mailto:zzq11650@htsec.com) |
| [hjj10361@htsec.com](mailto:hjj10361@htsec.com) | 联系人 |  |
| [hl11570@htsec.com](mailto:hl11570@htsec.com) | 杨彤昕010-56760095 | [ytx12741@htsec.com](mailto:ytx12741@htsec.com) |
| [ym13254@htsec.com](mailto:ym13254@htsec.com) |  |  |
|  | 纺织服装行业 |  |
| [yun@htsec.com](mailto:yun@htsec.com) | 梁希(021)23219407 | [lx11040@htsec.com](mailto:lx11040@htsec.com) |
| 1 [lyj12399@htsec.com](mailto:lyj12399@htsec.com) | 盛开(021)23154510 | [sk11787@htsec.com](mailto:sk11787@htsec.com) |
| [lx12671@htsec.com](mailto:lx12671@htsec.com) |  |  |
| [cy13115@htsec.com](mailto:cy13115@htsec.com) |  |  |
|  | 钢铁行业 |  |
| [swc11480@htsec.com](mailto:swc11480@htsec.com) | 刘彦奇(021)23219391 | [liuyq@htsec.com](mailto:liuyq@htsec.com) |
| ec.com | 周慧琳(021)23154399 | [zhl11756@htsec.com](mailto:zhl11756@htsec.com) |
| [js12801@htsec.com](mailto:js12801@htsec.com) |  |  |
| [zyw13208@htsec.com](mailto:zyw13208@htsec.com) |  |  |
| ec.com |  |  |
|  | 食品饮料行业 |  |
| [dingpin@htsec.com](mailto:dingpin@htsec.com) | 闻宏伟(010)58067941 | [whw9587@htsec.com](mailto:whw9587@htsec.com) |
| [cy10867@htsec.com](mailto:cy10867@htsec.com) | 颜慧菁 [yhj12866@htsec.com](mailto:yhj12866@htsec.com) |  |
|  | 张宇轩(021)23154172 | [zyx11631@htsec.com](mailto:zyx11631@htsec.com) |
| [myq12354@htsec.com](mailto:myq12354@htsec.com) | 程碧升(021)23154171 | [cbs10969@htsec.com](mailto:cbs10969@htsec.com) |
|  | 社会服务行业 |  |
| [st9998@htsec.com](mailto:st9998@htsec.com) | 汪立亭(021)23219399 | [wanglt@htsec.com](mailto:wanglt@htsec.com) |
| sec.com | 许樱之(755)82900465 | [xyz11630@htsec.com](mailto:xyz11630@htsec.com) |
| [ljl12245@htsec.com](mailto:ljl12245@htsec.com) | 联系人 |  |
|  | 毛弘毅(021)23219583 | [mhy13205@htsec.com](mailto:mhy13205@htsec.com) |
| [ddl13026@htsec.com](mailto:ddl13026@htsec.com) |  |  |

蔡铁清(0755)82775962 [ctq5979@htsec.com](mailto:ctq5979@htsec.com)
伏财勇(0755)23607963 [fcy7498@htsec.com](mailto:fcy7498@htsec.com)
辜丽娟(0755)83253022 [gulj@htsec.com](mailto:gulj@htsec.com)

蔡铁清(0755)82775962 [ctq5979@htsec.com](mailto:ctq5979@htsec.com)
伏财勇(0755)23607963 [fcy7498@htsec.com](mailto:fcy7498@htsec.com)

研究所销售团队

饶 伟(0755)82775282 [rw10588@htsec.com](mailto:rw10588@htsec.com)
欧阳梦楚(0755)23617160

[oymc11039@htsec.com](mailto:oymc11039@htsec.com)

[oymc11039@htsec.com](mailto:oymc11039@htsec.com)
巩柏含 [gbh11537@htsec.com](mailto:gbh11537@htsec.com)

赵 洋(021)23154126 [zy10340@htsec.com](mailto:zy10340@htsec.com)
联系人

辜丽娟(0755)83253022 [gulj@htsec.com](mailto:gulj@htsec.com)
刘晶晶(0755)83255933 [liujj4900@htsec.com](mailto:liujj4900@htsec.com)
饶 伟(0755)82775282 [rw10588@htsec.com](mailto:rw10588@htsec.com)

滕雪竹 [txz13189@htsec.com](mailto:txz13189@htsec.com)

胡雪梅(021)23219385 [huxm@htsec.com](mailto:huxm@htsec.com)
朱 健(021)23219592 [zhuj@htsec.com](mailto:zhuj@htsec.com)
季唯佳(021)23219384 [jiwj@htsec.com](mailto:jiwj@htsec.com)

黄 毓(021)23219410 [huangyu@htsec.com](mailto:huangyu@htsec.com)
漆冠男(021)23219281 [qgn10768@htsec.com](mailto:qgn10768@htsec.com)
胡宇欣(021)23154192 [hyx10493@htsec.com](mailto:hyx10493@htsec.com)
黄 诚(021)23219397 [hc10482@htsec.com](mailto:hc10482@htsec.com)

李 寅 021-23219691 [ly12488@htsec.com](mailto:ly12488@htsec.com)
董晓梅 [dxm10457@htsec.com](mailto:dxm10457@htsec.com)

王朝领 [wcl11854@htsec.com](mailto:wcl11854@htsec.com)
邵亚杰 23214650 [syj12493@htsec.com](mailto:syj12493@htsec.com)
李 寅 021-23219691 [ly12488@htsec.com](mailto:ly12488@htsec.com)

黄 诚(021)23219397 [hc10482@htsec.com](mailto:hc10482@htsec.com)
毛文英(021)23219373 [mwy10474@htsec.com](mailto:mwy10474@htsec.com)
马晓男 [mxn11376@htsec.com](mailto:mxn11376@htsec.com)

张思宇 [zsy11797@htsec.com](mailto:zsy11797@htsec.com)
王朝领 [wcl11854@htsec.com](mailto:wcl11854@htsec.com)
邵亚杰 23214650 [syj12493@htsec.com](mailto:syj12493@htsec.com)

李 寅 021-23219691 [ly12488@htsec.com](mailto:ly12488@htsec.com)
董晓梅 [dxm10457@htsec.com](mailto:dxm10457@htsec.com)

殷怡琦(010)58067988
郭 楠 010-5806 7936 [gn12384@htsec.com](mailto:gn12384@htsec.com)
张丽萱(010)58067931 [zlx11191@htsec.com](mailto:zlx11191@htsec.com)

郭金垚(010)58067851 [gjy12727@htsec.com](mailto:gjy12727@htsec.com)
张钧博 [zjb13446@htsec.com](mailto:zjb13446@htsec.com)

郭金垚(010)58067851 [gjy12727@htsec.com](mailto:gjy12727@htsec.com)
张钧博 [zjb13446@htsec.com](mailto:zjb13446@htsec.com)
高 瑞 [gr13547@htsec.com](mailto:gr13547@htsec.com)

* * *

行业研究〃信息服务行业

海通证券股份有限公司研究所 地址：上海市黄浦区广东路 689 号海通证券大厦 9 楼 电话：（021）23219000 传真：（021）23219392 网址： [www.htsec.com](http://www.htsec.com/)

请务必阅读正文之后的信息披露和法律声明

### 来源 9: Palantir产品套件与平台架构- 53AI-AI知识库

- URL: https://www.53ai.com/news/Palantir/2025122362370.html
- 精读方法：firecrawl-scrape

- [首页](https://www.53ai.com/)
- 产品服务
- 客户案例
- FDE知识库
- 关于我们

热门场景

工作+AI

业务+AI

AIx业务

[落地咨询](https://www.53ai.com/consulting.html)

[场景共创](https://www.53ai.com/fine-tuning.html)

热门产品

[![53AI Brain](https://static.53ai.com/uploads/20250429/f9ed1b6c2d16a688c5791a0057c2217d.png)\\
\\
53AI Brain \\
\\
让知识在人与AI之间高效流动](https://www.53ai.com/products/53AIBrain) [![53AI Studio](https://static.53ai.com/uploads/20250429/b2cd4330d03bce8eb0eb0332eb2954cd.png)\\
\\
53AI Studio \\
\\
高准确率的企业级智能体开发平台](https://www.53ai.com/products/53AIStudio) [![53AI Hub](https://static.53ai.com/uploads/20250429/94e6d990ee63512db567bc53c113e8bd.png)\\
\\
53AI Hub开源\\
\\
三分钟搭建出独立的企业AI门户](https://www.53ai.com/products/53AIHub) [![53AI Agents](https://static.53ai.com/uploads/20250429/05d03bb026421069826c64e2407ad7ee.png)\\
\\
53AI Agents \\
\\
“AI专家”效率倍增的武器](https://www.53ai.com/products/Agents)

[行业案例](https://www.53ai.com/kehuanli/hangyeanli) [场景案例](https://www.53ai.com/kehuanli/solution)

[前沿技术](https://www.53ai.com/news/qianyanjishu) [Agent框架](https://www.53ai.com/news/agentplatform) [行业应用](https://www.53ai.com/news/hangyeyingyong) [企业落地](https://www.53ai.com/news/qiyejingying)

[公司介绍](https://www.53ai.com/about/introduction) [渠道合作](https://www.53ai.com/about/cooperation)

![FDE知识库](https://static.53ai.com/uploads/20250210/aec076a60258b0cc07078c8ea7dff92c.webp)

FDE知识库

学习大模型的前沿技术与行业落地应用

立即咨询预约演示

[![](https://static.53ai.com/assets/static/images/tab1.png)首页](https://www.53ai.com/) [FDE知识库](https://www.53ai.com/news.html) [前沿技术](https://www.53ai.com/news/qianyanjishu) [Palantir](https://www.53ai.com/news/Palantir)

# Palantir产品套件与平台架构

发布日期：2025-12-23 04:56:11浏览次数： 2621

作者：智邻AI

![](https://static.53ai.com/assets/static/images/detail-icon.png)

微信搜一搜，关注“智邻AI”

推荐语

Palantir两大核心平台揭秘：从国家安全到企业数据治理的智能革命。

核心内容：

1\. Gotham平台如何通过动态网络图重塑情报分析工作流

2\. Foundry平台如何解决企业数据孤岛问题并实现统一治理

3\. 两大平台共通的"人机协作"哲学与实战应用案例

![](https://static.53ai.com/assets/static/images/avatar.jpg)

杨芳贤

53AI创始人/腾讯云(TVP)最具价值专家

* * *

## 一、Gotham：分析师的战情室

早在“大数据”成为流行语之前，Palantir 的第一个平台——代号为 Gotham的系统——就悄然重新定义情报官员的工作方式。《Gotham》源自一个简单却激进的洞见：应对国家安全威胁的分析师需要的不仅仅是静态报告;它们需要一个互动、直观的环境来追踪关联、检验假设并预判对手的行动。

Gotham 的核心结合了三个元素：数据采集、图形关联以及协作标注。实际上，这意味着安全设施中的分析师可以利用截获的通信、财务账本和地理空间数据，然后观看 Gotham 的引擎将原始输入转换为动态网络图。每个节点——无论是电话号码、运输清单还是人类情报记录——都变得可点击、可扩展且可丰富内容。分布在各大洲的团队实时标注分析结果，构建一个随着每个新数据不断演变的叙事。

Gotham 的“读取时建模”方法是一项关键创新。传统数据仓库要求严格且前置的建模：每个字段都必须定义，每个关系都必须预先确定。相比之下，Gotham 则将结构推迟到探索时再进行。它在分析师探查时实时学习，绘制实体和关联图。这种弹性在情报领域至关重要，因为对手会调整战术，新的数据源不断涌现。

在底层，Gotham 依赖于优化快速移动的图数据库。当分析师从一个节点点击到另一个节点时，平台会在毫秒内执行数百万次最短路径计算，确保深度多步连接无延迟地出现。由于敏感数据存在政府防火墙后，Palantir 与各机构 IT 团队紧密合作，部署加固的本地集群——配备空隙加密、多因素认证和分隔访问控制。

Gotham 的影响在反叛乱战场中最为明显。在一次部署中，联盟特遣部队称 Gotham 将识别安全屋的平均时间缩短了 40%，使单位能够比以往更早几天拦截阴谋。然而，Gotham 并非灵丹妙药;它的力量取决于人类分析师的判断。Palantir 的座右铭——“机器发现模式，人们赋予意义”——强调了对自动化的谨慎拥抱。

## 二、Foundry：企业数据枢纽

虽然 Gotham 在国防和情报领域开辟了 Palantir 的市场，但其姊妹平台 Foundry 则打开了私营部门的闸门。Foundry 为在数据资产破碎问题中挣扎的商业客户设计，提供了一个统一的工作空间，将信息孤岛压缩为单一、可治理的层级。

在入职培训阶段，Foundry 工程师与企业 IT 团队并肩工作，收集 ERP 日志、CRM 记录、物联网传感器数据流等内容。通过自定义连接器，Foundry 对不同系统字段进行规范化——对齐日期格式、对照客户 ID，并揭示数据质量问题。关键是，这一过程是声明式的：工程师不是手工编码流水线，而是用高级语言表达转换，Foundry 则优化分布式集群间的执行。

数据一旦被导入，会被编目成数据谱系图，细致追踪来源：谁访问了哪个表，何时执行转换，以及哪些上游源头向仪表盘输送。这种可审计性既满足了合规官员的认可，也增强了对平台输出的信任。

用户界面强调无代码探索。业务用户可以将数据集拖放到画布上，可视化地连接表格，并应用预建功能——预测、异常检测和队列分析——而无需编写 SQL。对于高级用户，Foundry 提供了一个集成笔记本环境，支持 Python 和 R 库，使团队能够在将模型推广到生产流水线前进行原型设计。

Foundry 在现实世界的应用非常广泛。一家全球汽车制造商聘请 Foundry 协调十个工厂的生产线数据，识别瓶颈并降低了 15% 的缺陷率。医疗服务提供者将患者记录、设备遥测和人员配置日志连接起来，预测入院激增，从而实现预先人员配置调整。在每种情况下，平台的承诺都是相同的：将庞大的数据转化为同步、可作的洞察。

## 三、Apollo：无形的策划者

然而，数据的导入和建模只是成功的一半。企业要求关键任务分析在本地服务器、公有云甚至空中隔离环境中可靠运行。这时，Apollo 登场了，Palantir 的部署和管理引擎——常被称为“隐形编排者”。

Apollo 自动化了 Gotham 和 Foundry 实例的打包、配置和更新。其设计反映了容器编排的经验教训：从图引擎到界面层的每个服务都被封装在一个具有指定依赖关系的可部署单元中。Apollo 监控健康检查、资源利用和安全态势，针对异常触发自动回滚或缩放事件。

对于一家跨国银行，Apollo 使 Foundry 在受监管的司法管辖区——法兰克福、新加坡和悉尼——同步推出，这些地区均适用其数据驻留法规。工程师集中定义部署模板;Apollo 将它们转化为区域特定的清单，无需人工干预即可处理网络策略、证书配置和防火墙规则。这种一致性将部署时间从数周缩短到数小时。

Apollo 也是 Palantir 持续集成和交付理念的基础。核心更新——安全补丁、功能增强——通过自动化流水线，在沙盒环境中进行集成测试后，才会传播到上线系统。客户可以通过 Apollo 的治理仪表盘查看变更日志、安排维护窗口，甚至否决升级。

## 四、AIP：人工智能与数据管道平台

随着机器学习的成熟，Palantir 认识到需要一个将数据工程与模型开发融合的专用平台。于是，AIP（人工智能平台）诞生了，这是一个统一框架，数据科学家在其中构建、训练并大规模部署人工智能工作流。

AIP 引入了流水线 DAG（有向无环图），将 ETL 任务与模型训练步骤交错交错。数据科学家可能会定义一条流式传输，汇入流销售数据，将其转换为特征向量，训练梯度增强的树，然后将预测数据推回 Foundry 进行仪表盘管理——所有这些都是在一个编排流程中完成的。每个阶段的版本控制确保了可重复性：只需一键回滚到昨天的模型和数据快照。

在底层，AIP 利用 GPU 加速的计算集群，并与流行的框架——TensorFlow、PyTorch、XGBoost——集成，同时提供 Palantir 开发的库用于可解释性和公平性审计。在一项案例研究中，一家大型保险公司利用 AIP 构建了一个理赔欺诈检测器，得益于内置的偏见缓解模块，该检测率提高了 23%，同时误报率减半。

除了监督学习，AIP 还支持基于图的算法——向 Palantir 的传承致敬——允许客户端挖掘社区结构、检测异常子图，或通过网络传播信念。这一能力在金融犯罪中极为宝贵，因为非法网络常常隐藏在合法交易的阴影中。

## 五、Warp Speed & Ontology(本体论)：制造业的操作系统

Palantir 公司进军工业制造领域的努力在该公司年度大会 AIPCon 上得以明确，客户们在此展示创新成果。在那里，在有关供应链弹性和数字孪生的演讲中，一个新的范例浮现出来：Warp Speed，这是一个低代码制造操作系统，其基础是一个反映工厂分层复杂性的本体论。

与早期那些基于智能或广泛的企业分析的平台不同，Warp Speed 需要对物理流程进行语义建模。电机、传送带、质量检查、维护日志：每个实体和关系都必须在本体论中明确界定。一旦建立，实时传感器数据就会通过这个概念框架流动，从而实现实时监控和规范性干预。

一家半导体工厂，作为对正常运行时间和精度要求最为严苛的环境之一，成为了测试案例。工程师们将数百个工艺步骤——蚀刻、光刻、沉积——映射到“极速”系统的本体论中。当颗粒物读数在亚纳米级别出现峰值时，该系统会自动将异常情况与近期的维护操作相关联，推荐冷却程序以进行纠正，并在工厂的制造执行系统（MES）中触发工作订单。结果是：晶圆报废率降低了 12 天，节省了数百万美元的产量优化成本。

在 2024 年的 AIPCon 大会上，Warp Speed 预测性维护模块的演示赢得了全场起立鼓掌。实时视频流中的机器人焊工被现场标注，由人工智能驱动的检测员标记出微小裂缝，自主调度机器人则安排维修顺序以最大限度减少停机时间。这种本体设计、流式分析和闭环自动化的融合彰显了 Palantir 的雄心：掌控未来工厂的操作系统。

Palantir 通过 Gotham、Foundry、Apollo、AIP 和 Warp Speed 等产品，编织了一张从国防掩体到董事会会议室再到工厂车间的广泛产品网络。每个平台都秉持着相同的核心理念：赋予人类清晰的认知，通过治理防止过度干预，并在不牺牲速度的前提下拥抱复杂性。其结果是一种既强大又宽容的架构——一个数字支架，客户在其上构建其最关键的业务运营。

[智能化改造](https://www.53ai.com/keyword/%E6%99%BA%E8%83%BD%E5%8C%96%E6%94%B9%E9%80%A0) [智能化改造的意义](https://www.53ai.com/keyword/%E6%99%BA%E8%83%BD%E5%8C%96%E6%94%B9%E9%80%A0%E7%9A%84%E6%84%8F%E4%B9%89) [智能化改造案例](https://www.53ai.com/keyword/%E6%99%BA%E8%83%BD%E5%8C%96%E6%94%B9%E9%80%A0%E6%A1%88%E4%BE%8B)

分享：

用微信扫描二维码

用微信扫描二维码

用微信扫描二维码

用微信扫描二维码

53AI，企业落地大模型首选服务商

**产品**：场景落地咨询+大模型应用平台+行业解决方案

**承诺**：免费POC验证，效果达标后再合作。 **零风险落地应用大模型**，已交付160+中大型企业

[上一篇：Palantir在企业的机会](https://www.53ai.com/news/Palantir/2025122360873.html) [下一篇：Palantir 启示录：AI 正在终结传统 SaaS 模式——告别SaaS幻想：AI时代ToB的终点是能力体系](https://www.53ai.com/news/Palantir/2025122382743.html)

[返回列表](https://www.53ai.com/news/Palantir)

相关资讯

[2026-06-20\\
\\
FDE 术语表：30 个词看懂这个行业在说什么](https://www.53ai.com/news/Palantir/2026062029765.html) [2026-06-19\\
\\
决策系统的真正内核：本体模型](https://www.53ai.com/news/Palantir/2026061937529.html) [2026-06-16\\
\\
中国市场FDE是否有机会？](https://www.53ai.com/news/Palantir/2026061690672.html) [2026-06-11\\
\\
AI组织进化：为什么必须先补Palantir本体论这一课](https://www.53ai.com/news/Palantir/2026061116354.html) [2026-06-10\\
\\
硅谷今年最火的岗位 FDE，我们闷头干了三年](https://www.53ai.com/news/Palantir/2026061023150.html) [2026-06-10\\
\\
咨询与软件FDE转型：深度拆解Palantir生态卡位](https://www.53ai.com/news/Palantir/2026061007516.html) [2026-06-09\\
\\
现在流行的本体(Ontology)，是不是就是我们常说的语义层？](https://www.53ai.com/news/Palantir/2026060908627.html) [2026-06-07\\
\\
别把 Palantir 的“本体”做成知识图谱：企业数据架构的务实落地指南](https://www.53ai.com/news/Palantir/2026060746835.html)

[联系获取](https://www.53ai.com/solution.html)

[联系获取](https://www.53ai.com/solution.html)

160+中大型企业正在使用53AI

立即咨询预约演示

[把握AI发展的机遇，共同探索、共同进步\\
\\
2025-01-22](https://www.53ai.com/news/dongtai/2025012294502.html) [如何打造基于GenAI的员工服务机器人\\
\\
2025-01-22](https://www.53ai.com/news/dongtai/2025012234192.html)

[![banner](https://static.53ai.com/uploads/20250611/c637940d8902b253d3264aaf89cd40fc.jpg)](https://hub.53ai.com/)

热点资讯

[Palantir的中国门徒们，走到哪一步了？ \\
\\
2026-04-21](https://www.53ai.com/news/Palantir/2026042180293.html) [Palantir 技术思路与架构发展史：从情报图谱到决策操作系统 \\
\\
2026-04-22](https://www.53ai.com/news/Palantir/2026042265749.html) [FDE：AI时代的职业转型号角已吹响？ \\
\\
2026-05-26](https://www.53ai.com/news/Palantir/2026052650763.html) [当 DeepSeek 遇见 Ontology：企业智能决策的新范式正在出现 \\
\\
2026-05-11](https://www.53ai.com/news/Palantir/2026051197150.html) [硅谷今年最火的岗位 FDE，我们闷头干了三年 \\
\\
2026-06-10](https://www.53ai.com/news/Palantir/2026061023150.html) [吴恩达给正火的 FDE 泼冷水：押注它，不如押注 AI Engineer \\
\\
2026-06-03](https://www.53ai.com/news/Palantir/2026060317459.html) [别把 Palantir 的“本体”做成知识图谱：企业数据架构的务实落地指南 \\
\\
2026-06-07](https://www.53ai.com/news/Palantir/2026060746835.html) [Agentic Ontology：构建企业数字世界 \\
\\
2026-06-04](https://www.53ai.com/news/Palantir/2026060460327.html) [AI组织进化：为什么必须先补Palantir本体论这一课 \\
\\
2026-06-11](https://www.53ai.com/news/Palantir/2026061116354.html) [从PPT到FDE：这是一场咨询人的自我革命 \\
\\
2026-06-05](https://www.53ai.com/news/Palantir/2026060502965.html)

大家都在问

[中国市场FDE是否有机会？ \\
\\
2026-06-16](https://www.53ai.com/news/Palantir/2026061690672.html) [现在流行的本体(Ontology)，是不是就是我们常说的语义层？ \\
\\
2026-06-09](https://www.53ai.com/news/Palantir/2026060908627.html) [FDE：AI时代的职业转型号角已吹响？ \\
\\
2026-05-26](https://www.53ai.com/news/Palantir/2026052650763.html) [Palantir的中国门徒们，走到哪一步了？ \\
\\
2026-04-21](https://www.53ai.com/news/Palantir/2026042180293.html) [本体论思想-抽象建模的本质是什么？ \\
\\
2026-02-05](https://www.53ai.com/news/Palantir/2026020535127.html) [咨询 \| Palantir：我们不想做带着UI的埃森哲；一家咨询公司有望成为Palantir吗？优势和劣势分别在哪里？ \\
\\
2026-01-27](https://www.53ai.com/news/Palantir/2026012743157.html) [Palantir 哪些功能已经被标注为 Sunset（退场）和当前主推的功能是什么？ \\
\\
2026-01-19](https://www.53ai.com/news/Palantir/2026011980765.html) [【深度拆解】Palantir AIP智能体六件套：为何它是企业级Agent的终极形态？ \\
\\
2026-01-08](https://www.53ai.com/news/Palantir/2026010854981.html)

热门标签

[内容创作](https://www.53ai.com/news/neirongchuangzuo) [大模型技术](https://www.53ai.com/news/LargeLanguageModel) [个人提效](https://www.53ai.com/news/gerentixiao) [langchain](https://www.53ai.com/news/langchain) [llamaindex](https://www.53ai.com/news/llamaindex) [多模态技术](https://www.53ai.com/news/MultimodalLargeModel) [RAG技术](https://www.53ai.com/news/RAG) [智能客服](https://www.53ai.com/news/zhinengkefu) [知识图谱](https://www.53ai.com/news/knowledgegraph) [模型微调](https://www.53ai.com/news/finetuning) [RAGFlow](https://www.53ai.com/news/RAGFlow) [coze](https://www.53ai.com/news/coze) [Dify](https://www.53ai.com/news/dify) [Fastgpt](https://www.53ai.com/news/fastgpt) [Bisheng](https://www.53ai.com/news/Bisheng) [Qanything](https://www.53ai.com/news/Qanything) [AI+汽车](https://www.53ai.com/news/AIqiche) [AI+金融](https://www.53ai.com/news/AIjinrong) [AI+工业](https://www.53ai.com/news/AIgongye) [AI+培训](https://www.53ai.com/news/AIpeixun) [AI+SaaS](https://www.53ai.com/news/AISaaS) [Skill](https://www.53ai.com/news/tishicikuangjia) [提示词技巧](https://www.53ai.com/news/tishicijiqiao) [AI+电商](https://www.53ai.com/news/AIdianshang) [AI面试](https://www.53ai.com/news/AImianshi) [数字员工](https://www.53ai.com/news/shuziyuangong) [ChatBI](https://www.53ai.com/news/zhinengbaobiao) [AI知识库](https://www.53ai.com/news/zhishiguanli) [开源大模型](https://www.53ai.com/news/OpenSourceLLM) [智能营销](https://www.53ai.com/news/zhinengyingxiao) [智能硬件](https://www.53ai.com/news/zhinengyingjian) [FDE](https://www.53ai.com/news/zhinenghuagaizao) [AI+医疗](https://www.53ai.com/news/AIyiliao) [MaxKB](https://www.53ai.com/news/MaxKB) [Palantir](https://www.53ai.com/news/Palantir) [Glean](https://www.53ai.com/news/Glean) [Openclaw](https://www.53ai.com/news/Openclaw)

[应聘简历请发送至： ceo@53ai.com](mailto:ceo@53ai.com)

联系我们

售前咨询

[186 6662 7370](tel:18666627370)

预约演示

[185 8882 0121](tel:18588820121)

![](https://static.53ai.com/assets/static/images/loading.svg)

微信扫码

添加专属顾问

回到顶部

![](https://static.53ai.com/assets/static/images/loading.svg)

加载中...

扫码咨询

![](https://www.53ai.com/news/Palantir/2025122362370.html)

![](https://www.53ai.com/news/Palantir/2025122362370.html)

[预约演示](https://work.weixin.qq.com/ca/cawcde2599cf74e2d9) [微信咨询](https://work.weixin.qq.com/ca/cawcdefb661890e885) [电话咨询](tel:400-838-1185)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

安全验证

拖动下方拼图完成验证

![close](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

AI生成背景

![success](<Base64-Image-Removed>)

您的速度已超过 99% 的用户

验证错误,请重试

![load error](<Base64-Image-Removed>)

确定

![slider arrow](<Base64-Image-Removed>)![slider arrow](<Base64-Image-Removed>)![slider arrow](<Base64-Image-Removed>)

安全验证

刷新验证码

![refresh](<Base64-Image-Removed>)

反馈

![tip](<Base64-Image-Removed>)

切换无障碍验证

![Barrier-free verification](<Base64-Image-Removed>)

切换常规验证

![switch](<Base64-Image-Removed>)

### 来源 10: [PDF] 相关研究报告北交所研究团队 - i研报

- URL: https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf
- 精读方法：firecrawl-scrape

北交
所研
究

开源
证券
证券
研究
报告

北交
所行
业主
题报
告

2025 年 03 月 07 日

北交所研究团队

全球巨头启示录：AI+国防双栖巨头 Palantir 商业启示，生成式 AI 产业化推手

《子公司产能建设+认证加速，2024 年预计营收 +18%— 北交所信息更新》
-2025.3.4

《汽车电子新订单注入业绩增长动力，2024 年归母净利润同比增长 10%
—北交所信息更新》-2025.3.5

《从"工具替代"到"流程再造"的数智手术生态小巨人，星航 1.0 已取证—新三板公司研究报告》-2025.3.3

——北交所行业主题报告

诸海滨（分析师）

[zhuhaibin@kysec.cn](mailto:zhuhaibin@kysec.cn)

证书编号：S0790522080007

l 看标杆：国防科技巨头 Palantir，持续更新平台及 AI 模型

Palantir 自 2003 年成立以来，始终致力于通过创新的软件解决方案，助力组织高效整合大规模数据、优化决策流程并提升运营效能。公司的发展历程始于为美国情报界开发反恐软件，凭借深厚的技术积累与卓越的数据处理能力，积累了丰富的行业经验。目前，Palantir 已成功构建了四大核心软件平台，包括 Palantir Gotham
（“ Gotham”）、 Palantir Foundry（“ Foundry”）、 Palantir Apollo（“ Apollo”）以及
Palantir 人工智能平台（“AIP”）。截至 2024 年 12 月 31 日，公司的客户总数达到
711 家。公司的软件目前在全球约 90 个行业中广泛应用，服务于不同业务职能和组织层级的用户，涵盖多样化的用例。在 2024 年，Palantir 实现了 29 亿美元的收入，其中 55%来自政府部门客户，45%来自商业部门客户，体现了“政府+
商业”双轮驱动的业务模式。2024 年营业收入达到 28.66 亿美元，同比增长
28.79%。其中政府业务实现 15.70 亿美元，商业业务实现 12.96 亿美元。

l 观布局：生成式 AI 市场广阔，应用逐渐落地

l 观布局：生成式 AI 市场广阔，应用逐渐落地根据麦肯锡研究显示，生成式 AI 的价值创造潜力极为惊人。到 2030 年前，它有望为全球经济贡献 7 万亿美元的价值，比传统 AI 或分析的潜在经济效益高出
50%。作为 AI 研发高地的中国，将凭借战略性投资分享生成式 AI 总效益的 1/3。经分析，MGI 发现，目前劳动者 50%工时内的工作可能在 2030 年前被自动化。仅中国就有约 2.2 亿个岗位可能被生成式 AI 等自动化技术重塑。全球范围内，
生成式 AI 对高科技行业的影响最为显著。而在中国，最具代表性的将是先进制造、电子与半导体这两大行业。IDC 预计，到 2025 年，中国的生成式 AI 软件市场规模将达到 35.4 亿美元。随着大模型基础能力的提升和应用形式的创新，未来大模型平台将逐渐分化为底层平台和智能体开发平台，前者将与企业数据分析和机器学习开发平台整合，后者则朝着低代码无代码的方向发展。

l 风险提示：行业竞争的风险、客户拓展的风险、产业政策落地不及预期风险

Palantir AIP 为全球关键商业和政府环境提供实时、人工智能驱动的决策支持。从公共卫生到电池生产，各类组织均依赖 Palantir 在其运营中安全、可靠且高效地利用人工智能技术，以推动卓越的运营成果。围绕 Palantir Ontology 构建的软件架构助力企业实现最优化决策。近年来，公司采取了多种销售和营销策略，
以加速客户获取能力，包括：公司平台的部署速度扩大计划长期合作的潜在客户范围。2023 年公司推出了 AIP 训练营， 2024 年公司推出了开发者层，在美国和部分国家/地区提供对 Foundry 和 AIP 的有限访问；公司已投资并计划继续投资基于账户的销售团队；开发行业操作系统，帮助公司和政府机构高效管理其整体运营；已与领先的公共云、私有云及混合云服务提供商建立了紧密合作；计划继续建立合资企业和新业务伙伴关系，特别是在特定行业或领域。

* * *

目 录

1、写在前面.....3
2、看标杆：国防科技巨头 Palantir，持续更新平台及 AI 模型.....3
2.1、历史发展：成立于 2003 年，逐步拓展业务领域与商业企业展开合作.....3
2.2、商业模式：2024年客户总数达到 711 家，“政府+商业”双轮驱动.....8
3、观布局：生成式 AI 市场广阔，应用逐渐落地.....10
3.1、2030年生成式 AI 有望为全球贡献 7 万亿美元价值，对高科技行业影响显著.....10
3.2、2025年中国生成式 AI 软件市场规模或达 35.4 亿美元，企业需提高变现能力.....12
4、学经验：战略布局+技术创新，为北交所公司提供发展范式.....15
4.1、平台：核心技术 Ontology 助力企业实现最优化决策，提升产品竞争力.....15
4.2、布局：采取多种策略加速获客，提前布局 AIGC.....18
5、

图表目录

图 1： Palantir 自 2003 年成立以来，始终致力于创新软件解决方案 .....3
图 2： 2023 年，Palantir 进一步拓展技术边界，推出了最新产品 AIP .....4
图 3： 2024 年营收 28.7 亿美元，同比增长 28.8%（亿美元） .....6
图 4： 2024 年政府业务 15.7 亿美元，商业业务 13 亿美元（万美元） .....6
图 5： Palantir 2023财年净利润扭亏为盈，实现净利润 2.1 亿美元（亿美元） .....7
图 6： 2024财年 Palantir 净利率为 16.33% .....7
图 7： 2024财年 Palantir毛利率为 80.25% .....7
图 8： 2024年美国客户贡献了 66%的收入，达到 19 亿美元（万美元） .....8
图 9： 至 2030

* * *

1、 写在前面

得益于数字基础设施的建设与夯实，作为通用性人工智能技术代表的生成式 AI，
已日益融入生产力提升环节，推动数据要素价值充分释放，为诸多领域带来变化。随着技术驱动的智能化战争趋势愈发明显，部分新科技公司越来越多的出现在美国国防部及各军兵种的采购合同中，其中，帕兰蒂尔（Palantir）便是其中的佼佼者。在本篇报告中，公司将聚焦全球数据分析解决方案提供商 Palantir Technologies，对其商业模式和业务布局等情况进行深入研究，思考并总结其成功经验，从微观角度探究其所在行业的发展特征与未来走势。

2、 看标杆：国防科技巨头 Palantir，持续更新平台及 AI 模型

2.1、 历史发展：成立于 2003 年，逐步拓展业务领域与商业企业展开合作

Palantir 自 2003 年成立以来，始终致力于通过创新的软件解决方案，助力组织高效整合大规模数据、优化决策流程并提升运营效能。公司的发展历程始于为美国情报界开发反恐软件，凭借深厚的技术积累与卓越的数据处理能力，积累了丰富的行业经验。此后，Palantir 逐步拓展业务领域，与众多商业企业展开合作，凭借对数据处理挑战的深刻洞察，为其提供定制化的解决方案。

公司总部位于美国特拉华州，2005 年公司成为美国中情局的软件供应商；2008
年以来，公司一直自与美国陆军合作，与用户一起设计和部署现代任务必需的软件解决方案；2020 年 9 月 30 日，Palantir 在纽约证券交易所通过直接上市公开发行，
股票代码为“PLTR”；2020 年 12 月，公司获得了美国食品药品监督管理局（FDA）
的一份三年期合同，推动其股价大涨逾 17%；2022 年，美国国土安全部与公司续签了合同，以用案件调查管理软件支持国土安全调查；2024 年 9 月 23 日，Palantir 纳入标普 500 指数。

图1：Palantir 自 2003 年成立以来，始终致力于创新软件解决方案

目前，Palantir 已成功构建了四大核心软件平台，包括 Palantir Gotham（“ Gotham”）、
Palantir Foundry（“ Foundry”）、 Palantir Apollo（“ Apollo”）以及 Palantir 人工智能平台（“AIP”）。其中，Gotham 和 Foundry 专注于将海量信息转化为集成数据资产，助力机构实现数据驱动的运营优化。Gotham 凭借其卓越的性能，已在国防、情报、救灾等多个领域为全球机构提供深度见解，积累了丰富的成功案例。Foundry 则致力于成为行业级中央操作系统，为不同行业的企业提供统一的数据管理和分析平台，推动行业数字化转型进程。Apollo 作为一款与云无关的单一控制层，自 2021 年推出以

资料来源：Palantir 官网、Wind、开源证券研究所

* * *

来，凭借其强大的功能，能够协调新功能、安全更新和平台配置的持续交付，确保关键系统的稳定运行，为客户在复杂多变的环境中提供可靠的技术支持，使其能够在几乎任何环境中灵活部署软件，满足多样化的业务需求。2023 年，公司进一步拓展技术边界，推出了最新产品 AIP。

表1：目前，Palantir 已成功构建了四大核心软件平台

| 平台名称 | 平台介绍 |
| --- | --- |
| Gotham | Gotham使用能够识别隐藏在数据集深处的模式，从信号情报来源到机密线人的报告。它还促进了分析师和操作用户之间的交接，帮助操作员计划和执行对平台内已识别威胁的实际响应。Gotham现在广泛应用于政府职能部门，公司也向公司的商业客户提供Gotham。 |
| Foundry | Foundry通过为数据创建中央操作系统，改变了组织的运营方式。个人用户可以在一个地方集成和分析他们需要的数据。因为用于构建数据管道的步骤和方法难以理解和重新创建，数据项目经常失败，公司构建了Foundry的后端来解决这个问题的根源。该平台的图形界面完成其余工作，允许用户跟踪和追踪他们的管道，以便他们知道表中的行和列代表什么以及它们在那里的原因。 |
| AIP | AIP通过使用主要的核心组件来实现整个企业的负责任的AI优势，这些组件旨在有效激活任何组织内的LLM和其他AI。它提供对开源、自托管和商业LLM的统一访问，这些LLM可以将结构化和非结构化数据转换为LLM可理解的对象，并将组织的行动和流程转变为人类和LLM驱动代理的工具。AIP可以允许组织通过用于决策、反馈和AI代理与人类操作员之间的安全交接的接口来为AI和LLM的操作使用提供动力，具有广泛的安全和审计控制，可以对模型使用进行精细控制，并在整个工作流中融入人工审查检查点。AIP旨在与现有的Palantir产品（如Foundry、Gotham和Apollo平台)无缝捆绑。 |
| Apollo | Apollo使公司的软件和更新能够在整个业务中快速、安全地交付，同时还使客户能够在几乎任何环境中安全地部署自己的软件。Apollo提供单一控制层来协调新功能、安全更新和平台配置的持续交付。 |

资料来源：Palantir 年报、开源证券研究所

AIP 平台专为商业和政府部门客户设计，通过将现有软件平台与大型语言模型
（LLM）相结合，助力客户充分挖掘人工智能技术的潜力，实现数据与人工智能的深度融合，从而在法律、道德和安全约束范围内做出精准决策，为组织的数字化转型注入强大动力。

图2：2023 年，Palantir 进一步拓展技术边界，推出了最新产品 AIP

* * *

往需要漫长的实施周期，难以满足快速响应的迫切需求。在此背景下，Palantir 的软件产品凭借其快速部署和高效应用的优势脱颖而出，成为众多客户的首选。与内部软件开发可能耗费数月甚至数年的漫长周期形成鲜明对比，Palantir 的软件能够在短短几天内完成部署并投入使用，极大地提升了客户的应急响应能力和运营效率。这一独特优势不仅为客户解决了燃眉之急，更在激烈的市场竞争中为 Palantir 赢得了宝贵的客户信任与市场份额。

公司核心管理团队具备深厚的产业背景与资源优势。公司创始人 Peter Thiel 为
PayPal 创始人，在硅谷科技与投资领域积累了广泛的产业资源与生态网络，其创立的基金为公司政府端业务拓展及融资渠道提供了有力支持。联合创始人兼 CEO
Alexander Karp 拥有超过 20 年的技术创业经验，并持有斯坦福大学法学博士学位，
具备深厚的技术与法律复合背景。公司核心技术团队均来自斯坦福大学、哈佛大学等全球顶尖院校，团队构成涵盖工程师、律师及社会科学家等多领域专业人才，形成了技术研发与合规实践的双重优势，为公司在数据安全与隐私保护领域建立了竞争壁垒。

| 资管理者 | 简介 |
| --- | --- |
| Alexander Karp | Karp先生是公司的联合创始人之一，自共同创立Palantir以来曾在公司担任过多个职位，最近担任首席执行官，自2003年以来一直担任公司董事会成员。Karp先生拥有哈弗福德学院的学士学位、斯坦福法学院的法学博士学位以及德国法兰克福歌大学的博士学位。 |
| Alexander Moore | 自2020年7月以来，Moore先生一直担任公司董事会成员。Moore先生最初于2005年2月加入，是创始员工之一，并担任公司的运营总监，直至2010年3月。2013年2月，Moore先生与他人共同创立了云自动化公司Node Prime，并担任首席运营官，直至2016年4月被爱立信收购。2017年5月，他加入了风险投资基金8VC，目前担任合伙人。Moore先生拥有斯坦福大学经济学学士学位。 |
| Alexandra Schiff | Schiff女士自2020年7月起担任公司董事会成员。于2004年6月至2005年3月以及2013年4月至2020年6月担任《华尔街日报》记者。2006年至2009年，她担任CondéNast Portfolio杂志的特约撰稿人，后来担任特约编辑，该杂志前身是全球媒体公司CondéNast的一部分。她曾为《纽约时报》、《名利场》和《彭博商业周刊》等出版物撰稿。Schiff女士拥有杜克大学英语学士学位。 |
| Stephen Cohen | Cohen先生是公司的联合创始人之一，自共同创立Palantir以来曾在公司担任过多个职务，最近担任总裁兼秘书，自2005年以来一直担任董事会成员。Cohen先生拥有斯坦福大学计算机科学学士学位。 |
| Peter Thiel | Thiel先生是公司的联合创始人之一，自2003年起一直担任董事会主席。他自2011年起担任投资公司Thiel Capital总裁，自2005年起担任风险投资公司Founders Fund合伙人。1998年，Thiel先生与他人共同创立了在线支付公司PayPal,Inc.，并从2000年起担任该公司的首席执行官、总裁兼董事会主席，直至2002年该公司被eBay收购。Thiel先生此前曾于2005年至2022年担任科技公司MetaPlatforms,Inc的董事会成员，并于2020年至2024年担任生物技术公司AbCelleraBiologicsInc的董事会成员。Thiel先生拥有斯坦福大学哲学学士学位和斯坦福法院法学博士学位。 |
| Lauren Friedman Stat | Stat女士自2021年1月起担任公司董事会成员。Stat女士拥有广泛的商业和领导经验，在医疗保健和技术领域拥有超过20年的经验。Stat女士在埃森哲工作了15年，从2005年10月到2021年1月，曾担任财富100强公司的高级顾问。Stat女士通过她的咨询公司担任顾问，并担任健康和软件技术公司以及非营利性医疗保健组织的董事会成员。Stat女士于2021年12月至2022年12月担任卫星通信技术公司FriendlyForce的兼职首席行政官，现在担任顾问。她还于2021年6月至2022年6月期间担任社会影响社区和风险投资组织Notley的驻地执行官。自2022年7月以来，Stat女士一直担任3D打印珠宝公司Figa Jewelry的管理员兼首席执行官。她拥有斯坦福大学科学、技术和社会学士学位，主修数学和化学。 |
| Eric Woersching | Woersching先生自2022年6月起担任公司董事会成员。Woersching先生目前担任早期软件公司的私人顾问，专注于企业战略、FP&A、分析、运营和高管招聘。2020年至2022年，Woersching先生担任EasyPost的收入运营副总裁，负责分析、运营和企业战略，并担任首席执行官高级顾问，专注于企业发展、并购和融资。2017年至2019年，Woersching |
|  | 先生是风险投资公司Initialized Capital的普通合伙人，并担任多家私营科技公司的董事会成员。他拥有斯坦福大学电气工程学士和硕士学位，并且是特许金融分析师。 |

资料来源：Palantir 官网、开源证券研究所

财务状况：随着人工智能行业蓬勃发展，企业越来越依赖数据分析进行决策，
公司的软件解决方案对寻求最大化数据效用使公司营收保持高速增长。2023 财年，
公司实现营业收入 22 亿美元，同比增长 17%。其中政府业务实现 12.22 亿美元，同比增长 14.04%，商业业务实现 10.03 亿美元，同比增长 20.23%。2024 财年营业收入达到 28.66 亿美元，同比增长 28.79%。其中政府业务实现 15.70 亿美元，商业业务实现 13 亿美元。

图3：2024 年营收 28.7 亿美元，同比增长 28.8%（亿美元）

图4：2024 年政府业务 15.7 亿美元，商业业务 13 亿美元
（万美元）

数据来源：Wind、开源证券研究所

数据来源：Wind、开源证券研究所

公司盈利能力较强。净利润方面，公司 2023 财年净利润扭亏为盈，实现净利润
2.1 亿美元，同比增长 156.15%，2024 年，实现净利润 4.62 亿美元，同比增长 120.27%。毛利率方面，2020-2024 财年，公司毛利率分别为 67.74%、77.99%、78.56%、80.62%、
80.25%。净利率呈上升趋势，分别为-106.75%、-33.75%、-19.47%、9.77%、16.33%。

* * *

图5：Palantir 2023 财年净利润扭亏为盈，实现净利润 2.1 亿美元（亿美元）

数据来源：Wind、开源证券研究所

图6：2024 财年 Palantir 净利率为 16.33%

图7：2024 财年 Palantir 毛利率为 80.25%

数据来源：Wind、开源证券研究所

数据来源：Wind、开源证券研究所

* * *

2.2、 商业模式：2024 年客户总数达到 711 家，“政府+商业”双轮驱动

Palantir 与众多世界领先的政府和商业机构建立了合作关系。截至 2024 年 12 月
31 日，公司的客户总数达到 711 家。公司的软件目前在全球约 90 个行业中广泛应用，
服务于不同业务职能和组织层级的用户，涵盖多样化的用例。例如，美国的公用事业运营分析师、汽车制造工人、石油和天然气技术人员及运营商、制药研究人员；
韩国的供应链经理；英国和美国的公共卫生管理人员；以及美国和其他国家的特种部队人员与军事官员等，均在使用公司的解决方案。

在 2024 财年，Palantir 实现了 29 亿美元的收入，其中 55%来自政府部门客户，
45%来自商业部门客户，体现了“政府+商业”双轮驱动的业务模式。公司的业务持续全球化扩展，2024 财年 66%的收入来自美国客户，预计未来仍将是公司收入增长的重要引擎，34%来自国际市场。

图8：2024 年美国客户贡献了 66%的收入，达到 19 亿美元（万美元）

数据来源：Wind、开源证券研究所

在客户拓展策略方面，公司通过自费试点和训练营等方式，深度参与客户需求挖掘与解决方案定制，尽管此类投入不保证未来回报，但为公司创造了独特的市场机会。公司采用账户层面的客户管理模式，而非行业或部门划分，以确保能够针对每个客户的特定需求优化增长策略。展望未来，公司计划进一步扩大在商业和政府市场的覆盖范围，并根据对客户长期价值的评估动态调整资源投入优先级。

表3：Palantir 的商业模式主要基于提供软件平台和服务

| 软件平台 | 商业模式 |
| --- | --- |
| Palantir Cloud | PalantirCloud订阅服务为客户提供了在Palantir全权管理的托管环境下访问专属软件功能的使用权，该服务以标准化运维(O&M)服务包形式进行商业化交付。根据合同条款，公司承诺在协议有效期内持续维护并保障客户对托管软件平台的访问权限。针对PalantirCloud订阅服务产生的收入，公司严格遵循控制权转移时点的会计准则，采用直线法在服务周期内进行系统性分摊确认。 |
| On Premises Software | 公司销售的软件许可证（主要为定期许可证）授予客户在合同期限内在其内部硬件基础设施或自有云实例上使用功能性知识产权的权利。此类许可证通常与标准的运营与维护(O&M)服务捆绑销售。O&M服务包括确保 |

公司的商业模式主要基于提供软件平台和服务。具体来说，公司通过销售订阅服务，使客户能够访问其在公司托管环境中的软件平台（PalantirCloud），以及提供软件许可，使客户能够在自己的环境中使用软件（On-PremisesSoftware）。此外，公司还提供专业服务，包括持续的运营和维护（O&M）服务，以确保软件的正常运行和维护。公司的收入主要来源于这些服务的销售，合同通常为 1 至 5 年的期限，收入在合同期间按比例确认。表3：Palantir 的商业模式主要基于提供软件平台和服务

* * *

| 软件平台 | 商业模式 |
| --- | --- |
|  | 软件运行所需的关键更新、技术支持及维护服务，这些服务对于软件在合同期限内保持其预期效用至关重要。基于这一要求，公司认定软件许可证与O&M服务（公司统称为OnPremises软件）高度相互依赖且紧密关联，共同构成合同范围内单一且独特的履约义务。因此，相关收入通常在合同期限内按比例确认。 |
| Professional Services | 公司提供专业服务以支持客户对软件平台的使用，具体内容包括按需用户支持、用户界面配置、培训以及持续的本体与数据建模支持。专业服务合同通常涵盖在合同期限内按需提供的各类专业服务。这些服务通常与PalantirCloud订阅或OnPremises软件部署同步进行。由于专业服务是按需提供，并在整个合同期内持续交付，因此相关收入在合同期限内按服务提供进度予以确认。 |
| Contract Liabilities | 客户的开票与付款时间相对于服务期开始时间因合同而异。公司根据合同提供服务之前，通常会向许多客户开具账单，从而形成由递延收入或客户押金构成的合同负债。其中，递延收入反映了在相关产品或服务转移给客户之前，根据不可撤销合同开具的账单金额；客户押金则包括在合同期开始前提前收取或支付的款项，或为应对客户取消合同期限内预计产生收入的活动而收取的金额 |

资料来源：Palantir 年报、开源证券研究所

* * *

北交所行业主题报告

# 3、 观布局：生成式 AI 市场广阔，应用逐渐落地

## 3.1、 2030 年生成式 AI 有望为全球贡献 7 万亿美元价值，对高科技行业

影响显著 生成式 AI 创造的主要价值可用“4C”来概括： Ø 简化（虚拟专家）(Concision)：生成式 AI 能够利用非结构化数据源归纳并 提炼洞见，从而促进专业知识的传播；它还能解读文本与转录稿，创建嵌 入式文本，以支持相关资料来源的查询和引用。 Ø 编码与软件开发(CodingandSoftware)：生成式 AI 能够推动代码重构，从 而加快主机迁移；可以解读、生成代码，从旧有系统大规模迁移主机资料， 自动开发、记录、纠正测试，简化软件开发流程。 Ø 内容创作(ContentCreation)：生成式 AI 能够创作各种形式的内容初稿，可 生成文本、图片等信息载体，自动编写合同、招标书等文件，还能生成视 觉元素，加快研发节奏。 Ø 客户互动(CustomerEngagement)：生成式 AI 有助于打造高度个性化的消 费体验，如通过聊天功能优化客户服务，还能拓宽客户聊天机器人的应用 场景，从而加速客户拓展与数据收集。 根据麦肯锡研究显示，生成式 AI 的价值创造潜力极为惊人。到 2030 年前，它 有望为全球经济贡献 7 万亿美元的价值，比传统 AI 或分析的潜在经济效益高出 50%。 作为 AI 研发高地的中国，将凭借战略性投资分享生成式 AI 总效益的 1/3。 图9：至 2030 年，生成式 AI 有望为中国进一步释放 2 万亿美元的价值潜力

25 20 15 10 5 0 全球 中国 生成式AI（万亿美元） 传统AI（万亿美元）

数据来源：麦肯锡全球研究院、开源证券研究所 生成式 AI 所具备的价值创造潜力毋庸置疑，但其效益取决于多重因素，不仅涉 及行业内不同职能的比例与重要性，也取决于行业的营收规模。

请务必参阅正文后面的信息披露和法律声明 10/21

* * *

图10：在数个业务职能部署生成式 AI，可获取该技术带来的大部分效益

资料来源：麦肯锡全球研究院

数十年来，科技进步不断重塑工作的本质，为劳动者持续注入“超能量”，帮助人类更快速更准确地完成工作。生成式 AI 不仅将延续这一趋势，还将带来前所未有的较大影响。伴随生成式 AI 的逐步推广，工作自动化的步伐将大幅加快，“中点情境”有望提前 10 年到来，50%的工时预计将实现自动化。

图11：全球工作自动化“中点情境”将提前 10 年实现

2017 年以来，麦肯锡全球研究院（MGI）始终密切关注自动化技术对工作的影响。经分析，MGI 发现，目前劳动者 50%工时内的工作可能在 2030 年前被自动化。仅中国就有约 2.2 亿个岗位可能被生成式 AI 等自动化技术重塑。这一系列惊人的数字充分印证了生成式 AI 将给劳动者带来的较大影响。

资料来源：麦肯锡全球研究院

* * *

图12：受生成式 AI 影响最大的前十大职业

资料来源：麦肯锡全球研究院

总体而言，生成式 AI 将促进劳动力转型升级，催生全新的工作方式，显著提高人效。

随着生成式 AI 的持续进化，企业与劳动者必须高效加以适应和运用。组织必须顺应 AI 发展潮流，围绕生成式 AI 的潜力重新定义工作岗位、培养全新技能。同样，
劳动者也必须树立终身学习的观念，积极提升自身技能，从而在 AI 赋能的未来持续成长。

全球范围内，生成式 AI 对高科技行业的影响最为显著。而在中国，最具代表性的将是先进制造、电子与半导体这两大行业。

* * *

图13：在中国生成式 AI 对先进制造、电子与半导体及消费品等行业将带来最大效益
\[Image: Image109\]

资料来源：麦肯锡报告《生成式 A1 的经济潜力:下一个生产力前沿领域》

《中国生成式 AI 应用开发平台市场:企业统一 AI 开发平台的雏形》报告指出，
企业在扩展生成式 AI 应用时亟需统一的 AI 开发平台。这一平台可以帮助各级管理层、员工及技术部门实现数据、模型和应用的统一管理。IDC 强调了生成式 AI 应用开发平台应具备的一系列基本能力，包括数据准备、模型调优、RAG/Prompt 支持、模型部署及确保应用安全等。

| 序号 | 厂商 | 优势 |
| --- | --- | --- |
| 1 | 阿里云 | 百炼以及PAI:应用构建开放高效,应用集成灵活可配,模型服务丰富多元 |
| 2 | AWS亚马逊云科技 | BedRock以及SageMaker:丰富的模型选择,差异化定制,应用集成 |
| 3 | 百度智能云 | 千帆平台作为国内较早的大模型平台,为模型开发者以及应用开发者提供不同的开发工具链,已培育出丰富的生成式AI应用生态 |
| 4 | 创新奇智 | 奇智孔明AlnnoGC工业大模型平台,功能包括ChatRobot、ChatBI、ChatDoc,应用场景包括工业机器人、数据分析、企业私域知识搜索等 |
| 5 | DataCanvas九章云极 | 大模型开发工具链定位全流程的LMLab大模型构建工具,支持LLM部署、压缩和推理能力的Inference大语言模型服务，支持Agent智能体构建以及直接调用AgentStudio |
| 6 | 华为云 | ModelArtsStudio为大模型与生成式AI应用开发提供全栈开发工具,尤其注重企业级用户 |
| 7 | 火山引擎 | 方舟平台、HiAgent、豆包、Codez形成大模型开发应用的完整矩阵,为用户打造数据飞轮 |
| 8 | 蚂蚁集团 | AIStudio支持蚂蚁自研大模型以及主流开源模型的调优与部署,产品功能完善,使用简单灵活 |
| 9 | 深信服 | 深信服AI应用创新平台：提供一体化的AI算力管理和大模型应用开发能力,单节点起步、向导化配置、预置企业常用应用模板，支持工作流零代码开发应用，业界首推模型动态加密能力 |
| 10 | 神州数码 | 神州问学·专注于打通数据、模型、算力与应用的企业级一站式AI原生赋能平台，是国内较早的生成式AI应用开发平台 |
| 11 | 360 | 360智脑基于大规模高质量的语料训练，支持根据业务场景选择API类型并定制，提供相关AI解决方案 |
| 12 | 天翼AI | 定位大模型深度应用综合解决方案，包含星海·全域AI平台、知识中台、智能体开发运营平台等 |
| 13 | 星环科技 | SophonLLMOps星环大模型运营平台支持一站式AI开发，提供包括知识库在内的丰富的应用开发能力 |
| 14 | 智谱AI | 智谱MaaS平台面向开发人员极速构建变革性AI体验，已在金融、汽车多家企业实现商业化部署 |

资料来源：IDC、开源证券研究所

请务必参阅正文后面的信息披露和法律声明

* * *

IDC 预计，到 2025 年，中国的生成式 AI 软件市场规模将达到 35.4 亿美元。随着大模型基础能力的提升和应用形式的创新，未来大模型平台将逐渐分化为底层平台和智能体开发平台，前者将与企业数据分析和机器学习开发平台整合，后者则朝着低代码无代码的方向发展。

图14：到 2025 年，预计中国的生成式 AI 软件市场规模将达到 35.4 亿美元

数据来源：IDC、开源证券研究所

麦肯锡研究显示，仅 9%的中国企业计划凭借部署 AI 实现超 10%的营收增长，
而领先国家有 19%的企业有望实现这一目标。同样，就利润贡献率而言，仅有 7%的中国企业称 AI 对 EBIT 的贡献率突破 20%，而领先国家有 14%的企业突破了这一比例。对比结果表明，中国企业亟需提高变现能力，将 AI 技术的潜力转化为切实的经济效益。

* * *

4、 学经验：战略布局+技术创新，为北交所公司提供发展范式

4.1、 平台：核心技术 Ontology 助力企业实现最优化决策，提升产品竞争力

Palantir AIP 为全球关键商业和政府环境提供实时、人工智能驱动的决策支持。从公共卫生到电池生产，各类组织均依赖 Palantir 在其运营中安全、可靠且高效地利用人工智能技术，以推动卓越的运营成果。

Palantir AIP 将生成式人工智能与运营紧密结合。作为 AI Mesh 的一部分，AIP
与 Foundry（Palantir 的数据运营平台）和 Apollo（Palantir 的自主软件部署任务控制系统）协同工作，提供全系列人工智能驱动的产品。这些产品涵盖从基于大语言模型（LLM）的 Web 应用程序，到利用视觉语言模型的移动应用程序，再到嵌入本地化人工智能的边缘应用程序。公司将这一整套功能、能力和工具统称为 Palantir 平台。

图15：Palantir AIP 将生成式人工智能与运营紧密结合

资料来源：Palantir 官网

尽管多种因素共同推动了 Palantir 平台实现并扩大其运营影响力，例如 AIP
Bootcamps，客户仅需通过实际操作即可在数小时内借助人工智能取得显著成果，但其核心差异化优势在于围绕 Palantir Ontology 构建的软件架构。

Ontology 原生支持多种数据类型及扩展原语，例如用于解锁非结构化数据的语义搜索、用于处理图像和视频的媒体引用，以及用于将其他约束和上下文嵌入数据的值类型。这些构成了人工智能工作流程开发的数据基础模块，并将在后续的逻辑

* * *

和操作部分进一步阐述。

该数据模型为开箱即用的应用程序提供支持，能够探索结构化、非结构化、地理空间、时间序列、模拟及其他数据模式。这些基线工具通过上下文感知的 AIP Assist
功能得到增强，显著缩短了在平台中探索和分析数据时的价值实现时间。

除了应用程序构建与分析功能外，在 Ontology 中建模数据还会自动生成一个强大的 API 网关和 Ontology 软件开发工具包(OSDK)，作为连接整个企业的“操作总线”。

图16：Ontology 促进了与现有企业系统的深度双向互操作性

资料来源：Palantir 官网

数据定义了决策的背景，逻辑则包含了丰富这一背景的推理与分析，使人类与人工智能团队能够做出更优的决策。这些逻辑可以以模型输出和可视化的形式作为额外背景呈现在操作应用程序中，也可以直接嵌入到操作机制中。

基于这一广泛定义，定义和执行逻辑的能力贯穿于整个平台。例如，模型、业务逻辑以及模板化分析与报告均体现了这一能力。

* * *

图17：定义和执行逻辑的能力贯穿于整个平台

资料来源：Palantir 官网

任何决策若要产生实际影响，都必须能够在全球范围内传播。在此过程中，行动定义了企业的“动词”，即具体执行的操作，并控制人类操作员或人工智能代理如何确保其决策的持久性，无论是通过本体数据模型还是通过与外部系统的交互实现。此外，在 Ontology 中捕获决策结果使用户能够将特定决策与未来数据中的结果观察相匹配。这种机制形成了反馈循环，将未来的决策建立在对过去选择的分析之上，
并可用于重新训练或微调模型，或帮助操作员更清晰地理解历史背景。

在 Ontology 中，表示这些“动态”的基本单位是行动（Action）。行动为更改或创建数据以及协调外部系统中的变更提供了精确且细粒度的控制。基本操作可以通过点击表单配置界面轻松定义，而更复杂的操作则可以通过函数支持的操作和本体编辑 TypescriptAPI 实现。此外，操作还可以在 Ontology 软件开发工具包(OSDK)和平台 API 中进行封装，以便自定义应用程序开发和现有第三方工具。

* * *

图18：在 Ontology 中，表示这些“动态”的基本单位是行动

资料来源：Palantir 官网

4.2、 布局：采取多种策略加速获客，提前布局 AIGC

近年来，公司采取了多种销售和营销策略，以加速客户获取能力：

Ø 扩大平台访问范围

公司平台的部署速度大大扩大了计划长期合作的潜在客户范围。2023 年，公司推出了 AIP 训练营，这使公司能够在几天内根据实际客户数据提供真实的工作流程。此外，在 2024 年，公司推出了开发者层，在美国和部分国家/地区提供对 Foundry 和
AIP 的有限访问。这一扩展使开发人员无需大量前期企业成本即可进行探索、创新和开发。

随着公司继续向尽可能广泛的客户群体扩大平台的访问范围，公司与各种企业及其所在行业的密切关系增强了公司自己的产品和业务开发工作，并有望继续增强。

公司已与领先的公共云、私有云及混合云服务提供商建立了紧密合作，并持续探索针对特定行业和领域的定制化合作伙伴关系。这些合作伙伴关系的形成，既满

* * *

足了公司对大规模计算资源的需求，也顺应了客户向云托管环境迁移的趋势。通过利用这些提供商的现有市场覆盖，公司能够触达其庞大的客户群体，并显著扩展了分销能力。

此外，公司正在积极探索与公共和私营组织建立渠道销售关系及类似联盟，为公司与各类技术提供商（包括中小型技术公司）的合作开辟了新的途径。

Ø 合资企业与新业务伙伴关系

公司计划继续建立合资企业和新业务伙伴关系，特别是在特定行业或领域，这些领域需要合作伙伴关系和额外投资以充分发挥平台的潜力。例如，公司通过 Palantir
Technologies Japan KK 与富士通有限公司建立了战略全球合作伙伴关系。通过这一合作，双方将把 Foundry 和 AIP 的功能整合为富士通 Uvance 数据基础设施的核心组成部分。富士通 Uvance 是一套旨在应对业务挑战和解决社会问题的全球解决方案。这一合作不仅增强了平台的应用范围，也为双方在技术创新和市场扩展方面提供了新的机遇。

图19：Palantir 计划继续建立合资企业和新业务伙伴关系

资料来源：Palantir 公告

5、 风险提示

行业竞争的风险、客户拓展的风险、产业链政策落地不及预期风险

Ø 客户增长

Ø 客户增长公司采用多种销售和营销策略来推动客户收入的持续增长。包括：(i)建立新的生态系统合作伙伴关系，将平台从客户业务扩展到其合作伙伴和供应商的运营中；(ii)
销售额外的产品化跨行业软件功能；以及(iii)提供针对特定用例的软件战略实施服务，
以实现竞争差异化。

* * *

特别声明

《证券期货投资者适当性管理办法》、《证券经营机构投资者适当性管理实施指引（试行）》已于2017年7月1日起正式实施。根据上述规定，开源证券评定此研报的风险等级为R4（中高风险），因此通过公共平台推送的研报其适用的投资者类别仅限定为专业投资者及风险承受能力为C4、C5的普通投资者。若您并非专业投资者及风险承受能力为C4、C5的普通投资者，请取消阅读，请勿收藏、接收或使用本研报中的任何信息。因此受限于访问权限的设置，若给您造成不便，烦请见谅！感谢您给予的理解与配合。

分析师承诺

负责准备本报告以及撰写本报告的所有研究分析师或工作人员在此保证，本研究报告中关于任何发行商或证券所发表的观点均如实反映分析人员的个人观点。负责准备本报告的分析师获取报酬的评判因素包括研究的质量和准确性、客户的反馈、竞争性因素以及开源证券股份有限公司的整体收益。所有研究分析师或工作人员保证他们报酬的任何一部分不曾与，不与，也将不会与本报告中具体的推荐意见或观点有直接或间接的联系。

股票投资评级说明

|  | 评级 | 说明 |
| --- | --- | --- |
| 证券评级 | 买入(Buy) | 预计相对强于市场表现20%以上; |
| 增持(outperform) | 预计相对强于市场表现5%~20%; |  |
| 中性(Neutral) | 预计相对市场表现在-5%~+5%之间波动; |  |
| 减持(underperform) | 预计相对弱于市场表现5%以下。 |  |
| 行业评级 | 看好(overweight) | 预计行业超越整体市场表现; |
| 中性(Neutral) | 预计行业与整体市场表现基本持平; |  |
| 看淡(underperform) | 预计行业弱于整体市场表现。 |  |
| 备注：评级标准为以报告日后的6~12个月内，证券相对于市场基准指数的涨跌幅表现，其中A股基准指数为沪深300指数、港股基准指数为恒生指数、新三板基准指数为三板成指（针对协议转让标的）或三板做市指数（针对做市转让标的）、美股基准指数为标普500或纳斯达克综合指数。公司在此提醒您，不同证券研究机构采用不同的评级术语及评级标准。公司采用的是相对评级体系，表示投资的相对比重建议；投资者买入或者卖出证券的决定取决于个人的实际情况，比如当前的持仓结构以及其他需要考虑的因素。投资者应阅读整篇报告，以获取比较完整的观点与信息，不应仅仅依靠投资评级来推断结论。 |  |  |

本报告所包含的分析基于各种假设，不同假设可能导致分析结果出现重大不同。本报告采用的各种估值方法及模型均有其局限性，估值结果不保证所涉及证券能够在该价格交易。

* * *

开源证券股份有限公司是经中国证监会批准设立的证券经营机构，已具备证券投资咨询业务资格。

本报告仅供开源证券股份有限公司（以下简称“本公司”）的机构或个人客户（以下简称“客户”）使用。本公司不会因接收人收到本报告而视其为客户。本报告是发送给开源证券客户的，属于商业秘密材料，只有开源证券客户才能参考或使用，如接收人并非开源证券客户，请及时退回并删除。

本报告是基于本公司认为可靠的已公开信息，但本公司不保证该等信息的准确性或完整性。本报告所载的资料、工具、意见及推测只提供给客户作参考之用，并非作为或被视为出售或购买证券或其他金融工具的邀请或向人做出邀

具、意见及推测只提供给客户作参考之用，并非作为或被视为出售或购买证券或其他金融工具的邀请或向人做出邀请。本报告所载的资料、意见及推测仅反映本公司于发布本报告当日的判断，本报告所指的证券或投资标的的价格、价值及投资收入可能会波动。在不同时期，本公司可发出与本报告所载资料、意见及推测不一致的报告。客户应当考虑到本公司可能存在可能影响本报告客观性的利益冲突，不应视本报告为做出投资决策的唯一因素。本报告中所指的投资及服务可能不适合个别客户，不构成客户私人咨询建议。本公司未确保本报告充分考虑到个别客户特殊的

具、意见及推测只提供给客户作参考之用，并非作为或被视为出售或购买证券或其他金融工具的邀请或向人做出邀请。本报告所载的资料、意见及推测仅反映本公司于发布本报告当日的判断，本报告所指的证券或投资标的的价格、价值及投资收入可能会波动。在不同时期，本公司可发出与本报告所载资料、意见及推测不一致的报告。客户应当考虑到本公司可能存在可能影响本报告客观性的利益冲突，不应视本报告为做出投资决策的唯一因素。本报告中所指的投资及服务可能不适合个别客户，不构成客户私人咨询建议。本公司未确保本报告充分考虑到个别客户特殊的

指的投资及服务可能不适合个别客户，不构成客户私人咨询建议。本公司未确保本报告充分考虑到个别客户特殊的投资目标、财务状况或需要。本公司建议客户应考虑本报告的任何意见或建议是否符合其特定状况，以及（若有必要）咨询独立投资顾问。在任何情况下，本报告中的信息或所表述的意见并不构成对任何人的投资建议。在任何情

要）咨询独立投资顾问。在任何情况下，本报告中的信息或所表述的意见并不构成对任何人的投资建议。在任何情况下，本公司不对任何人因使用本报告中的任何内容所引致的任何损失负任何责任。若本报告的接收人非本公司的客户，应在基于本报告做出任何投资决定或就本报告要求任何解释前咨询独立投资顾问。

要）咨询独立投资顾问。在任何情况下，本报告中的信息或所表述的意见并不构成对任何人的投资建议。在任何情况下，本公司不对任何人因使用本报告中的任何内容所引致的任何损失负任何责任。若本报告的接收人非本公司的客户，应在基于本报告做出任何投资决定或就本报告要求任何解释前咨询独立投资顾问。

本报告可能附带其它网站的地址或超级链接，对于可能涉及的开源证券网站以外的地址或超级链接，开源证券不对其内容负责。本报告提供这些地址或超级链接的目的纯粹是为了客户使用方便，链接网站的内容不构成本报告的任何部分，客户需自行承担浏览这些网站的费用或风险。

开源证券在法律允许的情况下可参与、投资或持有本报告涉及的证券或进行证券交易，或向本报告涉及的公司提供或争取提供包括投资银行业务在内的服务或业务支持。开源证券可能与本报告涉及的公司之间存在业务关系，并无需事先或在获得业务关系后通知客户。

本报告的版权归本公司所有。本公司对本报告保留一切权利。除非另有书面显示，否则本报告中的所有材料的版权均属本公司。未经本公司事先书面授权，本报告的任何部分均不得以任何方式制作任何形式的拷贝、复印件或复制品，或再次分发给任何其他人，或以任何侵犯本公司版权的其他方式使用。所有本报告中使用的商标、服务标记及标记均为本公司的商标、服务标记及标记。

开源证券研究所

邮编：200120

邮箱： [research@kysec.cn](mailto:research@kysec.cn)

地址：北京市西城区西直门外大街18号金贸大厦C2座9层邮编：100044

邮编：518000

邮箱： [research@kysec.cn](mailto:research@kysec.cn)


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
