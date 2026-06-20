---
title: "前端 Docker 构建不应默认强制使用 npmmirror"
kind: decision
domain: decisions
aliases:
  - "前端镜像 npm registry 选择"
  - "npmmirror 404 构建失败"
created: 2026-06-08
updated: 2026-06-08
confidence: medium
status: active
sources:
  - "[[sources/cicd-failure-summary]]"
source-count: 1
relations:
  related-to:
    - "[[uv-sync-python-upper-bound]]"
  is-part-of: []
  depends-on: []
  contradicts: []
  supersedes: []
  derived-from: []
tags: ["CICD失败经验总结"]
---

## 定义

前端 Docker 构建不默认强制使用 npmmirror，是一条 CI/CD 历史决策：当锁文件依赖在镜像源不可用时，镜像构建应显式切回 npm 官方 registry，以保证依赖可解析。

---

## 失败现象

前端镜像构建失败，错误文本为：

```text
npm error 404 Not Found - GET https://cdn.npmmirror.com/packages/electron-to-chromium/1.5.367/...
electron-to-chromium@... is not in this registry
```

原始 `frontend/Dockerfile` 强制使用：

```dockerfile
RUN npm config set registry https://registry.npmmirror.com && npm ci
```

但 `package-lock.json` 锁定的 `electron-to-chromium@1.5.367` 在 `npmmirror` 当前不可用，导致 `npm ci` 失败。本地验证 npm 官方 registry 可正常获取该包。

---

## 决策

前端 Docker 构建改为使用 npm 官方 registry：

```dockerfile
RUN npm ci --registry=https://registry.npmjs.org
```

验证命令：

```bash
npm ci --registry=https://registry.npmjs.org
npm run build
```

---

## 适用边界

该决策适用于依赖锁文件已经固定、但镜像源缺包或同步滞后导致 CI 构建失败的情况。若后续有公司内网 npm proxy 且能保证完整性和时效性，可重新评估 registry 策略。

---

## 验证结果

已验证修复提交：

```text
f3e6247 ci: use npm registry for frontend image build
```

---

## 关联说明

- [[uv-sync-python-upper-bound]] — related-to — 两者都是 CI/Docker 构建中依赖解析环境与实际依赖兼容性不匹配导致的失败经验。

---

## 来源

- [[sources/cicd-failure-summary]] — 提供 npm 404 错误、Dockerfile 原配置、修复配置、验证命令和修复提交。
