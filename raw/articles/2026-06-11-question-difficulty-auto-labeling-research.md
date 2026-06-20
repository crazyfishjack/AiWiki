---
title: "数学题难度自动标注依据调研"
source-type: article
generated: 2026-06-11
generated-by: wiki-research-skill
research-mode: standard
topic: "数学题难度自动标注、IRT/CTT、AI命题系统"
---

# 数学题难度自动标注依据调研

## 调研问题

讨论点 #9：AI 智能命题系统中，数学题“基础 / 提高 / 拔高”等难度自动标注的依据是什么，如何避免只靠模型主观判断；在无学生作答数据和有历史作答数据两种阶段分别如何估计难度；如何评测自动标注质量；如何落地到当前数学命题、题库入库和组卷场景。

## Wiki 优先查询结果

本次按 `SCHEMA.md` Query 流程先读 `wiki/_index.md`，未发现与“数学题难度自动标注、IRT、CTT、学生作答数据、专家一致性、Kappa、得分率校准”直接相关的 Wiki 知识页。现有 Wiki 中仅有少量 AI 命题访谈方法论片段，不能支撑本题。因此按 `wiki-research` 技能触发外部调研，并生成本 raw 调研报告。

---

## 核心结论

1. 数学题难度应定义为“目标学生群体在该题上的预期表现”，而不是模型对题面复杂度的主观感觉。传统 CTT 常用平均得分率 / 通过率刻画难度，IRT 则把题目难度建模为学生能力达到某一水平时答对概率变化的位置参数；二者都强调难度来自“题目 × 学生群体”的交互，而不是题面孤立属性。[可信度：高；来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml；https://ar5iv.labs.arxiv.org/html/2001.07569；https://arxiv.org/html/2507.05129]

2. 无历史作答数据时，难度自动标注应采用“规则化特征评分 + LLM 辅助抽取 + 教师复核”的冷启动方案；可用特征包括知识点数量与耦合、解题步骤数、参数数量、计算复杂度、认知层级、题型、干扰项迷惑性、文本 / 符号 / 图形复杂度、是否跨知识点与是否需要逆向思维。[可信度：高；来源: https://www.mdpi.com/2227-7390/12/10/1455；https://www.arxiv.org/pdf/2602.00034；https://arxiv.org/html/2503.08551v1]

3. 有历史作答数据后，应把难度从“先验预测”升级为“数据校准”：用真实得分率、错误率、选项选择分布或 IRT 参数回填校准，并区分不同班级、学校、考试场景的学生群体差异。中国科大团队的数学试题难度预测研究明确指出，不同学校 / 考试群体的得分率不可直接比较，需按 context 训练，否则会误判题目真实难度。[可信度：高；来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]

4. “基础 / 提高 / 拔高”不宜只写成自然语言等级，应绑定可审计阈值。可落地为双轨定义：冷启动时用规则特征总分映射三档；有数据后用实际得分率或 IRT 难度参数重新校准。MDPI 数学题难度研究用 `DC = 1 - AS / TS` 定义难度系数，并将 `[0,0.45]`、`[0.45,0.83]`、`[0.83,1]` 分为 easy / moderate / difficult，可作为阈值设计参考，但本校“7:2:1”比例仍需用本校样卷和教师判断校准。[可信度：中；来源: https://www.mdpi.com/2227-7390/12/10/1455]

5. 对 AI 生成题，难度标注最好同时输出“等级 + 证据解释”：例如“拔高，因为含 3 个主要知识点、8 步以上推理、需逆向构造、包含复杂符号运算”。XGBoost-SHAP 研究显示，解释性模型可给出参数层级、推理层级、知识内容等特征对难度的贡献，降低黑盒风险。[可信度：高；来源: https://www.mdpi.com/2227-7390/12/10/1455]

6. 自动标注评测应至少包含四类指标：与专家标签的一致性、分层混淆矩阵、Kappa 一致性、真实得分率 / IRT 参数校准误差。Minitab 对 Kappa 的解释是：Kappa 衡量评定一致性并校正偶然一致；Cohen Kappa 适合两个评定员，Fleiss Kappa 适合多个评定员；AIAG 建议 Kappa 至少 0.75 可视为一致性良好。[可信度：高；来源: https://support.minitab.com/zh-cn/minitab/help-and-how-to/quality-and-process-improvement/measurement-system-analysis/how-to/attribute-agreement-analysis/attribute-agreement-analysis/interpret-the-results/all-statistics-and-graphs/kappa-statistics]

7. 对当前 AI 智能命题系统，Phase 1 不应承诺“全自动准确难度”，而应承诺“可解释自动初标 + 教师可调 + 入库后持续校准”。这与当前 BRD 中“期末前可用、教师审核、题库逐步积累、7:2:1 组卷”的约束更匹配。[可信度：中；来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml；https://www.mdpi.com/2227-7390/12/10/1455；本项目 BRD 原始上下文]

---

## 内容整理

### 1. 难度的基本定义：不要把“题面复杂”误当“学生觉得难”

试题难度有两条主线。

第一条是 CTT / 经典测量思路。它通常用学生得分率、通过率或平均得分来度量题目难度。MDPI 数学题难度研究用 `DC = 1 - AS / TS`，其中 `AS` 是平均得分、`TS` 是题目满分；得分率越高，`DC` 越低，题越容易。[来源: https://www.mdpi.com/2227-7390/12/10/1455]

第二条是 IRT / 项目反应理论思路。R2DE 论文介绍的 2PL-IRT 中，每个学生有能力参数 `theta`，每道题有难度参数 `b` 和区分度参数 `a`；题越难，学生需要越高能力才有相同答对概率；区分度反映题目区分不同能力学生的能力。[来源: https://ar5iv.labs.arxiv.org/html/2001.07569]

这意味着难度不是题面独立属性，而是题目特征、学生能力、作答场景共同形成的结果。Easy2Hard-Bench 也强调，通过人类或模型的大量表现数据，可以用 IRT / Glicko-2 等统计模型给问题分配连续难度值，并将难度标准化到统一尺度。[来源: https://arxiv.org/html/2409.18433]

### 2. 可用于自动标注的题目侧特征

数学题难度的先验特征可分为八类，适合当前系统做冷启动初标。

1. 知识点复杂度：题目涉及知识点数量、知识点层级、是否跨单元、主次知识点是否耦合。MDPI 研究使用 KCF 表示知识内容特征，并按题目覆盖知识单元数量分级。[来源: https://www.mdpi.com/2227-7390/12/10/1455]

2. 解题步骤数：步骤越多，推理链越长，通常越难。MDPI 研究的 RLF 按解题所需推理步骤划分等级；Synthetic Student Responses 研究也把 “Number of Steps” 作为 LLM 抽取的关键教育特征。[来源: https://www.mdpi.com/2227-7390/12/10/1455；https://www.arxiv.org/pdf/2602.00034]

3. 计算量与符号复杂度：数值 / 符号运算复杂度、公式数量、特殊符号、LaTeX 表达、是否需要复杂变形。MDPI 研究使用 CRF 表示计算等级，Synthetic Student Responses 使用数学符号、数字、LaTeX 等结构特征。[来源: https://www.mdpi.com/2227-7390/12/10/1455；https://www.arxiv.org/pdf/2602.00034]

4. 参数与变量数量：未知参数越多，学生需处理的信息越多，难度往往上升。MDPI 研究中 PLF 是最重要特征之一，SHAP 结果显示参数层级特征对难度贡献最大。[来源: https://www.mdpi.com/2227-7390/12/10/1455]

5. 认知层级：题目是识记、理解、应用、分析、综合还是创造。MDPI 研究用 Bloom 认知分类构建 CLF；Synthetic Student Responses 也用 LLM 抽取 Bloom’s Taxonomy Level。[来源: https://www.mdpi.com/2227-7390/12/10/1455；https://www.arxiv.org/pdf/2602.00034]

6. 题型与选项结构：选择、填空、计算、操作 / 画图、应用题、证明题的认知负担不同。对选择题，还要考虑干扰项相似度与迷惑性；MCQ 难度预测论文指出，多选题难度取决于到达正确选项的复杂性和干扰项的可信度。[来源: https://arxiv.org/html/2503.08551v1]

7. 文本 / 图形复杂度：题干长度、字符数、抽象符号、图形或表格、背景信息都会影响理解负担。MDPI 研究把字符数量 CCF、背景信息 BIF、图表等纳入特征；Synthetic Student Responses 也纳入图片、抽象符号、选项相似度等特征。[来源: https://www.mdpi.com/2227-7390/12/10/1455；https://www.arxiv.org/pdf/2602.00034]

8. 错因与误概念：题目是否容易触发常见错因，尤其是负数、单位、图形条件遗漏、方程建模、几何辅助线等。MCQ 难度预测论文用 LLM 为正确选项生成推理步骤，为干扰项生成错误反馈，并用学生选项分布预测难度。[来源: https://arxiv.org/html/2503.08551v1]

### 3. 知识点标注与难度标注的关系

难度标注依赖知识点标注，但不能等同于知识点标注。

知识点自动标注用于确定题目考什么。K12 数学知识点自动标注研究指出，数学题通常含有符号、公式、隐含逻辑和多标签知识点，普通文本分类难以直接适用；其 LABS 模型把数学公式作为整体处理，并利用标签语义注意力和多标签平滑提升知识点预测。[来源: https://arxiv.org/html/2208.09867]

LLM 知识点标注研究进一步指出，传统知识点标注通常由教育专家完成，原因是它需要理解题干、知识定义和解题逻辑之间的关系；LLM 可在零样本 / 少样本下做知识点匹配，并通过示例检索提升效果。[来源: https://arxiv.org/html/2406.13885]

对本系统而言，知识点标签应作为难度模型的输入之一，而不是唯一依据。同一知识点可以有基础题、提高题和拔高题；区别往往来自知识点组合、推理层级、计算复杂度、题型和学生常见错因。

### 4. 无学生作答数据阶段：冷启动估计方案

在 Phase 1 或新题首次入库时，系统通常没有真实作答记录，此时建议采用“可解释规则初标”。

推荐字段：

| 维度 | 示例字段 | 推荐取值 |
|---|---|---|
| 知识点 | `primary_knowledge_points`、`secondary_knowledge_points`、`knowledge_count` | 主知识点、次知识点、数量 |
| 推理 | `solution_step_count`、`reasoning_level` | 1-3 / 4-6 / 7-9 / 10+，或 1-4 级 |
| 计算 | `calculation_level` | 简单口算 / 常规运算 / 复杂符号或多步计算 / 复杂混合运算 |
| 参数 | `parameter_count_level` | 无参数 / 1 个 / 2 个 / 3 个以上 |
| 题型 | `item_type`、`response_type` | 选择、填空、计算、作图、解决问题、证明 |
| 图文 | `text_length_level`、`has_diagram`、`diagram_complexity` | 短 / 中 / 长；无图 / 简图 / 复杂图 |
| 认知 | `bloom_level`、`curriculum_level` | 记忆、理解、应用、分析、综合 |
| 错因 | `misconception_tags`、`distractor_plausibility` | 常见错因标签、干扰项相似度 |
| 学段适配 | `grade_scope`、`out_of_scope_terms` | 年级、教材章节、超纲术语检查 |

初标策略：

1. LLM 解析题面、答案、解析，抽取上述字段，并给出每个字段的证据。
2. 系统用显式规则计算难度先验分，而不是直接采用 LLM 输出的“难 / 中 / 易”。
3. 规则结果映射为 `基础 / 提高 / 拔高`，并附带“触发原因”。
4. 教师可调整等级；调整时必须选择原因，例如“步骤数低估”“图形条件隐含”“本校学生未学该方法”“压轴题常见构造”。
5. 入库时保存 `auto_label`、`teacher_label`、`label_reason`、`review_status`，为后续校准积累数据。

冷启动阶段的核心原则是：LLM 可以负责抽取和解释，最终等级应由规则和人工复核兜底。Synthetic Student Responses 研究表明，LLM 可抽取解题步骤、认知复杂度、潜在误概念等教育特征，并与语义嵌入、语言特征组合预测难度；但其仍需要真实响应数据作为 benchmark 或训练信号。[来源: https://www.arxiv.org/pdf/2602.00034]

### 5. 有历史作答数据阶段：数据校准方案

一旦系统积累了学生作答或教师批改结果，应从“先验难度”转为“校准难度”。

可用数据：

- 客观题：答对 / 答错、选项选择分布、各选项人数、答题时长。
- 主观题：得分 / 满分、分步得分、教师评分、错误类型。
- 班级维度：班级、年级、学校、考试场景、教学进度。
- 题目维度：题型、知识点、难度初标、来源、是否 AI 生成。

CTT 校准：

- 计算 `score_rate = 平均得分 / 满分`。
- 计算 `difficulty_coefficient = 1 - score_rate`。
- 计算区分度，例如高分组 / 低分组正确率差异，或题目得分与总分的相关。
- 同一场考试内比较题目更稳妥，跨班级 / 跨学校比较需要控制学生群体差异。

IRT 校准：

- 对有足够答题数据的题，估计题目难度参数 `b`，必要时估计区分度 `a`。
- 客观题可用 1PL / 2PL / 3PL；主观题或步骤分可考虑广义部分评分模型。
- R2DE 和 SMART 均强调 IRT 的价值：IRT 能同时建模学生能力和题目参数，适合从真实作答中估计难度。[来源: https://ar5iv.labs.arxiv.org/html/2001.07569；https://arxiv.org/html/2507.05129]

上下文校准：

中国科大数学试题难度预测研究明确指出，单看不同学校 / 不同考试的得分率会受学生群体能力影响；该研究用同一学校同一天同卷作为 context，并证明 context 相关训练比 context 无关训练更适合数学难度预测。[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]

因此，本系统应至少按以下层级保存校准结果：

- `global_difficulty`：全校或全样本校准结果。
- `grade_difficulty`：年级层面校准结果。
- `class_context_difficulty`：班级 / 考试场景内校准结果。
- `teacher_adjusted_difficulty`：教师最终确认标签。

### 6. “基础 / 提高 / 拔高”的建议定义

以下定义是可落地建议，需用户与数学教师确认后固化。

#### 基础

定位：覆盖教学目标中的必会知识、常规方法和直接应用，适合 7:2:1 中的 70%。

冷启动判据建议：

- 主知识点 1 个，次知识点 0-1 个。
- 解题步骤通常 1-3 步，小学计算题可按题型单独配置。
- 计算过程直接，少量常规运算。
- 题干信息清楚，无复杂图形或隐含条件。
- 认知层级以理解、直接应用为主。
- 预期大多数完成对应教学内容的学生可完成。

有数据后判据建议：

- 本校目标学生群体得分率建议 ≥ 0.75 或 ≥ 0.80。
- 若采用 `DC = 1 - AS / TS`，则可参考 easy 区间，但本校阈值需用样卷校准。[来源: https://www.mdpi.com/2227-7390/12/10/1455]

#### 提高

定位：需要多步推理、知识点组合或一定计算组织能力，适合 7:2:1 中的 20%。

冷启动判据建议：

- 2-3 个知识点组合，或主知识点有明显变式。
- 解题步骤通常 4-6 步。
- 需要选择合适方法，而不是直接套公式。
- 有一定文字信息、图形信息或实际问题背景。
- 可包含常见易错点，但不依赖偏题怪题。

有数据后判据建议：

- 本校目标学生群体得分率建议约 0.45-0.75。
- 若题目区分度较高，可优先作为“提高”或“拔高”题保留。

#### 拔高

定位：用于区分高水平学生，或作为压轴 / 数学思维题，适合 7:2:1 中的 10%。

冷启动判据建议：

- 多知识点强耦合，可能跨单元。
- 解题步骤通常 7 步以上，或关键步骤需要构造、分类讨论、逆向思维、辅助线、模型迁移。
- 计算、符号、图形或条件关系复杂。
- 学生需自行发现隐藏结构，不能只套固定模板。
- 对初中“去模型化”改革，拔高题应体现从题目本身分析，而非机械套模型。

有数据后判据建议：

- 本校目标学生群体得分率建议 < 0.45。
- 若得分率低但区分度也低，可能是表述不清、超纲或坏题，不应简单归为拔高。

### 7. 如何避免只靠模型主观判断

1. 不让 LLM 直接输出最终难度，只让它抽取可审计特征和解释。
2. 将难度等级映射写成显式规则，例如“步骤数 + 知识点数 + 计算等级 + 认知等级 + 图形复杂度”的加权分。
3. 所有 AI 生成题保存结构化特征、规则得分、模型说明、教师复核标签。
4. 教师调整必须结构化记录原因，后续用于校准权重。
5. 有作答数据后，真实得分率 / IRT 参数优先级高于冷启动先验。
6. 对低得分率但低区分度的题，触发质量复核：可能是题意歧义、超纲、解析错误或答案错误。
7. 对“拔高”题必须额外校验：是否确实考查目标学段能力，是否使用超纲术语，是否存在唯一解和可解释解法。

---

## 推荐工作流

### Cursor / 系统执行步骤

1. 建立题目难度元数据 schema。
   - 字段至少包括：`auto_difficulty_label`、`auto_difficulty_score`、`difficulty_features`、`difficulty_evidence`、`teacher_label`、`teacher_review_status`、`score_rate`、`irt_difficulty`、`discrimination`、`calibration_context`。

2. 题目生成或导入后先做结构化解析。
   - OCR / PDF 拆题后，抽取题干、答案、解析、题型、图形、公式。
   - LLM 只负责抽取知识点、步骤数、计算等级、认知等级、错因、干扰项解释。
   - 数学正确性仍需符号验证或人工审核；本仓库规则已要求 LLM 生成题必须经过 SymPy 验证。

3. 用显式规则做冷启动初标。
   - 按特征加权得到 0-100 的先验难度分。
   - 映射为 `基础 / 提高 / 拔高`。
   - 输出“为什么是这个难度”的证据列表。

4. 教师复核。
   - 页面展示：题目、答案解析、AI 标注、触发特征、建议等级。
   - 教师可一键确认或调整。
   - 调整时记录原因，形成训练 / 校准数据。

5. 组卷时使用“教师确认标签优先，自动标签兜底”。
   - Phase 1 若教师未复核，则自动标签只能用于草稿组卷，导出前提示未复核。
   - 正式期末卷建议只使用教师确认或历史数据校准过的题。

6. 考后回收数据并校准。
   - 客观题记录答对率、选项分布。
   - 主观题记录平均得分率、分步得分、常见错误。
   - 按班级、年级、考试场景计算 CTT 指标。
   - 数据足够后估计 IRT 难度与区分度。

7. 定期评测自动标注质量。
   - 每周或每批入库题抽样，计算专家一致性、Kappa、混淆矩阵、得分率校准误差。
   - 对偏差最大的题型 / 知识点更新规则权重或提示词。

### 验收规则建议

Phase 1 最小可验收：

- 每道题必须有难度等级、触发特征和解释。
- 教师可手动调整难度。
- 组卷支持按 7:2:1 抽题，并显示未复核题数量。
- 抽样 100 道题，AI 初标与教师最终标签的相邻一致率达到可接受阈值；完全跨档错误（基础标成拔高或拔高标成基础）必须人工分析。

Phase 2 数据校准验收：

- 每道已使用题能回填得分率 / 错误率。
- 支持按班级 / 年级查看题目实际难度。
- 自动发现“标注为基础但得分率低”或“标注为拔高但得分率高”的异常题。
- 对足够作答样本的题估计 IRT / 区分度参数。

Phase 3 持续优化验收：

- 不同题型、知识点、年级均有标注质量报告。
- 能根据历史数据调整特征权重。
- 能识别“坏题”：低得分率且低区分度、超纲、歧义、答案错误。

---

## 适用场景

- 新题入库前需要快速初标难度。
- AI 生成题需要判断是否满足 7:2:1 组卷比例。
- 学校暂无完整学生作答数据，但有教师可复核。
- 已有历年试卷、练习册、教师自编题，需要批量拆题并标注。
- 后续能收集作答结果，用真实得分率持续校准。
- 初中“去模型化”题、数学思维题，需要比普通题更多解释和人工复核。

---

## 不适用场景

- 完全没有教师复核，且要直接用于高利害考试。
- 题目答案或解析未经数学正确性验证。
- 没有明确学段、教材版本、知识点范围，却要求系统给出绝对难度。
- 不保存作答数据，也不允许人工反馈，导致难度模型无法校准。
- 将不同学校、不同班级、不同教学进度下的得分率直接混合比较。
- 把低得分率题目直接当成拔高题，而不检查区分度、歧义、超纲和答案错误。

---

## 风险与约束

1. 冷启动标签只能是“预测难度”，不能等同于真实难度。真实难度需要学生作答数据校准。[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]

2. 得分率受学生群体影响，跨班级 / 跨学校直接比较会产生偏差，需按 context 建模或分层校准。[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]

3. LLM 抽取步骤数、认知层级、误概念可能不稳定，应通过多次抽取、结构化提示、教师复核和样本评测控制风险。Synthetic Student Responses 研究也采用多次 LLM 抽取并聚合特征以提高稳定性。[来源: https://www.arxiv.org/pdf/2602.00034]

4. 只看准确率会掩盖分层错误。MDPI 研究使用混淆矩阵、F1、precision、recall 等指标；当前系统也应关注“基础 / 提高 / 拔高”各档的召回和跨档误判。[来源: https://www.mdpi.com/2227-7390/12/10/1455]

5. 历史作答数据需要足够样本量。R2DE 研究在构建 IRT ground truth 时只保留至少 100 名不同学生回答过的题，以降低 IRT 参数估计噪声。[来源: https://ar5iv.labs.arxiv.org/html/2001.07569]

6. 图形题和主观步骤题难度更难自动估计。SMART 研究强调开放题需要模拟学生回答、自动评分再拟合 IRT；其质量取决于学生模拟和评分模型，仍有离群回答和评分误差风险。[来源: https://arxiv.org/html/2507.05129]

7. 本项目时间约束强，6 月底前应优先交付“可解释初标 + 教师可调 + 组卷比例控制”，不要在 Phase 1 过度追求完整 IRT 系统。

---

## 信源质量门控记录

### 门控规则

- Tavily score < 0.4：剔除，除非用户明确需要某一补充概念且有二次验证来源。
- Exa 学术 / 语义结果：默认保留，但按主题相关性、可访问性、同行评审 / 期刊 / 会议质量重新评级。
- 普通商业宣传、SEO 聚合、新闻弱相关内容：剔除或仅作背景。
- C/D 级来源不得作为唯一结论依据。
- PDF 或网页抓取失败时：降级，不作为核心事实来源。
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`。

### 保留信源

1. [数据驱动的数学试题难度预测](https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml)
   - 工具：Tavily / 二次 WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：中文数学试题难度预测高相关论文，含真实大规模数学考试与答题记录、context 校准、PCC/DOA/RMSE。
   - 后续处理：进入最终报告核心来源。

2. [Novel Feature-Based Difficulty Prediction Method for Mathematics Items Using XGBoost-Based SHAP Model](https://www.mdpi.com/2227-7390/12/10/1455)
   - 工具：Exa / 二次 WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：数学题难度特征体系直接相关，包含八类特征、DC 公式、三档难度、SHAP 解释、混淆矩阵。
   - 后续处理：进入最终报告核心来源。

3. [Reasoning and Sampling-Augmented MCQ Difficulty Prediction via LLMs](https://arxiv.org/html/2503.08551v1)
   - 工具：Exa / 二次 WebFetch
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：多选题难度预测、干扰项迷惑性、LLM 推理步骤、学生选择分布与 IRT 结合，主题高度相关；预印本需后续复核发表状态。
   - 后续处理：进入最终报告核心来源。

4. [R2DE: a NLP approach to estimating IRT parameters of newly generated questions](https://ar5iv.labs.arxiv.org/html/2001.07569)
   - 工具：Exa / 二次 WebFetch
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：LAK 2020 论文，解释 IRT 难度 / 区分度，并处理新题冷启动 IRT 参数估计。
   - 后续处理：进入最终报告核心来源。

5. [Knowledge Tagging System on Math Questions via LLMs with Flexible Demonstration Retriever](https://arxiv.org/html/2406.13885)
   - 工具：Exa / 二次 WebFetch
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：知识点自动标注与数学题解题逻辑相关，可支撑“知识点是难度特征之一”；预印本需复核。
   - 后续处理：用于知识点标注关系说明。

6. [Automatic tagging of knowledge points for K12 math problems](https://arxiv.org/html/2208.09867)
   - 工具：Exa / 二次 WebFetch
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：K12 数学知识点多标签自动标注，强调数学符号、公式、隐含逻辑和多标签关系。
   - 后续处理：用于知识点特征与题库入库建议。

7. [Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation](https://www.arxiv.org/pdf/2602.00034)
   - 工具：Exa / 二次 WebFetch 使用 arXiv HTML
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：LLM 抽取解题步骤、认知复杂度、误概念等特征，并用 25 万学生响应预测 IRT 难度；预印本且日期较新，需后续复核。
   - 后续处理：用于冷启动与仿真方案。

8. [SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction](https://arxiv.org/html/2507.05129)
   - 工具：Exa / 二次 WebFetch
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：模拟学生作答、自动评分、拟合 IRT 的方法，对开放题 / 主观题有参考价值；预印本且日期较新，需后续复核。
   - 后续处理：用于未来阶段建议。

9. [Easy2Hard-Bench: Standardized Difficulty Labels for Profiling LLM Performance and Generalization](https://arxiv.org/html/2409.18433)
   - 工具：Exa / 二次 WebFetch
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：连续难度标签、IRT / Glicko-2 标准化、人工表现数据验证，对“不要只用分类等级”有参考。
   - 后续处理：用于难度连续值与校准建议。

10. [Minitab Kappa 统计量解释](https://support.minitab.com/zh-cn/minitab/help-and-how-to/quality-and-process-improvement/measurement-system-analysis/how-to/attribute-agreement-analysis/attribute-agreement-analysis/interpret-the-results/all-statistics-and-graphs/kappa-statistics)
   - 工具：Tavily / 二次 WebFetch
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Kappa 一致性解释清晰，适合支持专家一致性评测。
   - 后续处理：用于评测方法。

11. [Level-Based Learning Algorithm Based on the Difficulty Level of the Test Problem](https://www.mdpi.com/2076-3417/11/10/4380)
   - 工具：Exa / 二次 WebFetch
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：讨论分层学习、题目难度、错误率与学生等级的组合，但主题混杂，作为辅助参考。
   - 后续处理：仅作背景，不作为核心依据。

### 剔除或降级信源

1. `https://link.springer.com/article/10.1007/s41237-022-00169-9`
   - 来源等级：A
   - 剔除 / 降级原因：网页抓取被阻断，未完成二次全文精读。
   - 后续处理：可后续通过机构访问或 DOI 重新获取。

2. `https://pmc.ncbi.nlm.nih.gov/articles/PMC10177318/`
   - 来源等级：B
   - 剔除 / 降级原因：返回浏览器验证页，未获得正文。
   - 后续处理：不进入核心结论。

3. `https://arxiv.org/html/2505.13406v1`
   - 来源等级：B
   - 剔除 / 降级原因：本次 WebFetch 超时；主题偏数学知识图谱，不是难度标注核心来源。
   - 后续处理：后续如需知识图谱架构再读。

4. `https://pdf.hanspub.org/ae_1882638.pdf`
   - 来源等级：C
   - 剔除 / 降级原因：脚本精读失败，主题偏错题智能体实践，非难度标注核心来源。
   - 后续处理：仅作为潜在背景。

5. 低分新闻、商业平台、博客园数据集文章、AI 题库宣传文章等
   - 来源等级：D
   - 剔除原因：score 低、主题弱相关或缺少方法细节。
   - 后续处理：不进入报告事实依据。

---

## 来源与可信度

| 来源 | 类型 | 可信度 | 支撑内容 |
|---|---|---|---|
| https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml | 中文学术论文 | 高 | 数学试题难度预测、得分率、答题记录、context 训练、PCC/DOA/RMSE |
| https://www.mdpi.com/2227-7390/12/10/1455 | 期刊论文 | 高 | 数学题八类难度特征、DC 公式、三档难度、SHAP 解释、混淆矩阵 |
| https://arxiv.org/html/2503.08551v1 | 预印本 | 中 | MCQ 难度、推理步骤、干扰项迷惑性、学生选择分布、IRT ground truth |
| https://ar5iv.labs.arxiv.org/html/2001.07569 | 会议论文 HTML | 高 | IRT 难度 / 区分度、冷启动估计、文本预测 IRT 参数 |
| https://arxiv.org/html/2406.13885 | 预印本 | 中 | LLM 数学题知识点标注、少样本 / 零样本、专家标签 |
| https://arxiv.org/html/2208.09867 | 预印本 / K12 数学 | 中 | K12 数学知识点多标签标注、公式处理、标签语义注意力 |
| https://www.arxiv.org/pdf/2602.00034 | 预印本 | 中 | LLM 抽取教育特征、模拟学生响应、IRT 难度参数估计 |
| https://arxiv.org/html/2507.05129 | 预印本 | 中 | 模拟学生、开放题、自动评分、IRT 拟合、PCC/SCC/RMSE |
| https://arxiv.org/html/2409.18433 | 预印本 | 中 | 连续难度标签、IRT/Glicko-2、难度标准化、人类表现数据 |
| https://support.minitab.com/zh-cn/minitab/help-and-how-to/quality-and-process-improvement/measurement-system-analysis/how-to/attribute-agreement-analysis/attribute-agreement-analysis/interpret-the-results/all-statistics-and-graphs/kappa-statistics | 软件统计文档 | 高 | Cohen / Fleiss Kappa 定义、解释与阈值 |

---

## 对于可信度较高的来源逐来源总结

### 1. 数据驱动的数学试题难度预测

正文内容：论文讨论高考试题等数学题难度预测。传统人工评估依赖专家经验，试测依赖样本学生作答；认知诊断和 IRT 可利用学生答题记录估计难度、区分度、猜测度等参数。论文提出 C-MIDP、R-MIDP、H-MIDP 三种神经网络模型，用试题文本和学生答题记录预测数学题难度，并重点处理不同学生群体得分率不可比的问题。[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]

可用事实：

- 数学题难度评估长期依赖专家经验或试测，但人工成本高、主观性强。[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]
- IRT 可估计题目难度、区分度和猜测度；DINA 等认知诊断模型还会用 Q 矩阵表示题目关联知识点。[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]
- 不同学校 / 学生群体的得分率不可直接比较，需按 context 建模。[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]
- 该研究使用 PCC、DOA、RMSE 评估预测效果，H-MIDP 案例中 PCC=0.797、DOA=0.823、RMSE=0.136。[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]

局限：研究数据来自较大规模中学考试和答题记录，当前项目 Phase 1 可能没有足够作答数据，不能直接套用其训练方式。

适合入库知识点：数学题难度预测、context 相关得分率校准、CTT/IRT 与学生作答数据。

### 2. Novel Feature-Based Difficulty Prediction Method for Mathematics Items Using XGBoost-Based SHAP Model

正文内容：论文基于中国高考数学主观题与成绩数据，构建包含八类特征的数学题难度预测框架，用 XGBoost 预测难度，用 SHAP 解释各特征贡献。[来源: https://www.mdpi.com/2227-7390/12/10/1455]

可用事实：

- 数学题难度受知识要求、思维深度、解题能力、时间限制等影响。[来源: https://www.mdpi.com/2227-7390/12/10/1455]
- 论文提出八类特征：参数层级 PLF、推理层级 RLF、思维方式 TMF、计算等级 CRF、背景信息 BIF、字符数 CCF、知识内容 KCF、认知层级 CLF。[来源: https://www.mdpi.com/2227-7390/12/10/1455]
- 论文用 `DC = 1 - AS / TS` 定义难度系数，并把 `[0,0.45]`、`[0.45,0.83]`、`[0.83,1]` 映射为 easy / moderate / difficult。[来源: https://www.mdpi.com/2227-7390/12/10/1455]
- SHAP 重要性排序中，PLF、RLF、KCF、CCF、CLF 等对难度有贡献，PLF 与 RLF 是重要因素。[来源: https://www.mdpi.com/2227-7390/12/10/1455]
- 模型测试集准确率为 0.8064，并使用混淆矩阵、F1、precision、recall 等指标评估。[来源: https://www.mdpi.com/2227-7390/12/10/1455]

局限：研究对象是高中高考主观题，阈值不能直接套到小学 / 初中校本题，需要本校样题校准。

适合入库知识点：数学题难度特征体系、SHAP 可解释难度标注、三档难度阈值参考。

### 3. R2DE

正文内容：R2DE 用题干和选项文本预测新生成选择题的 IRT 难度和区分度，目标是缓解新题冷启动时缺少作答历史的问题。[来源: https://ar5iv.labs.arxiv.org/html/2001.07569]

可用事实：

- IRT 中难度表示题目需要多高能力才能以同等概率答对；区分度表示答对概率随学生能力变化的速度，可作为题目质量指标。[来源: https://ar5iv.labs.arxiv.org/html/2001.07569]
- 新题没有作答历史时，通常需要 pretesting 或专家人工赋值；前者成本高、周期长，后者主观不确定。[来源: https://ar5iv.labs.arxiv.org/html/2001.07569]
- R2DE 使用 TF-IDF 和回归模型估计难度与区分度，在测试中难度估计 RMSE=0.823、相对 RMSE=8.23%。[来源: https://ar5iv.labs.arxiv.org/html/2001.07569]
- 论文强调 IRT 参数预测还应用 performance prediction 任务验证，而不只看不可观测的 IRT 参数误差。[来源: https://ar5iv.labs.arxiv.org/html/2001.07569]

局限：数据来自在线学习平台且是选择题，不完全覆盖中小学数学主观题、作图题和证明题。

适合入库知识点：新题冷启动 IRT 难度估计、区分度、预试替代方案。

### 4. Reasoning and Sampling-Augmented MCQ Difficulty Prediction via LLMs

正文内容：该预印本提出两阶段 MCQ 难度预测：先用 GPT-4o 为正确选项生成推理步骤、为干扰项生成错误反馈，再采样不同学生知识水平，预测各选项被选择概率，最后预测 MCQ 难度。[来源: https://arxiv.org/html/2503.08551v1]

可用事实：

- 多选题难度不仅取决于到达正确答案的复杂度，还取决于干扰项是否可信。[来源: https://arxiv.org/html/2503.08551v1]
- 该方法使用学生选择分布与 KL 散度约束，使预测选项分布对齐真实学生选项分布。[来源: https://arxiv.org/html/2503.08551v1]
- 实验使用两个真实数学 MCQ 与学生响应数据集，并以 IRT 难度作为 ground truth。[来源: https://arxiv.org/html/2503.08551v1]
- 指标包括 MSE、R²、MATCH；EEDI 数据集上相对最佳 baseline MSE 降低 28.3%、R² 提升 34.6%。[来源: https://arxiv.org/html/2503.08551v1]

局限：预印本；主要面向选择题，图形题被排除到未来研究。

适合入库知识点：干扰项迷惑性、学生选项分布、LLM 推理步骤辅助难度预测。

### 5. Knowledge Tagging System on Math Questions via LLMs

正文内容：该研究用 LLM 做数学题知识点匹配，指出传统专家标注成本高，而仅用题干与知识定义语义相似度容易忽略解题逻辑。[来源: https://arxiv.org/html/2406.13885]

可用事实：

- 数学题知识点标注需要连接题干、知识定义和解题逻辑。[来源: https://arxiv.org/html/2406.13885]
- LLM 可通过先给出理由再判断，完成知识点与题目的匹配。[来源: https://arxiv.org/html/2406.13885]
- 少样本示例能提升复杂知识点判断，例如连续进位乘法这类定义较细的知识点。[来源: https://arxiv.org/html/2406.13885]

局限：重点是知识点标注，不是难度标注；只能支撑难度模型中的知识点抽取环节。

适合入库知识点：数学题知识点自动标注、LLM 少样本标注、题目-知识点匹配。

### 6. Automatic tagging of knowledge points for K12 math problems

正文内容：该研究提出 LABS 模型做 K12 数学题知识点多标签分类，处理数学公式、标签语义注意力和标签平滑。[来源: https://arxiv.org/html/2208.09867]

可用事实：

- 数学题文本通常短、含公式和符号，隐含逻辑强，普通文本分类方法难以直接应用。[来源: https://arxiv.org/html/2208.09867]
- 数学题通常对应多个知识点，且知识点之间有层级关系。[来源: https://arxiv.org/html/2208.09867]
- 该研究构建 DA-20k 数据集，含 22,498 道高中数学题、427 个标签、平均 1.89 个标签。[来源: https://arxiv.org/html/2208.09867]

局限：重点是高中数学知识点多标签分类；与本项目小学 / 初中教材知识图谱仍需映射。

适合入库知识点：数学题多标签知识点、公式整体表示、题库知识点抽取。

### 7. Synthetic Student Responses

正文内容：该预印本用 LLM 抽取教育特征，并模拟学生作答矩阵，再用 1PL-IRT 估计难度参数。[来源: https://www.arxiv.org/pdf/2602.00034]

可用事实：

- 特征包括语言特征、数学符号 / 图形、选项相似度、LLM 生成的步骤数、认知复杂度、潜在误概念等。[来源: https://www.arxiv.org/pdf/2602.00034]
- 数据包含 251,851 条学生答案、4,696 道数学题和 1,875 名学生。[来源: https://www.arxiv.org/pdf/2602.00034]
- 模型在完全未见过的问题上，预测难度参数与实际难度参数 Pearson 相关约 0.78。[来源: https://www.arxiv.org/pdf/2602.00034]

局限：预印本；模型依赖特定平台数据、翻译和 LLM 特征抽取，落地时需本地复核。

适合入库知识点：LLM 抽取教育特征、模拟响应矩阵、IRT 难度估计。

### 8. SMART

正文内容：SMART 用 LLM 模拟不同能力学生对开放题的回答，用评分模型打分，再拟合 IRT 获得题目难度。[来源: https://arxiv.org/html/2507.05129]

可用事实：

- IRT 1PL 中学生能力 `theta` 和题目难度 `b` 决定答对概率，开放题可用部分评分模型或连续分数建模。[来源: https://arxiv.org/html/2507.05129]
- SMART 管线包括模拟学生回答、LLM 评分、IRT 拟合三阶段。[来源: https://arxiv.org/html/2507.05129]
- 实验用 PCC、SCC、RMSE 评估难度预测，并报告 SMART 在两个数据集上通常优于直接预测方法。[来源: https://arxiv.org/html/2507.05129]

局限：预印本；数据不是中小学数学题，且作者也指出会出现离群生成回答和评分错误。

适合入库知识点：开放题难度预测、模拟学生、IRT 对齐。

### 9. Minitab Kappa

正文内容：Minitab 文档解释 Cohen / Fleiss Kappa 的定义、适用条件与解释。[来源: https://support.minitab.com/zh-cn/minitab/help-and-how-to/quality-and-process-improvement/measurement-system-analysis/how-to/attribute-agreement-analysis/attribute-agreement-analysis/interpret-the-results/all-statistics-and-graphs/kappa-statistics]

可用事实：

- Kappa 是校正偶然一致后的评定一致性指标。[来源: https://support.minitab.com/zh-cn/minitab/help-and-how-to/quality-and-process-improvement/measurement-system-analysis/how-to/attribute-agreement-analysis/attribute-agreement-analysis/interpret-the-results/all-statistics-and-graphs/kappa-statistics]
- Cohen Kappa 常用于两个评定员；Fleiss Kappa 是两个以上评定员的一般化。[来源: https://support.minitab.com/zh-cn/minitab/help-and-how-to/quality-and-process-improvement/measurement-system-analysis/how-to/attribute-agreement-analysis/attribute-agreement-analysis/interpret-the-results/all-statistics-and-graphs/kappa-statistics]
- Kappa=1 完全一致，Kappa=0 与偶然预期一致，Kappa<0 低于偶然一致；AIAG 建议 Kappa 至少 0.75 表示一致性良好。[来源: https://support.minitab.com/zh-cn/minitab/help-and-how-to/quality-and-process-improvement/measurement-system-analysis/how-to/attribute-agreement-analysis/attribute-agreement-analysis/interpret-the-results/all-statistics-and-graphs/kappa-statistics]

局限：这是统计软件文档，不是教育测评论文；适合作为 Kappa 用法来源。

适合入库知识点：专家一致性评测、Kappa。

---

## 跨源矛盾检测结论

### 检测范围

- 已精读来源数量：11 个，其中核心采用 10 个。
- 检测对象：核心数字、日期、功能描述、因果判断、市场 / 公司事实。
- 检测时间：2026-06-11。

### 检测结果

结论：未检测到影响本报告主要建议的核心矛盾，但存在“阈值不可直接迁移”和“预印本可信度需复核”的适用边界。

### 核心数字

- MDPI 论文给出 DC 三档阈值 `[0,0.45]`、`[0.45,0.83]`、`[0.83,1]`，但这是高考主观题研究中的分档，不与本校 `基础 / 提高 / 拔高` 天然等价。[来源: https://www.mdpi.com/2227-7390/12/10/1455]
- 中国科大论文中案例指标 H-MIDP 为 PCC=0.797、DOA=0.823、RMSE=0.136；这是该数据集上的案例分析结果，不代表所有学校场景。[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]
- R2DE 难度估计 Relative RMSE=8.23%，但其数据来自在线学习平台选择题，不是中小学数学主观题。[来源: https://ar5iv.labs.arxiv.org/html/2001.07569]

### 日期

- 核心来源覆盖 2019、2020、2022、2024、2025、2026 年。较新的 2025/2026 预印本用于方法启发，不作为唯一事实依据。

### 功能描述

- 多来源一致认为：专家判断 / 预试有成本或主观性；自动预测可辅助冷启动，但真实作答数据仍是校准难度的重要依据。[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml；https://ar5iv.labs.arxiv.org/html/2001.07569；https://www.arxiv.org/pdf/2602.00034]

### 因果判断

- “题目特征越复杂，题目越难”不是绝对因果。MDPI 研究中字符数更多反而可能更易，因为数学符号更简洁但更抽象；这提醒系统不能只用字数判断难度。[来源: https://www.mdpi.com/2227-7390/12/10/1455]

### 市场 / 公司事实

- 本报告不涉及市场规模、公司能力或商业事实判断，未检测到相关矛盾。

---

## 矛盾与待验证问题

1. 本校“基础 / 提高 / 拔高”的真实阈值待确认。外部来源给出的是通用或特定考试场景阈值，不能直接替代本校 7:2:1 组卷标准。

2. 小学与初中应分开标定。小学数学思维题可能“比初中题还难”，不能用学段低直接推断题目简单；这需要教师样题确认和本校数据校准。

3. 初中“去模型化”趋势下，难度不只取决于知识点数量，还取决于是否要求学生从题目本身分析、构造方法或迁移模型。该维度需要与初中数学老师共同定义。

4. 图形题难度特征待细化。外部来源对图形、公式、布局有提及，但当前调研没有充分覆盖中小学几何作图、辅助线、图形变换的专门难度模型。

5. 主观题步骤分数据采集方式待定。如果 Phase 1 不做机器阅卷，则只能通过教师录入平均得分或抽样得分来校准主观题难度。

6. Kappa 验收阈值待用户确认。Minitab / AIAG 给出 0.75 作为良好一致性参考，但本项目初期可先设较低试运行阈值，再逐步提高。

7. 自动难度标签是否允许进入正式卷待确认。建议正式考试只使用教师确认或历史数据校准过的标签，AI 初标仅用于草稿组卷。

---

## 原始证据摘录

> “长久以来，试题难度，特别是高考试题难度，都是教育考试国家题库建设……重点关注的指标参数……传统方法中，试题难度评估大多是由人工进行。”[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]

> “IRT通过类逻辑斯蒂回归模型，结合学生的潜在能力，可以评估试题在难度、区分度和猜测度属性上的数值。”[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]

> “由此可知，试题得分率受到学生群体水平差异性的影响……当考试学生群体处于相同的context范围下，通过考试计算的试题得分率才具有可比性。”[来源: https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2019-5-1007.shtml]

> “The difficulty of mathematics items is important in assessing the quality of examinations and the value of educational outcomes. It is generally determined by several features, including the knowledge required, the depth of thinking, the problem-solving ability, and the time constraints.”[来源: https://www.mdpi.com/2227-7390/12/10/1455]

> “We identified eight features that significantly influence the difficulty level of Chinese high school math exam items, namely, Parameter Level Features, Reasoning Level Features, Thinking Mode Features, Calculate Rank Features, Background Information Features, Character Count Features, Knowledge Content Features, and Cognitive Level Features.”[来源: https://www.mdpi.com/2227-7390/12/10/1455]

> “D C = 1 − A S / T S ... items with DC falling within the ranges of [0,0.45], [0.45,0.83], and [0.83,1] were classified as Level 0, Level 1, and Level 2.”[来源: https://www.mdpi.com/2227-7390/12/10/1455]

> “Predicting MCQ difficulty is challenging since it requires understanding both the complexity of reaching the correct option and the plausibility of distractors.”[来源: https://arxiv.org/html/2503.08551v1]

> “The likelihood of average students selecting options is closely related to MCQ difficulty.”[来源: https://arxiv.org/html/2503.08551v1]

> “The concept of difficulty is straightforward: if a question is more difficult than another, it requires a higher skill level to be answered correctly with the same probability.”[来源: https://ar5iv.labs.arxiv.org/html/2001.07569]

> “When a new question is created, it cannot be used for assessing students until a reliable estimation of its latent traits is performed.”[来源: https://ar5iv.labs.arxiv.org/html/2001.07569]

> “Knowledge tagging for questions plays a crucial role in contemporary intelligent educational applications, including learning progress diagnosis, practice question recommendations, and course content organization.”[来源: https://arxiv.org/html/2406.13885]

> “Math texts have more complex structures and semantics compared with general texts because they contain unique elements such as symbols and formulas.”[来源: https://arxiv.org/html/2208.09867]

> “Our approach combines traditional linguistic features with pedagogical insights extracted using Large Language Models, including solution step count, cognitive complexity, and potential misconceptions.”[来源: https://www.arxiv.org/pdf/2602.00034]

> “Item response theory (IRT) is a framework for jointly estimating scalar-valued abilities of students and parameters of items, mainly difficulty and discrimination, from student responses to items.”[来源: https://arxiv.org/html/2507.05129]

> “Kappa 是检验员一致的次数比例（针对偶然一致性校正）……当多位评估员评估相同的样本时，可使用 kappa 统计数据评估由多位评估员给出的名义或顺序评级的一致程度。”[来源: https://support.minitab.com/zh-cn/minitab/help-and-how-to/quality-and-process-improvement/measurement-system-analysis/how-to/attribute-agreement-analysis/attribute-agreement-analysis/interpret-the-results/all-statistics-and-graphs/kappa-statistics]

---

## 对 AI 智能命题系统的落地建议摘要

1. 产品层面：难度字段不要只有一个枚举值，至少保存“自动等级、自动分、特征证据、教师确认等级、历史校准结果”。

2. 算法层面：冷启动用规则特征评分；有数据后用得分率 / IRT 回填；二者冲突时，以教师确认和真实作答数据优先。

3. 交互层面：生成题后展示“难度依据”，例如知识点、步骤数、计算等级、图形复杂度、错因，而不是只显示“提高”。

4. 验收层面：抽样评测 AI 初标与教师标签的一致性；计算分层混淆矩阵和 Kappa；考后对比实际得分率。

5. 运维层面：建立“标注偏差复盘”机制，对频繁错标的题型、知识点和教师调整原因进行规则更新。

6. 组卷层面：7:2:1 的抽题比例应优先使用教师确认或数据校准标签；自动标签未复核时应提示风险。

7. 风险控制：低得分率不等于好拔高题。若低得分率且低区分度，应进入坏题 / 超纲 / 歧义复核队列。
