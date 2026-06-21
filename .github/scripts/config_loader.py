#!/usr/bin/env python3
"""
配置加载模块。

支持从 GitHub Secrets（环境变量）和本地 JSON 文件加载配置，GitHub Secrets 优先。
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Any


def load_config(config_path: str | None = None) -> dict[str, Any]:
    """加载配置，GitHub Secrets 优先，本地 JSON 兜底。"""
    # 默认配置
    config: dict[str, Any] = {
        "raw_default_dir": "raw/articles",
        "llm_config": {
            "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
            "model": "qwen3.7-max",
            "max_tokens": 65000,
            "temperature": 0.7
        }
    }

    # 1. 从本地配置文件加载（如果存在）
    local_config = _load_local_config(config_path)
    if local_config:
        _deep_update(config, local_config)

    # 2. 从 GitHub Secrets（环境变量）覆盖敏感字段
    env_overrides = _load_from_env()
    if env_overrides:
        _deep_update(config, env_overrides)

    return config


def _load_local_config(config_path: str | None) -> dict[str, Any] | None:
    """尝试从本地 JSON 文件加载配置。"""
    if config_path:
        path = Path(config_path).expanduser().resolve()
        if path.exists():
            with path.open("r", encoding="utf-8") as f:
                return json.load(f)
        return None

    # 尝试默认路径
    script_dir = Path(__file__).resolve().parent
    local_path = script_dir / "config.local.json"
    if local_path.exists():
        with local_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    return None


def _load_from_env() -> dict[str, Any] | None:
    """从环境变量加载 GitHub Secrets 配置。"""
    env_config: dict[str, Any] = {"api_keys": {}, "webhooks": {}}
    has_env = False

    # API Keys
    for key_name, env_name in [
        ("tavily", "TAVILY_API_KEY"),
        ("exa", "EXA_API_KEY"),
        ("firecrawl", "FIRECRAWL_API_KEY"),
        ("jina", "JINA_API_KEY"),
        ("aliyun", "ALIYUN_API_KEY"),
    ]:
        value = os.environ.get(env_name)
        if value:
            env_config["api_keys"][key_name] = value
            has_env = True

    # Webhooks
    wechat_url = os.environ.get("WECHAT_WEBHOOK_URL")
    if wechat_url:
        env_config["webhooks"]["wechat"] = wechat_url
        has_env = True

    # Proxy (可选)
    proxy = os.environ.get("HTTP_PROXY") or os.environ.get("HTTPS_PROXY")
    if proxy:
        env_config["proxy"] = proxy
        has_env = True

    return env_config if has_env else None


def _deep_update(base: dict[str, Any], override: dict[str, Any]) -> None:
    """递归更新字典，override 优先。"""
    for key, value in override.items():
        if isinstance(value, dict) and key in base and isinstance(base[key], dict):
            _deep_update(base[key], value)
        else:
            base[key] = value


def validate_config(config: dict[str, Any]) -> list[str]:
    """校验配置完整性，返回问题列表。"""
    issues: list[str] = []

    # 检查必需字段
    required_api_keys = ["tavily", "exa", "firecrawl", "jina", "aliyun"]
    api_keys = config.get("api_keys", {})
    for key_name in required_api_keys:
        if not api_keys.get(key_name):
            issues.append(f"缺少 api_keys.{key_name}")

    # 检查代理 URL 格式（如果配置了）
    proxy = config.get("proxy")
    if proxy:
        if not re.match(r"^https?://", str(proxy)):
            issues.append(f"proxy URL 格式无效: {proxy}")

    # 检查 LLM 配置
    llm_config = config.get("llm_config", {})
    if not llm_config.get("base_url"):
        issues.append("缺少 llm_config.base_url")
    if not llm_config.get("model"):
        issues.append("缺少 llm_config.model")

    return issues


def require_valid_config(config: dict[str, Any]) -> None:
    """校验配置，有问题时直接退出。"""
    issues = validate_config(config)
    if issues:
        print("配置校验失败:", file=sys.stderr)
        for issue in issues:
            print(f"  - {issue}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # 简单测试
    config = load_config()
    issues = validate_config(config)
    if issues:
        print("配置问题:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("配置有效")
