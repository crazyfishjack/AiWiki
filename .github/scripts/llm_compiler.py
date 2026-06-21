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
    max_tokens = llm_config.get("max_tokens", 64000)
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

请按以下结构生成报告，每个章节必须遵守对应规则：

## 核心结论
- 从证据包中提取 3-7 条可复用结论
- 每条结论必须带来源和可信度标注
- 禁止只写结论不写支撑证据

## 内容整理
**这是最重要的章节，必须详细展开，禁止压缩。**

### 生成规则：
1. **结构镜像**：证据包中的每个章节、子章节，必须在内容整理中有对应。禁止跳过任何章节。
2. **信息密度守恒**：
   - 证据包中的每个段落，总结中至少保留 80% 的信息量
   - 禁止把多个段落合并为一句话
   - 禁止删除技术细节、数据指标、实现方式
   - 禁止用"包括但不限于"等模糊表述替代具体列表
3. **必须保留的内容类型**：
   - **技术架构细节**：分层设计、组件说明、接口定义、数据流
   - **实现机制**：具体算法、流程步骤、配置参数、代码逻辑
   - **对比分析**：不同方案/产品/版本的详细对比表格
   - **案例数据**：具体的客户名称、项目金额、效果指标、时间线
   - **启示建议**："对架构师的启示"、"行动建议"、"落地步骤"等指导性内容
   - **历史演进**：产品/技术的发展历程、版本迭代、架构演化
4. **格式保持**：
   - 证据包中的表格 → 总结中必须保留表格（不得转为文字）
   - 证据包中的列表 → 总结中必须保留列表（不得合并为段落）
   - 证据包中的代码/配置 → 总结中必须保留代码块
   - 证据包中的数据 → 总结中必须保留具体数值
   - **重复合并**：多个来源中重复的描述和数据，必须合并为一条，避免冗余
5. **概念完整性**：每个技术概念必须包含：
   - **定义**：详细说明（不少于 2 句话）
   - **示例**：具体实例（至少 3 个）
   - **实现**：技术细节、架构、流程（不少于 3 句话）
   - **关系**：与其他组件的交互方式（不少于 2 句话）
6. **数据完整性**：每个数据指标必须包含：
   - **具体数值**：不得省略或约化（如 80.25% 不能写成"约 80%"）
   - **上下文**：该数据的来源、时间、条件
   - **对比**：如果有多个来源的数据，必须全部列出

### 禁止行为（绝对不允许）：
- ❌ 把"对架构师的启示"类内容删除
- ❌ 把详细的技术实现压缩为一句话
- ❌ 把表格转为文字描述
- ❌ 删除具体的案例数据（如客户名称、金额、百分比）
- ❌ 用"等"、"包括但不限于"省略列表项
- ❌ 跳过证据包中的任何章节

## 推荐工作流
- 说明如何组合使用这些工具
- 提供具体的执行步骤和配置方法
- 必须包含从证据包中提取的具体操作建议

## 适用场景
- 列出适合采用该方法的项目类型
- 每个场景必须有具体说明
- 必须引用证据包中的实际案例

## 不适用场景
- 说明何时会过度工程或不值得引入
- 每个场景必须有具体说明
- 必须引用证据包中的限制条件

## 风险与约束
- 列出衔接点、上下文、测试、规格漂移等风险
- 每个风险必须有详细描述和应对措施
- 必须引用证据包中的具体风险案例

## 信源质量门控记录
- 列出门控规则、保留信源、剔除信源
- 记录来源等级（A/B/C/D）和保留/剔除原因
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`

## 来源与可信度
- 逐项列出关键来源、来源类型、可信度
- 每个来源必须说明支撑的具体内容

## 对于可信度较高的来源逐来源总结
- 逐篇整理高可信来源的核心内容
- 每个来源必须详细展开，不能只提取结论
- 必须包含：核心内容、可用事实、局限、适合入库的知识点
- 来源中的每个要点都必须在总结中有对应
- **特别要求**：必须保留"对架构师的启示"、"行动建议"、"落地步骤"等指导性内容

## 跨源矛盾检测结论
- 检测核心数字、日期、功能描述等矛盾
- 逐项列出矛盾项，说明来源和初步判断
- 未发现矛盾也必须明确写出

## 矛盾与待验证问题
- 保留冲突或证据不足处
- 每个问题必须有具体描述和建议

## 原始证据摘录
- 保留支持结论的必要摘录或完整证据片段
- 摘录必须包含来源标注

## 最终自检清单（生成完成后必须执行）

检查以下项目，如果有任何一项未通过，必须补充展开：

- [ ] **章节覆盖**：证据包中的每个章节是否在总结中有对应？
- [ ] **启示保留**：所有"对架构师的启示"、"行动建议"、"落地步骤"是否保留？
- [ ] **技术细节**：每个技术概念是否有定义+示例+实现+关系？
- [ ] **数据完整**：所有数据是否保留具体数值（未约化）？
- [ ] **表格保留**：所有表格是否保留原格式（未转为文字）？
- [ ] **案例保留**：所有具体案例（客户名称、金额、效果）是否保留？
- [ ] **历史演进**：产品/技术的发展历程是否保留？
- [ ] **禁止行为**：是否有"包括但不限于"、"等"等模糊表述？
- [ ] **一句话检查**：是否有任何章节被压缩为一句话？

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
