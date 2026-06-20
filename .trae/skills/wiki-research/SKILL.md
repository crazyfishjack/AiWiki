---
name: wiki-research
description: 为本 AI Wiki 执行知识调研、Wiki 优先检索、四工具外部搜索、raw 调研文档生成和确认后知识入库。当用户要求调研、搜索、检索 Wiki、知识入库、外部检索，或提到 Tavily、Exa、Firecrawl、Jina、四工具、wiki 没有结果、保存调研到 raw 时使用。
---

# Wiki 调研与入库

## 核心规则

本技能把当前项目作为 AI Wiki 操作。目标 Wiki 的唯一权威契约始终是 `SCHEMA.md`。

不得发明另一套 schema、关系类型、页面模板、索引格式或日志格式。若本技能说明与 `SCHEMA.md` 冲突，以 `SCHEMA.md` 为准。

## 必读输入

凡是依赖 Wiki 位置的操作，必须先执行：

1. 从 `--config`、`WIKI_RESEARCH_CONFIG`，或本技能旁边的 `config.local.json` 加载配置。
2. 从配置中读取 `wiki_root`。
3. 读取 `wiki_root` 下的 `SCHEMA.md`。
4. 读取 `wiki/_index.md` 后，再判断是否需要外部调研。

禁止打印 API Key，禁止把 Key 复制到对话里。若缺少 Key，只说明缺少哪个字段名。

## 工作流

每个调研任务都按以下顺序执行：

1. **Wiki 优先查询**
   - 遵循 `SCHEMA.md` 的 Query 规则。
   - 先读 `wiki/_index.md`。
   - 只读取直接相关页面和必要关联页面。
   - 如果现有 Wiki 内容足够回答，直接基于 Wiki 回答，不调用外部 API。

2. **Wiki 缺失或不足时外部调研**
   - 使用 `scripts/four_tool_research.py`。
   - 脚本从配置中读取 Tavily、Exa、Firecrawl、Jina Key 和 `wiki_root`。
   - 默认采用质量优先策略：Tavily + Exa 发现信源，Firecrawl 精读普通页面，Jina 仅用于学术 PDF / Rerank。
   - 默认精读最多 10 个 URL；Exa highlights 默认 4000 字符，仅用于候选发现和筛选。
   - 脚本输出的是“证据包草稿”，包含候选信源、完整精读结果和综合提示，不得直接视为可用调研报告。

3. **AI 编译中文调研报告**
   - 脚本完成后，必须读取生成的证据包。
   - 证据包默认保存 Firecrawl/Jina 的完整精读结果；如果高可信来源已有完整正文，不需要重复抓取同一 URL。
   - 当高可信来源精读失败、正文为空、明显只包含导航/付费墙/反爬内容，或工具返回结果不足以覆盖正文时，必须二次精读或标注不可验证。
   - 最终中文调研报告必须基于“证据包完整精读结果 + 必要的二次精读”综合编译，编写为一个新的 raw Markdown 文件，并删除对应证据包。
   - 最终 raw 调研报告必须包含：核心结论、内容整理、推荐工作流、适用场景、不适用场景、风险与约束、信源质量门控记录、来源与可信度、对于可信度较高的来源逐来源总结、跨源矛盾检测结论、矛盾与待验证问题。
   - `## 内容整理` 必须保留所有有用的信息，系统化，结构清晰，逻辑正确。
   - 最终 raw 调研报告必须包含 `## 对于可信度较高的来源逐来源总结`，逐篇整理高可信来源的正文内容、可用事实、局限和适合入库的知识点。
   - 如果重要来源在证据包中出现 `[truncated]`、正文为空、抓取失败或明显不足以覆盖正文，必须二次精读全文后再总结，不得只依赖不完整内容。
   - 每条关键事实必须标注来源 URL；不能找到来源的内容必须标注“未验证”，不得混入正文事实。
   - `## 信源质量门控记录` 必须列出门控规则、保留信源、剔除信源、来源等级、保留/剔除原因和后续处理。
   - `## 跨源矛盾检测结论` 必须检测核心数字、日期、功能描述、因果判断、市场/公司事实；未发现矛盾也必须明确写出。
   - 可信度使用三档：高（直接多源支撑）、中（单源或间接推断）、低（来源弱、矛盾或需验证）。
   - raw 调研阶段来源等级使用 A/B/C/D；用户确认入库到 `wiki/sources/` 时映射为：A/B → `source-quality: high`，C → `source-quality: medium`，D → `source-quality: low`。

4. **询问是否入库**
   - 最终 raw 调研报告创建后，必须询问用户是否将该 raw 文件入库。
   - 用户拒绝或没有明确确认时停止，不更新 `wiki/`、`_index.md`、`_graph.md` 或 `_log.md`。
   - 用户确认后，才对该 raw 文件执行完整 `SCHEMA.md` Ingest 工作流。

5. **严格按 SCHEMA 入库**
   - 使用 `SCHEMA.md` 的 9 步 Ingest 流程。
   - 为 raw 文件创建 `wiki/sources/` 来源摘要页。
   - raw 调研报告中的 A/B/C/D 来源等级必须按映射写入来源摘要页的 `source-quality`：A/B → high，C → medium，D → low。
   - 只按 `SCHEMA.md` 更新或新建知识页。
   - 按 `SCHEMA.md` 要求更新 `_index.md`、`_graph.md` 和 `_log.md`。

## 支撑文档

- 详细流程：[WORKFLOW.md](WORKFLOW.md)
- 配置与脚本用法：[README.md](README.md)
- 配置模板：[config.example.json](config.example.json)
- 调研脚本：[scripts/four_tool_research.py](scripts/four_tool_research.py)

## 硬性边界

- 没有用户明确确认，不得写入 `wiki/`。
- 本技能正常运行时不得修改 `SCHEMA.md`。
- 除非用户明确要求，不得修改已有项目文档。
- 普通页面不得使用 Jina readerlm-v2，必须使用 Firecrawl。
- 普通页面 Firecrawl 精读结果默认完整写入证据包，不得主动按字符数截断。
- 生成的调研文档通过 `SCHEMA.md` Ingest 前，只能视为 raw 原始资料，不能视为可信 Wiki 知识。
