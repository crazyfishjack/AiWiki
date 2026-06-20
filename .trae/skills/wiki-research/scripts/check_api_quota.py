#!/usr/bin/env python3
"""检查四工具（Tavily / Exa / Firecrawl / Jina）API Key 额度与状态。

用法：
    python check_api_quota.py [--config <path>]

说明：
- Tavily：调用 /usage 接口返回当前 billing cycle 的用量和限额。
- Exa：Exa 没有公开查询额度的 API，只能通过 dashboard 查看。
- Firecrawl：调用 /v1/team/credit-usage 接口返回剩余额度。
- Jina：Jina Reader 免费额度无法通过 API 查询，只能通过 dashboard 查看。

脚本会读取与 four_tool_research.py 相同的配置（config.local.json），
并统一使用其中的 proxy 设置。
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import requests


def load_config(config_path: str | None = None) -> dict:
    """按优先级加载配置文件，返回 JSON 字典。"""

    if config_path:
        path = Path(config_path).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"指定配置文件不存在: {path}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    # 1. 环境变量
    env_path = os.environ.get("WIKI_RESEARCH_CONFIG")
    if env_path:
        path = Path(env_path).expanduser().resolve()
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    # 2. 默认本地配置（与 four_tool_research.py 同级）
    script_dir = Path(__file__).resolve().parent
    local_path = script_dir / "config.local.json"
    if local_path.exists():
        with open(local_path, "r", encoding="utf-8") as f:
            return json.load(f)

    # 3. 向上查找 skills/wiki-research 目录
    for parent in script_dir.parents:
        if parent.name == "wiki-research":
            local_path = parent / "config.local.json"
            if local_path.exists():
                with open(local_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            break

    raise FileNotFoundError(
        "未找到配置文件。请提供 --config 参数，或设置 WIKI_RESEARCH_CONFIG 环境变量，"
        "或确保 config.local.json 与脚本在同一目录。"
    )


def get_proxy(config: dict) -> dict[str, str] | None:
    """根据配置返回 requests 代理参数。"""

    proxy = config.get("proxy")
    if proxy:
        return {"http": proxy, "https": proxy}
    return None


def check_tavily(api_key: str, proxies: dict[str, str] | None) -> dict:
    """检查 Tavily 额度。Tavily 提供 /usage 接口查询当前 billing cycle 用量。"""

    try:
        resp = requests.get(
            "https://api.tavily.com/usage",
            headers={"Authorization": f"Bearer {api_key}"},
            proxies=proxies,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        key_info = data.get("key", {})
        account_info = data.get("account", {})
        return {
            "status": "ok",
            "key_usage": key_info.get("usage", "未知"),
            "key_limit": key_info.get("limit", "未知"),
            "account_plan": account_info.get("current_plan", "未知"),
            "account_usage": account_info.get("plan_usage", "未知"),
            "account_limit": account_info.get("plan_limit", "未知"),
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def check_exa(api_key: str, proxies: dict[str, str] | None) -> dict:
    """检查 Exa 额度。Exa 没有公开查询额度的 API，只能通过 dashboard 查看。"""

    return {
        "status": "unsupported",
        "message": "Exa 没有提供公开查询额度的 API，请访问 https://dashboard.exa.ai 查看。",
    }


def check_firecrawl(api_key: str, proxies: dict[str, str] | None) -> dict:
    """检查 Firecrawl 额度。调用 /v1/team/credit-usage 接口。"""

    try:
        resp = requests.get(
            "https://api.firecrawl.dev/v1/team/credit-usage",
            headers={"Authorization": f"Bearer {api_key}"},
            proxies=proxies,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        credit_data = data.get("data", {})
        return {
            "status": "ok",
            "remaining_credits": credit_data.get("remaining_credits", "未知"),
            "plan_credits": credit_data.get("plan_credits", "未知"),
            "billing_period_start": credit_data.get("billing_period_start", "未知"),
            "billing_period_end": credit_data.get("billing_period_end", "未知"),
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


def check_jina(api_key: str, proxies: dict[str, str] | None) -> dict:
    """检查 Jina 额度。Jina Reader 免费额度无法通过 API 查询，只能通过 dashboard 查看。"""

    return {
        "status": "unsupported",
        "message": "Jina Reader 免费额度无法通过 API 查询，请访问 https://jina.ai 查看。",
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="检查四工具 API 额度")
    parser.add_argument("--config", help="配置文件路径（JSON）")
    args = parser.parse_args()

    config = load_config(args.config)
    api_keys = config.get("api_keys", {})
    proxies = get_proxy(config)

    tools = {
        "Tavily": (api_keys.get("tavily", ""), check_tavily),
        "Exa": (api_keys.get("exa", ""), check_exa),
        "Firecrawl": (api_keys.get("firecrawl", ""), check_firecrawl),
        "Jina": (api_keys.get("jina", ""), check_jina),
    }

    print("=" * 50)
    print("四工具 API 额度检查")
    print("=" * 50)

    for name, (key, checker) in tools.items():
        print(f"\n[{name}]")
        if not key:
            print("  状态: 未配置 API Key")
            continue
        result = checker(key, proxies)
        if result["status"] == "ok":
            print(f"  状态: 正常")
            if name == "Tavily":
                print(f"  Key 用量: {result['key_usage']} / {result['key_limit']}")
                print(f"  账户套餐: {result['account_plan']}")
                print(f"  账户用量: {result['account_usage']} / {result['account_limit']}")
            elif name == "Firecrawl":
                print(f"  剩余额度: {result['remaining_credits']}")
                print(f"  套餐额度: {result['plan_credits']}")
                print(f"  计费周期: {result['billing_period_start']} ~ {result['billing_period_end']}")
        elif result["status"] == "unsupported":
            print(f"  状态: 不支持自动查询")
            print(f"  说明: {result['message']}")
        else:
            print(f"  状态: 异常")
            print(f"  错误: {result['error']}")

    print("\n" + "=" * 50)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
