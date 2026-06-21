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


# 已知模型的上下文窗口（input）和输出窗口（output）限制
# 数据来源：阿里云百炼官方文档（2025-2026）
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
    "你是一名资深行业研究分析师，擅长从多源证据中提取、整合并重构高质量调研报告。"
    "你的核心能力包括：识别关键事实与数据、保留来源的论证逻辑与叙事结构、进行跨源交叉验证与矛盾检测、"
    "输出结构清晰且信息密度高的专业报告。工作原则：忠于原始证据，不遗漏分析性内容，"
    "不将段落压缩为参数列表，不编造无依据信息。"
)

USER_PROMPT_TEMPLATE = (
    "请基于以下证据包，生成一份结构化的中文调研报告。\n\n"
    "调研主题：[QUERY_PLACEHOLDER]\n\n"
    "证据包内容：\n[QUERY_PLACEHOLDER2]\n\n"
    "请按以下结构生成报告，每个章节必须遵守对应规则：\n\n"
    "## 核心结论\n"
    "- 从证据包中提取 3-7 条可复用结论\n"
    "- 每条结论必须带来源和可信度标注\n"
    "- 禁止只写结论不写支撑证据\n\n"
    "## 内容整理\n"
    "**这是最重要的章节，必须详细展开，禁止压缩。**\n\n"
    "### 生成规则：\n"
    "1. **结构镜像**：证据包中的每个章节、子章节，必须在内容整理中有对应。禁止跳过任何章节。\n"
    "2. **信息密度守恒**：\n"
    "   - 证据包中的每个段落，总结中至少保留 80% 的信息量\n"
    "   - 禁止把多个段落合并为一句话\n"
    "   - 禁止删除技术细节、数据指标、实现方式\n"
    "   - 禁止用'包括但不限于'等模糊表述替代具体列表\n"
    "3. **必须保留的内容类型**：\n"
    "   - **技术架构细节**：分层设计、组件说明、接口定义、数据流\n"
    "   - **实现机制**：具体算法、流程步骤、配置参数、代码逻辑\n"
    "   - **对比分析**：不同方案/产品/版本的详细对比表格\n"
    "   - **案例数据**：具体的客户名称、项目金额、效果指标、时间线\n"
    "   - **启示建议**：'对架构师的启示'、'行动建议'、'落地步骤'等指导性内容\n"
    "   - **历史演进**：产品/技术的发展历程、版本迭代、架构演化\n"
    "4. **格式保持**：\n"
    "   - 证据包中的表格 → 总结中必须保留表格（不得转为文字）\n"
    "   - 证据包中的列表 → 总结中必须保留列表（不得合并为段落）\n"
    "   - 证据包中的代码/配置 → 总结中必须保留代码块\n"
    "   - 证据包中的数据 → 总结中必须保留具体数值\n"
    "   - **重复合并**：多个来源中重复的描述和数据，必须合并为一条，避免冗余\n"
    "5. **概念完整性**：每个技术概念必须包含：\n"
    "   - **定义**：详细说明（不少于 2 句话）\n"
    "   - **示例**：具体实例（至少 3 个）\n"
    "   - **实现**：技术细节、架构、流程（不少于 3 句话）\n"
    "   - **关系**：与其他组件的交互方式（不少于 2 句话）\n"
    "6. **数据完整性**：每个数据指标必须包含：\n"
    "   - **具体数值**：不得省略或约化（如 80.25% 不能写成'约 80%'）\n"
    "   - **上下文**：该数据的来源、时间、条件\n"
    "   - **对比**：如果有多个来源的数据，必须全部列出\n\n"
    "### 禁止行为（绝对不允许）：\n"
    "- 把'对架构师的启示'类内容删除\n"
    "- 把详细的技术实现压缩为一句话\n"
    "- 把表格转为文字描述\n"
    "- 删除具体的案例数据（如客户名称、金额、百分比）\n"
    "- 用'等'、'包括但不限于'省略列表项\n"
    "- 跳过证据包中的任何章节\n\n"
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
    "## 信源质量门控记录\n"
    "- 列出门控规则、保留信源、剔除信源\n"
    "- 记录来源等级（A/B/C/D）和保留/剔除原因\n"
    "- 入库映射：A/B → source-quality: high；C → source-quality: medium；D → source-quality: low\n\n"
    "## 来源与可信度\n"
    "- 逐项列出关键来源、来源类型、可信度\n"
    "- 每个来源必须说明支撑的具体内容\n\n"
    "## 对于可信度较高的来源逐来源总结\n"
    "- 逐篇整理高可信来源的核心内容\n"
    "- 每个来源必须详细展开，不能只提取结论\n"
    "- 必须包含：核心内容、可用事实、局限、适合入库的知识点\n"
    "- 来源中的每个要点都必须在总结中有对应\n"
    "- **特别要求**：必须保留'对架构师的启示'、'行动建议'、'落地步骤'等指导性内容\n\n"
    "## 跨源矛盾检测结论\n"
    "- 检测核心数字、日期、功能描述等矛盾\n"
    "- 逐项列出矛盾项，说明来源和初步判断\n"
    "- 未发现矛盾也必须明确写出\n\n"
    "## 矛盾与待验证问题\n"
    "- 保留冲突或证据不足处\n"
    "- 每个问题必须有具体描述和建议\n\n"
    "## 原始证据摘录\n"
    "- 保留支持结论的必要摘录或完整证据片段\n"
    "- 摘录必须包含来源标注\n\n"
    "## 最终自检清单（生成完成后必须执行）：\n\n"
    "检查以下项目，如果有任何一项未通过，必须补充展开：\n\n"
    "- [ ] **章节覆盖**：证据包中的每个章节是否在总结中有对应？\n"
    "- [ ] **启示保留**：所有'对架构师的启示'、'行动建议'、'落地步骤'是否保留？\n"
    "- [ ] **技术细节**：每个技术概念是否有定义+示例+实现+关系？\n"
    "- [ ] **数据完整**：所有数据是否保留具体数值（未约化）？\n"
    "- [ ] **表格保留**：所有表格是否保留原格式（未转为文字）？\n"
    "- [ ] **案例保留**：所有具体案例（客户名称、金额、效果）是否保留？\n"
    "- [ ] **历史演进**：产品/技术的发展历程是否保留？\n"
    "- [ ] **禁止行为**：是否有'包括但不限于'、'等'等模糊表述？\n"
    "- [ ] **一句话检查**：是否有任何章节被压缩为一句话？\n\n"
    "要求：\n"
    "- 用中文输出\n"
    "- 每条关键事实后标注 [来源: URL]\n"
    "- 每条核心结论标注可信度：高 / 中 / 低\n"
    "- 不得把无 URL 支撑的内容写成事实\n"
)


def estimate_tokens(text: str) -> int:
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    eng_words = len(re.findall(r"[a-zA-Z]{2,}", text))
    # digits, whitespace, punctuation, markdown symbols
    punct = len(re.findall(r"[\d\s\.,;:!?\'\"()\-+{}\[\]|\\/#]", text))
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


def compile_evidence(
    evidence_path: str,
    config: dict,
    query: str,
) -> str | None:
    if requests is None:
        print("[LLM] 错误: 缺少 requests 依赖", file=sys.stderr)
        return None

    # 读取证据包（提前读取，用于 token 估算）
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
    max_output_tokens = llm_config.get("max_tokens", 64000)
    temperature = llm_config.get("temperature", 0.3)

    api_key = config.get("api_keys", {}).get("aliyun")
    if not api_key:
        print("[LLM] 错误: 缺少阿里云 API Key", file=sys.stderr)
        return None

    max_input_window, _ = get_model_window(model)

    # 调用前诊断
    log_llm_call_start(
        model=model,
        evidence_tokens=evidence_tokens,
        evidence_chars=len(evidence_content),
        query_chars=len(query),
        max_output_tokens=max_output_tokens,
        max_input_window=max_input_window,
    )

    # 构造提示词：用简单的 replace 替代 format（避免 { 和 } 的转义问题）
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
        "temperature": temperature
    }

    for attempt in range(3):
        try:
            print("[LLM] 调用阿里云 API (尝试 " + str(attempt + 1) + "/3)...", flush=True)
            response = requests.post(url, headers=headers, json=payload, timeout=1800)

            if response.status_code == 429:
                print("[LLM] 遇到速率限制，等待 5 秒后重试...", flush=True)
                time.sleep(5)
                continue

            response.raise_for_status()
            resp_data = response.json()

            if "choices" in resp_data and len(resp_data["choices"]) > 0:
                choice = resp_data["choices"][0]
                content = choice.get("message", {}).get("content", "")
                finish_reason = choice.get("finish_reason", "unknown")

                log_llm_call_end(resp_data, finish_reason, len(content))

                if finish_reason == "length":
                    print("[LLM] WARNING 输出被 max_tokens 上限截断，请增大 max_tokens 配置", file=sys.stderr)

                if content:
                    print("[LLM] 编译成功，生成 " + str(len(content)) + " 字符", flush=True)
                    return content
                else:
                    print("[LLM] 警告: API 返回空内容", file=sys.stderr)
                    return None
            else:
                print("[LLM] 警告: 未找到 choices: " + str(resp_data), file=sys.stderr)
                return None

        except requests.exceptions.Timeout:
            print("[LLM] 请求超时，尝试 " + str(attempt + 1) + "/3", file=sys.stderr)
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
