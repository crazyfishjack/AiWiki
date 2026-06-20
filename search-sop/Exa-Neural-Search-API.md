---
title: "Exa Neural Search API 工具指南"
category: tool
tags: [exa, neural-search, semantic-search, deep-research, retrieval, academic]
sources:
  - https://docs.exa.ai/reference/getting-started
  - https://docs.exa.ai/docs/reference/search
  - https://docs.exa.ai/docs/reference/search-api-guide
related:
  - "[[Deep-Research-Methodology]]"
  - "[[Tavily-Search-API]]"
  - "[[Jina-AI-API]]"
  - "[[Retrieval-Tools-Comparison]]"
  - "[[Exa-Research-Endpoint]]"
last_compiled: 2026-04-29
confidence: high
language: zh-CN+en
discovery:
  one_liner: "配置 Exa 神经搜索 API：搜索类型选择、参数配置、五类场景代码示例及与 Tavily/Jina 的组合策略"
  topic_cluster: ai-concepts
  load_when:
    - "需要用 Exa API 搜索学术论文、公司或人物信息时"
    - "设计 Deep Research 工作流需要选择语义搜索工具时"
    - "对比 Exa / Tavily / Jina 并决定各自分工时"
  key_outputs:
    - "六种搜索类型（auto/instant/fast/deep-lite/deep/deep-reasoning）的速度与适用场景对比"
    - "完整 /search 端点参数表及 highlights vs full-text 内容提取选择策略"
    - "质量优先、结构化研究、学术、公司人物、新闻五类场景的可直接复用 Python 代码"
    - "Exa / Tavily / Jina 三工具分工及 Stage 1-3 并行组合调用策略"
    - "2026年4月各操作单价速查表（Neural/Deep/Deep-Reasoning/Contents）"
  estimated_tokens: 1650
  sections:
    - heading: "What It Is / 是什么"
      one_liner: "Exa 神经语义搜索五大端点及在 Deep Research 工作流中的定位"
      lines: [4, 21]
      tokens: 200
    - heading: "API 架构 / Architecture"
      one_liner: "Base URL 与 x-api-key 认证方式（非 Bearer）示例"
      lines: [23, 39]
      tokens: 150
    - heading: "/search 端点详解"
      one_liner: "搜索类型、内容类型、类别过滤及完整参数表速查"
      lines: [41, 96]
      tokens: 500
    - heading: "Best Practices / 最佳实践"
      one_liner: "五类场景（质量优先/结构化/学术/公司人物/新闻）可直接运行的 Python 代码"
      lines: [98, 200]
      tokens: 550
    - heading: "定价参考（2026年4月）"
      one_liner: "Neural/Deep/Deep-Reasoning/Contents 各操作单价速查"
      lines: [202, 214]
      tokens: 100
    - heading: "与其他工具的对比定位"
      one_liner: "Exa/Tavily/Jina 强弱项对比及 Stage 1-3 并行组合调用策略"
      lines: [216, 238]
      tokens: 200
---

# Exa Neural Search API 工具指南

## What It Is / 是什么

Exa 是一家总部位于旧金山的研究实验室，致力于构建"完美搜索"。与传统关键词搜索不同，Exa 使用**神经网络/语义嵌入**来理解搜索意图，找到真正与查询含义匹配的内容。

**核心定位**：**"为 AI 而生的搜索引擎（Search engine made for AIs）"**

**五大核心能力**：
1. `/search` — 神经搜索，找到最相关的网页
2. `/contents` — 提取搜索结果的干净解析内容
3. `/findsimilar` — 基于给定链接找到语义相似页面
4. `/answer` — 直接回答问题（含引用）
5. ~~`/research`~~ — ⚠️ **已废弃（2026-05-01）**，功能已整合进 `/search` 的 `deep-reasoning` 类型。历史文档及迁移说明见 [[Exa-Research-Endpoint]]。

**在 Deep Research 工作流中的定位**：Exa 是**语义精准层**——特别适合发现学术论文、技术内容、特定公司/人物信息，语义理解能力强于关键词匹配型搜索引擎。

**凭据位置**：见 `retrieval-api-keys.md`（根目录）

---

## API 架构 / Architecture

### Base URL
```
https://api.exa.ai
```

### 认证方式
```bash
# 注意：Exa 使用 x-api-key header，而非 Authorization Bearer
curl -X POST 'https://api.exa.ai/search' \
  -H 'x-api-key: YOUR-EXA-API-KEY' \
  -H 'Content-Type: application/json' \
  -d '{"query": "your query here"}'
```

---

## `/search` 端点详解

### 搜索类型（type）— 核心参数

| 类型 | 速度 | 最适合 |
|------|------|--------|
| `auto` | ~1s | 智能选择 | 仅用于快速预查 |
| `instant` | ~200ms | 实时应用 | ❌ 质量优先时不用 |
| `fast` | ~450ms | 速度优先 | ❌ 质量优先时不用 |
| `deep-lite` | 2-10s | 轻量综合 | 次选 |
| `deep` | 5-60s | 复杂多步推理 | 备选 |
| **`deep-reasoning`** | **10-60s** | **最强推理** | **✅ 默认首选** |

> **Deep Search 类型特点**：`deep`/`deep-reasoning`/`deep-lite` 支持返回综合化的结构化输出（`output_schema`），适合 Deep Research 的 Synthesis 阶段。

### 内容类型（contents）

| 类型 | Token 效率 | 说明 |
|------|-----------|------|
| **Highlights** | **10x 高效** | 只提取与查询最相关的片段，推荐 4000 字符 |
| **Full text** | 完整 | 完整页面文本，需要全面性时使用 |

> **强烈推荐**：大多数场景使用 `highlights`（4000 字符），Token 成本仅为全文的 1/10。

### 类别过滤（category）

| 类别 | 数据规模 | 最适合 |
|------|---------|--------|
| `research paper` | 100M+ 全文论文 | 学术研究 |
| `news` | — | 时事新闻 |
| `company` | 50M+ 公司页面 | 企业信息 |
| `people` | 1B+ 人物信息 | 人物查询（支持 LinkedIn）|
| `personal site` | — | 博客/个人页面 |
| `financial report` | — | SEC 文件/财报 |

### 完整参数列表

| 参数 | 类型 | 说明 |
|------|------|------|
| `query` | string | **必填**，搜索查询 |
| `type` | enum | 搜索类型（见上表）|
| `category` | enum | 内容类别过滤 |
| `numResults` | int | 结果数，默认 10，最多 100 |
| `includeDomains` | string[] | 限定域名（最多 1200）|
| `excludeDomains` | string[] | 排除域名（最多 1200）|
| `startPublishedDate` | ISO 8601 | 发布时间起始 |
| `endPublishedDate` | ISO 8601 | 发布时间截止 |
| `startCrawlDate` | ISO 8601 | 爬取时间起始 |
| `endCrawlDate` | ISO 8601 | 爬取时间截止 |
| `userLocation` | string | 用户位置（两字母国家代码）|
| `contents` | object | 内容提取配置（highlights/text）|
| `outputSchema` | object | JSON Schema，用于结构化输出 |
| `systemPrompt` | string | 指导综合输出的系统提示 |
| `stream` | bool | 是否流式输出 |

---

## Best Practices / 最佳实践

### 1. 质量优先标准搜索

```python
from exa_py import Exa
exa = Exa(api_key="your-api-key")

# ✅ 质量优先配置：deep-reasoning + full text + highlights + summary
result = exa.search(
    "latest developments in LLM capabilities",
    type="deep-reasoning",          # 最强推理模式，质量最高
    num_results=25,                 # 更多候选供筛选
    contents={
        "text": {"max_characters": 50000},      # 全文，不截断
        "highlights": {
            "max_characters": 4000,
            "num_sentences": 10,
            "highlights_per_url": 5
        },
        "summary": True                          # AI 摘要
    }
)
```

### 2. 深度结构化研究

```python
# 使用 deep 模式 + outputSchema 返回结构化数据
result = exa.search(
    "top aerospace companies 2025",
    type="deep",
    output_schema={
        "type": "object",
        "required": ["companies"],
        "properties": {
            "companies": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["company_name", "ceo_name"],
                    "properties": {
                        "company_name": {"type": "string"},
                        "ceo_name": {"type": "string"}
                    }
                }
            }
        }
    }
)
```

### 3. 学术论文搜索（质量优先）

```python
# 质量优先：deep-reasoning + 全文 + 权威来源限定
result = exa.search(
    "transformer attention mechanism survey 2024",
    type="deep-reasoning",
    category="research paper",
    start_published_date="2024-01-01T00:00:00.000Z",
    include_domains=["arxiv.org","semanticscholar.org","aclanthology.org","openreview.net","nature.com"],
    num_results=25,
    contents={
        "text": {"max_characters": 50000},
        "highlights": {"max_characters": 4000, "num_sentences": 10, "highlights_per_url": 5},
        "summary": True
    }
)
```

### 4. 公司/人物信息获取

```python
# 公司信息
company_results = exa.search(
    "agtech companies in the US that have raised series A",
    type="auto",
    category="company",
    contents={"text": {"max_characters": 20000}}
)

# 人物信息（支持 LinkedIn）
people_results = exa.search(
    "software engineers at fintech companies",
    type="auto",
    category="people",
    contents={"text": {"max_characters": 20000}}
)
```

### 5. 实时新闻

```python
result = exa.search(
    "news about AI regulation",
    type="auto",
    category="news",
    contents={"highlights": {"max_characters": 4000}}
)
```

---

## 定价参考（2026年4月）

| 操作 | 单价 |
|------|------|
| Neural Search (1-10结果) | $0.007 |
| 每增加 1 个结果 | $0.001 |
| Deep Search | $0.012 |
| Deep Reasoning Search | $0.015 |
| Contents - Text（每页）| $0.001 |
| Contents - Highlights（每页）| $0.001 |
| Contents - Summary（每页）| $0.001 |

---

## 与其他工具的对比定位

| 工具 | 强项 | 弱项 | Deep Research 中的角色 |
|------|------|------|----------------------|
| **Exa** | 语义理解、学术论文、公司/人物信息 | 实时新闻覆盖稍弱 | 精准语义发现 |
| **Tavily** | 广泛网页覆盖、新闻、实时数据 | 语义理解不如 Exa | 广度检索主力 |
| **Jina** | 单页深度精读、Embedding、Rerank | 搜索发现能力弱 | 内容提取与精读 |

### 推荐组合策略

```
Stage 1 并行发现：
  Tavily search → 通用网页发现（新闻/最新动态）
  Exa search → 语义精准发现（学术/技术/公司）

Stage 2 深度阅读：
  Jina r.jina.ai → 精读 top URL 的完整内容

Stage 3 重排序：
  Jina Reranker → 合并多来源结果，按相关性重排
```

---

## Sources / 来源
- [Exa Getting Started](https://docs.exa.ai/reference/getting-started) — 产品概览与快速入门
- [Exa Search API Reference](https://docs.exa.ai/docs/reference/search) — 完整 API 参数文档
- [Exa Search API Guide](https://docs.exa.ai/docs/reference/search-api-guide) — 搜索类型对比与最佳实践
