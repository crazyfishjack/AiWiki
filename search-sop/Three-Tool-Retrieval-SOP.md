---
title: "四工具检索 SOP v2：Tavily + Exa + Firecrawl + Jina 联合调用标准工作流"
category: workflow
tags: [SOP, tavily, exa, firecrawl, jina, deep-research, retrieval, default-workflow, wiki-ingest, quality-first, anti-hallucination, v2]
sources:
  - wiki/tools/Tavily-Search-API.md
  - wiki/tools/Jina-AI-API.md
  - wiki/tools/Exa-Neural-Search-API.md
  - wiki/concepts/Deep-Research-Methodology.md
  - wiki/concepts/Anti-Hallucination-Engineering.md
  - wiki/concepts/RAG-System-Design.md
  - https://www.firecrawl.dev/blog/crawlbench-llm-extraction
  - https://use-apify.com/blog/firecrawl-vs-jina-reader-2026
  - https://arxiv.org/html/2603.07379v1 (SoK: Agentic RAG)
  - https://arxiv.org/pdf/2410.11414 (REDEEP: Hallucination in RAG)
  - https://arxiv.org/html/2605.21482 (DeepWeb-Bench)
related:
  - "[[AI-Driven-External-Retrieval]]"
  - "[[Deep-Research-Methodology]]"
  - "[[Retrieval-Tools-Comparison]]"
  - "[[Anti-Hallucination-Engineering]]"
  - "[[INGEST-Workflow]]"
  - "[[Firecrawl-API]]"
last_compiled: 2026-05-22
confidence: high
language: zh-CN+en
discovery:
  one_liner: "四工具（Tavily+Exa+Firecrawl+Jina）外部检索唯一默认 SOP，含 A/B/C/D 四模式、七步流程与零幻觉防御机制"
  topic_cluster: ai-concepts
  load_when:
    - "需要执行外部检索或入库新知识时"
    - "需要选择 Tavily/Exa/Firecrawl/Jina 具体调用参数时"
    - "排查检索结果幻觉或跨源矛盾问题时"
  key_outputs:
    - "四工具角色矩阵与 A/B/C/D 任务路由决策树"
    - "可直接复用的 Python 封装（tavily_search/exa_search/firecrawl_scrape/jina_rerank）"
    - "模式 A 七步标准研究流程（含 Step 2.5 信源过滤、Step 3.5 跨源矛盾检测、Step 5 反幻觉清单）"
    - "模式 B/C/D 快速融合、结构化萃取、整站爬取的调用示例与适用场景"
    - "Windows 脚本模式四步标准流程与等待脚本强制模板"
  related_must_read:
    - "[[Windows-API-Call-Guide]]"
  estimated_tokens: 6850
  sections:
    - heading: "一、四工具矩阵与角色定义"
      one_liner: "四工具四层架构（发现/精读/增强/综合）及角色速查表"
      lines: [19, 57]
      tokens: 450
    - heading: "二、任务路由前置：四种模式"
      one_liner: "A/B/C/D 四模式任务类型判断树，进入任何检索前必读"
      lines: [60, 79]
      tokens: 150
    - heading: "三、标准调用封装（Python，直接复用）"
      one_liner: "四工具 Python 封装函数，含代理配置与调用三步准备"
      lines: [82, 301]
      tokens: 1700
    - heading: "四、模式 A — 标准研究（七步流程）"
      one_liner: "七步深度研究流程，含子查询上界、信源过滤、矛盾检测、反幻觉清单"
      lines: [305, 541]
      tokens: 2000
    - heading: "五、模式 B — 快速融合搜索"
      one_liner: "Firecrawl search+scrape 一步获取搜索结果全文的快速模式"
      lines: [544, 578]
      tokens: 300
    - heading: "六、模式 C — 结构化多页萃取"
      one_liner: "Firecrawl /extract+schema 跨 URL 批量提取结构化字段"
      lines: [581, 645]
      tokens: 550
    - heading: "七、模式 D — 整站深度研究"
      one_liner: "Firecrawl /crawl 异步整站爬取与轮询状态脚本"
      lines: [648, 698]
      tokens: 450
    - heading: "八、Windows 调用标准（脚本模式）"
      one_liner: "Windows 下四步脚本流程、等待模板与四条禁令"
      lines: [701, 770]
      tokens: 600
    - heading: "九、场景速查与决策树"
      one_liner: "完整决策树 + 工具参数速查表（质量优先版）"
      lines: [773, 818]
      tokens: 400
    - heading: "十、注意事项 / Tips & Gotchas"
      one_liner: "Jina 幻觉风险重新定性、Firecrawl 最佳实践、Exa vs Tavily 选择指南"
      lines: [821, 869]
      tokens: 450
---

# 四工具检索 SOP v2：Tavily + Exa + Firecrawl + Jina

> ## ⚡ 默认行为声明
>
> **本页面是 Wiki 助理获取外部信息的唯一默认 SOP（v2 全量重写，2026-05-22）。**
> 每当需要从外部检索信息（入库新知识 / 回答需要最新数据的问题 / 补充 Wiki 空白），
> 优先按本流程执行，不允许直接依赖内置 Web Browsing 作为主力检索手段。
>
> **🎯 质量优先原则**：不考虑 API 调用成本，所有参数以获取最高质量结果为准。
>
> **🔒 零幻觉原则**：每个设计决策均以「消除检索侧幻觉注入」为首要约束。
>
> **API Key 位置**：`D:\Nextcloud\EngPath\AIWorkWiki\retrieval-api-keys.md`
> 调用前必须先读取该文件获取 Key，不在对话中明文展示 Key 值。

---

## 一、四工具矩阵与角色定义

> **v2 核心变更**：Firecrawl 升级为精读主力，Jina 降级为学术 PDF 专用 + Reranker。
> 选型依据：CrawlBench 独立基准（Firecrawl: 96% coverage, F1 0.638, ROUGE 93.7%）；
> Jina readerlm-v2 本质是 LLM 重写层，**所有非学术页面均有生成式幻觉注入风险**。

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 1 — 广度发现（DISCOVER）                                   │
│  Tavily  → 通用网页 / 新闻 / 最新动态，返回结构化 JSON + 全文      │
│  Exa     → 神经语义搜索，学术论文 / 技术内容 / 公司人物精准定位     │
│  两者并行执行                                                     │
├─────────────────────────────────────────────────────────────────┤
│  Layer 2 — 深度精读（READ）                        【v2 重构】    │
│  Firecrawl /scrape → 所有普通页面（中文/英文/技术/新闻）主力精读   │
│  Jina readerlm-v2  → 仅限 arXiv / 学术期刊 PDF（学术结构理解）   │
│  内置 Web Browsing → 降级备用（Firecrawl 失败时）                 │
├─────────────────────────────────────────────────────────────────┤
│  Layer 3 — 结构化增强（ENHANCE）                   【v2 新增】    │
│  Firecrawl /search+scrapeOptions → 搜索+全文一步获取（模式B）     │
│  Firecrawl /extract+schema       → 跨URL结构化数据萃取（模式C）   │
│  Firecrawl /crawl                → 整站递归爬取（模式D）          │
├─────────────────────────────────────────────────────────────────┤
│  Layer 4 — 重排与综合（SYNTHESIZE）                               │
│  Jina Reranker v3（可选）→ 候选文档 > 15 篇时重排序               │
│  LLM 综合 + 强制溯源 → 结构化带引用报告                            │
└─────────────────────────────────────────────────────────────────┘
```

### 工具角色速查表

| 工具 | 核心角色 | 关键限制 |
|------|---------|---------|
| **Tavily** | 广度发现主力，通用 + 新闻 | 精读质量不如 Firecrawl |
| **Exa** | 语义 / 学术精准定位 | 中文覆盖有限 |
| **Firecrawl** | 精读主力，结构化萃取，整站爬取 | PDF 学术结构理解不如 Jina readerlm |
| **Jina readerlm-v2** | 仅限 arXiv / 学术期刊 PDF | **所有普通页面禁用**（LLM 重写层幻觉风险）|
| **Jina Reranker v3** | 候选超量时重排序（可选）| 消耗 API 额度，仅在有必要时启用 |

---

## 二、任务路由前置：四种模式

**在执行任何检索前，必须先判断任务类型，路由到对应模式。**

```
任务类型判断
    │
    ├─ 需要深入研究多个维度（标准情况）
    │       → 【模式 A】标准研究（七步流程，见第四章）
    │
    ├─ 需要快速获取全文内容，不做深度拆解
    │       → 【模式 B】快速融合（Firecrawl search+scrape，见第五章）
    │
    ├─ 目标是从多个 URL 提取结构化数据（表格/字段/对比）
    │       → 【模式 C】结构化萃取（Firecrawl /extract，见第六章）
    │
    └─ 需要完整读取某个产品文档站 / 公司官网
            → 【模式 D】整站深研（Firecrawl /crawl，见第七章）
```

---

## 三、标准调用封装（Python，直接复用）

> **⚠️ Windows 平台铁律**：
> `curl.exe` JSON 引号转义不可靠；`PowerShell Invoke-RestMethod` 非交互环境输出不稳定。
> **唯一可靠方案：Python `requests` + 代理**。详见 `[[Windows-API-Call-Guide]]`。
>
> **调用三步准备**：
> 1. 读取 `retrieval-api-keys.md` 获取四个 Key
> 2. 脚本写入 `C:\Temp\` 再用 `runCommand` 执行（绕开 Shell 引号陷阱）
> 3. 代理地址：`http://127.0.0.1:10808`

```python
import requests, json, time, os

# ── 从 retrieval-api-keys.md 读取（调用时替换为实际值）──────────────
TAVILY_KEY    = "tvly-prod-..."
EXA_KEY       = "c4bb9e60-..."
JINA_KEY      = "jina_3bca2..."
FIRECRAWL_KEY = "fc-1f7752..."

PROXIES = {"http": "http://127.0.0.1:10808", "https": "http://127.0.0.1:10808"}
TIMEOUT = 45

# ════════════════════════════════════════════════════════════════
# TAVILY — 广度发现主力
# ════════════════════════════════════════════════════════════════
def tavily_search(query, topic="general", time_range=None):
    """质量优先：advanced 深度 + 完整 markdown + LLM 详细摘要"""
    body = {
        "query": query,
        "search_depth": "advanced",   # 始终 advanced
        "chunks_per_source": 3,
        "max_results": 10,
        "topic": topic,               # general / news / finance
        "include_answer": "advanced", # LLM 详细摘要
        "include_raw_content": "markdown",  # 完整页面内容
    }
    if time_range:
        body["time_range"] = time_range  # day / week / month / year
    r = requests.post(
        "https://api.tavily.com/search",
        headers={"Authorization": f"Bearer {TAVILY_KEY}", "Content-Type": "application/json"},
        json=body, proxies=PROXIES, timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()

# ════════════════════════════════════════════════════════════════
# EXA — 神经语义 / 学术精准定位
# ════════════════════════════════════════════════════════════════
def exa_search(query, category=None):
    """质量优先：deep-reasoning + 全文 50K + highlights + summary"""
    body = {
        "query": query,
        "type": "deep-reasoning",     # 始终 deep-reasoning
        "numResults": 15,
        "contents": {
            "text": {"maxCharacters": 50000},       # 全文不截断
            "highlights": {
                "maxCharacters": 4000,
                "numSentences": 10,
                "highlightsPerUrl": 5,
            },
            "summary": True,
        },
    }
    if category:
        body["category"] = category  # "research paper" / "company" / "tweet"
    r = requests.post(
        "https://api.exa.ai/search",
        headers={"x-api-key": EXA_KEY, "Content-Type": "application/json"},
        json=body, proxies=PROXIES, timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()

# ════════════════════════════════════════════════════════════════
# FIRECRAWL — 精读主力（v2 升级）
# ════════════════════════════════════════════════════════════════

def firecrawl_scrape(url, with_json_schema=None, question=None):
    """
    单页精读主力（替代 Jina 普通页面场景）。
    ✅ 适用：中文 / 英文 / 技术博客 / 新闻 / 官方文档 / GitHub
    ❌ 不适用：arXiv 学术 PDF（改用 jina_read_academic）
    
    可选：with_json_schema — Pydantic schema dict → 结构化 JSON 提取
          question — 对页面提问，直接返回答案
    """
    formats = ["markdown"]
    if with_json_schema:
        formats.append({"type": "json", "schema": with_json_schema})
    if question:
        formats.append({"type": "question", "question": question})

    r = requests.post(
        "https://api.firecrawl.dev/v2/scrape",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}", "Content-Type": "application/json"},
        json={
            "url": url,
            "formats": formats,
            "onlyMainContent": True,   # 过滤导航/侧栏/广告噪声
            "timeout": 30000,
        },
        proxies=PROXIES, timeout=60,
    )
    r.raise_for_status()
    data = r.json().get("data", {})
    result = {"markdown": data.get("markdown", ""), "url": url}
    if with_json_schema:
        result["json"] = data.get("json", {})
    if question:
        result["answer"] = data.get("answer", "")
    return result


def firecrawl_search(query, limit=5, with_full_content=True):
    """
    【模式 B 专用】搜索 + 全文一步获取，减少一个 round-trip。
    with_full_content=True 时，返回每条结果的完整 markdown 正文。
    """
    scrape_opts = {"formats": ["markdown"], "onlyMainContent": True} if with_full_content else {}
    r = requests.post(
        "https://api.firecrawl.dev/v2/search",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}", "Content-Type": "application/json"},
        json={"query": query, "limit": limit, "scrapeOptions": scrape_opts},
        proxies=PROXIES, timeout=60,
    )
    r.raise_for_status()
    return r.json().get("data", [])


def firecrawl_extract(urls, prompt, schema=None):
    """
    【模式 C 专用】跨 URL 结构化数据萃取（LLM 驱动）。
    urls 支持通配：["https://example.com/*"]
    schema 为 JSON Schema dict（推荐），不传则按 prompt 自由提取。
    """
    body = {"urls": urls, "prompt": prompt}
    if schema:
        body["schema"] = schema
    r = requests.post(
        "https://api.firecrawl.dev/v2/extract",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}", "Content-Type": "application/json"},
        json=body, proxies=PROXIES, timeout=120,
    )
    r.raise_for_status()
    return r.json()


def firecrawl_crawl(url, limit=50, include_paths=None, exclude_paths=None):
    """
    【模式 D 专用】整站递归爬取。
    limit：最大页面数（建议 20-100，视站点规模）
    """
    body = {
        "url": url,
        "limit": limit,
        "scrapeOptions": {"formats": ["markdown"], "onlyMainContent": True},
    }
    if include_paths:
        body["includePaths"] = include_paths
    if exclude_paths:
        body["excludePaths"] = exclude_paths
    r = requests.post(
        "https://api.firecrawl.dev/v2/crawl",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}", "Content-Type": "application/json"},
        json=body, proxies=PROXIES, timeout=120,
    )
    r.raise_for_status()
    return r.json()  # 返回 job_id，用 get_crawl_status 轮询

# ════════════════════════════════════════════════════════════════
# JINA — 仅限学术 PDF + Reranker
# ════════════════════════════════════════════════════════════════

def jina_read_academic(url):
    """
    ⚠️ 极度限制：仅用于 arXiv / 学术期刊 / IEEE 页面。
    原因：readerlm-v2 是 LLM 重写层，普通页面会产生生成式幻觉。
    其他所有页面 → 改用 firecrawl_scrape()。
    """
    r = requests.post(
        "https://r.jina.ai/",
        headers={
            "Authorization": f"Bearer {JINA_KEY}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Return-Format": "markdown",
            "X-Engine": "browser",
            "X-Respond-With": "readerlm-v2",      # 仅此场景开启
            "X-Remove-Selector": "nav,footer,aside,script,style",
            "X-With-Links-Summary": "true",
        },
        json={"url": url},
        proxies=PROXIES, timeout=60,
    )
    r.raise_for_status()
    return r.json().get("data", {}).get("content", "")


def jina_rerank(query, documents, top_n=10):
    """
    Jina Reranker v3：候选文档 > 15 篇时，用于精选 Top-N 进行精读。
    documents: list of {"id": str, "text": str}
    """
    r = requests.post(
        "https://api.jina.ai/v1/rerank",
        headers={"Authorization": f"Bearer {JINA_KEY}", "Content-Type": "application/json"},
        json={
            "model": "jina-reranker-v3",
            "query": query,
            "documents": documents,
            "top_n": top_n,
        },
        proxies=PROXIES, timeout=30,
    )
    r.raise_for_status()
    return r.json()
```

---

## 四、模式 A — 标准研究（七步流程）

> **适用**：需要深入研究多个维度的任何主题。这是最常用模式，也是默认模式。

### Step 1：需求解构（Query Decomposition）

将研究主题拆解为独立子查询。

**⚠️ 硬性约束：子查询总数 ≤ 6 个（上界铁律）**

> **为什么必须 ≤ 6？**
> 来源：DeepWeb-Bench (arXiv 2605.21482) + 生产实践共识。
> 子查询越多 → 引入矛盾信息比例越高 → LLM 在综合阶段越容易产生「妥协性幻觉」
> （将来自不同来源的矛盾数字混合编造成一个"合理"结论）。
> 扁平结构（≤ 1 层嵌套），每个子查询自包含、互不依赖。

```
研究主题：[X]
子查询（≤ 6 个，按优先级排列）：
  Q1: [X] 核心机制 / 工作原理           ← 优先级 P0
  Q2: [X] 主流工具 / 竞争格局 2025-2026 ← 优先级 P0
  Q3: [X] 最新进展 / 关键事件            ← 优先级 P1
  Q4: [X] 学术研究 / 基准测试数据        ← 优先级 P1（含"arXiv"关键词送 Exa）
  Q5: [X] 工程实践 / 已知踩坑            ← 优先级 P2（视需要）
  Q6: [X] 中文视角补充（如涉及中国市场）  ← 优先级 P2（加"中文"关键词）
```

### Step 2：并行发现（Parallel Discovery）

Tavily + Exa 同一批次并行发出，不串行等待。

```python
# 通用子查询 → Tavily（广度）
tavily_results = {}
for q in [Q1, Q2, Q3, Q5, Q6]:  # 通用查询
    tavily_results[q] = tavily_search(q)

# 学术子查询 → Exa（语义精准）
exa_results = {}
for q in [Q4] + [含 "paper"/"arxiv"/"research" 的子查询]:
    exa_results[q] = exa_search(q, category="research paper")
```

**参数铁律（质量优先）**：
- Tavily：始终 `search_depth="advanced"` + `include_raw_content="markdown"` + `include_answer="advanced"`
- Exa：始终 `type="deep-reasoning"` + `text.maxCharacters=50000` + `summary=True`
- 实时新闻：`tavily_search(q, topic="news", time_range="week")`
- 中文内容：Tavily 查询词加中文 + `country: china`（通过 `**kwargs` 传入）

### Step 2.5：信源质量过滤门控 ⭐NEW

**在进入 Step 3 之前，对所有检索结果进行质量过滤，丢弃低价值信源。**

```python
# 信源过滤规则
SCORE_THRESHOLD = 0.4  # Tavily score 低于此值直接丢弃

def filter_sources(tavily_results, exa_results):
    valid_urls = []
    
    for q, res in tavily_results.items():
        for item in res.get("results", []):
            score = item.get("score", 0)
            url = item.get("url", "")
            
            # 质量门控：低分 + 已知低质域名过滤
            LOW_QUALITY_DOMAINS = [
                "medium.com/@",  # 个人博客（非官方 medium publication）
                "quora.com", "answers.yahoo.com",  # Q&A 站
                "amazon.com/dp", "buy.", "shop.",  # 电商
            ]
            is_low_quality_domain = any(d in url for d in LOW_QUALITY_DOMAINS)
            
            if score >= SCORE_THRESHOLD and not is_low_quality_domain:
                valid_urls.append((score, url, item.get("title", ""), "tavily"))
    
    for q, res in exa_results.items():
        for item in res.get("results", []):
            url = item.get("url", "")
            valid_urls.append((1.0, url, item.get("title", ""), "exa"))  # Exa 无 score，默认保留
    
    # 去重 + 按分数降序
    seen = set()
    filtered = []
    for score, url, title, source in sorted(valid_urls, reverse=True):
        if url not in seen:
            seen.add(url)
            filtered.append((score, url, title, source))
    
    return filtered  # 返回 (score, url, title, source) 列表
```

### Step 3：智能精读路由（Smart Deep-Read Routing）

**正规则：Firecrawl 优先。Jina 仅用于学术 PDF。**

> 历史版本（旧 SOP）是负规则（「禁止 Jina 读中文」）。
> v2 改为正规则（「除 arXiv/学术期刊，全部用 Firecrawl」），
> 因为 Jina readerlm-v2 的幻觉风险不只限于中文——它是一个 LLM 重写层，
> 任何页面都有被"创造性改写"的风险（REDEEP, ICLR 2025）。

```
URL 精读路由（按顺序判断）
    │
    ├─ 含 "arxiv.org" / "ieeexplore.ieee.org" / "dl.acm.org"
    │   / "pubmed.ncbi" / "nature.com" / "science.org"
    │       → jina_read_academic(url)           ✅ readerlm-v2 学术专用
    │
    └─ 所有其他 URL（含中文/英文/技术博客/新闻/官网）
            → firecrawl_scrape(url)             ✅ Firecrawl 默认
            → 失败时降级：内置 crawlSinglePage   🔀 降级备用
```

```python
ACADEMIC_DOMAINS = [
    "arxiv.org", "ieeexplore.ieee.org", "dl.acm.org",
    "pubmed.ncbi.nlm.nih.gov", "nature.com", "science.org",
    "springer.com", "sciencedirect.com", "semanticscholar.org",
    "openreview.net", "pmlr.press",
]

def smart_deep_read(url):
    """路由到正确的精读工具"""
    is_academic = any(domain in url for domain in ACADEMIC_DOMAINS)
    
    if is_academic:
        # Jina readerlm-v2：学术结构理解能力强，PDF 处理佳
        return {"content": jina_read_academic(url), "method": "jina-readerlm"}
    else:
        # Firecrawl：确定性抓取，无 LLM 重写层，零幻觉注入
        result = firecrawl_scrape(url)
        return {"content": result["markdown"], "method": "firecrawl"}
```

从 Step 2.5 过滤后的 URL 列表中，取 **Top 5-8** 进行精读。
候选 > 15 篇时，先用 `jina_rerank()` 精选 Top 8 再精读。

### Step 3.5：跨源矛盾检测 ⭐NEW

**这是 v2 新增的最重要步骤，直接解决「妥协性幻觉」问题。**

> **什么是妥协性幻觉**：两个权威来源给出矛盾数字，LLM 综合时不报告矛盾，
> 而是自动取均值或选其一，输出一个"合理但无来源支撑"的结论。
> 来源：DeepWeb-Bench 交叉来源协调挑战 + 我们 Wiki Anti-Hallucination §Layer 2。

精读完成后，在进入综合前，向 LLM 发出以下强制提示：

```
【跨源矛盾检测指令】
请审查以上所有检索内容，重点识别以下类型的矛盾：
1. 数字/百分比/日期不一致（如：来源A说 X=80%，来源B说 X=60%）
2. 因果关系相反（如：来源A说 P导致Q，来源B说Q导致P）
3. 事实性描述冲突（如：来源A说产品具备功能F，来源B说不支持）

对每处矛盾，输出：
- 矛盾描述：[具体什么矛盾]
- 来源A：[URL] 说 [原文引用]
- 来源B：[URL] 说 [原文引用]
- 建议：[倾向哪个来源，或建议人工核实]

没有矛盾则输出：「未检测到跨源矛盾，可进入综合阶段。」
```

矛盾项在 Step 6 综合输出时**必须保留双方表述并标注**，不得静默合并。

### Step 4：迭代补充（Gap Filling）

执行 Step 3.5 后，检查知识空白：

- 哪些子查询仍无满意答案？→ 追加 Tavily/Exa 查询（注意：追加后总子查询仍不超过 6 个逻辑批次）
- 中文内容不足？→ Tavily 中文子查询补充
- 发现重要延伸来源？→ 对该 URL 单独调用 `firecrawl_scrape()`

### Step 5：反幻觉验证（Anti-Hallucination Checklist）

综合输出**写入 Wiki 之前**必须逐项核查。**未通过任何一项，不得入库。**

```
【检索侧幻觉检查】
□ 1. 参数记忆隔离：LLM 在综合时是否悄悄使用了参数记忆（未检索到但"知道"的内容）？
      → 强制要求：每条关键结论必须对应至少一条检索结果 URL
      → 无 URL 支撑的内容必须标注 [⚠️ 参数记忆，未经检索验证]

□ 2. 数字 / Benchmark 数据：每个具体数字有原始 URL？
      → 高危：30%/60%/80% 等整数比例，Benchmark 得分（特别容易被捏造）

□ 3. URL 真实性：引用的 URL 是否真实可访问（非 LLM 编造的合理看起来的 URL）？
      → 对所有关键引用 URL，抽查 1-2 个用 firecrawl_scrape 验证页面真实存在

□ 4. 时效标注：时效敏感内容（价格/市场份额/API 状态）标注了数据日期？

□ 5. 矛盾保留：Step 3.5 检测到的矛盾项，在输出中是否保留了双方表述，
      未静默丢弃任何一方？

□ 6. 中文信源交叉验证：涉及中国市场的核心结论，是否用中文来源确认过？

□ 7. Firecrawl 内容异常检查：精读结果字数是否与页面规模相符？
      过短（< 200 字）可能是抓取失败；过长且无结构可能是噪声。
      异常时降级到内置 Web Browsing 重抓比对。

□ 8. 来源等级评估：结论是否建立在 A/B 级信源上？（C/D 级信源不得作为唯一来源）
      A: 学术论文 arXiv / 官方文档 / 一手数据
      B: 知名技术媒体 / 权威博客 / 官方博客
      C: 个人博客 / 内容聚合站
      D: 未知来源 / SEO 垃圾站
```

### Step 6：综合输出（带强制溯源的综合）

综合阶段的 LLM 提示词结构（强制使用）：

```
【综合指令】
你只能基于以下检索到的文档生成回答。

强制规则：
1. 每条关键事实声明后，必须用 [来源: URL] 格式标注来源
2. 如果某信息来自你的参数记忆而非检索结果，必须标注 [⚠️ 参数记忆，建议验证]
3. 检测到矛盾的地方，必须呈现「来源A说X，来源B说Y，建议人工核实」
4. 置信度语言严格遵守三档：
   - 高置信（直接检索支撑）：「根据 [来源]，……」
   - 中置信（间接推断）：「现有资料显示……，但建议确认」
   - 低置信（来源稀少）：「目前资料不充分，建议进一步核实」
5. 禁止：超出检索内容范围的推断、捏造数字、省略来源矛盾
```

### Step 7：结构化入库（Structured Ingest）

按 SCHEMA.md §4.1 + §4.4 规范，经 CONFIRM 门控后写入：

```
raw/methodology/YYYY-MM-DD-{主题}-methodology.md  ← 原始检索结果 + 所有来源 URL
wiki/{category}/{主题}.md                          ← 编译后结构化知识页面
index.md                                           ← 更新目录
log.md                                             ← 追加操作记录
```

---

## 五、模式 B — 快速融合搜索

> **适用**：需要快速获取搜索结果全文，不做深度多维拆解。
> **优势**：一次 API 调用 = 搜索 + 全文，省去 Stage 3 的第二轮 round-trip。

```python
# 一步获取：搜索 + 完整 markdown 正文
results = firecrawl_search(
    query="agentic search retrieval hallucination grounding 2026",
    limit=5,
    with_full_content=True,  # 返回每条结果的完整 markdown
)

for item in results:
    print(f"Title: {item.get('title')}")
    print(f"URL: {item.get('url')}")
    print(f"Content: {item.get('markdown', '')[:500]}")
```

**模式 B 流程**：
```
Firecrawl /search + scrapeOptions（1次调用）
    ↓
直接获得搜索结果 + 每条结果完整正文
    ↓
（可选）并行 Exa 学术补充
    ↓
Step 3.5 矛盾检测 → Step 5 验证 → Step 6 综合
```

**适用场景**：
- 快速了解某产品/技术的最新状态
- 需要的信源相对集中（不超过 5 个来源）
- 研究深度不需要多维拆解

---

## 六、模式 C — 结构化多页萃取

> **适用**：从一批已知 URL 或某个域名下，批量提取结构化字段（竞品对比、定价表、功能列表）。
> **这是三工具时代完全缺失的新能力。**

```python
from pydantic import BaseModel
from typing import List, Optional

# 定义目标数据结构
class ToolProfile(BaseModel):
    name: str
    pricing_per_1k_queries: Optional[str]
    free_tier: Optional[str]
    key_features: List[str]
    best_for: str
    limitations: Optional[str]

# 跨多个 URL 同时提取
result = firecrawl_extract(
    urls=[
        "https://tavily.com/pricing",
        "https://exa.ai/pricing",
        "https://www.firecrawl.dev/pricing",
        "https://docs.perplexity.ai/docs/pricing",
    ],
    prompt="提取每个 AI 搜索 API 工具的定价信息、免费额度、核心功能和最适合的使用场景",
    schema={
        "type": "object",
        "properties": {
            "tools": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "pricing_per_1k": {"type": "string"},
                        "free_tier": {"type": "string"},
                        "best_for": {"type": "string"},
                    }
                }
            }
        }
    }
)

print(result["data"])  # 直接得到结构化 JSON，无需手动综合
```

**模式 C 流程**：
```
确定目标 URL 池（Tavily/Exa 发现 或 已知 URL）
    ↓
Firecrawl /extract + JSON Schema（1次调用）
    ↓
直接获得结构化 JSON，跳过手动综合步骤
    ↓
Step 5 验证关键字段 → Step 7 入库
```

**适用场景**：
- 竞品定价/功能横向对比（一键生成对比表格）
- 批量提取公司信息（成立时间/融资/团队规模）
- 从文档站抽取 API 参数表

---

## 七、模式 D — 整站深度研究

> **适用**：需要完整读取一个产品文档站、公司官网或 GitHub Wiki，将全部页面纳入研究范围。
> **这是三工具时代完全缺失的新能力。**

```python
# 爬取整个文档站（限 50 页以内）
job = firecrawl_crawl(
    url="https://docs.firecrawl.dev",
    limit=50,
    include_paths=["/features/", "/api-reference/", "/integrations/"],  # 可选：只爬特定路径
    exclude_paths=["/changelog/", "/blog/"],  # 可选：排除不需要的路径
)

job_id = job.get("id")

# 轮询状态（脚本中用 while 循环）
import time
while True:
    status_r = requests.get(
        f"https://api.firecrawl.dev/v2/crawl/{job_id}",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}"},
        proxies=PROXIES, timeout=30,
    )
    status = status_r.json()
    if status.get("status") == "completed":
        pages = status.get("data", [])
        break
    elif status.get("status") == "failed":
        raise Exception(f"Crawl failed: {status}")
    time.sleep(10)
```

**模式 D 流程**：
```
Firecrawl /crawl（异步任务）
    ↓
轮询 status → 获取所有页面 markdown
    ↓
（可选）Tavily /Exa 获取外部背景信息
    ↓
LLM 全量综合（基于完整站点内容）
    ↓
Step 3.5 矛盾检测 → Step 5 验证 → Step 7 入库
```

**适用场景**：
- 深度研究某产品时，读完其全部文档
- 竞品分析时，完整抓取竞品官网
- 将某机构的知识库全量入库

---

## 八、Windows 调用标准（脚本模式）

所有 API 调用均通过 Python 脚本执行，不直接在对话中调用。

### ✅ 执行前自检 Checklist（写脚本前必须逐项确认）

> **本 Checklist 是 §八 的强制前置步骤。** LLM 开始写 `research_task.py` 前，必须逐项过完。

| # | 检查项 | 风险等级 |
|---|--------|---------|
| □ 1 | `C:\Temp\research_out.txt` 旧文件已删除（避免 wait_done.py 读到旧 DONE） | 中 |
| □ 2 | `research_task.py` 最后两行是 `log("=== ALL DONE ===")` + `save()` | 高 |
| □ 3 | Step 2 的 `runCommand` 已设置 `run_in_background=True` | 高 |
| □ **4** | **Step 3 的 `runCommand` 未设置 `run_in_background`（不传此参数）** | 🔴 最高频错误 |
| □ 5 | Step 2 与 Step 4 之间只有**一次** `runCommand`（即 wait_done.py） | 高 |
| □ 6 | Step 4 使用 `readFile` 而非任何轮询手段 | 高 |

---

### 四步标准流程

| Step | 操作 | 命令 |
|------|------|------|
| 1 | 写入研究脚本 | `writeFile → C:\Temp\research_task.py` |
| 2 | 后台启动 | `runCommand(run_in_background=True, timeout=600000)` |
| 3 | 阻塞等待 | `runCommand(wait_done.py, 非后台, timeout=600000)` |
| 4 | 读取结果 | `readFile → C:\Temp\research_out.txt` |

### 研究脚本约定（必须遵守）

```python
# C:\Temp\research_task.py — 脚本结构约定
import requests, json, time, os

OUT = r"C:\Temp\research_out.txt"
lines = []
def log(msg): print(str(msg), flush=True); lines.append(str(msg))
def save():
    with open(OUT, "w", encoding="utf-8") as f: f.write("\n".join(lines))

# ── 研究逻辑 ───────────────────────────────────────────────
# ... 调用 tavily_search / exa_search / firecrawl_scrape 等 ...

# ── 结束标记（最后一行，必须有）────────────────────────────
log("=== ALL DONE ===")
save()
```

**约定铁律**：
- 所有输出写入 `C:\Temp\research_out.txt`（禁止自定义文件名）
- 脚本最后一行输出必须是 `log("=== ALL DONE ===")`
- 不在脚本内直接 `print` 到 stdout（会被 log 重定向丢失）

### 等待脚本（强制模板，禁止修改）

```python
# C:\Temp\wait_done.py — 直接复制，不要修改
import time, os
OUT = r"C:\Temp\research_out.txt"
MAX_WAIT = 600
start = time.time()
while time.time() - start < MAX_WAIT:
    if os.path.exists(OUT):
        with open(OUT, "r", encoding="utf-8") as f:
            if "=== ALL DONE ===" in f.read():
                print("DONE"); break
    time.sleep(5)
    print(f"  {int(time.time()-start)}s...", flush=True)
else:
    print("TIMEOUT")
```

调用：`runCommand("python C:\Temp\wait_done.py", timeout=620000)`（**不加 run_in_background**）

> ### 🚨 Step 3 高频错误警示（历史实测违规来源）
>
> **`wait_done.py` 必须前台阻塞执行，绝对禁止加 `run_in_background=True`。**
>
> **后果链**：一旦 Step 3 被后台化 →
> 1. 阻塞失效，LLM 立刻进入「任务还在跑但不知道何时结束」的未定义状态
> 2. LLM 面对不确定性，倾向使用**已被明确禁止**的 `getCommandOutput` 轮询补救
> 3. 连锁触发第二条禁令，两个错误叠加，上下文被污染
>
> **出错后的唯一合法动作**：立即停止所有工具调用 → 向用户报告「发生了什么、在哪一步偏离了 SOP」→ 等待用户决策。
> 禁止用任何其他被禁止的手段自行补救。

### ⚠️ 等待阶段四条禁令

> Step 2（后台启动）和 Step 4（读取结果）之间，**只允许恰好一次 runCommand**（即 wait_done.py）。

| 禁止行为 | 原因 |
|---------|------|
| ❌ `getCommandOutput` 轮询 stdout | 增量碎片，无法判断完成，污染上下文 |
| ❌ `readFile` 反复检查进度 | 浪费对话轮次，结果不可靠 |
| ❌ `timeout /t` + `type` CMD 组合 | 输出经常为空，不可靠 |
| ❌ 任何"等一会儿再看看"行为 | wait_done.py 阻塞等待是唯一合法等待方式 |
| ❌ 用禁止手段补救已发生的错误 | 叠加违规，上下文双重污染，问题更难恢复 |

### 🛑 错误恢复协议（任一步骤偏离 SOP 后的唯一合法流程）

> **规范没有「两害相权选其一」的空间。** 任何步骤偏离 SOP，立即执行以下协议：

```
偏离检测
    ↓
Step R1：立即停止所有工具调用（不再发出任何 runCommand / readFile / getCommandOutput）
    ↓
Step R2：向用户报告
         - 在哪一步发生了偏离（Step 2 / Step 3 / Step 4）
         - 做了什么不该做的操作
         - 当前系统状态（脚本是否还在跑、文件是否存在）
    ↓
Step R3：等待用户决策
         - 用户说「重新执行」→ 删旧文件，从 Step 1 重来
         - 用户说「直接读文件」→ 做一次 readFile 检查末尾是否有 ALL DONE
         - 用户说「放弃」→ 终止任务，log.md 记录中止原因
```

**禁止自行判断「用禁止手段补救」**：即使某个禁止手段在当前情境下看起来「无害」，也不允许使用。规范的价值在于可预期性，允许例外会使整个禁令体系失效。

---

## 九、场景速查与决策树

### 完整决策树

```
需要外部信息？
    │
    ├─ Wiki 中已有完整答案
    │       → 直接读取 wiki 页面，不调 API
    │
    ├─ 单一快速事实确认
    │       → 内置 Web Browsing 1-2 次
    │
    ├─ 已知具体 URL，要精读
    │       ├─ arXiv / 学术期刊 → jina_read_academic()
    │       └─ 其他所有 URL   → firecrawl_scrape()
    │
    ├─ 需要快速搜索 + 全文（不深拆）
    │       → 【模式 B】firecrawl_search(with_full_content=True)
    │
    ├─ 从多 URL 提取结构化字段（对比表/定价/功能）
    │       → 【模式 C】firecrawl_extract(urls, schema)
    │
    ├─ 需要读完整个文档站 / 官网
    │       → 【模式 D】firecrawl_crawl()
    │
    └─ 系统性深度研究（≥3 个维度，需引用报告）
            → 【模式 A】完整七步流程
```

### 工具参数速查（质量优先版）

| 场景 | 工具 | 关键参数 |
|------|------|---------|
| 通用网页深度研究 | Tavily | `depth="advanced"`, `max_results=10`, `include_raw_content="markdown"` |
| 实时新闻追踪 | Tavily | `topic="news"`, `time_range="week"` |
| 中文内容 | Tavily | 中文查询词, `country="china"` |
| 学术论文精准检索 | Exa | `category="research paper"`, `type="deep-reasoning"` |
| 语义发现（无关键词）| Exa | `type="deep-reasoning"`, `numResults=15` |
| 普通页面精读（主力）| Firecrawl | `onlyMainContent=True`, `formats=["markdown"]` |
| 搜索+全文一步 | Firecrawl | `/search` + `scrapeOptions` |
| 结构化跨URL萃取 | Firecrawl | `/extract` + `schema` |
| 整站递归爬取 | Firecrawl | `/crawl`, `limit=50` |
| 学术 PDF 精读 | Jina readerlm | `use_readerlm=True`（严格限于学术域名）|
| 候选文档重排序 | Jina Reranker | `model="jina-reranker-v3"`, `top_n=10` |

---

## 十、注意事项 / Tips & Gotchas

### 🔴 API Key 安全
- 每次调用前从 `retrieval-api-keys.md` 读取，不在对话输出中展示 Key 值
- Key 文件路径：`D:\Nextcloud\EngPath\AIWorkWiki\retrieval-api-keys.md`

### ⚠️ Jina readerlm-v2 幻觉风险（v2 版本重新定性）

> **v2 关键认知更新**：旧 SOP 把 readerlm-v2 的问题定性为「中文内容聚合站禁用」。
> v2 重新定性为：**readerlm-v2 本质是一个 LLM 重写层，所有普通页面都有生成式幻觉注入风险**，
> 而不只是中文内容。
>
> 根本原因（REDEEP, ICLR 2025）：LLM 在处理检索内容时，会将「外部检索到的知识」
> 和「参数记忆中已有的知识」混合，无法区分，导致输出内容可能已经过 LLM 改写/插值。
>
> **正确做法**：readerlm-v2 仅用于 arXiv/学术期刊 PDF（这类内容有清晰结构，
> 且 readerlm 的学术理解能力有实际价值）。其他所有页面用 Firecrawl（确定性抓取）。

### 🎯 Firecrawl 最佳实践

- 始终开启 `onlyMainContent: True`（过滤导航/侧栏/页脚/广告）
- 批量精读多个 URL，用 `batch_scrape` 而非多次单独调用（节省时间）
- `/extract` 比 `/scrape` + 手动综合更可靠：直接用 schema 约束输出格式
- `/crawl` 要谨慎设置 `limit`（默认 10000，建议明确设 20-100）
- Firecrawl 对 JavaScript 渲染站点表现良好（Playwright 内核）

### 🌐 中文内容保障策略

1. Tavily：发送中文查询词 + `country="china"` 参数
2. Firecrawl：中文页面精读表现与英文同等（v2 验证通过）
3. 关键中文事实：额外发一条中文子查询并交叉验证

### 📊 何时使用 Exa 而非 Tavily

| 场景 | 选 Exa | 选 Tavily |
|------|--------|---------|
| 学术论文 / arXiv | ✅ | — |
| 技术规格 / 代码 | ✅ | — |
| 概念语义搜索（无精确关键词）| ✅ | — |
| 最新新闻 / 动态 | — | ✅ |
| 通用宽泛查询 | — | ✅ |
| 中文内容 | — | ✅ |
| 公司/人物信息 | ✅（category="company"）| — |

### ⚡ 并行执行原则
- Tavily + Exa 的 Stage 2 **同一批次并行发出**，不串行等待
- Firecrawl 多页精读可用 `batch_scrape` 一次性发出
- 并行是减少总耗时的最关键单项优化

---

## 十一、与现有 Wiki 工作流的关系

| 工作流页面 | 关系说明 |
|-----------|---------|
| `[[AI-Driven-External-Retrieval]]` | 本 SOP 是其**具体实现版本**，将「AI 主动检索」落地为具体 API 调用 |
| `[[Deep-Research-Methodology]]` | 本 SOP 实现了 Plan-Execute-Reflect 四阶段流水线，并做了工程强化 |
| `[[INGEST-Workflow]]` | Step 7 对接入库工作流的路径 B（AI 主动检索后入库）|
| `[[Retrieval-Tools-Comparison]]` | 四工具详细对比矩阵，辅助场景决策 |
| `[[Anti-Hallucination-Engineering]]` | Step 3.5 / Step 5 / Step 6 的理论依据来自此页 §Layer 1-4 |
| `[[Firecrawl-API]]` | Firecrawl 四端点完整指南（/scrape /search /extract /crawl）|
| `[[Windows-API-Call-Guide]]` | Windows 平台调用禁忌与唯一可靠方案 |

---

## Sources / 来源

**工具文档**
- [Firecrawl Official Docs](https://docs.firecrawl.dev/) — /scrape /search /extract /crawl 端点规范
- [Firecrawl CrawlBench Benchmark](https://www.firecrawl.dev/blog/crawlbench-llm-extraction) — 96% coverage, F1 0.638, ROUGE 93.7%
- [Firecrawl vs Jina Reader 2026](https://use-apify.com/blog/firecrawl-vs-jina-reader-2026) — 独立对比测试
- [Tavily API Reference](https://docs.tavily.com/documentation/api-reference/introduction)
- [Exa Search API Guide](https://docs.exa.ai/docs/reference/search-api-guide)
- [Jina AI Docs](https://docs.jina.ai/)

**学术依据**
- [REDEEP: Detecting Hallucination in RAG via Mechanistic Interpretability](https://arxiv.org/pdf/2410.11414) — ICLR 2025；参数记忆 vs 外部检索解耦
- [SoK: Agentic RAG Taxonomy](https://arxiv.org/html/2603.07379v1) — Agentic RAG 系统性综述
- [DeepWeb-Bench: Cross-Source Evidence](https://arxiv.org/html/2605.21482) — 跨源矛盾协调挑战
- [ConfRAG: Confidence-Guided Retrieval](https://arxiv.org/pdf/2506.07309) — 置信度驱动检索触发机制
- [Rowen: Adaptive RAG for Hallucination Mitigation](https://arxiv.org/html/2402.10612v3) — 一致性检测模块
- [Agentic Search in 2026: Benchmark 8 APIs](https://aimultiple.com/agentic-search) — 8大检索 API Benchmark
- `wiki/concepts/Anti-Hallucination-Engineering.md` — 五层工程防御体系
- `wiki/concepts/Deep-Research-Methodology.md` — Deep Research 四阶段流水线
- `wiki/concepts/RAG-System-Design.md` — Layer 1-4 检索质量控制机制

**v2 版本对比 v1 主要变更**
1. 工具矩阵：三工具 → 四工具（Firecrawl 升级为精读主力）
2. 前置：新增任务类型路由（A/B/C/D 四模式）
3. Step 1：子查询硬性上界 ≤ 6（防矛盾信息涌入）
4. Step 2.5：新增信源质量过滤门控（score < 0.4 丢弃）
5. Step 3：精读路由从负规则（禁止 Jina 中文）改为正规则（Firecrawl 优先）
6. Step 3.5：新增跨源矛盾检测（妥协性幻觉防御）
7. Step 5：反幻觉清单新增「参数记忆隔离」+ URL 真实性验证
8. Step 6：综合提示词强制要求溯源标注 + 参数记忆标记
9. 新增模式 B/C/D（快速融合 / 结构化萃取 / 整站深研）
