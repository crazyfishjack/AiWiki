# Wiki 调研技能

这个项目技能用于调研 Wiki 缺失知识，将调研结果保存为 raw Markdown 原始资料，并在用户确认后按 `SCHEMA.md` 入库。

## 配置

1. 将 `config.example.json` 复制为本机私有配置文件。

推荐本地路径：

```text
.cursor/skills/wiki-research/config.local.json
```

2. 填写以下字段：

- `wiki_root`
- `raw_default_dir`
- `proxy`
- `api_keys.tavily`
- `api_keys.exa`
- `api_keys.firecrawl`
- `api_keys.jina`
- `research_defaults.max_deep_read_urls`：标准模式最多精读 URL 数，默认 10
- `research_defaults.exa_highlight_char_limit`：Exa highlights 字符上限，默认 4000
- `research_defaults.evidence_full_content`：是否将 Firecrawl/Jina 精读正文完整写入证据包，默认 `true`

3. 不要提交 `config.local.json`。

也可以把配置放在仓库外，并设置环境变量：

```bash
set WIKI_RESEARCH_CONFIG=C:\path\to\wiki-research-config.json
```

## 脚本用法

只验证配置，不调用 API：

```bash
python .cursor/skills/wiki-research/scripts/four_tool_research.py --dry-run --query "test"
```

标准调研：

```bash
python .cursor/skills/wiki-research/scripts/four_tool_research.py --query "需要调研的主题"
```

快速搜索 + 全文：

```bash
python .cursor/skills/wiki-research/scripts/four_tool_research.py --query "需要调研的主题" --mode quick
```

写入指定 raw 目录：

```bash
python .cursor/skills/wiki-research/scripts/four_tool_research.py --query "需要调研的主题" --raw-dir raw/papers
```

## 输出

脚本会在配置的 raw 目录中写入一篇中文 Markdown 证据包草稿。证据包包含来源 URL、信源质量门控记录、完整精读结果、跨源矛盾检测模板、工具运行摘要和 AI 综合提示。默认会精读最多 10 个 URL；Exa highlights 默认 4000 字符，仅用于候选发现和筛选；普通网页由 Firecrawl 精读，精读正文默认完整写入证据包，不做字符截断。

Agent 必须读取该证据包，并基于证据包中的完整精读结果生成最终中文调研报告，编写为一个新的 raw Markdown 文件，并删除对应证据包。若高可信来源精读失败、正文为空、明显只包含导航/付费墙/反爬内容，或工具返回结果不足以覆盖正文，Agent 必须二次精读或标注不可验证。最终报告需要包含核心结论、内容整理、推荐工作流、适用/不适用场景、风险与约束、信源质量门控记录、来源与可信度、对于可信度较高的来源逐来源总结、跨源矛盾检测结论、矛盾与待验证问题。其中 `内容整理` 必须保留所有有用的信息，系统化，结构清晰，逻辑正确；逐来源部分要求逐篇整理高可信来源正文。

信源质量门控记录必须保留门控规则、保留信源、剔除信源、来源等级、保留/剔除原因和后续处理。raw 调研阶段来源等级使用 A/B/C/D；用户确认入库到 `wiki/sources/` 时按以下规则写入 `source-quality`：A/B → `high`，C → `medium`，D → `low`。跨源矛盾检测结论必须覆盖核心数字、日期、功能描述、因果判断、市场/公司事实；未检测到矛盾也必须明确写出。

对重要来源，如果证据包正文为空、抓取失败、出现 `[truncated]`，或明显不足以覆盖正文，Agent 必须二次精读全文后再总结，不得只依赖不完整内容。

最终 raw 文件完成后，Agent 才能询问用户是否入库。入库必须遵循目标 Wiki 的 `SCHEMA.md`，不得修改无关文件。
