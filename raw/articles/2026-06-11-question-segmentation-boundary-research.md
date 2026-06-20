---
title: "试卷 PDF 拆题边界判断调研"
source-type: article
generated: 2026-06-11
generated-by: wiki-research-skill
research-topic: "question segmentation boundary detection for exam PDF/image OCR"
external-research-used: true
status: raw-research
---

# 试卷 PDF 拆题边界判断调研

## 调研问题

本报告聚焦：一张 PDF 或试卷图片中，系统如何判断一道题结束、下一道题开始；如何结合文档版面分析、题号检测、层级结构识别、OCR 文本信号、视觉布局信号、规则、模型和人工复核，处理小题、大题、材料题、组题、跨页题、多栏排版、答案区混排、选项换行和图文跨区域等边界问题。

应用背景是 AI 智能命题系统的题库导入能力：系统需要把教师上传的 PDF / 图片历年试卷、练习册、个人题库自动拆解为单题，同时保留整套卷结构，以支持后续知识点标注、难度标注、组卷和同型题生成。

## 核心结论

1. 拆题边界不能只靠 OCR 文本或题号正则，必须先做版面区域检测、阅读顺序恢复，再在结构化区域流上判断边界；直接全页 OCR 在多栏文档中会把不同栏文本串成错误顺序，MinerU 明确通过先做布局检测再对文本区域 OCR 来避免阅读顺序被破坏。[来源: https://arxiv.org/html/2409.18839] 可信度：高

2. 对数学试卷，题目是一个“结构单元”，边界应覆盖题干、选项、小问、公式、图形和关联图像，而不是只截取连续文字；MathDoc 将数学试卷抽取定义为结构化问题集合，并要求同时进行结构文本抽取、图形抽取和不完整输入拒答。[来源: https://arxiv.org/html/2601.10104] 可信度：高

3. 边界判断应采用多信号融合：题号/小题编号是强文本锚点，版面框、坐标、空白、缩进、外框、分栏、图表位置是强视觉锚点，二者冲突时进入低置信队列；DocLayNet 和 OmniDocBench 都显示版面标注需要 bounding box、阅读顺序、类别标签和人工/专家质检，单一信号不足以覆盖复杂文档。[来源: https://ar5iv.labs.arxiv.org/html/2206.01062] [来源: https://arxiv.org/html/2412.07626v2] 可信度：高

4. 对“下一题开始”比“本题自然结束”更适合作为终止条件。MathDoc 的 OCR 边界对齐提示明确提出：如果找不到第 N 题的语义结尾，优先定位第 N+1 题的开始，第 N 题结束定义为其前一个文本段。[来源: https://arxiv.org/html/2601.10104] 可信度：高

5. 真实场景必须有“不识别/需人工复核”机制。MathDoc 发现当前多模态模型在残缺、遮挡、折页等不完整题目上经常“强行转写”，Qwen3-VL-30B 虽然文本抽取较强，但拒答召回只有 0.14，说明自动拆题系统不能默认模型输出都是可用结果。[来源: https://arxiv.org/html/2601.10104] 可信度：高

6. 对有固定模板的考试卷，可显式维护模板配置和题区粗框，再用图像处理/模型结果校正；Springer 的纸笔测试自动评分系统用 Zoning 配置记录每题位置、题型、答案区域，并结合轮廓检测确认题区，真实测试中正确识别 52,317 / 52,320 个题区。[来源: https://link.springer.com/article/10.1007/s11042-023-15767-2] 可信度：高

7. 人工校验 UI 不应让老师逐像素修图，而应展示“题目卡片 + 原图框选 + 边界置信度 + 可拖拽调整 + 合并/拆分/跨页续接”四类动作；ACCSAMS 的用户研究显示，用户希望看到各子任务预测并修正错误，但逐阶段反复复核会造成疲劳，因此 UI 要聚合复核任务并按置信度排序。[来源: https://arxiv.org/html/2405.19124v1] 可信度：高

## 内容整理

### 1. 问题定义：题目边界是结构单元边界

拆题的目标不是把页面切成若干文字块，而是识别出每道题的完整结构单元。一个题目单元至少可能包含：

- 题号：如 `1.`、`一、`、`第 17 题`、`（1）`、`(2)`、`A.` 等。
- 题干：主干文字、数学公式、空格、填空线、表格内容。
- 选项：选择题的 `A/B/C/D` 选项，可能换行、分栏、带公式。
- 小问：解答题中的 `(1)(2)(3)`，通常属于同一大题，不应拆成独立题，除非业务明确要求。
- 图形：几何图、函数图、统计图、表格、插图，可能在题干前后或页面另一侧。
- 答案/解析/批注：导入教师资料时可能混排，默认不应并入题干，除非作为答案字段单独结构化。
- 跨页续接：题目题干或解答空间跨页时，需要合并为同一道题的多个页面区域。

MathDoc 将数学试卷抽取表示为 `S={q1,q2,...,qN}`，并要求每个问题既有结构文本 `Ti`，又可关联图形 bbox `Bi`，还要判断是否完整可识别。[来源: https://arxiv.org/html/2601.10104]

### 2. 可用信号

#### OCR 文本信号

- 题号模式：阿拉伯数字、中文数字、括号编号、罗马数字、带分值的题号、题型标题。
- 小问编号：`(1)`、`（2）`、`①`、`Ⅰ`、`解：`、`证明：` 等。
- 选项编号：`A.`、`B.`、`C.`、`D.`，但不能把选项误判为新题。
- 大题标题：`一、填空题`、`二、选择题`、`解答题` 等，可作为层级结构节点。
- 分值提示：`（本题 10 分）`、`17.（12分）` 常作为大题边界或题头附属信息。
- 材料提示：`阅读下列材料`、`根据材料回答`、`如图`、`表中` 等提示图文或组题关系。
- 页眉页脚：试卷名、页码、学校名、保密标识，应识别为噪声或卷级元数据。

MathDoc 的文本对齐流程把清洁 GT 题目映射到 noisy predicted text stream，使用 start/end snippet、严格单调顺序、精确匹配、模糊匹配和 fallback 机制定位题目边界；这说明 OCR 文本信号应被用于“锚点定位”，而不是作为唯一切分依据。[来源: https://arxiv.org/html/2601.10104]

#### 视觉布局信号

- bbox 坐标：题号、题干、公式、图形、表格、选项区域的位置。
- 阅读顺序：单栏、多栏、混合栏、跨栏标题的排序。
- 空白间距：题与题之间的垂直间距、横线、分割线、段落缩进。
- 对齐关系：题号与正文左边界、选项成列、图表与对应题干的近邻关系。
- 外框与模板：固定试卷可能有矩形题框、答题框、表格、角标、QR/条码。
- 页面干扰：页眉、页脚、页码、水印、答题线、学生涂写、批改痕迹、折痕和扫描黑边。

DocLayNet 的标注采用 Caption、Formula、List-item、Page-header、Page-footer、Picture、Table、Text、Title 等 11 类 bbox，强调文档布局需要人类可解释的区域对象，而不只是字符流。[来源: https://ar5iv.labs.arxiv.org/html/2206.01062]

OmniDocBench 进一步把布局、阅读顺序、图表/公式/表格识别放在统一评测中，并指出多栏和复杂布局会显著降低阅读顺序准确性。[来源: https://arxiv.org/html/2412.07626v2]

#### 规则信号

- 大题标题开启新组，后续题号归属该组，直到下一个同级标题。
- 同一大题下的 `(1)(2)(3)` 默认归属同一大题；只有当题型是“独立小题集合”或用户配置为“按小问入库”时才拆分。
- 选项编号必须满足同一候选题内至少 2 个连续选项、靠近题干、处于题干之后，才作为选项，不作为新题。
- 题号序列应单调递增；跳号、重复号、回退号触发复核。
- 若第 N 题没有清晰结束，使用第 N+1 题开始位置作为第 N 题下边界。
- 页面底部没有出现下一题且当前题未闭合时，标记为跨页候选。

Springer 纸笔测试系统显示，对于固定格式考试，可以用配置文件保存页尺寸、题目位置、题型、每页题数、选项矩阵维度等，再用图像处理确认实际轮廓。[来源: https://link.springer.com/article/10.1007/s11042-023-15767-2]

#### 模型信号

- 版面检测模型：检测 text、title、table、figure、formula、header、footer、question block 等。
- OCR/公式识别模型：输出文字、数学公式、置信度、字符框。
- 多模态模型：做结构化抽取、图文关联、材料题组判断、低置信解释。
- 检测模型加规则后处理：处理 bbox 包含、重叠、跨栏排序、跨页合并。
- LLM 辅助对齐：在 OCR 噪声下定位 start/end snippet，处理公式畸变和题号缺失。

MinerU 的流程是 PDF 预处理、版面/公式/表格/OCR 解析、bbox 后处理和格式转换；其后处理会处理 bbox 包含、局部重叠、按人类阅读顺序分区排序，并支持跨栏/跨页段落合并。[来源: https://arxiv.org/html/2409.18839]

### 3. 典型题型边界策略

#### 单题

单题的可靠边界通常由“题号开始 + 下一个同级题号开始”确定。正文内部的换行、公式换行、选项换行不应触发切分。若题干包含图形，则图形应按距离、同栏关系、题号区间和语义提示归属到该题。

#### 小题

小题编号通常属于大题内部层级。建议先建立层级树：

- 卷级：试卷标题、年级、科目、时间、总分。
- 大题级：题型标题，如“二、选择题”。
- 题级：独立题号，如 `1.`、`17.`。
- 小问级：`(1)(2)(3)`。
- 选项级：`A/B/C/D`。

默认入库粒度应为“题级”，小问作为题内结构字段。若教师需要按小问组卷，再提供“展开小问为独立题”的人工确认选项。

#### 材料题 / 组题

材料题通常由共同材料和多个子题组成。边界判断应先识别材料块，再识别其下属子题。共同材料不能复制进每道题作为独立题干而丢失组题关系，应保存为 `shared_context`。若单个子题离开材料无法成立，题库中应保留材料组 ID。

EXAMS-V 的数据构建要求每个样本图像包含一道选择题、候选选项及其表格/图/符号等视觉信息，说明考试题常常以“一题一图文快照”的方式组织；但真实 PDF 需要先用 bbox 把共同材料和子题分开。[来源: https://arxiv.org/html/2403.10378v1]

#### 跨页题

跨页题判断应结合页面位置和题号序列：

- 第 N 题在页面底部出现，当前页没有第 N+1 题。
- 下一页开头没有新题号，或者出现“续上页/继续”等提示。
- 下一页开头区域的缩进、字体、公式、图形与上一题保持连续。
- 若下一页开头先出现页眉/页码，再出现正文块，应忽略页眉后合并。

MinerU 提到需要跨栏和跨页段落合并，说明跨页不是异常，而是文档抽取必须处理的常规后处理。[来源: https://arxiv.org/html/2409.18839]

#### 答案区混排

答案、解析、学生作答、批改痕迹不应直接进入题干。建议识别为单独层：

- 纸质原卷导入：忽略手写作答和批改痕迹，保留印刷题干。
- 教师题库导入：若答案/解析是印刷内容，应作为 `answer` / `analysis` 字段。
- 练习册导入：题目与答案同页时，需要先识别“答案区标题”或答案区域布局，再与题干分离。

MathDoc 的严格转写提示明确要求主观题只转写印刷题干，忽略手写内容；客观题只有明确可见手写标记才附加答案标签，不能推断答案。[来源: https://arxiv.org/html/2601.10104]

#### 多栏排版

多栏试卷常见失败是 OCR 把第一栏某题与第二栏某题交错合并。应先按视觉布局分栏，再在每栏内部排序，最后跨栏合并顺序。OmniDocBench 的阅读顺序评测显示复杂布局、多栏布局会显著拉低模型的 reading order 指标；MinerU 也指出全页直接 OCR 可能把不同列识别成一列，导致错误文本顺序。[来源: https://arxiv.org/html/2412.07626v2] [来源: https://arxiv.org/html/2409.18839]

### 4. 常见失败场景与处理策略

| 失败场景 | 风险 | 推荐处理 |
|---|---|---|
| 跨页题 | 前半题和后半题拆成两题，或漏掉下一页图形 | 页面底部开放题 + 下一页无新题号时进入跨页合并候选 |
| 答案区混排 | 把答案/解析混入题干 | 识别答案标题、颜色、位置、手写/印刷属性，单独建字段 |
| 选项换行 | 把选项 `B/C/D` 误判为新题 | 选项必须连续、靠近题干、在同题 bbox 内 |
| 题干材料共用 | 每个子题缺上下文，题库语义不完整 | 建立材料组，保存 `shared_context` 与子题关系 |
| 多栏排版 | 题目顺序错乱，跨栏串题 | 先分栏/分区，再按区域内阅读顺序排序 |
| 图文跨区域 | 图形归错题或漏图 | 用距离、同栏、题号区间、图注/“如图”文本联合归属 |
| 页眉页脚/页码 | 误当题干或题号 | 版面类 `header/footer/page_number` 过滤 |
| 扫描歪斜/阴影/折痕 | 题号、公式、图形缺失 | 图像预处理、低置信拒答、人工复核 |
| 学生涂写/批改痕迹 | 干扰 OCR 和题干完整性 | 印刷文本优先，手写内容默认忽略或单独标记 |
| 无框试卷 | 纯规则难以确定视觉边界 | 题号锚点 + bbox 聚类 + LLM 语义边界联合判断 |

### 5. 置信度设计

建议按题目候选输出 `boundary_confidence`，并拆成几个子分数：

- `numbering_confidence`：题号是否清晰、序列是否连续。
- `layout_confidence`：bbox 是否完整、是否与邻题重叠、阅读顺序是否稳定。
- `ocr_confidence`：文字/公式识别质量、乱码率、缺失率。
- `figure_binding_confidence`：图形是否有明确归属。
- `integrity_confidence`：是否疑似跨页、遮挡、折痕、缺页。
- `rule_consistency_confidence`：是否符合题型模板、选项数量、分值结构。

置信度等级建议：

- 高：题号清晰、bbox 完整、顺序单调、无跨页/遮挡、图文归属明确。
- 中：存在轻微 OCR 噪声、图文位置不典型、选项换行、多栏但顺序可解释。
- 低：题号缺失或跳号、bbox 重叠、跨页候选、材料题归属不清、答案区混排。
- 拒识/人工：关键题干缺失、严重遮挡、折页截断、模型推测补全风险高。

MathDoc 对不完整题设定 `[Unrecognizable]` 类型，并将拒答能力纳入 Precision、Recall、F1 评测，说明拆题系统必须把“无法可靠拆分”作为正常输出，而不是失败异常。[来源: https://arxiv.org/html/2601.10104]

### 6. 对 AI 智能命题系统的落地建议

#### 最小可用版本

1. 上传 PDF / 图片，按页渲染为高分辨率图像。
2. 运行版面检测，识别正文、标题、图形、表格、页眉页脚、页码。
3. 对文本区域做 OCR 和公式识别，保留字符框与行框。
4. 用题号规则生成候选题头，按同级题号切分初始题区。
5. 用视觉 bbox 扩展题区，吸附公式、图形、表格、选项。
6. 用规则校验题号序列、选项数量、小问归属、跨页候选。
7. 对低置信题进入人工校验 UI。
8. 教师确认后再入库，并保存原图框、OCR 文本、题目结构和置信度。

#### 推荐数据结构

```json
{
  "paper_id": "paper_001",
  "question_id": "q_017",
  "parent_group_id": "group_material_003",
  "question_number": "17",
  "question_type": "solve",
  "page_spans": [
    {"page": 3, "bbox": [120, 420, 880, 1140]},
    {"page": 4, "bbox": [110, 80, 870, 360]}
  ],
  "stem_markdown": "...",
  "sub_questions": [
    {"label": "(1)", "text": "..."},
    {"label": "(2)", "text": "..."}
  ],
  "options": [],
  "figures": [
    {"bbox": [620, 540, 850, 760], "page": 3, "role": "geometry_figure"}
  ],
  "answer": "",
  "analysis": "",
  "boundary_confidence": 0.82,
  "review_status": "needs_review",
  "risk_flags": ["cross_page_candidate", "figure_binding_low"]
}
```

#### 人工校验 UI

必须让教师快速修正边界，而不是重新录题：

- 左侧显示原卷页面，题区用彩色框标注。
- 右侧显示题目卡片，含题号、题型、OCR 文本、图形预览、置信度。
- 支持“拆分、合并、调整框、标记跨页续接、绑定图形、移除答案区、改题号、改题型”。
- 低置信题优先排队，高置信题批量确认。
- 修改后保存训练样本，用于后续规则或模型迭代。

ACCSAMS 用户研究指出，用户希望能查看并修正布局分割、题/解答归属、层级和替代文本等子任务预测，但逐阶段反复校验会增加认知负担，因此校验 UI 应集中呈现关键问题并减少重复复核。[来源: https://arxiv.org/html/2405.19124v1]

#### 可接受错误率建议

暂无发现 K12 试卷拆题边界的行业统一错误率标准。结合题库入库风险，建议内部验收阈值如下，需由项目方确认：

- 自动拆题召回率：高优先级，目标 ≥ 98%，漏题比多切题更严重。
- 高置信题边界准确率：目标 ≥ 95%，允许人工抽检。
- 全量题边界准确率：上线初期目标 ≥ 90%，低置信题必须进入复核。
- 图形归属准确率：目标 ≥ 95%，几何/函数题低于阈值不得自动入库。
- 跨页题自动识别：目标 ≥ 90%，未达标时统一人工确认跨页候选。
- 低置信拦截率：宁可多拦截，不允许残缺题高置信入库。

这些数字是结合题库入库风险给出的产品建议，未找到直接行业标准来源，入库前应标注为“项目验收假设，待用户确认”。

## 推荐工作流

### 阶段 1：页面级预处理

1. PDF 渲染成页面图像，保留页号、DPI、原始尺寸。
2. 扫描件做去黑边、纠偏、去噪、二值化可选增强。
3. 判断 born-digital PDF 与 scanned PDF：有可靠文本层时可直接抽取文本，但仍需布局检测；扫描件必须走 OCR。

MinerU 使用 PDF metadata 判断可解析文本和扫描 PDF，并对扫描 PDF 启用 OCR，这个分流适合工程实现。[来源: https://arxiv.org/html/2409.18839]

### 阶段 2：版面区域检测

1. 检测标题、正文、列表项、公式、图形、表格、页眉、页脚、页码。
2. 对考试场景额外训练/标注：question-block、answer-area、solution-heading、shared-material、choice-option、sub-question。
3. 输出 bbox、类别、置信度和阅读顺序候选。

DocLayNet 的人工标注经验说明，复杂布局会有多种合理标法，必须制定清晰标注指南，例如 list-item 独立对象、caption 必须对应图片/表格等。[来源: https://ar5iv.labs.arxiv.org/html/2206.01062]

### 阶段 3：OCR 与结构锚点识别

1. 对每个文本 bbox 独立 OCR，保留行框、字符框、识别置信度。
2. 识别题号、小题号、选项号、大题标题、分值、答案标题。
3. 建立题号序列和层级树，输出候选题头。

### 阶段 4：候选题区生成

1. 根据同级题号确定初始边界：第 N 题开始至第 N+1 题开始之前。
2. 吸附区域内的文本、公式、图表、选项。
3. 若没有下一个题号，以页面底部或跨页候选作为临时结束。
4. 对跨栏文档先按栏内排序，再合成全页阅读顺序。

MathDoc 的提示把“找下一题开始”作为无法找到题目结尾时的终止策略，适合作为候选题区生成的核心规则。[来源: https://arxiv.org/html/2601.10104]

### 阶段 5：校验与置信度计算

1. 校验题号连续性、选项数量、分值结构、小问层级。
2. 校验 bbox 是否重叠、跨页、图文是否归属明确。
3. 对低置信题输出风险标签和复核原因。
4. 严重残缺、遮挡、折页、缺页时输出拒识，不自动入库。

### 阶段 6：人工复核与入库

1. 高置信题批量确认。
2. 中低置信题进入复核队列。
3. 教师修正边界、合并/拆分、绑定图形、处理跨页。
4. 保存最终题目结构和原图裁剪证据。
5. 入库前再进行题干完整性、公式渲染、知识点和难度标注。

## 适用场景

- 教师上传 PDF、图片、扫描试卷，目标是建立可复用题库。
- 历年真题、模拟卷、练习册、教师自编题需要拆成单题。
- 数学题含公式、图形、表格、选项和小问，需要保留结构。
- 题库入库前允许人工复核，系统目标是节省录入时间而不是完全无人值守。
- 学校有相对稳定的试卷模板或题型结构，可沉淀模板规则。

## 不适用场景

- 只需要整套卷归档，不需要单题级检索或组卷。
- 上传图片质量极差、严重遮挡、拍摄倾斜，且不愿人工复核。
- 需要自动判分主观数学证明过程，当前资料只支持边界和结构抽取，不能证明手写解答语义识别已可靠。
- 题目与答案、解析、讲义正文高度混排且没有明确版面规律，前期需要人工标注样本后再自动化。
- 要求 100% 自动无误入库。现有研究反复显示复杂版面和噪声场景仍需要人工质检或拒识机制。[来源: https://arxiv.org/html/2601.10104] [来源: https://arxiv.org/html/2412.07626v2]

## 风险与约束

- 模型强行补全风险：MathDoc 显示多模态模型在不完整题目上常常不主动拒答，而是推测补全。[来源: https://arxiv.org/html/2601.10104]
- 多栏顺序风险：OmniDocBench 和 MinerU 都指出复杂/多栏布局会影响阅读顺序，全页 OCR 不可靠。[来源: https://arxiv.org/html/2412.07626v2] [来源: https://arxiv.org/html/2409.18839]
- 图文绑定风险：数学题的图形可能不在题干紧邻位置，若只按距离归属会误绑。
- 版面标注歧义：DocLayNet 发现复杂布局可能有多个合理标注，必须用标注规范统一边界口径。[来源: https://ar5iv.labs.arxiv.org/html/2206.01062]
- 模板迁移风险：固定模板规则在另一种试卷上可能失效；Springer 方案依赖每套测试配置文件，泛化到非模板卷需补充模型和人工复核。[来源: https://link.springer.com/article/10.1007/s11042-023-15767-2]
- 评测指标风险：页面级编辑距离可能掩盖关键字段错误，RealDocBench 主张按字段/问题严格评分，拆题也应按题级完整性评分。[来源: https://arxiv.org/html/2606.07401v1]
- 可接受错误率未验证：本报告给出的错误率阈值是产品建议，未找到行业统一标准，需用户确认。

## 信源质量门控记录

### 门控规则

- Tavily score < 0.4 的网页默认剔除，除非与主题高度相关且可二次精读。
- 学术论文、开放论文 HTML、同行评审论文、官方开源项目优先保留。
- 无法访问全文的来源只作候选线索，不作为高置信核心结论唯一依据。
- 直接关于数学试卷、考试文档、文档版面检测、阅读顺序、真实考试处理的来源优先。
- C/D 级来源不得作为唯一结论依据。
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`。

### 保留信源

1. [MathDoc: Benchmarking Structured Extraction and Active Refusal on Noisy Mathematics Exam Papers](https://arxiv.org/html/2601.10104)
   - 工具：Exa + 二次 WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：直接面向真实数学试卷结构化抽取，覆盖题目单元、图形、拒识、边界对齐。
   - 后续处理：进入核心结论和逐来源总结。

2. [MinerU: An Open-Source Solution for Precise Document Content Extraction](https://arxiv.org/html/2409.18839)
   - 工具：Exa + 二次 WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：提供文档解析工程流程、布局检测、OCR 分区、阅读顺序、跨栏/跨页后处理。
   - 后续处理：进入核心结论和推荐工作流。

3. [OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations](https://arxiv.org/html/2412.07626v2)
   - 工具：Exa + 二次 WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：评测多种 PDF 类型、布局类别、阅读顺序、多栏复杂布局和 exam paper。
   - 后续处理：进入风险、评测指标和失败场景。

4. [DocLayNet: A Large Human-Annotated Dataset for Document-Layout Analysis](https://ar5iv.labs.arxiv.org/html/2206.01062)
   - 工具：Exa + 二次 WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：提供文档布局 bbox 类别、人工标注规范、复杂布局歧义和模型上限。
   - 后续处理：进入版面标注和人工标注规范。

5. [Automated assessment of pen and paper tests using computer vision](https://link.springer.com/article/10.1007/s11042-023-15767-2)
   - 工具：Exa + 二次 WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：真实纸笔数学测试系统，包含题区检测、模板配置、跨页题、人工复核和量化结果。
   - 后续处理：进入固定模板策略与可落地建议。

6. [ACCSAMS: Automatic Conversion of Exam Documents to Accessible Learning Material](https://arxiv.org/html/2405.19124v1)
   - 工具：Exa + 二次 WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：专门处理 exam documents，包含布局分割、层级抽取、题/解答识别、校验 UI。
   - 后续处理：进入人工复核 UI 和层级识别建议。

7. [RealDocBench: A Benchmark for Field-Level QA and Layout Understanding](https://arxiv.org/html/2606.07401v1)
   - 工具：Exa + 二次 WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：强调真实文档不能只用页面相似度，要按字段/问题严格评分；布局轨道有 adjacency-aware matcher。
   - 后续处理：进入验收指标和边界评分设计。

8. [EXAMS-V](https://arxiv.org/html/2403.10378v1)
   - 工具：Exa + 二次 WebFetch
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：真实考试题截图数据集，说明题目通常要包含文本、选项、图表、符号等完整快照。
   - 后续处理：作为题目图文完整性证据。

9. [A Hybrid Approach for Document Layout Analysis in Document Images](https://arxiv.org/html/2404.17888v2)
   - 工具：Tavily 候选补充 + 二次 WebFetch
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：提供现代版面检测方法、DocLayNet 评测和小对象检测改进。
   - 后续处理：作为模型路线背景。

10. [MathNet: a global multimodal benchmark for mathematical reasoning and retrieval](https://arxiv.org/html/2604.18584)
   - 工具：Exa + 二次 WebFetch
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：包含官方数学竞赛 PDF 的问题分割、问题/解答抽取和多阶段验证流程。
   - 后续处理：作为大规模数学题抽取与验证流程参考。

11. [HURIDOCS pdf-document-layout-analysis](https://github.com/huridocs/pdf-document-layout-analysis)
   - 工具：Tavily 候选补充 + 二次 WebFetch
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：开源服务可对 PDF 页面做分割和分类，识别 text、title、picture、table 等元素。
   - 后续处理：仅作为工程工具候选。

12. [A segmentation method for examination paper questions](https://dl.acm.org/doi/fullHtml/10.1145/3650400.3650461)
   - 工具：Exa 候选，WebFetch 超时，WebSearch 摘要补充
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：题名直接相关，搜索摘要显示其用 Otsu、自适应阈值、Sobel、形态学和相邻题区边缘分析做试卷题目分割。
   - 后续处理：未成功全文精读，只作为待验证方法线索，不作为高置信核心结论唯一依据。

### 剔除信源

1. LlamaIndex glossary 多栏/版面分析页面
   - 剔除原因：Tavily 分数低于 0.4，且为泛化 SEO/术语页。

2. Twig 多栏 chunking 帮助页
   - 剔除原因：Tavily 分数低于 0.4，偏 RAG chunking，非试卷拆题。

3. QuestPDF 多栏布局 API
   - 剔除原因：Tavily 分数低于 0.4，偏 PDF 生成 API，不是 OCR 拆题。

4. PMC / Nature printed document layout OCR 页面
   - 剔除原因：二次访问返回浏览器校验页面，未获得可用全文。

5. 低分 Nature、CNET、Financial Times 等无关新闻结果
   - 剔除原因：主题弱相关或完全无关。

## 来源与可信度

| 来源 | 类型 | 可信度 | 支撑内容 |
|---|---|---|---|
| https://arxiv.org/html/2601.10104 | 学术论文 | 高 | 数学试卷结构化抽取、题目边界对齐、拒识机制、噪声场景 |
| https://arxiv.org/html/2409.18839 | 学术论文/开源工具论文 | 高 | PDF 解析流程、布局检测、公式检测、OCR 分区、阅读顺序 |
| https://arxiv.org/html/2412.07626v2 | 学术 benchmark | 高 | 多类型 PDF 评测、exam paper、复杂/多栏布局、阅读顺序指标 |
| https://ar5iv.labs.arxiv.org/html/2206.01062 | 学术 dataset | 高 | 版面 bbox 类别、人工标注、标注歧义和跨域泛化 |
| https://link.springer.com/article/10.1007/s11042-023-15767-2 | 同行评审开放论文 | 高 | 纸笔考试题区/答案区检测、模板配置、真实测试结果 |
| https://arxiv.org/html/2405.19124v1 | 学术论文 | 高 | exam document 布局分割、层级、题/解答识别、用户复核 UI |
| https://arxiv.org/html/2606.07401v1 | 学术/benchmark | 高 | 字段级 QA、布局 bbox、严格 per-question 指标、邻接合并评分 |
| https://arxiv.org/html/2403.10378v1 | 学术 benchmark | 中 | 真实考试题截图、图表符号、单题快照与质量检查 |
| https://arxiv.org/html/2404.17888v2 | 学术论文 | 中 | 现代 DLA 模型、小对象检测、DocLayNet 结果 |
| https://arxiv.org/html/2604.18584 | 学术 benchmark | 中 | 数学问题 PDF 抽取、问题分割、问题/答案对齐、多阶段验证 |
| https://github.com/huridocs/pdf-document-layout-analysis | 开源项目 | 中 | PDF layout analysis 工具候选 |
| https://dl.acm.org/doi/fullHtml/10.1145/3650400.3650461 | 学术论文候选 | 低到中 | 直接题目分割方法线索，未全文精读 |

## 对于可信度较高的来源逐来源总结

### MathDoc

MathDoc 是本次最直接来源。它指出纸质数学试卷结构化抽取是智能教育和题库建设的基础，但真实场景存在手写解答/批改痕迹、灵活图文布局、遮挡、折痕和题目不完整等挑战。它把任务定义为从整页试卷图像中抽取问题集合，并要求结构文本、图形 bbox 和主动拒识同时处理。[来源: https://arxiv.org/html/2601.10104]

对拆题边界最有价值的是它的文本匹配和边界定位流程：给定 GT 问题集合和模型输出文本流，先由 LLM 找每题的 start/end snippet，再用精确匹配、8-15 字符滑窗的 Levenshtein 相似度和 fallback 规则定位字符索引。它还要求严格单调顺序，避免题目边界重叠或回退。[来源: https://arxiv.org/html/2601.10104]

MathDoc 的提示工程尤其适合落地：找不到本题结尾时，不强行寻找语义结束，而是定位下一题开始；若题目因折页、污渍、遮挡导致关键内容缺失，应输出 `[Unrecognizable]`，不得猜测补全。[来源: https://arxiv.org/html/2601.10104]

局限：它是 benchmark 和评测流程，不是完整生产系统；模型与数据时间较新，实际项目需要用本地试卷样本复测。

适合入库知识点：数学试卷结构化抽取、OCR 边界对齐、题目拒识机制、题目完整性评测。

### MinerU

MinerU 给出可工程化的文档解析 pipeline：PDF 预处理判断文本层/扫描件，布局检测和公式检测，分别调用 OCR/公式/表格识别，再做 bbox 关系和阅读顺序后处理，最后输出 Markdown/JSON。[来源: https://arxiv.org/html/2409.18839]

它明确指出全页 OCR 会在多栏文档中导致错误阅读顺序，因此应先布局分析，再对文本区域 OCR。它还提出通过 bbox 包含关系、局部重叠处理、按“从上到下、从左到右”的人类阅读顺序分区排序来重建内容。[来源: https://arxiv.org/html/2409.18839]

对 AI 命题系统而言，MinerU 适合作为“底层 PDF 解析层”的参考，但它不是试卷题目边界识别专用系统，还需要在其输出的 region / span / reading order 之上加题号层级和题目结构规则。

局限：论文中的模型和训练集虽含 exam paper 类别，但不保证对本地 K12 数学试卷、中文教材、扫描质量和教师手写资料直接达标。

适合入库知识点：PDF 解析分层架构、版面检测优先于 OCR、bbox 后处理、跨栏跨页排序。

### OmniDocBench

OmniDocBench 提供多类型 PDF 文档解析 benchmark，覆盖学术论文、教材、手写笔记、报纸、exam paper 等 9 类页面，并包含布局、文本、公式、表格和阅读顺序等细粒度评估。[来源: https://arxiv.org/html/2412.07626v2]

它显示多栏和复杂布局会明显降低阅读顺序表现，且不同工具在不同文档类型、视觉退化、语言和表格/公式场景下表现差异明显。[来源: https://arxiv.org/html/2412.07626v2]

对拆题边界的启发是：不要只用一个总分评估 OCR；应分别评估题号识别、阅读顺序、公式完整性、图表归属、题级边界准确率，并对多栏、复杂布局和模糊扫描单独统计。

局限：它是通用 PDF 解析 benchmark，不直接定义 K12 试卷题目边界规则。

适合入库知识点：PDF 解析评测、多栏阅读顺序风险、exam paper 属性评估。

### DocLayNet

DocLayNet 提供 80,863 页人类标注的文档版面数据，使用 COCO bbox 格式和 11 类标签，强调文档布局高度多样，科学论文模板数据训练出的模型在其他复杂文档上泛化下降。[来源: https://ar5iv.labs.arxiv.org/html/2206.01062]

它的关键价值在于标注规范。复杂版面可能有多个看似合理的标注方式，例如图形是否整体标注、列表是否逐项标注。DocLayNet 通过 100 页以上指南、训练考试和持续质控来降低标注不一致。[来源: https://ar5iv.labs.arxiv.org/html/2206.01062]

对试卷拆题而言，必须提前制定标注口径：大题、小题、选项、图形、材料、答案区、页眉页脚如何标；否则训练数据和人工复核会不一致，导致模型边界漂移。

局限：DocLayNet 没有专门的 question-block 类别，也不包含手写/拍照试卷。

适合入库知识点：文档版面标注规范、bbox 类别设计、标注一致性、复杂布局歧义。

### Automated assessment of pen and paper tests using computer vision

该论文是固定模板纸笔考试自动评分系统。系统分为 Zoning、Scanning、Processing、Verification 四模块。Zoning 阶段由人工在原始 PDF 模板中标记 QR/条码、题目位置和选择题答案区，并生成配置 JSON；Processing 阶段在扫描图上用灰度、Gaussian blur、Otsu 阈值、形态学操作、轮廓检测识别边框、题区和答案区，再用模板配置验证。[来源: https://link.springer.com/article/10.1007/s11042-023-15767-2]

该系统支持题目跨一页或多页，每个拆分部分由矩形识别；它也把开放题送人工评分，把选择题答案格自动识别。[来源: https://link.springer.com/article/10.1007/s11042-023-15767-2]

量化结果显示，在 2,180 份数学模板测试、52,320 个问题上，系统正确识别 52,317 个问题，仅有一份测试因扫描导致垂直线连接两个题目轮廓而识别失败。[来源: https://link.springer.com/article/10.1007/s11042-023-15767-2]

对 AI 命题系统的启发：若学校有固定小卷模板或期末卷模板，配置驱动比纯 AI 更稳；可先让教师上传空白模板并粗标题区，后续同模板导入走自动化。

局限：它依赖规则化模板和矩形框，不适用于任意练习册/非结构化 PDF 的完全自动拆题。

适合入库知识点：模板化题区识别、Zoning 配置、纸笔考试图像处理、人工验证模块。

### ACCSAMS

ACCSAMS 目标是把考试文档转成适合视障学生使用的 Markdown/Word。它的流程包括每页 layout segmentation、确定阅读顺序和层级、识别解答内容、给图表添加 alt-text，并通过 Web GUI 让用户验证和修正。[来源: https://arxiv.org/html/2405.19124v1]

它使用 YOLOv8 先在 DocLayNet 上预训练，再在自有 exam dataset 上微调；自有数据包含 1,293 德语和 900 英语考试文档，标注 1,917 页，检测类别包括 headings、paragraphs、list symbols、figures、formulas、tables，整体 mAP50 为 0.922。[来源: https://arxiv.org/html/2405.19124v1]

它的层级抽取用两个启发式：按页码、垂直和水平坐标排序；根据枚举样式、标题层级等文本特征分类 list items 和 headings，形成文档树。[来源: https://arxiv.org/html/2405.19124v1]

用户研究显示，用户认为系统有改进价值，但希望看到各子任务预测并能修正，且反复校验会造成疲劳。[来源: https://arxiv.org/html/2405.19124v1]

对 AI 命题系统的启发：人工校验 UI 要围绕题目结构树和低置信错误集中呈现，而不是让老师逐阶段重复看完整试卷。

局限：它不专门处理 K12 数学单题入库，也没有专门的题号/选项/小问 schema。

适合入库知识点：考试文档层级抽取、半自动复核 UI、题/解答识别、可访问格式转换。

### RealDocBench

RealDocBench 强调真实文档解析不能只看完整页面相似度，而应评估下游系统真正查询的字段值；它提供 QA track 和 layout track，layout track 用九类 bbox，并用 IoU >= 0.5 的 Hungarian matcher 加邻接恢复来处理 split/merge 的边界差异。[来源: https://arxiv.org/html/2606.07401v1]

这对拆题边界的启发是：题目边界评估不应只用裁剪框 IoU，也要看题干、选项、图形、公式、答案字段是否完整绑定。两个边界框略有差异但包含同一题语义，可能不影响题库；但漏掉图形或把下一题选项并入，则是严重错误。

局限：领域是受监管文档，不是教育试卷。

适合入库知识点：字段级评测、题级严格准确率、邻接 split/merge 评分。

## 跨源矛盾检测结论

### 检测范围

- 已精读可访问来源数量：10 个以上。
- 检测对象：核心数字、日期、功能描述、因果判断、市场/公司事实。
- 检测时间：2026-06-11。

### 检测结果

结论：未检测到会影响本报告核心建议的跨源矛盾。不同来源之间主要是适用对象和评价粒度不同：

- MathDoc 偏“数学试卷结构化抽取与拒识”。
- MinerU / OmniDocBench / DocLayNet 偏“通用文档版面解析与评测”。
- Springer 纸笔考试系统偏“固定模板和规则化图像处理”。
- ACCSAMS 偏“考试文档可访问转换和人机协同复核”。
- RealDocBench 偏“真实文档字段级评测和布局评分”。

### 数字一致性检查

- MathDoc 报告 3,609 个真实高中数学问题；该数字只用于说明其数据规模。[来源: https://arxiv.org/html/2601.10104]
- MinerU 的评测和版本信息来自论文，未与其他来源冲突。[来源: https://arxiv.org/html/2409.18839]
- OmniDocBench 报告 981 页、9 类 PDF 页面、超过 100,000 个标注；与 DocLayNet 的 80,863 页不是同一数据集，规模不同不构成矛盾。[来源: https://arxiv.org/html/2412.07626v2] [来源: https://ar5iv.labs.arxiv.org/html/2206.01062]
- Springer 系统报告 52,317 / 52,320 题区识别成功，该结果来自固定模板测试，不能外推到任意试卷。[来源: https://link.springer.com/article/10.1007/s11042-023-15767-2]

### 功能描述一致性检查

- 多个来源一致支持“布局分析先于或配合 OCR”：MinerU 显式采用布局检测后 OCR，DocLayNet/OmniDocBench 提供 bbox 级布局标注，ACCSAMS 用布局分割作为第一步。[来源: https://arxiv.org/html/2409.18839] [来源: https://ar5iv.labs.arxiv.org/html/2206.01062] [来源: https://arxiv.org/html/2412.07626v2] [来源: https://arxiv.org/html/2405.19124v1]
- 来源之间对 pipeline 与 end-to-end VLM 的优劣没有完全一致的结论，但差异来自数据集和任务不同。MathDoc 认为 end-to-end MLLM 在部分抽取上强，但拒识弱；OmniDocBench 认为 pipeline 工具在标准文档上强，VLM 在部分退化/非常规场景泛化更好。[来源: https://arxiv.org/html/2601.10104] [来源: https://arxiv.org/html/2412.07626v2]

## 矛盾与待验证问题

1. K12 中文数学试卷“题目边界准确率”的行业标准未找到。报告中的 95%/98% 等阈值是产品验收建议，需用户确认。
2. ACM 论文《A segmentation method for examination paper questions》网页未能全文精读，搜索摘要显示方法高度相关，但不得作为高置信唯一依据。[来源: https://dl.acm.org/doi/fullHtml/10.1145/3650400.3650461]
3. 现有来源大多是英文或国际数据集，中文 K12 数学试卷、北师大版小学教材题、辽宁中考/区模拟卷的版面模式需要本地样本验证。
4. 是否按“小问”独立入库不是技术事实，而是产品口径。建议默认题级入库，小问作为结构字段，需学校老师确认。
5. 答案/解析是否随题入库需要区分“教师题库资料”和“学生作答扫描件”。前者可作为答案字段，后者默认忽略手写作答。
6. 题目边界 UI 的教师可接受复核成本需要用户测试，ACCSAMS 的用户研究说明反复复核会造成疲劳，但没有给出 K12 教师场景的最佳交互标准。[来源: https://arxiv.org/html/2405.19124v1]

## 原始证据摘录

> “The automated extraction of structured questions from paper-based mathematics exams is fundamental to intelligent education, yet remains challenging in real-world settings due to severe visual noise.” [来源: https://arxiv.org/html/2601.10104]

> “This task requires the model to simultaneously perform three sub-tasks: structured text extraction, figure extraction, and intelligent rejection.” [来源: https://arxiv.org/html/2601.10104]

> “Physical Truncation: The problem is located at the edge of image, causing semantic interruption.” [来源: https://arxiv.org/html/2601.10104]

> “If the end can not be found, try to locate the start of Question N+1. The end of Question N is defined as the text segment immediately preceding it.” [来源: https://arxiv.org/html/2601.10104]

> “Direct OCR on the entire page can sometimes result in text from different columns being recognized as a single column, which leads to incorrect text order.” [来源: https://arxiv.org/html/2409.18839]

> “The layout detection model trained on diverse layout detection data performs well on documents such as textbooks.” [来源: https://arxiv.org/html/2409.18839]

> “OmniDocBench supports flexible, multi-dimensional evaluation... task-specific and attribute-based analysis across 9 document types.” [来源: https://arxiv.org/html/2412.07626v2]

> “Across all models, we observe a clear drop in accuracy on multi-column and complex layouts.” [来源: https://arxiv.org/html/2412.07626v2]

> “DocLayNet ... contains 80863 manually annotated pages from diverse data sources ... labelled bounding-boxes with 11 distinct classes.” [来源: https://ar5iv.labs.arxiv.org/html/2206.01062]

> “All regions of interest are placed within four borders on the paper... Questions are designated by the outermost rectangles within regions of interest.” [来源: https://link.springer.com/article/10.1007/s11042-023-15767-2]

> “The system managed to correctly identify 52,317 (out of 52,320) questions on 2180 tests.” [来源: https://link.springer.com/article/10.1007/s11042-023-15767-2]

> “The system is based on 3 steps: (1) segmenting the layout of every page... (2) determining the reading order and hierarchy... (3) generating alt-texts...” [来源: https://arxiv.org/html/2405.19124v1]

> “Predictions are matched to ground-truth boxes by a Hungarian one-to-one assignment... a second pass attempts adjacency recovery.” [来源: https://arxiv.org/html/2606.07401v1]

## 对 AI 智能命题系统的建议清单

1. Phase 1 不建议追求完全自动拆题，应实现“自动拆题 + 置信度 + 教师确认”。
2. 先支持固定模板和常见小学/初中数学卷型，再覆盖任意练习册。
3. 先按“题级”入库，小问、选项、图形、材料作为结构字段。
4. 上传整卷时同时保存卷级结构，避免只剩散题后无法还原试卷。
5. 对跨页、图形归属、材料题、答案混排全部打风险标签。
6. 高置信题允许批量确认，低置信题必须人工校验。
7. 每次教师修正边界都保存为训练样本，逐步形成学校本地版面数据。
8. 验收指标按题级完整性设计：漏题、错并题、错拆题、漏图、错绑图、答案混入题干分别统计。

