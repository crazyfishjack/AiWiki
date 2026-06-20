#!/usr/bin/env python3
"""
调研执行模块。

封装调用 four_tool_research.py 的逻辑。
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def run_research(query: str, wiki_root: str | None = None) -> str | None:
    """运行四工具调研，返回证据包文件路径。

    Args:
        query: 调研主题
        wiki_root: Wiki 根目录路径，默认从环境变量或当前目录推断

    Returns:
        证据包文件路径，失败时返回 None
    """
    if wiki_root is None:
        wiki_root = os.environ.get("WIKI_ROOT", ".")

    # 定位 four_tool_research.py
    script_dir = Path(__file__).resolve().parent
    four_tool_script = script_dir.parent.parent / ".trae" / "skills" / "wiki-research" / "scripts" / "four_tool_research.py"

    if not four_tool_script.exists():
        # 尝试其他路径
        four_tool_script = Path(wiki_root) / ".trae" / "skills" / "wiki-research" / "scripts" / "four_tool_research.py"

    if not four_tool_script.exists():
        print(f"错误: 找不到 four_tool_research.py", file=sys.stderr)
        return None

    # 构建命令
    cmd = [
        sys.executable,
        str(four_tool_script),
        "--query", query,
        "--mode", "standard",
        "--raw-dir", "raw/articles"
    ]

    print(f"[Research] 执行: {' '.join(cmd)}")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=wiki_root,
            timeout=600  # 10 分钟超时
        )

        print(f"[Research] 返回码: {result.returncode}")
        if result.stdout:
            print(f"[Research] stdout:\n{result.stdout}")
        if result.stderr:
            print(f"[Research] stderr:\n{result.stderr}", file=sys.stderr)

        if result.returncode != 0:
            print(f"[Research] 调研失败，返回码: {result.returncode}", file=sys.stderr)
            return None

        # 解析 RAW_RESEARCH_FILE
        for line in result.stdout.split("\n"):
            if line.startswith("RAW_RESEARCH_FILE="):
                return line[len("RAW_RESEARCH_FILE="):].strip()

        # 如果没有找到 RAW_RESEARCH_FILE，尝试从输出中推断
        print("[Research] 警告: 未找到 RAW_RESEARCH_FILE，尝试推断...", file=sys.stderr)
        return None

    except subprocess.TimeoutExpired:
        print("[Research] 调研超时（超过 10 分钟）", file=sys.stderr)
        return None
    except Exception as e:
        print(f"[Research] 执行异常: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    args = parser.parse_args()

    path = run_research(args.query)
    if path:
        print(f"RAW_RESEARCH_FILE={path}")
    else:
        print("调研失败", file=sys.stderr)
        sys.exit(1)
