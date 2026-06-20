---
title: "几何图形与表格类题目处理策略调研"
source-type: article
generated: 2026-06-11
generated-by: wiki-research-skill
research-topic: "AI 智能命题系统中几何图形、函数图像、坐标系、统计图、表格类题目的数字化处理策略"
wiki-first-query: true
external-research-used: true
---

# 几何图形与表格类题目处理策略调研

## 调研背景

本次调研服务于“AI 智能命题系统 · 数学学科”讨论点 #7：几何图形、函数图像、坐标系、统计图、表格类题目如何处理。当前 BRD 已明确系统需要支持 PDF / 图片格式题库导入、自动拆题、Word 导出、数学公式渲染、几何图形题显示，以及生成题人工校验流程；同时也明确本期不做复杂机器阅卷，生成题必须符合学段用语与教师审核要求。

Wiki 优先查询结果：已读取 `SCHEMA.md` 与 `wiki/_index.md`，并在 `wiki/` 中检索“几何、图形、图像、坐标、统计图、表格、图文、OCR、多模态、视觉问答、TikZ、SVG、LaTeX”等关键词。现有 Wiki 只有间接的方法论页面，没有可直接回答本讨论点的知识页，因此按 `wiki-research` 技能要求执行外部调研。

## 核心结论

1. 图形题不应只做“OCR 成文本”。现代文档解析研究正在从文本中心 OCR 转向“文本、表格、公式、图表、图形一起解析”的多模态 OCR；可复用资产应同时保留文本、版面、裁片、坐标和可选结构化表达。[来源: https://arxiv.org/html/2603.13032] 可信度：高。

2. 数学图形理解仍是多模态模型短板，尤其是细粒度定位、几何关系识别和图文冲突场景。Math Blind 显示现有 MLLM 在细粒度 grounding 上表现很差，结构化图元、关系和 bounding box 训练能显著改善感知能力。[来源: https://arxiv.org/html/2503.20745] 可信度：高。

3. 对 AI 命题系统而言，默认落地形态应是“Markdown/LaTeX 题文 + 图片裁片 + 元数据 JSON”，而不是强制把所有图表重建成 SVG/TikZ/JSON。只有当图表内容需要检索、重组、参数化出题或自动判题时，才进入结构化重建。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0] [来源: https://docs.mathpix.com/] 可信度：高。

4. 表格类题目应优先结构化，至少保存单元格文本、行列索引、合并单元格、表头角色和 cell-level 坐标；复杂表格在 Markdown 中容易失真，Azure Document Intelligence 已将复杂表格 Markdown 表示改为 HTML table，以支持合并单元格和多行表头。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0] 可信度：高。

5. 几何图形、函数图像和统计图的结构化应分层：先做裁片与图题绑定，再做图中标注 OCR，最后按需要抽取坐标轴、点线面、角度、长度、函数曲线、统计数据等结构。直接依赖通用 VLM 的“一步解释”风险高，必须保留原图裁片供人工复核。[来源: https://arxiv.org/html/2503.20745] [来源: https://arxiv.org/html/2403.14624] 可信度：高。

6. TikZ/SVG 适合“可渲染、可编辑、可参数化”的图形资产，但目前更适合用于标准图形重建、生成图形和训练数据，不适合作为所有历史题库导入的强制格式。MOCR 也明确指出复杂自然图像或缺乏简洁程序描述的内容应保留为 raster，而可程序化图形才转 SVG。[来源: https://arxiv.org/html/2603.13032] [来源: https://arxiv.org/html/2603.03072] 可信度：高。

7. 多图题和图文穿插题需要在资产模型里显式表达“题干片段顺序”和“图片依赖关系”。MV-MATH 显示真实 K-12 多图数学题普遍存在多图交错，顺序输入优于合并输入，且模型在图依赖任务上明显弱于图无关任务。[来源: https://arxiv.org/html/2502.20808] 可信度：高。

8. 当前项目本期建议采用“保真入库 + 半结构化增强 + 人工校验”的路线：先确保题目可显示、可搜索、可导出、可追溯；再逐步对高频题型建立可验证结构化模板。该结论来自文档智能官方能力、数学多模态评测与项目 BRD 的时间约束综合判断。[来源: https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk] [来源: https://arxiv.org/html/2409.02834v1] 可信度：高。

## 内容整理

### 1. 题目数字化不是单一 OCR，而是“题目资产化”

几何图形、函数图像、坐标系、统计图和表格题的核心难点是：信息不只在文字中，也在空间关系、图中标注、图表结构、题干与图的绑定关系里。MOCR 将文档解析定义为同时解析文本、版面结构、表格和信息密集图形，并把图表、示意图、图标等作为一等解析对象，而不是裁掉后丢给下游。[来源: https://arxiv.org/html/2603.13032]

对题库系统来说，单题资产至少应拆成以下层：

- `question_text_md`：题干、选项、解析的 Markdown / LaTeX 表示，保留数学公式。
- `source_page_image`：原始页图或 PDF 页引用，用于追溯。
- `question_crop`：整题裁片，用于人工复核和显示兜底。
- `media_assets`：题内图片、几何图、函数图像、统计图、表格裁片。
- `layout_regions`：题干、选项、解析、图、表、公式的 bounding polygon、阅读顺序和所属页。
- `semantic_metadata`：年级、知识点、题型、难度、学段用语、是否含图、是否含表、是否多图依赖。
- `structured_payload`：可选字段，对表格、图表、几何图元、函数表达式做结构化表达。
- `verification_state`：OCR 置信度、结构化置信度、教师校验状态、可用于出题/判题状态。

该分层与 Azure Document Intelligence 的 layout model 输出一致：它抽取 pages、paragraphs、text/lines/words、tables、figures、sections，并为段落、表格、图形等提供 bounding region / polygon；也与 PaddleOCR-VL 的两阶段架构一致，即先定位元素与阅读顺序，再识别文本、表格、公式和图表并输出 Markdown / JSON。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0] [来源: https://arxiv.org/html/2510.14528v1]

### 2. 图文混排题的存储方案比较

| 方案 | 适合内容 | 优点 | 缺点 | 建议 |
| --- | --- | --- | --- | --- |
| 纯文本 | 无图题、普通应用题、简单公式题 | 检索、重组、生成最简单 | 丢失图形、表格、版面关系 | 仅用于无视觉依赖题 |
| Markdown + LaTeX | 公式题、普通图文题题干 | 兼容编辑、预览、Word 导出 | 无法表达复杂图形关系 | 作为题文主格式 |
| Markdown + 图片裁片 | 几何图、函数图、统计图、图文混排题 | 保真、落地快、可人工校验 | 图内信息不可直接检索和参数化 | 作为本期默认方案 |
| 结构化 JSON | 表格、坐标点、几何图元、知识标签、裁片坐标 | 可检索、可验证、可重组、可判题 | 标注成本高，模型误差会污染题库 | 对表格和高频图形逐步引入 |
| HTML table | 合并单元格、多级表头、复杂表格 | 比 Markdown table 更保真 | 编辑体验不如结构化表格模型 | 表格显示与导出优先采用 |
| LaTeX/TikZ | 标准几何图、函数图、可参数化图形 | 可渲染、可编辑、可生成变式 | 自动重建难，编译和样式维护成本高 | 用于 AI 新出题和人工确认后的精品题 |
| SVG | 统计图、流程图、简单示意图、矢量图 | 可渲染、可编辑、适合网页 | 数学语义弱于显式 JSON / TikZ | 用于可程序化图形的结构化副本 |
| 原图裁片 | 历史试卷、复杂图形、低置信识别内容 | 最高保真，便于追溯 | 不利于语义检索和自动改编 | 所有视觉题都必须保留 |

关键原则：显示层可以先用 Markdown + 图片，检索层需要文本摘要与图表元数据，生成层需要可控参数，判题层需要结构化答案与验证规则。不要把一个格式承担所有职责。

### 3. 表格识别与表格题处理

表格题通常比几何图更适合结构化，因为表格天然有行、列、表头、单元格和数据类型。Azure Document Intelligence 的 layout model 输出表格行列数、row span、column span、cell bounding polygon、是否 columnHeader、单元格文本 span 等信息，并支持 rotated tables；其 v4.0 的 Markdown 输出对复杂表格改用 HTML table，以支持 merged cells 和 multirow headers。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0]

PaddleOCR-VL 将表格识别作为独立元素级任务，目标是抽取 cell content、rows、columns 和表格元素之间的逻辑关系，并生成 OTSL 结构化表示；它还将最终文档聚合为 Markdown 和 JSON。[来源: https://arxiv.org/html/2510.14528v1]

AI 命题系统中的表格建议保存：

- `table_html`：保真渲染和 Word 导出。
- `table_matrix`：二维数组，保留 `row_index`、`col_index`、`row_span`、`col_span`。
- `header_cells`：列头、行头、多级表头。
- `cell_bboxes`：每个单元格在裁片或页面内的坐标。
- `table_caption`：表题或题干中指向表格的句子。
- `table_semantic_summary`：用于检索的自然语言摘要，例如“某班成绩频数分布表，包含分数段与人数”。
- `extraction_confidence`：表格识别置信度与人工校验状态。

本期建议：表格题默认结构化到 `HTML + matrix JSON + 原图裁片`。如果表格是题干条件的一部分，则未经人工校验不得用于自动出变式题或自动判题。

### 4. 几何图形、函数图像、坐标系和统计图处理

#### 4.1 几何图形

几何图是符号图，不是普通自然图像。Math Blind 指出图形由精确几何结构和符号标注构成，通用 MLLM 对 shape classification、object counting、relationship identification、object grounding 都会出错，尤其 fine-grained grounding 准确率很低；其 GEOMETRIC 数据以对象属性、bounding box 和对象关系构成图结构，训练后能显著提升感知能力。[来源: https://arxiv.org/html/2503.20745]

几何图结构化字段建议：

- 图元：点、线段、射线、直线、圆、弧、多边形、角、辅助线。
- 标注：点名、角度、长度、平行/垂直/相等等符号、阴影区域。
- 关系：相交、共线、平行、垂直、相切、全等、相似、角平分、中点。
- 坐标：图元 bbox、关键点坐标、裁片内归一化坐标。
- 语义：是否为示意图、是否按比例、是否可从图中读数。
- 验证：结构化来源是 OCR/MLLM/人工，是否已教师确认。

决策规则：如果几何图只是辅助理解，可保留图片 + 图中标注 OCR + 人工摘要；如果系统要基于该图生成同型题、改数值、判定证明条件，则必须结构化为图元关系 JSON，必要时再生成 TikZ/SVG。

#### 4.2 函数图像与坐标系

函数图像题需要区分“图上可读信息”和“题干给定条件”。MathVerse 将题干信息拆为 Descriptive Information、Implicit Property、Essential Condition：描述信息可从图直接观察，隐含性质需要视觉感知，关键数值/表达式通常必须由题干给出，缺失后无法求解。[来源: https://arxiv.org/html/2403.14624]

函数图像字段建议：

- 坐标系：坐标轴方向、刻度、原点、单位、网格。
- 曲线：函数类型、曲线数量、颜色/线型、关键点、交点、端点、顶点、渐近线。
- 标注：点名、坐标、函数表达式、区域阴影、箭头方向。
- 可读数值：从图上读出的坐标或趋势必须标注置信度，避免把示意图误当精确图。
- 题干绑定：明确哪些条件来自文字，哪些来自图中标注。

本期建议：函数图像先保留图片裁片和图内标注 OCR；对初中高频类型（一次函数、二次函数、反比例函数、坐标几何）建立人工确认后的结构化模板。

#### 4.3 统计图

统计图包括条形图、折线图、扇形图、频数分布图等。PaddleOCR-VL 将 chart recognition 作为独立任务，目标是识别 bar chart、line graph、pie chart 等并转换为 Markdown table。[来源: https://arxiv.org/html/2510.14528v1] Google Gemini layout parser 也会对 figures、charts、tables 生成文字描述，使图表数据可用于检索和 RAG。[来源: https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk]

统计图字段建议：

- 图表类型：bar、line、pie、scatter、histogram、boxplot、frequency-table 等。
- 数据系列：series name、x/y labels、legend。
- 数据点：分类名、数值、单位、百分比、读取置信度。
- 图表说明：标题、图例、注释。
- 结构化表：如果可可靠抽取，则转成 `chart_data_table`；如果不可靠，只保留裁片 + 摘要 + 待校验。

#### 4.4 多图与图文交错题

MV-MATH 收集了 2,009 道真实 K-12 多图数学题，共 6,061 张图片，部分题可包含最多 8 张图片；它将图像关系分为互相依赖和相互独立，并发现当前 MLLM 在多图数学任务上与人类有显著差距，图像依赖任务更难，顺序输入优于合并输入。[来源: https://arxiv.org/html/2502.20808]

资产模型必须表达：

- `content_blocks`：按题干原顺序记录 text、formula、image、table。
- `media_order`：图片在题干中的出现顺序。
- `dependency_type`：单图、独立多图、互相依赖多图。
- `reference_text`：题干中“如图”“上图”“表 1”等指代文本与媒体 ID 的绑定。
- `merged_preview`：用于教师预览的整题裁片或渲染图。

### 5. 图中标注 OCR、图题绑定与裁剪

落地流程应从版面检测开始，而不是直接让 VLM 读整页。Azure 的 layout model 会抽取 figures 的 `boundingRegions`、`spans`、`elements`、`caption`，并可通过 `output=figures` 生成所有 detected figures 的 cropped images；但官方也说明 figures/tables 的 bounding regions 只覆盖核心内容，不包括 caption 和 footnotes，因此系统需要额外做 caption/题干绑定。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0]

建议裁片规范：

- 保存原始页：`source_page_id`、页码、页图 hash、DPI、宽高。
- 保存整题裁片：包含题号、题干、选项、图表、解析的最小完整区域。
- 保存媒体裁片：每个图、表、公式块独立裁剪。
- 坐标双写：页面绝对像素坐标 + 裁片内归一化坐标。
- 上下文窗口：媒体裁片额外保留周边题干/图题区域，避免 caption 被切掉。
- 绑定规则：同题范围内，最近 caption、题干指代词、阅读顺序、空间邻近共同决定绑定；低置信绑定进入人工校验。
- 文件命名：使用 `question_id`、`asset_id`、`page`、`bbox_hash`，避免依赖中文文件名。

### 6. 视觉问答 / 多模态理解的定位

VQA / MLLM 适合做“辅助理解”和“人工校验前的候选结构”，不适合直接作为唯一事实来源写入题库。MathVerse 发现一些模型去掉图片反而准确率更高，说明模型可能依赖文字捷径而不是真懂图；Math Blind 进一步指出模型在图文冲突时会过度依赖文本。[来源: https://arxiv.org/html/2403.14624] [来源: https://arxiv.org/html/2503.20745]

建议 VQA 使用方式：

- 图表摘要：生成可检索的 `visual_summary`。
- 结构候选：输出表格 JSON、几何图元 JSON、统计图数据候选。
- 异常检测：发现“题干说 A，图中标注似乎是 B”的冲突。
- 教师审核辅助：以差异高亮、低置信提示、缺失字段清单形式呈现。
- 禁止事项：未经校验不得直接用 VQA 结果改写原题、生成正式答案或判定学生答案。

## 推荐工作流

### A. 历史 PDF / 图片题库导入

1. 原始文件入库：保存 PDF、页图、hash、来源、年级、考试类型。
2. 页级版面分析：检测题号、题干、选项、解析、公式、表格、图形区域与阅读顺序。[来源: https://arxiv.org/html/2510.14528v1]
3. 拆题：按题号、空间布局、选项模式、解析区边界切分单题。
4. 裁片生成：保存整题裁片、图裁片、表裁片、公式裁片。
5. 文本与公式识别：题干和解析转 Markdown + LaTeX；保留 OCR raw。
6. 表格结构化：输出 HTML table、matrix JSON、cell bbox、表头角色。
7. 图形半结构化：输出图内标注 OCR、视觉摘要、图题绑定、是否需要进一步结构化。
8. 低置信人工校验：表格跨页、合并单元格、几何关系、函数坐标读数、图文冲突必须进入审核队列。
9. 题目资产入库：只有通过校验的结构化字段可参与检索、组卷、同型题生成和自动判题。

### B. AI 生成新题

1. 先生成题目 DSL：题干、知识点、难度、公式、答案、解析、图表需求。
2. 对无图题生成 Markdown + LaTeX。
3. 对表格题生成 `table_matrix`，再渲染 HTML/Word 表格。
4. 对函数图和统计图优先用程序化生成：Python/Matplotlib、SVG 或 TikZ，保存参数和渲染图。
5. 对几何图优先用模板化 JSON/TikZ：点线关系、标注、辅助线、已知条件。
6. 运行验证：数学结果用 SymPy 或规则校验；图表结构用 schema 校验；渲染结果人工抽检。
7. 教师确认后进入可复用题库；未确认题只可临时使用，不作为自动生成同型题的种子。

### C. 错题拍照上传与同型题

1. 拍照后先做整题裁剪、倾斜校正和清晰度检测。
2. 识别题文、公式、图表裁片。
3. 匹配题库已有题：文本 embedding + 图片 perceptual hash + 知识点标签。
4. 若命中已有题，使用已校验结构生成同型题。
5. 若未命中，只生成候选摘要和候选知识点，等待教师确认后再生成同型题。

## 适用场景

- 小学/初中数学题库导入，尤其是 PDF、拍照图片、练习册扫描件。
- 需要 Word 导出并保留公式、图形、表格排版的组卷系统。
- 需要按知识点、题型、难度检索含图题的题库系统。
- 需要从班级高频错题生成同型题，但允许教师校验后再正式入库。
- 表格、统计图、函数图、标准几何图等可逐步模板化的高频题型。
- 有明确教师审核流程、题目质量优先于全自动吞吐的教育场景。

## 不适用场景

- 本期就要求完全自动阅卷、识别手写证明过程并给步骤分的场景；BRD 已明确本期不做复杂机器阅卷。
- 对所有历史题库强制重建 TikZ/SVG/几何 JSON 的场景；这会显著拖慢上线，并引入大量结构化错误。
- 原始图像质量很差、图表被遮挡、扫描模糊、裁片缺失题干上下文的场景；这些应先进入人工修复。
- 需要严格自动判题但没有结构化答案和教师校验的图表题。
- 只有一次性打印使用、后续不检索不改编的低价值图题；保留图片裁片和题文即可。

## 风险与约束

- 结构幻觉风险：FireRed-OCR 将复杂文档解析中的错误称为 structural hallucination，表现为 Markdown 表格行列错乱、公式语法不存在、层级逻辑遗漏等；题库系统必须把格式校验和人工复核纳入流程。[来源: https://arxiv.org/html/2603.01840]
- 图文冲突风险：Math Blind 指出模型在图文冲突时可能盲信文字；历史试卷 OCR 中也可能出现题干识别正确但图中标注错误的情况。[来源: https://arxiv.org/html/2503.20745]
- Markdown 表格失真：复杂合并单元格、多级表头不适合普通 Markdown table；应保存 HTML table 或 matrix JSON。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0]
- 裁片上下文丢失：Azure 官方说明 figures/tables 的 bounding regions 可能只覆盖核心内容，不包括 caption 和 footnotes；题库裁片必须保留上下文窗口。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0]
- 多图关系错误：MV-MATH 显示多图数学题对模型仍很难，合并图片输入不如顺序输入；系统必须保留图像顺序与依赖关系。[来源: https://arxiv.org/html/2502.20808]
- TikZ/SVG 维护成本：TikZ 代码存在编译失败、包依赖、样式差异等工程成本；TikZilla 研究通过 LLM debugging 修复不可编译代码，说明这不是零成本格式。[来源: https://arxiv.org/html/2603.03072]
- 可信度约束：所有自动结构化字段都应带置信度、来源和校验状态；未校验字段不得作为判题或自动出题的唯一依据。

## 信源质量门控记录

### 门控规则

- 优先保留学术论文、官方产品文档、开源项目官方页。
- 对 Tavily / Exa 候选源做去重、相关性筛选和等级评估。
- C/D 级来源不得作为唯一结论依据。
- 抓取失败或正文不足的来源仅作为候选记录，不纳入核心事实。
- 对与本项目落地直接相关的 OCR、表格、图形、多模态数学评测来源优先精读。

### 保留信源

| 等级 | 来源 | 保留原因 | 后续处理 |
| --- | --- | --- | --- |
| A | https://arxiv.org/html/2603.13032 | MOCR 提供“文本 + 图形 + SVG/结构化”范式，直接支撑图形题资产化 | 纳入核心结论 |
| A | https://arxiv.org/html/2510.14528v1 | PaddleOCR-VL 说明文档解析两阶段架构、Markdown/JSON 输出、表格/公式/图表识别 | 纳入工程方案 |
| A | https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0 | 官方文档，提供 tables、figures、bounding regions、Markdown/HTML table 能力与限制 | 纳入落地字段设计 |
| A | https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk | 官方文档，提供 layout-aware chunking、图表描述、表格和 figures 识别思路 | 纳入检索与 RAG 影响 |
| A | https://docs.mathpix.com/ | 官方文档，确认 STEM OCR 支持 math、text、tables、chemistry diagrams、MMD 和格式转换 | 纳入导入工具背景 |
| A | https://arxiv.org/html/2503.20745 | Math Blind 证明几何图理解与 grounding 是当前 MLLM 短板 | 纳入风险和结构化必要性 |
| A | https://arxiv.org/html/2403.14624 | MathVerse 证明视觉数学题不能只看最终答案，模型会依赖文本捷径 | 纳入图文混排评估 |
| A | https://arxiv.org/html/2502.20808 | MV-MATH 覆盖 K-12 多图数学题，支撑多图顺序和依赖关系设计 | 纳入多图题模型 |
| A | https://arxiv.org/html/2409.02834v1 | CMM-Math 是中文 K-12 多模态数学数据集，提供 Mathpix 导入、JSON 解析、人工校验经验 | 纳入中文教育场景 |
| B | https://arxiv.org/html/2603.22687 | GeoTikzBridge 支撑 TikZ 作为几何结构中间表示，但偏研究前沿 | 纳入 TikZ 边界 |
| B | https://arxiv.org/html/2603.03072 | TikZilla 支撑 Text-to-TikZ 的数据、调试、RL 经验，但偏生成模型研究 | 纳入 TikZ 成本 |
| B | https://openreview.net/forum?id=OAXECnLxuk | DaVinci 支撑 scientific diagram parsing 到 TikZ，但仅 OpenReview 摘要可读 | 仅作为补充 |
| C | https://github.com/Layout-Parser/layout-parser/ | 开源工具页面抓取内容较少，但说明 layout detection + OCR pipeline 方向 | 背景参考 |
| C | https://github.com/PaddlePaddle/PaddleOCR | 官方仓库抓取内容较少，但与 PaddleOCR-VL 论文互证 | 背景参考 |

### 剔除或降权信源

| 来源 | 处理 | 原因 |
| --- | --- | --- |
| https://app.xiaomi.com/details?id=com.note.mathboard | 剔除 | 应用商店页，无法支撑系统架构事实 |
| https://comate.baidu.com/zh/page/x5kymbn4gmz | 降权 | 教程类内容，可作 TikZ 入门背景，不能支撑核心结论 |
| http://static.latexstudio.net/wp-content/uploads/2018/03/TikZ_PGFManualNotes-3.0.1a-3.pdf | 降权 | PDF 笔记偏工具使用，不直接回答题库资产模型 |
| https://bookdown.org/xiangyun/msg2nd/visualization-tikz.html | 降权 | 统计图形与 TikZ 背景相关，但非题库处理主证据 |
| https://www.cjig.cn/zh/article/doi/10.11834/jig.240610 | 降权 | 页面仅抓到元信息，正文不足，不能作为核心事实来源 |
| https://arxiv.org/pdf/2601.10104 | 剔除 | 证据包抓取正文为空，无法验证内容 |
| http://arxiv.org/pdf/2506.06727 | 剔除 | 证据包抓取正文为空，无法验证内容 |

## 来源与可信度

| 来源 | 类型 | 可信度 | 支撑内容 |
| --- | --- | --- | --- |
| https://arxiv.org/html/2603.13032 | 学术论文 | 高 | MOCR、图形作为一等解析对象、SVG/结构化表示、保留 raster 边界 |
| https://arxiv.org/html/2510.14528v1 | 学术论文 | 高 | PaddleOCR-VL、layout detection、reading order、Markdown/JSON、表格/公式/图表识别 |
| https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0 | 官方文档 | 高 | layout model、tables、figures、bounding polygon、Markdown/HTML table、裁片限制 |
| https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk | 官方文档 | 高 | layout parser、context-aware chunks、tables/figures、图表描述 |
| https://docs.mathpix.com/ | 官方文档 | 高 | STEM OCR、Mathpix Markdown、tables、math、图片/PDF 转换 |
| https://arxiv.org/html/2503.20745 | 学术论文 | 高 | 图形感知短板、grounding、结构化图元关系、人工校验必要性 |
| https://arxiv.org/html/2403.14624 | 学术论文 | 高 | MathVerse、文本冗余、图形理解评估、视觉数学题风险 |
| https://arxiv.org/html/2502.20808 | 学术论文 | 高 | 多图数学题、图像依赖、顺序输入、K-12 多图场景 |
| https://arxiv.org/html/2409.02834v1 | 学术论文 | 高 | 中文 K-12 多模态数学数据、Mathpix 导入、JSON、人工检查 |
| https://arxiv.org/html/2603.22687 | 学术论文 | 中 | TikZ 作为几何感知与推理桥梁 |
| https://arxiv.org/html/2603.03072 | 学术论文 | 中 | Text-to-TikZ、数据质量、编译调试、视觉反馈 |
| https://openreview.net/forum?id=OAXECnLxuk | 学术会议页面 | 中 | 科学图解析到 TikZ 的研究方向 |

## 对于可信度较高的来源逐来源总结

### Multimodal OCR: Parse Anything from Documents

该论文提出 MOCR，将文档中的文本、布局、表格和图形统一解析为有序文本/结构化表示。它明确批评传统 OCR 只识别文本、把图形裁成像素块的做法会丢失图表和示意图里的语义信息；MOCR 将图表、diagram、UI、icon 等转成 SVG 等可渲染结构，以便复用和重建。[来源: https://arxiv.org/html/2603.13032]

可用事实：视觉元素应作为一等资产；图形可转 SVG/结构化代码；复杂自然图像或无紧凑程序表达的图像仍应保留 raster。[来源: https://arxiv.org/html/2603.13032]

局限：论文偏研究前沿，不等同于现成教育题库系统；其当前 release 也说明 full-page parsing 与 region-level SVG decoding 仍需分开运行。[来源: https://arxiv.org/html/2603.13032]

适合入库知识点：多模态 OCR、图形结构化、图片裁片保留边界、题目资产分层。

### PaddleOCR-VL

PaddleOCR-VL 将文档解析拆成两阶段：先由 PP-DocLayoutV2 做元素定位、分类和阅读顺序预测，再由 PaddleOCR-VL-0.9B 识别文本、表格、公式、图表，最后输出结构化 Markdown 和 JSON。[来源: https://arxiv.org/html/2510.14528v1]

可用事实：表格识别抽取 cell content、rows、columns 和逻辑关系；公式识别转 LaTeX；图表识别覆盖 bar chart、line graph、pie chart 并转换为 Markdown table；论文报告支持 109 种语言。[来源: https://arxiv.org/html/2510.14528v1]

局限：论文指标来自公开与自建 benchmark，项目落地仍需根据本地试卷质量、中文教材、Word 导出链路做实测。

适合入库知识点：两阶段文档解析、表格/公式/图表元素级识别、Markdown/JSON 双输出。

### Azure Document Intelligence Layout Model

Azure 官方文档定义 layout analysis 为抽取文档区域及其相互关系，包含 geometric roles（text、tables、figures、selection marks）与 logical roles（titles、headings、footers）。它支持 PDF、图片和 Office/HTML 等文件，输出 paragraphs、tables、figures、sections 等结构。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0]

可用事实：表格输出 row/column count、row span、column span、cell bounding polygon、columnHeader 信息；Markdown 输出中复杂表格用 HTML table 支持 merged cells 和 multirow headers；figures 对象包含 boundingRegions、spans、elements、caption，并可生成 cropped images。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0]

局限：官方说明 figures/tables 的 bounding regions 只覆盖核心内容，不包括 caption 和 footnotes；因此不能直接把裁片当作完整题意。[来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0]

适合入库知识点：表格结构化字段、图表裁片规范、图题绑定风险。

### Google Gemini Layout Parser

Google 官方文档说明 Gemini layout parser 将复杂文件转成结构化、机器可读信息，识别 tables、figures、lists、headers，并保留段落与 heading 等上下文关系。其主要用途包括 Document OCR、Search/RAG、Structured Data Ingestion。[来源: https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk]

可用事实：layout-aware chunking 会把祖先 heading 和 table header 等上下文并入 chunk；layout annotation 会对 images/tables 生成描述文本，让图表内容可检索；官方限制包括在线处理文件大小、页数限制，以及不同文件类型可检测元素差异。[来源: https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk]

局限：这是云服务能力说明，具体中文数学题效果仍需样本测试。

适合入库知识点：图表摘要、RAG 检索、上下文保留。

### Mathpix Docs

Mathpix 官方文档说明其 OCR 可识别 printed/handwritten STEM document content，包括 math、text、tables、chemistry diagrams，输入支持 images、stroke data、PDF；主要输出格式为 Mathpix Markdown，且可转换为 DOCX、LaTeX、HTML、PDF、PPTX。[来源: https://docs.mathpix.com/]

可用事实：Mathpix 适合作为数学题 PDF/图片导入的一种 OCR 工具；其 MMD 对公式、表格、STEM 内容更友好。[来源: https://docs.mathpix.com/]

局限：官方首页没有提供本次所需的几何图元结构化能力证明；在 MV-MATH 和 CMM-Math 中也能看到 Mathpix 抽图数量、图片质量仍需人工过滤。[来源: https://arxiv.org/html/2502.20808] [来源: https://arxiv.org/html/2409.02834v1]

适合入库知识点：数学 OCR、MMD、导入链路。

### Math Blind

Math Blind 提出 diagram 是符号视觉语言，与自然图像不同；现有 MLLM 在 diagram 输入上会出现 flawed reasoning 和 hallucinations。它构建 MATHEMETRIC，将感知和推理隔离，覆盖 shape classification、object counting、relationship identification、object grounding，并显示当前模型在 fine-grained grounding 上表现很差。[来源: https://arxiv.org/html/2503.20745]

可用事实：结构化几何数据应包含形状、属性、关系和 bounding box；训练结构化表示可带来 grounding 提升，并迁移到推理任务。[来源: https://arxiv.org/html/2503.20745]

局限：论文是评测与训练研究，不是题库产品指南；但对“不能盲信 VLM 读图”具有强证据意义。

适合入库知识点：几何图结构化、图中标注 OCR、人工校验风险。

### MathVerse

MathVerse 关注 MLLM 是否真正“看懂”数学图形。它收集 2,612 道带图数学题，转换成六种不同图文信息版本，共 15K test samples，用于评估模型是否依赖文字冗余。论文发现多数 MLLM 仍严重依赖题干文字，有些模型无图输入反而更高。[来源: https://arxiv.org/html/2403.14624]

可用事实：图文混排题应区分可由图观察的信息、需要高阶视觉感知的隐含性质、必须由题干提供的关键条件；最终答案不能充分反映图形理解质量。[来源: https://arxiv.org/html/2403.14624]

局限：MathVerse 主要是评测集，不提供工程解析 API。

适合入库知识点：图文题条件分类、视觉数学评估、模型依赖文字风险。

### MV-MATH

MV-MATH 专门评估多图数学推理，含 2,009 道真实 K-12 多图数学题，共 6,061 张图，覆盖选择题、自由问答、多步骤题，按 11 个学科和 3 个难度标注；论文发现所有模型与人类能力有明显差距，图依赖任务更难，顺序图像输入优于合并输入。[来源: https://arxiv.org/html/2502.20808]

可用事实：真实 K-12 数学题存在多图交错；数据构建中用 Mathpix 提取文本、答案、解析和图片并组织成 JSON，但仍需验证 text-image alignment、缺失字段、语义错误和低质量图片。[来源: https://arxiv.org/html/2502.20808]

局限：英文场景为主，但结构问题对中文题库同样适用。

适合入库知识点：多图题资产模型、图像顺序、图片依赖关系。

### CMM-Math

CMM-Math 是中文多模态数学数据集，包含 28,069 个样本、15,213 张图片、23,825 个详细解答，覆盖小学到高中 12 个年级和 13 个学科。其构建流程包括从 10,000 多份数学试卷收集数据，用 Mathpix API 从 PDF 中提取 Markdown 文本和图片，再解析为 JSON 字段，并通过多轮验证修正 Mathpix 识别错误和图片识别错误。[来源: https://arxiv.org/html/2409.02834v1]

可用事实：中文 K-12 场景下，大规模试卷导入可以采用“Mathpix / OCR -> Markdown + 图片 -> JSON -> 多轮校验”的流程；图片可能出现在问题或选项中，也可能出现在答案解析中。[来源: https://arxiv.org/html/2409.02834v1]

局限：论文目标是数据集和模型评测，不直接给出产品级题库 schema。

适合入库知识点：中文数学题导入、JSON 字段、人工校验流程。

## 跨源矛盾检测结论

### 检测范围

检测对象包括核心数字、日期、功能描述、因果判断、市场/公司事实。重点比较 OCR/文档解析能力、数学图形理解能力、表格输出格式、图形结构化边界和人工校验必要性。

### 检测结果

未发现需要裁决的核心事实矛盾，但发现若干“适用边界差异”：

- 文档解析论文与官方文档都支持表格、公式、图表解析，但论文更强调模型能力，官方文档更强调 API 输出字段和限制；综合时应优先用官方文档定义工程字段，用论文说明技术趋势。[来源: https://arxiv.org/html/2510.14528v1] [来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0]
- MOCR、GeoTikzBridge、TikZilla 都强调 SVG/TikZ/代码化图形的价值，但它们没有证明所有历史题库图形都应强制代码化；MOCR 反而说明复杂自然图像应保留 raster。[来源: https://arxiv.org/html/2603.13032] [来源: https://arxiv.org/html/2603.22687] [来源: https://arxiv.org/html/2603.03072]
- MathVerse、Math Blind、MV-MATH 都指出 MLLM 数学图形理解仍弱，与“多模态模型可以直接读图解决所有题”的产品想象冲突；因此本报告不建议未经校验直接自动判题或自动结构化。[来源: https://arxiv.org/html/2403.14624] [来源: https://arxiv.org/html/2503.20745] [来源: https://arxiv.org/html/2502.20808]
- Google 文档强调图表可被描述并用于 RAG，Azure 文档强调 figures/tables 的 bounding region 与裁片访问；二者互补，不矛盾。[来源: https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk] [来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0]

## 矛盾与待验证问题

1. 未验证：本项目实际样卷中几何图、函数图、统计图、表格题的占比，需要从杨老师题库和初中样卷中抽样统计。
2. 未验证：Mathpix、PaddleOCR-VL、Azure Document Intelligence、Google Document AI 在中文小学/初中数学扫描件上的准确率，需要用本地样本 A/B 测试。
3. 未验证：Word 导出链路中 HTML table、LaTeX formula、SVG/TikZ 或图片裁片的兼容性，需要按学校打印模板测试。
4. 待确认：教师是否接受“含图题默认图片保真 + 图表元数据”的入库方式，还是希望可编辑重绘图形。
5. 待确认：本期是否需要自动结构化函数图像与统计图数据，还是只做到裁片、摘要、人工校验。
6. 待确认：题目审核 UI 是否需要展示 OCR 文本、原题裁片、结构化字段差异和低置信提示。
7. 待确认：同型题生成是否允许使用未完全结构化但已教师确认知识点/难度的图题作为参考样例。

## 原始证据摘录

> “MOCR ... jointly parses text and graphics into unified textual representations ... treats visual elements such as charts, diagrams, tables, and icons as first-class parsing targets.” [来源: https://arxiv.org/html/2603.13032]

> “For text-centric regions ... p_k corresponds to ... plain text, table markup, or LaTeX. For visual symbols ... p_k is a renderable structured representation, i.e., image-to-SVG conversion ... complex real-world imagery ... are retained as raster content.” [来源: https://arxiv.org/html/2603.13032]

> “PaddleOCR-VL performs layout detection and reading order prediction to obtain the positional coordinates and reading order of elements (text blocks, tables, formulas, and charts).” [来源: https://arxiv.org/html/2510.14528v1]

> “Finally, a lightweight post-processing module aggregates the outputs from both stages and formats the final document into structured Markdown and JSON.” [来源: https://arxiv.org/html/2510.14528v1]

> “Table Recognition ... extracting cell contents, identifying rows and columns ... generating structured representations based on OTSL ... Chart Recognition ... bar charts, line graphs, and pie charts and convert Markdown format tables.” [来源: https://arxiv.org/html/2510.14528v1]

> “Each cell with its bounding polygon is output along with information whether the area is recognized as columnHeader or not ... row and column index and bounding polygon coordinates.” [来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0]

> “For v4.0 2024-11-30 (GA), the representation of tables is changed to HTML tables to enable rendering of items like merged cells and multirow headers.” [来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0]

> “Figures ... key properties like boundingRegions, spans, elements, caption ... When output=figures is specified ... generates cropped images for all detected figures.” [来源: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-4.0.0]

> “Mathpix OCR recognizes printed and handwritten STEM document content, including math, text, tables, and chemistry diagrams ... output format is Mathpix Markdown.” [来源: https://docs.mathpix.com/]

> “MLLMs perform poorly on basic perceptual tasks ... with near-zero accuracy on fine-grained grounding ... weak diagram perception leads to blind faith in text.” [来源: https://arxiv.org/html/2503.20745]

> “The outputs are stored as structured JSON annotations specifying attributes, bounding boxes, and relationships ... images are rendered using Matplotlib ... Q&A pairs are generated using a template-based pipeline.” [来源: https://arxiv.org/html/2503.20745]

> “Most existing MLLMs struggle to understand math diagrams, relying heavily on textual questions ... some of them even achieve 5%+ higher accuracy without the visual input.” [来源: https://arxiv.org/html/2403.14624]

> “MV-MATH ... 2,009 high-quality mathematics problems ... interleaved multi-image and text ... derived from authentic K-12 sources.” [来源: https://arxiv.org/html/2502.20808]

> “Using the Mathpix API ... extract text content—such as questions, answers, and analyses—as well as images, and organized this data in JSON format ... verify the alignment between text and images.” [来源: https://arxiv.org/html/2502.20808]

> “CMM-Math contains over 28,000 high-quality samples ... across 12 grade levels from elementary to high school in China.” [来源: https://arxiv.org/html/2409.02834v1]

## 对 AI 智能命题系统的落地建议

### 题目资产模型建议

建议采用以下核心表/对象：

- `Question`：题目主记录，含题型、年级、学段、知识点、难度、题文 Markdown、答案、解析、审核状态。
- `QuestionBlock`：题内顺序块，类型为 `text | formula | image | table | chart | diagram`，保留顺序和父子关系。
- `MediaAsset`：图片/表格/图形/公式裁片，含源页、bbox、hash、DPI、文件路径、asset_type、caption、绑定置信度。
- `ParsedTable`：HTML table、matrix JSON、cell bbox、表头、数据类型、校验状态。
- `ParsedDiagram`：几何图元/坐标系/函数曲线/统计图数据候选，带结构化置信度。
- `VisualSummary`：图表自然语言摘要，用于检索和教师快速判断。
- `ExtractionAudit`：OCR 工具、模型版本、时间、置信度、人工修改记录。

### 图片裁片规范

- 每道含图题保留整题裁片和每个视觉元素裁片。
- 裁片不得只截图形主体，应保留与图形绑定的题号、caption、图中标注和相邻题干片段。
- 坐标保存为原页像素坐标与归一化坐标，便于重裁、回溯和 UI 高亮。
- 裁片文件不可作为唯一事实，应与 OCR 文本、图表摘要、结构化字段绑定。

### 图表元数据建议

- `contains_visual: true/false`
- `visual_types: ["geometry_diagram", "function_plot", "coordinate_system", "statistical_chart", "table"]`
- `visual_dependency: "decorative" | "condition_required" | "answer_required" | "multi_visual_dependent"`
- `reconstruction_level: "image_only" | "ocr_labeled" | "semi_structured" | "fully_structured" | "programmatic"`
- `usable_for_generation: true/false`
- `usable_for_auto_grading: true/false`
- `teacher_verified: true/false`

### 人工校验流程

1. 系统标红低置信题：图表题、表格跨页、几何关系、函数坐标读数、图文冲突。
2. 教师先确认“题目是否完整可显示”，再确认“结构化字段是否可用于检索/出题/判题”。
3. 未确认结构化字段不得驱动自动判题；可作为搜索关键词和候选摘要。
4. 对高频题型建立模板后，可将人工确认结果反哺模板和抽取规则。
5. 所有修改保留审计记录，避免后续模型重新解析覆盖人工结论。
