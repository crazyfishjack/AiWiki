#!/usr/bin/env python3
"""
企业微信通知模块。

通过 webhook 推送调研完成/失败通知。
"""

from __future__ import annotations

import json
import os
import sys
from typing import Any

try:
    import requests
except ImportError:
    requests = None  # type: ignore


def send_notification(
    query: str,
    status: str,
    report_path: str | None = None,
    conclusions: list[str] | None = None,
    error_step: str | None = None,
    error_summary: str | None = None,
    actions_url: str | None = None,
    webhook_url: str | None = None,
    report_text: str | None = None
) -> bool:
    """发送企业微信通知。

    Args:
        query: 调研主题
        status: "success" 或 "failure"
        report_path: 报告文件路径
        conclusions: 核心结论列表
        error_step: 失败环节
        error_summary: 错误摘要
        actions_url: GitHub Actions 运行日志链接
        webhook_url: 企业微信 webhook URL
        report_text: 报告完整内容，用于提取核心结论

    Returns:
        成功返回 True，失败返回 False
    """
    if requests is None:
        print("[WeChat] 错误: 缺少 requests 依赖", file=sys.stderr)
        return False

    if webhook_url is None:
        webhook_url = os.environ.get("WECHAT_WEBHOOK_URL")

    if not webhook_url:
        print("[WeChat] 警告: 未配置企业微信 webhook，跳过通知")
        return True  # 不中断管道

    # 构造消息
    if status == "success":
        content = _build_success_message(query, report_path, conclusions, report_text)
    else:
        content = _build_failure_message(query, error_step, error_summary, actions_url)

    payload = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    }

    try:
        print("[WeChat] 发送通知...")
        response = requests.post(webhook_url, json=payload, timeout=30)
        response.raise_for_status()
        print("[WeChat] 通知发送成功")
        return True
    except requests.exceptions.RequestException as e:
        print(f"[WeChat] 通知发送失败: {e}", file=sys.stderr)
        return False


def _extract_conclusions_from_report(report_text: str) -> list[str]:
    """从报告文本中提取核心结论。"""
    conclusions = []
    lines = report_text.split("\n")
    in_conclusions = False

    for line in lines:
        stripped = line.strip()

        # 检测核心结论章节
        if "## 核心结论" in stripped or "##核心结论" in stripped:
            in_conclusions = True
            continue

        # 遇到下一个章节标题，结束提取
        if in_conclusions and stripped.startswith("## ") and "核心结论" not in stripped:
            break

        # 提取结论条目
        if in_conclusions and stripped:
            # 匹配数字开头的条目：1. xxx 或 1、xxx
            if stripped[0].isdigit() and ("." in stripped[:3] or "、" in stripped[:3]):
                conclusion = stripped.split(".", 1)[-1].split("、", 1)[-1].strip()
                if conclusion:
                    conclusions.append(conclusion)
            # 匹配 - 或 * 开头的条目
            elif stripped.startswith("-") or stripped.startswith("*"):
                conclusion = stripped[1:].strip()
                if conclusion:
                    conclusions.append(conclusion)

    return conclusions[:5]  # 最多取 5 条


def _build_success_message(
    query: str,
    report_path: str | None,
    conclusions: list[str] | None,
    report_text: str | None = None
) -> str:
    """构造成功通知消息。"""
    from datetime import datetime
    import re

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 如果没有传入 conclusions，尝试从 report_text 提取
    if not conclusions and report_text:
        conclusions = _extract_conclusions_from_report(report_text)

    # 构造 GitHub 报告链接
    report_url = ""
    if report_path:
        # 提取相对路径
        repo_path = report_path.replace("\\", "/")
        if "raw/articles/" in repo_path:
            filename = repo_path.split("raw/articles/")[-1]
            report_url = f"https://github.com/crazyfishjack/AiWiki/blob/main/raw/articles/{filename}"
        else:
            report_url = f"https://github.com/crazyfishjack/AiWiki/tree/main/raw/articles"

    content = f"""## 调研完成

**主题**: {query}
**时间**: {timestamp}
"""

    # 核心结论
    if conclusions:
        content += "\n**核心结论**:\n"
        for i, conclusion in enumerate(conclusions[:5], 1):
            # 截断过长的结论
            if len(conclusion) > 100:
                conclusion = conclusion[:97] + "..."
            content += f"> {i}. {conclusion}\n"
    else:
        content += "\n> 报告已生成，点击查看详情\n"

    # 报告链接
    if report_url:
        content += f"\n**[查看完整报告]({report_url})**"

    return content


def _build_failure_message(
    query: str,
    error_step: str | None,
    error_summary: str | None,
    actions_url: str | None
) -> str:
    """构造失败通知消息。"""
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = f"""## 调研失败

**主题**: {query}
**时间**: {timestamp}
"""

    if error_step:
        content += f"\n**失败环节**: {error_step}\n"

    if error_summary:
        # 截断错误信息
        error_text = error_summary[:200] + "..." if len(error_summary) > 200 else error_summary
        content += f"**错误**: {error_text}\n"

    if actions_url:
        content += f"\n**[查看日志]({actions_url})**"

    return content


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--status", choices=["success", "failure"], required=True)
    parser.add_argument("--path", default=None)
    parser.add_argument("--error-step", default=None)
    parser.add_argument("--error-summary", default=None)
    args = parser.parse_args()

    success = send_notification(
        query=args.query,
        status=args.status,
        report_path=args.path,
        error_step=args.error_step,
        error_summary=args.error_summary
    )
    sys.exit(0 if success else 1)
