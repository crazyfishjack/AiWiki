---
title: "Gitea Actions 部署 job 需要显式安装 kubectl"
kind: workflow
domain: workflows
aliases:
  - "deploy job kubectl missing"
  - "Gitea Actions 安装 kubectl"
created: 2026-06-08
updated: 2026-06-08
confidence: medium
status: active
sources:
  - "[[sources/cicd-failure-summary]]"
source-count: 1
relations:
  related-to:
    - "[[gitea-actions-expression-compatibility]]"
  is-part-of: []
  depends-on: []
  contradicts: []
  supersedes: []
  derived-from: []
tags: ["CICD失败经验总结"]
---

## 定义

Gitea Actions 部署 job 显式安装 `kubectl`，是指 deploy workflow 在执行 Kubernetes 同步命令前，需要先确保 job 容器中存在 `kubectl`，不能假设 runner 镜像已预装。

---

## 失败现象

部署阶段失败：

```text
/var/run/act/workflow/7.sh: line 9: kubectl: command not found
Failure - Main Sync APP_ENV to Kubernetes
```

自定义 `deploy.yaml` 直接执行了：

```bash
kubectl create secret ...
kubectl set image ...
kubectl rollout status ...
```

但 Gitea Actions runner 的 job 容器没有预装 `kubectl`。

---

## 处理流程

在 `Configure kubeconfig` 之前增加安装步骤：

```yaml
- name: Install kubectl
  uses: azure/setup-kubectl@v4
  with:
    version: "v1.30.7"
```

`kubectl` 安装必须早于所有 `kubectl create secret`、`kubectl set image`、`kubectl rollout status` 等步骤。

---

## 验证结果

已验证修复提交：

```text
3ab5a33 ci: install kubectl before deploy steps
```

---

## 关联说明

- [[gitea-actions-expression-compatibility]] — related-to — 两者都属于 Gitea Actions deploy workflow 的运行时兼容和前置条件问题。

---

## 来源

- [[sources/cicd-failure-summary]] — 提供缺少 `kubectl` 的错误文本、根因、安装步骤和修复提交。
