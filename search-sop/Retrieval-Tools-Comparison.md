---
title: "检索工具四件套：Tavily / Exa / Firecrawl / Jina 对比与使用矩阵"
category: tool
tags: [tavily, exa, firecrawl, jina, deep-research, retrieval, comparison, api, anti-hallucination, v2]
sources:
  - https://docs.tavily.com/documentation/api-reference/introduction
  - https://docs.exa.ai/docs/reference/search-api-guide
  - https://docs.firecrawl.dev/introduction
  - https://docs.jina.ai/
  - https://www.firecrawl.dev/blog/crawlbench-llm-extraction
  - https://use-apify.com/blog/firecrawl-vs-jina-reader-2026
related:
  - "[[Three-Tool-Retrieval-SOP]]"
  - "[[Tavily-Search-API]]"
  - "[[Jina-AI-API]]"
  - "[[Exa-Neural-Search-API]]"
  - "[[Firecrawl-API]]"
  - "[[Deep-Research-Methodology]]"
  - "[[Anti-Hallucination-Engineering]]"
last_compiled: 2026-05-22
confidence: high
language: zh-CN+en
discovery:
  one_liner: "四工具（Tavily/Exa/Firecrawl/Jina）角色分工、场景速查与可直接运行的 API 调用代码"
  topic_cluster: ai-concepts
  load_when:
    - "需要决定用哪个检索工具（Tavily/Exa/Firecrawl/Jina）处理具体场景时"
    - "需要四工具的可运行 Python API 调用代码或参数铁律时"
    - "设计多工具协作研究流程或排查 Jina readerlm-v2 幻觉问题时"
  key_outputs:
    - "四工具能力对比矩阵（搜索广度/语义理解/精读/结构化萃取等 13 个维度评分）"
    - "13 类场景首选/备选工具速查表"
    - "A/B/C/D 四种协作模式架构图（标准研究/快速融合/结构化萃取/整站深研）"
    - "四工具各端点可直接运行 Python 代码及质量铁律参数"
    - "中文内容保障、并行执行、Jina readerlm-v2 禁用场景等注意事项"
  estimated_tokens: 2400
  sections:
    - heading: "概述：四工具当前持有状态"
      one_liner: "四工具 v2 角色定义与核心端点一览表"
      lines: [7, 16]
      tokens: 150
    - heading: "核心能力对比矩阵"
      one_liner: "13 个维度星级评分矩阵，含幻觉风险与深度研究端点对比"
      lines: [18, 36]
      tokens: 300
    - heading: "场景选择速查表"
      one_liner: "13 类检索场景对应首选工具与备选工具速查"
      lines: [38, 56]
      tokens: 300
    - heading: "四工具协作架构（SOP v2）"
      one_liner: "A/B/C/D 四模式协作流程图，含信源质量过滤与智能精读路由"
      lines: [58, 105]
      tokens: 400
    - heading: "API 调用速查"
      one_liner: "四工具各端点 Python 代码示例及质量铁律参数，含 Jina 禁用场景警告"
      lines: [107, 237]
      tokens: 1050
    - heading: "注意事项"
      one_liner: "API Key 安全、并行执行、中文内容保障、Exa vs Tavily 选择标准"
      lines: [239, 262]
      tokens: 250
---

# 检索工具四件套：Tavily / Exa / Firecrawl / Jina 对比与使用矩阵

> **v2 更新（2026-05-22）**：Firecrawl 加入成为第四工具，升级为精读主力；Jina 降级为学术 PDF 专用 + Reranker。
> 工具角色定义、场景速查表、协作方案、调用速查全面更新。

## 概述：四工具当前持有状态

| 工具 | 角色（v2）| 核心端点 | API Key |
|------|----------|---------|---------|
| **Tavily** | 广度发现主力 | `/search` `/research` | `retrieval-api-keys.md` |
| **Exa** | 神经语义 / 学术精准 | `/search` `/contents` `/answer` | `retrieval-api-keys.md` |
| **Firecrawl** | 精读主力 + 结构化萃取 + 整站爬取 | `/scrape` `/search` `/extract` `/crawl` | `retrieval-api-keys.md` |
| **Jina AI** | 学术 PDF 精读（降级专用）+ Reranker | `r.jina.ai`（readerlm）`/v1/rerank` | `retrieval-api-keys.md` |

---

## 核心能力对比矩阵

| 维度 | Tavily | Exa | Firecrawl | Jina |
|------|--------|-----|-----------|------|
| **搜索广度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **神经语义理解** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| **单页精读（普通页面）** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐（默认）|
| **单页精读（学术PDF）** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐（readerlm）|
| **学术内容检索** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **实时新闻** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **结构化数据萃取** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ |
| **中文内容** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⚠️（readerlm幻觉风险）|
| **整站爬取** | ❌ | ❌ | ⭐⭐⭐⭐⭐ | ❌ |
| **搜索+全文一步** | ❌ | ❌ | ⭐⭐⭐⭐⭐ | ❌ |
| **Embedding / Rerank** | ❌ | ❌ | ❌ | ⭐⭐⭐⭐⭐ |
| **幻觉注入风险** | 低 | 低 | **极低**（无LLM层）| 中（readerlm有LLM重写）|
| **深度研究端点** | ✅ `/research` | ❌ | ❌ | ❌ |

---

## 场景选择速查表

| 场景 | 首选工具 | 备选 | 说明 |
|------|---------|------|------|
| 通用网页搜索（广度）| **Tavily** | Exa | 广覆盖，RAG 优化，新闻强 |
| 实时新闻追踪 | **Tavily** (`topic: news`) | — | 新闻覆盖最强 |
| 中文内容搜索 | **Tavily** + `country: china` | — | 中文网页覆盖最好 |
| 学术论文检索 | **Exa** (`category: research paper`) | Tavily | 神经语义，100M+ 全文论文 |
| 公司 / 人物信息 | **Exa** (`category: company`) | Tavily | 50M+ 公司数据库 |
| 语义发现（无精确关键词）| **Exa** (`deep-reasoning`) | — | 神经网络语义匹配 |
| 普通页面精读（主力）| **Firecrawl** `/scrape` | 内置 crawl | 确定性抓取，无幻觉注入 |
| 搜索 + 全文一步获取 | **Firecrawl** `/search` + scrapeOptions | — | 省去 round-trip |
| 结构化跨URL数据萃取 | **Firecrawl** `/extract` + schema | — | LLM 驱动结构化提取 |
| 整站递归爬取 | **Firecrawl** `/crawl` | — | 文档站 / 官网全量入库 |
| arXiv / 学术期刊 PDF 精读 | **Jina** `readerlm-v2` | Firecrawl | 学术结构理解能力强 |
| 候选文档重排序 | **Jina Reranker v3** | — | 候选 >15 篇时精选 |
| 端到端自动研究报告 | **Tavily** `/research` | — | 委托 API 完成完整研究 |

---

## 四工具协作架构（SOP v2）

```
┌────────────────────────────────────────────────────────────────┐
│  前置：任务路由（选模式）                                         │
│  A 标准研究  B 快速融合  C 结构化萃取  D 整站深研                │
└───────────────────────┬────────────────────────────────────────┘
                        │
        ┌───────────────▼──────────────────┐
        │  模式 A：标准研究（最常用）          │
        │                                   │
        │  S1: 查询分解（≤6子查询）           │
        │        ↓                           │
        │  S2: 并行发现                       │
        │    Tavily → 通用/新闻/中文          │
        │    Exa    → 学术/语义/技术          │
        │        ↓ 信源质量过滤(score≥0.4)   │
        │  S3: 智能精读路由                   │
        │    学术域名 → Jina readerlm-v2     │
        │    其他所有 → Firecrawl /scrape    │
        │        ↓                           │
        │  S3.5: 跨源矛盾检测（新增）         │
        │        ↓                           │
        │  S4-S7: 验证→综合→入库             │
        └───────────────────────────────────┘

        ┌─────────────────────────┐
        │  模式 B：快速融合         │
        │  Firecrawl /search      │
        │  + scrapeOptions        │
        │  一步完成搜索+全文        │
        └─────────────────────────┘

        ┌─────────────────────────┐
        │  模式 C：结构化萃取       │
        │  Firecrawl /extract     │
        │  + Pydantic schema      │
        │  直出结构化 JSON         │
        └─────────────────────────┘

        ┌─────────────────────────┐
        │  模式 D：整站深研         │
        │  Firecrawl /crawl       │
        │  递归爬取目标站全部页面   │
        └─────────────────────────┘
```

---

## API 调用速查

### Tavily（广度发现，质量优先）

```python
import requests

def tavily_search(query, topic="general", time_range=None):
    body = {
        "query": query,
        "search_depth": "advanced",       # 始终 advanced
        "chunks_per_source": 3,
        "max_results": 10,
        "topic": topic,                   # general / news / finance
        "include_answer": "advanced",
        "include_raw_content": "markdown",
    }
    if time_range:
        body["time_range"] = time_range   # day / week / month
    r = requests.post(
        "https://api.tavily.com/search",
        headers={"Authorization": f"Bearer {TAVILY_KEY}", "Content-Type": "application/json"},
        json=body, proxies=PROXIES, timeout=45,
    )
    r.raise_for_status()
    return r.json()
```

**质量铁律**：始终 `search_depth="advanced"` + `include_raw_content="markdown"` + `include_answer="advanced"`

---

### Exa（语义/学术，质量优先）

```python
def exa_search(query, category=None):
    body = {
        "query": query,
        "type": "deep-reasoning",         # 始终 deep-reasoning
        "numResults": 15,
        "contents": {
            "text": {"maxCharacters": 50000},
            "highlights": {"maxCharacters": 4000, "numSentences": 10, "highlightsPerUrl": 5},
            "summary": True,
        },
    }
    if category:
        body["category"] = category       # "research paper" / "company" / "tweet"
    r = requests.post(
        "https://api.exa.ai/search",
        headers={"x-api-key": EXA_KEY, "Content-Type": "application/json"},
        json=body, proxies=PROXIES, timeout=45,
    )
    r.raise_for_status()
    return r.json()
```

**质量铁律**：始终 `type="deep-reasoning"` + `text.maxCharacters=50000` + `summary=True`

---

### Firecrawl（精读主力，质量优先）

```python
# 单页精读（所有普通页面）
def firecrawl_scrape(url):
    r = requests.post(
        "https://api.firecrawl.dev/v2/scrape",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}", "Content-Type": "application/json"},
        json={"url": url, "formats": ["markdown"], "onlyMainContent": True, "timeout": 30000},
        proxies=PROXIES, timeout=60,
    )
    r.raise_for_status()
    return r.json().get("data", {}).get("markdown", "")

# 搜索+全文一步（模式 B）
def firecrawl_search(query, limit=5):
    r = requests.post(
        "https://api.firecrawl.dev/v2/search",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}", "Content-Type": "application/json"},
        json={"query": query, "limit": limit,
              "scrapeOptions": {"formats": ["markdown"], "onlyMainContent": True}},
        proxies=PROXIES, timeout=60,
    )
    r.raise_for_status()
    return r.json().get("data", [])
```

**质量铁律**：始终 `onlyMainContent=True`（过滤导航/侧栏/广告）

---

### Jina（学术精读 + Reranker，限定场景）

```python
# 学术 PDF 精读（仅限学术域名白名单）
def jina_read_academic(url):
    r = requests.post(
        "https://r.jina.ai/",
        headers={
            "Authorization": f"Bearer {JINA_KEY}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Return-Format": "markdown",
            "X-Engine": "browser",
            "X-Respond-With": "readerlm-v2",   # 仅此场景开启
            "X-Remove-Selector": "nav,footer,aside,script,style",
            "X-With-Links-Summary": "true",
        },
        json={"url": url},
        proxies=PROXIES, timeout=60,
    )
    r.raise_for_status()
    return r.json().get("data", {}).get("content", "")

# Reranker（候选 >15 篇时使用）
def jina_rerank(query, documents, top_n=10):
    r = requests.post(
        "https://api.jina.ai/v1/rerank",
        headers={"Authorization": f"Bearer {JINA_KEY}", "Content-Type": "application/json"},
        json={"model": "jina-reranker-v3", "query": query,
              "documents": documents, "top_n": top_n},
        proxies=PROXIES, timeout=30,
    )
    r.raise_for_status()
    return r.json()
```

⚠️ **Jina readerlm-v2 禁用场景**：任何非学术域名的页面（中文/英文普通页面）。readerlm-v2 是 LLM 重写层，中文内容站实测触发严重幻觉（插入 20+ 条原文不存在内容）。详见 `[[Jina-AI-API]]` § readerlm-v2 幻觉风险。

---

## 注意事项

### 🔑 API Key 安全
- 四个 Key 均存放于 `retrieval-api-keys.md`（Wiki 根目录），不在对话中打印

### ⚡ 并行执行原则
- Tavily + Exa 的 Stage 2 **同一批次并行发出**，不串行等待
- Firecrawl 多页精读用 `batch_scrape` 一次性提交

### 🌐 中文内容保障
- Tavily：中文查询词 + `country="china"` 参数
- Firecrawl：中文页面表现与英文同等（v2 验证通过）
- Jina：中文页面关闭 readerlm-v2，改用 Firecrawl

### 📊 Exa vs Tavily 选择标准

| 选 Exa | 选 Tavily |
|--------|---------|
| 学术论文 / arXiv | 最新新闻 / 动态 |
| 技术规格 / 代码 | 通用宽泛查询 |
| 语义搜索（无精确关键词）| 中文内容 |
| 公司 / 人物定向查找 | 实时事件追踪 |

---

## Sources / 来源
- [Tavily API Reference](https://docs.tavily.com/documentation/api-reference/introduction)
- [Exa Search API Guide](https://docs.exa.ai/docs/reference/search-api-guide)
- [Firecrawl Official Docs](https://docs.firecrawl.dev/)
- [CrawlBench Benchmark](https://www.firecrawl.dev/blog/crawlbench-llm-extraction) — Firecrawl 96% / F1 0.638 / ROUGE 93.7%
- [Firecrawl vs Jina Reader 2026 (Apify)](https://use-apify.com/blog/firecrawl-vs-jina-reader-2026)
- [Jina AI Docs](https://docs.jina.ai/)
- `wiki/workflows/Three-Tool-Retrieval-SOP.md` — 四工具 SOP v2 完整流程
