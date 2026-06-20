# 自动调研脚本

通过 GitHub Issues 触发自动调研，生成中文调研报告并推送到企业微信。

## 触发方式

### 方式一：GitHub Issue（推荐）

在仓库创建标题以 `[调研]` 开头的 issue：

```
标题: [调研] 2026年大模型在招投标领域的最新应用
正文: （可选，补充详细描述）
```

GitHub Actions 会自动触发调研流程。

### 方式二：本地命令行

```bash
python .github/scripts/run-research.py --query "调研主题"
```

## 提示词拆解与多关键词覆盖

### 为什么要拆解提示词？

单一关键词往往无法覆盖调研主题的全部维度。例如 `[调研] trea与cursor能力差距` 可能遗漏：
- Trae 的 Builder 模式 vs Cursor 的 Composer 模式
- 定价策略对比
- 隐私合规差异
- 插件生态兼容性

### 拆解原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **核心实体拆分** | 将主题拆成多个子实体分别调研 | "Trae" + "Cursor" + "能力对比" |
| **维度覆盖** | 技术/商业/合规/生态等维度 | "架构对比" + "定价策略" + "隐私合规" |
| **时间维度** | 加入时间限定获取最新信息 | "2026年最新" + "2025年评测" |
| **场景限定** | 针对特定使用场景 | "企业级应用" + "个人开发者" |

### 推荐的多关键词策略

对于 `[调研] trea与cursor能力差距`，建议拆解为：

```
[调研] Trae AI 编程助手功能特性与架构设计
[调研] Cursor AI 编程助手功能特性与定价策略
[调研] Trae vs Cursor 代码生成质量对比评测
[调研] Trae Builder模式与Cursor Composer模式差异
[调研] AI编程助手隐私合规与企业级安全认证
[调研] Trae Cursor插件生态兼容性对比2026
```

**优势**：
- 每个 issue 聚焦一个子主题，调研更深入
- 四工具分别检索不同关键词，覆盖更多信源
- 最终可合并为多维度综合报告

### 在 Issue 正文中指定拆解关键词

```
标题: [调研] trea与cursor能力差距
正文:
## 调研范围
请重点覆盖以下子主题：
1. 核心功能对比（代码生成、重构、调试）
2. 定价与商业模式
3. 隐私合规与企业级安全
4. 插件生态与兼容性
5. 2026年最新功能更新

## 关键词
- Trae Builder模式
- Cursor Composer模式
- AI编程助手定价
- 代码生成质量评测
```

## 配置方法

### 1. 本地配置文件

复制模板文件并填写敏感信息：

```bash
cp .github/scripts/config.example.json .github/scripts/config.local.json
```

编辑 `.github/scripts/config.local.json`，填入所有 API Key。

### 2. GitHub Secrets（Actions 必需）

在仓库 Settings > Secrets and variables > Actions 中添加：

| Secret Name | 说明 |
|------------|------|
| `TAVILY_API_KEY` | Tavily API Key |
| `EXA_API_KEY` | Exa API Key |
| `FIRECRAWL_API_KEY` | Firecrawl API Key |
| `JINA_API_KEY` | Jina API Key |
| `ALIYUN_API_KEY` | 阿里云百炼 API Key |
| `WECHAT_WEBHOOK_URL` | 企业微信 Webhook URL |

## 脚本说明

| 脚本 | 功能 |
|------|------|
| `run-research.py` | 主入口，编排完整管道 |
| `config_loader.py` | 配置加载（环境变量 + 本地文件） |
| `issue_parser.py` | 解析 GitHub Issue 提取查询 |
| `research_runner.py` | 调用四工具调研 |
| `llm_compiler.py` | 调用阿里云 Qwen 编译报告 |
| `git_pusher.py` | Git commit + push |
| `wechat_notifier.py` | 企业微信通知 |

## 依赖安装

```bash
pip install -r .github/scripts/requirements.txt
```

## 注意事项

- `.github/scripts/config.local.json` 已加入 `.gitignore`，不会提交到仓库
- 所有 API Key 通过 GitHub Secrets 注入，不要在代码中硬编码
- 调研结果保存到 `raw/articles/` 目录
- 建议每个调研主题拆分为 3-5 个相关 issue，提升覆盖率和深度
