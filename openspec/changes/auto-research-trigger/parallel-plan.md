# 并行开发计划

## 依赖关系图

```
Batch 0 (基础层)
├── 1.1-1.4 配置管理模块
├── 2.1-2.4 Issue 解析模块
├── 3.1-3.5 GitHub Actions Workflow
├── 9.1-9.2 依赖管理
└── 10.1 GitHub Secrets 配置

Batch 1 (核心逻辑层) ──依赖──▶ Batch 0
├── 4.1-4.4 调研执行模块
├── 5.1-5.6 LLM 编译模块
└── 8.1-8.5 主入口脚本（部分）

Batch 2 (输出层) ──依赖──▶ Batch 1
├── 6.1-6.5 Git 推送模块
├── 7.1-7.5 企业微信通知模块
└── 8.1-8.5 主入口脚本（剩余部分）

Batch 3 (验证层) ──依赖──▶ Batch 2
├── 10.2-10.4 测试验证
└── 11.1-11.3 文档交付
```

## Batch 分组详情

### Batch 0：基础层（可并行 Agent 数：2）

**Agent A 任务包：**
| 任务 | 说明 | 共享文件 |
|------|------|---------|
| 1.1 | 创建 config.example.json | `.github/scripts/config.example.json` |
| 1.2 | 实现 config_loader.py | `.github/scripts/config_loader.py` |
| 1.3 | 实现 validate_config() | `.github/scripts/config_loader.py` |
| 1.4 | 更新 .gitignore | `.gitignore` |
| 3.1 | 创建 auto-research.yml | `.github/workflows/auto-research.yml` |
| 3.2 | 配置 Python 环境 | `.github/workflows/auto-research.yml` |
| 3.3 | 配置 Secrets 注入 | `.github/workflows/auto-research.yml` |
| 3.4 | 配置执行步骤 | `.github/workflows/auto-research.yml` |
| 3.5 | 配置权限 | `.github/workflows/auto-research.yml` |
| 9.1 | 创建 requirements.txt | `.github/scripts/requirements.txt` |
| 9.2 | 验证依赖版本 | `.github/scripts/requirements.txt` |
| 10.1 | 配置 GitHub Secrets | GitHub 仓库设置（手动） |

**Agent A2 任务包（并行）：**
| 任务 | 说明 | 共享文件 |
|------|------|---------|
| 2.1 | 实现 issue_parser.py | `.github/scripts/issue_parser.py` |
| 2.2 | 实现查询提取逻辑 | `.github/scripts/issue_parser.py` |
| 2.3 | 实现 --query 参数 | `.github/scripts/issue_parser.py` |
| 2.4 | 非调研 issue 过滤 | `.github/scripts/issue_parser.py` |

**禁止同时修改的共享文件：** 无（Batch 0 内各任务包文件独立）

**Agent A 验收标准：**
- `config_loader.py` 可从环境变量和本地 JSON 加载配置
- `auto-research.yml` 语法正确，Actions 可识别
- `requirements.txt` 可成功安装

**Agent A2 验收标准：**
- `issue_parser.py` 可从 GitHub event JSON 提取 query
- `--query` 参数直接传入时跳过解析
- 非 `[调研]` 标题返回 None

---

### Batch 1：核心逻辑层（可并行 Agent 数：2）

**依赖：** Batch 0 完成（config_loader.py、issue_parser.py 可用）

**Agent B 任务包：**
| 任务 | 说明 | 共享文件 |
|------|------|---------|
| 4.1 | 实现 research_runner.py | `.github/scripts/research_runner.py` |
| 4.2 | 标准模式调用 | `.github/scripts/research_runner.py` |
| 4.3 | 输出捕获 | `.github/scripts/research_runner.py` |
| 4.4 | 调研失败处理 | `.github/scripts/research_runner.py` |
| 5.1 | 实现 llm_compiler.py | `.github/scripts/llm_compiler.py` |
| 5.2 | 提示词构造 | `.github/scripts/llm_compiler.py` |
| 5.3 | 阿里云 API 调用 | `.github/scripts/llm_compiler.py` |
| 5.4 | 重试机制 | `.github/scripts/llm_compiler.py` |
| 5.5 | 编译失败回退 | `.github/scripts/llm_compiler.py` |
| 5.6 | 编译结果写入 | `.github/scripts/llm_compiler.py` |
| 8.1 | 主入口框架 | `.github/scripts/run-research.py` |
| 8.2 | 管道编排（前半） | `.github/scripts/run-research.py` |
| 8.4 | 日志输出 | `.github/scripts/run-research.py` |

**禁止同时修改的共享文件：**
- `.github/scripts/run-research.py`（Agent B 和 Agent C 都需修改，需分阶段）

**Agent B 验收标准：**
- `research_runner.py` 成功调用 four_tool_research.py
- `llm_compiler.py` 成功调用阿里云 API 并生成中文报告
- `run-research.py` 可执行到 LLM 编译步骤

---

### Batch 2：输出层（可并行 Agent 数：2）

**依赖：** Batch 1 完成（research_runner.py、llm_compiler.py 可用）

**Agent C 任务包：**
| 任务 | 说明 | 共享文件 |
|------|------|---------|
| 6.1 | 实现 git_pusher.py | `.github/scripts/git_pusher.py` |
| 6.2 | git add | `.github/scripts/git_pusher.py` |
| 6.3 | git commit | `.github/scripts/git_pusher.py` |
| 6.4 | git push | `.github/scripts/git_pusher.py` |
| 6.5 | 冲突处理 | `.github/scripts/git_pusher.py` |
| 7.1 | 实现 wechat_notifier.py | `.github/scripts/wechat_notifier.py` |
| 7.2 | 成功通知模板 | `.github/scripts/wechat_notifier.py` |
| 7.3 | 失败通知模板 | `.github/scripts/wechat_notifier.py` |
| 7.4 | webhook 缺失处理 | `.github/scripts/wechat_notifier.py` |
| 7.5 | 通知失败不影响管道 | `.github/scripts/wechat_notifier.py` |
| 8.3 | 错误处理 | `.github/scripts/run-research.py` |
| 8.5 | 退出码 | `.github/scripts/run-research.py` |

**Agent C2 任务包（并行，辅助）：**
| 任务 | 说明 | 共享文件 |
|------|------|---------|
| 8.2 | 管道编排（后半，git + notify） | `.github/scripts/run-research.py` |

**禁止同时修改的共享文件：**
- `.github/scripts/run-research.py`（Agent C 和 Agent C2 需协调）

**Agent C 验收标准：**
- `git_pusher.py` 成功 commit 并 push
- `wechat_notifier.py` 成功发送企业微信消息
- `run-research.py` 完整管道可执行

---

### Batch 3：验证层（可并行 Agent 数：1）

**依赖：** Batch 2 完成（完整管道可用）

**Agent D 任务包：**
| 任务 | 说明 | 共享文件 |
|------|------|---------|
| 10.2 | 本地测试 | `.github/scripts/run-research.py` |
| 10.3 | 创建测试 issue | GitHub Issues（手动） |
| 10.4 | 验证企业微信通知 | 企业微信（手动验证） |
| 11.1 | 创建 README.md | `.github/scripts/README.md` |
| 11.2 | 更新项目主 README | `README.md` |
| 11.3 | 端到端验证 | 完整流程 |

**禁止同时修改的共享文件：** 无

**Agent D 验收标准：**
- 本地 `--query` 测试通过
- GitHub Actions 触发测试通过
- 企业微信通知收到
- README 文档完整

---

## 执行顺序与并行策略

```
时间轴 ──────────────────────────────────────────────────────▶

Batch 0  [Agent A  ] ████████████████████████████████████████
         [Agent A2 ] ████████████████████████████████████████
                          │
                          ▼ 等待 Batch 0 完成
Batch 1  [Agent B  ]       ████████████████████████████████████████
                          │
                          ▼ 等待 Batch 1 完成
Batch 2  [Agent C  ]             ████████████████████████████████████████
         [Agent C2 ]             ████████████████████████████████████████
                          │
                          ▼ 等待 Batch 2 完成
Batch 3  [Agent D  ]                   ████████████████████████████████████████
```

**关键路径：**
1. Batch 0（Agent A + A2 并行）→ 2. Batch 1（Agent B）→ 3. Batch 2（Agent C + C2 并行）→ 4. Batch 3（Agent D）

**最短总时间估算：**
- Batch 0：~30 分钟（2 Agent 并行）
- Batch 1：~45 分钟（1 Agent）
- Batch 2：~30 分钟（2 Agent 并行）
- Batch 3：~30 分钟（1 Agent）
- **总计：~2.5 小时**（不含等待和测试时间）

## 风险与缓解

| 风险 | 影响 Batch | 缓解措施 |
|------|-----------|---------|
| run-research.py 多 Agent 修改冲突 | Batch 1-2 | Agent B 负责前半部分（config→research→llm），Agent C 负责后半部分（git→notify→error handling），最后 Agent C2 整合 |
| 阿里云 API 参数不确定 | Batch 1 | 在 Batch 0 结束前确认 API endpoint，否则 Agent B 阻塞 |
| GitHub Actions 权限问题 | Batch 2 | Batch 0 中配置 `contents: write`，Batch 3 中验证 |
| 企业微信 webhook 测试困难 | Batch 2-3 | 先用 curl 测试 webhook，再集成到脚本 |
