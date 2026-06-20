---
title: "投标 AI 助手 OCR+LLM+结构化输出链路评估与优化设计调研"
source-type: article
generated: 2026-06-17
generated-by: wiki-research-skill
research-mode: standard
base-context:
  - "raw/articles/2026-06-15-ai-bid-document-assistant-research.md"
  - "raw/articles/2026-06-15-general-complex-document-ai-platform-architecture-research.md"
  - "raw/articles/2026-06-16-投标AI助手招标文件解析与评审要素抽取调研.md"
---

# 投标 AI 助手 OCR+LLM+结构化输出链路评估与优化设计调研

## 调研问题

用户提出的投标 AI 助手链路是：

```text
扫描 PDF / 标书图片
  -> 专业文档 OCR（还原版面、表格、全文）
  -> 全文 Markdown 输入大模型
  -> 按预设字段抽取信息
  -> 统一输出 Excel / 数据库 JSON
```

本报告回答三个问题：

1. 这条“OCR + LLM + Markdown + JSON/Excel”的链路是否是最优？
2. 全链路还有哪些优化空间？
3. 每一步应如何具体设计，才能支撑“投标 AI 助手自动编写投标文件”而不只是“招标文件信息抽取”？

## 核心结论

1. 该链路是可行的基础骨架，但不是最优生产链路。它缺少原生解析优先、版面/表格/页码坐标保真、章节切分、响应矩阵、企业资料库/RAG、规则校验、证据溯源、人工复核和 Word/PDF 交付闭环；如果只做“全文 Markdown -> 大模型 -> Excel/JSON”，容易变成一次性抽取工具，而不是可交付的投标 AI 助手。[来源: raw/articles/2026-06-16-投标AI助手招标文件解析与评审要素抽取调研.md][来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction] 可信度：高。
2. OCR 不应无差别作为第一步。可复制文本 PDF、Word、Excel、HTML/网页和电子投标平台数据应优先走原生解析；只有扫描件、图片化 PDF、低质量图片、盖章页、截图、图纸和不可复制/乱码 PDF 才需要 OCR 或多模态文档解析。Docling 和 PaddleOCR 都把 OCR、layout、table structure、reading order、document parsing 区分为不同能力，说明“文字识别”只是文档理解的一部分。[来源: https://arxiv.org/html/2408.09869v3][来源: https://arxiv.org/html/2507.05595] 可信度：高。
3. Markdown 是很好的 LLM 中间表示，但不应是唯一真相源。最优设计应同时保存 `raw_file`、`page_image`、`layout_blocks`、`tables_html`、`markdown_view`、`json_ast`、`bbox/page/source` 等多种表示；复杂表格建议保留 HTML 或结构化表格 JSON，单纯 Markdown 表格会丢合并单元格、跨页表头、行列层级和坐标证据。[来源: https://arxiv.org/html/2408.09869v3][来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction] 可信度：高。
4. “一步输出标准化结构化台账”适合低风险字段抽取，不适合完整投标文件自动编写。招标文件解析应拆成多任务：项目基础信息、时间节点、资格、评分、废标、采购需求、暗标、材料清单、合同条款、投标文件格式、电子提交规则，再汇总为响应矩阵；每个任务都要有 schema、证据位置、置信度、校验规则和人工确认状态。[来源: raw/articles/2026-06-16-投标AI助手招标文件解析与评审要素抽取调研.md][来源: https://link.springer.com/article/10.1186/s12874-026-02847-8] 可信度：高。
5. RAG/企业资料库不是可选增强，而是“自动编写投标文件”的核心。招标文件只告诉“要什么”，投标文件还需要企业资质、人员、业绩、产品、历史中标方案、图表、服务承诺和报价边界；没有 RAG 和资料授权，LLM 只能写通用文本，容易编造资质、人员、业绩和承诺。[来源: raw/articles/2026-06-15-ai-bid-document-assistant-research.md][来源: https://arxiv.org/html/2408.04675] 可信度：高。
6. JSON/数据库应作为规范主数据，Excel 只应作为业务视图和复核界面。结构化抽取结果应先进入可版本化、可校验、可审计的 JSON/数据库表，再导出 Excel 台账供业务人员复核；直接把模型输出做成 Excel 会削弱 schema 校验、证据链、版本差异和自动审查能力。[来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction][来源: https://link.springer.com/article/10.1186/s12874-026-02847-8] 可信度：高。
7. 最优链路应采用“机器高召回 + 规则硬校验 + 人工终裁”。模型负责召回和解释，规则负责日期、金额、分值、资质有效期、格式和一致性校验，人工负责资格满足、偏离承诺、报价策略、法律风险和最终提交责任。[来源: raw/articles/2026-06-16-投标AI助手招标文件解析与评审要素抽取调研.md][来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction] 可信度：高。

## 内容整理

### 一、对用户给定链路的判断

#### 1. 这条链路哪里正确

用户给出的链路抓住了三个关键方向：

- 复杂招标文件确实需要 OCR / Document AI。扫描 PDF、图片化 PDF、盖章页、截图、图纸、复杂表格和跨页附件只靠普通文本解析不够。[来源: raw/articles/2026-06-16-投标AI助手招标文件解析与评审要素抽取调研.md]
- LLM 确实需要参与语义抽取。OCR 只能“看见文字”，不能稳定处理否定条件、组合资质、评分公式、跨章节引用、废标触发、材料归属和响应建议。[来源: raw/articles/2026-06-16-投标AI助手招标文件解析与评审要素抽取调研.md]
- 标准化 JSON/Excel 台账确实是必要产物。项目名称、编号、时间节点、资格要求、评分项、废标项、材料清单等必须结构化，否则无法做响应矩阵、缺口检查、风险关闭和后续生成。[来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

#### 2. 这条链路哪里不够

这条链路最大问题是“过早压扁”和“过早汇总”：

```text
PDF/图片 -> OCR全文 -> Markdown -> LLM -> Excel/JSON
```

如果这样直接做，容易出现以下问题：

- 原生 PDF/Word/Excel 的标题层级、表格对象和样式信息被 OCR 破坏。
- Markdown 压扁复杂表格，合并单元格、跨页表头和表格坐标丢失。
- 全文一次性输入模型，长文档上下文容易被截断或稀释。
- 只抽字段，不建立“要求 -> 响应章节 -> 材料 -> 风险”的响应矩阵。
- 没有企业资料库，无法生成真实投标正文。
- 没有证据链，业务人员无法定位到原文页码/段落。
- 没有规则校验，日期、金额、分值、资质有效期等仍需人工大面积返工。
- 没有人工确认状态，不能进入正式投标责任链。

更准确的定位是：用户链路适合作为“招标文件关键信息抽取 POC”，不适合作为“自动编写投标文件”的完整生产链路。

### 二、推荐的最优总体链路

推荐链路如下：

```text
0. 项目建档与权限
  -> 1. 文件包归集与版本管理
  -> 2. 文档类型识别与原生解析优先
  -> 3. OCR / Layout / Table / Reading Order 解析
  -> 4. 多表示保真存储：Markdown + HTML Table + Layout JSON + Page/BBox
  -> 5. 章节切分与语义分块
  -> 6. 分任务结构化抽取：项目/时间/资格/评分/废标/需求/暗标/材料
  -> 7. Schema 校验、规则校验、冲突合并
  -> 8. 响应矩阵生成
  -> 9. 企业资料库/RAG 匹配：资质/人员/业绩/产品/历史方案
  -> 10. 缺口清单、澄清问题、风险清单
  -> 11. 目录和章节规划
  -> 12. 分章节生成投标文件初稿
  -> 13. 合规检查、评分覆盖检查、格式/暗标/签章检查
  -> 14. 人工复核与风险关闭
  -> 15. Word/PDF/Excel/数据库输出与归档复盘
```

如果产品早期只做 POC，可以收敛为：

```text
文件上传
  -> 原生解析/OCR
  -> Markdown + 表格 HTML + 页码定位
  -> 分任务抽取 JSON
  -> 校验
  -> 响应矩阵 Excel
  -> 人工确认
```

但只要目标是“自动编写投标文件”，必须继续建设 RAG、章节生成、审查和交付。

### 三、每一步具体设计

#### 0. 项目建档与权限

输入：

- 项目名称、招标编号、标段、投标主体、负责人、截止时间。
- 项目密级、允许使用的模型、是否允许外部联网、是否私有化处理。

输出：

- `ProjectWorkspace`。
- 文件版本表。
- 操作审计日志。
- 权限矩阵。

设计要点：

- 投标资料包含报价、资质、人员、业绩、客户策略和商务秘密，默认应按项目隔离。
- 外部联网检索默认只允许公开字段，不应上传完整招标文件、证书文件、人员信息和报价策略。
- 所有上传、解析、抽取、生成、导出都记录审计日志。

#### 1. 文件包归集与版本管理

输入文件应覆盖：

- 招标公告。
- 招标文件。
- 投标人须知及前附表。
- 评标办法/评分表。
- 技术规范书/采购需求。
- 合同条款。
- 投标文件格式。
- 工程量清单、图纸、附件。
- 补遗、澄清、答疑。
- 电子投标平台说明、CA、签章、加密、上传规则。

输出字段：

```json
{
  "file_id": "file-001",
  "file_name": "招标文件.pdf",
  "file_type": "tender_document",
  "version": "v1",
  "source": "user_upload",
  "effective_date": "2026-06-17",
  "supersedes": [],
  "priority": 10,
  "hash": "sha256..."
}
```

设计要点：

- 补遗/澄清不能作为普通附件处理，必须能覆盖原条款。
- 每条抽取结果都要记录来自哪个文件版本。
- 文件 hash 用于去重和恢复中断任务；schema-constrained PDF extraction 来源也采用 resume-aware hashing、异步处理和并发控制来支撑大规模处理。[来源: https://link.springer.com/article/10.1186/s12874-026-02847-8]

#### 2. 文档类型识别与原生解析优先

不要所有文件都 OCR。推荐路由：

| 输入类型 | 优先策略 | 原因 |
| --- | --- | --- |
| Word / DOCX | 原生解析 | 保留标题、样式、表格、批注、页眉页脚 |
| Excel / 清单 | 原生解析 | 保留 sheet、公式、单元格、合并单元格 |
| 可复制 PDF | PDF 文本层 + layout | 避免 OCR 错字，保留原文 |
| 扫描 PDF / 图片 | OCR + layout | 无文本层，只能识别 |
| 图纸 / 图片化表格 | 多模态 OCR + 人工复核 | 高风险，需保留图像证据 |
| 网页公告 | HTML/DOM 解析 | 表格、链接、附件更准确 |
| 电子平台导出 JSON/API | 直接入库 | 不要转文本再抽 |

Docling 支持 PDF 转 JSON/Markdown，理解页面布局、阅读顺序、定位图片并恢复表格结构，且 OCR 是可选能力；这说明最优链路应“解析器路由优先”，而不是“一律 OCR”。[来源: https://arxiv.org/html/2408.09869v3]

#### 3. OCR / Layout / Table / Reading Order 解析

解析层不只是“识别文字”，至少要输出：

- 页面文本。
- 标题层级。
- 段落块。
- 表格结构。
- 图片、图纸、印章、签名位置。
- 页码、bbox、阅读顺序。
- 页眉页脚。
- 跨页表格关系。
- OCR 置信度。

Docling 把 layout analysis 和 table structure recognition 作为 PDF conversion 的关键模型；PaddleOCR 3.0 将 PP-OCRv5、PP-StructureV3、PP-ChatOCRv4 分别用于多语言文字识别、层级文档解析和关键信息抽取，说明生产系统应把 OCR、结构解析、信息抽取分层。[来源: https://arxiv.org/html/2408.09869v3][来源: https://arxiv.org/html/2507.05595]

建议输出：

```json
{
  "page": 12,
  "blocks": [
    {
      "block_id": "p12-b03",
      "type": "paragraph",
      "text": "投标人须具备...",
      "bbox": [120, 300, 820, 360],
      "reading_order": 17,
      "ocr_confidence": 0.98
    }
  ],
  "tables": [
    {
      "table_id": "p12-t01",
      "html": "<table>...</table>",
      "cells": [],
      "bbox": [80, 400, 900, 700]
    }
  ]
}
```

#### 4. 多表示保真存储

推荐同时保留：

- `raw_file`：原始文件。
- `page_image`：每页图片或截图。
- `layout_json`：块、bbox、页码、阅读顺序。
- `markdown_view`：给 LLM 快速阅读的视图。
- `html_tables`：复杂表格保留 HTML。
- `table_json`：结构化表格。
- `text_chunks`：按章节/语义分块。
- `evidence_index`：原文位置索引。

Markdown 的角色：

- 适合标题、段落、列表和简单表格。
- 适合给 LLM 做语义理解。
- 适合作为人工阅读视图。

Markdown 的不足：

- 复杂表格、合并单元格、跨页表格、表头层级不稳定。
- 无法自然表达 bbox、页码坐标、图片区域。
- 一旦作为唯一中间表示，后续无法做精确溯源。

智谱数据提取实践指出，复杂表格可转为 Markdown 和 HTML，实践中建议使用 HTML 表示复杂表格，以更好保留表格结构并方便 LLM 理解。[来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

#### 5. 章节切分与语义分块

不要把全文 Markdown 直接塞进一次 LLM 请求。应先切分：

- 招标文件基本信息。
- 投标人须知。
- 资格审查。
- 符合性审查。
- 评标办法。
- 采购需求/技术规范。
- 商务条款。
- 合同条款。
- 投标文件格式。
- 附件清单。
- 电子提交规则。
- 暗标规则。
- 废标/否决条款。
- 补遗澄清。

每个 chunk 记录：

```json
{
  "chunk_id": "sec-eval-001",
  "section_path": "第三章 评标办法 > 技术评分",
  "pages": [31, 32],
  "source_blocks": ["p31-b01", "p31-t02"],
  "text": "...",
  "tables": ["p31-t02"],
  "chunk_type": "evaluation_criteria"
}
```

schema-constrained extraction 来源使用 page-level 和 caption-aware chunks，并将 chunk-level outputs 合并为 study-level records；这对投标文件同样适用：先按页/章节/表格抽，再汇总为项目级响应矩阵。[来源: https://link.springer.com/article/10.1186/s12874-026-02847-8]

#### 6. 分任务结构化抽取

建议将 LLM 抽取拆成 10 类任务，而不是一个 prompt 抽全篇：

1. `extract_project_info`：项目名称、编号、标段、招标人、代理、预算、采购方式。
2. `extract_timeline`：报名、答疑、保证金、投标截止、开标、交付、验收。
3. `extract_eligibility`：主体资格、资质、业绩、人员、财务、信誉、联合体。
4. `extract_evaluation`：评分办法、分值、公式、证明材料、响应建议。
5. `extract_mandatory_clauses`：废标、否决投标、无效投标、实质性响应。
6. `extract_procurement_needs`：范围、数量、参数、功能、服务、验收。
7. `extract_bid_document_requirements`：目录、分册、格式、签章、页码、装订、上传。
8. `extract_blind_bid_rules`：暗标范围、禁止标识、匿名化动作、元数据清理。
9. `extract_material_requirements`：营业执照、资质证书、业绩、人员、财务、承诺函。
10. `extract_contract_terms`：付款、质保、违约、交付、验收、保密、知识产权。

每个对象建议采用统一字段：

```json
{
  "id": "REQ-SCORE-003",
  "type": "evaluation_criteria",
  "title": "项目实施方案评分",
  "original_text": "实施方案完整、可行得 10 分...",
  "source": {
    "file": "招标文件.pdf",
    "page": 31,
    "section": "第三章 评标办法",
    "block_id": "p31-t02-r05"
  },
  "is_mandatory": false,
  "score": 10,
  "logic": {
    "operator": "AND",
    "conditions": []
  },
  "risk_level": "medium",
  "response_target": {
    "bid_section": "技术方案 > 项目实施方案",
    "materials": ["历史实施方案", "项目进度模板"]
  },
  "confidence": "high",
  "needs_human_review": true
}
```

#### 7. Schema 与结构化输出设计

结构化输出不应只靠“请输出 JSON”。应使用：

- JSON Schema / Pydantic / Zod。
- 枚举字段。
- 必填字段。
- 缺失值规则。
- 证据字段强制要求。
- 字段级置信度。
- 人工复核标记。
- 错误码和异常原因。

智谱数据提取文档强调字段定义、异常处理、结构化输出、JSON 标准化、数据格式化、逻辑校验、完整性校验和一致性校验；schema-constrained extraction 来源则进一步强调 typed schemas、controlled vocabularies、evidence-gated decisions 和 sentence-level provenance。[来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction][来源: https://link.springer.com/article/10.1186/s12874-026-02847-8]

#### 8. 后处理、合并与冲突处理

抽取不是结束。必须有后处理：

- JSON parse / repair。
- 字段类型转换。
- 日期标准化。
- 金额单位统一。
- 大写金额和数字金额比对。
- 分值合计校验。
- 投标截止时间与开标时间逻辑校验。
- 补遗/澄清覆盖旧条款。
- 同一字段多来源冲突合并。
- 低置信字段进入人工复核。

推荐合并规则：

```text
补遗/澄清 > 正式招标文件 > 招标公告 > 附件说明
人工确认 > 规则校验 > LLM 抽取
高置信结构化表格 > 普通正文推断
原文明确数值 > 模型推断值
```

schema-constrained extraction 来源提出 chunk-level outputs 应确定性合并为记录，对 scalar fields 做 conflict-aware handling，对 list-valued fields 做 set-based aggregation；投标 AI 可以迁移这套思想。[来源: https://link.springer.com/article/10.1186/s12874-026-02847-8]

#### 9. 响应矩阵生成

响应矩阵是从“抽取台账”走向“自动写标”的分水岭。

最低字段：

| 字段 | 说明 |
| --- | --- |
| 要求 ID | `REQ-QUAL-001`、`REQ-SCORE-003` |
| 要求类型 | 资格、评分、废标、采购需求、格式、暗标、材料、时间、合同 |
| 原文摘录 | 原文关键条款 |
| 原文位置 | 文件、页码、章节、表格单元格 |
| 是否强制 | 必须、加分、建议、格式、风险 |
| 响应章节 | 投标文件中的章节 |
| 所需材料 | 企业资质、人员、业绩、产品、承诺函等 |
| 企业匹配结果 | 满足、不满足、存疑、需补材料 |
| 责任人 | 商务、技术、法务、财务、资质管理员 |
| 风险等级 | 高、中、低 |
| 状态 | 未处理、已匹配、待补资料、待澄清、已确认、接受风险 |

没有响应矩阵，系统只能“抽信息”；有响应矩阵，系统才知道每条要求要进入哪个投标章节、引用什么企业材料、由谁确认。[来源: raw/articles/2026-06-16-投标AI助手招标文件解析与评审要素抽取调研.md]

#### 10. 企业资料库 / RAG 匹配

自动编写投标文件必须引入企业资料：

- 历史中标标书。
- 高分技术方案。
- 企业资质。
- 人员证书、社保、简历。
- 业绩合同、中标通知书、验收报告。
- 产品参数、检测报告、厂家授权、产品彩页。
- 服务承诺、售后体系、组织架构。
- 图片、架构图、流程图、PPT。
- 法规政策和行业标准。

RAG 检索建议：

```text
结构化硬过滤
  -> 权限过滤
  -> 有效期过滤
  -> BM25/关键词召回
  -> 向量召回
  -> rerank
  -> 证据片段返回
  -> LLM 基于证据生成
```

注意：

- 硬条件不能被相似度补偿。例如资质等级不满足、证书过期、主体不一致，不应因为语义相似就推荐通过。
- RAG 不只是搜索资料，还要避免引用过期、无权限、低质量、不适配项目的历史材料。
- 对每个生成段落保留引用资料和页码/文件位置。

ConfReady 论文说明，检查清单类回答若只靠 LLM 容易不可靠，RAG 可将回答 grounded in 上传的 TeX/PDF；投标文件的响应矩阵和评分点回答也属于类似的“检查清单 + 证据生成”任务。[来源: https://arxiv.org/html/2408.04675]

#### 11. 目录规划与分章节生成

生成投标文件不能“一键整本生成”。推荐流程：

1. 根据招标文件格式生成目录。
2. 将响应矩阵映射到目录章节。
3. 对每章绑定允许引用的企业资料。
4. 每章独立生成初稿。
5. 每章做覆盖率、事实、格式、引用检查。
6. 人工确认后进入总稿。

章节生成输入：

```json
{
  "section": "技术方案 > 项目实施方案",
  "requirements": ["REQ-SCORE-003", "REQ-TECH-012"],
  "allowed_assets": ["asset-history-plan-001", "asset-team-003"],
  "forbidden": ["不得编造人员", "不得承诺招标文件外的工期"],
  "output_format": "markdown",
  "evidence_required": true
}
```

#### 12. 结构化台账、Excel 和数据库 JSON 的关系

建议不要“LLM 直接输出 Excel”。推荐：

```text
LLM 结构化抽取
  -> JSON Schema 校验
  -> 规则校验
  -> 数据库主表/子表
  -> Excel 导出视图
  -> 人工修订
  -> 修订回写数据库
```

数据模型建议：

- `project_info`。
- `source_files`。
- `parsed_blocks`。
- `requirements`。
- `evaluation_criteria`。
- `mandatory_clauses`。
- `material_requirements`。
- `response_matrix`。
- `enterprise_assets`。
- `asset_matches`。
- `risks`。
- `review_records`。
- `generated_sections`。

Excel 适合作为：

- 读标解析台账。
- 资格/评分/废标清单。
- 响应矩阵。
- 材料缺口表。
- 风险关闭表。
- 人工复核表。

数据库/JSON 适合作为：

- 自动校验。
- 版本管理。
- API 对接。
- 权限控制。
- 证据链。
- 复盘沉淀。

#### 13. 审查与校验

机器校验：

- JSON schema 校验。
- 字段必填检查。
- 日期/金额格式校验。
- 投标截止时间、开标时间、保证金截止时间逻辑校验。
- 评分项分值合计。
- 最高限价、报价、保证金单位和金额校验。
- 资质等级、有效期、主体一致性校验。
- 人员证书、社保、劳动合同有效期校验。
- 材料完整性校验。
- 暗标公司名、logo、人员姓名、文件属性、图片水印检查。
- 补遗/澄清版本更新检查。
- 溯源检查：每条风险、建议、字段是否有原文位置。

人工复核：

- 商务负责人：资格、报价、保证金、商务条款。
- 技术负责人：采购需求、技术参数、实施范围、偏离表。
- 法务/合规：废标、合同、授权、联合体、分包、承诺边界。
- 资质管理员：企业证照、人员证书、业绩证明、有效期。
- 排版/投标专员：格式、签章、页码、附件顺序、暗标、电子平台上传。

智谱文档给出了格式校验、逻辑校验、完整性校验、一致性校验和修复模块的思路；本地投标 AI 调研则把这些校验具体化为资质、金额、日期、评分公式、废标、暗标和响应矩阵校验。[来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction][来源: raw/articles/2026-06-16-投标AI助手招标文件解析与评审要素抽取调研.md]

#### 14. 输出与交付

最终输出不应只有 Excel/JSON，还应包括：

- 招标文件解析报告。
- 响应矩阵。
- 资格/评分/废标/暗标/材料清单。
- 缺口清单和澄清问题。
- 投标文件目录。
- 分章节投标文件初稿。
- 技术偏离表、商务偏离表。
- 材料包和附件清单。
- 合规检查报告。
- 预评分或评分覆盖报告。
- Word/PDF 正式稿。
- 电子投标平台提交检查单。
- 归档复盘包。

### 四、是否需要“全文 Markdown 输入大模型”

推荐答案：需要 Markdown，但不建议“全文一次输入”。

适合全文 Markdown 的场景：

- 快速摘要。
- 简单项目字段抽取。
- 小文档一次性解析。
- 人工预览。

不适合全文一次输入的场景：

- 数百页招标文件。
- 附件/补遗/图纸很多。
- 表格复杂。
- 废标条款分散。
- 需要逐字段证据链。
- 需要后续自动写正文。

推荐做法：

```text
Markdown view 作为 LLM 阅读视图
HTML/table JSON 作为表格真相源
layout JSON 作为溯源真相源
chapter chunks 作为抽取输入
RAG index 作为生成检索输入
response matrix 作为规划真相源
```

### 五、可落地的技术架构

```text
前端项目工作区
  ├─ 文件上传 / 文件包管理 / 版本管理
  ├─ 解析结果预览：原文页、Markdown、表格、抽取字段、证据定位
  ├─ 响应矩阵 Excel-like 复核界面
  ├─ 章节生成与人工编辑
  └─ 风险关闭与导出

文档解析服务
  ├─ 文件类型识别
  ├─ 原生解析：docx/xlsx/html/pdf text
  ├─ OCR：扫描件/图片/低质 PDF
  ├─ layout/table/reading-order
  └─ 多表示存储：markdown/html/json/bbox

抽取服务
  ├─ schema registry
  ├─ 分任务 prompt / structured output
  ├─ JSON repair / schema validation
  ├─ field-level evidence
  └─ conflict merge

规则服务
  ├─ 日期/金额/分值/公式
  ├─ 资格/资质/有效期
  ├─ 废标/暗标/格式/签章
  ├─ 补遗澄清版本
  └─ 风险分级

资料与 RAG 服务
  ├─ 企业资质库 / 人员库 / 业绩库 / 产品库 / 历史标书库
  ├─ 权限 / 有效期 / 授权引用
  ├─ BM25 + vector + rerank
  └─ evidence chunks

生成服务
  ├─ 目录规划
  ├─ 分章节生成
  ├─ 偏离表/材料清单/澄清问题
  ├─ 风格统一
  └─ 引用补全

交付服务
  ├─ Word 模板
  ├─ PDF 导出
  ├─ Excel 台账
  ├─ 附件包
  └─ 提交检查单

审计与评测
  ├─ 操作日志
  ├─ 模型/提示词/规则版本
  ├─ 字段准确率 / 召回率 / 风险召回
  ├─ 人工修改量
  └─ 项目复盘
```

## 推荐工作流

### P0：最小可行版本

目标：验证“招标文件解析 + 响应矩阵”。

范围：

- 支持 PDF/Word 上传。
- 原生解析优先，扫描件 OCR。
- 输出 Markdown + 表格 HTML + 页码定位。
- 抽项目基础信息、时间节点、资格、评分、废标、材料。
- 输出 JSON 和 Excel 响应矩阵。
- 支持人工修改和确认。

验收指标：

- 项目基础信息字段准确率。
- 资格/废标/评分项召回率。
- 表格结构保真率。
- 每条抽取是否有页码证据。
- 人工修改量。

### P1：投标文件生成版

目标：从响应矩阵生成目录和章节初稿。

范围：

- 企业资料库：资质、人员、业绩、产品、历史方案。
- 资料按章节授权引用。
- 生成目录、技术方案、商务响应、偏离表、材料清单。
- 检查评分覆盖、废标、资质、暗标、格式。

底线：

- 不允许无证据生成资质、人员、业绩和承诺。
- 所有高风险字段必须人工确认。

### P2：企业级生产版

目标：支持多项目协作和正式交付。

范围：

- 多用户权限。
- 版本管理。
- 规则包配置。
- Word/PDF 模板导出。
- 签章、页码、附件顺序、暗标元数据检查。
- 审计日志和复盘回流。

### P3：智能优化版

目标：提高质量和可复用性。

范围：

- 评测集。
- OCR/解析模型对比。
- chunk 策略 A/B。
- RAG 召回与 rerank 评估。
- 风险召回率评估。
- 历史中标/失分反馈回流。

## 适用场景

- 招标文件页数多、附件多、扫描件多、表格复杂。
- 项目需要抽取资格、评分、废标、暗标、材料、合同和电子提交规则。
- 企业已有资质、人员、业绩、产品和历史标书资料库。
- 多部门协作写标，容易出现漏项、前后不一致和格式错误。
- 企业希望把投标经验沉淀为规则、模板和知识库。

## 不适用场景

- 招标文件很短、格式简单、人工半小时可处理。
- 企业没有真实资料库，却期望 AI 自动编造资质、业绩、人员和承诺。
- 项目高度依赖报价策略和商业判断，无法用结构化规则替代。
- 扫描件质量差到 OCR 和人工都难以确认关键条款。
- 企业不愿维护 schema、规则、资料有效期、复盘和人工确认流程。

## 风险与约束

1. OCR 误识别风险：数字、金额、日期、证书编号、项目编号、表格行列最容易造成高风险错误，必须保留原文页码和人工复核。[来源: https://arxiv.org/html/2507.05595]
2. Markdown 压扁结构风险：复杂表格、跨页表格、合并单元格和图纸信息不能只靠 Markdown，应保留 HTML/table JSON/layout bbox。[来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
3. 全文一次输入风险：长招标文件会造成上下文稀释和漏项，应按章节、任务和证据链分解。[来源: https://link.springer.com/article/10.1186/s12874-026-02847-8]
4. 结构化输出幻觉风险：JSON 格式正确不等于事实正确，必须强制原文证据和规则校验。[来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
5. RAG 污染风险：过期、无权限、低分、行业不匹配的历史标书会放大错误经验，必须做资料治理。[来源: raw/articles/2026-06-15-ai-bid-document-assistant-research.md]
6. 响应矩阵缺失风险：没有响应矩阵，系统无法证明每个评分点、资格项和废标项都有响应。[来源: raw/articles/2026-06-16-投标AI助手招标文件解析与评审要素抽取调研.md]
7. 责任边界风险：AI 不能替代商务、技术、法务、资质和投标负责人做最终确认。[来源: raw/articles/2026-06-15-ai-bid-document-assistant-research.md]
8. 供应商宣传风险：部分厂商声称效率提升、中标率提升等数字缺少第三方验证，本报告不采信为事实结论。

## 信源质量门控记录

### 门控规则

- A 级：学术论文、官方文档、本地已编译高质量调研，可支撑核心结论。
- B 级：产品官网、云平台社区技术文章，可支撑产品形态和实践参考，但营销指标需降权。
- C 级：推广文章、社区经验、SEO 页面，只作背景，不单独支撑核心事实。
- D 级：抓取失败、正文为空、反爬页面、明显低相关或重复来源，剔除。
- C/D 级来源不得作为唯一核心结论依据。
- 入库映射：A/B -> `source-quality: high`；C -> `source-quality: medium`；D -> `source-quality: low`。

### 保留信源

1. [投标AI助手招标文件解析与评审要素抽取调研](raw/articles/2026-06-16-投标AI助手招标文件解析与评审要素抽取调研.md)
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：本地专题调研，直接覆盖招标文件解析、OCR 边界、评分/废标/暗标/材料抽取和响应矩阵。
   - 后续处理：作为投标 AI 专用链路主依据。

2. [国内 AI 标书助手能力、坑点与标准 SOP 调研](raw/articles/2026-06-15-ai-bid-document-assistant-research.md)
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：本地专题调研，覆盖 AI 标书助手能力、SOP、坑点、知识库和人工终审边界。
   - 后续处理：作为自动写标闭环依据。

3. [通用复杂文档 AI 平台能力抽象与产品架构调研](raw/articles/2026-06-15-general-complex-document-ai-platform-architecture-research.md)
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：本地专题调研，覆盖 Document AI、RAG、Structured Outputs、证据链、规则审查和复杂文档工厂架构。
   - 后续处理：作为平台化架构依据。

4. [Docling Technical Report](https://arxiv.org/html/2408.09869v3)
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术/技术报告，说明 PDF 转 JSON/Markdown、layout analysis、table structure recognition、reading order 和可选 OCR。
   - 后续处理：作为“Markdown 不是唯一真相源、解析层应保留 layout/table”的依据。

5. [PaddleOCR 3.0 Technical Report](https://arxiv.org/html/2507.05595)
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：OCR/文档解析技术报告，说明 OCR 在 LLM/RAG 时代从文字识别升级为文档理解基础设施。
   - 后续处理：作为 OCR/Layout/Table/Key Information Extraction 分层依据。

6. [智谱 AI 数据提取最佳实践](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction)
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档，直接覆盖招投标数据抽取、多格式输入、预处理、表格处理、Prompt、JSON、后处理和校验。
   - 后续处理：作为结构化抽取和校验模块依据。

7. [ConfReady: A RAG based Assistant and Dataset for Conference Checklist Responses](https://arxiv.org/html/2408.04675)
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文，说明 RAG 可以让 checklist responses grounded in 上传的 PDF/TeX，适合类比投标响应矩阵和评分点回答。
   - 后续处理：作为“检查清单类任务需要 RAG 而非纯生成”的依据。

8. [From chaos to clarity: schema-constrained AI for auditable biomedical evidence extraction from full-text PDFs](https://link.springer.com/article/10.1186/s12874-026-02847-8)
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：同行评审文章，说明 schema-constrained extraction、typed schema、controlled vocabulary、chunk-level outputs、sentence-level provenance、CSV/Parquet 和 markdown reconstruction。
   - 后续处理：作为生产级结构化抽取、证据链和可审计输出依据。

9. [喜鹊标书 AI](https://www.xiquebiaoshu.com)
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：产品官网，可作为市场产品形态背景。
   - 后续处理：只作背景，不单独支撑核心技术结论。

10. [高效速搭基于 DeepSeek 的招标文书智能写作 Agent](https://cloud.tencent.com/developer/article/2498790)
    - 来源等级：C
    - 入库映射：`source-quality: medium`
    - 保留原因：社区文章，覆盖 Agent、RAG、Markdown 输出和工作流配置，但包含未验证模型指标和推广性内容。
    - 后续处理：仅作实践背景，不采信营销数字。

### 剔除或降权信源

- [https://arxiv.org/pdf/2509.11937](https://arxiv.org/pdf/2509.11937)：精读内容为空/不匹配，仅返回无实际正文，剔除。
- [Qianfan-OCR](https://arxiv.org/pdf/2603.13398v1)：精读内容为空/不匹配，未用于核心结论。
- Mistral Document AI、华为云 OCR、阿里云文档智能等来源因本次 Tavily 分数低于阈值未纳入核心证据；若后续需要做供应商选型，可单独调研。
- 多个招投标 AI 产品页和社区文章因分数低、重复、推广性强，仅作为背景或剔除。
- 腾讯云 DeepSeek Agent 文章中的 DeepSeek 与 OpenAI 精度对比等数字缺少原始白皮书验证，本报告不采信。

## 来源与可信度

| 来源 | 类型 | 可信度 | 主要支撑内容 |
| --- | --- | --- | --- |
| 本地投标 AI 解析调研 | 本地 raw 调研 | 高 | OCR 边界、评分/废标/暗标/材料抽取、响应矩阵 |
| 本地 AI 标书助手 SOP 调研 | 本地 raw 调研 | 高 | 标书助手能力、RAG、分章节生成、合规检查 |
| 本地复杂文档平台调研 | 本地 raw 调研 | 高 | Document AI、RAG、结构化输出、证据链、平台架构 |
| Docling Technical Report | 技术报告/论文 | 高 | PDF 转 Markdown/JSON、layout、table、reading order |
| PaddleOCR 3.0 | 技术报告/论文 | 高 | OCR、层级文档解析、关键信息抽取 |
| 智谱数据提取 | 官方文档 | 高 | 招投标字段抽取、Prompt、JSON、后处理、校验 |
| ConfReady | 学术论文 | 中高 | RAG 支撑 checklist responses，类比响应矩阵 |
| BMC schema-constrained extraction | 同行评审论文 | 高 | schema 约束、chunk、provenance、CSV/Parquet、审计 |
| 喜鹊标书 AI | 产品官网 | 中 | 产品能力背景 |
| 腾讯云 DeepSeek Agent 文章 | 社区文章 | 低到中 | Agent/RAG/Markdown 实践背景，数字需验证 |

## 对于可信度较高的来源逐来源总结

### 1. 本地《投标AI助手招标文件解析与评审要素抽取调研》

该来源直接回答了 OCR 是否需要、OCR 后是否还需要 LLM、是否主要靠提示词等问题。它的核心结论是：标准投标 AI 助手入口不是写标书，而是读标解析；OCR 是复杂文件基础设施之一，但不应无差别替代原生解析；OCR 后仍然需要 LLM 做语义抽取和风险解释；系统不能主要依赖提示词，而应包含 schema、规则库、企业资料库、响应矩阵、证据链、校验器和人工复核。[来源: raw/articles/2026-06-16-投标AI助手招标文件解析与评审要素抽取调研.md]

可用事实：

- OCR 适用于扫描件、图片、盖章页、复杂表格、图纸等。
- Word、Excel、可复制文本 PDF 应优先保留原生结构。
- 评分标准、废标项、资质要求必须作为一等对象进入响应矩阵。
- LLM 不应单独裁决报价、资质、废标、法律风险和承诺边界。

局限：

- 主要面向投标 AI 助手，通用 Document AI 细节需外部技术来源补充。

适合入库知识点：

- 投标 AI 助手解析链路。
- 响应矩阵。
- OCR 与 LLM 分工。

### 2. Docling Technical Report

Docling 是 PDF 文档转换工具，支持将 PDF 转为 JSON 或 Markdown，并理解详细页面布局、阅读顺序、图像定位和表格结构，也可选择性开启 OCR。[来源: https://arxiv.org/html/2408.09869v3]

可用事实：

- PDF 转 machine-processable format 很难，因为 PDF 面向打印展示，结构和元数据弱。
- 面向 LLM/RAG 的 PDF 利用需要文档转换工具。
- Docling 支持 layout analysis 和 table structure recognition。
- Docling 可输出 JSON/Markdown。

局限：

- 不是专门面向投标文件，但对 PDF 解析链路有强参考价值。

适合入库知识点：

- PDF 到 Markdown/JSON。
- 文档解析多表示。
- Layout/table 解析。

### 3. PaddleOCR 3.0 Technical Report

PaddleOCR 3.0 将 OCR 与文档解析、关键信息抽取结合，提出 PP-OCRv5、PP-StructureV3、PP-ChatOCRv4 三个方案，面向 LLM 时代的 OCR 和文档理解。[来源: https://arxiv.org/html/2507.05595]

可用事实：

- OCR 不再只是文字转写，而是高质量数据构造、知识抽取和视觉层到语义层的桥梁。
- 现代 OCR 需要处理多语言、复杂布局、表格、手写、艺术字体、特殊符号、图表和印章。
- OCR/文档解析应考虑部署效率和异构硬件。

局限：

- 证据包精读内容较短，未覆盖全文细节。

适合入库知识点：

- OCR 在 LLM/RAG 时代的定位。
- 层级文档解析。
- 文档关键信息抽取。

### 4. 智谱 AI 数据提取最佳实践

该官方文档直接以招投标数据提取为场景，说明招投标文件格式复杂、表格嵌套、金额大小写并存、字段分散，传统 OCR/规则工具常出现字段缺失和表格识别错误；其方案包含多格式输入、预处理、表格解析、Prompt 字段定义、结构化 JSON 输出、JSON 修复、格式/逻辑/完整性/一致性校验和数据修复。[来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

可用事实：

- 输入应支持 PDF、Word、Excel、网页、扫描图片。
- 预处理要做文本清洗、规范化、分段分块、表格解析、上下文维护。
- 复杂表格建议用 HTML 表示。
- Prompt 应明确字段定义、异常处理和结构化输出。
- 后处理和校验是流程的一部分，不是可选项。

局限：

- 是厂商官方文档，示例和平台能力需结合实际产品验证。

适合入库知识点：

- 招投标字段抽取。
- JSON 后处理。
- 表格 HTML 表示。
- 数据校验模块。

### 5. Schema-constrained AI extraction 论文

该论文面向生物医学 PDF 证据抽取，提出 schema-constrained AI extraction：使用 typed schemas、controlled vocabularies、evidence-gated decisions，将 PDF 分成 page-level 和 caption-aware chunks，异步处理，再把 chunk-level outputs 确定性合并为 study-level records，并保留 sentence-level provenance，最终输出 CSV/Parquet 和 multimodal markdown reconstructions。[来源: https://link.springer.com/article/10.1186/s12874-026-02847-8]

可用事实：

- 对复杂 PDF 做结构化抽取应采用 schema 约束，而不是任意生成。
- chunk 级输出要确定性合并。
- 字段冲突要显式处理。
- list 字段适合集合聚合。
- sentence-level provenance 支撑审计。
- 人可读 Markdown 和机器可用结构化数据可以并存。

局限：

- 领域是生物医学证据抽取，不是招投标；但技术模式可迁移。

适合入库知识点：

- Schema-constrained extraction。
- Evidence provenance。
- Chunk merge。
- CSV/Parquet/Markdown 双表示。

### 6. ConfReady RAG 论文

ConfReady 是帮助论文作者填写会议 checklist 的 RAG 助手，支持上传 TeX source 或 PDF，由 RAG 生成 checklist responses 并允许用户修改和导出。论文指出，单纯 LLM checklist assistant 未充分反映真实提交复杂性，RAG 可提升准确性和相关性。[来源: https://arxiv.org/html/2408.04675]

可用事实：

- checklist 类型任务需要 grounded in source documents。
- 上传源文档后，RAG 能辅助生成需要证据支撑的回答。
- 生成结果仍应允许用户修改和导出。

局限：

- 任务是学术 checklist，不是投标响应矩阵；属于类比迁移。

适合入库知识点：

- Checklist RAG。
- 响应矩阵类任务的 RAG grounding。

## 跨源矛盾检测结论

### 检测范围

- 已纳入分析来源：10 个，其中核心来源 8 个。
- 检测对象：OCR/解析功能描述、Markdown/JSON 角色、结构化输出、RAG 必要性、校验方式、人工复核边界、产品能力声明。
- 检测时间：2026-06-17。

### 检测结果

结论：未检测到需要保留为事实冲突的核心矛盾。各来源在抽象层级上不同，但方向一致：

- Docling/PaddleOCR 强调文档解析不是单纯 OCR。
- 智谱和 schema-constrained extraction 强调 schema、后处理、校验和证据。
- 本地投标 AI 调研强调响应矩阵、RAG、规则审查和人工复核。
- 产品/社区文章强调自动生成、Markdown 和 Agent/RAG，但其营销数字和模型指标需降权。

### 需要降权处理的差异

1. 社区文章对 DeepSeek 的性能数字和“中文语义理解精准度”等说法缺少可验证原始来源，不作为事实结论。
2. 产品官网/厂商文章描述“一键写标”能力，但本地多源调研和高风险文档证据均支持“分章节生成 + 人工终审”更稳妥。
3. “Markdown 输出”在社区实践中被描述为格式控制能力，但 Docling/智谱/BMC 来源显示生产系统仍应保留 layout/table/json/provenance，而不能只保留 Markdown。

## 矛盾与待验证问题

1. 具体 OCR/Document AI 工具选型未在本报告中完成。Docling、PaddleOCR、云厂商 Document AI、国内 OCR 服务各有成本、私有化、中文表格、印章、图纸、批量性能差异，需用真实招标文件做 POC。
2. 复杂表格的最优表示需要测试。理论上 HTML/table JSON 优于 Markdown，但不同 LLM 对 HTML/Markdown/CSV 的理解效果需实测。
3. 自动生成投标正文的质量高度依赖企业资料库质量。本报告没有验证具体企业知识库的资料覆盖率。
4. 响应矩阵字段 schema 应按行业细化。工程、IT、设备、物业、咨询服务类招标字段差异明显。
5. Excel 复核界面是否足够，需要结合用户操作习惯验证；复杂项目可能需要 Web 表格和证据页联动，而不只是下载 Excel。
6. 暗标、签章、电子投标平台提交规则高度地域化，必须按项目原文和平台测试环境验证。

## 原始证据摘录

> Docling “Converts PDF documents to JSON or Markdown format”，并能理解页面布局、阅读顺序、定位 figures、恢复 table structures，OCR 是可选功能。[来源: https://arxiv.org/html/2408.09869v3]

> PaddleOCR 3.0 提出 PP-OCRv5、PP-StructureV3、PP-ChatOCRv4，分别面向多语言文本识别、层级文档解析和关键信息抽取。[来源: https://arxiv.org/html/2507.05595]

> 智谱数据提取文档指出，传统 OCR 或规则提取面对 PDF 格式混乱、表格嵌套、金额大小写并存时效果不理想，仍需人工二次校验。[来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

> 智谱文档建议复杂表格可转换为 Markdown 和 HTML，实践中建议使用 HTML 表示复杂表格，以保留表格结构并方便 LLM 理解。[来源: https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

> Schema-constrained extraction 论文使用 typed schemas、controlled vocabularies、evidence-gated decisions、page-level chunks、sentence-level evidence capture，将 PDF 转为结构化可审计记录。[来源: https://link.springer.com/article/10.1186/s12874-026-02847-8]

> ConfReady 将 RAG 用于基于论文源文件/PDF 的 checklist responses，以提升准确性和相关性。[来源: https://arxiv.org/html/2408.04675]

