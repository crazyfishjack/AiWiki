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
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:
    requests = None  # type: ignore
    HTTPAdapter = None  # type: ignore
    Retry = None  # type: ignore


MODEL_WINDOW_LIMITS = {
    "qwen3-7b-plus": (128_000, 32_000),
    "qwen3.7-plus": (128_000, 32_000),
    "qwen3.7-max": (1_000_000, 65_536),
    "qwen3-14b-plus": (128_000, 32_000),
    "qwen3.14-plus": (128_000, 32_000),
    "qwen3-30b-plus": (128_000, 32_000),
    "qwen3.30b-plus": (128_000, 32_000),
    "qwen3-32b-plus": (128_000, 32_000),
    "qwen3.32b-plus": (128_000, 32_000),
    "qwen3-7b": (32_000, 8_000),
    "qwen3.7b": (32_000, 8_000),
    "qwen3-14b": (32_000, 8_000),
    "qwen3.14b": (32_000, 8_000),
    "qwen3-30b-a3b": (128_000, 32_000),
    "qwen3.30b-a3b": (128_000, 32_000),
    "qwen-plus": (128_000, 32_000),
    "qwen-max": (1_048_576, 8_192),
    "qwen3.5-plus": (120_000, 60_000),
    "qwen3.5-max": (1_048_576, 8_192),
    "qwen-turbo": (128_000, 8_192),
    "qwen-long": (1_048_576, 8_192),
    "qwen2.5-72b-instruct": (32_000, 8_192),
    "qwen2.5-32b-instruct": (32_000, 8_192),
    "qwen2.5-14b-instruct": (32_000, 8_192),
    "qwen2.5-7b-instruct": (32_000, 8_192),
    "_default": (128_000, 32_000),
}

SYSTEM_PROMPT_TEXT = (
    "你是一名严谨的信息整理师。你的任务是：从提供的证据包中，逐来源地、逐章节地提取并组织信息，"
    "原样呈现到最终报告中。你不做创造性写作，不做摘要压缩，不做'去冗余'的合并。"
    "你的产出标准是：一个人只读你的整理结果，就能还原证据包中 95% 以上的有信息量的内容，"
    "包括技术细节、案例、数据、表格、时间线、架构演进、对架构师的启示、风险、组织实践等。"
    "如果证据包中某个章节或段落你无法确定应放在最终报告的哪个位置，你保留它并标注[待整理]，而不是丢弃它。"
    "你的工作原则：忠于原始证据，不遗漏分析性内容，不将段落压缩为参数列表，不编造无依据信息。"
)

USER_PROMPT_TEMPLATE = (
    "# 任务\n\n"
    "基于以下证据包，生成一份详细、可靠的中文调研报告。\n\n"
    "调研主题：[QUERY_PLACEHOLDER]\n\n"
    "[REQUIREMENTS_PLACEHOLDER]\n"
    "## 报告结构\n\n"
    "## 核心结论\n"
    "- 从证据包中提取 3-7 条可复用结论\n"
    "- 每条结论必须带来源和可信度标注\n"
    "- 禁止只写结论不写支撑证据\n\n"
    "## 内容整理\n"
    "**这是最重要的章节**。对证据包进行统一分析，不分组、不分来源，将所有有用信息完整保留在此章节中。\n\n"
    "### 编写要求：\n"
    "- 证据包中的每个主要章节（以数字编号的节）必须有对应内容，不能跳过\n"
    "- 证据包中每句有用的表述（并非脏数据水印等就算有用数据）都需要保留，不得简要带过，需要仔细整理\n"
    "- 技术架构：分层设计、组件、接口、数据流等细节全部保留\n"
    "- 实现机制：算法、流程、配置、代码等全部保留\n"
    "- 案例数据：客户名称、项目金额、效果指标、时间线等全部保留\n"
    "- 启示建议：'对架构师的启示'、'行动建议'、'落地步骤'等全部保留\n"
    "- 历史演进：版本迭代、架构演化等全部保留\n"
    "- 格式保持：表格→表格，列表→列表，代码→代码块，数据→具体数值\n"
    "- 具体数值不得约化（如 80.25% 不能写成约 80%）\n"
    "- 不得用'包括但不限于'、'等'替代具体列表项\n"
    "- 禁止把表格转为文字描述\n"
    "- 多个来源中重复的内容合并为一条即可，避免冗余\n\n"
    "## 推荐工作流\n"
    "- 说明如何组合使用这些工具\n"
    "- 提供具体的执行步骤和配置方法\n"
    "- 必须包含从证据包中提取的具体操作建议\n\n"
    "## 适用场景\n"
    "- 列出适合采用该方法的项目类型\n"
    "- 每个场景必须有具体说明\n"
    "- 必须引用证据包中的实际案例\n\n"
    "## 不适用场景\n"
    "- 说明何时会过度工程或不值得引入\n"
    "- 每个场景必须有具体说明\n"
    "- 必须引用证据包中的限制条件\n\n"
    "## 风险与约束\n"
    "- 列出衔接点、上下文、测试、规格漂移等风险\n"
    "- 每个风险必须有详细描述和应对措施\n"
    "- 必须引用证据包中的具体风险案例\n\n"
    "## 跨源矛盾检测\n"
    "- 检测核心数字、日期、功能描述等矛盾\n"
    "- 逐项列出矛盾项，说明来源和初步判断\n"
    "- 未发现矛盾也必须明确写出\n\n"
    "## 矛盾与待验证问题\n"
    "- 保留冲突或证据不足处\n"
    "- 每个问题必须有具体描述和建议\n\n"
    "## 原始证据摘录\n"
    "- 保留支持结论的必要摘录或完整证据片段\n"
    "- 摘录必须包含来源标注\n\n"
    "------------------------------------------------------------\n\n"
    "以下是完整的证据包内容：\n\n"
    "------------------------------------------------------------\n\n"
    "[QUERY_PLACEHOLDER2]\n"
)


def estimate_tokens(text: str) -> int:
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    eng_words = len(re.findall(r"[a-zA-Z]{2,}", text))
    punct = len(re.findall(r"[\d\s\.,;:!?\(\)\-+{}\[\]|\\/#]", text))
    other = max(0, len(text) - cjk - eng_words * 2 - punct)
    return int(cjk * 1.75 + eng_words * 1.2 + punct * 0.4 + other * 0.5)


def get_model_window(model_name: str) -> tuple:
    if model_name in MODEL_WINDOW_LIMITS:
        return MODEL_WINDOW_LIMITS[model_name]
    for key in MODEL_WINDOW_LIMITS:
        if key == "_default":
            continue
        for suffix in ["", "-plus", ".plus", "-max", ".max"]:
            if model_name.startswith(key + suffix):
                return MODEL_WINDOW_LIMITS[key]
    return MODEL_WINDOW_LIMITS["_default"]


def log_llm_call_start(
    model: str,
    evidence_tokens: int,
    evidence_chars: int,
    query_chars: int,
    max_output_tokens: int,
    max_input_window: int,
) -> int:
    system_tokens = estimate_tokens(SYSTEM_PROMPT_TEXT)
    fixed_prompt_tokens = estimate_tokens(USER_PROMPT_TEMPLATE)
    query_tokens = min(query_chars // 2, 300)
    total_input = system_tokens + fixed_prompt_tokens + query_tokens + evidence_tokens

    print("", flush=True)
    print("=" * 60, flush=True)
    print("【LLM 调用诊断 - 调用前】", flush=True)
    print("=" * 60, flush=True)
    print("[LLM] 模型名称             : " + model, flush=True)
    print("[LLM] 模型上下文窗口上限   : " + str(max_input_window) + " tokens", flush=True)
    print("[LLM] 模型最大输出上限     : " + str(max_output_tokens) + " tokens", flush=True)
    print("-" * 60, flush=True)
    print("[LLM] System prompt        : ~" + str(system_tokens) + " tokens (~" + str(len(SYSTEM_PROMPT_TEXT)) + " 字符)", flush=True)
    print("[LLM] 固定指令前缀         : ~" + str(fixed_prompt_tokens) + " tokens (~" + str(len(USER_PROMPT_TEMPLATE)) + " 字符)", flush=True)
    print("[LLM] Query               : ~" + str(query_tokens) + " tokens (~" + str(query_chars) + " 字符)", flush=True)
    print("[LLM] 证据包              : ~" + str(evidence_tokens) + " tokens (~" + str(evidence_chars) + " 字符)", flush=True)
    print("-" * 60, flush=True)
    print("[LLM] 估算输入总量         : ~" + str(total_input) + " tokens", flush=True)
    print("[LLM] 上下文窗口上限       : " + str(max_input_window) + " tokens", flush=True)

    if total_input > max_input_window:
        overflow = total_input - max_input_window
        pct = total_input / max_input_window * 100
        print("[LLM] WARNING 输入超过上下文窗口 " + str(overflow) + " tokens（" + str(int(pct)) + "%），前半部分将被丢弃", flush=True)
        print("[LLM] WARNING 建议：将证据包分块后多次调用，或换用大上下文模型（qwen-max/qwen-long）", flush=True)
    elif total_input > max_input_window * 0.85:
        print("[LLM] WARNING 输入接近上下文上限（" + str(int(total_input / max_input_window * 100)) + "%），存在截断风险", flush=True)
    else:
        print("[LLM] OK 输入在上下文窗口内（" + str(int(total_input / max_input_window * 100)) + "%）", flush=True)

    print("[LLM] 最大输出上限         : " + str(max_output_tokens) + " tokens", flush=True)
    print("=" * 60, flush=True)
    return total_input


def log_llm_call_end(
    data: dict,
    finish_reason: str,
    content_chars: int,
) -> None:
    usage = data.get("usage") or {}
    prompt_tokens = usage.get("prompt_tokens", 0) if usage else 0
    completion_tokens = usage.get("completion_tokens", 0) if usage else 0
    total_tokens = usage.get("total_tokens", 0) if usage else 0

    print("", flush=True)
    print("=" * 60, flush=True)
    print("【LLM 调用诊断 - 调用后】", flush=True)
    print("=" * 60, flush=True)
    print("[LLM] finish_reason        : " + finish_reason, flush=True)
    if finish_reason == "length":
        print("[LLM] WARNING 输出被 max_tokens 上限截断（finish_reason=length）", flush=True)
    elif finish_reason == "stop":
        print("[LLM] OK 模型自然停止（非截断）", flush=True)
    print("-" * 60, flush=True)
    print("[LLM] 实际输入 tokens      : " + str(prompt_tokens) + " tokens (API 实测)", flush=True)
    print("[LLM] 实际输出 tokens      : " + str(completion_tokens) + " tokens (API 实测)", flush=True)
    print("[LLM] 实际总 tokens        : " + str(total_tokens) + " tokens", flush=True)
    print("[LLM] 输出文本长度         : " + str(content_chars) + " 字符", flush=True)
    ratio = completion_tokens / prompt_tokens * 100 if prompt_tokens > 0 else 0
    print("[LLM] 输出/输入比          : " + ("%.1f" % ratio) + "% (completion/prompt)", flush=True)
    print("=" * 60, flush=True)


def _build_session() -> Any:
    """构建带有指数退避重试策略的 Session。"""
    session = requests.Session()
    if HTTPAdapter is not None and Retry is not None:
        retry_strategy = Retry(
            total=5,
            backoff_factor=2,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["POST"],
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)
        session.mount("http://", adapter)
    return session


def _parse_sse_chunk(chunk_bytes: bytes) -> tuple[str, dict]:
    """解析一条 SSE chunk，返回 (event_type, data_dict)。

    正常数据行：data: {"choices": [...]}
    结束行：data: [DONE]
    """
    try:
        line = chunk_bytes.decode("utf-8", errors="replace").strip()
    except Exception:
        return "", {}

    if not line:
        return "", {}

    if not line.startswith("data:"):
        return "", {}

    data_str = line[5:].strip()
    if not data_str:
        return "", {}

    if data_str == "[DONE]":
        return "done", {}

    try:
        data_dict = json.loads(data_str)
        return "content", data_dict
    except json.JSONDecodeError:
        return "", {}


def _stream_call_api(
    url: str,
    headers: dict,
    payload: dict,
) -> tuple[str, str, dict]:
    """流式调用 LLM API，边收边存。

    返回 (content, finish_reason, last_chunk_data)。
    """
    content_parts: list[str] = []
    finish_reason = "unknown"
    last_data: dict = {}
    char_count = 0
    last_log_time = time.time()

    session = _build_session()
    try:
        response = session.post(
            url,
            headers=headers,
            json=payload,
            timeout=(10, 600),
            stream=True,
        )

        if response.status_code == 429:
            print("[LLM] 遇到速率限制 (429)，等待 5 秒后重试...", flush=True)
            time.sleep(5)
            return "", "rate_limit", {}

        response.raise_for_status()

        print("[LLM] 开始流式接收响应...", flush=True)

        for chunk in response.iter_lines(decode_unicode=False, delimiter=b"\n"):
            if not chunk:
                continue

            event_type, data_dict = _parse_sse_chunk(chunk)

            if event_type == "done":
                break

            if event_type == "content":
                # OpenAI 兼容格式：choices[0].delta.content
                choices = data_dict.get("choices", [])
                if choices:
                    choice = choices[0]
                    delta = choice.get("delta", {})
                    delta_content = delta.get("content", "")
                    if delta_content:
                        content_parts.append(delta_content)
                        char_count += len(delta_content)

                    # 记录 finish_reason（可能在最后一个 chunk 中）
                    fr = choice.get("finish_reason")
                    if fr:
                        finish_reason = fr
                        last_data = data_dict
                    elif data_dict.get("usage"):
                        last_data = data_dict

                # 每 5 秒打印一次进度
                current_time = time.time()
                if current_time - last_log_time >= 5:
                    print("[LLM] 已接收 " + str(char_count) + " 字符...", flush=True)
                    last_log_time = current_time
    finally:
        session.close()

    content = "".join(content_parts)
    return content, finish_reason, last_data


def compile_evidence(
    evidence_path: str,
    config: dict,
    query: str,
    requirements: str | None = None,
) -> str | None:
    if requests is None:
        print("[LLM] 错误: 缺少 requests 依赖", file=sys.stderr)
        return None

    try:
        with Path(evidence_path).open("r", encoding="utf-8") as f:
            evidence_content = f.read()
    except OSError as e:
        print("[LLM] 读取证据包失败: " + str(e), file=sys.stderr)
        return None

    evidence_tokens = estimate_tokens(evidence_content)

    llm_config = config.get("llm_config", {})
    base_url = llm_config.get("base_url", "https://dashscope.aliyuncs.com/compatible-mode/v1")
    model = llm_config.get("model", "qwen3.5-plus")
    max_output_tokens = llm_config.get("max_tokens", 60000)
    temperature = llm_config.get("temperature", 0.3)

    api_key = config.get("api_keys", {}).get("aliyun")
    if not api_key:
        print("[LLM] 错误: 缺少阿里云 API Key", file=sys.stderr)
        return None

    max_input_window, _ = get_model_window(model)

    log_llm_call_start(
        model=model,
        evidence_tokens=evidence_tokens,
        evidence_chars=len(evidence_content),
        query_chars=len(query),
        max_output_tokens=max_output_tokens,
        max_input_window=max_input_window,
    )

    # 构建 requirements 部分
    requirements_section = ""
    if requirements:
        requirements_section = "## 额外整理要求\n" + requirements + "\n\n"

    prompt = USER_PROMPT_TEMPLATE.replace("[QUERY_PLACEHOLDER]", query).replace("[REQUIREMENTS_PLACEHOLDER]", requirements_section).replace("[QUERY_PLACEHOLDER2]", evidence_content)

    url = base_url + "/chat/completions"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_TEXT},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_output_tokens,
        "temperature": temperature,
        "stream": True,
        "stream_options": {"include_usage": True},
    }

    for attempt in range(3):
        try:
            print("", flush=True)
            print("[LLM] 调用阿里云 API (尝试 " + str(attempt + 1) + "/3, 流式)...", flush=True)
            print("[LLM] timeout: connect=10s, read=600s", flush=True)
            content, finish_reason, last_data = _stream_call_api(url, headers, payload)

            if finish_reason == "rate_limit":
                if attempt < 2:
                    print("[LLM] 速率限制触发重试...", flush=True)
                    time.sleep(5)
                    continue
                else:
                    print("[LLM] 错误: 持续速率限制，3 次重试后仍失败", file=sys.stderr)
                    return None

            if not content:
                print("[LLM] 警告: API 返回空内容 (finish_reason=" + finish_reason + ")", file=sys.stderr)
                if attempt < 2:
                    print("[LLM] 等待 5 秒后重试...", flush=True)
                    time.sleep(5)
                    continue
                return None

            print("", flush=True)
            print("[LLM] 流式接收完成", flush=True)

            # 使用实际收到的 data 结构打印诊断
            log_llm_call_end(last_data, finish_reason, len(content))

            if finish_reason == "length":
                print("[LLM] WARNING 输出被 max_tokens 上限截断，请增大 max_tokens 配置", file=sys.stderr)

            print("[LLM] 编译成功，生成 " + str(len(content)) + " 字符", flush=True)
            return content

        except requests.exceptions.Timeout as e:
            print("[LLM] 请求超时 (" + str(e) + ")，尝试 " + str(attempt + 1) + "/3", file=sys.stderr)
            if attempt < 2:
                time.sleep(5)
            continue
        except requests.exceptions.RequestException as e:
            print("[LLM] 请求异常: " + str(e), file=sys.stderr)
            if attempt < 2:
                time.sleep(5)
            continue

    print("[LLM] 错误: 3 次重试后仍失败", file=sys.stderr)
    return None


def save_compiled_report(report_text: str, raw_dir: str, query: str) -> str:
    import hashlib
    from datetime import date

    today = date.today().isoformat()
    slug = re.sub(r"[^\w\u4e00-\u9fff]+", "-", query).strip("-").lower()[:40]
    if not slug:
        slug = hashlib.md5(query.encode()).hexdigest()[:8]

    filename = today + "-" + slug + "-compiled.md"
    output_path = Path(raw_dir) / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        f.write(report_text)

    print("[LLM] 报告已保存: " + str(output_path), flush=True)
    return str(output_path)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--query", required=True)
    parser.add_argument("--requirements", help="AI 整理额外要求")
    args = parser.parse_args()

    from config_loader import load_config
    config = load_config()

    result = compile_evidence(args.evidence, config, args.query, args.requirements)
    if result:
        print(result)
    else:
        print("编译失败", file=sys.stderr)
        sys.exit(1)
