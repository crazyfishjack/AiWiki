---
title: "数学公式 OCR 识别准确率调研"
source-type: article
generated: 2026-06-11
generated-by: wiki-research-skill
research-scope: "数学公式 OCR / MER / HMER / PDF formula extraction accuracy"
---

# 数学公式 OCR 识别准确率调研

## 调研问题

围绕 AI 智能命题系统中“数学公式 OCR / 数学表达式识别”的可落地能力进行调研，重点覆盖：

- 数学题中公式 OCR / 数学表达式识别的实际准确率、评测指标和行业可达水平。
- 印刷体、手写体、扫描 PDF、拍照图片、LaTeX / MathML 输出等场景差异。
- 几何图形中公式、角标、上下标、根号、分式、矩阵等常见失败类型。
- 普通 OCR 与公式专用 OCR / VLM / multimodal pipeline 的能力边界。
- 对 AI 智能命题系统的准确率预期、人工复核阈值、低置信度回退策略建议。

---

## 核心结论

1. **“普通 OCR 准确率”不能代表数学公式 OCR 准确率；数学公式应按公式级完全匹配、编辑距离、BLEU/CDM、结构保真和语义等价共同评估。可信度：高。** 公式具有二维结构、上下标、分式、矩阵和多种等价 LaTeX 写法，文本级 BLEU/Edit Distance/ExpRate 会把视觉等价但 LaTeX 写法不同的公式误判为错误，也可能对语义错误给出偏高分数。[来源: https://arxiv.org/html/2409.03643][来源: https://arxiv.org/html/2512.09874v1]

2. **印刷体、干净裁剪的单公式图片是当前最成熟场景，可把“编辑相似度/视觉字符匹配”预期放在 90% 以上，但“公式级完全正确率”仍显著低于字符级或编辑分。可信度：高。** MathNet 在 im2latexv2 上达到 Edit 97.2%、BLEU-4 96.8%、Exact Match 83.9%；PaddleX 官方模型 PP-FormulaNet_plus-L 给出 En-BLEU 92.22%、Zh-BLEU 90.64%。[来源: https://arxiv.org/html/2404.13667][来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html]

3. **真实 PDF / 扫描 PDF / 屏幕截图明显比合成或单公式测试难，扫描噪声、分辨率、布局和跨行公式会把完全正确率拉低。可信度：高。** MathNet 在真实 arXiv 公式 realFormula 上 Edit 88.3%，多行公式只有 71.2% Edit；在 600 DPI 扫描公式 InftyMDB-1 上 Edit 89.2%、Exact Match 35.4%。[来源: https://arxiv.org/html/2404.13667]

4. **手写数学表达式已能达到可用水平，但必须区分“单行孤立公式”和“学生多行解题过程”。可信度：高。** Uni-MuMER 在 CROHME 平均 ExpRate 79.74%、ExpRate@CDM 82.86%，HME100K ExpRate 71.93%、ExpRate@CDM 73.67%；但多行学生解题场景中，VLM 会把学生错误“纠正”为正确答案，过度纠错在不同模型上出现于 42.1% 到 66.2% 测试样例。[来源: https://arxiv.org/html/2505.23566v2][来源: https://arxiv.org/html/2604.22774v1]

5. **VLM / 多模态模型适合作为文档级解析和低置信度复核组件，但不能单独替代公式专用 OCR。可信度：高。** PDF 公式抽取基准中 Qwen3-VL、Gemini 3 Pro、PaddleOCR-VL、Mathpix 得分均超过 9.6/10，但论文同时指出即使高分解析器也会偶发严重公式错误；CDM 论文也观察到 GPT-4o 文档级预测会出现公式幻觉、分隔符缺失和渲染失败。[来源: https://arxiv.org/html/2512.09874v1][来源: https://arxiv.org/html/2409.03643]

6. **最常见失败类型集中在结构而非普通字符：数组/矩阵、上下标、花括号、相似符号、数学字体、多行切分、公式检测边界和 LaTeX 渲染语法。可信度：高。** MathNet 错误分析显示 array 结构只占 im2latexv2 公式的 4.8%，却贡献 52.6% 预测错误；常见纠错 token 包括 `{`、`}`、`^`、`_`，以及 `a`/`\alpha`、`\nu`/`v`、`\phi`/`\varphi` 等视觉相似符号。[来源: https://arxiv.org/html/2404.13667]

7. **AI 智能命题系统不应把公式 OCR 结果直接入题库或用于自动判分；推荐采用“专用公式 OCR + 渲染回检 + SymPy/规则校验 + 低置信度人工复核”的流水线。可信度：高。** 公式 OCR 输出的是 LaTeX/MathML 等结构化表示，后续必须校验能否渲染、是否语义等价、是否符合题目知识点与答案约束；教育场景还要防止 VLM 对学生手写步骤进行“过度纠错”。[来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html][来源: https://arxiv.org/html/2604.22774v1]

---

## 内容整理

### 1. 任务定义：数学公式 OCR 与普通 OCR 的差异

数学表达式识别通常称为 Mathematical Expression Recognition（MER）或 Handwritten Mathematical Expression Recognition（HMER）。它的目标不是把图片里的字符线性读出来，而是把图像中的公式转换为 LaTeX、MathML、Markdown 公式或其他机器可读结构。[来源: https://arxiv.org/html/2404.15254v1][来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html]

普通 OCR 面向线性文本；公式 OCR 必须处理二维空间关系，包括上标、下标、分式、根号、矩阵、积分上下限、多行对齐、数学字体、括号配对和符号语义。UniMERNet 论文明确指出，MER 相比普通 OCR 需要理解复杂结构，例如 superscripts、subscripts 和特殊符号。[来源: https://arxiv.org/html/2404.15254v1]

文档级解析还要先做公式检测（从正文、表格、图形中定位公式区域），再做公式识别。TextIn 的 MEDR 文章把公式识别拆为 Detection 与 Recognition 两步：先定位公式区域，区分文本、表格与公式，再把图像或手写公式转换成 LaTeX/MathML 等结构化表示。[来源: https://www.textin.com/news/20250428161814596]

### 2. 评测指标：不能只看“识别率”

常见指标及适用边界如下：

| 指标 | 含义 | 优点 | 局限 |
| --- | --- | --- | --- |
| Token/字符准确率 | 单个 token 或字符是否正确 | 易解释，适合训练监控 | 对公式结构和语义不敏感 |
| Edit / Levenshtein | 预测串转为真值串所需编辑量，常归一化为 Edit Score | 能反映人工修正工作量 | LaTeX 等价写法会被罚，语义错误可能被低估 |
| BLEU-4 | n-gram 相似度 | 常用于 image-to-LaTeX 论文对比 | 对短公式、边界 token、LaTeX 变体不稳 |
| ExpRate / Exact Match | 整个公式完全匹配比例 | 严格，适合题库入库门槛 | 对等价 LaTeX 表达过严 |
| CDM / ExpRate@CDM | 先渲染公式，再按字符检测匹配空间位置 | 更贴近视觉正确性，可缓解 LaTeX 非唯一性 | 依赖可渲染 LaTeX；对 Unicode、数学字体和语义差异仍有限 |
| LLM-as-a-judge / PINK | 语义、完整性、教育保真综合评分 | 更接近人类对“是否保留数学含义”的判断 | 需模型评审，成本、稳定性和可审计性需控制 |

CDM 论文指出，ExpRate、BLEU、Edit Distance 会因 LaTeX 表达多样性而不可靠。例如视觉上相同的公式可能因为括号、命令别名或上下标顺序不同而被低估；相反，语义错误但文本形式相近的输出也可能得分偏高。[来源: https://arxiv.org/html/2409.03643]

PDF 公式抽取基准进一步验证了这一点：在 250 个公式对、30 名评估者、750 个评分的人类验证中，LLM-as-a-judge 与人类评分 Pearson 相关达到 0.78，CDM 为 0.34，文本相似度约为 0。[来源: https://arxiv.org/html/2512.09874v1]

### 3. 场景差异与可达水平

#### 3.1 印刷体单公式 / 干净截图

这是当前最适合自动化的场景。MathNet 在 im2latexv2 多字体印刷公式测试集上达到 Edit 97.2%、BLEU-4 96.8%、Exact Match 83.9%；在 im2latex-100k rendered 版本上达到 Edit 94.7%、BLEU-4 94.5%、Exact Match 63.4%。[来源: https://arxiv.org/html/2404.13667]

UniMERNet 在 UniMER-Test 的简单印刷公式（SPE）上 BLEU 0.917、EditDis 0.058，在复杂印刷公式（CPE）上 BLEU 0.916、EditDis 0.060；CDM 论文重新评测的 UniMERNet-base 在 SPE 上 CDM 0.9914、ExpRate@CDM 0.9329，在 CPE 上 CDM 0.9595、ExpRate@CDM 0.8046。[来源: https://arxiv.org/html/2404.15254v1][来源: https://arxiv.org/html/2409.03643]

PaddleX 公式识别模块给出的产业模型指标显示，PP-FormulaNet_plus-L 达到 En-BLEU 92.22%、Zh-BLEU 90.64%，PP-FormulaNet_plus-M 达到 En-BLEU 91.45%、Zh-BLEU 89.76，说明中文教材、试卷、学位论文等来源上需要选择中文公式增强模型，而不是只用英文公式模型。[来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html]

#### 3.2 扫描 PDF / 真实论文 PDF / 屏幕截图

真实 PDF 和扫描场景中，单公式裁剪质量、DPI、版式和噪声都会影响结果。MathNet 分辨率实验显示，im2latexv2 测试集中 100 DPI 只有 Edit 78.2%、BLEU-4 66.0%、Exact Match 6.0%；提升到 600 DPI 后达到 Edit 98.0%、BLEU-4 98.2%、Exact Match 84.9%。[来源: https://arxiv.org/html/2404.13667]

同一论文在真实 arXiv 公式 realFormula 上，MathNet 达到 Edit 88.3%；在 InftyMDB-1 的 600 DPI 扫描公式上，MathNet 达到 Edit 89.2%、BLEU-4 85.4%、Exact Match 35.4%。这说明扫描噪声下编辑相似度仍可较高，但公式级完全正确率可能大幅下降，不能把 89% Edit 等价为 89% 可自动入库。[来源: https://arxiv.org/html/2404.13667]

UniMERNet 的屏幕截图公式（SCE）明显弱于印刷体和手写孤立公式：BLEU 0.616、EditDis 0.229；CDM 重评中 UniMERNet-base 在 SCE 上 CDM 0.9373、ExpRate@CDM 0.7697。[来源: https://arxiv.org/html/2404.15254v1][来源: https://arxiv.org/html/2409.03643]

#### 3.3 手写单公式

手写单公式比印刷体更难，但专用 HMER 模型已达到可用水平。UniMERNet 在 CROHME2014/2016/2019 上 ExpRate 分别为 67.4%、68.4%、65.4%，HME100K 为 68.0%；Uni-MuMER 使用外部数据后在 CROHME 平均 ExpRate 79.74%、ExpRate@CDM 82.86%，HME100K ExpRate 71.93%、ExpRate@CDM 73.67%。[来源: https://arxiv.org/html/2404.15254v1][来源: https://arxiv.org/html/2505.23566v2]

通用 VLM 零样本并不稳定。Uni-MuMER 论文中 GPT-4o 在 CROHME 平均 ExpRate 48.81%、ExpRate@CDM 56.21，Gemini2.5-flash 平均 ExpRate 55.32%、ExpRate@CDM 65.57，Qwen2.5-VL-72B 平均 ExpRate 56.40%、ExpRate@CDM 62.99，均低于专门微调的 Uni-MuMER。[来源: https://arxiv.org/html/2505.23566v2]

#### 3.4 多行学生解题过程

多行手写解题不是“更长的公式”这么简单，它包含推理步骤、错误中间值、单位、解释文本和边界条件。PINK 论文指出，VLM 在教育场景会出现 over-correction：模型不是忠实转写学生笔迹，而是把错误步骤修正为更合理的答案，导致自动批改系统看不到学生错误。该论文报告不同模型上的 over-correction 出现在 42.1% 到 66.2% 测试样例中。[来源: https://arxiv.org/html/2604.22774v1]

PINK 的人类专家实验显示，PINK 分数相比 BLEU 更符合人类判断：专家在同一 OCR 输出上偏好 PINK 55.0%，偏好 BLEU 39.5%。这对 AI 智能命题系统的启示是：如果后续有“拍学生解题步骤自动出题/诊断”的场景，必须要求忠实转写，不能让 VLM 自动纠错覆盖原始错误。[来源: https://arxiv.org/html/2604.22774v1]

#### 3.5 文档级 PDF 公式抽取

PDF 文档级解析比单公式 OCR 多了公式检测、阅读顺序、内联/显示公式识别、分隔符恢复和跨栏排序等问题。PDF 公式抽取基准指出，PDF 本身是面向视觉展示和打印的格式，多数 PDF 缺少语义结构，公式尤其难，因为它包含大符号集、二维结构和 LaTeX/MathML 等结构化转换需求。[来源: https://arxiv.org/html/2512.09874v1]

在 100 个合成 PDF、2,000+ 公式、20+ 解析器的基准中，排名靠前的是 Qwen3-VL-235B-A22B-Instruct（9.76/10）、Gemini 3 Pro（9.75/10）、PaddleOCR-VL（9.65/10）、Mathpix（9.64/10）。传统规则解析器和没有文档专门化的通用模型显著较弱，例如 GROBID 5.70、PyMuPDF4LLM 6.67、GPT-5-mini 6.61。[来源: https://arxiv.org/html/2512.09874v1]

### 4. 常见失败类型

1. **公式检测边界错误。** 内联公式与正文紧贴，显示公式与图表/编号/注释相邻，检测阶段就可能漏检、误检或把多个公式合并。[来源: https://www.textin.com/news/20250428161814596][来源: https://arxiv.org/html/2512.09874v1]

2. **DPI、模糊、倾斜、阴影、拍照透视。** 低分辨率导致细节丢失；MathNet 从 100 DPI 到 600 DPI，Exact Match 从 6.0% 提升到 84.9%。[来源: https://arxiv.org/html/2404.13667]

3. **数组、矩阵和多行公式。** MathNet 错误分析显示 array 结构只占 im2latexv2 的 4.8%，却贡献 52.6% 错误；realFormula 中单行公式 Edit 92.5%，多行公式 Edit 71.2%。[来源: https://arxiv.org/html/2404.13667]

4. **上下标、花括号和嵌套结构。** MathNet 的高频 Levenshtein 修正 token 包括 `{`、`}`、`^`、`_`，说明结构性 token 是主要错误来源之一。[来源: https://arxiv.org/html/2404.13667]

5. **视觉相似符号。** 常见替换包括 `*`/`\ast`、`a`/`\alpha`、`\nu`/`v`、`\phi`/`\varphi`、`\epsilon`/`\varepsilon`、`\langle`/`<`，这类错误对数学语义可能很关键。[来源: https://arxiv.org/html/2404.13667]

6. **数学字体和样式。** `\mathbb`、`\mathcal`、`\operatorname` 等数学字体会明显降低真实场景表现；MathNet 在 realFormula 中 `\mathbb` 和 `\operatorname` 的 Exact Match 均为 0.0%。[来源: https://arxiv.org/html/2404.13667]

7. **LaTeX 渲染失败。** CDM 依赖可渲染 LaTeX；Pix2tex、Texify、Mathpix、UniMERNet 在 UniMER-Test 中的 LaTeX 渲染/语法错误比例分别为 13.83%、5.03%、2.38%、1.05%。[来源: https://arxiv.org/html/2409.03643]

8. **VLM 幻觉和过度纠错。** 文档级 GPT-4o 预测会生成结构相似但内容无关的公式、缺少数学分隔符或产生 CDM=0 的渲染失败；多行手写解题中，VLM 还可能把学生错误自动修正。[来源: https://arxiv.org/html/2409.03643][来源: https://arxiv.org/html/2604.22774v1]

### 5. 普通 OCR、公式专用 OCR、VLM 和 multimodal pipeline 的边界

普通 OCR 适合线性文字、题干、选项、说明文字，但不适合把公式作为普通字符串处理。公式 OCR 应作为独立模块输出 LaTeX/MathML，并把公式区域、置信度、原图裁剪、渲染图和错误信息一起传递给下游。[来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html]

公式专用 OCR 在孤立公式和教材/论文公式上更稳，适合作为主识别器。PaddleX 公式模块、UniMERNet、MathNet、Mathpix 等都属于这个方向；其优势是针对公式结构、LaTeX 输出和训练数据做过优化。[来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html][来源: https://arxiv.org/html/2404.15254v1][来源: https://arxiv.org/html/2404.13667]

VLM 适合补全文档上下文、处理复杂布局、做二次审校、语义评估和低置信度复核。但 VLM 有幻觉、改写和过度纠错风险，不能在教育场景无约束地“理解后重写”学生公式或题目公式。[来源: https://arxiv.org/html/2512.09874v1][来源: https://arxiv.org/html/2604.22774v1]

multimodal pipeline 的合理边界是：用版面/检测模型定位公式，用公式专用 OCR 生成候选 LaTeX/MathML，用渲染/CDM/LLM judge/SymPy 校验候选，再由人工处理低置信度或高风险公式。[来源: https://arxiv.org/html/2409.03643][来源: https://arxiv.org/html/2512.09874v1]

### 6. 对 AI 智能命题系统的可落地准确率预期

| 输入场景 | 可落地预期 | 自动通过建议 | 复核建议 |
| --- | --- | --- | --- |
| 数字原生 PDF 中的干净单公式 | 较成熟；专业模型可达 90%+ 编辑/CDM 水平，Exact Match 仍需审慎 | LaTeX 可渲染、结构简单、CDM/渲染一致、SymPy 校验通过 | 涉及答案、约束条件、单位、矩阵、分段函数时抽检 |
| 教材/试卷扫描 PDF，600 DPI，版面清晰 | 可用但要按页做检测与复核 | 只允许低风险题干辅助录入自动通过 | 公式多、跨行、图文混排页面进入人工复核 |
| 手机拍照题目 | 依赖拍摄质量；倾斜、阴影、反光会显著降低可靠性 | 仅在裁剪清晰、公式短、双模型一致时自动通过 | 默认人工复核公式和答案区域 |
| 手写单公式 | 专用 HMER 可用，但完全正确率通常低于印刷体 | 简单短公式、模型高置信、渲染一致可半自动 | 所有用于出题答案、评分规则的手写公式需复核 |
| 学生多行解题过程 | 不建议只用 OCR 输出自动判分 | 不自动改写学生表达 | 重点防止 VLM 过度纠错；保留原始转写与图像 |
| 几何图形内标注公式/角标 | 高风险，检测边界和语义绑定困难 | 不建议自动通过 | 人工确认标注与图形对象关系 |

---

## 推荐工作流

### 工作流 A：题库资料导入 / 教材 PDF 解析

1. **预处理。** 输入 PDF/图片统一转为高分辨率页面图，优先 300-600 DPI；对拍照图做透视校正、去阴影、去噪和裁剪。[来源: https://arxiv.org/html/2404.13667]
2. **版面分析。** 将题干文本、表格、图形、公式区域分离；内联公式与显示公式分别标注。
3. **公式专用 OCR。** 对每个公式 crop 调用公式专用模型，输出 LaTeX/MathML、置信度、原图 crop、渲染图。
4. **渲染回检。** 将预测 LaTeX 渲染为图片，与原公式 crop 做视觉比对；不可渲染直接标记为失败。[来源: https://arxiv.org/html/2409.03643]
5. **语义校验。** 对可解析表达式用 SymPy 或规则校验等价性、变量范围、答案一致性；无法符号化的公式转人工。
6. **双模型/多模型一致性。** 对关键公式调用第二模型或 VLM judge；若 LaTeX 差异但渲染/语义一致，可降为人工抽检；若差异影响数值、上下标、单位或符号，必须复核。
7. **题目入库。** 只把通过校验的公式进入结构化题库；保留原图、公式 crop、OCR 输出、渲染图、校验记录和人工修改记录。

### 工作流 B：拍照搜题 / 图片生成题目草稿

1. 先做图片质量评分：清晰度、倾斜角、公式区域完整性、遮挡、光照。
2. 对低质量图片提示重新拍摄，不进入题目生成。
3. OCR 输出仅作为草稿，不直接生成最终题目和答案。
4. 如果公式 OCR 影响答案、约束条件、函数定义、几何标注，必须进入人工确认。
5. 对确认后的 LaTeX 再做题目知识点、答案、解析一致性校验。

### 工作流 C：学生手写解题步骤识别

1. 把目标定义为“忠实转写”，不是“求解”。
2. 禁止在 OCR 阶段让 VLM 自动修正学生错误。
3. 保存原始图像、逐行转写、模型置信度、可疑位置。
4. 下游批改模型必须能看到“学生原始表达”和“规范化表达”的差异。
5. 对模型转写得分高于原始学生步骤合理得分的情况，触发 over-correction 检测或人工复核。[来源: https://arxiv.org/html/2604.22774v1]

### 人工复核阈值建议

以下阈值是面向工程落地的保守建议，不是来源论文给出的统一行业标准：

- **自动通过。** LaTeX 可渲染；公式 crop 清晰；双模型或渲染回检一致；不含矩阵/分段/多行/图形标注；SymPy 或规则校验通过；公式不直接决定答案或评分规则。
- **人工抽检。** 单模型高置信但含上下标、根号、分式、长公式、中文教材公式或扫描噪声；题目可由上下文纠错。
- **人工必检。** 矩阵/array、分段函数、几何图形内角标和边标、单位换算、答案公式、关键条件、跨行推导、多行手写步骤、无法渲染、双模型不一致、VLM 改写迹象。
- **回退重拍/重扫。** 公式区域缺失、模糊、严重倾斜、阴影/反光遮挡、DPI 过低、渲染失败且无法定位错误。

---

## 适用场景

- 教材、教辅、试卷 PDF 中的公式结构化录入，尤其是数字原生 PDF 或高质量扫描件。
- AI 命题系统中的“题目草稿生成”和“公式标准化录入”，前提是保留人工确认环节。
- 题库清洗中对已有 LaTeX/图片公式进行渲染一致性检查。
- 教研人员将少量手写公式转为 LaTeX 草稿。
- 文档 RAG / 科研知识库中抽取显示公式和公式上下文，但需要记录解析器和置信度。

---

## 不适用场景

- 直接用普通 OCR 读取公式并自动入库。
- 将手机拍照题目 OCR 结果直接生成最终题目、答案和解析。
- 对学生手写多行解题过程直接用 VLM “理解后改写”为标准解。
- 几何图形中的公式、角标、边标和图形对象关系完全自动化抽取。
- 对高风险考试题、竞赛题、证明题、含矩阵/分段/复杂符号的题目免人工复核。

---

## 风险与约束

1. **指标误读风险。** BLEU/Edit/CDM/ExpRate 度量对象不同，不能把 BLEU 90% 解读为 90% 题目可自动入库。[来源: https://arxiv.org/html/2409.03643]
2. **输入质量风险。** DPI、模糊、扫描噪声、拍照角度对结果影响巨大；低分辨率会显著降低 Exact Match。[来源: https://arxiv.org/html/2404.13667]
3. **语义关键错误风险。** 一个上下标、负号、单位、矩阵元素或希腊字母错误就可能改变整题答案。
4. **VLM 幻觉风险。** 文档级 VLM 可能生成结构相似但内容无关的公式，或缺少数学分隔符导致解析失败。[来源: https://arxiv.org/html/2409.03643]
5. **过度纠错风险。** 在教育场景，VLM 可能把学生错误修正成正确结果，使诊断系统漏掉学习问题。[来源: https://arxiv.org/html/2604.22774v1]
6. **中文公式和教材域适配风险。** PaddleX 文档显示不同模型的中文 BLEU 差异很大，说明中文教材/试卷不应只用英文公式模型评估。[来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html]
7. **评测集外泛化风险。** 论文基准常是裁剪公式或合成 PDF；真实试卷可能含图形、手写批注、印章、低清扫描和排版噪声。

---

## 信源质量门控记录

### 门控规则

- A 级：同行评审或 arXiv 学术论文、官方文档、明确实验数据或基准；可作为核心事实来源。
- B 级：学术预印本或课程/项目论文，有实验数据但样本或严谨度较弱；可作补充，不单独支撑关键结论。
- C 级：厂商博客、产品文档、技术说明；可用于工程能力、产品指标和行业背景，需与 A/B 级交叉验证。
- D 级：低相关、营销性强、无数据、抓取失败或与主题偏离；不纳入核心结论。
- 对所有数字结论检查来源、场景、指标定义，不跨场景取平均值。

### 保留信源

| 等级 | 来源 | 保留原因 | 后续处理 |
| --- | --- | --- | --- |
| A | https://arxiv.org/html/2404.15254v1 | UniMERNet / UniMER-Test，覆盖简单印刷、复杂印刷、屏幕截图、手写四类场景 | 作为场景差异和行业可达水平依据 |
| B | https://arxiv.org/html/2412.03853v1 | 手写公式到 LaTeX 的 transformer/CNN-RNN 对比，指标完整但更像课程项目 | 作为早期/低基线参考，不支撑 SOTA 结论 |
| A | https://arxiv.org/html/2409.03643 | CDM 指标论文，系统讨论 BLEU/Edit/ExpRate 局限与视觉字符匹配 | 作为评测指标和 VLM 失败类型依据 |
| A | https://arxiv.org/html/2404.13667 | MathNet / im2latexv2 / realFormula / InftyMDB-1，给出 DPI、扫描、多行、array、数学字体错误分析 | 作为准确率、失败类型和输入质量依据 |
| A | https://arxiv.org/html/2604.22774v1 | 多行手写数学 OCR 和 VLM 过度纠错，直接对应教育 AI 场景 | 作为学生解题步骤场景的风险依据 |
| A | https://arxiv.org/html/2505.23566v2 | Uni-MuMER 手写公式 SOTA，覆盖 CROHME、HME100K、VLM 零样本对比 | 作为手写公式水平依据 |
| A | https://arxiv.org/html/2512.09874v1 | PDF 公式抽取基准，20+ parser，LLM-as-a-judge 与人类相关性 | 作为文档级 PDF pipeline 与评测方法依据 |
| C | https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html | 官方产品文档，列出 PaddleX 公式识别模型 BLEU、推理耗时、输出格式 | 用于工程选型和中文公式模型指标 |
| C | https://www.textin.com/news/20250428161814596 | 产业文章，解释 MEDR 检测/识别流程与应用场景 | 用于背景说明，不单独支撑准确率 |
| C | https://doc.simpletex.cn/zh/blog/ocr_tech.html | 工具厂商博客，列举手写公式挑战和拍摄建议 | 仅作工程实践参考 |

### 剔除或弱化信源

| 来源 | 等级 | 原因 | 处理 |
| --- | --- | --- | --- |
| https://dl.acm.org/doi/fullHtml/10.1145/3581807.3581844 | A | 页面抓取超时，本次未完成全文精读 | 不纳入最终核心事实 |
| https://huggingface.co/blog/prithivMLmods/multimodal-ocr-vlms | C | 证据包中抓取失败，且偏 VLM 展示汇总 | 不纳入核心事实 |
| https://www.llamaindex.ai/blog/ocr-accuracy | C | 普通 OCR 指标文章，非数学公式专用 | 不纳入公式准确率数字 |
| https://generic-account.github.io/OCR-Accuracy-Without-Ground-Truth-Data.html | C | 普通 OCR 无真值评估，非数学公式专用 | 不纳入公式准确率数字 |
| Medium / LinkedIn / 低分营销页面 | D | 低相关或低可信 | 剔除 |

---

## 来源与可信度

| 来源 | 类型 | 可信度 | 支撑内容 |
| --- | --- | --- | --- |
| https://arxiv.org/html/2404.15254v1 | 学术论文 | 高 | UniMERNet、UniMER-Test、SPE/CPE/SCE/HWE 指标和数据规模 |
| https://arxiv.org/html/2404.13667 | 学术论文 | 高 | MathNet、im2latexv2、realFormula、InftyMDB-1、DPI、array、数学字体、多行公式错误分析 |
| https://arxiv.org/html/2409.03643 | 学术论文 | 高 | CDM 指标、BLEU/Edit/ExpRate 局限、LaTeX 渲染错误比例、VLM 文档级错误 |
| https://arxiv.org/html/2505.23566v2 | 学术论文 | 高 | Uni-MuMER、CROHME/HME100K 手写公式指标、VLM 零样本对比 |
| https://arxiv.org/html/2604.22774v1 | 学术论文 | 高 | 多行手写数学 OCR、PINK、over-correction、教育场景评测 |
| https://arxiv.org/html/2512.09874v1 | 学术论文 | 高 | PDF 公式抽取 benchmark、LLM-as-a-judge、人类相关性、parser 排名 |
| https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html | 官方文档 | 中 | PaddleX 公式识别模型 En/Zh BLEU、模型大小、推理耗时、输出格式 |
| https://www.textin.com/news/20250428161814596 | 厂商技术文章 | 中 | MEDR 检测/识别流程、行业应用背景 |
| https://doc.simpletex.cn/zh/blog/ocr_tech.html | 厂商技术文章 | 中 | 拍照/手写/截图实践建议、工具场景描述 |
| https://arxiv.org/html/2412.03853v1 | 学术预印本/课程项目 | 中 | 手写公式到 LaTeX 的 baseline 指标和 transformer 优势 |

---

## 对于可信度较高的来源逐来源总结

### UniMERNet: A Universal Network for Real-World Mathematical Expression Recognition

URL: https://arxiv.org/html/2404.15254v1

这篇论文提出 UniMER-1M 与 UniMER-Test，覆盖简单印刷公式、复杂印刷公式、屏幕截图公式和手写公式。它强调现有基准偏向简单渲染公式或手写公式，难以代表真实场景中的长公式、噪声截图和复杂版式。[来源: https://arxiv.org/html/2404.15254v1]

可用事实：

- UniMER-1M 包含 1,061,791 个 LaTeX-Image 样本；UniMER-Test 包含 6,762 个 SPE、5,921 个 CPE、4,774 个 SCE、6,332 个 HWE，总计约 23,789 个测试样本。[来源: https://arxiv.org/html/2404.15254v1]
- UniMERNet 在 SPE/CPE/SCE/HWE 上 BLEU 分别为 0.917/0.916/0.616/0.921，EditDis 分别为 0.058/0.060/0.229/0.055。[来源: https://arxiv.org/html/2404.15254v1]
- 手写公式 CROHME2014/2016/2019 的 ExpRate 分别为 67.4%、68.4%、65.4；HME100K 为 68.0%。[来源: https://arxiv.org/html/2404.15254v1]

局限：论文指标以模型论文基准为主，仍需在本项目真实试卷、教材 PDF、拍照图上做私有评测。

适合入库的知识点：真实场景公式 OCR 需要按输入类型拆分评估；屏幕截图和复杂公式显著低于简单印刷公式。

### MathNet: A Data-Centric Approach for Printed Mathematical Expression Recognition

URL: https://arxiv.org/html/2404.13667

这篇论文价值很高，因为它不仅给准确率，还给出 DPI、真实 PDF、扫描 PDF、array、数学字体、多行公式和高频 token 错误分析。它说明训练数据规范化和多字体增强比单纯换模型更影响印刷公式 OCR 的稳健性。[来源: https://arxiv.org/html/2404.13667]

可用事实：

- 分辨率从 100 DPI 到 600 DPI 时，im2latexv2 的 Exact Match 从 6.0% 提升到 84.9%。[来源: https://arxiv.org/html/2404.13667]
- MathNet 在 im2latexv2 上 Edit 97.2%、BLEU-4 96.8%、EM 83.9%；在真实 arXiv 公式 realFormula 上 Edit 88.3%；在 InftyMDB-1 扫描公式上 Edit 89.2%、EM 35.4%。[来源: https://arxiv.org/html/2404.13667]
- array 结构占比 4.8%，却贡献 52.6% 错误；单行无 array 公式 Edit 93.3%，单行有 array 公式 Edit 84.1%。[来源: https://arxiv.org/html/2404.13667]
- 多行公式 Edit 71.2%，单行公式 Edit 92.5%；简单 y-cut 切分可把多行公式提升到 96.2% Edit，前提是行切分可靠。[来源: https://arxiv.org/html/2404.13667]
- 常见 token 错误包括 `{`、`}`、`^`、`_`，视觉相似符号包括 `a`/`\alpha`、`\nu`/`v`、`\phi`/`\varphi`。[来源: https://arxiv.org/html/2404.13667]

局限：重点是印刷公式，不直接覆盖几何图内标注和复杂手写步骤。

适合入库的知识点：公式 OCR 准确率受 DPI、array、多行切分和数学字体强影响；公式级 EM 远低于 Edit/BLEU。

### Image Over Text: Character Detection Matching

URL: https://arxiv.org/html/2409.03643

这篇论文重点不是提出新 OCR 模型，而是指出评测指标本身的问题。它认为公式识别评估不能只在 LaTeX 字符串层面比较，因为同一个公式可以有多种合法 LaTeX 表达。[来源: https://arxiv.org/html/2409.03643]

可用事实：

- ExpRate、BLEU、Edit Distance 会因公式表达风格差异而不可靠，可能低估视觉正确公式，也可能高估语义错误公式。[来源: https://arxiv.org/html/2409.03643]
- CDM 将预测 LaTeX 和真值 LaTeX 渲染成公式图片，再做字符级目标匹配，计算 F1 和 ExpRate@CDM。[来源: https://arxiv.org/html/2409.03643]
- 用户偏好实验中，CDM 在 64% 情况下优于 BLEU，32% 二者都可接受，BLEU 仅 3% 更好；作者称 CDM 在 96% 情况下可靠。[来源: https://arxiv.org/html/2409.03643]
- Pix2tex、Texify、Mathpix、UniMERNet 的 LaTeX 渲染/语法错误比例分别为 13.83%、5.03%、2.38%、1.05%。[来源: https://arxiv.org/html/2409.03643]
- UniMERNet-base 在 SPE/CPE/HWE/SCE 上 CDM 分别为 0.9914/0.9595/0.9400/0.9373，ExpRate@CDM 分别为 0.9329/0.8046/0.6431/0.7697。[来源: https://arxiv.org/html/2409.03643]

局限：CDM 依赖 LaTeX 渲染，对 Unicode、数学字体风格和语义差异仍有限。

适合入库的知识点：OCR 评测要引入渲染回检，不能只比较 LaTeX 字符串。

### Uni-MuMER: VLM Fine-Tuning for HMER

URL: https://arxiv.org/html/2505.23566v2

这篇论文说明手写公式识别的最新方向是把通用 VLM 通过 Tree-CoT、Error-Driven Learning、Symbol Counting 等任务进行领域微调，而不是直接零样本调用通用 VLM。[来源: https://arxiv.org/html/2505.23566v2]

可用事实：

- CROHME 数据集包含 8,836 个训练样本，2014/2016/2019 测试集分别含 986、1,147、1,199 张图；HME100K 包含 74,502 训练和 24,607 测试图；MathWriting 包含 230K 人写和 400K 合成表达式。[来源: https://arxiv.org/html/2505.23566v2]
- Uni-MuMER† 在 CROHME 平均 ExpRate 79.74%、ExpRate@CDM 82.86%；在 HME100K 上 ExpRate 71.93%、ExpRate@CDM 73.67%。[来源: https://arxiv.org/html/2505.23566v2]
- GPT-4o、Gemini2.5-flash、Qwen2.5-VL-72B 零样本 CROHME 平均 ExpRate 分别为 48.81%、55.32%、56.40%。[来源: https://arxiv.org/html/2505.23566v2]
- Error-Driven Learning 可减少视觉相似字符混淆，例如 `2`/`z`、`0`/`o`、`1`/`i`。[来源: https://arxiv.org/html/2505.23566v2]

局限：论文强调 HMER，不覆盖完整题目版面和几何图形语义。

适合入库的知识点：手写公式需要领域微调和结构化任务；通用 VLM 零样本不足以承担高风险自动化。

### When VLMs Fix Students / PINK

URL: https://arxiv.org/html/2604.22774v1

这篇论文直接对应教育 AI 场景。它指出多行手写数学 OCR 的目标是忠实转写学生解题过程，而不是求解；VLM 因具备数学推理能力，可能在 OCR 时把学生错误改成正确结果。[来源: https://arxiv.org/html/2604.22774v1]

可用事实：

- Over-correction 在不同模型上出现于 42.1% 到 66.2% 测试样例。[来源: https://arxiv.org/html/2604.22774v1]
- PINK 用 LLM rubric 评分，并在模型输出得分高于原始学生真值时惩罚过度纠错。[来源: https://arxiv.org/html/2604.22774v1]
- 专家偏好实验中，PINK 被偏好 55.0%，BLEU 为 39.5%。[来源: https://arxiv.org/html/2604.22774v1]
- GPT-4o 在 BLEU 排名靠前但因激进过度纠错被 PINK 惩罚；Gemini 2.5 Flash 因更忠实转写排名上升。[来源: https://arxiv.org/html/2604.22774v1]

局限：论文是 2026 预印本，需关注后续复现；但风险模式与教育场景高度相关。

适合入库的知识点：教育 OCR 必须区分“识别”和“解题”，禁止 OCR 阶段静默纠错。

### Benchmarking Document Parsers on Mathematical Formula Extraction from PDFs

URL: https://arxiv.org/html/2512.09874v1

这篇论文聚焦 PDF 公式抽取，不是孤立公式识别。它提供了面向文档 parser 的公式语义评测方法和 20+ 解析器排名，对构建题库导入 pipeline 很有参考价值。[来源: https://arxiv.org/html/2512.09874v1]

可用事实：

- 人类验证中，LLM-as-a-judge 与人类评分 Pearson r=0.78，CDM 为 0.34，文本相似度约为 0。[来源: https://arxiv.org/html/2512.09874v1]
- 基准包含 100 个合成 PDF 页面、1,411 个内联公式、641 个显示公式，评测 20+ parser。[来源: https://arxiv.org/html/2512.09874v1]
- 排名前四为 Qwen3-VL-235B-A22B-Instruct 9.76、Gemini 3 Pro 9.75、PaddleOCR-VL 9.65、Mathpix 9.64。[来源: https://arxiv.org/html/2512.09874v1]
- 论文指出 PDF 公式解析难点包括缺少语义结构、公式分隔符不一致、多栏顺序、公式漏检和多个公式合并。[来源: https://arxiv.org/html/2512.09874v1]

局限：基准使用合成 PDF，未完全覆盖真实扫描、历史文档、复杂表格和图形。

适合入库的知识点：PDF 公式抽取需要文档级 parser 评测；LLM judge 可作为评估组件但不是唯一真值。

### PaddleX 公式识别模块官方文档

URL: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html

PaddleX 文档是工程落地的重要来源，说明公式识别模块输出 LaTeX/MathML，可作为 OCR 系统关键组成部分，并列出多个模型的 BLEU、推理耗时和模型大小。[来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html]

可用事实：

- PP-FormulaNet_plus-L：En-BLEU 92.22%、Zh-BLEU 90.64，GPU 常规推理约 1476.07 ms，模型 698 MB。[来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html]
- PP-FormulaNet_plus-M：En-BLEU 91.45%、Zh-BLEU 89.76，GPU 常规推理约 1040.27 ms，模型 592 MB。[来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html]
- PP-FormulaNet-S 适用于简单印刷公式、跨行简单印刷公式；PP-FormulaNet-L 适用于简单印刷、复杂印刷、手写公式等场景。[来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html]

局限：官方文档未充分披露测试集细节，指标应通过项目私有集复测。

适合入库的知识点：中文公式识别要优先考虑 PP-FormulaNet_plus-M/L 这类中文增强模型，并用项目数据复评。

---

## 跨源矛盾检测结论

### 检测范围

- 核心数字：准确率、BLEU、Edit、ExpRate、CDM、PDF parser 评分。
- 日期：论文/文档发布时间和模型能力所处时间。
- 功能描述：公式 OCR 输出 LaTeX/MathML、文档 parser 处理 PDF、VLM 用于解析/评审。
- 因果判断：DPI、数据多样性、array、多行、数学字体、VLM 过度纠错对准确率的影响。
- 市场/公司事实：PaddleX、TextIn、SimpleTex 等厂商能力描述。

### 检测结果

未发现必须裁决的直接冲突，但发现 4 类需要保留上下文的“表面差异”：

1. **指标口径不同导致数字不可直接比较。** MathNet 的 Edit 97.2%、PaddleX 的 BLEU 92.22%、Uni-MuMER 的 ExpRate 79.74%、PDF parser 的 9.76/10 不是同一指标，不能横向排序。[来源: https://arxiv.org/html/2404.13667][来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html][来源: https://arxiv.org/html/2505.23566v2][来源: https://arxiv.org/html/2512.09874v1]

2. **同一技术在不同场景表现差异大。** 印刷公式和干净裁剪可达高编辑分；扫描、屏幕截图、多行、array 和真实 PDF 会显著下降。这不是来源冲突，而是数据域不同。[来源: https://arxiv.org/html/2404.15254v1][来源: https://arxiv.org/html/2404.13667]

3. **VLM 能力描述存在边界。** PDF parser 基准显示顶级 VLM/文档模型可在合成 PDF 公式抽取上高分，但 PINK 与 CDM 论文显示 VLM 存在幻觉、格式缺失和过度纠错。这不是矛盾，而是“文档抽取能力强”与“教育保真风险高”同时成立。[来源: https://arxiv.org/html/2512.09874v1][来源: https://arxiv.org/html/2604.22774v1][来源: https://arxiv.org/html/2409.03643]

4. **厂商博客称“高准确率”但缺少可复现实验细节。** SimpleTex/TextIn 可用于背景和流程说明，但不用于支撑准确率阈值。[来源: https://doc.simpletex.cn/zh/blog/ocr_tech.html][来源: https://www.textin.com/news/20250428161814596]

---

## 矛盾与待验证问题

1. **项目私有准确率未验证。** 当前来源给出的是公开数据集和厂商模型指标，尚未在“AI 智能命题系统-BRD-数学学科”的真实样本上复测。
2. **几何图形内公式/角标缺少直接基准。** 本次来源覆盖公式 OCR 和 PDF 公式抽取，但对几何图形中的角标、边长标注、辅助线关系识别没有足够直接数据。
3. **中文 K12 试卷场景需要单独评测。** PaddleX 给出中文 BLEU，但具体试卷扫描、中文题干混排、手写批注、几何图标注仍需私有数据。
4. **LLM judge 可用于评估但不能作为唯一事实基准。** PDF parser 论文显示 LLM judge 与人类相关性更高，但也承认 LLM judge 不完美，偶尔会漏掉细微语义错误。[来源: https://arxiv.org/html/2512.09874v1]
5. **未来模型更新会改变行业上限。** 2025-2026 文档解析和 VLM 进展很快，模型排名和成本需按季度复核。

---

## 原始证据摘录

> Mathematical Expression Recognition (MER) ... aims to convert image-based mathematical expressions into corresponding markup languages such as LaTeX or Markdown. Unlike typical OCR tasks, MER requires ... superscripts, subscripts, and various special symbols.  
> 来源: https://arxiv.org/html/2404.15254v1

> MathNet 在 im2latexv2：Edit 97.2%、BLEU-4 96.8%、EM 83.9%；realFormula：Edit 88.3%；InftyMDB-1 扫描公式：Edit 89.2%、BLEU-4 85.4%、EM 35.4%。  
> 来源: https://arxiv.org/html/2404.13667

> When the resolution is low ... 100 DPI: Edit 78.2, BLEU-4 66.0, EM 6.0; 600 DPI: Edit 98.0, BLEU-4 98.2, EM 84.9.  
> 来源: https://arxiv.org/html/2404.13667

> Out of all the prediction errors ... 52.6% are related to MEs with an array structure. However, this array structure is only present in 4.8% of all the MEs.  
> 来源: https://arxiv.org/html/2404.13667

> Formula recognition ... existing evaluation metrics such as BLEU and Edit Distance ... overlook that the same formula has diverse representations ... causing unfairness in formula recognition evaluation.  
> 来源: https://arxiv.org/html/2409.03643

> Pix2tex, Texify, Mathpix, and UniMERNet ... LaTeX rendering and syntax errors ... 13.83%, 5.03%, 2.38%, and 1.05%.  
> 来源: https://arxiv.org/html/2409.03643

> Uni-MuMER† ... reaches an ExpRate of 79.74% and ExpRate@CDM of 82.86% on the CROHME Average ... HME100K ExpRate 71.93 and @CDM 73.67.  
> 来源: https://arxiv.org/html/2505.23566v2

> Over-Correction ... occurring in 42.1% to 66.2% of test cases across different models ... experts preferred PINK 55.0% of the time versus BLEU’s 39.5%.  
> 来源: https://arxiv.org/html/2604.22774v1

> LLM-based evaluation achieves substantially higher correlation with human judgment (Pearson r=0.78) compared to CDM (r=0.34) and text similarity (r approximately 0).  
> 来源: https://arxiv.org/html/2512.09874v1

> PaddleX 公式识别模型：PP-FormulaNet_plus-L En-BLEU 92.22、Zh-BLEU 90.64；PP-FormulaNet_plus-M En-BLEU 91.45、Zh-BLEU 89.76。  
> 来源: https://paddlepaddle.github.io/PaddleX/3.0/module_usage/tutorials/ocr_modules/formula_recognition.html

---

## 入库建议

本报告目前仅为 raw 调研资料。若需要入库，建议拆分为以下 Wiki 知识点：

- `math-formula-ocr-accuracy`：数学公式 OCR 准确率与场景差异。
- `formula-ocr-evaluation-metrics`：BLEU、Edit、ExpRate、CDM、LLM judge、PINK 的边界。
- `math-formula-ocr-failure-modes`：上下标、矩阵、数学字体、多行、VLM 过度纠错等失败类型。
- `ai-question-generation-formula-ocr-workflow`：AI 智能命题系统公式 OCR 落地工作流。

未获得用户明确确认前，不应更新 `wiki/`、`wiki/_index.md`、`wiki/_graph.md`、`wiki/_log.md` 或 `SCHEMA.md`。
