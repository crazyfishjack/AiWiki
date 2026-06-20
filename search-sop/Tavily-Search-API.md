---
title: "Tavily Search API 工具指南"
category: tool
tags: [tavily, search-api, deep-research, retrieval, web-search]
sources:
  - https://docs.tavily.com/documentation/about
  - https://docs.tavily.com/documentation/api-reference/introduction
  - https://docs.tavily.com/documentation/api-reference/endpoint/search
  - https://docs.tavily.com/documentation/best-practices/best-practices-search
  - https://docs.tavily.com/documentation/best-practices/best-practices-research
related:
  - "[[Deep-Research-Methodology]]"
  - "[[AI-Driven-External-Retrieval]]"
  - "[[Jina-AI-API]]"
  - "[[Exa-Neural-Search-API]]"
  - "[[Retrieval-Tools-Comparison]]"
last_compiled: 2026-04-28
confidence: high
language: zh-CN+en
discovery:
  one_liner: "配置 Tavily Search API 五大端点并在 Deep Research 四阶段流水线中调用的操作指南"
  topic_cluster: ai-concepts
  load_when:
    - "需要为 LLM Agent 接入实时网络搜索或配置 Tavily API 参数时"
    - "构建 Deep Research 工作流需要选择搜索深度或并发策略时"
    - "排查 Tavily 搜索结果质量不足（相关性低、内容不完整）问题时"
  key_outputs:
    - "五大端点（/search /extract /crawl /map /research）用途与适用场景速查"
    - "search_depth 四档选择矩阵（延迟/相关性/费用对比）及质量优先标准配置模板"
    - "七条 Best Practices：Query 拆分、异步并发、Score 过滤、Exact Match 等可直接复用的代码示例"
    - "/research 端点 pro/mini/auto 模型选择及官方提示词示例"
    - "与 Deep Research 四阶段流水线集成的 Two-Step 工作流与定价参考"
  estimated_tokens: 1650
  sections:
    - heading: "What It Is / 是什么"
      one_liner: "Tavily 定位为 AI 网络访问层，单次调用返回 LLM 可用结构化内容"
      lines: [4, 15]
      tokens: 150
    - heading: "API 架构 / Architecture"
      one_liner: "Base URL、Bearer 认证方式及五大端点功能速查表"
      lines: [17, 42]
      tokens: 250
    - heading: "/search 端点详解"
      one_liner: "全部请求参数说明与 search_depth 四档延迟/相关性/费用对比矩阵"
      lines: [44, 74]
      tokens: 350
    - heading: "Best Practices / 最佳实践"
      one_liner: "七条实践：Query 拆分、深度选择、过滤技巧、质量标准配置、异步并发代码模板"
      lines: [76, 163]
      tokens: 500
    - heading: "/research 端点（端到端深度研究）"
      one_liner: "委托 Tavily 完成完整研究任务的模型选择与官方提示词示例"
      lines: [165, 193]
      tokens: 200
    - heading: "与 Deep Research 工作流的集成"
      one_liner: "四阶段流水线中 Tavily 的定位与推荐 Two-Step 工作流"
      lines: [195, 214]
      tokens: 150
    - heading: "定价参考（2026年4月）"
      one_liner: "各端点 Credit 消耗与每月免费额度数字"
      lines: [217, 225]
      tokens: 50
---

# Tavily Search API 工具指南

## What It Is / 是什么

Tavily 是专为 LLM Agent 构建的 AI 搜索引擎，定位为 **AI 的网络访问层（Web Access Layer）**。与传统搜索 API（Google/Bing/Serp）不同，Tavily 整合了搜索、抓取、过滤、提取的全流程，通过单次 API 调用直接返回 LLM 可用的结构化内容。

**核心差异化**：
- 不只返回 URL 和摘要，而是返回**经过 AI 评分、过滤、排序**的结构化内容
- 支持 RAG 优化输出，直接作为 LLM 上下文
- 提供 `/search` `/extract` `/crawl` `/map` `/research` 五大端点

**凭据位置**：见 `retrieval-api-keys.md`（根目录）

---

## API 架构 / Architecture

### Base URL
```
https://api.tavily.com
```

### 认证方式
```bash
curl -X POST https://api.tavily.com/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer tvly-YOUR_API_KEY" \
  -d '{"query": "your query here"}'
```

### 五大端点概览

| 端点 | 用途 | 适用场景 |
|------|------|---------|
| **`POST /search`** | 网页搜索，返回相关结果列表 | Deep Research 的主力检索 |
| **`POST /extract`** | 从指定 URL 提取结构化内容 | 精读目标页面 |
| **`POST /crawl`** | 智能站点图导航与内容提取 | 系统性爬取某站点 |
| **`POST /map`** | 生成站点的 URL 地图 | 探索站点结构 |
| **`POST /research`** | 端到端自动化深度研究 | 委托 Tavily 完成完整研究任务 |

---

## `/search` 端点详解

### 核心参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `query` | string | **必填** | 搜索查询，建议 < 400 字符 |
| `search_depth` | enum | `basic` | 延迟 vs 相关性的权衡 |
| `max_results` | int | 5 | 返回结果数，0-20 |
| `topic` | enum | `general` | `general` / `news` / `finance` |
| `time_range` | enum | — | `day` / `week` / `month` / `year` |
| `include_answer` | bool/enum | false | 是否生成 LLM 摘要答案 |
| `include_raw_content` | bool/enum | false | 是否返回原始页面内容 |
| `include_domains` | string[] | — | 限定来源域名（最多 300） |
| `exclude_domains` | string[] | — | 排除域名（最多 150） |
| `auto_parameters` | bool | false | AI 自动优化参数 |
| `exact_match` | bool | false | 精确短语匹配 |
| `country` | enum | — | 地区优先（仅 general topic） |

### `search_depth` 选择矩阵

| 深度 | 延迟 | 相关性 | 内容类型 | 费用 | 适用场景 |
|------|------|--------|---------|------|---------|
| `ultra-fast` | 最低 | 较低 | Content（NLP摘要）| 1 Credit | 实时应用，极速优先 |
| `fast` | 低 | 较好 | Chunks（相关片段）| 1 Credit | 速度 > 质量 |
| `basic` | 中 | 高 | Content（NLP摘要）| 1 Credit | 通用搜索，默认推荐 |
| `advanced` | 较高 | 最高 | Chunks（相关片段）| **2 Credits** | 需要精准详情时 |

> **Content vs Chunks**：Content 是 NLP 驱动的页面综合摘要；Chunks 是按与查询相关性重排序的短片段（每段最多 500 字符）。需要高度针对性信息时选 Chunks（`advanced`/`fast`）；需要页面概览时选 Content（`basic`/`ultra-fast`）。

---

## Best Practices / 最佳实践

### 1. Query 优化
- **保持 < 400 字符**：Tavily 适合简洁的 Agent 查询，而非长文本 Prompt
- **拆分复杂查询**：将多主题查询拆为多个独立请求，并行发送

```python
# ✅ 正确做法：拆分子查询
queries = [
    "Company ABC competitors",
    "Company ABC financial performance 2025",
    "Company ABC recent product launches"
]
# 并行发送，而非一个巨大的查询
```

### 2. Search Depth 选择策略（质量优先）
- **默认** → `advanced` + `chunks_per_source: 3`（最高质量，标准配置）
- 实时对话 / 快速确认 → `basic`（唯一可降级的场景）
- **不再使用** `ultra-fast` / `fast`（质量不足）

### 3. 结果过滤技巧

```python
# 时间过滤：获取最新内容
{"query": "AI news", "time_range": "week"}

# 域名限制：只看权威来源
{"query": "Python best practices", "include_domains": ["docs.python.org", "realpython.com"]}

# 地区优先
{"query": "tech startups", "country": "china"}

# 新闻模式（含 published_date）
{"query": "market trends today", "topic": "news"}
```

### 4. 质量优先标准配置

```python
# ✅ 质量优先的标准调用模板
{
  "query": "your focused sub-query < 400 chars",
  "search_depth": "advanced",          # 最高质量，始终使用
  "chunks_per_source": 3,              # 每来源最多 3 段相关片段
  "max_results": 10,                   # 最大结果数
  "include_answer": "advanced",        # 详细 LLM 摘要
  "include_raw_content": "markdown",   # 完整页面内容
  "include_favicon": true
}
```

> ✅ **质量原则**：不考虑 API 费用，永远使用 `advanced` 深度，始终开启 `include_raw_content`。

### 5. Exact Match 精确匹配

仅用于：尽职调查、特定人名/公司查询、法律合规等场景。

```python
{
  "query": '"John Smith" CEO Acme Corp',
  "exact_match": true
}
```

### 6. 异步并发（提升 Deep Research 效率）

```python
import asyncio
from tavily import AsyncTavilyClient

async def parallel_search(queries):
    client = AsyncTavilyClient("tvly-YOUR_API_KEY")
    responses = await asyncio.gather(
        *(client.search(q) for q in queries),
        return_exceptions=True
    )
    return responses
```

### 7. Score-based 结果过滤

```python
# 只保留高相关性结果
filtered = [r for r in results["results"] if r["score"] > 0.7]
```

---

## `/research` 端点（端到端深度研究）

Tavily 的最新端点，可将完整的 Deep Research 任务委托给 Tavily。

### 模型选择

| 模型 | 适用场景 |
|------|---------|
| `pro` | 复杂多领域研究，需要综合多角度分析 |
| `mini` | 聚焦的、范围明确的问题 |
| `auto` | 不确定复杂度时的默认选项 |

### 提示词示例（官方最佳实践）

```json
// pro 模式 - 深度竞争分析
{
  "input": "Analyze the competitive landscape for [Company] in the SMB market, including key competitors, positioning, pricing models, customer segments, recent product moves, and where [Company] has defensible advantages or risks over the next 2–3 years.",
  "model": "pro"
}

// mini 模式 - 快速聚焦问题
{
  "input": "What are the top 5 competitors to [Company] in the SMB market, and how do they differentiate?",
  "model": "mini"
}
```

---

## 与 Deep Research 工作流的集成

### 在四阶段流水线中的定位

```
Stage 1: Query Decomposition → Tavily search（探索子问题）
Stage 2: Parallel Search → Tavily search（多查询并行）
Stage 3: Iterative Refinement → Tavily extract（精读高价值页面）
Stage 4: Synthesis → 使用 Tavily 返回的 score + content 排序
```

### 推荐的 Two-Step 工作流

```
Step 1: /search → 获取相关 URL 列表（max_results=10）
Step 2: /extract → 对 top URL 做深度内容提取
```

> 直接在 search 中设置 `include_raw_content=true` 也可，但会增加延迟和 Token 消耗；建议仅对 top 3-5 结果做 extract。

---

## 定价参考（2026年4月）

| 操作 | 费用 |
|------|------|
| `/search` basic/fast/ultra-fast | 1 Credit |
| `/search` advanced | 2 Credits |
| 免费额度 | 1,000 Credits/月 |

---

## Sources / 来源
- [Tavily About](https://docs.tavily.com/documentation/about) — 产品定位与工作原理
- [Tavily API Introduction](https://docs.tavily.com/documentation/api-reference/introduction) — API 端点总览
- [Tavily Search Endpoint](https://docs.tavily.com/documentation/api-reference/endpoint/search) — Search 完整参数文档
- [Tavily Best Practices: Search](https://docs.tavily.com/documentation/best-practices/best-practices-search) — 官方搜索最佳实践
- [Tavily Best Practices: Research](https://docs.tavily.com/documentation/best-practices/best-practices-research) — Research 端点最佳实践
