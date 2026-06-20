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
