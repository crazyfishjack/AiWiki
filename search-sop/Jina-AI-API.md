---
title: "Jina AI API 工具指南"
category: tool
tags: [jina, reader-api, reader-default, search-api, embeddings, rerank, deep-research, retrieval, readerlm-v2, anti-hallucination, cost-aware, primary-reader, v2.1]
sources:
  - https://docs.jina.ai/
  - https://arxiv.org/abs/2503.01151
  - https://seodiff.io/research/hallucination-risk
  - https://arxiv.org/pdf/2511.23119v2
  - wiki/tools/Windows-API-Call-Guide.md
related:
  - "[[Deep-Research-Methodology]]"
  - "[[Tavily-Search-API]]"
  - "[[Exa-Neural-Search-API]]"
  - "[[Retrieval-Tools-Comparison]]"
  - "[[Windows-API-Call-Guide]]"
  - "[[Anti-Hallucination-Engineering]]"
last_compiled: 2026-06-16
confidence: high
language: zh-CN+en
discovery:
  one_liner: "四类 Jina API 完整调用指南；Reader 默认模式=v2.1 精读主力（确定性/按需/失败降级 Firecrawl），readerlm-v2 仅学术；含幻觉路由与成本"
  topic_cluster: ai-concepts
  load_when:
    - "需要将 URL 转为 LLM 可读 Markdown 或调用 Jina Reader/Search/Embeddings/Reranker 时"
    - "Deep Research 工作流中选择精读工具或对候选文档做 Reranker 重排序时"
    - "排查 readerlm-v2 返回内容膨胀、插入原文不存在内容等幻觉问题时"
    - "确认 Jina Reader 默认模式 vs readerlm-v2 的区别、精读主力定位或按 token 计费成本时"
  key_outputs:
    - "Reader / Search / Embeddings / Reranker 四类 API 的端点、关键 Header 与可运行代码示例"
    - "Reader 默认模式（纯规则，精读主力）vs readerlm-v2（LLM，学术专用）辨析与成本差异"
    - "readerlm-v2 幻觉根因、ACRI 结构评分量化数据及 URL 类型路由决策表"
    - "Deep Research 三场景（精读主力+Firecrawl 降级/补充搜索/重排序）配置与 Reader vs Search 选择表"
  estimated_tokens: 2500
  sections:
    - heading: "What It Is / 是什么"
      one_liner: "Jina AI 四类核心 API 简介及其 v2.1 SOP 定位（Reader 默认模式=精读主力 + 学术 readerlm-v2 + Reranker）"
      lines: [4, 18]
      tokens: 250
    - heading: "API 架构 / Architecture"
      one_liner: "四类 API 端点对照表与 Bearer Token 认证方式"
      lines: [20, 36]
      tokens: 150
    - heading: "Reader API (`r.jina.ai`) 详解"
      one_liner: "Reader API 基本用法、全部关键 Header 说明及高质量提取标准配置"
      lines: [38, 85]
      tokens: 400
    - heading: "Search API (`s.jina.ai`) 详解"
      one_liner: "Search API 用法、站内搜索 X-Site 参数及请求体参数说明"
      lines: [87, 118]
      tokens: 250
    - heading: "Embeddings API 详解"
      one_liner: "最新五款 Embeddings 模型参数对比与 Python 调用示例"
      lines: [120, 153]
      tokens: 250
    - heading: "Reranker API 详解"
      one_liner: "四款 Reranker 模型选型表与候选文档重排序调用示例"
      lines: [155, 182]
      tokens: 200
    - heading: "⚠️ readerlm-v2 幻觉风险与 URL 类型路由"
      one_liner: "readerlm-v2「翻译」设计导致幻觉的根因、ACRI 量化数据、URL 路由决策表及检测信号"
      lines: [184, 227]
      tokens: 450
    - heading: "与竞品对比（2026）"
      one_liner: "Jina/Firecrawl/Crawl4AI/Trafilatura 幻觉风险与中文站适用性对比及 v2.1 SOP 立场（Jina 默认精读主力、Firecrawl 降级）"
      lines: [229, 248]
      tokens: 220
    - heading: "Deep Research 工作流中的使用策略"
      one_liner: "精读主力(默认模式)+Firecrawl 降级/补充搜索/重排序三场景配置 + Reader vs Search 情景选择速查表"
      lines: [250, 296]
      tokens: 400
---

# Jina AI API 工具指南

## What It Is / 是什么

Jina AI 是一个面向 LLM 的 **搜索基础设施工具集（Search Foundation API）**，提供四类核心能力：
1. **Reader API** (`r.jina.ai`) — 将任意 URL 转换为 LLM 友好的 Markdown 格式内容
2. **Search API** (`s.jina.ai`) — 搜索网页并返回 LLM 优化格式的结果集
3. **Embeddings API** — 生成文本/图像/代码的语义向量
4. **Reranker API** — 对搜索结果按相关性重排序

**在 Deep Research 工作流中的定位（v2.1 SOP 更新 2026-06-16）**：Jina 是**精读主力（Reader 默认模式）+ 学术 PDF（readerlm-v2）+ Reranker**：① **所有普通页面精读主力**——Reader 默认模式走 turndown + readability 纯规则提取，确定性、零生成式幻觉、按 token 计费（失败再降级 Firecrawl）；② arXiv / 学术期刊 / IEEE 等结构化学术页面精读（**显式开** readerlm-v2，吃其学术结构理解、容忍 3x token 与幻觉风险）；③ 候选文档超量（>15篇）时的 Reranker 重排序。

> ⚠️ **v2.1 修正**：v2 曾把 Jina 降为「学术 PDF 专用」、精读交给 Firecrawl，理由是 readerlm-v2 幻觉——这是把 **Reader 默认模式**（纯规则、安全）与可选的 **readerlm-v2**（LLM 重写层、有幻觉）混为一谈的论据滑坡。默认模式精读既安全又更省（按需 token vs 月订阅），故 v2.1 升回精读主力。

**凭据位置**：见 `retrieval-api-keys.md`（根目录）

---

## API 架构 / Architecture

| API | Endpoint | 最适合 |
|-----|----------|--------|
| Reader | `POST https://r.jina.ai/` | 已知 URL → 提取完整页面内容 |
| Search | `POST https://s.jina.ai/` | 关键词 → 获取搜索结果集（含内容） |
| Embeddings | `POST https://api.jina.ai/v1/embeddings` | 文本/图片 → 语义向量 |
| Reranker | `POST https://api.jina.ai/v1/rerank` | Query + 候选列表 → 相关性排序 |

### 认证方式
```bash
curl https://r.jina.ai/https://example.com \
  -H "Authorization: Bearer $JINA_API_KEY" \
  -H "Accept: application/json"
```

---

## Reader API (`r.jina.ai`) 详解

### 基本用法

```bash
# GET 方式（最简单）
curl https://r.jina.ai/https://example.com \
  -H "Authorization: Bearer $JINA_API_KEY"

# POST 方式（支持更多参数）
curl https://r.jina.ai/ \
  -H "Authorization: Bearer $JINA_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{"url": "https://example.com"}'
```

### 关键请求头（Headers）

| Header | 值 | 用途 |
|--------|-----|------|
| `X-Return-Format` | `markdown` / `html` / `text` / `screenshot` | 返回格式，默认 markdown |
| `X-Engine` | `browser` / `direct` / `cf-browser-rendering` | `browser` 质量最高；`direct` 速度最快 |
| `X-Timeout` | 秒数（如 `30`） | 页面加载超时 |
| `X-Target-Selector` | CSS 选择器 | 聚焦页面特定元素 |
| `X-Remove-Selector` | CSS 选择器 | 排除页面特定元素（如导航/页脚）|
| `X-With-Links-Summary` | `true` / `all` | 在响应末尾附加链接列表 |
| `X-With-Images-Summary` | `true` / `all` | 在响应末尾附加图片列表 |
| `X-No-Cache` | `true` | 绕过缓存，获取最新内容 |
| `X-Token-Budget` | Token 数 | 限制最大输出 Token |
| `X-Respond-With` | `readerlm-v2` | ⚠️ AI 后处理模型（见下方幻觉风险章节）；默认**不加**，仅对学术结构化页面可选启用 |

### 最佳实践

```bash
# 高质量提取（JS 渲染页面）
curl https://r.jina.ai/ \
  -H "Authorization: Bearer $JINA_API_KEY" \
  -H "X-Engine: browser" \
  -H "X-Return-Format: markdown" \
  -H "X-Remove-Selector: nav,footer,aside" \
  -H "Accept: application/json" \
  -d '{"url": "https://target-page.com"}'
```

> 响应内容在 `response["data"]["content"]` 字段中

---

## Search API (`s.jina.ai`) 详解

### 基本用法

```bash
curl https://s.jina.ai/ \
  -H "Authorization: Bearer $JINA_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{"q": "latest AI research 2025"}'
```

### 关键请求头

| Header | 说明 |
|--------|------|
| `X-Site` | 限制在某域名内搜索（站内搜索） |
| `X-No-Cache` | `true` 获取实时数据 |
| `X-Return-Format` | `markdown` / `html` / `text` |
| `X-Engine` | `browser`（最佳质量）/ `direct`（最快速度）|

### 请求体参数

| 参数 | 说明 |
|------|------|
| `q` | 搜索词（必填）|
| `gl` | 国家代码（两字母，如 `CN`）|
| `hl` | 语言代码（如 `zh`）|
| `num` | 返回结果数（增加可能影响延迟）|
| `page` | 分页偏移 |

---

## Embeddings API 详解

### 最新模型（2026年4月）

| 模型 | 参数量 | 向量维度 | 上下文 | 特点 |
|------|--------|---------|--------|------|
| `jina-embeddings-v5-text-small` | 677M | 1024 | 32K | 基于 Qwen3-0.6B，多语言，Matryoshka |
| `jina-embeddings-v5-text-nano` | 239M | 768 | 8K | 基于 EuroBERT，低延迟/边缘部署 |
| `jina-embeddings-v4` | 3.8B | 2048 | — | 多模态（文本+图片+PDF）|
| `jina-embeddings-v3` | 570M | 1024 | — | 100+ 语言，通用文本 |
| `jina-clip-v2` | 885M | 1024 | — | 跨模态文本-图像检索 |

### 基本用法

```python
import requests

response = requests.post(
    "https://api.jina.ai/v1/embeddings",
    headers={
        "Authorization": f"Bearer {JINA_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    },
    json={
        "model": "jina-embeddings-v5-text-small",
        "input": ["text to embed"],
        "task": "retrieval.passage",  # retrieval.query / retrieval.passage / text-matching
        "normalized": True
    }
)
```

---

## Reranker API 详解

### 模型选择

| 模型 | 参数量 | 特点 |
|------|--------|------|
| `jina-reranker-v3` | 0.6B | 最新，causal self-attention，多语言 |
| `jina-reranker-m0` | 2.4B | 多模态（文本+图像）|
| `jina-reranker-v2-base-multilingual` | 278M | 轻量多语言 |
| `jina-colbert-v2` | 560M | ColBERT 风格，多向量匹配 |

### 用法

```python
response = requests.post(
    "https://api.jina.ai/v1/rerank",
    headers={"Authorization": f"Bearer {JINA_API_KEY}", "Accept": "application/json"},
    json={
        "model": "jina-reranker-v3",
        "query": "what is deep research?",
        "documents": ["doc1 text", "doc2 text", "doc3 text"],
        "top_n": 3,
        "return_documents": True
    }
)
```

---

## ⚠️ readerlm-v2 幻觉风险与 URL 类型路由

> **来源**：arxiv 2503.01151（官方论文）+ SEODiff 2025 + 实测踩坑 2026-04-30
> **结论**：默认关闭 `X-Respond-With: readerlm-v2`；仅对学术结构化页面可选开启。

### 根因：「翻译」而非「提取」

readerlm-v2（2025年1月发布，1.5B 参数，基于 Qwen2.5-1.5B-Instruct）在设计上将
HTML→Markdown 定义为**语言翻译**而非忠实提取。

> *"We treat HTML-to-Markdown as true translation, not simple copy."*  — arxiv 2503.01151

语言模型会在转换过程中**补全/插值语义**——对结构化的学术论文这是优势（生成更干净的 Markdown），
对结构松散的中文内容聚合站这就是幻觉的来源（凭语义补全插入原文没有的内容）。

### 结构噪声量化数据（SEODiff 2025）

| HTML 结构质量（ACRI 评分）| 相对幻觉率 |
|--------------------------|-----------|
| ACRI ≥ 80（结构良好）     | 基准 1x    |
| ACRI 40–80（中等）        | ~2x        |
| ACRI < 40（结构差）       | **3.5x**   |

中文内容聚合站（搜狐/百家号/新闻站）普遍 ACRI < 40 → 直接落入 3.5x 高风险区。
arXiv、GitHub README 等学术技术内容 ACRI 普遍 ≥ 80 → 风险可接受。

### URL 类型路由表（决策速查）

| URL 类型 | `X-Respond-With: readerlm-v2` | 原因 |
|---------|-------------------------------|------|
| arXiv / 学术期刊 / IEEE | ✅ 可选开启 | 结构化，ACRI 高，风险低 |
| GitHub README / 官方技术文档 | ❌ 默认关闭 | 默认 reader 已足够忠实 |
| 政府官网 / `.edu.cn` / `.gov.cn` | ❌ 关闭 | 格式简单，无需 AI 后处理 |
| 新华网 / 人民网 / 各类新闻站 | ❌ 关闭 | 内容被改写风险高 |
| 搜狐 / 百家号 / 内容聚合 | ❌❌ **禁止** | 实测：插入 20+ 条原文不存在的内容 |

### 幻觉检测信号

精读后若出现以下情况，疑似 readerlm 幻觉，用内置 Web Browsing 比对原页面：
- 返回字数超出预期 **150%+**（内容膨胀）
- 出现与主题不相关的列表条目
- 数字/日期细节与其他来源矛盾

---

## 与竞品对比（2026）

> 来源：Firecrawl vs Jina 对比（firecrawl.dev）+ Apify vs Firecrawl vs Jina（use-apify.com）+ 行业综述

| 工具 | 核心定位 | 幻觉风险 | 中文站适用性 | 适用场景 |
|------|---------|---------|-------------|---------|
| **Jina Reader**（默认） | 单页精读主力，API 最简 | 低（不开 readerlm，纯规则）| ✅ 可用 | **v2.1 SOP 精读层主力** |
| **Jina + readerlm-v2** | 学术结构化内容 | 高（中文站）| ❌ 禁用 | 仅限 arXiv 等学术页面 |
| **Firecrawl** | 多页爬取流水线，企业级 | 低（无 LLM 后处理）| ✅ 较好 | 需要批量抓取、站点地图时 |
| **Crawl4AI** | 开源自托管，Python 原生 | 低 | ✅ 较好 | 成本敏感 / 自托管需求 |
| **Trafilatura** | 纯启发式提取，无 LLM | 极低（零生成）| ✅ 最忠实 | 最高保真需求，不依赖 JS 渲染 |
| **Dripper**（研究阶段）| 约束序列标注（keep/remove）| 极低（非生成式）| — | 理论上最优，尚未产品化 |

**当前 SOP 立场（v2.1，2026-06-16）**：四工具 SOP 以 **Jina Reader 默认模式作为普通页面精读主力**（按需计费、确定性、零生成式幻觉），
失败（取空/超时/JS 重渲染/反爬）时**降级 Firecrawl `/scrape`**（Playwright 兜底）；arXiv/学术期刊才显式开 `readerlm-v2`。
中文内容聚合站（搜狐/百家号等 ACRI<40）仍**禁用 readerlm-v2**，但用 Jina **默认模式**精读无虞；必要时 Tavily `raw_content` 交叉验证。

> 注：v2.0 曾把 Jina 降为学术专用、精读交 Firecrawl，已于 v2.1 修正回此立场（见 `[[Three-Tool-Retrieval-SOP]]` v2.1 变更记录）。

---

## Deep Research 工作流中的使用策略

### 场景一：精读目标页面（精读主力路径）
```
Tavily/Exa → 获取 top URL 列表
Jina r.jina.ai（默认模式，不开 readerlm-v2）→ 对每个重要 URL 提取完整 Markdown ← 主力
  └─ 失败（取空/超时/JS 重渲染/反爬）→ 降级 Firecrawl /scrape（Playwright 兜底）
arXiv/学术期刊 → Jina r.jina.ai + X-Respond-With:readerlm-v2（学术专用）
```

### 场景二：补充搜索覆盖
```
当 Tavily 搜索结果不足时 → Jina s.jina.ai 补充搜索
尤其适合：需要限制在某一域名内搜索（X-Site 参数）
```

### 场景三：结果重排序
```
多工具搜索后有大量候选文档 → Jina Reranker 按相关性重排
输出 top-N 精选结果给 LLM 综合
```

### 质量优先标准配置

**Reader（始终使用认证 + browser 引擎）**：
```bash
# 每次调用都使用这套配置（readerlm-v2 默认不加，见幻觉风险章节）
Headers:
  X-Engine: browser           # 完整 JS 渲染
  # X-Respond-With: readerlm-v2  ← 默认注释掉；仅 arXiv/学术期刊可启用
  X-Remove-Selector: nav,footer,aside,script,style
  X-With-Links-Summary: true  # 附加出链，便于发现延伸来源
  X-Return-Format: markdown
  Authorization: Bearer {KEY}
```

### 何时选 Reader vs Search

| 情况 | 用哪个 |
|------|--------|
| 已知目标 URL，需要提取完整内容 | `r.jina.ai` Reader（认证 + browser）|
| 不知道哪些 URL 相关，需要发现 | `s.jina.ai` Search |
| JS 渲染的复杂页面 | `r.jina.ai` + `X-Engine: browser`（已是默认）|
| 语义搜索（非关键词） | `s.jina.ai` |
| Jina 默认模式取空/失败 | 降级 `firecrawl_scrape(URL)`（Playwright/反爬兜底）|

---

## Sources / 来源
- [Jina AI Meta-Prompt / LLM Guide](https://docs.jina.ai/) — 官方 API 完整文档（v13，2026年）
- [ReaderLM-v2 官方论文](https://arxiv.org/abs/2503.01151)（arxiv 2503.01151，2025年3月）— 「翻译」设计哲学，Draft-Refine-Critique 三阶段训练流程
- [SEODiff: Hallucination Risk Whitepaper](https://seodiff.io/research/hallucination-risk)（2025）— ACRI 结构质量评分与幻觉率 3.5x 量化数据
- [Dripper: Token-Efficient Content Extraction](https://arxiv.org/pdf/2511.23119v2)（arxiv 2511.23119，2025）— 约束序列标注替代生成式提取的理论方案
- `wiki/tools/Windows-API-Call-Guide.md` — 陷阱二：中文内容站 readerlm-v2 幻觉实测（2026-04-30）
