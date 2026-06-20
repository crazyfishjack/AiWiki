---
title: "Firecrawl API 工具指南"
category: tool
tags: [firecrawl, scrape, search, extract, crawl, retrieval, anti-hallucination, web-data, RAG, deep-research]
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
last_compiled: 2026-05-22
confidence: high
language: zh-CN+en
discovery:
  one_liner: "四端点完整代码示例 + 与 Jina Reader 路由规则，让 AI Agent 零幻觉抓取任意页面"
  topic_cluster: ai-concepts
  load_when:
    - "需要调用 Firecrawl API 实现单页精读、搜索或整站爬取时"
    - "设计 RAG 检索层选型时，需判断 Firecrawl 与 Jina Reader 的使用边界"
    - "排查 LLM 检索结果被改写或内容幻觉注入问题时"
  key_outputs:
    - "scrape / search / extract / crawl 四端点可直接复用的 Python 代码"
    - "Firecrawl vs Jina Reader 能力边界路由规则（学术 URL → Jina，其余 → Firecrawl）"
    - "CrawlBench 基准数据：96% 覆盖率、F1 0.638、ROUGE 93.7% 等指标对比"
    - "onlyMainContent / limit / timeout 等关键参数推荐值与陷阱说明"
  estimated_tokens: 3100
  sections:
    - heading: "What It Is / 是什么"
      one_liner: "Firecrawl 定位、Base URL、API Key 及在四工具 SOP v2 中的角色"
      lines: [4, 13]
      tokens: 150
    - heading: "为什么选 Firecrawl 而非 Jina Reader（反幻觉角度）"
      one_liner: "确定性抓取 vs LLM 重写层对比表，含 CrawlBench / REDEEP 数据支撑"
      lines: [16, 33]
      tokens: 350
    - heading: "1. `/scrape` — 单页精读主力"
      one_liner: "单页精读完整 Python 代码、formats 表、关键参数及批量调用示例"
      lines: [37, 117]
      tokens: 700
    - heading: "2. `/search` — 搜索+全文一步获取（模式 B）"
      one_liner: "搜索+全文一次 API 调用代码及高级过滤参数（域名/时间/类别）"
      lines: [120, 167]
      tokens: 400
    - heading: "3. `/extract` — 结构化多页萃取（模式 C）"
      one_liner: "跨 URL 按 JSON Schema 批量提取结构化数据的代码与适用场景"
      lines: [169, 228]
      tokens: 450
    - heading: "4. `/crawl` — 整站递归爬取（模式 D）"
      one_liner: "整站爬取异步轮询代码及 limit / includePaths 等关键参数说明"
      lines: [230, 304]
      tokens: 500
    - heading: "与 Jina Reader 的职能边界"
      one_liner: "精确路由规则：学术域名白名单走 Jina，其余全部走 Firecrawl"
      lines: [307, 334]
      tokens: 250
    - heading: "注意事项 / Tips & Gotchas"
      one_liner: "质量最大化、JS 渲染、/extract 异步陷阱及 SOP 脚本集成代码片段"
      lines: [336, 365]
      tokens: 250
    - heading: "Benchmark 数据"
      one_liner: "CrawlBench 独立基准：覆盖率 96%、F1 0.638、ROUGE 93.7% 等 5 项指标"
      lines: [367, 380]
      tokens: 150
---

# Firecrawl API 工具指南

## What It Is / 是什么

Firecrawl 是一个面向 AI Agent 的 **全栈 Web 数据 API**，提供搜索、单页精读、结构化萃取、整站爬取四大能力。YC 孵化，2025 年成长为 RAG/Agent 工作流的主流数据层工具。

**在四工具检索 SOP v2 中的定位**：**精读主力**。替代 Jina Reader 承担所有普通页面的深度精读任务（含中文/英文/技术博客/新闻/官方文档），同时新增结构化萃取和整站爬取两类此前缺失的能力。

**API Key**：见 `retrieval-api-keys.md`（`FIRECRAWL_API_KEY`）
**Base URL**：`https://api.firecrawl.dev/v2`
**认证**：`Authorization: Bearer {KEY}`

---

## 为什么选 Firecrawl 而非 Jina Reader（反幻觉角度）

> 核心判断依据：CrawlBench 独立基准测试（2026）+ REDEEP ICLR 2025 学术结论

| 维度 | Firecrawl `/scrape` | Jina Reader（默认）| Jina readerlm-v2 |
|------|--------------------|--------------------|-----------------|
| **提取机制** | 确定性抓取 + 清洗（无 LLM）| 确定性抓取 | **LLM 重写层**（幻觉风险）|
| **页面覆盖率** | **96%**（CrawlBench）| 低于 Firecrawl | — |
| **F1 accuracy** | **0.638** | 更低 | — |
| **ROUGE 分数** | **93.7%** | 更低 | — |
| **延迟** | 更快 | ~7.9s/页（实测）| — |
| **中文内容** | ✅ 同等处理 | ✅ 可用 | ❌ 高概率幻觉（ACRI<40）|
| **普通页面幻觉风险** | **极低**（无生成层）| 低 | **高**（会插值）|
| **学术 PDF** | 一般 | 一般 | **✅ 结构理解强** ← Jina 唯一优势保留场景 |

**关键结论**：Jina readerlm-v2 本质是 LLM 重写层（REDEEP，ICLR 2025），会将外部检索内容与参数记忆混合生成，任何非学术页面都有内容被"创造性改写"的风险。Firecrawl 是确定性抓取，`onlyMainContent` 主动过滤噪声，**零 LLM 参与，零生成式幻觉注入**。

---

## 四大端点详解

### 1. `/scrape` — 单页精读主力

**定位**：SOP v2 精读层核心，替代 Jina Reader 用于所有普通页面。

```python
import requests

FIRECRAWL_KEY = "fc-..."  # 从 retrieval-api-keys.md 读取
PROXIES = {"http": "http://127.0.0.1:10808", "https": "http://127.0.0.1:10808"}

def firecrawl_scrape(url, with_json_schema=None, question=None):
    """
    单页精读主力。
    ✅ 适用：中文/英文/技术博客/新闻/官方文档/GitHub 等所有普通页面
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

> **正规则（v2 SOP）**：除学术域名白名单，所有页面用 Firecrawl。

```
URL 精读路由
    │
    ├─ arxiv.org / ieeexplore.ieee.org / dl.acm.org
    │  pubmed / nature.com / science.org / springer.com
    │  sciencedirect.com / openreview.net / pmlr.press
    │       → jina_read_academic(url)    ← readerlm-v2，学术结构理解强
    │
    └─ 所有其他 URL（中文/英文/技术/新闻/官网）
            → firecrawl_scrape(url)      ← 零幻觉注入，确定性抓取
```

| 能力 | Firecrawl `/scrape` | Jina Reader |
|------|--------------------|--------------| 
| 中文页面 | ✅ 同等处理 | ⚠️ readerlm-v2 幻觉风险 |
| 英文技术博客 | ✅ 推荐 | ✅ 可用（但不如 Firecrawl 准确）|
| arXiv/学术 PDF | ⚠️ 一般 | ✅ **readerlm-v2 优势** |
| 结构化萃取 | ✅ `/extract`+schema | ❌ 不支持 |
| 整站爬取 | ✅ `/crawl` | ❌ 不支持 |
| 搜索+内容一步 | ✅ `/search`+scrapeOptions | ❌ 不支持 |
| Reranker | ❌ | ✅ `jina-reranker-v3` |
| Embeddings | ❌ | ✅ `jina-embeddings-v5` |

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

### ⚡ 在 SOP 脚本中的集成位置
```python
# research_task.py 中调用 Firecrawl 的标准位置

# Stage 2（发现）后，Stage 3（精读）时：
for score, url, title, source in filtered_urls[:8]:
    if any(d in url for d in ACADEMIC_DOMAINS):
        content = jina_read_academic(url)     # 学术域名 → Jina
    else:
        result = firecrawl_scrape(url)        # 其余全部 → Firecrawl
        content = result["markdown"]
```

---

## Benchmark 数据

> 来源：[CrawlBench — Evaluating Web Data Extraction](https://www.firecrawl.dev/blog/crawlbench-llm-extraction)（Firecrawl 官方，2026）
> 及 [Firecrawl vs Jina Reader 2026](https://use-apify.com/blog/firecrawl-vs-jina-reader-2026)（Apify 独立测试）

| 指标 | Firecrawl | Jina Reader |
|------|-----------|------------|
| 页面覆盖率 | **96%** | 低于 Firecrawl |
| F1 accuracy | **0.638** | 更低 |
| ROUGE 分数 | **93.7%** | 更低 |
| CrawlBench Hard 精确匹配 | **87.5%** | 更低 |
| 平均延迟 | 更快 | ~7.9s/页 |

---

## Sources / 来源
- [Firecrawl Official Docs](https://docs.firecrawl.dev/) — 四端点完整规范
- [CrawlBench Benchmark](https://www.firecrawl.dev/blog/crawlbench-llm-extraction) — 96% coverage / F1 0.638 / ROUGE 93.7%
- [Firecrawl vs Jina Reader 2026 (Apify)](https://use-apify.com/blog/firecrawl-vs-jina-reader-2026) — 独立对比测试
- [REDEEP: Hallucination in RAG via Mechanistic Interpretability](https://arxiv.org/pdf/2410.11414) — ICLR 2025，LLM 重写层幻觉机制
- `wiki/workflows/Three-Tool-Retrieval-SOP.md` — 四工具 SOP v2，Firecrawl 使用规范
- `wiki/tools/Windows-API-Call-Guide.md` — Windows 平台调用实践
