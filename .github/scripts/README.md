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

## 提示词设计与多维度检索策略

### 四工具的子查询自动拆解

脚本会自动将你的问题拆解为多个子查询，多角度检索：

| 子查询类型 | 示例 | 用途 |
|-----------|------|------|
| 原始查询 | `trea与cursor能力差距` | 核心主题检索 |
| 官方文档 | `trea与cursor能力差距 official documentation best practices` | 获取权威文档 |
| 最新动态 | `trea与cursor能力差距 latest developments 2025 2026` | 获取最新信息 |
| 工程实践 | `trea与cursor能力差距 engineering practice pitfalls` | 获取实践经验 |
| 学术论文 | `trea与cursor能力差距 research paper benchmark arXiv` | 获取学术研究 |
| 中文资料 | `trea与cursor能力差距 中文 资料 官方 文档` | 获取中文内容 |

### 一个 [调研] 是否足够？

**是的，一个 [调研] 足以覆盖多方位检索。**

原因：
- 四工具会自动生成 **最多 6 个子查询**，覆盖不同角度
- 每个子查询由不同工具执行（Tavily、Exa、Firecrawl、Jina）
- 最终合并去重，生成完整证据包

### 如何设计好的调研问题？

**推荐做法**：
- ✅ 用一句话描述核心主题
- ✅ 包含关键实体（产品名、技术名、公司名）
- ✅ 避免过于宽泛（如"AI 最新进展"）

**示例**：

| 好的问题 | 不好的问题 |
|---------|-----------|
| `trea与cursor能力差距` | `AI 编程工具`（太宽泛） |
| `2026年大模型在招投标领域的应用` | `大模型应用`（太宽泛） |
| `RAG技术在医疗领域的最新进展` | `RAG技术`（太宽泛） |

**不推荐的做法**：
- ❌ 在一个 issue 中提多个不相关的主题（应拆分为多个 issue）
- ❌ 问题过于宽泛，无法聚焦
- ❌ 包含过多限定条件（工具会自动补充）

### 多 Issue 并行策略

如果你有多个相关主题，可以创建多个 issue：

```
[调研] trea与cursor能力差距
[调研] tree与cursor定价策略对比
[调研] trea与cursor隐私合规差异
```

每个 issue 会独立执行，生成独立的调研报告。

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
- 每个 `[调研]` issue 会生成独立的调研报告，多个 issue 可并行执行
