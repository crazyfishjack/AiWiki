# 覆盖自检报告

## 原始需求覆盖检查

| # | 原始需求 | 状态 | 覆盖位置 |
|---|---------|------|---------|
| 1 | Trae 移动端输入自然语言触发 | ✅ 已覆盖 | `github-actions-trigger/spec.md` Requirement 1, Task 2.1-2.4 |
| 2 | GitHub Actions 自动执行 | ✅ 已覆盖 | `github-actions-trigger/spec.md` Requirement 1, Task 3.1-3.5 |
| 3 | 按照 wiki-research skill 启动检索/调研 | ✅ 已覆盖 | `research-executor/spec.md` Requirement 3, Task 4.1-4.4 |
| 4 | 文档写到 raw 文件夹 | ✅ 已覆盖 | `research-executor/spec.md` Requirement 5, Task 6.1-6.5 |
| 5 | 使用阿里云 LLM（qwen3.5-plus） | ✅ 已覆盖 | `aliyun-llm-compiler/spec.md` Requirement 1-3, Task 5.1-5.6 |
| 6 | 推消息到企业微信 | ✅ 已覆盖 | `wechat-notifier/spec.md` Requirement 1-2, Task 7.1-7.5 |
| 7 | 四工具 API Key 独立配置文件 | ✅ 已覆盖 | `config-management/spec.md` Requirement 1-3, Task 1.1-1.4 |
| 8 | 配置支持 GitHub Secrets | ✅ 已覆盖 | `config-management/spec.md` Requirement 1, Task 1.2, 10.1 |
| 9 | 非调研 issue 过滤 | ✅ 已覆盖 | `github-actions-trigger/spec.md` Requirement 1 Scenario 2, Task 2.4 |
| 10 | LLM 编译失败回退 | ✅ 已覆盖 | `aliyun-llm-compiler/spec.md` Requirement 1 Scenario 3, Task 5.5 |
| 11 | Git push 冲突处理 | ✅ 已覆盖 | `research-executor/spec.md` Requirement 5 Scenario 2, Task 6.5 |
| 12 | 通知失败不影响管道 | ✅ 已覆盖 | `wechat-notifier/spec.md` Requirement 1 Scenario 3, Task 7.4-7.5 |
| 13 | 本地测试支持（--query 参数） | ✅ 已覆盖 | `research-executor/spec.md` Requirement 4 Scenario 2, Task 2.3, 10.2 |
| 14 | 完整错误处理与日志 | ✅ 已覆盖 | `research-executor/spec.md` Requirement 2, Task 8.1-8.5 |
| 15 | 依赖管理 | ✅ 已覆盖 | Task 9.1-9.2 |
| 16 | 文档交付 | ✅ 已覆盖 | Task 11.1-11.3 |

## 未覆盖 / 低置信度 / 需确认条目

| # | 条目 | 状态 | 原因 | 建议 |
|---|------|------|------|------|
| 1 | 阿里云百炼 API 具体 endpoint | 🔴 未覆盖 | 用户未提供 | 需要用户提供阿里云百炼的 base URL 和 chat completion endpoint |
| 2 | 企业微信 webhook URL 格式 | 🔴 未覆盖 | 用户未提供 | 需要用户提供 webhook URL，确认是群机器人还是应用消息 |
| 3 | issue label 过滤需求 | 🟡 低置信度 | design.md 中标记为 Open Question | 是否需要只处理带 `research` label 的 issue？ |
| 4 | 代理配置在 Actions 中的处理 | 🟡 低置信度 | Actions 环境通常不需要代理 | 是否需要为 Actions 环境禁用代理？ |
| 5 | 报告文件命名规则 | 🟡 低置信度 | 现有脚本使用日期+slug | 是否需要添加 `[auto-research]` 前缀以区分手动调研？ |
| 6 | Actions 运行时长限制 | 🟡 低置信度 | GitHub Actions 有 6 小时限制 | 四工具调研+LLM 编译通常在 15 分钟内，风险较低 |
| 7 | 并发 issue 处理 | 🟡 低置信度 | 未明确 | 是否需要队列机制防止多个 issue 同时触发冲突？ |
| 8 | 报告内容摘要提取 | 🟡 低置信度 | 企业微信通知需要核心结论 | 如何从 LLM 编译结果中提取 3-5 条核心结论？ |

## 覆盖统计

| 类别 | 数量 |
|------|------|
| 已覆盖需求 | 16/16 (100%) |
| 未覆盖条目 | 2 |
| 低置信度条目 | 6 |
| 总 Spec Requirements | 16 |
| 总 Scenarios | 32 |
| 总 Tasks | 29 |
| 总 Batch | 4 |

## 关键阻塞项

1. **阿里云百炼 API endpoint**：影响 Task 5.3（阿里云 API 调用），阻塞 Batch 1
2. **企业微信 webhook URL**：影响 Task 7.1-7.5（企业微信通知），阻塞 Batch 2

## 建议下一步

1. **确认阿里云 API 参数**：获取 base URL、endpoint、请求格式
2. **确认企业微信配置**：获取 webhook URL，确认消息格式
3. **确认 issue label 过滤**：是否需要 `research` label 过滤
4. **确认报告命名规则**：是否添加 `[auto-research]` 前缀

以上确认后，即可进入 `/opsx:apply` 执行阶段。
