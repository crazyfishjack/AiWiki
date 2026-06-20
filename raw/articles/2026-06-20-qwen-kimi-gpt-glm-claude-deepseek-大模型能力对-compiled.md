# 大模型代码能力对比调研报告：Qwen Kimi GPT GLM Claude DeepSeek (2026)

## 核心结论

1.  **SWE-bench Verified 领跑模型**：截至 2026 年 6 月，Claude Opus 4.6/4.8 系列在 SWE-bench Verified 基准上表现最强，得分在 80.8% 至 88.6% 之间，其次是 MiniMax M2.5 (80.2%) 和 GLM-5 (77.8%) [来源：https://www.datalearner.com/leaderboards/category/code] [来源：https://onyx.app/insights/best-llms-for-coding-2026] [来源：https://vals.ai/benchmarks/swebench]。
    *   **可信度**：高
2.  **算法与竞赛能力分化**：在 LiveCodeBench 等算法竞赛类基准上，Kimi K2.5 (85.0%) 和 DeepSeek V3.2-Speciale (88.7%) 表现优于通用工程模型，显示出专用模型在算法推理上的优势 [来源：https://onyx.app/insights/best-llms-for-coding-2026] [来源：https://unifuncs.com/s/RYSb15zp]。
    *   **可信度**：高
3.  **终端代理能力差异**：GPT-5.3/5.4 Codex 系列在 Terminal-Bench 2.0 上得分最高 (77.3%)，显著高于 Claude Opus 4.6 (65.4%)，表明其在命令行和自动化任务上的特殊性 [来源：https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding]。
    *   **可信度**：高
4.  **开源模型性价比突破**：DeepSeek V4 Flash 和 MiniMax M2.5 提供了接近旗舰模型的编程能力，但成本降低 10 倍以上（如 DeepSeek V4 Flash 输入$0.23/1M tokens），适合成本敏感型任务 [来源：https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm]。
    *   **可信度**：高
5.  **基准测试方法论演进**：SWE-Compass 和 LiveCodeBench 等新基准强调防污染和多语言覆盖，SWE-bench Verified 成为衡量真实工程修复能力的核心标准，HumanEval 因饱和（>90%）已失去区分度 [来源：https://arxiv.org/html/2511.05459v3] [来源：https://arxiv.org/html/2403.07974]。
    *   **可信度**：高
6.  **视觉与智能体能力融合**：Kimi K2.5 和 GLM-5.2 展示了视觉编程（Visual Agentic）能力，支持从截图生成代码，这在 DesignArena 排行榜上得到验证 [来源：https://arxiv.org/html/2602.02276] [来源：https://www.datalearner.com/leaderboards/category/code]。
    *   **可信度**：中
7.  **模型版本迭代快速**：2026 年上半年模型版本更新频繁（如 Claude Opus 4.6/4.7/4.8, GPT-5.2/5.3/5.4/5.5），基准分数随版本波动较大，需关注具体发布日期 [来源：https://vals.ai/benchmarks/swebench]。
    *   **可信度**：高

## 内容整理

### 1. 全球代码能力排行榜概览 (基于 SWE-bench Verified)

根据 DataLearner 和 Vals AI 的最新数据，2026 年 6 月的大模型代码能力排名如下。SWE-bench Verified 被视为最接近真实软件工程任务的基准。

#### 1.1 综合排名 top 10 (SWE-bench Verified)

| 排名 | 模型 | 机构 | SWE-bench Verified | LiveCodeBench | Terminal-Bench | 开源情况 | 来源 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Claude Fable 5 | Anthropic | 95.00% | — | — | 闭源 | [来源：https://www.datalearner.com/leaderboards/category/code] |
| 2 | Claude Opus 4.8 | Anthropic | 88.60% | — | — | 闭源 | [来源：https://vals.ai/benchmarks/swebench] |
| 3 | Claude Opus 4.6 | Anthropic | 80.8% - 81.42% | 76.0% | 65.4% | 闭源 | [来源：https://onyx.app/insights/best-llms-for-coding-2026] |
| 4 | MiniMax M2.5 | MiniMax | 80.2% | 65.0% | 42.2% | API | [来源：https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding] |
| 5 | GPT 5.5 | OpenAI | 82.60% | — | — | 闭源 | [来源：https://vals.ai/benchmarks/swebench] |
| 6 | GLM 5.2 | zAI | 82.80% | — | — | 免费商用 | [来源：https://vals.ai/benchmarks/swebench] |
| 7 | GLM-5 | 智谱 AI | 77.8% | 52.0% | 56.2% | 免费商用 | [来源：https://onyx.app/insights/best-llms-for-coding-2026] |
| 8 | Kimi K2.6 | Moonshot AI | 80.20% | — | — | 免费商用 | [来源：https://www.datalearner.com/leaderboards/category/code] |
| 9 | Kimi K2.5 | Moonshot AI | 76.8% | 85.0% | 未报告 | 免费商用 | [来源：https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding] |
| 10 | Qwen 3.5-plus | 阿里巴巴 | 76.4% | 83.6% | 52.5% | 免费商用 | [来源：https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding] |

*注：部分数据因来源不同存在细微差异，详见“跨源矛盾检测结论”。*

#### 1.2 设计 arena 代码类别排名 (视觉前端能力)

基于 Arcada Labs 平台，对视觉前端代码任务（网站、UI 组件、游戏、数据可视化等）进行匿名投票。

| 排名 | 模型 | 机构 | Elo 分数 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | GLM-5.2 | 智谱 AI | 1360 | [来源：https://www.datalearner.com/leaderboards/category/code] |
| 2 | Claude Fable 5 | Anthropic | 1350 | [来源：https://www.datalearner.com/leaderboards/category/code] |
| 3 | Claude Opus 4.6 | Anthropic | 1341 | [来源：https://www.datalearner.com/leaderboards/category/code] |
| 4 | Opus 4.7 (thinking) | Anthropic | 1337 | [来源：https://www.datalearner.com/leaderboards/category/code] |
| 5 | Kimi K2.6 | Moonshot AI | 1328 | [来源：https://www.datalearner.com/leaderboards/category/code] |

### 2. 主流模型详细能力对比 (2026 年 3 月快照)

基于 Onyx AI 和 Tech Jacks Solutions 的详细评测数据，以下是主要模型在四大基准上的表现及成本分析。

#### 2.1 核心基准得分对比表

| 模型 | 提供商 | SWE-bench | HumanEval | LiveCode | Terminal-Bench | API 成本 (每 1M 输入/输出) | 许可证 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Claude Opus 4.6** | Anthropic | **80.8%** | 95.0% | 76.0% | 65.4% | $15 / $75 | 专有 |
| **GPT-5.4** | OpenAI | N/A† | N/A | N/A | **75.1%** | $2.50 / $15 | 专有 |
| **MiniMax M2.5** | MiniMax | 80.2% | 89.6% | 65.0% | 42.2% | $0.30 / $1.20 | API |
| **Claude Sonnet 4.6** | Anthropic | 79.6% | 92.1% | 72.4% | 59.1% | $3 / $15 | 专有 |
| **Gemini 3.1 Pro** | Google | 78.0% | 93.0% | 81.3% | 56.2% | $2 / $12 | 专有 |
| **GLM-5** | Zhipu AI | 77.8% | 90.0% | 52.0% | 56.2% | Free API | MIT |
| **Kimi K2.5** | Moonshot | 76.8% | **99.0%** | 85.0% | 50.8% | Free API | MIT |
| **Qwen 3.5** | Qwen | 76.4% | N/A | 83.6% | 52.5% | Free API | Apache 2.0 |
| **Step-3.5-Flash** | Stepfun | 74.4% | 81.1% | **86.4%** | 51.0% | $0.10 / $0.30 | API |
| **MiMo-V2-Flash** | Xiaomi | 73.4% | 84.8% | 80.6% | 38.5% | Free API | MIT |

_† SWE-bench Verified 尚未公布 GPT-5.4 数据，SWE-bench Pro = 57.7%。_
[来源：https://onyx.app/insights/best-llms-for-coding-2026]

#### 2.2 任务难度分辨率 (Resolution Rate by Task Difficulty)

不同模型在不同耗时任务上的解决率（SWE-bench Verified 子集）：

| 模型 | <15 min (194 tasks) | 15m–1h (261 tasks) | 1–4 hr (42 tasks) | >4 hr (3 tasks) |
| :--- | :--- | :--- | :--- | :--- |
| GPT 5.5 | 92% | 81% | 50% | 67% |
| Claude Opus 4.7 | 90% | 79% | 64% | 67% |
| Composer 2.5 | 87% | 79% | 52% | 67% |
| Gemini 3.1 Pro Preview (02/26) | 89% | 78% | 43% | 33% |
| Claude Opus 4.6 (Thinking) | 90% | 75% | 43% | 33% |
| GPT 5.3 Codex | 90% | 73% | 55% | 33% |
| DeepSeek V4 | 88% | 76% | 45% | 0% |
| GLM 5.1 | 89% | 73% | 45% | 33% |
| Kimi K2.6 | 88% | 74% | 40% | 0% |
| MiniMax-M2.5 | 87% | 71% | 38% | 33% |

[来源：https://vals.ai/benchmarks/swebench]

### 3. 开源模型生态系统与成本路由策略

根据 Atlas Cloud 的开发者指南，2026 年开源编程模型已形成完整的成本 - 性能梯队，模型路由成为优化成本的关键策略。

#### 3.1 开源模型规格与成本对照表

| 模型 | 实验室 | 上下文 | 输入费率 ($/1K) | 输出费率 ($/1K) | 缓存写入 | 较官方优惠 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| DeepSeek V4 Flash | DeepSeek AI | 1M | 0.23 | 0.46 | 0.046 | -50% |
| DeepSeek V3.2 | DeepSeek AI | 160K | 0.42 | 0.62 | 0.193 | -55% |
| MiniMax M2.5 | MiniMax | 200K | 0.65 | 2.18 | 0.109 | -45% |
| Kimi K2.5 | Moonshot AI | 262K | 1.09 | 5.45 | 0.182 | -45% |
| Kimi K2.6 | Moonshot AI | 262K | 1.72 | 7.26 | 0.290 | -45% |
| GLM-5 | Zhipu AI | 200K | 1.82 | 5.81 | 0.363 | -45% |
| GLM-5.1 | Zhipu AI | 200K | 2.54 | 7.99 | 0.472 | -45% |
| DeepSeek V4 Pro | DeepSeek AI | 1M | 2.87 | 5.75 | 0.231 | -50% |
| Qwen3.6-plus | Alibaba | 256K+ | 3.30 | 9.90 | 0.660 | -50% |

[来源：https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm]

#### 3.2 模型路由成本计算示例

假设一次会话中 50 次 API 调用里有 60% 是简单任务（平均 2,000 输入 + 500 输出 Token）：

*   **若在 V4 Flash 上运行**：
    *   成本：30 次调用 × (2,000 × 0.23 + 500 × 0.46) = 30 × (460 + 230) = **20,700 积分**
*   **若全部在 V4 Pro 上运行**：
    *   成本：30 次调用 × (2,000 × 2.87 + 500 × 5.75) = 30 × (5,740 + 2,875) = **258,450 积分**
*   **差价**：仅这 30 次调用，差价就高达 12.5 倍。

[来源：https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm]

#### 3.3 推荐路由策略

*   **轻量级及后台任务**：DeepSeek V4 Flash (文档字符串、变量重命名、简单补全)。
*   **兼顾成本与性能**：DeepSeek V3.2 和 MiniMax M2.5 (中等复杂度工作)。
*   **长上下文工作负载**：Kimi K2.5 和 K2.6 (262K 上下文，大型代码库分析)。
*   **结构化输出与指令精准度**：GLM-5 和 GLM-5.1 (JSON 模式、格式化代码片段)。
*   **旗舰级推理**：DeepSeek V4 Pro 和 Qwen3.6-plus (复杂架构决策、多系统交互调试)。

[来源：https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm]

### 4. 基准测试方法论与演进

#### 4.1 LiveCodeBench 方法论

LiveCodeBench 是一个全面且无污染的代码评估框架，集成代码生成、自修复、代码执行和测试输出预测四个场景。

*   **数据来源**：LeetCode, AtCoder, CodeForces 的公开可见部分。
*   **过滤标准**：程序长度 100-500 字符，无语法错误，编译时间≤3 秒，运行时间≤2 秒。
*   **数据集统计**：最终基准包含 85 个不同问题的 479 个样本。
*   **防污染机制**：仅抓取问题陈述、真实解决方案和测试用例，避免付费墙或交互数据。

[来源：https://arxiv.org/html/2403.07974]

#### 4.2 SWE-Compass 统一评估框架

SWE-Compass 旨在解决现有基准任务覆盖窄、语言偏见和与真实工作流对齐不足的问题。

*   **覆盖范围**：8 种任务类型，8 种编程场景，10 种编程语言。
*   **设计原则**：
    1.  **真实世界对齐**：数据源自真实的开发者交互 (GitHub PRs)。
    2.  **全面覆盖**： diverse tasks and languages.
    3.  **系统分类**：结构化标签和平衡分布。
    4.  **评估 fidelity**：所有实例可执行且可验证。
*   **标准化构建/测试命令**：
    *   Python: `pytest -q`
    *   JavaScript/TypeScript: `npm ci && npm test --run`
    *   Java: `mvn -B -DskipTests=false test`
    *   Go: `go test ./...`
    *   Rust: `cargo test --locked`
    *   C/C++: `cmake --build && ctest -j1`

[来源：https://arxiv.org/html/2511.05459v3]

#### 4.3 SWE-bench Verified 说明

*   **定义**：模型被给予真实的 GitHub 问题，必须自主编写代码补丁使现有测试通过。
*   **重要性**：比 HumanEval 更能衡量理解整个代码库、定位相关文件的能力。
*   **阈值**：2026 年得分高于 75% 被视为前沿水平。
*   **局限性**：分数依赖于代理支架 (Agent Harness)，同一模型在不同支架下得分可能不同。

[来源：https://onyx.app/insights/best-llms-for-coding-2026] [来源：https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding]

### 5. 特定模型技术报告摘要

#### 5.1 Kimi K2.5: Visual Agentic Intelligence

*   **推理基准**：
    *   HLE-Full: 30.1%
    *   AIME 2025: 96.1%
    *   HMMT Feb 2025: 95.4%
    *   GPQA-Diamond: 87.6%
*   **长基准 v2**：
    *   WideSearch: 79.0%
    *   DeepSearchQA: 35.4%
    *   FinSearchComp T2&T3: 49.7%
*   **计算机使用能力**：Seal-QA, PaperBench。
*   **特点**：支持 100 个子智能体并行工作 (Agent Swarm)，视觉编程能力突出。

[来源：https://arxiv.org/html/2602.02276]

#### 5.2 Qwen3-Coder-Next Technical Report

*   **状态**：证据包中该来源精读失败，正文为空，无法提取具体技术细节。
*   **说明**：需二次精读或标注不可验证。

[来源：https://www.arxiv.org/pdf/2603.00729]

### 6. 2026 年 AI 编程能力八大模型深度对比 (UniFuncs 数据)

基于 UniFuncs 2026 年 3 月 1 日的深度搜索，以下是 8 个指定模型的客观评价数据汇总。

#### 6.1 编程能力数据汇总

| 模型 | SWE-bench Verified | Terminal-Bench 2.0 | LiveCodeBench / Codeforces | 核心优势 | 发布时间 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Claude Opus 4.6** | 81.42% | 65.4% | ~2850 (ELO) | 多文件重构、长上下文 (1M)、深度推理 | 2026 年 2 月 5 日 |
| **GPT-5.3-Codex** | ~80% (Pro 56.8%) | 77.3% | ~2887 (推测) | 终端操作最强、Token 效率高 2-4 倍 | 2026 年 2 月 5 日 |
| **Minimax M2.5** | 80.2% | - | ~2720 | 速度最快（37% 提升）、成本效益高 | 2026 年 2 月 12 日 |
| **Deepseek V3.2-Speciale** | - | - | 88.7% (LCB), 2701 (CF) | 算法竞赛最强、ICPC 金牌水平 | 2025 年 12 月 1 日 |
| **GLM-5** | 77.8% | 56.2% | ~2650 (ELO) | 开源模型最高、Agentic Engineering 领先 | 2026 年 2 月 |
| **Kimi K2.5** | 76.8% | 50.8% | 85.0% | 视觉编程能力突出、智能体集群 | 2026 年 1 月 27 日 |
| **Qwen3.5-Plus** | 70.6% | 52.5% | ~2580 (ELO) | 中文技术栈理解领先、多模态支持 | 2026 年 2 月 16 日 |
| **Seed-Coder** | 8B 级最佳 | - | 与 o1-mini 相当 | 小参数优化、轻量化 | 2026 年 2 月 |

[来源：https://unifuncs.com/s/RYSb15zp]

#### 6.2 选型建议

*   **企业级生产环境**：首选 Claude Opus 4.6 (最稳定可靠)，备选 MiniMax M2.5 (性价比极高)。
*   **成本敏感项目**：首选 DeepSeek V3.2 (开源 + 低成本)，备选 Qwen3.5-Plus (中文优化 + 低价)。
*   **前端/视觉开发**：首选 Kimi K2.5 (视觉编程 SOTA)。
*   **算法/竞赛**：首选 Deepseek V3.2-Speciale (ICPC 金牌水平)。
*   **边缘/轻量部署**：首选 Seed-Coder 8B (小参数最优)。
*   **国产化要求**：首选 GLM-5 (国产芯片适配 + 开源)。
*   **自动化/DevOps**：首选 GPT-5.3-Codex (终端操作最强)。

[来源：https://unifuncs.com/s/RYSb15zp]

## 推荐工作流

基于证据包中的模型路由策略和工具集成建议，推荐以下工作流：

1.  **统一网关接入**：使用支持多模型路由的统一 API 网关（如 Atlas Cloud Coding Plan），通过单一 API Key 访问 DeepSeek, Kimi, GLM, MiniMax, Qwen 等模型，避免维护多个账户 [来源：https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm]。
2.  **任务分级路由**：
    *   **规划与调试步骤**：路由至 DeepSeek V4 Pro 或 Claude Opus 4.6。
    *   **中等推理步骤**：路由至 Kimi K2.5 或 GLM-5。
    *   **辅助步骤 (文件读取/状态检查)**：路由至 DeepSeek V4 Flash 或 Step-3.5-Flash [来源：https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm]。
3.  **工具链集成配置**：
    *   **Claude Code**：配置 `ANTHROPIC_DEFAULT_HAIKU_MODEL` 为 DeepSeek V4 Flash，主模型为 V4 Pro [来源：https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm]。
    *   **Codex/OpenClaw**：配置 Base URL 为统一网关地址，模型 ID 动态切换 [来源：https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm]。
4.  **基准验证流程**：在生产环境部署前，使用 SWE-bench Verified 子集或内部 GitHub _issue_ 进行小规模 POC 测试，验证模型在特定代码库上的表现 [来源：https://onyx.app/insights/best-llms-for-coding-2026]。

## 适用场景

1.  **大型项目架构设计与重构**：适合使用 Claude Opus 4.6 或 GPT-5.4，利用其长上下文 (1M/256K) 和多文件理解能力 [来源：https://unifuncs.com/s/RYSb15zp]。
2.  **成本敏感的全栈开发**：适合使用 MiniMax M2.5 或 DeepSeek V4 系列，在保证 80% 左右 SWE-bench 得分的同时大幅降低 API 成本 [来源：https://onyx.app/insights/best-llms-for-coding-2026]。
3.  **前端 UI/UX 设计与还原**：适合使用 Kimi K2.5 或 GLM-5.2，利用其视觉编程和 DesignArena 高分表现 [来源：https://www.datalearner.com/leaderboards/category/code]。
4.  **算法竞赛与数学推理**：适合使用 DeepSeek V3.2-Speciale 或 Kimi K2.5，利用其 LiveCodeBench 高分和 AIME/GPQA 表现 [来源：https://arxiv.org/html/2602.02276]。
5.  **终端自动化与 DevOps**：适合使用 GPT-5.3-Codex，利用其 Terminal-Bench 领先优势 [来源：https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding]。
6.  **私有化部署与国产化**：适合使用 GLM-5 或 Qwen 系列，支持国产芯片适配和开源权重 [来源：https://unifuncs.com/s/RYSb15zp]。

## 不适用场景

1.  **极度保密的源代码处理**：不建议使用公共 API 模型（除非企业版零保留条款），应优先选择自托管开源模型（如 DeepSeek V4 开源权重）[来源：https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding]。
2.  **简单代码补全任务**：不建议全程使用旗舰模型（如 Opus 4.6），应路由至 Flash 模型以节省成本，否则属于过度工程 [来源：https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm]。
3.  **依赖 HumanEval 单一指标选型**：HumanEval 在 2026 年已饱和（>90%），无法区分前沿模型，仅参考此指标会导致选型失误 [来源：https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding]。
4.  **长上下文推理任务使用短上下文模型**：如使用上下文窗口仅 128K 的模型处理 1M 代码库，会导致信息丢失，应选择 DeepSeek V4 Pro 或 Claude Opus 4.6 [来源：https://unifuncs.com/s/RYSb15zp]。

## 风险与约束

1.  **基准分数依赖代理支架 (Scaffold-Dependent)**：SWE-bench 和 Terminal-Bench 分数受运行模型的代理 harness 影响，同一模型在不同支架下得分可能不同，小差距应视为噪声 [来源：https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding]。
2.  **模型版本迭代快速**：2026 年上半年模型版本更新频繁（如 Claude Opus 4.6/4.7/4.8），基准分数随版本波动，报告数据可能随时间失效 [来源：https://vals.ai/benchmarks/swebench]。
3.  **数据隐私与训练政策**：免费和消费级 API 可能保留输入用于训练，处理专有代码前需审查供应商数据保留政策，优先选择企业版 [来源：https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding]。
4.  **规格漂移 (Specification Drift)**：模型可能产生看似合理但错误的指导，特别是在 mental health, medical, legal 等领域，需人工核实 [来源：https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding]。
5.  **开源模型基准数据缺失**：部分新发布开源模型（如 DeepSeek V4-Pro, Kimi K2.6）缺乏公开独立报告的编码基准，排名可能存在滞后 [来源：https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding]。
6.  **Qwen 技术报告获取失败**：证据包中 Qwen3-Coder-Next 技术报告精读失败，相关内容无法验证，需谨慎引用 [来源：https://www.arxiv.org/pdf/2603.00729]。

## 信源质量门控记录

### 门控规则
*   Tavily score < 0.4：剔除
*   已知低质域名：剔除
*   重复 URL：合并保留最高分结果
*   Exa 学术/语义结果：默认保留，但进入来源等级评估
*   C/D 级来源不得作为唯一结论依据
*   入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`

### 保留信源
1.  **DataLearner Leaderboard** (https://www.datalearner.com/leaderboards/category/code) - 等级：B, 原因：与主题高度相关，含详细排行榜。
2.  **Onyx AI Blog** (https://onyx.app/insights/best-llms-for-coding-2026) - 等级：B, 原因：与主题高度相关，含详细对比表。
3.  **Tech Jacks Solutions** (https://techjacksolutions.com/ai-tools/rankings/best-llms-for-coding) - 等级：B, 原因：与主题高度相关，含方法论说明。
4.  **Kimi K2.5 Arxiv** (https://arxiv.org/html/2602.02276) - 等级：A, 原因：学术论文。
5.  **UniFuncs Deep Search** (https://unifuncs.com/s/RYSb15zp) - 等级：B, 原因：与主题高度相关，含 8 模型对比。
6.  **Vals AI SWE-bench** (https://vals.ai/benchmarks/swebench) - 等级：B, 原因：与主题高度相关，含最新 SWE 数据。
7.  **Atlas Cloud Blog** (https://www.atlascloud.ai/zh/blog/guides/coding-plan-best-open-source-coding-llm) - 等级：A, 原因：官方文档/技术文档，含成本路由。
8.  **LiveCodeBench Arxiv** (https://arxiv.org/html/2403.07974) - 等级：A, 原因：学术论文。
9.  **SWE-Compass Arxiv** (https://arxiv.org/html/2511.05459v3) - 等级：A, 原因：学术论文。
10. **Qwen3-Coder-Next Arxiv** (https://www.arxiv.org/pdf/2603.00729) - 等级：A, 原因：学术论文 (但精读失败)。

### 剔除信源
*   多个重复 URL (如 DataLearner, UniFuncs 的重复抓取) - 原因：重复 URL，已合并到最高分结果。
*   部分低分 Tavily 结果 - 原因：分数低于阈值或内容不相关。

## 来源与可信度

| 来源 | 类型 | 可信度 | 支撑内容 |
| :--- | :--- | :--- | :--- |
| DataLearner Leaderboard | 第三方榜单 | 高 | SWE-bench, LiveCodeBench 综合排名，DesignArena 排名 |
| Onyx AI Blog | 技术博客 | 高 | 模型详细对比表，成本分析，选型建议 |
| Tech Jacks Solutions | 技术博客 | 高 | 排名方法论，Top 7 模型详细评测，基准说明 |
| Kimi K2.5 Arxiv | 学术论文 | 高 | Kimi K2.5 推理基准，视觉智能体能力 |
| UniFuncs Deep Search | 深度搜索报告 | 中 | 8 模型对比数据，选型建议 (部分数据需交叉验证) |
| Vals AI SWE-bench | 第三方榜单 | 高 | SWE-bench Verified 最新得分，任务难度分辨率 |
| Atlas Cloud Blog | 技术指南 | 高 | 开源模型成本，路由策略，配置示例 |
| LiveCodeBench Arxiv | 学术论文 | 高 | LiveCodeBench 方法论，数据收集标准 |
| SWE-Compass Arxiv | 学术论文 | 高 | 统一评估框架，多语言支持，