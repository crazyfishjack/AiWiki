# 大模型能力对比调研报告：Qwen/Kimi/GPT/GLM/Claude/DeepSeek 全系列代码跑分与选型指南 (2026 年 6 月)

## 核心结论

1.  **Claude 系列在代码能力基准测试中仍居首位，但国产模型差距显著缩小。**
    Claude Fable 5 在 SWE-bench Verified 上达到 95.00%，Opus 4.6 为 80.84%；国产模型中 DeepSeek-V4-Pro 达到 80.60%，Qwen3.7-Max-Preview 达到 80.40%，GLM-5.1 在编程能力上达到 Claude Opus 4.6 的 94.6%。[来源：https://www.datalearner.com/leaderboards/category/code] [来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
    *可信度：高*

2.  **国产模型在 Token 消耗量上已全面超越美国模型，成为开发者首选。**
    2026 年 3 月 30 日至 4 月 5 日一周内，中国模型处理 12.96 万亿 tokens，美国模型仅 3.03 万亿 tokens；全球 token 消耗量前六名全部来自中国，DeepSeek 开源份额虽降至 40%，但 Qwen、MiMo 分流明显。[来源：https://www.cnblogs.com/skyseraph/p/19966095]
    *可信度：高*

3.  **DeepSeek-V4 系列以极致性价比颠覆定价体系，适合高并发生产环境。**
    DeepSeek-V4-Flash 输入价格低至 $0.14/1M tokens，输出 $0.28/1M tokens，约为 GPT-5.5 的 1/350，且支持 1M 上下文，SWE-bench Verified 得分 79.00%-80.60%。[来源：https://www.cnblogs.com/skyseraph/p/19966095] [来源：https://www.datalearner.com/leaderboards/category/code]
    *可信度：高*

4.  **Kimi K2.6 与 GLM-5.1 在 Agent 编排与开源权重上具有独特优势。**
    Kimi K2.6 支持 Agent Swarm 编排，SWE-Bench Pro 得分 58.6%；GLM-5.1 为 MIT 协议开源，编程能力接近闭源旗舰，且全华为昇腾训练。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
    *可信度：高*

5.  **上下文窗口已成为旗舰模型标配，1M tokens 成为新基准。**
    Claude Opus 4.6、GPT-4.1、Gemini 2.5 Pro、Qwen3.5-Plus、DeepSeek-V4 均支持 1M 上下文；Kimi K2.6 支持 256K-2M 上下文，适合长文档分析。[来源：https://segmentfault.com/a/1190000047676047] [来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
    *可信度：高*

6.  **模型选型需按场景分化，无单一最优解。**
    复杂架构设计首选 Claude Opus 4.7；日常编码首选 DeepSeek-V4 或 Claude Sonnet 4.6；国内项目首选 GLM-5.1 或 Kimi K2.6；高并发首选 DeepSeek-V4-Flash。[来源：https://cloud.tencent.com/developer/article/2670420]
    *可信度：中*

7.  **SWE-bench 等基准测试存在版本差异，需结合实测数据。**
    不同来源显示的 SWE-bench 分数存在差异（如 Opus 4.6 在 72.5% 至 80.84% 之间），源于测试集版本（Verified vs Pro vs Multilingual）及更新时间不同。[来源：https://www.datalearner.com/leaderboards/category/code] [来源：https://segmentfault.com/a/1190000047676047]
    *可信度：中*

## 内容整理

### 1. 2026 年大模型市场格局与 Token 使用量

#### 1.1 全球 Token 使用量排行榜
2026 年最显著的趋势是国产模型在 token 使用量上已全面超越美国。据 OpenRouter 数据，2026 年 3 月 30 日至 4 月 5 日一周内，中国模型处理 **12.96 万亿 tokens**，美国模型仅 **3.03 万亿 tokens**。全球 token 消耗量前六名 **全部来自中国**。[来源：https://www.cnblogs.com/skyseraph/p/19966095]

| 排名 | 模型 | 厂商 | 周 Token 量（估算） | 主要优势 |
| --- | --- | --- | --- | --- |
| 1 | MiMo-V2.5-Pro | 小米 | ~4.79T | 1T 参数 MoE，1M 上下文 |
| 2 | Kimi K2.6 | Moonshot AI | ~1.4T | 编码榜第一，256K 上下文 |
| 3 | DeepSeek-V4-Flash | DeepSeek | 高 | 极低成本，1M 上下文 |
| 4 | Qwen 系列 | 阿里巴巴 | 高 | 多尺寸覆盖，开源生态 |
| 5 | GLM-5 | 智谱 Z.AI | 中高 | 国内首个上市大模型公司旗舰 |
| 6 | Claude Sonnet 4.6 | Anthropic | 中 | SWE-bench 标杆，综合能力领先 |
| 7 | Gemini 3.1 Flash | Google | 中 | 速度快，价格低，多模态 |
| 8 | GPT-5.5 | OpenAI | 中 | 生态最广，品牌溢价高 |
| 9 | MiniMax-M2.5 | MiniMax | 中 | 音视频多模态领先 |
| 10 | Grok 4 | xAI | 低中 | 实时 X 数据，推理强 |

**关键数据对比：**
| 时间 | 中国模型 | 美国模型 | 全球总量 |
| --- | --- | --- | --- |
| 2025-05（首次超越） | 4.12 万亿 | 2.94 万亿 | — |
| 2026-03-30 ~ 04-05 | **12.96 万亿** | 3.03 万亿 | **27 万亿** |

中国模型在 OpenRouter 平台占比从 2025 年初 <2% 升至 2026 年 Q2 **>45%**。DeepSeek 开源份额从 ~80% 降至 ~40%，被 Qwen、MiMo 分流。[来源：https://www.cnblogs.com/skyseraph/p/19966095]

#### 1.2 两条赛道与博弈
大模型套餐市场分化为两种范式：
- **按量计费（API）**：以 token 为单位付费，适合开发者，成本透明。
- **订阅制（Consumer）**：月付/年付，固定费用解锁配额，适合个人和非技术用户。[来源：https://www.cnblogs.com/skyseraph/p/19966095]

### 2. 各大模型系列详细能力对比

#### 2.1 Qwen 全系列 (阿里巴巴)
Qwen3.6 的关键不是某一个模型，而是阿里用一套品牌名同时打了四张牌。
- **Qwen3.6-Plus**：2026-04-02 发布，闭源 API，1M token 上下文默认开启，主打企业级 agentic 编码。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
- **Qwen3.6-Max-Preview**：2026-04-20 发布，260K 上下文，在 SWE-bench Pro、Terminal-Bench 2.0、SciCode 等六个 agentic 编码 benchmark 拿第一。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
- **Qwen3.6-35B-A3B**：2026-04-16 发布，35B / 3B（MoE），256K 上下文，Apache 2.0 开源，中等推理成本社区款。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
- **Qwen3.6-27B**：2026-04-22 发布，27B（稠密），256K 上下文，Apache 2.0 开源，单卡可跑入门款。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
- **Qwen3.7-Max-Preview**：DataLearner 数据显示 SWE-bench Verified 得分 80.40%，SWE-Bench Pro - Public 60.60%。[来源：https://www.datalearner.com/leaderboards/category/code]

**架构细节：**
Qwen3 系列包括 models of both dense and Mixture-of-Expert (MoE) architectures，parameter scales ranging from 0.6 to 235 billion。Key innovation is the integration of thinking mode (for complex, multi-step reasoning) and non-thinking mode (for rapid, context-driven responses) into a unified framework。Qwen3 introduces a thinking budget mechanism, allowing users to allocate computational resources adaptively during inference。[来源：https://arxiv.org/html/2505.09388]

#### 2.2 Kimi 全系列 (Moonshot AI)
- **Kimi K2.6**：2026-04-20 发布，1T 总参数，32B 激活（MoE），256K 上下文，Modified MIT 开源。原生多模态，自带 Agent Swarm 编排能力，可以同时调度 300 个领域子代理，在一次自主运行中执行最多 4000 步协调动作。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
- **跑分数据**：SWE-Bench Pro 拿到 58.6%，与 GPT-5.5 持平；Humanity's Last Exam（带工具）拿到 54.0%，超过 Claude Opus 4.6。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
- **DataLearner 数据**：SWE-bench Verified 80.20%，SWE-Bench Pro - Public 58.60%，SWE-bench Multilingual 76.70%。[来源：https://www.datalearner.com/leaderboards/category/code]
- **定价**：输入 $0.60/1M，输出 $2.50/1M。[来源：https://www.cnblogs.com/skyseraph/p/19966095]

#### 2.3 GPT 全系列 (OpenAI)
- **GPT-5.5**：2026 年 4 月推出，套餐扩展至六档。Plus 套餐 ($20/月) 默认使用 GPT-5.5。[来源：https://www.cnblogs.com/skyseraph/p/19966095]
- **API 计费**：GPT-5.5 输入 $1.75/1M，输出 $14.00/1M。[来源：https://www.cnblogs.com/skyseraph/p/19966095]
- **能力数据**：DataLearner 显示 GPT-5.2 SWE-bench Verified 80.00%，SWE-Bench Pro - Public 55.60%。Tencent Cloud 文章称 GPT-5.5 SWE-bench Verified 得分 88.7%。[来源：https://www.datalearner.com/leaderboards/category/code] [来源：https://cloud.tencent.com/developer/article/2670420]
- **特色**：电脑操控能力 OSWorld-Verified 成功率 75%，超人类平均水平。[来源：https://cloud.tencent.com/developer/article/2670420]

#### 2.4 GLM 全系列 (智谱 AI)
- **GLM-5.1**：2026-04-07 发布，MIT 协议开源，编程能力达 Claude Opus 4.6 的 94.6%，训练算力全程华为昇腾。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
- **GLM-5**：DataLearner 显示 SWE-bench Verified 77.80%。[来源：https://www.datalearner.com/leaderboards/category/code]
- **定价**：GLM-5 输入 $1.00/1M，输出 $0.20/1M，上下文 200K。[来源：https://www.cnblogs.com/skyseraph/p/19966095]
- **SWE-bench Pro**：Tencent Cloud 文章称 GLM-5.1 SWE-bench Pro 得分 58.4%，正式超越 Claude Sonnet 4.5 Thinking。[来源：https://cloud.tencent.com/developer/article/2670420]

#### 2.5 Claude 全系列 (Anthropic)
- **Claude Fable 5**：DataLearner 显示 SWE-bench Verified 95.00%，LMArena Coding Arena Elo 1563 排名第一。[来源：https://www.datalearner.com/leaderboards/category/code]
- **Claude Opus 4.6/4.7/4.8**：
    - Opus 4.6：SWE-bench Verified 80.84%，输入 $5.00/1M，输出 $25.00/1M，上下文 1M。[来源：https://www.datalearner.com/leaderboards/category/code] [来源：https://www.cnblogs.com/skyseraph/p/19966095]
    - Opus 4.7：LMArena Coding Arena Elo 1553 (Thinking)，1549 (Normal)。[来源：https://www.datalearner.com/leaderboards/category/code]
    - Opus 4.8：SWE-bench Verified 88.60%。[来源：https://www.datalearner.com/leaderboards/category/code]
- **订阅套餐**：Pro $20/月，Max 5x $100/月，Max 20x $200/月。[来源：https://www.cnblogs.com/skyseraph/p/19966095]

#### 2.6 DeepSeek 全系列 (深度求索)
- **DeepSeek-V4-Pro**：1.6T 总参数 / 49B 激活，1M 上下文。DataLearner 显示 SWE-bench Verified 80.60% (思考水平·极高工具)，79.40% (开启思考工具)。[来源：https://www.datalearner.com/leaderboards/category/code]
- **DeepSeek-V4-Flash**：284B 总参数 / 13B 激活，1M 上下文。DataLearner 显示 SWE-bench Verified 79.00%。[来源：https://www.datalearner.com/leaderboards/category/code]
- **定价**：V4-Flash 输入 $0.14/1M，输出 $0.28/1M。V4-Pro 原价输入 ~$1.74/1M，输出 ~$3.48/1M，折扣后 $0.435/$0.87。[来源：https://www.cnblogs.com/skyseraph/p/19966095]
- **策略**：免费版功能完整，无消费者订阅套餐，超低 API 价格服务开发者。[来源：https://www.cnblogs.com/skyseraph/p/19966095]

#### 2.7 MiniMax 全系列
- **MiniMax M2.7**：2026-03-18 上线，230B / 10B（MoE），200K 上下文。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
- **跑分**：Atlas Cloud 的 SWE-Bench Pro 测试里，M2.7 拿到 56.22%，是 GLM-5.1 的 94%。DataLearner 显示 M2.5 SWE-bench Verified 80.20%。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026] [来源：https://www.datalearner.com/leaderboards/category/code]
- **定价**：输入 ~$0.30/1M。[来源：https://www.cnblogs.com/skyseraph/p/19966095]

### 3. 代码能力基准测试详细数据 (2026 年 6 月)

#### 3.1 SWE-bench Verified 排行榜 (Top 15)
| 排名 | 模型 | 厂商 | SWE-bench Verified | LiveCodeBench | SWE-Bench Pro - Public | 开源情况 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Claude Fable 5 | Anthropic | 95.00 | — | 80.30 | 闭源 |
| 2 | Claude Mythos Preview | Anthropic | 93.90 | — | 77.80 | 闭源 |
| 3 | Claude Opus 4.8 | Anthropic | 88.60 | — | 69.20 | 闭源 |
| 4 | Opus 4.7 | Anthropic | 87.60 | — | 64.30 | 闭源 |
| 5 | Claude Sonnet 4.5 | Anthropic | 82.00 | — | — | 闭源 |
| 6 | Claude Sonnet 5 | Anthropic | 82.00 | — | — | 闭源 |
| 7 | Opus 4.5 | Anthropic | 80.90 | 87.00 | — | 闭源 |
| 8 | Claude Opus 4.6 | Anthropic | 80.84 | — | — | 闭源 |
| 9 | Gemini 3.1 Pro Preview | Google | 80.60 | 91.70 | 54.20 | 闭源 |
| 10 | DeepSeek-V4-Pro | DeepSeek | 80.60 | — | 55.40 | 免费商用 |
| 11 | Qwen3.7-Max-Preview | 阿里巴巴 | 80.40 | — | 60.60 | 闭源 |
| 12 | Claude Sonnet 4 | Anthropic | 80.20 | — | — | 闭源 |
| 13 | MiniMax M2.5 | MiniMax | 80.20 | — | 55.40 | 免费商用 |
| 14 | Kimi K2.6 | Moonshot | 80.20 | — | 58.60 | 免费商用 |
| 15 | GPT-5.2 | OpenAI | 80.00 | — | 55.60 | 闭源 |
[来源：https://www.datalearner.com/leaderboards/category/code]

#### 3.2 LMArena Coding Arena (Elo 排名)
1. Claude Fable 5 (1563)
2. Opus 4.7 (thinking) (1553)
3. Claude Opus 4.6 (thinking) (1551)
4. Opus 4.7 (1549)
5. Claude Opus 4.6 (1548)
9. GLM 5.1 (1529)
10. Claude Sonnet 4.6 (1527)
[来源：https://www.datalearner.com/leaderboards/category/code]

#### 3.3 DesignArena Code Category (Elo 排名)
1. GLM-5.2 (1360)
2. Claude Fable 5 (1350)
3. Claude Opus 4.6 (1341)
7. Kimi K2.6 (1328)
[来源：https://www.datalearner.com/leaderboards/category/code]

### 4. API 价格与套餐对比 (2026 年)

#### 4.1 国际模型 API 计费 (/1M tokens)
| 模型 | 输入 | 输出 | 上下文 |
| --- | --- | --- | --- |
| Claude Opus 4.6 | $5.00 | $25.00 | 1M |
| Claude Sonnet 4.6 | $3.00 | $15.00 | 200K |
| Claude Haiku 4.5 | $1.00 | $5.00 | 200K |
| GPT-5.5 | $1.75 | $14.00 | — |
| GPT-5 mini | $0.25 | $2.00 | — |
| Gemini 2.5 Pro | $1.25 | $5.00 | 2M |
| Gemini 3 Flash | $0.50 | $3.00 | 1M |
[来源：https://www.cnblogs.com/skyseraph/p/19966095] [来源：https://segmentfault.com/a/1190000047676047]

#### 4.2 国内模型 API 计费 (/1M tokens)
| 模型 | 输入 | 输出 | 上下文 |
| --- | --- | --- | --- |
| DeepSeek-V4-Flash | $0.14 | $0.28 | 1M |
| DeepSeek-V4-Pro（折扣） | $0.435 | $0.87 | 1M |
| DeepSeek-V4-Pro（原价） | ~$1.74 | ~$3.48 | 1M |
| Kimi K2.6 | $0.60 | $2.50 | 256K |
| GLM-5 | $1.00 | $0.20 | 200K |
| MiniMax-M2.5 | ~$0.30 | — | 200K |
| Qwen3.6-Plus | $0.36–$1.00 | $1.43–$4.01 | 262K |
[来源：https://www.cnblogs.com/skyseraph/p/19966095] [来源：https://segmentfault.com/a/1190000047676047]

#### 4.3 消费者订阅套餐对比
| 平台 | 免费档 | 入门付费 | 主力 | 旗舰 |
| --- | --- | --- | --- | --- |
| DeepSeek | ✅ 功能完整 | 无 | 无 | 无 |
| Kimi | ✅ 有限额 | — | ~$19/月 | 多档 |
| 智谱清言 | ✅ | — | 官网查看 | — |
| ChatGPT | ✅ | $8（Go） | $20（Plus） | $100–200（Pro） |
| Claude | ✅ | — | $20（Pro） | $100–200（Max） |
| Gemini | ✅ | $7.99 | $19.99 | $249.99 |
[来源：https://www.cnblogs.com/skyseraph/p/19966095]

### 5. 选型建议与工作流

#### 5.1 场景化选型
| 场景 | 首选 | 备选 |
| --- | --- | --- |
| 个人日常（国内，0 成本） | DeepSeek 免费 | Kimi 免费 |
| 个人日常（海外，$20） | Claude Pro | ChatGPT Plus |
| 超长文档分析 | Kimi 付费 | Gemini Pro |
| AI 编码代理 | Claude Max | DeepSeek API + Claude Code |
| 极致低成本 API | DeepSeek-V4-Flash | MiniMax-M2.5 |
| 研究/实时搜索 | Perplexity Pro | Kimi + 联网 |
| 企业级（国内合规） | 智谱 GLM 企业版 | DeepSeek API 私有化 |
[来源：https://www.cnblogs.com/skyseraph/p/19966095]

#### 5.2 推荐工作流
- **复杂架构、跨模块调试、安全敏感代码** → Claude Opus 4.7
- **快速编码、简单函数、日常 CRUD** → Claude Sonnet 4.6 / DeepSeek V4
- **需要操作软件、自动化流程** → GPT-5.5
- **国内项目、中文场景** → GLM 5.1 / Kimi 2.6 / DeepSeek V4
[来源：https://cloud.tencent.com/developer/article/2670420]

#### 5.3 一站式调用建议
五雄并起的副作用是 API 治理变复杂。每家都自定义了一套鉴权头、错误码、SDK 包名。OpenAI 兼容的 AI API 聚合平台（如 ofox.ai）的价值在于：一个 OpenAI 兼容的 endpoint，model 字段换名字就切换模型，结算合并到一张账单。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]

### 6. 风险与约束

#### 6.1 通用陷阱
- **"无限制"水分**：所有套餐都有隐性 Rate Limit，高峰期降速。建议实测高峰期响应再决定。
- **上下文窗口 ≠ 有效理解**：模型在超长文档的"中间遗忘"现象仍存在，实际可靠长度远低于技术上限。
- **年付退款风险**：通常不支持中途退款，模型迭代快，建议先月付观察 1-2 个月再年付。[来源：https://www.cnblogs.com/skyseraph/p/19966095]

#### 6.2 国内平台弊端
- **DeepSeek**：无订阅制，无多模态；高峰期服务器繁忙；对话历史同步弱。
- **Kimi**：免费额消耗快；付费档不透明需登录查看；长文档摘要偶发幻觉。
- **GLM**：消费端套餐模糊；API 价格偏高；中文开发环境适配有限。
[来源：https://www.cnblogs.com/skyseraph/p/19966095]

#### 6.3 海外平台弊端
- **ChatGPT Plus**：高峰期仍降速；对话记忆弱；国内需 FQ+ 境外支付。
- **Claude Pro**：有每日上限，重度用户易触顶。
- **Gemini Pro**：Ultra $249.99 定价过高；产品多次改名影响信任。
[来源：https://www.cnblogs.com/skyseraph/p/19966095]

#### 6.4 待验证问题
- **GLM-5.1 在长链路 Agent 任务上的稳定性**：跑分接近 Claude Opus 4.6 不等于在 1000 步的真实 workflow 里同样稳定。
- **Qwen3.6-Plus 1M 上下文的有效衰减点**：默认 1M 不等于 1M 全部可用，要看在 700K-900K 区间检索准确率掉多少。
- **DeepSeek V4 Preview 转 GA 的定价**：当前是 preview 价格，正式定价可能调整。
- **Kimi K2.6 Agent Swarm 的可观测性**：300 个子代理并行调度的状态追踪和失败回滚目前文档很薄。
[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]

## 推荐工作流

1.  **模型接入层**：使用兼容 OpenAI SDK 的聚合网关（如七牛云 AI 大模型推理服务、OfoxAI），统一 `base_url`，通过切换 `model` 参数实现多模型对比，无需为每家分别写 SDK 调用逻辑。[来源：https://segmentfault.com/a/1190000047676047]
2.  **开发阶段**：
    -   **原型设计**：使用 Claude Opus 4.7 或 GPT-5.5 进行架构设计和复杂逻辑推导。
    -   **日常编码**：使用 DeepSeek-V4-Flash 或 Claude Sonnet 4.6 进行快速代码生成和补全，降低成本。
    -   **代码审查**：使用 GLM-5.1 或 Qwen3.6 进行中文注释生成和本土化适配检查。
3.  **测试阶段**：
    -   使用 SWE-bench Verified 或 LiveCodeBench 基准测试集对候选模型进行小规模抽样测试。
    -   对于关键业务逻辑，使用 GPT-5.5 的电脑操控能力进行自动化流程验证。
4.  **部署阶段**：
    -   高并发场景优先路由至 DeepSeek-V4-Flash 或 MiniMax-M2.5。
    -   复杂推理场景路由至 Claude Opus 4.6 或 GLM-5.1。
    -   监控 Token 消耗量，设置阈值报警，避免隐性 Rate Limit 导致的服务中断。[来源：https://www.cnblogs.com/skyseraph/p/19966095] [来源：https://cloud.tencent.com/developer/article/2670420]

## 适用场景

1.  **企业级私有化部署**：适合采用 Qwen3.6-35B-A3B 或 Qwen3.6-27B（Apache 2.0 开源），或 GLM-5.1（MIT 开源），可在单台 80GB 卡或集群上运行，满足数据合规要求。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
2.  **高并发 API 服务**：适合采用 DeepSeek-V4-Flash 或 MiniMax-M2.5，成本极低（$0.14-$0.30/1M tokens），适合客服、文档处理、批量数据处理。[来源：https://www.cnblogs.com/skyseraph/p/19966095]
3.  **复杂 Agent 编排**：适合采用 Kimi K2.6（Agent Swarm）或 Claude Opus 4.6（Computer Use），适合需要多步骤自主交付的场景（研究/自动生成完整代码库）。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
4.  **超长文档分析**：适合采用 Kimi K2.6（2M 上下文）或 Gemini 2.5 Pro（2M 上下文），适合法律合同、学术论文、大型代码库分析。[来源：https://www.cnblogs.com/skyseraph/p/19966095]
5.  **国内合规项目**：适合采用智谱 GLM 企业版或 DeepSeek API 私有化，满足国内数据安全法规，网络稳定。[来源：https://www.cnblogs.com/skyseraph/p/19966095]

## 不适用场景

1.  **极致低成本且需多模态**：DeepSeek 无多模态能力，MiniMax 文字能力略弱于 DeepSeek/Kimi，若需同时满足低成本和高质量多模态，需组合使用。[来源：https://www.cnblogs.com/skyseraph/p/19966095]
2.  **重度依赖海外生态**：国产模型在 Google Workspace、GitHub 原生集成上不如 GPT/Claude，若工作流强依赖这些工具，首选海外模型。[来源：https://www.cnblogs.com/skyseraph/p/19966095]
3.  **预算极度敏感且需订阅制**：DeepSeek 无消费者订阅套餐，仅提供免费版和 API，若用户习惯月付订阅模式，需选择 Kimi 或 ChatGPT。[来源：https://www.cnblogs.com/skyseraph/p/19966095]
4.  **超大规模 Agent 集群本地部署**：Kimi K2.6 1T MoE 本地跑成本过高，除非有 H100 集群，否则不实际。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
5.  **对延迟极度敏感且需长上下文**：虽然 DeepSeek V4-Flash 延迟低，但在 1M 上下文下的首 token 延迟仍高于短上下文模型，需实测验证。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]

## 风险与约束

1.  **规格漂移风险**：模型迭代快（如 Qwen3.6 到 3.7，GLM-5 到 5.1），API 行为可能变化，需预留缓冲期进行回归测试。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026]
2.  **上下文有效衰减**：默认 1M 上下文不等于 1M 全部可用，在 700K-900K 区间检索准确率可能下降，需进行"中间遗忘"测试。[来源：https://ofox.ai/zh/blog/open-source-llm-china-roundup-2026] [来源：https://www.cnblogs.com/skyseraph/p/19966095]
3.  **隐性 Rate Limit**：所有套餐都有隐性 Rate Limit，高峰期降速，建议实测高峰期响应再决定，避免生产环境中断。[来源：https://www.cnblogs.com/skyseraph/p/19966095]
4.  **定价调整风险**：DeepSeek V4 Preview 当前是 preview 价格，正式定价可能调整；GLM-5.1 在云厂商上的价格可能波动。[来源：https://ofox.ai/zh/blog/open-source-ll