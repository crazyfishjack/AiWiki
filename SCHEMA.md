## § 1 项目概述

本 Wiki 是一个由 LLM 全权维护的通用知识库，用于积累和关联任意领域的知识。

- 目标：构建一个持续增长、可被 AI 高效检索的结构化知识图谱
- 原则：raw/ 不可变；wiki/ 由 LLM 写入；人类负责提供原料和提问
- 权威规则：`SCHEMA.md` 是本 Wiki 的唯一结构与操作契约。若其他说明文件与本文冲突，以 `SCHEMA.md` 为准；其他说明文件只能作为入口提示或补充背景，不得定义另一套字段、文件名或关系类型。

## § 2 目录结构说明

```
root/
├── SCHEMA.md                    # LLM 操作指南（核心配置文件）
├── raw/                         # 原始资料层（不可变，LLM 只读）
│   ├── articles/                # 文章、网页剪藏
│   ├── papers/                  # 论文
│   ├── notes/                   # 手动笔记、会议记录
│   ├── projects/                # 项目相关原始文档
│   └── [可按需新建]/             # 其他原始资料类型
└── wiki/
    ├── _index.md                # 全局目录
    ├── _log.md                  # 操作日志
    ├── _graph.md                # 当前关联图谱
    ├── _inbox/                  # 未归域知识点暂存区
    │   ├── some-concept.md      # domain: inbox
    │   └── some-tool.md         # domain: inbox
    ├── sources/                 # 来源摘要（固定域）
    ├── outputs/                 # 输出归档
    ├── concepts/                # 已毕业的域
    ├── tools/                   # 已毕业的域
    └── [按需新建]/              # 新知识域
```

## § 3 知识点类型注册表

| Kind           | 含义           | 示例                    |
| -------------- | ------------ | --------------------- |
| concept        | 概念、术语、理论     | 注意力机制、贝叶斯推断           |
| workflow       | 操作流程、方法论、SOP | 代码审查流程、部署步骤           |
| tool           | 工具、软件、平台、库   | Obsidian、Claude、React |
| project        | 项目、任务、计划     | 重构项目、Q3 目标            |
| person         | 人物           | Andrej Karpathy       |
| organization   | 组织、团队、公司     | Anthropic、OpenAI      |
| event          | 事件、时间节点      | GPT-4 发布、会议记录         |
| decision       | 决策记录（ADR）    | 选择 PostgreSQL 的原因     |
| source-summary | 来源摘要页        | attention-paper 摘要    |
| output         | 查询输出归档       | attention-vs-rnn 对比分析 |

> LLM 规则：遇到无法归类的知识点，可创建新 kind，
> 但必须在本表追加一行说明，并在 \_index.md 中注册。

## § 4 知识域管理规则

### 4.1 知识点的生命周期

所有新建知识点，按以下路径流转：

\[新知识点] → wiki/\_inbox/ → wiki/\[域文件夹]/
↑                    ↑
临时存放区           正式归档区

### 4.2 \_inbox/ 规则

- 所有尚未归域的知识点，统一放入 wiki/\_inbox/
- \_inbox/ 中的文件与其他知识点格式完全相同（含 frontmatter）
- frontmatter 中 domain 字段填写 inbox

### 4.3 新建域文件夹的触发条件

满足以下任一条件时，新建域文件夹：

| 条件                             | 说明     |
| ------------------------------ | ------ |
| \_inbox/ 中同一 kind 或主题的文件 ≥ 3 个 | 数量触发   |
| 某个主题被多个知识点频繁 related-to 引用     | 关联密度触发 |
| 用户明确指定                         | 手动触发   |

### 4.4 新建域文件夹时的迁移操作（必须执行）

新建域文件夹后，LLM 必须执行以下步骤：

1. **识别**：扫描 \_inbox/ 中所有属于该域的文件
2. **移动**：将这些文件从 \_inbox/ 移动到新域文件夹
3. **更新 frontmatter**：将这些文件的 domain 字段从 inbox 改为新域名
4. **更新 \_index.md**：
   - 在「知识域目录」表格中新增该域
   - 更新这些知识点条目的「域」列
5. **检查 \_graph.md**：关联关系中的文件路径无需修改
   （因为 \[\[wikilinks]] 只用文件名，不含路径）
6. **写入 \_log.md**：
   \[日期] reorganize | 新建域 \[域名]
   - 迁移文件：\[\[知识点A]], \[\[知识点B]], \[\[知识点C]]

### 4.5 迁移的安全保障

- 普通知识点的 \[\[wikilinks]] 使用文件名而非路径，迁移文件不会导致链接失效
- 唯一例外：引用来源摘要页时允许并必须使用 `[[sources/文件名]]` 前缀；`sources/` 为固定目录，不参与域迁移
- 迁移前检查：确认目标文件夹不存在同名文件
- 迁移是原子操作：要么全部完成，要么全部不做，
  不允许部分迁移后停止

### 4.6 不允许的操作

- 在 raw/ 中新建 wiki 页面
- 在 sources/ 中存放非摘要内容
- 新建域文件夹后不执行迁移（遗留文件在 \_inbox/ 中）

## § 5 页面模板（完整版）

本节定义 Wiki 中所有页面类型的标准格式。共分为 **4 大类模板**：

***

## 模板总览

| 模板编号 | 页面类型                            | 存放位置                         | 创建者 |
| ---- | ------------------------------- | ---------------------------- | --- |
| 5.1  | 通用知识点页面                         | `wiki/_inbox/` 或 `wiki/[域]/` | LLM |
| 5.2  | 来源摘要页面                          | `wiki/sources/`              | LLM |
| 5.3  | 输出归档页面                          | `wiki/outputs/`              | LLM |
| 5.4  | 特殊页面（\_index / \_log / \_graph） | `wiki/` 根目录                  | LLM |

***

### 5.1 通用知识点页面模板

适用于所有知识点，无论 `kind` 是什么。**这是使用频率最高的模板。**

#### 5.1.1 完整 Frontmatter 字段说明

```
---
# ── 【身份字段】唯一标识这个知识点 ──────────────────────
title: "知识点名称"
# 规则：与文件名保持一致，文件名用 kebab-case，title 可用自然语言

kind: concept
# 规则：从 § 3 类型注册表中选择，遇到新类型可自行创建并登记
# 可选值：concept | workflow | tool | project | person |
#         organization | event | decision | [自定义]

domain: inbox
# 规则：填写所在知识域文件夹名，未归域时填 inbox
# 示例：concepts | tools | workflows | inbox

aliases: []
# 规则：该知识点的其他常见名称或缩写，用于 Obsidian 搜索
# 示例：["注意力机制", "Attention"]

# ── 【时间字段】追踪页面生命周期 ──────────────────────
created: YYYY-MM-DD
updated: YYYY-MM-DD
# 规则：每次修改页面内容时更新 updated，created 永不修改

# ── 【质量字段】标注可信程度 ──────────────────────────
confidence: medium
# 规则：
#   high       → 多个来源印证，无矛盾，内容稳定
#   medium     → 单一来源，或存在轻微分歧，需关注
#   low        → 推断性内容，证据不足，需更多验证
#   speculative → 高度不确定，仅作假设记录，必须注明原因

status: active
# 规则：
#   active     → 当前有效的知识点（默认值）
#   superseded → 已被更新的知识点取代，不再推荐引用
#   archived   → 不再活跃但保留作历史记录
#   draft      → 内容不完整，待补充

# ── 【状态扩展字段】仅在对应状态触发时出现 ───────────────
superseded-by: ""
# 规则：仅当 status: superseded 时填写，格式为 "[[新知识点]]"

superseded-date: ""
# 规则：仅当 status: superseded 时填写，格式为 YYYY-MM-DD

archived-date: ""
# 规则：仅当 status: archived 时填写，格式为 YYYY-MM-DD

archived-reason: ""
# 规则：仅当 status: archived 时填写，说明归档原因

staleness-warning: ""
# 规则：仅当 Lint 判定来源可能过时时填写；问题解决后删除本字段

# ── 【来源字段】追踪知识来源 ──────────────────────────
sources:
  - "[[sources/article-001]]"
# 规则：
#   - 必须链接到 wiki/sources/ 中的摘要页，而非直接链接 raw/
#   - sources 链接是 wikilinks 中唯一允许带目录前缀的形式
#   - 至少有一个来源，否则 confidence 不得高于 speculative
#   - 多个来源按重要性排序

source-count: 1
# 规则：等于 sources 列表的长度，由 LLM 自动维护
#       Dataview 插件可用此字段筛选"单一来源"知识点

# ── 【关联字段】六种标准关系类型 ───────────────────────
relations:
  related-to: []
  # 含义：主题相近，但无明确方向或依赖关系
  # 方向：双向（A ↔ B）
  # 示例：[[transformer]] 与 [[bert]] 互相 related-to

  is-part-of: []
  # 含义：A 是 B 的组成部分、子集或下属概念
  # 方向：单向（A → B，A 是 B 的一部分）
  # 示例：[[注意力机制]] is-part-of [[transformer]]

  depends-on: []
  # 含义：A 的存在或运作依赖于 B
  # 方向：单向（A → B，A 依赖 B）
  # 示例：[[fine-tuning]] depends-on [[预训练模型]]

  contradicts: []
  # 含义：A 与 B 在某个观点或结论上存在冲突
  # 方向：双向（A ↔ B）
  # 规则：必须在正文「矛盾说明」章节中解释冲突的具体内容

  supersedes: []
  # 含义：A 取代了 B（A 是更新的版本或更优的替代）
  # 方向：单向（A → B，A 取代 B）
  # 规则：被取代的 B 页面必须将 status 改为 superseded

  derived-from: []
  # 含义：A 基于 B 发展而来，B 是 A 的思想来源或前身
  # 方向：单向（A → B，A 派生自 B）
  # 示例：[[transformer]] derived-from [[seq2seq]]

# ── 【标签字段】辅助检索 ────────────────────────────
tags: []
# 规则：
#   - 用于跨域的横切关注点，不用于替代 kind 或 domain
#   - 示例：["核心概念", "待深入", "已验证", "争议中"]
#   - 不超过 5 个，避免标签膨胀
---
```

#### 5.1.2 正文结构

```
## 定义

[一句话核心定义。要求：精确、自包含，不依赖上下文即可理解。]

---

## 详细说明

[主体内容。根据 kind 的不同，侧重点不同；暂无专用模板时使用本通用结构。]

---

## 关键要点

- [要点 1：最重要的结论或特征]
- [要点 2]
- [要点 3]
<!-- 规则：3-7 条，每条一句话，可直接被 LLM 引用作为答案片段 -->

---

## 关联说明

<!-- 规则：
  - 正文中所有指向知识点页面的 [[wikilinks]] 必须在 frontmatter relations 中有对应分类
  - 指向 [[sources/xxx]] 的来源链接不写入 relations，只在 frontmatter sources 和「来源」章节维护
  - 重要关联在此处用一句话说明关联的具体含义，而不只是列出链接
  - 格式：[[知识点]] — [关联类型] — [一句话说明关联原因]
-->

- [[transformer]] — is-part-of — 注意力机制是 Transformer 架构的核心组件
- [[rnn]] — supersedes — 注意力机制在序列建模任务上已全面超越 RNN

---

## 矛盾说明

<!-- 规则：
  - 仅当 frontmatter contradicts 字段非空时，此章节必须存在
  - 说明矛盾的具体内容、各方观点、当前倾向性结论
  - 如果 contradicts 为空，删除此章节
-->

- 与 [[xxx]] 的矛盾：[具体说明分歧点和各方论据]

---

## 来源

<!-- 规则：
  - 列出 frontmatter sources 中所有来源的链接
  - 每条来源后注明该来源支撑了哪些核心观点
-->

- [[sources/article-001]] — 提供了定义和基础原理
- [[sources/paper-002]] — 提供了实验验证数据
```

#### 5.1.3 完整示例

```
---
title: "注意力机制"
kind: concept
domain: concepts
aliases: ["Attention Mechanism", "Self-Attention"]
created: 2026-05-31
updated: 2026-05-31
confidence: high
status: active
sources:
  - "[[sources/attention-is-all-you-need]]"
  - "[[sources/bahdanau-attention-2014]]"
source-count: 2
relations:
  related-to:
    - "[[self-attention]]"
    - "[[multi-head-attention]]"
  is-part-of:
    - "[[transformer]]"
  depends-on:
    - "[[query-key-value]]"
  contradicts: []
  supersedes:
    - "[[rnn-sequence-modeling]]"
  derived-from:
    - "[[bahdanau-attention]]"
tags: ["核心概念", "已验证"]
---

## 定义

注意力机制是一种让神经网络在处理序列时，动态地为不同位置的输入分配
不同权重的计算方法，使模型能够聚焦于当前任务最相关的信息。

---

## 详细说明

### 背景
传统 RNN 在处理长序列时存在梯度消失问题，难以捕捉长距离依赖。
注意力机制最初由 Bahdanau 等人在 2014 年提出，作为 RNN 的补充模块。
2017 年 Transformer 论文将其发展为独立的核心架构。

### 核心机制
注意力计算分三步：
1. 将输入映射为 Query、Key、Value 三个向量
2. 计算 Query 与所有 Key 的相似度得分（点积后 softmax）
3. 用得分对 Value 加权求和，得到输出

### 应用场景
- 机器翻译（源语言→目标语言的对齐）
- 文本摘要（识别关键句子）
- 图像描述（关注图像的关键区域）

### 局限性
- 计算复杂度为 O(n²)，长序列计算开销大
- 需要大量数据才能学习到有效的注意力模式

---

## 关键要点

- 注意力机制让模型动态决定"看哪里"，而非固定处理顺序
- 是 Transformer 架构的核心，间接支撑了 GPT、BERT 等所有现代大模型
- 相比 RNN，能更好地捕捉长距离依赖关系

---

## 关联说明

- [[transformer]] — is-part-of — 注意力机制是 Transformer 的核心计算单元
- [[rnn-sequence-modeling]] — supersedes — 在大多数序列任务上已取代 RNN
- [[bahdanau-attention]] — derived-from — 本机制是 Bahdanau 注意力的泛化版本

---

## 来源

- [[sources/attention-is-all-you-need]] — 提供了 Scaled Dot-Product Attention 的完整定义
- [[sources/bahdanau-attention-2014]] — 提供了注意力机制的历史起源和原始动机
```

### 5.2 来源摘要页面模板

存放于 `wiki/sources/`，每个 `raw/` 文件对应一个。

```
---
# ── 【身份字段】────────────────────────────────────
title: "[来源标题]"
kind: source-summary
# 规则：来源摘要页的 kind 固定为 source-summary，不可更改

# ── 【来源溯源字段】──────────────────────────────────
original-path: "raw/articles/article-001.md"
# 规则：填写 raw/ 中原始文件的相对路径（精确到文件名）

original-url: ""
# 规则：如果原始资料来自网络，填写原始 URL；本地文件留空

source-type: article
# 规则：原始资料的类型
# 可选值：article | paper | note | project-doc | book-chapter |
#         meeting-note | video-transcript | [其他]

# ── 【时间字段】────────────────────────────────────
ingested: YYYY-MM-DD
# 规则：LLM 处理该来源的日期，永不修改

updated: YYYY-MM-DD
# 规则：来源摘要页最后一次被修改的日期；创建时等于 ingested
#       回填影响字段、修正来源元数据、复核质量或重摄入时均更新

original-date: YYYY-MM-DD
# 规则：原始资料的发布或创作日期，不确定时留空

# ── 【质量字段】────────────────────────────────────
source-quality: medium
# 规则：对原始资料本身质量的评估
#   high   → 权威来源、经过同行评审、论据充分
#   medium → 可信来源，但未经严格验证
#   low    → 个人观点、未经证实、需谨慎引用

# ── 【影响追踪字段】──────────────────────────────────
pages-created:
  - "[[知识点A]]"
# 规则：因摄入本来源而新建的 wiki 知识点页面

pages-updated:
  - "[[知识点B]]"
# 规则：因摄入本来源而更新的 wiki 知识点页面

contradictions-found: []
# 规则：本来源与已有 wiki 内容存在矛盾的知识点列表
#       格式：["[[知识点X]] — [矛盾描述]"]
---

## 核心摘要

[3-5 句话概括原始资料的核心内容。要求：
- 说明资料的主要论点或结论
- 不是逐段复述，而是提炼核心价值
- 读完这段就能判断是否需要深入阅读原文]

---

## 关键观点

<!-- 规则：列出 3-10 个具体的、可被引用的观点或事实 -->

1. [观点 1：尽量保留原文的具体数据或表述]
2. [观点 2]
3. [观点 3]

---

## 对 Wiki 的影响

### 新建的知识点
<!-- 列出因本来源而新建的页面及其简要说明 -->
- [[知识点A]] — [为什么新建：这是本来源引入的新概念]

### 更新的知识点
<!-- 列出因本来源而更新的页面及更新内容 -->
- [[知识点B]] — [更新了什么：补充了实验验证数据]

### 发现的矛盾
<!-- 如果本来源与已有 wiki 内容存在矛盾，在此说明 -->
<!-- 如果没有矛盾，写"无" -->
- [[知识点X]] — [矛盾描述：本来源认为 A，但现有 wiki 记录为 B]

---

## 原文摘录

<!-- 规则：
  - 仅摘录最关键的 1-3 段原文，用于支撑核心观点
  - 用引用格式（>）标注
  - 如果没有特别值得保留的原文，删除此章节
-->

> [原文摘录]
```

### 5.3 输出归档页面模板

存放于 `wiki/outputs/`，用于归档有价值的查询结果。

```
---
# ── 【身份字段】────────────────────────────────────
title: "[输出标题]"
kind: output
output-type: comparison
# 规则：输出的形式类型
# 可选值：comparison | analysis | summary | report | qa | [其他]

# ── 【时间字段】────────────────────────────────────
created: YYYY-MM-DD
updated: YYYY-MM-DD
query-date: YYYY-MM-DD
# 规则：created 为归档创建日期，永不修改；updated 为最后修改日期
#       query-date 为产生这个输出的查询日期

# ── 【溯源字段】────────────────────────────────────
triggered-by: "[用户的原始问题]"
# 规则：记录产生这个输出的原始问题，便于日后理解上下文

references:
  - "[[知识点A]]"
  - "[[知识点B]]"
# 规则：生成本输出时参考的 wiki 知识点页面

# ── 【质量字段】────────────────────────────────────
confidence: medium
filed-back: false
# 规则：
#   false → 仅作为输出归档，未反哺到知识点页面
#   true  → 输出中的新知识已被提取并更新到相应知识点页面

filed-back-to: []
# 规则：仅当 filed-back: true 时填写，列出被反哺更新的知识点页面
# 示例：["[[知识点X]]", "[[知识点Y]]"]

filed-back-date: ""
# 规则：仅当 filed-back: true 时填写，格式为 YYYY-MM-DD
---

## 问题

[用户的原始问题，原文记录]

---

## 回答

[LLM 生成的完整回答内容]

---

## 引用的知识点

- [[知识点A]] — [引用了其中哪个具体观点]
- [[知识点B]] — [引用了其中哪个具体观点]

---

## 反哺说明

<!-- 规则：
  - 如果本输出中包含新的洞察或综合结论，应反哺到知识点页面
  - 记录哪些内容已被提取并更新到 wiki
  - 如果没有反哺，写"本次输出无新增知识点，未反哺"
-->

- 已将 [具体结论] 补充到 [[知识点X]] 的关键要点章节
```

### 5.4 特殊页面格式规范

#### 5.4.1 `_index.md` 格式

```
---
title: "Wiki 全局索引"
updated: YYYY-MM-DD
total-pages: 0
total-domains: 0
---

# Wiki 索引

## 知识域目录

| 域文件夹 | 页面数 | 说明 | 最近更新 |
|---------|--------|------|---------|
| `_inbox/` | 2 | 待归域知识点暂存区 | 2026-05-31 |
| `concepts/` | 12 | 核心概念和术语 | 2026-05-30 |
| `tools/` | 8 | 工具和平台 | 2026-05-29 |
| `sources/` | 15 | 来源摘要（固定域） | 2026-05-31 |

---

## 知识点索引

<!-- 规则：
  - 按域分组排列
  - 每行一个知识点
  - LLM 查询时先读此表定位目标页面
-->

### _inbox/（待归域）
| 页面 | Kind | 摘要 | 更新日期 |
|------|------|------|---------|
| [[some-concept]] | concept | 一句话摘要 | 2026-05-31 |

### concepts/
| 页面 | Kind | 摘要 | 更新日期 |
|------|------|------|---------|
| [[注意力机制]] | concept | Transformer 的核心计算单元 | 2026-05-31 |

### sources/
| 页面 | 原始资料 | 摄入日期 |
|------|---------|---------|
| [[sources/attention-is-all-you-need]] | raw/papers/... | 2026-05-31 |
```

#### 5.4.2 `_log.md` 格式

```
---
title: "操作日志"
---

# 操作日志

<!-- 规则：
  - append-only，只追加，永不修改历史记录
  - 每条记录以 ## [日期] 操作类型 | 标题 开头
  - 便于 grep 解析：grep "^## \[" _log.md
-->

## [2026-05-31] ingest | attention-is-all-you-need.pdf
- 新建页面：[[注意力机制]], [[transformer]], [[sources/attention-is-all-you-need]]
- 更新页面：无（首次摄入）
- 发现矛盾：无

## [2026-05-31] reorganize | 新建域 concepts/
- 触发条件：_inbox/ 中 concept 类知识点达到 3 个
- 迁移文件：[[注意力机制]], [[transformer]], [[seq2seq]]
- 更新 _index.md：已登记 concepts/ 域

## [2026-05-31] query | 注意力机制与 RNN 的对比
- 参考页面：[[注意力机制]], [[rnn-sequence-modeling]]
- 输出归档：[[outputs/attention-vs-rnn-comparison]]
- 反哺：无

## [2026-05-31] lint | 全量健康检查
- 孤儿页：[[xxx]]（无入链，建议删除或补充关联）
- 缺失概念：[[yyy]]（被引用但无独立页面，建议新建）
- 矛盾待解：[[zzz]] 与 [[aaa]] 存在冲突，待人工确认
- 过时声明：无
```

#### 5.4.3 `_graph.md` 格式

```
---
title: "当前关联图谱"
updated: YYYY-MM-DD
---

# 关联图谱

<!-- 规则：
  - 按六种关联类型分组
  - _graph.md 是当前关系视图，不是历史日志
  - 允许增量更新、删除过期边，也允许全量重建
  - 箭头含义：→ 单向，↔ 双向
  - 与各知识点页面 frontmatter 的 relations 字段保持同步
  - 冲突解决、页面合并、关系删除、重复边修复时，必须改写对应章节
-->

## related-to（主题相近）
- [[注意力机制]] ↔ [[self-attention]]
- [[注意力机制]] ↔ [[multi-head-attention]]

## is-part-of（组成关系）
- [[注意力机制]] → [[transformer]]
- [[self-attention]] → [[transformer]]

## depends-on（依赖关系）
- [[注意力机制]] → [[query-key-value]]
- [[fine-tuning]] → [[预训练模型]]

## contradicts（矛盾关系）
<!-- 格式：A ↔ B | 矛盾点简述 -->
- [[scaling-law]] ↔ [[emergent-abilities]] | 涌现能力是否可预测存在分歧

## supersedes（取代关系）
<!-- 格式：新 → 旧 | 取代原因 -->
- [[注意力机制]] → [[rnn-sequence-modeling]] | 序列建模性能全面超越

## derived-from（派生关系）
<!-- 格式：新 → 源 | 派生说明 -->
- [[注意力机制]] → [[bahdanau-attention]] | Scaled Dot-Product 是其泛化
- [[transformer]] → [[seq2seq]] | 保留编解码结构，以注意力替换 RNN
```

### 5.5 Frontmatter 字段注册与更新规则

本节是所有字段更新的统一依据。模板说明字段形态，工作流说明操作顺序，本节说明字段在不同场景下如何创建、更新、清除。

#### 5.5.1 统一字段命名规则

- 字段名统一使用 kebab-case，例如 `source-count`、`original-path`、`filed-back`。
- 关系名称只允许使用 §5.5.4 中的六种标准名称，不得混用 `type`、`category`、`part_of`、`uses` 等其他体系字段。
- 页面类型统一使用 `kind` 字段，不使用 `type` 字段。
- 知识域统一使用 `domain` 字段，不使用 `folder`、`category` 字段。
- 特殊文件统一使用带下划线的文件名：`_index.md`、`_log.md`、`_graph.md`。

#### 5.5.2 通用知识点页面字段规则

| 字段                  | 类型     | 必填 | 创建规则                       | 更新规则                                      |
| ------------------- | ------ | -- | -------------------------- | ----------------------------------------- |
| `title`             | string | 是  | 使用自然语言标题，与文件名语义一致          | 只有重命名或合并页面时更新                             |
| `kind`              | enum   | 是  | 从 §3 注册表选择                 | 类型判断错误时修正；新增 kind 必须先登记 §3                |
| `domain`            | string | 是  | 新建默认 `inbox`               | 迁移到正式域时改为目标文件夹名                           |
| `aliases`           | list   | 是  | 无别名填 `[]`                  | 发现常用别名、缩写、中文名时追加；合并页面时合并去重                |
| `created`           | date   | 是  | 创建页面当天                     | 永不修改                                      |
| `updated`           | date   | 是  | 创建页面当天                     | 正文、frontmatter、关系、状态发生实质变化时更新；单纯读取不更新     |
| `confidence`        | enum   | 是  | 按 §8.3 初评                  | 新来源、矛盾、过时、人工裁决、反哺更新后重算                    |
| `status`            | enum   | 是  | 默认 `active`，内容不足可为 `draft` | 触发 §8.5 状态规则时更新                           |
| `superseded-by`     | string | 否  | 不创建                        | 仅 `status: superseded` 时添加；恢复 active 时删除  |
| `superseded-date`   | date   | 否  | 不创建                        | 仅 `status: superseded` 时添加；恢复 active 时删除  |
| `archived-date`     | date   | 否  | 不创建                        | 仅 `status: archived` 时添加；恢复 active 时删除    |
| `archived-reason`   | string | 否  | 不创建                        | 仅 `status: archived` 时添加；恢复 active 时删除    |
| `staleness-warning` | string | 否  | 不创建                        | Lint 判定来源过时时添加；补充新来源或人工复核后删除              |
| `sources`           | list   | 是  | 填写支撑本页面的 `[[sources/xxx]]` | Ingest 新来源或反哺有来源的新知识时追加，去重排序              |
| `source-count`      | number | 是  | 等于 `sources` 长度            | 每次 `sources` 变化后重算，不手工估算                  |
| `relations`         | object | 是  | 六种关系均初始化为空列表               | 关系新增、删除、矛盾解决、页面合并时同步改写                    |
| `tags`              | list   | 是  | 无标签填 `[]`                  | 只添加跨域检索标签；不用于替代 `kind` 或 `domain`；不超过 5 个 |

#### 5.5.3 来源摘要页与输出归档页字段规则

| 页面    | 字段                     | 创建规则                                        | 更新规则                                          |
| ----- | ---------------------- | ------------------------------------------- | --------------------------------------------- |
| 来源摘要页 | `title`                | 使用来源标题或原文件语义标题                              | 原始来源标题识别错误时修正                                 |
| 来源摘要页 | `kind`                 | 固定为 `source-summary`                        | 不修改                                           |
| 来源摘要页 | `original-path`        | 填写 raw 相对路径                                 | 原始路径录入错误时修正                                   |
| 来源摘要页 | `original-url`         | 网络来源填 URL，本地资料填 `""`                        | 发现更准确 URL 时更新                                 |
| 来源摘要页 | `source-type`          | 按 raw 类型或内容类型填写                             | 类型判断错误时修正                                     |
| 来源摘要页 | `ingested`             | 首次摄入日期                                      | 永不修改；重新摄入另记 `_log.md`                         |
| 来源摘要页 | `updated`              | 创建时等于 `ingested`                            | 回填影响字段、修正元数据、重评质量、重摄入或正文摘要变化时更新               |
| 来源摘要页 | `original-date`        | 原文发布/创作日期，不确定填 `""`                         | 后续查明日期时更新                                     |
| 来源摘要页 | `source-quality`       | 按 §8.6 评估                                   | 来源可信度判断改变时更新                                  |
| 来源摘要页 | `pages-created`        | 第 3 步可先填 `[]`                               | 第 8 步回填本次新建页面                                 |
| 来源摘要页 | `pages-updated`        | 第 3 步可先填 `[]`                               | 第 8 步回填本次更新页面                                 |
| 来源摘要页 | `contradictions-found` | 默认 `[]`                                     | 第 8 步回填本次发现的矛盾                                |
| 输出归档页 | `title`                | 使用查询结果标题                                    | 标题不清晰时修正                                      |
| 输出归档页 | `kind`                 | 固定为 `output`                                | 不修改                                           |
| 输出归档页 | `output-type`          | 从 comparison、analysis、summary、report、qa 中选择 | 输出分类错误时修正                                     |
| 输出归档页 | `created`              | 归档创建日期                                      | 永不修改                                          |
| 输出归档页 | `updated`              | 创建时等于 `created`                             | 修正标题、补充遗漏引用、重评置信度、反哺状态变化时更新                   |
| 输出归档页 | `query-date`           | 原查询日期                                       | 录入错误时修正                                       |
| 输出归档页 | `triggered-by`         | 原始用户问题                                      | 不改写，只在明显录入错误时修正                               |
| 输出归档页 | `references`           | 生成答案时读取的页面                                  | 归档时一次性填写；补充遗漏引用时更新                            |
| 输出归档页 | `confidence`           | 继承答案整体置信度                                   | 反哺或复核后可重评                                     |
| 输出归档页 | `filed-back`           | 默认 `false`                                  | 新洞察已更新到知识点页面后改为 `true`                        |
| 输出归档页 | `filed-back-to`        | 默认 `[]`                                     | `filed-back: true` 时填写本次反哺更新的知识点页面；取消或回滚反哺时清空 |
| 输出归档页 | `filed-back-date`      | 默认 `""`                                     | `filed-back: true` 时填写反哺日期；取消或回滚反哺时清空         |

#### 5.5.4 关系名称注册表

| 关系名            | 方向 | 含义                   | 双向维护规则                                               |
| -------------- | -- | -------------------- | ---------------------------------------------------- |
| `related-to`   | 双向 | 主题相近但无明确层级、依赖或替代关系   | A 添加 B 时，B 也必须添加 A                                   |
| `is-part-of`   | 单向 | A 是 B 的组成部分、子集或下属概念  | 只在 A 中记录 B；B 可在正文说明但不需要反向字段                          |
| `depends-on`   | 单向 | A 的存在、理解或运作依赖 B      | 只在 A 中记录 B                                           |
| `contradicts`  | 双向 | A 与 B 在事实、观点或结论上存在冲突 | A/B 双方都记录，并在双方「矛盾说明」中说明冲突                            |
| `supersedes`   | 单向 | A 取代 B               | A 记录 B；B 改为 `status: superseded` 并添加 `superseded-by` |
| `derived-from` | 单向 | A 基于 B 发展而来，但不是直接取代  | 只在 A 中记录 B                                           |

#### 5.5.5 场景更新规则

| 场景             | 必须更新的字段/文件                                                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 新建知识点          | 填全 §5.5.2 必填字段；`created`、`updated` 为当天；`domain: inbox`；`source-count` 等于 `sources` 长度                                                                   |
| 更新已有知识点        | 追加或去重 `sources`；重算 `source-count`、`confidence`；更新 `updated`；必要时更新 `aliases`、`relations`、`tags`                                                          |
| 发现矛盾           | 双方 `relations.contradicts` 同步追加；双方补「矛盾说明」；`confidence` 降级；双方 `updated` 更新                                                                               |
| 解决矛盾           | 双方移除已解决的 `contradicts`；删除或改写「矛盾说明」；重算 `confidence`；同步 `_graph.md`                                                                                       |
| 建立取代关系         | 新页面 `relations.supersedes` 添加旧页面；旧页面按 §8.5 状态机进入 `superseded`，添加 `superseded-by`、`superseded-date` 和正文提示块                                               |
| 草稿补全           | `status` 从 `draft` 改为 `active`；删除正文草稿提示块；补齐缺失章节；更新 `updated`；追加 `_log.md`                                                                               |
| 归档页面           | 按 §8.5 状态机进入 `archived`；添加 `archived-date`、`archived-reason` 和正文提示块                                                                                     |
| 取消归档或恢复 active | 按 §8.5 状态机恢复 `active`；删除 `draft` / `superseded` / `archived` 对应扩展字段和正文提示块；更新 `updated`；追加 `_log.md`                                                     |
| Lint 发现过时      | 降低 `confidence`；按 §8.5 过时警告规则添加 `staleness-warning` 和正文提示块；更新 `updated`；写入 Lint 报告                                                                      |
| 补充新来源解除过时      | 追加 `sources`；重算 `source-count`、`confidence`；删除 `staleness-warning` 和正文过时提示块；更新 `updated`；追加 `_log.md`                                                   |
| 域迁移            | 修改 `domain`；更新 `_index.md` 域目录和页面索引；必要时重建 `_graph.md`；追加 `_log.md`                                                                                      |
| Query 普通回答     | 只读，不更新任何 wiki 文件，不写 `_log.md`                                                                                                                           |
| Query 归档       | 新建 `outputs/` 页面；填 `created`、`updated`、`filed-back: false`、`filed-back-to: []`、`filed-back-date: ""`；更新 `_index.md`；追加 `_log.md`；反哺确认后更新知识点字段和输出归档页反哺字段 |
| Lint 自动修复      | 根据修复内容更新 `_index.md`、`_graph.md` 或页面字段；归档报告；追加 `_log.md`                                                                                                |

## §6 三大工作流程

### 工作流总览

#### 触发机制（核心原则）

所有工作流均由**人工显式触发**，LLM 不得自动执行任何写入操作。

#### 触发词识别规则

##### 【Ingest 触发】

用户说出以下任意形式，均识别为 Ingest 指令：

- `raw/xxx 加入 wiki`
- `处理 raw/xxx`
- `摄入 raw/xxx`
- `把 raw/xxx 加进来`
- `ingest raw/xxx`
- `raw/xxx 入库`
  **提取规则**：识别 `raw/` 路径，支持单个文件或文件夹。

##### 【Query 触发】

用户说出以下任意形式，均识别为 Query 指令：

- 直接提问（xxx 是什么、xxx 和 yyy 的区别）
- 查一下 xxx
- wiki 里有关于 xxx 的内容吗
- 帮我分析 xxx

##### 【Lint 触发】

用户说出以下任意形式，均识别为 Lint 指令：

- 帮我进行健康检查
- 检查 wiki
- lint
- wiki 健康吗
- 有没有问题

##### 【禁止自动触发】

LLM 不得在以下场景主动写入 wiki：

1. 普通对话过程中
2. 用户未明确说出触发词时
3. 用户仅单纯提及某个文件时（例如：我刚写了 raw/xxx）

***

### 工作流一：Ingest（摄入）

#### 触发确认

收到 Ingest 指令后，先复述理解，再执行流程。
**示例**

> 用户：raw/articles/attention-paper.md 加入 wiki
>
> LLM：收到。我将把 raw/articles/attention-paper.md 摄入 wiki，执行完整的 Ingest 流程（共 9 步）。开始执行……

#### 完整执行步骤（共 9 步，按序执行）

##### 第 1 步：读取原始文件

- 操作：读取 `raw/` 下指定文件全文
- 目的：解析内容，作为后续流程素材
- 注意事项：
  1. 仅读取，不做写入操作
  2. 若文件不存在，立即终止流程并告知用户
  3. 若指定为文件夹，列出内部所有文件并逐个处理

##### 第 2 步：读取 Wiki 当前状态

按顺序读取以下文件：

1. `wiki/_index.md`：梳理现有知识点全貌
2. `wiki/_graph.md`：梳理现有知识关联关系
3. `wiki/sources/`：校验当前来源是否已摄入
   **处理规则**

- 若来源已存在于 `sources/`：告知用户「该来源已于 \[日期] 摄入，对应页面为 \[\[sources/xxx]]。如需重新摄入（来源有更新），请确认。」，等待用户确认后继续。
- 若来源未摄入，正常推进流程。

##### 第 3 步：创建来源摘要页

- 操作：在 `wiki/sources/` 新建文件
- 命名规则：与 `raw/` 原文件名保持一致（kebab-case）
  示例：`raw/articles/attention-paper.md` → `wiki/sources/attention-paper.md`
- 内容：按照 §5.2 来源摘要模板填写，`pages-created`、`pages-updated` 字段暂留空，后续回填。
- 写入要求：本步骤完成后**立即写入磁盘**，不统一延后处理。

##### 第 4 步：识别并处理知识点

从来源内容中提取可独立建页的知识点，**满足任一标准即可建页**：

1. 属于独立概念、工具、人物、组织、流程、项目、决策
2. 为内容重点阐述对象，非一笔带过
3. 预估会被其他知识点引用

###### 分支判断逻辑

1. **Wiki 中已有同名页面 → 执行更新流程**
   a. 读取现有页面全文
   b. 将新来源信息补充至正文对应章节
   c. 在 frontmatter 的 `sources` 列表追加新来源
   d. 按 `sources` 实际长度重算 `source-count`
   e. 校验新旧内容是否矛盾：存在矛盾则在页面「矛盾说明」章节记录，并在 frontmatter `contradicts` 字段追加；无矛盾则正常更新
   f. 将 frontmatter `updated` 字段更新为当日日期
   g. 结合新来源质量，重新评估 `confidence` 字段
   h. 按 §5.5.2 检查 `title`、`kind`、`domain`、`aliases`、`status`、`relations`、`tags` 是否需要同步更新
2. **Wiki 中无同名页面 → 执行新建流程**
   a. 按照 §5.1 通用知识点模板创建文件
   b. 新文件统一存放至 `wiki/_inbox/`
   c. 根据内容填写 `kind` 字段（参考 §3 类型注册表）
   d. `domain` 字段统一填写 `inbox`
   e. 按 §5.5.2 填全所有必填字段：`title`、`aliases`、`created`、`updated`、`confidence`、`status`、`sources`、`source-count`、`relations`、`tags`
   f. 校验阈值：若 `_inbox/` 内**同类知识点≥3 个**，触发域升级检查。

###### 第 4 步附录：域升级检查

**触发条件**：`_inbox/` 内同一 `kind`/ 主题的文件数量达到 3 个
**执行步骤**

1. 提示用户：`_inbox/ 中已有 3 个 [kind] 类知识点，建议新建域文件夹 [推荐名称]/。是否现在创建？`
2. 用户确认创建：
   a. 新建 `wiki/[域名]/` 文件夹
   b. 将 `_inbox/` 内相关文件迁移至新文件夹
   c. 更新对应文件的 `domain` 字段
   d. 在 `_index.md`「知识域目录」表格中新增该域条目
3. 用户拒绝创建：记录提示，新文件继续存入 `_inbox/`。

##### 第 5 步：处理关联关系

针对本次所有新建、更新的知识点，遍历六种关联类型建立对应关系，**仅基于明确依据添加，不主观猜测**。

| 关联类型         | 规则说明         | 操作方向                                                            |
| ------------ | ------------ | --------------------------------------------------------------- |
| related-to   | 主题相近的知识点     | 双向添加（双方互相引用）                                                    |
| is-part-of   | 属于某个大概念的组成部分 | 单向添加                                                            |
| depends-on   | 运作依赖其他知识点    | 单向添加                                                            |
| contradicts  | 观点、内容存在冲突    | 双向添加，双方页面均需补充矛盾说明                                               |
| supersedes   | 取代旧知识点       | 单向添加；同时将旧页面 `status` 改为 `superseded`，并新增 `superseded-by: [[A]]` |
| derived-from | 基于现有知识点发展而来  | 单向添加                                                            |

**写入原则**

1. 双向关联需同步更新双方页面
2. 所有被关联页面的 `updated` 字段更新为当日日期

##### 第 6 步：更新 \_index.md

采用**增量更新**，保留原有格式，分三部分修改：

1. **更新「知识域目录」表格**
   - 新建域：新增表格行
   - 所有相关域：更新页面数、最近更新日期
2. **更新「知识点索引」表格**
   - 新建知识点：在对应域分组下新增行，填写页面链接、kind、一句话摘要、当日日期
   - 已有知识点：更新更新日期，摘要大幅变动时同步更新摘要内容
3. **更新文件头部统计**
   - `total-pages`：统计 wiki 下全部有效 `.md` 文件总数（排除特殊文件）
   - `total-domains`：统计知识域文件夹总数
   - `updated`：填写当日日期

##### 第 7 步：同步 \_graph.md

`_graph.md` 是当前关联图谱视图，允许增量更新、删除过期边，也允许全量重建；不得为了保留历史而留下已经失效的关系。历史变化只记录在 `_log.md`。

1. 按六种关联类型分章节维护内容，格式规范：
   ```
   related-to:   [[A]] ↔ [[B]]
   is-part-of:   [[A]] → [[B]]
   depends-on:   [[A]] → [[B]]
   contradicts:  [[A]] ↔ [[B]]  |  矛盾点简述
   supersedes:   [[A]] → [[B]]  |  取代原因简述
   derived-from: [[A]] → [[B]]  |  派生说明简述
   ```
2. 一致性检查：以所有知识点页面的 `relations` 字段为准，去重、删除过期边、补齐缺失边。
3. 更新文件头部 `updated` 为当日日期。

##### 第 8 步：回填来源摘要页

回到第 3 步创建的 `sources/` 摘要页，补全空字段：

- `pages-created`：填写本次新建的所有知识点页面链接
- `pages-updated`：填写本次更新的所有知识点页面链接
- `contradictions-found`：填写本次发现的矛盾关系，格式：`[[知识点X]] — 矛盾描述`

##### 第 9 步：写入 \_log.md 并输出摘要

###### 操作 A：追加日志至 \_log.md

格式（固定格式，便于检索解析）：

```
## [YYYY-MM-DD] ingest | [原始文件名]
- 来源页面：[[sources/xxx]]
- 新建知识点（N 个）：[[A]], [[B]], [[C]]
- 更新知识点（M 个）：[[D]], [[E]]
- 新建域文件夹：[域名]（如有）/ 无
- 迁移文件（如有）：[[X]], [[Y]] → [域名]/
- 发现矛盾：[[P]] ↔ [[Q]]（矛盾描述）/ 无
- 新增关联（K 条）：[关联类型] [[A]] → [[B]] 等
```

###### 操作 B：向用户输出执行摘要

**示例**

```
✅ Ingest 完成：raw/articles/attention-paper.md
📄 来源摘要：[[sources/attention-paper]]
🆕 新建知识点（3 个）：[[注意力机制]], [[transformer]], [[query-key-value]]
🔄 更新知识点（1 个）：[[seq2seq]]（补充了被取代的说明）
🔗 新增关联（5 条）：
   - [[注意力机制]] is-part-of [[transformer]]
   - [[注意力机制]] supersedes [[rnn-sequence-modeling]]
   - [[注意力机制]] derived-from [[bahdanau-attention]]
   - [[注意力机制]] depends-on [[query-key-value]]
   - [[注意力机制]] related-to [[self-attention]]
⚠️  发现矛盾（1 处）：[[scaling-law]] ↔ [[emergent-abilities]]，已记录
📁 _inbox/ 提示：concept 类已有 3 个，建议新建 concepts/ 域
```

#### Ingest 流程图

```
用户触发
    ↓
第1步：读取 raw/ 文件
    ↓
第2步：读取 _index.md / _graph.md / sources/
    ↓ （检查是否重复摄入）
第3步：创建 sources/ 摘要页（pages-created 暂留空）
    ↓
第4步：逐个处理知识点
    ├── 已有页面 → 更新内容 + sources + confidence
    └── 无页面  → 新建到 _inbox/ + 检查域升级阈值
    ↓
第5步：建立六种关联关系（更新双方页面）
    ↓
第6步：增量更新 _index.md
    ↓
第7步：同步 _graph.md
    ↓
第8步：回填 sources/ 摘要页的 pages-created/updated 字段
    ↓
第9步：追加 _log.md + 输出摘要给用户
```

***

### 工作流二：Query（查询）

#### 触发确认

Query 分为两类：

- **普通查询**：只读操作，只读取 wiki 并回答用户；不创建文件、不更新 `_index.md`、不写 `_log.md`。
- **归档查询**：用户确认归档后才写入 `wiki/outputs/`，并同步更新 `_index.md` 与 `_log.md`；如需反哺知识点，必须再次获得用户确认。

普通查询无需额外确认，直接执行流程。
**示例**

> 用户：注意力机制和 RNN 有什么区别？
> LLM：（直接进入查询流程）

#### 完整执行步骤（共 5 步；前 4 步只读）

##### 第 1 步：解析问题，制定检索策略

分析用户问题，识别核心实体、概念，内部输出：

- 核心关键词：\[xxx, xxx]
- 预期页面类型：\[类型]
- 检索策略：优先通过 `_index.md` 定位页面，再读取详情内容

##### 第 2 步：读取 \_index.md 定位相关页面

1. 读取 `wiki/_index.md` 全文，在「知识点索引」中检索关键词
2. 按优先级排序候选页面：精确匹配 > 摘要含关键词 > 同域页面
3. 无匹配内容时，回复：`Wiki 中暂无关于 [关键词] 的内容。如需建立，可以提供相关资料并触发 Ingest。`，终止流程。

##### 第 3 步：读取目标页面及关联页面

按候选列表依次读取页面，规则如下：

1. 优先读取直接命中的目标页面
2. 其次读取页面 `relations` 下的关联页面（优先 `contradicts`、`supersedes`、`related-to`）
3. 递归读取关联页面，**最大递归 2 层**
4. 单次查询读取页面上限：**15 个**，超限仅保留直接命中页面

##### 第 4 步：综合生成答案

基于读取内容输出结构化答案，格式要求：

1. 所有引用知识点使用 `[[wikilinks]]` 标注
2. 存在 `contradicts` 关系，明确标注分歧点
3. 存在 `supersedes` 关系，说明新旧替代关系
4. 引用来源链接至 `sources/` 摘要页，不指向 raw 原文

##### 第 5 步：询问是否归档

普通查询到第 4 步结束即完成，不写入任何 wiki 文件。仅当满足归档询问条件并且用户明确选择「是」时，进入归档查询写入流程。

**触发询问条件**（满足任一即可）

1. 答案字数超 200 字
2. 答案综合分析跨 3 个及以上页面
3. 用户明确表示内容有价值
   **询问话术**：`这个分析是否值得归档到 wiki？归档后可在未来查询中直接引用。[是/否]`

- 用户选择「否」或未明确确认：保持普通查询结果，不写入 `_log.md`。
- 用户选择「是」：执行归档查询写入流程。

###### 归档查询写入流程

1. 在 `wiki/outputs/` 新建文件，按 §5.3 输出归档模板填写。
2. 在 `_index.md` 的 `outputs/` 域新增条目，并更新 `_index.md` frontmatter 统计。
3. 检测答案内新知识点或新综合结论，询问用户是否反哺更新原有知识点页面。
4. 用户确认反哺后，按 §5.5.5 更新相关知识点页面、`_graph.md` 和 `_index.md`。
5. 追加一条 query 记录至 `_log.md`。

###### 归档查询日志格式

格式：

```
## [YYYY-MM-DD] query | [问题摘要（不超过30字）]
- 参考页面（N 个）：[[A]], [[B]], [[C]]
- 输出归档：[[outputs/xxx]] / 未归档
- 反哺更新：[[知识点X]]（补充了 yyy）/ 无
```

***

### 工作流三：Lint（健康检查）

#### 触发确认

**示例**

> 用户：帮我进行健康检查
> LLM：收到。开始对 wiki/ 进行全量健康检查，将扫描以下 7 类问题。这可能需要几分钟……

#### 完整执行步骤（共 3 步）

##### 第 1 步：全量扫描（7 类检查项）

遍历 `wiki/` 下所有 `.md` 文件，逐项检测：

1. **孤儿页面**
   - 定义：文件存在，但无任何页面通过 `[[wikilinks]]` 引用；`_index.md`、`_log.md`、`_graph.md` 不计入
   - 检测：统计全量引用链接，筛选未被引用的知识点页面
2. **断链**
   - 定义：页面内 `[[wikilink]]` 指向的文件不存在
   - 检测：逐一校验链接对应的文件是否真实存在
3. **关联不一致**
   - 定义：页面 `relations` 字段与 `_graph.md` 内容不同步
   - 检测：对比两者关联对，区分「\_graph.md 缺失关联」「\_graph.md 冗余过期关联」
4. **未分类的 wikilinks**
   - 定义：正文内使用链接，但未在 `frontmatter relations` 中归类
   - 检测：对比正文链接与 `relations` 列表，筛选未分类链接
5. **过时声明**
   - 定义：已标记 `status: superseded` 的废弃页面，仍被其他页面引用且未标注状态
   - 检测：检索废弃页面，校验所有引用页面
6. **\_index.md 同步状态**
   - 定义：`_index.md` 记录与实际文件不一致
   - 检测：对比文件列表与索引表格，区分「未登记页面」「幽灵条目」
7. **知识缺口建议**
   - 定义：链接出现频次≥3 次，但无对应独立页面（通常同步为断链）
   - 检测：统计链接引用频次，筛选高频无页概念

##### 第 2 步：生成健康检查报告

输出结构化报告，格式如下：

```
## Wiki 健康检查报告
检查时间：YYYY-MM-DD
扫描页面总数：N 个

### 🔴 需要立即处理
**断链（X 处）**
| 所在页面 | 断链目标 | 建议操作 |
|---------|---------|---------|
| [[页面A]] | [[不存在的页面]] | 新建页面 / 修正链接名 |

**过时引用（X 处）**
| 引用方 | 被引用的废弃页面 | 应改为引用 |
|--------|----------------|-----------|
| [[页面B]] | [[旧知识点]] | [[新知识点]] |

### 🟡 建议处理
**孤儿页面（X 个）**
| 页面 | Kind | 建议操作 |
|------|------|---------|
| [[页面C]] | concept | 在相关页面中添加引用，或评估是否删除 |

**未分类 wikilinks（X 处）**
| 所在页面 | 未分类链接 | 建议关联类型 |
|---------|-----------|------------|
| [[页面D]] | [[页面E]] | related-to |

**_index.md 未登记页面（X 个）**
| 文件路径 | 建议操作 |
|---------|---------|
| wiki/_inbox/xxx.md | 在 _index.md 中补充登记 |

### 🟢 知识缺口建议
**建议新建页面（X 个）**
| 被引用名称 | 引用次数 | 建议 kind |
|-----------|---------|---------|
| [[概念X]] | 5 次 | concept |

**_graph.md 待同步（X 条）**
| 关联类型 | 关联对 | 操作 |
|---------|-------|------|
| related-to | [[A]] ↔ [[B]] | 同步到 _graph.md |

### 📊 总体状态
- 严重问题：X 个（需立即处理）
- 一般问题：Y 个（建议处理）
- 知识缺口：Z 个（可选处理）
```

##### 第 3 步：询问修复方式，写入 \_log.md

###### 操作 A：修复选择询问

话术：

> 以上问题是否需要我自动修复？
> 可选：
> \[1] 自动修复所有「需要立即处理」的问题
> \[2] 逐条确认后修复
> \[3] 仅保存报告，不修复
> \[4] 指定修复某类问题（如：只修复断链）

**修复权限划分**

- ✅ 可自动修复：补充 `_index.md` 未登记页面、同步 `_graph.md` 缺失或冗余关联、更新过时引用链接
- ❌ 必须用户确认：删除孤儿页面、新建知识缺口页面、修改 `contradicts` 关系

###### 操作 B：归档报告

在 `wiki/outputs/` 创建报告文件，命名规则：`lint-YYYY-MM-DD.md`，存入完整检查报告。

###### 操作 C：追加日志至 \_log.md

格式：

```
## [YYYY-MM-DD] lint | 全量健康检查
- 扫描页面：N 个
- 断链：X 处
- 孤儿页面：X 个
- 未分类 wikilinks：X 处
- _index.md 未登记：X 个
- _graph.md 待同步：X 条
- 知识缺口建议：X 个
- 过时引用：X 处
- 自动修复：[已执行 / 未执行]
- 报告归档：[[outputs/lint-YYYY-MM-DD]]
```

***

### 附录：特殊对象的更新规则速查表

| 对象          | Ingest 时                | 普通 Query 时 | 归档 Query 时         | Lint 时       |
| ----------- | ----------------------- | ---------- | ------------------ | ------------ |
| `_index.md` | 增量更新：新增知识点行、更新域页面数与日期   | 只读         | 新增 outputs 条目，更新统计 | 修复：补充未登记页面   |
| `_log.md`   | 追加一条 ingest 记录          | 不写入        | 追加一条 query 记录      | 追加一条 lint 记录 |
| `_graph.md` | 同步当前关系：可增量、可删除过期边、可全量重建 | 只读         | 反哺知识点时同步当前关系       | 修复：同步缺失或冗余关联 |
| `sources/`  | 新建来源摘要页                 | 只读（作为引用来源） | 只读（作为引用来源）         | 只读（检查未摄入来源）  |
| `outputs/`  | 不写入                     | 不写入        | 新建输出归档页            | 新建 Lint 报告页  |

**核心原则**：`_log.md` 仅做追加操作，永不修改历史记录。

## §7 命名规范

### 7.1 设计原则

命名规范的目标只有一个：让任何 Agent 在任何时候都能通过名称准确定位文件，不产生歧义，不需要额外解释。

好的命名必须满足四个条件：

- ✅ 可预测 — 看到内容能猜到文件名，看到文件名能猜到内容
- ✅ 跨平台 — 在 Windows /macOS/ Linux 下均不出错
- ✅ 机器友好 — grep /glob 可直接使用，不需要转义
- ✅ 人类可读 — 不需要解码，扫一眼就知道是什么

### 7.2 文件命名规则

#### 7.2.1 通用规则（所有文件）

规则 1：统一使用 kebab-case（小写字母 + 连字符）

- ✅ attention-mechanism.md
- ✅ react-hooks-workflow\.md
- ❌ AttentionMechanism.md（PascalCase，禁止）
- ❌ attention\_mechanism.md（下划线，禁止）
- ❌ Attention Mechanism.md（空格，禁止）
- ❌ 注意力机制.md（中文文件名，禁止 —— 见规则 2）

规则 2：文件名只使用 ASCII 字符

原因：部分 Agent 和工具链对非 ASCII 文件名处理不稳定。

中文知识点的处理方式：文件名使用英文 kebab-case 音译或语义翻译，title 字段填写中文原名。

示例：知识点「注意力机制」，文件名：attention-mechanism.md，title: "注意力机制"，aliases: \["Attention Mechanism", "注意力机制"]。

规则 3：文件名与 title 字段保持语义一致

文件名是 title 的机器可读版本。

- ✅ title: "React Hooks 工作流" → react-hooks-workflow\.md
- ❌ title: "React Hooks 工作流" → rh-workflow\.md（缩写，禁止）

规则 4：文件名不包含日期（特殊文件除外）

日期信息放在 frontmatter 的 created /updated 字段。

- ❌ attention-mechanism-2026-05.md
- ✅ attention-mechanism.md（frontmatter 中有 created: 2026-05-31）

  例外：outputs/ 中的 lint 报告文件名包含日期（见 7.2.4）。

规则 5：文件名长度不超过 60 个字符（不含 .md 后缀）

超过时，保留最关键的语义词，去掉修饰词。

- ❌ introduction-to-the-core-concepts-of-attention-mechanism.md
- ✅ attention-mechanism-core-concepts.md

规则 6：同一 wiki/ 下不允许存在同名文件（即使在不同子目录）

原因：\[\[wikilinks]] 只用文件名定位，同名文件会造成歧义。

冲突处理：在文件名末尾加语义后缀区分。

示例：wiki/concepts/transformer.md（Transformer 架构）、wiki/tools/transformer-library.md（Hugging Face Transformers 库）。

#### 7.2.2 各目录文件命名规则

【wiki/\_inbox/ 和各知识域文件夹】

格式：\[语义名称].md

示例：attention-mechanism.md、react-hooks-workflow\.md、andrej-karpathy.md、anthropic.md、database-migration-decision.md

【wiki/sources/】

格式：与 raw/ 中原始文件名保持完全一致

原因：便于追溯，一眼看出对应哪个原始资料。

示例：raw/articles/attention-paper.md → wiki/sources/attention-paper.md；raw/papers/bert-2018.md → wiki/sources/bert-2018.md

【wiki/outputs/】

格式：\[输出类型]-\[主题]-\[YYYY-MM-DD].md

类型前缀：lint- 健康检查报告、query- 查询结果归档、compare- 对比分析、analysis- 深度分析

示例：lint-2026-05-31.md、query-attention-vs-rnn-2026-05-31.md、compare-gpt4-vs-claude3-2026-05-20.md、analysis-transformer-evolution-2026-05-15.md

【wiki/ 根目录特殊文件】

固定名称，不可更改：\_index.md、\_log.md、\_graph.md（下划线前缀，与知识域文件夹区分）

#### 7.2.3 禁止使用的字符和模式

禁止字符：空格、中文、日文、韩文等非 ASCII 字符；特殊符号：! @ # $ % ^ & \* () + = \[] { } | \ ; ' " , < > ? /；连续连字符：attention--mechanism（双连字符）；首尾连字符：-attention-mechanism- 或 attention-mechanism-。

禁止模式：以数字开头：1-attention.md（易与序号混淆）；纯缩写：llm.md、rag.md（歧义大，gpt.md、bert.md 等专有名词缩写除外）；版本号后缀：attention-v2.md（版本信息放 frontmatter）；temp /draft/new /test 等临时性前缀，❌ temp-attention.md，✅ 直接用正式名称，draft 状态在 frontmatter 的 status 字段标注。

### 7.3 文件夹命名规则

规则：与文件命名相同，使用 kebab-case，ASCII 字符。

固定文件夹（不可重命名）：wiki/\_inbox/ 暂存区、wiki/sources/ 来源摘要、wiki/outputs/ 输出归档、raw/articles/、raw/papers/、raw/notes/、raw/projects/。

知识域文件夹命名指引：使用名词复数形式（表示 "这类知识的集合"），✅ concepts/ ❌ concept/、✅ tools/ ❌ tool/、✅ workflows/ ❌ workflow/、✅ people/ ❌ persons/、✅ decisions/ ❌ decision-records/；语义要清晰，不用缩写，✅ machine-learning/ ❌ ml/；新建域文件夹时，LLM 必须在 \_index.md 中登记后才能使用。

### 7.4 wikilinks 命名规则

规则 1：普通知识点页面的 \[\[wikilinks]] 使用文件名（不含 .md 后缀，不含路径），✅ \[\[attention-mechanism]]，❌ \[\[wiki/concepts/attention-mechanism.md]]、❌ \[\[concepts/attention-mechanism]]。

规则 2：显示文本与文件名不同时，使用管道符，格式：\[\[文件名|显示文本]]，管道符两侧不加空格，示例：\[\[attention-mechanism|注意力机制]]、\[\[andrej-karpathy|Karpathy]]。

规则 3：引用来源摘要页时，`sources/` 是唯一允许的路径前缀，✅ \[\[sources/attention-paper]]，❌ \[\[attention-paper]]（与知识点页面混淆），❌ \[\[wiki/sources/attention-paper.md]]。

规则 4：wikilinks 中的文件名必须与实际文件名完全一致（区分大小写），✅ \[\[attention-mechanism]]，❌ \[\[Attention-Mechanism]]、❌ \[\[attention\_mechanism]]。

### 7.5 frontmatter 字段命名规则

规则：所有 frontmatter 字段名使用 kebab-case，✅ source-count: 2、✅ original-path: "raw/..."，❌ sourceCount: 2、❌ source\_count: 2。

字段值的格式规则：日期字段严格使用 ISO 8601 格式 YYYY-MM-DD，✅ created: 2026-05-31，❌ created: 2026/05/31、❌ created: May 31, 2026；字符串字段使用双引号包裹，✅ title: "注意力机制"，❌ title: 注意力机制；列表字段即使只有一项也使用列表格式，✅ sources: - "\[\[sources/paper-001]]"，❌ sources: "\[\[sources/paper-001]]"；空列表使用 \[]，不留空，✅ contradicts: \[]，❌ contradicts:、❌ contradicts: null。

### 7.6 \_log.md 条目命名规则

格式（严格遵守，便于 grep 解析）：## \[YYYY-MM-DD] 操作类型 | 标题

操作类型枚举（固定，不可自定义）：ingest 摄入原始资料、query 查询操作、lint 健康检查、reorganize 域重组（新建文件夹 + 迁移文件）。

示例：## \[2026-05-31] ingest | attention-paper.md、## \[2026-05-31] query | 注意力机制与 RNN 的对比、## \[2026-05-31] lint | 全量健康检查、## \[2026-05-31] reorganize | 新建域 concepts/。

grep 解析命令：grep "^## \[" wiki/\_log.md（所有条目）、grep "^## \[" wiki/\_log.md | tail -10（最近 10 条）、grep "ingest" wiki/\_log.md（所有摄入记录）。

## §8 质量与置信度规则

### 8.1 设计原则

Wiki 的核心价值在于可信赖性。一个充满不确定内容却不加标注的 Wiki，比没有 Wiki 更危险 —— 它会让 Agent 以高置信度输出错误答案。

本节规则的目标：让每个知识点都清楚地知道 "自己有多可靠"；让 Agent 在引用时能判断 "这条信息值得多大的权重"；让人类在审阅时能快速识别 "哪里需要关注"。

### 8.2 置信度（confidence）四级定义

**confidence: high**

适用条件（必须全部满足）：有 ≥2 个独立来源印证（source-count ≥ 2）；各来源之间无矛盾（contradicts 字段为空）；最近一次来源更新距今 ≤6 个月；内容是事实性陈述，而非推断或预测。

Agent 引用时的行为：可以直接引用，无需加注不确定性说明。

**confidence: medium**

适用条件（满足任一）：只有 1 个来源（source-count = 1），但来源质量为 high；有 ≥2 个来源，但存在轻微分歧（非根本性矛盾）；内容包含部分推断，但推断有明确依据。

Agent 引用时的行为：可以引用，建议加注："根据现有资料……"；Lint 时重点关注，检查是否有新来源可以提升置信度。

**confidence: low**

适用条件（满足任一）：只有 1 个来源，且来源质量为 medium 或 low；内容主要基于推断，缺乏直接证据；来源距今 >6 个月，且领域变化较快（如 AI 工具类）；存在未解决的矛盾（contradicts 字段非空）。

Agent 引用时的行为：引用时必须加注："此信息置信度较低，建议验证"；不得作为其他知识点的唯一依据。

**confidence: speculative**

适用条件（满足任一）：没有来源支撑（source-count = 0）；内容是假设、猜测或预测；来源本身明确标注为 "未经验证"。

Agent 引用时的行为：引用时必须明确标注："以下为推测性内容，未经验证"；Lint 时优先检查，寻找可以升级或删除的依据。

特殊规则：speculative 页面必须在正文开头添加警示块：

> ⚠️ **推测性内容**：本页面内容缺乏充分来源支撑，仅作假设记录。引用前请验证。推测原因：\[说明为什么建立这个页面但没有来源]

### 8.3 置信度计算规则

置信度由 LLM 在 Ingest 时综合判断，依据以下四个维度：

维度 1：来源数量。0 个来源 → 强制 speculative；1 个来源 → 最高 medium（来源质量 high 时可为 medium）；2 个来源 → 最高 high（需无矛盾）；≥3 个来源 → 可为 high（即使有轻微分歧）。

维度 2：来源质量（source-quality 字段）。high 权威来源、经过同行评审、论据充分；medium 可信来源，未经严格验证；low 个人观点、未经证实。来源质量影响：1 个 low 质量来源 → 最高 low；1 个 medium 质量来源 → 最高 medium；1 个 high 质量来源 → 最高 medium（单一来源上限）；2 个 high 质量来源 → 可为 high。

维度 3：矛盾状态。contradicts 非空 → 置信度最高降为 low（矛盾未解决时，不能声称高置信度）。

维度 4：内容性质。事实性陈述 → 按上述规则正常评估；推断性内容 → 在上述结果基础上降一级；预测性内容 → 最高 low。

置信度综合判断示例：

案例 1：来源数量 2 个、来源质量均为 high、无矛盾、事实性陈述 → confidence: high。

案例 2：来源数量 1 个、来源质量 high、无矛盾、事实性陈述 → confidence: medium（单一来源上限）。

案例 3：来源数量 3 个、来源质量均为 medium、存在轻微分歧、事实性陈述 → confidence: medium（有分歧，不能为 high）。

案例 4：来源数量 1 个、来源质量 low、无矛盾、推断性内容 → confidence: speculative（low 质量 + 推断，降两级）。

### 8.4 置信度的动态变化规则

#### 升级规则（置信度提升）

触发条件：Ingest 新来源时，新来源印证了现有知识点。

操作：1. 追加新来源并按 `sources` 实际长度重算 `source-count`；2. 重新评估 confidence（按 8.3 规则）；3. 如果 confidence 提升，更新字段并在正文末尾注明："（置信度已从 \[旧级别] 升级为 \[新级别]，新增来源：\[\[sources/xxx]]）"。

#### 降级规则（置信度下降）

触发条件 A：Ingest 新来源时，新来源与现有内容矛盾。

操作：1. 在 contradicts 字段添加矛盾方；2. confidence 降为 low（有未解决矛盾时的上限）；3. 在「矛盾说明」章节记录矛盾内容。

触发条件 B：Lint 时发现来源已过时（领域变化快的知识点）。判断标准：AI / 工具类知识点：updated 距今 >3 个月 → 降一级；理论 / 概念类知识点：updated 距今 >12 个月 → 降一级；历史 / 事实类知识点：不自动降级（历史不会变）。

操作：1. confidence 降一级；2. 在 frontmatter 添加：staleness-warning: "来源可能已过时，建议验证"。

#### 矛盾解决后的恢复规则

当 contradicts 中的矛盾被人工解决后：1. 从 contradicts 字段移除已解决的矛盾方；2. 如果 contradicts 变为空，重新按 8.3 规则评估 confidence；3. 在 \_log.md 记录矛盾解决过程。

### 8.5 页面状态（status）规则

#### 8.5.1 状态字段统一规则

- `status` 是页面主状态，同一页面同一时间只能是 `active`、`draft`、`superseded`、`archived` 之一。
- 进入或退出任一非 active 状态时，必须同时处理四类内容：frontmatter 字段、正文开头提示块、`updated` 日期、`_log.md` 记录。
- 恢复 `active` 时，必须清除原状态对应的扩展字段和正文提示块；不得只改 `status` 字段。
- `staleness-warning` 不是 `status`，而是可与任一主状态并存的过时警告字段；添加或解除时同样要更新 `updated` 和 `_log.md`。

**status: active**（默认值，当前有效）

触发：新建页面时自动设置，无需特殊操作。

进入 active 的操作：

1. 将 `status` 设为 `active`。
2. 删除不再适用的状态扩展字段：`superseded-by`、`superseded-date`、`archived-date`、`archived-reason`。
3. 删除正文开头不再适用的状态提示块：草稿提示、已被取代提示、已归档提示。
4. 若同时解除过时状态，删除 `staleness-warning` 和正文过时提示块；否则保留仍然有效的过时警告。
5. 更新 `updated` 为当日日期，并在 `_log.md` 追加状态恢复记录。

**status: draft**

触发条件（满足任一）：页面内容不完整（缺少「定义」或「详细说明」章节）；confidence 为 speculative 且正文少于 100 字；Ingest 时判断信息不足以建立完整页面。

进入 draft 的操作：

1. 将 `status` 设为 `draft`。
2. 不添加额外 frontmatter 扩展字段。
3. 在正文开头添加提示块：> 📝 **草稿**：本页面内容不完整，待补充。缺失内容：\[说明缺少什么]。
4. 更新 `updated` 为当日日期，并在 `_log.md` 追加状态变更记录。

退出 draft 的操作：

1. 补齐缺失章节或关键内容。
2. 将 `status` 改为 `active`，或在同时满足归档/取代条件时改为对应状态。
3. 删除正文草稿提示块。
4. 更新 `updated` 为当日日期，并在 `_log.md` 追加草稿补全记录。

LLM 处理规则：Query 时可以引用 draft 页面，但必须注明 "内容不完整"；Lint 时列出所有 draft 页面，提示用户补充。

**status: superseded**

触发条件：有其他知识点在 supersedes 字段中引用了本页面。

进入 superseded 的操作（必须同时执行）：

1. 将本页面 `status` 改为 `superseded`。
2. 在 frontmatter 添加 `superseded-by: "[[新知识点]]"`、`superseded-date: YYYY-MM-DD`。
3. 在正文开头添加警示块：> ⛔ **已被取代**：本页面内容已过时。请参阅：\[\[新知识点]]（取代日期：YYYY-MM-DD）保留原因：\[说明为什么保留而非删除，如：历史记录价值]。
4. 保留原有正文内容，不删除。
5. 更新 `updated` 为当日日期，并在 `_log.md` 追加取代关系记录。

退出 superseded 的操作（仅在人工确认取代关系撤销或判断错误时执行）：

1. 从新页面的 `relations.supersedes` 中移除本页面。
2. 将本页面 `status` 改为 `active`，或在同时满足归档/草稿条件时改为对应状态。
3. 删除 `superseded-by`、`superseded-date`。
4. 删除正文已被取代提示块。
5. 同步 `_graph.md` 的 `supersedes` 关系，更新双方 `updated`，并在 `_log.md` 追加撤销取代记录。

LLM 处理规则：Query 时不主动引用 superseded 页面，用户明确询问旧版本 / 历史时可引用并说明状态；Lint 时检查引用该页面的条目是否已更新。

重要原则：superseded 页面永不删除，用于保留历史演化记录。

**status: archived**

触发条件：项目已结束，相关知识点不再活跃；工具已停止维护，但信息有历史参考价值；人工明确标注归档。

进入 archived 的操作：

1. 将 `status` 改为 `archived`。
2. 在 frontmatter 添加 `archived-date: YYYY-MM-DD`、`archived-reason: "[归档原因]"`。
3. 在正文开头添加：> 📦 **已归档**：本页面内容不再活跃更新。归档原因：\[原因]（归档日期：YYYY-MM-DD）。
4. 更新 `updated` 为当日日期，并在 `_log.md` 追加归档记录。

退出 archived 的操作（仅在人工确认重新启用时执行）：

1. 将 `status` 改为 `active`，或在同时满足草稿/取代条件时改为对应状态。
2. 删除 `archived-date`、`archived-reason`。
3. 删除正文已归档提示块。
4. 更新 `updated` 为当日日期，并在 `_log.md` 追加取消归档记录。

LLM 处理规则：Query 时可以引用，但注明 "已归档内容"；Lint 时不将 archived 页面列为 "孤儿页面" 问题。

#### 8.5.2 过时警告（staleness-warning）规则

触发条件：Lint 或人工复核判定页面来源可能过时；该警告可与 `active`、`draft`、`superseded`、`archived` 任一主状态并存。

进入过时警告的操作：

1. 在 frontmatter 添加 `staleness-warning: "来源可能已过时，建议验证"`。
2. 按 §8.4 降低或重评 `confidence`。
3. 在正文开头、状态提示块之后添加：> ⚠️ **可能过时**：本页面来源可能已过时，引用前请验证。触发原因：\[说明原因]。
4. 更新 `updated` 为当日日期，并在 `_log.md` 或 Lint 报告中记录。

解除过时警告的操作：

1. 补充新来源、人工复核或确认内容仍有效。
2. 删除 `staleness-warning`。
3. 删除正文可能过时提示块。
4. 重算 `source-count` 和 `confidence`。
5. 更新 `updated` 为当日日期，并在 `_log.md` 追加解除过时记录。

### 8.6 来源质量（source-quality）评估规则

在创建 sources/ 摘要页时，LLM 必须评估原始来源的质量。

**high（高质量来源）**：满足以下 ≥2 条：经过同行评审（学术论文、技术规范）；来自权威机构或知名专家；有明确的数据、实验或论据支撑；发布时间近期（AI 领域 ≤1 年，其他领域 ≤3 年）；被其他高质量来源引用。示例：arXiv 论文、官方文档、知名机构报告。

**medium（中等质量来源）**：满足以下 ≥1 条，但不满足 high 条件：来自可信的个人博客或技术社区（如 HN、Medium 技术文章）；有一定论据但未经严格验证；信息可信但来源不够权威。示例：技术博客、Stack Overflow 高票回答、行业报告。

**low（低质量来源）**：满足以下任一：主要是个人观点，缺乏论据；来源不明或匿名；内容存在明显偏向性；发布时间过久（AI 领域 >2 年，其他领域 >5 年）。示例：社交媒体帖子、未注明来源的文章、过时文档。

### 8.7 质量红线（LLM 不得违反的硬性规则）

红线 1：来源必须可追溯。每个知识点页面的 sources 字段必须非空，唯一例外是 confidence: speculative 的页面（需注明原因）；禁止凭自身训练知识直接写入 wiki 且不注明来源，所有内容必须来自 raw/ 中的实际文件。

红线 2：矛盾必须显式记录，不得静默覆盖。禁止直接用新内容覆盖旧内容；需在 contradicts 字段、「矛盾说明」章节记录双方观点，等待人工裁决。

红线 3：superseded 页面不得删除。禁止删除被取代的知识点页面；仅标注状态、添加跳转链接，保留原文。

红线 4：\_log.md 只能追加，不能修改。禁止修改或删除历史记录，仅在文件末尾追加新记录。

红线 5：raw/ 目录不可写入。禁止在 raw/ 中创建或修改任何文件，raw/ 为只读事实基准。

红线 6：不得在未触发工作流时写入 wiki。禁止在普通对话中自动更新 wiki 页面；仅用户显式触发 Ingest / Query 归档 / Lint 修复时才可执行写入。

### 8.8 质量规则速查表

表格

| 场景               | 规则             | 操作                   |
| ---------------- | -------------- | -------------------- |
| 新建页面，无来源         | 强制 speculative | 添加警示块，说明推测原因         |
| 新建页面，1 个来源       | 最高 medium      | 正常建立，标注来源            |
| 新建页面，≥2 个来源无矛盾   | 可为 high        | 正常建立                 |
| 发现矛盾             | 降至 low         | 记录双方，等待裁决            |
| 矛盾解决             | 重新评估置信度        | 按 8.3 规则重算           |
| 新来源印证现有内容        | 可能升级置信度        | 重新评估，更新字段            |
| 知识点被新知识点取代       | 标记为 superseded | 添加警示块，保留原文           |
| 内容过时（AI 类 > 3 月） | 置信度降一级         | 添加 staleness-warning |
| 内容不完整            | 标记为 draft      | 添加草稿提示               |
| LLM 自身知识写入 wiki  | 严格禁止           | 必须依托 raw/ 来源         |

