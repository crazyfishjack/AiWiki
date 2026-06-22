---
title: "Firecrawl API 工具指南"
category: tool
tags: [firecrawl, scrape, search, extract, crawl, retrieval, anti-hallucination, web-data, RAG, deep-research, fallback, cost-aware, v2.1]
sources:
  - https://docs.firecrawl.dev/introduction
  - https://docs.firecrawl.dev/features/scrape
  - https://docs.firecrawl.dev/features/search
  - https://docs.firecrawl.dev/features/extract
  - https://docs.firecrawl.dev/features/crawl
  - https://www.firecrawl.dev/blog/crawlbench-llm-extraction
  - https://use-apify.com/blog/firecrawl-vs-jina-reader-2026
related:
  - "[[Three-Tool-Retrieval-SOP]]"
  - "[[Jina-AI-API]]"
  - "[[Retrieval-Tools-Comparison]]"
  - "[[Windows-API-Call-Guide]]"
  - "[[Anti-Hallucination-Engineering]]"
last_compiled: 2026-06-16
confidence: high
language: zh-CN+en
discovery:
  one_liner: "四端点完整代码示例 + 与 Jina 路由（v2.1：/extract·/crawl 独占主力 + 精读降级后备，精读主力为 Jina 默认模式）+ 成本/计费"
  topic_cluster: ai-concepts
  load_when:
    - "需要调用 Firecrawl API 实现单页精读、搜索或整站爬取时"
    - "设计 RAG 检索层选型时，需判断 Firecrawl 与 Jina Reader 的使用边界"
    - "排查 LLM 检索结果被改写或内容幻觉注入问题时"
  key_outputs:
    - "scrape / search / extract / crawl 四端点可直接复用的 Python 代码"
    - "Firecrawl vs Jina 能力边界路由（v2.1：普通页面 Jina 默认主力→失败降级 Firecrawl；学术→Jina readerlm；结构化/整站→Firecrawl 独占）"
    - "CrawlBench 基准数据（96%/F1 0.638/ROUGE 93.7%）及其为 Firecrawl 自家基准的利益倾向提示"
    - "Firecrawl 成本与定位（月订阅 credits 不滚存、降本策略、何时仍必须用 Firecrawl）"
    - "onlyMainContent / limit / timeout 等关键参数推荐值与陷阱说明"
  estimated_tokens: 3400
  sections:
    - heading: "What It Is / 是什么"
      one_liner: "Firecrawl 定位（v2.1：/extract·/crawl 独占主力 + 精读降级后备）、Base URL 与 API Key"
      lines: [4, 14]
      tokens: 180
    - heading: "Firecrawl vs Jina Reader：能力边界与选型（v2.1 修正）"
      one_liner: "v2.1 修正两处偏差（论据滑坡 + 自家基准）；能力/成本对比表，定位降级后备 + extract/crawl 独占"
      lines: [16, 36]
      tokens: 400
    - heading: "1. `/scrape` — 单页精读降级后备（v2.1）"
      one_liner: "降级后备精读 + 结构化/问答的 Python 代码、formats 表、关键参数及批量调用"
      lines: [40, 122]
      tokens: 700
    - heading: "2. `/search` — 搜索+全文一步获取（模式 B）"
      one_liner: "搜索+全文一次 API 调用代码及高级过滤参数（域名/时间/类别）"
      lines: [124, 171]
      tokens: 400
    - heading: "3. `/extract` — 结构化多页萃取（模式 C）"
      one_liner: "跨 URL 按 JSON Schema 批量提取结构化数据的代码与适用场景（Firecrawl 独占）"
      lines: [173, 232]
      tokens: 450
    - heading: "4. `/crawl` — 整站递归爬取（模式 D）"
      one_liner: "整站爬取异步轮询代码及 limit / includePaths 等关键参数（Firecrawl 独占）"
      lines: [234, 309]
      tokens: 500
    - heading: "与 Jina Reader 的职能边界"
      one_liner: "v2.1 路由：普通页面 Jina 默认主力→失败降级 Firecrawl；学术 Jina readerlm；结构化/整站 Firecrawl 独占"
      lines: [311, 340]
      tokens: 280
    - heading: "注意事项 / Tips & Gotchas"
      one_liner: "质量最大化、JS 渲染、/extract 异步陷阱、成本与定位（v2.1）及 SOP 脚本集成代码"
      lines: [342, 375]
      tokens: 350
    - heading: "Benchmark 数据"
      one_liner: "CrawlBench 5 项指标 + 利益相关披露（Firecrawl 自家基准，审慎采信）"
      lines: [377, 389]
      tokens: 180
---

# Firecrawl API 工具指南

## What It Is / 是什么

Firecrawl 是一个面向 AI Agent 的 **全栈 Web 数据 API**，提供搜索、单页精读、结构化萃取、整站爬取四大能力。YC 孵化，2025 年成长为 RAG/Agent 工作流的主流数据层工具。

**在四工具检索 SOP v2.1 中的定位（2026-06-16 修正）**：**结构化萃取 `/extract` + 整站爬取 `/crawl` 的独占主力 + 单页精读的降级后备**。普通页面精读主力已改由 **Jina Reader 默认模式**（确定性、按需计费）承担；Firecrawl `/scrape` 仅在 Jina 失败（取空/超时/JS 重渲染/反爬）时作为 Playwright 兜底。`/extract`（结构化）与 `/crawl`（整站）是 Firecrawl 独占、Jina 不具备的能力，仍为模式 C/D 主力。

**API Key**：见 `retrieval-api-keys.md`（`FIRECRAWL_API_KEY`）
**Base URL**：`https://api.firecrawl.dev/v2`
**认证**：`Authorization: Bearer {KEY}`

---

## Firecrawl vs Jina Reader：能力边界与选型（v2.1 修正）

> **v2.1 修正说明**：旧版本此章标题为「为什么选 Firecrawl 而非 Jina Reader」，论证 Firecrawl 做精读主力。该论证有两处偏差，v2.1 已纠正——精读主力改回 Jina Reader 默认模式，Firecrawl 转为降级后备 + `/extract`·`/crawl` 专用。
>
> 偏差一（论据滑坡）：把「Jina = readerlm-v2 幻觉」套到整个 Jina，但 **Jina Reader 默认模式**（不开 readerlm-v2）是 turndown + readability 纯规则提取，与 Firecrawl **同属确定性、零生成式幻觉**；幻觉只来自可选的 readerlm-v2。
> 偏差二（利益相关基准）：下表 96%/F1 0.638/ROUGE 93.7% 来自 **Firecrawl 自家 CrawlBench**（[firecrawl.dev/blog](https://www.firecrawl.dev/blog/crawlbench-llm-extraction)），非中立第三方，存在选择性披露倾向；多家第三方实测两者默认模式提取质量接近。

| 维度 | Firecrawl `/scrape` | Jina Reader 默认模式 | Jina readerlm-v2 |
|------|--------------------|--------------------|-----------------|
| **提取机制** | 确定性抓取 + 清洗（无 LLM）| 确定性 turndown+readability（无 LLM）| **LLM 重写层**（幻觉风险）|
| **生成式幻觉** | **零** | **零** | 有（会插值）|
| **JS 重渲染/反爬** | ✅ 强（Playwright）← 降级理由 | ⚠️ 较弱（basic rendering）| — |
| **噪声过滤** | ✅ `onlyMainContent` | ✅ readability + Remove-Selector | — |
| **CrawlBench 覆盖率/F1/ROUGE** | 96% / 0.638 / 93.7%（⚠️ 自家基准）| 自家口径标注"更低"（未独立复核）| — |
| **成本模型** | 固定月订阅，credits 不滚存 | **按 token 付费，失败不扣费** ← 主力理由 | 约 3x token |
| **中文内容** | ✅ 同等处理 | ✅ 同等处理 | ❌ 高概率幻觉（ACRI<40）|
| **学术 PDF** | 一般 | 一般 | **✅ 结构理解强** ← readerlm-v2 保留场景 |

**关键结论（v2.1）**：普通页面精读用 **Jina Reader 默认模式**（确定性、零幻觉、按需计费、更省）为主力；**Firecrawl `/scrape` 作降级后备**——当 Jina 默认模式取空/超时或遇 JS 重渲染/反爬站时，用 Firecrawl 的 Playwright + 代理兜底（同样确定性、零生成式幻觉）。Firecrawl 的不可替代价值在 `/extract`（结构化萃取）与 `/crawl`（整站爬取），是 Jina 不具备的独占能力。readerlm-v2 只在 arXiv/学术 PDF 显式开启。

---

## 四大端点详解

### 1. `/scrape` — 单页精读降级后备（v2.1）

**定位**：v2.1 中精读主力是 Jina Reader 默认模式；`/scrape` 仅在 Jina 失败（取空/超时/JS 重渲染/反爬）时作为 Playwright 兜底。下方代码同时承载 `/scrape` 的结构化（json schema）与问答（question）能力。

```python
import requests

FIRECRAWL_KEY = "fc-..."  # 从 retrieval-api-keys.md 读取
PROXIES = {"http": "http://127.0.0.1:10808", "https": "http://127.0.0.1:10808"}

def firecrawl_scrape(url, with_json_schema=None, question=None):
    """
    单页精读降级后备（v2.1）：常规精读先走 jina_read() 默认模式，失败再用本函数兜底。
    ✅ 降级触发：Jina 取空/超时、JS 重渲染、反爬站（Playwright 突破）
    ✅ 独占能力：with_json_schema 结构化提取、question 页面问答
    ❌ 不适用：arXiv 学术 PDF（改用 jina_read_academic）
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
```

#### 支持的 formats

| format | 说明 | 典型用途 |
|--------|------|---------|
| `"markdown"` | 清洁 Markdown 全文（**默认首选**）| 普通精读 |
| `{"type": "json", "schema": {...}}` | 按 schema 提取结构化字段 | 萃取特定信息 |
| `{"type": "question", "question": "..."}` | 对页面直接提问，返回答案 | 快速问答 |
| `{"type": "highlights", "query": "..."}` | 返回与 query 最相关的段落片段 | 精准摘要 |
| `"screenshot"` | 页面截图 | 调试/可视化 |
| `"links"` | 页面所有出链 | 发现延伸来源 |

#### 关键参数

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| `onlyMainContent` | `True` | **必须开启**，过滤导航/页脚/广告 |
| `timeout` | `30000` | 毫秒，JS 渲染页面需要较长时间 |
| `maxAge` | `0`（实时）| 绕过缓存获取最新内容 |

#### 批量精读（多 URL）

```python
def firecrawl_batch_scrape(urls):
    """批量精读，比多次单独调用高效"""
    r = requests.post(
        "https://api.firecrawl.dev/v2/batch/scrape",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}", "Content-Type": "application/json"},
        json={
            "urls": urls,
            "formats": ["markdown"],
            "onlyMainContent": True,
        },
        proxies=PROXIES, timeout=120,
    )
    r.raise_for_status()
    return r.json()
```

---

### 2. `/search` — 搜索+全文一步获取（模式 B）

**定位**：SOP 模式 B 核心，一次 API 调用同时完成搜索和内容获取，省去 round-trip。

```python
def firecrawl_search(query, limit=5, with_full_content=True):
    """
    【SOP 模式 B 专用】搜索 + 全文一步到位。
    with_full_content=True：每条结果同时返回完整 markdown 正文。
    """
    scrape_opts = {
        "formats": ["markdown"],
        "onlyMainContent": True
    } if with_full_content else {}

    r = requests.post(
        "https://api.firecrawl.dev/v2/search",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}", "Content-Type": "application/json"},
        json={
            "query": query,
            "limit": limit,
            "scrapeOptions": scrape_opts,
        },
        proxies=PROXIES, timeout=60,
    )
    r.raise_for_status()
    return r.json().get("data", [])

# 使用示例
results = firecrawl_search("四工具检索 SOP 反幻觉最佳实践 2026", limit=5)
for item in results:
    print(f"Title: {item.get('title')}")
    print(f"URL:   {item.get('url')}")
    print(f"Content preview: {item.get('markdown', '')[:300]}")
```

#### 搜索高级参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `sources` | 搜索类型 | `["web", "news"]` |
| `categories` | 垂直类别 | `["github", "research"]` |
| `includeDomains` | 限定域名 | `["arxiv.org", "github.com"]` |
| `excludeDomains` | 排除域名 | `["example.com"]` |
| `tbs` | 时间范围 | `"qdr:d"`（过去1天）/ `"qdr:w"` / `"qdr:m"` |
| `location` | 地区 | `"China"` |

---

### 3. `/extract` — 结构化多页萃取（模式 C）

**定位**：SOP 模式 C 核心。从一批 URL 或整个域名按 schema 批量提取结构化数据，三工具时代完全缺失的能力。

```python
def firecrawl_extract(urls, prompt, schema=None):
    """
    【SOP 模式 C 专用】跨 URL 结构化萃取。
    urls 支持通配符：["https://example.com/*"]
    schema 为 JSON Schema dict（推荐），不传则按 prompt 自由提取。
    """
    body = {"urls": urls, "prompt": prompt}
    if schema:
        body["schema"] = schema

    r = requests.post(
        "https://api.firecrawl.dev/v2/extract",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}", "Content-Type": "application/json"},
        json=body,
        proxies=PROXIES, timeout=120,
    )
    r.raise_for_status()
    return r.json()

# 使用示例：从多个竞品页面一次性提取定价信息
result = firecrawl_extract(
    urls=[
        "https://tavily.com/pricing",
        "https://exa.ai/pricing",
        "https://www.firecrawl.dev/pricing",
    ],
    prompt="提取每个工具的定价、免费额度、最适合的使用场景",
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
print(result["data"])  # 直接得到结构化 JSON
```

**适用场景**：
- 竞品定价 / 功能横向对比（一键生成对比表）
- 批量提取公司信息（成立时间 / 融资 / 团队规模）
- 从文档站批量抽取 API 参数表
- 产品发布页提取版本更新记录

---

### 4. `/crawl` — 整站递归爬取（模式 D）

**定位**：SOP 模式 D 核心。递归爬取一个网站的全部（或指定路径下的）页面，三工具时代完全缺失的能力。

```python
import time

def firecrawl_crawl_and_wait(url, limit=50, include_paths=None, exclude_paths=None):
    """
    【SOP 模式 D 专用】整站递归爬取，同步等待完成后返回所有页面。
    limit：最大页面数，建议 20-100
    """
    body = {
        "url": url,
        "limit": limit,
        "scrapeOptions": {"formats": ["markdown"], "onlyMainContent": True},
    }
    if include_paths:
        body["includePaths"] = include_paths   # 如 ["/docs/", "/api-reference/"]
    if exclude_paths:
        body["excludePaths"] = exclude_paths   # 如 ["/blog/", "/changelog/"]

    # 启动爬取任务
    r = requests.post(
        "https://api.firecrawl.dev/v2/crawl",
        headers={"Authorization": f"Bearer {FIRECRAWL_KEY}", "Content-Type": "application/json"},
        json=body, proxies=PROXIES, timeout=60,
    )
    r.raise_for_status()
    job_id = r.json().get("id")

    # 轮询直到完成
    while True:
        status_r = requests.get(
            f"https://api.firecrawl.dev/v2/crawl/{job_id}",
            headers={"Authorization": f"Bearer {FIRECRAWL_KEY}"},
            proxies=PROXIES, timeout=30,
        )
        status = status_r.json()
        state = status.get("status", "")
        completed = status.get("completed", 0)
        total = status.get("total", "?")
        print(f"  Crawl status: {state} ({completed}/{total})", flush=True)

        if state == "completed":
            return status.get("data", [])
        elif state == "failed":
            raise Exception(f"Crawl failed: {status}")
        time.sleep(10)

# 使用示例：爬取 Firecrawl 全部文档
pages = firecrawl_crawl_and_wait(
    url="https://docs.firecrawl.dev",
    limit=50,
    include_paths=["/features/", "/api-reference/"],
    exclude_paths=["/changelog/"],
)
for page in pages:
    print(f"  {page.get('metadata', {}).get('sourceURL')} ({len(page.get('markdown',''))} chars)")
```

#### `/crawl` 关键参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `limit` | int | 最大爬取页数（默认 10000，**务必手动设置**）|
| `maxDiscoveryDepth` | int | 最大链接发现深度（不设则无限）|
| `includePaths` | `string[]` | 只爬匹配的路径（正则）|
| `excludePaths` | `string[]` | 排除匹配的路径（正则）|
| `crawlEntireDomain` | bool | `false` 只爬子路径；`true` 爬整个域名 |
| `allowSubdomains` | bool | 是否跟随子域名链接 |
| `sitemap` | string | `"include"`（默认）/ `"skip"` / `"only"` |

⚠️ **`limit` 必须明确设置**：默认值 10000 会爬取大型站点的全部页面，耗时极长。建议先从 20-50 开始。

---

## 与 Jina Reader 的职能边界

> **正规则（v2.1 SOP）**：普通页面精读主力 = Jina 默认模式，失败降级 Firecrawl；学术 PDF = Jina readerlm-v2；结构化/整站 = Firecrawl 独占。

```
URL 精读路由（v2.1）
    │
    ├─ arxiv.org / ieeexplore.ieee.org / dl.acm.org
    │  pubmed / nature.com / science.org / springer.com
    │  sciencedirect.com / openreview.net / pmlr.press
    │       → jina_read_academic(url)    ← readerlm-v2，学术结构理解强
    │
    └─ 所有其他 URL（中文/英文/技术/新闻/官网）
            → jina_read(url)             ← 主力：Jina 默认模式（确定性·按需）
            → 失败降级 firecrawl_scrape(url)  ← Playwright/反爬兜底
```

| 能力 | Firecrawl | Jina Reader |
|------|--------------------|--------------| 
| 普通页面精读 | 降级后备（`/scrape`，JS/反爬兜底）| ✅ **主力**（默认模式，确定性、按需）|
| 中文页面 | ✅ 降级时同等处理 | ✅ 默认模式同等处理（仅 readerlm-v2 有幻觉风险）|
| arXiv/学术 PDF | ⚠️ 一般 | ✅ **readerlm-v2 优势** |
| 结构化萃取 | ✅ **独占** `/extract`+schema | ❌ 不支持 |
| 整站爬取 | ✅ **独占** `/crawl` | ❌ 不支持 |
| 搜索+内容一步 | ✅ `/search`+scrapeOptions | ⚠️ 另有 `s.jina.ai` Search API |
| Reranker | ❌ | ✅ `jina-reranker-v3` |
| Embeddings | ❌ | ✅ `jina-embeddings-v5` |
| 成本模型 | 固定月订阅、credits 不滚存 | 按 token、失败不扣费 |

---

## 注意事项 / Tips & Gotchas

### 🎯 质量最大化
- 始终开启 `onlyMainContent: True`（过滤 nav/footer/ads）
- 精读多个 URL 用 `batch_scrape` 而非多次单独调用（节省时间 + 配额）
- `/extract` 比手动综合更可靠：schema 约束直接消除格式幻觉
- `/crawl` 务必明确设 `limit`（默认 10000 会爬满整站）

### 🌐 JavaScript 渲染
- Firecrawl 内置 Playwright，对 JS 渲染站点（SPA/React）表现良好
- 静态页面：`timeout: 15000` 即可；JS 重页面：`timeout: 30000`

### 🔴 陷阱：`/extract` 异步任务
- `/extract` 是异步的，调用后返回 `job_id`，需轮询 `get_extract_status(id)`
- 与 `/crawl` 类似，都需要轮询状态

### 💰 成本与定位（v2.1）
- **计费**：Firecrawl 是**固定月订阅**、按 credits，**月度 credits 不滚存**（到月清零）；突发式检索易浪费或超额（实测精读 `/scrape` 曾占用量约 99%、撑爆订阅）。
- **降本策略**：把高频单页精读迁到按需计费的 Jina 默认模式后，Firecrawl 仅留 `/extract`·`/crawl`（占用极低）+ 偶发精读降级 → 订阅档位可下调，甚至回落免费/低档位保活。
- **何时仍必须用 Firecrawl**：① 结构化萃取 `/extract`（schema 约束，Jina 无）；② 整站递归 `/crawl`（Jina 无）；③ Jina 默认模式失败的 JS 重渲染/反爬站精读降级。

### ⚡ 在 SOP 脚本中的集成位置（v2.1）
```python
# research_task.py 中精读路由的标准位置（Stage 2 发现后、Stage 3 精读时）：
for score, url, title, source in filtered_urls[:8]:
    if any(d in url for d in ACADEMIC_DOMAINS):
        content = jina_read_academic(url)              # 学术域名 → Jina readerlm-v2
    else:
        content = jina_read(url)                       # 主力：Jina 默认模式（确定性·按需）
        if not content or len(content) < 200:          # 取空/过短 → 判定失败
            content = firecrawl_scrape(url)["markdown"] # 降级：Firecrawl Playwright 兜底
```

---

## Benchmark 数据（⚠️ 含自家基准，审慎采信）

> **利益相关披露（v2.1）**：下表 CrawlBench 数据来自 [CrawlBench](https://www.firecrawl.dev/blog/crawlbench-llm-extraction)——**Firecrawl 官方自建基准**，非中立第三方，"Jina 更低"系其自家口径，存在选择性披露倾向，**不可作为「Jina 不如 Firecrawl」的中立证据**。Apify 的 [对比](https://use-apify.com/blog/firecrawl-vs-jina-reader-2026) 相对独立但亦各有侧重。结论：两者默认模式提取质量接近，选型应按「成本 + JS/反爬鲁棒性 + 独占能力」，而非这张表。

| 指标 | Firecrawl（自家口径）| Jina Reader |
|------|-----------|------------|
| 页面覆盖率 | 96%（CrawlBench 自测）| 标注"更低"（未独立复核）|
| F1 accuracy | 0.638（CrawlBench 自测）| 标注"更低"（未独立复核）|
| ROUGE 分数 | 93.7%（CrawlBench 自测）| 标注"更低"（未独立复核）|
| CrawlBench Hard 精确匹配 | 87.5%（自测）| 标注"更低"|
| 平均延迟 | 更快 | ~7.9s/页（第三方实测）|

---

## Sources / 来源
- [Firecrawl Official Docs](https://docs.firecrawl.dev/) — 四端点完整规范
- [CrawlBench Benchmark](https://www.firecrawl.dev/blog/crawlbench-llm-extraction) — 96% coverage / F1 0.638 / ROUGE 93.7%
- [Firecrawl vs Jina Reader 2026 (Apify)](https://use-apify.com/blog/firecrawl-vs-jina-reader-2026) — 独立对比测试
- [REDEEP: Hallucination in RAG via Mechanistic Interpretability](https://arxiv.org/pdf/2410.11414) — ICLR 2025，LLM 重写层幻觉机制
- `wiki/workflows/Three-Tool-Retrieval-SOP.md` — 四工具 SOP v2，Firecrawl 使用规范
- `wiki/tools/Windows-API-Call-Guide.md` — Windows 平台调用实践
