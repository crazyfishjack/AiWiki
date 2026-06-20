## Context

当前项目是一个 AI Wiki 系统，使用四工具（Tavily、Exa、Firecrawl、Jina）进行外部调研，调研结果保存为 raw Markdown 文件，经用户确认后按 SCHEMA.md 入库。现有调研流程依赖用户在本地环境手动运行 `four_tool_research.py` 脚本，无法通过移动端随时触发。

用户的核心诉求：在 Trae 移动端（云端模式）通过自然语言描述调研需求，自动触发完整调研流程，最终收到企业微信通知。

## Goals / Non-Goals

**Goals:**
- 建立 GitHub Issues → GitHub Actions → 自动调研 → 企业微信通知的完整工作流
- 复用现有 `four_tool_research.py` 脚本，不破坏其独立运行能力
- 新增阿里云 Qwen LLM 编译步骤，将证据包转换为中文调研报告
- 敏感配置独立管理，支持 GitHub Secrets 和本地配置文件两种模式
- 调研结果自动写入 `raw/articles/` 并推送回仓库
- 企业微信 webhook 推送完成通知（包含报告链接和摘要）

**Non-Goals:**
- 不修改现有 wiki-research skill 的核心逻辑（SCHEMA.md、SKILL.md、WORKFLOW.md）
- 不替代 Trae Agent 的人工审查和入库确认环节
- 不实现实时双向通信（仅单向通知）
- 不支持非 GitHub 仓库的触发方式
- 不实现调研结果的自动入库（仍需用户确认）

## Decisions

### Decision 1：触发方式选择 GitHub Issues 而非 webhook 或 schedule
- **选项 A**：GitHub Issues（推荐）—— 用户在 Trae 移动端创建 issue，Actions 监听 `issues: [opened]`
- **选项 B**：Repository Dispatch webhook —— 需要中间服务转发 Trae 请求
- **选项 C**：Schedule 定时轮询 —— 延迟高，不够实时
- **选择**：选项 A。理由：Trae 移动端可直接创建 issue，无需额外中间服务；issue 天然留存需求记录；支持标题和正文传递调研主题。

### Decision 2：敏感配置管理采用 GitHub Secrets + 本地配置文件双模式
- **选项 A**：仅 GitHub Secrets —— 安全但本地调试困难
- **选项 B**：仅本地配置文件 —— 方便调试但容易泄露
- **选项 C**：GitHub Secrets 优先，本地配置文件兜底（推荐）
- **选择**：选项 C。理由：Actions 运行环境读取 GitHub Secrets；本地开发时读取 `.github/scripts/config.local.json`（已加入 `.gitignore`）。

### Decision 3：阿里云 Qwen 集成方式
- **选项 A**：直接调用阿里云百炼 API（推荐）
- **选项 B**：通过 OpenRouter 等聚合平台
- **选择**：选项 A。理由：用户已有阿里云 Key 和明确使用 qwen3.5-plus 的意愿；直接调用减少中间依赖。

### Decision 4：企业微信推送时机和内容
- **推送时机**：调研完成且 git push 成功后
- **推送内容**：调研主题、报告文件路径、核心结论摘要（3-5 条）、执行状态（成功/失败）
- **失败处理**：推送失败通知，包含错误摘要

### Decision 5：脚本架构设计
- 主脚本 `run-research.py` 作为 GitHub Actions 的入口
- 内部模块化：
  - `config_loader`：配置加载（Secrets/本地文件）
  - `issue_parser`：解析 issue 标题和正文
  - `research_runner`：调用 four_tool_research.py
  - `llm_compiler`：调用阿里云 Qwen 编译报告
  - `git_pusher`：git commit + push
  - `wechat_notifier`：企业微信推送

## Risks / Trade-offs

| 风险 | 缓解措施 |
|------|---------|
| GitHub Actions 运行时间限制（6小时） | 四工具调研通常 < 10 分钟，LLM 编译 < 2 分钟，总体可控 |
| API Key 泄露 | 仅通过 GitHub Secrets 注入，本地配置文件加入 `.gitignore` |
| 企业微信 webhook 频率限制 | 单次调研只推送一次，不会触发限制 |
| Issue 被恶意创建导致滥用 | 未来可添加 label 过滤或白名单机制（当前版本不实现） |
| LLM 编译质量不稳定 | 保留原始证据包，编译失败时回退到证据包直接保存 |
| Git push 冲突 | 使用 `git pull --rebase` 策略，冲突时推送失败通知 |

## Migration Plan

1. **Phase 0**：创建 OpenSpec change 产物（当前阶段）
2. **Phase 1**：实现核心脚本和 workflow（Task 1-8）
3. **Phase 2**：配置 GitHub Secrets 和测试（Task 9-10）
4. **Phase 3**：验证端到端流程（Task 11）

## Open Questions

1. 阿里云 Qwen API 的具体 endpoint 和参数格式（需要用户提供）
2. 企业微信 webhook URL 的具体格式（需要用户提供）
3. 是否需要支持 issue label 过滤（如只处理带 `research` label 的 issue）
