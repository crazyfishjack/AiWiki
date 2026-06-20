#!/usr/bin/env python3
"""
Git 推送模块。

自动 commit 和 push 生成的调研报告。
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def git_push_report(report_path: str, query: str, wiki_root: str | None = None) -> bool:
    """将报告文件 commit 并 push 到仓库。

    Args:
        report_path: 报告文件路径
        query: 调研主题
        wiki_root: Wiki 根目录

    Returns:
        成功返回 True，失败返回 False
    """
    if wiki_root is None:
        wiki_root = "."

    # 配置 git 用户
    _run_git(["config", "user.name", "github-actions[bot]"], cwd=wiki_root)
    _run_git(["config", "user.email", "github-actions[bot]@users.noreply.github.com"], cwd=wiki_root)

    # git add
    result = _run_git(["add", report_path], cwd=wiki_root)
    if result.returncode != 0:
        print(f"[Git] git add 失败", file=sys.stderr)
        return False

    # git commit
    commit_msg = f"[auto-research] {query}"
    result = _run_git(["commit", "-m", commit_msg], cwd=wiki_root)
    if result.returncode != 0:
        # 可能是没有变更
        print(f"[Git] git commit 失败或无变更", file=sys.stderr)
        return False

    # git push
    result = _run_git(["push", "origin", "main"], cwd=wiki_root)
    if result.returncode != 0:
        # 尝试 pull --rebase 后重试
        print("[Git] push 失败，尝试 rebase...", file=sys.stderr)
        _run_git(["pull", "--rebase", "origin", "main"], cwd=wiki_root)
        result = _run_git(["push", "origin", "main"], cwd=wiki_root)
        if result.returncode != 0:
            print(f"[Git] push 重试失败", file=sys.stderr)
            return False

    print("[Git] 推送成功")
    return True


def _run_git(args: list[str], cwd: str | None = None) -> subprocess.CompletedProcess:
    """执行 git 命令。"""
    cmd = ["git"] + args
    return subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--query", required=True)
    args = parser.parse_args()

    success = git_push_report(args.path, args.query)
    sys.exit(0 if success else 1)
