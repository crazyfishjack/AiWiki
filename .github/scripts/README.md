# 自动调研脚本

通过 GitHub Issues 触发自动调研，生成中文调研报告并推送到企业微信。

## 触发方式

### 方式一：GitHub Issue（推荐）

在仓库创建标题以 `[调研]` 开头的 issue：

```
标题: [调研] 2026年大模型在招投标领域的最新应用
正文: （可选，补充详细描述或 AI 整理要求）
```

**正文内容作为 AI 整理要求**：
- 在 issue 正文中填写的内容会作为 AI 整理时的额外要求传递给 LLM
- 可以指定重点关注的内容、输出格式、分析角度等
- 例如："重点关注技术架构部分"、"对比不同厂商方案"、"输出表格对比"等
- 如不填写，则按默认方式生成报告

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

| Secret Name          | 说明                |
| -------------------- | ----------------- |
| `TAVILY_API_KEY`     | Tavily API Key    |
| `EXA_API_KEY`        | Exa API Key       |
| `FIRECRAWL_API_KEY`  | Firecrawl API Key |
| `JINA_API_KEY`       | Jina API Key      |
| `ALIYUN_API_KEY`     | 阿里云百炼 API Key     |
| `WECHAT_WEBHOOK_URL` | 企业微信 Webhook URL  |

## 脚本说明

| 脚本                   | 功能                   |
| -------------------- | -------------------- |
| `run-research.py`    | 主入口，编排完整管道           |
| `config_loader.py`   | 配置加载（环境变量 + 本地文件）    |
| `issue_parser.py`    | 解析 GitHub Issue 提取查询和 AI 整理要求 |
| `research_runner.py` | 调用四工具调研              |
| `llm_compiler.py`    | 调用阿里云 Qwen 编译报告（支持额外整理要求） |
| `git_pusher.py`      | Git commit + push    |
| `wechat_notifier.py` | 企业微信通知               |

## 依赖安装

```bash
pip install -r .github/scripts/requirements.txt
```

## 调研查询语义说明

### `[调研]` 标题的含义

`[调研]` 后面的内容**不是对用户问题的简单复述**，而是经过理解、拆解后的**多个检索关键词组合**。

#### 正确示例

用户问题："我想了解 Trae 和 Cursor 哪个更好用"

| 错误写法                       | 正确写法                                             |
| -------------------------- | ------------------------------------------------ |
| `[调研] Trae 和 Cursor 哪个更好用` | `[调研] Trae Cursor 功能特性 代码生成 模式 定价策略 跨文件重构 企业级隐私` |

#### 为什么需要拆解关键词？

1. **四工具检索原理**：Tavily、Exa、Firecrawl、Jina 通过关键词匹配网页内容
2. **多方位覆盖**：一个 `[调研]` 任务会同时检索多个关键词，覆盖不同维度
3. **避免遗漏**：简单复述用户问题可能遗漏关键维度（如定价、隐私、性能）

#### 关键词拆解原则示例

```
用户问题: "2026年大模型在招投标领域的最新应用"

拆解为检索关键词：
- 时间维度: 2026年
- 技术维度: 大模型 LLM AI
- 领域维度: 招投标  tender  bid
- 应用维度: 自动写作 智能评审 风险识别
- 组合检索: "大模型 招投标 2026" "AI tender automation"
```

### 四工具检索策略

一个 `[调研]` 任务会自动执行以下检索：

| 工具            | 作用     | 检索方式          |
| ------------- | ------ | ------------- |
| **Tavily**    | 通用搜索   | 基于关键词发现信源     |
| **Exa**       | 语义搜索   | 基于语义相似度发现相关页面 |
| **Firecrawl** | 精读普通页面 | 抓取并提取正文内容     |
| **Jina**      | 学术/PDF | 处理 PDF 和学术文献  |

**建议**：一个 `[调研]` 任务中放置 **5-10 个关键词**，覆盖用户问题的各个维度，不需要拆分成多个 issue。

## 注意事项

- `.github/scripts/config.local.json` 已加入 `.gitignore`，不会提交到仓库
- 所有 API Key 通过 GitHub Secrets 注入，不要在代码中硬编码
- 调研结果保存到 `raw/articles/` 目录

