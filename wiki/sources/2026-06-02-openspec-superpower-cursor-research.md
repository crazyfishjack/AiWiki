---
title: "OpenSpec + Superpowers 结合 Cursor 开发的方式"
kind: source-summary
original-path: "raw/articles/2026-06-02-openspec-superpower-cursor-research.md"
original-url: ""
source-type: article
ingested: 2026-06-02
updated: 2026-06-02
original-date: 2026-06-02
source-quality: medium
pages-created:
  - "[[openspec]]"
  - "[[superpowers]]"
  - "[[openspec-superpowers-cursor-workflow]]"
pages-updated: []
contradictions-found: []
---

## 核心摘要

该调研报告梳理了 OpenSpec、Superpowers 与 Cursor 组合使用的 AI 辅助开发方式。报告认为 OpenSpec 适合管理规格、变更提案、任务和归档，Superpowers 适合约束 Cursor 代理的规划、TDD、调试和评审等工程行为，Cursor 则作为实际执行环境。报告同时强调该组合不适合所有任务，尤其对一次性脚本、小型低风险改动可能过重，并指出安装细节、版本号、GitHub Star 数等社区说法仍需官方来源验证。

---

## 关键观点

1. OpenSpec 更适合承担“规格与变更管理”角色，用于降低需求偏移和历史决策丢失风险。
2. Superpowers 更适合承担“开发行为纪律”角色，用于引导 Cursor 代理执行规划、TDD、调试和代码审查。
3. OpenSpec 与 Superpowers 解决不同层面的问题：前者约束“做什么、为什么”，后者约束“怎么做”。
4. OpenSpec + Superpowers + Cursor 的组合更适合复杂、长期、跨模块或需要审计的项目。
5. 该组合存在衔接点断裂、规格与代码漂移、流程过重和测试形式化等风险。
6. 部分社区数字和安装细节缺少官方验证，不应作为稳定事实写入知识页。

---

## 对 Wiki 的影响

### 新建的知识点

- [[openspec]] — 记录 OpenSpec 在 AI 编程中的规格驱动开发定位。
- [[superpowers]] — 记录 Superpowers 在 Cursor 中的开发流程约束定位。
- [[openspec-superpowers-cursor-workflow]] — 记录二者结合 Cursor 的推荐工作流和适用边界。

### 更新的知识点

无。

### 发现的矛盾

无正式页面矛盾；报告中保留了若干待验证声明，例如 Superpowers Star 数、OpenSpec npm 包版本和 Cursor 安装路径。

---

## 原文摘录

> OpenSpec 是面向 AI 智能体的轻量级规范驱动开发框架，通过“提案-审查-实施-归档”工作流，解决 AI 编程中的需求偏移与不可预测性问题。

> Superpowers 是一个为 Cursor 设计的软件开发工作流系统，提供头脑风暴、测试驱动开发、系统化调试、编写和执行计划、子代理驱动开发、Git Worktrees、代码审查工作流、自定义技能创建等能力。

> 社区对 OpenSpec 与 Superpowers 的分工概括为：一个管行为纪律，一个管规格管理；它们解决的是不同层面的问题。
