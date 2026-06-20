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
    webhook_url: str | None = None
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
        content = _build_success_message(query, report_path, conclusions)
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


def _build_success_message(
    query: str,
    report_path: str | None,
    conclusions: list[str] | None
) -> str:
    """构造成功通知消息。"""
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = f"""## 自动调研完成

**调研主题**: {query}
**执行时间**: {timestamp}
"""

    if report_path:
        content += f"**报告路径**: {report_path}\n"

    if conclusions:
        content += "\n**核心结论**:\n"
        for i, conclusion in enumerate(conclusions[:5], 1):
            content += f"{i}. {conclusion}\n"

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

    content = f"""## 自动调研失败

**调研主题**: {query}
**失败时间**: {timestamp}
"""

    if error_step:
        content += f"**失败环节**: {error_step}\n"

    if error_summary:
        content += f"**错误摘要**: {error_summary}\n"

    if actions_url:
        content += f"**查看日志**: [Actions 运行日志]({actions_url})\n"

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
