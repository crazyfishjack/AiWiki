---
title: "Kubernetes rollout timeout 的 CI 诊断输出流程"
kind: workflow
domain: workflows
aliases:
  - "rollout timeout diagnostics"
  - "Kubernetes 部署超时诊断"
created: 2026-06-08
updated: 2026-06-08
confidence: medium
status: active
sources:
  - "[[sources/cicd-failure-summary]]"
source-count: 1
relations:
  related-to:
    - "[[python-src-layout-docker-pythonpath]]"
  is-part-of: []
  depends-on:
    - "[[gitea-actions-kubectl-install]]"
  contradicts: []
  supersedes: []
  derived-from: []
tags: ["CICD失败经验总结"]
---

## 定义

Kubernetes rollout timeout 的 CI 诊断输出流程，是指当 `kubectl rollout status` 超时后，在 workflow 中自动打印 Deployment、ReplicaSet、Pod、Events、describe 和日志信息，以便从 CI 日志继续定位真实根因。

---

## 触发场景

部署阶段失败：

```text
deployment.apps/wdz-demo-backend image updated
Waiting for deployment "wdz-demo-backend" rollout to finish:
1 out of 2 new replicas have been updated...
error: timed out waiting for the condition
```

这说明镜像已经成功更新到 Kubernetes Deployment，但新 Pod 没有在超时时间内全部 Ready。诊断输出显示：

```text
wdz-demo-backend ... CrashLoopBackOff
Last State: Terminated
Exit Code: 1
```

---

## 权限约束

CI 使用的 `ci-deployer` ServiceAccount 如果没有 `pods/log` 权限，workflow 无法直接读取容器日志：

```text
cannot get resource "pods/log" in API group "" in the namespace "wdz-demo"
```

即使无法读取日志，`get events`、`describe deployment`、`describe pod` 仍可能提供关键线索。

---

## 诊断命令清单

rollout 失败时应自动打印：

```bash
kubectl get deployment -n "$namespace" -o wide
kubectl get rs -n "$namespace" -o wide
kubectl get pods -n "$namespace" -o wide
kubectl get events -n "$namespace" --sort-by=.lastTimestamp | tail -n 80
kubectl describe deployment ...
kubectl describe pod ...
kubectl logs ... --all-containers --tail=200
kubectl logs ... --all-containers --previous --tail=200
```

---

## 诊断分支

- 如果 Pod 是 `CrashLoopBackOff`，优先检查 Python import path、启动命令、环境变量和容器日志。
- 如果 Pod 是 `ImagePullBackOff`，检查 Harbor 镜像 tag、`harbor-pull-secret` 和 namespace。
- 如果 readiness probe 失败，检查 Deployment probe path 是否为 `/health`，以及容器是否监听 `8000`。

---

## 验证结果

已验证修复提交：

```text
48969ab ci: dump Kubernetes diagnostics on deploy failure
```

---

## 关联说明

- [[gitea-actions-kubectl-install]] — depends-on — 诊断命令依赖 deploy job 中可用的 `kubectl`。
- [[python-src-layout-docker-pythonpath]] — related-to — 本次 rollout timeout 的最终根因是 Python `src/` 布局容器缺少 `PYTHONPATH`。

---

## 来源

- [[sources/cicd-failure-summary]] — 提供 rollout timeout 现象、CrashLoopBackOff 线索、权限限制、诊断命令和修复提交。
