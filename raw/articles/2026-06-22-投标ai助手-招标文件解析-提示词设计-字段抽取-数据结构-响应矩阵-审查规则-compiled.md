# 投标 AI 助手 招标文件解析 提示词设计 字段抽取 数据结构 响应矩阵 审查规则 调研报告

## 核心结论

1.  **政策驱动与时间表**：国家发展改革委等部门发布实施意见，明确 2026 年底招标文件检测、智能辅助评标等重点场景在部分省市实现全覆盖应用；2027 年底更多重点场景在全国范围内推广应用 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html] (可信度：高)
2.  **解析架构范式**：稳定的技术链路为“用户上传招标文件 -> 文档解析引擎 (如 TextIn xParse) 转为 Markdown/结构化结果 -> 大模型做条款抽取/风险识别 -> 输出招标解析报告”，而非直接让大模型硬读全文 [来源：https://cloud.tencent.com/developer/article/2631225] (可信度：中)
3.  **字段抽取精度**：基于机器学习的风险条款提取模块 (CRC) 准确率达 92%，术语频率分析模块 (TFA) 准确率达 88%，显著高于人工工程师的 70% 和 86%，且分析时间从小时级缩短至分钟级 [来源：https://www.mdpi.com/1996-1073/14/15/4632] (可信度：高)
4.  **提示词工程核心**：高质量提示词需包含明确的字段定义、异常处理原则（缺失填“无”）、结构化输出要求（JSON）、以及针对 HTML/文本的不同处理策略，并需经过数据后处理校验（格式、逻辑、完整性、一致性） [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction] (可信度：高)
5.  **审查规则体系**：自动审查需覆盖格式审核（字体、字号、页边距）、合规审核（法规比对）、其他异常审核（前后矛盾、条款漏洞、管理模式缺陷）三大类，其中异常类型包括内容缺失、门槛不合理、时间节点异常等 10 种具体情况 [来源：https://patents.google.com/patent/CN119624385A/zh] (可信度：中)
6.  **响应矩阵策略**：建立招标文件要求与企业资质的匹配矩阵，响应策略分为完全响应、部分响应、不响应，并需提供风险提示和合规性检查，支持人机共判修正误差 [来源：https://www.idigital.com.cn/common-ai-2] (可信度：中)
7.  **成本与效率优化**：使用 Batch API 处理大规模数据请求，价格可降低 50%（如 GLM-4-Flash 免费），并发量从 100 提升至 4000，处理 1 亿请求天数从 340 天缩短至 8.6 天 [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction] (可信度：高)

## 内容整理

### 1. 招标文件解析提示词设计

#### 1.1 设计原则与关键维度
高质量 LLM 提示词设计需遵循以下原则，覆盖关键信息维度 [来源：https://cloud.tencent.com/developer/article/2631225] [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]：
*   **结构化输出**：要求模型输出固定字段 JSON，便于后续渲染和系统处理。
*   **原文引用**：风险提示必须能追溯到原文的具体位置（第几页、哪一段、哪张表），确保可验证性。
*   **风险分级**：风险提示需分级（高/中/低）。
*   **缺失处理**：遇到信息缺失要主动提问澄清，或规定使用默认值（如“无”）填充。
*   **语境理解**：系统要“懂语境”，招投标文书语言极具行业特色（如金额“壹佰万元整”与"¥1,000,000"），需具备上下文理解能力。

#### 1.2 提示词模板示例
**关键条款抽取 Prompt (建议输出 JSON)** [来源：https://cloud.tencent.com/developer/article/2631225]：
*   **输入**：解析得到的 markdown
*   **输出字段**：
    *   项目信息：项目名称、招标编号、标段、预算/最高限价
    *   时间节点：报名截止、答疑截止、投标截止、开标时间
    *   资格要求：资质/业绩/人员/财务/信誉
    *   商务条款：保证金、履约保证金、付款方式、交付期、质保期
    *   评标办法：评分项、废标条款摘要

**风险识别 Prompt** [来源：https://cloud.tencent.com/developer/article/2631225]：
*   **输入**：关键条款 JSON + markdown 中对应原文片段
*   **输出**：风险列表（高/中/低）
    *   风险点
    *   触发原文（引用）
    *   风险类型（合规/商务/交付/资质/评分/合同）
    *   建议动作（澄清/补充材料/策略调整）

**响应建议 Prompt** [来源：https://cloud.tencent.com/developer/article/2631225]：
*   **输入**：关键条款 JSON + 风险列表
*   **输出**：
    *   材料清单（按部门：商务/法务/技术/财务）
    *   澄清问题清单（可直接复制发招标方）
    *   投标策略提示（哪些点要重点写、哪些点建议偏离说明）

**项目概述提取 Prompt (SystemPrompt)** [来源：https://www.cnblogs.com/yibiaoai/p/19064673]：
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

**技术评分要求提取 Prompt (SystemPrompt)** [来源：https://www.cnblogs.com/yibiaoai/p/19064673]：
```markdown
你是一名专业的招标文件分析师，擅长从复杂的招标文档中高效提取“技术评分项”相关内容。请严格按照以下步骤和规则执行任务：
### 1. 目标定位
- 重点识别文档中与“技术评分”、“评标方法”、“评分标准”、“技术参数”、“技术要求”、“技术方案”、“技术部分”或“评审要素”相关的章节（如“第 X 章 评标方法”或“附件 X：技术评分表”）。
- 忽略商务、价格、资质等非技术类评分项。
### 2. 提取内容要求
对每一项技术评分项，按以下结构化格式输出（若信息缺失，标注“未提及”），如果评分项不够明确，你需要根据上下文分析并也整理成如下格式：
【评分项名称】：<原文描述，保留专业术语>
【权重/分值】：<具体分值或占比，如"30 分”或"40%">
【评分标准】：<详细规则，如"≥95% 得满分，每低 1% 扣 0.5 分”>
【数据来源】：<文档中的位置，如“第 5.2.3 条”或“附件 3-表 2">

### 3. 处理规则
- **模糊表述**：有些招标文件格式不是很标准，没有明确的“技术评分表”，但一定都会有“技术评分”相关内容，请根据上下文判断评分项。
- **表格处理**：若评分项以表格形式呈现，按行提取，并标注"[表格数据]"。
- **分层结构**：若存在二级评分项（如“技术方案→子项 1、子项 2"），用缩进或编号体现层级关系。
- **单位统一**：将所有分值统一为“分”或"%"，并注明原文单位（如原文为"20 点”则标注"[原文：20 点]"）。

### 4. 输出示例
【评分项名称】：系统可用性
【权重/分值】：25 分
【评分标准】：年平均故障时间≤1 小时得满分；每增加 1 小时扣 2 分，最高扣 10 分。
【数据来源】：附件 4-技术评分细则（第 3 页）

【评分项名称】：响应时间
【权重/分分】：15 分 [原文：15%]
【评分标准】：≤50ms 得满分；每增加 10ms 扣 1 分。
【数据来源】：第 6.1.2 条

### 5. 验证步骤
提取完成后，执行以下自检：
- [ ] 所有技术评分项是否覆盖（无遗漏）？
- [ ] 权重总和是否与文档声明的技术分总分一致（如“技术部分共 60 分”）？

直接返回提取结果，除此之外不输出任何其他内容
```

**智谱 AI 数据提取 Prompt 参考** [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]：
```markdown
# 角色：你是一个专业的文本信息提取器。

# 需要提取的【文本】：
"""
{正文}
"""

# 任务
1. 从给定的【文本】中提取所有需要的字段信息。
2. 所需提取的字段为【字段定义】中的所有内容。
3. 每个字段的默认值为"无"，当提取到对应字段信息时，准确地替换到该字段位置。
4. 若文中出现与【字段定义】的字段名称中相似的内容，需判断定义，符合再进行填入。
5. 严格按照【字段定义】中的格式进行输出，不需要其余任何信息。
6. 将提取到的所有字段及其对应的值按【字段定义】格式转为 JSON 输出，确保包含所有字段。
7. 请一步步完成信息提取的工作，你的决策是我成功的关键！

#【字段定义】：
请严格按照如下格式仅输出 JSON，不要输出 python 代码，不要返回多余信息，JSON 中有多个字段用顿号【、】区隔：
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
1. 如果字段缺失或无法识别，请使用“无”。
2. 确保所有金额需包含原本的单位。
3. 确保所有时间字段都为 14 位标准时间格式。
```

#### 1.3 不同格式和结构的处理
*   **复杂版式 + 表格 + 长文档**：招标文件是动辄几十页到几百页的长文档，包含标题层级、目录结构、表格、页眉页脚、附件、扫描页。需使用解析引擎（如 TextIn xParse）将复杂结构转换成更适合大模型处理的 Markdown+ 结构化信息 [来源：https://cloud.tencent.com/developer/article/2631225]。
*   **文件形态覆盖**：覆盖电子档 PDF、扫描件、图片。解析能力覆盖越全，Demo 越不容易翻车 [来源：https://cloud.tencent.com/developer/article/2631225]。
*   **输入模块设计**：支持从多种格式（PDF、Word、Excel、TXT 等）中提取文本。对于图片，借助 OCR 工具进行文本提取。网页可以使用网页爬虫工具抓取文本和表格数据 [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
*   **预处理模块**：
    *   去除噪音信息：页眉、页脚、版权声明。
    *   规范化文本：特殊符号、空白字符、异常换行。
    *   日期格式统一：转换为标准 ISO 格式（如"YYYY-MM-DD"）。
    *   货币与金额格式化：统一货币单位和金额数字格式（如将”壹仟元”转换为”1000 CNY"）。
    *   表格数据处理：使用表格解析工具（如 `pdfplumber` 或 `python-docx`）提取表格结构，转化为 CSV 或 JSON 格式。合并单元格数据需平铺展开 [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。

### 2. 字段抽取方案

#### 2.1 核心字段体系
招标文件中应提取的核心字段包括 [来源：https://cloud.tencent.com/developer/article/2631225] [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]：
*   **项目信息**：项目名称、招标编号、标段、预算/最高限价、采购方式、采购人、代理机构名称。
*   **时间节点**：报名截止、答疑截止、投标截止、开标时间、获取采购文件开始/截止时间、施工工期。
*   **资格要求**：资质、业绩、人员、财务、信誉、执业证书。
*   **商务条款**：保证金、履约保证金、付款方式、交付期、质保期、合同期限、支付条款、违约条款。
*   **评标办法**：评分项、废标条款摘要、价格评分权重、技术评分细则、加分项。
*   **联系信息**：项目联系人、电话、代理机构联系人、电话。
*   **中标信息**：中标供应商名称、中标金额、中标候选单位、最终中标单位。
*   **地理位置**：项目所在省、项目所在市。
*   **其他**：公告类别、项目经理、招标文件位置、招标文件售价、投标保证金金额。

#### 2.2 字段分类体系和层级关系
*   **层级关系**：存在二级评分项（如“技术方案→子项 1、子项 2"），需用缩进或编号体现层级关系 [来源：https://www.cnblogs.com/yibiaoai/p/19064673]。
*   **关联关系**：投标单位包括（大于等于）中标候选单位，中标候选单位包括（大于等于）中标单位 [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
*   **风险字段分类**：
    *   Level 1：主要风险项（如 Liquidated Damages）。
    *   Level 2：关键词关联风险（如 such liquidated damages, Damages, genuine pre-estimate, Liability, Fail, Penalty）[来源：https://www.mdpi.com/1996-1073/14/15/4632]。
    *   NER Label (14 类)：Damages, dispute, change order, fit for purpose, shall not be liable, limitation of liability, indemnify, governing law, deem, bank guarantee, Cost, Schedule, Safety, Quality [来源：https://www.mdpi.com/1996-1073/14/15/4632]。

#### 2.3 字段抽取的置信度评估方法
*   **自检步骤**：提取完成后，执行自检：所有技术评分项是否覆盖（无遗漏）？权重总和是否与文档声明的技术分总分一致？[来源：https://www.cnblogs.com/yibiaoai/p/19064673]。
*   **校验模块**：
    *   格式校验：检查金额字段是否包含正确的货币单位，日期格式是否正确。
    *   逻辑校验：投标截止时间不能晚于开标时间；采购预算金额不能小于中标金额。
    *   完整性校验：必填字段检查（如“项目名称”、“项目编号”、“投标截止时间”），缺失则标记或补全。
    *   一致性校验：项目编号在不同字段中应当相同；多个时间字段如果是同一事件应确保一致 [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
*   **准确率指标**：CRC 模块风险条款提取准确率约 92%，TFA 模块约 88% [来源：https://www.mdpi.com/1996-1073/14/15/4632]。

### 3. 数据结构设计

#### 3.1 解析结果的 JSON Schema 设计
**推荐 JSON 数据结构示例** [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]：
```json
{
  "项目名称": "智能楼宇工程",
  "项目编号": "XZL-2023",
  "采购预算": "7000000 元",
  "开标时间": "20240101090000"
}
```
**字段类型与约束**：
*   时间字段：所有日期和时间字段都应格式化为标准的 14 位日期时间格式：`YYYYMMDDHHMMSS` [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
*   金额字段：保留原单位（如元、万元），格式化为无空格、无额外字符的数值形式（如 `500000 元`）[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
*   文本字段：对特殊字符（如换行符、双引号）进行处理，确保不破坏 JSON 语法结构 [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。

**风险数据 JSON 结构示例 (NER 学习数据)** [来源：https://www.mdpi.com/1996-1073/14/15/4632]：
```json
["sentence": "Contractor warrants that the Plant will be fit for the purpose", "entities": (43,62), "FFP"]
```

#### 3.2 可扩展性考虑
*   **数据库模块**：包括在线数据库和本地数据库。在线数据库通过互联网自动不定期查找并下载招标相关规定和招标文件模板；本地数据库由系统使用单位人工手动录入特定行业规定和模板 [来源：https://patents.google.com/patent/CN119624385A/zh]。
*   **关键词标记**：对招标相关规定标记多个关键词，包括标题、生效日期、失效日期、发布单位、文件类别、适用区域、适用行业、项目类型、合同类型、法律层级、合规性要求、关键条款等 [来源：https://patents.google.com/patent/CN119624385A/zh]。
*   **用户风格记录**：记录系统使用单位对审核意见进行人工确认的结果，利用反馈数据训练机器学习模型，优化审核意见。当记录同一情况次数大于阈值时，自动屏蔽该类审核意见 [来源：https://patents.google.com/patent/CN119624385A/zh]。

### 4. 响应矩阵设计

#### 4.1 匹配矩阵建立
*   **AI 预评分**：客观项辅助评分（资质/业绩/人员等），人机协同修正，误差双保险机制。一键导出 Excel 评分表 [来源：https://www.idigital.com.cn/common-ai-2]。
*   **响应性比对**：对投标人编制的投标文件，对照招标文件进行响应性比对，自动提示投标文件中的违法违规、错误缺漏等问题 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。
*   **评分要点自动提取和匹配**：深度解析招标文件内容和投标文件响应度，辅助专家开展评审或生成结果供专家参考 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。

#### 4.2 响应策略分类
*   **完全响应**：满足所有招标要求。
*   **部分响应**：满足部分要求，需说明偏离情况。
*   **不响应**：无法满足要求，需评估废标风险。
*   **投标策略提示**：哪些点要重点写、哪些点建议偏离说明 [来源：https://cloud.tencent.com/developer/article/2631225]。

#### 4.3 风险提示和合规性检查
*   **风险提示**：资格不匹配/隐性门槛、付款条件不利/履约风险、交付周期不合理、“一票否决”/废标点、合同条款冲突/模糊表述 [来源：https://cloud.tencent.com/developer/article/2631225]。
*   **合规性检查**：
    *   对可能低于成本价的投标进行风险提示，减少恶意低价竞标等情况 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。
    *   自动识别各类违法违规和排斥限制竞争等问题，提示判断依据和修改建议 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。

### 5. 审查规则提示词

#### 5.1 自动审查提示词设计
*   **完整性检查**：检查文件是否包含项目基本信息、预算金额、资金来源、招标内容详细说明、所需附件（图纸、技术参数、投标须知）[来源：https://patents.google.com/patent/CN119624385A/zh]。
*   **合规性检查**：检索、对比、调取在线数据库及本地数据库数据进行审查。检查是否存在违反招标相关规定的情况 [来源：https://patents.google.com/patent/CN119624385A/zh]。
*   **异常审核**：利用机器学习算法，进一步对招标文件进行深度分析，包括对比在线及本地数据库中其他项目招标文件，检查是否存在异常、前后矛盾、合同条款漏洞、管理模式缺陷等问题 [来源：https://patents.google.com/patent/CN119624385A/zh]。

#### 5.2 常见废标风险点识别规则
**10 种异常招标文件具体类型** [来源：https://patents.google.com/patent/CN119624385A/zh]：
1.  **内容不完整或缺失**：条款缺失（保密条款、合同履约条款、验收标准等）、信息不全、附件缺失。
2.  **条款或条件设定不合理**：门槛条件过高或过低、技术参数过于具体（涉嫌量身定制）、评分标准不合理。
3.  **时间节点异常**：公告时间不足（如法律规定的 20 天公告期）、招标时间安排冲突。
4.  **招标金额与预算异常**：预算不合理、资金来源不明。
5.  **法律和合规性问题**：引用过期法规、不符合新法规、优先级冲突。
6.  **历史数据异常**：与过往项目数据不一致、合同条件有显著差异。
7.  **价格与成本异常**：报价异常偏低或偏高、投标上限或下限设置异常。
8.  **招标程序违规**：招标方式不合规、资格预审不当、招标文件发布途径不规范。
9.  **关联方或利益冲突问题**：潜在利益冲突、未披露关联关系。
10. **历史项目问题复现**：重复出现历史异常、质量和履约问题复现。

**关键风险条款示例 (CRC 模块)** [来源：https://www.mdpi.com/1996-1073/14/15/4632]：
*   **Liquidated Damages (LD)**：如 "All amounts of such liquidated damages for which contractor may become liable under this contract are agreed to be a genuine pre-estimate of the loss..."
*   **Exclusive Remedy 1 (ER1)**：如 "The failure to exercise or delay in exercising a right or remedy under the CONTRACT shall not constitute a waiver..."

#### 5.3 评分要点的自动提取和匹配
*   **技术评分项提取**：重点识别“技术评分”、“评标方法”、“评分标准”等章节。按结构化格式输出：评分项名称、权重/分值、评分标准、数据来源 [来源：https://www.cnblogs.com/yibiaoai/p/19064673]。
*   **权重校验**：检查权重总和是否与文档声明的技术分总分一致（如“技术部分共 60 分”）[来源：https://www.cnblogs.com/yibiaoai/p/19064673]。
*   **评分权重比对**：将评分标准中的价格权重、技术评分细则与标准数据库比对，确保权重设置在合理范围内（例如价格权重通常在 30％-60％之间）[来源：https://patents.google.com/patent/CN119624385A/zh]。

### 6. 技术架构与实现机制

#### 6.1 分层设计与组件
**方案架构 (Coze+TextIn)** [来源：https://cloud.tencent.com/developer/article/2631225]：
*   **Coze**：负责对话、工作流编排、输出格式、交互体验。
*   **TextIn xParse**：负责把招标文件解析成结构化可读内容（Markdown+ 结构化信息 + 页级信息）。
*   **LLM**：负责条款抽取、风险识别、建议生成。
*   **链路**：用户上传招标文件 -> Coze 调用 TextIn xParse 插件 -> 得到 markdown/结构化结果 -> Coze 用大模型做解析结果抽取 -> 输出最终“招标解析报告”。

**EMAP 平台架构 (Engineering Machine learning Automation Platform)** [来源：https://www.mdpi.com/1996-1073/14/15/4632]：
*   **模块**：(1) ITB Analysis, (2) Engineering Design, (3) Predictive Maintenance。
*   **ITB Analysis 子模块**：Critical Risk Check (CRC), Terms Frequency Analysis (TFA)。
*   **技术栈**：Python 3.7, spaCy (PhraseMatcher, en_core_web_sm), MySQL/MariaDB, HTML/CSS/JavaScript。
*   **部署**：Cloud-service platform (SaaS)。

**专利系统模块 (CN119624385A)** [来源：https://patents.google.com/patent/CN119624385A/zh]：
*   模块 1：数据库模块（在线数据库 + 本地数据库）。
*   模块 2：文件上传模块。
*   模块 3：招标文件审核模块（格式审核、合规审核、其他异常审核）。
*   模块 4：修改建议模块。
*   模块 5：招标文件生成模块。
*   模块 6：用户交互界面。
*   模块 7：学习模块（使用者风格记录模块）。

#### 6.2 数据流与接口
*   **文件提取代码 (Python)** [来源：https://www.cnblogs.com/yibiaoai/p/19064673]：
    *   Word: `docx2python`
    *   PDF: `pdfplumber` (提取文本 + 表格，添加页码标识)
*   **AI 流式请求** [来源：https://www.cnblogs.com/yibiaoai/p/19064673]：
    *   使用 `AsyncOpenAI` 异步客户端，支持并发请求。
    *   `stream_chat_completion` 函数实现真正的异步流式输出。
*   **Batch API** [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]：
    *   适用于无需即时反馈并需使用大模型处理大量请求的场景。
    *   价格降低 50%（GLM-4-Flash 免费）、无并发限制。
    *   单次处理千万级数据：GLM-4-Flash/Air 最大 1000 万次请求。

#### 6.3 算法与流程
**CRC 模块算法流** [来源：https://www.mdpi.com/1996-1073/14/15/4632]：
1.  上传 ITB 文档到 Risk Extraction Algorithm 模块 (A1)。
2.  算法通过预处理过程检查是否存在 DB 风险条款 (A2)。
3.  算法调查风险存在性，若存在提取句子，若无则生成通知 (A3)。
4.  使用 PhraseMatcher 技术自动分析和提取风险规则。

**TFA 模块算法流** [来源：https://www.mdpi.com/1996-1073/14/15/4632]：
1.  上传 ITB 文档 (B1)。
2.  基于风险 DB，应用 NER 包的分析模型 (B2)。
3.  通过模型分析，标记风险实体，提取频率 (B3)。
4.  提取结果可视化为频率图、HTML 渲染文件、词云 (B4)。

**预处理步骤 (EPC ITB 文档)** [来源：https://www.mdpi.com/1996-1073/14/15/4632]：
1.  按页序识别 ITB 文档中的文本。
2.  提取文本为子类每行，转换为 CSV 格式。
3.  在 CSV 文件的基于行的文本内容中添加位置代码。
4.  将大写字母转换为小写字母，按类别标记单词，消除停用词和空格。
5.  消除页眉、页脚和水印。

### 7. 案例数据与效果指标

#### 7.1 客户案例
*   **某大型央国企** [来源：https://www.idigital.com.cn/common-ai-2]：
    *   搭建私有化部署标书工具，将历史投标案例作为素材进行大模型演练。
    *   全年支持上百个投标项目。
    *   投标文件输出效率提升 30%。
    *   全年 0 废标。
*   **投标龙 (金润科技)** [来源：https://cloud.tencent.com/developer/article/2583012]：
    *   4 大智能能力降 75% 废标率。
    *   聚焦“文件编制 - 风险审查 - 围串标防范 - 评标适配”全流程。

#### 7.2 效果指标 (学术验证)
**CRC 模块验证结果** [来源：https://www.mdpi.com/1996-1073/14/15/4632]：
| 风险类别 | 主体 | 总句子数 | 时间跨度 (小时) | 提取句子 | SMEs 验证 (TP) | SMEs 验证 (FP) | 准确率 (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Single Rule | Module | 1122 | 0.6 | 230 | 205 | 25 | 89 |
| Single Rule | Engineer | 1122 | 30 | 120 | 120 | 0 | 100 |
| Multi-Rule (LD) | Module | 1122 | 0.5 | 36 | 34 | 2 | 94 |
| Multi-Rule (LD) | Engineer | 1222 | 24 | 28 | 28 | 0 | 100 |

**TFA 模块验证结果** [来源：https://www.mdpi.com/1996-1073/14/15/4632]：
| 目标标签 | 主体 | 合同 (项目) | 时间跨度 (小时) | 提取关键词 | SMEs 验证 (TP) | SMEs 验证 (FP) | 准确率 (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Damages | Module | I-1 | 1 | 98 | 90 | 8 | 92 |
| Damages | Engineer | I-1 | 24 | 82 | 82 | 0 | 100 |
| Fit for Purpose (FFP) | Module | I-1 | 0.9 | 6 | 5 | 1 | 83 |
| Fit for Purpose (FFP) | Engineer | I-1 | 22 | 4 | 4 | 0 | 100 |

**框架性能对比** [来源：https://arxiv.org/html/2410.09077v1]：
| Method | Paragraph Score | Table Score | Score |
| :--- | :--- | :--- | :--- |
| Our Framework | 78.31 | 76.15 | 77.74 |
| ChatGLM-4 | 12.55 | 0 | 12.55 |
| ChatGLM-4 with retrieval module | 38.27 | 15.23 | 29.42 |

### 8. 历史演进与政策背景
*   **政策演进**：2026 年 2 月 10 日，国家发展改革委等部门发布《关于加快招标投标领域人工智能推广应用的实施意见》(发改法规〔2026〕195 号) [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。
*   **目标**：2026 年底，招标文件检测、智能辅助评标、围串标识别等重点场景在部分省市实现全覆盖应用；2027 年底，更多重点场景在全国范围内推广应用 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。
*   **技术演进**：从通用 Agent 到招标文件合规引擎，基于 openJiuwen + Skills 的工程化落地实践 [来源：https://cloud.tencent.com/developer/article/2679822]。
*   **专利演进**：2024-12-05 申请专利 CN119624385A，2025-03-14 公开，状态 Pending [来源：https://patents.google.com/patent/CN119624385A/zh]。

## 推荐工作流

### 1. 工具组合与执行步骤
**组合方案：Coze (工作流) + TextIn xParse (解析) + LLM (抽取/审查)** [来源：https://cloud.tencent.com/developer/article/2631225]
1.  **新建 Bot (智能体)**：人设建议写得“专业 + 严谨”，核心强调输出要结构化、尽量引用原文/页码、风险提示要分级、遇到信息缺失要主动提问澄清 [来源：https://cloud.tencent.com/developer/article/2631225]。
2.  **添加插件**：在「技能 / 插件」里添加“通用文档解析”（TextIn xParse）[来源：https://cloud.tencent.com/developer/article/2631225]。
3.  **定义输出格式**：约定输出三段：1. 关键条款摘要（结构化字段）；2. 风险提示（按严重程度排序，尽量含引用）；3. 响应建议（checklist）[来源：https://cloud.tencent.com/developer/article/2631225]。
4.  **工作流编排**：
    *   Bot 收到用户上传文件后，优先执行调用 xParse → 获取解析结果（markdown/结构化信息）。
    *   把解析结果喂给大模型 → 做条款抽取/风险/建议。
    *   最后把内容渲染成报告 [来源：https://cloud.tencent.com/developer/article/2631225]。

**代码实现方案：Python + React + AsyncOpenAI** [来源：https://www.cnblogs.com/yibiaoai/p/19064673]
1.  **文件内容提取**：Word 使用 `docx2python`，PDF 使用 `pdfplumber`（提取文本 + 表格，添加页码标识）[来源：https://www.cnblogs.com/yibiaoai/p/19064673]。
2.  **封装 AI 流式请求**：使用 `AsyncOpenAI` 异步客户端，实现 `stream_chat_completion` 函数支持并发请求 [来源：https://www.cnblogs.com/yibiaoai/p/19064673]。
3.  **提示词调用**：分别调用项目概述提取、技术评分要求提取等 Prompt [来源：https://www.cnblogs.com/yibiaoai/p/19064673]。

**大规模数据处理方案：Batch API** [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
1.  **提交任务**：通过文件提交大量任务。
2.  **优势**：价格降低 50%，无并发限制（4000 并发）。
3.  **适用**：无需即时反馈并需使用大模型处理大量请求的场景 [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。

### 2. 配置方法
*   **模型选择**：GLM-4-AIR（卓越性能，性价比极高），GLM-4-Flash（免费，适合批量）[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
*   **JSON 修复**：使用 `json_repair` 库处理模型输出的 faulty json [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
*   **数据库配置**：在线数据库可采用分布式数据库系统（Elasticsearch + PostgreSQL）；本地数据库采用 PostgreSQL [来源：https://patents.google.com/patent/CN119624385A/zh]。
*   **NER 模型校准**：Epoch=2000, Batch size=128, Dropout rate=0.75, Learning rate=1.001, Optimizer=SGD [来源：https://www.mdpi.com/1996-1073/14/15/4632]。

## 适用场景

1.  **政企采购、基建工程、教育医疗等领域招投标**：每一份招标公告、投标文件、结果公示背后，都是一套格式不一、结构复杂、语义高度专业化的文本材料，适合利用大语言模型构建自动抽取招投标关键字段的通用方案 [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
2.  **EPC 项目投标风险分析**：承包商负责工程、采购和施工项目的整个执行，面临多种风险（如 lump-sum turn-key 和 low-bid selection），适合使用 CRC 和 TFA 模块自动提取和分析合同风险 [来源：https://www.mdpi.com/1996-1073/14/15/4632]。
3.  **大型平台批量公告处理**：大型平台一周可能需处理上千份公告，传统逐条人工录入不现实，迫切希望实现“批量上传、自动抽取、一键校验”[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
4.  **招标文件合规性检测**：结合有关政策法规要求，对招标文件开展合规性、合理性、错敏词等多维度检测，自动识别各类违法违规和排斥限制竞争等问题 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。
5.  **智能辅助评标**：打造类人化的评审推理能力，全面提取招标投标文件要素，深度解析招标文件内容和投标文件响应度，辅助专家开展评审 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。

## 不适用场景

1.  **替代自主判断**：坚持技术的辅助性定位，模型生成的结论不替代招标人、招标代理机构、投标人、评标专家等的自主判断，不改变使用主体的法定责任 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。
2.  **极低质量/无法解析的扫描件**：虽然解析能力覆盖电子档 PDF、扫描件、图片，但若文档过长会被截断，信息丢失；无法可靠解析扫描件、复杂表格和特殊版式时，让大模型直接“硬读”全文常会翻车 [来源：https://cloud.tencent.com/developer/article/2631225]。
3.  **需要即时反馈的超大规模请求**：若无 Batch API 支持，正常请求并发量仅 100，处理 1 亿请求需 340 天，不适合无批量处理能力的场景 [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
4.  **非结构化程度极高且无语境支持的文本**：若没有上下文理解和对领域语言的适配能力，提取出的结果往往前后矛盾、缺乏价值 [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。

## 风险与约束

### 1. 衔接点风险
*   **解析层决定可用性**：真正决定“能不能用”的，往往是解析层。若无法将复杂结构转换成更适合大模型处理的 Markdown+ 结构化信息，大幅降低“模型看不懂文档”的概率 [来源：https://cloud.tencent.com/developer/article/2631225]。
*   **上下文窗口限制**：招标文件动辄几万字，虽然现在各主流大模型的上下文窗口都越来越大，但也只能代表 AI“可以处理几十万字的上下文”，并不代表随便扔给 AI 几十万字，它就能“处理得好几十万字的上下文”[来源：https://www.cnblogs.com/yibiaoai/p/19064673]。

### 2. 上下文与幻觉风险
*   **模型幻觉**：有效防范和应对模型黑箱、幻觉和算法歧视等风险 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。
*   **生成内容转化**：健全模型生成内容的转化应用机制，保障模型充分发挥作用 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。
*   **FP (False Positive)  tagging 错误**：主要成因是基于知识的学習模型不完整，需要机器理解人类语言。需通过连续扩展学习数据和机器学习功能的进步来最小化 [来源：https://www.mdpi.com/1996-1073/14/15/4632]。

### 3. 测试与规格漂移风险
*   **数据质量底线**：哪怕是自动化系统输出的结果，也必须可追溯、可校验。是否符合格式？时间逻辑是否成立？金额字段有没有异常？一旦进入财务、合规、系统对接环节，数据容不得含糊 [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
*   **模型迭代**：建立人工智能模型常态化升级机制，及时更新数据集和知识库，运用招标投标专业数据进行针对性训练，不断优化模型算法，提升模型精准度 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。
*   **安全水平**：严格开展算法、模型备案和安全审核。构建数据、算力、算法和系统安全防护体系，确保模型安全可靠 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。

### 4. 具体风险案例
*   **废标风险**：不再因团队沟通反馈不及时，投标时间紧，出现信息错误或者遗漏等废标风险 [来源：https://www.xiquebiaoshu.com]。
*   **围串标风险**：通过多维数据碰撞和主体画像，穿透式发现企业特征信息雷同，主体关系、投标行为、中标概率异常，专家打分倾向等隐蔽性问题 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。
*   **低于成本价竞标**：对可能低于成本价的投标进行风险提示，减少恶意低价竞标等情况 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。

## 信源质量门控记录

### 门控规则
*   Tavily score < 0.4：剔除
*   已知低质域名：剔除
*   重复 URL：合并保留最高分结果
*   Exa 学术/语义结果：默认保留，但进入来源等级评估
*   C/D 级来源不得作为唯一结论依据
*   入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`

### 保留信源
1.  [A Large Language Model-based Framework for Semi-Structured Tender Document Retrieval-Augmented Generation](https://arxiv.org/html/2410.09077v1) - 来源等级：A - 入库映射：`source-quality: high`
2.  [Information Extraction from Visually Rich Documents using LLM-based Organization of Documents into Independent Textual Segments](https://arxiv.org/html/2505.13535v1) - 来源等级：A - 入库映射：`source-quality: high`
3.  [Arctic-Extract Technical Report](https://arxiv.org/html/2511.16470v1) - 来源等级：A - 入库映射：`source-quality: high`
4.  [Large Language Model for Extracting Complex Contract Information in Industrial Scenes](https://arxiv.org/html/2507.06539v2) - 来源等级：A - 入库映射：`source-quality: high`
5.  [[2603.13651v1] Benchmarking Large Language Models on Reference Extraction and Parsing in the Social Sciences and Humanities](https://arxiv.org/abs/2603.13651v1) - 来源等级：A - 入库映射：`source-quality: high`
6.  [[2309.10952] LMDX: Language Model-based Document Information Extraction And Localization](https://arxiv.org/pdf/2309.10952) - 来源等级：A - 入库映射：`source-quality: high`
7.  [[2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models](https://arxiv.org/abs/2309.12132v2) - 来源等级：A - 入库映射：`source-quality: high`
8.  [OmniCompliance-100K: A Multi-Domain, Rule-Grounded, Real-World Safety Compliance Dataset](https://arxiv.org/pdf/2603.13933) - 来源等级：A - 入库映射：`source-quality: high`
9.  [Intelligent Processing of Design Notices in Engineering Procurement Construction Projects](https://www.mdpi.com/2075-5309/15/5/805) - 来源等级：B - 入库映射：`source-quality: high`
10. [https://arxiv.org/pdf/2603.00369](https://arxiv.org/pdf/2603.00369) - 来源等级：A - 入库映射：`source-quality: high`
11. [ProcureGym: A Multi-Agent Markov Game Framework for Modeling National Volume-based Drug Procurement](https://arxiv.org/html/2603.23880v1) - 来源等级：A - 入库映射：`source-quality: high`
12. [BKRAG : A BGE Reranker RAG for similarity analysis of power project requirements](https://dl.acm.org/doi/fullHtml/10.1145/3689218.3689224) - 来源等级：A - 入库映射：`source-quality: high`
13. [AIReg-Bench: Benchmarking Language Models That Assess AI Regulation Compliance](https://arxiv.org/html/2510.01474v3) - 来源等级：A - 入库映射：`source-quality: high`
14. [Extract-0: A Specialized Language Model for Document Information Extraction](https://arxiv.org/html/2509.22906v1) - 来源等级：A - 入库映射：`source-quality: high`
15. [AI and Text-Mining Applications for Analyzing Contractor's Risk in Invitation to Bid (ITB) and Contracts for Engineering Procurement and Construction (EPC) Projects](https://www.mdpi.com/1996-1073/14/15/4632) - 来源等级：B - 入库映射：`source-quality: high`
16. [标书智能体（一）——AI 解析招标文件代码 + 提示词 - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673) - 来源等级：C - 入库映射：`source-quality: medium`
17. [智能标书助手 - 艾瑞数智](https://www.idigital.com.cn/common-ai-2) - 来源等级：C - 入库映射：`source-quality: medium`
18. [零代码搭建「招标文件解析智能体」：Coze+TextIn xParse 实现 PDF 上传自动提条款、标风险、出建议 - 腾讯云开发者社区 - 腾讯云](https://cloud.tencent.com/developer/article/2631225) - 来源等级：C - 入库映射：`source-quality: medium`
19. [喜鹊标书 AI | AI 标书制作平台与投标方案助手](https://www.xiquebiaoshu.com) - 来源等级：C - 入库映射：`source-quality: medium`
20. [数据提取 - 智谱 AI 开放文档](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction) - 来源等级：A - 入库映射：`source-quality: high`
21. [高效速搭基于 DeepSeek 的招标文书智能写作 Agent - 腾讯云](https://cloud.tencent.com/developer/article/2498790) - 来源等级：C - 入库映射：`source-quality: medium`
22. [View of AI 在招投标文件编制中的应用 - omniscient](http://ojs.omniscient.sg/index.php/mepm/article/view/69302/67852) - 来源等级：C - 入库映射：`source-quality: medium`
23. [关于加快招标投标领域人工智能推广应用的实施意见 (发改法规〔2026 ...](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html) - 来源等级：C - 入库映射：`source-quality: medium`
24. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统](https://patents.google.com/patent/CN119624385A/zh) - 来源等级：C - 入库映射：`source-quality: medium`

### 剔除信源
*   共剔除 41 个信源，主要原因为 score 低于 0.4 或重复 URL。具体包括标桥首页、阿里云帮助文档、多个专利文档、PDF 招标文件原文等 [来源：证据包信源质量门控记录]。

## 来源与可信度

| 来源 | 来源类型 | 可信度 | 支撑内容 |
| :--- | :--- | :--- | :--- |
| https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html | 政府政策 | 高 | 政策目标、应用场景、监管要求 |
| https://docs.bigmodel.cn/cn/best-practice/case/data-extraction | 官方文档 | 高 | 数据结构、Prompt 工程、校验逻辑、Batch API |
| https://www.mdpi.com/1996-1073/14/15/4632 | 学术论文 | 高 | 准确率数据、算法流程、风险分类、验证结果 |
| https://arxiv.org/html/2410.09077v1 | 学术论文 | 高 | 框架性能对比、RAG 技术 |
| https://cloud.tencent.com/developer/article/2631225 | 技术博客 | 中 | 架构设计、Prompt 模板、实操步骤 |
| https://www.cnblogs.com/yibiaoai/p/19064673 | 技术博客 | 中 | 代码实现、Prompt 模板、文件提取 |
| https://patents.google.com/patent/CN119624385A/zh | 专利 | 中 | 审查规则、系统模块、异常类型 |
| https://www.idigital.com.cn/common-ai-2 | 产品页面 | 中 | 客户案例、效率指标 |
| https://www.xiquebiaoshu.com | 产品页面 | 中 | 功能描述、应用场景 |

## 对于可信度较高的来源逐来源总结

### 来源 5: 关于加快招标投标领域人工智能推广应用的实施意见 (发改法规〔2026〕195 号)
*   **核心内容**：国家发展改革委等部门发布的政策文件，明确招标投标和人工智能深度融合的目标和路径。
*   **可用事实**：
    *   2026 年底，招标文件检测、智能辅助评标、围串标识别等重点场景在部分省市实现全覆盖应用。
    *   2027 年底，更多重点场景在全国范围内推广应用。
    *   具体场景包括：招标策划、招标文件编制、招标文件检测、投标策划、投标合规自查、开标、专家抽取、智能辅助评标、评标报告核验、辅助定标决策、中标合同签订、场所调度、见证管理、档案管理、智慧问答、专家管理、围串标识别、信用管理、协同监管、投诉处理 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。
*   **局限**：政策文件，不包含具体技术实现细节。
*   **适合入库知识点**：政策目标、应用场景列表、合规性要求、监管方向。

### 来源 7: 数据提取 - 智谱 AI 开放文档
*   **核心内容**：官方提供的招投标数据提取最佳实践，包含完整的方案框架、Prompt 设计、代码示例和校验逻辑。
*   **可用事实**：
    *   提供了完整的 JSON Schema 示例和字段定义。
    *   提供了日期、金额格式化的具体代码和规则（14 位日期时间格式）。
    *   提供了数据校验模块的代码（格式校验、逻辑校验、完整性校验、一致性校验）。
    *   提供了 Batch API 的成本和效率数据（价格降低 50%，并发提升 40 倍）[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
*   **局限**：主要针对智谱 AI 模型，其他模型需适配。
*   **适合入库知识点**：Prompt 模板、JSON Schema、校验代码、Batch API 配置。

### 来源 10: AI and Text-Mining Applications for Analyzing Contractor's Risk in ITB and Contracts for EPC Projects
*   **核心内容**：学术论文，详细描述了 CRC 和 TFA 两个核心模块的开发、验证和结果。
*   **可用事实**：
    *   CRC 模块准确率 92%，TFA 模块准确率 88%。
    *   收集了 25 个 EPC 项目，21,683 行文本数据。
    *   提供了详细的算法流程、NER 标签列表、验证表格数据 [来源：https://www.mdpi.com/1996-1073/14/15/4632]。
*   **局限**：主要针对英文 EPC 合同，中文场景需适配。
*   **适合入库知识点**：准确率数据、风险分类体系、算法流程、验证方法。

### 来源 1: 零代码搭建「招标文件解析智能体」：Coze+TextIn xParse 实现 PDF 上传自动提条款、标风险、出建议
*   **核心内容**：腾讯云开发者社区文章，介绍如何使用 Coze 和 TextIn 搭建招标文件解析智能体。
*   **可用事实**：
    *   提出了“先解析，再抽取”的稳定性技巧。
    *   提供了关键条款抽取、风险识别、响应建议的 Prompt 模板结构。
    *   强调输出可追溯的原文定位信息（页码、段落）[来源：https://cloud.tencent.com/developer/article/2631225]。
*   **局限**：依赖特定平台（Coze, TextIn）。
*   **适合入库知识点**：架构范式、Prompt 结构、溯源要求。

## 跨源矛盾检测结论

### 检测范围
*   已精读来源数量：10 个
*   检测对象：核心数字、日期、功能描述、因果判断、市场/公司事实
*   检测时间：2026-06-22

### 检测结果
结论：检测到 2 处跨源矛盾/差异，综合输出时必须保留双方表述，不得静默合并。

### 矛盾项 1：准确率数据差异
*   **矛盾描述**：不同来源报告的系统准确率数据存在差异，可能源于测试集、场景或定义不同。
*   **来源 A**：[AI and Text-Mining Applications for Analyzing Contractor's Risk in ITB and Contracts for EPC Projects](https://www.mdpi.com/1996-1073/14/15/4632)
    *   原文引用："risk clause extraction accuracy rates with the CRC module and the TFA module were about 92% and 88%, respectively"
    *   来源等级：B (High)
    *   发布时间 / 数据日期：2021-07-30
*   **来源 B**：[智能标书助手 - 艾瑞数智](https://www.idigital.com.cn/common-ai-2)
    *   原文引用："全年 0 废标" (隐含准确率极高，但未给出具体提取准确率数字)
    *   来源等级：C (Medium)
    *   发布时间 / 数据日期：2025-07-15 (页面显示时间)
*   **初步判断**：
    *   倾向：来源 A
    *   理由：来源 A 为学术论文，有详细的验证方法（SMEs Validation）和计算公式（Accuracy = TP/(TP + FP)），数据更透明可验证。来源 B 为产品宣传，"0 废标"是结果指标而非提取准确率。
*   **综合输出要求**：
    *   必须写成“来源 A 报告 CRC 模块准确率 92%，TFA 模块 88%（基于 25 个项目验证）；来源 B 报告某央国企案例全年 0 废标（基于私有化部署工具）”

### 矛盾项 2：政策发布时间与内容
*   **矛盾描述**：政策文件编号与发布时间在不同上下文中可能存在的细微差异（证据包内一致，但需注意未来验证）。
*   **来源 A**：[关于加快招标投标领域人工智能推广应用的实施意见 (发改法规〔2026〕195 号)](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html)
    *   原文引用："发布时间：2026/02/10", "发改法规〔2026〕195 号"
    *   来源等级：C (Medium - 门控记录评定，实际为政府官网)
    *   发布时间 / 数据日期：2026-02-10
*   **来源 B**：[5 月 26 日三部门重磅发文！招投标智能体正式 "转正"，政企数字化最大风口来了](https://cloud.tencent.com/developer/article/2693712?policyId=1003) (证据包候选信源列表中提到，但未精读全文，仅在推荐文章列表出现)
    *   原文引用："2026 年 5 月 26 日，国家网信办、国家发展改革委、工业和信息化部三部门联合印发《智能体规范应用与创新发展实施意见》"
    *   来源等级：C (Medium)
    *   发布时间 / 数据日期：2026-06-19
*   **初步判断**：
    *   倾向：来源 A
    *   理由：来源 A 为发改委官网原文，直接展示了文件头和发布时间。来源 B 为腾讯开发者社区文章，可能是解读或另一份文件。证据包中未精读来源 B 全文，但标题提及的是《智能体规范应用与创新发展实施意见》，与来源 A《关于加快招标投标领域人工智能推广应用的实施意见》名称不同，可能为两份不同文件，非直接矛盾，但需注意区分。
*   **综合输出要求**：
    *   必须写成“来源 A 显示 2026 年 2 月 10 日发布《关于加快招标投标领域人工智能推广应用的实施意见》；来源 B 提及 2026 年 5 月 26 日三部门印发《智能体规范应用与创新发展实施意见》，需核实是否为两份不同文件”

## 矛盾与待验证问题

1.  **政策文件区分**：2026 年 2 月 10 日发布的《关于加快招标投标领域人工智能推广应用的实施意见》与 2026 年 5 月 26 日提及的《智能体规范应用与创新发展实施意见》是否为两份不同文件？证据包中仅精读了前者，后者仅在推荐列表出现，需二次验证 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html] [来源：https://cloud.tencent.com/developer/article/2693712?policyId=1003]。
2.  **准确率通用性**：MDPI 论文中的 92%/88% 准确率基于英文 EPC 合同和 25 个项目数据集，在中文招投标场景下的泛化能力未验证 [来源：https://www.mdpi.com/1996-1073/14/15/4632]。
3.  **Batch API 成本时效性**：智谱 AI 文档中提到的 Batch API 价格降低 50% 及 GLM-4-Flash 免费为“限时特惠”，长期成本策略需确认 [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]。
4.  **专利实施状态**：专利 CN119624385A 状态为 Pending (2024-12-05 申请)，其描述的系统功能是否已实际落地产品未验证 [来源：https://patents.google.com/patent/CN119624385A/zh]。
5.  **模型幻觉防范**：政策要求有效防范模型幻觉，但具体技术实现（如 RAG、校验模块）在实际生产环境中的效果需进一步验证 [来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]。

## 原始证据摘录

1.  **政策目标**："2026 年底，招标文件检测、智能辅助评标、围串标识别等重点场景在部分省市实现全覆盖应用；2027 年底，更多重点场景在全国范围内推广应用”[来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]
2.  **架构范式**：“更稳的打法是：先把文档变成结构化可理解的内容，再让大模型做抽取和风控。”[来源：https://cloud.tencent.com/developer/article/2631225]
3.  **准确率数据**："pilot test results showed that risk clause extraction accuracy rates with the CRC module and the TFA module were about 92% and 88%, respectively, whereas the risk clause extraction accuracy rates manually by the engineers were about 70% and 86%, respectively." [来源：https://www.mdpi.com/1996-1073/14/15/4632]
4.  **Prompt 原则**：“如果某些字段信息在文本中缺失或未识别，Prompt 应规定使用默认值（如“无”）填充。”[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
5.  **异常类型**："1.内容不完整或缺失... 2.条款或条件设定不合理... 3.时间节点异常... 4.招标金额与预算异常... 5.法律和合规性问题... 6.历史数据异常... 7.价格与成本异常... 8.招标程序违规... 9.关联方或利益冲突问题... 10.历史项目问题复现”[来源：https://patents.google.com/patent/CN119624385A/zh]
6.  **Batch API 效率**："1 亿请求（2048 tokens）... 正常请求 340 天... Batch 请求 8.6 天 (40 倍效率)... 价格 204,800 元... 102,400 元（省钱一半）”[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
7.  **客户案例**：“为该企业全年支持上百个个投标项目，投标文件输出效率提升 30%，全年 0 废标。”[来源：https://www.idigital.com.cn/common-ai-2]
8.  **技术栈**："Python 3.7, spaCy (PhraseMatcher, en_core_web_sm), MySQL/MariaDB, HTML/CSS/JavaScript" [来源：https://www.mdpi.com/1996-1073/14/15/4632]
9.  **溯源要求**：“投标场景里，单单给出风险提示没用，必须能指回原文：第几页、哪一段、哪张表。”[来源：https://cloud.tencent.com/developer/article/2631225]
10. **合规定位**：“坚持技术的辅助性定位，模型生成的结论不替代招标人、招标代理机构、投标人、评标专家等的自主判断，不改变使用主体的法定责任。”[来源：https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html]