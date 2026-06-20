#!/usr/bin/env python3
"""
自动调研主入口脚本。

完整管道：config → issue_parser → research_runner → llm_compiler → git_pusher → wechat_notifier
"""

from __future__ import annotations

import os
import sys
import traceback
from pathlib import Path

# 添加脚本目录到路径
script_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(script_dir))

from config_loader import load_config, require_valid_config
from issue_parser import get_query, parse_args
from research_runner import run_research
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

    # 4. 执行调研
    print("[INFO] 开始执行调研...")
    evidence_path = run_research(query)
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
