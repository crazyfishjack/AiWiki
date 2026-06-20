#!/usr/bin/env python3
"""
自动调研主入口脚本。

完整管道：config → issue_parser → research_runner → llm_compiler → git_pusher → wechat_notifier
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import traceback
from pathlib import Path

# 添加脚本目录到路径
script_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(script_dir))

from config_loader import load_config, require_valid_config
from issue_parser import get_query, parse_args
from llm_compiler import compile_evidence, save_compiled_report
from git_pusher import git_push_report
from wechat_notifier import send_notification


def main() -> int:
    """主入口。"""
    print("=" * 60)
    print("自动调研脚本启动")
    print("=" * 60)

    # 1. 解析参数
    args = parse_args()

    # 2. 获取查询
    query = get_query(args)
    if not query:
        print("[ERROR] 未找到调研主题", file=sys.stderr)
        return 1

    print(f"[INFO] 调研主题: {query}")

    # 3. 加载配置
    print("[INFO] 加载配置...")
    config = load_config()
    require_valid_config(config)
    print("[INFO] 配置加载成功")

    # 4. 执行调研（调用 four_tool_research.py）
    print("[INFO] 开始执行调研...")
    evidence_path = _run_four_tool_research(query, config)
    if not evidence_path:
        _handle_failure(query, "调研执行", "四工具调研失败，未生成证据包")
        return 1

    print(f"[INFO] 证据包生成: {evidence_path}")

    # 5. LLM 编译
    print("[INFO] 开始 LLM 编译...")
    report_text = compile_evidence(evidence_path, config, query)
    if not report_text:
        print("[WARN] LLM 编译失败，使用原始证据包", file=sys.stderr)
        # 回退：使用原始证据包
        with Path(evidence_path).open("r", encoding="utf-8") as f:
            report_text = f.read()

    # 6. 保存报告
    wiki_root = config.get("wiki_root", ".")
    raw_dir = config.get("raw_default_dir", "raw/articles")
    report_path = save_compiled_report(report_text, raw_dir, query)
    print(f"[INFO] 报告已保存: {report_path}")

    # 7. Git 推送
    print("[INFO] 开始 Git 推送...")
    success = git_push_report(report_path, query, wiki_root)
    if not success:
        _handle_failure(query, "Git 推送", "推送失败")
        return 1

    print("[INFO] Git 推送成功")

    # 8. 企业微信通知
    print("[INFO] 发送企业微信通知...")
    send_notification(
        query=query,
        status="success",
        report_path=report_path
    )

    print("=" * 60)
    print("自动调研完成")
    print("=" * 60)
    return 0


def _run_four_tool_research(query: str, config: dict) -> str | None:
    """调用 four_tool_research.py 执行调研。

    在 Actions 环境中，需要创建临时配置文件。
    """
    # 定位 four_tool_research.py
    script_dir = Path(__file__).resolve().parent
    four_tool_script = script_dir.parent.parent / ".trae" / "skills" / "wiki-research" / "scripts" / "four_tool_research.py"

    if not four_tool_script.exists():
        # 尝试其他路径
        four_tool_script = Path(".trae/skills/wiki-research/scripts/four_tool_research.py")

    if not four_tool_script.exists():
        print("[ERROR] 找不到 four_tool_research.py", file=sys.stderr)
        return None

    # 创建临时配置文件
    temp_config = _create_temp_config(config)
    if not temp_config:
        print("[ERROR] 创建临时配置失败", file=sys.stderr)
        return None

    # 构建命令
    cmd = [
        sys.executable,
        str(four_tool_script),
        "--query", query,
        "--mode", "standard",
        "--raw-dir", "raw/articles",
        "--config", str(temp_config)
    ]

    print(f"[Research] 执行: {' '.join(cmd)}")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
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

        print("[Research] 警告: 未找到 RAW_RESEARCH_FILE", file=sys.stderr)
        return None

    except subprocess.TimeoutExpired:
        print("[Research] 调研超时（超过 10 分钟）", file=sys.stderr)
        return None
    except Exception as e:
        print(f"[Research] 执行异常: {e}", file=sys.stderr)
        return None


def _create_temp_config(config: dict) -> Path | None:
    """创建临时配置文件供 four_tool_research.py 使用。"""
    try:
        # 合并配置
        temp_config = {
            "wiki_root": config.get("wiki_root", "."),
            "raw_default_dir": config.get("raw_default_dir", "raw/articles"),
            "proxy": config.get("proxy", ""),
            "api_keys": config.get("api_keys", {}),
            "research_defaults": config.get("research_defaults", {
                "max_subqueries": 6,
                "max_deep_read_urls": 10,
                "exa_highlight_char_limit": 4000,
                "evidence_full_content": True,
                "tavily_min_score": 0.4
            })
        }

        temp_path = Path("/tmp/wiki_research_config.json")
        temp_path.parent.mkdir(parents=True, exist_ok=True)
        with temp_path.open("w", encoding="utf-8") as f:
            json.dump(temp_config, f, ensure_ascii=False, indent=2)

        return temp_path
    except Exception as e:
        print(f"[ERROR] 创建临时配置失败: {e}", file=sys.stderr)
        return None


def _handle_failure(query: str, step: str, error_summary: str) -> None:
    """处理失败情况。"""
    print(f"[ERROR] {step} 失败: {error_summary}", file=sys.stderr)

    # 尝试发送失败通知
    try:
        send_notification(
            query=query,
            status="failure",
            error_step=step,
            error_summary=error_summary
        )
    except Exception:
        pass  # 通知失败不中断


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[FATAL] 未捕获异常: {e}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)
