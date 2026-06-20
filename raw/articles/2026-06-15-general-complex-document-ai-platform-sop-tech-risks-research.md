---
title: "通用复杂文档 AI 平台标准 SOP、技术栈、坑点与难点调研"
source-type: article
generated: 2026-06-15
generated-by: wiki-research-skill
research-mode: standard
---

# 通用复杂文档 AI 平台标准 SOP、技术栈、坑点与难点调研

## 调研问题

通用复杂文档 AI 平台若要能写任意复杂文档，并完全覆盖标书专用 AI 平台的专业度和功能，标准流程应如何设计，需要哪些关键技术，落地时有哪些坑点、难点和验收指标。

## 核心结论

1. 标准流程必须从“定义文档类型”开始，而不是从“输入一句话生成全文”开始。复杂文档的生产链路应是：定义文档类型 -> 收集资料 -> 解析需求 -> 生成大纲/响应矩阵 -> 绑定资料 -> 分章节生成 -> 结构化表单/附件 -> 审查评分 -> 人工终审 -> 排版导出 -> 归档复盘。标书种子资料与投标文档 RAG 论文均支持“模板/规则/资料/分阶段生成”的流程，而不是只靠通用大模型直接生成。[来源: https://arxiv.org/html/2410.09077v1][来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html][来源: https://market.aliyun.com/products/201204006/cmgj00074082.html] 可信度：高。
2. 技术栈应按“IDP + RAG/GraphRAG + Schema/DSL + Workflow/Agent + Rule Engine + Provenance + Evaluation + Office/PDF + Security”组合，而不是只选一个大模型。Google、Azure、AWS 文档智能资料覆盖 OCR、layout、表格、字段、分类和自定义抽取；Microsoft RAG/GraphRAG 文档覆盖检索、chunk、metadata、embedding、搜索和图谱；OpenAI Structured Outputs 覆盖 JSON Schema 结构化输出；Ragas 和 TROVE 分别覆盖评测与来源追踪。[来源: https://cloud.google.com/document-ai/docs/overview][来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide][来源: https://microsoft.github.io/graphrag/][来源: https://platform.openai.com/docs/guides/structured-outputs][来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/][来源: https://arxiv.org/html/2503.15289v3] 可信度：高。
3. 标书专业能力要以插件方式保留在流程和技术栈中：读标解析、评分/废标规则、响应矩阵、企业资料绑定、偏离表、资质/人员/业绩清单、暗标、签章、格式和预打分必须是标书插件的一等能力。投标文档 RAG 论文指出采购/投标文档需要专业知识和结构控制；阿里云市场埃文 AI 标书系统、喜鹊标书 AI 和实在智能资料均强调标书快读、合规检查、预打分、偏离表、风险审查和原文溯源。[来源: https://arxiv.org/html/2410.09077v1][来源: https://market.aliyun.com/products/201204006/cmgj00074082.html][来源: https://www.xiquebiaoshu.com][来源: https://www.ai-indeed.com/encyclopedia/18040.html] 可信度：高。
4. 最大工程难点在“证据链、长文档一致性、格式交付和评测闭环”。TROVE 表明句子级来源追踪在长文档、多文档场景下仍很难，检索增强可显著提升追踪能力但关系分类仍有挑战；SOPStruct 表明长 SOP 即使用长上下文也会丢细节，分段和 DAG 更稳；docxtpl 文档显示 Word 模板生成有段落、表格、run、特殊字符、富文本和嵌入对象限制。[来源: https://arxiv.org/html/2503.15289v3][来源: https://arxiv.org/html/2504.00029][来源: https://docxtpl.readthedocs.io/en/latest/] 可信度：高。
5. 安全治理不是附属功能。复杂文档平台通常处理投标报价、资质、客户策略、合同、财务、医疗或审计资料；OWASP LLM Top 10 将 Prompt Injection、Training Data Poisoning、Sensitive Information Disclosure、Insecure Plugin Design、Excessive Agency、Overreliance 等列为核心风险。平台必须做权限、密级、审计、输出验证、资料污染治理和人工责任链。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/][来源: https://www.ai-indeed.com/encyclopedia/18040.html] 可信度：高。
6. 供应商声称的“效率提升”“中标率提升”“文本可用比例”等不能作为上线验收标准。应以自有样本建立验收指标：解析字段准确率、要求召回率、响应矩阵覆盖率、引用准确率、事实一致性、格式错误率、人工修改量、审查通过率、废标项召回率和交付周期。Microsoft RAG 指南强调逐阶段评估和记录实验结果；Ragas 提供 RAG、Agent、事实性和相关性指标。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide][来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/] 可信度：高。

## 内容整理

### 一、标准 SOP 总览

#### 0. 文档类型定义与项目立项

输入：目标文档类型、行业、客户/项目、密级、交付格式、截止时间、负责人、适用规则、是否需要标书插件。

动作：

- 选择或新建 `DocumentType`。
- 配置章节树、字段 schema、表格/附件 schema、输出模板、审查规则、权限和评测指标。
- 为高风险文档指定人工责任人，如业务负责人、技术负责人、法务/合规、排版/交付负责人。
- 对标书类项目启用标书专用规则包，包括评分点、废标项、偏离表、资质证明、暗标、签章和电子投标格式。[来源: https://market.aliyun.com/products/201204006/cmgj00074082.html]

输出：文档类型配置、项目空间、权限清单、流程计划。

关键坑点：文档类型没有 schema 会导致后续抽取、生成、审查和导出都靠 prompt 临时约定，难以复用和评测。Google Document AI 文档指出字段命名影响生成式抽取准确性，OpenAI Structured Outputs 指出 schema 可以约束模型输出结构。[来源: https://docs.cloud.google.com/document-ai/docs/label-documents][来源: https://platform.openai.com/docs/guides/structured-outputs]

#### 1. 资料收集与资产治理

输入：需求文件、历史文档、模板、合同、政策标准、案例、资质、人员、产品、图片、Excel、PPT、附件包。

动作：

- 记录来源、上传人、时间、版本、密级、有效期、适用范围。
- 对资料做去重、分类、版本化、权限绑定。
- 标记可引用、不可引用、过期、需人工确认的资料。
- 对标书场景额外收集历史中标标书、资质证书、人员证书、业绩合同、中标通知书、授权书、产品参数、施工图/架构图、商务材料。[来源: https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html][来源: https://www.xiquebiaoshu.com]

输出：资料资产清单、权限矩阵、资料质量状态。

关键坑点：资料库脏数据会污染生成结果，包括过期资质、低分历史方案、无权限客户资料、错误产品参数和旧版本政策。该风险与 OWASP 的训练数据污染、敏感信息泄露和过度信任相关。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]

#### 2. 解析与结构化抽取

输入：项目资料包和需求文件。

动作：

- OCR/IDP：抽取文本、手写体、表格、键值对、段落、标题、图片、页码、附件。
- 文档分类：判断文件类型和附件类型，并路由到不同抽取 schema。
- 字段抽取：按文档类型 schema 抽取基础信息、时间、金额、主体、范围、清单、合规条款、格式要求。
- 要求抽取：识别硬性要求、评分要求、合规要求、资料要求、格式要求、提交要求。
- 版本比对：处理主文件、补遗、澄清、修订版本的差异。

输出：结构化解析报告、字段表、要求清单、版本差异表。

技术依据：Google Document AI 支持 OCR、layout、KVP、表格、分类、拆分和自定义抽取；Azure Document Intelligence 支持 Read/Layout/预置/自定义模型和强类型字段；AWS Textract 支持表单、表格、Queries、发票/收据/ID/贷款包和异步多页处理。[来源: https://cloud.google.com/document-ai/docs/overview][来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview][来源: https://docs.aws.amazon.com/textract/latest/dg/what-is.html]

关键坑点：扫描件、复杂表格、图片化附件、页眉页脚、签章页、补遗文件和电子平台说明最容易漏读。标书种子资料显示，漏掉废标项、格式要求、签章和暗标会造成交付风险。[来源: https://www.ai-indeed.com/encyclopedia/18040.html][来源: https://cloud-help.mandao.com/docs/ai/ai-bid-document-build]

#### 3. 大纲、响应矩阵与 DAG 计划

输入：解析报告、要求清单、文档类型模板、资料资产。

动作：

- 生成文档大纲和章节树。
- 建立要求-响应矩阵：每条要求映射到章节、资料、证据、负责人、风险、状态和检查结果。
- 建立任务 DAG：章节依赖、资料依赖、人工关口、并行任务、输出物依赖。
- 对缺失字段生成追问清单，禁止模型自行补编。

输出：文档大纲、响应矩阵、任务 DAG、缺失资料清单。

技术依据：投标文档 RAG 论文使用智能标签和 Agent 追问缺失信息；SOPStruct 将复杂 SOP 分段成 DAG，节点包括 name、description、dependencies、inputs、inputs from dependencies、output、category，并用 PDDL 验证结构。[来源: https://arxiv.org/html/2410.09077v1][来源: https://arxiv.org/html/2504.00029]

关键坑点：没有响应矩阵时，生成出来的文档可能“看起来完整”，但无法证明每条要求被覆盖。没有 DAG 时，跨章节依赖、前置资料和人工确认容易丢失。该结论来自标书流程与 SOPStruct 方法的综合推断。[来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html][来源: https://arxiv.org/html/2504.00029]

#### 4. 检索与资料绑定

输入：章节任务、要求、资料资产、权限。

动作：

- 按章节检索相关资料，使用关键词、向量、混合检索、rerank。
- 对需要跨章节、跨文档关系的问题使用 GraphRAG 或图查询。
- 对有明确规则的问题使用规则引导检索。
- 对每个章节绑定允许引用的资料，排除无权限、过期、低质量和不适用资料。

输出：章节资料包、引用候选、检索审计记录。

技术依据：Microsoft RAG 设计指南要求选择 chunk 策略、metadata enrichment、embedding、vector/full-text/hybrid/manual multiple searches 并逐步评估；Microsoft GraphRAG 指出基线 RAG 在连接分散信息和整体理解大型集合/单个大文档时较弱；RuleRAG 说明规则能指导 retriever 召回逻辑支持文档并指导 generator 使用证据。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide][来源: https://microsoft.github.io/graphrag/][来源: https://arxiv.org/html/2410.22353v2]

关键坑点：只用向量 top-k 会漏掉精确条款、编号、金额、日期和否定条件；只用关键词会漏掉语义相近资料；检索资料过多会引入噪声。RuleRAG 论文也指出标准 RAG 检索可能只匹配词面而无法提供推理所需事实。[来源: https://arxiv.org/html/2410.22353v2]

#### 5. 分章节与组件生成

输入：章节任务、要求、资料包、输出 schema、模板、禁止事项。

动作：

- 按章节生成，不一次性整本生成。
- 对每章提示模型：章节目标、覆盖要求、允许引用资料、禁止编造、格式/字数、输出 schema。
- 对表格、清单、附件、图表、摘要等组件单独生成和校验。
- 用 Structured Outputs 生成响应矩阵、审查结果、字段表、风险清单等结构化数据。
- 生成时记录来源证据，无法引用时输出“缺失资料”。

输出：章节草稿、组件草稿、引用记录、缺失资料清单。

技术依据：OpenAI Structured Outputs 可使模型输出遵循 JSON Schema；投标文档 RAG 论文使用 Word 模板和智能标签填充；标书种子资料明确反对复杂项目“一键生成整本标书”，主张分章节生成和人工审核。[来源: https://platform.openai.com/docs/guides/structured-outputs][来源: https://arxiv.org/html/2410.09077v1][来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html]

关键坑点：结构化输出只保证结构，不保证事实正确。OpenAI 文档明确提醒 Structured Outputs 仍可能有内容错误，需要拆分任务、示例和处理不兼容输入。[来源: https://platform.openai.com/docs/guides/structured-outputs]

#### 6. 证据链与引用溯源

输入：章节草稿、源资料、检索结果。

动作：

- 将生成句子/段落绑定到源文档、页码、源句、字段和资料版本。
- 分类来源关系：直接引用、压缩总结、推理扩展、冲突/否定、人工输入。
- 对无证据内容标注缺资料或需人工确认。
- 支持点击跳转到原文位置或原始资料片段。

输出：句子/段落证据链、引用报告、不可溯源清单。

技术依据：TROVE 将 target sentence 追溯到 source sentences，并分类 quotation、compression、inference、others；实在智能资料强调结构化结果应支持原文溯源，便于人工确认。[来源: https://arxiv.org/html/2503.15289v3][来源: https://www.ai-indeed.com/encyclopedia/18040.html]

关键坑点：事后给全文附几个来源链接不能证明每句事实。TROVE 实验显示关系分类仍是难点，检索增强有帮助但不能完全解决。[来源: https://arxiv.org/html/2503.15289v3]

#### 7. 审查、评分与一致性检查

输入：草稿、响应矩阵、证据链、规则包、输出模板。

动作：

- 要求覆盖：每条要求是否响应，是否有证据。
- 事实一致：主体、金额、日期、人员、产品、项目、指标、报价、工期是否一致。
- 规则审查：合规、合同、格式、禁用词、行业规则、企业规则。
- 标书专项：废标项、评分点、偏离表、资质证明、暗标、签章、目录页码、电子平台格式。
- 预评分：按规则输出得分预测或质量评分，但必须标注非真实评委结果。
- 风险闭环：每条风险状态为修正、补资料、人工确认、接受风险或关闭。

输出：审查报告、评分/预评分报告、风险关闭清单、人工确认清单。

技术依据：Ragas 提供 context precision、context recall、faithfulness、response relevancy、factual correctness、tool call accuracy 等指标；阿里云市场标书系统列出预打分、技术偏离表、全维度合规检查等能力。[来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/][来源: https://market.aliyun.com/products/201204006/cmgj00074082.html]

关键坑点：预打分容易被误解为真实评审结果；供应商宣传的中标率提升和文本可用比例缺少第三方验证，必须用企业自有样本验证。[来源: https://cloud.tencent.com/developer/article/2549224][来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html]

#### 8. 人工终审与责任签发

输入：审查报告、草稿、风险清单、证据链。

动作：

- 业务负责人审目标、策略、客户名称、范围和价值主张。
- 技术负责人审技术方案、指标、可实施性和承诺边界。
- 法务/合规审合同、法规、禁止承诺、废标/合规风险。
- 财务/商务审价格、金额、付款、工期、人员和商务条款。
- 排版/交付负责人审格式、附件、目录、页码、签章、水印、元数据。

输出：终审意见、修订版、签发记录。

技术依据：标书种子资料强调 AI 是助手，不替代投标策略、真实性确认、商务决策和最终责任；OWASP 将 overreliance 列为 LLM 应用风险。[来源: https://www.ai-indeed.com/encyclopedia/18040.html][来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]

关键坑点：高风险文档若没有责任链，AI 错误会变成组织风险。

#### 9. 排版导出与交付前检查

输入：终审版草稿、输出模板、附件包。

动作：

- 套用 Word 模板、样式、目录、页码、封面、页眉页脚、表格、图表。
- 生成 PDF 和可编辑 Word。
- 检查文件名、文件大小、签章、水印、元数据、附件顺序、电子平台格式。
- 标书暗标项目清理公司名、作者、页眉页脚、水印、图片元数据。

输出：最终 Word、最终 PDF、附件包、提交检查单。

技术依据：满道云帮助文档要求生成后核对核心信息、关键模块、页码和签章位置，并支持 PDF/Word 下载；docxtpl 可从复杂 Word 模板生成 docx，但对段落、表格、run、特殊字符和富文本有约束。[来源: https://cloud-help.mandao.com/docs/ai/ai-bid-document-build][来源: https://docxtpl.readthedocs.io/en/latest/]

关键坑点：复杂 Word/PDF 交付是独立工程，不是把 Markdown 转 PDF 就结束。页眉页脚、目录、编号、表格跨页、图片、附件、签章、元数据都可能出错。

#### 10. 归档复盘与知识回流

输入：最终交付物、过程版本、审查报告、人工修改、客户/评审反馈。

动作：

- 归档最终版、证据链、响应矩阵、风险关闭清单、提交回执。
- 标注项目结果、反馈、失分点、人工修改点。
- 回流高质量章节、案例、规则、模板和错误样本。
- 更新评测集、规则包、提示词、检索配置和文档类型包。

输出：复盘报告、知识库更新项、评测样本、规则/模板版本。

技术依据：Microsoft RAG 指南强调记录超参数和评估结果并聚合展示；标书种子资料强调中标/未中标结果、评分反馈、专家意见和最终提交版本应回流知识库。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide][来源: https://raw.githubusercontent.com/FB208/OpenBidKit_Yibiao/master/README.md] 第二个 OpenBidKit 原始 README 未在本轮成功精读，仅作待验证背景。

### 二、关键技术栈

#### 1. OCR / IDP / 多模态文档解析

必须覆盖：

- OCR：打印体、手写体、扫描件、图片化 PDF。
- Layout：标题、段落、表格、列表、页眉页脚、页码、图片位置。
- Form/KVP：键值对、表单字段、勾选框。
- Tables：单表、多表、跨页表、嵌套表、行列标题。
- Classifier/Splitter：文档类型识别、附件包拆分、按类型路由。
- Query Extraction：用自然语言或字段 schema 抽取目标信息。

来源依据：Google Document AI、Azure Document Intelligence、AWS Textract 均提供相关能力描述。[来源: https://cloud.google.com/document-ai/docs/overview][来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview][来源: https://docs.aws.amazon.com/textract/latest/dg/what-is.html]

难点：

- 表格跨页、图片化表格、印章遮挡、扫描歪斜、低清晰度。
- 复杂附件包的文档类型识别与路由。
- OCR 误字会污染后续抽取和生成。
- 高风险字段需要人工复核和双人标注规范。[来源: https://docs.cloud.google.com/document-ai/docs/label-documents]

#### 2. RAG / 混合检索 / Rerank

必须覆盖：

- Chunk 策略：按章节、语义、页面、表格、附件、字段切分。
- Metadata enrichment：标题、摘要、关键词、文档类型、项目、版本、权限、有效期。
- Embedding：选择模型并评估语义相似性。
- Search：向量、全文、混合、多次搜索、手动 query decomposition。
- Rerank：按语义、规则、权限和章节任务重排。

来源依据：Microsoft RAG 指南明确列出 chunking、enrichment、embedding、search index、vector/full-text/hybrid/manual multiple searches、retrieval evaluation。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]

难点：

- 长文档 chunk 太大召回不准，太小丢上下文。
- 权限、版本、有效期必须进入检索过滤条件。
- 检索指标要按字段、章节、文档类型分别评估。
- 噪声上下文会降低生成质量，BM25 召回增加不一定提升答案质量，RuleRAG 论文也观察到检索噪声可能影响生成。[来源: https://arxiv.org/html/2410.22353v2]

#### 3. GraphRAG / 知识图谱

适用：

- 跨章节、跨文档、跨实体关系推理。
- 大型资料库整体总结。
- 需要“公司-资质-人员-业绩-产品-项目-政策-条款”关系链的场景。
- 标书中产品分类、采购清单、项目案例匹配和历史知识复用。

来源依据：Microsoft GraphRAG 从文本抽取实体、关系、关键主张，构建社区层级和摘要，并提供 Global、Local、DRIFT、Basic Search；投标文档 RAG 论文用 GraphRAG 构建采购知识图谱并用 Cypher 查询相关实体。[来源: https://microsoft.github.io/graphrag/][来源: https://arxiv.org/html/2410.09077v1]

难点：

- 图谱 schema 设计和实体消歧成本高。
- 自动抽取关系会有错误，需要人工抽样审查。
- 图谱更新、增量构建、版本回滚和权限控制复杂。
- 对简单文档过度引入 GraphRAG 会增加成本和延迟。

#### 4. Schema / DSL / 结构化输出

必须覆盖：

- 文档类型 DSL：章节、字段、资料、规则、输出模板。
- 字段 schema：类型、必填、枚举、正则、范围、来源要求。
- 任务 schema：输入、输出、依赖、人工关口、状态。
- 审查 schema：规则编号、严重等级、证据、结论、处理状态。
- 响应矩阵 schema：要求、章节、资料、证据、负责人、状态、风险。

来源依据：OpenAI Structured Outputs 说明 JSON Schema 可约束模型输出；Google Document AI 提醒字段命名影响抽取准确率。[来源: https://platform.openai.com/docs/guides/structured-outputs][来源: https://docs.cloud.google.com/document-ai/docs/label-documents]

难点：

- Schema 过度复杂会增加配置成本。
- Schema 太弱会导致后续审查无法计算。
- 结构正确不代表事实正确，必须结合证据链和规则审查。[来源: https://platform.openai.com/docs/guides/structured-outputs]

#### 5. 工作流 / Agent 编排

必须覆盖：

- 解析 Agent、检索 Agent、规划 Agent、生成 Agent、审查 Agent、排版 Agent。
- DAG：任务依赖、输入输出、人工确认、失败重试、并行任务。
- 缺资料追问：向用户或资料负责人请求补充。
- 工具调用：文档解析、检索、模板渲染、格式检查、导出。

来源依据：SOPStruct 证明复杂流程适合分段和 DAG；投标文档 RAG 论文使用 Agent 与用户交互以补齐模板参数。[来源: https://arxiv.org/html/2504.00029][来源: https://arxiv.org/html/2410.09077v1]

难点：

- Agent 过度自治会造成错误操作，OWASP 将 Excessive Agency 列为风险。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]
- 工作流必须有人工关口和审计，不应让模型直接覆盖最终文档。

#### 6. 规则引擎 / 审查引擎

必须覆盖：

- 硬规则：字段必填、格式、编号、金额一致、日期范围、签章页、附件顺序。
- 软规则：逻辑完整、语言风格、评分倾向、风险提示。
- 垂直规则：标书废标项、评分点、偏离表、暗标；合同条款；申报政策；审计证据。
- 规则引导检索：用规则改写/扩展检索，召回更支持推理的资料。

来源依据：RuleRAG 证明规则可以指导 retriever 和 generator；标书种子资料显示废标项和评分点是关键审查对象。[来源: https://arxiv.org/html/2410.22353v2][来源: https://market.aliyun.com/products/201204006/cmgj00074082.html]

难点：

- 行业规则持续维护成本高。
- 规则冲突和版本更新需要审计。
- 软规则不能伪装成法律或评审结论。

#### 7. 引用溯源 / Provenance

必须覆盖：

- 段落/句子来源：源文件、页码、源句、资料版本。
- 关系类型：引用、压缩、推理、人工输入、冲突。
- 可点击回源：PDF/Word 原文位置、高亮片段。
- 引用质量：是否唯一来源、是否过期、是否低可信、是否人工确认。

来源依据：TROVE 提出句子级来源追踪和关系分类；实在智能资料强调原文溯源便于人工确认。[来源: https://arxiv.org/html/2503.15289v3][来源: https://www.ai-indeed.com/encyclopedia/18040.html]

难点：

- 句子往往由多个来源压缩或推理而来，不能简单绑定一个 URL。
- 大模型会生成“看似有来源但实际不支持”的内容。
- 引用准确率需要专门评测集。

#### 8. 评测体系

必须覆盖：

- 解析：字段准确率、字段召回率、表格结构准确率、OCR 错误率。
- 检索：context precision、context recall、实体召回、噪声敏感性。
- 生成：faithfulness、response relevancy、factual correctness、章节完整性。
- Agent：tool call accuracy、tool call F1、agent goal accuracy。
- 文档业务：要求覆盖率、响应矩阵完整率、风险项关闭率、人工修改量、交付错误率。
- 标书专项：废标项召回率、评分点覆盖率、偏离表准确率、格式检查准确率、暗标泄露检查通过率。

来源依据：Ragas 指标覆盖 RAG、Agent、事实性、相似度和通用评分；Microsoft RAG 指南强调逐阶段评估和记录实验结果。[来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/][来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]

难点：

- 复杂文档没有唯一标准答案，很多指标需要人工或专家标注。
- 业务成功与文本相似度不等价。
- 供应商营销指标不可直接采信。

#### 9. Office / PDF 渲染与交付

必须覆盖：

- docx 模板、样式、目录、页码、页眉页脚、表格、图片、子文档。
- PDF 渲染、可搜索 PDF、签章、水印、文件大小、元数据清理。
- 附件包和电子平台格式。

来源依据：docxtpl 文档说明可用复杂 Word 模板、Jinja2 标签、表格行/列、富文本、图片、子文档和变量检查生成 docx；满道云帮助文档强调 Word/PDF 下载和页码、签章核验。[来源: https://docxtpl.readthedocs.io/en/latest/][来源: https://cloud-help.mandao.com/docs/ai/ai-bid-document-build]

难点：

- Word 内部 XML 的 run、段落、表格结构会影响模板标签。
- 特殊字符 `<`、`>`、`&` 需要转义，否则可能破坏 docx。
- PDF 与 Word 版式一致性、签章、目录和附件顺序需要端到端测试。

### 三、典型文档类型落地要点

| 文档类型 | 关键流程差异 | 必备规则包/模板包 | 主要风险 |
| --- | --- | --- | --- |
| 标书/投标文件 | 读标、响应矩阵、评分/废标、偏离表、暗标、签章、提交检查 | 标书专用规则包、评分包、废标包、偏离表包、资质包 | 废标、格式错误、资质/报价/工期不一致、数据泄露。[来源: https://market.aliyun.com/products/201204006/cmgj00074082.html] |
| 申报书 | 政策匹配、指标承诺、预算、附件证明、绩效目标 | 政策规则包、预算表、附件清单、绩效指标模板 | 政策误读、预算不合规、附件缺失。未验证 |
| 可研报告 | 建设必要性、方案、投资估算、财务、风险、合规 | 可研章节包、财务测算表、风险包 | 数据来源不清、测算错误、跨章节不一致。未验证 |
| 商业计划书 | 市场、产品、团队、商业模式、财务预测 | BP 模板、财务预测表、投资人问答 | 夸大预测、缺证据、合规披露不足。未验证 |
| 解决方案/技术方案 | 客户需求、架构、功能、实施、运维、安全、案例 | 技术方案模板、架构图组件、案例库 | 泛泛而谈、与真实能力不符、承诺过度。未验证 |
| 合同/法务文档 | 条款抽取、风险条款、主体/金额/期限一致性 | 条款库、风险规则、审批流 | 法律责任、条款冲突、AI 越权给法律结论。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview] |
| SOP/项目管理文档 | 步骤、依赖、角色、输入输出、异常分支 | DAG 模板、RACI、检查单 | 漏步骤、依赖错误、不可执行。[来源: https://arxiv.org/html/2504.00029] |
| 审计/合规报告 | 证据、发现、依据、整改、责任 | 证据链、法规规则、整改跟踪 | 证据不足、引用不可溯源、责任链断裂。[来源: https://arxiv.org/html/2503.15289v3] |

未验证说明：除标书、SOP、合同抽取和通用 IDP/RAG 技术外，其他文档类型的专用规则包需后续专题调研验证。

### 四、落地坑点清单

#### 产品与抽象坑

1. 抽象过度导致专业度下降：把标书、合同、申报书都做成“章节模板 + AI 写作”，会失去规则、审查和证据链。[来源: https://arxiv.org/html/2410.09077v1]
2. 文档类型包失控：每个客户都改一套模板，缺少版本和继承机制，会导致维护成本爆炸。未验证。
3. 功能看板漂亮但流程不闭环：能生成大纲和正文，但没有响应矩阵、审查、人工终审、导出和归档。
4. 把“预评分”当真实结果：供应商或产品容易夸大 AI 评分能力，真实评审仍需专家和历史数据验证。[来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html]

#### 数据与知识库坑

1. 知识库污染：过期、错误、低分、无权限资料进入生成。
2. 资料没有有效期和适用范围：历史案例、资质、政策可能已经作废。
3. 章节绑定缺失：模型会引用与当前章节不相关或无权限材料。
4. 多版本资料冲突：主文件、补遗、澄清、合同版本、模板版本未处理差异。

来源依据：RAG 设计需要 metadata、索引和评估；标书种子资料强调历史资料、资质、人员、法规政策、图片资源要分类授权引用。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide][来源: https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html]

#### 模型与生成坑

1. 幻觉：模型编造业绩、资质、人员、报价、承诺、法律结论。
2. 长文档上下文丢失：跨章节的金额、人员、日期、指标不一致。
3. 表格生成难：字段、行列、跨页、公式、合并单元格难以稳定。
4. 结构正确但事实错误：JSON Schema 不保证事实正确。[来源: https://platform.openai.com/docs/guides/structured-outputs]
5. 生成依赖模板但模板不适配：模板检索错了，后续内容会系统性跑偏。[来源: https://arxiv.org/html/2410.09077v1]

#### 检索与引用坑

1. 引用不可追溯：只标注来源文件，不知道哪句话支持哪句话。
2. 检索召回不足：关键条款没有进入上下文。
3. 检索噪声过多：相关但不支持结论的资料误导生成。
4. 图谱错误扩散：GraphRAG 抽取错误实体关系后，可能影响多个章节。
5. 来源关系分类难：TROVE 显示关系分类仍是难点。[来源: https://arxiv.org/html/2503.15289v3]

#### 审查与评测坑

1. 没有黄金样本：无法量化解析、检索、生成和审查效果。
2. 只测文本相似度：忽略要求覆盖率、事实一致性、格式错误和业务结果。
3. 评测集过小：无法覆盖不同文档类型、扫描质量、附件、行业规则。
4. 人工复核成本被低估：高风险文档必须保留责任链。

来源依据：Microsoft RAG 指南强调代表性测试媒体、测试查询和逐阶段评估；Ragas 提供多类指标但仍需业务指标补充。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide][来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/]

#### 安全与合规坑

1. 提示注入：需求文件或资料中夹带恶意指令。
2. 敏感信息泄露：模型、日志、向量库、导出文件、协作者权限都可能泄露。
3. 插件权限过大：Agent 自动调用导出、发送、删除、审批等工具。
4. 过度信任：人工跳过审查，直接提交 AI 生成文件。
5. 审计缺失：无法追踪是谁生成、谁确认、引用了哪些资料。

来源依据：OWASP LLM Top 10 覆盖 Prompt Injection、Insecure Output Handling、Training Data Poisoning、Sensitive Information Disclosure、Insecure Plugin Design、Excessive Agency、Overreliance 等风险。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]

#### 交付格式坑

1. Word 样式丢失：run、段落、表格标签位置错误导致模板渲染失败。
2. 特殊字符破坏 XML：`<`、`>`、`&` 未转义会造成 docx 问题。[来源: https://docxtpl.readthedocs.io/en/latest/]
3. 目录页码、附件顺序、签章位置错误。
4. PDF 与 Word 不一致。
5. 暗标泄露：作者、公司名、水印、图片元数据、页眉页脚泄露身份。[来源: https://cloud-help.mandao.com/docs/ai/ai-bid-document-build]

### 五、验收指标建议

#### 文档解析指标

- OCR 字符准确率：按样本页抽样。
- 字段抽取准确率/召回率：按字段 schema 和人工标注对比。
- 表格结构准确率：行列、表头、合并单元格、跨页表。
- 文档分类准确率：文件类型、附件类型、版本类型。

来源依据：Google/Azure/AWS 均将 OCR、layout、表格、字段和分类作为文档智能基础能力。[来源: https://cloud.google.com/document-ai/docs/overview][来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview][来源: https://docs.aws.amazon.com/textract/latest/dg/what-is.html]

#### 检索与引用指标

- Context Precision / Context Recall。
- 来源句追踪 Precision / Recall。
- 引用支持率：生成事实是否被来源支持。
- 无证据内容比例。
- 过期/无权限资料引用次数。

来源依据：Ragas 指标和 TROVE 指标。[来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/][来源: https://arxiv.org/html/2503.15289v3]

#### 生成质量指标

- 要求覆盖率。
- 响应矩阵完整率。
- 章节完整性。
- 事实一致性。
- 人工修改量。
- 缺资料识别准确率。

来源依据：标书响应矩阵流程、SOPStruct 完整性评估和 RAG 评测方法综合推导。[来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html][来源: https://arxiv.org/html/2504.00029][来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]

#### 审查与交付指标

- 规则命中准确率。
- 严重风险召回率。
- 格式错误率。
- Word/PDF 导出成功率。
- 提交前检查通过率。
- 标书专项：废标项召回率、评分点覆盖率、偏离表准确率、暗标检查通过率。

来源依据：标书种子资料中的废标项、评分点、格式、签章、暗标等风险与 Ragas 评测指标综合。[来源: https://market.aliyun.com/products/201204006/cmgj00074082.html][来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/]

#### 安全与治理指标

- 越权引用拦截率。
- 敏感信息输出拦截率。
- 提示注入测试通过率。
- 审计链完整率。
- 人工终审覆盖率。

来源依据：OWASP LLM Top 10 与高价值文档安全要求。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/][来源: https://www.ai-indeed.com/encyclopedia/18040.html]

## 推荐工作流

### MVP 到正式上线流程

1. 选择一个高价值文档类型作为首个 POC，建议从标书或申报书开始，因为它们有明确要求、资料、格式和审查规则。标书场景已有更充分来源支撑。[来源: https://arxiv.org/html/2410.09077v1]
2. 收集 20-50 个历史样本，至少覆盖成功稿、失败稿、扫描件、附件包、复杂表格和不同模板。样本量为经验建议，未验证。
3. 建立文档类型 schema、章节树、响应矩阵 schema、审查规则和输出模板。[来源: https://docs.cloud.google.com/document-ai/docs/label-documents]
4. 做解析 POC：字段抽取、要求抽取、表格抽取和附件分类先达标，再做生成。[来源: https://cloud.google.com/document-ai/docs/overview]
5. 做 RAG POC：比较 chunk、metadata、embedding、关键词/向量/混合检索、rerank，记录结果。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]
6. 做章节生成 POC：只生成 3-5 个关键章节，要求全部带证据链和缺资料清单。[来源: https://platform.openai.com/docs/guides/structured-outputs]
7. 做审查 POC：先实现硬规则和高风险规则，再做软评分。[来源: https://arxiv.org/html/2410.22353v2]
8. 做 Word/PDF 交付 POC：选择真实模板，测试目录、页码、表格、图片、附件和特殊字符。[来源: https://docxtpl.readthedocs.io/en/latest/]
9. 组织人工盲审：让业务/技术/法务/排版人员按真实流程评价，不只看 AI 自评。该步骤为治理建议，未验证。
10. 建立评测基线：解析、检索、引用、生成、审查、交付、安全六类指标全部留档。[来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/]
11. 小范围试运行：限制项目、用户、模型、资料权限和导出权限。
12. 复盘迭代：把人工修改、风险、失败样本和最终交付结果回流规则包、模板包和评测集。

### 标书插件专用流程

1. 读标建档：解析招标文件、公告、附件、补遗、澄清、电子平台说明。[来源: https://www.ai-indeed.com/encyclopedia/18040.html]
2. Bid/No-Bid：资格、评分、风险、报价空间、交付能力人工判断。
3. 响应矩阵：评分点、废标项、格式要求、提交要求映射到章节和资料。[来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html]
4. 资料绑定：历史标书、资质、人员、业绩、产品、案例、图片、法规按章节授权。[来源: https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html]
5. 分章节生成：技术、商务、服务、施工、实施、售后等章节逐个生成。
6. 表单附件：技术偏离表、商务偏离表、指标响应证明、资质证明清单、人员/业绩表。[来源: https://market.aliyun.com/products/201204006/cmgj00074082.html]
7. 合规检查：废标、评分点、格式、签章、暗标、报价/工期/人员一致性。
8. 人工终审：经营、技术、法务、商务、排版多角色确认。
9. 导出提交：Word/PDF、签章、加密、附件、电子平台检查。
10. 归档复盘：中标/未中标、评分反馈、专家意见、修改记录回流。

## 适用场景

- 有稳定重复流程、结构复杂、证据要求高、格式正式、需要多人审查的文档生产。
- 有历史资料、模板、专家规则和可评测样本的组织。
- 高价值文档，如标书、申报书、合同、解决方案、可研、审计/合规报告、医疗/工程/政府采购文档。
- 需要私有资料和专业规则参与生成，而非只写通用语言。
- 愿意做资料治理、评测集、人工终审和持续规则维护的团队。

以上适用性为多源综合结论，技术基础来自 IDP/RAG/GraphRAG/Structured Outputs/评测/安全来源，垂直业务细节需按文档类型验证。[来源: https://cloud.google.com/document-ai/docs/overview][来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide][来源: https://microsoft.github.io/graphrag/][来源: https://platform.openai.com/docs/guides/structured-outputs]

## 不适用场景

- 一次性短文、低风险文案、没有正式格式和证据链要求的内容。
- 企业没有可靠资料，也没有人工确认机制，却希望 AI 编造完整正式文件。
- 法律、医疗、投标、审计等高风险文档，但组织不允许人工终审或责任签发。
- 资料高度涉密但无法私有化部署、权限隔离或审计。
- 没有样本、没有评测、没有规则维护预算，只想采购“全自动写文档”按钮。

这些结论为产品落地判断，部分属于综合推断；高风险边界由 OWASP 安全风险和标书种子资料支撑。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/][来源: https://www.ai-indeed.com/encyclopedia/18040.html]

## 风险与约束

### 技术约束

- OCR/IDP 对扫描质量、表格复杂度、语言和版面敏感。[来源: https://docs.aws.amazon.com/textract/latest/dg/what-is.html]
- RAG 需要大量实验调参，chunk、metadata、embedding、检索方式和评测都会影响结果。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]
- GraphRAG 更适合复杂关系，不适合所有文档都默认开启；构图成本和错误维护需验证。[来源: https://microsoft.github.io/graphrag/]
- Structured Outputs 只保证结构，不保证事实正确。[来源: https://platform.openai.com/docs/guides/structured-outputs]
- Word/PDF 交付涉及复杂模板和渲染，不是 LLM 能单独解决。[来源: https://docxtpl.readthedocs.io/en/latest/]

### 业务约束

- 标书、合同、审计、医疗等高风险文档必须保留人工终审和责任链。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]
- 专业规则包需要持续维护，政策、法规、电子平台格式、企业资质都会变化。
- 供应商宣传指标不可直接采信，应以自有 POC 和历史项目复盘验证。[来源: https://cloud.tencent.com/developer/article/2549224][来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html]

### 安全约束

- 必须处理提示注入、敏感信息泄露、训练/知识库污染、插件权限、过度代理和过度信任。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]
- 涉密文档要明确模型、向量库、日志、缓存、导出文件是否出域。
- 审计日志要覆盖上传、解析、检索、生成、修改、审查、导出和权限变更。

## 信源质量门控记录

### 门控规则

- A 级：官方文档、学术论文、权威安全组织、云厂商正式文档，可作为核心事实依据。
- B 级：工具文档、厂商/产品页面、本地已完成调研报告，可作为实践依据，但商业效果需验证。
- C 级：社区文章、营销文章、SEO 内容，仅作背景。
- D 级：低相关、重复、抓取失败、无法访问，不进入核心结论。
- C/D 级来源不得单独支撑核心结论。
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`。

### 保留信源

1. [Tender Document RAG](https://arxiv.org/html/2410.09077v1)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：标书/采购文档生成的学术框架，覆盖模板检索、智能标签、GraphRAG、Word 模板和实验。
   - 后续处理：进入 SOP 与标书插件依据。
2. [SOPStruct](https://arxiv.org/html/2504.00029)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：复杂 SOP 分段、DAG 和 PDDL 评估方法。
   - 后续处理：进入工作流编排依据。
3. [Microsoft RAG solution design guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：RAG 全流程设计和评测官方指南。
   - 后续处理：进入 RAG 技术栈和验收指标依据。
4. [Microsoft GraphRAG documentation](https://microsoft.github.io/graphrag/)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：GraphRAG 官方文档，覆盖图谱、社区摘要和查询模式。
   - 后续处理：进入 GraphRAG 技术栈依据。
5. [Google Document AI overview](https://cloud.google.com/document-ai/docs/overview)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：OCR、layout、KVP、表格、分类、拆分、自定义抽取。
   - 后续处理：进入 IDP 技术栈依据。
6. [Azure Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：Read/Layout/预置/自定义模型、强类型字段、文档分类。
   - 后续处理：进入 IDP 技术栈依据。
7. [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：表单、表格、Queries、手写体、多页异步处理。
   - 后续处理：进入 OCR/IDP 技术栈依据。
8. [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：JSON Schema 结构化输出与限制。
   - 后续处理：进入 Schema/结构化输出依据。
9. [RuleRAG](https://arxiv.org/html/2410.22353v2)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：规则引导检索与生成。
   - 后续处理：进入规则引擎依据。
10. [TROVE](https://arxiv.org/html/2503.15289v3)
    - 工具：WebFetch
    - 来源等级：A
    - 入库映射：`source-quality: high`
    - 保留原因：句子级来源追踪和关系分类。
    - 后续处理：进入 provenance 依据。
11. [Ragas metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)
    - 工具：WebFetch
    - 来源等级：B
    - 入库映射：`source-quality: high`
    - 保留原因：RAG、Agent、事实性和相关性评测指标。
    - 后续处理：进入评测体系依据。
12. [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
    - 工具：WebFetch
    - 来源等级：A
    - 入库映射：`source-quality: high`
    - 保留原因：LLM 应用安全风险权威框架。
    - 后续处理：进入安全治理依据。
13. [python-docx-template](https://docxtpl.readthedocs.io/en/latest/)
    - 工具：WebFetch
    - 来源等级：B
    - 入库映射：`source-quality: high`
    - 保留原因：Word 模板生成实践和限制。
    - 后续处理：进入 Office 交付依据。
14. [国内 AI 标书助手能力、坑点与标准 SOP 调研](raw/articles/2026-06-15-ai-bid-document-assistant-research.md)
    - 工具：ReadFile
    - 来源等级：B
    - 入库映射：`source-quality: high`
    - 保留原因：本仓库种子资料，提供标书专用能力、SOP、坑点和来源门控。
    - 后续处理：作为标书基线。

### 剔除信源

1. [DocScope](https://arxiv.org/html/2605.08888v1)
   - 工具：WebFetch
   - 来源等级：A
   - 剔除原因：读取超时，未进入核心结论。
2. [OpenReview SCHEMARAG PDF](https://openreview.net/pdf?id=VjtMhU3zWn)
   - 工具：four_tool_research.py
   - 来源等级：A
   - 剔除原因：连接中断，未二次精读。
3. [知乎 GraphRAG 文章](https://zhuanlan.zhihu.com/p/1928982650628084885)
   - 工具：four_tool_research.py
   - 来源等级：C
   - 剔除原因：已有 Microsoft GraphRAG 官方文档替代。
4. [GraphRAG 中文教程站](https://graphragcn.com)
   - 工具：four_tool_research.py
   - 来源等级：C
   - 剔除原因：非一手来源。
5. [火眼审阅官网](https://firesee.fagougou.com)
   - 工具：four_tool_research.py
   - 来源等级：C
   - 剔除原因：精读失败，且不作为核心依据。
6. [金现代智能文档处理平台](https://idp.jxdinfo.com)
   - 工具：four_tool_research.py
   - 来源等级：C
   - 剔除原因：精读失败，且不作为核心依据。

## 来源与可信度

| 来源 | 类型 | 可信度 | 主要支撑内容 |
| --- | --- | --- | --- |
| Tender Document RAG | 学术论文 | 高 | 标书/采购文档 RAG、模板、智能标签、知识图谱 |
| SOPStruct | 学术论文 | 高 | SOP 分段、DAG、依赖、PDDL 评估 |
| Microsoft RAG guide | 官方架构文档 | 高 | RAG 数据管线、检索策略、逐阶段评测 |
| Microsoft GraphRAG | 官方项目文档 | 高 | 图谱抽取、社区摘要、查询模式 |
| Google Document AI | 官方文档 | 高 | OCR、layout、KVP、表格、分类、拆分 |
| Azure Document Intelligence | 官方文档 | 高 | Read/Layout/预置/自定义模型、强类型字段 |
| Amazon Textract | 官方文档 | 高 | 文本、手写体、表单、表格、Queries |
| OpenAI Structured Outputs | 官方文档 | 高 | JSON Schema 输出与限制 |
| RuleRAG | 学术论文 | 高 | 规则引导 RAG |
| TROVE | 学术论文 | 高 | 来源追踪与关系分类 |
| Ragas | 工具文档 | 中到高 | RAG/Agent/事实性评测指标 |
| OWASP LLM Top 10 | 安全项目 | 高 | LLM 应用安全风险 |
| docxtpl | 工具文档 | 中到高 | Word 模板生成与限制 |
| 标书种子报告 | 本地 raw | 高 | 标书基线、SOP、坑点 |

## 对于可信度较高的来源逐来源总结

### 1. Tender Document RAG

正文内容：论文指出采购文档复杂且需满足法律、技术和利益相关方需求，基础 LLM 缺少采购专业知识。框架先检索相似历史模板，再用记忆网络验证检索文档、政策和新信息一致性，最后用采购知识库和 GraphRAG 修改文档。系统用 Word 模板、智能标签、缺失信息 Agent、PageOffice/python-docx 修改段落和表格。[来源: https://arxiv.org/html/2410.09077v1]

可用事实：专业复杂文档应模板化、结构化、检索增强、缺资料追问和知识库修订。

局限：实验集中在医疗采购文档，通用化需验证。

适合入库知识点：标书 RAG 框架、智能标签、模板检索、采购知识图谱。

### 2. SOPStruct

正文内容：论文将复杂 SOP 转成 DAG，先分段，再生成节点和依赖，每个节点有 name、description、dependencies、inputs、inputs from dependencies、output、category；用 PDDL 验证图连通、依赖、输入输出和目标状态。论文指出直接处理长 SOP 会丢细节，分段可避免遗漏。[来源: https://arxiv.org/html/2504.00029]

可用事实：复杂文档流程应以 DAG 管理任务、依赖、输入输出和人工关口。

局限：方法针对 SOP 结构化，不直接生成正式文档。

适合入库知识点：DAG 工作流、SOP 结构化、PDDL 验证。

### 3. Microsoft RAG guide

正文内容：文档把 RAG 分为应用流和数据管线。数据管线包括 chunk、metadata enrich、embed、persist；设计过程要准备代表性测试媒体和查询，选择 chunk、embedding、索引、向量/全文/混合检索，并评估每一步和端到端效果。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]

可用事实：平台上线必须有检索实验和评测闭环。

局限：不含垂直文档规则。

适合入库知识点：RAG 数据管线、RAG 实验设计。

### 4. Microsoft GraphRAG

正文内容：GraphRAG 从原始文本抽取知识图谱，构建社区层级并生成社区摘要；相比 baseline RAG，它更适合需要连接分散信息和整体理解大型集合/长文档的问题；查询模式包括 Global、Local、DRIFT、Basic。[来源: https://microsoft.github.io/graphrag/]

可用事实：跨章节/跨文档关系和整体理解应考虑 GraphRAG。

局限：构图成本和质量需验证。

适合入库知识点：GraphRAG 查询模式、知识图谱增强检索。

### 5. Google Document AI / Azure Document Intelligence / Amazon Textract

正文内容：三类官方文档共同说明 IDP 平台通常包括 OCR、layout、表格、键值对、字段、分类、拆分、自定义抽取、强类型字段、Queries、预置模型和多页处理。[来源: https://cloud.google.com/document-ai/docs/overview][来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview][来源: https://docs.aws.amazon.com/textract/latest/dg/what-is.html]

可用事实：复杂文档平台底层必须有文档智能解析层。

局限：云服务能力和自建实现有差异。

适合入库知识点：IDP、文档解析、表格抽取、文档分类。

### 6. OpenAI Structured Outputs

正文内容：Structured Outputs 使模型输出遵循 JSON Schema，区别于只保证 JSON 有效的 JSON mode；文档也提醒结构化输出仍可能有内容错误，需要拆任务、示例和处理不兼容输入。[来源: https://platform.openai.com/docs/guides/structured-outputs]

可用事实：响应矩阵、审查结果、字段表、任务计划都应使用 schema 输出，但不能替代事实检查。

局限：模型和 API 能力会变化，需看实际供应商。

适合入库知识点：结构化输出、Schema 校验。

### 7. RuleRAG

正文内容：RuleRAG 指出标准 RAG 检索可能只匹配关键词，不能保证召回支持推理；规则能给检索方向和生成归因机制。实验显示规则引导检索和生成可显著提升 R@10、EM 和 T-F1。[来源: https://arxiv.org/html/2410.22353v2]

可用事实：规则包应前置参与检索和生成，而不是只做事后检查。

局限：论文任务是 QA，迁移到文档生成需验证。

适合入库知识点：规则引导检索、规则引导生成。

### 8. TROVE

正文内容：TROVE 要求把目标句追踪到源句，并分类 quotation、compression、inference、others；覆盖长文档、多文档、中英文场景。实验表明检索增强普遍优于直接提示，但关系分类仍有挑战。[来源: https://arxiv.org/html/2503.15289v3]

可用事实：复杂文档平台要做句子级来源链，而不是粗粒度参考文献列表。

局限：benchmark 不是生产系统。

适合入库知识点：句子级 provenance、引用评测。

### 9. Ragas

正文内容：Ragas 提供 RAG 指标、Agent 指标、自然语言比较和通用评分指标，如 context precision、context recall、faithfulness、response relevancy、tool call accuracy、factual correctness。[来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/]

可用事实：平台应把评测指标产品化为运营能力。

局限：指标需要结合业务指标。

适合入库知识点：RAG 评测、Agent 评测。

### 10. OWASP LLM Top 10

正文内容：OWASP 列出 LLM 应用核心风险，包括 Prompt Injection、Insecure Output Handling、Training Data Poisoning、Sensitive Information Disclosure、Insecure Plugin Design、Excessive Agency、Overreliance 等。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]

可用事实：复杂文档平台必须有安全治理层。

局限：安全框架不提供具体产品实现。

适合入库知识点：LLM 应用安全、提示注入、敏感信息泄露。

### 11. python-docx-template

正文内容：docxtpl 使用 python-docx 和 Jinja2，在 Word 模板中插入标签生成 docx，支持段落、表格行/列、富文本、图片、子文档等；也有标签不能跨 run/段落、特殊字符需要转义、富文本过滤限制等注意事项。[来源: https://docxtpl.readthedocs.io/en/latest/]

可用事实：Office 交付需要模板引擎和格式工程。

局限：不覆盖全部 PDF、签章和电子平台需求。

适合入库知识点：Word 模板生成、docx 渲染坑点。

## 跨源矛盾检测结论

### 检测范围

- 已精读来源数量：13 个核心来源，加 1 篇本地标书种子报告。
- 检测对象：核心数字、日期、功能描述、因果判断、市场/公司事实。
- 检测时间：2026-06-15。

### 检测结果

结论：未发现会推翻 SOP 和技术栈建议的实质矛盾；发现以下需要保留边界的差异。

1. 一键生成 vs 分阶段生成：轻量产品文档会宣传快速生成，标书实战资料和学术论文更强调模板、检索、分章节和人工审核。本文采用分阶段流程作为高风险复杂文档标准，允许一键生成作为低风险初稿入口。[来源: https://cloud-help.mandao.com/docs/ai/ai-bid-document-build][来源: https://arxiv.org/html/2410.09077v1][来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html]
2. RAG、GraphRAG、RuleRAG 的关系：Microsoft RAG 指南强调检索管线实验；GraphRAG 强调图结构；RuleRAG 强调规则。三者不是互斥方案，应按任务复杂度组合。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide][来源: https://microsoft.github.io/graphrag/][来源: https://arxiv.org/html/2410.22353v2]
3. 结构化输出和审查的边界：Structured Outputs 解决结构约束，Ragas/TROVE 解决评测和来源追踪，两者互补。本文没有把 schema 当事实校验。[来源: https://platform.openai.com/docs/guides/structured-outputs][来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/][来源: https://arxiv.org/html/2503.15289v3]
4. 定量效果差异：论文中的实验数字、工具指标和供应商宣传数字不可横向比较。本文只引用论文数字作为论文内实验结果，不将供应商营销数字作为平台效果承诺。[来源: https://arxiv.org/html/2410.09077v1][来源: https://arxiv.org/html/2410.22353v2][来源: https://cloud.tencent.com/developer/article/2549224]

## 矛盾与待验证问题

1. 本报告提出的通用 SOP 是综合设计，不是任何单一来源的完整标准，需要用至少 2-3 类文档 POC 验证。
2. 申报书、可研报告、商业计划书、审计报告、医疗/工程文档的专用规则包尚未逐类调研；当前仅给出通用落地要点。
3. 标书插件的废标项、暗标、签章、电子平台格式需按地区、行业、采购平台继续细化。
4. GraphRAG、RuleRAG、TROVE 在生产级文档生成中的成本、延迟和准确率需工程验证。
5. Word/PDF 导出需结合具体模板引擎、Office 兼容性、PDF 渲染器、签章工具和电子平台测试。
6. 安全治理需确认部署模式、模型供应商、日志、向量库、缓存和备份是否满足企业密级要求。
7. 供应商宣称的效率、中标率、文本可用比例需用企业自有历史项目做盲测验证。

## 原始证据摘录

> “The generation of tender documents typically involves a three-step process: ... retrieval-augmentation module ... memory network ... procurement project knowledge base.”[来源: https://arxiv.org/html/2410.09077v1]

> “We use Word templates base on historical tender documents with smart tags to generate information.”[来源: https://arxiv.org/html/2410.09077v1]

> “SOPStruct comprises of three primary phases: SOP Segmentation, SOP Structure Generation and Evaluation.”[来源: https://arxiv.org/html/2504.00029]

> “Without segmentation, directly generating a structured representation leads to the loss of fine-grained details.”[来源: https://arxiv.org/html/2504.00029]

> “The data pipeline processes each media file individually by completing the following steps: Chunking, Enrich chunks, Embed chunks, Persist chunks.”[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]

> “GraphRAG is a structured, hierarchical approach to Retrieval Augmented Generation (RAG), as opposed to naive semantic-search approaches using plain text snippets.”[来源: https://microsoft.github.io/graphrag/]

> “Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied JSON Schema.”[来源: https://platform.openai.com/docs/guides/structured-outputs]

> “Retrieval is essential. Every model benefits significantly from retrieval...”[来源: https://arxiv.org/html/2503.15289v3]

> “Context Precision, Context Recall, Context Entities Recall, Noise Sensitivity, Response Relevancy, Faithfulness.”[来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/]

> “Prompt Injection... Sensitive Information Disclosure... Excessive Agency... Overreliance.”[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]

> “The idea is to begin to create an example of the document you want to generate with microsoft word, it can be as complex as you want... insert jinja2-like tags directly in the document.”[来源: https://docxtpl.readthedocs.io/en/latest/]
