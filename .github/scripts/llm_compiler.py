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
    "qwen3.5-plus": (128_000, 32_000),
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
    "# 任务说明\n\n"
    "以下是本次任务的完整执行计划。你必须按顺序执行每一个步骤，不得跳过。\n\n"
    "## 第一步：禁止清单（开始前必须明确知道）\n\n"
    "以下任何一条如果被违反，将严重损害整理质量。你必须把这些禁令作为最高优先级约束。\n\n"
    "- 禁止跳过证据包中任何一个主要章节（如第 3 节、第 4 节、第五章等以数字编号的章节）\n"
    "- 禁止删除任何一个来源中的'对架构师的启示'、'行动建议'、'落地步骤'类内容\n"
    "- 禁止把证据包中的表格转为文字描述（表格必须保持表格格式）\n"
    "- 禁止把多个段落合并为一句话\n"
    "- 禁止删除具体案例数据：客户名称、项目金额、效果指标、时间线、百分比、版本号等\n"
    "- 禁止约化数值（如 80.25% 不能写成约 80%）\n"
    "- 禁止删除技术细节：架构、算法、流程、配置、代码、接口、数据流等\n"
    "- 禁止删除历史演进：产品版本迭代、技术路线、架构演化等\n"
    "- 禁止用'包括但不限于'、'等'省略列表中的项\n"
    "- 禁止把前员工回忆录、第一手资料、学术论文内容压缩为 1-2 句话\n"
    "- 禁止删除竞争对手对比分析、估值模型、财务数据等\n\n"
    "## 第二步：目录索引（先阅读证据包的结构）\n\n"
    "在开始整理之前，先通读证据包，列出每个来源的章节结构。\n\n"
    "输出格式：\n\n"
    "【来源 1】：来源名称（如技术博客 / 研报 / 论文）\n"
    "包含的主要章节：第 1 章，第 2 章，...\n"
    "每个章节的大致内容类型（技术架构 / 案例分析 / 数据表格 / 财务数据 / 对架构师的启示 / ...）\n\n"
    "【来源 2】：同上\n"
    "...\n\n"
    "（注：这个目录索引将作为你后续整理的参考，确保你在写最终报告时不会遗漏任何一个章节。）\n\n"
    "## 第三步：逐来源逐章节整理\n\n"
    "按第二步生成的目录顺序，逐一处理每个来源。\n\n"
    "对每个来源，按原始章节顺序，逐章提取和整理内容：\n\n"
    "- （一）用 ### 标题标记来源编号和名称（例如：### 来源 1：XXX 技术博客）\n"
    "- （二）按原始章节顺序，逐章提取和整理内容\n"
    "- （三）保留所有表格（不得转为文字）\n"
    "- （四）保留所有具体数字、百分比、金额、版本号\n"
    "- （五）保留所有案例、具体客户名称、效果指标、时间线\n"
    "- （六）保留'对架构师的启示'、'行动建议'、'落地步骤'等指导性内容\n"
    "- （七）保留技术架构细节、实现机制、接口定义、数据流\n"
    "- （八）保留产品 / 技术的历史演进、版本迭代、架构演化\n\n"
    "## 第四步：跨来源去重与矛盾检测\n\n"
    "完成第三步后，对不同来源中重复的内容进行合并。\n\n"
    "处理原则：\n\n"
    "- 同一事实被多个来源重复提到时，保留信息最完整的那一处，其他来源中简要标注为'同来源'\n"
    "- 不同来源中的矛盾内容，在矛盾检测章节中明确列出\n"
    "- 保留每个来源中的独特信息（只在某来源中出现的内容）\n\n"
    "## 第五步：最终组装与自检\n\n"
    "按以下结构组装为最终报告。在输出最终报告之前，先完成以下自检，用中文回答每个问题。\n\n"
    "### 最终报告结构：\n\n"
    "## 核心结论\n\n"
    "- 从证据包中提取 3-7 条可复用结论\n"
    "- 每条结论必须带来源和可信度标注\n"
    "- 禁止只写结论不写支撑证据\n\n"
    "## 内容整理\n\n"
    "- 按第二步的目录索引，逐来源逐章节详细展开\n"
    "- 证据包中的每个章节、子章节，必须在内容整理中有对应\n"
    "- 保留所有表格、列表、代码、配置、数据等\n\n"
    "## 推荐工作流\n\n"
    "- 说明如何组合使用这些工具\n"
    "- 提供具体的执行步骤和配置方法\n"
    "- 必须包含从证据包中提取的具体操作建议\n\n"
    "## 适用场景\n\n"
    "- 列出适合采用该方法的项目类型\n"
    "- 每个场景必须有具体说明\n"
    "- 必须引用证据包中的实际案例\n\n"
    "## 不适用场景\n\n"
    "- 说明何时会过度工程或不值得引入\n"
    "- 每个场景必须有具体说明\n"
    "- 必须引用证据包中的限制条件\n\n"
    "## 风险与约束\n\n"
    "- 列出衔接点、上下文、测试、规格漂移等风险\n"
    "- 每个风险必须有详细描述和应对措施\n"
    "- 必须引用证据包中的具体风险案例\n\n"
    "## 信源质量门控记录\n\n"
    "- 列出门控规则、保留信源、剔除信源\n"
    "- 记录来源等级（A/B/C/D）和保留/剔除原因\n"
    "- 入库映射：A/B 对应 source-quality: high；C 对应 source-quality: medium；D 对应 source-quality: low\n\n"
    "## 来源与可信度\n\n"
    "- 逐项列出关键来源、来源类型、可信度\n"
    "- 每个来源必须说明支撑的具体内容\n\n"
    "## 对于可信度较高的来源逐来源整理\n\n"
    "- 逐篇整理高可信来源的核心内容\n"
    "- 每个来源必须详细展开，不能只提取结论\n"
    "- 必须包含：核心内容、可用事实、局限、适合入库的知识点\n"
    "- 来源中的每个要点都必须在整理中有对应\n"
    "- 特别要求：必须保留'对架构师的启示'、'行动建议'、'落地步骤'等指导性内容\n\n"
    "## 跨源矛盾检测结论\n\n"
    "- 检测核心数字、日期、功能描述等矛盾\n"
    "- 逐项列出矛盾项，说明来源和初步判断\n"
    "- 未发现矛盾也必须明确写出\n\n"
    "## 矛盾与待验证问题\n\n"
    "- 保留冲突或证据不足处\n"
    "- 每个问题必须有具体描述和建议\n\n"
    "## 原始证据摘录\n\n"
    "- 保留支持结论的必要摘录或完整证据片段\n"
    "- 摘录必须包含来源标注\n\n"
    "### 自检问题（在输出最终报告之前先回答以下问题，用中文）\n\n"
    "1. 我是否覆盖了证据包中的每个主要章节？（是/否）\n"
    "2. 我是否保留了所有'对架构师的启示'、'行动建议'、'落地步骤'？（是/否）\n"
    "3. 我是否保留了所有表格而没有转为文字？（是/否）\n"
    "4. 我是否保留了所有具体案例数据（客户名称、金额、百分比、时间线）？（是/否）\n"
    "5. 我是否保留了所有技术架构细节和实现机制？（是/否）\n"
    "6. 我是否保留了所有历史演进？（是/否）\n"
    "7. 我是否保留了前员工回忆录、第一手资料、学术论文内容，没有压缩为 1-2 句话？（是/否）\n"
    "8. 我是否在内容整理中保留了每个来源中的每个主要章节？（是/否）\n"
    "9. 我是否保留了竞争对手对比分析、估值模型、财务数据？（是/否）\n"
    "10. 我是否没有用'包括但不限于'、'等'的表述替代具体列表？（是/否）\n\n"
    "## 最终报告（在完成自检之后，开始输出最终报告内容）\n\n"
    "请按上述报告结构输出完整的中文报告。\n\n"
    "输出要求：\n"
    "- 用中文输出\n"
    "- 每条关键事实后标注 [来源: URL]\n"
    "- 每条核心结论标注可信度：高 / 中 / 低\n"
    "- 不得把无 URL 支撑的内容写成事实\n\n"
    "------------------------------------------------------------\n\n"
    "以下是本次调研主题：\n\n"
    "[QUERY_PLACEHOLDER]\n\n"
    "------------------------------------------------------------\n\n"
    "以下是完整的证据包内容：\n\n"
    "------------------------------------------------------------\n\n"
    "[QUERY_PLACEHOLDER2]\n\n"
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
    usage = data.get("usage", {})
    prompt_tokens = usage.get("prompt_tokens", 0)
    completion_tokens = usage.get("completion_tokens", 0)
    total_tokens = usage.get("total_tokens", 0)

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
    model = llm_config.get("model", "qwen3.7-max")
    max_output_tokens = llm_config.get("max_tokens", 64000)
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

    prompt = USER_PROMPT_TEMPLATE.replace("[QUERY_PLACEHOLDER]", query).replace("[QUERY_PLACEHOLDER2]", evidence_content)

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
    args = parser.parse_args()

    from config_loader import load_config
    config = load_config()

    result = compile_evidence(args.evidence, config, args.query)
    if result:
        print(result)
    else:
        print("编译失败", file=sys.stderr)
        sys.exit(1)
