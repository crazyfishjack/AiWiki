# 调研报告：Palantir Foundry Gotham Apollo ontology 语义建模 核心产品技术架构 企业数据平台 金融风控政府情报 Spark Elasticsearch 行业对标

## 核心结论

1.  **Ontology 是 Palantir 的核心技术护城河，而非单纯的知识图谱。** 它将数据、逻辑、操作、安全统一建模，形成运营层的数字孪生，支持 AI 在治理框架内直接提出操作建议并回写业务系统。[来源：https://techwhims.com/cn/posts/palantir-core-architecture] [来源：https://www.53ai.com/news/Palantir/2025121217384.html] **可信度：高**
2.  **Palantir 采用“产品 + 咨询”混合模式（FDE 模式），前线部署工程师驻场解决业务问题，将定制解决方案提炼为标准化工具，实现从定制服务到平台化产品的复利增长。** [来源：https://www.smartcity.team/investment/companies/palantir] [来源：https://www.53ai.com/news/Palantir/2025121217384.html] **可信度：高**
3.  **四大平台分工明确：Gotham 服务于政府国防，Foundry 服务于商业企业，Apollo 为底层持续交付底座，AIP 为 AI 驱动层。** 2024 年营收 28.66 亿美元，同比增长 28.79%，其中政府业务占 55%，商业业务占 45%。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf] [来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf] **可信度：高**
4.  **数据版本控制（Git for Data）与细粒度权限控制是架构关键。** 支持时光回溯、回滚、分支与合并，权限可达对象 - 属性 - 操作级别，满足军工/政府高安全需求。[来源：https://techwhims.com/cn/posts/palantir-core-architecture] [来源：https://www.53ai.com/news/Palantir/2025121217384.html] **可信度：高**
5.  **AIP 将大模型与 Ontology 深度融合，解决 AI 落地“最后一公里”。** AI 不只检索信息，而是在治理框架内对真实业务对象提出操作建议，经过人工审批后回写到业务系统。[来源：https://techwhims.com/cn/posts/palantir-core-architecture] [来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf] **可信度：高**
6.  **高客户粘性与转换成本。** 客户数据经过 Palantir 平台归一化处理后深度融入本体架构，迁移意味着业务逻辑和数字资产作废，净收入留存率（NRR）约为 120%。[来源：https://www.smartcity.team/investment/companies/palantir] **可信度：中**
7.  **技术架构基于云原生与分布式计算。** 前端 TypeScript/React，后端 Kubernetes + Apollo + Spark/Flink，支持混合云/多云/边缘部署。[来源：https://www.53ai.com/news/Palantir/2025121217384.html] [来源：https://www.modb.pro/db/1930804422725087232] **可信度：高**

## 内容整理

### 1. 公司发展历程与 Overview

*   **创立背景：** Palantir 成立于 2003 年，由 Peter Thiel、Alex Karp 等创立。2005 年获得 CIA 旗下风投基金 In-Q-Tel 首轮投资。早期专注于为美国国防与情报部门提供反恐数据分析服务。[来源：https://www.smartcity.team/investment/companies/palantir] [来源：https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf]
*   **发展阶段：**
    *   **政务业务奠基期 (2003-2010)：** 2008 年推出 Gotham 平台。2005-2008 年，CIA 是唯一大客户。[来源：https://www.smartcity.team/investment/companies/palantir] [来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
    *   **商业业务起步期 (2011-2016)：** 2010 年摩根大通成为首位商业客户。2014-2015 年与 BP、空客合作。[来源：https://www.smartcity.team/investment/companies/palantir]
    *   **商业平台规模化期 (2016-2022)：** 2016 年推出 Foundry 平台。2020 年 9 月纽交所直接上市。2018 年推出 Apollo 平台。[来源：https://www.smartcity.team/investment/companies/palantir]
    *   **AI 驱动增长期 (2023-至今)：** 2023 年 4 月推出 AIP 平台。2023 年首次实现盈利，归母净利润 2.10 亿美元。2024 年纳入标普 500 指数。[来源：https://www.smartcity.team/investment/companies/palantir] [来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
*   **财务表现：**
    *   2023 年收入 22.25 亿美元，近两年收入保持 20% 左右增速。政府业务贡献约 55% 营收，商业业务贡献约 45% 营收。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
    *   2024 年营收 28.66 亿美元，同比增长 28.79%。其中政府业务 15.70 亿美元，商业业务 12.96 亿美元。2024 年毛利率 80.25%，净利率 16.33%。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
    *   2025 年 Q2 营收 10.04 亿美元，同比增长 48%。美国商业收入 3.06 亿美元，同比增长 93%。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **客户分布：** 截至 2024 年 12 月 31 日，客户总数 711 家。软件在全球约 90 个行业中应用。2024 年 66% 收入来自美国客户。[来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf] [来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]

### 2. 核心产品体系架构

Palantir 构建了四大核心产品平台，形成从底层部署、中层数据融合到上层 AI 应用的全栈能力。[来源：https://www.smartcity.team/investment/companies/palantir]

| 平台 | 定位 | 核心用户 | 特点 |
| --- | --- | --- | --- |
| **Gotham** | 政府与国防 | 情报机构、军队、安全部门 | 高敏感数据处理、跨机构协同、实时态势感知 |
| **Foundry** | 商业企业 | 能源、制造、金融、医疗、零售 | 运营决策平台、数据管道构建、Ontology 驱动的业务应用 |
| **Apollo** | 基础底座 | 上述所有平台 | 持续交付与自动化运维，支撑平台本身的迭代更新 |
| **AIP** | AI 驱动层 | 所有平台用户 | 接入大语言模型，在应用中使用 AI 实现代理和自动化 |

[来源：https://techwhims.com/cn/posts/palantir-core-architecture] [来源：https://www.smartcity.team/investment/companies/palantir]

#### 2.1 Gotham 平台
*   **定位：** 用于生成全球决策的操作系统，服务于政府和国防。使用户能够识别出隐藏在从信号情报源到机密线人报告等数据集深处的关键信息。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
*   **核心功能：** 武器管理系统；提供从太空到地面的决策优势；统筹战斗力使用；人工智能驱动战斗优势。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
*   **特点：**
    1.  增强杀伤链：“瞄准”产品支持战士使用 AI 增强杀伤链，无缝可信地匹配识别目标与杀伤目标的装备。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
    2.  自主任务分配：基于人工智能驱动的规则或人在回路中的控制，实现从无人机到卫星等传感器的自主任务分配。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
    3.  可成为任意地点的作战中心：混合现实能力使操作员和指挥官能够在边缘环境中的虚拟作战中心进行协作。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
*   **应用程序及模块：**
    | 应用/模块 | 功能 |
    | --- | --- |
    | Graph | 提供了类似于白板的界面，用户可以在图中创建或编辑数据，还可以通过插件进行时间分析，网络分析，识别数据模式。 |
    | Gaia | 允许用户通过共享的实时地图跟踪实时数据，以便每个人都可以对相同的信息采取行动。 |
    | Dossier | 实时协作文档编辑器，用户可以跨团队和组织进行协作，以在 Gotham 生态系统内创建实时和动态情报产品。 |
    | Stencil | 结构化的表单输入工具，支持协作数据输入和报告创作，可以执行结构化的内容创建，同时支持自定义的审批流程。 |
    | Video | 允许多种格式的实时和历史视频数据进行交互的应用程序。 |
    | Table | 交互式的自上而下的搜索工具，用于快速检索大量事件型信息。 |
    | Ava | 人工智能系统，可扫描数十亿个数据点，全天候针对数据流进行调查。 |
    | Forward | 可以在不稳定甚至无信号的网络环境中过提供同步的 Gotham 服务。 |
    | Mobile | 携载 Gotham 的移动设备，支持实时和分布式操作。 |
    [来源：https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf]

#### 2.2 Foundry 平台
*   **定位：** 基于本体论（Ontology）的现代企业操作系统。旨在打破企业内部的数据孤岛，将生产、供应链、销售、财务等所有数据集中到一个统一的平台上。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf] [来源：https://www.smartcity.team/investment/companies/palantir]
*   **Ontology 三层能力：**
    | 分层 | 功能 | 描述 |
    | --- | --- | --- |
    | 语义层 | 动态对象和链接 | 将不同的数据和模型源集成到业务“名词”的实时、交互式视图中，包括其对象、实体、关系和事件 |
    | | 多模态属性 | 从模型、结构化数据、流数据、地理空间数据和任何其他数据或模型源生成对象特性 |
    | | 本体原语 | 使用预定义的配置模式快速配置常见现实概念 (如计划) 的属性、行为和相互依赖关系 |
    | 动力层 | AI 驱动的动作和功能 | Foundry 本体将动作链接到语义对象，形成 AI 指导操作的基础 |
    | | 流程挖掘和自动化 | 挖掘行动和流程，揭示隐藏的行动流程和低效率，并量化变化的业务影响 |
    | | 动作编排 | 通过将写回过程分配给执行动作，以稳定、受控的方式跨系统执行操作 |
    | | 实时监控 | 让非技术团队监控本体的语义和动态元素，采用低代码工具使得在对象、操作和流程上创建规则变得容易 |
    | 动态层 | 人工智能指导的决策 | 将模型绑定到对象和操作，以指导决策和自动化流程。模型可以对业务的语义和动态变量进行推理 |
    | | 多步模拟 | 通过跨一系列指标 (如盈利能力、生产或客户价值) 模拟决策，在战略和运营之间建立实时联系 |
    | | 决策捕捉和学习 | 以编程方式将决策数据反馈给 AI/ML，关闭运营和分析之间的环路，并提高您的模拟预测能力 |
    [来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
*   **应用程序及模块：**
    | 应用程序 | 功能 |
    | --- | --- |
    | Monocle | 使用能够使用图形界面访问和管理数据链条，比如访问和管理产业链上下游的各种数据 |
    | Contour | 支持自上而下对大规模数据进行研究，用户可以在 Foundry 中过滤、添加以及可视化数据集 |
    | Object Explorer | 允许用户与表示为对象（如客户、设备或工厂）的数据进行交互，支持搜索索引数据并遍历对象之间的连接 |
    | Fusion | Foundry 的电子表格环境，用户可以创建单元格引用和函数，以创建新的数据集或报表 |
    | Workshop | 帮助用户在低代码或无代码的环境中构建应用程序，可以动态地构建交互式工作流 |
    | Vertex | 使用可以模拟变化并执行假设性分析，帮助机构优化运营 |
    | Code Authoring | 是为数据工程师设计的一套应用，便于数据工程师在平台上进行开发 |
    | Quiver | 是一个多维图表应用程序，用于分析非常大的时间序列数据集，例如来自机器传感器的流式数据 |
    | AI/ML | 将人工智能和机器学习与 Foundry 平台的核心组件集成，用户可以进行调用以实现各种功能 |
    | Code Workbooks | 每个计算步骤都可以保存为 Foundry 数据集，可供其他应用程序使用以及跨工作簿重用 |
    | Reports | 允许用户动态发布并实时更新工作及数据 |
    [来源：https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf]
*   **核心模块能力：**
    *   **Data Connectivity & Integration：** 支持对接近 160 多种数据库；专门开发了与 SAP 对接的插件。数据存储用了 HDFS 作为解决方案。[来源：https://www.smartcity.team/investment/companies/palantir]
    *   **Ontology 本体论：** 数字孪生模块，支持基于各类业务系统中的数据表构建逻辑模型。[来源：https://www.smartcity.team/investment/companies/palantir]
    *   **Analytic：** 分析模块，支持业务流的展现，与业务系统的一键协同。[来源：https://www.smartcity.team/investment/companies/palantir]
    *   **AI Platform：** 包含基础的 AI 能力，实现机器学习、预测、策略优化等能力。[来源：https://www.smartcity.team/investment/companies/palantir]
    *   **Market Place：** 应用市场能力，快速获取开箱即用的模板。[来源：https://www.smartcity.team/investment/companies/palantir]
    *   **Developer Toolchain：** 实现应用层的 Operation 能力，从看数到执行（数据回写 Write Back）。[来源：https://www.smartcity.team/investment/companies/palantir]
    *   **Security & Governance：** 安全管控能力。[来源：https://www.smartcity.team/investment/companies/palantir]

#### 2.3 Apollo 平台
*   **定位：** 在异构环境中部署、监控、修复和保护软件。作为 Gotham 和 Foundry 的底层技术基座。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf] [来源：https://www.smartcity.team/investment/companies/palantir]
*   **功能：** 自动部署、产品和环境约束解决、高级升级策略、安全回收、配置管理、主动监测和警报、合规性和可审计性、安全行动、软件供应链。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
*   **优势：** 支持在任意环境运行，包括公有云、私有云、边缘等。通过单一平台管理所有软件的持续维护和更新。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]

#### 2.4 AIP 平台
*   **定位：** 在应用中使用 AI 实现代理和自动化，接入 openAI 等大语言模型。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
*   **核心模块：** AIP Assist（界面聊天助手）、AIP Logic（无代码开发环境）、AIP Agent Studio（快速创建智能代理）。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **功能：** 使用 LLM 分析图片和视频；在构建流程中使用 LLM 分析 PDF 文件；使用 Palantir 提供的模型进行语义搜索；在 Pipeline Builder 中使用 LLM 进行情感分析。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
*   **案例：** AI 查看警报并自动提出解决方案；自定义 AI 工具，并用自然语言告知其任务。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]

### 3. Ontology 语义建模技术架构

#### 3.1 Ontology 定义与定位
*   **定义：** Ontology 是一种操作层（operational layer），它“坐落于平台中已接入的数字资产（数据集、模型等）之上，将它们与现实世界的实体／业务对象连接起来”。[来源：https://www.cnblogs.com/end/p/19144086]
*   **要素：** 一个 Ontology 包含三类要素：1. 语义型（静态）元素：Object 类型、Link 类型（关系）、属性、接口等；2. 动力型（行为／函数／操作）元素：操作（Actions）、函数（Functions）、写回（Writeback）等；3. 治理、安全、版本控制与审计支持。[来源：https://www.cnblogs.com/end/p/19144086]
*   **与传统数仓区别：** 传统数仓建模逻辑是表（Table），描述的是数据的结构；Ontology 描述的是可操作的业务对象。传统数仓名词和动词是分离的；Ontology 名词和动词一起建模。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **四要素集成：**
    | 要素 | 描述 |
    | --- | --- |
    | Data | 从 ERP、CRM、工业数据库、地理空间、实时传感器等异构数据源统一抽象为 objects/properties/links |
    | Logic | 业务规则、ML 模型、LLM 函数、多步编排统一在 Ontology 内定义 |
    | Action | 从简单属性更新到复杂多步事务，变更可实时回写到运营系统 |
    | Security | 行级、列级权限控制，AI agent 继承人类权限或项目权限 |
    [来源：https://techwhims.com/cn/posts/palantir-core-architecture]

#### 3.2 底层架构：三层设计与微服务分解
*   **Language（建模语义）：** 解决「如何定义业务对象」的问题。定义了 Object Types、Property Types、Link Types、Action Types、Logic。通过 SDK（OSDK）声明式地描述。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **Engine（执行层）：** 负责高性能执行。包含高规模 SQL 查询、实时状态变更订阅、原子事务更新、批量变更与流式处理、版本控制。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **Toolchain（开发与运维）：** OSDK 自动生成 API 网关和多语言 SDK；DevOps 工具链；IDE 集成。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]

#### 3.3 微服务架构拆解：OMS 与 OSS
*   **OMS（Ontology Metadata Service）：** Ontology 的「元数据服务」。负责管理 Object Types 的元数据、Link Types 的定义、Action Types 的定义。是 Ontology 的「schema 注册中心」。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **OSS（Object Set Service）：** Ontology 的「读取服务」。负责对象的搜索与过滤、聚合计算、对象加载、对象集的动态维护。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **Object Sets 的分类：**
    | 类型 | 描述 | 典型场景 |
    | --- | --- | --- |
    | Static | 主键列表，一经创建不变 | 「我关注的 100 个重点客户」 |
    | Dynamic | 过滤条件，结果随数据自动更新 | 「所有未处理的订单」 |
    | Temporary | 24 小时过期，适合临时分析 | 一次 ad-hoc 查询的结果集 |
    | Permanent | 长期保存的对象集 | 业务定义的关键群体 |
    [来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **数据写入：Object Data Funnel：** 数据从源系统通过 CDC 管道进入，经过清洗、转换、映射到 Ontology 对象模型，写入 Object Databases，触发 OMS 元数据更新和 OSS 缓存刷新。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]

#### 3.4 版本控制与分支治理（Git for Data）
*   **设计哲学：** 借鉴 Git 的设计哲学。每个 Ontology 变更都有版本记录，变更可以开「分支」，在分支上做实验性修改，批准后 merge 回主版本。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **与代码 Git 的区别：**
    | 特点 | 代码 Git | Foundry Git-for-Data |
    | --- | --- | --- |
    | 存储对象 | 文本文件（几 KB ~ MB） | 数据集（GB ~ TB 级） |
    | 变更方式 | 基于行的差异（diff/patch） | 基于数据块/分区的差异（block/partition delta） |
    | 合并逻辑 | 按行合并冲突 | 按数据粒度合并（字段、分区、数据对象），更多自动化 |
    | 索引方式 | 文件树 + commit | 数据集索引 + 时间/版本号 |
    | 性能优化 | 面向小文件优化 | 面向大规模分布式存储优化（列存/对象存储 + 元数据索引） |
    [来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **冗余数据解决：** 采用增量存储（Delta Storage）、列存压缩、分区化、生命周期管理、冷热分层存储。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

#### 3.5 权限控制体系
*   **粒度：** 源数据层（行/列/表权限）、Ontology 层（业务对象为中心）、属性级别、实例级别（Row-level Security）、操作级别。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **技术实现：** Policy-as-Code、语义绑定、动态评估、遮罩/变形。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **与传统数据库权限对比：**
    | 维度 | 传统数据库 / ERP 权限 | Foundry Ontology 权限 |
    | --- | --- | --- |
    | 控制对象 | 表、字段（Column-level Security） | 业务对象（Order、Customer、Asset）、属性（字段）、实例（单条记录）、操作（动作） |
    | 粒度 | 表级、字段级 | 对象级、属性级、实例级、操作级 |
    | 业务语义 | 权限绑定在表结构上，语义弱 | 权限绑定在 Ontology 对象及关系上，直接映射业务逻辑 |
    | 上下文动态性 | 固定规则 | 动态策略：基于用户角色、部门、地域、上下文条件 |
    | 操作权限 | 通常只有 CRUD | 可定义“业务动作权限”，如 cancelOrder、approvePayment、rerouteTruck |
    | 数据遮罩 | 部分支持 | 内置多级遮罩：完全隐藏、部分脱敏、汇总级展示 |
    | 跨系统一致性 | 难以统一 | 统一在 Foundry Ontology 层做语义权限管理 |
    | 审计能力 | 日志较粗粒度 | 精细审计：谁在什么上下文下访问了哪个对象的哪个属性、执行了什么操作 |
    [来源：https://www.53ai.com/news/Palantir/2025121217384.html]

### 4. 技术栈与实现细节

*   **前端：** TypeScript + React（UI 框架）、GraphQL / REST（交互）、WebGL（渲染引擎）、MapboxGL（地图与 3D 场景）、D3.js / Highcharts（BI 可视化）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **后端：** Kubernetes（容器编排）、Apollo（持续交付与多云部署）、分布式存储（S3 兼容、Parquet、ORC）、关系数据库（Postgres、Oracle）、分布式计算引擎（Apache Spark、Flink）、Graph 数据存储（自研或基于分布式 KV）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **AI/数据科学：** 工作台支持 Python、R、SQL，集成 scikit-learn、TensorFlow、PyTorch。内置 MLOps 模块。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **DevOps 与运维：** CI/CD（Apollo + Git 集成）、监控（Prometheus、Grafana、Elastic Stack）、安全合规（Kubernetes 原生安全策略 + 自研隔离机制）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **数据生命周期管理：** 数据引入（Ingestion）、存储（Storage & Modeling）、使用（Usage & Execution）、归档/销毁（Archival & Deletion）。支持数据保留策略（Retention Policy）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **PB/TB 规模计算优化：** 分层/分级数据架构、预计算与特征工程、增量计算与流式处理、分布式与并行计算、容错与回溯。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

### 5. AI 与 Agent 融合 (AIP)

*   **传统 RAG 局限：** LLM 只是「更好地搜索」，不介入业务操作。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **AIP 解法：** AI 不只检索信息，而是在治理框架内对真实业务对象提出操作建议。每个 Action 都有权限校验，AI 的操作建议要经过人工审批。审批通过后，操作回写到业务系统。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **Proposal 工作流：** 借鉴 Git 的 branching 思想。1. AI 提议一个操作；2. 提议作为一个「branch」存在，可被 review；3. 人类审批通过后，merge 到主状态；4. 操作执行到业务系统。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **AIP 核心能力：**
    | 能力 | 描述 |
    | --- | --- |
    | Pipeline Builder | 用 LLM 对非结构化数据做分类、摘要、实体提取，自动构建数据管道 |
    | Scenario Primitive | 模拟「假设」场景，如「如果这条生产线调整，对供应链的影响是什么」 |
    | Language Model Service | 统一接口切换/比较多个 LLM 提供商（OpenAI, Anthropic, 自托管等） |
    | AI Agent | 自然语言操作 Foundry（创建 pipeline、管理 repo、构建 ontology 对象） |
    [来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **Ontology 与 AI 双向融合：** Ontology 赋能大模型（提供高质量上下文输入）；大模型加速 Ontology（基于已有数据快速生成 Ontology 初始框架）。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

### 6. 商业模式与交付模式

*   **FDE 模式（Forward Deployed Engineers）：** 嵌入客户运营环境的工程师。住在客户现场，理解客户的业务流程，基于 Ontology 定制开发，持续优化客户的运营流程。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **产品复利逻辑：** 摒弃传统产品设计模式，派工程师深入客户现场，积累解决实际问题的经验。将重复痛点转化为标准化工具，打造出 Foundry 等核心平台。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **客户商业化三阶段：** 获客（Acquire）、扩张（Expand）、留存（Scale）。2020 年前三季度，处在获客阶段的用户产生了 4,110 万美元的收入，产生了 420 万美元的贡献亏损；扩张阶段客户创造了 2.544 亿美元的收入，边际贡献率为 41％；留存阶段客户创造了 4.522 亿美元的收入，贡献率为 69％。[来源：https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf]
*   **收入模式：** 订阅制、项目制、混合。按照“用户数 / 节点数 / 数据量”收费，或以“价值分享”方式收费。[来源：https://www.53ai.com/news/Palantir/2025121217384.html] [来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]

### 7. 行业案例与对标

*   **政府/国防案例：**
    *   美国陆军：2019 年签订 4.58 亿美元生产协议支持陆军 Vantage；2024 年 12 月 18 日签订四年 4.01 亿美元合同，最高上限可达 6.19 亿美元。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
    *   美国特种作战司令部：2023 年 6 月 5 日获得多年合同，价值高达 4.63 亿美元。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
    *   英国国防部：2022 年 12 月 21 日达成协议，价值 7500 万英镑，为期三年。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
    *   捕获本拉登：通过分析海量的卫星图像，发现在深山的废弃屋舍旁出现了人类垃圾，判断本拉登可能藏匿于此。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **商业案例：**
    *   摩根大通：2010 年成为首位商业客户，对付欺诈犯。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf] [来源：https://www.smartcity.team/investment/companies/palantir]
    *   空客：2017 年达成合作伙伴关系，连接了来自全球一百多家航空公司 9000 余架飞机的航空数据。A350 机型产能提升 4 倍速增长。[来源：https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf] [来源：https://www.smartcity.team/investment/companies/palantir]
    *   3M：2021 年 2 月 23 日，数百万美元，支持 3M 数字化转型，建立动态供应链。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
    *   喜力啤酒：利用 Palantir“快进”供应链：从被动救火到预知未来。[来源：https://www.53ai.com/news/Palantir/2025121296031.html]
*   **行业对标：**
    | 维度 | Foundry | Databricks | Snowflake ML | SageMaker |
    | --- | --- | --- | --- | --- |
    | 训练能力 | 支持外部训练产物接入，本地也可跑常见 Python ML，不是超大规模分布式训练平台 | 原生支持大规模 Spark/Flink 训练，MLflow 实验管理 | 内嵌 AutoML + 轻量模型训练，偏中小规模场景 | 大规模分布式训练、GPU/TPU 调度、自动超参优化 |
    | 算法库 | 内置标准算子库，可扩展；强调“与 Ontology 绑定” | 广泛支持开源库，高度自由 | Snowpark ML API，功能相对有限 | 深度支持 TensorFlow、PyTorch、Hugging Face 等框架 |
    | 工作流编排 | 算法即节点，可组成 DAG，直接作用于业务对象 | Pipelines + MLflow 实验管理，面向数据科学团队 | SQL/Python 调用，简化工作流 | Step Functions + SageMaker Pipelines，面向 MLOps 工程师 |
    | 模型部署 | 模型作为服务封装到 Foundry 内部，直接挂载到业务应用 | 部署到 Databricks Serving 或外部 API | 模型可转化为 SQL UDF/表函数 | 最完善的在线/批量推理服务 |
    | 差异化 | 算法与 Ontology 强绑定：结果直接映射到“订单、车辆、库存”等对象 | 超大规模训练 & 数据湖原生 | 仓库内轻量 ML | 最强的 ML 工程平台 |
    [来源：https://www.53ai.com/news/Palantir/2025121217384.html]
    | 功能模块 | Palantir 的特色 | 可能的替代品/类似产品 | 差异与门槛 |
    | --- | --- | --- | --- |
    | 地图与地理信息可视化 | 深度集成任务数据，支持多源数据叠加 | Google Earth、ESRI ArcGIS、OpenStreetMap、CesiumJS | Palantir 能将异构数据实时叠加并用于决策 |
    | 数据集成与建模 | 异构数据源快速接入 | Talend、Informatica、Fivetran、Apache NiFi | Palantir 更关注安全环境和高度复杂的数据权限隔离 |
    | 知识图谱 / 关系建模 | 将人、物、地点、事件串联成图谱 | Neo4j、TigerGraph、Stardog，IBM I2 | Palantir 优势在于自动化构建、与安全权限体系深度结合 |
    | 权限与安全体系 | 细粒度权限控制，支持跨部门、跨级别的共享与隔离 | Okta、SailPoint、Centrify | 在军事/情报级别的复杂安全需求下，Palantir 的设计难以被替代 |
    [来源：https://www.53ai.com/news/Palantir/2025121217384.html]

### 8. 对架构师的启示与行动建议

*   **核心认知：** Palantir 的 Ontology 并不是一个新的「数据库」或「数据中台」，它本质上是一套「业务语义操作系统」。数据不只是被查询的对象，而是可以被操作的主体。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **行动建议：**
    | 阶段 | 行动 | 衡量标准 |
    | --- | --- | --- |
    | 短期（1-3 个月） | 梳理核心业务对象，识别关键实体及其关系 | 产出核心 Ontology 草图（10-20 个对象类型） |
    | 中期（3-6 个月） | 构建语义 API 层，将常用查询封装为服务 | 业务方通过 API 获取数据的比例超过 50% |
    | 长期（6-12 个月） | 引入 AI 操作建议，试点分支治理 | AI 建议被采纳并执行的操作 > 10 条/周 |
    [来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **可借鉴的理念：** 业务对象统一建模、OMS/OSS 分离、Object Set API 化、AI 介入操作层、版本控制治理、CDC 实时同步、FDE 驻场模式。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **风险提示：** 不要「为了 Ontology 而 Ontology」；小心过度工程；权限和安全是底线；组织配套是关键。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]

## 推荐工作流

*   **组合使用工具：** 将 Ontology 作为记忆层，AIP 作为执行层，Apollo 作为部署层。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **执行步骤：**
    1.  **语义上下文接入：** 在 Agent Studio 创建一个 agent，可选择加入"Ontology Context"或"Ontology semantic search tool"作为上下文来源。[来源：https://www.cnblogs.com/end/p/19144086]
    2.  **配置检索 K 值、查询属性：** 在语义搜索设置中，可以指定返回多少个对象（K 值）、哪些属性参与检索、哪些字段用于 embedding 向量检索等。[来源：https://www.cnblogs.com/end/p/19144086]
    3.  **绑定 Action / Function：** 为 agent 提供可以调用的本体 Action，如“更新状态”、“触发审批流程”、“创建任务”等。[来源：https://www.cnblogs.com/end/p/19144086]
    4.  **处理 agent 输出 / 写回：** Agent 调用操作后，操作结果可以写回本体级别或外部系统，实现真正的业务落地。[来源：https://www.cnblogs.com/end/p/19144086]
    5.  **应用状态 / 任务流与 UI 集成：** 可以将 agent 嵌入 Workshop 应用、通过 Agent Studio 的交互界面、或借助 API 嵌入到外部 UI 中。[来源：https://www.cnblogs.com/end/p/19144086]
    6.  **安全 / 限权 / 审计：** 对 agent 的操作调用进行权限校验、审计日志、异常处理、回滚策略等保障机制。[来源：https://www.cnblogs.com/end/p/19144086]
*   **配置方法：** 使用 Pipeline Builder 构建数据集成管道，将原始数据源转换为可供进一步分析的干净输出。步骤：1）输入；2）转换；3）预览；4）交付；5）输出。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]

## 适用场景

*   **复杂多源数据整合：** 适合 ERP、CRM、实时传感器、行为日志分布在不同系统，每次要做一个跨系统分析，都要经历痛苦的 ETL 和数据对齐的场景。[来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   **高安全/合规要求：** 适合军事、金融、能源等高风险领域，需要细粒度权限控制、审计追溯、防止数据泄露的场景。[来源：https://techwhims.com/cn/posts/palantir-core-architecture] [来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **需要决策与执行闭环：** 适合不仅需要洞察，还需要将“洞察”与“行动”打通，从根本上缩短价值实现链条的场景。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **情报分析与风险控制：** 适合情报分析、风险管控、供应链可视化等多实体、多关系场景，尤其在事件溯源和模式发现上具备天然优势。[来源：https://www.53ai.com/news/Palantir/2025121217384.html] [来源：https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf]
*   **实际案例：** 美国陆军 Vantage 平台（支持陆军数据平台 ADP）；空客 A350 产能优化（产量提升 33%）；摩根大通反欺诈；捕获本拉登行动。[来源：https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf] [来源：https://www.smartcity.team/investment/companies/palantir]

## 不适用场景

*   **单纯数值优化：** 知识图谱长于关系建模，却不擅长数值优化（如调度、线性规划），需借助外部算法引擎。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **实时高频数据流处理：** 知识图谱本身难以处理实时高频数据流（如传感器毫秒级信号），必须依赖额外的流式计算框架。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **高度动态、非结构化数据环境：** 在一些高度动态、非结构化的数据环境（例如社交媒体、非标准 IoT）下，建模难度陡增。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **低成本/轻量化需求：** Palantir 实施成本昂贵，高客单价商业模式（软件年费数百万美元），不是所有企业能承受。[来源：https://techwhims.com/cn/posts/palantir-core-architecture] [来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   **限制条件：** 高度依赖建模能力和行业理解，不同客户的语义差异大，实施成本高。[来源：https://www.53ai.com/news/Palantir/2025121217384.html]

## 风险与约束

*   **建模成本高/启动门槛高：** 构建一个高质量的本体模型需要领域专家、系统工程师、架构师的协作。初期投入可能较高。[来源：https://www.cnblogs.com/end/p/19144086]
*   **模型一致性/变更冲突：** 多人、多个业务线协作时，本体模型的冲突、语义分歧很容易产生。必须引入严格的协作流程、版本控制、审批机制。[来源：https://www.cnblogs.com/end/p/19144086]
*   **平台锁定/迁移成本：** 如果把 Agent/业务严重依赖在特定本体平台之上，未来迁移成本高。客户数据在经过 Palantir 平台归一化处理后，深度融入其本体架构，转换成本极高。[来源：https://www.cnblogs.com/end/p/19144086] [来源：https://www.smartcity.team/investment/companies/palantir]
*   **安全/越权/恶意操作风险：** 虽然本体提供权限机制，但设计不周可能仍被绕过或滥用，必须严格测试、监控 agent 的行为。[来源：https://www.cnblogs.com/end/p/19144086]
*   **具体风险案例：** 近期，其为美军打造的“下一代指挥与控制系统”（NGC2）被内部报告曝光存在“基础安全控制、流程和治理方面的严重缺陷”，系统风险等级被评为“极高”。该报告严厉指出，系统“无法控制访问权限、无法验证软件安全”。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **估值风险：** 当前估值对应 2026 年预期自由现金流的 153 倍，远高于软件行业 48 倍的平均水平。[来源：https://www.smartcity.team/investment/companies/palantir]
*   **国际业务疲软：** 2025 年 Q2，其国际商业收入同比下滑 3%，已连续多个季度呈现负增长。[来源：https://www.smartcity.team/investment/companies/palantir]

## 信源质量门控记录

### 门控规则
*   Tavily score < 0.4：剔除
*   已知低质域名：剔除
*   重复 URL：合并保留最高分结果
*   Exa 学术/语义结果：默认保留，但进入来源等级评估
*   C/D 级来源不得作为唯一结论依据
*   入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`

### 保留信源
1.  [Palantir 核心技术架构深度研究 - Tech Whims | 张晓龙](https://techwhims.com/cn/posts/palantir-core-architecture) - 来源等级：B - 保留原因：与主题高度相关，技术细节丰富。
2.  [万字解读 Palantir 产品、技术和架构讨论 - 53AI](https://www.53ai.com/news/Palantir/2025121217384.html) - 来源等级：B - 保留原因：与主题高度相关，内容详尽。
3.  [Concept-Centric Software Development](https://arxiv.org/html/2304.14975) - 来源等级：A - 保留原因：学术论文，一手数据。
4.  [深度解析 Palantir (中邮证券)](https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf) - 来源等级：A - 保留原因：官方文档 / 一手数据，财务与案例详细。
5.  [Palantir 产品体系深度解构：Ontology 驱动下的分层架构与模块 - 墨天轮](https://www.modb.pro/db/1930804422725087232) - 来源等级：C - 保留原因：相关性一般，需交叉验证，作为补充。
6.  [Palantir 的“本体工程”的核心思路、技术架构与实践示例 - 博客园](https://www.cnblogs.com/end/p/19144086) - 来源等级：C - 保留原因：相关性一般，需交叉验证，作为补充。
7.  [一文全面解析 Palantir 产品以及其“本体论” - 智慧城市行业分析](https://www.smartcity.team/investment/companies/palantir) - 来源等级：B - 保留原因：与主题高度相关，商业与财务数据详细。
8.  [Palantir— —深挖政府大数据的神秘独角兽 (海通证券)](https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf) - 来源等级：C - 保留原因：相关性一般，数据较旧（2021），作为历史参考。
9.  [相关研究报告北交所研究团队 - i 研报 (开源证券)](https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf) - 来源等级：A - 保留原因：官方文档 / 一手数据，2024-2025 财务数据。

### 剔除信源
*   多个重复 URL（如 53AI 不同路径但内容相同）已合并。
*   Tavily score < 0.4 的信源已剔除（如 SIJE Unveils Agentic AI...等）。
*   低质域名或导航页已剔除。

## 来源与可信度

| 来源 | 来源类型 | 可信度 | 支撑内容 |
| --- | --- | --- | --- |
| https://techwhims.com/cn/posts/palantir-core-architecture | 技术博客/分析 | 高 | Ontology 架构三层设计、OMS/OSS 微服务、AIP 工作流、架构师启示 |
| https://www.53ai.com/news/Palantir/2025121217384.html | 技术博客/分析 | 高 | 产品定位、数据层设计、算法引擎、权限体系、技术栈、竞品对标 |
| https://arxiv.org/html/2304.14975 | 学术论文 | 高 | Concept-Centric Software Development 内部开发流程 |
| https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf | 券商研报 | 高 | 财务数据、国防业务案例、产品模块列表、专利分析 |
| https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf | 券商研报 | 高 | 2024-2025 财务数据、商业模式、AIP 布局 |
| https://www.smartcity.team/investment/companies/palantir | 行业分析 | 中 | 公司发展历程、四大平台、护城河分析、风险 |
| https://www.modb.pro/db/1930804422725087232 | 技术博客 | 中 | 产品架构分层、核心模块列表 |
| https://www.cnblogs.com/end/p/19144086 | 技术博客 | 中 | Ontology 工程思路、Agent 融合、风险挑战 |
| https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf | 券商研报 | 中 | 早期财务数据（2020-2021）、Gotham/Foundry 模块、知识图谱技术 |

## 对于可信度较高的来源逐来源总结

### 来源 1: Palantir 核心技术架构深度研究 - Tech Whims
*   **核心内容：** 深入解析 Ontology 的技术架构（Language, Engine, Toolchain），OMS/OSS 微服务分解，AIP 的 Proposal 工作流，以及三大平台（Gotham, Foundry, Apollo）的区别。
*   **可用事实：** Ontology 四要素（Data, Logic, Action, Security）；Object Sets 四种类型（Static, Dynamic, Temporary, Permanent）；Git for Data 设计哲学；对架构师的行动建议（短期/中期/长期）。
*   **局限：** 部分技术细节可能基于公开文档推断，非内部源码。
*   **适合入库知识点：** Ontology 架构分层、微服务拆解、AIP 工作流、架构师启示。

### 来源 2: 万字解读 Palantir 产品、技术和架构讨论 - 53AI
*   **核心内容：** 全面解析 Palantir 产品、技术、架构、商业模式、竞品对标。包含大量技术栈细节（前端/后端/AI/DevOps）。
*   **可用事实：** 详细的技术栈列表（TypeScript, React, Kubernetes, Spark 等）；权限控制体系对比表；与 Databricks/Snowflake/SageMaker 的对标表；Git for Data 与代码 Git 的区别表。
*   **局限：** 部分内容为综合整理，需交叉验证。
*   **适合入库知识点：** 技术栈细节、权限体系、竞品对标、数据生命周期管理。

### 来源 4: 深度解析 Palantir (中邮证券)
*   **核心内容：** 券商研报，侧重财务数据、国防业务案例、产品模块列表、专利分析。
*   **可用事实：** 2023 年收入 22.25 亿美元；国防业务具体合同金额（如陆军 4.58 亿美元）；Gotham/Foundry 应用程序及功能列表；专利分布（G06F17 等）。
*   **局限：** 财务数据截至 2024 年初，需结合更新报告。
*   **适合入库知识点：** 财务数据、国防案例、产品模块列表、专利分析。

### 来源 10: 相关研究报告北交所研究团队 - i 研报 (开源证券)
*   **核心内容：** 2025 年 3 月报告，包含 2024 年最新财务数据，AIP 布局，商业模式。
*   **可用事实：** 2024 年营收 28.66 亿美元；客户总数 711 家；毛利率 80.25%；AIP 训练营策略。
*   **局限：** 侧重投资分析，技术细节略少于技术博客。
*   **适合入库知识点：** 最新财务数据、客户数据、商业模式、AIP 策略。

## 跨源矛盾检测结论

### 检测范围
*   已精读来源数量：10 个
*   检测对象：核心数字、日期、功能描述、因果判断、市场/公司事实
*   检测时间：2026-06-21

### 检测结果
结论：检测到 3 处跨源矛盾，综合输出时必须保留双方表述，不得静默合并。

### 矛盾项 1：2023 年营收数据
*   **矛盾描述：** 不同来源对 2023 年营收数据的表述略有差异。
*   **来源 A：** [https://pdf.dfcfw.com/pdf/H3_AP202501221642435170_1.pdf]
    *   原文引用："2023 年，Palantir 公司收入 22.25 亿美元”
    *   来源等级：A
    *   发布时间 / 数据日期：2025 年 1 月 21 日
*   **来源 B：** [https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
    *   原文引用："2023 财年，公司实现营业收入 22 亿美元”
    *   来源等级：A
    *   发布时间 / 数据日期：2025 年 03 月 07 日
*   **初步判断：**
    *   倾向：来源 A
    *   理由：来源 A 数据更精确（22.25 亿 vs 22 亿），且为详细研报。
*   **综合输出要求：** 必须写成“来源 A 说 22.25 亿美元，来源 B 说 22 亿美元，建议人工核实”

### 矛盾项 2：2024 年营收数据
*   **矛盾描述：** 不同来源对 2024 年营收数据的表述略有差异。
*   **来源 A：** [https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
    *   原文引用："2024 财年营业收入达到 28.66 亿美元”
    *   来源等级：A
    *   发布时间 / 数据日期：2025 年 03 月 07 日
*   **来源 B：** [https://www.smartcity.team/investment/companies/palantir]
    *   原文引用："2024 年与 BP 达成 AIP 合作...2025 年与 xAI 等合作”（未直接给出 2024 全年营收具体数字，但提到 2025 年 Q2 营收 10.04 亿美元）
    *   来源等级：B
    *   发布时间 / 数据日期：2025 年 10 月
*   **初步判断：**
    *   倾向：来源 A
    *   理由：来源 A 明确给出了 2024 财年数据。
*   **综合输出要求：** 以来源 A 数据为准，来源 B 作为补充。

### 矛盾项 3：Gotham 架构独立性
*   **矛盾描述：** 关于 Gotham 是否是独立单体架构。
*   **来源 A：** [https://www.53ai.com/news/Palantir/2025121217384.html]
    *   原文引用：“今天 Gotham 实际上是运行在 Foundry 栈上的一个垂直应用（Government Vertical），而 Foundry 是底层通用操作系统。”
    *   来源等级：B
    *   发布时间 / 数据日期：2025-12-12
*   **来源 B：** [https://file.iyanbao.com/pdf/1913d-99d0e401-e9a1-4d4c-9878-e90824c59ccc.pdf]
    *   原文引用："Palantir 拥有两个软件平台 Gotham 和 Foundry...这两个平台既可以单独使用，也可以捆绑在一起作为统一的生态系统。”（2021 年报告，暗示相对独立）
    *   来源等级：C
    *   发布时间 / 数据日期：2021 年 2 月
*   **初步判断：**
    *   倾向：来源 A
    *   理由：来源 A 时间更新，反映了架构演进（向 Foundry 栈融合）。
*   **综合输出要求：** 必须写成“来源 A 说 Gotham 运行在 Foundry 栈上，来源 B 说两者可单独使用，建议人工核实架构演进状态”

## 矛盾与待验证问题

*   **Gotham 架构演进状态：** 早期报告（2021）称 Gotham 和 Foundry 为两个独立平台，可单独使用；近期分析（2025）称 Gotham 实际上是运行在 Foundry 栈上的垂直应用。需核实当前 Gotham 是否已完全融合进 Foundry 底层。
*   **2024 年精确营收：** 开源证券报告称 28.66 亿美元，中邮证券报告称 2023 年 22.25 亿美元。需核实 2024 年确切财报数据。
*   **AIP 具体收费模式：** 有来源提到“价值分享”方式收费，有来源提到“订阅制、项目制、混合”。需核实 AIP 的具体定价模型是基于调用次数、算力消耗还是场景/用户打包。
*   **NGC2 系统安全风险：** 有来源提到“下一代指挥与控制系统”（NGC2）被内部报告曝光存在“极高”风险等级。需核实该报告的真实性和当前修复状态。
*   **国际业务增长：** 有来源提到 2025 年 Q2 国际商业收入同比下滑 3%，连续多个季度负增长。需核实这是否为长期趋势。

## 原始证据摘录

*   "Palantir 的回答是：**把数据变成运营层的数字孪生，让 AI 在治理框架内直接提出操作建议**。这不是一个简单的「知识图谱」或「数据中台」概念。Palantir 构建的叫 **Ontology**——一个把数据、逻辑、操作、安全统一建模的语义层。” [来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   "Ontology 是 **四要素集成**：Data（从 ERP、CRM...统一抽象）、Logic（业务规则、ML 模型...）、Action（从简单属性更新到复杂多步事务）、Security（行级、列级权限控制）。” [来源：https://techwhims.com/cn/posts/palantir-core-architecture]
*   "Palantir 的模式介于“软件公司”和“咨询公司”之间，强调产品平台 + 咨询交付。这种“重交付”模式难以规模化，但形成了与 SaaS 厂商的差异化。” [来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   "2024 年营收 28.66 亿美元，同比增长 28.79%。其中政府业务实现 15.70 亿美元，商业业务实现 12.96 亿美元。2024 年毛利率 80.25%，净利率 16.33%。” [来源：https://file.iyanbao.com/pdf/1f1fc-fd3e408a-98d0-47f5-a93a-a9e7dd6537e9.pdf]
*   "Palantir 的护城河并非单一优势，而是由技术、数据、品牌、模式四大要素交织构成的立体化、自增强体系。其商业模式常被类比为 **“微软（技术）+ 麦肯锡（咨询）”** 的结合体。” [来源：https://www.smartcity.team/investment/companies/palantir]
*   "Foundry 的"Git for Data"与代码 Git 的主要区别：存储对象（文本文件 vs 数据集）、变更方式（基于行的差异 vs 基于数据块/分区的差异）、合并逻辑（按行合并冲突 vs 按数据粒度合并）。” [来源：https://www.53ai.com/news/Palantir/2025121217384.html]
*   "近期，其为美军打造的“下一代指挥与控制系统”（NGC2）被内部报告曝光存在“基础安全控制、流程和治理方面的严重缺陷”，系统风险等级被评为“极高”。” [来源：https://www.smartcity.team/investment/companies/palantir]
*   "Ontology 作为一种语义层与行为层的统一建模方法，被越来越多企业和平台（包括 Palantir）视为支撑 AI 未来落地的关键能力之一。” [来源：https://www.cnblogs.com/end/p/19144086]