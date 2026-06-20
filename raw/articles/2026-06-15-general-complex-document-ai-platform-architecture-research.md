---
title: "通用复杂文档 AI 平台能力抽象与产品架构调研"
source-type: article
generated: 2026-06-15
generated-by: wiki-research-skill
research-mode: standard
---

# 通用复杂文档 AI 平台能力抽象与产品架构调研

## 调研问题

如果把“AI 标书助手”扩展为通用的、可写任意复杂文档的 AI 平台，同时必须完全覆盖标书专用 AI 平台的专业度和功能，需要如何抽象功能、如何设计产品架构、需要完成哪些能力，并且如何避免通用化稀释垂直专业能力。

## 核心结论

1. 通用复杂文档 AI 平台不应抽象成“万能写作助手”，而应抽象成“文档类型配置 + 资料资产 + 需求解析 + 规划编排 + 分章节生成 + 规则审查 + 证据溯源 + 排版交付”的文档工厂。标书种子资料显示，成熟标书助手的核心是读标解析、响应矩阵、企业知识库、分章节生成、合规审查和 Word/PDF 输出；Google、Azure、AWS 文档智能资料也把文档处理拆成 OCR、版面/表格/键值对/字段抽取、分类、结构化输出和下游集成。[来源: https://www.xiquebiaoshu.com][来源: https://market.aliyun.com/products/201204006/cmgj00074082.html][来源: https://cloud.google.com/document-ai/docs/overview][来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview][来源: https://docs.aws.amazon.com/textract/latest/dg/what-is.html] 可信度：高。
2. “文档类型 schema”是通用平台的根抽象：每类文档都应配置章节树、字段 schema、资料类型、要求-响应矩阵、审查规则、输出模板和角色权限，而不是只给大模型一个长提示词。Google Document AI 明确指出字段命名会影响生成式抽取准确率，建议字段名使用文档中相同语言且避免缩写；OpenAI Structured Outputs 说明 JSON Schema 可以约束模型输出结构并减少缺字段、非法枚举等问题。[来源: https://docs.cloud.google.com/document-ai/docs/label-documents][来源: https://platform.openai.com/docs/guides/structured-outputs] 可信度：高。
3. 要覆盖标书专业度，平台必须保留“标书专用插件/规则包/模板包/评审包”，而不是把标书做成普通文档类型的一套弱模板。投标文档 RAG 论文指出政府采购文档相比普通文档更要求结构、风格、用户需求和政策匹配，基础 LLM 缺少采购专业知识；种子报告中的产品资料也显示标书场景需要废标项、评分点、偏离表、资质/人员/业绩清单、暗标和签章格式等专用能力。[来源: https://arxiv.org/html/2410.09077v1][来源: https://market.aliyun.com/products/201204006/cmgj00074082.html][来源: https://www.ai-indeed.com/encyclopedia/18040.html][来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html] 可信度：高。
4. 通用平台的知识/资料资产层必须从“上传文件”升级为“可治理资产”：支持文档分类、字段抽取、版本、权限、有效期、来源证据、章节绑定和引用授权。RAG 方案设计需要对测试语料、chunk、元数据、embedding、索引、向量/全文/混合检索和评测进行结构化实验；标书种子资料也强调知识库应包含历史标书、资质、人员、案例、产品资料、法规政策和图片资源，并按章节授权引用。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide][来源: https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html][来源: https://www.xiquebiaoshu.com] 可信度：高。
5. 对复杂长文档，向量 RAG 只是底座之一；需要混合检索、重排、GraphRAG、规则引导检索和细粒度 provenance。Microsoft GraphRAG 文档指出基线 RAG 在需要“连接分散信息”和“整体理解大型集合或单个大文档”时表现较差；GraphRAG 通过从文本抽取实体、关系、关键主张、社区层级和摘要来支持全局/局部查询。RuleRAG 与 TROVE 论文进一步表明，规则能给检索和生成提供归因机制，检索增强能显著提升句子级来源追踪表现。[来源: https://microsoft.github.io/graphrag/][来源: https://arxiv.org/html/2410.22353v2][来源: https://arxiv.org/html/2503.15289v3] 可信度：高。
6. 平台的最终竞争力不是“能生成多长”，而是“能证明每个要求被响应、每个事实有来源、每个风险被审查、每个输出可提交”。TROVE 将来源追踪细化到目标句与源句之间的 quotation、compression、inference 等关系；Ragas 列出 RAG 评测中的 context precision、context recall、faithfulness、response relevancy 等指标；这些都说明复杂文档平台要把证据链和评测做成一等能力。[来源: https://arxiv.org/html/2503.15289v3][来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/] 可信度：高。

## 内容整理

### 一、从“标书助手”抽象到“复杂文档工厂”

#### 1. 标书助手的需求基线

种子资料中的标书专用 AI 平台不是普通写作工具，而是垂直生产系统：先解析招标文件，抽取资格要求、评分标准、废标项、格式要求和时间节点，再建立响应矩阵，绑定企业知识库，分章节生成，生成偏离表/证明材料/图表附件，最后做合规检查、预打分、排版导出和人工终审。[来源: https://www.xiquebiaoshu.com][来源: https://market.aliyun.com/products/201204006/cmgj00074082.html][来源: https://www.ai-indeed.com/encyclopedia/18040.html]

这条基线可以抽象为通用复杂文档平台的七个中间产物：

| 标书中间产物 | 通用抽象 | 说明 |
| --- | --- | --- |
| 招标文件解析报告 | 源需求解析报告 | 把外部要求、约束、评分/审查标准、交付格式抽成结构化对象。[来源: https://cloud.google.com/document-ai/docs/overview] |
| 评分点/废标项 | 要求与硬约束 | 任意复杂文档都存在“必须覆盖”“不能违反”“优先得分”的要求。[来源: https://market.aliyun.com/products/201204006/cmgj00074082.html] |
| 响应矩阵 | 要求-响应矩阵 | 每条要求映射到章节、证据、负责人、状态、风险和审查结论；这是防漏项的核心工件。[来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html] |
| 企业知识库 | 资料资产库 | 历史文档、案例、资质、产品、人员、法规、图表、模板都应变成可检索、可授权、可追溯资产。[来源: https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html] |
| 分章节生成 | 章节/组件级生成 | 长文档应按章节和组件生成、审查、确认，而不是一次性整本生成。[来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html] |
| 合规/预打分 | 审查评估 | 用规则、模型和人工复核检查覆盖率、一致性、格式、事实、风险和质量。[来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/] |
| Word/PDF 导出 | 输出交付 | 需要模板、样式、目录、页码、表格、附件、签章/元数据和归档。[来源: https://cloud-help.mandao.com/docs/ai/ai-bid-document-build][来源: https://docxtpl.readthedocs.io/en/latest/] |

#### 2. 通用平台应支持的复杂文档类型

平台应按“文档类型包”扩展，而不是把所有文档塞进同一个 prompt。可优先支持：

- 标书/投标文件：保留标书专用插件、评分点、废标项、偏离表、资质证明、暗标、签章、电子投标平台格式。[来源: https://market.aliyun.com/products/201204006/cmgj00074082.html]
- 政府/科技/资金申报书：项目背景、创新性、可行性、预算、绩效指标、附件证明、政策匹配。部分为标书能力的同构迁移，具体规则包需另行调研，未验证。
- 可研报告/立项报告：市场需求、建设方案、投资估算、财务测算、风险评估、合规依据。具体行业指标需专业规则库，未验证。
- 商业计划书/融资材料：市场、产品、团队、商业模式、财务预测、里程碑、风险披露。真实性和投资合规需人工把关，未验证。
- 解决方案/技术方案：客户需求、总体架构、功能模块、实施计划、安全方案、运维方案、案例和报价边界。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]
- 合同/法务文档：条款抽取、风险条款、主体/金额/期限一致性、模板条款库、审查意见。Azure Document Intelligence 有 contract 预置模型，但法律结论不能由 AI 单独裁决。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview]
- 技术规范/项目管理文档：需求规格、设计文档、测试方案、SOP、项目计划、验收报告。SOPStruct 说明复杂流程可转为 DAG，捕捉逻辑和时间依赖。[来源: https://arxiv.org/html/2504.00029]
- 合规报告/审计报告/医疗或工程文档：字段抽取、规则核查、证据链和人工签字责任很关键。Azure/AWS/Google 文档智能资料均显示多行业文档需要 OCR、表格、键值对、类型分类和定制抽取能力。[来源: https://cloud.google.com/document-ai/docs/overview][来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview][来源: https://docs.aws.amazon.com/textract/latest/dg/what-is.html]

#### 3. 根对象模型

建议把平台内核抽象为以下对象。该模型为本文综合设计，需通过真实项目 POC 验证。

1. `DocumentType`：文档类型定义，包括适用场景、章节模板、字段 schema、资料类型、角色、审查规则、输出格式和评测指标。[来源: https://docs.cloud.google.com/document-ai/docs/label-documents][来源: https://platform.openai.com/docs/guides/structured-outputs]
2. `DocumentSchema`：文档字段 schema，包括项目字段、章节字段、表格字段、附件字段、输出字段、字段类型、是否必填、来源要求、校验规则。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview]
3. `Requirement`：外部要求、内部目标、评分项、合规条款、格式约束或用户自定义要求。[来源: https://arxiv.org/html/2410.09077v1]
4. `ResponseMatrix`：要求到章节、资料、证据、负责人、状态、审查结果和风险等级的映射。标书场景已证明这是核心中间产物；通用场景属于抽象迁移，需 POC 验证。[来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html]
5. `KnowledgeAsset`：资料资产，包括原始文件、解析结果、chunk、实体、表格、图片、版本、权限、有效期、可信度和来源。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]
6. `Section` / `Component`：章节和可复用组件，如正文段落、表格、图表、附件、证明材料、条款、清单、签章页、目录。[来源: https://docxtpl.readthedocs.io/en/latest/]
7. `GenerationTask`：生成任务，包含输入、依赖、允许引用资料、禁止事项、结构化输出 schema、质量门槛和人工确认状态。[来源: https://arxiv.org/html/2504.00029]
8. `ReviewRule`：规则对象，包括触发条件、适用章节、规则类型、证据要求、严重等级、自动/人工处理方式。RuleRAG 证明规则可以指导检索和生成的归因机制。[来源: https://arxiv.org/html/2410.22353v2]
9. `EvidenceLink`：证据链对象，记录生成句子、引用资料、源页码/源句、关系类型、可信度和人工确认状态。TROVE 将 target sentence 与 source sentence 关系分为 quotation、compression、inference、others，可作为证据链设计参考。[来源: https://arxiv.org/html/2503.15289v3]
10. `Deliverable`：交付物对象，包括 Word、PDF、表格附件、图片、压缩包、电子平台文件和归档版本。[来源: https://cloud-help.mandao.com/docs/ai/ai-bid-document-build]

### 二、平台功能分层

#### 1. 文档类型配置层

作用：把每类复杂文档的专业知识产品化为可配置资产。

必须能力：

- 文档类型包：名称、适用范围、默认流程、章节树、字段 schema、输出模板、角色和权限。
- 章节/组件库：章节模板、表格模板、附件模板、图表模板、常用段落、禁用表达。
- 要求类型：硬性要求、评分要求、合规要求、格式要求、资料要求、人工判断要求。
- 审查规则包：字段必填、一致性、引用、格式、事实、权限、合规、专业评分。
- 模板版本：模板变更、规则变更、适用行业、废弃状态、迁移说明。

来源依据：字段 schema 与命名影响抽取质量，结构化输出可强制 JSON Schema，复杂 SOP 可转为带依赖的 DAG。[来源: https://docs.cloud.google.com/document-ai/docs/label-documents][来源: https://platform.openai.com/docs/guides/structured-outputs][来源: https://arxiv.org/html/2504.00029]

#### 2. 知识/资料资产层

作用：将企业资料从“文件堆”变成“可查、可管、可引用、可审计”的资产。

必须能力：

- 资料上传：Word、PDF、扫描件、图片、Excel、PPT、压缩包、网页剪藏。
- 解析结果：OCR 文本、版面结构、表格、键值对、段落、标题、页码、图片、公式、手写体。
- 分类与标签：文档类型、项目、客户、行业、年份、地区、密级、有效期。
- 版本与有效期：历史版本、作废版本、最新版本、来源日期、适用边界。
- 权限与授权引用：按项目、角色、章节、资料类型和密级控制引用。
- 知识沉淀：历史高分章节、案例、资质、人员、产品、政策、标准、复盘结果。

来源依据：Document AI 支持 OCR、layout、form parser、custom extractor、custom classifier、document splitting；Azure Document Intelligence 支持 read、layout、prebuilt、custom extraction、custom classifier 和强类型字段；AWS Textract 支持文本、手写体、表单、表格、Queries、发票/收据/ID/贷款包处理。[来源: https://cloud.google.com/document-ai/docs/overview][来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview][来源: https://docs.aws.amazon.com/textract/latest/dg/what-is.html]

#### 3. 解析抽取层

作用：把输入资料和外部要求转为可计算对象。

必须能力：

- 多模态文档解析：OCR、表格、图片、页眉页脚、目录、页码、公式、印章/签名、附件包。
- 需求抽取：目标、范围、字段、清单、时间、角色、约束、评分、风险、附件。
- 文档切分：按章节、标题、表格、页面、语义块、附件和版本进行切分。
- 字段抽取 schema：字段名称、类型、层级、是否必填、校验规则、来源页码。
- 版本差异：主文件、补遗、澄清、修订版之间的差异比对。

来源依据：Google Document AI 把文档处理拆成 OCR、布局、键值对、表格、分类、拆分、schema 管理和评估；Azure 文档智能返回 string、number、integer、date、currency、address 等强类型字段。[来源: https://cloud.google.com/document-ai/docs/overview][来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview]

#### 4. 规划编排层

作用：先规划，再生成。

必须能力：

- 目录/大纲生成：根据文档类型、需求、规则和模板生成章节树。
- 响应矩阵：要求映射章节、证据、责任人、状态和风险。
- DAG 工作流：任务依赖、并行任务、人工关口、缺资料回填、失败重试。
- Agent 编排：解析 Agent、检索 Agent、规划 Agent、生成 Agent、审查 Agent、排版 Agent。
- 缺失信息追问：在生成前输出缺资料清单，不得编造。

来源依据：投标文档 RAG 论文提出先检索相似模板，再用智能标签与 Agent 追问缺失参数，直到模板所需信息完整；SOPStruct 把 SOP 分段、生成 DAG 并验证依赖完整性。[来源: https://arxiv.org/html/2410.09077v1][来源: https://arxiv.org/html/2504.00029]

#### 5. 生成编辑层

作用：把“生成”限制在可控边界内。

必须能力：

- 章节级生成：每章独立输入、输出、证据、审查和人工确认。
- 组件级生成：段落、表格、图表说明、附件清单、证明材料、偏离表、摘要、目录。
- 结构化输出：JSON Schema、表格 schema、章节 schema、审查结果 schema。
- 编辑 Copilot：改写、扩写、压缩、风格统一、术语统一、引用补全。
- 协作编辑：多人批注、任务分派、修订记录、版本对比。

来源依据：OpenAI Structured Outputs 可确保模型输出符合 JSON Schema；docxtpl 使用 Word 模板和 Jinja2 标签填充复杂 docx，支持段落、表格行/列、富文本、图片、子文档等。[来源: https://platform.openai.com/docs/guides/structured-outputs][来源: https://docxtpl.readthedocs.io/en/latest/]

#### 6. 审查评估层

作用：把质量、合规和风险作为平台核心闭环。

必须能力：

- 要求覆盖检查：每条要求是否被响应，是否有证据。
- 事实检查：主体、金额、日期、人员、项目、指标、承诺是否有来源且一致。
- 引用溯源：句子级或段落级回链到来源页码、源句、资料版本。
- 规则审查：文档类型规则、行业规则、企业规则、项目规则。
- 评测指标：检索、生成、事实性、相关性、完整性、格式、人工修改量。

来源依据：Ragas 列出 context precision、context recall、faithfulness、response relevancy、factual correctness、tool call accuracy 等指标；TROVE 说明高风险领域需要知道内容从哪里来以及如何从来源生成。[来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/][来源: https://arxiv.org/html/2503.15289v3]

#### 7. 输出交付层

作用：交付可编辑、可提交、可归档的正式文件。

必须能力：

- Word 导出：样式、目录、页码、表格、图片、页眉页脚、封面、附件。
- PDF 导出：固定版式、可搜索 PDF、签章/水印、文件大小控制。
- 附件包：证书、图片、清单、Excel、PPT、压缩包顺序。
- 格式检查：字体、字号、行距、页边距、编号、目录、页码、元数据。
- 归档：最终版、过程版、证据链、审查记录、人工确认、复盘结果。

来源依据：满道云 AI 投标文件生成帮助文档要求生成后下载 PDF/Word 并核对核心信息、关键模块、页码、签章位置；docxtpl 支持从复杂 Word 模板生成 docx，但也列出同一段落/表格标签、特殊字符转义、富文本样式等限制。[来源: https://cloud-help.mandao.com/docs/ai/ai-bid-document-build][来源: https://docxtpl.readthedocs.io/en/latest/]

#### 8. 治理安全层

作用：保证资料不被滥用、泄露、污染或越权引用。

必须能力：

- 身份与权限：组织、项目、角色、章节、资料、模型、导出权限。
- 密级控制：资料出域控制、私有化/混合部署、模型供应商留存策略。
- 审计日志：上传、解析、检索、生成、导出、删除、权限变更。
- 安全防护：提示注入、敏感信息泄露、输出验证、插件权限、过度代理。
- 知识库治理：资料质量、过期、重复、冲突、污染、授权状态。

来源依据：OWASP LLM Top 10 包含 Prompt Injection、Insecure Output Handling、Training Data Poisoning、Sensitive Information Disclosure、Insecure Plugin Design、Excessive Agency、Overreliance 等风险；标书种子资料强调报价、资质、客户策略等资料需要私有化、权限和审计。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/][来源: https://market.aliyun.com/products/201204006/cmgj00074082.html][来源: https://www.ai-indeed.com/encyclopedia/18040.html]

#### 9. 运营评测层

作用：让平台从每次交付中变聪明，而不是每次从零开始。

必须能力：

- 样本文档集：按文档类型沉淀测试集、黄金答案、审查规则和错误样本。
- 指标体系：解析准确率、字段召回率、检索召回率、引用准确率、覆盖率、人工修改量、交付错误率。
- A/B 实验：chunk 策略、embedding、rerank、prompt、模型、规则包版本对比。
- 复盘回流：最终版、人工修改、客户反馈、中标/审批/审查结果、专家意见。
- 质量看板：文档类型、团队、项目、规则、模型版本的效果追踪。

来源依据：Microsoft RAG 设计指南强调按准备、chunking、enrichment、embedding、retrieval、end-to-end evaluation 各阶段评估，并记录超参数和评估结果；Ragas 提供 RAG 与 Agent 工作流评测指标。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide][来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/]

### 三、如何覆盖标书专业度

#### 1. 标书不能只是一个通用模板

如果把标书做成“文档类型 = 标书，章节 = 技术方案/商务方案”会丢失专业度。标书至少需要以下专用包：

| 专用包 | 必备内容 | 支撑来源 |
| --- | --- | --- |
| 标书解析包 | 招标文件、公告、补遗、澄清、附件、图纸、清单、电子平台说明解析 | [来源: https://www.ai-indeed.com/encyclopedia/18040.html] |
| 评分/废标规则包 | 资格性、符合性、技术评分、商务评分、废标项、格式项、暗标项 | [来源: https://market.aliyun.com/products/201204006/cmgj00074082.html] |
| 响应矩阵模板包 | 招标要求、响应章节、资料证据、负责人、状态、风险、检查结论 | [来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html] |
| 企业资料包 | 资质、人员、业绩、产品、案例、财务、授权、图片、历史中标标书 | [来源: https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html] |
| 表单附件包 | 技术偏离表、商务偏离表、资质证明清单、人员表、业绩表、指标响应证明 | [来源: https://market.aliyun.com/products/201204006/cmgj00074082.html] |
| 输出格式包 | Word/PDF、目录、页码、签章、暗标、封装、电子投标平台要求 | [来源: https://cloud-help.mandao.com/docs/ai/ai-bid-document-build] |
| 评审包 | 废标检查、评分点覆盖、预打分、一致性、格式、原文溯源、人工终审 | [来源: https://www.xiquebiaoshu.com][来源: https://www.ai-indeed.com/encyclopedia/18040.html] |

#### 2. 标书插件的产品边界

标书插件应覆盖：

- 读标：解析招标文件、补遗、答疑、图纸、清单和电子平台规则。
- 决策：资格满足度、高分项、缺口项、风险项、是否投标。
- 策划：响应矩阵、目录、章节任务、资料清单、人工关口。
- 生成：技术方案、商务方案、服务方案、施工组织、偏离表、证明材料。
- 审查：废标、评分点、暗标、签章、格式、报价、工期、人员、业绩一致性。
- 交付：Word/PDF、附件包、签章、加密、提交清单、归档复盘。

这些能力来自种子资料中的多源交叉结论，实际产品实现深度需按行业和电子投标平台进一步验证。[来源: https://www.xiquebiaoshu.com][来源: https://market.aliyun.com/products/201204006/cmgj00074082.html][来源: https://www.ai-indeed.com/encyclopedia/18040.html][来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html]

### 四、产品架构蓝图

#### 1. 逻辑架构

```text
文档类型配置层
  ├─ 文档类型包 / schema / 章节树 / 输出模板 / 规则包
知识与资料资产层
  ├─ 原始文件 / 解析结果 / chunk / metadata / 实体关系 / 权限 / 版本
解析抽取层
  ├─ OCR / layout / 表格 / 字段 / 要求 / 版本差异 / 附件解析
规划编排层
  ├─ 大纲 / 响应矩阵 / DAG / Agent 工作流 / 缺资料追问
生成编辑层
  ├─ 章节生成 / 组件生成 / 结构化输出 / 协作编辑 / 版本
审查评估层
  ├─ 覆盖率 / 事实一致 / 引用溯源 / 规则审查 / 预评分 / 评测
输出交付层
  ├─ Word / PDF / 附件包 / 格式检查 / 签章元数据 / 归档
治理安全层
  ├─ 权限 / 密级 / 审计 / 提示注入防护 / 数据污染治理
运营评测层
  ├─ 测试集 / 指标 / A/B 实验 / 复盘回流 / 质量看板
```

该架构为综合设计，需通过标书、申报书、合同、可研报告等多个文档类型 POC 验证。其组成模块分别由文档智能、RAG、GraphRAG、结构化输出、SOPStruct、Ragas、OWASP 等来源支撑。[来源: https://cloud.google.com/document-ai/docs/overview][来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide][来源: https://microsoft.github.io/graphrag/][来源: https://platform.openai.com/docs/guides/structured-outputs][来源: https://arxiv.org/html/2504.00029][来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/][来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]

#### 2. 最小可行产品到企业级平台的演进

| 阶段 | 能力目标 | 不应妥协的底线 |
| --- | --- | --- |
| P0 单类型 POC | 选择标书或申报书，完成上传、解析、大纲、章节生成、Word 导出 | 必须保留来源引用和人工终审，不能宣传全自动交付。[来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html] |
| P1 标书专业版 | 读标、响应矩阵、知识库绑定、偏离表、废标检查、格式检查 | 标书能力不能被通用化稀释。[来源: https://market.aliyun.com/products/201204006/cmgj00074082.html] |
| P2 多文档类型 | 用 DocumentType 包扩展申报书、合同、技术方案、可研报告 | 每类文档必须有 schema、规则包、输出模板和评测集。[来源: https://docs.cloud.google.com/document-ai/docs/label-documents] |
| P3 企业资产与协作 | 资料治理、权限、版本、协作、审计、归档复盘 | 涉密资料必须有权限和出域控制。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/] |
| P4 智能评测运营 | 指标、A/B、复盘、模型/检索/规则优化 | 供应商宣传指标不得替代企业自测。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide] |

## 推荐工作流

### 通用复杂文档工厂的标准产品流程

1. 定义文档类型：配置文档类型包、章节树、字段 schema、资料类型、输出格式、角色权限和审查规则。[来源: https://docs.cloud.google.com/document-ai/docs/label-documents][来源: https://platform.openai.com/docs/guides/structured-outputs]
2. 建立项目空间：录入项目目标、文档类型、密级、负责人、截止时间、交付格式和协作者。该步骤为综合设计，未验证。
3. 收集资料：上传需求文件、历史材料、政策/标准、案例、模板、附件、图片和表格；记录来源、版本、有效期、权限。[来源: https://cloud.google.com/document-ai/docs/overview]
4. 解析需求：用 OCR/IDP 抽取文本、布局、表格、字段、附件和要求，生成源需求解析报告。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview][来源: https://docs.aws.amazon.com/textract/latest/dg/what-is.html]
5. 生成大纲和响应矩阵：把每条要求映射到章节、资料、证据、负责人、状态和风险。[来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html]
6. 绑定资料：按章节限定可引用资料，过滤过期、无权限、低质量或不适用材料。[来源: https://www.53ai.com/news/zhinenghuagaizao/2025022571652.html]
7. 分章节生成：每章使用章节目标、要求、资料、禁止编造规则和输出 schema；缺资料时生成缺失清单。[来源: https://arxiv.org/html/2410.09077v1]
8. 组件与附件生成：生成表格、图表、证明材料、清单、摘要、附件索引和特殊文档组件。[来源: https://docxtpl.readthedocs.io/en/latest/]
9. 审查评分：检查要求覆盖、事实一致、引用、规则、格式、权限和安全，输出风险清单。[来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/][来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]
10. 人工终审：业务、技术、法务/合规、排版负责人按责任域确认。AI 不应替代最终责任人，特别是在法律、医疗、投标等高风险场景。[来源: https://www.ai-indeed.com/encyclopedia/18040.html]
11. 排版导出：套用 Word 模板、生成 PDF、检查目录页码、签章、水印、元数据和附件顺序。[来源: https://cloud-help.mandao.com/docs/ai/ai-bid-document-build][来源: https://docxtpl.readthedocs.io/en/latest/]
12. 归档复盘：保存最终版、证据链、审查记录、人工修改、客户反馈和评测结果，并回流资料库。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]

## 适用场景

- 企业有大量重复但复杂的正式文档，需要保持格式、结构、证据和审查一致性，例如标书、申报书、解决方案、合同、可研报告、审计/合规报告。[来源: https://cloud.google.com/document-ai/docs/overview]
- 文档需要引用企业私有资料、历史文档、政策法规、产品信息或项目案例，且不能靠模型参数知识直接生成。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]
- 文档存在硬性要求、评分规则、审查规则、字段 schema、附件清单和正式输出格式。[来源: https://market.aliyun.com/products/201204006/cmgj00074082.html]
- 多人协作、多轮修改、多版本归档和责任审计很重要。该场景为综合判断，需按企业流程验证。
- 企业愿意建立资料治理、规则维护、评测集和人工终审机制，而不是只采购一个聊天窗口。[来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/]

## 不适用场景

- 简单短文、一次性营销文案、没有硬性格式/证据/审查要求的内容，使用普通写作助手可能更轻。[来源: https://platform.openai.com/docs/guides/structured-outputs] 该结论为产品取舍推断。
- 企业没有可靠资料库，也没有人工提供真实信息，却期望 AI 编造完整正式文件；这会带来幻觉和责任风险。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]
- 法律、医疗、投标、审计等高风险文件如果没有专业人员终审，不适合让 AI 单独交付。[来源: https://www.ai-indeed.com/encyclopedia/18040.html]
- 文档格式极端依赖专有客户端、电子签章或地方平台，且无法获得格式规则或测试环境。该项未验证。
- 组织不愿维护文档类型包、规则包、模板包、评测集和资料治理，只希望一次性“全自动”。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]

## 风险与约束

1. 过度抽象风险：通用平台若只保留章节模板和大模型生成，会丢掉标书等垂直场景的废标项、偏离表、资质证明、暗标、签章和电子平台格式能力。[来源: https://market.aliyun.com/products/201204006/cmgj00074082.html]
2. Schema 设计风险：字段命名、层级、类型和标注规范会影响抽取质量；字段一旦进入生产后频繁变更会造成数据迁移和模型重训成本。[来源: https://docs.cloud.google.com/document-ai/docs/label-documents]
3. 知识库污染风险：过期、低分、无权限、错误或不适用资料进入 RAG，会把错误经验放大。OWASP 将训练数据污染和敏感信息泄露列为 LLM 应用风险。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]
4. 引用不可追溯风险：仅给段落尾部附几个来源不能满足高风险文档；复杂文档需要句子级/要求级证据链。TROVE 说明真实场景需要定位目标句来自哪些源句以及关系类型。[来源: https://arxiv.org/html/2503.15289v3]
5. 长文档上下文丢失风险：SOPStruct 指出即使长上下文模型能处理较长 SOP，仍可能丢失细粒度依赖，分段和结构化表示可减少遗漏。[来源: https://arxiv.org/html/2504.00029]
6. RAG 评测复杂风险：chunk、metadata、embedding、检索方式、rerank 和模型都影响最终质量，必须按阶段评估。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]
7. Word/PDF 格式风险：docx 模板可支持复杂 Word 内容，但 Jinja 标签在段落、表格行/列、run 中有约束，特殊字符、富文本、页眉页脚图片、嵌入对象都有实现限制。[来源: https://docxtpl.readthedocs.io/en/latest/]
8. 安全治理风险：提示注入、插件权限、敏感信息泄露、过度代理和对 AI 输出过度信任都可能造成严重后果。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]
9. 供应商指标风险：种子报告已记录多个供应商宣传的效率、中标率、文本可用比例缺少第三方验证；通用平台采购也应以企业自有 POC 指标评估。[来源: https://cloud.tencent.com/developer/article/2549224][来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html]

## 信源质量门控记录

### 门控规则

- A 级：官方文档、学术论文、云厂商/平台正式文档、产品官网或云市场正式页面，可支撑核心事实。
- B 级：厂商文章、开源工具文档、行业文章，可支撑产品能力和实践参考，但营销指标需交叉验证。
- C 级：推广性强、SEO/社区文章、单方经验，谨慎作为背景，不单独支撑核心结论。
- D 级：低相关、抓取失败、重复、无法访问或明显广告，剔除或只记录为失败。
- C/D 级来源不得作为唯一结论依据；供应商自述能力不等于独立验证效果。
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`。

### 保留信源

1. [Google Document AI overview](https://cloud.google.com/document-ai/docs/overview)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档，说明 Document AI 的 OCR、layout、KVP、表格、分类、拆分、自定义抽取和下游集成。
   - 后续处理：进入正式报告核心依据。
2. [Google Document AI label documents](https://docs.cloud.google.com/document-ai/docs/label-documents)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档，说明字段命名、zero/few-shot、标注、复核和质量控制。
   - 后续处理：进入 schema 与标注规范依据。
3. [Azure Document Intelligence overview](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档，说明 Read/Layout/预置模型/自定义模型/强类型字段。
   - 后续处理：进入解析抽取层依据。
4. [Amazon Textract overview](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档，说明文本、手写体、表单、表格、Queries、发票/收据/ID/贷款包处理。
   - 后续处理：进入 OCR/IDP 能力依据。
5. [Microsoft RAG solution design guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方架构文档，说明 RAG 数据管线、chunk、metadata、embedding、search、评测和实验。
   - 后续处理：进入知识资产层、RAG 与评测依据。
6. [Microsoft GraphRAG documentation](https://microsoft.github.io/graphrag/)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方项目文档，说明 GraphRAG 从文本抽取图谱、社区层级和摘要，并支持 global/local/DRIFT/basic search。
   - 后续处理：进入 GraphRAG 设计依据。
7. [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档，说明 JSON Schema 结构化输出、schema adherence、JSON mode 差异和最佳实践。
   - 后续处理：进入结构化输出依据。
8. [SOPStruct](https://arxiv.org/html/2504.00029)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文，说明 SOP 分段、DAG、依赖、输入/输出和 PDDL 评估。
   - 后续处理：进入规划编排依据。
9. [Tender Document RAG](https://arxiv.org/html/2410.09077v1)
   - 工具：WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文，说明投标/采购文档 RAG、模板检索、智能标签、GraphRAG 和 Word 模板。
   - 后续处理：进入标书专业能力依据。
10. [RuleRAG](https://arxiv.org/html/2410.22353v2)
    - 工具：WebFetch
    - 来源等级：A
    - 入库映射：`source-quality: high`
    - 保留原因：学术论文，说明规则引导检索和生成，标准 RAG 难以捕捉逻辑关系。
    - 后续处理：进入规则包和审查依据。
11. [TROVE](https://arxiv.org/html/2503.15289v3)
    - 工具：WebFetch
    - 来源等级：A
    - 入库映射：`source-quality: high`
    - 保留原因：学术论文，说明句子级 provenance、来源关系分类和检索增强。
    - 后续处理：进入引用溯源依据。
12. [Ragas metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)
    - 工具：WebFetch
    - 来源等级：B
    - 入库映射：`source-quality: high`
    - 保留原因：工具文档，列出 RAG、Agent、事实性、相似度和通用评测指标。
    - 后续处理：进入运营评测依据。
13. [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
    - 工具：WebFetch
    - 来源等级：A
    - 入库映射：`source-quality: high`
    - 保留原因：权威安全项目，列出 LLM 应用主要安全风险。
    - 后续处理：进入治理安全依据。
14. [python-docx-template documentation](https://docxtpl.readthedocs.io/en/latest/)
    - 工具：WebFetch
    - 来源等级：B
    - 入库映射：`source-quality: high`
    - 保留原因：工具文档，说明 Word 模板、Jinja2 标签、表格、富文本、图片、子文档和限制。
    - 后续处理：进入 Office 交付依据。
15. [AI 标书助手种子报告中的来源集合](raw/articles/2026-06-15-ai-bid-document-assistant-research.md)
    - 工具：ReadFile
    - 来源等级：B
    - 入库映射：`source-quality: high`
    - 保留原因：本仓库已有 raw 调研报告，包含标书产品、论文、官方文档和坑点门控记录。
    - 后续处理：作为标书能力基线，不直接替代原始 URL 引用。

### 剔除信源

1. [OpenReview SCHEMARAG PDF](https://openreview.net/pdf?id=VjtMhU3zWn)
   - 工具：four_tool_research.py
   - 来源等级：A
   - 剔除原因：脚本抓取连接中断，未能二次读取 PDF；不进入核心结论。
2. [DocScope](https://arxiv.org/html/2605.08888v1)
   - 工具：WebFetch
   - 来源等级：A
   - 剔除原因：二次读取超时；不进入核心结论。
3. [知乎 GraphRAG 文章](https://zhuanlan.zhihu.com/p/1928982650628084885)
   - 工具：four_tool_research.py
   - 来源等级：C
   - 剔除原因：社区文章，已有 Microsoft GraphRAG 官方文档替代。
4. [GraphRAG 中文教程站](https://graphragcn.com)
   - 工具：four_tool_research.py
   - 来源等级：C
   - 剔除原因：非一手来源，已有官方文档替代。
5. [金现代智能文档处理平台](https://idp.jxdinfo.com)
   - 工具：four_tool_research.py
   - 来源等级：C
   - 剔除原因：Firecrawl 精读失败，且本报告不以厂商宣传为核心依据。
6. [火眼审阅官网](https://firesee.fagougou.com)
   - 工具：four_tool_research.py
   - 来源等级：C
   - 剔除原因：Firecrawl 精读失败，且本报告已有标书种子资料覆盖文档审阅产品能力。

## 来源与可信度

| 来源 | 类型 | 可信度 | 主要支撑内容 |
| --- | --- | --- | --- |
| Google Document AI overview | 官方文档 | 高 | OCR、布局、KVP、表格、分类、拆分、schema 管理、集成 |
| Google Document AI labeling | 官方文档 | 高 | 字段命名、few-shot、标注规范、人工复核 |
| Azure Document Intelligence | 官方文档 | 高 | Read/Layout/预置/自定义模型、强类型字段、文档分类 |
| Amazon Textract | 官方文档 | 高 | 文本、手写体、表单、表格、Queries、异步多页处理 |
| Microsoft RAG design | 官方架构文档 | 高 | RAG 数据管线、chunk、metadata、embedding、检索、评测 |
| Microsoft GraphRAG | 官方项目文档 | 高 | 图谱抽取、社区层级、global/local/DRIFT/basic search |
| OpenAI Structured Outputs | 官方文档 | 高 | JSON Schema 结构化输出、schema adherence、JSON mode 差异 |
| Tender Document RAG | 学术论文 | 高 | 标书/采购文档模板检索、智能标签、GraphRAG、Word 模板 |
| SOPStruct | 学术论文 | 高 | SOP 分段、DAG、依赖、输入输出、PDDL 评估 |
| RuleRAG | 学术论文 | 高 | 规则引导检索与生成，标准 RAG 的逻辑关系短板 |
| TROVE | 学术论文 | 高 | 句子级来源追踪、关系分类、检索增强 |
| Ragas metrics | 工具文档 | 中到高 | RAG 与 Agent 评测指标 |
| OWASP LLM Top 10 | 安全项目 | 高 | LLM 应用安全风险 |
| docxtpl | 工具文档 | 中到高 | Word 模板生成能力和限制 |
| AI 标书助手种子报告 | 本地 raw 调研 | 高 | 标书专用平台基线、SOP、坑点、产品能力 |

## 对于可信度较高的来源逐来源总结

### 1. Google Document AI overview

正文内容：Google Document AI 被定义为文档处理和理解平台，可将非结构化文档数据转为结构化数据；能力包括 OCR、文本和版面信息抽取、键值对、表格、文档分类、拆分、自定义抽取、schema 管理、数据集和评估，并可与 Cloud Storage、BigQuery、Agent Search 等集成。[来源: https://cloud.google.com/document-ai/docs/overview]

可用事实：通用复杂文档平台需要把 OCR、布局、分类、拆分、字段抽取和下游存储/检索视为基础层，而不是只做 LLM 生成。

局限：这是云厂商产品文档，未给出本文场景下的准确率，需要企业 POC 验证。

适合入库知识点：文档智能处理平台、文档处理 pipeline、文档类型分类与抽取。

### 2. Google Document AI label documents

正文内容：该文档说明字段命名会影响生成式 AI 抽取准确性，建议字段名称与文档语言一致、不要缩写；few-shot 效果依赖整洁且仔细标注的数据，通常至少需要 10 个训练样本和 10 个测试样本；还建议创建标注说明、训练标注人员、初始样本复核和第二标注员质量检查。[来源: https://docs.cloud.google.com/document-ai/docs/label-documents]

可用事实：DocumentType 的字段 schema、命名规范和标注质量直接影响复杂文档抽取与生成质量。

局限：针对 Google Document AI 生态，但方法可迁移到通用文档平台。

适合入库知识点：文档 schema 命名规范、标注质量控制。

### 3. Azure Document Intelligence

正文内容：Azure Document Intelligence 支持 Read、Layout、General document、预置模型、自定义模型和自定义分类器；可抽取文本、表格、结构、键值对、合同、发票、收据、身份证、税务、贷款等文档字段，并返回 string、number、integer、date、currency、address 等强类型字段。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview]

可用事实：平台设计应支持“先分类再调用对应抽取模型/规则”的架构，并在字段层保留强类型和标准化结果。

局限：具体模型覆盖地域和版本会变化，生产使用需看版本与区域。

适合入库知识点：Azure Document Intelligence、强类型字段抽取、文档分类器。

### 4. Amazon Textract

正文内容：Amazon Textract 可检测打印和手写文本，抽取表单和表格，使用 Queries 指定抽取信息，处理发票/收据/ID/贷款包，并支持同步单页和异步多页处理；它可用于创建智能搜索索引、NLP 输入分组、表单数据自动化和文档分类抽取。[来源: https://docs.aws.amazon.com/textract/latest/dg/what-is.html]

可用事实：复杂文档平台需要同步/异步处理、表格/表单抽取、查询式抽取和文档包自动路由能力。

局限：AWS 产品能力不等同于自建平台能力，需要按成本、语言和文档类型验证。

适合入库知识点：OCR/IDP、查询式文档抽取、文档包处理。

### 5. Microsoft RAG solution design guide

正文内容：该文档将 RAG 分为应用流和数据管线流。应用流包括用户查询、orchestrator、搜索、打包 top N 结果、发送给语言模型；数据管线包括 chunking、enrich chunks、embed chunks、persist chunks。文档还强调准备代表性测试媒体和查询、选择 chunk 策略、metadata enrichment、embedding、全文/向量/混合/多次搜索、逐阶段评估和记录超参数。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]

可用事实：复杂文档平台的 RAG 不能一次性搭建后长期不测，必须按阶段实验和评估。

局限：是通用 RAG 架构指南，不包含标书、合同等垂直规则。

适合入库知识点：RAG 设计流程、RAG 评测、chunk 策略。

### 6. Microsoft GraphRAG documentation

正文内容：GraphRAG 是结构化、层级化的 RAG 方法，会从原始文本中抽取知识图谱，构建社区层级，生成社区摘要，再在查询时使用这些结构。文档指出基线 RAG 在需要连接分散信息或整体理解大型集合/单个大文档时表现较差；GraphRAG 提供 Global Search、Local Search、DRIFT Search、Basic Search。[来源: https://microsoft.github.io/graphrag/]

可用事实：复杂文档平台应在跨章节、跨文档关系推理和整体摘要上引入 GraphRAG 或图结构，而不是只靠 top-k chunks。

局限：GraphRAG 成本、构图质量、实体/关系 schema 和更新策略需单独评估。

适合入库知识点：GraphRAG、知识图谱增强检索、全局/局部检索模式。

### 7. OpenAI Structured Outputs

正文内容：Structured Outputs 可使模型响应遵循开发者提供的 JSON Schema，降低缺字段、非法枚举等问题；它比 JSON mode 更强，因为 JSON mode 只保证有效 JSON，不保证 schema adherence。文档也提醒结构化输出仍可能包含内容错误，需拆分任务、改进指令和用 Pydantic/Zod 避免 schema 与代码类型分叉。[来源: https://platform.openai.com/docs/guides/structured-outputs]

可用事实：复杂文档平台中，解析结果、响应矩阵、审查结果、章节计划都应尽量用结构化输出和 schema 校验承载。

局限：结构正确不等于事实正确，仍需证据链和审查。

适合入库知识点：结构化输出、JSON Schema 约束、LLM 输出校验。

### 8. Tender Document RAG

正文内容：论文指出政府采购文档比普通生成任务更严格，需符合结构、风格、用户要求和政策；提出模板检索、记忆网络一致性验证、采购知识库修改三步框架。系统用历史 Word 模板、智能标签、缺失信息 Agent、python-docx/PageOffice 修改段落和表格，并用 GraphRAG 建采购知识图谱。[来源: https://arxiv.org/html/2410.09077v1]

可用事实：复杂专业文档应采用“模板检索 + 智能字段 + 缺失信息追问 + 知识库修改”的流程，而不是单 prompt 生成。

局限：实验集中在医疗采购历史文档，泛化到所有复杂文档需验证。

适合入库知识点：投标文档 RAG、智能标签填充、模板检索、采购知识图谱。

### 9. SOPStruct

正文内容：论文提出用 LLM 将自然语言 SOP 转成 DAG，先分段，再生成节点和依赖，节点包含 name、description、dependencies、inputs、inputs from dependencies、output、category，并用 PDDL 和 LLM 评估结构完整性、依赖和目标状态。论文强调不分段会丢失细粒度细节，即使长上下文模型也会遗漏复杂依赖。[来源: https://arxiv.org/html/2504.00029]

可用事实：复杂文档生成流程应建模为可验证 DAG，尤其是跨章节依赖、人工关口和缺资料处理。

局限：不是文档生成产品论文，但流程结构化方法高度相关。

适合入库知识点：SOP 结构化、DAG 工作流、PDDL 评估。

### 10. RuleRAG

正文内容：论文指出标准 RAG 的检索可能只匹配关键词，无法保证召回能支持推理；生成阶段也不清楚如何使用噪声检索内容。RuleRAG 将规则加入检索与生成，用规则指导 retrieval directions 和 attribution mechanisms，在 RuleQA 上相较标准 RAG 显著提升 Recall@10、Exact Match 和 Token F1。[来源: https://arxiv.org/html/2410.22353v2]

可用事实：复杂文档平台的规则包不应只用于事后检查，也可以用于检索和生成前的上下文选择。

局限：QA 任务与复杂文档生成不同，迁移需要实验。

适合入库知识点：规则引导 RAG、规则包、知识密集推理。

### 11. TROVE

正文内容：TROVE 要求把目标文本的每个句子追溯到长文档或多文档输入中的源句，并分类关系为 quotation、compression、inference、others；数据覆盖中英文、单/多文档、0-5k、5-10k、10k+ 长度。实验表明 retrieval-augmented tracing 普遍优于 direct prompting，关系分类仍是难点。[来源: https://arxiv.org/html/2503.15289v3]

可用事实：复杂文档平台需要细粒度 provenance，尤其是高风险文档的句子级引用和推理关系标注。

局限：这是 benchmark 论文，不是生产系统方案。

适合入库知识点：文本来源追踪、句子级 provenance、引用可信度评测。

### 12. Ragas metrics

正文内容：Ragas 提供 RAG、Agent、自然语言比较、SQL、通用评分等指标。RAG 指标包括 context precision、context recall、context entities recall、noise sensitivity、response relevancy、faithfulness、多模态 faithfulness 和 relevance；Agent 指标包括 tool call accuracy、tool call F1、agent goal accuracy。[来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/]

可用事实：复杂文档平台应建立检索、生成、工具调用和事实性的评测体系。

局限：指标能测一部分质量，不等于业务成功；需要业务指标补充。

适合入库知识点：RAG 评测指标、Agent 评测指标。

### 13. OWASP Top 10 for LLM Applications

正文内容：OWASP 项目列出 LLM 应用的核心安全风险，包括 Prompt Injection、Insecure Output Handling、Training Data Poisoning、Model Denial of Service、Supply Chain Vulnerabilities、Sensitive Information Disclosure、Insecure Plugin Design、Excessive Agency、Overreliance、Model Theft。[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]

可用事实：复杂文档平台涉及敏感资料、插件、模型调用和自动导出，必须建立治理安全层。

局限：OWASP 是安全风险框架，不提供具体文档平台实现。

适合入库知识点：LLM 应用安全、提示注入、敏感信息泄露、过度代理。

### 14. python-docx-template

正文内容：docxtpl 用 python-docx 和 Jinja2 管理 Word 模板标签，可从复杂 Word 模板生成 docx，支持段落、表格行/列、run、富文本、图片、子文档、媒体替换、变量检查和命令行生成；文档也列出同一段落/表格中标签放置、特殊字符转义、富文本过滤、页眉页脚图片等限制。[来源: https://docxtpl.readthedocs.io/en/latest/]

可用事实：复杂文档平台应将 Office 交付作为独立工程，不应只输出 Markdown 或纯文本。

局限：docxtpl 是 Python 工具，不覆盖 PDF、电子签章和复杂 Office 协同全部需求。

适合入库知识点：docx 模板引擎、Office 文档生成限制。

## 跨源矛盾检测结论

### 检测范围

- 已精读来源数量：14 个核心来源，加 1 篇本地标书种子报告。
- 检测对象：核心数字、日期、功能描述、因果判断、市场/公司事实。
- 检测时间：2026-06-15。

### 检测结果

结论：未发现会推翻本报告架构判断的跨源实质矛盾，但发现 4 类表达差异或待验证项，综合输出时已保留边界。

1. 自动化程度差异：标书产品和模板工具会描述“一键生成”或快速生成，但标书种子资料、投标文档 RAG 论文和 SOPStruct 均支持更稳妥的分阶段、分章节、结构化流程。综合判断：一键生成可作为低风险初稿入口，不应作为高风险复杂文档唯一流程。[来源: https://cloud-help.mandao.com/docs/ai/ai-bid-document-build][来源: https://arxiv.org/html/2410.09077v1][来源: https://arxiv.org/html/2504.00029]
2. RAG 与 GraphRAG 适用范围差异：Microsoft RAG 指南强调向量/全文/混合检索和逐阶段评估；GraphRAG 文档强调图谱和社区摘要对“连接分散信息”和“整体理解”的价值。二者不是矛盾，而是适用层级不同。[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide][来源: https://microsoft.github.io/graphrag/]
3. 结构化输出与事实正确性的边界：OpenAI Structured Outputs 保证 schema adherence，但提醒内容仍可能错误；TROVE 和 Ragas 关注来源追踪与事实性评测。综合判断：schema 只能解决格式和类型问题，不能替代证据链和审查。[来源: https://platform.openai.com/docs/guides/structured-outputs][来源: https://arxiv.org/html/2503.15289v3][来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/]
4. 供应商宣传指标不可验证：标书种子报告中腾讯云文章、GitCode/CSDN 文章等包含效率/中标率/文本可用比例等宣传性数字，缺少第三方验证；本报告未把这些数字作为事实依据。[来源: https://cloud.tencent.com/developer/article/2549224][来源: https://gitcode.csdn.net/6a2b7c7f662f9a54cb7d7c85.html]

## 矛盾与待验证问题

1. “通用复杂文档 AI 平台”的对象模型、九层架构和最小产品路线是本文综合设计，虽然各模块有来源支撑，但整体架构尚未由单一来源直接验证，需要真实 POC。
2. 标书专用插件/规则包/模板包/评审包的细粒度规则需要按行业、地区、电子投标平台和企业内部模板继续拆解，本报告只给产品架构级清单。
3. 申报书、可研报告、商业计划书、审计报告、医疗/工程/政府采购文档的具体规则包尚未逐类外部调研，当前示例分类为通用抽象，需后续专题报告验证。
4. GraphRAG、RuleRAG、TROVE 等论文能力迁移到复杂文档生成的成本、准确率和工程复杂度需要实验验证。
5. Word/PDF、电子签章、暗标清理、附件包、电子投标平台上传格式的工程细节需按具体工具链和平台测试。
6. 私有化部署是否做到模型、文档、向量库、日志和审计全链路不出域，需要技术审计。
7. 企业采用平台后的真实效果应使用自有指标验证：要求覆盖率、字段抽取准确率、引用准确率、人工修改量、交付错误率、审查通过率、标书废标项召回率等。

## 原始证据摘录

> “Document AI is a document processing and understanding platform that takes unstructured data from documents and transforms it into structured data.”[来源: https://cloud.google.com/document-ai/docs/overview]

> “Name the field with the same language used to describe it in the document... Don't use abbreviations.”[来源: https://docs.cloud.google.com/document-ai/docs/label-documents]

> “Structured Outputs is a feature that ensures the model will always generate responses that adhere to your supplied JSON Schema.”[来源: https://platform.openai.com/docs/guides/structured-outputs]

> “The data pipeline processes each media file individually by completing the following steps: Chunking, Enrich chunks, Embed chunks, Persist chunks.”[来源: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide]

> “GraphRAG is a structured, hierarchical approach to Retrieval Augmented Generation (RAG), as opposed to naive semantic-search approaches using plain text snippets.”[来源: https://microsoft.github.io/graphrag/]

> “We use Word templates base on historical tender documents with smart tags to generate information.”[来源: https://arxiv.org/html/2410.09077v1]

> “SOPStruct comprises of three primary phases: SOP Segmentation, SOP Structure Generation and Evaluation.”[来源: https://arxiv.org/html/2504.00029]

> “Retrieval is essential. Every model benefits significantly from retrieval...”[来源: https://arxiv.org/html/2503.15289v3]

> “Context Precision, Context Recall, Faithfulness, Response Relevancy.”[来源: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/]

> “Prompt Injection... Sensitive Information Disclosure... Excessive Agency... Overreliance.”[来源: https://owasp.org/www-project-top-10-for-large-language-model-applications/]
