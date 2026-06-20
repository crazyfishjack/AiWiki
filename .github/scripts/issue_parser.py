#!/usr/bin/env python3
"""
Issue 解析模块。

从 GitHub Actions 事件 JSON 或命令行参数提取调研查询。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description="自动调研脚本")
    parser.add_argument("--query", help="直接传入调研主题，跳过 issue 解析")
    return parser.parse_args()


def extract_query_from_issue(event_path: str | None = None) -> str | None:
    """从 GitHub Issue 事件 JSON 提取调研查询。

    返回 None 表示非调研 issue 或提取失败。
    """
    if event_path is None:
        event_path = os.environ.get("GITHUB_EVENT_PATH")

    if not event_path:
        return None

    path = Path(event_path)
    if not path.exists():
        return None

    try:
        with path.open("r", encoding="utf-8") as f:
            event = json.load(f)
    except (json.JSONDecodeError, OSError):
        return None

    issue = event.get("issue", {})
    title = issue.get("title", "")
    body = issue.get("body", "") or ""

    # 检查标题是否以 [调研] 开头
    if not title.startswith("[调研]"):
        return None

    # 提取查询内容
    query = title[len("[调研]"):].strip()

    # 如果标题只有 [调研]，使用正文第一行
    if not query and body:
        query = body.strip().split("\n")[0].strip()

    return query if query else None


def get_query(args: argparse.Namespace | None = None) -> str | None:
    """获取调研查询。

    优先级：
    1. 命令行 --query 参数
    2. GitHub Issue 事件
    3. None
    """
    # 1. 命令行参数
    if args and args.query:
        return args.query

    # 2. GitHub Issue
    return extract_query_from_issue()


def main() -> int:
    """CLI 入口。"""
    args = parse_args()
    query = get_query(args)

    if query is None:
        print("未找到调研主题。请使用 --query 参数或创建 [调研] 开头的 issue。", file=sys.stderr)
        return 1

    print(f"QUERY={query}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
