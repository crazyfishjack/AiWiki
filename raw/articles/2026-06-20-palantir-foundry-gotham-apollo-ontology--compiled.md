# Palantir Foundry Gotham Apollo Ontology 语义建模与核心产品技术架构调研报告

## 核心结论

1.  **Palantir 核心架构由四大平台构成**：Gotham（政府/国防）、Foundry（商业企业）、Apollo（持续交付/部署）、AIP（人工智能平台）。Foundry 基于本体论（Ontology）构建企业操作系统，Gotham 侧重情报分析，Apollo 实现“一次构建，随处部署”，AIP 将大模型与本体数据深度融合。[来源：https://techwhims.com/cn/posts/palantir-core-architecture] [来源：https://lygw.ai/blog/20250818-palantir-tech-report] **可信度：高**
2.  **Ontology 是核心差异化壁垒**：Ontology 不仅是数据模型，而是连接数据、业务逻辑和操作行为的“数字孪生”语义层。它定义了 Object Types（对象类型）、Link Types（链接类型）、Action Types（动作类型）和 Logic（逻辑），实现了从“看数据”到“操作数据”的转变。[来源：https://techwhims.com/cn/posts/palantir-core-architecture] [来源：https://www.smartcity.team/investment/companies/palantir] **可信度：高**
3.  **技术栈深度集成开源与自研**：前端基于 TypeScript/React/WebGL，后端基于 Kubernetes/Apollo/Spark/Flink，存储支持 S3/Parquet/对象数据库。安全体系实现行级、列级、对象级细粒度权限控制，支持 Git for Data 版本管理。[来源：https://www.53ai.com/news/Palantir/2025121217384.html] [来源：https://lygw.ai/blog/20250818-palantir-tech-report] **可信度：高**
4.  **商业模式为“产品 + 咨询”混合**：通过 FDE（前线部署工程师）驻场模式深入客户业务，将定制解决方案转化为标准化产品模块。2024 年营收约 28.66-29 亿美元，政府与商业业务占比约为 55%:45%。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf] [来源：https://www.smartcity.team/investment/companies/palantir] **可信度：中**
5.  **AIP 驱动新一轮增长**：AIP（AI Platform）通过 AIP Logic、AIP Assist、AIP Agent Studio 等模块，将 LLM 能力嵌入 Foundry/Gotham 工作流，解决 AI 落地中的数据准备和上下文理解问题。2025 年 Q2 美国商业收入同比增长 93%。[来源：https://www.smartcity.team/investment/companies/palantir] [来源：https://lygw.ai/blog/20250818-palantir-tech-report] **可信度：高**
6.  **与传统数据平台存在本质差异**：相比 Databricks/Snowflake 侧重数据计算与存储，Palantir 侧重端到端决策执行与业务语义映射；相比 SAP/Oracle 侧重流程固化，Palantir 侧重数据驱动的动态本体建模。[来源：https://www.53ai.com/news/Palantir/2025121217384.html] [来源：https://lygw.ai/blog/20250818-palantir-tech-report] **可信度：高**

## 内容整理

### 1. 产品体系与核心平台架构

Palantir 的产品体系并非单一软件，而是由四个核心平台组成的协同生态系统，各自定位明确但底层技术互通。

#### 1.1 四大核心平台定位

| 平台名称 | 定位 | 核心用户 | 特点与功能 |
| :--- | :--- | :--- | :--- |
| **Gotham** | 政府与国防操作系统 | 情报机构、军队、安全部门 | 高敏感数据处理、跨机构协同、实时态势感知、实体关联分析、知识图谱推理。[来源：https://techwhims.com/cn/posts/palantir-core-architecture] |
| **Foundry** | 商业企业操作系统 | 能源、制造、金融、医疗、零售 | 运营决策平台、数据管道构建、Ontology 驱动的业务应用、数字孪生、动态调度。[来源：https://techwhims.com/cn/posts/palantir-core-architecture] |
| **Apollo** | 基础底座/持续交付 | 上述所有平台 | 持续交付与自动化运维，支撑平台本身的迭代更新，实现“一次构建，随处部署”（公有云、私有云、边缘、断网环境）。[来源：https://techwhims.com/cn/posts/palantir-core-architecture] |
| **AIP** | 人工智能平台 | 所有平台用户 | 接入 OpenAI 等大语言模型，在应用中使用 AI 实现代理和自动化，包含 AIP Assist、AIP Logic、AIP Agent Studio。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf] |

*   **Gotham 演进**：诞生于 2003 年，最初用于反恐情报分析。早期架构为高度封闭、本地化部署的单体/模块化架构（Java/Scala + 关系数据库）。2017 年后通过 Rubix 项目重构为云原生，现运行在 Foundry 栈上作为垂直应用（Government Vertical）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **Foundry 演进**：2016 年正式推出，将 Gotham 的能力向商业企业输出。关键演进是 Ontology 原生、自服务数据管道、行业模板、更友好的 UX。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **Apollo 功能**：自动化部署、产品和环境约束解决、高级升级策略、安全回收、配置管理、主动监测和警报、合规性和可审计性。支持在任意 Kubernetes 环境运行。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]

#### 1.2 技术架构分层

Palantir 的产品架构可视为从底层基础设施管理，到中间的数据整合与本体构建，再到上层的分析、应用开发和 AI 集成的完整体系。

1.  **基础设施与部署层 (Infrastructure & Deployment Layer)**
    *   **核心代表**：Palantir Apollo。
    *   **功能**：自动化软件安装、升级、监控和维护，确保跨不同环境（公有云、私有云、混合云、边缘设备、离线环境）的一致性和弹性。
    *   **底层服务网格**：由 Apollo 强制执行的一组软件定义原则，确保平台内数百项服务的可用性、冗余和可扩展性。[来源：https://www.modb.pro/db/1930804422725087232]
2.  **数据整合与本体层 (Data Integration & Ontology Layer)**
    *   **核心能力**：Foundry 和 Gotham 的基础能力。
    *   **组件**：数据连接器（200+ 即用型）、数据管道与转换引擎（Spark/Flink/自研）、本体构建工具（定义 Object Types, Action Types, Logic）。
    *   **功能**：连接、摄取、转换和整合异构数据源。构建“本体 (Ontology)"，即现实世界实体及其相互关系的数字表示，为数据赋予业务含义和上下文。[来源：https://www.modb.pro/db/1930804422725087232]
3.  **数据分析与应用开发层 (Data Analysis & Application Development Layer)**
    *   **核心平台**：Palantir Foundry, Palantir Gotham。
    *   **Foundry 组件**：分析工具（可视化、代码工作簿）、应用构建器（Workshop, Slate）、模型集成与开发。
    *   **Gotham 组件**：链接分析、地理空间可视化与分析、时间轴分析、协作工具。
    *   **功能**：在整合和理解数据的基础上，提供强大的分析工具、应用构建能力和人工智能集成，支持决策制定。[来源：https://www.modb.pro/db/1930804422725087232]
4.  **人工智能集成层 (Artificial Intelligence Platform - AIP Layer)**
    *   **组件**：AIP Logic（编排 LLM 和本体数据）、AIP Assist（嵌入 AI 助手）、安全与治理工具。
    *   **功能**：将大型语言模型 (LLM) 和其他人工智能能力安全、负责任地集成到核心平台及其构建的应用中。[来源：https://www.modb.pro/db/1930804422725087232]
5.  **安全与治理层 (Security & Governance Layer)**
    *   **贯穿所有层次**：细粒度访问控制、数据血缘与溯源、审计日志、加密、合规性工具。
    *   **功能**：确保数据在整个生命周期中的安全性、隐私保护和合规性。[来源：https://www.modb.pro/db/1930804422725087232]

### 2. Ontology（本体论）技术深度解析

Ontology 是 Palantir 技术的核心，远不止是一个数据模型或数据库模式。

#### 2.1 核心理念与定义
*   **定义**：Ontology 是将一个组织的真实世界（关键实体、属性、复杂关系）进行数字化、语义化的表达，构建组织的“数字孪生”。它是连接底层分散数据和上层业务操作的语义中枢。[来源：https://lygw.ai/blog/20250818-palantir-tech-report]
*   **与传统数仓的区别**：传统数仓建模逻辑是“表（Table）”，描述数据结构；Ontology 描述可操作的业务对象（名词和动词一起建模）。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **四要素集成**：
    *   **Data**：从异构数据源统一抽象为 objects/properties/links。
    *   **Logic**：业务规则、ML 模型、LLM 函数、多步编排统一在 Ontology 内定义。
    *   **Action**：从简单属性更新到复杂多步事务，变更可实时回写到运营系统。
    *   **Security**：行级、列级权限控制，AI agent 继承人类权限或项目权限。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]

#### 2.2 三层结构设计
根据深度分析，Palantir 的本体可以理解为三个层次的结合：
1.  **语义层 (Semantic Layer)**：定义世界。回答“在我们的业务世界里，哪些事物是重要的？”。定义业务的概念模型（如统一为"Person"实体），为整个组织提供共享的、无歧义的业务语言。[来源：https://lygw.ai/blog/20250818-palantir-tech-report]
2.  **动力学层 (Kinetic Layer)**：连接现实。通过数据管道（ETL/ELT）将来自 SQL 数据库、CSV 文件、实时 API 等各种数据源的原始数据，映射到语义层定义的实体和关系上。为本体注入生命。[来源：https://lygw.ai/blog/20250818-palantir-tech-report]
3.  **动态层 (Dynamic Layer)**：赋予行为。包含业务规则、访问控制策略、工作流和生命周期管理。确保本体不仅仅是一个静态模型，而是一个能够主动执行业务逻辑的“活系统”。[来源：https://lygw.ai/blog/20250818-palantir-tech-report]

#### 2.3 核心组件与微服务架构
Palantir 官方文档将 Ontology 架构分为三个层次，并拆解为微服务：
*   **Language（建模语义）**：定义 Object Types, Property Types, Link Types, Action Types, Logic。通过 SDK（OSDK）声明式描述。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **Engine（执行层）**：负责高性能执行。包含高规模 SQL 查询、实时状态变更订阅、原子事务更新、批量变更与流式处理、版本控制。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **Toolchain（开发与运维）**：OSDK 自动生成 API 网关和多语言 SDK，DevOps 工具链，IDE 集成。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **OMS (Ontology Metadata Service)**：Ontology 的“元数据服务”，管理 Object Types 的元数据、Link Types 定义、Action Types 定义。理解为 Ontology 的"schema 注册中心”。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **OSS (Object Set Service)**：Ontology 的“读取服务”，负责对象的搜索与过滤、聚合计算、对象加载、对象集的动态维护（Static, Dynamic, Temporary, Permanent）。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **Object Data Funnel**：写入流程编排。数据从源系统通过 CDC 管道进入，经过清洗、转换、映射到 Ontology 对象模型，写入 Object Databases。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]

#### 2.4 跨系统 Ontology 示例
以“订单（Order）”为例：
*   **业务对象**：Order（来自 ERP）、Shipment（来自 TMS）、Inventory（来自 WMS）、Sensor（来自 IoT）、Customer（来自 CRM）。
*   **关系**：Order → Shipment（部分发货）、Order → Inventory（判断可发货）、Shipment → Sensor（实时监控）、Order → Customer（信用风险控制）。
*   **版本化 & Time Travel**：订单状态变化在 Ontology 里都有版本号，可回溯历史状态。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

### 3. 技术栈与实现细节

#### 3.1 前端技术栈
*   **框架与语言**：TypeScript + React（主要 UI 框架），GraphQL / REST（数据查询和交互）。
*   **可视化与地图**：WebGL（浏览器端渲染引擎），MapboxGL（地图与 3D 场景渲染），D3.js / Highcharts（常规 BI 可视化）。
*   **交互体验**：浏览器端低代码工具（App Builder、Workshop），封装了 React + 内部 DSL。多人协作机制类似 Google Docs。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **3D 地图性能**：依赖浏览器端 WebGL。后端提前做好“切片、抽稀、聚合”，前端拿到可视化友好结果。对大数据场景提供分层加载。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

#### 3.2 后端技术栈
*   **运行与调度**：Kubernetes（统一容器编排平台），Apollo（自研持续交付与多云部署系统）。
*   **数据存储与处理**：分布式存储（S3 兼容、Parquet、ORC），关系数据库（Postgres、Oracle），分布式计算引擎（Apache Spark 批处理/机器学习，Flink 流处理），Graph 数据存储（自研或基于分布式 KV）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **数据治理与权限**：内置 RBAC/ABAC 模型，支持行/列/单元格级别权限。血缘追踪和审计日志存储（Kafka + ElasticSearch 或自研管道）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **Rubix 项目**：2017 年启动，将云架构从 Apache YARN 迁移到以 Kubernetes 为核心的统一基础设施基板。利用 Kubernetes 容器化技术和 Pod 安全上下文提供更强安全保障，实现计算资源动态伸缩。[来源：https://lygw.ai/blog/20250818-palantir-tech-report]

#### 3.3 AI/数据科学集成
*   **工作台**：Code Workbooks 支持 Python、R、SQL，直接运行在 Spark 集群或容器沙箱里。集成 scikit-learn、TensorFlow、PyTorch 等。
*   **模型管理**：内置 MLOps 模块，支持版本控制、实验追踪、模型部署。与外部 MLflow、SageMaker 有对接能力。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **AIP 组件**：
    *   **AIP Logic**：无代码/低代码开发环境，编排 LLM 和本体数据。
    *   **AIP Agent Studio**：创建和部署 AI 代理。
    *   **AIP Evals**：系统性测试、评估和比较 LLM 支持的工作流。[来源：https://lygw.ai/blog/20250818-palantir-tech-report]
    *   **AIP Threads**：通用生产力工具，利用 LLM 帮助完成任务（测试阶段）。[来源：https://www.modb.pro/db/1930804422725087232]

#### 3.4 安全与权限体系
*   **细粒度控制**：分为源数据层、Ontology 层、属性级别、实例级别（Row-level Security）、操作级别。
*   **技术实现**：Policy-as-Code（策略引擎），语义绑定（权限绑定在 Ontology 对象），动态评估（基于上下文），遮罩/变形（脱敏）。
*   **对比传统权限**：传统数据库权限绑定在表结构上；Foundry Ontology 权限绑定在业务对象及关系上，支持操作权限（如 cancelOrder），跨系统一致性，精细审计。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **零信任架构**：默认不信任网络内部或外部的任何人、设备或系统，必须对每一次访问请求进行验证。[来源：https://lygw.ai/blog/20250818-palantir-tech-report]

### 4. 核心功能模块详解

#### 4.1 数据连接与集成
*   **Pipeline Builder**：构建数据集成管道，将原始数据源转换为干净输出。步骤：输入、转换、预览、交付、输出。支持无代码转换。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
*   **HyperAuto V2/V1**：便捷、迅速、开放的数据集成，可在数小时内解锁复杂数据资产。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
*   **数据血缘 (Data Lineage)**：自动记录和追踪每一份数据从源头到最终应用的完整路径。支持影响分析、问题排查、合规审计、安全传播。[来源：https://lygw.ai/blog/20250818-palantir-tech-report]
*   **实体解析 (Entity Resolution)**：智能识别、匹配和链接指向同一实体的记录，创建统一“黄金记录”。[来源：https://lygw.ai/blog/20250818-palantir-tech-report]

#### 4.2 本体管理模块
*   **Ontology Manager**：构建和管理组织本体。
*   **Object Explorer**：对象集搜索分析。
*   **Object Monitors**：对象监视器。
*   **Vertex**：基于 Ontology 中定义的实体做业务化呈现，把多个有关系的实体进行串联，用业务流程的思路进行展现。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **Foundry Rules**：创建规则并应用于数据集、Objects 和时间序列，支持警报生成或数据分类。[来源：https://www.modb.pro/db/1930804422725087232]

#### 4.3 分析模块
*   **Contour**：点击式用户界面，用于在大规模表格上执行数据分析。[来源：https://www.modb.pro/db/1930804422725087232]
*   **Quiver**：分析和仪表盘套件，搜索和可视化时间序列和 Object 数据，搭建和发布到参数化的交互式仪表盘。[来源：https://www.modb.pro/db/1930804422725087232]
*   **Code Workbook**：高级版 notebook，支持 Python/R/SQL。[来源：https://www.modb.pro/db/1930804422725087232]
*   **Code Workspaces**：将 JupyterLab®、RStudio® Workbench 和 VS Code 第三方 IDE 引入 Palantir Foundry。[来源：https://www.modb.pro/db/1930804422725087232]
*   **Fusion**：电子表格应用程序（处于稳定状态，不再更新）。[来源：https://www.modb.pro/db/1930804422725087232]

#### 4.4 应用开发模块
*   **Workshop**：使应用构建者能够为操作用户创建互动且高质量的应用程序。[来源：https://www.modb.pro/db/1930804422725087232]
*   **Slate**：通过拖放界面构建具有自定义设计的动态和响应式应用。[来源：https://www.modb.pro/db/1930804422725087232]
*   **Automate**：自动化应用程序，允许用户定义条件和效果。[来源：https://www.modb.pro/db/1930804422725087232]
*   **Carbon**：为需要执行关键操作工作流的非技术用户提供专注的体验。[来源：https://www.modb.pro/db/1930804422725087232]

#### 4.5 其他核心能力
*   **Digital Twin（数字孪生）**：通过数字模型对现实世界的物理实体或系统进行实时模拟和分析。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
*   **Dynamic Scheduling（动态调度）**：将现实世界复杂性转化为实时的适应性，自动触发下游操作系统。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
*   **Edge AI（边缘人工智能）**：跨环境对传感器群进行现代化改造，在传感器运行的任何地方训练、管理和部署 AI 模型。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
*   **Git for Data**：支持时光回溯、回滚、分支与合并。基于数据分块的方式存储差异（类似 Delta Lake / Iceberg / Hudi）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

### 5. 行业对标与竞争分析

#### 5.1 与传统 MDM 的差异

| 维度 | 传统 MDM（Informatica / Collibra） | Palantir Foundry Ontology |
| :--- | :--- | :--- |
| 定位 | 数据治理工具（管好 Golden Record、标准化主数据） | 业务语义层 + 应用开发基座（建模、可视化、工作流） |
| 数据形态 | 以 表/字段 为核心（Customer 表，Product 表） | 以 对象/关系/动作 为核心（Customer→下单→Order） |
| 集成模式 | ETL/ESB，先抽取清洗再写回 MDM | Schema-on-Read，Ontology 映射到源数据，避免复制 |
| 使用人群 | 数据治理/IT 部门（负责全局主数据） | 一线业务/开发（在 Ontology 上直接构建应用） |
| 更新节奏 | 主数据版本更新较慢（季度/年度） | 动态、可实时更新（支持 Time Travel 和差异对比） |
| 产出 | 干净的数据资产 | 可直接驱动应用的业务模型、图谱、工作流、权限 |
| 扩展性 | 偏治理、目录化 | 内置 DSL，低代码/无代码开发，直接跑应用 |
[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

#### 5.2 与 Databricks/Snowflake/SageMaker 的算法能力对比

| 维度 | Foundry | Databricks | Snowflake ML | SageMaker |
| :--- | :--- | :--- | :--- | :--- |
| 训练能力 | 支持外部训练产物接入，本地也可跑常见 Python ML，不是超大规模分布式训练平台 | 原生支持大规模 Spark/Flink 训练，MLflow 实验管理 | 内嵌 AutoML + 轻量模型训练，偏中小规模场景 | 大规模分布式训练、GPU/TPU 调度、自动超参优化 |
| 算法库 | 内置标准算子库，可扩展；强调“与 Ontology 绑定” | 广泛支持开源库，高度自由 | Snowpark ML API，功能相对有限 | 深度支持 TensorFlow、PyTorch、Hugging Face 等框架 |
| 工作流编排 | 算法即节点，可组成 DAG，直接作用于业务对象 | Pipelines + MLflow 实验管理，面向数据科学团队 | SQL/Python 调用，简化工作流 | Step Functions + SageMaker Pipelines，面向 MLOps 工程师 |
| 模型部署 | 模型作为服务封装到 Foundry 内部，直接挂载到业务应用 | 部署到 Databricks Serving 或外部 API | 模型可转化为 SQL UDF/表函数 | 最完善的在线/批量推理服务 |
| 差异化 | 算法与 Ontology 强绑定：结果直接映射到“订单、车辆、库存”等对象 → 更偏应用集成 | 超大规模训练 & 数据湖原生 → 更偏数据科学研究与实验 | 仓库内轻量 ML → 更偏 SQL 用户与数据分析师 | 最强的 ML 工程平台 → 适合全栈 ML/AI 团队 |
[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

#### 5.3 主要竞争对手分析
*   **Databricks**：擅长数据仓库/湖和模型训练等计算任务，覆盖超过 60% 的财富 500 强企业。由客户和合作伙伴自主解决业务问题，不提供端到端的交付能力。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **Snowflake**：专注于云数据仓库和数据处理，主要面向商业客户，缺乏 Palantir 在政府和高安全性领域的深度渗透。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **C3.ai**：专注于企业级 AI 部署，目标客户包括国防和企业领域，更侧重于 AI 模型和工具服务，而非深度行业定制。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **SAP/Oracle**：以流程/事务边界来组织数据。Palantir 的 Ontology 强调“把数据、模型、对象、动作”映射到统一的业务语义层。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

### 6. 财务表现与商业模式

#### 6.1 财务数据
*   **2023 年**：收入 22.25 亿美元，同比增长 17%。政府业务 12.22 亿美元（55%），商业业务 10.03 亿美元（45%）。首次实现盈利，归母净利润 2.10 亿美元。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
*   **2024 年**：营收 28.66 亿美元（另有来源称 29 亿美元），同比增长 28.79%。政府业务 15.70 亿美元，商业业务 12.96 亿美元。净利润 4.62 亿美元，同比增长 120.27%。毛利率 80.25%。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
*   **2025 年 Q2**：营收 10.04 亿美元，同比增长 48%。美国商业收入 3.06 亿美元，同比增长 93%。美国政府收入 4.26 亿美元，同比增长 53%。GAAP 净利润率 33%。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **客户总数**：截至 2024 年 12 月 31 日，客户总数达到 711 家。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]

#### 6.2 商业模式
*   **收入模式**：订阅制、项目制、混合。通过销售订阅服务（Palantir Cloud）和软件许可（On-Premises Software），以及专业服务（O&M、培训、建模支持）。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
*   **FDE 模式**：前线部署工程师（Forward Deployed Engineers）驻场，每周 3-4 天在客户现场。深度解决业务问题，将定制解决方案转化为标准化产品模块。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **AIP 训练营**：2023 年推出，使公司能够在几天内根据实际客户数据提供真实的工作流程，加速客户获取。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
*   **价值分享**：Palantir 可以通过帮助客户降本增效来进行成果分成，获得远超传统软件许可证的回报。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

### 7. 典型应用案例

*   **美国陆军**：2019 年签订 4.58 亿美元生产协议支持陆军 Vantage。2024 年 12 月签订四年 4.01 亿美元合同，最高上限可达 6.19 亿美元。Vantage 集成了来自 160 多个不同系统的 30000 多个独特数据集。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
*   **空中客车 (Airbus)**：Foundry 平台集成了 7 个以上 ERP 数据源，生成组织价值链的数字孪生。A350 机型产能提升 33%（另有来源称 4 倍速增长）。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf] [来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **Swiss Re (瑞士再保险)**：通过实施 Palantir Foundry，实现了 170% 的年化投资回报率（ROI），投资回收期仅为 7.3 个月。报告时间减少了 70-80%。[来源：https://lygw.ai/blog/20250818-palantir-tech-report]
*   **英国国防部 (MOD)**：2022 年达成协议，价值 7500 万英镑，为期三年，支持数字化转型。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
*   **NHS (英国国家医疗服务体系)**：2023 年签订为期七年、价值 3.3 亿英镑的合同，构建下一代数据平台。[来源：https://lygw.ai/blog/20250818-palantir-tech-report]

### 8. 对大数据架构师的启示与行动建议

#### 8.1 核心认知
*   Palantir 的 Ontology 并不是一个新的“数据库”或“数据中台”，它本质上是一套“业务语义操作系统”。
*   数据不只是被查询的对象，而是可以被操作的主体。
*   AI 不只是回答问题，而是可以提出操作建议。
*   变更不只是修改，而是可追溯、可审查、可回滚的治理对象。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]

#### 8.2 行动建议
| 阶段 | 行动 | 衡量标准 |
| :--- | :--- | :--- |
| **短期（1-3 个月）** | 梳理核心业务对象，识别关键实体及其关系 | 产出核心 Ontology 草图（10-20 个对象类型） |
| **中期（3-6 个月）** | 构建语义 API 层，将常用查询封装为服务 | 业务方通过 API 获取