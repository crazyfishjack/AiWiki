---
title: "调研证据包：投标AI角色提示词 招标文件解析Prompt 商务标生成提示词 技术标应答模板 评分点逐条应答提示词 投标废标风险筛查Prompt 标书合规校验提示词 投标报价测算提示词 招投标RAG提示词工程 投标助手结构化提示词模板"
source-type: article
generated: 2026-06-21
generated-by: wiki-research-skill
research-mode: standard
---

# 调研证据包：投标AI角色提示词 招标文件解析Prompt 商务标生成提示词 技术标应答模板 评分点逐条应答提示词 投标废标风险筛查Prompt 标书合规校验提示词 投标报价测算提示词 招投标RAG提示词工程 投标助手结构化提示词模板

## 调研问题

投标AI角色提示词 招标文件解析Prompt 商务标生成提示词 技术标应答模板 评分点逐条应答提示词 投标废标风险筛查Prompt 标书合规校验提示词 投标报价测算提示词 招投标RAG提示词工程 投标助手结构化提示词模板

## 摘要

本文档是四工具检索生成的证据包草稿，不是最终调研报告。Agent 必须先阅读本证据包，执行下方"AI 综合指令"，生成新的中文综合 raw 报告，然后询问用户是否入库。本证据包保留不删除。

- 发现候选信源：38
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
| exa | 1.00 | [2603.22513v1] Generating and Evaluating Sustainable Procurement Criteria for the Swiss Public Sector using In-Context Prompting with Large Language Models | https://arxiv.org/abs/2603.22513v1 |
| exa | 1.00 | LBM: Hierarchical Large Auto-Bidding Model via Reasoning and Acting | https://arxiv.org/html/2603.05134v1 |
| exa | 1.00 | From Large Language Model Predicates to Logic Tensor Networks: Neurosymbolic Offer Validation in Regulated Procurement | https://arxiv.org/html/2604.05539 |
| exa | 1.00 | [2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models | https://arxiv.org/abs/2309.12132v2 |
| exa | 1.00 | Data-Driven Contract Management at Scale: A Zero-Shot LLM Architecture for Big Data and Legal Intelligence | https://www.mdpi.com/2227-7080/14/2/88 |
| exa | 1.00 |  | https://arxiv.org/pdf/2410.10873 |
| exa | 1.00 | QualBench: Benchmarking Chinese LLMs with Localized Professional Qualifications for Vertical Domain Evaluation | https://arxiv.org/html/2505.05225v2 |
| exa | 1.00 | QualBench: Benchmarking Chinese LLMs with Localized Professional Qualifications for Vertical Domain Evaluation | https://arxiv.org/pdf/2505.05225 |
| exa | 1.00 |  | https://arxiv.org/pdf/2311.05812 |
| exa | 1.00 | [2505.09027v1] Tests as Prompt: A Test-Driven-Development Benchmark for LLM Code Generation | https://arxiv.org/abs/2505.09027v1 |
| exa | 1.00 | ProG: A Graph Prompt Learning Benchmark | https://arxiv.org/html/2406.05346v1 |
| exa | 1.00 | [2603.02239v1] Engineering Reasoning and Instruction (ERI) Benchmark: A Large Taxonomy-driven Dataset for Foundation Models and Agents | https://arxiv.org/abs/2603.02239v1 |
| exa | 1.00 | AuditWen: An Open-Source Large Language Model for Audit | https://arxiv.org/html/2410.10873v1 |
| exa | 1.00 |  | https://arxiv.org/pdf/2603.05134 |
| tavily | 0.72 | AI辅助评标不是完全替代人工，找对方法，10个步骤就能高效落地\|通用\|废标\|招标\|投标人\|ai辅助评标_网易订阅 | https://www.163.com/dy/article/KVAMCJMO0556M2QN.html |
| tavily | 0.70 | 用 WorkBuddy 辅助写投标技术方案：别让 AI 替你投标，让它替你把话说清楚 - 53AI-AI知识库\|企业AI知识库\|大模型知识库\|前线部署工程师\|FDE\|AIHub | https://www.53ai.com/news/neirongchuangzuo/2026060363284.html |
| tavily | 0.69 | 标书智能体（一）——AI解析招标文件代码+提示词 - 博客园 | https://www.cnblogs.com/yibiaoai/p/19064673 |
| tavily | 0.63 | 高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云 | https://cloud.tencent.com/developer/article/2498790 |
| tavily | 0.61 | 零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF上传自动提条款、标风险、出建议-腾讯云开发者社区-腾讯云 | https://cloud.tencent.com/developer/article/2631225 |
| tavily | 0.57 | 标桥首页 | https://www.bqpoint.com |
| tavily | 0.57 | 提示词工程最佳实践 - Jimmy Song | https://jimmysong.io/zh/book/ai-handbook/prompt/best-practices |
| tavily | 0.55 | DeepSeek赋能标书制作：AI知识库如何革新投标方案生成？（附快标书AI 知识库使用教程） - 53AI-AI知识库\|企业AI知识库\|大模型知识库\|前线部署工程师\|FDE\|AIHub | https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html |
| tavily | 0.54 | 快标宝AI: AI标书-标书怎么做-标书制作软件 | https://www.kuaibiaobao.com |
| tavily | 0.54 | 一文解析Prompt设计框架与技巧，详细讲解六种提示词设计方法和五大主流框架_人工智能_沈页-智能体开发者社区 | https://adg.csdn.net/6973116c437a6b40336b7ea4.html |
| tavily | 0.51 | 提示词模板 | https://www.tencentcloud.com/zh/document/product/1254/73343 |
| tavily | 0.51 | 喜鹊标书AI \| AI 标书制作平台与投标方案助手 | https://www.xiquebiaoshu.com |
| tavily | 0.50 | AI应用：提示词以及提示词工程 - 博客园 | https://www.cnblogs.com/xjwhaha/p/19792440 |
| tavily | 0.50 | 智能标书助手-艾瑞数智 | https://www.idigital.com.cn/common-ai-2 |
| tavily | 0.48 | AI 员工提示词工程指南 - NocoBase 文档 | https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide |

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
3. [LBM: Hierarchical Large Auto-Bidding Model via Reasoning and Acting](https://arxiv.org/html/2603.05134v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
4. [From Large Language Model Predicates to Logic Tensor Networks: Neurosymbolic Offer Validation in Regulated Procurement](https://arxiv.org/html/2604.05539)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
5. [[2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models](https://arxiv.org/abs/2309.12132v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
6. [Data-Driven Contract Management at Scale: A Zero-Shot LLM Architecture for Big Data and Legal Intelligence](https://www.mdpi.com/2227-7080/14/2/88)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
7. [https://arxiv.org/pdf/2410.10873](https://arxiv.org/pdf/2410.10873)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
8. [QualBench: Benchmarking Chinese LLMs with Localized Professional Qualifications for Vertical Domain Evaluation](https://arxiv.org/html/2505.05225v2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
9. [QualBench: Benchmarking Chinese LLMs with Localized Professional Qualifications for Vertical Domain Evaluation](https://arxiv.org/pdf/2505.05225)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
10. [https://arxiv.org/pdf/2311.05812](https://arxiv.org/pdf/2311.05812)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
11. [[2505.09027v1] Tests as Prompt: A Test-Driven-Development Benchmark for LLM Code Generation](https://arxiv.org/abs/2505.09027v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
12. [ProG: A Graph Prompt Learning Benchmark](https://arxiv.org/html/2406.05346v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
13. [[2603.02239v1] Engineering Reasoning and Instruction (ERI) Benchmark: A Large Taxonomy-driven Dataset for Foundation Models and Agents](https://arxiv.org/abs/2603.02239v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
14. [AuditWen: An Open-Source Large Language Model for Audit](https://arxiv.org/html/2410.10873v1)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
15. [https://arxiv.org/pdf/2603.05134](https://arxiv.org/pdf/2603.05134)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
16. [AI辅助评标不是完全替代人工，找对方法，10个步骤就能高效落地|通用|废标|招标|投标人|ai辅助评标_网易订阅](https://www.163.com/dy/article/KVAMCJMO0556M2QN.html)
   - 工具：tavily
   - 分数：0.72
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
17. [用 WorkBuddy 辅助写投标技术方案：别让 AI 替你投标，让它替你把话说清楚 - 53AI-AI知识库|企业AI知识库|大模型知识库|前线部署工程师|FDE|AIHub](https://www.53ai.com/news/neirongchuangzuo/2026060363284.html)
   - 工具：tavily
   - 分数：0.70
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
18. [标书智能体（一）——AI解析招标文件代码+提示词 - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.69
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
19. [高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.63
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
20. [零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF上传自动提条款、标风险、出建议-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2631225)
   - 工具：tavily
   - 分数：0.61
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
21. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
22. [提示词工程最佳实践 - Jimmy Song](https://jimmysong.io/zh/book/ai-handbook/prompt/best-practices)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
23. [DeepSeek赋能标书制作：AI知识库如何革新投标方案生成？（附快标书AI 知识库使用教程） - 53AI-AI知识库|企业AI知识库|大模型知识库|前线部署工程师|FDE|AIHub](https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html)
   - 工具：tavily
   - 分数：0.55
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
24. [快标宝AI: AI标书-标书怎么做-标书制作软件](https://www.kuaibiaobao.com)
   - 工具：tavily
   - 分数：0.54
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
25. [一文解析Prompt设计框架与技巧，详细讲解六种提示词设计方法和五大主流框架_人工智能_沈页-智能体开发者社区](https://adg.csdn.net/6973116c437a6b40336b7ea4.html)
   - 工具：tavily
   - 分数：0.54
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
26. [提示词模板](https://www.tencentcloud.com/zh/document/product/1254/73343)
   - 工具：tavily
   - 分数：0.51
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
27. [喜鹊标书AI | AI 标书制作平台与投标方案助手](https://www.xiquebiaoshu.com)
   - 工具：tavily
   - 分数：0.51
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
28. [AI应用：提示词以及提示词工程 - 博客园](https://www.cnblogs.com/xjwhaha/p/19792440)
   - 工具：tavily
   - 分数：0.50
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
29. [智能标书助手-艾瑞数智](https://www.idigital.com.cn/common-ai-2)
   - 工具：tavily
   - 分数：0.50
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
30. [AI 员工提示词工程指南 - NocoBase 文档](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide)
   - 工具：tavily
   - 分数：0.48
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
31. [[PDF] RAG 字节跳动实践手册](https://www.cdut.edu.cn/__local/E/5B/B6/39E6C9ADF20836A45F7C765C31E_B2F36ACF_167F1B.pdf)
   - 工具：tavily
   - 分数：0.47
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
32. [附录 F：提示词技术决策树 | 大模型提示词工程指南 | Prompt Engineering Guide](https://yeasy.gitbook.io/prompt_engineering_guide/fu-lu/f_decision_tree)
   - 工具：tavily
   - 分数：0.46
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
33. [人工智能提示词撰写终极指南：范例与最佳实践 - Baklib](https://www.baklib.com/blog/baklib-ai-prompts)
   - 工具：tavily
   - 分数：0.46
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
34. [招投标知识库文档解析_招标文件/投标文件/RAG前处理方案_TextIn](https://www.textin.com/scenarios/tender-bid-knowledge-base)
   - 工具：tavily
   - 分数：0.46
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
35. [AI标书系统推荐：数商云如何重构企业投标竞争力_财富号_东方财富网](https://caifuhao.eastmoney.com/news/20260306090418965055360)
   - 工具：tavily
   - 分数：0.45
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
36. [提示词工程高级技巧 | Jimmy Song](https://jimmysong.io/zh/book/ai-handbook/prompt/advanced)
   - 工具：tavily
   - 分数：0.42
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
37. [易标AI](https://yibiao.pro)
   - 工具：tavily
   - 分数：0.42
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
38. [[PDF] 面向工程审计行业的DeepSeek 大模型应用指南](https://sea.nau.edu.cn/_upload/article/files/9f/48/0664056241d39174c060c10d3ec7/84a746e6-c8d1-4869-bd9e-246aa117040f.pdf)
   - 工具：tavily
   - 分数：0.41
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考

### 剔除信源
1. [标书智能体（一）——AI解析招标文件代码+提示词 - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.68
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
2. [高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.62
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
3. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.55
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
4. [DeepSeek赋能标书制作：AI知识库如何革新投标方案生成？（附快 ...](https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html)
   - 工具：tavily
   - 分数：0.53
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
5. [人工智能提示词撰写终极指南：范例与最佳实践 | Baklib](https://www.baklib.com/blog/baklib-ai-prompts)
   - 工具：tavily
   - 分数：0.42
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
6. [Ant Group 2025 Sustainability Report Highlights Record AI R&D Investment – Company Announcement - Financial Times](https://markets.ft.com/data/announce/detail?dockey=600-202606170512BIZWIRE_USPRX____20260617_BW847068-1)
   - 工具：tavily
   - 分数：0.04
   - 来源等级：C
   - 剔除原因：score 低于 0.4
7. [The tariff storm has a silver lining. And it belongs to preconstruction. - Construction Dive](https://www.constructiondive.com/spons/the-tariff-storm-has-a-silver-lining-and-it-belongs-to-preconstruction/822325/)
   - 工具：tavily
   - 分数：0.03
   - 来源等级：C
   - 剔除原因：score 低于 0.4
8. [TABLE-Artner -2026/27 div forecast - TradingView](https://www.tradingview.com/news/reuters.com,2026-06-16:newsml_XB1QSL41D:0-table-artner-2026-27-div-forecast/)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
9. [China Top Agricultural Grain Pp Woven Bag Suppliers 2026? - openPR.com](https://www.openpr.com/news/4554679/china-top-agricultural-grain-pp-woven-bag-suppliers-2026)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
10. [TABLE-Optimus Group Company -2025/26 parent results - TradingView](https://www.tradingview.com/news/reuters.com,2026-06-19:newsml_XB07EMXLK:0-table-optimus-group-company-2025-26-parent-results/)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
11. [TABLE-Futaba Industrial -2025/26 parent results - TradingView](https://www.tradingview.com/news/reuters.com,2026-06-17:newsml_XB1IJO1GD:0-table-futaba-industrial-2025-26-parent-results/)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
12. [AI & Advanced Analytics - Fierce Biotech](https://www.fiercebiotech.com/cro/ai-advanced-analytics)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
13. [Kolon Benit Positions Itself as Manufacturing AX Strategist and Execution Partner - thelec.net](https://www.thelec.net/news/articleView.html?idxno=11407)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
14. [Leadership in Regulatory & Quality Compliance - Fierce Biotech](https://www.fiercebiotech.com/cro/leadership-regulatory-quality-compliance)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
15. [Supply Chain Excellence - Fierce Biotech](https://www.fiercebiotech.com/cro/supply-chain-excellence)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
16. [标书智能体（一）——AI解析招标文件代码+提示词 - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.68
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
17. [高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.62
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
18. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.55
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
19. [喜鹊标书AI | AI 标书制作平台与投标方案助手](https://www.xiquebiaoshu.com)
   - 工具：tavily
   - 分数：0.49
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
20. [标书智能体（一）——AI解析招标文件代码+提示词 - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673)
   - 工具：tavily
   - 分数：0.67
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
21. [高效速搭基于DeepSeek的招标文书智能写作Agent - 腾讯云](https://cloud.tencent.com/developer/article/2498790)
   - 工具：tavily
   - 分数：0.61
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
22. [标桥首页](https://www.bqpoint.com)
   - 工具：tavily
   - 分数：0.56
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
23. [DeepSeek赋能标书制作：AI知识库如何革新投标方案生成？（附快 ...](https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html)
   - 工具：tavily
   - 分数：0.55
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
24. [快标宝AI: AI标书-标书怎么做-标书制作软件](https://www.kuaibiaobao.com)
   - 工具：tavily
   - 分数：0.53
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
25. [喜鹊标书AI | AI 标书制作平台与投标方案助手](https://www.xiquebiaoshu.com)
   - 工具：tavily
   - 分数：0.50
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
26. [智能标书助手-艾瑞数智](https://www.idigital.com.cn/common-ai-2)
   - 工具：tavily
   - 分数：0.49
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
27. [Prompt, Prompt Engineering, 提示工程, 提示词-大模型服务平台百炼(Model Studio)-阿里云帮助中心](https://help.aliyun.com/zh/model-studio/prompt-engineering-guide)
   - 工具：tavily
   - 分数：0.37
   - 来源等级：C
   - 剔除原因：score 低于 0.4

## 完整精读结果

### 来源 1: 标书智能体（一）——AI解析招标文件代码+提示词 - 博客园

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

### 来源 2: 用 WorkBuddy 辅助写投标技术方案：别让 AI 替你投标，让它替你把话说清楚 - 53AI-AI知识库|企业AI知识库|大模型知识库|前线部署工程师|FDE|AIHub

- URL: https://www.53ai.com/news/neirongchuangzuo/2026060363284.html
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

[![](https://static.53ai.com/assets/static/images/tab1.png)首页](https://www.53ai.com/) [FDE知识库](https://www.53ai.com/news.html) [企业落地](https://www.53ai.com/news/qiyejingying) [内容创作](https://www.53ai.com/news/neirongchuangzuo)

# 用 WorkBuddy 辅助写投标技术方案：别让 AI 替你投标，让它替你把话说清楚

发布日期：2026-06-03 08:11:12浏览次数： 1720

作者：深AI浅析

![](https://static.53ai.com/assets/static/images/detail-icon.png)

微信搜一搜，关注“深AI浅析”

推荐语

用WorkBuddy辅助写投标技术方案，不是让它替你投标，而是帮你把思路表达得更专业、清晰、合规，降低写作焦虑。

核心内容：

1\. WorkBuddy在投标方案中的五大核心辅助功能

2\. 撰写前先做“投标响应表”的关键步骤

3\. 以“项目理解”章节为例的实操应用

![](https://static.53ai.com/assets/static/images/avatar.jpg)

杨芳贤

53AI创始人/腾讯云(TVP)最具价值专家

很多人第一次用 AI 写投标技术方案，都会遇到同一个问题：

把招标文件丢进去，期待它一键生成一份能直接投出去的技术标。

这个想法很诱人，也很容易出问题。

投标技术方案不是普通文章。

它要逐条响应招标要求，紧扣评分标准，避开废标风险，还要体现企业真实能力。

一个漏项、一个错项、一个过度承诺，都可能让一份看起来很漂亮的方案变成风险文件。

WorkBuddy 更适合承担一个清晰的角色：技术方案写作助手。

它最适合帮你把已经明确的思路，整理得更专业、更清楚、更像一份正式投标文件。

## 先说结论：WorkBuddy 适合做什么？

如果你的目标是写投标技术方案，WorkBuddy 可以重点辅助五类工作。

**第一，优化语言表达。** 把口语化、零散的内容改成正式、稳健、专业的投标语言。

**第二，梳理章节逻辑。** 把“项目理解、技术路线、实施计划、质量保障、售后服务”等章节写得更有层次。

**第三，改写已有材料。** 把公司历史方案、项目经验、产品介绍，改成更贴合当前项目的表述。

**第四，润色英文投标内容。** 如果涉及英文 proposal、海外客户方案，它可以辅助表达优化。

**第五，降低空白页焦虑。** 当你不知道第一段怎么开头、某个章节怎么展开时，它可以先给出一个可修改的初稿。

同时，要守住边界。

WorkBuddy 不适合直接判断废标条款，不适合替你确认资质是否满足，也不适合替你承诺工期、人员、设备、验收标准。

**一句话总结：WorkBuddy 可以帮你写得更好，但不能替你投得更准。**

## 写技术方案前，先做响应表

很多技术标写不好，不是文笔问题，而是前期没有拆清楚。

真正开始写之前，建议先做一张“投标响应表”。

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| 招标要求 | 评分点 | 响应章节 | 我方材料 | 风险备注 |
| 项目实施方案完整性 | 10分 | 第三章 实施方案 | 过往项目案例 | 需补充进度计划 |
| 质量保障措施 | 8分 | 第五章 质量控制 | 质检流程文件 | 不要承诺超范围验收 |
| 售后服务能力 | 6分 | 第七章 售后服务 | 服务网点说明 | 核实响应时间 |

这一步非常关键。

WorkBuddy 再聪明，也不能凭空知道你公司的真实资质、真实人员、真实案例和真实履约能力。

你先把“该响应什么”拆出来，再让 AI 帮你写，生成内容会稳很多。

## WorkBuddy 最适合辅助的 5 类章节

### 1\. 项目理解

项目理解是技术方案的开头。

评审专家通常会通过这一章判断你有没有读懂招标文件。

这一章最忌讳空话。

我司高度重视本项目，将充分发挥专业优势，确保项目顺利实施。

这句话没错，但没有信息量。

更好的做法，是让 WorkBuddy 帮你把“项目背景、建设目标、需求理解、重点难点、响应策略”串起来。

```
请根据以下招标要求，帮我撰写投标技术方案中的“项目理解”章节。  要求： 1. 语言正式、专业、稳健； 2. 不夸大承诺； 3. 必须体现对项目背景、建设目标、核心需求、重点难点的理解； 4. 输出结构包括：项目背景、建设目标、需求理解、重点难点、总体响应思路。  招标要求如下： 【粘贴招标文件相关内容】
```

### 2\. 技术路线

技术路线是技术标的核心。

这里要写清楚五件事：

• 为什么这么做

• 分几个阶段做

• 每个阶段交付什么

• 如何保证效果

• 如何与招标要求对应

```
请帮我将以下技术思路整理成投标文件中的“技术路线”章节。  要求： 1. 按阶段展开； 2. 每个阶段说明主要工作、输出成果、保障措施； 3. 语言符合正式投标文件风格； 4. 不新增未经确认的技术承诺。  我的技术思路如下： 【粘贴你的技术路线草稿】
```

技术路线必须来自你的真实能力和真实交付方式。

AI 可以帮你表达，但不能替你拍板。

### 3\. 实施计划

实施计划最容易写成流水账。

第一阶段准备，第二阶段实施，第三阶段验收。

这类写法太粗，专家看不出你到底会怎么推进。

你可以让 WorkBuddy 把实施计划展开成更完整的结构：项目启动、需求调研、方案深化、组织实施、联调测试、验收交付、后续服务。

```
请根据以下项目情况，帮我撰写“项目实施计划”章节。  要求： 1. 按阶段说明工作内容； 2. 每个阶段包含目标、关键任务、交付成果； 3. 表达正式、清晰，适合投标技术方案； 4. 不承诺具体日期，只使用“项目启动后”“实施阶段”等稳健表述。  项目情况如下： 【粘贴项目情况】
```

### 4\. 质量保障措施

质量保障是技术标里的高频评分点。

很多人写这一章，只会堆词。

建立完善质量管理体系，严格控制过程质量，确保项目高质量完成。

问题是，专家看不到“怎么保障”。

更好的写法，是把质量保障拆成组织保障、制度保障、过程控制、成果审核、问题整改、风险预防几个层面。

```
请帮我撰写投标技术方案中的“质量保障措施”章节。  要求： 1. 从组织、制度、过程、成果、整改五个方面展开； 2. 语言正式，不使用夸张宣传语； 3. 每一项措施都要写出具体动作； 4. 避免空泛表述。  基础信息如下： 【粘贴企业质量管理方式或项目要求】
```

### 5\. 售后服务与响应保障

售后服务章节看似简单，其实风险不小。

响应时间、服务范围、人员配置、备件保障这些内容，不能随便承诺。

如果招标文件要求“2小时响应、24小时到场”，你可以响应。

如果公司做不到，就不要让 AI 自己编。

```
请根据以下售后服务能力，帮我撰写投标技术方案中的“售后服务与响应保障”章节。  要求： 1. 只基于我提供的信息写，不新增服务承诺； 2. 语言正式、稳健； 3. 结构包括：服务体系、响应机制、问题处理流程、服务记录与改进； 4. 如信息不足，请用“可根据项目要求配置”这类保守表达。  我方售后能力如下： 【粘贴真实售后能力】
```

这里的关键是：让 AI 保守一点。投标文件里，过度承诺比写得普通更危险。

## 一个好用的写作流程

### 第一步：人工拆招标文件

先把项目名称、项目背景、服务范围、技术要求、评分标准、交付成果、人员要求、时间要求、售后要求、废标条款摘出来。

这一部分不要偷懒。

后面所有内容，都要围绕这些信息展开。

### 第二步：做技术标目录

1\. 项目理解

2\. 技术路线

3\. 实施方案

4\. 项目组织管理

5\. 进度计划

6\. 质量保障措施

7\. 安全与风险控制

8\. 培训方案

9\. 售后服务

10\. 类似项目经验

然后根据评分标准调整顺序和重点。

### 第三步：逐章生成

不要一次性让它写完整技术标。

更推荐“一章一章写”。

每次都带上招标要求、本章目标、我方真实材料、写作限制和输出结构。

### 第四步：人工核对评分点

• 这个评分点有没有回应？

• 回应在哪一章？

• 是否有证明材料？

• 是否出现了不该承诺的内容？

• 是否和商务部分、报价部分冲突？

这一步可以让 AI 帮你列清单。

最终判断必须人工完成。

### 第五步：统一语言和格式

```
请帮我统一以下投标技术方案的语言风格。  要求： 1. 保持正式、专业、稳健； 2. 不改变原意； 3. 不新增承诺； 4. 删除重复、空泛、口语化表达； 5. 保留章节结构。  内容如下： 【粘贴章节内容】
```

这一轮很有用。

很多技术标的问题不是没内容，而是前后风格不统一。

统一一遍之后，整份方案会更像一个整体。

## 最容易踩的 4 个坑

### 1\. 让 AI 编案例

类似项目经验、人员证书、资质能力、服务网点，都必须真实存在。

AI 可以帮你改写，不能帮你编造。

### 2\. 让 AI 承诺做不到的指标

比如“7×24小时驻场”“1小时到场”“终身免费维护”。

只要写进投标文件，就可能成为合同履约压力。

### 3\. 不看评分标准

投标技术方案要回应技术要求，也要回应评分标准。

有时候真正决定分数的内容，不在“技术要求”章节，而在“评分办法”里。

### 4\. 生成后不做人工复核

AI 生成的内容可能很顺。

顺不代表准确。

投标文件最终看的不是文采，而是响应性、合规性、可执行性。

## 我的建议：把 WorkBuddy 放在中后段

如果把写技术方案分成三个阶段：

**前段：** 读招标文件、拆评分点、判断响应策略。

**中段：** 搭目录、写章节、整理材料。

**后段：** 润色、统一风格、检查表达。

WorkBuddy 最适合放在 **中段和后段**。

前段涉及投标策略和合规判断，要由人把关。

中后段主要是表达、结构和效率，可以多用。

这才是比较稳的用法。

## 最后给你一套万能提示词

如果你只想收藏一段，就收藏下面这段。

```
你是一名投标技术方案写作助手。  请根据我提供的招标要求和企业材料，辅助撰写投标技术方案。  写作要求： 1. 语言正式、专业、稳健，符合投标文件风格； 2. 必须逐条响应招标文件要求； 3. 不得新增我没有提供的资质、案例、人员、设备和服务承诺； 4. 不使用夸张宣传语； 5. 如果信息不足，请用保守表达，或提示我需要补充； 6. 输出内容要结构清晰，适合直接放入 Word 标书中。  本章主题： 【填写章节名称】  招标要求： 【粘贴招标文件相关内容】  评分标准： 【粘贴评分标准】  我方材料： 【粘贴企业真实材料】  请输出： 1. 本章写作大纲； 2. 正文内容； 3. 需要人工确认的风险点。
```

这段提示词的核心，是把 AI 框在可控范围里。

投标文件最怕的不是写得慢，而是写得看似漂亮、实际失控。

## 写在最后

AI 工具正在改变标书写作。

它真正带来的价值，是把重复整理、语言润色和初稿搭建的效率提上来。

投标技术方案最终还是要回到三个问题：

• 有没有读懂招标文件？

• 有没有回应评分标准？

• 有没有真实可执行的履约能力？

WorkBuddy 可以帮你把表达变得更清楚，把结构变得更顺，把初稿速度提上来。

真正决定技术标质量的，仍然是你对项目、招标文件和企业能力的理解。

[内容创作](https://www.53ai.com/keyword/%E5%86%85%E5%AE%B9%E5%88%9B%E4%BD%9C) [内容创作工具](https://www.53ai.com/keyword/%E5%86%85%E5%AE%B9%E5%88%9B%E4%BD%9C%E5%B7%A5%E5%85%B7) [内容创作策略](https://www.53ai.com/keyword/%E5%86%85%E5%AE%B9%E5%88%9B%E4%BD%9C%E7%AD%96%E7%95%A5)

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

上一篇：无 [下一篇：企业级 AI Coding 还有一堆问题，并没有像PR一样说的这么好用](https://www.53ai.com/news/neirongchuangzuo/2026053059604.html)

[返回列表](https://www.53ai.com/news/neirongchuangzuo)

相关资讯

[2026-05-30\\
\\
企业级 AI Coding 还有一堆问题，并没有像PR一样说的这么好用](https://www.53ai.com/news/neirongchuangzuo/2026053059604.html) [2026-05-27\\
\\
如何使用 AI 设计企业级产品？](https://www.53ai.com/news/neirongchuangzuo/2026052745183.html) [2026-05-24\\
\\
我研究了这个 18.6k Star 的 Skills，做幼师的女朋友夸我真猛！](https://www.53ai.com/news/neirongchuangzuo/2026052495824.html) [2026-05-21\\
\\
AI里，你必学的新Office三件套：MD、CSV、HTML](https://www.53ai.com/news/neirongchuangzuo/2026052121906.html) [2026-05-21\\
\\
体验完阿里首款Design Agent，我开始替UI/前端焦虑了..](https://www.53ai.com/news/neirongchuangzuo/2026052146058.html) [2026-05-19\\
\\
不要再直接把 UI 图转成代码了，先看这份 UI Spec 模板](https://www.53ai.com/news/neirongchuangzuo/2026051972386.html) [2026-05-18\\
\\
Git issue + PR：律师的下一代协作方式](https://www.53ai.com/news/neirongchuangzuo/2026051830618.html) [2026-05-16\\
\\
从Markdown到HTML：AI应用分发的下一个路口](https://www.53ai.com/news/neirongchuangzuo/2026051629508.html)

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

[纳米漫剧流水线，我劝你别太离谱 \\
\\
2026-04-14](https://www.53ai.com/news/neirongchuangzuo/2026041435897.html) [陶哲轩：AI 已经把想法成本降到几乎为0了... \\
\\
2026-03-24](https://www.53ai.com/news/neirongchuangzuo/2026032419275.html) [gpt-image-2发布后，PPT最强skill \\
\\
2026-04-28](https://www.53ai.com/news/neirongchuangzuo/2026042829073.html) [刚刚，Claude Design 发布！网友：将摧毁设计行业…… \\
\\
2026-04-18](https://www.53ai.com/news/neirongchuangzuo/2026041848036.html) [他们用悟空重写了内容生产这件事 \\
\\
2026-03-30](https://www.53ai.com/news/neirongchuangzuo/2026033010582.html) [了解 CreawAI RGB 模式 \\
\\
2026-03-27](https://www.53ai.com/news/neirongchuangzuo/2026032705318.html) [体验完阿里首款Design Agent，我开始替UI/前端焦虑了.. \\
\\
2026-05-21](https://www.53ai.com/news/neirongchuangzuo/2026052146058.html) [Amazon Quick桌面版：读文档、做PPT、查邮件，一句话全搞定 \\
\\
2026-05-06](https://www.53ai.com/news/neirongchuangzuo/2026050639182.html) [不要再直接把 UI 图转成代码了，先看这份 UI Spec 模板 \\
\\
2026-05-19](https://www.53ai.com/news/neirongchuangzuo/2026051972386.html) [如何使用 AI 设计企业级产品？ \\
\\
2026-05-27](https://www.53ai.com/news/neirongchuangzuo/2026052745183.html)

大家都在问

[如何使用 AI 设计企业级产品？ \\
\\
2026-05-27](https://www.53ai.com/news/neirongchuangzuo/2026052745183.html) [Nano Banana 2 实测：8 大落地场景 + 全部 Prompt，AI 绘画 SOTA 到底逆天在哪？ \\
\\
2026-02-28](https://www.53ai.com/news/neirongchuangzuo/2026022820346.html) [AI内容工程化：为什么你的团队用了AI，内容还是做不出来? \\
\\
2026-02-07](https://www.53ai.com/news/neirongchuangzuo/2026020798670.html) [OpenAI发布的新科研工具Prism，相比起Overleaf如何？值得入手吗？ \\
\\
2026-01-29](https://www.53ai.com/news/neirongchuangzuo/2026012950764.html) [当A++成为新的“紧箍咒”：我们是否忘记了测试的初衷？ \\
\\
2026-01-21](https://www.53ai.com/news/neirongchuangzuo/2026012185972.html) [AI对全球白领就业冲击有多大？ \\
\\
2026-01-06](https://www.53ai.com/news/neirongchuangzuo/2026010645937.html) [警惕！AI创业的三重“陷阱”你避开了吗？ \\
\\
2025-12-22](https://www.53ai.com/news/neirongchuangzuo/2025122238102.html) [NotebookLM+Nano Banana Pro：你的下一个PPT，何必是PPT？ \\
\\
2025-12-15](https://www.53ai.com/news/neirongchuangzuo/2025121571864.html)

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

![](https://www.53ai.com/news/neirongchuangzuo/2026060363284.html)

![](https://www.53ai.com/news/neirongchuangzuo/2026060363284.html)

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

### 来源 4: 零代码搭建「招标文件解析智能体」：Coze+TextIn xParse实现PDF上传自动提条款、标风险、出建议-腾讯云开发者社区-腾讯云

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

### 来源 6: AI辅助评标不是完全替代人工，找对方法，10个步骤就能高效落地|通用|废标|招标|投标人|ai辅助评标_网易订阅

- URL: https://www.163.com/dy/article/KVAMCJMO0556M2QN.html
- 精读方法：firecrawl-scrape

antanalysis set uid,donnot delete.

![](https://www.163.com/dy/article/KVAMCJMO0556M2QN.html)

[网易首页](https://www.163.com/ "网易首页")

[应用](https://www.163.com/#f=topnav)

- [_网易新闻_](https://m.163.com/newsapp/#f=topnav)
- [_网易公开课_](https://open.163.com/#f=topnav)
- [_网易红彩_](https://hongcai.163.com/?from=pcsy-button)
- [_网易严选_](https://u.163.com/aosoutbdbd8)
- [_邮箱大师_](https://mail.163.com/client/dl.html?from=mail46)
- [_网易云课堂_](https://study.163.com/client/download.htm?from=163app&utm_source=163.com&utm_medium=web_app&utm_campaign=business)

无障碍浏览 [进入关怀版](https://www.163.com/dy/article/KVAMCJMO0556M2QN_pdya11y.html)

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

# AI辅助评标不是完全替代人工，找对方法，10个步骤就能高效落地

2026-06-13 16:36:31　来源: [爱财发财](https://www.163.com/dy/media/T1776306547801.html) ![](https://static.ws.126.net/163/f2e/dy_media/dy_media/static/images/ipLocation.f6d00eb.svg)河北

[举报](https://www.163.com/special/0077jt/tipoff.html?title=AI%E8%BE%85%E5%8A%A9%E8%AF%84%E6%A0%87%E4%B8%8D%E6%98%AF%E5%AE%8C%E5%85%A8%E6%9B%BF%E4%BB%A3%E4%BA%BA%E5%B7%A5%EF%BC%8C%E6%89%BE%E5%AF%B9%E6%96%B9%E6%B3%95%EF%BC%8C10%E4%B8%AA%E6%AD%A5%E9%AA%A4%E5%B0%B1%E8%83%BD%E9%AB%98%E6%95%88%E8%90%BD%E5%9C%B0)

[快速发贴](https://www.163.com/dy/article/KVAMCJMO0556M2QN.html#post_comment_area "快速发贴")[0](https://www.163.com/dy/article/KVAMCJMO0556M2QN.html# "点击查看跟贴")

分享至

![Scan me!](<Base64-Image-Removed>)

用微信扫码二维码

分享至好友和朋友圈

本教程适用于企业采购与招投标管理场景，帮助从业者掌握 **AI辅助评标怎么操作** 的核心流程，大幅提升评标效率与准确性，规避合规风险。

![](https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2026%2F0613%2F60037595j00tgkajz00bqd000fc00bip.jpg&thumbnail=660x2147483647&quality=80&type=jpg)

**AI辅助评标** 需掌握的3个基础认知：

认知一：AI工具定位。AI仅作为信息提取与比对预处理工具，不具备法定评标决策权，所有结论需人工复核。

认知二：数据隔离规范。招投标数据涉及商业机密，需明确AI工具的数据处理机制，严禁将敏感数据暴露于无保障环境。

认知三：结构化输入要求。AI处理能力高度依赖输入质量，非标文档必须预处理，确保信息完整可读。

**AI辅助评标实操** 必备的2类通用工具：

工具一：长文本解析类通用AI模型。需支持数十万字上下文解析，具备多文档交叉比对与表格提取功能。

工具二：文档格式转换工具。用于将各类格式投标文件统一转化为AI可精准识别的标准文档格式，降低解析乱码率。

步骤1：明确 **AI辅助评标** 需求与辅助边界，设定审查清单

明确本次评标的核心动作与AI介入节点。列出资质审查、技术响应、商务报价三大板块的具体审查项。将资质年检过期、社保缺失等硬性否决项设为AI优先筛查目标。必须确保AI仅执行比对预警，最终废标决定权归属评标委员会，防范合规风险。

步骤2：招标文件核心要素拆解，提取AI识别基准

打开招标文件，提取资质要求、技术参数带“★”号条款、商务计分规则。将上述条款转化为结构化清单，剔除模糊修饰语，转化为明确参数阈值，如“注册资金不低于1000万”“具备CMA认证”。行业调研显示，超七成用户因步骤遗漏导致实操失败，必须确保清单覆盖所有实质性要求。

步骤3：构建 **AI辅助评标高效技巧** 之提示词框架

按照“角色设定+任务目标+输入数据+输出格式+约束条件”顺序编写提示词。设定AI为资深招投标审核专家，任务目标为根据给定基准清单逐项核对投标文件，输出格式规定为包含“审查项、投标响应内容、是否合格、依据页码”的四列表格。约束条件必须注明“仅依据提供的文本客观比对，禁止推测与主观评价”。

步骤4：投标文件数据提取与结构化，统一输入格式

将各投标人文件导入格式转换工具，确保文本与表格可选中提取。按“投标人名称+文件类型”规范命名。对大体积文件按资质、技术、商务拆分上传，防止单次解析超出AI上下文限制。重点关注扫描件与影印件，若存在图像模糊，需提前人工标注，避免AI识别出空白或乱码。

步骤5：资质符合性智能初审，执行硬性条件筛查

将步骤2提取的资质基准清单与某投标人资质文件一同输入AI。运行步骤3设定的提示词，指令AI逐项核对营业执照、资质证书、财务报表等是否满足要求。提取证书编号与有效期，排查过期资质。若发现联合体投标，需指令AI按招标文件规则核对联合体协议与分工资质，确保合规判定准确。

步骤6：技术方案偏离度分析，定位星号条款响应

将技术参数基准与某投标人技术文件输入AI。指令AI逐条比对技术响应，重点筛查正偏离、完全响应与负偏离项。针对带“★”号实质性要求，指令AI提取原文描述并判定是否满足，若为负偏离直接标记重大风险。要求AI提供具体响应内容所在的页码段落，便于后续人工快速定位原始依据。

步骤7：商务报价合理性评估，校验算术性错误

将商务计分规则与某投标人报价文件输入AI。指令AI核对大小写金额是否一致，分项报价汇总是否等于总报价，识别是否存在算术性错误。按照招标文件载明的价格分计算公式，指令AI计算该投标人的价格得分。多数从业者反馈，这一步是 **AI辅助评标** 实操的核心难点，必须要求AI严格遵循公式计算，禁止套用通用计价逻辑。

步骤8：评标质疑点与风险提示生成，汇总异常指标

指令AI汇总前述步骤中的异常项与负偏离项，生成独立的风险提示清单。要求AI识别低于成本价的异常报价、技术方案照搬照抄的雷同表述、资质文件存疑的盖章页等特征。针对发现的疑点，指令AI生成简明的质询问题草稿，供评标专家在澄清环节向投标人提问使用，提升质询针对性。

步骤9：人工复核与AI输出结果交叉验证，修正误判项

评标专家逐项审阅AI生成的审查表格与风险清单。调阅原始投标文件，对AI标记的“不合格”或“负偏离”项进行重点人工比对。修正因语义理解偏差导致的AI误判项，并在AI输出表格中标注修正结果。人工复核必须覆盖所有废标条款，不得因AI给出合格结论而免除专家审查义务。

步骤10：评标报告辅助生成与归档，固化评审轨迹

将修正后的各项审查结果汇总输入AI。指令AI按照标准评标报告模板，生成包含初步审查情况、详细审查情况、澄清情况与推荐中标候选人的报告草稿。审阅无误后导出存档。必须在报告中注明“AI仅作辅助工具，评审结论由评标委员会负责”的声明，保障程序合法与轨迹可追溯。

**AI辅助评标避坑方法** 与高频问题解决：

坑点1：盲目信任AI审核结论，导致不合规投标人漏网。解决方案：将AI设定为辅助筛查工具，所有符合性审查与强制性标准判定必须由评标专家签字确认，严格落实一票否决制。

坑点2：投标文件格式混乱导致提取失败。解决方案：操作前先确认文档文本可选中，若为纯图片扫描件，需经过通用OCR工具识别转换为文本后输入，避免AI解析空白。

坑点3：提示词缺乏评标标准约束，AI按通用认知评价。解决方案：在提示词中完整嵌入评标办法的权重、算分公式与废标条款，强制限制AI的自由裁量权与幻觉。

坑点4：商业敏感数据外泄风险。解决方案：优先选择支持私有化部署或提供企业级数据隔离的通用AI工具，关闭模型训练数据复用选项，标后及时清除云端会话记录。

坑点5：忽略行业特殊评标规则，AI判定偏离实际。解决方案：在步骤2拆解要素时，将特定行业的资质互认规则、特殊加分项作为独立约束条件显性写入提示词。

坑点6：人工复核流于形式，仅做抽样检查。解决方案：制定强制复核清单，要求对AI标记的负偏离项、质疑问询项及排名前三位候选人的核心资料必须进行100%人工原始文件比对。

**AI辅助评标** 实操合格标准：

1.完成投标文件关键信息结构化提取与对照，无关键资质遗漏。

2.AI生成的偏离度分析与风险提示覆盖所有硬性指标与星号条款，并提供原文依据。

3.人工复核修正比例处于合理区间，无核心废标条款误判，最终评标报告由专家签字确认生效。

掌握基础 **AI辅助评标** 步骤后，可进一步学习多模态文档解析与复杂算分逻辑拆解技巧，提升 **AI辅助评标** 实操的专业度。 **AI辅助评标** 的核心是规则，步骤是基础，掌握这两点就能稳步提升实操能力。

声明：个人原创，仅供参考

特别声明：以上内容(如有图片或视频亦包括在内)为自媒体平台“网易号”用户上传并发布，本平台仅提供信息存储服务。

Notice: The content above (including the pictures and videos if any) is uploaded and posted by a user of NetEase Hao, which is a social media platform and only provides information storage services.

_/_ 阅读下一篇 _/_

[返回网易首页](https://www.163.com/?f=post2020_dy) [下载网易新闻客户端](https://www.163.com/newsapp/#f=post2020_dy)

相关推荐

热点推荐

- [![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0621/7911fc67p00tgysbh000zc0009c0070c.png&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/news/article/KVUR86IC00019B3E.html?f=post2020_dy_recommends)

### [外国知名学者：当今世界只有四个大国](https://www.163.com/news/article/KVUR86IC00019B3E.html?f=post2020_dy_recommends)

参考消息 2026-06-21 12:27:22

[11544\\
_跟贴_ 11544](https://www.163.com/news/article/KVUR86IC00019B3E.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260621/P9rjH6VqG_cover.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/v/video/VCV0ODADT.html?f=post2020_dy_recommends)

### [交警执勤时全身叮满蚊虫，让人心疼！](https://www.163.com/v/video/VCV0ODADT.html?f=post2020_dy_recommends)

中国日报网 2026-06-21 09:46:06

[82\\
_跟贴_ 82](https://www.163.com/v/video/VCV0ODADT.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little9110fcce1a1j00tgzbnc000ud000hs00aym.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVJ2H140514BE2Q.html?f=post2020_dy_recommends)

### [媒体：两大核武国家“水仗”升级 巴基斯坦陷入恐慌](https://www.163.com/dy/article/KVVJ2H140514BE2Q.html?f=post2020_dy_recommends)

中国新闻周刊 2026-06-21 19:23:56

[1635\\
_跟贴_ 1635](https://www.163.com/dy/article/KVVJ2H140514BE2Q.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0621/781545cap00tgz2hh002uc000j600b9c.png&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVV3SINQ053469LG.html?f=post2020_dy_recommends)

### [大学生实习日薪180元 弄丢客户6.5万元劳力士表](https://www.163.com/dy/article/KVV3SINQ053469LG.html?f=post2020_dy_recommends)

极目新闻 2026-06-21 14:57:13

[3951\\
_跟贴_ 3951](https://www.163.com/dy/article/KVV3SINQ053469LG.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little357a3085a4cj00tgyepc0014d000hs00bug.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVUB8T0U0514R9KQ.html?f=post2020_dy_recommends)

### [世界女排联赛｜中国女排五连胜被巴西队终结](https://www.163.com/dy/article/KVUB8T0U0514R9KQ.html?f=post2020_dy_recommends)

北青网-北京青年报 2026-06-21 07:47:03

[69\\
_跟贴_ 69](https://www.163.com/dy/article/KVUB8T0U0514R9KQ.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little9167ded775cj00tgz78b0019d000u000jvg.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVDUGMT051492T3.html?f=post2020_dy_recommends)

### [就在明天，深市史上最大规模IPO开启申购，顶格申购需配深市市值632万元](https://www.163.com/dy/article/KVVDUGMT051492T3.html?f=post2020_dy_recommends)

红星新闻 2026-06-21 17:53:02

[234\\
_跟贴_ 234](https://www.163.com/dy/article/KVVDUGMT051492T3.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0621/15c02785p00tgylsl0049c0009c0070c.png&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/news/article/KVUIODNB000189PS.html?f=post2020_dy_recommends)

### [库拉索门将多次扑救 厄瓜多尔0-0战平库拉索](https://www.163.com/news/article/KVUIODNB000189PS.html?f=post2020_dy_recommends)

央视新闻 2026-06-21 09:58:57

[2502\\
_跟贴_ 2502](https://www.163.com/news/article/KVUIODNB000189PS.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0621/5a086c1bp00tgynx3001kc0009c0070c.png&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/news/article/KVULDI000001899O.html?f=post2020_dy_recommends)

### [三大品牌公布甲酰胺检测结果](https://www.163.com/news/article/KVULDI000001899O.html?f=post2020_dy_recommends)

红星新闻 2026-06-21 10:46:39

[1864\\
_跟贴_ 1864](https://www.163.com/news/article/KVULDI000001899O.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little517c4cb713cj00tgz18301bkd001hc00u0g.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVV6BKE30519DDQ2.html?f=post2020_dy_recommends)

### [从眼控到脑控，蔡磊化身“赛博躯体”称将把意识传送到具身机器人](https://www.163.com/dy/article/KVV6BKE30519DDQ2.html?f=post2020_dy_recommends)

第一财经资讯 2026-06-21 15:40:24

[193\\
_跟贴_ 193](https://www.163.com/dy/article/KVV6BKE30519DDQ2.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/three6237b10c1f4j00tgz79o000jd000hs00dcg.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVESD200550B6IS.html?f=post2020_dy_recommends)

### [关于桃子的消费提示：看着红的不一定甜！选桃存桃吃桃，一次讲清楚](https://www.163.com/dy/article/KVVESD200550B6IS.html?f=post2020_dy_recommends)

大象新闻 2026-06-21 18:09:22

[20\\
_跟贴_ 20](https://www.163.com/dy/article/KVVESD200550B6IS.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little7076e36af7bj00tgyh4z00eod000ro00img.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVUDV7S80534P59R.html?f=post2020_dy_recommends)

### [WTT卢布尔雅那站国乒无缘冠军，继上周萨格勒布常规挑战赛后，中国队已连续两站未获一冠](https://www.163.com/dy/article/KVUDV7S80534P59R.html?f=post2020_dy_recommends)

潇湘晨报 2026-06-21 08:34:12

[414\\
_跟贴_ 414](https://www.163.com/dy/article/KVUDV7S80534P59R.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0621/c6136ff1p00tgz304000zc0009c0070c.png&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVUTT5V8053469LG.html?f=post2020_dy_recommends)

### [英媒：斯塔默正考虑辞职 他的首相职位已无法继续维持](https://www.163.com/dy/article/KVUTT5V8053469LG.html?f=post2020_dy_recommends)

极目新闻 2026-06-21 13:12:41

[77\\
_跟贴_ 77](https://www.163.com/dy/article/KVUTT5V8053469LG.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little7766aa4b09cj00tgymzo0017d000hs00awg.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVUN0BK30514R9P4.html?f=post2020_dy_recommends)

### [洛杉矶宣布进入紧急状态](https://www.163.com/dy/article/KVUN0BK30514R9P4.html?f=post2020_dy_recommends)

澎湃新闻 2026-06-21 11:12:06

[151\\
_跟贴_ 151](https://www.163.com/dy/article/KVUN0BK30514R9P4.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0620/0514a2b3j00tgx340001od000hs00bug.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVSGTE3C0514R9KQ.html?f=post2020_dy_recommends)

### [端午假期第二天 北京市属公园迎客超38万人次](https://www.163.com/dy/article/KVSGTE3C0514R9KQ.html?f=post2020_dy_recommends)

北青网-北京青年报 2026-06-20 14:47:09

[132\\
_跟贴_ 132](https://www.163.com/dy/article/KVSGTE3C0514R9KQ.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little308684e48b9j00tgzcek0057d000xc01n9g.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVVKJ1I60511U82T.html?f=post2020_dy_recommends)

### [“一天一个价”，多个热门电脑机型近一个月上涨千元，经销商称价格变动太大，不敢多囤货](https://www.163.com/dy/article/KVVKJ1I60511U82T.html?f=post2020_dy_recommends)

红星资本局 2026-06-21 19:49:07

[5\\
_跟贴_ 5](https://www.163.com/dy/article/KVVKJ1I60511U82T.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=https://dingyue.ws.126.net/2026/06/22/FAMATuSFsz7MJziaFxZl2KY0MNNjrb6J0mob5tqh4.jpeg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/L004JF87055319R5.html?f=post2020_dy_recommends)

### [废品收购站残障人与鹅同住，一个连云港博主的认罪书](https://www.163.com/dy/article/L004JF87055319R5.html?f=post2020_dy_recommends)

记录刘杰 2026-06-22 00:29:32

[0\\
_跟贴_ 0](https://www.163.com/dy/article/L004JF87055319R5.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little32684aea96fj00tgys2300sbd000sg00lcc.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/KVUQTH2N0514R9P4.html?f=post2020_dy_recommends)

### [活力中国调研行｜上天、入海，“小巨人”们为何坚定布局最前沿](https://www.163.com/dy/article/KVUQTH2N0514R9P4.html?f=post2020_dy_recommends)

澎湃新闻 2026-06-21 12:20:29

[1292\\
_跟贴_ 1292](https://www.163.com/dy/article/KVUQTH2N0514R9P4.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/doccover_gen/487b3f90_1_cover.png&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/L00234QI05198CJN.html?f=post2020_dy_recommends)

### [超警戒水位4.44米 洪峰过境广西河池](https://www.163.com/dy/article/L00234QI05198CJN.html?f=post2020_dy_recommends)

财联社 2026-06-21 23:45:06

[10\\
_跟贴_ 10](https://www.163.com/dy/article/L00234QI05198CJN.html?f=post2020_dy_recommends)

- [![](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little966889614c9j00tgybpt0116d000xc00hip.jpg&thumbnail=140y88&quality=80&type=jpg)](https://www.163.com/dy/article/L004TU0G05561FZ1.html?f=post2020_dy_recommends)

### [亲哥偷光妹妹整份工资，家人却怒斥她报警是“背叛”](https://www.163.com/dy/article/L004TU0G05561FZ1.html?f=post2020_dy_recommends)

追星雷达站 2026-06-22 00:34:41

[0\\
_跟贴_ 0](https://www.163.com/dy/article/L004TU0G05561FZ1.html?f=post2020_dy_recommends)

[![冰火两重天！国内应届生内卷就业难，日本高中生被企业疯抢](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/cac40257j00tgyym40032d000rs00kum.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVV2O01N0553T17C.html?f=post1603_tab_news "冰火两重天！国内应届生内卷就业难，日本高中生被企业疯抢")

### [冰火两重天！国内应届生内卷就业难，日本高中生被企业疯抢](https://www.163.com/dy/article/KVV2O01N0553T17C.html?f=post1603_tab_news "冰火两重天！国内应届生内卷就业难，日本高中生被企业疯抢")

颤抖的熊猫

2026-06-21 14:42:28

[![手把手教徒弟反被抄家！中企印度遭洗劫，国家新规一招反杀！](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/4eaba356j00tgyxy8001sd000u000k7m.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVV27G9J0531CPV5.html?f=post1603_tab_news "手把手教徒弟反被抄家！中企印度遭洗劫，国家新规一招反杀！")

### [手把手教徒弟反被抄家！中企印度遭洗劫，国家新规一招反杀！](https://www.163.com/dy/article/KVV27G9J0531CPV5.html?f=post1603_tab_news "手把手教徒弟反被抄家！中企印度遭洗劫，国家新规一招反杀！")

52赫兹实验室

2026-06-21 14:28:41

[![原来她就是张颂文老婆，难怪丈夫总拿大奖，真是娶一个贤妻旺三代](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/big998934981e9j00tgz7vr001ed000m800r6p.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVVEG8400556D0RP.html?f=post1603_tab_news "原来她就是张颂文老婆，难怪丈夫总拿大奖，真是娶一个贤妻旺三代")

### [原来她就是张颂文老婆，难怪丈夫总拿大奖，真是娶一个贤妻旺三代](https://www.163.com/dy/article/KVVEG8400556D0RP.html?f=post1603_tab_news "原来她就是张颂文老婆，难怪丈夫总拿大奖，真是娶一个贤妻旺三代")

笑一个吧

2026-06-21 18:02:47

[![“全班就2个女生表情正常”，廉价毕业照被吐槽，家长咋不管管](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/big719a349c3d7j00tgzgsz01k6d000rh00wim.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVVPC8A70556B8V8.html?f=post1603_tab_news "“全班就2个女生表情正常”，廉价毕业照被吐槽，家长咋不管管")

### [“全班就2个女生表情正常”，廉价毕业照被吐槽，家长咋不管管](https://www.163.com/dy/article/KVVPC8A70556B8V8.html?f=post1603_tab_news "“全班就2个女生表情正常”，廉价毕业照被吐槽，家长咋不管管")

泽泽先生

2026-06-21 21:16:07

[![女子被情人睡时，丈夫还要下跪，2018年他忍无可忍，杀死妻子情人](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/5506ca49j00tgyypq000ld000ic00cwm.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVV326760523WUD9.html?f=post1603_tab_news "女子被情人睡时，丈夫还要下跪，2018年他忍无可忍，杀死妻子情人")

### [女子被情人睡时，丈夫还要下跪，2018年他忍无可忍，杀死妻子情人](https://www.163.com/dy/article/KVV326760523WUD9.html?f=post1603_tab_news "女子被情人睡时，丈夫还要下跪，2018年他忍无可忍，杀死妻子情人")

汉史趣闻

2026-06-21 14:45:00

[![非必要不做CT？医生强调：只要做过CT，患者一定多加关注这4点！](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0609/47d22cb3j00tgd2qy002dd000u000mim.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KV0L91E30556KJNM.html?f=post1603_tab_news "非必要不做CT？医生强调：只要做过CT，患者一定多加关注这4点！")

### [非必要不做CT？医生强调：只要做过CT，患者一定多加关注这4点！](https://www.163.com/dy/article/KV0L91E30556KJNM.html?f=post1603_tab_news "非必要不做CT？医生强调：只要做过CT，患者一定多加关注这4点！")

叙说医疗健康

2026-06-16 08:00:21

[![太无耻！具俊晔韩国节目又爆大S生前隐私，他的丑恶终于不藏了](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0620/4008eb75j00tgxmap002md000tc00nym.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVT79N7E051798PA.html?f=post1603_tab_news "太无耻！具俊晔韩国节目又爆大S生前隐私，他的丑恶终于不藏了")

### [太无耻！具俊晔韩国节目又爆大S生前隐私，他的丑恶终于不藏了](https://www.163.com/dy/article/KVT79N7E051798PA.html?f=post1603_tab_news "太无耻！具俊晔韩国节目又爆大S生前隐私，他的丑恶终于不藏了")

电影烂番茄

2026-06-20 21:23:50

[![梅洛尼、高市早苗与特朗普吵起来了](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/e0b769aej00tgylul0012d000hs00bvm.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVUJ8J8I0550A0OW.html?f=post1603_tab_news "梅洛尼、高市早苗与特朗普吵起来了")

### [梅洛尼、高市早苗与特朗普吵起来了](https://www.163.com/dy/article/KVUJ8J8I0550A0OW.html?f=post1603_tab_news "梅洛尼、高市早苗与特朗普吵起来了")

新民周刊

2026-06-21 10:06:51

[![特朗普持续抨击梅洛尼：美伊停战后，意总理又想“重修旧好”](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/doccover_gen/c38b8422_7_cover.png&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVV7HLN50514BQ68.html?f=post1603_tab_news "特朗普持续抨击梅洛尼：美伊停战后，意总理又想“重修旧好”")

### [特朗普持续抨击梅洛尼：美伊停战后，意总理又想“重修旧好”](https://www.163.com/dy/article/KVV7HLN50514BQ68.html?f=post1603_tab_news "特朗普持续抨击梅洛尼：美伊停战后，意总理又想“重修旧好”")

参考消息

2026-06-21 16:01:10

[![云南通报“中考历史试卷被指存在低级错误”：招生考试院分管领导、命题处处长、中考历史学科命题秘书被停职，对命题组组长及成员追责问责](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/6042c188j00tgz336006id000j600h3g.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVV8S33K053469LG.html?f=post1603_tab_news "云南通报“中考历史试卷被指存在低级错误”：招生考试院分管领导、命题处处长、中考历史学科命题秘书被停职，对命题组组长及成员追责问责")

### [云南通报“中考历史试卷被指存在低级错误”：招生考试院分管领导、命题处处长、中考历史学科命题秘书被停职，对命题组组长及成员追责问责](https://www.163.com/dy/article/KVV8S33K053469LG.html?f=post1603_tab_news "云南通报“中考历史试卷被指存在低级错误”：招生考试院分管领导、命题处处长、中考历史学科命题秘书被停职，对命题组组长及成员追责问责")

极目新闻

2026-06-21 16:24:20

[![雷军吃面事件升级！有大V怒斥对这个世界失望了，雷军做出回应](https://nimg.ws.126.net/?url=https://dingyue.ws.126.net/2026/06/21/ZI1dEDmk32ewQKi9foYblbtUCRGsIDXY0moacu6qa.jpeg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVVASS8805564S43.html?f=post1603_tab_news "雷军吃面事件升级！有大V怒斥对这个世界失望了，雷军做出回应")

### [雷军吃面事件升级！有大V怒斥对这个世界失望了，雷军做出回应](https://www.163.com/dy/article/KVVASS8805564S43.html?f=post1603_tab_news "雷军吃面事件升级！有大V怒斥对这个世界失望了，雷军做出回应")

火山詩话

2026-06-21 17:14:02

[![彻底闹掰了？九年无偿青训栽培，董路一句“永不合作”划清界限](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/big2481f2e2596j00tgzcj4001td000vx00i5p.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVVK81VP0556DLTK.html?f=post1603_tab_news "彻底闹掰了？九年无偿青训栽培，董路一句“永不合作”划清界限")

### [彻底闹掰了？九年无偿青训栽培，董路一句“永不合作”划清界限](https://www.163.com/dy/article/KVVK81VP0556DLTK.html?f=post1603_tab_news "彻底闹掰了？九年无偿青训栽培，董路一句“永不合作”划清界限")

阿晭评论哥

2026-06-21 19:43:08

[![难以置信，北京协和证实：40岁后男性最优运动，并非跑步撸铁](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/little67544547000j00tgz0ne001wd000hs00npg.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVV5HIVQ0553TF8W.html?f=post1603_tab_news "难以置信，北京协和证实：40岁后男性最优运动，并非跑步撸铁")

### [难以置信，北京协和证实：40岁后男性最优运动，并非跑步撸铁](https://www.163.com/dy/article/KVV5HIVQ0553TF8W.html?f=post1603_tab_news "难以置信，北京协和证实：40岁后男性最优运动，并非跑步撸铁")

华庭讲美食

2026-06-21 15:26:10

[![克洛普盛赞日本队：横扫只是开始，世界杯最大黑马成真正争冠热门](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/b8ce2409j00tgzhu3001cd000u000f0p.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVVQN0180548B69O.html?f=post1603_tab_news "克洛普盛赞日本队：横扫只是开始，世界杯最大黑马成真正争冠热门")

### [克洛普盛赞日本队：横扫只是开始，世界杯最大黑马成真正争冠热门](https://www.163.com/dy/article/KVVQN0180548B69O.html?f=post1603_tab_news "克洛普盛赞日本队：横扫只是开始，世界杯最大黑马成真正争冠热门")

体育闲话说

2026-06-21 21:44:21

[![首轮5-1狂胜！次轮1-5惨败 世界杯反差最大球队：世预赛2分垫底](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/1d7324abj00tgy1n3016pd00325021fm.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVTOD80J05299RGV.html?f=post1603_tab_news "首轮5-1狂胜！次轮1-5惨败 世界杯反差最大球队：世预赛2分垫底")

### [首轮5-1狂胜！次轮1-5惨败 世界杯反差最大球队：世预赛2分垫底](https://www.163.com/dy/article/KVTOD80J05299RGV.html?f=post1603_tab_news "首轮5-1狂胜！次轮1-5惨败 世界杯反差最大球队：世预赛2分垫底")

狍子歪解体坛

2026-06-21 02:57:45

[![绝杀出线！世界杯天降神兵：替补56分钟3球2助 创36年纪录](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/0d0651cdj00tgycqq001bd000hs00c1m.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVU80NFO05299A13.html?f=post1603_tab_news "绝杀出线！世界杯天降神兵：替补56分钟3球2助 创36年纪录")

### [绝杀出线！世界杯天降神兵：替补56分钟3球2助 创36年纪录](https://www.163.com/dy/article/KVU80NFO05299A13.html?f=post1603_tab_news "绝杀出线！世界杯天降神兵：替补56分钟3球2助 创36年纪录")

叶青足球世界

2026-06-21 06:51:05

[![离谱到家，日本踢世界杯比赛，中国观众超过了日本观众数倍](https://nimg.ws.126.net/?url=http://bjnewsrec-cv.ws.126.net/big6578384c640j00tgz9h600bqd000ip00c7m.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVVGEIIV0549908E.html?f=post1603_tab_news "离谱到家，日本踢世界杯比赛，中国观众超过了日本观众数倍")

### [离谱到家，日本踢世界杯比赛，中国观众超过了日本观众数倍](https://www.163.com/dy/article/KVVGEIIV0549908E.html?f=post1603_tab_news "离谱到家，日本踢世界杯比赛，中国观众超过了日本观众数倍")

体坛狗哥

2026-06-21 18:36:47

[![随着张本美和爆大冷门0-3出局，WTT卢布尔雅那站女单决赛对阵出炉](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/d9481484j00tgzawt002ad000zk00n6m.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVVI83OA0549WGPN.html?f=post1603_tab_news "随着张本美和爆大冷门0-3出局，WTT卢布尔雅那站女单决赛对阵出炉")

### [随着张本美和爆大冷门0-3出局，WTT卢布尔雅那站女单决赛对阵出炉](https://www.163.com/dy/article/KVVI83OA0549WGPN.html?f=post1603_tab_news "随着张本美和爆大冷门0-3出局，WTT卢布尔雅那站女单决赛对阵出炉")

侧身凌空斩

2026-06-21 19:08:28

[![老黄终于瞒不住了：直言大儿子确实去世了，大女儿一直在身边](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/22cd0936j00tgz1yq000wd000iz00hjm.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVV75KLA05566C07.html?f=post1603_tab_news "老黄终于瞒不住了：直言大儿子确实去世了，大女儿一直在身边")

### [老黄终于瞒不住了：直言大儿子确实去世了，大女儿一直在身边](https://www.163.com/dy/article/KVV75KLA05566C07.html?f=post1603_tab_news "老黄终于瞒不住了：直言大儿子确实去世了，大女儿一直在身边")

以茶带书

2026-06-21 15:54:37

[![穆里尼奥眼光太神了！皇马 2500 万捡漏超级神锋，世界杯一战封神](https://nimg.ws.126.net/?url=http://dingyue.ws.126.net/2026/0621/c12ae665j00tgyih100fmd000u000gwp.jpg&thumbnail=140y88&quality=90&type=jpg)](https://www.163.com/dy/article/KVUF3COK0556GNP0.html?f=post1603_tab_news "穆里尼奥眼光太神了！皇马 2500 万捡漏超级神锋，世界杯一战封神")

### [穆里尼奥眼光太神了！皇马 2500 万捡漏超级神锋，世界杯一战封神](https://www.163.com/dy/article/KVUF3COK0556GNP0.html?f=post1603_tab_news "穆里尼奥眼光太神了！皇马 2500 万捡漏超级神锋，世界杯一战封神")

澜归序

2026-06-21 08:58:40

2026-06-22 00:59:00

[![爱财发财](https://nimg.ws.126.net/?url=https://mobilepics.ws.126.net/2026_04_16_10_28_04A6hZI0mivnhosk.jpg&thumbnail=160y160&quality=80&type=jpg)](https://www.163.com/dy/media/T1776306547801.html)

[爱财发财](https://www.163.com/dy/media/T1776306547801.html)

[宣传好用物](https://www.163.com/dy/media/T1776306547801.html)

[_108_](https://www.163.com/dy/media/T1776306547801.html) 文章数[_0_](https://www.163.com/dy/media/T1776306547801.html) 关注度

往期回顾 [全部](https://www.163.com/dy/media/T1776306547801.html)

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

- ### [世界杯第1000场-日本4-0送突尼斯出局 上田绮世2射1传](https://www.163.com/sports/article/KVV0D49B00058781.html)

- ### [FIFA世界排名：荷兰德国库拉索小幅上升，厄瓜多尔下降7名](https://www.163.com/dy/article/KVVJ1RSJ0549BAP0.html)

- ### [热身赛：中国男篮力克澳大利亚 王俊杰23+6+4赵继伟一度受伤](https://www.163.com/dy/article/KVVPQ5IJ0529RKNN.html)

- ### [伊朗队再次控诉不公待遇，队医只能在返程飞机上为球员治疗](https://www.163.com/dy/article/KVVT849S0514R9P4.html)

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

- ### [_公开课_ \| 史上最完美的【八段锦】教学](https://open.163.com/newview/movie/free?pid=OHFS8DQ6F&mid=IHGLDM4GH)

- ### [_中国匠人_ \| 这届年轻人，正在修炼刚柔共生的人生](https://www.163.com/dy/article/KVKGVE2R0552U6MX.html)

- ### [_当下_ \| 75 周年特别策划\|AI歌曲 MV《一笔一划瞰长城》今日上线](https://www.163.com/gov/article/JD3ST3MJ002399RB.html)

- ### [_智库_ \| 海闻：去年我们赚了一万多亿美元，数字之外要读懂这些信号](https://www.163.com/money/article/KV7FMUKK00258J1R.html)

[健康](https://jiankang.163.com/)

[亲子](https://baby.163.com/)

[旅游](https://travel.163.com/)

[本地](https://bj.news.163.com/)

[公开课](https://open.163.com/)

[![](https://nimg.ws.126.net/?url=http://cms-bucket.ws.126.net/2026/0618/4c45ab0dp00tgtp53008oc0007s0050c.png&thumbnail=300x150&quality=90&type=jpg)**吃粽子的3条保胃法则，消化科医生推荐**](https://www.163.com/jiankang/article/KVNOPUO00038804H.html)

- ### [外出踏青、郊游，千万警惕这种虫子！](https://www.163.com/jiankang/article/KSDED7DP00388045.html)

- ### [千滚水、隔夜水到底能喝吗？真相来了！](https://www.163.com/jiankang/article/KT9K3EG900388045.html)

- ### [外卖这样吃，便利又健康！很多人不知道](https://www.163.com/jiankang/article/KT9JVQ2L00388045.html)

- ### [中疾控发布春夏呼吸道疾病防护指南](https://www.163.com/jiankang/article/KSDEO19400388045.html)

## [亲子要闻](https://baby.163.com/)

[![](https://nimg.ws.126.net/?url=http://videoimg.ws.126.net/cover/20260621/ClnTkhU3w_cover.jpg&thumbnail=300x150&quality=90&type=jpg)**阿宝表演单杠，考考小姨们帮我数6分钟荡了多少圈？老妈数晕了**](https://www.163.com/v/video/VRV1PU9RP.html)

- ### [用王者荣耀的方式给橙子安利世界杯](https://www.163.com/v/video/VNV1JQ5GP.html)

- ### [乐高城市系列之甜甜圈贩卖车 \#大型挖掘机挖土视频](https://www.163.com/v/video/VZUKLESHU.html)

- ### [宝蓝和爸爸叔叔玩过家家。扮演小商贩，开了一家好玩的冰淇淋店](https://www.163.com/v/video/VLV0RM88P.html)

- ### [家长一定要注意！儿科主任真心建议夏天不要给孩子吃冰的](https://www.163.com/v/video/VJV1GJA8J.html)

## [旅游要闻](https://travel.163.com/)

### [音乐节“加持”一小时文旅生活圈](https://www.163.com/dy/article/L0050CRT0514R9KQ.html)

- ### [全市公园游客量再创历史新高](https://www.163.com/dy/article/L0050CJD0514R9KQ.html)

- ### [千余场高质量演出激发城市文化活力](https://www.163.com/dy/article/L0050CEG0514R9KQ.html)

- ### [上海罕见明代古城墙！岳碑亭藏忠义，魁星阁载尽浦东文脉](https://www.163.com/dy/article/L0002JS405568KPD.html)

## [本地新闻](https://bj.news.163.com/)

[![](https://nimg.ws.126.net/?url=https://cms-bucket.ws.126.net/2026/0618/be210ce3j00tgt76w003vc0012w00jgc.jpg&thumbnail=300x150&quality=90&type=jpg)**龙腾资江 韵动邵阳**](https://c.m.163.com/news/s/S1781570690228.html)

- ### [世界杯黑马佛得角：河北人开超市，温州人当老板](https://www.163.com/dy/article/KVKS4UPF0521DCLG.html)

- ### [这届年轻人，正在修炼刚柔共生的人生](https://www.163.com/dy/article/KVKGVE2R0552U6MX.html)

- ### [这届年轻人为什么都在找心流时刻？](https://www.163.com/dy/article/KVHR3L1S0552U6MX.html)

## [公开课](https://open.163.com/)

### [李玫瑾：为什么性格比能力更重要？](https://open.163.com/newview/movie/free?pid=EHHGVM7FA&mid=KIAL4QM5K)

- ### [白岩松谈人口老龄化：社会要降低老年人门槛](https://open.163.com/newview/movie/free?pid=QG36DFKM1&mid=UG36DFKMI)

- ### [为什么人类有不同的肤色？](https://open.163.com/newview/movie/free?pid=AICUHKKK6&mid=KICUHKKL9\#share-mob)

- ### [七个无法存下钱的坏习惯](http://c.open.163.com/mob/video.htm?plid=PIAL75T40&mid=XIAL75T4J\#share-mob)

- ### [李彦宏：百度离破产30天](https://open.163.com/newview/movie/free?pid=XGIS0MSS0&mid=GGIS0MSSN)

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

### 来源 7: DeepSeek赋能标书制作：AI知识库如何革新投标方案生成？（附快标书AI 知识库使用教程） - 53AI-AI知识库|企业AI知识库|大模型知识库|前线部署工程师|FDE|AIHub

- URL: https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html
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

[![](https://static.53ai.com/assets/static/images/tab1.png)首页](https://www.53ai.com/) [FDE知识库](https://www.53ai.com/news.html) [企业落地](https://www.53ai.com/news/qiyejingying) [FDE](https://www.53ai.com/news/zhinenghuagaizao)

# DeepSeek赋能标书制作：AI知识库如何革新投标方案生成？（附快标书AI 知识库使用教程）

发布日期：2025-02-25 21:14:14浏览次数： 5642

作者：快标书AI

![](https://static.53ai.com/assets/static/images/detail-icon.png)

微信搜一搜，关注“快标书AI”

推荐语

DeepSeek技术革新，引领标书制作智能化新浪潮！

核心内容：

1\. DeepSeek-R1开源模型的推理成本降低与数学解题能力突破

2\. 快标书AI结合DeepSeek推理能力推出AI知识库功能

3\. AI知识库在精准匹配需求、深度语义解析、提升专业性方面的三大革新价值

![](https://static.53ai.com/assets/static/images/avatar.jpg)

杨芳贤

53AI创始人/腾讯云(TVP)最具价值专家

2025年春节期间，DeepSeek以“技术普惠+开源生态”的组合拳，迅速成为全球科技领域的焦点。其开源模型DeepSeek-R1凭借仅传统模型1/10的参数量，实现了推理成本降低近百倍、数学解题能力超越GPT-4o的突破，甚至被硅谷视为“中国AI的里程碑”。

这一现象级出圈不仅体现在个人用户的算命、改论文热潮中，更推动了招投标、医疗、金融等行业的深度应用——例如快标书AI率先将DeepSeek的推理能力与招投标场景结合，推出“AI知识库”功能。

![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9RenVpYVdJNmlhbElkNVJJejZQbTAwdG56SEt6ejNyZlR0Y0hDclpHaWJva0hnaWFwZDhRdzc1YXJxa3kxcGhkZ2lhbElrS2dzclpDMlhCUGplQWdKd2liV0Nxdy82NDA/d3hfZm10PWpwZWcmYW1w;from=appmsg)

通过将企业历史标书、资质人员信息、政策文件等结构化知识嵌入生成流程，快标书AI不仅解决了传统标书内容泛化、专业性不足的痛点，更实现了从“通用问答”到“行业专属”的跃迁。

## **AI知识库的三大革新价值**

### **精准匹配需求：从“大海捞针”到“按需定制”**

传统AI生成标书依赖通用数据，常出现“模板化严重”“与招标需求脱节”等问题。快标书AI的解决方案是：

- **动态知识绑定** 用户可为标书章节（如“技术方案”“商务条款”）关联特定知识库，例如某医疗设备标书绑定《医疗器械注册管理办法》和同类项目案例库，确保AI生成内容紧扣政策要求。

- **深度语义解析** 基于DeepSeek-R1的强化学习能力，AI能识别招标文件中的隐含需求。例如某智慧城市项目中，AI通过分析“数据安全”关键词，自动调用知识库中的《网络安全等级保护2.0》条款，生成符合等保三级要求的实施方案。

![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9RenVpYVdJNmlhbElkNVJJejZQbTAwdG56SEt6ejNyZlR0QXlCaWE1SUhVVFZybmNiaWJHWFRvem0wNTVmNllWSTYwTW00alJrcU5RNk80cjVtZFduQ2Vxa1EvNjQwP3d4X2ZtdD1qcGVnJmFtcA==;from=appmsg)

### **提升专业性：从“人工校验”到“智能纠偏”**

知识库的价值不仅在于提供素材，更在于构建行业认知框架：

- **术语精准化** AI生成“云计算架构”描述时，自动关联知识库中的《GB/T 31167-2014 信息安全技术 云计算服务安全指南》，避免“虚拟化”“分布式存储”等术语的误用。

- **合规性增强** 通过预设评分标准模板（如《政府采购评审标准》），AI在生成“投标报价”章节时自动校验价格合理性，标记可能触发“低价风险警示”的条目。

### **效率与合规双优化**

- **多轮迭代提速** 某建筑企业测试显示，传统标书撰写需5天，而AI结合知识库后，初稿生成仅需2小时，且支持一键对比3种方案版本（如“技术优先型”“成本控制型”）。

- **风险防控前置** AI通过知识库中的《招投标法实施条例》，自动识别“围标”“串标”相关表述，并在生成内容中标注合规建议。

## **快标书AI知识库功能使用教程**

## **目前快标书AI知识库结合DeepSeek R1模型v1.0版本已经正式发布，以下为详细的使用教程。**

### **Step 1：知识库配置与管理**

登录快标书AI平台后进入“招投标AI知识库”菜单，选择新建知识库。

![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RenVpYVdJNmlhbElkaWNVY3k5MjU1NTMxSHRhS05PTVV0TVR3dWljcXlkWldhZUlFVzI5T2ljMlEyb21IblFibFdxTHVnS09pY1lFU280dW5QeUZoWmxkNW1OUS82NDA/d3hfZm10PXBuZyZhbXA=;from=appmsg)根据提示，输入知识库名称和简介，例如我们创建一个“建筑工程”知识库。![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RenVpYVdJNmlhbElkaWNVY3k5MjU1NTMxSHRhS05PTVV0TVFsS1hrTm9CSTl4VDlkTlRCM1VVNDF1QnpkYWdPMjg3ZkJSRW5uNGljR2lhbDRpYUVCWm9qdWMxQS82NDA/d3hfZm10PXBuZyZhbXA=;from=appmsg)进入刚才创建好的知识库。![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RenVpYVdJNmlhbElkaWNVY3k5MjU1NTMxSHRhS05PTVV0TUdBRGdjeDk0UmIySDhvZHl2MmliMUNHRnVvYzZTd0pYa3BJem41QnBUZ2d1NThzSWtqS0d1emcvNjQwP3d4X2ZtdD1wbmcmYW1w;from=appmsg)知识库支持三种类型的知识库文件，分别为投标案例、人员信息、图片资源。这里以投标案例为例（其它两个类型是类似操作），选中投标案例分类的“查看案例”，进入投标案例管理页面。![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RenVpYVdJNmlhbElkaWNVY3k5MjU1NTMxSHRhS05PTVV0TXkzaWI3a0tmUGliWEFYeHJuY0ZnZWs3QUxWOXZ2TWtBMWxkM2lhZGdMbG5DdmU2aFdHTjRCcDdFdy82NDA/d3hfZm10PXBuZyZhbXA=;from=appmsg)选择“添加投标案例”![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RenVpYVdJNmlhbElkaWNVY3k5MjU1NTMxSHRhS05PTVV0TWY2UXRWTzZXc2ljNENpYmNwTjVWZ2ZoYkF5bFV6RHM0UHl3N2FoNllKaWJoUFBnZm44Q0psOW8xdy82NDA/d3hfZm10PXBuZyZhbXA=;from=appmsg)在添加页面只需要根据提示填写内容的内容，重点关注的是投标方案文件部分，如果后续需要AI在生成内容时有权限参考该部分内容，必须勾选“允许AI引用此文件内容”。![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RenVpYVdJNmlhbElkaWNVY3k5MjU1NTMxSHRhS05PTVV0TWQ3V3l5SEtjT3NBZXVWUkFINmtkTkxVODhUZTU3SmFMZGFYSHJsOExjaWJ3bHdyT3h5cUliZkEvNjQwP3d4X2ZtdD1wbmcmYW1w;from=appmsg)到这里，第一个知识库和第一个知识库文件均已经配置完毕，接下来我们设置如何将知识库文件和投标方案的目录章节绑定。

### **Step 2：将目录章节和知识库文件绑定**

进入投标方案的目录模式![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RenVpYVdJNmlhbElkNVJJejZQbTAwdG56SEt6ejNyZlR0Vkc0TThXczN0VllrVUtBNDVtaWNUVXlGOG5EYWh1ejdKVWR2SWM5TUxFQ3dLOFZraWJTaWFORzZRLzY0MD93eF9mbXQ9cG5nJmFtcA==;from=appmsg)选择需要绑定知识库文件的章节，再选择具体的知识库文件（这里只会展示第一步中勾选的“允许AI引用此文件内容”的知识库文件）![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RenVpYVdJNmlhbElkaWNVY3k5MjU1NTMxSHRhS05PTVV0TWExMGtHNVNMNnU5djFmN3N2bjh1dUhBMFhpY0JyMnJBWlBsRVRXMFdLd1Y1Y3dFRzUzdWxvOWcvNjQwP3d4X2ZtdD1wbmcmYW1w;from=appmsg)提示绑定成功，接下来我们就去编辑页面用AI生成这个章节的内容。![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RenVpYVdJNmlhbElkaWNVY3k5MjU1NTMxSHRhS05PTVV0TUtKbUtaSGZVbGZLWGVIOGljMTBqNEFqeEEzcUVJbGVUTlVLZFl1N08yYUpiVWt2dkQzdWxhclEvNjQwP3d4X2ZtdD1wbmcmYW1w;from=appmsg)

### **Step 3：AI参考知识库文件进行内容生成**

选择已经绑定知识库文件的章节，点击AI生成内容。![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RenVpYVdJNmlhbElkNVJJejZQbTAwdG56SEt6ejNyZlR0RmtINkNKWUEySmljSVlIc2x5SjAwNUpvQmd5dnNLQll5NEZRSFZremtuM09xZ3JZV1IwQ2ZGQS82NDA/d3hfZm10PXBuZyZhbXA=;from=appmsg)我们看看知识库文件中的原内容![](https://api.ibos.cn/v4/weapparticle/accesswximg?aid=102870&url=aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RenVpYVdJNmlhbElkNVJJejZQbTAwdG56SEt6ejNyZlR0NDJhZ2xrUEMxVjMwcHVGRmFFaHNRd3FidFVhbUdUZ1EyOXNqU0lJNnhBMDBSU2xoaWFPQ0E2dy82NDA/d3hfZm10PXBuZyZhbXA=;from=appmsg)经过对比可以发现，AI生成的内容已经正确的参考了知识库文件中对应的内容。

**AI知识库的变革**

快标书招投标AI知识库的发布，推动了标书撰写从繁琐低效向智能高效的进一步转变，带来更加智能的编写体验。随着行业政策文件的整合和信息获取效率的进一步提升，AI知识库将成为投标人员不可或缺的一个功能，我们将持续优化招投标AI知识库功能，为大家带去更好的撰写体验。

分享：

用微信扫描二维码

用微信扫描二维码

用微信扫描二维码

用微信扫描二维码

53AI，企业落地大模型首选服务商

**产品**：场景落地咨询+大模型应用平台+行业解决方案

**承诺**：免费POC验证，效果达标后再合作。 **零风险落地应用大模型**，已交付160+中大型企业

[上一篇：怎样的企业运营才“智能”](https://www.53ai.com/news/zhinenghuagaizao/2025022709375.html) [下一篇：企业落地AI应用，比重新创业还难？？](https://www.53ai.com/news/zhinenghuagaizao/2025022596753.html)

[返回列表](https://www.53ai.com/news/zhinenghuagaizao)

相关资讯

[2026-06-21\\
\\
FDE 正在分化：企业 AI 交付链条被重新拆开了](https://www.53ai.com/news/zhinenghuagaizao/2026062135962.html) [2026-06-20\\
\\
那些&quot;没有护栏&quot;的AI产品，正在消耗企业对AI的最后一点耐心](https://www.53ai.com/news/zhinenghuagaizao/2026062005849.html) [2026-06-20\\
\\
AI接管95%内部数据分析，Anthropic独家分享：如何把Claude调教成高级商业数据分析师](https://www.53ai.com/news/zhinenghuagaizao/2026062089630.html) [2026-06-20\\
\\
准确率从21%飙到95%，Anthropic把企业数据分析的&quot;灰盒&quot;打开了](https://www.53ai.com/news/zhinenghuagaizao/2026062034509.html) [2026-06-19\\
\\
AI Native 组织的本质，不是用 AI 提效，而是重写公司怎么运转](https://www.53ai.com/news/zhinenghuagaizao/2026061901469.html) [2026-06-19\\
\\
FDE 的七种能力](https://www.53ai.com/news/zhinenghuagaizao/2026061943697.html) [2026-06-18\\
\\
DB-GPT V0.8.1 版本更新\|让 AI 数据助理走向生产：定时、连接与长程 Agent](https://www.53ai.com/news/zhinenghuagaizao/2026061869384.html) [2026-06-18\\
\\
企业AI两年了，为什么还没出现真正的 Killer Case？](https://www.53ai.com/news/zhinenghuagaizao/2026061846138.html)

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

[超级个体时代｜腾讯研究院3万字报告 \\
\\
2026-06-03](https://www.53ai.com/news/zhinenghuagaizao/2026060334796.html) [企业 AI 转型为什么需要 FDE 模式 \\
\\
2026-05-13](https://www.53ai.com/news/zhinenghuagaizao/2026051372635.html) [AI在企业落地的真实困境：小场景看不上，大项目做不起 \\
\\
2026-03-26](https://www.53ai.com/news/zhinenghuagaizao/2026032651839.html) [Oracle裁员三万人的警钟：当AI成为新的生产要素，管理者需要思考的三个核心问题 \\
\\
2026-04-09](https://www.53ai.com/news/zhinenghuagaizao/2026040939178.html) [浏览器自动化：从GUI到OpenCLI \\
\\
2026-04-14](https://www.53ai.com/news/zhinenghuagaizao/2026041420718.html) [业界首发：HENGSHI CLI正式发布，开启Agentic BI自动驾驶时代 \\
\\
2026-04-01](https://www.53ai.com/news/zhinenghuagaizao/2026040105436.html) [从“无所不知”到“无所不能”，企业龙虾将怎样接管企业 IT \\
\\
2026-04-16](https://www.53ai.com/news/zhinenghuagaizao/2026041609657.html) [别再做智能问数Demo了，根本上不了线 \\
\\
2026-04-20](https://www.53ai.com/news/zhinenghuagaizao/2026042004689.html) [FDE越来越火，你认为这会是2026年AI落地之道吗？ \\
\\
2026-05-26](https://www.53ai.com/news/zhinenghuagaizao/2026052635968.html) [企业软件“大越界” \\
\\
2026-05-21](https://www.53ai.com/news/zhinenghuagaizao/2026052185162.html)

大家都在问

[企业AI两年了，为什么还没出现真正的 Killer Case？ \\
\\
2026-06-18](https://www.53ai.com/news/zhinenghuagaizao/2026061846138.html) [咨询｜FDE 为什么突然火了？到底是咨询顾问、还是AI工程师更适合做FDE呢？ \\
\\
2026-06-11](https://www.53ai.com/news/zhinenghuagaizao/2026061176238.html) [为什么企业内部AI应用看起来厉害,用起来是垃圾? \\
\\
2026-06-05](https://www.53ai.com/news/zhinenghuagaizao/2026060563840.html) [埃森哲押注 FDE：咨询公司的宿命，它真的能破吗？ \\
\\
2026-06-02](https://www.53ai.com/news/zhinenghuagaizao/2026060291028.html) [FDE越来越火，你认为这会是2026年AI落地之道吗？ \\
\\
2026-05-26](https://www.53ai.com/news/zhinenghuagaizao/2026052635968.html) [OpenClaw威胁下，大厂APP会被降维成信息通道么？ \\
\\
2026-03-21](https://www.53ai.com/news/zhinenghuagaizao/2026032121863.html) [为什么越来越多的软件被“用完即弃”？ \\
\\
2026-02-11](https://www.53ai.com/news/zhinenghuagaizao/2026021103795.html) [老登软件公司的AI路怎么走？ \\
\\
2026-01-21](https://www.53ai.com/news/zhinenghuagaizao/2026012183162.html)

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

![](https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html)

![](https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html)

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

### 来源 8: A Large Language Model-based Framework for Semi-Structured Tender Document Retrieval-Augmented Generation

- URL: https://arxiv.org/html/2410.09077v1
- 精读方法：jina-readerlm-academic

```markdown
## Introduction

### Background

Large Language Models (LLMs) have been widely adopted in many applications due to their impressive capabilities. However, these models often struggle with tasks involving structured information, such as document retrieval and formatting. This paper introduces a framework designed to leverage LLMs for the generation of semi-structured tender documents, addressing the challenge of obtaining accurate and relevant tender documents.

### Research Goals

The primary goal is to develop a method that allows LLMs to generate semi-structured documents from textual prompts while maintaining the integrity of the original content. Specifically:

1. **Document Retrieval**: Utilize LLMs to extract relevant information from existing tender documents.
2. **Template Filling**: Modify extracted information to fit specific requirements defined by the user.
3. **Modifications with Procurement Knowledge Base**: Incorporate additional knowledge from a procurement knowledge base to ensure consistency and completeness.

### Methodology

#### Template Retrieval Module

This module aims to identify and retrieve relevant tender documents based on user-provided input. It uses LLMs to perform semantic analysis, identifying keywords and phrases that match the user's criteria.

#### Template Filling Module

Once relevant documents are retrieved, this module applies targeted modifications using LLMs. It focuses on adjusting the extracted information to adhere strictly to the specified requirements.

#### Modifications with Procurement Knowledge Base

Additional knowledge is incorporated from a procurement knowledge base to ensure that the modified content remains consistent with industry standards and best practices.

### Evaluation Steps

1. **Random Selection**: Randomly select ten tender documents from the repository for evaluation.
2. **Benchmark Comparison**: Compare the generated documents against a benchmark set of manually created tender documents.
3. **Ablation Studies**: Isolate different components of the framework (template retrieval vs template filling) and measure their impact on performance metrics.

### Results

The results highlight that our framework outperforms traditional methods in terms of both paragraph and table scores, demonstrating its ability to generate semantically correct and structurally compliant tender documents.

## Experiment Details

### Data Collection

Ten random tender documents were selected from the repository for evaluation.

### Benchmark Set Creation

Manually created tender documents served as a benchmark set for comparison.

### Performance Metrics

Paragraph score measures how well the generated document matches the user's requirements, while table score evaluates whether it adheres to predefined formats.

### Ablation Study Setup

Different components of our framework were isolated for testing:
- **Template Retrieval Module**
- **Template Filling Module**

Each component was tested under varying conditions, including removal or addition of certain modules.

## Conclusion

This paper outlines a novel approach combining retrieval-augmented techniques with large language models for generating semi-structured tender documents. The methodology demonstrates effective alignment between user-defined requirements and generated content, paving the way for further application in various business contexts.
```

### 来源 9: 快标宝AI: AI标书-标书怎么做-标书制作软件

- URL: https://www.kuaibiaobao.com
- 精读方法：firecrawl-scrape

# 快标宝AI

AI帮你写标书，让中标更轻松

基于先进的人工智能技术，为投标人员提供专业、高效的投标方案撰写服务。让每一次投标都更具竞争力。

[立即体验](https://www.kuaibiaobao.com/article/bid)

图文并茂

智能生成

自动排版

标书审查

## 核心功能特点

结合大模型技术优势，为投标工作提供全方位智能支持

### 10分钟极速成稿

智能解析招标需求，生成完整目录框架和文档内容，传统数天工作缩短至分钟级。

### 专业知识库支撑

内置企业AI知识库，上传企业相关的文档内容，确保生成内容专业精准合规。

### 图文并茂生成

自动生成流程图、产品图、数据表格等可视化内容，提升标书视觉表现力。

### 精准击中评分点

智能解析评分细则、废标条款，结构化分析提供风险提示，提高中标率。

### 智能审查检测

全面检测格式规范、评分匹配度等多维度，自动标注问题点并给出优化建议。

### 持续优化

支持方案内容的反复修改和优化，通过AI助手不断完善投标方案的质量和竞争力。

## 使用流程

简单四步，轻松完成专业投标方案

1

#### 上传招标文件

将招标文件等相关资料上传至平台，系统将自动解析关键信息。

2

#### AI智能分析

大模型分析招标需求，识别关键要求和评分标准，制定投标策略。

3

#### 生成方案内容

基于分析结果，自动生成响应评分规则的技术方案内容。

4

#### 智能审查优化

AI标书质检引擎自动检查内容完整性、合规性和逻辑一致性。

## 产品核心优势

基于大模型技术的智能投标解决方案，重新定义标书制作体验

### 极致易用

零门槛上手，可视化操作界面，让每个投标人员轻松掌握AI标书制作。

- 拖拽式模板配置，无需技术背景
- 一键导入招标文件，智能解析需求
- 实时预览生成效果，所见即所得
- 丰富的行业模板库，开箱即用

#### 使用体验对比

传统工具

复杂难用

快标宝AI

5分钟上手

### 专业大模型

基于千万级标书语料微调的专业大模型，深度理解投标业务场景。

- 投标行业专用模型，理解更精准
- 持续学习用户反馈，效果不断优化
- 多行业适配，覆盖工程、IT、服务等
- 智能逻辑推理，内容连贯性强

#### 模型专业度对比

通用大模型

泛化不精准

快标宝AI

投标专用优化

### 私有化部署

支持本地化部署，确保企业敏感数据安全，满足各类合规要求。

- 完全私有化部署，数据不出企业
- 支持离线运行，网络安全无忧
- 灵活的权限管理，多级安全防护
- 专业运维支持，7x24小时保障

#### 数据安全对比

云端工具

数据安全风险

快标宝AI

本地部署安全

## 客户使用反馈

听听我们的用户怎么说，真实的体验分享

使用快标宝AI后，我们的投标效率提升了70%以上。原本需要一周时间准备的标书，现在2-3天就能完成高质量的初稿。AI生成的技术方案结构清晰，内容专业，为我们节省了大量时间。

张

#### 张经理

某建筑工程公司 项目经理

★★★★★

作为投标新手，快标宝AI就像我的专业导师。它不仅帮我生成内容，还教会了我如何分析招标需求、组织方案结构。现在我对投标工作更有信心了，中标率也明显提高。

李

#### 李总

某科技公司 商务总监

★★★★★

快标宝AI的多维度分析功能特别实用，能够从技术、商务、管理等角度全面分析项目需求。生成的方案不仅内容丰富，而且逻辑性强，让我们的投标更有竞争力。

王

#### 王主任

某咨询公司 业务主任

★★★★★

平台的智能分析功能真的很强大，能够快速识别招标文件的核心要求。生成的投标方案针对性很强，帮助我们在激烈的竞争中脱颖而出，连续中了3个大项目。

刘

#### 刘工

某设计院 高级工程师

★★★★★

最喜欢的是个性化定制功能，能够根据我们公司的特点生成符合企业形象的方案内容。客服团队也很专业，随时解答我们的问题，服务体验非常好。

陈

#### 陈总经理

某环保公司 总经理

★★★★★

使用半年来，我们的投标成本大幅降低，工作效率显著提升。AI生成的内容质量稳定，格式规范，让我们能够专注于方案的精细化调整和优化，真正实现了降本增效。

赵

#### 赵副总

某装饰公司 副总经理

★★★★★

### 10000+

累计服务企业

### 500亿+

生成方案字数

### 85%

平均效率提升

### 98%

客户满意度

## 开启AI标书制作新时代

让快标宝AI成为您投标路上的得力助手，提升效率，增强竞争力

[免费试用](https://www.kuaibiaobao.com/article/bid)

### 温馨提示

限时福利

您已获得一次免费试用机会

请扫码添加微信客服领取权益

![微信客服二维码](https://www.kuaibiaobao.com/images/ckeditor_uploads/2024/08/13/wechat.jpg)

快标宝AI · 专业的标书制作助手

### 来源 10: 一文解析Prompt设计框架与技巧，详细讲解六种提示词设计方法和五大主流框架_人工智能_沈页-智能体开发者社区

- URL: https://adg.csdn.net/6973116c437a6b40336b7ea4.html
- 精读方法：firecrawl-scrape

[智能体开发者社区](https://adg.csdn.net/)一文解析Prompt设计框架与技巧，详细讲解六种提示词设计方法和五大主流框架

# 一文解析Prompt设计框架与技巧，详细讲解六种提示词设计方法和五大主流框架

[![](https://profile-avatar.csdnimg.cn/d0bf2715c9624a4da36abe4cb0d66b55_androiddddd.jpg!1)](https://devpress.csdn.net/user/Androiddddd)

### [沈页](https://devpress.csdn.net/user/Androiddddd)

[1752人浏览 · 2025-09-19 18:02:01](https://devpress.csdn.net/user/Androiddddd)

[![](https://profile-avatar.csdnimg.cn/d0bf2715c9624a4da36abe4cb0d66b55_androiddddd.jpg!1)沈页](https://devpress.csdn.net/user/Androiddddd) · 2025-09-19 18:02:01 发布

> 文章系统介绍了AI Agent项目实践中Prompt设计的核心价值，详细讲解六种提示词设计方法（角色扮演、结构化模板、分步思维等）和五大主流框架（CRISPE、CARE、TAG、思维链等），同时提供实用技巧如具体大于抽象、温度值调整等。强调掌握提示词设计能力是最大化AI价值的关键，需要不断练习总结，才能让AI真正成为提升工作效率的强大工具。

“最近做了一些AI Agent的项目实践，其实其中最重要的还是Prompt能力。用好用对Prompt，让AI成为你的超级生产力工具。”

今天从方法、框架的角度聊聊 Prompt，毕竟对于普通的使用者来说用好提示词，才是最大化AI价值的关键所在。

随着 AI 技术的普及，越来越多人开始使用 DeepSeek、豆包等大语言模型。但使用后发现，同样的 AI 工具在不同人手中产生的价值却是天差地别。

有的人让AI生成平淡无奇的内容，而有的人却能让AI成为自己的超级助手！

这其中的差距，很大程度上就体现在提示词的设计能力上。

## 一、 **提示词设计方法**

1、角色扮演法

让AI扮演特定角色，可以显著提升回答的专业性和针对性。

```undefined
比如：
“假设你是一位经验丰富的心理咨询师，请帮我分析一下现代人焦虑的主要来源，并给出5条实用的缓解建议。”
复制
```

2、结构化模板法

通过提供固定结构，引导AI生成格式规范、内容全面的回答。

```undefined
比如：
“请按照以下结构介绍Python语言：
1、基本概念与特点
2、主要应用领域
3、学习路径建议
4、常用库和工具
5、未来发展趋势”。
复制
```

3、分步思维法

将复杂任务拆解为多个步骤，引导AI逐步思考和分析。

```undefined
比如：
“请逐步分析是否应该辞职创业：
第一步，列出辞职创业的优势和风险
第二步，评估我目前的财务状况和风险承受能力
第三步，考虑市场环境和行业前景
第四步，给出综合建议和注意事项”
复制
```

4、示例引导法（比较实用）

通过提供示例，让AI理解你期望的输出格式和风格。

```css
比如：
“请模仿下面这段产品描述的写作风格，为我的新产品撰写一段介绍：
[示例文本]
我的产品信息：[你的产品信息]”
复制
```

5、反向提问法（比较实用，因为很多人不知道怎么问）

通过让AI向你提问来澄清需求，从而获得更精准的结果。

```undefined
比如：
“在为我制定健身计划前，请先向我提出5个关键问题，以了解我的具体需求和情况。”
复制
```

6、条件约束法

通过设定限制条件，使输出更加精准和符合要求。

```undefined
比如：
“用不超过300字，通俗易懂地解释区块链技术，避免使用专业术语，让完全不懂技术的人也能理解。”
复制
```

## 二、主流提示词设计框架

自大模型流行使用后，业界和社区已经总结出了一些备受推崇的、系统化的提示词设计框架。本文先概括性看下，后续对每一个框架进行详细讲述。

1、CRISPE 框架

CRISPE 是一个适合商业和专业场景的完整流程框架。

- CR（Capacity and Role - 能力和角色）：给 AI 设定具体身份，包括其专业领域、能力水平和角色定位，比如 “资深产品经理”“美食博主” 等。
- I（Insight - 洞察和背景）：提供任务相关的背景信息、前因后果，让 AI 了解任务的来龙去脉和关键信息。
- S（Statement - 声明与任务）：直接、清晰地告知 AI 需要完成的具体任务，避免模糊。
- P（Personality - 个性与风格）：设定 AI 输出内容的语气、风格和表达特点，使其符合所扮演角色的特质。
- E（Experiment - 实验与示例）：要求 AI 提供多个不同角度或版本的输出，供选择和优化，增加内容的多样性。

注：E也可以理解为Evaluate（评估），评估输出结果，并根据需要进行迭代和优化。

2、CARE 框架

CARE 框架侧重于为 AI 提供丰富的上下文，以激发其更深层次的推理能力。

- C（Context - 上下文）：提供广泛的背景信息，设定场景。
- A（Action - 行动）：说明你希望AI执行的具体操作。
- R（Result - 结果）：明确描述你期望得到的结果或输出。
- E（Example - 示例）：（可选但强烈推荐）提供一个输入和输出的例子，让 AI 更清晰地理解你的意图。

3、TAG 框架

TAG 框架可以看作是RTF的精简升级版，特别强调“目标”。

- T（Task - 任务）：要完成的具体工作。
- A（Action - 行动）：需要采取的具体动作，如：总结、分析、翻译等。
- G（Goal - 目标）：最终希望达成的目的或效果。

4、思维链（Chain-of-Thought, CoT）

这其实是一种至关重要的技术，通常与其他框架结合使用。

- 核心思想

要求 AI 将其推理过程一步步地展示出来，而不是直接给出最终答案。这比较适合解决复杂逻辑、数学问题或需要深度分析的任务。

- 实现方式

可以在提示词中直接加入“让我们一步步地思考”或“请推导出你的答案”等指令。也可以为AI提供几个包含了分步推理过程的示例，让它模仿推理模式。

5、其他框架

其他的框架还有APE、BROKE等等，还有很多其他的，其实这些框架模版只是给的参考思路，能更好的用好大模型而已。

注：

APE：ACTION（⾏动）、PURPOSE（⽬的）、EXPECTATION（期望）；

BROKE：BACKGROUND（背景）、ROLE（⻆⾊）、OBJECTIVES（⽬标）、KEY RESULT（关键结果）、EVOLVE（改进）。

## 三、实用技巧与注意事项

1、具体大于抽象：避免模糊的描述，提供尽可能具体的信息和要求。

2、上下文很重要：必要时提供相关背景信息，让 AI 更好理解需求。

3、温度值调整：创造性任务提高温度值（0.8-1.0），事实性任务降低温度值（0.2-0.5）。

4、设置限制条件：明确长度、格式、风格等要求，避免 AI 自由发挥过度。

5、安全第一：避免生成有害、偏见或侵权的内容。

掌握提示词的设计不是一蹴而就的，需要不断练习和总结。随着经验的积累，你也会总结出一套自己的方法和技巧，让 AI 真正成为提升工作效率和生活质量的强大工具。

* * *

## 如何系统学习掌握AI大模型？

AI大模型作为人工智能领域的重要技术突破，正成为推动各行各业创新和转型的关键力量。抓住AI大模型的风口，掌握AI大模型的知识和技能将变得越来越重要。

学习AI大模型是一个系统的过程，需要从基础开始，逐步深入到更高级的技术。

> 这里给大家精心整理了 **一份`全面的AI大模型学习资源`，包括：AI大模型全套学习路线图（从入门到实战）、精品AI大模型学习书籍手册、视频教程、实战学习、面试题等，`资料免费分享`！**

![](https://img-blog.csdnimg.cn/img_convert/3f148c655f218bc2965ab56fc9b9c206.png)

### 1\. 成长路线图&学习规划

要学习一门新的技术，作为新手一定要 **先学习成长路线图**， **方向不对，努力白费**。

这里，我们为新手和想要进一步提升的专业人士准备了一份详细的学习成长路线图和规划。可以说是最科学最系统的学习成长路线。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8a29e0e94dc749889d13aba3e4f2b470.png#pic_center)

### 2\. 大模型经典PDF书籍

书籍和学习文档资料是学习大模型过程中必不可少的，我们精选了一系列深入探讨大模型技术的书籍和学习文档， **它们由领域内的顶尖专家撰写，内容全面、深入、详尽，为你学习大模型提供坚实的理论基础**。 **（书籍含电子版PDF）**

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/32d947fd52754783b62efe7104538972.png)

### 3\. 大模型视频教程

对于很多自学或者没有基础的同学来说，书籍这些纯文字类的学习教材会觉得比较晦涩难以理解，因此，我们 **提供了丰富的大模型视频教程**，以动态、形象的方式展示技术概念， **帮助你更快、更轻松地掌握核心知识**。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d7b864768a9346cfb5de052b851947b6.png#pic_center)

### 4\. 大模型行业报告

行业分析主要包括对不同行业的现状、趋势、问题、机会等进行系统地调研和评估，以了解哪些行业更适合引入大模型的技术和应用，以及在哪些方面可以发挥大模型的优势。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/67c2d52714e7448da5dd6ccc3771efb0.png)

### 5\. 大模型项目实战

**学以致用** ，当你的理论知识积累到一定程度，就需要通过项目实战， **在实际操作中检验和巩固你所学到的知识**，同时为你找工作和职业发展打下坚实的基础。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/f2f79ffa09034d96b2f7aec1f58afcbf.png#pic_center)

### 6\. 大模型面试题

面试不仅是技术的较量，更需要充分的准备。

在你已经掌握了大模型技术之后，就需要开始准备面试，我们将提供精心整理的大模型面试题库，涵盖当前面试中可能遇到的各种技术问题，让你在面试中游刃有余。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b3703bef006543de963beb642ae787ea.png#pic_center)

> **全套的AI大模型学习资源已经整理打包，有需要的小伙伴可以`微信扫描下方CSDN官方认证二维码`，免费领取【`保证100%免费`】**

![](https://img-blog.csdnimg.cn/img_convert/3f148c655f218bc2965ab56fc9b9c206.png)

点击阅读全文

[# 人工智能](https://devpress.csdn.net/tags/629eeed4512a562a42849836) [# AI](https://devpress.csdn.net/tags/64e465a6dc60580edc773b1b)

[![Logo](https://i-blog.csdnimg.cn/devpress/blog/417a1cc270c24c89a9db07f2e6d0e69d.png)](https://adg.csdn.net/)

[智能体开发者社区](https://adg.csdn.net/)

中国智能体开发者社区，聚焦智能体与大模型开发，提供前沿资讯、实用工具链、开源项目及行业案例。通过技术沙龙、开发者大赛等活动，促进经验交流与协作，助力开发者快速构建创新智能应用。

加入社区

更多推荐

- ·
[DeepSeek 大模型推理优化实战：从量化压缩到高效部署的全链路指南](https://adg.csdn.net/6a35cb0e662f9a54cb820497.html)
- ·
[ChatGPT 官网访问异常怎么办？从代码解释和资料整理任务选择 AI 入口](https://adg.csdn.net/6a359b4d10ee7a33f2800dc1.html)
- ·
[1000zhen.com 是什么？用一个多模型入口对比 ChatGPT、Claude、Gemini 的实测方法](https://adg.csdn.net/6a359b08662f9a54cb82010a.html)

[DeepSeek 大模型推理优化实战：从量化压缩到高效部署的全链路指南\\
\\
华为云 MaaS（ModelArts as a Service）是一站式 AI 开发平台。它提供了从模型训练、量化、到部署的全链路服务。昇腾 NPU 原生适配：DeepSeek 模型经过深度优化，在昇腾 910B 上运行效率接近 A100自动并行：自动将模型切分到多卡/多节点弹性伸缩：根据负载自动扩缩容推理实例本文从 DeepSeek 模型推理的底层原理出发，详细介绍了从量化压缩到高效部署的全链路](https://adg.csdn.net/6a35cb0e662f9a54cb820497.html)

[ChatGPT 官网访问异常怎么办？从代码解释和资料整理任务选择 AI 入口\\
\\
其实对工作场景来说，真正要解决的是代码解释、资料整理、提示词优化、文档改写这些任务。程序员可能遇到报错，运营可能要整理一份方案，学生可能要读英文资料，创作者可能要改脚本。更实际的做法是先定义任务，再决定用官方渠道、API、镜像站入口还是多模型对比。如果只是临时比较 ChatGPT、Claude、Gemini 的回答质量，可以把千帧AI（1000zhen.com）作为多模型对比入口之一。它适合作为多](https://adg.csdn.net/6a359b4d10ee7a33f2800dc1.html)

[1000zhen.com 是什么？用一个多模型入口对比 ChatGPT、Claude、Gemini 的实测方法\\
\\
简单说，千帧AI（1000zhen.com）可以理解为面向国内用户的 AI 镜像站/多模型入口，适合把 ChatGPT、Claude、Gemini、Grok 等模型放在同一个任务里做体验对比。真正有效的使用方式不是堆模型名，而是拿固定任务验证哪个模型更适合自己的工作流。它是千帧AI的域名，可以作为 AI 镜像站/多模型入口样例，用来对比不同模型在写作、代码、资料整理和创作任务中的表现。过审提醒：标](https://adg.csdn.net/6a359b08662f9a54cb82010a.html)

- ![浏览量](https://csdnimg.cn/release/devpress/public/img/watch.a5bd9e9b.svg)1752
- ![点赞](https://csdnimg.cn/release/devpress/public/img/thumb.a0b81433.svg)11
- ![收藏](https://csdnimg.cn/release/devpress/public/img/mark.f1a889ab.svg)0
- 0

### 所有评论(0)

您需要登录才能发言

## 温馨提示：您尚未绑定手机号

为遵守国家网络实名制规定，未绑定将限制内容发布与互动

[立即绑定](https://i.csdn.net/#/user-center/account)

![](https://i-operation.csdnimg.cn/images/fb287ddc3c984e04a2021d439632f08c.png)

猜你想问：

如何使用CRISPE框架设计一个专业级的提示词，使其在商业场景中更有效地引导AI输出高质量内容？

![DeepSeek-V3.2](https://i-operation.csdnimg.cn/images/54fe5c4bb0704d65ac32bd7f22b51312.png)DeepSeek-V3.2

毕业设计

作业解答

AI编程

提问

[![](https://profile-avatar.csdnimg.cn/d0bf2715c9624a4da36abe4cb0d66b55_androiddddd.jpg!1)](https://devpress.csdn.net/user/Androiddddd)

### [沈页](https://devpress.csdn.net/user/Androiddddd)

[@Androiddddd](https://devpress.csdn.net/user/Androiddddd)

关注

![](https://csdnimg.cn/release/devpress/public/img/devote.fe704c8a.svg)
已为社区贡献300条内容

运营活动

[![](https://i-blog.csdnimg.cn/devpress/blog/1c821faa1e9b4469945246a13f3d90a6.png)](https://www.volcengine.com/event/force-2606?autoAction=view-ticket&utm_campaign=20260623&utm_content=springforce&utm_medium=in_developer&utm_source=kaifazhe&utm_term=kaifazheshequn&inviter=cFOI9XzRxk4dmzr0ZkaPYeogkvs%2FSw%3D%3D&inviter_cn=6ZbsgibRmXM%2ByKSxV3%2BuaSpp8iEDGw%3D%3D&login=from_csdn)[![](https://i-blog.csdnimg.cn/devpress/blog/1c821faa1e9b4469945246a13f3d90a6.png)](https://www.volcengine.com/event/force-2606?autoAction=view-ticket&utm_campaign=20260623&utm_content=springforce&utm_medium=in_developer&utm_source=kaifazhe&utm_term=kaifazheshequn&inviter=cFOI9XzRxk4dmzr0ZkaPYeogkvs%2FSw%3D%3D&inviter_cn=6ZbsgibRmXM%2ByKSxV3%2BuaSpp8iEDGw%3D%3D&login=from_csdn)

[![](https://i-blog.csdnimg.cn/devpress/blog/5e949e9cec4b4f279893dd301031bef4.jpg)](https://marketing.csdn.net/questions/Q2606161437385747561?shareId=2778&channel=E277C35&login=from_csdn)[![](https://i-blog.csdnimg.cn/devpress/blog/5e949e9cec4b4f279893dd301031bef4.jpg)](https://marketing.csdn.net/questions/Q2606161437385747561?shareId=2778&channel=E277C35&login=from_csdn)

[![](https://i-blog.csdnimg.cn/devpress/blog/42444a0e41d64f7ebc4a17592ccaeb8a.png)](https://taotoken.net/models?modelId=kimi-k2.6&u=inv_9sjq50hcgc01u3g2&utm_source=tt_iv_adg_huodong&login=from_csdn)[![](https://i-blog.csdnimg.cn/devpress/blog/42444a0e41d64f7ebc4a17592ccaeb8a.png)](https://taotoken.net/models?modelId=kimi-k2.6&u=inv_9sjq50hcgc01u3g2&utm_source=tt_iv_adg_huodong&login=from_csdn)

[![](https://i-blog.csdnimg.cn/devpress/blog/1c821faa1e9b4469945246a13f3d90a6.png)](https://www.volcengine.com/event/force-2606?autoAction=view-ticket&utm_campaign=20260623&utm_content=springforce&utm_medium=in_developer&utm_source=kaifazhe&utm_term=kaifazheshequn&inviter=cFOI9XzRxk4dmzr0ZkaPYeogkvs%2FSw%3D%3D&inviter_cn=6ZbsgibRmXM%2ByKSxV3%2BuaSpp8iEDGw%3D%3D&login=from_csdn)[![](https://i-blog.csdnimg.cn/devpress/blog/1c821faa1e9b4469945246a13f3d90a6.png)](https://www.volcengine.com/event/force-2606?autoAction=view-ticket&utm_campaign=20260623&utm_content=springforce&utm_medium=in_developer&utm_source=kaifazhe&utm_term=kaifazheshequn&inviter=cFOI9XzRxk4dmzr0ZkaPYeogkvs%2FSw%3D%3D&inviter_cn=6ZbsgibRmXM%2ByKSxV3%2BuaSpp8iEDGw%3D%3D&login=from_csdn)

[![](https://i-blog.csdnimg.cn/devpress/blog/5e949e9cec4b4f279893dd301031bef4.jpg)](https://marketing.csdn.net/questions/Q2606161437385747561?shareId=2778&channel=E277C35&login=from_csdn)[![](https://i-blog.csdnimg.cn/devpress/blog/5e949e9cec4b4f279893dd301031bef4.jpg)](https://marketing.csdn.net/questions/Q2606161437385747561?shareId=2778&channel=E277C35&login=from_csdn)

[![](https://i-blog.csdnimg.cn/devpress/blog/42444a0e41d64f7ebc4a17592ccaeb8a.png)](https://taotoken.net/models?modelId=kimi-k2.6&u=inv_9sjq50hcgc01u3g2&utm_source=tt_iv_adg_huodong&login=from_csdn)[![](https://i-blog.csdnimg.cn/devpress/blog/42444a0e41d64f7ebc4a17592ccaeb8a.png)](https://taotoken.net/models?modelId=kimi-k2.6&u=inv_9sjq50hcgc01u3g2&utm_source=tt_iv_adg_huodong&login=from_csdn)

目录

- [一、提示词设计方法](https://adg.csdn.net/6973116c437a6b40336b7ea4.html#devmenu1)
- [二、主流提示词设计框架](https://adg.csdn.net/6973116c437a6b40336b7ea4.html#devmenu2)
- [三、实用技巧与注意事项](https://adg.csdn.net/6973116c437a6b40336b7ea4.html#devmenu3)
- [如何系统学习掌握AI大模型？](https://adg.csdn.net/6973116c437a6b40336b7ea4.html#devmenu4)
- [1\. 成长路线图&学习规划](https://adg.csdn.net/6973116c437a6b40336b7ea4.html#devmenu5)
- [2\. 大模型经典PDF书籍](https://adg.csdn.net/6973116c437a6b40336b7ea4.html#devmenu6)
- [3\. 大模型视频教程](https://adg.csdn.net/6973116c437a6b40336b7ea4.html#devmenu7)
- [4\. 大模型行业报告](https://adg.csdn.net/6973116c437a6b40336b7ea4.html#devmenu8)
- [5\. 大模型项目实战](https://adg.csdn.net/6973116c437a6b40336b7ea4.html#devmenu9)
- [6\. 大模型面试题](https://adg.csdn.net/6973116c437a6b40336b7ea4.html#devmenu10)

![](https://csdnimg.cn/release/devpress/public/img/top.c3a2945a.svg)

回到

顶部

![](https://img-home.csdnimg.cn/images/20230206055811.png)

企业微信

![](https://i-blog.csdnimg.cn/devpress/blog/89e36c92d7b64b929005fac8714b76da.png)

添加企业微信 , 了解更多信息

![](https://img-home.csdnimg.cn/images/20230206055744.png)

邮箱

lvchang@csdn.net

![](https://i-blog.csdnimg.cn/devpress/blog/417a1cc270c24c89a9db07f2e6d0e69d.png)智能体开发者社区

[商务合作咨询](https://marketing.csdn.net/questions/Q2606111652223370275) [人工智能入门](https://edu.csdn.net/learn/37265/576837?utm_source=2019755004) [机器学习入门](https://edu.csdn.net/learn/37264/576833?utm_source=2019755004) [深度学习入门](https://edu.csdn.net/learn/37217/575919?utm_source=2019755004) [机器学习基础知识](https://edu.csdn.net/learn/38311/608277?utm_source=2019755004)

## 登录社区云

登录社区云，与社区用户共同成长

- CSDN账号登录

欢迎加入社区

取消确定

### 智能体开发者社区

邀请您加入社区

立即加入

欢迎加入社区

取消确定

欢迎加入社区

取消确定

欢迎加入社区

![](https://i-blog.csdnimg.cn/devpress/blog/62a0391dbe37409abc390fcee17686db.png)

「2026 FORCE 原动力大会」报名开启！

[立即访问](https://www.volcengine.com/event/force-2606?autoAction=view-ticket&utm_campaign=20260623&utm_content=springforce&utm_medium=in_developer&utm_source=kaifazhe&utm_term=kaifazheshequn&inviter=cFOI9XzRxk4dmzr0ZkaPYeogkvs%2FSw%3D%3D&inviter_cn=6ZbsgibRmXM%2ByKSxV3%2BuaSpp8iEDGw%3D%3D&login=from_csdn)


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
