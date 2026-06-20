---
title: "Wiki 全局索引"
updated: 2026-06-08
total-pages: 21
total-domains: 7
---

# Wiki 索引

## 知识域目录

| 域文件夹 | 页面数 | 说明 | 最近更新 |
|---------|--------|------|---------|
| `_inbox/` | 0 | 待归域知识点暂存区 | 2026-06-08 |
| `concepts/` | 2 | 核心概念和术语 | 2026-06-08 |
| `tools/` | 2 | 工具和平台 | 2026-06-08 |
| `workflows/` | 9 | 操作流程、方法论和 SOP | 2026-06-08 |
| `decisions/` | 1 | 决策记录与历史选择 | 2026-06-08 |
| `sources/` | 7 | 来源摘要（固定域） | 2026-06-08 |
| `outputs/` | 0 | 输出归档 | 2026-05-31 |

---

## 知识点索引

<!-- 规则：
  - 按域分组排列
  - 每行一个知识点
  - LLM 查询时先读此表定位目标页面
-->

### _inbox/（待归域）
| 页面 | Kind | 摘要 | 更新日期 |
|------|------|------|---------|

### concepts/
| 页面 | Kind | 摘要 | 更新日期 |
|------|------|------|---------|
| [[gitea-actions-expression-compatibility]] | concept | Gitea Actions / act_runner 对 string/boolean 表达式的兼容性陷阱 | 2026-06-08 |
| [[python-src-layout-docker-pythonpath]] | concept | Python src-layout 后端镜像通过 PYTHONPATH 暴露业务包路径，避免容器启动导入失败 | 2026-06-08 |

### tools/
| 页面 | Kind | 摘要 | 更新日期 |
|------|------|------|---------|
| [[openspec]] | tool | 面向 AI 辅助开发的规格与变更管理工具，包含 Cursor 命令级用法 | 2026-06-02 |
| [[superpowers]] | tool | 用于约束 Cursor 代理开发行为的工作流技能集合，包含插件安装方式 | 2026-06-02 |

### workflows/
| 页面 | Kind | 摘要 | 更新日期 |
|------|------|------|---------|
| [[openspec-superpowers-cursor-workflow]] | workflow | 将 OpenSpec、Superpowers 与 Cursor 分层组合的命令级开发工作流，含规格资产与验证检查 | 2026-06-02 |
| [[provision-workflow-merge-deduplication]] | workflow | provision 初始化 workflow 合并后的重复 YAML 清理与验证流程 | 2026-06-08 |
| [[uv-sync-python-upper-bound]] | workflow | 在 CI、Docker 和本地环境中限制 Python 上界以避免 PyO3 构建失败 | 2026-06-08 |
| [[gitea-actions-kubectl-install]] | workflow | Gitea Actions 部署 job 执行 Kubernetes 命令前显式安装 kubectl | 2026-06-08 |
| [[kubernetes-rollout-timeout-diagnostics]] | workflow | Kubernetes rollout timeout 后在 CI 中打印 Deployment、Pod、Events 和日志的诊断流程 | 2026-06-08 |
| [[spin-consultative-sales-questioning]] | workflow | B2B 顾问式销售中按情境、难点、暗示、需求效益推进的 SPIN 提问流程 | 2026-06-08 |
| [[business-understanding-framework]] | workflow | 按主体、价值、流程、组织、技术、环境六维读懂客户业务并标注置信度 | 2026-06-08 |
| [[expert-judgment-extraction-workflow]] | workflow | 将专家隐性判断通过情境、线索、推理、约束、行动、边界六层提取为可复用规则 | 2026-06-08 |
| [[deep-demand-discovery-workflow]] | workflow | 从业务理解、5Why 痛点挖掘到 AI 场景价值判断、方案构想和说服叙事的需求挖透流程 | 2026-06-08 |

### decisions/
| 页面 | Kind | 摘要 | 更新日期 |
|------|------|------|---------|
| [[npm-registry-frontend-docker-build]] | decision | 前端 Docker 构建遇到 npmmirror 缺包时切回 npm 官方 registry 的决策 | 2026-06-08 |

### sources/
| 页面 | 原始资料 | 摘要/关键词 | 摄入日期 |
|------|---------|-----------|---------|
| [[sources/2026-06-02-openspec-superpower-cursor-research]] | raw/articles/2026-06-02-openspec-superpower-cursor-research.md | OpenSpec 与 Superpowers 分工、Cursor 工作流、适用边界 | 2026-06-02 |
| [[sources/2026-06-02-openspec-superpowers-cursor-command-workflow-research]] | raw/articles/2026-06-02-openspec-superpowers-cursor-command-workflow-research.md | 命令级 SOP、/opsx、openspec validate、archive、delta spec、逐来源总结、Superpowers 插件命令差异 | 2026-06-02 |
| [[sources/cicd-failure-summary]] | DDC/raw/CICD_FAILURE_SUMMARY.md | CI/CD 失败复盘、Gitea Actions、uv、npm registry、kubectl、Kubernetes rollout、PYTHONPATH | 2026-06-08 |
| [[sources/research-methodology-ai-readable]] | raw/notes/调研方法论（可ai读）.md | SPIN 提问法、隐性需求转显性需求、B2B 角色 Jobs、华拓售前问题示例 | 2026-06-08 |
| [[sources/business-understanding-ai-readable]] | raw/notes/读懂业务（可ai读）.md | 业务理解公式、六维调研清单、置信度表达规则、业务理解段位 | 2026-06-08 |
| [[sources/expert-judgment-extraction-ai-readable]] | raw/notes/经验提取（可ai读）.md | 专家判断显性化、六层提取流程、强制约束、反模式、场景适配 | 2026-06-08 |
| [[sources/deep-demand-discovery-ai-readable]] | raw/notes/挖透需求（可ai读）.md | 五层需求挖掘、5Why、AI 场景价值判断、价值估算、说服叙事 | 2026-06-08 |

### outputs/
| 页面 | 输出类型 | 创建日期 |
|------|---------|---------|