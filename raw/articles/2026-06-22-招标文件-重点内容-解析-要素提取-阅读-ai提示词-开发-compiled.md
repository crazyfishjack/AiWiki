# 招标文件重点内容解析与要素提取 AI 提示词开发调研报告

## 核心结论

1.  **招标文件解析需采用“解析引擎 + 大模型”分层架构**：单纯依赖大模型直接读取长文档易导致信息丢失或幻觉，稳态打法是先用专业解析引擎（如 TextIn xParse、pdfplumber）将复杂版式转换为结构化 Markdown/JSON，再交由大模型进行要素抽取与风控。[来源：https://cloud.tencent.com/developer/article/2631225] [可信度：高]
2.  **提示词工程需遵循“九要素”黄金公式**：有效的提示词应包含起名、双重指令、模拟确认、反复强调、强制规则、背景信息、正向激励、参考示例、反面示例，以确保 AI 输出稳定可控。[来源：https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide] [可信度：高]
3.  **政策明确推动招投标领域人工智能应用**：国家发展改革委等部门发布实施意见，明确 2026 年底招标文件检测、智能辅助评标等重点场景在部分省市实现全覆盖应用，2027 年底全国推广。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html] [可信度：高]
4.  **数据提取需具备完整的后处理与校验机制**：大模型提取后的数据必须经过 JSON 格式标准化、数据格式化（如日期统一为 14 位）、逻辑校验（如投标截止时间不能晚于开标时间）及自动修复，才能进入业务系统。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction] [可信度：高]
5.  **批量处理可显著降低成本**：使用 Batch API 处理大量招标文件请求，价格可降低 50%（如 GLM-4-Flash 免费），并发量可从 100 提升至 4000，处理 1 亿请求天数从 340 天缩短至 8.6 天。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction] [可信度：高]
6.  **解析精度依赖对复杂版式的处理能力**：招标文件包含目录、征文、技术规范、商务条款、复杂表格和各类附件，解析能力需覆盖电子档 PDF、扫描件、图片，并能处理合并单元格、页眉页脚噪音。[来源：https://cloud.tencent.com/developer/article/2631225] [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction] [可信度：高]
7.  **AI 在招投标中的应用场景覆盖全流程**：包括招标策划、文件编制、文件检测、投标策划、合规自查、开标、专家抽取、智能辅助评标、定标、合同签订、现场管理、监管等 20 个具体场景。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html] [可信度：高]

## 内容整理

### 政策背景与总体目标

国家发展改革委等部门发布《关于加快招标投标领域人工智能推广应用的实施意见》（发改法规〔2026〕195 号），发布时间为 2026/02/10。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

**总体目标：**
围绕招标投标交易全过程和管理重点环节，按照政府引导、多方参与、场景牵引、安全可控的原则，积极稳妥推进人工智能在招标投标领域的应用。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- 2026 年底，招标文件检测、智能辅助评标、围串标识别等重点场景在部分省市实现全覆盖应用。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- 2027 年底，更多重点场景在全国范围内推广应用，形成一批模型训练、场景应用、机制保障等方面的经验做法。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

**规范部署实施要求：**
- 科学组织推进：对于提高交易效率、适合市场化推进的场景，要积极培育人工智能应用服务商；对于保障交易公平公正、提升监管质效的场景，要注重发挥政府主导作用。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- 强化系统集成：持续深化公共资源交易平台整合共享，在统一制度规则和技术标准的基础上有序开展集约化改造。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- 夯实数据基础：加强招标投标数据治理，强化数据清洗和标注，加快构建涵盖招标投标政策法规和全流程各环节的高质量数据集和知识库。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- 持续迭代优化：建立人工智能模型常态化升级机制，及时更新数据集和知识库，运用招标投标专业数据进行针对性训练。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- 健全应用机制：坚持技术的辅助性定位，模型生成的结论不替代招标人、招标代理机构、投标人、评标专家等的自主判断，不改变使用主体的法定责任。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- 提升安全水平：严格落实人工智能模型安全管理要求，强化模型算法、数据资源、基础设施、应用系统等安全能力建设，严格开展算法、模型备案和安全审核。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

### 技术架构与实现机制

**分层设计原则：**
招标文件解析不能只靠人看，也不能只丢给大模型。文档过长会被截断，信息丢失；无法可靠解析扫描件、复杂表格和特殊版式；生成的总结常常笼统，无法提供可验证的原文引用。更稳的打法是：先把文档变成结构化可理解的内容，再让大模型做抽取和风控。[来源：https://cloud.tencent.com/developer/article/2631225]

**方案架构（零代码/低代码）：**
- **Coze 负责：** 对话、工作流编排、输出格式、交互体验。[来源：https://cloud.tencent.com/developer/article/2631225]
- **TextIn xParse 负责：** 把招标文件解析成结构化可读内容（Markdown+ 结构化信息 + 页级信息）。[来源：https://cloud.tencent.com/developer/article/2631225]
- **LLM 负责：** 条款抽取、风险识别、建议生成。[来源：https://cloud.tencent.com/developer/article/2631225]

**最稳定的链路：**
1. 用户上传招标文件。[来源：https://cloud.tencent.com/developer/article/2631225]
2. Coze 调用 TextIn xParse 插件 → 得到 markdown/结构化结果。[来源：https://cloud.tencent.com/developer/article/2631225]
3. Coze 用大模型做解析结果抽取：关键条款抽取（结构化字段）、风险识别（可以带引用）。[来源：https://cloud.tencent.com/developer/article/2631225]
4. 输出最终“招标解析报告”。[来源：https://cloud.tencent.com/developer/article/2631225]

**学术框架（LLM-based Framework）：**
- **Template Retrieval Module：** 运用语义搜索算法和 embeddings 准确定位与用户规格一致的文件。[来源：https://arxiv.org/html/2410.09077v1]
- **Template Filling Module：** 使用 LLMs 根据用户要求填写模板细节。[来源：https://arxiv.org/html/2410.09077v1]
- **Modifications with Procurement Knowledge Base：** 整合采购知识库的额外知识，确保生成文件符合行业标准和最佳实践。[来源：https://arxiv.org/html/2410.09077v1]
- **Evaluation Steps：** 段落得分（Paragraph Score）、表格得分（Table Score）、总体得分（Overall Score）。[来源：https://arxiv.org/html/2410.09077v1]

**输入模块设计：**
- 多种文件格式支持：需要支持从多种格式（PDF、Word、Excel、TXT 等）中提取文本。对于图片，可以借助 OCR 工具进行文本提取。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 网页可以使用网页爬虫工具（如 `Scrapy`、`BeautifulSoup`、`Selenium`）抓取网页中的文本和表格数据。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 参考代码（智谱 AI 文件上传）：
```python
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
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

**预处理模块设计：**
- 去除噪音信息：常见的噪音信息包括页眉、页脚、版权声明等。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 规范化文本：处理文本中的特殊符号、空白字符、异常换行等问题。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 日期格式统一：通过正则表达式或日期识别工具将所有的日期格式统一转换为标准的 ISO 格式（如”YYYY-MM-DD"）。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 参考代码（日期规范化）：
```python
import re
from datetime import datetime

def normalize_date(text):
   patterns = [
       r'\d{1,2}\/\d{1,2}\/\d{4}',       # "MM/DD/YYYY"
       r'\d{1,2}-\w{3}-\d{4}',           # "DD-MMM-YYYY"
       r'\d{4}年\d{1,2}月\d{1,2}日',     # "YYYY 年 MM 月 DD 日"
   ]
   for pattern in patterns:
       text = re.sub(pattern, lambda x: datetime.strptime(x.group(), '%Y年%m月%d日').strftime('%Y-%m-%d'), text)
   return text
```
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 货币与金额格式化：统一这些金额表示，确保货币单位和金额数字的格式标准化。例如将”壹仟元”转换为”1000 CNY"，或将”$1,000"转换为”1000 USD"。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 表格数据处理：对于 PDF 或 Word 文档中的表格，可以使用表格解析工具（如 `pdfplumber` 或 `python-docx`）提取表格的结构和数据。提取后的表格数据可以转化为 CSV 或 JSON 格式。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 合并单元格处理：预处理模块需要将合并单元格的数据平铺展开，确保每个单元格都包含完整的信息。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 表格结构化转换建议使用 HTML 表示复杂表格，例如：
```html
<table>
  <tr>
    <th>项目</th>
    <th>金额</th>
    <th>说明</th>
  </tr>
  <tr>
    <td>项目 A</td>
    <td colspan="2">1000（包含材料费和人工费）</td>
  </tr>
  <tr>
    <td>项目 B</td>
    <td>500</td>
    <td>材料费</td>
  </tr>
  <tr>
    <td>项目 B</td>
    <td>1500</td>
    <td>人工费</td>
  </tr>
</table>
```
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

**文件内容提取代码（Python+React 方案）：**
- Word 文件提取，选用的是 `docx2python`：
```python
content = None
try:
    # 使用 docx2python 提取，它能更好地处理表格和结构
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
[来源：https://www.cnblogs.com/yibiaoai/p/19064673]
- PDF 文件提取，则使用 pdfplumber：
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
    # 确保关闭 PDF 文件
    if pdf:
        pdf.close()
    gc.collect()
    return result
except Exception as e:
    # 确保关闭 PDF 文件
    if pdf:
        pdf.close()
    gc.collect()
```
[来源：https://www.cnblogs.com/yibiaoai/p/19064673]

**封装 AI 流式请求通用函数：**
- 注意这里使用的是 `AsyncOpenAI` 即 OpenAI 的异步客户端，因为之后要一次性编写几十万字的标书，为了提高速度，使用并发请求，则必须使用 `AsyncOpenAI`。[来源：https://www.cnblogs.com/yibiaoai/p/19064673]
```python
def __init__(self, api_key: str, base_url: str = None, model_name: str = "gpt-3.5-turbo"):
    """初始化 OpenAI 服务"""
    self.api_key = api_key
    self.base_url = base_url
    self.model_name = model_name

    # 初始化 OpenAI 客户端 - 使用异步客户端
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
        yield f"错误：{str(e)}"
```
[来源：https://www.cnblogs.com/yibiaoai/p/19064673]

### 提示词工程与要素提取

**提示词“九要素”黄金公式：**
实践验证好用的一套结构：起名 + 双重指令 + 模拟确认 + 反复强调 + 强制规则 + 背景信息 + 正向激励 + 参考示例 + 反面示例（可选）。[来源：https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide]

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

[来源：https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide]

**快速上手模板：**
```markdown
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
[来源：https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide]

**招标文件解析提示词（项目概述）：**
- SystemPrompt:
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
[来源：https://www.cnblogs.com/yibiaoai/p/19064673]
- UserPrompt:
```markdown
请分析以下招标文件内容，提取项目概述信息：
{request.file_content}
```
[来源：https://www.cnblogs.com/yibiaoai/p/19064673]

**技术评分要求提取提示词：**
- SystemPrompt:
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
[来源：https://www.cnblogs.com/yibiaoai/p/19064673]

**智谱 AI 数据提取 Prompt 策略：**
- 策略 01：明确的待处理内容指引。在构建 Prompt 时，明确告诉模型它需要处理的内容是关键步骤之一。应清晰地定义需要处理的文本，并使用标记将其框起来。例如：`'''这是需要处理的文本'''`、`《》这是需要处理的文本《》`。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 策略 02：提供明确字段定义。字段定义为 LLM 提供了标准，使它在解析文本时能够准确地提取所需信息并填充到对应字段。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 策略 03：异常处理。如果某些字段信息在文本中缺失或未识别，Prompt 应规定使用默认值（如“无”）填充。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 策略 04：要求结构化输出。Prompt 应指示 LLM 以结构化的格式输出数据。结构化输出便于自动化处理，常见的格式如 JSON。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

**智谱 AI 数据提取 Prompt 参考（Model: GLM-4-AIR）：**
- System Prompt: `你是一个专业的文本信息提取器，可以严格按照 Json 格式输出` [来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- User Prompt:
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
  "中标信息": [
    {
      "中标供应商名称": "中标的供应商名称，仅提取供应商的企业名称。",
      "中标金额": "中标的合同金额，单位为元。"
    }
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
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

**Coze 智能体提示词模板：**
- A）关键条款抽取 Prompt（建议输出 JSON，后续好渲染）：输入为解析得到的 markdown，输出为固定字段 JSON（项目信息、时间节点、资格要求、商务条款、评标办法）。[来源：https://cloud.tencent.com/developer/article/2631225]
- B）风险识别 Prompt（输出风险清单，带证据）：输入为上一步 JSON + markdown 中对应原文片段，输出为风险列表（高/中/低），每条风险包含风险点、触发原文（引用）、风险类型（合规/商务/交付/资质/评分/合同）、建议动作（澄清/补充材料/策略调整）。[来源：https://cloud.tencent.com/developer/article/2631225]
- C）响应建议 Prompt（输出 checklist，能落地）：输入为关键条款 JSON + 风险列表，输出为材料清单（按部门）、澄清问题清单（可直接复制发招标方）、投标策略建议（写作重点、偏离说明建议等）。[来源：https://cloud.tencent.com/developer/article/2631225]

### 数据后处理与校验

**JSON 格式标准化：**
在使用大语言模型提取数据时，生成的 JSON 格式可能出现结构问题、不正确的语法、特殊字符等问题，导致数据无法正确解析。因此，需要通过 JSON 格式化工具对提取出的 JSON 数据进行标准化处理。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 参考代码（JSON 清洗）：
```python
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
        .replace('"[{', "[{")
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
```
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

**数据格式化：**
- 日期格式：所有日期和时间字段都应格式化为标准的 14 位日期时间格式：`YYYYMMDDHHMMSS`。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 金额格式：金额字段应保留原单位（如元、万元），并且格式化为无空格、无额外字符的数值形式（如 `500000 元`）。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 文本字段格式化：对文本字段中的特殊字符（如换行符、双引号）进行处理，确保文本内容不会破坏 JSON 的语法结构。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 格式化示例：
输入：
```json
{
  "项目名称": "智能楼宇工程",
  "项目编号": "XZL-2023",
  "采购预算": " 7,000,000.00 元",
  "开标时间": "2024/01/01 09:00"
}
```
格式化后的输出：
```json
{
  "项目名称": "智能楼宇工程",
  "项目编号": "XZL-2023",
  "采购预算": "7000000 元",
  "开标时间": "20240101090000"
}
```
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

**数据校验模块：**
- 格式校验：确保所有数据符合预期的格式标准，例如日期、金额、电话号码等字段的格式是否正确。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 参考代码（金额校验）：
```python
def validate_currency_format(amount_str):
    if '元' in amount_str or '万元' in amount_str:
        try:
            amount = float(amount_str.replace("万元", "").replace("元", "").replace(",", "").strip())
            return True
        except ValueError:
            return False
    return False
```
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 逻辑校验：检查数据之间的逻辑关系是否符合业务规则。例如：投标截止时间不能晚于开标时间。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 参考代码（时间顺序校验）：
```python
from datetime import datetime

def validate_time_order(submit_time, open_time):
    submit_dt = datetime.strptime(submit_time, "%Y%m%d%H%M%S")
    open_dt = datetime.strptime(open_time, "%Y%m%d%H%M%S")
    return submit_dt <= open_dt
```
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 金额校验：采购预算金额不能小于中标金额。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 完整性校验：确保所有关键字段都已经填入有效数据，避免信息缺失。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 参考代码（缺失字段填充）：
```python
def fill_missing_fields(data, default="无"):
    required_fields = ["项目名称", "项目编号", "采购预算", "投标截止时间"]
    for field in required_fields:
        if field not in data or not data[field]:
            data[field] = default
    return data
```
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 一致性校验：确保同一信息在不同字段或位置的值保持一致。例如项目编号在不同字段中应当相同。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 参考代码（综合校验）：
```python
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
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

**数据修复模块：**
- 基于规则的自动修复：在大部分情况下，错误可以通过预定义的规则和算法进行自动修复。此步骤作为第一层处理机制，针对格式错误、简单的逻辑冲突、特殊字符处理等问题进行修正。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 提交更高级模型处理：对于规则无法解决的复杂错误，或者需要更高层次推理的情况，可以将这些 Bad Case 提交给高级模型（如 GLM-4-plus）处理。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

### 产品案例与效能数据

**快标书 AI 案例：**
- 功能：自动提取关键信息（投标保证金金额、履约保证金比例、项目交付周期），自动识别废标项和评分规则，快速生成标书目录。[来源：https://www.kuaibiaoshu.com/course/ai-bid-document-analysis]
- 技术支撑：接入 deepseek-r1 模型，具备强大的深度思考能力。[来源：https://www.kuaibiaoshu.com/course/ai-bid-document-analysis]
- 效能数据：投标准备时间平均缩短了 70%。某 IT 企业反馈，原本需要两名专业人员耗时一天才能完成的招标文件解析工作，现在只需上传文件，20 分钟内即可获得完整的解析报告和标书目录框架。[来源：https://www.kuaibiaoshu.com/course/ai-bid-document-analysis]
- 使用流程：登录账号 -> 进入工作台 -> 点击“招标文件解析” -> 上传文件 -> 自动跳转解析页面 -> 解析完成后展示“查看详情”和“生成标书”。[来源：https://www.kuaibiaoshu.com/course/ai-bid-document-analysis]

**百炼智能（知了标讯）案例：**
- 功能：支持直接识别 Word、PDF 格式招标文档的关键信息，结合行业数据做深度分析（如服务范围匹配度达 85% 标注“高适配”）。[来源：https://www.bailian-ai.com/news/2243.html]
- 痛点解决：一份 30 页的招标，人工找“投标截止时间”“预算金额”得 1 个多小时，AI 能在 2 分钟内从几十页招标里精准抓出。[来源：https://www.bailian-ai.com/news/2243.html]
- 效能数据：用知了标讯分析招标，既能省出 1.5 小时去跟进客户，又能减少因漏看条款导致的投标失败。[来源：https://www.bailian-ai.com/news/2243.html]

**智谱 AI 招标解析智能体：**
- 价格：按 Token 后付费，5 元/百万 Tokens。计量范围：智能体全任务流节点产生的 Tokens 总数。[来源：https://docs.bigmodel.cn/cn/guide/agents/tender]
- 接口请求：传输方式 https，请求地址 `https://open.bigmodel.cn/api/v1/agents`，接口请求类型 POST。[来源：https://docs.bigmodel.cn/cn/guide/agents/tender]
- 请求参数：agent_id (String, 是，智能体 ID：`bidwin_parser_agent`), stream (boolean, 否), messages (List<Object>, 是), custom_variables (Object, 是)。[来源：https://docs.bigmodel.cn/cn/guide/agents/tender]

**Batch API 效能数据：**
|  | 正常请求 | Batch 请求 |
| --- | --- | --- |
| 任务量 | 1 亿请求（2048 tokens） | 1 亿请求（2048 tokens） |
| 模型 | GLM-4-Air | GLM-4-Air |
| 并发量 | 100 并发 | 4000 并发 |
| 天数 | 340 天 | 8.6 天 (40 倍效率) |
| 价格 | 204,800 元 | 102,400 元（省钱一半） |
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

**单次处理千万级数据：**
| 模型 | Batch 一次最大请求 |
| --- | --- |
| GLM-4-Flash | 1000 万次 |
| GLM-4-Air | 1000 万次 |
| GLM-3-Turbo | 200 万次 |
| Embedding-2 | 200 万次 |
| Embedding-3 | 200 万次 |
| GLM-4-Plus | 200 万次 |
| GLM-4-0520 | 50 万次 |
| GLM-4 | 50 万次 |
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

### 招投标领域 AI 应用场景（政策定义）

**（一）“人工智能+"招标**
1. 招标策划：辅助招标人对行业趋势、市场供需、资源要素等进行综合研判，生成客观量化的招标需求、技术和商务条件。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
2. 招标文件编制：智能匹配招标文件范本，推荐适合的资格条件、评标办法和评标标准，辅助招标人编制或自动生成招标文件。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
3. 招标文件检测：结合有关政策法规要求，对招标文件开展合规性、合理性、错敏词等多维度检测，自动识别各类违法违规和排斥限制竞争等问题。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

**（二）“人工智能+"投标**
4. 投标策划：全方位捕捉各类项目招标信息，结合投标人特点推送适合的项目信息，自动提取并解析项目招标计划、招标公告和招标文件等资料中的关键要素。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
5. 投标合规自查：深度解析项目招标需求和招标文件要求，结合投标人的特点和优势，辅助投标人确定技术方案和报价区间。对投标人编制的投标文件，对照招标文件进行响应性比对。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

**（三）“人工智能+"开标和评标**
6. 开标：打造类人化的数字开标人，调度项目开标活动全流程，自动完成宣读开标纪律、公布投标人名单、标书解密、唱标、结果确认等工作。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
7. 专家抽取：综合解析项目特点和评标要点，根据评标专家的专业分类、地域分布、回避规则等条件，自动生成与项目相适应的专家抽取方案。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
8. 智能辅助评标：打造类人化的评审推理能力，掌握不同专业评标专家的知识结构体系，按照项目类型建立综合评审指标体系，辅助专家开展评审或生成结果供专家参考。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

**（四）“人工智能+"定标**
9. 评标报告核验：打造评标报告智能审核能力，辅助招标人核查评标报告的数据准确性、逻辑关联性、内容合规性等。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
10. 辅助定标决策：基于招标需求、供应链管理、历史交易情况等，结合有关行业、信用、税务、司法等平台系统数据，对中标候选人进行多维立体画像。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
11. 中标合同签订：在招标投标文件资料中自动提取中标合同的主要签约要素，参考有关示范文本并结合项目专用合同条款生成合同。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

**（五）“人工智能+"现场管理**
12. 场所调度：对交易场所进行全方位智能化管理，高效调配场所工位资源和人员力量。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
13. 见证管理：构建“智能研判—动态干预—链上存证”的闭环见证体系，对招标投标交易各环节进行无感化数字见证。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
14. 档案管理：构建招标投标交易档案智能化管理体系，结合智能见证管理实现交易文件的智能填报、交易数据的链上存证。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
15. 智慧问答：搭建招标投标领域专业问答引擎，针对各类政策法规、业务知识、操作流程等，提供多模态交互式咨询服务。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

**（六）“人工智能+"监管**
16. 专家管理：构建评标专家全生命周期智能管理体系，结合专业能力、履职考核、信用评价、教育培训等情况，对评标专家进行多维立体画像。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
17. 围串标识别：构建“主体 + 行为”全覆盖的综合预警体系，通过多维数据碰撞和主体画像，穿透式发现企业特征信息雷同，主体关系、投标行为、中标概率异常，专家打分倾向等隐蔽性问题。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
18. 信用管理：打造招标投标智慧信用管理能力，实现信用信息的客观记录、自动归集、共享应用、动态调整。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
19. 协同监管：打造贯通项目标前、标中、标后的分析预警模型，加强全过程数据采集、治理和运用。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
20. 投诉处理：打造招标投标智能化投诉处理能力，辅助行政监督部门分析投诉书，结合政策法规、历史案例和调查取证情况等，形成初步审查意见。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

## 推荐工作流

**组合使用工具：**
1.  **文档解析层**：使用 TextIn xParse 或 `pdfplumber`/`docx2python` 进行文件内容提取，将 PDF/Word 转换为结构化 Markdown/JSON。[来源：https://cloud.tencent.com/developer/article/2631225] [来源：https://www.cnblogs.com/yibiaoai/p/19064673]
2.  **编排与交互层**：使用 Coze 或 NocoBase 进行工作流编排，定义 Bot 人设、输出格式和交互体验。[来源：https://cloud.tencent.com/developer/article/2631225] [来源：https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide]
3.  **模型处理层**：使用智谱 AI（GLM-4-AIR/Plus）或 DeepSeek-R1 进行条款抽取、风险识别和建议生成。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction] [来源：https://www.kuaibiaoshu.com/course/ai-bid-document-analysis]
4.  **后处理与校验层**：使用 Python 脚本进行 JSON 标准化、数据格式化、逻辑校验和自动修复。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
5.  **批量处理层**：对于大量文档，使用 Batch API 提交任务，降低成本并提高并发。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

**具体执行步骤和配置方法：**
1.  **新建 Bot（智能体）**：创建 Bot，人设建议写得“专业 + 严谨”，核心强调输出要结构化、尽量引用原文/页码、风险提示要分级（高/中/低）、遇到信息缺失要主动提问澄清。[来源：https://cloud.tencent.com/developer/article/2631225]
2.  **添加插件**：在「技能 / 插件」里添加“通用文档解析”（如 TextIn xParse），让 Bot 具备“读懂招标文件”的能力。[来源：https://cloud.tencent.com/developer/article/2631225]
3.  **定义输出格式**：建议在 Bot 里约定输出结构（关键条款摘要、风险提示、响应建议），后面提示词都围绕它。[来源：https://cloud.tencent.com/developer/article/2631225]
4.  **执行流程**：Bot 在收到用户上传文件后，优先执行调用 xParse → 获取解析结果（markdown/结构化信息）→ 把解析结果喂给大模型 → 做条款抽取/风险/建议 → 最后把内容渲染成报告。[来源：https://cloud.tencent.com/developer/article/2631225]
5.  **提示词配置**：使用“九要素”黄金公式编写提示词，包含起名、双重指令、模拟确认、反复强调、强制规则、背景信息、正向激励、参考示例、反面示例。[来源：https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide]
6.  **数据校验配置**：配置后处理脚本，进行格式校验（日期、金额）、逻辑校验（时间顺序、金额大小）、完整性校验（必填字段）、一致性校验（编号一致）。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

**具体操作建议：**
- 对于复杂表格，建议使用 HTML 表示，能很好地保留表格的结构，并方便 LLM 理解。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 日期格式统一转换为标准的 ISO 格式（如”YYYY-MM-DD"）或 14 位标准时间格式（`YYYYMMDDHHMMSS`）。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 如果字段缺失或无法识别，Prompt 应规定使用默认值（如“无”）填充。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 对于大量请求，使用 Batch API，价格降低 50%，并发量从 100 提升至 4000。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

## 适用场景

1.  **政企采购与基建工程**：招投标是极为常见的业务流程，每一份招标公告、投标文件、结果公示背后，都是一套格式不一、结构复杂、语义高度专业化的文本材料。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
2.  **教育医疗领域**：涉及设备招标、服务采购等，需要提取项目名称、投标方、资格要求、预算金额、开标时间等关键信息。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
3.  **IT 行业系统集成项目**：快标书 AI 的招标文件解析功能在 IT 行业的系统集成项目中表现出色，能精准识别技术规范和质量要求。[来源：https://www.kuaibiaoshu.com/course/ai-bid-document-analysis]
4.  **建筑行业工程招标**：建筑行业的用户表示，快标书 AI 能够精准识别工程项目中的技术规范和质量要求，大大减少了因对招标文件理解偏差导致的投标失败情况。[来源：https://www.kuaibiaoshu.com/course/ai-bid-document-analysis]
5.  **大型平台批量处理**：大型平台一周可能需处理上千份公告，传统逐条人工录入根本不现实，需要实现“批量上传、自动抽取、一键校验”。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
6.  **销售跟进与商机分析**：销售面对招标时，需要快速抓准招标关键条款，对比历史招标数据，避免漏看条款导致的投标失败。[来源：https://www.bailian-ai.com/news/2243.html]
7.  **招标文件检测与合规性审查**：结合有关政策法规要求，对招标文件开展合规性、合理性、错敏词等多维度检测，自动识别各类违法违规和排斥限制竞争等问题。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
8.  **智能辅助评标**：打造类人化的评审推理能力，辅助专家开展评审或生成结果供专家参考，提升评标的公正性。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
9.  **围串标识别**：构建“主体 + 行为”全覆盖的综合预警体系，通过多维数据碰撞和主体画像，穿透式发现企业特征信息雷同，主体关系、投标行为、中标概率异常等问题。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

## 不适用场景

1.  **替代自主判断与法定责任**：坚持技术的辅助性定位，模型生成的结论不替代招标人、招标代理机构、投标人、评标专家等的自主判断，不改变使用主体的法定责任。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
2.  **无结构化需求的简单文本**：如果文档是纯文本且结构简单，无需复杂解析，直接使用大模型可能过度工程。[来源：https://cloud.tencent.com/developer/article/2631225]（推断：文中强调复杂版式 + 表格 + 长文档才需要解析引擎）
3.  **对数据安全性要求极高且无法上云的场景**：严格落实人工智能模型安全管理要求，强化模型算法、数据资源、基础设施、应用系统等安全能力建设，严格开展算法、模型备案和安全审核。若无法通过安全审核，则不适用。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
4.  **缺乏高质量数据集支撑的模型训练**：各地要加强招标投标数据治理，强化数据清洗和标注，加快构建涵盖招标投标政策法规和全流程各环节的高质量数据集和知识库。若缺乏数据基础，模型精准度无法保障。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
5.  **县级及以下无上级模型资源复用的场景**：地市应当在省级层面统筹指导下开展部署应用，县级及以下原则上应当复用上级的模型资源。若无法复用且无独立建设能力，则不适用。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

## 风险与约束

1.  **信息丢失与截断风险**：文档过长会被截断，信息丢失。单纯让大模型直接“硬读”全文常会翻车。[来源：https://cloud.tencent.com/developer/article/2631225]
2.  **解析能力不足风险**：无法可靠解析扫描件、复杂表格和特殊版式。招标文件来源很杂：有的是电子版、有的是扫描版、有的来自截图/拍照版。[来源：https://cloud.tencent.com/developer/article/2631225]
3.  **幻觉与不可溯源风险**：生成的总结常常笼统，无法提供可验证的原文引用。投标场景里，单单给出风险提示没用，必须能指回原文：第几页、哪一段、哪张表。[来源：https://cloud.tencent.com/developer/article/2631225]
4.  **数据格式与逻辑错误风险**：生成的 JSON 格式可能出现结构问题、不正确的语法、特殊字符等问题。时间逻辑是否成立（如投标截止时间不能晚于开标时间）？金额字段有没有异常？[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
5.  **模型黑箱与算法歧视风险**：有效防范和应对模型黑箱、幻觉和算法歧视等风险。严格开展算法、模型备案和安全审核。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
6.  **规格漂移风险**：模型生成的结论不替代自主判断，不改变使用主体的法定责任。若过度依赖 AI 可能导致责任主体不清。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
7.  **上下文理解局限性**：招投标文书语言极具行业特色，同样是“金额”，有的写成"¥1,000,000"，有的写“壹佰万元整”；同样是“时间”，既可能出现在正文段落中，也可能藏在表格里。若没有上下文理解和对领域语言的适配能力，提取出的结果往往前后矛盾、缺乏价值。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
8.  **人工复核成本**：现实中，即使部分机构已尝试用传统 OCR 或规则提取工具来处理此类文档，但面对 PDF 格式混乱、表格嵌套、金额大小写并存等情况，提取效果仍不理想，最终还是得依赖人工去二次校验。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

**应对措施：**
- 采用“解析引擎 + 大模型”分层架构，先用专业解析引擎将复杂版式转换为结构化内容。[来源：https://cloud.tencent.com/developer/article/2631225]
- 输出可追溯的原文定位信息，让输出更专业、客户更信任。[来源：https://cloud.tencent.com/developer/article/2631225]
- 建立数据校验和修复机制，通过轻量规则或高级模型推理进行自动修正，大幅降低人工复核负担。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- 坚持技术的辅助性定位，模型生成的结论不替代自主判断。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- 建立用户评价反馈机制，及时收集、处理用户需求，完善应用功能，以用户反馈驱动模型迭代优化。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

## 信源质量门控记录

### 门控规则
- Tavily score < 0.4：剔除
- 已知低质域名：剔除
- 重复 URL：合并保留最高分结果
- Exa 学术/语义结果：默认保留，但进入来源等级评估
- C/D 级来源不得作为唯一结论依据
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`

### 保留信源
1. [A Large Language Model-based Framework for Semi-Structured Tender Document Retrieval-Augmented Generation](https://arxiv.org/html/2410.09077v1) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
2. [Large Language Model for Extracting Complex Contract Information in Industrial Scenes](https://arxiv.org/html/2507.06539v2) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
3. [ExtractBench: A Benchmark and Evaluation Methodology for Complex Structured Extraction](https://arxiv.org/html/2602.12247) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
4. [Retrieval Augmented Structured Generation: Business Document Information Extraction As Tool Use](https://arxiv.org/html/2405.20245) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
5. [Intelligent Processing of Design Notices in Engineering Procurement Construction Projects](https://www.mdpi.com/2075-5309/15/5/805) - 来源等级：B - 入库映射：`source-quality: high` - 保留原因：Exa 学术/语义结果
6. [BenchBench: Benchmarking Automated Benchmark Generation](https://www.arxiv.org/pdf/2603.20807) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
7. [BIMCoder: A Comprehensive Large Language Model Fusion Framework for Natural Language-Based BIM Information Retrieval](https://www.mdpi.com/2076-3417/15/14/7647) - 来源等级：B - 入库映射：`source-quality: high` - 保留原因：Exa 学术/语义结果
8. [Meta-Prompting Generative AI for Standards-Based IT Project Management Documentation Using Business Data Semantics | Springer Nature Link](https://link.springer.com/chapter/10.1007/978-3-032-23241-0_12) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
9. [READoc: A Unified Benchmark for Realistic Document Structured Extraction](https://arxiv.org/html/2409.05137) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
10. [Arctic-Extract Technical Report](https://arxiv.org/html/2511.16470v1) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
11. [AuditWen: An Open-Source Large Language Model for Audit](https://arxiv.org/html/2410.10873v1) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
12. [[2309.12132v2] Automating construction contract review using knowledge graph-enhanced large language models](https://arxiv.org/abs/2309.12132v2) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
13. [[2603.22513v1] Generating and Evaluating Sustainable Procurement Criteria for the Swiss Public Sector using In-Context Prompting with Large Language Models](https://arxiv.org/abs/2603.22513v1) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
14. [[2603.02239v1] Engineering Reasoning and Instruction (ERI) Benchmark: A Large Taxonomy-driven Dataset for Foundation Models and Agents](https://arxiv.org/abs/2603.02239v1) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
15. [[2105.06083] Cross-Domain Contract Element Extraction with a Bi-directional Feedback Clause-Element Relation Network](https://arxiv.org/pdf/2105.06083) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：学术论文
16. [标书智能体（一）——AI 解析招标文件代码 + 提示词 - 易标 AI - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673) - 来源等级：B - 入库映射：`source-quality: high` - 保留原因：与主题高度相关
17. [数据提取 - 智谱 AI 开放文档](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：官方文档 / 一手数据
18. [90% 的投标人还在手动读标书？快标书 AI 解析功能直接提炼标书重点 - 快标书 AI](https://www.kuaibiaoshu.com/course/ai-bid-document-analysis) - 来源等级：C - 入库映射：`source-quality: medium` - 保留原因：相关性一般，需交叉验证
19. [招标解析（已下线） - 智谱 AI 开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：官方文档 / 一手数据
20. [易标 AI - 博客园](https://www.cnblogs.com/yibiaoai) - 来源等级：C - 入库映射：`source-quality: medium` - 保留原因：相关性一般，需交叉验证
21. [【关于加快招标投标领域人工智能推广应用的实施意见】- 国家发展和改革委员会](https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html) - 来源等级：C - 入库映射：`source-quality: medium` - 保留原因：相关性一般，需交叉验证
22. [如何利用 AI 工具快速分析招标文件中的关键条款 - 百炼智能](https://www.bailian-ai.com/news/2243.html) - 来源等级：C - 入库映射：`source-quality: medium` - 保留原因：相关性一般，需交叉验证
23. [国家新政落地，企业如何抢占招标投标智能化先机？](https://www.yonyou.com/subject/caigou-liucheng/news/5280) - 来源等级：C - 入库映射：`source-quality: medium` - 保留原因：相关性一般，需交叉验证
24. [AI 员工提示词工程指南 - NocoBase 文档](https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide) - 来源等级：A - 入库映射：`source-quality: high` - 保留原因：官方文档 / 一手数据
25. [零代码搭建「招标文件解析智能体」：Coze+TextIn xParse 实现 PDF 上传自动提条款、标风险、出建议 - 腾讯云开发者社区 - 腾讯云](https://cloud.tencent.com/developer/article/2631225) - 来源等级：C - 入库映射：`source-quality: medium` - 保留原因：相关性一般，需交叉验证
26. [高效速搭基于 DeepSeek 的招标文书智能写作 Agent-腾讯云开发者社区 - 腾讯云](https://cloud.tencent.com/developer/article/2498790) - 来源等级：C - 入库映射：`source-quality: medium` - 保留原因：相关性一般，需交叉验证
27. [关于加快招标投标领域人工智能推广应用的实施意见 (发改法规〔2026 ...](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html) - 来源等级：C - 入库映射：`source-quality: medium` - 保留原因：相关性一般，需交叉验证
28. [人工智能 + 招投标迎关键节点，南方财经 AI 智审打造数智赋能场景 - 21 经济网](https://www.21jingji.com/article/20260314/herald/c5bcc1467f71b37449cc86b084249342.html) - 来源等级：C - 入库映射：`source-quality: medium` - 保留原因：相关性一般，需交叉验证
29. [企业招投标文件自动比对工具：核心能力解析与智能化落地指南 - 实在智能](https://www.ai-indeed.com/encyclopedia/18040.html) - 来源等级：C - 入库映射：`source-quality: medium` - 保留原因：相关性一般，需交叉验证
30. [招投标审查文档解析_评分项提取/资格项识别/比对前处理_TextIn](https://www.textin.com/scenarios/tender-review-parse) - 来源等级：C - 入库映射：`source-quality: medium` - 保留原因：相关性一般，需交叉验证

### 剔除信源
1. [标书智能体（一）——AI 解析招标文件代码 + 提示词 - 易标 AI - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673) - 剔除原因：重复 URL，已合并到最高分结果
2. [数据提取 - 智谱 AI 开放文档](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction) - 剔除原因：重复 URL，已合并到最高分结果
3. [招标解析（已下线） - 智谱 AI 开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender) - 剔除原因：重复 URL，已合并到最高分结果
4. [高效速搭基于 DeepSeek 的招标文书智能写作 Agent-腾讯云开发者社区 - 腾讯云](https://cloud.tencent.com/developer/article/2498790) - 剔除原因：重复 URL，已合并到最高分结果
5. [企业招投标文件自动比对工具：核心能力解析与智能化落地指南 - 实在智能](https://www.ai-indeed.com/encyclopedia/18040.html) - 剔除原因：重复 URL，已合并到最高分结果
6. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统 - Google Patents](https://patents.google.com/patent/CN119624385A/zh) - 剔除原因：score 低于 0.4
7. [AI 提示工程指南 - Google Cloud](https://cloud.google.com/discover/what-is-prompt-engineering?hl=zh-CN) - 剔除原因：score 低于 0.4
8. [Ant Group 2025 Sustainability Report Highlights Record AI R&D Investment – Company Announcement - Financial Times](https://markets.ft.com/data/announce/detail?dockey=600-202606170512BIZWIRE_USPRX____20260617_BW847068-1) - 剔除原因：score 低于 0.4
9. [EBAday 2026: Zooming in on AI and digital assets as the key themes of the event - Finextra Research](https://www.finextra.com/newsarticle/47948/ebaday-2026-zooming-in-on-ai-and-digital-assets-as-the-key-themes-of-the-event) - 剔除原因：score 低于 0.4
10. [China's 5-Year Plan for Agricultural and Rural Modernisation Sets Ambitious Targets for 2030 - Global Agriculture](https://www.global-agriculture.com/global-agriculture/chinas-5-year-plan-for-agricultural-and-rural-modernisation-sets-ambitious-targets-for-2030/) - 剔除原因：score 低于 0.4
11. [Infringement risks of AIGC in the entertainment industry (Part 2) | China - Law.asia](https://law.asia/generative-ai-entertainment-industry-part-2/) - 剔除原因：score 低于 0.4
12. [China's reported AIDC plan could put telcos at center of AI ecosystem - RCR Wireless News](https://www.rcrwireless.com/20260617/carriers/china-aidc-telcos) - 剔除原因：score 低于 0.4
13. [WorldBridge Group and DRSB Express Forge Strategic Alliance to Boost Cambodia's Cross-Border E-Commerce and Logistics Sector - Cambodia Investment Review](https://cambodiainvestmentreview.com/2026/06/22/worldbridge-group-and-drsb-express-forge-strategic-alliance-to-boost-cambodias-cross-border-e-commerce-and-logistics-sector/) - 剔除原因：score 低于 0.4
14. [Russia-BRICS Agricultural Trade Up 5% In 2025 As BRICS Agriculture Ministers Meet In India - russia's pivot to asia](https://russiaspivottoasia.com/russia-brics-agricultural-trade-up-5-in-2025-as-brics-agriculture-ministers-meet-in-india/) - 剔除原因：score 低于 0.4
15. [In-house Counsel Awards 2026 - Law.asia](https://law.asia/china-in-house-counsel-awards-2026/) - 剔除原因：score 低于 0.4
16. [A+H dual listings signal China healthcare's shift toward global expansion - Asian Business Review](https://asianbusinessreview.com/in-focus/ah-dual-listings-signal-china-healthcares-shift-toward-global-expansion) - 剔除原因：score 低于 0.4
17. [Before AI: Fixing the Hidden Modernization Barriers Blocking Federal Agency Progress - Defense One](https://www.defenseone.com/assets/ai-fixing-hidden-modernization-barriers/portal/) - 剔除原因：score 低于 0.4
18. [标书智能体（一）——AI 解析招标文件代码 + 提示词 - 易标 AI - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673) - 剔除原因：重复 URL，已合并到最高分结果
19. [如何利用 AI 工具快速分析招标文件中的关键条款 - 百炼智能](https://www.bailian-ai.com/news/2243.html) - 剔除原因：重复 URL，已合并到最高分结果
20. [招标解析（已下线） - 智谱 AI 开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender) - 剔除原因：重复 URL，已合并到最高分结果
21. [关于加快招标投标领域人工智能推广应用的实施意见 (发改法规〔2026 ...](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260210_1403680.html) - 剔除原因：score 低于 0.4
22. [高效速搭基于 DeepSeek 的招标文书智能写作 Agent-腾讯云开发者社区 - 腾讯云](https://cloud.tencent.com/developer/article/2498790) - 剔除原因：score 低于 0.4
23. [大模型提示词工程指南 | Prompt Engineering Guide](https://yeasy.gitbook.io/prompt_engineering_guide) - 剔除原因：score 低于 0.4
24. [AI 提示工程指南 - Google Cloud](https://cloud.google.com/discover/what-is-prompt-engineering?hl=zh-CN) - 剔除原因：score 低于 0.4
25. [企业招投标文件自动比对工具：核心能力解析与智能化落地指南 - 实在智能](https://www.ai-indeed.com/encyclopedia/18040.html) - 剔除原因：score 低于 0.4
26. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统 - Google Patents](https://patents.google.com/patent/CN119624385A/zh) - 剔除原因：score 低于 0.4
27. [标书智能体（一）——AI 解析招标文件代码 + 提示词 - 易标 AI - 博客园](https://www.cnblogs.com/yibiaoai/p/19064673) - 剔除原因：重复 URL，已合并到最高分结果
28. [数据提取 - 智谱 AI 开放文档](https://docs.bigmodel.cn/cn/best-practice/case/data-extraction) - 剔除原因：重复 URL，已合并到最高分结果
29. [招标解析（已下线） - 智谱 AI 开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender) - 剔除原因：重复 URL，已合并到最高分结果
30. [如何利用 AI 工具快速分析招标文件中的关键条款 - 百炼智能](https://www.bailian-ai.com/news/2243.html) - 剔除原因：重复 URL，已合并到最高分结果
31. [高效速搭基于 DeepSeek 的招标文书智能写作 Agent-腾讯云开发者社区 - 腾讯云](https://cloud.tencent.com/developer/article/2498790) - 剔除原因：重复 URL，已合并到最高分结果
32. [企业招投标文件自动比对工具：核心能力解析与智能化落地指南 - 实在智能](https://www.ai-indeed.com/encyclopedia/18040.html) - 剔除原因：score 低于 0.4
33. [CN119624385A - 一种基于人工智能的招标文件自动审核方法及系统 - Google Patents](https://patents.google.com/patent/CN119624385A/zh) - 剔除原因：score 低于 0.4
34. [招标中标信息抽取高级版 API 参考与调用示例 - 自然语言处理 - 阿里云](https://help.aliyun.com/zh/document_detail/256460.html) - 剔除原因：score 低于 0.4
35. [犀牛书 - 中文技术文档大全](https://xiniushu.com) - 剔除原因：score 低于 0.4

## 来源与可信度

| 来源标题 | 来源类型 | 可信度 | 支撑内容 |
| --- | --- | --- | --- |
| 关于加快招标投标领域人工智能推广应用的实施意见 - 国家发展和改革委员会 | 政府政策 | 高 | 政策目标、20 个应用场景、实施要求 |
| 数据提取 - 智谱 AI 开放文档 | 官方文档 | 高 | 技术架构、代码示例、Prompt 策略、校验规则、Batch API 数据 |
| 标书智能体（一）——AI 解析招标文件代码 + 提示词 - 易标 AI - 博客园 | 技术博客 | 高 | Python 代码、Prompt 模板、异步请求实现 |
| AI 员工提示词工程指南 - NocoBase 文档 | 官方文档 | 高 | 提示词九要素、模板、优化原则 |
| 零代码搭建「招标文件解析智能体」：Coze+TextIn xParse 实现 PDF 上传自动提条款、标风险、出建议 - 腾讯云开发者社区 | 技术文章 | 中 | 架构设计、Coze 实操步骤、提示词模板 |
| 90% 的投标人还在手动读标书？快标书 AI 解析功能直接提炼标书重点 - 快标书 AI | 产品博客 | 中 | 产品功能、效能数据（70% 时间缩短）、使用流程 |
| 如何利用 AI 工具快速分析招标文件中的关键条款 - 百炼智能 | 产品博客 | 中 | 痛点分析、产品功能、效能数据（1.5 小时节省） |
| 招标解析（已下线） - 智谱 AI 开放文档 | 官方文档 | 高 | API 接口、价格、请求参数 |
| A Large Language Model-based Framework for Semi-Structured Tender Document Retrieval-Augmented Generation | 学术论文 | 高 | 学术框架、评估步骤 |

## 对于可信度较高的来源逐来源总结

### 1. 关于加快招标投标领域人工智能推广应用的实施意见 - 国家发展和改革委员会
- **核心内容**：提出了招标投标领域人工智能推广应用的总体目标（2026 年底部分省市全覆盖，2027 年底全国推广），详细列出了 20 个应用场景（招标、投标、开标、评标、定标、现场管理、监管），并规定了规范部署实施的要求（科学组织、系统集成、数据基础、迭代优化、应用机制、安全水平）。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- **可用事实**：政策发布时间 2026/02/10，文号发改法规〔2026〕195 号。20 个具体场景名称及描述。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- **局限**：政策文件主要提供指导方向，不包含具体技术实现代码或工具配置细节。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- **适合入库的知识点**：政策目标时间节点、20 个应用场景列表、安全与责任定位原则。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]

### 2. 数据提取 - 智谱 AI 开放文档
- **核心内容**：提供了完整的招投标数据提取解决方案，包括输入模块、预处理模块、LLM 处理模块、数据后处理模块、数据校验模块、数据修复模块。包含详细的 Python 代码示例、Prompt 模板、JSON 标准化代码、校验逻辑代码。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- **可用事实**：Batch API 效能数据（1 亿请求从 340 天缩短至 8.6 天，价格减半），日期格式化标准（14 位），金额校验逻辑。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- **局限**：部分代码示例可能需要根据实际 API 版本调整。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- **适合入库的知识点**：数据提取全流程架构、Prompt 策略、校验代码、Batch API 性能数据。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]

### 3. 标书智能体（一）——AI 解析招标文件代码 + 提示词 - 易标 AI - 博客园
- **核心内容**：提供了基于 Python+React 的开源 AI 写标书智能体实现细节，包括 Word/PDF 文件提取代码（docx2python, pdfplumber）、AsyncOpenAI 异步请求封装、招标文件解析提示词（项目概述、技术评分要求）。[来源：https://www.cnblogs.com/yibiaoai/p/19064673]
- **可用事实**：具体的 Prompt 内容（SystemPrompt/UserPrompt），代码实现细节（gc.collect 资源释放）。[来源：https://www.cnblogs.com/yibiaoai/p/19064673]
- **局限**：博客文章，代码可能需要根据实际环境调试。[来源：https://www.cnblogs.com/yibiaoai/p/19064673]
- **适合入库的知识点**：文件提取代码、异步请求封装、招标文件解析专用 Prompt。[来源：https://www.cnblogs.com/yibiaoai/p/19064673]

### 4. AI 员工提示词工程指南 - NocoBase 文档
- **核心内容**：提供了提示词“九要素”黄金公式（起名、双重指令、模拟确认、反复强调、强制规则、背景信息、正向激励、参考示例、反面示例），包含快速上手模板、实战示例、优化原则（正面 80% : 负面 20%）。[来源：https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide]
- **可用事实**：九要素表格说明，提示词长度建议（基础 500-800 字符，复杂 800-1500 字符）。[来源：https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide]
- **局限**：通用指南，非专门针对招投标场景，但方法论适用。[来源：https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide]
- **适合入库的知识点**：提示词九要素、优化流程、长度建议。[来源：https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide]

### 5. 招标解析（已下线） - 智谱 AI 开放文档
- **核心内容**：提供了招标解析智能体的 API 接口详情，包括价格（5 元/百万 Tokens）、请求地址、请求参数（agent_id, stream, messages, custom_variables）。[来源：https://docs.bigmodel.cn/cn/guide/agents/tender]
- **可用事实**：接口地址 `https://open.bigmodel.cn/api/v1/agents`，agent_id 参数值。[来源：https://docs.bigmodel.cn/cn/guide/agents/tender]
- **局限**：文档标注“已下线”，可能 API 已变更或不可用。[来源：https://docs.bigmodel.cn/cn/guide/agents/tender]
- **适合入库的知识点**：API 参数结构、价格信息。[来源：https://docs.bigmodel.cn/cn/guide/agents/tender]

## 跨源矛盾检测结论

### 检测范围
- 已精读来源数量：10 个
- 检测对象：核心数字、日期、功能描述、因果判断、市场/公司事实
- 检测时间：2026-06-22

### 检测结果
结论：检测到 1 处跨源矛盾，综合输出时必须保留双方表述，不得静默合并。

### 矛盾项 1：智谱 AI 招标解析智能体 Agent ID
- 矛盾描述：智谱 AI 开放文档中关于招标解析智能体的 Agent ID 描述不一致。
- 来源 A：[招标解析（已下线） - 智谱 AI 开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender)
  - 原文引用：“请求参数表格中 agent_id 参数说明为：智能体 ID：`bidwin_parser_agent`"
  - 来源等级：A
  - 发布时间 / 数据日期：2026-06-22（证据包生成时间）
- 来源 B：[招标解析（已下线） - 智谱 AI 开放文档](https://docs.bigmodel.cn/cn/guide/agents/tender)
  - 原文引用："**体验中心** 点击立即体验链接中 agentId 为 `bidding_parser_agent`"
  - 来源等级：A
  - 发布时间 / 数据日期：2026-06-22（证据包生成时间）
- 初步判断：
  - 倾向：暂不倾向
  - 理由：同一文档内部矛盾，可能是文档更新不同步或笔误。
- 综合输出要求：
  - 必须写成“来源文档表格中说 `bidwin_parser_agent`，体验链接中说 `bidding_parser_agent`，建议人工核实”
  - 禁止取平均值、合并成第三种说法、只保留其中一方

## 矛盾与待验证问题

- **Agent ID 不一致**：智谱 AI 招标解析智能体文档中，请求参数表格显示 agent_id 为 `bidwin_parser_agent`，而体验中心链接显示 agentId 为 `bidding_parser_agent`。建议在实际调用前通过官方渠道核实最新 ID。[来源：https://docs.bigmodel.cn/cn/guide/agents/tender]
- **文档下线状态**：智谱 AI 招标解析文档标题标注“已下线”，但内容仍提供 API 详情和体验链接。需验证该智能体是否仍可用或已迁移至其他入口。[来源：https://docs.bigmodel.cn/cn/guide/agents/tender]
- **政策落地时间**：政策文件发布时间为 2026/02/10，目标 2026 年底部分省市全覆盖。需验证当前实际落地进度是否符合预期。[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- **效能数据真实性**：快标书 AI 宣称投标准备时间平均缩短了 70%，百炼智能宣称省出 1.5 小时。这些数据基于特定案例，需在实际项目中交叉验证。[来源：https://www.kuaibiaoshu.com/course/ai-bid-document-analysis] [来源：https://www.bailian-ai.com/news/2243.html]
- **模型版本差异**：不同来源提到的模型版本不同（GLM-4-AIR, GLM-4-Plus, DeepSeek-R1, gpt-3.5-turbo），不同模型对复杂表格和长文档的处理能力可能存在差异，需根据实际场景选择。[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction] [来源：https://www.kuaibiaoshu.com/course/ai-bid-document-analysis] [来源：https://www.cnblogs.com/yibiaoai/p/19064673]

## 原始证据摘录

- **政策目标**："2026 年底，招标文件检测、智能辅助评标、围串标识别等重点场景在部分省市实现全覆盖应用；2027 年底，更多重点场景在全国范围内推广应用”[来源：https://www.ndrc.gov.cn/xwdt/tzgg/202602/t20260210_1403681.html]
- **架构原则**：“更稳的打法是：先把文档变成结构化可理解的内容，再让大模型做抽取和风控。”[来源：https://cloud.tencent.com/developer/article/2631225]
- **提示词公式**：“起名 + 双重指令 + 模拟确认 + 反复强调 + 强制规则 + 背景信息 + 正向激励 + 参考示例 + 反面示例（可选）”[来源：https://docs.nocobase.com/cn/ai-employees/configuration/prompt-engineering-guide]
- **Batch API 数据**："1 亿请求（2048 tokens）... 正常请求 340 天 204,800 元 ... Batch 请求 8.6 天 (40 倍效率) 102,400 元（省钱一半）”[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- **效能数据**：“投标准备时间平均缩短了 70%"[来源：https://www.kuaibiaoshu.com/course/ai-bid-document-analysis]
- **代码片段**：
```python
def validate_time_order(submit_time, open_time):
    submit_dt = datetime.strptime(submit_time, "%Y%m%d%H%M%S")
    open_dt = datetime.strptime(open_time, "%Y%m%d%H%M%S")
    return submit_dt <= open_dt
```
[来源：https://docs.bigmodel.cn/cn/best-practice/case/data-extraction]
- **Agent ID 矛盾**：“智能体 ID：`bidwin_parser_agent`"vs"agentId=bidding_parser_agent"[来源：https://docs.bigmodel.cn/cn/guide/agents/tender]