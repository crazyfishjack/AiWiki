---
title: "检索工具四件套：Tavily / Exa / Firecrawl / Jina 对比与使用矩阵"
category: tool
tags: [tavily, exa, firecrawl, jina, deep-research, retrieval, comparison, api, anti-hallucination, cost-aware, v2, v2.1]
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
last_compiled: 2026-06-16
confidence: high
language: zh-CN+en
discovery:
  one_liner: "四工具（Tavily/Exa/Jina/Firecrawl）角色分工、场景速查与可运行 API 代码；v2.1 精读主力=Jina 默认模式、Firecrawl 降级后备，含成本维度"
  topic_cluster: ai-concepts
  load_when:
    - "需要决定用哪个检索工具（Tavily/Exa/Firecrawl/Jina）处理具体场景时"
    - "需要四工具的可运行 Python API 调用代码或参数铁律时"
    - "设计多工具协作研究流程或排查 Jina readerlm-v2 幻觉问题时"
  key_outputs:
    - "四工具能力对比矩阵（搜索/语义/精读/结构化/成本等 14 个维度评分，v2.1 含幻觉风险与成本模型）"
    - "13 类场景首选/备选工具速查表（v2.1：普通页面精读主力=Jina 默认模式）"
    - "A/B/C/D 四种协作模式架构图（含 v2.1 精读路由：Jina 默认→失败降级 Firecrawl）"
    - "四工具各端点可运行 Python 代码（含 jina_read 默认模式主力）及质量铁律参数"
    - "中文内容保障、并行执行、Jina readerlm-v2 禁用（≠禁默认模式）等注意事项"
  estimated_tokens: 2700
  sections:
    - heading: "概述：四工具当前持有状态"
      one_liner: "四工具 v2.1 角色定义（Jina 默认精读主力、Firecrawl 降级+extract/crawl）与核心端点一览"
      lines: [7, 16]
      tokens: 160
    - heading: "核心能力对比矩阵"
      one_liner: "14 维星级评分矩阵，含幻觉风险（默认模式 vs readerlm-v2）与成本模型对比"
      lines: [18, 37]
      tokens: 320
    - heading: "场景选择速查表"
      one_liner: "13 类检索场景对应首选/备选工具（v2.1：普通页面精读主力=Jina 默认模式）"
      lines: [39, 57]
      tokens: 300
    - heading: "四工具协作架构（SOP v2）"
      one_liner: "A/B/C/D 四模式协作流程图，含信源质量过滤与 v2.1 精读路由（Jina 默认→降级 Firecrawl）"
      lines: [59, 107]
      tokens: 400
    - heading: "API 调用速查"
      one_liner: "四工具各端点 Python 代码（含 jina_read 默认模式主力 + Firecrawl 降级）及质量铁律"
      lines: [109, 259]
      tokens: 1250
    - heading: "注意事项"
      one_liner: "API Key 安全、并行执行、中文内容保障（Jina 默认主力）、Exa vs Tavily 选择标准"
      lines: [261, 284]
      tokens: 260
---

# 检索工具四件套：Tavily / Exa / Firecrawl / Jina 对比与使用矩阵

> **v2 更新（2026-05-22）**：Firecrawl 加入成为第四工具。
> **v2.1 修正（2026-06-16，成本/原理）**：精读主力 = **Jina Reader 默认模式**（确定性 turndown+readability、非 LLM、按需计费）；**Firecrawl 降为精读降级后备 + `/extract`·`/crawl` 独占主力**；Jina readerlm-v2 仅限学术 PDF。修正依据：① v2「Jina=幻觉」混淆了 Jina 默认模式（纯规则、零幻觉）与可选 readerlm-v2（LLM 重写层）；② Firecrawl 月订阅 credits 不滚存，高频精读迁 Jina 按需更省。详见 `[[Three-Tool-Retrieval-SOP]]` v2.1 变更记录。

## 概述：四工具当前持有状态

| 工具 | 角色（v2.1）| 核心端点 | API Key |
|------|----------|---------|---------|
| **Tavily** | 广度发现主力 | `/search` `/research` | `retrieval-api-keys.md` |
| **Exa** | 神经语义 / 学术精准 | `/search` `/contents` `/answer` | `retrieval-api-keys.md` |
| **Firecrawl** | 结构化萃取/整站爬取主力 + 精读降级后备 | `/scrape` `/search` `/extract` `/crawl` | `retrieval-api-keys.md` |
| **Jina AI** | 普通页面精读主力（默认模式）+ 学术 PDF（readerlm）+ Reranker | `r.jina.ai` `/v1/rerank` | `retrieval-api-keys.md` |

---

## 核心能力对比矩阵

| 维度 | Tavily | Exa | Firecrawl | Jina |
|------|--------|-----|-----------|------|
| **搜索广度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **神经语义理解** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| **单页精读（普通页面）** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐（降级后备）| ⭐⭐⭐⭐⭐（默认模式主力）|
| **单页精读（学术PDF）** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐（readerlm）|
| **学术内容检索** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **实时新闻** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **结构化数据萃取** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ |
| **中文内容** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐（默认模式安全；仅 readerlm 有风险）|
| **整站爬取** | ❌ | ❌ | ⭐⭐⭐⭐⭐ | ❌ |
| **搜索+全文一步** | ❌ | ❌ | ⭐⭐⭐⭐⭐ | ❌ |
| **Embedding / Rerank** | ❌ | ❌ | ❌ | ⭐⭐⭐⭐⭐ |
| **幻觉注入风险** | 低 | 低 | **极低**（无LLM层）| 默认模式**极低**；readerlm-v2 中 |
| **深度研究端点** | ✅ `/research` | ❌ | ❌ | ❌ |
| **成本模型** | 按次/订阅 | 按次/订阅 | 月订阅·credits 不滚存 | **按 token·失败不扣费** |

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
| 普通页面精读（主力）| **Jina** 默认模式 | Firecrawl 降级 | 确定性 turndown+readability，按需计费，失败降级 Firecrawl |
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
        │    其他所有 → Jina 默认模式（主力） │
        │      失败降级 → Firecrawl /scrape  │
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

### Firecrawl（精读降级后备 + extract/crawl 独占，v2.1）

```python
# 单页精读降级后备（仅 Jina 默认模式失败时兜底）
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

### Jina（精读主力默认模式 + 学术 readerlm + Reranker，v2.1）

```python
# 普通页面精读主力：默认模式（不开 readerlm-v2，确定性、按需计费）
def jina_read(url):
    r = requests.post(
        "https://r.jina.ai/",
        headers={
            "Authorization": f"Bearer {JINA_KEY}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Return-Format": "markdown",
            "X-Engine": "browser",                 # 浏览器渲染，无 LLM 重写层
            "X-Remove-Selector": "nav,footer,aside,script,style",
            "X-With-Links-Summary": "true",
            # ⚠️ 绝不设 X-Respond-With:readerlm-v2（那是 LLM 引擎，仅学术用）
        },
        json={"url": url},
        proxies=PROXIES, timeout=60,
    )
    r.raise_for_status()
    return r.json().get("data", {}).get("content", "")

# 学术 PDF 精读（仅限学术域名白名单，显式开 readerlm-v2）
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

⚠️ **Jina readerlm-v2 禁用场景**：任何非学术域名的页面（中文/英文普通页面）禁开 `X-Respond-With:readerlm-v2`——它是 LLM 重写层，中文内容站实测触发严重幻觉（插入 20+ 条原文不存在内容）。**注意：这只禁 readerlm-v2 开关，不禁 Jina 默认模式**——普通页面精读主力正是 `jina_read()` 默认模式（纯规则、零幻觉）。详见 `[[Jina-AI-API]]` § readerlm-v2 幻觉风险。

---

## 注意事项

### 🔑 API Key 安全
- 四个 Key 均存放于 `retrieval-api-keys.md`（Wiki 根目录），不在对话中打印

### ⚡ 并行执行原则
- Tavily + Exa 的 Stage 2 **同一批次并行发出**，不串行等待
- 多页精读并行发出（Jina 默认模式主力可并发；降级的 Firecrawl 可用 `batch_scrape`）

### 🌐 中文内容保障
- Tavily：中文查询词 + `country="china"` 参数
- Jina 默认模式：中文页面确定性提取、表现稳定（精读主力）；失败再降级 Firecrawl
- 关闭 readerlm-v2：中文聚合站（搜狐/百家号等 ACRI<40）禁开 readerlm-v2（默认模式无此问题）

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
