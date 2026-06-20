## 1. 配置管理模块 (config-management)

- [x] 1.1 创建 `.github/scripts/config.example.json` 模板文件，包含所有字段（Tavily/Exa/Firecrawl/Jina/阿里云/企业微信）
- [x] 1.2 实现 `config_loader.py`：支持从 GitHub Secrets（环境变量）和本地 JSON 文件加载配置，GitHub Secrets 优先
- [x] 1.3 实现配置校验函数 `validate_config()`：检查所有必需字段非空，代理 URL 格式正确，缺失时打印具体字段名并退出
- [x] 1.4 更新 `.gitignore`，添加 `.github/scripts/config.local.json` 和 `.github/scripts/config.*.local.json`

## 2. Issue 解析模块 (github-actions-trigger)

- [x] 2.1 实现 `issue_parser.py`：从 `GITHUB_EVENT_PATH` JSON 解析 issue 标题和正文
- [x] 2.2 实现查询提取逻辑：标题以 `[调研]` 开头时提取后续内容；标题仅为 `[调研]` 时使用正文第一行
- [x] 2.3 实现 `--query` 命令行参数支持，直接传入时跳过 issue 解析
- [x] 2.4 添加非调研 issue 过滤：标题不含 `[调研]` 前缀时直接退出状态码 0

## 3. GitHub Actions Workflow (github-actions-trigger)

- [x] 3.1 创建 `.github/workflows/auto-research.yml`：监听 `issues: types: [opened]`
- [x] 3.2 配置 workflow 环境：Python 3.11、依赖安装（`requests` 等）
- [x] 3.3 配置 Secrets 注入：将 GitHub Secrets 映射为环境变量
- [x] 3.4 配置 workflow 执行步骤：检出代码 → 安装依赖 → 运行 `run-research.py`
- [x] 3.5 配置 workflow 权限：`contents: write`（用于 git push）

## 4. 调研执行模块 (research-executor)

- [x] 4.1 实现 `research_runner.py`：封装调用 `four_tool_research.py` 的函数
- [x] 4.2 实现标准模式调用：`--query <query> --mode standard --raw-dir raw/articles`
- [x] 4.3 实现输出捕获：解析 stdout 中的 `RAW_RESEARCH_FILE=` 获取证据包路径
- [x] 4.4 实现调研失败处理：捕获异常，记录错误，继续执行通知步骤

## 5. LLM 编译模块 (aliyun-llm-compiler)

- [x] 5.1 实现 `llm_compiler.py`：读取证据包文件，构造编译提示词
- [x] 5.2 实现提示词构造：包含证据内容、输出结构要求、引用规则、可信度标注、跨源矛盾检测要求
- [x] 5.3 实现阿里云百炼 API 调用：POST 到 chat completion endpoint，模型 `qwen3.5-plus`
- [x] 5.4 实现重试机制：HTTP 429 时等待 5 秒重试，最多 3 次
- [x] 5.5 实现编译失败回退：API 失败时保存原始证据包，包含警告通知
- [x] 5.6 实现编译结果写入：将 LLM 输出保存为新的 raw Markdown 文件，删除证据包

## 6. Git 推送模块 (research-executor)

- [x] 6.1 实现 `git_pusher.py`：配置 git 用户信息（`git config user.name/email`）
- [x] 6.2 实现 git add：添加生成的报告文件
- [x] 6.3 实现 git commit：消息格式 `[auto-research] <query>`
- [x] 6.4 实现 git push：推送到 `origin main`
- [x] 6.5 实现冲突处理：`git pull --rebase` 后重试一次，失败时报告错误

## 7. 企业微信通知模块 (wechat-notifier)

- [x] 7.1 实现 `wechat_notifier.py`：POST markdown 格式消息到企业微信 webhook
- [x] 7.2 实现成功通知模板：包含调研主题、报告路径、核心结论、执行时间
- [x] 7.3 实现失败通知模板：包含调研主题、失败环节、错误摘要、Actions 日志链接
- [x] 7.4 实现 webhook 缺失处理：`WECHAT_WEBHOOK_URL` 未配置时跳过通知，记录警告
- [x] 7.5 实现通知失败不影响管道：通知失败时记录日志但不中断流程

## 8. 主入口脚本 (research-executor)

- [x] 8.1 实现 `run-research.py`：主入口，按顺序调用各模块
- [x] 8.2 实现管道编排：config → issue_parser → research_runner → llm_compiler → git_pusher → wechat_notifier
- [x] 8.3 实现错误处理：任一环节失败时跳过后续步骤，执行失败通知
- [x] 8.4 实现日志输出：每个步骤的开始/结束/结果输出到 stdout，便于 Actions 日志查看
- [x] 8.5 实现退出码：成功返回 0，失败返回 1

## 9. 依赖管理

- [x] 9.1 创建 `.github/scripts/requirements.txt`：列出所有 Python 依赖（`requests` 等）
- [x] 9.2 验证依赖版本兼容性：确保与现有 `four_tool_research.py` 的依赖一致

## 10. 测试与配置

- [ ] 10.1 配置 GitHub Secrets：`TAVILY_API_KEY`、`EXA_API_KEY`、`FIRECRAWL_API_KEY`、`JINA_API_KEY`、`ALIYUN_API_KEY`、`WECHAT_WEBHOOK_URL`
- [ ] 10.2 本地测试：使用 `--query` 参数直接运行 `run-research.py`，验证完整管道
- [ ] 10.3 创建测试 issue：在仓库创建 `[调研] 测试主题` issue，验证 Actions 自动触发
- [ ] 10.4 验证企业微信通知：确认收到成功/失败通知

## 11. 文档与交付

- [x] 11.1 创建 `.github/scripts/README.md`：说明脚本用法、配置方法、触发方式
- [ ] 11.2 更新项目主 README：添加自动调研功能说明
- [ ] 11.3 端到端验证：从创建 issue 到收到企业微信通知的完整流程验证
