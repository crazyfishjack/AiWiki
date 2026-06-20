#!/usr/bin/env python3
"""
四工具 Wiki 调研脚本。

脚本职责：
1. 从本地私有配置读取 Wiki 地址和四个工具的 API Key。
2. 按项目四工具 SOP 执行外部调研。
3. 将调研结果保存为 raw Markdown，等待用户确认后再由 Agent 按 SCHEMA 入库。
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

try:
    import requests
except ImportError:  # pragma: no cover - 只在用户环境缺依赖时触发
    requests = None


ACADEMIC_DOMAINS = (
    "arxiv.org",
    "ieeexplore.ieee.org",
    "dl.acm.org",
    "pubmed.ncbi.nlm.nih.gov",
    "nature.com",
    "science.org",
    "springer.com",
    "sciencedirect.com",
    "semanticscholar.org",
    "openreview.net",
    "pmlr.press",
)

LOW_QUALITY_DOMAINS = (
    "medium.com/@",
    "quora.com",
    "answers.yahoo.com",
    "amazon.com/dp",
    "buy.",
    "shop.",
)


@dataclass
class ResearchConfig:
    """脚本运行配置，所有敏感字段只从本地配置读取，不写入输出。"""

    wiki_root: Path
    raw_default_dir: str
    proxy: str | None
    api_keys: dict[str, str]
    max_subqueries: int
    max_deep_read_urls: int
    exa_highlight_char_limit: int
    evidence_full_content: bool
    excerpt_char_limit: int
    tavily_min_score: float
    config_path: Path


@dataclass
class Candidate:
    """候选信源，用于发现、过滤、重排和精读。"""

    url: str
    title: str
    source_tool: str
    score: float
    snippet: str = ""


@dataclass
class SourceGateRecord:
    """信源门控审计记录，保留剔除、去重和等级判断的依据。"""

    url: str
    title: str
    source_tool: str
    score: float
    status: str
    source_grade: str
    reason: str
    next_step: str


@dataclass
class DeepRead:
    """精读结果，保存抓取方法、正文和失败信息。"""

    url: str
    title: str
    method: str
    content: str
    error: str = ""


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""

    parser = argparse.ArgumentParser(
        description="调用 Tavily + Exa + Firecrawl + Jina 完成调研，并保存中文 raw Markdown 文件。"
    )
    parser.add_argument("--query", required=False, help="调研问题或主题。")
    parser.add_argument(
        "--mode",
        choices=("auto", "standard", "quick", "extract", "crawl"),
        default="standard",
        help="调研模式。standard 是默认四工具工作流。",
    )
    parser.add_argument("--raw-dir", help="相对 wiki_root 的 raw 目录，例如 raw/articles。")
    parser.add_argument("--config", help="本机私有配置 JSON 路径。")
    parser.add_argument("--urls", nargs="*", default=[], help="extract 或 crawl 模式使用的已知 URL。")
    parser.add_argument("--dry-run", action="store_true", help="只验证配置和参数，不调用 API。")
    return parser.parse_args()


def skill_dir() -> Path:
    """返回技能根目录，便于定位默认配置文件。"""

    return Path(__file__).resolve().parents[1]


def locate_config(args: argparse.Namespace) -> Path:
    """按显式参数、环境变量、本地配置、示例配置顺序定位配置文件。"""

    if args.config:
        return Path(args.config).expanduser().resolve()

    env_path = os.environ.get("WIKI_RESEARCH_CONFIG")
    if env_path:
        return Path(env_path).expanduser().resolve()

    local_path = skill_dir() / "config.local.json"
    if local_path.exists():
        return local_path

    example_path = skill_dir() / "config.example.json"
    if args.dry_run and example_path.exists():
        return example_path

    raise FileNotFoundError(
        "未找到配置文件。请复制 config.example.json 为 config.local.json，"
        "或设置 WIKI_RESEARCH_CONFIG，或传入 --config。"
    )


def load_config(args: argparse.Namespace) -> ResearchConfig:
    """读取并校验配置文件，返回标准化配置对象。"""

    config_path = locate_config(args)
    with config_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    wiki_root_raw = data.get("wiki_root")
    if not wiki_root_raw:
        raise ValueError("配置缺少 wiki_root。")

    defaults = data.get("research_defaults", {})
    api_keys = data.get("api_keys", {})
    evidence_full_content = bool(defaults.get("evidence_full_content", True))

    return ResearchConfig(
        wiki_root=Path(wiki_root_raw).expanduser().resolve(),
        raw_default_dir=data.get("raw_default_dir", "raw/articles"),
        proxy=data.get("proxy") or None,
        api_keys={
            "tavily": api_keys.get("tavily", ""),
            "exa": api_keys.get("exa", ""),
            "firecrawl": api_keys.get("firecrawl", ""),
            "jina": api_keys.get("jina", ""),
        },
        max_subqueries=int(defaults.get("max_subqueries", 6)),
        max_deep_read_urls=int(defaults.get("max_deep_read_urls", 10)),
        exa_highlight_char_limit=int(defaults.get("exa_highlight_char_limit", 4000)),
        evidence_full_content=evidence_full_content,
        excerpt_char_limit=int(defaults.get("excerpt_char_limit", 2000)),
        tavily_min_score=float(defaults.get("tavily_min_score", 0.4)),
        config_path=config_path,
    )


def validate_config(config: ResearchConfig, dry_run: bool) -> list[str]:
    """检查配置完整性；dry-run 只报告缺失，不阻止查看结构。"""

    issues: list[str] = []
    if not config.wiki_root.exists():
        issues.append(f"wiki_root 不存在: {config.wiki_root}")
    if not (config.wiki_root / "SCHEMA.md").exists():
        issues.append("wiki_root 下缺少 SCHEMA.md")
    if not (config.wiki_root / "wiki" / "_index.md").exists():
        issues.append("wiki_root 下缺少 wiki/_index.md")

    for key_name, key_value in config.api_keys.items():
        if not key_value:
            issues.append(f"缺少 api_keys.{key_name}")

    if issues and not dry_run:
        raise ValueError("配置校验失败:\n- " + "\n- ".join(issues))
    return issues


def require_requests() -> None:
    """确保 requests 可用，避免运行到一半才失败。"""

    if requests is None:
        raise RuntimeError("缺少 Python 依赖 requests。请先安装：pip install requests")


def proxies(config: ResearchConfig) -> dict[str, str] | None:
    """根据配置生成 requests 代理参数。"""

    if not config.proxy:
        return None
    return {"http": config.proxy, "https": config.proxy}


def contains_cjk(text: str) -> bool:
    """判断查询是否包含中文字符，用于 Tavily 中国地区优先。"""

    return bool(re.search(r"[\u4e00-\u9fff]", text))


def tavily_search(config: ResearchConfig, query: str, topic: str = "general", time_range: str | None = None) -> dict[str, Any]:
    """调用 Tavily /search 做广度发现。"""

    require_requests()
    body: dict[str, Any] = {
        "query": query,
        "search_depth": "advanced",
        "chunks_per_source": 3,
        "max_results": 10,
        "topic": topic,
        "include_answer": "advanced",
        "include_raw_content": "markdown",
    }
    if time_range:
        body["time_range"] = time_range
    if contains_cjk(query) and topic == "general":
        body["country"] = "china"

    response = requests.post(
        "https://api.tavily.com/search",
        headers={"Authorization": f"Bearer {config.api_keys['tavily']}", "Content-Type": "application/json"},
        json=body,
        proxies=proxies(config),
        timeout=60,
    )
    response.raise_for_status()
    return response.json()


def exa_search(config: ResearchConfig, query: str, category: str | None = None) -> dict[str, Any]:
    """调用 Exa /search 做语义和学术发现。"""

    require_requests()
    body: dict[str, Any] = {
        "query": query,
        "type": "deep-reasoning",
        "numResults": 15,
        "contents": {
            "text": {"maxCharacters": 50000},
            "highlights": {
                "maxCharacters": config.exa_highlight_char_limit,
                "numSentences": 10,
                "highlightsPerUrl": 5,
            },
            "summary": True,
        },
    }
    if category:
        body["category"] = category

    response = requests.post(
        "https://api.exa.ai/search",
        headers={"x-api-key": config.api_keys["exa"], "Content-Type": "application/json"},
        json=body,
        proxies=proxies(config),
        timeout=90,
    )
    response.raise_for_status()
    return response.json()


def firecrawl_scrape(config: ResearchConfig, url: str) -> dict[str, Any]:
    """调用 Firecrawl /scrape 精读普通网页。"""

    require_requests()
    response = requests.post(
        "https://api.firecrawl.dev/v2/scrape",
        headers={"Authorization": f"Bearer {config.api_keys['firecrawl']}", "Content-Type": "application/json"},
        json={"url": url, "formats": ["markdown"], "onlyMainContent": True, "timeout": 30000},
        proxies=proxies(config),
        timeout=90,
    )
    response.raise_for_status()
    return response.json().get("data", {})


def firecrawl_search(config: ResearchConfig, query: str, limit: int = 5) -> list[dict[str, Any]]:
    """调用 Firecrawl /search，一步获取搜索结果和全文。"""

    require_requests()
    response = requests.post(
        "https://api.firecrawl.dev/v2/search",
        headers={"Authorization": f"Bearer {config.api_keys['firecrawl']}", "Content-Type": "application/json"},
        json={
            "query": query,
            "limit": limit,
            "scrapeOptions": {"formats": ["markdown"], "onlyMainContent": True},
        },
        proxies=proxies(config),
        timeout=90,
    )
    response.raise_for_status()
    return response.json().get("data", [])


def firecrawl_extract(config: ResearchConfig, urls: list[str], prompt: str) -> dict[str, Any]:
    """调用 Firecrawl /extract，从多个 URL 中按提示抽取结构化信息。"""

    require_requests()
    response = requests.post(
        "https://api.firecrawl.dev/v2/extract",
        headers={"Authorization": f"Bearer {config.api_keys['firecrawl']}", "Content-Type": "application/json"},
        json={"urls": urls, "prompt": prompt},
        proxies=proxies(config),
        timeout=180,
    )
    response.raise_for_status()
    return response.json()


def firecrawl_crawl(config: ResearchConfig, url: str, limit: int = 50) -> list[dict[str, Any]]:
    """调用 Firecrawl /crawl 并轮询完成，适合文档站或官网整站调研。"""

    require_requests()
    create_response = requests.post(
        "https://api.firecrawl.dev/v2/crawl",
        headers={"Authorization": f"Bearer {config.api_keys['firecrawl']}", "Content-Type": "application/json"},
        json={"url": url, "limit": limit, "scrapeOptions": {"formats": ["markdown"], "onlyMainContent": True}},
        proxies=proxies(config),
        timeout=120,
    )
    create_response.raise_for_status()
    job_id = create_response.json().get("id")
    if not job_id:
        raise RuntimeError("Firecrawl crawl 未返回任务 id。")

    for _ in range(60):
        status_response = requests.get(
            f"https://api.firecrawl.dev/v2/crawl/{job_id}",
            headers={"Authorization": f"Bearer {config.api_keys['firecrawl']}"},
            proxies=proxies(config),
            timeout=60,
        )
        status_response.raise_for_status()
        status = status_response.json()
        if status.get("status") == "completed":
            return status.get("data", [])
        if status.get("status") == "failed":
            raise RuntimeError(f"Firecrawl crawl failed: {status}")
        time.sleep(10)
    raise TimeoutError("Firecrawl crawl 轮询超时。")


def jina_read_academic(config: ResearchConfig, url: str) -> str:
    """调用 Jina readerlm-v2 精读学术 URL；普通网页禁止走此函数。"""

    require_requests()
    response = requests.post(
        "https://r.jina.ai/",
        headers={
            "Authorization": f"Bearer {config.api_keys['jina']}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Return-Format": "markdown",
            "X-Engine": "browser",
            "X-Respond-With": "readerlm-v2",
            "X-Remove-Selector": "nav,footer,aside,script,style",
            "X-With-Links-Summary": "true",
        },
        json={"url": url},
        proxies=proxies(config),
        timeout=90,
    )
    response.raise_for_status()
    return response.json().get("data", {}).get("content", "")


def jina_rerank(config: ResearchConfig, query: str, candidates: list[Candidate], top_n: int) -> list[Candidate]:
    """候选信源过多时调用 Jina Reranker 精选 Top-N。"""

    require_requests()
    documents = [
        {"id": str(index), "text": f"{candidate.title}\n{candidate.snippet}\n{candidate.url}"}
        for index, candidate in enumerate(candidates)
    ]
    response = requests.post(
        "https://api.jina.ai/v1/rerank",
        headers={"Authorization": f"Bearer {config.api_keys['jina']}", "Content-Type": "application/json"},
        json={"model": "jina-reranker-v3", "query": query, "documents": documents, "top_n": top_n},
        proxies=proxies(config),
        timeout=60,
    )
    response.raise_for_status()
    ranked = []
    for item in response.json().get("results", []):
        index = item.get("index")
        if isinstance(index, int) and 0 <= index < len(candidates):
            ranked.append(candidates[index])
    return ranked or candidates[:top_n]


def is_academic_url(url: str) -> bool:
    """判断 URL 是否属于 Jina readerlm-v2 允许的学术域名。"""

    host = urlparse(url).netloc.lower()
    return any(domain in host for domain in ACADEMIC_DOMAINS)


def decompose_query(query: str, max_subqueries: int) -> list[tuple[str, str]]:
    """生成不超过上限的子查询；保持简单可预测，综合交给 Agent 入库阶段。"""

    candidates = [
        (query, "general"),
        (f"{query} official documentation best practices", "general"),
        (f"{query} latest developments 2025 2026", "news"),
        (f"{query} engineering practice pitfalls", "general"),
        (f"{query} research paper benchmark arXiv", "academic"),
    ]
    if contains_cjk(query):
        candidates.append((f"{query} 中文 资料 官方 文档", "general"))
    else:
        candidates.append((f"{query} 中文 资料 官方 文档", "general"))
    return candidates[:max_subqueries]


def collect_candidates(
    config: ResearchConfig, query: str
) -> tuple[list[Candidate], list[str], list[SourceGateRecord]]:
    """并行执行 Tavily 与 Exa 发现，并转换为统一候选信源列表。"""

    subqueries = decompose_query(query, config.max_subqueries)
    candidates: list[Candidate] = []
    notes: list[str] = []

    def run_one(item: tuple[str, str]) -> tuple[str, str, Any, str | None]:
        subquery, kind = item
        try:
            if kind == "academic":
                return subquery, "exa", exa_search(config, subquery, category="research paper"), None
            topic = "news" if kind == "news" else "general"
            return subquery, "tavily", tavily_search(config, subquery, topic=topic), None
        except Exception as exc:  # noqa: BLE001 - 调研脚本需要保留单工具失败并继续
            return subquery, kind, None, str(exc)

    with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(subqueries), 6)) as executor:
        for subquery, tool, result, error in executor.map(run_one, subqueries):
            if error:
                notes.append(f"{tool} failed for {subquery}: {error}")
                continue

            if tool == "tavily":
                for item in result.get("results", []):
                    url = item.get("url", "")
                    score = float(item.get("score", 0) or 0)
                    if not url:
                        continue
                    candidates.append(
                        Candidate(
                            url=url,
                            title=item.get("title", ""),
                            source_tool="tavily",
                            score=score,
                            snippet=item.get("content") or item.get("raw_content", "")[:800],
                        )
                    )
            elif tool == "exa":
                for item in result.get("results", []):
                    url = item.get("url", "")
                    if not url:
                        continue
                    highlights = item.get("highlights") or []
                    snippet = "\n".join(highlights) if isinstance(highlights, list) else str(highlights)
                    if not snippet:
                        snippet = item.get("summary", "") or item.get("text", "")[:800]
                    candidates.append(
                        Candidate(
                            url=url,
                            title=item.get("title", ""),
                            source_tool="exa",
                            score=1.0,
                            snippet=snippet,
                        )
                    )

    gated_candidates, gate_records = apply_source_gate(candidates, config.tavily_min_score)
    return gated_candidates, notes, gate_records


def is_low_quality(url: str) -> bool:
    """过滤已知低质量或明显商业噪声域名。"""

    lowered = url.lower()
    return any(domain in lowered for domain in LOW_QUALITY_DOMAINS)


def classify_source(candidate: Candidate) -> tuple[str, str, str]:
    """按 URL 与工具信号给来源分级，供 raw 阶段门控与入库映射使用。"""

    host = urlparse(candidate.url).netloc.lower()
    path = urlparse(candidate.url).path.lower()

    if is_low_quality(candidate.url):
        return "D", "已知低质域名", "仅作背景参考"
    if is_academic_url(candidate.url):
        return "A", "学术论文", "进入精读"
    if host.endswith(".gov") or host.endswith(".edu") or host.startswith(("docs.", "developer.", "developers.")):
        return "A", "官方文档 / 一手数据", "进入精读"
    if any(part in path for part in ("/docs", "/documentation", "/manual", "/guide", "/api")):
        return "A", "官方文档 / 技术文档", "进入精读"
    if candidate.source_tool == "exa":
        return "B", "Exa 学术/语义结果，默认保留但进入来源等级评估", "进入 rerank"
    if candidate.score >= 0.7:
        return "B", "与主题高度相关", "进入精读"
    return "C", "相关性一般，需交叉验证", "仅作背景参考"


def source_quality_mapping_text(source_grade: str) -> str:
    """返回 raw 门控等级入库到 SCHEMA source-quality 的映射说明。"""

    if source_grade in {"A", "B"}:
        return "`source-quality: high`"
    if source_grade == "C":
        return "`source-quality: medium`"
    return "`source-quality: low`"


def apply_source_gate(candidates: list[Candidate], tavily_min_score: float) -> tuple[list[Candidate], list[SourceGateRecord]]:
    """执行信源质量门控，并保留所有保留、剔除和重复合并记录。"""

    seen: dict[str, Candidate] = {}
    records: list[SourceGateRecord] = []
    for candidate in candidates:
        grade, source_reason, next_step = classify_source(candidate)
        if candidate.source_tool == "tavily" and candidate.score < tavily_min_score:
            records.append(
                SourceGateRecord(
                    url=candidate.url,
                    title=candidate.title,
                    source_tool=candidate.source_tool,
                    score=candidate.score,
                    status="rejected",
                    source_grade=grade,
                    reason=f"score 低于 {tavily_min_score:g}",
                    next_step="剔除",
                )
            )
            continue
        if is_low_quality(candidate.url):
            records.append(
                SourceGateRecord(
                    url=candidate.url,
                    title=candidate.title,
                    source_tool=candidate.source_tool,
                    score=candidate.score,
                    status="rejected",
                    source_grade="D",
                    reason="已知低质域名",
                    next_step="剔除",
                )
            )
            continue

        existing = seen.get(candidate.url)
        if existing is None:
            seen[candidate.url] = candidate
            continue

        if candidate.score > existing.score:
            seen[candidate.url] = candidate
            records.append(
                SourceGateRecord(
                    url=existing.url,
                    title=existing.title,
                    source_tool=existing.source_tool,
                    score=existing.score,
                    status="merged",
                    source_grade=classify_source(existing)[0],
                    reason="重复 URL，已合并到最高分结果",
                    next_step="合并",
                )
            )
        else:
            records.append(
                SourceGateRecord(
                    url=candidate.url,
                    title=candidate.title,
                    source_tool=candidate.source_tool,
                    score=candidate.score,
                    status="merged",
                    source_grade=grade,
                    reason="重复 URL，已合并到最高分结果",
                    next_step="合并",
                )
            )

    kept = sorted(seen.values(), key=lambda item: item.score, reverse=True)
    for candidate in kept:
        grade, source_reason, next_step = classify_source(candidate)
        records.append(
            SourceGateRecord(
                url=candidate.url,
                title=candidate.title,
                source_tool=candidate.source_tool,
                score=candidate.score,
                status="kept",
                source_grade=grade,
                reason=source_reason,
                next_step=next_step,
            )
        )
    return kept, records


def gate_records_for_candidates(candidates: list[Candidate]) -> list[SourceGateRecord]:
    """为非 Tavily/Exa 发现模式生成保留型门控记录。"""

    records: list[SourceGateRecord] = []
    for candidate in candidates:
        grade, reason, next_step = classify_source(candidate)
        records.append(
            SourceGateRecord(
                url=candidate.url,
                title=candidate.title,
                source_tool=candidate.source_tool,
                score=candidate.score,
                status="kept",
                source_grade=grade,
                reason=reason,
                next_step=next_step,
            )
        )
    return records


def deep_read_candidates(config: ResearchConfig, candidates: list[Candidate]) -> list[DeepRead]:
    """按 URL 类型路由到 Firecrawl 或 Jina 精读。"""

    reads: list[DeepRead] = []
    for candidate in candidates:
        try:
            if is_academic_url(candidate.url):
                content = jina_read_academic(config, candidate.url)
                method = "jina-readerlm-academic"
            else:
                data = firecrawl_scrape(config, candidate.url)
                content = data.get("markdown", "")
                method = "firecrawl-scrape"
            reads.append(DeepRead(candidate.url, candidate.title, method, content or "", ""))
        except Exception as exc:  # noqa: BLE001 - 单 URL 失败不应中断整个调研
            reads.append(DeepRead(candidate.url, candidate.title, "failed", "", str(exc)))
    return reads


def run_standard(
    config: ResearchConfig, query: str
) -> tuple[list[Candidate], list[DeepRead], list[str], dict[str, Any], list[SourceGateRecord]]:
    """执行标准模式：发现、过滤、必要时重排、精读。"""

    candidates, notes, gate_records = collect_candidates(config, query)
    selected = candidates
    if len(candidates) > 15:
        try:
            selected = jina_rerank(config, query, candidates[:25], config.max_deep_read_urls)
            notes.append("候选信源超过 15 个，已使用 Jina Reranker 精选。")
        except Exception as exc:  # noqa: BLE001
            selected = candidates[: config.max_deep_read_urls]
            notes.append(f"Jina Reranker 失败，已回退为按分数排序：{exc}")
    else:
        selected = candidates[: config.max_deep_read_urls]

    reads = deep_read_candidates(config, selected)
    stats = {"candidate_count": len(candidates), "deep_read_count": len(reads), "mode": "standard"}
    return candidates, reads, notes, stats, gate_records


def run_quick(
    config: ResearchConfig, query: str
) -> tuple[list[Candidate], list[DeepRead], list[str], dict[str, Any], list[SourceGateRecord]]:
    """执行快速模式：Firecrawl search + scrapeOptions 一步获取全文。"""

    notes: list[str] = []
    items = firecrawl_search(config, query, limit=5)
    candidates = [
        Candidate(
            url=item.get("url", ""),
            title=item.get("title", ""),
            source_tool="firecrawl-search",
            score=1.0,
            snippet=item.get("description", ""),
        )
        for item in items
        if item.get("url")
    ]
    reads = [
        DeepRead(
            url=item.get("url", ""),
            title=item.get("title", ""),
            method="firecrawl-search",
            content=item.get("markdown", "") or item.get("content", "") or "",
        )
        for item in items
        if item.get("url")
    ]
    stats = {"candidate_count": len(candidates), "deep_read_count": len(reads), "mode": "quick"}
    return candidates, reads, notes, stats, gate_records_for_candidates(candidates)


def run_extract(
    config: ResearchConfig, query: str, urls: list[str]
) -> tuple[list[Candidate], list[DeepRead], list[str], dict[str, Any], list[SourceGateRecord]]:
    """执行结构化萃取模式；结果以 JSON 文本写入 raw 文档。"""

    if not urls:
        raise ValueError("extract 模式需要 --urls。")
    result = firecrawl_extract(config, urls, query)
    content = json.dumps(result.get("data", result), ensure_ascii=False, indent=2)
    candidates = [Candidate(url=url, title=url, source_tool="firecrawl-extract", score=1.0) for url in urls]
    reads = [DeepRead(url="; ".join(urls), title="Firecrawl extract result", method="firecrawl-extract", content=content)]
    stats = {"candidate_count": len(candidates), "deep_read_count": 1, "mode": "extract"}
    return candidates, reads, [], stats, gate_records_for_candidates(candidates)


def run_crawl(
    config: ResearchConfig, query: str, urls: list[str]
) -> tuple[list[Candidate], list[DeepRead], list[str], dict[str, Any], list[SourceGateRecord]]:
    """执行整站爬取模式；只接受第一个 URL 作为入口。"""

    if not urls:
        raise ValueError("crawl 模式需要 --urls 指定入口 URL。")
    pages = firecrawl_crawl(config, urls[0], limit=50)
    candidates = [
        Candidate(url=page.get("url", urls[0]), title=page.get("title", ""), source_tool="firecrawl-crawl", score=1.0)
        for page in pages
    ]
    reads = [
        DeepRead(
            url=page.get("url", urls[0]),
            title=page.get("title", ""),
            method="firecrawl-crawl",
            content=page.get("markdown", "") or page.get("content", "") or "",
        )
        for page in pages
    ]
    stats = {"candidate_count": len(candidates), "deep_read_count": len(reads), "mode": "crawl"}
    return candidates, reads, [], stats, gate_records_for_candidates(candidates)


def slugify(text: str) -> str:
    """生成符合项目命名习惯的 ASCII kebab-case 文件名片段。"""

    lowered = text.lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    lowered = lowered.strip("-")
    if not lowered:
        digest = hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]
        lowered = f"research-{digest}"
    return lowered[:48].strip("-") or "research"


def resolve_raw_dir(config: ResearchConfig, raw_dir_arg: str | None) -> Path:
    """解析 raw 输出目录，确保输出仍位于 wiki_root/raw 下。"""

    raw_dir = raw_dir_arg or config.raw_default_dir
    path = (config.wiki_root / raw_dir).resolve()
    raw_root = (config.wiki_root / "raw").resolve()
    if raw_root not in path.parents and path != raw_root:
        raise ValueError(f"raw 输出目录必须位于 raw/ 下: {path}")
    path.mkdir(parents=True, exist_ok=True)
    return path


def unique_output_path(raw_dir: Path, query: str) -> Path:
    """生成不覆盖既有文件的 raw Markdown 路径。"""

    today = dt.date.today().isoformat()
    base_name = f"{today}-{slugify(query)}-research"
    candidate = raw_dir / f"{base_name}.md"
    index = 2
    while candidate.exists():
        candidate = raw_dir / f"{base_name}-{index}.md"
        index += 1
    return candidate


def excerpt(text: str, limit: int = 2000) -> str:
    """限制原文摘录长度，避免 raw 调研文件过大。"""

    normalized = re.sub(r"\n{3,}", "\n\n", text.strip())
    if len(normalized) <= limit:
        return normalized
    return normalized[:limit].rstrip() + "\n\n[truncated]"


def evidence_content(text: str, full_content: bool, excerpt_limit: int) -> str:
    """按证据包策略输出精读正文，默认保留完整 Firecrawl/Jina 结果。"""

    normalized = re.sub(r"\n{3,}", "\n\n", text.strip())
    if full_content:
        return normalized
    return excerpt(normalized, excerpt_limit)


def markdown_escape_cell(text: str) -> str:
    """转义 Markdown 表格单元格中的换行和竖线。"""

    return text.replace("|", "\\|").replace("\n", " ")[:240]


def score_text(record: SourceGateRecord) -> str:
    """格式化工具分数，明确 Exa 语义结果默认保留的特殊规则。"""

    if record.source_tool == "exa":
        return "Exa 默认保留"
    return f"{record.score:.2f}"


def append_source_gate_section(lines: list[str], gate_records: list[SourceGateRecord]) -> None:
    """向证据包写入完整信源质量门控记录。"""

    kept_records = [record for record in gate_records if record.status == "kept"]
    excluded_records = [record for record in gate_records if record.status in {"rejected", "merged"}]

    lines.extend(
        [
            "",
            "## 信源质量门控记录",
            "",
            "### 门控规则",
            "- Tavily score < 0.4：剔除",
            "- 已知低质域名：剔除",
            "- 重复 URL：合并保留最高分结果",
            "- Exa 学术/语义结果：默认保留，但进入来源等级评估",
            "- C/D 级来源不得作为唯一结论依据",
            "- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`",
            "",
            "### 保留信源",
        ]
    )

    if not kept_records:
        lines.append("无。")
    for index, record in enumerate(kept_records, start=1):
        lines.extend(
            [
                f"{index}. [{record.title or record.url}]({record.url})",
                f"   - 工具：{record.source_tool}",
                f"   - 分数：{score_text(record)}",
                f"   - 来源等级：{record.source_grade}",
                f"   - 入库映射：{source_quality_mapping_text(record.source_grade)}",
                f"   - 保留原因：{record.reason}",
                f"   - 后续处理：{record.next_step}",
            ]
        )

    lines.extend(["", "### 剔除信源"])
    if not excluded_records:
        lines.append("无。")
    for index, record in enumerate(excluded_records, start=1):
        lines.extend(
            [
                f"{index}. [{record.title or record.url}]({record.url})",
                f"   - 工具：{record.source_tool}",
                f"   - 分数：{score_text(record)}",
                f"   - 来源等级：{record.source_grade}",
                f"   - 剔除原因：{record.reason}",
            ]
        )


def append_conflict_check_template(lines: list[str], successful_read_count: int, generated: str) -> None:
    """写入跨源矛盾检测模板，要求最终报告显式裁决或保留冲突。"""

    lines.extend(
        [
            "",
            "## 跨源矛盾检测结论",
            "",
            "### 检测范围",
            f"- 已精读来源数量：{successful_read_count} 个",
            "- 检测对象：核心数字、日期、功能描述、因果判断、市场/公司事实",
            f"- 检测时间：{generated}",
            "",
            "### 检测结果",
            "结论：待 Agent 基于精读全文检测。最终报告必须替换为以下二选一：",
            "",
            "结论：未检测到跨源矛盾，可进入综合阶段。",
            "",
            "或：",
            "",
            "结论：检测到 X 处跨源矛盾，综合输出时必须保留双方表述，不得静默合并。",
            "",
            "### 矛盾项 1：[简短标题]",
            "- 矛盾描述：[具体什么矛盾]",
            "- 来源 A：[URL]",
            "  - 原文引用：“……”",
            "  - 来源等级：A / B / C / D",
            "  - 发布时间 / 数据日期：YYYY-MM-DD",
            "- 来源 B：[URL]",
            "  - 原文引用：“……”",
            "  - 来源等级：A / B / C / D",
            "  - 发布时间 / 数据日期：YYYY-MM-DD",
            "- 初步判断：",
            "  - 倾向：[来源 A / 来源 B / 暂不倾向]",
            "  - 理由：[官方一手来源优先 / 数据更新 / 方法更透明 / 与中文本地来源一致]",
            "- 综合输出要求：",
            "  - 必须写成“来源 A 说 X，来源 B 说 Y，建议人工核实”",
            "  - 禁止取平均值、合并成第三种说法、只保留其中一方",
        ]
    )


def build_markdown(
    query: str,
    mode: str,
    candidates: list[Candidate],
    reads: list[DeepRead],
    notes: list[str],
    stats: dict[str, Any],
    evidence_full_content: bool,
    excerpt_char_limit: int,
    gate_records: list[SourceGateRecord],
) -> str:
    """将调研结果编排为 raw Markdown 文档。"""

    generated = dt.date.today().isoformat()
    title = f"调研证据包：{query}"
    successful_reads = [item for item in reads if item.content]
    failed_reads = [item for item in reads if item.error]

    lines: list[str] = [
        "---",
        f'title: "{title.replace(chr(34), chr(39))}"',
        "source-type: article",
        f"generated: {generated}",
        "generated-by: wiki-research-skill",
        f"research-mode: {mode}",
        "---",
        "",
        f"# {title}",
        "",
        "## 调研问题",
        "",
        query,
        "",
        "## 摘要",
        "",
        '本文档是四工具检索生成的证据包草稿，不是最终调研报告。Agent 必须先阅读本证据包，执行下方"AI 综合指令"，生成新的中文综合 raw 报告，然后询问用户是否入库。本证据包保留不删除。',
        "",
        f"- 发现候选信源：{stats.get('candidate_count', len(candidates))}",
        f"- 精读信源数量：{stats.get('deep_read_count', len(reads))}",
        f"- 精读成功数量：{len(successful_reads)}",
        f"- 精读失败数量：{len(failed_reads)}",
        "",
        "## AI 综合指令（Agent 必须执行）",
        "",
        "请基于本文档的候选信源和完整精读结果生成最终中文调研报告。最终报告必须编写为一个新的 raw Markdown 文件，并删除本文档这个证据包。最终报告必须满足：",
        "",
        "1. 删除本“AI 综合指令”占位说明，保留必要原始证据摘录。",
        "2. 用中文输出，不要只粘贴网页摘录。",
        "3. 每条关键事实后标注 `[来源: URL]`。",
        "4. 每条核心结论标注可信度：高 / 中 / 低。",
        "5. 显式列出跨源矛盾、证据不足和待验证问题。",
        "6. 不得把无 URL 支撑的内容写成事实；如确需提及，标注“未验证”。",
        "7. 若本文档中的高可信来源精读失败、正文为空、明显不完整或只有导航/付费墙内容，必须二次精读；否则优先使用证据包中的完整精读结果。",
        "8. 必须包含 `## 对于可信度较高的来源逐来源总结`，逐篇整理高可信来源的核心内容、可用事实、局限和适合入库的知识点。",
        "9. 对重要来源进行完整性检查：若本文档精读结果不足以覆盖正文，应重新读取或抓取该来源全文后再生成最终报告，不得只依赖不完整内容。",
        "10. 必须保留 `## 信源质量门控记录`，列出保留信源、剔除信源、来源等级、保留/剔除原因和后续处理。",
        "11. 必须保留 `## 跨源矛盾检测结论`，逐项检测核心数字、日期、功能描述、因果判断、市场/公司事实。",
        "12. 入库到 `wiki/sources/` 时，来源等级按 A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low` 映射。",
        "",
        "最终报告结构必须包含：",
        "",
        "- `## 核心结论`：3-7 条可复用结论，每条带来源和可信度。",
        "- `## 内容整理`：保留所有有用的信息，系统化，结构清晰，逻辑正确。",
        "- `## 推荐工作流`：说明如何组合使用这些工具，明确 Cursor 中的执行步骤。",
        "- `## 适用场景`：列出适合采用该方法的项目类型。",
        "- `## 不适用场景`：说明何时会过度工程或不值得引入。",
        "- `## 风险与约束`：列出衔接点、上下文、测试、规格漂移等风险。",
        "- `## 信源质量门控记录`：记录门控规则、保留信源、剔除信源和 A/B/C/D 来源等级。",
        "- `## 来源与可信度`：逐项列出关键来源、来源类型、可信度和支撑内容。",
        "- `## 对于可信度较高的来源逐来源总结`：逐篇整理高可信来源正文，不只提取少量核心结论。",
        "- `## 跨源矛盾检测结论`：说明检测范围、检测结果和所有矛盾项；未发现矛盾也必须明确写出。",
        "- `## 矛盾与待验证问题`：保留冲突或证据不足处。",
        "- `## 原始证据摘录`：保留支持结论的必要摘录或完整证据片段。",
        "",
        "本证据包默认保存完整精读结果，不对 Firecrawl/Jina 正文做字符截断。若配置关闭全文证据模式，才会回退为摘录模式。",
        f"- 证据包全文模式：{str(evidence_full_content).lower()}",
        f"- 兼容摘录上限：{excerpt_char_limit} 字符（仅在全文模式关闭时使用）",
        "- 若某来源精读失败、正文为空、疑似反爬/付费墙/导航页或工具返回明显不完整，Agent 必须二次精读或标注不可验证。",
        "",
        "## 候选信源",
        "",
        "| 工具 | 分数 | 标题 | URL |",
        "|------|-------|-------|-----|",
    ]

    for candidate in candidates[:30]:
        lines.append(
            f"| {markdown_escape_cell(candidate.source_tool)} | {candidate.score:.2f} | "
            f"{markdown_escape_cell(candidate.title)} | {candidate.url} |"
        )

    append_source_gate_section(lines, gate_records)

    lines.extend(["", "## 完整精读结果", ""])
    for index, item in enumerate(reads, start=1):
        lines.extend(
            [
                f"### 来源 {index}: {item.title or item.url}",
                "",
                f"- URL: {item.url}",
                f"- 精读方法：{item.method}",
            ]
        )
        if item.error:
            lines.extend(["", f"精读失败：{item.error}", ""])
            continue
        if not item.content.strip():
            lines.extend(["", "精读成功但正文为空，需要二次抓取或标注不可验证。", ""])
            continue
        lines.extend(
            ["", evidence_content(item.content, evidence_full_content, excerpt_char_limit), ""]
        )

    append_conflict_check_template(lines, len(successful_reads), generated)

    lines.extend(
        [
            "## 矛盾与不确定性",
            "",
            "- 脚本不会自动裁决跨源矛盾。Agent 编译最终报告时，必须比较数字、日期、因果关系和产品能力声明。",
            "- 本证据包中没有 URL 支撑的说法都应视为未验证，不得作为事实写入最终调研报告或 Wiki。",
            "",
            "## 工具运行记录",
            "",
        ]
    )

    if notes:
        for note in notes:
            lines.append(f"- {note}")
    else:
        lines.append("- 未发现工具级警告。")

    lines.extend(
        [
            "",
            "## 入库提醒",
            "",
            "只有在 Agent 已完成新的中文综合 raw 报告并删除本证据包后，才能询问用户是否入库。若用户确认，按完整 `SCHEMA.md` Ingest 工作流执行。",
            "",
        ]
    )
    return "\n".join(lines)


def write_raw_markdown(config: ResearchConfig, args: argparse.Namespace, markdown: str) -> Path:
    """写入 raw Markdown 文件并返回路径。"""

    raw_dir = resolve_raw_dir(config, args.raw_dir)
    output_path = unique_output_path(raw_dir, args.query or "research")
    output_path.write_text(markdown, encoding="utf-8")
    return output_path


def main() -> int:
    """主入口：校验配置，执行调研，保存 raw 文档。"""

    args = parse_args()
    config = load_config(args)
    issues = validate_config(config, dry_run=args.dry_run)

    if args.dry_run:
        print(f"配置路径: {config.config_path}")
        print(f"Wiki 根目录: {config.wiki_root}")
        if issues:
            print("Dry-run 检查结果:")
            for issue in issues:
                print(f"- {issue}")
        else:
            print("Dry-run 通过。")
        return 0

    if not args.query:
        raise ValueError("必须提供 --query。")

    mode = "standard" if args.mode == "auto" else args.mode
    if mode == "quick":
        candidates, reads, notes, stats, gate_records = run_quick(config, args.query)
    elif mode == "extract":
        candidates, reads, notes, stats, gate_records = run_extract(config, args.query, args.urls)
    elif mode == "crawl":
        candidates, reads, notes, stats, gate_records = run_crawl(config, args.query, args.urls)
    else:
        candidates, reads, notes, stats, gate_records = run_standard(config, args.query)

    markdown = build_markdown(
        args.query,
        mode,
        candidates,
        reads,
        notes,
        stats,
        config.evidence_full_content,
        config.excerpt_char_limit,
        gate_records,
    )
    output_path = write_raw_markdown(config, args, markdown)
    relative = output_path.relative_to(config.wiki_root) if output_path.is_relative_to(config.wiki_root) else output_path

    print(f"RAW_RESEARCH_FILE={relative}")
    print("NEXT_STEP=请询问用户是否按 SCHEMA.md 将该 raw 文件入库。")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001 - CLI 需要给 Agent 直接可读的失败原因
        print(f"错误: {exc}", file=sys.stderr)
        raise SystemExit(1)
