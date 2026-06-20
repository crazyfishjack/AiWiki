---
title: "Tavily /research 端点完整指南"
category: tool
tags: [tavily, research-api, deep-research, async, streaming, polling, structured-output]
sources:
  - https://docs.tavily.com/documentation/api-reference/endpoint/research
  - https://docs.tavily.com/documentation/api-reference/endpoint/research-get
  - https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming
  - https://docs.tavily.com/documentation/best-practices/best-practices-research
related:
  - "[[Tavily-Search-API]]"
  - "[[Exa-Research-Endpoint]]"
  - "[[Three-Tool-Retrieval-SOP]]"
  - "[[Deep-Research-Methodology]]"
last_compiled: 2026-04-28
confidence: high
language: zh-CN+en
discovery:
  one_liner: "调用 Tavily /research 端点委托 AI Agent 自动执行深度研究并获取带引用报告"
  topic_cluster: ai-concepts
  load_when:
    - "需要委托外部 Agent 自动完成多轮深度研究任务时"
    - "需要 Tavily /research 端点的 API 参数、轮询/流式模式代码示例时"
    - "需要将研究结果输出为结构化 JSON 供下游流程消费时"
  key_outputs:
    - "POST /research 完整参数与 pro/mini/auto 模型选择决策表"
    - "轮询模式（GET）与 SSE Streaming 模式的 PowerShell/Python 完整代码"
    - "output_schema 结构化 JSON 输出设计原则与竞品分析示例"
    - "质量优先提示词三类模板（公司分析/定向研究/技术调研）"
    - "/research 与三工具 SOP 的场景对比及 Wiki 工作流定位"
  estimated_tokens: 2550
  sections:
    - heading: "What It Is / 是什么"
      one_liner: "/research 与 /search 的架构区别：异步任务模式、自动多轮检索、自动生成带引用报告"
      lines: [4, 24]
      tokens: 250
    - heading: "API 架构 / Architecture"
      one_liner: "三个端点组成：POST 创建任务、GET 轮询结果、SSE 流式获取"
      lines: [26, 37]
      tokens: 100
    - heading: "POST /research — 创建任务"
      one_liner: "完整参数表、pro/mini/auto 模型对比及 PowerShell 创建任务代码示例"
      lines: [38, 98]
      tokens: 500
    - heading: "GET /research/{request_id} — 轮询结果"
      one_liner: "PowerShell 轮询实现与完成后响应结构（含状态流转 pending→running→completed）"
      lines: [100, 143]
      tokens: 300
    - heading: "Streaming 模式 — 实时 SSE"
      one_liner: "5 类 SSE 事件格式与 Pro 模式完整执行流程（ResearchSubtopic 子主题深度研究）"
      lines: [145, 242]
      tokens: 600
    - heading: "Structured Output / 结构化输出"
      one_liner: "output_schema JSON Schema 设计原则与竞品分析结构化输出完整示例"
      lines: [244, 295]
      tokens: 300
    - heading: "提示词最佳实践 / Prompting"
      one_liner: "核心原则与三类质量优先提示词模板（公司分析/定向研究/技术调研）"
      lines: [297, 328]
      tokens: 200
    - heading: "在 Wiki 工作流中的定位"
      one_liner: "/research 委托模式 vs 三工具 SOP 的控制度对比与推荐/不推荐使用场景"
      lines: [330, 344]
      tokens: 150
    - heading: "Python SDK 完整示例"
      one_liner: "Python SDK 创建任务+轮询直到完成的端到端代码示例"
      lines: [346, 386]
      tokens: 250
---

# Tavily `/research` 端点完整指南

## What It Is / 是什么

Tavily `/research` 是一个**端到端自动化深度研究 API**，将完整的研究任务委托给 Tavily 的 AI Agent 执行。与 `/search`（单次检索）不同，`/research` 会：

1. 自动分解研究问题为多个子查询
2. 并行执行多轮网页搜索（`pro` 模式含子主题深度研究）
3. 自动综合所有来源，生成带引用的结构化报告

**架构特点**：**异步任务模式**——提交后立即返回 `request_id`，通过轮询或流式获取结果。

**与 `/search` 的核心区别**：

| 维度 | `/search` | `/research` |
|------|-----------|-------------|
| 控制粒度 | 高（每次搜索可精细调参）| 低（委托给 Agent）|
| 多轮检索 | 手动多次调用 | 自动执行 |
| 报告生成 | 需 LLM 自行综合 | 自动生成含引用报告 |
| 适用场景 | Wiki 助理自主研究 | 委托外部研究任务 |
| 结果可控性 | ✅ 完全可控 | ❌ 依赖 Tavily Agent |

---

## API 架构 / Architecture

Tavily Research 由三个端点组成：

| 端点 | 方法 | 说明 |
|------|------|------|
| `POST /research` | POST | 创建研究任务，返回 `request_id` |
| `GET /research/{request_id}` | GET | 轮询任务状态与结果 |
| Streaming（`stream: true`）| SSE | 实时流式获取进度和结果 |

---

## POST /research — 创建任务

### 完整参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `input` | string | **必填** | 研究任务描述，是研究质量的核心决定因素 |
| `model` | enum | `auto` | `mini` / `pro` / `auto` |
| `stream` | bool | false | 是否开启 SSE 流式返回 |
| `output_schema` | object | — | JSON Schema，指定时返回结构化 JSON 而非 Markdown 报告 |
| `citation_format` | enum | `numbered` | `numbered` / `mla` / `apa` / `chicago` |

### 模型选择（质量优先选 `pro`）

| 模型 | 特点 | 质量优先时 |
|------|------|-----------|
| `pro` | 多 Agent 协作，ResearchSubtopic 子主题深度挖掘，最高质量 | **✅ 首选** |
| `mini` | 单 Agent，聚焦高效，适合范围明确的问题 | 次选 |
| `auto` | 自动判断复杂度 | 不确定时使用 |

**`pro` 与 `mini` 的流程差异**：
- `mini`：Planning → WebSearch × N → Generating
- `pro`：Planning → WebSearch × N → **ResearchSubtopic × M（并行子主题深度研究）** → Generating

### 调用示例（质量优先）

```bash
# PowerShell — 创建研究任务
$key = "从 retrieval-api-keys.md 读取 TAVILY_API_KEY"

$body = @{
  input          = "你的研究任务描述（见下方提示词最佳实践）"
  model          = "pro"               # 质量优先，始终用 pro
  stream         = $false              # 先用轮询模式
  citation_format = "numbered"         # 编号引用格式
} | ConvertTo-Json

$response = Invoke-RestMethod `
  -Uri "https://api.tavily.com/research" `
  -Method POST `
  -Headers @{"Authorization"="Bearer $key"; "Content-Type"="application/json"} `
  -Body $body

$requestId = $response.request_id
Write-Host "Research task created: $requestId"
```

### 初始响应（201）

```json
{
  "request_id": "123e4567-e89b-12d3-a456-426614174111",
  "created_at": "2025-01-15T10:30:00Z",
  "status": "pending",
  "input": "Your research question",
  "model": "pro",
  "response_time": 1.23
}
```

---

## GET /research/{request_id} — 轮询结果

### 轮询模式实现

```bash
# PowerShell — 轮询直到完成
$key = "从 retrieval-api-keys.md 读取"

function Poll-Research($requestId) {
  do {
    Start-Sleep -Seconds 10      # 每 10 秒轮询一次
    $result = Invoke-RestMethod `
      -Uri "https://api.tavily.com/research/$requestId" `
      -Headers @{"Authorization"="Bearer $key"}
    Write-Host "Status: $($result.status)"
  } while ($result.status -eq "pending" -or $result.status -eq "running")
  return $result
}

$finalResult = Poll-Research $requestId
```

### 完成后响应（200）

```json
{
  "request_id": "123e4567-e89b-12d3-a456-426614174111",
  "created_at": "2025-01-15T10:30:00Z",
  "status": "completed",
  "content": "# Research Report\n\n## Executive Summary\n\n...",
  "sources": [
    {
      "title": "Source Title",
      "url": "https://example.com/article",
      "favicon": "https://example.com/favicon.ico"
    }
  ],
  "response_time": 1.23
}
```

**响应状态值**：`pending` → `running` → `completed` | `failed`

---

## Streaming 模式 — 实时 SSE

### 何时用 Streaming vs Polling

| 场景 | 推荐方式 |
|------|---------|
| 交互式界面，显示实时进度 | **Streaming** |
| 后台批量研究任务 | **Polling** |
| Wiki 助理内部使用 | **Polling**（等待完成后一次性读取） |

### Streaming 开启方式

```bash
$body = @{
  input  = "Research question"
  model  = "pro"
  stream = $true    # ← 开启 SSE
} | ConvertTo-Json
```

### SSE 事件流类型

流式响应遵循 **OpenAI chat completions** 格式，包含以下事件类型：

#### 1. Tool Call 事件（Agent 执行动作时）
```json
{
  "delta": {
    "tool_calls": {
      "type": "tool_call",
      "tool_call": [{
        "name": "WebSearch",
        "arguments": "Executing 5 search queries",
        "queries": ["query1", "query2", "..."]
      }]
    }
  }
}
```

#### 2. Tool Response 事件（动作执行完成后）
```json
{
  "delta": {
    "tool_calls": {
      "type": "tool_response",
      "tool_response": [{
        "name": "WebSearch",
        "arguments": "Completed executing search tool call",
        "sources": [{"url": "...", "title": "...", "favicon": "..."}]
      }]
    }
  }
}
```

#### 3. Content 事件（报告流式输出）
```json
{"delta": {"content": "# Research Report\n\nBased on..."}}
```

#### 4. Sources 事件（所有引用来源）
```json
{"delta": {"sources": [{"url": "...", "title": "...", "favicon": "..."}]}}
```

#### 5. Done 事件（流结束）
```
event: done
```

### Pro 模式专有工具类型

| Tool 名称 | 说明 | 模式 |
|-----------|------|------|
| `Planning` | 初始化研究计划 | 两种 |
| `WebSearch` | 执行网页搜索 | 两种 |
| `Generating` | 生成最终报告 | 两种 |
| **`ResearchSubtopic`** | **深度研究特定子主题**（Pro 独有）| **Pro only** |

### Pro 模式的完整执行流程

```
1. Planning (tool_call)          → 初始化研究计划
2. Planning (tool_response)      → 计划制定完成
3. WebSearch (tool_call)         → 执行初始搜索（附 queries 数组）
4. WebSearch (tool_response)     → 搜索完成（附 sources 数组）
5. ResearchSubtopic (tool_call)  → 深入研究子主题 A    ← Pro 独有
6. ResearchSubtopic (tool_resp)  → 子主题 A 完成       ← Pro 独有
7. ResearchSubtopic × N ...      → 更多子主题           ← Pro 独有
8. Generating (tool_call)        → 开始生成报告
9. Generating (tool_response)    → 报告生成完成
10. Content events               → 流式输出报告内容
11. Sources event                → 所有引用来源
12. Done event                   → 流结束
```

---

## Structured Output / 结构化输出

### 何时用结构化输出 vs 报告

| 输出类型 | 适用场景 |
|---------|---------|
| **Markdown 报告**（默认）| 阅读、分享、直接展示 |
| **结构化 JSON**（`output_schema`）| 数据提取、写入数据库、特定字段 |

### output_schema 最佳实践

```json
// 示例：竞争对手分析结构化输出
{
  "properties": {
    "company_name": {
      "type": "string",
      "description": "公司全称"
    },
    "competitors": {
      "type": "array",
      "description": "主要竞争对手列表，每个包含名称和核心差异化",
      "items": {
        "type": "object",
        "properties": {
          "name": {"type": "string"},
          "differentiator": {"type": "string"},
          "market_position": {"type": "string"}
        }
      }
    },
    "key_metrics": {
      "type": "array",
      "description": "关键业务指标，如营收、增长率",
      "items": {"type": "string"}
    },
    "outlook_2026": {
      "type": "string",
      "description": "2026年展望和主要风险"
    }
  },
  "required": ["company_name", "competitors"]
}
```

**Schema 设计原则**（官方最佳实践）：
- ✅ 字段描述写清楚"具体要找什么"（1-3句话）
- ✅ 用正确类型（`string[]` 而非 `"A, B, C"` 字符串）
- ✅ 每个字段保持唯一性，避免重叠
- ❌ 不要把多个值堆在一个字符串字段里

---

## 提示词最佳实践 / Prompting

### 核心原则

- **明确目标**：清楚说明要找什么信息、如何研究、输出什么
- **已知信息先说**：把已知背景包含进去，避免重复研究
- **开放探索时明说**：「告诉我最有影响力的...」
- **避免矛盾**：不要在同一个 prompt 里包含冲突的约束

### 质量优先提示词模板

```
// 模板1：公司/竞品深度分析
"Analyze the competitive landscape for [Company/Product] in the [Market/Industry] in 2026.
Include: key competitors and their positioning, pricing models, customer segments,
recent product moves (2025-2026), differentiators, and defensible advantages or risks
over the next 2-3 years. Include citations for all factual claims."

// 模板2：带背景知识的定向研究
"We're evaluating [Target] as a potential [partner/acquisition/competitor].
We already know: [已知信息1], [已知信息2], [已知信息3].
Research [Target]'s 2026 outlook, including [具体关注维度],
where we might have [synergies/risks/gaps]. Include citations."

// 模板3：技术/产品调研
"Research the current state of [Technology/Topic] as of 2026.
Cover: technical fundamentals, major implementations/products,
benchmark comparisons, known limitations, and real-world adoption trends.
Prefer academic and official sources. Include citations."
```

---

## 在 Wiki 工作流中的定位

`/research` 端点与本 Wiki 助理的「三工具 SOP」是**两种不同的策略**：

| 策略 | 控制度 | 透明度 | 适用场景 |
|------|--------|--------|---------|
| **三工具 SOP**（Tavily /search + Exa + Jina）| 高 | 完全透明 | Wiki 助理日常研究入库，需要精细控制 |
| **Tavily /research**（委托 Agent）| 低 | 黑盒 | 快速获取大型研究任务的初始报告，再手动验证 |

**推荐使用场景**：
- ✅ 需要快速获得某主题的**全面初始报告**，再用三工具 SOP 补充验证
- ✅ 需要生成**带格式的结构化 JSON** 供下游流程消费
- ❌ 不推荐作为 Wiki 入库的唯一来源（缺乏可追溯性）

---

## Python SDK 完整示例

```python
from tavily import TavilyClient
import time

client = TavilyClient(api_key="从 retrieval-api-keys.md 读取")

# 1. 创建任务（质量优先：pro + 详细提示）
response = client.research(
    input="""Analyze the competitive landscape for [Company] in 2026.
    Include key competitors, positioning, pricing, and 2-3 year outlook.
    Provide citations for all claims.""",
    model="pro",
    citation_format="numbered"
)

request_id = response["request_id"]
print(f"Task created: {request_id}, Status: {response['status']}")

# 2. 轮询直到完成
while True:
    result = client.get_research(request_id)
    status = result["status"]
    print(f"Status: {status}")
    
    if status == "completed":
        print("\n=== Research Report ===")
        print(result["content"])
        print("\n=== Sources ===")
        for s in result["sources"]:
            print(f"- [{s['title']}]({s['url']})")
        break
    elif status == "failed":
        print("Research failed")
        break
    
    time.sleep(10)  # 等待 10 秒再次轮询
```

---

## Sources / 来源
- [Tavily: Create Research Task](https://docs.tavily.com/documentation/api-reference/endpoint/research)
- [Tavily: Get Research Task Status](https://docs.tavily.com/documentation/api-reference/endpoint/research-get)
- [Tavily: Streaming Documentation](https://docs.tavily.com/documentation/api-reference/endpoint/research-streaming)
- [Tavily: Best Practices for Research](https://docs.tavily.com/documentation/best-practices/best-practices-research)
