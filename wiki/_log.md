---
title: "操作日志"
---

# 操作日志

<!-- 规则：
  - append-only，只追加，永不修改历史记录
  - 每条记录以 ## [日期] 操作类型 | 标题 开头
  - 便于 grep 解析：grep "^## \[" _log.md
-->

## [2026-05-31] init | Wiki 初始化
- 操作：创建 Wiki 基础目录结构
- 创建目录：raw/articles/, raw/papers/, raw/notes/, raw/projects/
- 创建目录：wiki/_inbox/, wiki/sources/, wiki/outputs/, wiki/concepts/, wiki/tools/
- 创建文件：wiki/_index.md, wiki/_log.md, wiki/_graph.md
- 状态：完成

## [2026-06-02] ingest | 2026-06-02-openspec-superpower-cursor-research.md
- 来源页面：[[sources/2026-06-02-openspec-superpower-cursor-research]]
- 新建知识点（3 个）：[[openspec]], [[superpowers]], [[openspec-superpowers-cursor-workflow]]
- 更新知识点（0 个）：无
- 新建域文件夹：无
- 迁移文件（如有）：无
- 发现矛盾：无
- 新增关联（5 条）：related-to [[openspec]] ↔ [[superpowers]], related-to [[openspec]] ↔ [[openspec-superpowers-cursor-workflow]], related-to [[superpowers]] ↔ [[openspec-superpowers-cursor-workflow]], depends-on [[openspec-superpowers-cursor-workflow]] → [[openspec]], depends-on [[openspec-superpowers-cursor-workflow]] → [[superpowers]]

## [2026-06-02] ingest | 2026-06-02-openspec-superpowers-cursor-command-workflow-research.md
- 来源页面：[[sources/2026-06-02-openspec-superpowers-cursor-command-workflow-research]]
- 新建知识点（0 个）：无
- 更新知识点（3 个）：[[openspec]], [[superpowers]], [[openspec-superpowers-cursor-workflow]]
- 新建域文件夹：无
- 迁移文件（如有）：无
- 发现矛盾：无
- 新增关联（0 条）：无

## [2026-06-02] reorganize | 信息保真规则优化
- 更新 SCHEMA.md：知识点正文改为 AI 自适应结构，来源摘要页改为保真来源页
- 新增规则：retention-level、retained-sections、omitted-sections、必保留信息清单、入库保真检查
- 更新页面：[[sources/2026-06-02-openspec-superpowers-cursor-command-workflow-research]], [[openspec-superpowers-cursor-workflow]]
- 更新 _index.md：sources 表增加摘要/关键词列
- 发现矛盾：无

## [2026-06-02] ingest | 2026-06-02-openspec-superpowers-cursor-command-workflow-research.md (reingest)
- 来源页面：[[sources/2026-06-02-openspec-superpowers-cursor-command-workflow-research]]
- 新建知识点（0 个）：无
- 更新知识点（3 个）：[[openspec]], [[superpowers]], [[openspec-superpowers-cursor-workflow]]
- 新建域文件夹：无
- 迁移文件（如有）：无
- 发现矛盾：无
- 新增关联（0 条）：无
- 保真补录：补充 delta spec 写法、proposal 前检查命令、逐来源总结、Superpowers Agent chat 使用边界

## [2026-06-08] ingest | CICD_FAILURE_SUMMARY.md
- 来源页面：[[sources/cicd-failure-summary]]
- 新建知识点（7 个）：[[gitea-actions-expression-compatibility]], [[provision-workflow-merge-deduplication]], [[uv-sync-python-upper-bound]], [[npm-registry-frontend-docker-build]], [[gitea-actions-kubectl-install]], [[kubernetes-rollout-timeout-diagnostics]], [[python-src-layout-docker-pythonpath]]
- 更新知识点（0 个）：无
- 新建域文件夹：无
- 迁移文件（如有）：无
- 发现矛盾：无
- 新增关联（6 条）：related-to [[gitea-actions-expression-compatibility]] ↔ [[provision-workflow-merge-deduplication]], related-to [[gitea-actions-expression-compatibility]] ↔ [[gitea-actions-kubectl-install]], related-to [[uv-sync-python-upper-bound]] ↔ [[npm-registry-frontend-docker-build]], related-to [[uv-sync-python-upper-bound]] ↔ [[python-src-layout-docker-pythonpath]], related-to [[kubernetes-rollout-timeout-diagnostics]] ↔ [[python-src-layout-docker-pythonpath]], depends-on [[kubernetes-rollout-timeout-diagnostics]] → [[gitea-actions-kubectl-install]]
- 保真检查：retention-level=detailed；已保留=[failure-symptoms, root-causes, commands, configuration-snippets, diagnostic-workflow, fix-commits, follow-up-recommendations]；舍弃=无
- 标记：全部新建知识点 tags 包含 `CICD失败经验总结`

## [2026-06-08] reorganize | 归域 _inbox 知识点
- 触发条件：用户要求检查 _inbox 并将可归域知识点迁移到相应域；workflow 类知识点数量达到 5 个，新增 workflows/ 域；decision 类页面按明确类型新增 decisions/ 域
- 新建域文件夹：workflows/, decisions/
- 迁移文件：[[openspec]], [[superpowers]] → tools/；[[openspec-superpowers-cursor-workflow]], [[provision-workflow-merge-deduplication]], [[uv-sync-python-upper-bound]], [[gitea-actions-kubectl-install]], [[kubernetes-rollout-timeout-diagnostics]] → workflows/；[[gitea-actions-expression-compatibility]], [[python-src-layout-docker-pythonpath]] → concepts/；[[npm-registry-frontend-docker-build]] → decisions/
- 更新 _index.md：已登记 workflows/ 与 decisions/ 域，并将 _inbox/ 页面数更新为 0
- 检查 _graph.md：wikilinks 使用文件名且未发生重命名，关系路径无需修改

## [2026-06-08] ingest | 调研方法论（可ai读）.md
- 来源页面：[[sources/research-methodology-ai-readable]]
- 新建知识点（1 个）：[[spin-consultative-sales-questioning]]
- 更新知识点（0 个）：无
- 新建域文件夹：无
- 迁移文件（如有）：无
- 发现矛盾：无
- 新增关联（1 条）：related-to [[spin-consultative-sales-questioning]] ↔ [[business-understanding-framework]]
- 保真检查：retention-level=detailed；已保留=[spin-framework, situation-problem-transition, question-examples, hidden-to-explicit-needs, b2b-job-levels, role-job-matrix]；舍弃=无

## [2026-06-08] ingest | 读懂业务（可ai读）.md
- 来源页面：[[sources/business-understanding-ai-readable]]
- 新建知识点（1 个）：[[business-understanding-framework]]
- 更新知识点（0 个）：无
- 新建域文件夹：无
- 迁移文件（如有）：无
- 发现矛盾：无
- 新增关联（2 条）：related-to [[spin-consultative-sales-questioning]] ↔ [[business-understanding-framework]], related-to [[business-understanding-framework]] ↔ [[expert-judgment-extraction-workflow]]
- 保真检查：retention-level=detailed；已保留=[business-formula, confidence-rules, research-dimensions, maturity-levels]；舍弃=无

## [2026-06-08] ingest | 经验提取（可ai读）.md
- 来源页面：[[sources/expert-judgment-extraction-ai-readable]]
- 新建知识点（1 个）：[[expert-judgment-extraction-workflow]]
- 更新知识点（0 个）：无
- 新建域文件夹：无
- 迁移文件（如有）：无
- 发现矛盾：无
- 新增关联（2 条）：related-to [[business-understanding-framework]] ↔ [[expert-judgment-extraction-workflow]], related-to [[expert-judgment-extraction-workflow]] ↔ [[deep-demand-discovery-workflow]]
- 保真检查：retention-level=detailed；已保留=[purpose-and-role, output-template, session-loop, six-layer-extraction, hard-constraints, anti-patterns, scenario-adaptations]；舍弃=[部分长篇示例话术已等价压缩，完整原文可回溯 raw]

## [2026-06-08] ingest | 挖透需求（可ai读）.md
- 来源页面：[[sources/deep-demand-discovery-ai-readable]]
- 新建知识点（1 个）：[[deep-demand-discovery-workflow]]
- 更新知识点（0 个）：无
- 新建域文件夹：无
- 迁移文件（如有）：无
- 发现矛盾：无
- 新增关联（3 条）：related-to [[expert-judgment-extraction-workflow]] ↔ [[deep-demand-discovery-workflow]], depends-on [[deep-demand-discovery-workflow]] → [[business-understanding-framework]], depends-on [[deep-demand-discovery-workflow]] → [[spin-consultative-sales-questioning]]
- 保真检查：retention-level=detailed；已保留=[five-layer-workflow, five-whys-example, value-criteria, value-estimation-formula, solution-reframing, persuasion-narrative, output-template]；舍弃=无