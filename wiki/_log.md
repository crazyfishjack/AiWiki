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
