#!/usr/bin/env python3
"""
LLM 编译模块。

调用阿里云百炼 API 将证据包编译为中文调研报告。
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

try:
    import requests
except ImportError:
    requests = None  # type: ignore


def compile_evidence(
    evidence_path: str,
    config: dict[str, Any],
    query: str
) -> str | None:
    """调用阿里云 Qwen 编译证据包为中文调研报告。

    Args:
        evidence_path: 证据包文件路径
        config: 配置字典，包含 llm_config 和 api_keys
        query: 原始调研查询

    Returns:
        编译后的报告文本，失败时返回 None
    """
    if requests is None:
        print("[LLM] 错误: 缺少 requests 依赖", file=sys.stderr)
        return None

    # 读取证据包
    try:
        with Path(evidence_path).open("r", encoding="utf-8") as f:
            evidence_content = f.read()
    except OSError as e:
        print(f"[LLM] 读取证据包失败: {e}", file=sys.stderr)
        return None

    # 获取 LLM 配置
    llm_config = config.get("llm_config", {})
    base_url = llm_config.get("base_url", "https://dashscope.aliyuncs.com/compatible-mode/v1")
    model = llm_config.get("model", "qwen3.5-plus")
    max_tokens = llm_config.get("max_tokens", 32000)
    temperature = llm_config.get("temperature", 0.3)

    api_key = config.get("api_keys", {}).get("aliyun")
    if not api_key:
        print("[LLM] 错误: 缺少阿里云 API Key", file=sys.stderr)
        return None

    # 构造提示词
    prompt = _build_prompt(evidence_content, query)

    # 调用 API
    url = f"{base_url}/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "你是一个专业的调研报告撰写助手。请基于提供的证据包，生成结构化的中文调研报告。"},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    # 重试机制
    for attempt in range(3):
        try:
            print(f"[LLM] 调用阿里云 API (尝试 {attempt + 1}/3)...")
            response = requests.post(url, headers=headers, json=payload, timeout=500)

            if response.status_code == 429:
                print(f"[LLM] 遇到速率限制，等待 5 秒后重试...")
                time.sleep(5)
                continue

            response.raise_for_status()
            data = response.json()

            # 提取生成的内容
            if "choices" in data and len(data["choices"]) > 0:
                content = data["choices"][0].get("message", {}).get("content", "")
                if content:
                    print(f"[LLM] 编译成功，生成 {len(content)} 字符")
                    return content
                else:
                    print("[LLM] 警告: API 返回空内容", file=sys.stderr)
                    return None
            else:
                print(f"[LLM] 警告: 未找到 choices: {data}", file=sys.stderr)
                return None

        except requests.exceptions.Timeout:
            print(f"[LLM] 请求超时，尝试 {attempt + 1}/3", file=sys.stderr)
            if attempt < 2:
                time.sleep(5)
            continue
        except requests.exceptions.RequestException as e:
            print(f"[LLM] 请求异常: {e}", file=sys.stderr)
            if attempt < 2:
                time.sleep(5)
            continue

    print("[LLM] 错误: 3 次重试后仍失败", file=sys.stderr)
    return None


def _build_prompt(evidence_content: str, query: str) -> str:
    """构造编译提示词。"""
    prompt = f"""请基于以下证据包，生成一份结构化的中文调研报告。

调研主题：{query}

证据包内容：
{evidence_content}

请按以下结构生成报告：

## 核心结论
（3-7 条可复用结论，每条带来源和可信度）

## 内容整理
（保留所有有用的信息，系统化，结构清晰，逻辑正确）

## 推荐工作流
（如何组合使用这些工具）

## 适用场景
（适合采用该方法的项目类型）

## 不适用场景
（何时会过度工程）

## 风险与约束
（衔接点、上下文、测试、规格漂移等风险）

## 信源质量门控记录
（保留信源、剔除信源、来源等级）

## 来源与可信度
（关键来源、来源类型、可信度）

## 对于可信度较高的来源逐来源总结
（逐篇整理高可信来源的核心内容）

## 跨源矛盾检测结论
（检测核心数字、日期、功能描述等矛盾）

## 矛盾与待验证问题
（保留冲突或证据不足处）

## 原始证据摘录
（保留必要摘录）

要求：
- 用中文输出
- 每条关键事实后标注 `[来源: URL]`
- 每条核心结论标注可信度：高 / 中 / 低
- 不得把无 URL 支撑的内容写成事实
"""
    return prompt


def save_compiled_report(report_text: str, raw_dir: str, query: str) -> str:
    """保存编译后的报告到 raw 目录。

    Returns:
        保存的文件路径
    """
    from datetime import date
    import hashlib

    today = date.today().isoformat()
    slug = re.sub(r"[^\w\u4e00-\u9fff]+", "-", query).strip("-").lower()[:40]
    if not slug:
        slug = hashlib.md5(query.encode()).hexdigest()[:8]

    filename = f"{today}-{slug}-compiled.md"
    output_path = Path(raw_dir) / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        f.write(report_text)

    print(f"[LLM] 报告已保存: {output_path}")
    return str(output_path)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--query", required=True)
    args = parser.parse_args()

    # 加载配置
    from config_loader import load_config
    config = load_config()

    result = compile_evidence(args.evidence, config, args.query)
    if result:
        print(result)
    else:
        print("编译失败", file=sys.stderr)
        sys.exit(1)
