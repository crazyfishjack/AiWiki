---
title: "调研证据包：投标 AI 提示词 招标解析 Prompt 模板 评分点 废标风险 合规校验"
source-type: article
generated: 2026-06-21
generated-by: wiki-research-skill
research-mode: standard
---

# 调研证据包：投标 AI 提示词 招标解析 Prompt 模板 评分点 废标风险 合规校验

## 调研问题

投标 AI 提示词 招标解析 Prompt 模板 评分点 废标风险 合规校验

## 摘要

本文档是四工具检索生成的证据包草稿，不是最终调研报告。Agent 必须先阅读本证据包，执行下方"AI 综合指令"，生成新的中文综合 raw 报告，然后询问用户是否入库。本证据包保留不删除。

- 发现候选信源：26
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
| exa | 1.00 | [2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models | https://arxiv.org/abs/2309.12132v2 |
| exa | 1.00 | From Large Language Model Predicates to Logic Tensor Networks: Neurosymbolic Offer Validation in Regulated Procurement | https://arxiv.org/html/2604.05539 |
| exa | 1.00 | GRAPH-GRPO-LEX: Contract Graph Modeling and Reinforcement Learning with Group Relative Policy Optimization | https://arxiv.org/html/2511.06618 |
| exa | 1.00 | Construction contract risk identification based on knowledge-augmented language models \| Computers in Industry | https://dl.acm.org/doi/10.1016/j.compind.2024.104082 |
| exa | 1.00 | [2605.29427] FinGuard: Detecting Financial Regulatory Non-Compliance in LLM Interactions | https://arxiv.org/pdf/2605.29427 |
| exa | 1.00 | MarketBench: Evaluating AI Agents as Market Participants | https://arxiv.org/html/2604.23897v1 |
| exa | 1.00 | Intelligent Checking Method for Construction Schemes via Fusion of Knowledge Graph and Large Language Models | https://www.mdpi.com/2075-5309/14/8/2502 |
| exa | 1.00 | PromptBench: A Unified Library for Evaluation of Large Language Models | https://arxiv.org/html/2312.07910v2 |
| exa | 1.00 | AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects | https://www.mdpi.com/1996-1073/14/15/4632 |
| exa | 1.00 | MarketBench: Evaluating AI Agents as Market Participants | https://arxiv.org/pdf/2604.23897 |
| exa | 1.00 |  | https://openreview.net/attachment?id=WCNAcIKREG&name=pdf |
| exa | 1.00 | ResearchRubrics: A Benchmark of Prompts and Rubrics for Evaluating Deep Research Agents | https://openreview.net/pdf?id=ErnvfmSX0P |
| exa | 1.00 |  | https://arxiv.org/pdf/2312.17522 |
| exa | 1.00 | PromptExp: Multi-granularity Prompt Explanation of Large Language Models | https://arxiv.org/html/2410.13073 |
| tavily | 0.62 | 投标总因细节废标？2026 这款 AI 标书工具实用又省心\|通用\|招标_网易订阅 | https://www.163.com/dy/article/KVMTIJ5A0556KMI7.html |
| tavily | 0.59 | 标书智能体（一）——AI解析招标文件代码+提示词 - 博客园 | https://www.cnblogs.com/yibiaoai/p/19064673 |
| tavily | 0.58 | 零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF ... | https://cloud.tencent.com/developer/article/2631225 |
| tavily | 0.55 | 标桥首页 | https://www.bqpoint.com |
| tavily | 0.53 | 【生态合作】钛投标×火山引擎联合发布首个招投标垂直Agent5大原子 ... | https://developer.volcengine.com/articles/7640049781385756718 |
| tavily | 0.51 | 标书软件系统选型推荐_哪家好_价格_免费试用-云巴巴 | https://www.yun88.com/product/biaoshu |
| tavily | 0.47 | 智能标书助手-艾瑞数智 | https://www.idigital.com.cn/common-ai-2 |
| tavily | 0.45 | AI 评标系统双场景技术实现：标书合规检测与围标串标智能识别_深度优先_jiangnan920-AtomGit开源社区 | https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html |
| tavily | 0.45 | 喜鹊标书AI \| AI 标书制作平台与投标方案助手 | https://www.xiquebiaoshu.com |
| tavily | 0.43 | 招标解析（已下线） - 智谱AI开放文档 | https://docs.bigmodel.cn/cn/guide/agents/tender |
| tavily | 0.41 | Prompt, Prompt Engineering, 提示工程, 提示词-大模型服务平台百炼(Model Studio)-阿里云帮助中心 | https://help.aliyun.com/zh/model-studio/prompt-engineering-guide |

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
2. [[2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models](https://arxiv.org/abs/2309.12132v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
3. [From Large Language Model Predicates to Logic Tensor Networks: Neurosymbolic Offer Validation in Regulated Procurement](https://arxiv.org/html/2604.05539)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
4. [GRAPH-GRPO-LEX: Contract Graph Modeling and Reinforcement Learning with Group Relative Policy Optimization](https://arxiv.org/html/2511.06618)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
5. [Construction contract risk identification based on knowledge-augmented language models | Computers in Industry](https://dl.acm.org/doi/10.1016/j.compind.2024.104082)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
6. [[2605.29427] FinGuard: Detecting Financial Regulatory Non-Compliance in LLM Interactions](https://arxiv.org/pdf/2605.29427)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
7. [MarketBench: Evaluating AI Agents as Market Participants](https://arxiv.org/html/2604.23897v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
8. [Intelligent Checking Method for Construction Schemes via Fusion of Knowledge Graph and Large Language Models](https://www.mdpi.com/2075-5309/14/8/2502)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
9. [PromptBench: A Unified Library for Evaluation of Large Language Models](https://arxiv.org/html/2312.07910v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
10. [AI and Text-Mining Applications for Analyzing Contractor’s Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects](https://www.mdpi.com/1996-1073/14/15/4632)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
11. [MarketBench: Evaluating AI Agents as Market Participants](https://arxiv.org/pdf/2604.23897)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
12. [https://openreview.net/attachment?id=WCNAcIKREG&name=pdf](https://openreview.net/attachment?id=WCNAcIKREG&name=pdf)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
13. [ResearchRubrics: A Benchmark of Prompts and Rubrics for Evaluating Deep Research Agents](https://openreview.net/pdf?id=ErnvfmSX0P)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
14. [https://arxiv.org/pdf/2312.17522](https://arxiv.org/pdf/2312.17522)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
15. [PromptExp: Multi-granularity Prompt Explanation of Large Language Models](https://arxiv.org/html/2410.13073)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
16. [投标总因细节废标？2026 这款 AI 标书工具实用又省心|通用|招标_网易订阅](https://www.163.com/dy/article/KVMTIJ5A0556KMI7.html)
   - 工具：tavily
   - 分数：0.62
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
17. [标书智能体（一）——AI解析招标文件代码+提示词 - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.59
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
18. [零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF ...](https://cloud.tencent.com/developer/article/2631225)
   - 工具：tavily
   - 分数：0.58
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
19. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.55
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
20. [【生态合作】钛投标×火山引擎联合发布首个招投标垂直Agent5大原子 ...](https://developer.volcengine.com/articles/7640049781385756718)
   - 工具：tavily
   - 分数：0.53
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
21. [标书软件系统选型推荐_哪家好_价格_免费试用-云巴巴](https://www.yun88.com/product/biaoshu)
   - 工具：tavily
   - 分数：0.51
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
22. [智能标书助手-艾瑞数智](https://www.idigital.com.cn/common-ai-2)
   - 工具：tavily
   - 分数：0.47
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
23. [AI 评标系统双场景技术实现：标书合规检测与围标串标智能识别_深度优先_jiangnan920-AtomGit开源社区](https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html)
   - 工具：tavily
   - 分数：0.45
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
24. [喜鹊标书AI | AI 标书制作平台与投标方案助手](https://www.xiquebiaoshu.com)
   - 工具：tavily
   - 分数：0.45
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
25. [招标解析（已下线） - 智谱AI开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender)
   - 工具：tavily
   - 分数：0.43
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
26. [Prompt, Prompt Engineering, 提示工程, 提示词-大模型服务平台百炼(Model Studio)-阿里云帮助中心](https://help.aliyun.com/zh/model-studio/prompt-engineering-guide)
   - 工具：tavily
   - 分数：0.41
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考

### 剔除信源
1. [Prompt评估 - 百度AI开放平台](https://ai.baidu.com/ai-doc/WENXINWORKSHOP/ilpukpaiq)
   - 工具：tavily
   - 分数：0.39
   - 来源等级：C
   - 剔除原因：score 低于 0.4
2. [招投标会变成AI“全包”吗？答案是“人机搭档”才是未来](https://www.chinabidding.com.cn/pageInfoSsr/3000000016666/1087000001241861)
   - 工具：tavily
   - 分数：0.38
   - 来源等级：C
   - 剔除原因：score 低于 0.4
3. [高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.37
   - 来源等级：C
   - 剔除原因：score 低于 0.4
4. [易标AI](https://yibiao.pro)
   - 工具：tavily
   - 分数：0.34
   - 来源等级：C
   - 剔除原因：score 低于 0.4
5. [企业招投标文件自动比对工具：核心能力解析与智能化落地指南](https://www.ai-indeed.com/encyclopedia/18040.html)
   - 工具：tavily
   - 分数：0.33
   - 来源等级：C
   - 剔除原因：score 低于 0.4
6. [雄安新区加速构建“人工智能+招投标”样板-中国雄安官网](https://www.xiongan.gov.cn/20260313/f79fb28ec6094d8f854675b3e94fdab4/c.html)
   - 工具：tavily
   - 分数：0.31
   - 来源等级：C
   - 剔除原因：score 低于 0.4
7. [[PDF] 招标文件 - 中华人民共和国司法部](https://www.moj.gov.cn/pub/sfbgw/zwxxgk/fdzdgknr/fdzdgknrtzwj/202501/W020250122622938330518.pdf)
   - 工具：tavily
   - 分数：0.27
   - 来源等级：C
   - 剔除原因：score 低于 0.4
8. [标书智能体（一）——AI解析招标文件代码+提示词 - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.59
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
9. [招投标会变成AI“全包”吗？答案是“人机搭档”才是未来](https://www.chinabidding.com.cn/pageInfoSsr/3000000016666/1087000001241861)
   - 工具：tavily
   - 分数：0.39
   - 来源等级：C
   - 剔除原因：score 低于 0.4
10. [Prompt 模板库 - AI 实战模板与结构化输出 | JR Academy](https://jiangren.com.au/tools/prompt-templates)
   - 工具：tavily
   - 分数：0.34
   - 来源等级：C
   - 剔除原因：score 低于 0.4
11. [企业招投标文件自动比对工具：核心能力解析与智能化落地指南](https://www.ai-indeed.com/encyclopedia/18040.html)
   - 工具：tavily
   - 分数：0.32
   - 来源等级：C
   - 剔除原因：score 低于 0.4
12. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统](https://patents.google.com/patent/CN119624385A/zh)
   - 工具：tavily
   - 分数：0.31
   - 来源等级：C
   - 剔除原因：score 低于 0.4
13. [[PDF] 基于生成式AI的招标文件智能编制与合规性实时审查模型构建研究](https://ojs.vitu-pub.com/index.php/gcjsfzs/article/viewFile/158342/157237)
   - 工具：tavily
   - 分数：0.29
   - 来源等级：C
   - 剔除原因：score 低于 0.4
14. [Prompt Engineering 教學：系統化提示設計完全指南](https://www.meta-intelligence.tech/insight-prompt-engineering)
   - 工具：tavily
   - 分数：0.29
   - 来源等级：C
   - 剔除原因：score 低于 0.4
15. [Prompt模板概述-大模型服务平台百炼(Model Studio) - 阿里云帮助文档](https://help.aliyun.com/zh/model-studio/prompt-template)
   - 工具：tavily
   - 分数：0.23
   - 来源等级：C
   - 剔除原因：score 低于 0.4
16. [China securities regulator warns against speculating on 'tech hype' and using AI for stock picking - CNBC](https://www.cnbc.com/2026/06/17/china-securities-regulator-csrc-artificial-intelligence-investing-stocks-.html)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
17. [Leadership in Regulatory & Quality Compliance - Fierce Biotech](https://www.fiercebiotech.com/cro/leadership-regulatory-quality-compliance)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
18. [AI & Advanced Analytics - Fierce Biotech](https://www.fiercebiotech.com/cro/ai-advanced-analytics)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
19. [2026 Fierce Outsourcing Awards - Fierce Biotech](https://www.fiercebiotech.com/book/2026-fierce-outsourcing-awards)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
20. [Clinical Trial Management - Fierce Biotech](https://www.fiercebiotech.com/cro/clinical-trial-management)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
21. [Supply Chain Excellence - Fierce Biotech](https://www.fiercebiotech.com/cro/supply-chain-excellence)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
22. [Digital Transformation Partner - Fierce Biotech](https://www.fiercebiotech.com/cro/digital-transformation-partner)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
23. [Excellence in Client Service & Partnership - Fierce Biotech](https://www.fiercebiotech.com/cro/excellence-client-service-partnership)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
24. [零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF ...](https://cloud.tencent.com/developer/article/2631225)
   - 工具：tavily
   - 分数：0.56
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
25. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.51
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
26. [AI写标书如何避免废标与串标？深度解析RAG、私有知识库的选型关键 - 陈工0237 - 企业博客](https://www.cnblogs.com/biaoshu1234/p/20287913)
   - 工具：tavily
   - 分数：0.36
   - 来源等级：C
   - 剔除原因：score 低于 0.4
27. [易标AI](https://yibiao.pro)
   - 工具：tavily
   - 分数：0.33
   - 来源等级：C
   - 剔除原因：score 低于 0.4
28. [解决方案 快书编标为制作标书能做更多的事情](https://www.kshbb.com/AIIntelligent.html)
   - 工具：tavily
   - 分数：0.30
   - 来源等级：C
   - 剔除原因：score 低于 0.4
29. [Prompt模板概述-大模型服务平台百炼(Model Studio) - 阿里云帮助文档](https://help.aliyun.com/zh/model-studio/prompt-template)
   - 工具：tavily
   - 分数：0.21
   - 来源等级：C
   - 剔除原因：score 低于 0.4
30. [[PDF] 招标文件 - 信息资源系统](https://13115299.s21i.faiusr.com/61/1/ABUIABA9GAAg3PPYkwYo1Jy2mQE.pdf)
   - 工具：tavily
   - 分数：0.18
   - 来源等级：C
   - 剔除原因：score 低于 0.4
31. [标书智能体（一）——AI解析招标文件代码+提示词 - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.56
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
32. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.53
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
33. [喜鹊标书AI | AI 标书制作平台与投标方案助手](https://www.xiquebiaoshu.com)
   - 工具：tavily
   - 分数：0.40
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
34. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统](https://patents.google.com/patent/CN119624385A/zh)
   - 工具：tavily
   - 分数：0.40
   - 来源等级：C
   - 剔除原因：score 低于 0.4
35. [易标AI](https://yibiao.pro)
   - 工具：tavily
   - 分数：0.34
   - 来源等级：C
   - 剔除原因：score 低于 0.4
36. [[PDF] 招标文件 - 中华人民共和国司法部](https://www.moj.gov.cn/pub/sfbgw/zwxxgk/fdzdgknr/fdzdgknrtzwj/202501/W020250122622938330518.pdf)
   - 工具：tavily
   - 分数：0.33
   - 来源等级：C
   - 剔除原因：score 低于 0.4
37. [高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.33
   - 来源等级：C
   - 剔除原因：score 低于 0.4

## 完整精读结果

### 来源 1: 【生态合作】钛投标×火山引擎联合发布首个招投标垂直Agent5大原子 ...

- URL: https://developer.volcengine.com/articles/7640049781385756718
- 精读方法：firecrawl-scrape

[![](https://lf3-static.bytednsdoc.com/obj/eden-cn/nulopslf/developer/community_logo.svg)](https://developer.volcengine.com/)

[文档](https://www.volcengine.com/docs) [备案](https://www.volcengine.com/beian) [控制台](https://console.volcengine.com/home)

[登录](https://console.volcengine.com/auth/login?redirectURI=https%3A%2F%2Fdeveloper.volcengine.com%2Farticles%2F7640049781385756718) [免费开始使用](https://console.volcengine.com/auth/signup?redirectURI=https%3A%2F%2Fdeveloper.volcengine.com%2Farticles%2F7640049781385756718)

[免费注册](https://console.volcengine.com/auth/signup?redirectURI=https%3A%2F%2Fdeveloper.volcengine.com%2Farticles%2F7640049781385756718) [登录](https://console.volcengine.com/auth/login?redirectURI=https%3A%2F%2Fdeveloper.volcengine.com%2Farticles%2F7640049781385756718)

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

【生态合作】钛投标×火山引擎联合发布首个招投标垂直Agent5大原子化AI Skills零代码快速集

一、整体技术架构

二、核心能力：5个招投标垂直原子化Skills

1.招标解析Skill

2.标书生成Skill

3.标书美化Skill

4.标书检查Skill

5.标书查重Skill

三、ArkClaw编排：实现招投标全流程自动化落地

四、集成方式：低代码/零代码快速接入

五、安全与合规设计

六、总结与未来展望

评论区

# 【生态合作】钛投标×火山引擎联合发布首个招投标垂直Agent5大原子化AI Skills零代码快速集

[![TAI Bidding](https://p6-passport.byteacctimg.com/img/user-avatar/36b89f98458e1d236307fb8af06cb5ca~300x300.image)\\
\\
TAI Bidding](https://developer.volcengine.com/user/4280812909110169)

2026-05-15

[AI](https://developer.volcengine.com/articles?category=3)

Skill

![](https://portal.volccdn.com/obj/volcfe-scm/deploy/volc_developer_/42325/static/image/rec-product.424eb1f0.png)

应用型负载均衡

[了解详情](https://www.volcengine.com/product/alb?utm_campaign=20241107&utm_content=allproduct&utm_medium=in_banner&utm_source=community&utm_term=guanggaowei)

面向 7 层互联网应用及云原生应用，基于内容精细化调度，提供稳定、弹性、安全、高性能的应用层负载均衡服务

随着大模型应用日趋成熟，行业发展重心正从通用模型能力探索，逐步转向垂直领域的商业化落地，以 **Agent+Skills** 为核心的建设模式，也成为了企业搭建AI体系的主流选择。

![picture.image](https://p3-volc-community-sign.byteimg.com/tos-cn-i-tlddhu82om/95a63502fcd04fd0bc2136167608a01f~tplv-tlddhu82om-image.image?=&rk3s=8031ce6d&x-expires=1782150730&x-signature=7N0NqiJsSegVJOefWGcHzBx0dOw%3D)
招投标作为政企采购核心场景，长期面临非结构化文本占比高、规则强、合规约束严，流程长、环节多、数据格式异构（PDF、Word、扫描件、网页公告），传统系统耦合重、扩展差，难以接入大模型能力，自建行业模型成本高、标注难、迭代慢等痛点。

针对这一行业痛点， **钛投标与火山引擎达成深度生态合作**，依托火山引擎 **MaaS底座+ArkClaw智能体+EcoMesh技能/Agent市场** 技术体系，联合打造行业首个招投标垂直Agent生态。通过将招投标领域多年积累的专业能力拆解为可插拔、可编排、可复用的原子化AI微服务（Skills），提供从解析、生成、排版、审查到查重的全链路AI能力，让企业以低改造成本，快速落地适配自身业务的行业AI，真正推动招投标行业从"人力驱动"向"算力驱动"转型。

## **一、整体技术架构**

本次解决方案采用 **"底座—ArkClaw智能体—技能—业务系统"** 四层分层架构，实现能力解耦与灵活扩展：

**底层：火山引擎MaaS底座**

支持多模型统一接入（豆包大模型、行业垂直模型）

提供企业级推理、批量处理、私有部署/混合部署能力

实现权限、审计、数据隔离、加密链路的统一管控

**智能体层：ArkClaw**

核心负责意图理解、任务拆解、技能编排、结果整合

支持多轮规划、异常分支处理、自动重试、工具链串联

与钛投标行业逻辑深度集成，形成招投标领域专用智能体

**技能层：钛投标5大招投标Skills（原子化能力）**

每个Skill独立封装输入输出、调用协议、权限控制

可单独调用、可链式编排、可按需组合，也可使用完整集成Agent

统一接入火山引擎EcoMesh技能/Agent市场，支持一键注册、一键部署、一键集成

**业务层：企业现有系统**

通过标准OpenClaw/Hermes协议对接，低侵入、无强耦合

可与企业内部ERP、OA、政采云、自研系统实现全流程集成

## **二、核心能力：5个招投标垂直原子化Skills**

本次联合发布的招投标垂直Agent，核心包含5大原子化AI微服务，覆盖招投标全流程核心环节，实现"读、写、排、审、防"全自动化：

### **1.招标解析Skill**

**输入**：PDF、Word、扫描件、网页公告

**核心能力**：版式分析、表格识别、关键信息结构化抽取

**输出**：JSON结构化字段（废标项、评分细则、资质要求、预算、工期、技术参数）

**技术要点**：混合布局解析+规则引擎+行业知识图谱校验

**解决痛点**：人工解读长文本招标文件耗时久、漏项风险高

### **2.标书生成Skill**

**输入**：结构化招标要求+企业私有知识库+历史标案库

**核心能力**：章节生成、逻辑链构建、商务/技术内容自动撰写、合规约束校验

**输出**：可编辑Word初稿

**技术要点**：领域Prompt模板化+RAG私有知识召回+大纲+段落两级生成

**解决痛点**：标书撰写工作量大、内容匹配度低、逻辑不清晰

### **3.标书美化Skill**

**输入**：Word文档

**核心能力**：目录生成、样式统一、页眉页脚/页码标准化、图表格式校正、多级标题规范

**输出**：符合行业规范的合规排版Word

**技术要点**：模板引擎+样式规则库+文档DOM结构化遍历

**解决痛点**：人工排版效率低、格式不统一、不符合招标方要求

### **4.标书检查Skill**

**输入**：标书+招标文件+行业规则库

**核心能力**：资质匹配校验、废标项命中检测、暗标合规、格式风险、逻辑冲突检查

**输出**：风险报告（标注风险位置、原因及建议修复方案）

**技术要点**：规则引擎+关键词/正则库+意图校验模型

**解决痛点**：人工检查易遗漏、废标风险高、合规性难以保障

### **5.标书查重Skill**

**输入**：多份标书文本

**核心能力**：跨文档相似度计算、片段级重复检测、来源溯源

**输出**：相似度矩阵、重复片段定位报告

**技术要点**：向量检索+局部序列比对+行业文本指纹

**解决痛点**：标书雷同风险高、串标隐患难以排查

## **三、ArkClaw编排：实现招投标全流程自动化落地**

基于火山引擎ArkClaw智能体的编排能力，可将上述5个原子化Skill串联成完整的自动化业务链路，无需人工干预即可完成全流程流转：

导入招标文件→调用 **招标解析Skill** →完成招标信息结构化处理

结合结构化招标信息和企业私有知识库→调用 **标书生成Skill** →生成标书初稿

针对初稿文档→调用 **标书美化Skill** →实现全文标准化排版优化

对比排版后的标书与招标规则→调用 **标书检查Skill** →执行全面风险扫描

批量导入多份标书→调用 **标书查重Skill** →完成合规性查重校验

**最终输出**：标书终稿+风险评估报告+查重报告

**运行特性**：全程采用API化调度，任务状态可实时追踪，任一节点失败后支持自动重试

**扩展能力**：支持定时任务、批量处理以及事件触发（例如：新招标公告入库后自动启动处理流程）

## **四、集成方式：低代码/零代码快速接入**

企业无需重构现有业务系统，通过以下三步即可快速接入全套AI招投标能力：

在火山方舟平台开通模型权限和ArkClaw智能体服务

在EcoMesh技能/Agent市场安装「钛投标招投标Skills或Agents」

选择适合的调用方式：

**对话式调用**：通过ArkClaw自然语言对话直接调用招投标技能和Agent

**API调用**：通过OpenAPI直接调用单个Skill，实现灵活定制

**系统集成**：采用标准JSON接口对接自有系统，支持同步/异步回调

## **五、安全与合规设计**

招投标业务涉及企业核心商业信息与资质数据，数据安全至关重要。本次解决方案全面依托火山引擎企业级安全能力体系，提供全维度安全保障：

**数据安全**：全链路TLS加密、标书数据隔离存储、支持私有化部署

**权限控制**：基于角色的API访问控制、Skill调用细粒度授权

**审计追溯**：调用日志全留存、参数脱敏处理、所有操作可追溯

**合规适配**：全面适配等保要求、操作留痕、敏感字段脱敏输出

## **六、总结与未来展望**

钛投标与火山引擎将招投标行业的核心能力拆解为可复用的原子化Skills，并通过ArkClaw智能体跑通了全流程自动化落地。技术团队无需从零搭建模型与业务逻辑，即可快速接入行业化的AI智能体，把文本处理、规则校验这些高重复、强约束的工作交给自动化，大幅降低大模型在垂直行业的落地门槛。

未来，火山引擎将持续开放MaaS、智能体等核心技术能力，携手钛投标陆续推出更多招投标垂直Skill，包括标后履约、数据分析、智能预警等方向，同时补充更多样例、SDK和最佳实践。欢迎广大开发者与企业体验本次发布的招投标垂直Agent及AI Skills，共同探索大模型在行业场景的深度应用价值。

245

0

0

0

点赞评论收藏分享

关于作者

[![TAI Bidding](https://p6-passport.byteacctimg.com/img/user-avatar/36b89f98458e1d236307fb8af06cb5ca~300x300.image)](https://developer.volcengine.com/user/4280812909110169)

[TAI Bidding](https://developer.volcengine.com/user/4280812909110169)

关注

关于作者

[![TAI Bidding](https://p6-passport.byteacctimg.com/img/user-avatar/36b89f98458e1d236307fb8af06cb5ca~300x300.image)](https://developer.volcengine.com/user/4280812909110169)

[TAI Bidding](https://developer.volcengine.com/user/4280812909110169)

文章

244

获赞

0

收藏

0

关注

相关资源

CV 技术在视频创作中的应用

本次演讲将介绍在拍摄、编辑等场景，我们如何利用 AI 技术赋能创作者；以及基于这些场景，字节跳动积累的领先技术能力。

点击下载

相关产品

应用型负载均衡

面向 7 层互联网应用及云原生应用，基于内容精细化调度，提供稳定、弹性、安全、高性能的应用层负载均衡服务

[了解详情](https://www.volcengine.com/product/alb?utm_campaign=20241107&utm_content=allproduct&utm_medium=in_banner&utm_source=community&utm_term=guanggaowei)

缓存数据库 Redis 版

与Redis兼容的全托管缓存和存储服务，以其超高读写性能为企业应用赋能

[了解详情](https://www.volcengine.com/product/redis?utm_campaign=20241107&utm_content=allproduct&utm_medium=in_banner&utm_source=community&utm_term=guanggaowei)

专线连接

专线连接是一种连接用户本地数据中心与火山引擎云上网络的服务，能够搭建高速、低时延、稳定安全的专属通道

[了解详情](https://www.volcengine.com/product/directconnect?utm_campaign=20241107&utm_content=allproduct&utm_medium=in_banner&utm_source=community&utm_term=guanggaowei)

推荐阅读

[2026 重庆 GEO 服务商权威排名｜本地实测 5 强，靠谱 AI 获客机构首选盘点\\
\\
2026-06-17](https://developer.volcengine.com/articles/7652546112418480171) [云上应用接美股行情 API：先用 AAPL.US 跑通三关验证\\
\\
2026-06-19](https://developer.volcengine.com/articles/7653012947572097075) [2026年第一季度全国GEO服务商综合实力PK赛，来自重庆的黑马团队—重庆百云数知公司稳居行业榜首！\\
\\
2026-06-20](https://developer.volcengine.com/articles/7653362580609892398) [别让AI把你讲错：B2B企业如何用GEO做“品牌事实对齐”？\\
\\
2026-06-17](https://developer.volcengine.com/articles/7652286497006796838) [同行在用的豆包获客是什么\\
\\
2026-06-21](https://developer.volcengine.com/articles/7653436752526311460)

评论

未登录

看完啦，登录分享一下感受吧～

暂无评论

售前客服

售后客服

购买咨询

业务咨询

### 来源 2: 零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF ...

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

### 来源 3: 投标总因细节废标？2026 这款 AI 标书工具实用又省心|通用|招标_网易订阅

- URL: https://www.163.com/dy/article/KVMTIJ5A0556KMI7.html
- 精读方法：firecrawl-scrape

antanalysis set uid,donnot delete.

![](https://www.163.com/dy/article/KVMTIJ5A0556KMI7.html)

[网易首页](https://www.163.com/ "网易首页")

[应用](https://www.163.com/#f=topnav)

- [_网易新闻_](https://m.163.com/newsapp/#f=topnav)
- [_网易公开课_](https://open.163.com/#f=topnav)
- [_网易红彩_](https://hongcai.163.com/?from=pcsy-button)
- [_网易严选_](https://u.163.com/aosoutbdbd8)
- [_邮箱大师_](https://mail.163.com/client/dl.html?from=mail46)
- [_网易云课堂_](https://study.163.com/client/download.htm?from=163app&utm_source=163.com&utm_medium=web_app&utm_campaign=business)

无障碍浏览 [进入关怀版](https://www.163.com/dy/article/KVMTIJ5A0556KMI7_pdya11y.html)

_快速导航_

- ### [新闻](https://news.163.com/)

- [国内](https://news.163.com/domestic)
- [国际](https://news.163.com/world)
- [王三三](https://news.163.com/special/wangsansanhome/)

- ### [体育](https://sports.163.com/)

- [NBA](https://sports.163.com/nba)
- [CBA](https://sports.163.com/cba)
- [综合](https://sports.163.com/allsports)
- [中超](https://sports.163.com/zc)
- [国际足球](https://sports.163.com/world)
- [英超](https://sports.163.com/yc)
- [西甲](https://sports.163.com/xj)
- [意甲](https://sports.163.com/yj)

- ### [娱乐](https://ent.163.com/)

- [明星](https://ent.163.com/star)
- [电影](https://ent.163.com/movie)
- [电视](https://ent.163.com/tv)
- [音乐](https://ent.163.com/music)
- [封面故事](https://ent.163.com/special/fmgs/)

- ### [财经](https://money.163.com/)

- [股票](https://money.163.com/stock)
- [原创](https://money.163.com/special/caijingyuanchuang/)
- [智库](https://money.163.com/special/wycjzk-pc/)

- ### [汽车](https://auto.163.com/)

- [购车](https://auto.163.com/buy)
- [车型库](http://product.auto.163.com/)

- ### [科技](https://tech.163.com/)

- [网易智能](https://tech.163.com/smart/)
- [原创](https://tech.163.com/special/S1554800475317/)
- [IT](https://tech.163.com/it)
- [互联网](https://tech.163.com/internet)
- [通信](https://tech.163.com/telecom/)

- ### [时尚](https://fashion.163.com/)

- [艺术](https://fashion.163.com/art)
- [旅游](https://travel.163.com/)

- ### [手机](https://mobile.163.com/)/ [数码](https://digi.163.com/)

- [惊奇科技](https://mobile.163.com/special/jqkj_list/)
- [易评机](https://mobile.163.com/special/cpshi_list/)
- [家电](https://hea.163.com/)

- ### [房产](https://house.163.com/)/ [家居](https://home.163.com/)

- [北京房产](https://bj.house.163.com/)
- [上海房产](https://sh.house.163.com/)
- [广州房产](https://gz.house.163.com/)
- [楼盘库](https://xf.house.163.com/)
- [设计师库](https://designer.home.163.com/search)
- [案例库](https://photo.home.163.com/)

- ### [教育](https://edu.163.com/)

- [留学](https://edu.163.com/liuxue)
- [高考](https://edu.163.com/gaokao)

[查看网易地图](https://sitemap.163.com/)

[登录](https://reg.163.com/)

[注册免费邮箱](https://mail.163.com/register/index.htm?from=163navi&regPage=163)

- [注册VIP邮箱（特权邮箱，付费）](https://reg1.vip.163.com/newReg1/reg?from=new_topnav&utm_source=new_topnav)
- [免费下载网易官方手机邮箱应用](https://mail.163.com/client/dl.html?from=mail46)

安全退出

- [_移动端_](https://www.163.com/newsapp/#f=163nav)

[![](https://static.ws.126.net/f2e/include/common_nav/images/topapp.jpg)](https://www.163.com/newsapp/#f=163nav)

- [_网易公开课_](https://open.163.com/#ftopnav0)

  - [TED](https://open.163.com/ted/#ftopnav1)
  - [中国大学视频公开课](https://open.163.com/cuvocw/#ftopnav2)
  - [国际名校公开课](https://open.163.com/ocw/#ftopnav3)
  - [赏课·纪录片](https://open.163.com/appreciation/#ftopnav4)
  - [付费精品课程](https://vip.open.163.com/#ftopnav5)
  - [北京大学公开课](https://open.163.com/special/School/beida.html#ftopnav6)
  - [英语课程学习](https://open.163.com/newview/movie/courseintro?newurl=ME7HSJR07#ftopnav7)

- [_网易严选_](https://you.163.com/?from=web_fc_menhu_xinrukou_1)

  - [新人特价](https://act.you.163.com/act/pub/ABuyLQKNmKmK.html?from=out_ynzy_xinrukou_2)
  - [9.9专区](https://you.163.com/topic/v1/pub/Pew1KBH9Au.html?from=out_ynzy_xinrukou_3)
  - [新品热卖](https://you.163.com/item/newItemRank?from=out_ynzy_xinrukou_4)
  - [人气好物](https://you.163.com/item/recommend?from=out_ynzy_xinrukou_5)
  - [居家生活](https://you.163.com/item/list?categoryId=1005000&from=out_ynzy_xinrukou_7)
  - [服饰鞋包](https://you.163.com/item/list?categoryId=1010000&from=out_ynzy_xinrukou_8)
  - [母婴亲子](https://you.163.com/item/list?categoryId=1011000&from=out_ynzy_xinrukou_9)
  - [美食酒水](https://you.163.com/item/list?categoryId=1005002&from=out_ynzy_xinrukou_10)

- [_支付_](https://ecard.163.com/)

  - [一卡通充值](https://ecard.163.com/#f=topnav)
  - [一卡通购买](https://ecard.163.com/script/index#f=topnav)
  - [我的网易支付](https://epay.163.com/)
  - [网易跨境支付](https://globalpay.163.com/home)

- _邮箱_

  - [免费邮箱](https://email.163.com/#f=topnav)
  - [VIP邮箱](https://vipmail.163.com/#f=topnav)
  - [企业邮箱](https://qiye.163.com/?from=NetEase163top)
  - [免费注册](https://mail.163.com/register/index.htm?from=ntes_nav&regPage=163)
  - [客户端下载](https://mail.163.com/dashi/dlpro.html?from=mail46)

[网易首页](https://www.163.com/) \> [网易号](https://dy.163.com/) \> 正文
[申请入驻](https://dy.163.com/wemedia/index.html)

# 投标总因细节废标？2026 这款 AI 标书工具实用又省心

2026-06-18 10:34:36　来源: [别摸鲨鱼的脚](https://www.163.com/dy/media/T1772013324233.html) ![](https://static.ws.126.net/163/f2e/dy_media/dy_media/static/images/ipLocation.f6d00eb.svg)湖北

[举报](https://www.163.com/special/0077jt/tipoff.html?title=%E6%8A%95%E6%A0%87%E6%80%BB%E5%9B%A0%E7%BB%86%E8%8A%82%E5%BA%9F%E6%A0%87%EF%BC%9F2026%20%E8%BF%99%E6%AC%BE%20AI%20%E6%A0%87%E4%B9%A6%E5%B7%A5%E5%85%B7%E5%AE%9E%E7%94%A8%E5%8F%88%E7%9C%81%E5%BF%83)

[快速发贴](https://www.163.com/dy/article/KVMTIJ5A0556KMI7.html#post_comment_area "快速发贴")[0](https://comment.tie.163.com/KVMTIJ5A0556KMI7.html "点击查看跟贴")

分享至

![Scan me!](<Base64-Image-Removed>)

用微信扫码二维码

分享至好友和朋友圈

做招投标的同行，大概都有过这种憋屈的经历：熬了三四个通宵打磨的标书，方案、报价、业绩样样做足了准备，结果开标就因为一处格式偏差、一条评分项漏响应、一个资质有效期没核对，直接被判废标，所有心血全部打了水漂。

行业里有个不成文的说法：十次废标九次是细节。很多时候不是企业实力不够，而是几百页的招标文件里，废标红线藏得太散、太细，纯靠人工逐页核对，再细心的人也难免有百密一疏的时候。不少团队试过用通用大模型帮忙写标书，最后却发现用处有限 —— 通用 AI 只会生成通顺的文字，既不懂招投标的评审规则，也识别不了隐性风险，甚至会凭空编造资质业绩，改起来比自己写还费时间。

在 2026 年的 AI 标书工具市场里，钛投标就是一款以实用性见长的产品，没有花哨的概念，专注把 “解标准、风控严、成本灵活” 这几件事做透，成了很多投标团队悄悄在用的提效利器。

![](https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2026%2F0618%2Ff356ce12j00tgt35a000vd000zk00npm.jpg&thumbnail=660x2147483647&quality=80&type=jpg)

几百页招标文件不用逐字啃，3 分钟抓全核心要求

投标的第一道坎，永远是解读招标文件。人工通读一份上百页的招标文档，光是梳理资质要求、评分细则、格式规范就要耗掉大半天，稍有不慎还会漏掉藏在备注、附件里的隐性要求，给后续编标埋下隐患。

钛投标针对招投标场景做了专属大模型优化，对长文档理解能力做了定向强化。上传招标文件后，3 分钟就能完成全文深度解析，自动提取资质门槛、评分标准、废标条款、递交要求、格式规范等核心信息，关键要素提取准确率处于行业第一梯队。哪怕是散落在正文边角、附件说明里的隐性要求，也能被精准识别并高亮标注，不用再反复翻页查找，前期信息梳理的效率能提升好几倍。

对投标团队来说，这不止是省时间，更是从源头减少了 “漏看要求” 这种低级失误，拿到项目就能快速判断能不能投、重点要补什么，不用等到编标后半段才发现踩了门槛。

数百项风控规则兜底，躲开绝大多数冤枉废标

很多人用 AI 标书工具，最担心的是 “生成快但错得也快”，反而增加废标风险。钛投标的核心优势，恰恰是把合规风控做成了核心能力，而不是可有可无的附加功能。

平台内置了 32 大类、三百余项细分废标检测规则，覆盖资质有效期、条款响应度、格式规范、报价逻辑、签章要求、暗标规则等绝大多数常见废标场景。生成标书的全过程会同步进行多轮校验，每一处风险都会精准定位到具体章节，附上对应的招标原文依据和可落地的整改建议，相当于给标书做了一次全方位的合规体检。

从不少团队的实测反馈来看，这套风控体系能排查掉绝大多数人工容易忽略的细节问题，大幅降低 “冤枉废标” 的概率。尤其是人手有限、没有专职审核岗的中小团队，相当于用很低的成本配齐了一道专业审核防线。

全行业适配不套模板，优质经验还能持续沉淀

通用 AI 写标书常被吐槽 “假大空”，就是因为不懂行业逻辑，写出来的内容全是套话，落地性很差。

钛投标覆盖了工程建设、IT 信息等 200 多个细分行业，每个行业都有专属的规则库和案例库，生成的内容贴合行业表述习惯与评审标准。比如工程类的施工组织设计、IT 类的技术方案架构、医疗类的合规资质表述，输出内容的专业度远高于通用 AI，不用再花大量时间做行业化返工。

针对有沉淀需求的团队，它还支持搭建企业私有知识库。历史中标标书、资质证件、业绩案例、技术方案都可以统一上传入库，做新项目时 AI 会自动匹配调用对应素材，优质方案复用率很高。知识库用得越久，团队的投标资产越扎实，哪怕有人员流动，核心经验也不会跟着流失。对于经常承接大型项目的团队，千页级标书一键生成的能力，也能大幅缩短初稿产出周期。

成本友好不捆绑，大小团队都能用得起

市面上不少专业标书工具动辄上万年费，对于投标频率不高的中小团队来说，性价比很低，用几次就闲置了。

钛投标采用的是 “基础功能免费 \+ 增值服务按需付费” 的模式，日常使用率最高的招标解析、基础标书生成、合规校验、格式排版等核心功能，全部免费开放，企业完成认证即可使用，没有生成次数和导出数量的限制。对低频投标的中小团队和个人从业者来说，基本可以零成本满足日常需求，不用为了一年几次的项目承担高额年费。

高频使用的团队可以按需选择月度或年度会员，解锁高级风控、知识库扩容、团队协作等功能；对数据安全有高要求的企业项目团队，也支持全本地化私有化部署，平台本身具备等保三级、数据加密等安全资质，数据安全有足够保障。不同规模、不同需求的团队，都能找到适配的方案。

说到底，AI 标书工具的价值从来不是 “替代人写标书”，而是把人工从重复的核对、排版、基础撰写工作里解放出来，把精力放回报价策略、方案亮点、竞争分析这些真正决定中标率的事情上。

声明：个人原创，仅供参考

特别声明：以上内容(如有图片或视频亦包括在内)为自媒体平台“网易号”用户上传并发布，本平台仅提供信息存储服务。

Notice: The content above (including the pictures and videos if any) is uploaded and posted by a user of NetEase Hao, which is a social media platform and only provides information storage services.

[![](https://static.ws.126.net/tie/2017/5/tie_box_ad_2.jpg)](http://go.163.com/2017/1030/taidu/index.html) 关闭

[注册](http://reg.163.com/reg0.shtml?product=tie&url=https://www.163.com/dy/article/KVMTIJ5A0556KMI7.html) _\|_ [手机发跟贴](http://m.163.com/newsapp/)

登录并发贴

网友评论仅供其表达个人看法，并不表明网易立场。

目前没有热门跟贴

目前没有跟贴，欢迎你发表观点

[查看更多跟贴](https://comment.tie.163.com/KVMTIJ5A0556KMI7.html)

[去跟贴广场看看](http://tie.163.com/?f=0tie)

_/_ 阅读下一篇 _/_

[返回网易首页](https://www.163.com/?f=post2020_dy) [下载网易新闻客户端](https://www.163.com/newsapp/#f=post2020_dy)

相关推荐

热点推荐

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little517c4cb713cj00tgz18301bkd001hc00u0g.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVV6BKE30519DDQ2.html?f=post2020_dy_recommends)

### [从眼控到脑控，蔡磊化身“赛博躯体”称将把意识传送到具身机器人](https://www.163.com/dy/article/KVV6BKE30519DDQ2.html?f=post2020_dy_recommends)

第一财经资讯 2026-06-21 15:40:24

[205\\
_跟贴_ 205](https://www.163.com/dy/article/KVV6BKE30519DDQ2.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/ce561534j00tgzhq300c5d000te00g8m.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVQL5AG051100B9.html?f=post2020_dy_recommends)

### [大批歌手即将失业？实测AI作曲仅需5分钟，传统音乐被逼死胡同？](https://www.163.com/dy/article/KVVQL5AG051100B9.html?f=post2020_dy_recommends)

雷科技 2026-06-21 21:37:09

[19\\
_跟贴_ 19](https://www.163.com/dy/article/KVVQL5AG051100B9.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/a3f9a6afj00tgzcyx00sxd000v900dbp.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVKE19V0511AQHO.html?f=post2020_dy_recommends)

### [快手开源GoLongRL：23K样本、9大任务类型，长上下文RL荒时代结束](https://www.163.com/dy/article/KVVKE19V0511AQHO.html?f=post2020_dy_recommends)

机器之心Pro 2026-06-21 19:52:29

[0\\
_跟贴_ 0](https://www.163.com/dy/article/KVVKE19V0511AQHO.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/e3d71baaj00tgzgvo013rd000u000gwm.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVPK45705119734.html?f=post2020_dy_recommends)

### [南洋理工推出支持物理仿真三维模型！生成资产可部署于机器人训练](https://www.163.com/dy/article/KVVPK45705119734.html?f=post2020_dy_recommends)

DeepTech深科技 2026-06-21 21:17:07

[0\\
_跟贴_ 0](https://www.163.com/dy/article/KVVPK45705119734.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/638f1ac3j00tgzgom00v8d000u000grm.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVPCCHE05119734.html?f=post2020_dy_recommends)

### [25亿美金估值，零收入、这家公司试图用大脑算法破解AI能耗危机](https://www.163.com/dy/article/KVVPCCHE05119734.html?f=post2020_dy_recommends)

DeepTech深科技 2026-06-21 21:13:02

[1\\
_跟贴_ 1](https://www.163.com/dy/article/KVVPCCHE05119734.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little3634a39d1f2j00tgyrqq006hd000rs00k0g.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVSSHMB051188EA.html?f=post2020_dy_recommends)

### [死磕完几十个一线案例，我们对AI怎么落地营销服有了这些判断](https://www.163.com/dy/article/KVVSSHMB051188EA.html?f=post2020_dy_recommends)

虎嗅APP 2026-06-21 22:14:07

[0\\
_跟贴_ 0](https://www.163.com/dy/article/KVVSSHMB051188EA.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/430773e9j00tgzh0200jrd000sg00c4p.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVPOFE60511AQHO.html?f=post2020_dy_recommends)

### [AI隐私训练时，那个最难控制的「阀门」能自动调节吗？](https://www.163.com/dy/article/KVVPOFE60511AQHO.html?f=post2020_dy_recommends)

机器之心Pro 2026-06-21 21:19:41

[0\\
_跟贴_ 0](https://www.163.com/dy/article/KVVPOFE60511AQHO.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little918443c6ea7j00tgr8vk00lqd000xc00ism.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVKBOE4G0511C2NV.html?f=post2020_dy_recommends)

### [投标书怎么写简单?用AI专门写投标标书一劳永逸](https://www.163.com/dy/article/KVKBOE4G0511C2NV.html?f=post2020_dy_recommends)

澎湃黑科技 2026-06-17 10:43:09

[0\\
_跟贴_ 0](https://www.163.com/dy/article/KVKBOE4G0511C2NV.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260620/OQ7eb2Eud_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VVUU3T0GJ.html?f=post2020_dy_recommends)

### [沙漠种麦竟成治沙神器！中国方案震惊全球](https://www.163.com/v/video/VVUU3T0GJ.html?f=post2020_dy_recommends)

晨初浮若 2026-06-20 09:09:11

[0\\
_跟贴_ 0](https://www.163.com/v/video/VVUU3T0GJ.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260619/yPA62nNT3_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VMURRGKJ9.html?f=post2020_dy_recommends)

### [顶级特工趁鬼子不注意，将绝密文件藏在他裤腿里](https://www.163.com/v/video/VMURRGKJ9.html?f=post2020_dy_recommends)

飞鸟潜影 2026-06-20 00:00:00

[0\\
_跟贴_ 0](https://www.163.com/v/video/VMURRGKJ9.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260620/LjugIy4Qp_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VGUTB0C4Q.html?f=post2020_dy_recommends)

### [刘亦菲站在那里就是标准潮流模板来的吧](https://www.163.com/v/video/VGUTB0C4Q.html?f=post2020_dy_recommends)

娱蜀黍ss 2026-06-20 01:54:07

[0\\
_跟贴_ 0](https://www.163.com/v/video/VGUTB0C4Q.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260622/ZoGC1kj5b_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VZV2AKACK.html?f=post2020_dy_recommends)

### [黄健翔爆料马宁中长跑项目出身绝对不会在世界杯抽筋翻车！](https://www.163.com/v/video/VZV2AKACK.html?f=post2020_dy_recommends)

咪咕体育 2026-06-22 00:23:44

[4\\
_跟贴_ 4](https://www.163.com/v/video/VZV2AKACK.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0621/7911fc67p00tgysbh000zc0009c0070c.png&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/news/article/KVUR86IC00019B3E.html?f=post2020_dy_recommends)

### [外国知名学者：当今世界只有四个大国](https://www.163.com/news/article/KVUR86IC00019B3E.html?f=post2020_dy_recommends)

参考消息 2026-06-21 12:27:22

[12101\\
_跟贴_ 12101](https://www.163.com/news/article/KVUR86IC00019B3E.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260621/P9rjH6VqG_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VCV0ODADT.html?f=post2020_dy_recommends)

### [交警执勤时全身叮满蚊虫，让人心疼！](https://www.163.com/v/video/VCV0ODADT.html?f=post2020_dy_recommends)

中国日报网 2026-06-21 09:46:06

[97\\
_跟贴_ 97](https://www.163.com/v/video/VCV0ODADT.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260620/gXtOaoARv_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VZUTQRROT.html?f=post2020_dy_recommends)

### [为什么说葡萄牙主帅是个纯舔狗？他从没有真正帮C罗兜底的方案！](https://www.163.com/v/video/VZUTQRROT.html?f=post2020_dy_recommends)

一个香蕉说球 2026-06-20 06:31:16

[75\\
_跟贴_ 75](https://www.163.com/v/video/VZUTQRROT.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little666880dbd8aj00tgyrv9006nd000u0013tm.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVUQOCGI0556DOLV.html?f=post2020_dy_recommends)

### [运城:蒲东小区供暖改造招标存猫腻 惠民工程疑沦为少数人牟利工具](https://www.163.com/dy/article/KVUQOCGI0556DOLV.html?f=post2020_dy_recommends)

事实真相 2026-06-21 12:17:42

[0\\
_跟贴_ 0](https://www.163.com/dy/article/KVUQOCGI0556DOLV.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260619/oigQdhKVL_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VYUR5IOLK.html?f=post2020_dy_recommends)

### [养老金调整方案将分档实施，低养老金群体涨幅较高](https://www.163.com/v/video/VYUR5IOLK.html?f=post2020_dy_recommends)

夏至陌离殇 2026-06-19 05:40:49

[0\\
_跟贴_ 0](https://www.163.com/v/video/VYUR5IOLK.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260620/vzMpiCbId_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VTUTEMA1J.html?f=post2020_dy_recommends)

### [1经理抢下属方案领3万奖金，被揭穿后老板做法太解气！](https://www.163.com/v/video/VTUTEMA1J.html?f=post2020_dy_recommends)

竖笛小魔王 2026-06-20 02:58:31

[0\\
_跟贴_ 0](https://www.163.com/v/video/VTUTEMA1J.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0621/781545cap00tgz2hh002uc000j600b9c.png&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVV3SINQ053469LG.html?f=post2020_dy_recommends)

### [大学生实习日薪180元 弄丢客户6.5万元劳力士表](https://www.163.com/dy/article/KVV3SINQ053469LG.html?f=post2020_dy_recommends)

极目新闻 2026-06-21 14:57:13

[3974\\
_跟贴_ 3974](https://www.163.com/dy/article/KVV3SINQ053469LG.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2023/0918/4b309a23j00s1677800xcd000uk00h6p.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVUF0H0N0552C5PL.html?f=post2020_dy_recommends)

### [启动施工图审核招标、工期3.5年，长三角这条高铁有望年底开工！](https://www.163.com/dy/article/KVUF0H0N0552C5PL.html?f=post2020_dy_recommends)

交建动态 2026-06-21 12:05:12

[0\\
_跟贴_ 0](https://www.163.com/dy/article/KVUF0H0N0552C5PL.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260620/Oebt1qMuh_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VUUTD76TM.html?f=post2020_dy_recommends)

### [6月16日浙江台州烤鱼店老板儿子被熟客扇巴掌，警方提议赔偿玩具，妈妈不接受调解方案](https://www.163.com/v/video/VUUTD76TM.html?f=post2020_dy_recommends)

南昌晚报 2026-06-20 02:32:48

[1\\
_跟贴_ 1](https://www.163.com/v/video/VUUTD76TM.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260618/tYb6uCIB3_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VXUPHL7V6.html?f=post2020_dy_recommends)

### [疯狂抢建等拆迁，高速一穿隧道，全成泡影](https://www.163.com/v/video/VXUPHL7V6.html?f=post2020_dy_recommends)

皮皮流鼻涕 2026-06-18 14:33:24

[24\\
_跟贴_ 24](https://www.163.com/v/video/VXUPHL7V6.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260621/uydN6mTio_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VHV0A9R8G.html?f=post2020_dy_recommends)

### [国米盯上边后卫帕莱斯特拉，转会费浮动条款谈崩？](https://www.163.com/v/video/VHV0A9R8G.html?f=post2020_dy_recommends)

输在感情刀 2026-06-21 05:39:32

[1\\
_跟贴_ 1](https://www.163.com/v/video/VHV0A9R8G.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little9110fcce1a1j00tgzbnc000ud000hs00aym.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVJ2H140514BE2Q.html?f=post2020_dy_recommends)

### [媒体：两大核武国家“水仗”升级 巴基斯坦陷入恐慌](https://www.163.com/dy/article/KVVJ2H140514BE2Q.html?f=post2020_dy_recommends)

中国新闻周刊 2026-06-21 19:23:56

[1965\\
_跟贴_ 1965](https://www.163.com/dy/article/KVVJ2H140514BE2Q.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260620/eWgSCp9q4_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VYUTI551B.html?f=post2020_dy_recommends)

### [养老金调整与补发政策解析](https://www.163.com/v/video/VYUTI551B.html?f=post2020_dy_recommends)

夏至陌离殇 2026-06-20 03:59:03

[0\\
_跟贴_ 0](https://www.163.com/v/video/VYUTI551B.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/e8c611ddj00tgzhhs0021d000da007zm.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVQ9G6T051100B9.html?f=post2020_dy_recommends)

### [WPS背刺用户？C盘爆满、基础功能收费，官方紧急回应](https://www.163.com/dy/article/KVVQ9G6T051100B9.html?f=post2020_dy_recommends)

雷科技 2026-06-21 21:32:04

[6\\
_跟贴_ 6](https://www.163.com/dy/article/KVVQ9G6T051100B9.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/three5848bc7262bj00tgzfrk00jxd000sg00jyp.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVO7JV90556B2P4.html?f=post2020_dy_recommends)

### [幸亏中国没中标！泰国高铁曾选日本人建设，建成后让泰国欲哭无泪](https://www.163.com/dy/article/KVVO7JV90556B2P4.html?f=post2020_dy_recommends)

奥字侃剧 2026-06-21 20:52:55

[12\\
_跟贴_ 12](https://www.163.com/dy/article/KVVO7JV90556B2P4.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/7e4bb1a0j00tgzh1t00zkd000u000grm.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVPQQL405119734.html?f=post2020_dy_recommends)

### [OpenRouter推出复合方案，用一半价格实现性能碾压](https://www.163.com/dy/article/KVVPQQL405119734.html?f=post2020_dy_recommends)

DeepTech深科技 2026-06-21 21:20:46

[3\\
_跟贴_ 3](https://www.163.com/dy/article/KVVPQQL405119734.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260621/YPXylro6J_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VXV0RVVUV.html?f=post2020_dy_recommends)

### [旧社会女性处境太窒息：她们不是弱，是被规则勒死](https://www.163.com/v/video/VXV0RVVUV.html?f=post2020_dy_recommends)

小六一影视 2026-06-21 10:48:43

[1\\
_跟贴_ 1](https://www.163.com/v/video/VXV0RVVUV.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little993088f1ad5j00tgu3210121d000tc00iec.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVOA1C6605568W0A.html?f=post2020_dy_recommends)

### [振铃波抗扰度测试EMC设备，振波玲模拟器/耦合/去耦网络：从标准到产品的厂商/品牌全面解读](https://www.163.com/dy/article/KVOA1C6605568W0A.html?f=post2020_dy_recommends)

新浪财经 2026-06-18 23:30:02

[0\\
_跟贴_ 0](https://www.163.com/dy/article/KVOA1C6605568W0A.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260619/1vAaEbDoJ_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VYUR5RJ6T.html?f=post2020_dy_recommends)

### [养老金调整方案即将公布，低收入、工龄长、高龄老人将更受益](https://www.163.com/v/video/VYUR5RJ6T.html?f=post2020_dy_recommends)

夏至陌离殇 2026-06-19 05:45:39

[0\\
_跟贴_ 0](https://www.163.com/v/video/VYUR5RJ6T.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260620/G8leTxjLI_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VWUTAGNIU.html?f=post2020_dy_recommends)

### [新能源汽车下乡政策揭秘，真的有优惠吗？](https://www.163.com/v/video/VWUTAGNIU.html?f=post2020_dy_recommends)

我是六耳猕猴 2026-06-20 01:45:34

[0\\
_跟贴_ 0](https://www.163.com/v/video/VWUTAGNIU.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0621/15c02785p00tgylsl0049c0009c0070c.png&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/news/article/KVUIODNB000189PS.html?f=post2020_dy_recommends)

### [库拉索门将多次扑救 厄瓜多尔0-0战平库拉索](https://www.163.com/news/article/KVUIODNB000189PS.html?f=post2020_dy_recommends)

央视新闻 2026-06-21 09:58:57

[2534\\
_跟贴_ 2534](https://www.163.com/news/article/KVUIODNB000189PS.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/06/19/cLz9mrLB6enphC3VkfLGwLT5Jsfh3mXG0mo4k61gn.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVV00QR005497CHS.html?f=post2020_dy_recommends)

### [2026年反腐重点，没有烟草、消防、医药、工程建设了，有三个变化](https://www.163.com/dy/article/KVV00QR005497CHS.html?f=post2020_dy_recommends)

职场资深秘书 2026-06-21 13:49:51

[14\\
_跟贴_ 14](https://www.163.com/dy/article/KVV00QR005497CHS.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260620/qKHs7I4Ng_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VZUTNTNND.html?f=post2020_dy_recommends)

### [福建舰打破西方海权规则西太平洋格局加速重构](https://www.163.com/v/video/VZUTNTNND.html?f=post2020_dy_recommends)

精彩一网打尽 2026-06-20 05:39:52

[0\\
_跟贴_ 0](https://www.163.com/v/video/VZUTNTNND.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260621/IyLGl9bEx_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VTV1VNGQI.html?f=post2020_dy_recommends)

### [村委会大变样，百姓福祉升级](https://www.163.com/v/video/VTV1VNGQI.html?f=post2020_dy_recommends)

明媚如初k 2026-06-21 21:13:15

[0\\
_跟贴_ 0](https://www.163.com/v/video/VTV1VNGQI.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260620/YSJKEIr2y_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VPUUUFK0B.html?f=post2020_dy_recommends)

### [甲方表示交付了就结全款，谁敢接？](https://www.163.com/v/video/VPUUUFK0B.html?f=post2020_dy_recommends)

给你大肥鱼 2026-06-20 16:53:44

[1\\
_跟贴_ 1](https://www.163.com/v/video/VPUUUFK0B.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little9167ded775cj00tgz78b0019d000u000jvg.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVDUGMT051492T3.html?f=post2020_dy_recommends)

### [就在明天，深市史上最大规模IPO开启申购，顶格申购需配深市市值632万元](https://www.163.com/dy/article/KVVDUGMT051492T3.html?f=post2020_dy_recommends)

红星新闻 2026-06-21 17:53:02

[274\\
_跟贴_ 274](https://www.163.com/dy/article/KVVDUGMT051492T3.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260612/gMceqKtwp_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VVU9IQ40G.html?f=post2020_dy_recommends)

### [刑事案件的审判监督](https://www.163.com/v/video/VVU9IQ40G.html?f=post2020_dy_recommends)

刑事律师赖建平 2026-06-21 05:00:00

[0\\
_跟贴_ 0](https://www.163.com/v/video/VVU9IQ40G.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260621/Sp3PW1Arl_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VXV06HOOG.html?f=post2020_dy_recommends)

### [休人员返聘新规来了！2026年7月起超龄用工四大权益强制保障](https://www.163.com/v/video/VXV06HOOG.html?f=post2020_dy_recommends)

两面包夹芋头 2026-06-21 04:33:57

[0\\
_跟贴_ 0](https://www.163.com/v/video/VXV06HOOG.html?f=post2020_dy_recommends)

[![不要再为贺红梅感到惋惜了，55岁升任高官的她，早已走上另一路](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/big701ead70afdj00tgym8l001od000zk00i2p.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVUJNL8M0556C0UB.html?f=post1603_tab_news "不要再为贺红梅感到惋惜了，55岁升任高官的她，早已走上另一路")

### [不要再为贺红梅感到惋惜了，55岁升任高官的她，早已走上另一路](https://www.163.com/dy/article/KVUJNL8M0556C0UB.html?f=post1603_tab_news "不要再为贺红梅感到惋惜了，55岁升任高官的她，早已走上另一路")

落雪听梅a

2026-06-21 10:14:57

[![江苏多地机关将“处长”调整为“科长”，是什么原因？属于降级吗](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/09e7914ej00tgyszt002id000hs00h8g.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVUS2N6B05566S5I.html?f=post1603_tab_news "江苏多地机关将“处长”调整为“科长”，是什么原因？属于降级吗")

### [江苏多地机关将“处长”调整为“科长”，是什么原因？属于降级吗](https://www.163.com/dy/article/KVUS2N6B05566S5I.html?f=post1603_tab_news "江苏多地机关将“处长”调整为“科长”，是什么原因？属于降级吗")

手工制作阿爱

2026-06-21 12:40:46

[![帕公主隐秘男友再度守灵！帕里塔特少将满脸悲伤，迟迟走不出丧痛](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/big4387afb684ej00tgyxfs003od000yk00p1p.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVV1ISDG0556D0RP.html?f=post1603_tab_news "帕公主隐秘男友再度守灵！帕里塔特少将满脸悲伤，迟迟走不出丧痛")

### [帕公主隐秘男友再度守灵！帕里塔特少将满脸悲伤，迟迟走不出丧痛](https://www.163.com/dy/article/KVV1ISDG0556D0RP.html?f=post1603_tab_news "帕公主隐秘男友再度守灵！帕里塔特少将满脸悲伤，迟迟走不出丧痛")

笑一个吧

2026-06-21 14:17:00

[![穆里尼奥出手！当年被全英超骂成水货的球员，皇马 6000 万抢着要](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0615/90d8091dj00tgn45900erd000v900nfp.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVEJLDFQ0556GNP0.html?f=post1603_tab_news "穆里尼奥出手！当年被全英超骂成水货的球员，皇马 6000 万抢着要")

### [穆里尼奥出手！当年被全英超骂成水货的球员，皇马 6000 万抢着要](https://www.163.com/dy/article/KVEJLDFQ0556GNP0.html?f=post1603_tab_news "穆里尼奥出手！当年被全英超骂成水货的球员，皇马 6000 万抢着要")

澜归序

2026-06-15 05:14:22

[![女人偷情时的“嗯嗯”声代表着什么？](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/big15622afb840j00tgzmyo002xd000xc00m8g.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/L0036KDI0548JFLW.html?f=post1603_tab_news "女人偷情时的“嗯嗯”声代表着什么？")

### [女人偷情时的“嗯嗯”声代表着什么？](https://www.163.com/dy/article/L0036KDI0548JFLW.html?f=post1603_tab_news "女人偷情时的“嗯嗯”声代表着什么？")

思絮

2026-06-22 00:04:28

[![中央再发铁令！领导干部出现这15种情形 , 将不能再担任现职！](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/06/19/mnbVMw99gzz3k69TlNvm05HuDg49qs0K0mo5075vr.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVSHRM200556AA6V.html?f=post1603_tab_news "中央再发铁令！领导干部出现这15种情形 , 将不能再担任现职！")

### [中央再发铁令！领导干部出现这15种情形 , 将不能再担任现职！](https://www.163.com/dy/article/KVSHRM200556AA6V.html?f=post1603_tab_news "中央再发铁令！领导干部出现这15种情形 , 将不能再担任现职！")

细说职场

2026-06-20 15:03:51

[![二十余年遗憾终圆满！陈伟霆首个父亲节，一双定制亲子鞋戳哭全网](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/b3763cd0j00tgz2gq000nd000j400ecp.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVV7MQDL0556LV9S.html?f=post1603_tab_news "二十余年遗憾终圆满！陈伟霆首个父亲节，一双定制亲子鞋戳哭全网")

### [二十余年遗憾终圆满！陈伟霆首个父亲节，一双定制亲子鞋戳哭全网](https://www.163.com/dy/article/KVV7MQDL0556LV9S.html?f=post1603_tab_news "二十余年遗憾终圆满！陈伟霆首个父亲节，一双定制亲子鞋戳哭全网")

繁华羽淡洛

2026-06-21 16:05:36

[![英国又为乌克兰研发出一款大杀器](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/06/21/7f6AkpKTVW5mRLuJGTLsMmg5Ntx6FalD0mob1qk8t.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/L000G12M0552D6K3.html?f=post1603_tab_news "英国又为乌克兰研发出一款大杀器")

### [英国又为乌克兰研发出一款大杀器](https://www.163.com/dy/article/L000G12M0552D6K3.html?f=post1603_tab_news "英国又为乌克兰研发出一款大杀器")

史政先锋

2026-06-21 23:18:32

[![今夏已完成8笔重磅转会！皇马独揽4笔，热刺也签下了两员大将！](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/06/20/eQ0Tgq4HifXwoL05VtmXIp6ADN307bz60mo866p5c.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVT4SMBD0537B2DW.html?f=post1603_tab_news "今夏已完成8笔重磅转会！皇马独揽4笔，热刺也签下了两员大将！")

### [今夏已完成8笔重磅转会！皇马独揽4笔，热刺也签下了两员大将！](https://www.163.com/dy/article/KVT4SMBD0537B2DW.html?f=post1603_tab_news "今夏已完成8笔重磅转会！皇马独揽4笔，热刺也签下了两员大将！")

田先生篮球

2026-06-20 20:36:40

[![土耳其为啥世界杯改名Türkiye？两个原因一个比一个尴尬](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/big82596425eacj00tgws0n0032d001hc00p8p.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVS1STK50556C67B.html?f=post1603_tab_news "土耳其为啥世界杯改名Türkiye？两个原因一个比一个尴尬")

### [土耳其为啥世界杯改名Türkiye？两个原因一个比一个尴尬](https://www.163.com/dy/article/KVS1STK50556C67B.html?f=post1603_tab_news "土耳其为啥世界杯改名Türkiye？两个原因一个比一个尴尬")

李絙在北漂

2026-06-20 10:24:46

[![笑死人！客服笑了两个小时才舍得发出，评论区已沦陷](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0620/13c38efdj00tgxq24001md000j100rem.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVTBV3OA0556E96Z.html?f=post1603_tab_news "笑死人！客服笑了两个小时才舍得发出，评论区已沦陷")

### [笑死人！客服笑了两个小时才舍得发出，评论区已沦陷](https://www.163.com/dy/article/KVTBV3OA0556E96Z.html?f=post1603_tab_news "笑死人！客服笑了两个小时才舍得发出，评论区已沦陷")

另子维爱读史

2026-06-20 22:40:00

[![宝马全新一代 X5 曝光：换脸换芯，2026年还要让你掏钱包？](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/big18165bc49c2j00tgv99k000pd000hs00a0g.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVPU70PM055616X1.html?f=post1603_tab_news "宝马全新一代 X5 曝光：换脸换芯，2026年还要让你掏钱包？")

### [宝马全新一代 X5 曝光：换脸换芯，2026年还要让你掏钱包？](https://www.163.com/dy/article/KVPU70PM055616X1.html?f=post1603_tab_news "宝马全新一代 X5 曝光：换脸换芯，2026年还要让你掏钱包？")

音乐时光的娱乐

2026-06-19 14:41:52

[![浙江民富实力十强县！慈溪仅排第六，温州入围两城](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/d84648f2j00tgz0990046d000zk00klm.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVV5201V05448ZCM.html?f=post1603_tab_news "浙江民富实力十强县！慈溪仅排第六，温州入围两城")

### [浙江民富实力十强县！慈溪仅排第六，温州入围两城](https://www.163.com/dy/article/KVV5201V05448ZCM.html?f=post1603_tab_news "浙江民富实力十强县！慈溪仅排第六，温州入围两城")

城市生态圈

2026-06-21 15:47:55

[![先2-2，再4-0！淘汰赛还要赢巴西，世界杯日本喊出夺冠？醒醒吧](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0622/c63ef4bbj00tgzpvz001kd000ys00jjm.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/L004NND505566C07.html?f=post1603_tab_news "先2-2，再4-0！淘汰赛还要赢巴西，世界杯日本喊出夺冠？醒醒吧")

### [先2-2，再4-0！淘汰赛还要赢巴西，世界杯日本喊出夺冠？醒醒吧](https://www.163.com/dy/article/L004NND505566C07.html?f=post1603_tab_news "先2-2，再4-0！淘汰赛还要赢巴西，世界杯日本喊出夺冠？醒醒吧")

以茶带书

2026-06-22 00:31:22

[![林生斌现状：定居澳洲富人区，如今儿女双全，妻子是之前公司员工](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0619/27e5cedcj00tgvghq002od000v900fmp.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVQ74P4F0556E0G2.html?f=post1603_tab_news "林生斌现状：定居澳洲富人区，如今儿女双全，妻子是之前公司员工")

### [林生斌现状：定居澳洲富人区，如今儿女双全，妻子是之前公司员工](https://www.163.com/dy/article/KVQ74P4F0556E0G2.html?f=post1603_tab_news "林生斌现状：定居澳洲富人区，如今儿女双全，妻子是之前公司员工")

离离言几许

2026-06-19 17:17:57

[![你知道吗？这些公安部门以前全是独立的！](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/big183c4763797j00tgyswc0019d000hs00a0g.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVURURKK055616X1.html?f=post1603_tab_news "你知道吗？这些公安部门以前全是独立的！")

### [你知道吗？这些公安部门以前全是独立的！](https://www.163.com/dy/article/KVURURKK055616X1.html?f=post1603_tab_news "你知道吗？这些公安部门以前全是独立的！")

音乐时光的娱乐

2026-06-21 12:38:39

[![太难了！知名车厂再宣布裁员5万](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little8224fccc04dj00tgyzwt00opd000u000mic.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVV4K55L05568W0A.html?f=post1603_tab_news "太难了！知名车厂再宣布裁员5万")

### [太难了！知名车厂再宣布裁员5万](https://www.163.com/dy/article/KVV4K55L05568W0A.html?f=post1603_tab_news "太难了！知名车厂再宣布裁员5万")

新浪财经

2026-06-21 15:10:07

[![“初中女生坏起来比男孩更可怕”，班主任曝内情：三观都被刷新了](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little670f1ad2c8ej00tgtt7l001ed000q400q2m.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVNTB17M0556B8V8.html?f=post1603_tab_news "“初中女生坏起来比男孩更可怕”，班主任曝内情：三观都被刷新了")

### [“初中女生坏起来比男孩更可怕”，班主任曝内情：三观都被刷新了](https://www.163.com/dy/article/KVNTB17M0556B8V8.html?f=post1603_tab_news "“初中女生坏起来比男孩更可怕”，班主任曝内情：三观都被刷新了")

泽泽先生

2026-06-18 19:58:44

[![“山东最大酒商”爆雷？只是个倒爷](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/d0006e62j00tgyiky0031d000rm01d6m.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVUF7M270552CEZG.html?f=post1603_tab_news "“山东最大酒商”爆雷？只是个倒爷")

### [“山东最大酒商”爆雷？只是个倒爷](https://www.163.com/dy/article/KVUF7M270552CEZG.html?f=post1603_tab_news "“山东最大酒商”爆雷？只是个倒爷")

茅小福

2026-06-21 08:58:11

[![离婚 无孩 五年空窗，43岁尼格买提终于摊牌了 我心里那个人：是我妈](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/big4919cf905cdj00tgswkh000xd000hs00e4g.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVMLH5890553TET5.html?f=post1603_tab_news "离婚 无孩 五年空窗，43岁尼格买提终于摊牌了 我心里那个人：是我妈")

### [离婚 无孩 五年空窗，43岁尼格买提终于摊牌了 我心里那个人：是我妈](https://www.163.com/dy/article/KVMLH5890553TET5.html?f=post1603_tab_news "离婚 无孩 五年空窗，43岁尼格买提终于摊牌了 我心里那个人：是我妈")

TVB的四小花

2026-06-18 08:12:23

2026-06-22 01:51:00

[![别摸鲨鱼的脚](https://nimg.ws.126.net/?url=https://mobilepics.ws.126.net/2026_02_25_17_55_22oRHTf0mevp8rva.png&thumbnail=160y160&quality=80&type=jpg)](https://www.163.com/dy/media/T1772013324233.html)

[别摸鲨鱼的脚](https://www.163.com/dy/media/T1772013324233.html)

[标书届来了一个莎士比亚](https://www.163.com/dy/media/T1772013324233.html)

[_138_](https://www.163.com/dy/media/T1772013324233.html) 文章数[_0_](https://www.163.com/dy/media/T1772013324233.html) 关注度

往期回顾 [全部](https://www.163.com/dy/media/T1772013324233.html)

## [科技要闻](https://tech.163.com/)

[![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0621/ba916e09j00tgyn2q000zc000s600e3c.jpg&thumbnail=300x150&quality=90&type=jpg)**马斯克拿下7800亿元天价薪酬 2028年可兑现**](https://www.163.com/dy/article/KVUB2U730534A4SC.html)

- ### [韩国央行忧心忡忡：芯片厂狂发奖金 通胀怎么办？](https://www.163.com/dy/article/KVU00QRB05198CJN.html)

- ### [DeepSeek上线识图模式，看谁都像梁文锋](https://www.163.com/dy/article/KVS0AEUQ051481US.html)

- ### [对中国出口EUV光刻机？阿斯麦立即否认美国质疑](https://www.163.com/dy/article/KVRTB6PG051481US.html)

- ### [智谱回应马斯克：到Fable水平用不了那么久](https://www.163.com/dy/article/KVRQLML80514R9P4.html)

## [头条要闻](https://news.163.com/?f=post2020_dy_news_bj)

[![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little9110fcce1a1j00tgzbnc000ud000hs00aym.jpg&thumbnail=300x150&quality=90&type=jpg)**媒体：两大核武国家“水仗”升级 巴基斯坦陷入恐慌**](https://www.163.com/dy/article/KVVJ2H140514BE2Q.html)

- ### [伊朗代表团拒绝与美方握手合影](https://www.163.com/news/article/KVVQRVDR0001899O.html)

- ### [知名作家"南派三叔"向媒体求助：思虑再三联系了你们](https://www.163.com/news/article/KVVNUFG50001899O.html)

- ### [两年前"震惊世界"的洲际弹道导弹发射 细节披露](https://www.163.com/news/article/KVVLB7A30001899O.html)

- ### [高市早苗再现外交"名场面" 引发大量日本网民吐槽](https://www.163.com/news/article/KVVEH92K0001899O.html)

## [头条要闻](https://news.163.com/?f=post2020_dy_news)

[![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little9110fcce1a1j00tgzbnc000ud000hs00aym.jpg&thumbnail=300x150&quality=90&type=jpg)**媒体：两大核武国家“水仗”升级 巴基斯坦陷入恐慌**](https://www.163.com/dy/article/KVVJ2H140514BE2Q.html)

- ### [伊朗代表团拒绝与美方握手合影](https://www.163.com/news/article/KVVQRVDR0001899O.html)

- ### [知名作家"南派三叔"向媒体求助：思虑再三联系了你们](https://www.163.com/news/article/KVVNUFG50001899O.html)

- ### [两年前"震惊世界"的洲际弹道导弹发射 细节披露](https://www.163.com/news/article/KVVLB7A30001899O.html)

- ### [高市早苗再现外交"名场面" 引发大量日本网民吐槽](https://www.163.com/news/article/KVVEH92K0001899O.html)

## [体育要闻](https://sports.163.com/)

[![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0621/e06327ebp00tgz8ur00c1c000s600e3c.png&thumbnail=300x150&quality=90&type=jpg)**德国的超级替补，10年前还在工厂上班**](https://www.163.com/sports/article/KVUD346G00059A7T.html)

- ### [18岁斩世界杯首球！西班牙2亿天才连创5大纪录 超越梅西+比肩贝利](https://www.163.com/dy/article/L005S7QV0529CA1F.html)

- ### [世界杯第1000场-日本4-0送突尼斯出局 上田绮世2射1传](https://www.163.com/sports/article/KVV0D49B00058781.html)

- ### [FIFA世界排名：荷兰德国库拉索小幅上升，厄瓜多尔下降7名](https://www.163.com/dy/article/KVVJ1RSJ0549BAP0.html)

- ### [热身赛：中国男篮力克澳大利亚 王俊杰23+6+4赵继伟一度受伤](https://www.163.com/dy/article/KVVPQ5IJ0529RKNN.html)

## [娱乐要闻](https://ent.163.com/)

[![](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/66806108j00tgz7wd003id000zi00nsp.jpg&thumbnail=300x150&quality=90&type=jpg)**原来她就是张颂文老婆**](https://www.163.com/dy/article/KVVEG8400556D0RP.html)

- ### [《开始推理吧4》真的越看越上头](https://www.163.com/dy/article/KVO044R90556AWQW.html)

- ### [上海电视节开幕在即，国际影视市场启动](https://www.163.com/dy/article/KVVEDDJ905506BEH.html)

- ### [《莫离》全剧最大的恋爱脑不是笨女人叶莹](https://www.163.com/dy/article/KVVE86QM05563WV3.html)

- ### [《歌手》五期：胡彦斌破音却封神！](https://www.163.com/dy/article/KVVE2TQ60556CICS.html)

## [财经要闻](https://money.163.com/)

[![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0621/0e8c142ap00tgzj4a009hc000s600e3c.png&thumbnail=300x150&quality=90&type=jpg)**“床垫界的特斯拉”破产了**](https://www.163.com/dy/article/KVV9K5TG05199LET.html)

- ### [纸尿裤“罗生门”：真相越辩越远？](https://www.163.com/dy/article/KVVOHCER0519BQPG.html)

- ### [深夜滴滴，特斯拉北京小伙把我丢在了立交桥下](https://www.163.com/dy/article/KVUO34MA0519B5UO.html)

- ### [减肥针网售“限令”刺痛了谁？](https://www.163.com/dy/article/KVTRJAKN051188EA.html)

- ### [龙江银行压舱石越来越小，谁能压住四大风险？丨正经深度](https://www.163.com/dy/article/L001C4GG0519B5UO.html)

## [汽车要闻](https://auto.163.com/)

[![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0618/0e6dc9e8j00tgtjix02ksc000s600e3c.jpg&thumbnail=300x150&quality=90&type=jpg)**惊出冷汗！重庆实测奥迪A5L，华为智驾这波操作绝了…**](https://www.163.com/v/video/VKUPO7QQC.html)

- ### [有点小酷 吉利熊猫勇士轻越野纯电小车来了](https://www.163.com/v/video/VKUPQM443.html)

- ### [舒适智能可城可野 郑州赛车场硬核易体验方程豹](https://www.163.com/v/video/VKUPJ2MRV.html)

- ### [强化运动属性/1.6T版本动力升级 艾瑞泽8征服版限时售10.29万起](https://www.163.com/auto/article/KVMV86Q30008856R.html)

- ### [新款玛莎拉蒂GT跑车/GC敞篷跑车与格雷嘉SUV首发](https://www.163.com/auto/article/KVO3LUH70008856R.html)

## 态度原创

- ### [_药说漫画_ \| 干细胞能延缓衰老吗？答案藏在一生里](https://www.163.com/jiankang/article/KQDJE4M700388045.html)

- ### [_界外编辑部_ \| 世界排名700位的选手，打出了中国网球2026年的第一份惊喜](https://www.163.com/sports/article/KVF5GFSH00059B4P.html)

- ### [_上流_ \| 世界杯黑马佛得角：河北人开超市，温州人当老板](https://www.163.com/dy/article/KVKS4UPF0521DCLG.html)

- ### [_清流_ \| 广州通则康威IPO:产品海外市场空间或有隐忧，关联方信披语焉不详\|清流IPO](https://www.163.com/money/article/KQ0GK3VI00258105.html)

[亲子](https://baby.163.com/)

[时尚](https://fashion.163.com/)

[艺术](https://art.163.com/)

[手机](https://mobile.163.com/)

[军事航空](https://war.163.com/)

## [亲子要闻](https://baby.163.com/)

[![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260621/ClnTkhU3w_cover.jpg&thumbnail=300x150&quality=90&type=jpg)**阿宝表演单杠，考考小姨们帮我数6分钟荡了多少圈？老妈数晕了**](https://www.163.com/v/video/VRV1PU9RP.html)

- ### [用王者荣耀的方式给橙子安利世界杯](https://www.163.com/v/video/VNV1JQ5GP.html)

- ### [乐高城市系列之甜甜圈贩卖车 \#大型挖掘机挖土视频](https://www.163.com/v/video/VZUKLESHU.html)

- ### [宝蓝和爸爸叔叔玩过家家。扮演小商贩，开了一家好玩的冰淇淋店](https://www.163.com/v/video/VLV0RM88P.html)

- ### [家长一定要注意！儿科主任真心建议夏天不要给孩子吃冰的](https://www.163.com/v/video/VJV1GJA8J.html)

[![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little80699187ef1j00tgyiuj0039d000xc00irg.jpg&thumbnail=300x150&quality=90&type=jpg)**邮报盘点哈兰德奢侈品收藏：33万镑爱马仕包、28万豪华腕表**](https://www.163.com/dy/article/KVUGDR1H0549BAP0.html)

- ### [夏天衣服没必要买太贵，准备几件白色T恤，舒适清爽又减龄](https://www.163.com/dy/article/KVNJ4BMP05389724.html)

- ### [人过五十，夏天试试“这样穿”：简约又大气](https://www.163.com/dy/article/KVUC0LSB05455CGK.html)

- ### [最敢花钱的人，也带不动这个品牌了？](https://www.163.com/dy/article/KVT9D2SL0514BE2Q.html)

## [艺术要闻](https://art.163.com/)

[![](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/7b03180bj00tgzoew000gd000hs00cpm.jpg&thumbnail=300x150&quality=90&type=jpg)**310米！欧盟第一高楼，坐落于波兰**](https://www.163.com/dy/article/L002TLJP0514ETGI.html)

- ### [沃尔顿家族出资！美国一座新型大学吸引各界目光](https://www.163.com/dy/article/L000JQ9U0514ETGI.html)

- ### [丝绸滑落肩头的瞬间、光影穿过窗棂的温度：他用画笔定格时间本身](https://www.163.com/dy/article/KVVO4A9B0514F1DO.html)

- ### [当印象派遇见维米尔：他用画笔捕捉了美国镀金时代最温柔的侧影](https://www.163.com/dy/article/KVVNPFET0514F1DO.html)

## [手机要闻](https://mobile.163.com/)

[![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little1319b3d03b1j00tgzge5000vd000qy00mig.jpg&thumbnail=300x150&quality=90&type=jpg)**消息称供应链公司已向苹果首款折叠屏iPhone小批量供货**](https://www.163.com/dy/article/KVVQ8C4D0511B8LM.html)

- ### [荣耀X80 Pro Max现身中国电信终端产品库，至高12GB+512GB规格](https://www.163.com/dy/article/KVVNPICA0511B8LM.html)

- ### [高通SM8975应用处理器被曝可选高/低2种移动连接系统配置](https://www.163.com/dy/article/KVVNPIEV0511B8LM.html)

- ### [曝小米18延续背屏设计，引入iOS光感UI，计划9月发布](https://www.163.com/dy/article/KVVMVD4G05118A8G.html)

## [军事要闻](https://war.163.com/)

[![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0621/5e7c3d1fp00tgyw1a000zc000s600e3c.png&thumbnail=300x150&quality=90&type=jpg)**时隔44年试射洲际导弹 现场照片传递三个重磅信息**](https://www.163.com/news/article/KVUNSIOL000189PS.html)

- ### [美伊谈判代表均已抵达瑞士](https://www.163.com/dy/article/KVURG8RJ05346RC6.html)

- ### [又一名半岛电视台记者身亡 以军:他是哈马斯的人](https://www.163.com/dy/article/KVURFDSD0514EGPO.html)

- ### [看现场！直击陆军某旅反坦克导弹分队训练](https://www.163.com/dy/article/KVUR3OAN0514R9OJ.html)

[![](https://static.ws.126.net/f2e/www/index2014/images/sprite_dw2.png)](http://www.163.com/newsapp/#f=qr)

© 1997-2026 网易公司版权所有 [About NetEase](https://corp.163.com/) \|
[公司简介](https://corp.163.com/gb/about/overview.html) \|
[联系方法](https://corp.163.com/gb/contactus.html) \|
[招聘信息](https://corp.163.com/gb/job/job.html) \|
[客户服务](https://help.163.com/) \|
[隐私政策](https://corp.163.com/gb/legal.html) \|
[不良信息举报 Complaint Center](https://www.163.com/special/0077jt/tipoff.html) \|
[廉正举报](https://jubao.163.com/) \|
[侵权投诉 Reporting Infringements](https://corp.163.com/special/008397U0/reporting_infringements_dy.html?35)

### 来源 4: 标书智能体（一）——AI解析招标文件代码+提示词 - 博客园

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

### 来源 5: 标桥首页

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

### 来源 6: 标书软件系统选型推荐_哪家好_价格_免费试用-云巴巴

- URL: https://www.yun88.com/product/biaoshu
- 精读方法：firecrawl-scrape

Access Forbidden

id: 51b1aa431eab44deaec304c85d5f7471

若您是正常访问，请联系管理员partner@yun88.com

[Security Detection Powered BySafeLine WAF](https://waf.chaitin.com/)

### 来源 7: 智能标书助手-艾瑞数智

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

### 来源 8: 招标解析（已下线） - 智谱AI开放文档

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

### 来源 9: AI 评标系统双场景技术实现：标书合规检测与围标串标智能识别_深度优先_jiangnan920-AtomGit开源社区

- URL: https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html
- 精读方法：firecrawl-scrape

[AtomGit开源社区](https://gitcode.csdn.net/)AI 评标系统双场景技术实现：标书合规检测与围标串标智能识别

# AI 评标系统双场景技术实现：标书合规检测与围标串标智能识别

[![](https://profile-avatar.csdnimg.cn/default.jpg!1)](https://devpress.csdn.net/user/jiangnan920)

### [jiangnan920](https://devpress.csdn.net/user/jiangnan920)

[675人浏览 · 2026-05-18 21:25:31](https://devpress.csdn.net/user/jiangnan920)

[![](https://profile-avatar.csdnimg.cn/default.jpg!1)jiangnan920](https://devpress.csdn.net/user/jiangnan920) · 2026-05-18 21:25:31 发布

### 一、前言： [AI](https://link.csdn.net/?target=https%3A%2F%2Fgitcode.com%2FCherryHQ%2Fcherry-studio%3Futm_source%3Ddevpress_gitcode_keyword) 评标系统的双向技术价值

2026 年，全国 92% 的省级公共资源交易平台已完成 AI 评标系统部署，但行业内技术文章普遍存在两个极端：要么只讲投标方如何 "迎合"AI，要么只讲监管方如何 "打击" 违规，很少有文章从 **技术实现者的第一视角** 同时拆解这两个核心场景。

作为安华招标 AI 技术团队，我们既为全国 5 万 + 投标企业提供了 AI 标书合规检测服务，也为 3 个省级公共资源交易中心开发了围标串标智能识别模块。本文将完整分享这两个场景的技术架构、核心算法、工程化落地细节和真实生产环境踩坑记录，所有代码片段均经过生产验证。

* * *

### 二、CSDN 合规声明与文章说明

本文为纯技术分享文章，所有内容均来自我们的实际项目经验。文中提及的安华招标相关技术产品仅作为案例说明，不构成任何商业推荐。如需技术交流，可通过文章末尾作者简介中的方式联系。

本文严格遵守 CSDN 社区规则：

- 无硬广植入，技术内容占比 \> 95%
- 所有代码示例可直接运行
- 数据真实可信，无虚假宣传
- 联系方式仅放置于作者简介区域
- 不使用绝对化用语和夸大表述

* * *

### 三、AI 评标系统整体技术架构（双场景统一架构）

投标方的标书合规检测和评标方的围标串标检测，底层技术架构高度统一，仅在业务层和算法层有差异。我们采用 "数据层 \- 算法层 \- 服务层 \- 应用层" 的四层微服务架构，实现了一套代码支撑两个场景：

plaintext

```undefined
┌─────────────────────────────────────────────────────────┐
│ 应用层：投标端检测系统、评标端监管系统、管理后台        │
├─────────────────────────────────────────────────────────┤
│ 服务层：文档解析服务、合规检测服务、串标识别服务        │
│         知识图谱服务、报告生成服务、系统管理服务        │
├─────────────────────────────────────────────────────────┤
│ 算法层：OCR引擎、NLP语义引擎、向量检索引擎             │
│         图神经网络、异常检测模型、大语言模型接口        │
├─────────────────────────────────────────────────────────┤
│ 数据层：MySQL业务库、MongoDB文件库、Neo4j知识图谱      │
│         Milvus向量库、Redis缓存、Elasticsearch         │
└─────────────────────────────────────────────────────────┘
复制
```

#### 3.1 核心技术选型（2026 年最新生产级选型）

表格

| 技术模块 | 选型 | 版本 | 选型理由 |
| --- | --- | --- | --- |
| OCR 引擎 | PaddleOCR | 2.8.0 | 中文识别准确率 99.5%，表格识别支持嵌套结构，支持 GPU/CPU 部署 |
| NLP 基础模型 | [Qwen](https://link.csdn.net/?target=https%3A%2F%2Fai.gitcode.com%2Fhf_mirrors%2FQwen%2FQwen2.5-7B-Instruct-AWQ)-7B-Chat | 最新 | 中文语义理解能力强，推理速度快，可商用，支持微调 |
| 向量数据库 | Milvus | 2.3.3 | 支持十亿级向量检索，查询延迟 < 10ms，支持分布式部署 |
| 图数据库 | Neo4j | 5.16.0 | 支持复杂图查询，Cypher 语言成熟，企业版支持高可用 |
| Web 框架 | FastAPI | 0.110.0 | 异步性能优异，自动生成 OpenAPI 文档，类型提示完善 |
| 部署方式 | Docker + Kubernetes | 26.0.1 | 环境一致性好，支持自动扩缩容，运维成本低 |

* * *

### ![](https://i-blog.csdnimg.cn/direct/53c0cfa6fd4c4b709bf592c9be132274.png)

### 四、场景一：投标方标书合规检测技术实现

标书合规检测的核心目标是 **在提交前提前发现所有可能导致废标的问题**，包括实质性条款不响应、资质不符合要求、格式错误、算术错误等。

#### 4.1 技术实现流程

plaintext

```mathematica
PDF上传 → 文档解析 → 结构化提取 → 多维度检测 → 风险分级 → 生成报告
复制
```

#### 4.2 核心模块技术细节

##### 4.2.1 高精度文档解析模块

这是整个系统的基础，解析准确率直接决定了后续检测的准确性。我们在 PaddleOCR 基础上做了大量优化：

python

运行

```python
# 优化后的PDF解析核心代码（支持可编辑PDF和扫描件PDF自动切换）
import fitz
from paddleocr import PaddleOCR, PaddleStructure
import json

def pdf_parser(pdf_path, use_ocr_threshold=0.3):
    """
    智能PDF解析器：自动判断是否使用OCR
    :param pdf_path: PDF文件路径
    :param use_ocr_threshold: 可提取文本占比阈值，低于此值使用OCR
    :return: 结构化文档数据
    """
    doc = fitz.open(pdf_path)
    total_chars = 0
    extracted_chars = 0
    pages_data = []

    # 第一遍：尝试提取可编辑文本
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        total_chars += len(text)
        extracted_chars += len(text.strip())

        page_data = {
            "page_num": page_num + 1,
            "text": text,
            "blocks": page.get_text("blocks"),
            "tables": []
        }
        pages_data.append(page_data)

    # 判断是否需要使用OCR
    if total_chars == 0 or extracted_chars / total_chars < use_ocr_threshold:
        print("检测到扫描件PDF，启用OCR解析")
        ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=True)
        structure = PaddleStructure(use_gpu=True)

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))  # 300DPI渲染
            img_bytes = pix.tobytes("png")

            # 文本识别
            ocr_result = ocr.ocr(img_bytes, cls=True)
            # 表格识别
            table_result = structure(img_bytes)

            pages_data[page_num]["text"] = "\n".join([line[1][0] for line in ocr_result[0]])
            pages_data[page_num]["tables"] = table_result[0]

    return json.dumps(pages_data, ensure_ascii=False, indent=2)
复制
```

**生产环境优化点**：

- 自动判断 PDF 类型，可编辑 PDF 直接提取文本，速度提升 10 倍
- 扫描件使用 300DPI 渲染，识别准确率提升 15%
- 表格识别使用 PaddleStructure v2，支持嵌套表格和合并单元格

##### 4.2.2 实质性条款响应检测

这是标书检测中最核心的功能，我们采用 "关键词匹配 \+ 语义相似度 \+ 大语言模型校验" 的三级检测机制：

python

运行

```python
from sentence_transformers import SentenceTransformer
import numpy as np

# 加载语义匹配模型
model = SentenceTransformer('BAAI/bge-large-zh-v1.5')

def check_substantive_response(requirement, response, threshold=0.78):
    """
    三级实质性响应检测
    :param requirement: 招标文件要求
    :param response: 投标文件响应
    :param threshold: 相似度阈值
    :return: 检测结果
    """
    # 第一级：关键词匹配（快速过滤明显不响应）
    keywords = extract_keywords(requirement)
    response_keywords = extract_keywords(response)
    keyword_match_rate = len(set(keywords) & set(response_keywords)) / len(keywords)

    if keyword_match_rate < 0.3:
        return {"result": "不满足", "confidence": 0.95, "reason": "缺少核心关键词"}

    # 第二级：语义相似度匹配
    req_emb = model.encode(requirement, normalize_embeddings=True)
    res_emb = model.encode(response, normalize_embeddings=True)
    similarity = np.dot(req_emb, res_emb)

    if similarity < threshold - 0.1:
        return {"result": "不满足", "confidence": 0.85, "reason": f"语义相似度{similarity:.2f}，低于阈值"}
    elif similarity > threshold + 0.1:
        return {"result": "满足", "confidence": 0.85, "reason": f"语义相似度{similarity:.2f}"}

    # 第三级：大语言模型校验（处理模糊情况）
    llm_result = llm_check_response(requirement, response)
    return llm_result

def llm_check_response(requirement, response):
    """使用大语言模型进行最终校验"""
    prompt = f"""
    请判断以下投标响应是否满足招标文件要求：
    招标文件要求：{requirement}
    投标响应：{response}

    请只返回JSON格式结果，包含以下字段：
    - result: "满足"或"不满足"
    - confidence: 0-1之间的置信度
    - reason: 简要说明理由
    """
    # 调用大语言模型API
    response = qwen_api.call(prompt)
    return json.loads(response)
复制
```

**生产环境效果**：

- 检测准确率：96.3%
- 单条检测时间：<200ms（前两级），<2s（第三级）
- 误报率：<3%

##### 4.2.3 算术错误自动检测

自动检测报价文件中的算术错误，包括分项报价之和与总价不一致、大写小写不一致等：

python

运行

```python
import re
from decimal import Decimal, getcontext

getcontext().prec = 20

def check_arithmetic_errors(price_table):
    """
    检测报价表中的算术错误
    :param price_table: 结构化报价表数据
    :return: 错误列表
    """
    errors = []

    for row in price_table:
        # 检测分项之和与总价不一致
        if "subtotal" in row and "items" in row:
            calculated_subtotal = sum([Decimal(item["price"]) * Decimal(item["quantity"]) for item in row["items"]])
            stated_subtotal = Decimal(row["subtotal"])

            if abs(calculated_subtotal - stated_subtotal) > Decimal("0.01"):
                errors.append({
                    "type": "subtotal_mismatch",
                    "row": row["id"],
                    "calculated": float(calculated_subtotal),
                    "stated": float(stated_subtotal),
                    "difference": float(calculated_subtotal - stated_subtotal)
                })

        # 检测大写小写不一致
        if "amount" in row and "amount_upper" in row:
            lower_amount = Decimal(row["amount"])
            upper_amount = convert_upper_to_decimal(row["amount_upper"])

            if abs(lower_amount - upper_amount) > Decimal("0.01"):
                errors.append({
                    "type": "upper_lower_mismatch",
                    "row": row["id"],
                    "lower": float(lower_amount),
                    "upper": float(upper_amount)
                })

    return errors
复制
```

* * *

### 五、场景二：评标方围标串标智能识别技术实现

围标串标是招投标领域最严重的违规行为之一，传统人工识别方式效率低、漏检率高。AI 技术可以从 **文本相似度、行为特征、关系网络** 三个维度实现精准识别。

#### 5.1 技术实现流程

plaintext

```undefined
批量标书上传 → 文档解析 → 特征提取 → 多维度分析 → 异常评分 → 生成预警报告
复制
```

#### 5.2 核心识别算法与代码实现

##### 5.2.1 文本相似度检测（最常用的串标识别方法）

串标标书通常存在大量雷同内容，我们采用 "局部敏感哈希 \+ 向量检索 \+ 细粒度对比" 的三级检测机制：

python

运行

```python
from datasketch import MinHash, MinHashLSH
import numpy as np

def calculate_document_similarity(doc1, doc2):
    """
    计算两个文档的相似度
    :param doc1: 文档1的文本内容
    :param doc2: 文档2的文本内容
    :return: 相似度得分
    """
    # 第一级：MinHash快速筛选（处理大量文档时）
    minhash1 = MinHash(num_perm=128)
    minhash2 = MinHash(num_perm=128)

    for word in doc1.split():
        minhash1.update(word.encode('utf-8'))
    for word in doc2.split():
        minhash2.update(word.encode('utf-8'))

    jaccard_sim = minhash1.jaccard(minhash2)

    if jaccard_sim < 0.1:
        return 0.0  # 快速排除不相似文档

    # 第二级：向量相似度计算
    emb1 = model.encode(doc1, normalize_embeddings=True)
    emb2 = model.encode(doc2, normalize_embeddings=True)
    cos_sim = np.dot(emb1, emb2)

    if cos_sim < 0.5:
        return cos_sim

    # 第三级：细粒度段落对比
    paragraphs1 = doc1.split('\n\n')
    paragraphs2 = doc2.split('\n\n')

    identical_paragraphs = 0
    for p1 in paragraphs1:
        for p2 in paragraphs2:
            p_sim = np.dot(model.encode(p1, normalize_embeddings=True),
                          model.encode(p2, normalize_embeddings=True))
            if p_sim > 0.95:
                identical_paragraphs += 1
                break

    paragraph_sim = identical_paragraphs / max(len(paragraphs1), len(paragraphs2))

    # 综合得分
    final_score = 0.3 * jaccard_sim + 0.4 * cos_sim + 0.3 * paragraph_sim
    return final_score
复制
```

**生产环境效果**：

- 雷同内容识别准确率：98.7%
- 支持同时对比 1000 + 份标书
- 可定位到具体雷同段落和页码

##### 5.2.2 行为特征异常检测

串标行为通常会留下一些异常的行为特征，我们通过分析这些特征来识别串标：

python

运行

```python
def detect_behavior_anomalies(bid_records):
    """
    检测投标行为异常
    :param bid_records: 投标记录列表
    :return: 异常投标方列表
    """
    anomalies = []

    # 异常1：同一IP地址提交多份标书
    ip_counts = {}
    for record in bid_records:
        ip = record["submit_ip"]
        if ip not in ip_counts:
            ip_counts[ip] = []
        ip_counts[ip].append(record["bidder_name"])

    for ip, bidders in ip_counts.items():
        if len(bidders) > 1:
            anomalies.append({
                "type": "same_ip",
                "ip": ip,
                "bidders": bidders,
                "confidence": 0.9
            })

    # 异常2：标书提交时间过于集中
    submit_times = [record["submit_time"] for record in bid_records]
    submit_times.sort()

    for i in range(len(submit_times) - 2):
        time_diff = submit_times[i+2] - submit_times[i]
        if time_diff.total_seconds() < 300:  # 5分钟内提交3份以上标书
            anomalies.append({
                "type": "concentrated_submission",
                "time_range": f"{submit_times[i]} - {submit_times[i+2]}",
                "bidders": [r["bidder_name"] for r in bid_records if submit_times[i] <= r["submit_time"] <= submit_times[i+2]],
                "confidence": 0.8
            })

    # 异常3：报价呈规律性差异
    prices = [Decimal(record["price"]) for record in bid_records]
    prices.sort()

    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        if diff == Decimal("0"):
            anomalies.append({
                "type": "identical_price",
                "price": float(prices[i]),
                "confidence": 0.95
            })

    return anomalies
复制
```

##### 5.2.3 关系网络分析

通过构建企业关系图谱，识别隐藏的关联关系：

cypher

```pgsql
// 查询存在关联关系的投标企业
MATCH (b1:Bidder)-[r:RELATED_TO]-(b2:Bidder)
WHERE r.type IN ["same_legal_person", "same_address", "same_contact", "shareholder"]
RETURN b1.name, b2.name, r.type, r.confidence
ORDER BY r.confidence DESC

// 查询围标团伙
MATCH path = (b:Bidder)-[*1..3]-(c:Bidder)
WHERE b <> c
WITH b, collect(DISTINCT c) AS connected_bidders, count(DISTINCT c) AS connection_count
WHERE connection_count >= 3
RETURN b.name AS core_bidder, [bidder.name FOR bidder IN connected_bidders] AS gang_members, connection_count
ORDER BY connection_count DESC
复制
```

#### 5.3 综合评分模型

我们将多个维度的检测结果进行融合，得到最终的串标风险评分：

python

运行

```python
def calculate_collusion_risk(similarity_score, behavior_score, relation_score):
    """
    计算综合串标风险评分
    :param similarity_score: 文本相似度得分(0-1)
    :param behavior_score: 行为异常得分(0-1)
    :param relation_score: 关系网络得分(0-1)
    :return: 综合风险评分(0-100)
    """
    weights = {
        "similarity": 0.5,
        "behavior": 0.3,
        "relation": 0.2
    }

    total_score = (
        similarity_score * weights["similarity"] +
        behavior_score * weights["behavior"] +
        relation_score * weights["relation"]
    ) * 100

    risk_level = "低"
    if total_score >= 80:
        risk_level = "高"
    elif total_score >= 50:
        risk_level = "中"

    return {
        "total_score": round(total_score, 2),
        "risk_level": risk_level,
        "details": {
            "similarity_score": round(similarity_score * 100, 2),
            "behavior_score": round(behavior_score * 100, 2),
            "relation_score": round(relation_score * 100, 2)
        }
    }
复制
```

**生产环境效果**：

- 串标识别准确率：92.5%
- 漏检率：<5%
- 误报率：<8%

* * *

### 六、工程化落地关键技术

#### 6.1 高并发处理方案

开标时段系统会面临极高的并发压力，我们采用以下方案保证系统稳定性：

- **异步任务队列**：使用 Celery+Redis 处理耗时的 AI 推理任务
- **自动扩缩容**：基于 Kubernetes 的 HPA 实现服务自动扩缩容
- **多级缓存**：使用 Redis 缓存热点数据和模型推理结果
- **熔断降级**：使用 Sentinel 实现服务熔断和降级，防止雪崩效应

#### 6.2 模型部署优化

AI 模型推理是系统的性能瓶颈，我们采取了以下优化措施：

- **模型量化**：将 FP32 模型量化为 INT8 模型，推理速度提升 3 倍
- **TensorRT 加速**：使用 TensorRT 对 PyTorch 模型进行优化，推理速度再提升 2 倍
- **模型服务化**：使用 Triton Inference Server 部署模型，支持动态批处理
- **GPU 共享**：使用 vGPU 技术实现多个模型共享一块 GPU，提高资源利用率

#### 6.3 数据安全与合规

招投标数据涉及大量商业机密，我们严格遵守《数据安全法》和《个人信息保护法》：

- **传输加密**：所有数据传输使用 TLS 1.3 加密
- **存储加密**：敏感数据使用 AES-256 加密存储
- **访问控制**：基于 RBAC 的细粒度权限控制，最小权限原则
- **操作审计**：记录所有用户的操作日志，保存期限不少于 3 年
- **数据脱敏**：对个人信息和商业机密进行脱敏处理

* * *

### 七、生产环境真实踩坑记录

1. **坑 1：OCR 识别公章区域导致文本混乱**
   - 问题：公章覆盖在文本上时，OCR 会将公章图案识别为乱码
   - 解决方案：训练专门的公章检测模型，识别后将公章区域屏蔽，只识别公章外的文本
2. **坑 2：大文件上传超时**
   - 问题：超过 100MB 的标书文件上传时经常超时
   - 解决方案：实现分片上传和断点续传，支持最大 1GB 文件上传
3. **坑 3：向量检索性能随数据量增长急剧下降**
   - 问题：当向量库中数据超过 1000 万条时，查询延迟超过 1 秒
   - 解决方案：使用 Milvus 的分区功能，按项目和时间分区，查询时只搜索相关分区
4. **坑 4：不同地区的标书格式差异巨大**
   - 问题：全国各省市的标书格式不统一，导致解析准确率不稳定
   - 解决方案：建立格式模板库，支持自定义模板，持续迭代优化解析规则

* * *

### 八、安华招标技术实践分享

基于上述技术架构，我们开发了两套产品：

1. **安华 AI 标书检测系统**：面向投标企业，提供标书合规检测服务，已累计处理 5 万 + 份标书，帮助客户提前排查 2 万 + 个废标风险点
2. **安华 AI 监管平台**：面向公共资源交易中心，提供围标串标智能识别服务，已在 3 个省级平台部署，累计识别 120 + 起串标案件

我们的技术团队将持续投入 AI 技术在招投标领域的应用研究，推动行业数字化转型。

* * *

### 九、未来技术展望

1. **[大模型](https://link.csdn.net/?target=https%3A%2F%2Fai.gitcode.com%2Fhf_mirrors%2FQwen%2FQwen2.5-7B-Instruct-AWQ) 深度应用**：基于大语言模型实现标书自动生成、招标文件自动审核、智能答疑等功能
2. **多模态 AI 评审**：支持图片、图纸、视频等多模态数据的智能分析
3. **区块链技术融合**：利用区块链实现招投标全流程存证，保证数据不可篡改
4. **联邦学习**：在保护数据隐私的前提下，实现跨平台模型训练和数据共享

* * *

### 十、总结

AI 评标系统是一个复杂的系统工程，涉及 OCR、NLP、知识图谱、图神经网络等多个技术领域。本文从投标方和评标方两个核心场景出发，详细介绍了 AI 评标系统的技术架构、核心算法和工程化落地技巧，希望能为从事相关领域开发的工程师提供一些参考。

技术本身没有善恶，关键在于如何使用。我们相信，AI 技术的合理应用，将推动招投标行业更加公平、透明、高效。

* * *

**作者简介**：安华招标技术研发中心，专注于 AI 技术在招投标领域的应用研究，拥有 10 + 年行业经验，主导开发了多个省级 AI 评标系统和安华 AI 标书检测系统。

阅读全文

AI总结

[# 深度优先](https://devpress.csdn.net/tags/629eeed0512a562a42849792) [# rabbitmq](https://devpress.csdn.net/tags/629eeed1512a562a428497b9) [# kafka](https://devpress.csdn.net/tags/629eeed1512a562a428497ba) [# 预编码算法](https://devpress.csdn.net/tags/629eeed0512a562a4284978d)

[![Logo](https://devpress.csdnimg.cn/8bc8dd1a2bc24184a16a142654c4a49e.png)](https://gitcode.csdn.net/)

[AtomGit开源社区](https://gitcode.csdn.net/)

AtomGit 是由开放原子开源基金会联合 CSDN 等生态伙伴共同推出的新一代开源与人工智能协作平台。平台坚持“开放、中立、公益”的理念，把代码托管、模型共享、数据集托管、智能体开发体验和算力服务整合在一起，为开发者提供从开发、训练到部署的一站式体验。

加入社区

更多推荐

- ·
[追寻像素级监督的视觉预训练：Pixio](https://gitcode.csdn.net/6a38080110ee7a33f2807c3c.html)
- ·
[大湾区医疗健康EMBA实测解析与科学选型指南](https://gitcode.csdn.net/6a3696cd662f9a54cb822845.html)
- ·
[Imbalanced Learning](https://gitcode.csdn.net/6a36b58d10ee7a33f2803ca6.html)

[![cover](https://i-blog.csdnimg.cn/direct/ccf4ae9c3f0a41b4bc1ca7b9f19cb4d8.png)\\
\\
追寻像素级监督的视觉预训练：Pixio](https://gitcode.csdn.net/6a38080110ee7a33f2807c3c.html)

[大湾区医疗健康EMBA实测解析与科学选型指南\\
\\
师资团队国际化程度极高，外籍教师占比约50%，100%博士学历，汇聚哈佛、剑桥、斯坦福、哥伦比亚等全球顶级高校学者，覆盖战略管理、资本运作、市场营销、宏观经济、组织变革等全领域，兼具学术深度与企业实战经验。二是数字化转型，助力传统医疗企业落地AI医疗、智能设备研发等科技升级；依托港科大顶尖的AI、数据科学科研实力，精准匹配当下智慧医疗、医疗数字化转型的行业趋势，同时完善的跨境课程与全球游学体系，完](https://gitcode.csdn.net/6a3696cd662f9a54cb822845.html)

[![cover](https://i-blog.csdnimg.cn/direct/be13781c383c4a73be8e9d03b0b0e40a.png)\\
\\
Imbalanced Learning](https://gitcode.csdn.net/6a36b58d10ee7a33f2803ca6.html)

- ![浏览量](https://csdnimg.cn/release/devpress/public/img/watch.a5bd9e9b.svg)675
- ![点赞](https://csdnimg.cn/release/devpress/public/img/thumb.a0b81433.svg)10
- ![收藏](https://csdnimg.cn/release/devpress/public/img/mark.f1a889ab.svg)0
- 0

### 所有评论(0)

您需要登录才能发言

## 温馨提示：您尚未绑定手机号

为遵守国家网络实名制规定，未绑定将限制内容发布与互动

[立即绑定](https://i.csdn.net/#/user-center/account)

![](https://i-operation.csdnimg.cn/images/fb287ddc3c984e04a2021d439632f08c.png)

猜你想问：

在AI评标系统中，如何通过三级检测机制实现投标文件实质性条款的准确响应判断？

![DeepSeek-V3.2](https://i-operation.csdnimg.cn/images/54fe5c4bb0704d65ac32bd7f22b51312.png)DeepSeek-V3.2

毕业设计

作业解答

AI编程

提问

[![](https://profile-avatar.csdnimg.cn/default.jpg!1)](https://devpress.csdn.net/user/jiangnan920)

### [jiangnan920](https://devpress.csdn.net/user/jiangnan920)

[@jiangnan920](https://devpress.csdn.net/user/jiangnan920)

关注

![](https://csdnimg.cn/release/devpress/public/img/devote.fe704c8a.svg)
已为社区贡献3条内容

相关推荐
[查看更多](https://gitcode.com/?utm_source=devpress_gitcode_821)

atomcode

![](https://devpress.csdnimg.cn/079a76d2246c4583bf0c9294ed5e25ec.png)2.1 K

Claude Code 的开源替代方案。连接任意大模型，编辑代码，运行命令，自动验证 — 全自动执行。用 Rust 构建，极致性能。 ｜ An open-source alternative to Claude Code. Connect any LLM, edit code, run commands, and verify changes — autonomously. Built in Rust for speed.

Get Started

cann-learning-hub

![](https://devpress.csdnimg.cn/079a76d2246c4583bf0c9294ed5e25ec.png)402

CANN 学习中心仓，支持在线互动运行、边学边练，提供教程、示例与优化方案，一站式助力昇腾开发者快速上手。

uni-app

![](https://devpress.csdnimg.cn/079a76d2246c4583bf0c9294ed5e25ec.png)65

A cross-platform framework using Vue.js

热门开源项目

[DeepSeek-V3](https://gitcode.com/Hly2700w/DeepSeek-V3-0324?utm_source=devpress_gitcode_keyword&login=from_csdn) [Ultralytics YOLOv8](https://gitcode.com/onetwothreejcq/ultralytics_yolov8?utm_source=devpress_gitcode_keyword&login=from_csdn) [RuoYi 若依](https://gitcode.com/yangzongzhuan/RuoYi/overview?utm_source=devpress_gitcode_keyword&login=from_csdn) [鸿蒙开发工具广场](https://gitcode.com/OpenHarmonyToolkitsPlaza?utm_source=devpress_gitcode_keyword&login=from_csdn) [旋武](https://gitcode.com/xuanwu?utm_source=devpress_gitcode_keyword&login=from_csdn) [OpenHarmony](https://gitcode.com/Cangjie/OpenHarmony?utm_source=devpress_gitcode_keyword&login=from_csdn) [cherry-studio](https://gitcode.com/CherryHQ/cherry-studio?utm_source=devpress_gitcode_keyword&login=from_csdn) [vscode](https://gitcode.com/gh_mirrors/vscode6/vscode?utm_source=devpress_gitcode_keyword&login=from_csdn) [windows](https://gitcode.com/world_minecraft/Windows12?utm_source=devpress_gitcode_keyword&login=from_csdn) [VMware](https://gitcode.com/open-source-toolkit/4d7f0/overview?utm_source=devpress_gitcode_keyword&login=from_csdn) [仓颉](https://gitcode.com/Cangjie/CangjieCommunity/overview?utm_source=devpress_gitcode_keyword&login=from_csdn) [vue](https://gitcode.com/DevCloudFE/vue-devui?utm_source=devpress_gitcode_keyword&login=from_csdn) [WxJava](https://gitcode.com/binary/WxJava?utm_source=devpress_gitcode_keyword&login=from_csdn) [vscode](https://gitcode.com/weixin_44128887/vscode?utm_source=devpress_gitcode_keyword&login=from_csdn) [opencv](https://gitcode.com/logiczhao/opencv?utm_source=devpress_gitcode_keyword&login=from_csdn) [Qwen2.5-7B-Instruct-AWQ](https://ai.gitcode.com/hf_mirrors/Qwen/Qwen2.5-7B-Instruct-AWQ?login=from_csdn) [jeesite](https://gitcode.com/thinkgem/jeesite?utm_source=devpress_gitcode_keyword&login=from_csdn) [vision](https://gitcode.com/iwordshow/vision?utm_source=devpress_gitcode_keyword&login=from_csdn) [anaconda](https://gitcode.com/robin1983liu/anaconda?utm_source=devpress_gitcode_keyword&login=from_csdn) [openHiTLS](https://gitcode.com/openHiTLS/openhitls?utm_source=devpress_gitcode_keyword&login=from_csdn)

活动日历
[查看更多](https://gitcode.csdn.net/activelist)

活动时间 2025-07-05 14:00:00

[已结束![](https://i-blog.csdnimg.cn/devpress/blog/53a013d2a8dc44ca836c0dd6724ffa42.png)](https://gitcode.csdn.net/6853bf59965a29319f26dce5.html)

[openvela 城市沙龙—北京站](https://gitcode.csdn.net/6853bf59965a29319f26dce5.html)

[![](https://devpress.csdnimg.cn/b62ae7181dc24b7aa9bc526023c59a1b.jpg)](https://devpress.csdn.net/user/csdn_codechina)[AtomGit](https://devpress.csdn.net/user/csdn_codechina)

直播时间 2026-02-28 16:22:32

[![](https://csdnimg.cn/release/devpress/public/img/play.17062ee0.svg)回放中![](https://live-file.csdnimg.cn/release/live/file/1772180964344.png?x-oss-process=image/resize,l_1000)](https://gitcode.csdn.net/69afd78e0a2f6a37c5964c97.html)

[仓颉社区workshop](https://gitcode.csdn.net/69afd78e0a2f6a37c5964c97.html)

[![](https://devpress.csdnimg.cn/b62ae7181dc24b7aa9bc526023c59a1b.jpg)](https://devpress.csdn.net/user/csdn_codechina)[AtomGit](https://devpress.csdn.net/user/csdn_codechina)

直播时间 2026-02-04 19:50:55

[![](https://csdnimg.cn/release/devpress/public/img/play.17062ee0.svg)回放中![](https://live-file.csdnimg.cn/release/live/file/1769676396794.png?x-oss-process=image/resize,l_1000)](https://gitcode.csdn.net/69afd80d0a2f6a37c5964d85.html)

[解构“如意玲珑（Linyaps）”](https://gitcode.csdn.net/69afd80d0a2f6a37c5964d85.html)

[![](https://devpress.csdnimg.cn/b62ae7181dc24b7aa9bc526023c59a1b.jpg)](https://devpress.csdn.net/user/csdn_codechina)[AtomGit](https://devpress.csdn.net/user/csdn_codechina)

直播时间 2026-01-15 16:49:33

[![](https://csdnimg.cn/release/devpress/public/img/play.17062ee0.svg)回放中![](https://live-file.csdnimg.cn/release/live/file/1612251329735.png)](https://gitcode.csdn.net/69afddb754b52172bc6041e1.html)

[LazyLLM Agentic 应用开发快速上手](https://gitcode.csdn.net/69afddb754b52172bc6041e1.html)

[![](https://devpress.csdnimg.cn/b62ae7181dc24b7aa9bc526023c59a1b.jpg)](https://devpress.csdn.net/user/csdn_codechina)[AtomGit](https://devpress.csdn.net/user/csdn_codechina)

直播时间 2025-11-18 18:56:26

[![](https://csdnimg.cn/release/devpress/public/img/play.17062ee0.svg)回放中![](https://live-file.csdnimg.cn/release/live/file/1763359363452.png?x-oss-process=image/resize,l_1000)](https://gitcode.csdn.net/69afdde40a2f6a37c596529d.html)

[fountain 实现细节与使用方法](https://gitcode.csdn.net/69afdde40a2f6a37c596529d.html)

[![](https://devpress.csdnimg.cn/b62ae7181dc24b7aa9bc526023c59a1b.jpg)](https://devpress.csdn.net/user/csdn_codechina)[AtomGit](https://devpress.csdn.net/user/csdn_codechina)

目录

- [一、前言：AI 评标系统的双向技术价值](https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html#devmenu1)
- [二、CSDN 合规声明与文章说明](https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html#devmenu2)
- [三、AI 评标系统整体技术架构（双场景统一架构）](https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html#devmenu3)
- [四、场景一：投标方标书合规检测技术实现](https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html#devmenu5)
- [五、场景二：评标方围标串标智能识别技术实现](https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html#devmenu6)
- [六、工程化落地关键技术](https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html#devmenu7)
- [七、生产环境真实踩坑记录](https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html#devmenu8)
- [八、安华招标技术实践分享](https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html#devmenu9)
- [九、未来技术展望](https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html#devmenu10)
- [十、总结](https://gitcode.csdn.net/6a0e8911662f9a54cb760a4e.html#devmenu11)

查看AI大纲

![](https://csdnimg.cn/release/devpress/public/img/top.c3a2945a.svg)

回到

顶部

![](https://devpress.csdnimg.cn/8bc8dd1a2bc24184a16a142654c4a49e.png)AtomGit开源社区

[AI 编程助手](https://ai.atomgit.com/serverless-api?utm_source=devpress_gitcode) [🔥 国产模型专区](https://ai.gitcode.com/models?utm_source=devpress_gitcode) [G-Star](https://gitcode.com/g-star/apply?utm_source=devpress_gitcode) [AI 学习教程](https://ai.gitcode.com/learn?utm_source=devpress_gitcode) [最新活动](https://news.gitcode.com/activity?utm_source=devpress_gitcode)

## 登录社区云

登录社区云，与社区用户共同成长

- CSDN账号登录

欢迎加入社区

取消确定

### AtomGit开源社区

邀请您加入社区

立即加入

欢迎加入社区

取消确定

欢迎加入社区

取消确定

欢迎加入社区

取消确定

### 来源 10: [2605.29427] FinGuard: Detecting Financial Regulatory Non-Compliance in LLM Interactions

- URL: https://arxiv.org/pdf/2605.29427
- 精读方法：jina-readerlm-academic

```markdown
The provided draft Markdown does not match the content of the original HTML, which only contains a head tag with no actual body content. Therefore, there is nothing to extract or refine further into Markdown beyond the title "Your Title" if one were present.
```


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
