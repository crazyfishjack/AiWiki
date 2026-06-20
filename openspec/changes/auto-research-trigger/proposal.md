## Why

当前 wiki-research 技能需要用户在本地环境手动运行四工具调研脚本，无法通过 Trae 移动端（云端模式）随时随地触发调研任务。本项目需要建立一个自动化工作流：用户通过 GitHub Issues 提交自然语言调研需求后，GitHub Actions 自动执行四工具检索、阿里云 Qwen LLM 编译中文调研报告、将结果写入 `raw/` 目录并推送回仓库，同时通过企业微信 webhook 推送完成通知。

## What Changes

- **新增 GitHub Actions workflow**：监听 `issues: [opened]` 事件，自动触发调研流程
- **新增调研执行脚本**：封装四工具调研 + 阿里云 Qwen 编译 + 企业微信通知的完整流程
- **新增配置文件体系**：独立配置四工具 API Key、阿里云 LLM Key、企业微信 Webhook URL 等敏感信息
- **新增需求覆盖索引**：`requirement-coverage.md`，映射原始需求 → spec → task → 验收标准
- **新增并行计划**：`parallel-plan.md`，按 Batch 分组任务，支持多 agent 并行执行

## Capabilities

### New Capabilities
- `github-actions-trigger`：GitHub Actions workflow 配置，监听 issue 事件并触发调研
- `research-executor`：调研执行脚本，封装四工具调用 + LLM 编译 + 结果处理
- `aliyun-llm-compiler`：阿里云 Qwen LLM 集成，将证据包编译为中文调研报告
- `wechat-notifier`：企业微信 webhook 推送通知
- `config-management`：敏感配置独立管理（API Keys、Webhook URL 等）

### Modified Capabilities
- 无

## Impact

- **新增文件**：
  - `.github/workflows/auto-research.yml`
  - `.github/scripts/run-research.py`
  - `.github/scripts/config.local.json`（敏感配置模板）
  - `openspec/changes/auto-research-trigger/proposal.md`
  - `openspec/changes/auto-research-trigger/design.md`
  - `openspec/changes/auto-research-trigger/specs/*/spec.md`
  - `openspec/changes/auto-research-trigger/tasks.md`
  - `openspec/changes/auto-research-trigger/requirement-coverage.md`
  - `openspec/changes/auto-research-trigger/parallel-plan.md`
- **依赖**：GitHub Actions、Python 3.x、requests、阿里云 Qwen API、企业微信 webhook
- **敏感信息**：所有 API Key 通过 GitHub Secrets 管理，不硬编码
