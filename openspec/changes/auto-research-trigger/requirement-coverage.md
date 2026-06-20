# 需求覆盖索引

## 原始需求点 → OpenSpec Spec → Task → Batch → Agent → 验收标准

| # | 原始需求点 | Spec 条目 | Task 编号 | Batch | 负责 Agent 建议 | 验收标准 |
|---|-----------|----------|----------|-------|---------------|---------|
| 1 | Trae 移动端输入自然语言触发 | `github-actions-trigger` / Requirement: Workflow listens for new issues | 2.1, 2.2, 2.3, 2.4 | Batch 0 | Agent A | 创建 `[调研] xxx` issue 后 Actions 在 60 秒内触发 |
| 2 | GitHub Actions 自动执行 | `github-actions-trigger` / Requirement: Workflow listens for new issues | 3.1, 3.2, 3.3, 3.4, 3.5 | Batch 0 | Agent A | `.github/workflows/auto-research.yml` 存在且语法正确 |
| 3 | 按照 wiki-research skill 启动检索/调研 | `research-executor` / Requirement: Research runner invokes four-tool research | 4.1, 4.2, 4.3, 4.4 | Batch 1 | Agent B | `run-research.py` 成功调用 `four_tool_research.py` 并生成证据包 |
| 4 | 文档写到 raw 文件夹 | `research-executor` / Requirement: Git pusher commits and pushes results | 6.1, 6.2, 6.3, 6.4, 6.5 | Batch 2 | Agent C | 生成的报告文件出现在 `raw/articles/` 目录并推送到仓库 |
| 5 | 使用阿里云 LLM（qwen3.5-plus） | `aliyun-llm-compiler` / Requirement: LLM compiler compiles evidence into Chinese report | 5.1, 5.2, 5.3, 5.4, 5.5, 5.6 | Batch 1 | Agent B | 证据包成功编译为包含所有必需章节的中文报告 |
| 6 | 推消息到企业微信 | `wechat-notifier` / Requirement: WeChat notifier sends completion notification | 7.1, 7.2, 7.3, 7.4, 7.5 | Batch 2 | Agent C | 调研完成后收到企业微信消息，包含主题、路径、结论 |
| 7 | 四工具 API Key 独立配置文件 | `config-management` / Requirement: Config management isolates sensitive data | 1.1, 1.2, 1.3, 1.4 | Batch 0 | Agent A | 配置从环境变量或本地 JSON 加载，敏感信息不硬编码 |
| 8 | 配置支持 GitHub Secrets | `config-management` / Requirement: Config management isolates sensitive data | 1.2, 10.1 | Batch 0 | Agent A | Actions 中环境变量正确注入，脚本可读取 |
| 9 | 非调研 issue 过滤 | `github-actions-trigger` / Requirement: Workflow listens for new issues | 2.4, 3.1 | Batch 0 | Agent A | 创建普通 issue 时 workflow 跳过执行 |
| 10 | LLM 编译失败回退 | `aliyun-llm-compiler` / Requirement: LLM compilation failure fallback | 5.5 | Batch 1 | Agent B | 断开阿里云 API 后脚本保存原始证据包并继续 |
| 11 | Git push 冲突处理 | `research-executor` / Requirement: Git pusher commits and pushes results | 6.5 | Batch 2 | Agent C | 模拟远程变更后脚本成功 rebase 并推送 |
| 12 | 通知失败不影响管道 | `wechat-notifier` / Requirement: Notification respects webhook URL configuration | 7.4, 7.5 | Batch 2 | Agent C | 断开 webhook 后脚本完成调研和推送，仅跳过通知 |
| 13 | 本地测试支持（--query 参数） | `research-executor` / Requirement: Issue parser extracts research intent | 2.3, 10.2 | Batch 3 | Agent D | 本地运行 `python run-research.py --query "xxx"` 成功 |
| 14 | 完整错误处理与日志 | `research-executor` / Requirement: Pipeline handles partial failures gracefully | 8.1, 8.2, 8.3, 8.4, 8.5 | Batch 1-2 | Agent B/C | Actions 日志显示每个步骤的开始/结束/结果 |
| 15 | 依赖管理 | 9.1, 9.2 | Batch 0 | Agent A | `requirements.txt` 存在且 `pip install` 成功 |
| 16 | 文档交付 | 11.1, 11.2, 11.3 | Batch 3 | Agent D | README.md 存在，端到端流程验证通过 |

## Spec 覆盖统计

| Capability | Spec 数量 | Scenario 数量 | Task 数量 |
|-----------|----------|--------------|----------|
| github-actions-trigger | 4 Requirements | 7 Scenarios | 5 Tasks (2.1-2.4, 3.1-3.5) |
| research-executor | 4 Requirements | 8 Scenarios | 9 Tasks (4.1-4.4, 6.1-6.5, 8.1-8.5) |
| aliyun-llm-compiler | 3 Requirements | 6 Scenarios | 6 Tasks (5.1-5.6) |
| wechat-notifier | 2 Requirements | 5 Scenarios | 5 Tasks (7.1-7.5) |
| config-management | 3 Requirements | 6 Scenarios | 4 Tasks (1.1-1.4) |
| **总计** | **16 Requirements** | **32 Scenarios** | **29 Tasks** |

## 低置信度 / 待确认条目

| # | 条目 | 原因 | 建议 |
|---|------|------|------|
| 1 | 阿里云百炼 API 具体 endpoint | 用户未提供 | 需要用户提供阿里云百炼的 base URL 和 chat completion endpoint |
| 2 | 企业微信 webhook URL 格式 | 用户未提供 | 需要用户提供 webhook URL，确认是群机器人还是应用消息 |
| 3 | issue label 过滤需求 | design.md 中标记为 Open Question | 是否需要只处理带 `research` label 的 issue？ |
| 4 | 代理配置在 Actions 中的处理 | Actions 环境通常不需要代理 | 是否需要为 Actions 环境禁用代理？ |
| 5 | 报告文件命名规则 | 现有脚本使用日期+slug | 是否需要添加 `[auto-research]` 前缀以区分手动调研？ |
