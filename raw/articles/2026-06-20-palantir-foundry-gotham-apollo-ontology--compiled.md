# Palantir Foundry Gotham Apollo 核心产品技术架构与本体论调研报告

## 核心结论

1.  **Palantir 核心架构由四大平台组成**：Foundry（商业企业操作系统）、Gotham（政府国防情报系统）、Apollo（持续交付与基础设施管理）、AIP（人工智能平台）。Foundry 与 Gotham 共享底层技术栈，但面向不同场景。[来源：https://www.smartcity.team/investment/companies/palantir] [来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf] **可信度：高**
2.  **Ontology（本体论）是核心语义层**：不同于传统数仓的表结构，Ontology 将数据抽象为业务对象（Objects）、关系（Links）、操作（Actions）和逻辑（Logic），实现数据与业务语义的统一，支持 AI 直接理解业务上下文。[来源：https://www.palantir.com/docs/zh/foundry/platform-overview/overview] [来源：https://techwhims.com/cn/posts/palantir-core-architecture] **可信度：高**
3.  **AIP 实现 AI 与操作的闭环**：AIP 不仅是聊天机器人，而是通过 Ontology 将 LLM 与业务操作绑定，支持"AI 提议 - 人类审批 - 自动执行"的工作流，解决传统 RAG 只能检索不能执行的问题。[来源：https://techwhims.com/cn/posts/palantir-core-architecture] [来源：https://www.palantir.com/docs/zh/foundry/platform-overview/overview] **可信度：高**
4.  **数据版本控制与时间回溯（Git for Data）**：平台支持数据集的版本化管理、分支合并及时间回溯（Time Travel），基于增量存储（Delta Storage）和列存压缩解决 TB/PB 级数据的冗余问题。[来源：https://www.53ai.com/news/Palantir/2025121217384.html] [来源：https://www.palantir.com/docs/zh/foundry/platform-overview/overview] **可信度：高**
5.  **细粒度安全与权限体系**：权限控制深入到对象、属性、实例及操作级别（Object/Attribute/Row/Action Level），支持基于策略的代码（Policy-as-Code）和动态评估，满足军工/政府级合规需求。[来源：https://www.53ai.com/news/Palantir/2025121217384.html] [来源：https://www.palantir.com/docs/zh/foundry/platform-overview/overview] **可信度：高**
6.  **FDE 交付模式构成护城河**：前线部署工程师（FDE）驻场客户现场，将定制解决方案转化为标准化产品模块，实现从“咨询服务”到“平台产品”的复利增长。[来源：https://www.smartcity.team/investment/companies/palantir] [来源：https://techwhims.com/cn/posts/palantir-core-architecture] **可信度：高**
7.  **技术栈基于开源与自研混合**：底层计算依赖 Spark/Flink，编排依赖 Kubernetes/Apollo，前端基于 TypeScript/React/WebGL，但核心 Ontology 引擎、对象存储及安全框架为自研。[来源：https://www.53ai.com/news/Palantir/2025121217384.html] [来源：https://www.modb.pro/db/1930804422725087232] **可信度：中**

## 内容整理

### 1. 核心产品架构体系

Palantir 的产品体系并非单一软件，而是由四个相互协作的平台组成的生态系统，覆盖从基础设施到 AI 应用的全栈能力。

| 平台 | 定位 | 核心用户 | 关键功能与特点 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| **Foundry** | 商业企业操作系统 | 能源、制造、金融、医疗、零售 | 基于本体论（Ontology）构建，支持数据集成、数字孪生、动态调度、低代码应用开发。旨在打破数据孤岛，协调复杂环境中的决策。 | [来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf] |
| **Gotham** | 政府与国防情报系统 | 情报机构、军队、安全部门 | 起源于反恐情报分析，支持跨源数据融合、实体关联分析、知识图谱推理。高安全管控，支持分级权限与审计追溯。 | [来源：https://techwhims.com/cn/posts/palantir-core-architecture] |
| **Apollo** | 持续交付与基础设施 | 所有平台底层底座 | 自动化软件安装、升级、监控和维护。支持公有云、私有云、边缘设备甚至断网环境（Air-gapped）的一致部署。 | [来源：https://www.smartcity.team/investment/companies/palantir] |
| **AIP** | 人工智能平台 | 所有平台用户 | 将大语言模型（LLM）安全整合到 Foundry/Gotham 中。包含 AIP Assist（助手）、AIP Logic（逻辑编排）、AIP Agent Studio（智能体创建）。 | [来源：https://www.palantir.com/docs/zh/foundry/platform-overview/overview] |

**架构演进逻辑**：
*   **初期（2008-2014）**：Gotham 为高度封闭、本地化部署的单体/模块化架构，依赖 Java/Scala + 关系数据库。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **中期（2014-2017）**：拆分服务化组件，2017 年 Rubix 项目用 Kubernetes 重构云基础设施。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **云原生过渡（2017 至今）**：Gotham 能力抽象融入 Foundry，Apollo 成熟支持多云迭代。Gotham 现为运行在 Foundry 栈上的垂直应用。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

### 2. Ontology（本体论）技术详解

Ontology 是 Palantir 的核心差异化技术，它不是简单的 Schema，而是运营层的数字孪生。

**核心要素**：
*   **对象类型（Object Types）**：语义对象类型（如 Order, Customer, Shipment）。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **属性类型（Property Types）**：基础类型 + 复杂类型（地理坐标、时间序列）。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **链接类型（Link Types）**：对象之间的关系（对称、非对称、多重关系）。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **操作类型（Action Types）**：可对对象执行的操作（原子操作、流程化操作），支持回写到业务系统。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **逻辑（Logic）**：业务规则、计算属性、验证逻辑、ML 模型、LLM 函数。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]

**架构分层**：
1.  **Language（建模语义）**：通过 SDK（OSDK）声明式描述业务语义模型。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
2.  **Engine（执行层）**：高规模 SQL 查询、实时状态变更订阅、原子事务更新、批量变更与流式处理、版本控制。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
3.  **Toolchain（开发与运维）**：自动生成 API 网关和多语言 SDK，CI/CD 版本管理。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]

**微服务拆解**：
*   **OMS（Ontology Metadata Service）**：元数据服务，管理对象类型、链接、操作的定义，相当于 Schema 注册中心。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **OSS（Object Set Service）**：读取服务，负责对象搜索、过滤、聚合、加载。支持 Static、Dynamic、Temporary、Permanent 四种对象集类型。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **Object Data Funnel**：写入流程，数据从源系统经 CDC 管道清洗映射后写入 Object Databases。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]

**与传统 MDM 差异**：
| 维度 | 传统 MDM (Informatica/Collibra) | Palantir Foundry Ontology | 来源 |
| :--- | :--- | :--- | :--- |
| 定位 | 数据治理工具（管好 Golden Record） | 业务语义层 + 应用开发基座 | [来源：https://www.53ai.com/news/Palantir/2025121217384.html] |
| 数据形态 | 以表/字段为核心 | 以对象/关系/动作为核心 | [来源：https://www.53ai.com/news/Palantir/2025121217384.html] |
| 集成模式 | ETL/ESB，先抽取清洗再写回 | Schema-on-Read，Ontology 映射到源数据 | [来源：https://www.53ai.com/news/Palantir/2025121217384.html] |
| 更新节奏 | 主数据版本更新较慢（季度/年度） | 动态、可实时更新（支持 Time Travel） | [来源：https://www.53ai.com/news/Palantir/2025121217384.html] |

### 3. 数据层设计与计算引擎

**数据接入与存储**：
*   **多源接入**：支持结构化（ERP、DB）、非结构化（PDF、图像）、实时流（IoT、Kafka）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **存储优化**：底层使用对象存储（S3 兼容）、列式存储（Parquet、ORC）。支持冷热分层、自动压缩、智能索引。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **Git for Data**：每次数据变更生成版本号，支持不可变快照、回滚、分支合并。底层实现类似 Delta Lake/Iceberg/Hudi，以“数据分块”方式存储差异。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **冗余解决**：采用增量存储（Delta Storage）、列存压缩、分区化、生命周期管理（Retention Policy）、冷热分层存储。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

**计算引擎**：
*   **分布式计算**：底层依赖 Apache Spark（批处理/机器学习）、Flink（流处理场景）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **优化策略**：分层/分级数据架构（冷热分层）、预计算与特征工程（物化视图）、增量计算与流式处理、分布式与并行计算。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **PB/TB 规模决策**：系统优先使用最新、关键样本数据推理，必要时调用全量数据回溯。支持事后通过 Time Travel 全量重算校正。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

### 4. 人工智能平台（AIP）

**战略定位**：
*   AIP 不是“聊天机器人”，而是**Actionable AI**，让模型能读、写、调用、执行。[来源：https://www.smartcity.team/investment/companies/palantir]
*   解决传统 RAG 局限：RAG 只解决知识获取，AIP 让 LLM 在治理框架内对真实业务对象提出操作建议。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]

**核心能力**：
*   **Tool Use with Guardrails**：每个 AI Agent 只能调用预授权的 Actions，受 RBAC 控制，所有操作留痕。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **RAG on Ontology**：检索增强生成直接基于 Ontology 对象图进行，而非原始文本块。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **Proposal 工作流**：AI 提议操作 -> 作为 Branch 存在 -> 人类审批 -> Merge 到主状态 -> 执行回写。借鉴 Git 分支思想。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **模型路由**：支持多模型路由（OpenAI, Anthropic, 自托管等），统一接口切换/比较。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]

**与竞品对比**：
| 维度 | Foundry (Palantir) | Databricks | Snowflake ML | SageMaker | 来源 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 训练能力 | 支持外部训练产物接入，非超大规模分布式训练平台 | 原生支持大规模 Spark/Flink 训练 | 内嵌 AutoML + 轻量模型训练 | 大规模分布式训练、GPU/TPU 调度 | [来源：https://www.53ai.com/news/Palantir/2025121217384.html] |
| 算法库 | 内置标准算子库，强调与 Ontology 绑定 | 广泛支持开源库，高度自由 | Snowpark ML API，功能相对有限 | 深度支持 TensorFlow/PyTorch 等 | [来源：https://www.53ai.com/news/Palantir/2025121217384.html] |
| 差异化 | 算法与 Ontology 强绑定，结果映射到业务对象 | 超大规模训练 & 数据湖原生 | 仓库内轻量 ML | 最强的 ML 工程平台 | [来源：https://www.53ai.com/news/Palantir/2025121217384.html] |

### 5. 安全与权限体系

**权限粒度**：
*   **源数据层**：传统的行/列/表权限。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **Ontology 层**：以业务对象为中心（Order, Customer）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **属性级别**：敏感字段可见/不可见/脱敏。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **实例级别**：Row-level Security，如“销售 A 只能看到自己负责区域的订单”。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **操作级别**：限制能否触发某个动作（如 cancelOrder）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

**技术实现**：
*   **Policy-as-Code**：权限规则写成可配置策略（JSON/YAML/DSL）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **动态评估**：基于用户角色、部门、地域、上下文条件动态评估。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **合规性**：内置对 GDPR、CCPA、HIPAA 等支持，自动触发数据过期删除，保留销毁记录。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

### 6. 交付与商业模式

**FDE 模式**：
*   **前线部署工程师（FDE）**：嵌入客户运营环境的工程师，住在客户现场，理解业务流程，基于 Ontology 定制开发。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **复利逻辑**：FDE 在客户现场解决具体问题，将重复痛点转化为标准化工具（如 Magritte, Contour, Workshop），最终汇聚成 Foundry 平台。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **训练营（Bootcamp）**：7 天极速 POC，将获客周期缩短 6-12 个月。[来源：https://www.smartcity.team/investment/companies/palantir]

**财务表现**：
*   **2023 年**：收入 22.25 亿美元，首次实现盈利，归母净利润 2.10 亿美元。政府业务约 55%，商业业务约 45%。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
*   **2024 年 Q2**：营收 10.04 亿美元，同比增长 48%。美国商业收入同比增长 93%。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **毛利率**：维持在 80% 左右（2023 年剔除股权激励后约 82%）。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]

## 推荐工作流

基于 Palantir 架构理念，企业构建类似数据平台的工作流建议如下：

1.  **语义层先行**：
    *   不要直接建表，先梳理核心业务对象（10-20 个对象类型），定义属性、关系及操作。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
    *   建立元数据服务（类似 OMS）与数据读取服务（类似 OSS）分离的架构。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
2.  **数据管道标准化**：
    *   构建语义 API 层，将常用查询封装为服务，业务方通过 API 获取数据比例超过 50%。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
    *   引入 CDC 实时同步，缩短 ETL 延迟至分钟级或秒级。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
3.  **AI 介入操作层**：
    *   设计"AI 建议 → 人工审批 → 自动执行”的闭环，AI 操作建议必须有审批环节。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
    *   操作日志完整保留，支持审计和回滚。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
4.  **版本控制治理**：
    *   对核心数据模型和 Ontology 变更引入分支和审批机制（Git for Data）。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
    *   支持时光回溯，保证分析结果的可验证性。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
5.  **组织配套**：
    *   数据团队派人深入业务一线（类似 FDE 模式），而非只在后方支持。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]

## 适用场景

1.  **高复杂度决策场景**：需要跨系统、跨部门数据融合，且决策链路长、风险高的场景（如供应链调度、金融风控、国防情报）。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
2.  **数据孤岛严重企业**：拥有多个遗留系统（ERP, CRM, LMS），语义不通，需要统一业务视图。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
3.  **强合规与安全需求**：政府、军工、金融等需要细粒度权限控制、审计追溯、数据驻留的场景。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
4.  **AI 落地操作层**：希望 AI 不仅提供洞察，还能直接驱动业务操作（如自动调拨库存、审批订单）的企业。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
5.  **动态数字孪生**：需要实时映射物理世界状态（如工厂设备、物流车辆），并进行模拟推演的场景。[来源：https://www.smartcity.team/investment/companies/palantir]

## 不适用场景

1.  **简单报表需求**：如果仅需静态 BI 报表，无需跨系统操作或复杂语义建模，引入 Ontology 可能过度工程。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
2.  **数据源单一且稳定**：若企业只有一个核心系统（如纯 SAP 环境）且无跨系统整合需求，传统数仓可能更经济。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
3.  **预算有限**：Palantir 模式年费数百万美元，且需要高阶工程师驻场，中小企业难以承受。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
4.  **纯算法研究**：若核心需求是大规模模型训练而非业务操作闭环，Databricks 或 SageMaker 可能更合适。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
5.  **业务逻辑极不稳定**：Ontology 建模需要一定稳定性，若业务对象定义每周剧烈变化，维护成本过高。[来源：https://www.smartcity.team/investment/companies/palantir]

## 风险与约束

1.  **过度工程风险**：不要“为了 Ontology 而 Ontology"，没有明确业务痛点不要盲目投入，Ontology 应该是演进的。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
2.  **权限与安全底线**：AI 介入操作必须有完善的权限控制，否则是灾难。需防止 AI 超权限调用。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
3.  **组织配套关键**：技术问题往往不是纯技术问题，需要 FDE 模式的组织配合，否则难以落地。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
4.  **供应商锁定**：客户一旦迁移到 Foundry/Gotham，退出成本极高（数据模型、工作流、治理体系）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
5.  **性能瓶颈**：浏览器端 3D 地图性能取决于 GPU 配置、数据处理和网络环境，需做好分层加载和抽稀。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
6.  **数据一致性**：跨系统写回需保证事务性，建立幂等键、重试与补偿策略，避免拖垮源系统。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
7.  **模型幻觉风险**：LLM 概率黑箱属性需通过 Policy Engine/审批环节拦截危险指令，确保可追溯、可验证。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

## 信源质量门控记录

### 门控规则
*   Tavily score < 0.4：剔除
*   已知低质域名：剔除
*   重复 URL：合并保留最高分结果
*   Exa 学术/语义结果：默认保留，但进入来源等级评估
*   C/D 级来源不得作为唯一结论依据
*   入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`

### 保留信源
1.  **Palantir 核心技术架构深度研究 - Tech Whims** (https://techwhims.com/cn/posts/palantir-core-architecture) - 来源等级：B → `source-quality: high` (与主题高度相关，技术细节丰富)
2.  **万字解读 Palantir 产品、技术和架构讨论 - 53AI** (https://www.53ai.com/news/Palantir/2025121217384.html) - 来源等级：B → `source-quality: high` (与主题高度相关，内容详尽)
3.  **Palantir - 全球大数据与 AI 领域市值最高的公司 - 53AI** (https://www.53ai.com/news/knowledgegraph/2025120478305.html) - 来源等级：C → `source-quality: medium` (相关性一般，需交叉验证，但提供了核心产品概览)
4.  **深度解析 Palantir - 中邮证券** (https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf) - 来源等级：C → `source-quality: medium` (金融研报，财务数据可靠，技术细节略少)
5.  **Palantir 产品体系深度解构 - 墨天轮** (https://www.modb.pro/db/1930804422725087232) - 来源等级：C → `source-quality: medium` (技术博客，架构拆解清晰)
6.  **一文全面解析 Palantir 产品以及其“本体论” - 智慧城市行业分析** (https://www.smartcity.team/investment/companies/palantir) - 来源等级：B → `source-quality: high` (与主题高度相关，涵盖本体论详解)
7.  **平台概览 - Palantir 官方文档** (https://www.palantir.com/docs/zh/foundry/platform-overview/overview) - 来源等级：A → `source-quality: high` (官方文档，技术定义最权威)
8.  **Concept-Centric Software Development - Arxiv** (https://arxiv.org/html/2304.14975) - 来源等级：A → `source-quality: high` (学术论文，Palantir 员工撰写)
9.  **Data Digitization in Manufacturing Factory Using Palantir Foundry Solution - MDPI** (https://www.mdpi.com/2227-9717/12/12/2816) - 来源等级：B → `source-quality: high` (学术论文，案例研究)
10. **A Brief Analysis of Palantir Gotham - IEEE** (https://ieeexplore.ieee.org/document/10808897) - 来源等级：A → `source-quality: high` (学术论文)

### 剔除信源
*   部分 Tavily 分数低于 0.4 的信源（如 France to ditch Palantir's AI data tools 等）。
*   重复 URL 已合并（如多个 53AI 相同文章链接）。
*   Source 5 (Arxiv PDF 2304.14975) 精读失败，正文为空，标记为不可验证，但保留 HTML 版本 Source 6。

## 来源与可信度

| 来源 | 类型 | 可信度 | 支撑内容 |
| :--- | :--- | :--- | :--- |
| **Palantir 官方文档** | 官方技术文档 | 高 | Ontology 定义、AIP 功能、平台组件、安全模型。 |
| **Tech Whims** | 行业技术分析 | 高 | 架构分层、OMS/OSS 微服务、AIP 工作流、FDE 模式。 |
| **53AI (万字解读)** | 行业深度分析 | 高 | 技术栈细节、Git for Data 实现、竞品对比、权限体系。 |
| **中邮证券研报** | 金融投资报告 | 中 | 财务数据、国防合同金额、发展历程、市场份额。 |
| **智慧城市行业分析** | 行业分析 | 高 | 本体论详解、四大平台定位、护城河分析。 |
| **Arxiv (Concept-Centric)** | 学术论文 | 高 | 软件开发方法论、概念设计理论。 |
| **墨天轮** | 技术博客 | 中 | 产品模块列表、架构分层图。 |

## 对于可信度较高的来源逐来源总结

### 1. Palantir 核心技术架构深度研究 - Tech Whims
*   **URL**: https://techwhims.com/cn/posts/palantir-core-architecture
*   **核心内容**: 详细解析了 Ontology 的三层架构（Language, Engine, Toolchain）和微服务拆解（OMS, OSS）。阐述了 AIP 如何通过 Proposal 工作流实现人机协同。对比了 Gotham、Foundry、Apollo 三大平台定位。
*   **可用事实**:
    *   Ontology 四要素：Data, Logic, Action, Security。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
    *   OMS 管理元数据，OSS 负责读取服务，支持 Static/Dynamic/Temporary/Permanent 对象集。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
    *   AIP 核心能力：Pipeline Builder, Scenario Primitive, Language Model Service, AI Agent。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
    *   FDE 模式：嵌入客户运营环境的工程师，住在客户现场。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **局限**: 部分底层实现细节（如存储引擎具体算法）未完全公开，依赖作者推断。
*   **适合入库知识点**: Ontology 架构分层、OMS/OSS 服务定义、AIP Proposal 工作流机制、FDE 交付模式细节。

### 2. 万字解读 Palantir 产品、技术和架构讨论 - 53AI
*   **URL**: https://www.53ai.com/news/Palantir/2025121217384.html
*   **核心内容**: 全方位拆解 Palantir 产品技术，包括数据层设计、Git for Data 范式、权限体系、技术栈（Spark/Flink/K8s）、与竞品（Databricks/Snowflake）对比。
*   **可用事实**:
    *   技术栈：前端 TypeScript/React，后端 K8s/Apollo/Spark/Flink，存储 S3/Parquet。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
    *   Git for Data 区别：存储对象为数据集（GB~TB），变更方式为数据块/分区差异，合并逻辑按数据粒度。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
    *   冗余解决：增量存储、列存压缩、分区化、生命周期管理、冷热分层。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
    *   权限体系：对象级、属性级、实例级、操作级控制，Policy-as-Code。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **局限**: 部分内容为作者观察观点，非官方白皮书，需与官方文档交叉验证。
*   **适合入库知识点**: 技术栈组件列表、Git for Data 实现细节、权限粒度定义、竞品对比表格。

### 3. 平台概览 - Palantir 官方文档
*   **URL**: https://www.palantir.com/docs/zh/foundry/platform-overview/overview
*   **核心内容**: 官方定义 Ontology、决策组件（数据、逻辑、操作）、平台能力（数据连接、模型、应用、安全）。
*   **可用事实**:
    *   Ontology 集成数据（对象和链接）、逻辑（模型和函数）、操作（平台操作）。[来源：https://www.palantir.com/docs/zh/foundry/platform-overview/overview]
    *   决策组件分解：数据（事实）、逻辑（规则/模型）、操作（动力学/效果）。[来源：https://www.palantir.com/docs/zh/foundry/platform-overview/overview]
    *   安全模型：所有数据加密、身份验证、授权控制（角色/标记/目的）、审计日志。[来源：https://www.palantir.com/docs/zh/foundry/platform-overview/overview]
*   **局限**: 偏向功能介绍，底层架构细节较少。
*   **适合入库知识点**: 官方术语定义、决策组件模型、安全合规标准、平台能力列表。

### 4. 深度解析 Palantir - 中邮证券
*   **URL**: https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf
*   **核心内容**: 财务数据分析、国防业务合同详情、发展历程、核心能力专利分析。
*   **可用事实**:
    *   2023 年收入 22.25 亿美元，政府业务 55%，商业业务 45%。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
    *   2023 年归母净利润 2.10 亿美元，首次盈利。[来源：https://pdf.dfcfw.com/pdf/H3_AP20250