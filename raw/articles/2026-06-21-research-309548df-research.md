---
title: "调研证据包：医院导视 设计逻辑 导视设计 适老化 通用设计 地面导流"
source-type: article
generated: 2026-06-21
generated-by: wiki-research-skill
research-mode: standard
---

# 调研证据包：医院导视 设计逻辑 导视设计 适老化 通用设计 地面导流

## 调研问题

医院导视 设计逻辑 导视设计 适老化 通用设计 地面导流

## 摘要

本文档是四工具检索生成的证据包草稿，不是最终调研报告。Agent 必须先阅读本证据包，执行下方"AI 综合指令"，生成新的中文综合 raw 报告，然后询问用户是否入库。本证据包保留不删除。

- 发现候选信源：25
- 精读信源数量：10
- 精读成功数量：9
- 精读失败数量：1

## AI 综合指令（Agent 必须执行）

请基于本文档的候选信源和完整精读结果生成最终中文调研报告。最终报告必须编写为一个新的 raw Markdown 文件，并删除本文档这个证据包。最终报告必须满足：

1. 删除本“AI 综合指令”占位说明，保留必要原始证据摘录。
2. 用中文输出，不要只粘贴网页摘录。
3. 每条关键事实后标注 `[来源: URL]`。
4. 每条核心结论标注可信度：高 / 中 / 低。
5. 显式列出跨源矛盾、证据不足和待验证问题。
6. 不得把无 URL 支撑的内容写成事实；如确需提及，标注“未验证”。
7. 若本文档中的高可信来源精读失败、正文为空、明显不完整或只有导航/付费墙内容，必须二次精读；否则优先使用证据包中的完整精读结果。
8. 必须包含 `## 对于可信度较高的来源逐来源总结`，逐篇整理高可信来源的核心内容、可用事实、局限和适合入库的知识点。
9. 对重要来源进行完整性检查：若本文档精读结果不足以覆盖正文，应重新读取或抓取该来源全文后再生成最终报告，不得只依赖不完整内容。
10. 必须保留 `## 信源质量门控记录`，列出保留信源、剔除信源、来源等级、保留/剔除原因和后续处理。
11. 必须保留 `## 跨源矛盾检测结论`，逐项检测核心数字、日期、功能描述、因果判断、市场/公司事实。
12. 入库到 `wiki/sources/` 时，来源等级按 A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low` 映射。

最终报告结构必须包含：

- `## 核心结论`：3-7 条可复用结论，每条带来源和可信度。
- `## 内容整理`：保留所有有用的信息，系统化，结构清晰，逻辑正确。
- `## 推荐工作流`：说明如何组合使用这些工具，明确 Cursor 中的执行步骤。
- `## 适用场景`：列出适合采用该方法的项目类型。
- `## 不适用场景`：说明何时会过度工程或不值得引入。
- `## 风险与约束`：列出衔接点、上下文、测试、规格漂移等风险。
- `## 信源质量门控记录`：记录门控规则、保留信源、剔除信源和 A/B/C/D 来源等级。
- `## 来源与可信度`：逐项列出关键来源、来源类型、可信度和支撑内容。
- `## 对于可信度较高的来源逐来源总结`：逐篇整理高可信来源正文，不只提取少量核心结论。
- `## 跨源矛盾检测结论`：说明检测范围、检测结果和所有矛盾项；未发现矛盾也必须明确写出。
- `## 矛盾与待验证问题`：保留冲突或证据不足处。
- `## 原始证据摘录`：保留支持结论的必要摘录或完整证据片段。

本证据包默认保存完整精读结果，不对 Firecrawl/Jina 正文做字符截断。若配置关闭全文证据模式，才会回退为摘录模式。
- 证据包全文模式：true
- 兼容摘录上限：2000 字符（仅在全文模式关闭时使用）
- 若某来源精读失败、正文为空、疑似反爬/付费墙/导航页或工具返回明显不完整，Agent 必须二次精读或标注不可验证。

## 候选信源

| 工具 | 分数 | 标题 | URL |
|------|-------|-------|-----|
| exa | 1.00 | Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan | https://www.mdpi.com/2220-9964/10/8/570 |
| exa | 1.00 | Improving wayfinding in hospitals for people with diverse needs and abilities: An exploratory approach based on multi-criteria decision making | https://www.sciencedirect.com/science/article/abs/pii/S0003687023001874 |
| exa | 1.00 | Exploring Sign System Design for a Medical Facility: A Virtual Environment Study on Wayfinding Behaviors | https://www.mdpi.com/2075-5309/13/6/1366 |
| exa | 1.00 | Implementation of Wayfinding Signage in Public Hospitals and Its Evaluation Towards Quality Improvement - PMC | https://pmc.ncbi.nlm.nih.gov/articles/PMC11345034/ |
| exa | 1.00 | Elderly users’ perceptions of signage systems from tertiary hospitals in Guangzhou | https://pmc.ncbi.nlm.nih.gov/articles/PMC10840000/ |
| exa | 1.00 |  | http://www.nature.com/articles/s41598-025-20128-0.pdf |
| exa | 1.00 | A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness | https://pmc.ncbi.nlm.nih.gov/articles/PMC9656047/ |
| exa | 1.00 | Frontiers \| Enhancing the digital adoption in healthcare built environments: a framework for a therapeutic user-based wayfinding system | https://www.frontiersin.org/journals/medical-technology/articles/10.3389/fmedt.2025.1323446/full |
| exa | 1.00 | Optimized Wayfinding Signage Positioning in Hospital Built Environment through Medical Data and Flows Simulations | https://www.mdpi.com/2075-5309/12/9/1426 |
| exa | 1.00 | Aging Adaptation Transition of Health Care Buildings for Accessibility Optimization for the Elderly | https://www.mdpi.com/2075-5309/15/3/379 |
| exa | 1.00 | Enhancing Disaster Resilience in Hospitals Through Flow Space-Optimized Evacuation Routes | https://www.mdpi.com/2071-1050/17/12/5419 |
| exa | 1.00 | A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness | https://www.mdpi.com/1660-4601/19/21/13885 |
| exa | 1.00 | Research on Optimization Design of Corridor Entry Space of Elderly Facilities Based on Visual–Perceptual and Electroencephalogram Feedback Mechanisms | https://www.mdpi.com/2075-5309/14/11/3370 |
| exa | 1.00 | Adaptive Aging Safety of Guidance Marks in Rail Transit Connection Systems Based on Eye Movement Data | https://pmc.ncbi.nlm.nih.gov/articles/PMC8775515/ |
| exa | 1.00 | 虚拟现实技术联合电磁导航手术机器人辅助治疗复杂骨盆骨折一例 - PMC | https://pmc.ncbi.nlm.nih.gov/articles/PMC8171533/ |
| tavily | 0.64 | 友善设计——老年医院导视系统的适老化设计实践探究-维普期刊 中文期刊服务平台 | http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688&from=Qikan_Article_Detail |
| tavily | 0.61 | 筑医台--HCD医养设计--医院导视标识的前世今生 | http://hcd.zhuyitai.com/journals/hcd/article/d2195d017b9249f296ad72725c7ed2f6 |
| tavily | 0.58 | [PDF] 基于案例分析的国内外医疗机构导视系统设计现状研究 | https://pdf.hanspub.org/design202496_1871181613.pdf |
| tavily | 0.58 | 适老化视阙下医院导视设计策略探究 | https://www.hanspub.org/journal/paperinformation?paperid=71956 |
| tavily | 0.57 | 〖梅奥艺术〗设计医院导视制作分享_梅奥艺术设计-站酷ZCOOL | https://m.zcool.com.cn/article/ZMTU3ODM2OA==.html |
| tavily | 0.55 | [PDF] 积极老龄化视角下社区公共导视系统适老化设计研究 | https://pdf.hanspub.org/ar_3141153.pdf |
| tavily | 0.53 | 医院医疗标识导视系统设计素材_医院医疗标识导视系统设计模板_医院医疗标识导视系统设计设计图片免费下载-众图网 | https://www.ztupic.com/tupian/yiyuanyiliaobiaoshidaoshixitongsheji.html |
| tavily | 0.43 | 微信长辈就医适老化设计规范 \| 微信服务号文档 | https://developers.weixin.qq.com/doc/service/guide/product/elderMedical/elderMedical-designstandards.html |
| tavily | 0.42 | 专家观点 - 智慧医院产品观（十一）：适老化设计-中国医院协会信息专业委员会 | https://www.chima.org.cn/Html/News/Articles/15495.html |
| tavily | 0.41 | 医院导视系统 | https://www.pinterest.com/ideas/%E5%8C%BB%E9%99%A2%E5%AF%BC%E8%A7%86%E7%B3%BB%E7%BB%9F/948575276788 |

## 信源质量门控记录

### 门控规则
- Tavily score < 0.4：剔除
- 已知低质域名：剔除
- 重复 URL：合并保留最高分结果
- Exa 学术/语义结果：默认保留，但进入来源等级评估
- C/D 级来源不得作为唯一结论依据
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`

### 保留信源
1. [Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan](https://www.mdpi.com/2220-9964/10/8/570)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
2. [Improving wayfinding in hospitals for people with diverse needs and abilities: An exploratory approach based on multi-criteria decision making](https://www.sciencedirect.com/science/article/abs/pii/S0003687023001874)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
3. [Exploring Sign System Design for a Medical Facility: A Virtual Environment Study on Wayfinding Behaviors](https://www.mdpi.com/2075-5309/13/6/1366)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
4. [Implementation of Wayfinding Signage in Public Hospitals and Its Evaluation Towards Quality Improvement - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11345034/)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
5. [Elderly users’ perceptions of signage systems from tertiary hospitals in Guangzhou](https://pmc.ncbi.nlm.nih.gov/articles/PMC10840000/)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
6. [http://www.nature.com/articles/s41598-025-20128-0.pdf](http://www.nature.com/articles/s41598-025-20128-0.pdf)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
7. [A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness](https://pmc.ncbi.nlm.nih.gov/articles/PMC9656047/)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
8. [Frontiers | Enhancing the digital adoption in healthcare built environments: a framework for a therapeutic user-based wayfinding system](https://www.frontiersin.org/journals/medical-technology/articles/10.3389/fmedt.2025.1323446/full)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
9. [Optimized Wayfinding Signage Positioning in Hospital Built Environment through Medical Data and Flows Simulations](https://www.mdpi.com/2075-5309/12/9/1426)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
10. [Aging Adaptation Transition of Health Care Buildings for Accessibility Optimization for the Elderly](https://www.mdpi.com/2075-5309/15/3/379)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
11. [Enhancing Disaster Resilience in Hospitals Through Flow Space-Optimized Evacuation Routes](https://www.mdpi.com/2071-1050/17/12/5419)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
12. [A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness](https://www.mdpi.com/1660-4601/19/21/13885)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
13. [Research on Optimization Design of Corridor Entry Space of Elderly Facilities Based on Visual–Perceptual and Electroencephalogram Feedback Mechanisms](https://www.mdpi.com/2075-5309/14/11/3370)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
14. [Adaptive Aging Safety of Guidance Marks in Rail Transit Connection Systems Based on Eye Movement Data](https://pmc.ncbi.nlm.nih.gov/articles/PMC8775515/)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
15. [虚拟现实技术联合电磁导航手术机器人辅助治疗复杂骨盆骨折一例 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8171533/)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
16. [友善设计——老年医院导视系统的适老化设计实践探究-维普期刊 中文期刊服务平台](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688&from=Qikan_Article_Detail)
   - 工具：tavily
   - 分数：0.64
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
17. [筑医台--HCD医养设计--医院导视标识的前世今生](http://hcd.zhuyitai.com/journals/hcd/article/d2195d017b9249f296ad72725c7ed2f6)
   - 工具：tavily
   - 分数：0.61
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
18. [[PDF] 基于案例分析的国内外医疗机构导视系统设计现状研究](https://pdf.hanspub.org/design202496_1871181613.pdf)
   - 工具：tavily
   - 分数：0.58
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
19. [适老化视阙下医院导视设计策略探究](https://www.hanspub.org/journal/paperinformation?paperid=71956)
   - 工具：tavily
   - 分数：0.58
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
20. [〖梅奥艺术〗设计医院导视制作分享_梅奥艺术设计-站酷ZCOOL](https://m.zcool.com.cn/article/ZMTU3ODM2OA==.html)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
21. [[PDF] 积极老龄化视角下社区公共导视系统适老化设计研究](https://pdf.hanspub.org/ar_3141153.pdf)
   - 工具：tavily
   - 分数：0.55
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
22. [医院医疗标识导视系统设计素材_医院医疗标识导视系统设计模板_医院医疗标识导视系统设计设计图片免费下载-众图网](https://www.ztupic.com/tupian/yiyuanyiliaobiaoshidaoshixitongsheji.html)
   - 工具：tavily
   - 分数：0.53
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
23. [微信长辈就医适老化设计规范 | 微信服务号文档](https://developers.weixin.qq.com/doc/service/guide/product/elderMedical/elderMedical-designstandards.html)
   - 工具：tavily
   - 分数：0.43
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
24. [专家观点 - 智慧医院产品观（十一）：适老化设计-中国医院协会信息专业委员会](https://www.chima.org.cn/Html/News/Articles/15495.html)
   - 工具：tavily
   - 分数：0.42
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
25. [医院导视系统](https://www.pinterest.com/ideas/%E5%8C%BB%E9%99%A2%E5%AF%BC%E8%A7%86%E7%B3%BB%E7%BB%9F/948575276788)
   - 工具：tavily
   - 分数：0.41
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考

### 剔除信源
1. [医院导视系统](https://www.pinterest.com/ideas/%E5%8C%BB%E9%99%A2%E5%AF%BC%E8%A7%86%E7%B3%BB%E7%BB%9F/948575276788)
   - 工具：tavily
   - 分数：0.37
   - 来源等级：C
   - 剔除原因：score 低于 0.4
2. [导视美学](http://www.comvery.com/case/show/523)
   - 工具：tavily
   - 分数：0.36
   - 来源等级：C
   - 剔除原因：score 低于 0.4
3. [[PDF] 《互联网网站适老化通用设计规范》 交 流 会](https://www.w3.org/2021/05/29-older-users-and-accessibility/slides/slides-huangchang.pdf)
   - 工具：tavily
   - 分数：0.24
   - 来源等级：C
   - 剔除原因：score 低于 0.4
4. [友善设计——老年医院导视系统的适老化设计实践探究-维普期刊 中文期刊服务平台](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688&from=Qikan_Article_Detail)
   - 工具：tavily
   - 分数：0.53
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
5. [[PDF] 基于案例分析的国内外医疗机构导视系统设计现状研究](https://pdf.hanspub.org/design202496_1871181613.pdf)
   - 工具：tavily
   - 分数：0.52
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
6. [适老化视阙下医院导视设计策略探究](https://www.hanspub.org/journal/paperinformation?paperid=71956)
   - 工具：tavily
   - 分数：0.48
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
7. [医院导视系统](https://www.pinterest.com/ideas/%E5%8C%BB%E9%99%A2%E5%AF%BC%E8%A7%86%E7%B3%BB%E7%BB%9F/948575276788)
   - 工具：tavily
   - 分数：0.32
   - 来源等级：C
   - 剔除原因：score 低于 0.4
8. [导视美学](http://www.comvery.com/case/show/523)
   - 工具：tavily
   - 分数：0.31
   - 来源等级：C
   - 剔除原因：score 低于 0.4
9. [微信长辈就医适老化设计规范 | 微信服务号文档](https://developers.weixin.qq.com/doc/service/guide/product/elderMedical/elderMedical-designstandards.html)
   - 工具：tavily
   - 分数：0.30
   - 来源等级：A
   - 剔除原因：score 低于 0.4
10. [上海长征医院导视系统设计 :: Behance](https://www.behance.net/gallery/137875995/_)
   - 工具：tavily
   - 分数：0.29
   - 来源等级：C
   - 剔除原因：score 低于 0.4
11. [上海长征医院导视系统设计 :: Behance](https://www.behance.net/gallery/137875995/_?locale=zh_CN)
   - 工具：tavily
   - 分数：0.29
   - 来源等级：C
   - 剔除原因：score 低于 0.4
12. [[PDF] 《互联网网站适老化通用设计规范》 交 流 会](https://www.w3.org/2021/05/29-older-users-and-accessibility/slides/slides-huangchang.pdf)
   - 工具：tavily
   - 分数：0.24
   - 来源等级：C
   - 剔除原因：score 低于 0.4
13. [[PDF] 《移动互联网应用(APP)适老化通用设计规范》解读](https://www.w3.org/2021/05/29-older-users-and-accessibility/slides/slides-dingliting.pdf)
   - 工具：tavily
   - 分数：0.23
   - 来源等级：C
   - 剔除原因：score 低于 0.4
14. [Opmed and Mayo Clinic Unveil Multimodal AI Platform at ACC.26 to Optimize Surgical Capacity - HIT Consultant](https://hitconsultant.net/2026/06/18/opmed-mayo-clinic-cardiovascular-ai-scheduling/)
   - 工具：tavily
   - 分数：0.09
   - 来源等级：C
   - 剔除原因：score 低于 0.4
15. [Collaborative success in hospital renovation: Gillette Children's OR upgrade - Building Design + Construction](https://www.bdcnetwork.com/building-sector-reports/healthcare-facilities/blog/55385013/collaborative-success-in-hospital-renovation-gillette-childrens-or-upgrade)
   - 工具：tavily
   - 分数：0.08
   - 来源等级：C
   - 剔除原因：score 低于 0.4
16. [More Americans Have a Plan to Age in Place - WSJ](https://www.wsj.com/lifestyle/relationships/americans-aging-housing-0e073f48)
   - 工具：tavily
   - 分数：0.04
   - 来源等级：C
   - 剔除原因：score 低于 0.4
17. [Ultra-wealthy home buyers are clamoring to have longevity amenities within easy reach - New York Post](https://nypost.com/2026/06/16/real-estate/newest-real-estate-amenity-among-the-rich-longevity/)
   - 工具：tavily
   - 分数：0.04
   - 来源等级：C
   - 剔除原因：score 低于 0.4
18. [The highlights from 3 Days of Design 2026 - Vogue Australia](https://www.vogue.com.au/vogue-living/events/3-days-of-design-2026/image-gallery/82b17f6883142de0566ae2737927be17)
   - 工具：tavily
   - 分数：0.02
   - 来源等级：C
   - 剔除原因：score 低于 0.4
19. [Maze Design Basel fair returns for second edition with more exhibitors—and art - The Art Newspaper](https://www.theartnewspaper.com/2026/06/17/maze-design-basel-returns-for-second-edition-with-more-exhibitorsand-art)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
20. [7 Highlights From Copenhagen’s 3 Days of Design - Vogue](https://www.vogue.com/article/3-days-of-design-copenhagen-2026-highlights)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
21. [Photos show how the Ebola outbreak is changing nightlife in Congo - Greenwich Time](https://www.greenwichtime.com/news/article/photos-show-how-the-ebola-outbreak-is-changing-22305457.php)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
22. [City shows off models of proposed sidewalk sheds - New York Post](https://nypost.com/2026/06/14/business/city-shows-off-models-of-proposed-sidewalk-sheds/)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
23. [Measuring children’s spatial accessibility to urban park green spaces - Nature](https://www.nature.com/articles/s41598-026-48526-y)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：A
   - 剔除原因：score 低于 0.4
24. [友善设计——老年医院导视系统的适老化设计实践探究-维普期刊 中文期刊服务平台](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688&from=Qikan_Article_Detail)
   - 工具：tavily
   - 分数：0.54
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
25. [适老化视阙下医院导视设计策略探究](https://www.hanspub.org/journal/paperinformation?paperid=71956)
   - 工具：tavily
   - 分数：0.53
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
26. [[PDF] 基于案例分析的国内外医疗机构导视系统设计现状研究](https://pdf.hanspub.org/design202496_1871181613.pdf)
   - 工具：tavily
   - 分数：0.50
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
27. [13 Hospital Design Mistakes Doctors Regret | Avoid These Flaws](https://www.actisshealthcare.com/13-most-common-hospital-design-mistakes-doctors-regret)
   - 工具：tavily
   - 分数：0.35
   - 来源等级：C
   - 剔除原因：score 低于 0.4
28. [Healthcare Construction Mistakes to Avoid | Apex Design Build](https://www.apexdesignbuild.net/costly-healthcare-construction-mistakes-that-practices-and-hospitals-make)
   - 工具：tavily
   - 分数：0.34
   - 来源等级：C
   - 剔除原因：score 低于 0.4
29. [专家观点 - 智慧医院产品观（十一）：适老化设计-中国医院协会信息专业委员会](https://www.chima.org.cn/Html/News/Articles/15495.html)
   - 工具：tavily
   - 分数：0.31
   - 来源等级：C
   - 剔除原因：score 低于 0.4
30. [医院导视系统](https://www.pinterest.com/ideas/%E5%8C%BB%E9%99%A2%E5%AF%BC%E8%A7%86%E7%B3%BB%E7%BB%9F/948575276788)
   - 工具：tavily
   - 分数：0.29
   - 来源等级：C
   - 剔除原因：score 低于 0.4
31. [5 Engineering Design Mistakes That Cost Millions - UGCE](https://ugceconsultants.com/5-engineering-design-mistakes)
   - 工具：tavily
   - 分数：0.26
   - 来源等级：C
   - 剔除原因：score 低于 0.4
32. [[PDF] 适老化街道空间的包容性设计策略 - Art and Design](https://api.artdesignp.com/uploads/file/asp/2024051008231869fb26205.pdf)
   - 工具：tavily
   - 分数：0.18
   - 来源等级：C
   - 剔除原因：score 低于 0.4
33. [友善设计——老年医院导视系统的适老化设计实践探究-维普期刊 中文期刊服务平台](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688&from=Qikan_Article_Detail)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
34. [筑医台--HCD医养设计--医院导视标识的前世今生](http://hcd.zhuyitai.com/journals/hcd/article/d2195d017b9249f296ad72725c7ed2f6)
   - 工具：tavily
   - 分数：0.60
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
35. [适老化视阙下医院导视设计策略探究](https://www.hanspub.org/journal/paperinformation?paperid=71956)
   - 工具：tavily
   - 分数：0.57
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
36. [[PDF] 积极老龄化视角下社区公共导视系统适老化设计研究](https://pdf.hanspub.org/ar_3141153.pdf)
   - 工具：tavily
   - 分数：0.46
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
37. [[PDF] 《互联网网站适老化通用设计规范》 交 流 会](https://www.w3.org/2021/05/29-older-users-and-accessibility/slides/slides-huangchang.pdf)
   - 工具：tavily
   - 分数：0.30
   - 来源等级：C
   - 剔除原因：score 低于 0.4
38. [互联网网站适老化通用设计规范（工业和信息化部）](http://wza.isc.org.cn/bztx/bzjd/lgf)
   - 工具：tavily
   - 分数：0.23
   - 来源等级：C
   - 剔除原因：score 低于 0.4
39. [[PDF] 「通用設計理念應用於市區道路暨附屬設施及人行環境改善之探討 ...](https://www.nlma.gov.tw/uploads/files/afb7ff04bed2acbf134ff9af8fa9367b.pdf)
   - 工具：tavily
   - 分数：0.22
   - 来源等级：C
   - 剔除原因：score 低于 0.4
40. [[PDF] 上海市既有住宅适老化改造技术导则（正文）](https://zjw.sh.gov.cn/cmsres/aa/aab97b16be89424698acaa58c55f1709/4bc0662f4ca91f897ad38fbad0a0cca1.pdf)
   - 工具：tavily
   - 分数：0.13
   - 来源等级：C
   - 剔除原因：score 低于 0.4

## 完整精读结果

### 来源 1: 友善设计——老年医院导视系统的适老化设计实践探究-维普期刊 中文期刊服务平台

- URL: http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688&from=Qikan_Article_Detail
- 精读方法：firecrawl-scrape

期刊文献+

任意字段题名或关键词题名关键词文摘作者第一作者机构刊名分类号参考文献作者简介基金资助栏目信息

任意字段题名或关键词题名关键词文摘作者第一作者机构刊名分类号参考文献作者简介基金资助栏目信息

检索

- [高级检索](http://dianda.cqvip.com/Qikan/Search/Advance?from=Qikan_Article_Detail)
- [期刊导航](http://dianda.cqvip.com/Qikan/Journal/JournalGuid?from=Qikan_Article_Detail)

# 友善设计——老年医院导视系统的适老化设计实践探究  被引量：16

_Friendly Design, Exploration of Aging-friendly Design Practice of Guidance System in Elderly Hospitals_

原文传递

[导出](http://dianda.cqvip.com/Qikan/Search/Export?ids=7101034688&from=Qikan_Article_Detail)

摘要文章基于北京市卫生计生委提出的"老年友善医院"的概念来研究老年医院导视系统的适老化设计。通过分析老年患者特性及就医困惑,结合多学科研究成果,提出老年医院导视系统设计中便利性、易识别、安全性和人文关怀的原则,并依托理论成果,对导视系统中的造型、色彩、字体、位置等相关元素提出了具体的设计方法,开展设计实践,进而验证研究成果的可靠性和准确性。_Aimed at the concept of"Friendly Hospital for the Elderly"put forward by Beijing Health and Family Planning Commission,this paper studies the aging design of guidance system for elderly hospitals.By analyzing the characteristics of elderly patients and medical confusion,and combining with the results of multidisciplinary research,it puts forward the principles of convenience,easy identification,safety and humanistic care in the design of guidance system for elderly hospitals.Relying on the theoretical results,specific design methods are put forward for the relevant elements such as shape,color,font and location,and design practice is carried out to verify the reliability and accuracy of the research results._

作者[赵浩凯](http://dianda.cqvip.com/Qikan/Search/Index?key=A%3d%e8%b5%b5%e6%b5%a9%e5%87%af&from=Qikan_Article_Detail "赵浩凯") _Zhao Haokai(Beijing Geriatric Hospital,Beijing 100095,China)_

机构地区[北京老年医院](http://dianda.cqvip.com/Qikan/Search/Index?key=S%3d%e5%8c%97%e4%ba%ac%e8%80%81%e5%b9%b4%e5%8c%bb%e9%99%a2&from=Qikan_Article_Detail "北京老年医院")

出处[《艺术与设计（理论版）》](http://dianda.cqvip.com/Qikan/Search/Index?key=J%3d%e8%89%ba%e6%9c%af%e4%b8%8e%e8%ae%be%e8%ae%a1%ef%bc%88%e7%90%86%e8%ae%ba%e7%89%88%ef%bc%89&from=Qikan_Article_Detail "艺术与设计（理论版）")
2020年第1期74-76,共3页
_Art and Design_

关键词[老年患者](http://dianda.cqvip.com/Qikan/Search/Index?key=K%3d%e8%80%81%e5%b9%b4%e6%82%a3%e8%80%85&from=Qikan_Article_Detail "老年患者")[导视系统](http://dianda.cqvip.com/Qikan/Search/Index?key=K%3d%e5%af%bc%e8%a7%86%e7%b3%bb%e7%bb%9f&from=Qikan_Article_Detail "导视系统")[适老化](http://dianda.cqvip.com/Qikan/Search/Index?key=K%3d%e9%80%82%e8%80%81%e5%8c%96&from=Qikan_Article_Detail "适老化")[设计实践](http://dianda.cqvip.com/Qikan/Search/Index?key=K%3d%e8%ae%be%e8%ae%a1%e5%ae%9e%e8%b7%b5&from=Qikan_Article_Detail "设计实践") _elderly patientsguidance systemaging-friendly designdesign practice_

分类号[TU246\\
\\
\[建筑科学—建筑设计及理论\]](http://dianda.cqvip.com/Qikan/Search/Index?key=C%3dTU246&from=Qikan_Article_Detail "TU246")[G20\\
\\
\[文化科学—传播学\]](http://dianda.cqvip.com/Qikan/Search/Index?key=C%3dG20&from=Qikan_Article_Detail "G20")

- 引文网络
- 相关文献

- [节点文献](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688#referenceRelate)
- [二级参考文献11](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688#SecreferenceRelate)
- [参考文献1](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688#referenceRelate)
- [共引文献4](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688#CouplingRelate)
- [同被引文献98](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688#ByCouplingRelate)
- [引证文献16](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688#CitationRelate)
- [二级引证文献44](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688#SecCitationRelate)

## 参考文献1

- 1晋良海,闵露,陈述,郑霞忠,江新,陈雁高. [公共空间导视系统的空间视域模型及其眼动验证\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7000397922&from=Qikan_Article_Detail).工程研究（跨学科视野中的工程）,2017,9(5):430-438. 被引量：5

## 二级参考文献11

- 1茹斯·康罗伊·戴尔顿,窦强(译). [空间句法与空间认知\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=22571949&from=Qikan_Article_Detail).世界建筑,2005(11):41-45. 被引量：76
- 2陈庆荣,邓铸. [阅读中的眼动控制理论与SWIFT模型\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=22802568&from=Qikan_Article_Detail).心理科学进展,2006,14(5):675-681. 被引量：13
- 3吴娇蓉,胡山川,陈振武. [基于运动空间视觉感知的导向标志布局评价\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=39097956&from=Qikan_Article_Detail).同济大学学报（自然科学版）,2011,39(8):1167-1172. 被引量：8
- 4李智杰,李昌华,李晨,介军. [空间句法中定量视域分析算法研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=39338909&from=Qikan_Article_Detail).西安建筑科技大学学报（自然科学版）,2011,43(5):716-719. 被引量：13
- 5张智君,刘志方,赵亚军,季靖. [汉语阅读过程中词切分的位置:一项基于眼动随动显示技术的研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=40592175&from=Qikan_Article_Detail).心理学报,2012,44(1):51-62. 被引量：18
- 6何立国,周爱保,郭田友,鲍旭辉. [任务信息通达对视觉表象眼动的影响\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=42561801&from=Qikan_Article_Detail).心理学报,2012,44(7):910-923. 被引量：7
- 7房慧聪,周琳. [性别、寻路策略与导航方式对寻路行为的影响\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=42904731&from=Qikan_Article_Detail).心理学报,2012,44(8):1058-1065. 被引量：11
- 8郭长弓,顾保南. [城轨站行人流线网络构建及走行时间计算\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=49317040&from=Qikan_Article_Detail).同济大学学报（自然科学版）,2014,42(3):429-434. 被引量：8
- 9闫国利,刘妮娜,梁菲菲,刘志方,白学军. [中文读者词汇视觉信息获取速度的发展——来自消失文本的证据\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=663984680&from=Qikan_Article_Detail).心理学报,2015,47(3):300-318. 被引量：15
- 10刘兵,董卫华,王彦文,张宁旭. [视场角与观察角度对三维地图视觉信息加工的影响研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=666920060&from=Qikan_Article_Detail).地球信息科学学报,2015,17(12):1490-1496. 被引量：8

<_1_2>

## 共引文献4

- 1吕文蕾,贺田潇,耿晓杰. [虚拟现实结合眼动追踪技术在家具设计中的应用前景\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7001860499&from=Qikan_Article_Detail).木材工业,2019,33(3):36-40. 被引量：11
- 2晋良海,刘硕,殷双萍,邵波,陈述,彭爽. [商业综合体导向标志空间秩序标定研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7106296962&from=Qikan_Article_Detail).中国安全科学学报,2021,31(12):121-128. 被引量：2
- 3舒靖瑶,张振,李待宾. [基于老年人心理及行为特征的老年专科诊室设计研究——以华中科技大学校医院改造设计为例\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7109151902&from=Qikan_Article_Detail).工业设计,2023(2):56-58. 被引量：6
- 4孙澄,杨阳. [基于眼动追踪的寻路标志物视觉显著性研究——以哈尔滨凯德广场购物中心为例\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=74908866504849574850484852&from=Qikan_Article_Detail).建筑学报,2019(2):18-23.

## 同被引文献98

- 1杜鹏,李龙. [新时代中国人口老龄化长期趋势预测\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=00002EGGLH3O7JP0MNDO8JP16NR&from=Qikan_Article_Detail).中国人民大学学报,2021,35(1):96-109. 被引量：334
- 2郑磊. [城市数字化转型的内容、路径与方向\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=00002F8G456G7JP0MNDO5JP0MLR&from=Qikan_Article_Detail).探索与争鸣,2021(4):147-152.
- 3戴俭,朱小平,王珊. [医院建筑室内环境“人性化”设计\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=10564530&from=Qikan_Article_Detail).建筑学报,2003(7):22-24. 被引量：33
- 4周芃,黄杰. [上海市未来乐龄居住需求分析\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=26022731&from=Qikan_Article_Detail).城市规划学刊,2007(6):94-102. 被引量：8
- 5王秋惠. [老年人行为分析与产品无障碍设计策略\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=29717155&from=Qikan_Article_Detail).北京理工大学学报（社会科学版）,2009,11(1):57-61. 被引量：36
- 6舒余安,熊兴福,黄婉春. [基于老年人居家养老的产品设计研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=44967144&from=Qikan_Article_Detail).包装工程,2013,34(6):37-40. 被引量：18
- 7周燕珉,刘佳燕. [居住区户外环境的适老化设计\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=45618839&from=Qikan_Article_Detail).建筑学报,2013(3):60-64. 被引量：179
- 8平旭亮. [河北迁安中医院导视系统设计\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=49009181&from=Qikan_Article_Detail).中国医院建筑与装备,2014,15(3):48-50. 被引量：3
- 9辛向阳. [交互设计:从物理逻辑到行为逻辑\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=664758450&from=Qikan_Article_Detail).装饰,2015(1):58-62. 被引量：519
- 10王亚南,舒平. [基于循证设计的失智老人护理空间设计探究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=665685483&from=Qikan_Article_Detail).中外建筑,2015,0(8):107-109. 被引量：8

<_1_2345…10>

## 引证文献16

- 1刘健,鞠紫薇,韦婧雯. [老年病医院适老化导视系统设计研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7106197078&from=Qikan_Article_Detail).设计,2021,34(23):87-89. 被引量：7
- 2张倩,陈员,陈怡洋. [医疗服务数字转型中的适老化改造探讨\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7107572134&from=Qikan_Article_Detail).中国现代医生,2022,60(19):77-80. 被引量：5
- 3袁吉,秦悦,陈钰,吴昆禹,钱稳吉,马兆俊,吴毓,姜艳. [三级公立医院建设老年友善医疗机构的分析和思考\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7107894503&from=Qikan_Article_Detail).现代医院管理,2022,20(4):13-15. 被引量：12
- 4刘斐,杨璐嘉,张晨阳. [基于行为适应性评价的老年人家居产品设计方法研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7108370258&from=Qikan_Article_Detail).包装工程,2022,43(22):105-113. 被引量：2
- 5舒靖瑶,张振,李待宾. [基于老年人心理及行为特征的老年专科诊室设计研究——以华中科技大学校医院改造设计为例\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7109151902&from=Qikan_Article_Detail).工业设计,2023(2):56-58. 被引量：6
- 6谢海棠. [医院建筑适老化设计研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7110128604&from=Qikan_Article_Detail).城市建筑空间,2023,30(6):111-112. 被引量：1
- 7齐畅,李永昌. [社会设计导向下的失智老人养老空间环境设计研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7110753031&from=Qikan_Article_Detail).中国建筑装饰装修,2023(19):116-118. 被引量：3
- 8镇红霞. [老年友善医院的建设现状及推动策略研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7111933390&from=Qikan_Article_Detail).中国卫生标准管理,2024,15(7):84-87. 被引量：3
- 9于风,谢杨,刘盛泽,谷有法,王泓. [高品质住宅空间适老化设计中的人性化元素分析\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7112265671&from=Qikan_Article_Detail).建设科技,2024(9):42-45. 被引量：2
- 10李娜. [基于不同群体寻路特征的新余市中医院导视设计研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7112559020&from=Qikan_Article_Detail).丝网印刷,2024(12):74-76.

<_1_2>

## 二级引证文献44

- 1杨原媛,贾茹,叶茂慧,黄鑫,郭延佼. [适老化友善服务联合SMG模式在老年慢性病患者体检及健康管理中的应用\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=006382827B741B0A97282C8038CE349103479&from=Qikan_Article_Detail).中华老年病研究电子杂志,2023,10(3):51-55.
- 2张筠浛,陈琪然,梁雅馨,宁晓蕾. [现代宜居老年智慧社区打造智能化空间设计\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7109103438&from=Qikan_Article_Detail).中国住宅设施,2023(1):193-195.
- 3傅一弘,付青,梁昌虎. [老年友善医院创建的探索和实践\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7109464668&from=Qikan_Article_Detail).上海节能,2023(4):517-521. 被引量：1
- 4凯丽比努尔,王子沂,田柠枫,张淑谦. [数字化养老服务场景分析\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7110361301&from=Qikan_Article_Detail).中国科技纵横,2023(12):117-119. 被引量：1
- 5李沅蓉. [“适老化”背景下基于Kano模型的老年用户交互设计需求分析——以医疗App老年用户界面设计为例\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7110579935&from=Qikan_Article_Detail).数字通信世界,2023(9):69-71. 被引量：4
- 6邱雪君,谢震林. [基于人文关怀视角的医院住院部导视系统设计——以颍上县中医院为例\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7110642206&from=Qikan_Article_Detail).中国包装,2023,43(9):104-107.
- 7李璧媛,谢亚平. [情感化设计理论在养老院导视系统设计中的应用研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7110841010&from=Qikan_Article_Detail).设计,2023,36(19):57-60. 被引量：4
- 8朱贇,叶小云,章莉丽. [“数字医疗”背景下门诊适老化建设\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7110944886&from=Qikan_Article_Detail).现代医院,2023,23(11):1649-1651. 被引量：8
- 9张大辉,葛松梅,王安生. [人口老龄化背景下黑龙江省老年友善医院发展策略探析\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7111006599&from=Qikan_Article_Detail).中国初级卫生保健,2023,37(11):11-14. 被引量：2
- 10马钰洁,李亚军. [基于心流理论的老年人健身体感游戏设计研究\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7111235536&from=Qikan_Article_Detail).工业设计,2023(12):34-37. 被引量：9

<_1_2345>

- 1史一丰. [缺失与接通:徽学中的民间音乐研究展望\[J\]](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101039069&from=Qikan_Article_Detail).长沙大学学报,2020,34(1):60-62. 被引量：3

[![](http://image1.cqvip.com/vip1000/qkclearimg/81412x/81412x.jpg?site=abca3be269630857caa08c7c64816374)](http://dianda.cqvip.com/Qikan/Journal/Summary?kind=1&gch=81412X&from=Qikan_Article_Detail)

[艺术与设计（理论版）](http://dianda.cqvip.com/Qikan/Journal/Summary?kind=1&gch=81412X&from=Qikan_Article_Detail)

[2020年 第1期](http://dianda.cqvip.com/Qikan/Journal/Summary?kind=1&gch=81412X&y=2020&n=1&from=Qikan_Article_Detail)

职称评审材料打包下载

## 相关作者

内容加载中请稍等...

## 相关机构

内容加载中请稍等...

## 相关主题

内容加载中请稍等...

## 浏览历史

内容加载中请稍等...

;

- 用户登录

![](http://dianda.cqvip.com/Qikan/RegistLogin/VerficationCode)

登录IP登录

[使用帮助](http://dianda.cqvip.com/Qikan/WebControl/UseHelp?from=Qikan_Article_Detail) [返回顶部](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688&from=Qikan_Article_Detail#top)

### 来源 2: 筑医台--HCD医养设计--医院导视标识的前世今生

- URL: http://hcd.zhuyitai.com/journals/hcd/article/d2195d017b9249f296ad72725c7ed2f6
- 精读方法：firecrawl-scrape

# 筑医台科技有限公司

登录

搜索

- [首页](http://www.zhuyitai.com/)

- [项目](http://news.zhuyitai.com/list?fl=zx-xmxx)

[专题](http://news.zhuyitai.com/elastic/special/index)

[政策](http://news.zhuyitai.com/list?fl=zx-zc)

[人物](http://news.zhuyitai.com/list?fl=zx-rw)

[报道](http://news.zhuyitai.com/list?fl=zx-bd)

[看方案](http://news.zhuyitai.com/list?fl=zx-kfa)

[大咖](http://news.zhuyitai.com/list?fl=zx-dkfx)

[话题](http://news.zhuyitai.com/list?fl=zx-ht)

[其他](http://news.zhuyitai.com/list?fl=zx-qt)

[资讯](http://news.zhuyitai.com/)

- [视频](http://www.zhuyitai.com/video)

- [活动](http://active.zhuyitai.com/)

- [政策](http://news.zhuyitai.com/policy)

[课件](http://zk.zhuyitai.com/zk/courseware/index)

[知识](http://zk.zhuyitai.com/)

- [专家智库](http://www.zhuyitai.com/expert/list)

- [建设项目](http://www.zhuyitai.com/hospital)

- [供应商库](http://supplier.zhuyitai.com/)

- [行业奖项](https://2026chcc.chccchina.com/)

- 资讯公众号

HCD公众号

视频号

媒体品牌

- [咨询评审](http://www.zhuyitai.com/zxps/index)

项目服务

- [会员中心](http://uc.zhuyitai.com/uc/member/center)

- [商城](http://edi.zhuyitai.com/)

[CHCC2026](https://www.chccchina.com/)

筑医台资讯微信公众号

![筑医台](https://img.36krcdn.com/20200523/v2_60978139c1384260a7356df795ceaad7_img_png)

微信扫一扫，获取更多资讯

![](http://www.zhuyitai.com/jsp/portal/index/retrieval/img/sousuoicon.png)

热门搜索

医院导视标识的前世今生

作者：秦乙波

医院导视标识与医院建筑相辅相成，对提高医院建筑的使用效率和改善患者的就医体验具有重要作用，而且对医院文化的传播和医院形象的提升具有一定作用。透过导视标识可以体会一家医院的服务意识、管理水平和执行能力。

```
1864年8月，由瑞士和法国联合召开的有12个特命全权代表参加的日内瓦外交会议签署了《关于改善战地伤者境遇之日内瓦公约》，公约规定，将白底红十字作为战时医疗与救助活动的人员与设施的保护性标志。从那时起，该标志长期被国际承认，并具有法律效力。
1998年，我国卫生部、国家中医药管理局及总后卫生部联合发文，起用红花白十字的标志作为我国医疗卫生机构的统一标志。四颗红心分别代表卫生人员对患者、对服务对象的爱心、耐心、细心、责任心。总体图形在医疗机构表示以患者为中心，在其他卫生机构表示以保护和增进人民健康为中心。

红十字标志

红花白十字标志

医院标识导视的1.0时代

过去的医院面积较小，导视设施简单，随着医院面积扩大、功能区域增多，导视信息点位规划不合理、不连贯、不顺畅、流线卡顿等问题不断出现，而且标识系统色彩不统一、材质粗糙、工艺落后、标识尺度欠推敲、导视效率低、时有误导（使患者来回转路），难以发挥应用的作用。这对医院服务意识提出了较高的要求，也对设计制作的专业能力提出了较高要求。

医院标识导视的2.0时代
经过40年的改革开放，中国医院建设快速发展，医院导视标识进入2.0时代。随着大规模医院建设，导视标识有专业设计企业介入，他们设计的医院标识系统色彩统一，材质耐用，工艺精致，在提供导视信息的同时融入医院文化、历史传承，展示了医院形象。

2.0时代的医院导视标识设计

医院LOGO设计及品牌规划
在医院标识导视的2.0时代，一些医院意识到品牌传播的价值，陆续开始规划CI（企业识别）系统，很多医院创建了自己的VI（视觉识别）规范，并在标识导视项目实施中注重视觉信息传递的一致性，为医院管理、形象提升、文化传播等提供了很好的工具。

医院VI设计

医院导视标识系统的兴起
在医院标识导视系统的2.0时代，很多医院从上到下重视导视标识的设计制作，组织基建、后勤、宣传、院办、党办甚至工会等部门，投入精力、人手，既提供良好的导向服务，又创建良好的环境形象，同时还能传播医院文化，树立较好的医院形象。在这个阶段，医院导视标识得到很大改观，在满足不同程度的导视要求的同时，也对医院环境形象的提升起到了较好的作用。

2.0时代的医院导视标识系统的设计

2.0阶段医院存在的3大问题
医院对专业诉求不甚清晰  一些医院存在认识误区，比如认为导视是文化、美化、形象、传播、个性等，由此导视标识被寄予了较多的期待，医院在物色合作单位时纠结于设计公司、制造公司、广告公司、文化公司等，对专业诉求不甚清晰。
合作公司专业设计资源不足  合作公司专业设计资源不足，让做什么就做什么。由于对医疗流程、功能布局缺少了解，缺乏主动引导的能力，还不能根据就医流程、建筑构造特点进行点位规划、节点引导、电位结构预留、精装配合等，医院方面感觉工作难以推进。
日常维护工作需要专职人员跟进  同一家医院的导视标识在不同阶段、不同区域呈现不同风格，色彩、材质、形态各异。在医院运营过程中，因为各种原因导致挪位置、改名称、增减标识牌等需要服务跟进，日常维护工作需要专职人员跟进。

医院导视标识的3.0时代
目前，医院导视标识正进入3.0时代，这是提升医疗质量、传递人文关怀、拥有医者仁心的必然趋势。3.0时代对导视设计和医院规划、建设、管理、运营工作提出了更高要求。此阶段的医院导视标识以提高医疗建筑使用效率、改善医疗服务体验和建立医疗和谐生态为原则。下面介绍相对于2.0时代，3.0时代医院导视标识的精进之处。

3.0时代的医院导视标识系统更需要统筹

医疗建筑效率的提升
统筹规划  品牌、导视、精装、软装专业合作，统筹规划，同步施工，改变过去精装完成后再附加导视的工作模式，利用墙面、柱面、地面等进行色彩、图文引导，既能提升建筑装饰效果，又能降低成本、缩短工期。
定位、流程更清晰  明确医院建筑、楼层、区域、房间的统一物理位置信息，先定位再引导，加强医院导视的内在逻辑性，提升医院导视效率、提升医院建筑使用效率，为未来智慧医院奠定基础。
除上述优势外，3.0时代精确分析视角、视距、流向，规划重要节点的信息设置，做到了直接引导，减少近处间接引导，避免信息冗余，在导视效率方面做到点位无缺失、无冗余，内容无缺失、无冗余，信息编排逻辑清晰。
医疗服务体验的改善
医疗服务体验的改善要注意以下问题 ：安装高度符合人机工程学高度规范；图文大小符合人机工程学视距规范；标识尺度与建筑物形成恰当关系；视角符合人机工程学识别规范；色彩按照医院VI（视觉识别）规范进行主色设计；色相以偏安静的色系为主；运用同类色或对比色进行色彩搭配；字体轮廓清晰的黑体或略有圆角的圆黑体为主；材质以钢板、铝板、亚克力板、PVC板、型材为主，石材、木材的选用视项目情况而定；工艺上以雕刻、裁切、折弯、打磨、烤漆等形式呈现，图文以高目丝印为主；图标符合国家规范和行业规范，易识别无歧义；语言方面要中英文对照，符合国家公共场所中英文字使用规范，符合医疗行业中英文字使用要求，符合医院医学专业中英文字使用的具体要求；安全上保证材料的光洁、圆滑，避免尖角。

3.0时代的医院导视标识设计、安装更加人性化

医疗和谐生态的打造
适度设计：控制设计度，理性、逻辑、经济；以高效的导视标识营造和谐的就医环境；结构预留：提前处理吊杆、楼顶结构；电位预留：提前做好回路，预留电源；精装定制：墙板、墙漆定制专色、特制图案，一气呵成；护士站吊挂灯槽色彩一次处理到位；地面导引一次性切割安装到位；消防：各房间消防逃生图、公共区域重要节点消防逃生图、消火栓灭火器标识齐备；构造简洁：加工维护便捷；更换：操作便捷，并且不影响美观；维护：整体设计、整体施工，给后期维护创造方便；可追溯：导视标识的逻辑清晰，竣工文件齐整。

 上：3.0时代的医院导视标识颜色偏安静 下：3.0时代以高效的导视标识营造和谐的就医环境

3.0时代医院SSI交互设计研究的兴起
SSI（空间与服务识别）是英文Space&Service Identity（空间与服务识别）的英文首字母，源于企业识别系统（CIS），其以文化、意象、LOGO、图形符号、建筑功能逻辑编码等各类呈现手段构建独特的空间交互特征，为建筑空间硬环境向以人为本的软服务过渡提供系统解决方案，也是从建筑硬环境过渡到软服务的必要环节。
SSI处理人与环境、人与服务的交互，涵盖建筑功能逻辑、人机工程学、材料工艺学、企业文化、视觉艺术等综合学科门类。当医院完成建筑建造投入使用时，会面临环境导视、文化宣传、品牌塑造等众多环节规划实施，头绪繁杂。一个包含SSI 完整交互设计的医院建筑成品，可以让医院建筑硬环境顺畅地进入医疗软服务，这是医疗建筑设计亟待提升的重要环节，也是医院急需的一个重要体验。
```

![](http://hcd.zhuyitai.com/jsp/hcd/img/collectFeesIcon.png)

此书籍为收费书籍

需 _1799阅点_(￥17.99)

购买跳转至可读章节

编辑：马志晖

2019年8期

莫让医院成迷宫

#### 导航目录

- 印记

[全国医院建设大会公益行山东站顺利举行](http://news.zhuyitai.com/detail/fbe3448afff94625a6f6cb2d4cd86abb) [明年“全国医院建设大会”将设100场论坛](http://news.zhuyitai.com/detail/4d23a3c685254276b15ad2c57f4a92a5)

- 建筑视界

[昆士兰理工大学Peter Coaldrake教育中心](http://news.zhuyitai.com/detail/0c235baf0d0d4de0a8705fb214b323ee)

- “中国医院建设奖”获奖案例

[丽水市中心医院：江南山水中精美瑰丽的花园](http://news.zhuyitai.com/detail/e8203cc979824b41bc3f9f9a1ea7b9ac) [复旦大学附属中山医院厦门医院：拥抱大海 拥抱生命](http://news.zhuyitai.com/detail/e35370b6cfbf4f4abad08f2a5a4beac2) [泰康之家吴园二级康复医院：追求场所精神的空间设计](http://news.zhuyitai.com/detail/9c1362b4fd7f4edb8ccb3ca2728e8a4f)

- 案例

[常州市妇幼保健院室内设计方案：由心发出的设计](http://news.zhuyitai.com/detail/045b93126d334154b998e9c68d45b80f) [新希望晓康之家健康管理机构：打破医疗空间的刻板印象](http://news.zhuyitai.com/detail/91e95b9af91446a1a0fe7fb08d9fa201) [蒙特利尔大学中心医院：北美洲最大的健康护理机构](http://news.zhuyitai.com/detail/2b31dd63a96747ba83c87938a22bfb07)

- 聚焦

[漫谈医院标识系统](http://news.zhuyitai.com/detail/428c1c00bb4b42a59d82c3b49cf7c338) [医院导视标识的前世今生](http://news.zhuyitai.com/detail/d2195d017b9249f296ad72725c7ed2f6) [医院标识导向系统建设策略](http://news.zhuyitai.com/detail/0e797eb25b804c0882204c3efc9ebc90) [环境图形在医疗机构导视设计中的作用：不止是画龙点睛](http://news.zhuyitai.com/detail/96399027f0e542fe92da5f71c2bb22e6) [医院数码导视系统畅想](http://news.zhuyitai.com/detail/2b9546686d054f10b2db2234455f5b86) [设计是平衡的艺术：厦门弘爱医院标识系统设计特色](http://news.zhuyitai.com/detail/36abadab238c490c83c799ff4090b14a)

- 业界

[科学策划，破除医院建设的魔咒](http://news.zhuyitai.com/detail/3f04b0cdd85f43488e0aa6da1b90f07b) [医院建设前期工作中的惑与解](http://news.zhuyitai.com/detail/feab9a0443d146c6a5b212b94e13fe4d) [医用物资招标/采购环节质量把控与风险防范](http://news.zhuyitai.com/detail/07a498b54c0642b4a53315d3cc134efe) [上海市第一人民医院新建综合楼医疗工艺流程规划要点](http://news.zhuyitai.com/detail/ccd108e2a709492aae1a6832a29e99eb)

#### 近期内容

- [![](http://file.zhuyitai.com/journals/hcd/66bcbbcf4ed94c0ebe35fe08d0cc1994/abd7f299f8b14794a68aa98a5e98aff6.jpg)\\
2022年第1期\\
\\
医疗建筑之美](http://news.zhuyitai.com/detail/66bcbbcf4ed94c0ebe35fe08d0cc1994)
- [![](http://file.zhuyitai.com/journals/hcd/d1a9803e03374060a0c2d21c091d7c50/191fcdcab08e491297ff4efae19a8a90.jpg)\\
2021年第12期\\
\\
问道EPC](http://news.zhuyitai.com/detail/d1a9803e03374060a0c2d21c091d7c50)
- [![](http://file.zhuyitai.com/journals/hcd/7afde10e77064f3aa2184a0c4ed884f3/034cbcf375c342e68e2bd6aacfafdfab.jpg)\\
2021年第11期\\
\\
装配式医院](http://news.zhuyitai.com/detail/7afde10e77064f3aa2184a0c4ed884f3)
- [![](http://file.zhuyitai.com/journals/hcd/c51d4ab536834edfbf3d2bfdfb10a27d/b419d4dfd1664dfa8b84e6fa185829a0.jpg)\\
2021年第10期\\
\\
最美医院](http://news.zhuyitai.com/detail/c51d4ab536834edfbf3d2bfdfb10a27d)
- [![](http://file.zhuyitai.com/journals/hcd/8b8e34a3fa514aa8b899e3e95456b2f3/05fbf8e25c2a43e9a2ddb304645dd8fb.jpg)\\
2021年第9期\\
\\
医院应急防灾体系建设与管理](http://news.zhuyitai.com/detail/8b8e34a3fa514aa8b899e3e95456b2f3)
- [![](http://file.zhuyitai.com/journals/hcd/0096572301c04eb893e94e68b2b15e74/b10a25f7c9694e0a9f8ea0524ec2f04c.jpg)\\
2021年第8期\\
\\
高质量发展康复医院建设](http://news.zhuyitai.com/detail/0096572301c04eb893e94e68b2b15e74)

### 来源 3: 适老化视阙下医院导视设计策略探究

- URL: https://www.hanspub.org/journal/paperinformation?paperid=71956
- 精读方法：firecrawl-scrape

- [首页](https://www.hanspub.org/)
- [人文社科](https://www.hanspub.org/8.shtml)
- [设计进展](https://www.hanspub.org/journal/Sheji.html)
- [Vol. 8 No. 3 (September 2023)](https://www.hanspub.org/journal/paperhis?issueid=7132&journalid=8831)

#### [期刊菜单](https://www.hanspub.org/journal/paperinformation?paperid=71956\#collapse1)

- [最新文章](https://www.hanspub.org/journal/home?journalid=8831)
- [历史文章](https://www.hanspub.org/journal/paperhis?journalid=8831)
- [检索](https://www.hanspub.org/journal/retrieval?journalid=8831)
- [领域](https://www.hanspub.org/journal/domain?journalid=8831)
- [编委](https://www.hanspub.org/journal/editor?journalid=8831)
- [投稿须知](https://www.hanspub.org/journal/instructions?journalid=8831)
- [文章处理费](https://www.hanspub.org/journal/fee?journalid=8831)

- [最新文章](https://www.hanspub.org/journal/home?journalid=8831)
- [历史文章](https://www.hanspub.org/journal/paperhis?journalid=8831)
- [检索](https://www.hanspub.org/journal/retrieval?journalid=8831)
- [领域](https://www.hanspub.org/journal/domain?journalid=8831)
- [编委](https://www.hanspub.org/journal/editor?journalid=8831)
- [投稿须知](https://www.hanspub.org/journal/instructions?journalid=8831)
- [文章处理费](https://www.hanspub.org/journal/fee?journalid=8831)

**适老化视阙下医院导视设计策略探究**

Research on Design Strategy of Guided Vision in Hospital for Aging Patients

**DOI:** [10.12677/Design.2023.83148](https://doi.org/10.12677/Design.2023.83148),
[PDF](https://pdf.hanspub.org/design20230300000_57502640.pdf),
[被引量](https://www.hanspub.org/journal/citations?paperid=71956&journalid=8831)下载:1,779  浏览:2,696

**作者:**[谢小漫](https://www.hanspub.org/journal/articles?searchcode=%e8%b0%a2%e5%b0%8f%e6%bc%ab&searchfield=authors&page=1), [周杨静\*](https://www.hanspub.org/journal/articles?searchcode=%e5%91%a8%e6%9d%a8%e9%9d%99&searchfield=authors&page=1)：南京林业大学艺术设计学院，江苏 南京

**关键词:**[老龄化](https://www.hanspub.org/journal/articles?searchcode=%e8%80%81%e9%be%84%e5%8c%96&searchfield=keyword&page=1)； [医院导视](https://www.hanspub.org/journal/articles?searchcode=%e5%8c%bb%e9%99%a2%e5%af%bc%e8%a7%86&searchfield=keyword&page=1)； [适老化改造](https://www.hanspub.org/journal/articles?searchcode=%e9%80%82%e8%80%81%e5%8c%96%e6%94%b9%e9%80%a0&searchfield=keyword&page=1)； [Aging](https://www.hanspub.org/journal/articles?searchcode=Aging&searchfield=keyword&page=1)； [Hospital Vision Guidance](https://www.hanspub.org/journal/articles?searchcode=+Hospital+Vision+Guidance&searchfield=keyword&page=1)； [Suitable for Aging Reform](https://www.hanspub.org/journal/articles?searchcode=+Suitable+for+Aging+Reform&searchfield=keyword&page=1)

**摘要:** 目的：针对国内人口老龄化，探索老年人产生的独立就医困难现象的原因，找出国内医疗导视系统存在的漏洞，提出具有参考价值的医院导视设计改善策略。方法：系统分析医院导视系统设计的组成部分以确认其功能性，结合国内江苏省会南京的医院导视系统现状与国外导视设计案例，模拟医院导视系统面对老年人所适合的情境，总结老年人就医面临的心理及生理需求，对医院导视设计的适老化改善提出建设性意见。结论：医院导视设计不应只服务于多数人，更应服务于少数人。提高导视系统设计的效率，在功能性的基础上与时代主题相结合，加强设计的完整性、舒适性、易辩性与安全性，设计具有艺术性、创造性，具有人情味的医院导视系统，将极大改善国内老年人就医困难现象，增加老年人就医的幸福感。

**Abstract:**
Objective: To explore the causes of the difficulty of independent medical care for the elderly in China, to find out the loopholes in the domestic medical population ageing system, and to propose some useful strategies for improving the design of hospital vision guidance. Methods: The components of the design of hospital guided vision system were systematically analyzed to confirm its functionality, and the current situation of the hospital guided vision system in Nanjing, capital of Jiangsu Province, and the cases of foreign guided vision design were combined. This paper simulates the situation that the hospital guidance system is suitable for the elderly, summarizes the psychological and physiological needs of the elderly, and puts forward some constructive suggestions for the aging improvement of the hospital guidance design. Conclusion: Hospital Vision Guidance Design should not only serve the majority, but also serve the minority. We should improve the efficiency of the design of the guide system, combine with the theme of the times on the basis of the function, strengthen the integrity, comfort, argumentation and security of the design. The design is artistic and creative. The humanistic vision guidance system in hospital will greatly improve the medical difficulties of the elderly in China and increase their happiness in seeking medical treatment.

**文章引用：** 谢小漫, 周杨静. 适老化视阙下医院导视设计策略探究\[J\]. 设计进展, 2023, 8(3): 1222-1232. [https://doi.org/10.12677/Design.2023.83148](https://doi.org/10.12677/Design.2023.83148)

**参考文献**

|     |     |
| --- | --- |
| \[1\] | 白雪锋, 郑婕, 周成玲, 王浩. 基于Citespace知识图谱的中国适老化研究历程与趋势分析\[J\]. 中国老年学杂志, 2021, 41(20): 4561-4566. |
| \[2\] | 杨晨晨, 吴学林. 老年人数字鸿沟的问题及解决办法分析\[J\]. 科技风, 2023(21): 148-150. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=%e8%80%81%e5%b9%b4%e4%ba%ba%e6%95%b0%e5%ad%97%e9%b8%bf%e6%b2%9f%e7%9a%84%e9%97%ae%e9%a2%98%e5%8f%8a%e8%a7%a3%e5%86%b3%e5%8a%9e%e6%b3%95%e5%88%86%e6%9e%90&doi=10.19392%2fj.cnki.1671-7341.202321050)\] \[ [CrossRef](https://doi.org/10.19392/j.cnki.1671-7341.202321050)\] |
| \[3\] | 战宁. 童话般的视觉体验——墨尔本皇家儿童医院导视系统设计探析\[J\]. 装饰, 2014(4): 139-140. |
| \[4\] | 郭丽萍, 丛焘. 城市发展中公共景观空间适老化设计研究\[J\]. 现代物业(中旬刊), 2020(6): 70-71. |
| \[5\] | 段莉, 高云峰, 刘亚莉, 田建丽. 乡镇社区老年人居家环境适老化水平的调查研究\[J\]. 护理学杂志, 2019, 34(9): 87-90. |
| \[6\] | 王天赋, 王睿. 养老设施适老化产品满意度多层次模糊综合评价\[J\]. 包装工程, 2022, 43(12): 192-198. |
| \[7\] | 王杰. 数字产品适老化评估体系研究\[J\]. 老龄科学研究, 2022, 10(4): 9-27. |
| \[8\] | 郭铁军, 王春晓, 高渤. 文化地标导视设计研究\[J\]. 包装工程, 2021, 42(2): 180-185, 194. |
| \[9\] | 邓俊, 汤迪欣. 基于人机工程学的城市公共导视设计研究\[J\]. 包装工程, 2020, 41(24): 46-52, 78. |
| \[10\] | 刘梁. 环境心理学语境下的数字化医院导视系统研究\[J\]. 包装工程, 2020, 41(14): 272-277, 338. |
| \[11\] | 李战鹏. 基于色彩视觉心理特征的医院室内设计及导视设计探究\[J\]. 设计, 2020, 33(8): 111-113. |
| \[12\] | 王聪, 朱华. 妇幼保健院视觉导视系统中的情感化设计研究\[J\]. 包装工程, 2020, 41(8): 258-262. |
| \[13\] | 陈佳音. 马斯洛理论视角下的老年公寓公共空间环境设计\[J\]. 文化产业, 2022(10): 157-159. |
| \[14\] | 何铨, 张湘笛. 老年人数字鸿沟的影响因素及社会融合策略\[J\]. 浙江工业大学学报(社会科学版), 2017, 16(4): 437-441. |
| \[15\] | 高丹阳. 老年人“数字鸿沟”弥合路径探析\[J\]. 新闻研究导刊, 2022, 13(4): 127-129. |
| \[16\] | 徐越, 韵卓敏, 王婧媛, 景荣杰, 黄黎明, 沈勤. 智能化背景下, 老年人数字鸿沟的影响因素及其形成过程分析\[J\]. 智能计算机与应用, 2020, 10(2): 75-82. |
| \[17\] | 王娟, 张劲松. 数字鸿沟: 人工智能嵌入社会生活对老年人的影响及其治理\[J\]. 湖南社会科学, 2021(5): 123-130. |

[投稿](https://papersubmission.hanspub.org/paper/showAddPaper?journalID=287 "投稿")

友情链接

- [科研出版社](http://www.scirp.org/ "科研出版社")
- [开放图书馆](http://www.oalib.com/ "开放图书馆")

在线咨询

[声音提醒](https://k.hanspub.org/php/app.php?widget-iframe-content#) [自动滚屏](https://k.hanspub.org/php/app.php?widget-iframe-content#) [使用表情](https://k.hanspub.org/php/app.php?widget-iframe-content#) [使用媒体](https://k.hanspub.org/php/app.php?widget-iframe-content#) [自动显示](https://k.hanspub.org/php/app.php?widget-iframe-content#) [全屏切换](https://k.hanspub.org/php/app.php?widget-iframe-content#) [结束聊天](https://k.hanspub.org/php/app.php?widget-iframe-content#)

你确定当前操作? [是](https://k.hanspub.org/php/app.php?widget-iframe-content#) [取消](https://k.hanspub.org/php/app.php?widget-iframe-content#)

Please fill the following form to start the chat

[Select department](https://k.hanspub.org/php/app.php?widget-iframe-content#)

[Start](https://k.hanspub.org/php/app.php?widget-iframe-content#)

Operator has closed the talk [Login again](https://k.hanspub.org/php/app.php?widget-iframe-content#)

当前客服未在线，请提交留言，客服收到后会及时与您取得联系.

[发送](https://k.hanspub.org/php/app.php?widget-iframe-content#)

![](https://k.hanspub.org/img/loading.gif)

[Back](https://k.hanspub.org/php/app.php?widget-iframe-content#)

### 来源 4: [PDF] 基于案例分析的国内外医疗机构导视系统设计现状研究

- URL: https://pdf.hanspub.org/design202496_1871181613.pdf
- 精读方法：firecrawl-scrape

基于案例分析的国内外医疗机构导视系统设计现状研究

李增瑞，孙 声

山东建筑大学艺术学院，山东 济南

收稿日期：2024年10月29日；录用日期：2024年12月24日；发布日期：2024年12月31日

摘 要

本研究致力于全面且深入地剖析国内外医疗机构导视系统设计案例，旨在探寻其内在的设计规律以及独特的特点。运用文献研究、案例分析等科学方法，对中国香港大学深圳医院、美国梅奥诊所、日本川西市医疗中心等具有代表性的医疗机构导视系统展开了详尽的分析。研究结果表明，国内外医疗机构导视系统在设计原则方面存在一定的相通性，然而在表现形式以及细节处理层面却显现出差异。国外医疗机构在人性化设计和文化融合方面展现出诸多值得借鉴之处，我国医疗机构同样具备自身的特色亮点。此项研究成果将为我国医疗机构导视系统的设计优化提供具有重要参考价值的依据。

导视系统，人性化，文化融合

Abstract

Study on the Current Situation of Guide
System Design in Domestic and Foreign
Medical Institutions Based on Case Analysis

This study is dedicated to a comprehensive and deep analysis of medical institutions at home and
abroad, aiming to explore the inherent design rules and unique characteristics. Using scientific
\*
通讯作者。

School of Art, Shandong Jianzhu University, Jinan Shandong

文章引用: 李增瑞, 孙声. 基于案例分析的国内外医疗机构导视系统设计现状研究\[J\]. 设计, 2024, 9(6): 1759-1767.
DOI: 10.12677/design.2024.96846

* * *

李增瑞，孙声

**methods such as literature research and case analysis, the analysis of the guide system of representa-** **tive medical institutions such as Shenzhen Hospital of the University of Hong Kong (China), Mayo** **Clinic in the United States, and Kawasaki Medical Center of Japan was conducted in detail. The results** **show that the guide system of domestic and foreign medical institutions has some similarities in the** **design principles, but there are differences in the expression form and detail treatment. Foreign med-** **ical institutions have shown many worthy lessons from in humanized design and cultural integration,** **and China’s medical institutions also have their own characteristics and highlights. This research re-** **sult will provide an important reference basis for the design optimization of guide system in medical** **institutions in China.**

# Keywords

## Guide System, Humanization, Cultural Integration

Copyright © 2024 by author(s) and Hans Publishers Inc. This work is licensed under the Creative Commons Attribution International License (CC BY 4.0). [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/) Open Access

# 1\. 引言

1.1.研究背景 随着现代医疗水平的不断提高，医疗机构的规模日益扩大且功能分区复杂。患者在就医过程中，往 往面临着寻找科室、了解就医流程等问题。医疗机构导视系统作为一种信息传达的重要手段，对于提高 患者就医体验、提升医疗效率具有关键作用。在全球化背景下，国内外医疗机构在导视系统设计方面都 有值得研究和借鉴之处。同时，我国近年来对医疗服务质量提升有一系列政策支持，如改善就医环境等， 这也为导视系统设计的优化提供了政策依据。
**1.2.** 研究意义及目的 本研究有利于丰富医疗环境设计理论体系，深入挖掘导视系统在医疗机构中的作用机制，为后续相 关研究提供理论基础和研究视角。从设计学、心理学、人机工程学等多学科角度剖析导视系统设计，拓 展跨学科研究的深度和广度。有助于提高医疗机构的运营效率。清晰准确的导视系统可减少患者就医时 间，缓解人流拥堵，提高医疗资源的利用率。改善患者就医体验，减轻患者就医过程中的焦虑情绪，增 强患者对医疗机构的信任度和满意度。对于我国医疗机构建设，通过借鉴国外先进经验，推动我国医疗 机构导视系统设计水平与国际接轨，提升我国医疗环境的整体品质。 深入分析国内外医疗机构导视系统设计的成功案例，总结其设计原则和方法\[1\]。比较国内外设计的 异同点，找出我国设计可借鉴的国外优势。结合我国国情和医疗政策，提出适合我国医疗机构导视系统 设计的改进建议和创新思路。

# 2\. 研究内容与方法

研究内容包括导视系统的基本设计原则、国内外典型医疗机构导视系统的设计分析，如中国香港大 学深圳医院、美国梅奥诊所、日本川西市医疗中心等，以及对比国内外设计的异同点和对我国的启示。 研究方法如下：

(一) 资料收集：深入开展此项工作时，笔者广泛涉猎众多导向设计相关书籍与文献。尤其聚焦于医
DOI: 10.12677/design.2024.96846 设计

* * *

李增瑞，孙声

院导向设计资料，精心梳理其中蕴含的理论成果。在此过程中，充分结合设计心理学、设计符号学、环 境心理学以及人机工程学等多学科知识，深度挖掘它们与医院导向设计的紧密连结点，并巧妙地将这些 知识运用到实际研究当中，为后续的设计优化奠定坚实理论基础。并借助互联网的便捷，积极浏览国外 专业设计机构网站，从中探寻有关医院导向设计的各类信息。通过这种方式，及时掌握医院导向设计的 最新设计动态，敏锐捕捉其中的人性化设计方法。

(二) 实地考察和调研：为获取最真实、最直观的资料，笔者对身边的医院导向设计情况展开实地拍摄与问卷调研。通过实地拍摄，能够清晰记录下医院导向标识的实际设置、呈现形式等细节；而问卷调 研则可以深入了解患者、医护人员等不同群体对于医院导向设计的切身感受和实际需求，为后续的分析 研究提供一手且极具针对性的数据支撑。

(三) 统计分析法：一方面，针对国外医院导向设计现状展开全面调查，细致对比不同国家、地区之间的差异，进而精准总结出医院导向设计应当遵循的原则。这些原则不仅要满足基本的指引功能，更要 契合当下国际上对于医院环境人性化、高效化的热点趋势\[2\]。另一方面，对国内医院导向设计现状进行 深入剖析，总结现存的诸多问题，诸如标识不够清晰明确、缺乏对特殊人群的关怀等。结合当下提升就 医体验的热点诉求，提出具有针对性和可操作性的解决对策，旨在推动国内医院导向设计迈向新的台阶， 更好地服务于广大患者和医护人员。

# 3\. 导视系统的设计原则

3.1.清晰性原则 导视信息必须清晰明了，无论是文字、图形还是色彩，都要让患者和家属能够快速准确地理解。文 字大小要合适，避免因距离或视力问题导致信息获取困难。图形设计要简洁易懂，例如用通用的图标表 示厕所、电梯等。色彩的对比度要高，如使用白色文字在深色背景上，以增强视觉效果。
**3.2.** 一致性原则 在整个医疗机构内，导视系统的风格、色彩、字体、图标等要保持一致。这样可以帮助患者形成统 一的视觉认知，避免因信息表现形式的变化而产生困惑。例如，所有科室指示牌都采用相同的字体和颜 色搭配。
**3.3.** 醒目性原则 导视标识要能够在复杂的环境中迅速吸引人们的注意力。可以通过合理的尺寸设计、独特的造型以 及适当的照明等方式来实现。比如在医院大厅设置大型的、造型独特的楼层索引牌，并配备灯光，方便 患者在不同光线条件下查看。
**3.4.** 人性化原则 要充分考虑患者和家属的需求和心理状态。设计要符合人体工程学\[3\]，比如标识的高度要适合不同 身高的人群观看。同时，要考虑特殊人群的需求，如为盲人设置盲文标识，为老年人设置较大字体和简 单易懂的导视信息。
**3.5.** 文化性原则 导视系统可以融入医疗机构的文化特色和当地的文化元素。例如，一家具有悠久历史的医院可以在 导视设计中体现其发展历程和文化传承，使患者在就医过程中感受到医院的独特魅力。
DOI: 10.12677/design.2024.96846 设计

* * *

李增瑞，孙声

# 4\. 国内外医疗机构导视系统设计案例分析

4.1.中国香港大学深圳医院导视系统分析
4.1.1. 设计风格
(1) 色彩搭配：中国香港大学深圳医院的 logo 色彩是绿色与蓝色，这两种颜色在导视系统中得到了充分运用，绿色代表着生命的广阔、积极以及自然的宁静、安详，蓝色则给人以平和、公正的感觉\[4\]。 这种色彩组合既符合医院的专业形象，又能给人带来一种安心、舒适的视觉感受。同时，不同科室还搭 配了不同的暖系色调，在保持整体风格统一的基础上，通过色彩差异彰显了各科室的独特性，也方便患 者快速识别和区分。

(2) 造型设计：标识牌以圆中带方的造型为主，圆形的元素给人一种柔和、亲切的感觉，而方形则体现出医院的严谨和专业，两者相结合，凸显出医院的时代厚重感与兼具的人文关怀气质。标识牌的局部 还会做凸起和异化处理，增加了视觉上的层次感和立体感，给人带来简洁大气的视觉触感\[5\]。

(3) 与医院环境的协调性：医院的导视系统设计与医院的建筑风格和内部装修相呼应，形成了一个整体的视觉效果。例如，在医院的公共区域，导视标识的颜色和材质与周围的环境相融合，不会显得突兀； 在科室内部，导视标识的设计也与科室的功能和氛围相契合，为患者提供了一个舒适、和谐的就医环境。

## 4.1.2. 信息呈现方式

(1) 文字内容：导视系统中的文字简洁明了，使用了容易理解的语言和语调，能够准确地传达信息。例如，在科室标识上，清晰地标明了科室的名称、所在楼层和位置等关键信息，让患者能够快速找到自 己需要的科室\[6\]。同时，对于一些重要的提示信息，如紧急出口、无障碍通道等，也采用了醒目的文字 进行标注，确保患者在紧急情况下能够快速找到逃生通道。

(2) 图标设计：图标设计具有高度的辨识度，能够直观地传达信息。例如，使用了通用的医疗图标，
如“ +”代表医疗、“箭头”代表方向等，让患者即使不认识文字，也能够通过图标理解导视信息。此外， 针对一些特殊的科室或区域，还设计了独特的图标，如儿科区域可能会使用卡通形象的图标，增加了导 视系统的趣味性和吸引力。

(3) 信息的分级与分类：导视系统对信息进行了合理的分级和分类，方便患者快速获取所需信息。例如，在医院的入口处和主要通道，设置了一级索引标识，告知患者各科室所在的楼层；在楼层的电梯口 和走廊交汇处，设置了二级分流导视，引导患者到达具体的科室区域；在科室门口，则设置了三级诊室 门牌标识，明确了目的诊室的位置。

## 4.1.3. 空间利用与引导

(1) 空间布局的适配性：导视系统的设置充分考虑了医院的空间布局，在关键的节点位置，如电梯口、楼梯间、走廊交汇处等，都设置了导视标识，确保患者能够在复杂的空间中快速找到方向。同时，导视 标识的大小和安装位置也经过了精心设计，既不会占用过多的空间，又能够起到良好的引导作用。

(2) 人流引导的合理性：医院的人流量较大，导视系统的设计能够合理地引导人流，避免拥堵和混乱。例如，通过设置单向通行的指示标识和分流通道，引导患者有序地流动；在一些容易出现拥堵的区域， 如挂号处、缴费处等，加强了标识的提示力度，引导患者提前做好准备，减少排队等待的时间。

(3) 与周边环境的融合：医院的周边环境可能会对导视系统的设计产生影响，中国香港大学深圳医院的导视系统能够与周边环境相融合(如图 1)。例如，如果医院附近有地铁站或公交站等交通枢纽，导视系 统会在相应的位置设置指示标识，引导患者从交通枢纽到达医院；如果医院周边有商业区或居民区，导 视系统也会考虑到这些区域的人流特点，合理地设置导视标识，方便患者和周边居民的就医。

DOI: 10.12677/design.2024.96846 设计

* * *

李增瑞，孙声

**Figure 1. Guide system of the University of Hong Kong (China), Shenzhen Hospital**

图 1 . 中国香港大学深圳医院导视系统 ①

**4.2.** 美国梅奥诊所导视系统分析
4.2.1. 设计理念
(1) 简洁直观：梅奥诊所的导视系统在设计上遵循简洁直观的风格，标识牌上的文字简洁明了，避免了复杂的表述和过多的装饰元素，让患者能够快速理解信息。例如，科室名称直接用清晰的字体标注， 没有过多的花哨设计，使患者能够在短时间内获取关键信息(如图 2)。

(2) 色彩搭配协调：色彩的运用上较为讲究，通常选择与医院整体环境相协调且具有较高辨识度的颜色。比如，采用温和的蓝色、绿色等作为主色调，蓝色给人专业、冷静、可靠的感觉，符合医院的专业形 象；绿色则代表着生命与健康，能让患者在视觉上感到舒适和安心。

(3) 造型统一规范：导视标识的造型设计具有统一的规范，无论是字体的样式、大小，还是图标的设计，都保持了一致性。这种统一的设计风格使得整个导视系统在医院的不同区域都具有很强的识别性， 患者能够快速适应并找到所需的信息。

(4) 与环境融合：导视系统的设计与医院的建筑风格和内部装修紧密融合，不会显得突兀。无论是在宽敞的大厅、走廊，还是在各个诊疗区域，导视标识的材质、颜色和安装方式都与周围环境相协调，既 起到了引导作用，又不破坏医院的整体美感。

## 4.2.2. 信息呈现方式

(1) 信息准确全面：导视系统中的信息准确无误，能够清晰地告知患者各个科室的位置、楼层、就诊流程等关键信息。无论是文字说明还是图标指示，都经过精心设计和准确表达，确保患者能够根据导视 信息顺利找到目的地。例如，在电梯口和走廊交汇处的导视牌上，详细标注了各楼层的科室分布，让患 者在进入医院后能够快速了解医院的布局。

DOI: 10.12677/design.2024.96846 设计

* * *

李增瑞，孙声

(2) 信息分层清晰：对信息进行了合理的分层设计，从医院的整体布局到具体的科室位置，都有明确的指引。在医院的主要入口处，设置了一级索引标识，提供医院的整体平面图和各区域的大致方向；在 楼层之间的转换区域，设置了二级导视，明确各楼层的科室分布；在科室门口，则设置了三级标识，详 细标注了科室的名称和具体的房间号，方便患者精准定位。

(3) 信息更新及时：随着医院的发展和科室的调整，导视系统的信息能够及时进行更新，确保患者获取的信息始终是准确的。医院有专门的管理团队负责导视系统的维护和更新，保证信息的时效性。

## 4.2.3. 人性化设计

(1) 考虑患者需求：充分考虑到了患者的特殊需求，例如为行动不便的患者设置了无障碍导视标识，
标识的高度和位置都便于轮椅使用者查看。同时，梅奥诊所在导视信息的设计上，也充分考虑到了患者 的视力、阅读能力等因素，采用了较大的字体和醒目的颜色，方便患者获取信息(如图 2)。

(2) 提供温馨提示：除了基本的导视信息外，还会在一些关键位置设置温馨提示，如提醒患者注意安全、遵守医院的规定等。这些提示信息能够帮助患者更好地适应医院的环境，提高就医的安全性和 舒适性。

(3) 融入文化元素：梅奥诊所的导视系统设计中融入了医院的文化元素，体现了医院的价值观和服务理念。例如，在一些公共区域的导视牌上，会展示医院的历史、文化和荣誉，让患者在就医的过程中能 够了解医院的文化底蕴，增强对医院的信任和认可。

**Figure 2. Mayo Clinic guide system, USA**

图 2 . 美国梅奥诊所导视系统 ②

## 4.3. 川西市综合医疗中心导视系统分析

4.3.1. 设计风格
(1) 整体概念特色：hada 工作室以“花园医院”为概念进行设计，这一概念使得导视系统与医疗中心的周边环境以及整体氛围相契合。将自然元素融入到导视设计中，为患者和医护人员营造出一种温馨、 舒适且亲近自然的感觉，有助于缓解人们在医疗场所中可能产生的紧张情绪(如图 3)。

DOI: 10.12677/design.2024.96846 设计

* * *

(2) 色彩运用：在外部平面设计上，采用了川西的里山和合川的色彩，并且在病房区域，里山的春秋景观以及枫叶的颜色成为东西病房的象征。这种色彩的运用不仅具有地域特色，能够传达川西自然环境的魅力，还通过不同的配色方案让人们感受到四季的变化，为相对单调的医疗环境增添了丰富的视觉元素和活力。

(3) 造型设计：导视系统的造型设计可能相对简洁大方，不过多追求复杂的装饰，以确保信息的清晰传达。同时，在一些细节上可能会有独特的设计，比如采用特殊的材质或形状来吸引人们的注意力，使导视标识既具有功能性，又具有一定的艺术美感。

Figure 3. Guide system of Kawanishi comprehensive medical center
③
图 3 . 川西市综合医疗中心导视系统

③
图 3 . 川西市综合医疗中心导视系统

(2) 信息的分级与分类：对于医疗中心这样复杂的场所，信息的分级和分类非常重要。导视系统可能会将信息分为不同的级别，如一级导向标识用于引导人们进入医院院区和各个单体建筑，二级导向标识用于引导人们在单体建筑内到达目的就医科室，三级导向标识则用于具体房间的功能性说明。这种分级分类的方式可以使信息更加有条理，方便人们快速找到自己需要的信息。
(3) 多语言支持：作为一个综合医疗中心，可能会接待来自不同地区的患者和访客，因此导视系统需

4.3.2. 信息呈现方式

* * *

李增瑞，孙声

## 4.3.3. 文化融合

(1) 色彩运用体现地域特色：在外部平面设计中，融入了川西的里山和合川的色彩。这种色彩的选择并非随意，而是基于对当地自然景观和文化特色的深入理解与提炼。里山是日本传统的乡村景观，具有 独特的生态和文化价值，将其色彩融入导视系统，能够让人们在进入医疗中心的瞬间，感受到强烈的地 域文化氛围，增强对该地区的认同感和归属感。

(2) 简洁风格与传统美学的平衡：导视系统的整体设计风格简洁大方，符合现代设计的审美趋势和功能需求。同时，在简洁的设计中，又蕴含着日本传统文化中对简洁、纯粹的追求。例如，标识牌上的文字 简洁明了，没有过多的装饰和复杂的图案，这与日本传统的书法艺术和平面设计理念相契合，体现了传 统文化在现代设计中的传承和发展。

(3) 通用标识的国际化：在导视系统的图标和标识设计中，借鉴了国际通用的医疗标识和符号，以便于不同国家和地区的患者能够快速理解和识别。这体现了日本在医疗领域对国际标准的重视和借鉴，同 时也反映了全球化背景下文化交流和融合的趋势。 人性化设计的国际理念引入：导视系统的设计充分考虑了患者的需求和体验，这与国际上先进的医 疗设计理念相契合。例如，在标识的高度、位置和字体大小等方面，都进行了精心的设计，以方便不同 年龄、身体状况的患者查看。这种人性化的设计理念不仅体现了对患者的关爱，也反映了日本医疗中心 在设计上积极吸收国际先进经验的开放态度。

## 4.4. 小结

4.4.1. 相同点 从设计目的来看，国内外医疗机构导视系统都以方便患者就医、提高医疗效率为主要目标。都遵 循可视性、易懂性、系统性等基本设计原则，确保导视信息能够准确传达给患者。在与医疗流程的结 合方面，都重视根据患者的就医顺序和行动路线来设置导视标识，减少患者在就医过程中的困惑和时 间浪费。

## 4.4.2. 区别

在文化表达上，国外案例更注重突出本国文化特色，如美国梅奥诊所的效率文化、日本立川综合医 院的关怀文化，而中国香港大学深圳医院则是融合了中西方文化。在设计细节方面，日本的导视系统更 强调趣味性和情感关怀，美国则侧重于专业性和简洁性，中国香港大学深圳医院在融合多元文化的基础 上注重实用性。在材质选择上，各国根据自身的资源和环保理念有所不同，日本注重质感和触感，美国 追求高品质和耐用性，中国香港大学深圳医院则兼顾环保和美观。

# 5\. 结论

通过对国内外医疗机构导视系统设计案例的分析，可以看出国内外在设计上既有相同点又有区别。 我国在医疗机构导视系统设计中，可以吸收国外的优势，如进一步强化文化内涵的融入，不仅仅是简单 的地域文化体现，更要深入挖掘医院自身的文化价值。在信息呈现方面，可以学习国外对于复杂信息的 分解和详细标注的方法，提高信息的实用性。同时，我国的导视系统设计也有自身的亮点，如多语言服 务等，应继续保持和优化。在未来的设计中，要紧密结合我国的医疗政策，以提升患者就医体验为核心 目标，打造更加完善、高效、人性化的医疗机构导视系统，为我国医疗事业的发展提供有力支持，同时 也为全球医疗导视系统设计贡献中国智慧。在设计过程中，要充分考虑到随着科技发展和社会变化，患 者对于导视系统可能产生的新需求，如与智能设备的交互等，不断创新设计理念和方法。

DOI: 10.12677/design.2024.96846 设计

* * *

李增瑞，孙声

# 注 释

① 图 1 来源：网页引用， [https://www.sohu.com/a/73040631\_358997。](https://www.sohu.com/a/73040631_358997%E3%80%82) ② 图 2 来源：网页引用， [https://blog.csdn.net/mdg666/article/details/132227699。](https://blog.csdn.net/mdg666/article/details/132227699%E3%80%82) ③ 图 3 来源：网页引用， [https://www.zcool.com.cn/article/ZMTYxMTgyMA==.html。](https://www.zcool.com.cn/article/ZMTYxMTgyMA==.html%E3%80%82)

# 参考文献

\[1\] 梅文凤, 任玉洁. 基于服务设计的澳门公共医疗机构导视系统优化设计óó以仁伯爵综合医院为例\[J\]. 设计, 2023(19): 61-66. \[2\] 汤贺平. 人文关怀下公共医疗空间交互导视系统设计探究\[D\]: \[硕士学位论文\]. 沈阳: 沈阳师范大学, 2024: 2. \[3\] 徐磊青. 人体工程学与环境行为学\[M\]. 北京: 中国建筑工业出版社: 2010. \[4\] \[美\]唐纳德·A·诺曼. 设计心理学 1 \[M\]. 梅琼, 译. 北京: 中信出版社: 2010. \[5\] \[美\]唐纳德·A·诺曼. 设计心理学 2 \[M\]. 梅琼, 译. 北京: 中信出版社: 2010. \[6\] \[日\]田中直人. 通用标识设计手法与实践\[M\]. 北京: 中国建筑工业出版社: 2014.

DOI: 10.12677/design.2024.96846 设计

### 来源 5: A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness

- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9656047/
- 精读方法：firecrawl-scrape

Checking your browser before accessing pmc.ncbi.nlm.nih.gov ...

Click [here](https://www.google.com/recaptcha/challengepage/#) if you are not automatically redirected after 5 seconds.

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**

reCAPTCHA

### 来源 6: 医院导视系统

- URL: https://www.pinterest.com/ideas/%E5%8C%BB%E9%99%A2%E5%AF%BC%E8%A7%86%E7%B3%BB%E7%BB%9F/948575276788
- 精读方法：failed

精读失败：403 Client Error: Forbidden for url: https://api.firecrawl.dev/v2/scrape

### 来源 7: Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan

- URL: https://www.mdpi.com/2220-9964/10/8/570
- 精读方法：firecrawl-scrape

Next Article in Journal

[Application-Based COVID-19 Micro-Mobility Solution for Safe and Smart Navigation in Pandemics](https://www.mdpi.com/2220-9964/10/8/571)

Previous Article in Journal

[Spatiotemporal Dynamic Analysis of A-Level Scenic Spots in Guizhou Province, China](https://www.mdpi.com/2220-9964/10/8/568)

## Journals

[Active Journals](https://www.mdpi.com/about/journals) [Find a Journal](https://www.mdpi.com/about/journalfinder) [Journal Proposal](https://www.mdpi.com/about/journals/proposal) [Proceedings Series](https://www.mdpi.com/about/proceedings)

[**Topics**](https://www.mdpi.com/topics)

## Information

[For Authors](https://www.mdpi.com/authors) [For Reviewers](https://www.mdpi.com/reviewers) [For Editors](https://www.mdpi.com/editors) [For Librarians](https://www.mdpi.com/librarians) [For Publishers](https://www.mdpi.com/publishing_services) [For Societies](https://www.mdpi.com/societies) [For Conference Organizers](https://www.mdpi.com/conference_organizers)

[Open Access Policy](https://www.mdpi.com/openaccess) [Institutional Open Access Program](https://www.mdpi.com/ioap) [Special Issues Guidelines](https://www.mdpi.com/special_issues_guidelines) [Editorial Process](https://www.mdpi.com/editorial_process) [Research and Publication Ethics](https://www.mdpi.com/ethics) [Article Processing Charges](https://www.mdpi.com/apc) [Awards](https://www.mdpi.com/awards) [Testimonials](https://www.mdpi.com/testimonials)

[**Author Services**](https://www.mdpi.com/authors/english)

## Initiatives

[Sciforum](https://sciforum.net/) [MDPI Books](https://www.mdpi.com/books) [Preprints.org](https://www.preprints.org/) [Scilit](https://www.scilit.com/) [SciProfiles](https://sciprofiles.com/) [Encyclopedia](https://encyclopedia.pub/) [JAMS](https://jams.pub/) [Proceedings Series](https://www.mdpi.com/about/proceedings)

## About

[Overview](https://www.mdpi.com/about) [Contact](https://www.mdpi.com/about/contact) [Careers](https://careers.mdpi.com/) [News](https://www.mdpi.com/about/announcements) [Press](https://www.mdpi.com/about/press) [Blog](http://blog.mdpi.com/)

[Sign In / Sign Up](https://www.mdpi.com/user/login)

## Notice

You can make submissions to other journals
[here](https://susy.mdpi.com/user/manuscripts/upload).

_clear_

## Notice

You are accessing a machine-readable page. In order to be human-readable, please install an RSS reader.

ContinueCancel

_clear_

All articles published by MDPI are made immediately available worldwide under an open access license. No special
permission is required to reuse all or part of the article published by MDPI, including figures and tables. For
articles published under an open access Creative Common CC BY license, any part of the article may be reused without
permission provided that the original article is clearly cited. For more information, please refer to
[https://www.mdpi.com/openaccess](https://www.mdpi.com/openaccess).

Feature papers represent the most advanced research with significant potential for high impact in the field. A Feature
Paper should be a substantial original Article that involves several techniques or approaches, provides an outlook for
future research directions and describes possible research applications.

Feature papers are submitted upon individual invitation or recommendation by the scientific editors and must receive
positive feedback from the reviewers.

Editor’s Choice articles are based on recommendations by the scientific editors of MDPI journals from around the world.
Editors select a small number of articles recently published in the journal that they believe will be particularly
interesting to readers, or important in the respective research area. The aim is to provide a snapshot of some of the
most exciting work published in the various research areas of the journal.

Original Submission Date Received: .

[![ijgi-logo](https://pub.mdpi-res.com/img/journals/ijgi-logo.png?0b04dd6b73016292)](https://www.mdpi.com/journal/ijgi)

[Submit to this Journal](https://susy.mdpi.com/user/manuscripts/upload?form%5Bjournal_id%5D%3D113) [Review for this Journal](https://susy.mdpi.com/volunteer/journals/review) [Propose a Special Issue](https://www.mdpi.com/journalproposal/sendproposalspecialissue/ijgi)

[►▼\\
Article Menu](https://www.mdpi.com/2220-9964/10/8/570#)

## Article Menu

- [Academic Editor](https://www.mdpi.com/2220-9964/10/8/570#academic_editors)

![](https://pub.mdpi-res.com/bundles/mdpisciprofileslink/img/unknown-user.png?1781764495)Wolfgang Kainz

- [Recommended Articles](https://www.mdpi.com/2220-9964/10/8/570#)
- [Related Info Link](https://www.mdpi.com/2220-9964/10/8/570#related)

  - [Google Scholar](http://scholar.google.com/scholar?q=Exploring%20the%20Planning%20and%20Configuration%20of%20the%20Hospital%20Wayfinding%20System%20by%20Space%20Syntax%3A%20A%20Case%20Study%20of%20Cheng%20Ching%20Hospital%2C%20Chung%20Kang%20Branch%20in%20Taiwan)

- [More by Authors Links](https://www.mdpi.com/2220-9964/10/8/570#authors)

  - on DOAJ

    - [Chen, M.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Ming-Shih%20Chen%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)
    - [Ko, Y.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Yao-Tsung%20Ko%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)
    - [Hsieh, W.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Wen-Che%20Hsieh%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)

  - on Google Scholar

    - [Chen, M.](http://scholar.google.com/scholar?q=Ming-Shih%20Chen)
    - [Ko, Y.](http://scholar.google.com/scholar?q=Yao-Tsung%20Ko)
    - [Hsieh, W.](http://scholar.google.com/scholar?q=Wen-Che%20Hsieh)

  - on PubMed

    - [Chen, M.](http://www.pubmed.gov/?cmd=Search&term=Ming-Shih%20Chen)
    - [Ko, Y.](http://www.pubmed.gov/?cmd=Search&term=Yao-Tsung%20Ko)
    - [Hsieh, W.](http://www.pubmed.gov/?cmd=Search&term=Wen-Che%20Hsieh)

[Article Views](https://www.mdpi.com/2220-9964/10/8/570#metrics)

[Citations-](https://www.mdpi.com/2220-9964/10/8/570#metrics)

- [Table of Contents](https://www.mdpi.com/2220-9964/10/8/570#table_of_contents)

Altmetric[_share_ Share](https://www.mdpi.com/2220-9964/10/8/570# "Share") [_announcement_ Help](https://www.mdpi.com/2220-9964/10/8/570# "Help")_format\_quote_ Cite [_question\_answer_ Discuss in SciProfiles](https://sciprofiles.com/discussion-groups/public/10.3390/ijgi10080570?utm_source=mpdi.com&utm_medium=publication&utm_campaign=discuss_in_sciprofiles "Discuss in Sciprofiles")

## Need Help?

### Support

Find support for a specific problem in the support section of our website.

[Get Support](https://www.mdpi.com/about/contactform)

### Feedback

Please let us know what you think of our products and services.

[Give Feedback](https://www.mdpi.com/feedback/send)

### Information

Visit our dedicated information section to learn more about MDPI.

[Get Information](https://www.mdpi.com/authors)

_clear_

## JSmol Viewer

_clear_

_first\_page_

[Download PDF](https://www.mdpi.com/2220-9964/10/8/570/pdf?version=1629797845)

_settings_

[Order Article Reprints](https://www.mdpi.com/2220-9964/10/8/570/reprints)

Font Type:

_Arial__Georgia__Verdana_

Font Size:

AaAaAa

Line Spacing:

______

Column Width:

______

Background:

Open AccessFeature PaperArticle

# Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan

by

Ming-Shih Chen

![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Ming-Shih Chen

[SciProfiles](https://sciprofiles.com/profile/author/SW9jMjdZdUNqa2pneHFldTRsRzhZUT09?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Ming-Shih%20Chen) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Ming-Shih+Chen%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Ming-Shih+Chen)

,

Yao-Tsung Ko

![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Yao-Tsung Ko

[SciProfiles](https://sciprofiles.com/profile/933191?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Yao-Tsung%20Ko) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Yao-Tsung+Ko%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Yao-Tsung+Ko)

\* and

Wen-Che Hsieh

![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Wen-Che Hsieh

[SciProfiles](https://sciprofiles.com/profile/author/WTM4eEN6OTFrRjM2Z3BqVmxNZHBYRnorWHlpMnF3WTlaUERRb01JcjJtST0=?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Wen-Che%20Hsieh) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Wen-Che+Hsieh%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Wen-Che+Hsieh)

Department of Industrial Design, Tunghai University, No. 1727, Sec. 4, Taiwan Boulevard, Xitun District, Taichung City 40704, Taiwan

\*

Author to whom correspondence should be addressed.

_ISPRS Int. J. Geo-Inf._ **2021**, _10_(8), 570; [https://doi.org/10.3390/ijgi10080570](https://doi.org/10.3390/ijgi10080570)

Submission received: 26 June 2021
/
Revised: 12 August 2021
/
Accepted: 20 August 2021
/
Published: 23 August 2021

Download _keyboard\_arrow\_down_

[Download PDF](https://www.mdpi.com/2220-9964/10/8/570/pdf?version=1629797845)

[Download PDF with Cover](https://www.mdpi.com/2220-9964/10/8/570#)

[Download XML](https://www.mdpi.com/2220-9964/10/8/570#)

[Download Epub](https://www.mdpi.com/2220-9964/10/8/570/epub)

[Browse Figures](https://www.mdpi.com/2220-9964/10/8/570#)

[\
                        <strong>Figure 1</strong><br/>\
                                                    <p>Dynamic space syntax graph [<a href="#B34-ijgi-10-00570" class="html-bibr">34</a>].</p>\
                                                ](https://pub.mdpi-res.com/ijgi/ijgi-10-00570/article_deploy/html/images/ijgi-10-00570-g001.png?1629797931 "                         <strong>Figure 1</strong><br/>                                                     <p>Dynamic space syntax graph [<a href=\"#B34-ijgi-10-00570\" class=\"html-bibr\">34</a>].</p>                                                 ")[\
                        <strong>Figure 2</strong><br/>\
                                                    <p>Analysis of the axial map [<a href="#B34-ijgi-10-00570" class="html-bibr">34</a>].</p>\
                                                ](https://pub.mdpi-res.com/ijgi/ijgi-10-00570/article_deploy/html/images/ijgi-10-00570-g002.png?1629797931 "                         <strong>Figure 2</strong><br/>                                                     <p>Analysis of the axial map [<a href=\"#B34-ijgi-10-00570\" class=\"html-bibr\">34</a>].</p>                                                 ")[\
                        <strong>Figure 3</strong><br/>\
                                                    <p>Classification of the content of the signage in the research field.</p>\
                                                ](https://pub.mdpi-res.com/ijgi/ijgi-10-00570/article_deploy/html/images/ijgi-10-00570-g003.png?1629797931 "                         <strong>Figure 3</strong><br/>                                                     <p>Classification of the content of the signage in the research field.</p>                                                 ")[\
                        <strong>Figure 4</strong><br/>\
                                                    <p>Classification of the forms of the signage in the research field.</p>\
                                                ](https://pub.mdpi-res.com/ijgi/ijgi-10-00570/article_deploy/html/images/ijgi-10-00570-g004.png?1629797931 "                         <strong>Figure 4</strong><br/>                                                     <p>Classification of the forms of the signage in the research field.</p>                                                 ")[\
                        <strong>Figure 5</strong><br/>\
                                                    <p>The signage configuration and distribution of the outpatient areas B1 to 2F in CCH/CKB.</p>\
                                                ](https://pub.mdpi-res.com/ijgi/ijgi-10-00570/article_deploy/html/images/ijgi-10-00570-g005.png?1629797931 "                         <strong>Figure 5</strong><br/>                                                     <p>The signage configuration and distribution of the outpatient areas B1 to 2F in CCH/CKB.</p>                                                 ")[\
                        <strong>Figure 6</strong><br/>\
                                                    <p>The axial mapping analysis of the first floor of the CCH/CKB Building.</p>\
                                                ](https://pub.mdpi-res.com/ijgi/ijgi-10-00570/article_deploy/html/images/ijgi-10-00570-g006.png?1629797931 "                         <strong>Figure 6</strong><br/>                                                     <p>The axial mapping analysis of the first floor of the CCH/CKB Building.</p>                                                 ")[\
                        <strong>Figure 7</strong><br/>\
                                                    <p>The axial mapping analysis of the first basement floor of the CCH/CKB Building.</p>\
                                                ](https://pub.mdpi-res.com/ijgi/ijgi-10-00570/article_deploy/html/images/ijgi-10-00570-g007.png?1629797931 "                         <strong>Figure 7</strong><br/>                                                     <p>The axial mapping analysis of the first basement floor of the CCH/CKB Building.</p>                                                 ")[\
                        <strong>Figure 8</strong><br/>\
                                                    <p>The axial mapping analysis of the second floor of the CCH/CKB Building.</p>\
                                                ](https://pub.mdpi-res.com/ijgi/ijgi-10-00570/article_deploy/html/images/ijgi-10-00570-g008.png?1629797931 "                         <strong>Figure 8</strong><br/>                                                     <p>The axial mapping analysis of the second floor of the CCH/CKB Building.</p>                                                 ")[\
                        <strong>Figure 9</strong><br/>\
                                                    <p>The research recorder observed and recorded the participants performing the wayfinding tasks.</p>\
                                                ](https://pub.mdpi-res.com/ijgi/ijgi-10-00570/article_deploy/html/images/ijgi-10-00570-g009.png?1629797931 "                         <strong>Figure 9</strong><br/>                                                     <p>The research recorder observed and recorded the participants performing the wayfinding tasks.</p>                                                 ")[\
                        <strong>Figure 10</strong><br/>\
                                                    <p>The behavioral annotation diagram and points where participants became lost on the first basement floor of the CCH/CKB Building.</p>\
                                                ](https://pub.mdpi-res.com/ijgi/ijgi-10-00570/article_deploy/html/images/ijgi-10-00570-g010.png?1629797931 "                         <strong>Figure 10</strong><br/>                                                     <p>The behavioral annotation diagram and points where participants became lost on the first basement floor of the CCH/CKB Building.</p>                                                 ")[\
                        <strong>Figure 11</strong><br/>\
                                                    <p>The overlapping map of the signage, axis and route isovist on the first basement floor of the CCH/CKB Building.</p>\
                                                ](https://pub.mdpi-res.com/ijgi/ijgi-10-00570/article_deploy/html/images/ijgi-10-00570-g011.png?1629797931 "                         <strong>Figure 11</strong><br/>                                                     <p>The overlapping map of the signage, axis and route isovist on the first basement floor of the CCH/CKB Building.</p>                                                 ")[\
                        <strong>Figure 12</strong><br/>\
                                                    <p>The visual area of the subject location in the intersection area of route numbers 186, 32, 2, and 8.</p>\
                                                ](https://pub.mdpi-res.com/ijgi/ijgi-10-00570/article_deploy/html/images/ijgi-10-00570-g012.png?1629797931 "                         <strong>Figure 12</strong><br/>                                                     <p>The visual area of the subject location in the intersection area of route numbers 186, 32, 2, and 8.</p>                                                 ")

[Review Reports](https://www.mdpi.com/2220-9964/10/8/570/review_report) [Versions Notes](https://www.mdpi.com/2220-9964/10/8/570/notes)

## Abstract

**:**

With regard to the outpatient areas of a hospital, the smoothness of the route is now taken into consideration in the process of configuring the wayfinding system. As patients often spend time on ineffective wayfinding processes, and there is limited manpower at hospitals and a lack of clarity in the information provided by the wayfinding system, it is difficult to provide effective and timely consultation services for patients. This study was conducted at Cheng Ching Hospital, Chung Kang Branch (CCH/CKB) in Taiwan. This study attempts to investigate the relationships between the wayfinding system of the outpatient areas and the patients’ behaviors in the hospital. Depthmap software based on space syntax is adopted to assist in the route analysis and wayfinding behaviors. It integrates axial mapping analysis and isovist analysis and gives suggestions on the location, format and content of the wayfinding system. The final results of the study show that in the wayfinding task experiment gender has no significant impact on the effect of wayfinding efficiency, while a significant difference is found for age. Older people need more time to complete the wayfinding task, which means that they have poorer performance in wayfinding efficiency. The analysis of the results of space syntax shows that a good wayfinding system should be a symmetric tree-branch structure rather than circular structure in a medical building, that areas where it is easy to become lost should have a clear signage guiding system planning and configuration, and that clear guidance information should be provided to the patients to achieve the goal of saving consultation time and improving the quality of the medical environment.

Keywords:

[health care facilities](https://www.mdpi.com/search?q=health+care+facilities); [outpatient areas](https://www.mdpi.com/search?q=outpatient+areas); [wayfinding system](https://www.mdpi.com/search?q=wayfinding+system); [space syntax](https://www.mdpi.com/search?q=space+syntax); [wayfinding behaviors](https://www.mdpi.com/search?q=wayfinding+behaviors)

## 1\. Introduction

Nowadays, medical treatment is naturally more advanced, and the types of diseases and treatment methods used are becoming more and more detailed. Hence, the space required for the corresponding examination and treatment in different units has been expanded at health care facilities in order to meet the demands for medical treatment. Facing these changes in medical operations and more detailed diagnostic units, if health care facilities do not have additional land or sufficient funds to construct a new medical building, then when it comes to the early-stage wayfinding system configuration and planning the primary consideration is indoor partitioning and changing the routes in existing buildings to meet the new demands. In such cases the changed units receive additional signage to aid indoor route planning, but this often lacks overall consideration and ignores the different needs of different groups of people, resulting in great difficulties for patients when using the wayfinding system. A good wayfinding system in outpatient areas should place signage in appropriate locations to guide patients to quickly reach the required area to receive medical services. Routes and signage are both environmental factors in wayfinding processes \[ [1](https://www.mdpi.com/2220-9964/10/8/570#B1-ijgi-10-00570)\]. It is thus necessary to construct a user-friendly framework for an indoor public space wayfinding system for health care facilities, for use by both patients and visitors \[ [2](https://www.mdpi.com/2220-9964/10/8/570#B2-ijgi-10-00570), [3](https://www.mdpi.com/2220-9964/10/8/570#B3-ijgi-10-00570)\].

Blumberg and Devlin \[ [4](https://www.mdpi.com/2220-9964/10/8/570#B4-ijgi-10-00570)\] pointed out that the amount of wayfinding behaviors among hospital users is an important indicator of the pressure put on hospital consultations. In a complex public environment, all such behaviors must be guided by information and intelligence objects in the environment to be successfully completed. Chen \[ [5](https://www.mdpi.com/2220-9964/10/8/570#B5-ijgi-10-00570)\] noted that one way to handle wayfinding problems is related to the use of directories. Baskaya et al. \[ [6](https://www.mdpi.com/2220-9964/10/8/570#B6-ijgi-10-00570)\] indicated that space syntax and wayfinding systems are important environmental factors influencing indoor wayfinding. To reduce the occurrence of wayfinding problems, it is necessary to better understand the characteristics of wayfinding behaviors, the space syntax in which these occur, and to help people find their destinations through appropriate signage formats, thus addressing the problems people have with wayfinding and providing users with good spatial service quality. Huang and Tseng \[ [7](https://www.mdpi.com/2220-9964/10/8/570#B7-ijgi-10-00570)\] stated that the research on wayfinding signage design in medical environments in Taiwan is relatively limited, with most such studies examining the addition or expansion of wayfinding systems. They also stated that in the future more emphasis should be given to research on insufficient directional information and the decision points in the wayfinding behaviors.

Based on above, we attempted to investigate the content and form of the signage configuration in this research context, and further applied the space syntax theory and Depthmap software to assist in the simulation analysis of the routes in order to find out the wayfinding problems caused by the current spatial route planning in health care facilities. Based on the results we proposed some suggestions for wayfinding system planning and configuration for hospitals, thus achieving the purpose of this study.

## 2\. Related Works

#### 2.1. Characteristics of the Spatial Environment

Some researchers indicated that even well-designed signs often do not provide enough information to guide visitors to move freely in a hospital without becoming lost \[ [8](https://www.mdpi.com/2220-9964/10/8/570#B8-ijgi-10-00570), [9](https://www.mdpi.com/2220-9964/10/8/570#B9-ijgi-10-00570)\]. Carroll \[ [10](https://www.mdpi.com/2220-9964/10/8/570#B10-ijgi-10-00570)\] noted that floor plan complexity has a significant effect on wayfinding behaviors, while O’Neill \[ [11](https://www.mdpi.com/2220-9964/10/8/570#B11-ijgi-10-00570)\] suggested a close relationship between building plan complexity and the number of times people become lost. The sizes, forms and relationships among spaces and the irregularity of floor plans are the main causes of this complexity. Moderate and straightforward route planning in space will help reduce the problems of wayfinding, although too many route intersections will increase the number of decision points, making users more easily confused. Best \[ [12](https://www.mdpi.com/2220-9964/10/8/570#B12-ijgi-10-00570)\] pointed out that too many decision points increase the uncertainty of users’ judgments, creating confusion and increasing the difficulty of finding the way. Thus, too many decision points on a floor plan will cause difficulties in wayfinding. In fact, any point in the wayfinding process can be a decision point for behavior, which is not limited to the choice of directions. The lack of complete information in the environment also prevents users from constructing a complete spatial concept, resulting in an inability to recognize and analyze the situation when searching for directions \[ [13](https://www.mdpi.com/2220-9964/10/8/570#B13-ijgi-10-00570)\]. Arthur and Passini \[ [14](https://www.mdpi.com/2220-9964/10/8/570#B14-ijgi-10-00570)\] proposed decision making as a means for solving wayfinding spatial problems and determining decision execution and information processing, including environmental awareness and cognition. When planning and designing a hospital wayfinding system, it is necessary to consider both patients’ perceptions and the impact on the hospital space environment. For patients, good design can promote recovery, because when patients understand their environment and try to find their destination in a more relaxed way, it can re-establish a sense of control and accomplishment for them \[ [15](https://www.mdpi.com/2220-9964/10/8/570#B15-ijgi-10-00570), [16](https://www.mdpi.com/2220-9964/10/8/570#B16-ijgi-10-00570)\].

#### 2.2. Space Syntax Literatures

Space syntax theory is a method of “quantifying the environment as a set of predictive variables for specific behaviors” that predicts wayfinding behaviors in public areas by targeting people’s tendency to move to spaces with higher levels of integration; in other words, such spaces act as transit hubs and are more connected to other places \[ [17](https://www.mdpi.com/2220-9964/10/8/570#B17-ijgi-10-00570)\]. This principle has been demonstrated in various architectural layouts. Morgareidg et al. \[ [18](https://www.mdpi.com/2220-9964/10/8/570#B18-ijgi-10-00570)\] also applied space syntax to analyze emergency rooms for environmental planning and conducted research on the interaction situation with regard to users’ actual routes. Wang \[ [19](https://www.mdpi.com/2220-9964/10/8/570#B19-ijgi-10-00570)\] used space syntax to investigate the factors impacting wayfinding that resulted from the layout inside a museum. The results of axial mapping analysis and space syntax indicate that the longest routes have a higher proportion of wayfinding behaviors in the case of a moderate Rn value of route configuration characteristics, but the interlacing of complex routes and excessive number of decision points in a floor plan increase the chance of becoming lost significantly when the number of nodes (CN) of the moderate Rn value is six or more. If the environment does not provide complete information, the pathfinder cannot construct a complete spatial concept or carry out cognitive analysis, and thus cannot make correct wayfinding decisions. Chaudhary et al. \[ [20](https://www.mdpi.com/2220-9964/10/8/570#B20-ijgi-10-00570)\] applied the concept of space syntax to describe the configuration of medical buildings, such as making predictions on the movement of nurses through hospital units, by measuring their connectivity and integration and analyzing spatial configurations (i.e., layouts). Haq and Luo \[ [21](https://www.mdpi.com/2220-9964/10/8/570#B21-ijgi-10-00570)\] pointed out that many studies have used this technique to examine the spatial configurations of health care facilities, including wayfinding systems.

#### 2.3. Wayfinding Behavior

The term “wayfinding” can be traced back to the 1960s when it was first mentioned by Kevin Lynch \[ [22](https://www.mdpi.com/2220-9964/10/8/570#B22-ijgi-10-00570)\] in his book The Image of the City. Lynch \[ [22](https://www.mdpi.com/2220-9964/10/8/570#B22-ijgi-10-00570)\] used “wayfinding” to explain people’s cognition and analytical capabilities toward the urban environment. The elements that prevent people from becoming lost in the urban space were classified through a process of experimentation, including: (1) orientation recognition; (2) environmental perception; (3) strategy adoption; (4) gender and age characteristics. Early environmental psychologists focused on exploring the relationships between “space” and “behavior”, trying to clarify the decision-making processes about how people will react and find the right route when they become lost in space and people’s perception, cognition, and route choice. Downs and Stea \[ [23](https://www.mdpi.com/2220-9964/10/8/570#B23-ijgi-10-00570)\] stated that wayfinding behavior is a process of people understanding which external environment they are in using a certain method and making route choices based on this. Evans et al. \[ [24](https://www.mdpi.com/2220-9964/10/8/570#B24-ijgi-10-00570)\] defined wayfinding behavior as “a work of recognizing and reacting to the complex space environment and guiding sign systems” from the perspective of human perception. Blades \[ [25](https://www.mdpi.com/2220-9964/10/8/570#B25-ijgi-10-00570)\] explained people’s wayfinding behavior in the environment based on them learning the characteristics of the current surrounding environment and recalling past experiences, and constructing and choosing the correct routes from the starting point to the destination. Some studies have claimed that men’s wayfinding ability is better than women’s, due to the differences in preference between men and women in the wayfinding strategies adopted. Men usually use an Euclidean strategy while women generally use a landmark one to find their ways. However, if the focus is on the time spent on the wayfinding process and the degree of hesitation and delay at decision points, there is no significant difference between men and women \[ [26](https://www.mdpi.com/2220-9964/10/8/570#B26-ijgi-10-00570), [27](https://www.mdpi.com/2220-9964/10/8/570#B27-ijgi-10-00570)\]. As for the relationship between age and wayfinding ability, most studies believe that older people have worse performance with regard to wayfinding \[ [28](https://www.mdpi.com/2220-9964/10/8/570#B28-ijgi-10-00570), [29](https://www.mdpi.com/2220-9964/10/8/570#B29-ijgi-10-00570)\]. In general, wayfinding behavior is not based on a single, linear information processing action, but is a recursive information process. The decision-making processes interact with each other at the psychological level after a person receives various stimuli based on environmental information, including the recognition of the complex structure of the spatial environment and the graphics of guiding sign systems.

#### 2.4. Decision-Making and Wayfinding Systems

MacMinner \[ [30](https://www.mdpi.com/2220-9964/10/8/570#B30-ijgi-10-00570)\] suggested that people use architectural space and internal information to determine their own location, indicating that “architectural space” and “internal processing” can be used as vision clues for users to identify their orientation. In architectural spaces, such as staircases, elevators, halls and corridors, spatial characteristics are used to identify orientation. Using the clues provided by the environment can reduce the chances of becoming lost. As for internal processing, this includes wall color, form and structure, floor changes, and the use of lighting techniques to emphasize or hide certain areas, such as ceiling treatments and the configuration of equipment. Rousek and Hallbeck \[ [31](https://www.mdpi.com/2220-9964/10/8/570#B31-ijgi-10-00570)\] pointed out that a well-designed guiding wayfinding system for health care facilities should take into account the internal and external environment, pay attention to relevant design elements to improve understanding, and integrate visual guidelines with the design concept to reduce the pressure and anxiety of the people attending a clinic and, thus, achieve the greatest independence of the individual. Koneczny et al. \[ [32](https://www.mdpi.com/2220-9964/10/8/570#B32-ijgi-10-00570)\] stated that improper design planning will cause wayfinding-related difficulties for the public, such as: (1) improper decorative elements such as luminous floor tiles; (2) too bright or too dark lighting may be misleading; and (3) too small a signage size and improper placement, along with many other factors.

In the past, most studies on wayfinding behaviors and signage systems used questionnaires combined with on-site examinations of the actual behaviors of experimental participants. However, traditional experiments and questionnaires are time-consuming and labor-intensive, and often result in human interference that impacts the findings of the research. Nowadays, with the advance of digital technology, computer techniques can provide researchers with more accurate and efficient assistance in the study of wayfinding behaviors. Moreover, the use of data to analyze the deeper meaning of spatial complexes and to carry out image analysis can help explain people’s movement habits and navigation needs in space. Therefore, in this study, we aim to use the Depthmap analysis software with space syntax as a tool for analysis and prediction to find the points where people tend to become lost in order to provide useful references for health care facilities in designing and planning their wayfinding systems.

## 3\. Methodology

In this study, we adopted the axial mapping analysis and isovist analysis of Depthmap software based on space syntax to define the routes people use in health care facilities and predict the frequency and visual location of each route. The results of the axial mapping and isovist analysis are applied to provide references for the relative health care facilities to establish their wayfinding systems.

#### 3.1. Research Field

In this study, Cheng Ching Hospital, Chung Kang Branch (CCH/CKB), Taichung, Taiwan was taken as the research field, with the focus on the outpatient medical space from the first basement floor to the second floor of the Chung Kang Building. The spatial configuration and composition characteristics of the research field are described below:

(1)

First floor of Chung Kang Building

The first floor of Cheng Ching Hospital, Chung Kang Branch is the entrance/exit for the patients. The entrance of main route is located at Fukang Rd. The major structure is centered on a high-ceilinged lobby. The lobby itself also serves as the mobile space of the institute and the medical collection and waiting area. Therefore, after entering the lobby you have the pharmacy (medicine collection office) on your left and the united service center on the right, which is used for first-time patients to find the consultation unit, make an appointment and give basic information.

(2)

Second floor of Chung Kang Building

This floor is divided into mental health, dentistry, otorhinolaryngology, psychiatry, and infectious disease units with a semi-open waiting area connecting to private treatment spaces.

(3)

First basement floor of Chung Kang Building

The main consultation units and examination rooms as well as the appointment and cashier counter are located on the first basement floor. The outpatient areas include internal medicine, medical, surgery, family medicine, rehabilitation, and health care consultation rooms, while the examination rooms include general physiological examination rooms, blood sampling stations, cardiology-related examination rooms, extracorporeal shock wave rooms, urodynamic rooms, and radiology-related examination spaces.

#### 3.2. Space Syntax Theory

Shu (1999) analyzed the deeper meaning of space syntax. The foundation of its inner structural logic can be divided into two directions: relative depth and choice of path. Relative depth refers to the relative position and connection relationships among the elements of the structure in the space syntax system, and from this is derived a depth relationship expression where each route can be regarded as a unit in the dynamic space syntax ( [Figure 1](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f001)), and this is used to discuss the depth relationship, while the path choice is based on all possible paths for the intercommunication between any two elements in the space syntax system. Although there may be more than one path choice between two elements in the system, the relative depth relationship between them is unique, i.e., the shortest path depth between them. Taking the example in this study, there are many paths from the lobby of the Chung Kang Building to the appointment and cashier counter on the first basement floor for path choice; however, from the analysis of relative depth, the relative depth is the layer of the shortest routes to reach the destination \[ [33](https://www.mdpi.com/2220-9964/10/8/570#B33-ijgi-10-00570)\].

The element, “longest route”, comes from two perspectives, visibility and permeability, both of which are related to innate human instincts. In this study, the concept of the decomposed elements of the longest route was used to analyze the outpatient area routes of the health care facilities. As shown in [Figure 2](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f002), in the spatial floor plan configuration, by plotting the longest route connecting units we can develop an axial map. After analyzing this, we can obtain the integration of each longest route presented by color code, ranging from red to blue (high to low integration). Hence, we can learn from an axial map that the longest route 1 (red lines) is the most convenient location in the area, while the longest route 12 (blue lines) is in the least convenient location.

A detailed introduction to the related proper nouns of space syntax theory is given below \[ [35](https://www.mdpi.com/2220-9964/10/8/570#B35-ijgi-10-00570)\]:

Rn: Rn is the meaning of “global integration” in space syntax. Rn is used to calculate the deep or shallow relationships between each space or each axis. The spaces or axes with high global integration are those that reach all other spaces or axes with relatively few steps. That is to say, these spaces or axes with high global integration are distributed in convenient locations that are easier to reach in the spatial organization.

CN: CN means the connectivity between spaces and axes. It is used to calculate the sum of each space or axis connected to other spaces or axes.

Axial map/Axial mapping analysis: Space syntax theory compares the axis of space to the movement of a person in space. Each axis represents a number of steps in space, and movement also represents the visibility of a person in motion. In principle, a fewer number of axes is better, and a longer length of axes is better. Axial mapping analysis is used to present the deduction process of the overall spatial axis map in the most concise way.

Isovist analysis: Isovist analysis is also called visual graph analysis. Any position in the space can produce its isovist. Its definition is the maximum visual range we can see from a certain position. Isovist analysis is based on the integration to calculate the spatial neighborhood size and clustering coefficient and the mean shortest path length boundary. In this way, a visual image of the space is generated. Therefore, isovist analysis can show the relationships between visibility and permeability in space. The characteristics of visual graphics are closely related to the manifestations of space perception, such as wayfinding, movement and space use.

## 4\. Experiments and Analysis Results

In this study, the CCH/CKB medical building was taken as the major research field. In the physical investigation, the outpatient areas from the first basement floor to the second floor of the medical building were used as the experiment site. In the first part of the study, we investigated the distribution and location of consultation rooms and examination rooms in the outpatient areas and recorded the type of signage and locations, then we applied space syntax to draw the paths and routes to anticipate the user behavior tendency and visual concentration areas. The experimental results of the participants’ wayfinding tasks were compared to the analysis results predicted by space syntax, to see if they are consistent. Finally, we applied axial mapping analysis and isovist analysis to make a consolidated summary in order to give suggestions on planning the wayfinding system at the research field.

#### 4.1. Outpatient Areas Space Configuration and Signage Forms

In this paper, we first analyzed and annotated the signage configuration and forms from the first basement floor to the second floor of the outpatient areas of the building, and used different symbols to represent the different attributes of the signage, and finally summarized them into two major blocks: (1) the contents of the signage: identification, guidance, direction and description, in total four types ( [Figure 3](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f003)); (2) the forms of the signage: free stand, up hanging, protruding and wall-mounted, in total four types ( [Figure 4](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f004)).

We actually went to CCH/CKB hospital to do fieldwork. Based on the above classification of the content and presentation format of signage, we investigated and recorded the signage configuration and distribution in the outpatient area from the first basement floor to the second floor. The detailed information is marked on the layout diagram of each floor. The analysis results are shown in [Figure 5](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f005).

The results showed that there are seven categories and 82 signs in the outpatient area from the first basement floor to the second floor. Among them, the distribution of the up hanging type with guidance contents has a maximum of 23 signs, accounting for 28.05% of the total. Next is the signage of the wall-mounted type with identification contents with 21 examples, accounting for 25.61% of the total. In addition, in terms of floor distribution, the number and types of the signage are the most on the first basement floor due to its larger area and more clinic and examination rooms, with a total of seven categories and 53 signs. The number and type distribution of the signage on each floor is shown in [Table 1](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t001).

#### 4.2. The Results of Axial Mapping Analysis

#### 4.2.1. The First Floor of CCH/CKB Medical Building

The main entrance/exit route of CCH/CKB Building is the first floor, and the main building is accessed via route number 62. For direct access to the outpatient areas on the second floor, the vertical routes available are escalator route 60, elevators 235–237 and 232–234; staircases are also available, with route 246 to the second floor. The most common routes on the first floor of the building can be seen in [Figure 6](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f006), and the properties of each route can be compared in [Table 2](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t002). The routes in each section are numbered by Depthmap software, and the global integration is ranked by the Rn value of all the outpatient area routes in the medical building after axial mapping analysis. A larger Rn value indicates higher integration and a rank closer to the top; in contrast, a smaller Rn value with lower integration is ranked towards the bottom. From the axial mapping analysis of the first floor of the CCH/CKB Building in [Figure 6](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f006), we can predict that the escalators to the first basement floor of the medical building with the route numbers 144 and 221 are ranked 12 and 15 in terms of global integration, i.e., in the top 15 most frequently used routes for direct access ( [Table 2](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t002)).

#### 4.2.2. The First Basement Floor of the CCH/CKB Medical Building

The main consultation units and examination rooms as well as the appointment and cashier counter are located on the first basement floor of the Chung Kang Building. The outpatient area includes internal medicine, medical, surgery, family medicine, rehabilitation, and health care consultation rooms, while the examination rooms include general physiological examination rooms, blood sampling stations, cardiology-related examination rooms, extracorporeal shock wave rooms, urodynamic rooms, and radiology-related examination spaces. The general public can reach this floor by vertical routes with escalator routes 34 and 33, elevators 235–237 and 232–234, or by stairs with route 246. From [Figure 7](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f007), we can find that the main moving routes are numbered 32, 193, 186, and 8, and their Rn rank is 3, 6, 7, and 5, respectively ( [Table 3](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t003)), which can be used to predict that this floor is the main queuing area for people attending the clinic. In the structure formed by the main moving routes, it is found that the route numbers 32, 186, 8 and 2 form a symmetrical ring structure.

#### 4.2.3. The 2nd Floor of CCH/CKB Medical Building

On this floor, the units are infectious disease, neurology, otorhinolaryngology, mental health and dentistry with a semi-open waiting area connecting to private treatment spaces setting the boundary between the different units ( [Figure 8](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f008)). The open type of routes are numbered 100, 113 and 50 ( [Table 4](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t004)) with a single moving route, which can be regarded as the trunk routes, while the semi-open type of routes of the clinic with the route numbers 100–111, 100–107 and 100–113, and routes 50–86 and 50–52, are determined as the branch routes based on their route properties. Under the overall review, the route plan of the 2nd floor is a single type of tree structure, a simple and concise space pattern, which is a more user-friendly spatial route plan for the patients.

From the analysis above, it can be found that the five routes ( [Table 3](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t003)) which are numbered 32, 193, 186, 2, and 8 are the open main routes. From the results of axial mapping analysis in space syntax, the global integration value, Rn, is a moderate value. Moreover, the number of branches connected to each of the five open main routes exceeds six, which verifies Wang’s study \[ [19](https://www.mdpi.com/2220-9964/10/8/570#B19-ijgi-10-00570)\]. In his work it is pointed out that the longest routes have a higher rate of wayfinding behaviors under a moderate Rn value of route configuration characteristics. Due to the complexity of the routes and the large number of decision points on the floor plan, the chance of becoming lost increases significantly when the number of connected routes (CN value) with a medium Rn value is six or more.

#### 4.3. Wayfinding Tasks Experiment Planning and Analysis

In the outpatient area of the medical building, the clinics and examination rooms are divided into different departments on different floors according to the business considerations of different departments. Meanwhile, each department has an independent diagnosis and treatment area. This can be regarded as the outpatient clinic area of each department as a spatial unit, which is then arranged and combined into the plane space of each floor. In order to objectively analyze wayfinding behaviors of the general public in the hospital, the recruitment object of this study was members of the general public who had never been to the experimental site before. The age range was between 19 and 64. The experiment participants were divided into three age groups (19–30, 31–44, 45–64). They were all assigned the same wayfinding tasks on the first floor, second floor and first basement floor of the outpatient area of the hospital. The wayfinding tasks were executed from the entrance of the first-floor gate of the hospital as a starting point. The participants had to complete the wayfinding tasks one by one in the order listed in [Table 5](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t005). During the experiment, the participants could only reach the destination according to the signage guiding system of the medical building. The main task of the research recorder was to confirm whether the participants did indeed complete each wayfinding task and record the time to complete the task ( [Figure 9](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f009)). The research recorder included two members, one of whom used the digital camera to record video images and record the whole wayfinding task of each participant, while the other followed the participants at a distance of about five meters, and observed and recorded whether the participants actually completed the wayfinding tasks for each floor. The recorder also wrote notes to record whether the participants had any wayfinding difficulties or became lost, such as whether there was a place or corner where they moved back and forth or stayed for a long time, and if so, the recorder wrote down the location and duration of stay. Afterwards, these notes were compared and analyzed with the video images. The criterion of this study is that if the experimental participant moved back and forth more than twice or stayed for more than 1 min in the same place or corner, they are judged as having lost their way. Research recorders were required to receive two hours of training and task instructions before actually performing the recording tasks to ensure that they could do their work. Finally, the time spent by the 30 participants (15 males and 15 females) when performing the wayfinding tasks was calculated after all experiments were completed. A comparative analysis of different genders and the time spent on wayfinding tasks with three different age groups (five males and females in each age group) of 19–30, 31–44, and 45–64 was also performed.

Basically, in [Table 6](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t006) it can be seen with regard to the average time spent on wayfinding tasks that women need less time (mean = 1621, SD = 327) than men (mean = 1697, SD = 236). To further examine whether gender has significant differences in the time spent on wayfinding tasks the independent samples t-test was applied. The results also show that the significance value of 0.470 far exceeds the statistical significance value of 0.05 (p < 0.05). Therefore, it can be determined that the influence of gender on the wayfinding tasks is a homogeneity factor. This means that the time spent by the participants in this experiment to perform wayfinding tasks was not significantly different with regard to gender.

In addition, it can be seen from [Table 7](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t007) that with regard to the three different age groups (19–30, 31–44, and 45–64) it was the group aged 19–30 years old that had the shortest wayfinding time (mean = 1531, SD = 258), and thus was most efficient, followed by the group aged 31–44 years old (mean = 1687, SD = 231), and finally that aged 45–64 years old (mean = 1758, SD = 282). The upper and lower values of the 95% confidence interval of mean indicate that the sample follows a normal distribution. Meanwhile, the homogeneity of variances is also calculated using a Levene test, with the results shown in [Table 8](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t008). The significance value of 0.815 is greater than the threshold value of 0.05. This means that these three sets of parameters are homogeneous. In order to verify whether the three different age groups have significant differences in the time spent on the wayfinding tasks, this study then used statistical one-way analysis of variance (ANOVA) to analyze the data. From the results in [Table 9](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t009) it can be seen that the significance value of p is 0.028 under the statistically determined value of 0.05. Further post-hoc analysis was used to determine whether there were significant differences between the groups. The results in [Table 10](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t010) show that the main significant differences in the time spent on wayfinding tasks were between the groups aged 19–30 and 45–64. This means that the time spent by the participants in the experiment to perform the wayfinding task was significantly different due to the difference in age. In short, older people needed much more time to complete the wayfinding tasks, which means that they had poorer performance with regard to wayfinding efficiency. There are three possible reasons why the older participants needed to spend more time on the wayfinding tasks. The first may be the deterioration of physiological functions, especially in mobility, which is not as efficient as in younger people. The second reason may be the inability to see the signage system clearly due to poorer vision. The third is that the older participants may have had problems with reduced cognitive ability and thus, understanding of the graphic images, and so an inability to obtain the necessary and sufficient wayfinding information from the guiding signage system in order to reach the destinations in a short time. The detailed reasons for these results can be studied in future research.

The participants were given a questionnaire after performing the wayfinding tasks, and feedback was given for each task. The options were set as (1) very easy to find—one point; (2) easy to find—two points; (3) ordinary—three points; (4) not easy to find—four points; (5) very difficult to find—five points. The average number of points was calculated based on the responses of the 30 participants, and this was used to assess the degree of difficulty of each wayfinding task. This research analysis mainly selects wayfinding tasks with more than three points as those locations with significant wayfinding problems in the opinions of the 30 participants. The statistical results of wayfinding task difficulty are shown in [Table 5](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t005). Meanwhile, these results are supplemented by the axial analysis of the space syntax theory to cross-compare the factors that affect the wayfinding behaviors. In the questionnaire feedback, it was found that scores greater than three points were all scattered on the first basement floor of the medical building, including physiological examination room, blood collection station, aisle of urodynamic examination, extracorporeal shock wave lithotripsy room, MRI Room, 64-row computed tomography (CT) room, and angiography room ( [Table 4](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t004)). The results show that the route planning of the first basement floor is likely to cause trouble in wayfinding processes for patients visiting the clinic.

The results of the wayfinding experiment show that the first basement floor is the one where most people became lost. The behavioral annotation diagram ( [Figure 10](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f010)) shows that the five routes numbered 32, 193, 186, 2, and 8 are the open main routes ( [Table 2](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t002)), and they are also the most common routes on which people become lost. Compared with the axial analysis of space syntax theory, its global integration value, Rn, is a moderate value and the number of branch routes connected to each of these five open main routes exceeds six. This result validates Wang’s research \[ [19](https://www.mdpi.com/2220-9964/10/8/570#B19-ijgi-10-00570)\], which pointed out that when the longest moving route has a moderate Rn value (>6), it is likely to cause a higher proportion of lost wayfinding behaviors.

In addition, from the five open main routes in [Table 3](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-t003) (routes 32, 193, 186, 8, and 2) and the behavioral annotation diagram and lost points on the first basement floor of the medical building in [Figure 10](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f010), it can be found that the ring structure formed by the routes 32, 186, 8, and 2 can be regarded as a “symmetrical ring” space pattern. We found that many participants moved back and forth on this ring structure aisle or stayed at corners for a long time. This phenomenon of becoming lost that was seen with the participants is consistent with Liu’s research \[ [33](https://www.mdpi.com/2220-9964/10/8/570#B33-ijgi-10-00570)\], which pointed out that a “symmetrical ring” spatial pattern is more likely to become a maze. Therefore, it is recommended that when designing and planning the guiding signage system for medical buildings, special attention should be paid to whether there is any confusion caused by the ring structure. The results of the wayfinding tasks and space syntax analysis presented in this study have consistent conclusions with regard to the locations where it is easy to become lost.

#### 4.4. Isovist Analysis and Signage Planning

The relationship between space syntax and the signage types is mainly based on the degree of the visibility, as obtained by the results of isovist analysis and the size of the surrounding walls of the location. In principle, if the location has a wide visibility range and there are not too many walls, it is recommended to set up hanging signage. In contrast, if there is a large area of the wall, the wall-mount type of signage is recommended. As for spaces with a narrow field of view, the protruding type is recommended for these. If there are not too many walls at such locations, it is recommended that free stand signage is used. The spatial characteristics should be taken into account with regard to the type of wayfinding system so that the appropriate type and content of the signage are used. In the case of the first basement floor, where the current route planning is more likely to cause confusion and disorientation to the public, this can be easily seen from the major route isovist analysis ( [Figure 11](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f011)). The main visual dislocation is in the area surrounded by the walls of the aisle with route 34-32-186, followed by the intersection with route 186-8, then the intersection with route 32-2, and finally the intersection with route 2-8. However, the signage is configured densely at the five routes (routes 32, 193, 186, 8 and 2), and this could easily cause confusion. In line with Macminner \[ [30](https://www.mdpi.com/2220-9964/10/8/570#B30-ijgi-10-00570)\], it is proposed that there should not be too many signs here to avoid visual confusion caused by too many directories, so the signage should be placed at appropriate distances at decision points with easy-to-read, direct and conspicuous icons and contents, and the overall spatial design of the wayfinding system should be consistent.

In [Figure 11](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f011), the escalator leads to the first basement floor, and the first location is the open space formed by the routes 34, 32, 193 and 255, and the spatial characteristics of this location are transitional areas for selecting the main direction of movement via this position. The Depthmap calculates a 360° field of view at the subject location to obtain the visual field of this area. The main visual dislocation is in the area surrounded by the walls of the clinics and the route 34-32-186. The signage here should be a wall-mounted first basement floor plan, so that the patients can quickly determine the direction of their destination.

In [Figure 12](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f012), because of the intersection (point A) of the route number 186-8, and the fact that the spatial characteristics of this area are cross-shaped and located in the secondary visual axis staggering area, the sign type here should be an up hanging guiding sign, and the guiding content should be the identification space and examination room that the route mainly belongs to, and then supplemented by the target space and examination room that the secondary route belongs to, to show the primary and secondary structures of different routes. The main and secondary structures of the different routes are presented to facilitate the identification of the destination routes by the patients. The spatial characteristics will lead the patients to turn right intuitively and proceed to the intersection of route number 32-2 (point B) and follow route number 32 in the direction of number 2, which is a T-shaped space. Therefore, the wall at the intersection should be set up with wall-mounted guiding directories, and the guiding contents should be mainly the identification space and examination room that the route will pass through, so as to help people to reach the destination quickly. The up hanging signage along route 32 should be removed, and the location of the inspection room should be marked by protruding identification signage on the door of the inspection room. Finally, the intersection (point C) with the intersection of the route 2–8 is a T-shaped intersection, but there is also a route number 7 further down along route number 8, so the signage type that should be set up at this intersection should be an up hanging sign, and the guidance content should be the identification space and examination room that the route will pass through, and then the target space and examination room that the secondary route belongs to should be added. The primary and secondary structures of the different routes will be displayed to facilitate the identification of the destination by the patients.

Next, Depthmap software is used for the isovist analysis, and we can see that the escalator’s route 34 reaches the first floor of the basement, and the first thing is the open area formed by routes 33, 34, 193 and 255 ( [Figure 12](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f012)). When the spatial characteristics of this area are not clear enough, it is easy to be confused and not know how to move. In addition, for the ring-shaped area formed by the routes 32, 2, 186 and 8 the two opposite sides are of equal length, that is, there is a “symmetrical ring” spatial structure ( [Figure 12](https://www.mdpi.com/2220-9964/10/8/570#ijgi-10-00570-f012), red rectangular area), making the spatial system of this area too homogeneous, and thus, it is difficult for people to identify the various routes and so they can easily become lost. It is recommended that a good outpatient area plan should be a symmetrical tree plan with clear indicators in areas that are easy to become lost in, as this will provide clear and precise information to the public.

## 5\. Conclusions

This study investigated the relationships between the spatial configuration of the outpatient areas of health care facilities and the wayfinding behavior of patients. It also examined whether the results of the participants’ wayfinding tasks were consistent with the analysis results predicted by the space syntax analysis. In addition, this study applied axial mapping analysis and isovist analysis to find out the locations of visual axis staggering and suggest the location and type of content of the signage to optimize the functional efficiency of the guiding signage system.

When people are in an unfamiliar environment, they first receive environmental information through their vision. They then form their own knowledge of the environment through internalization of this and complete the process of interpreting the environment they are in. In health care facilities, when patients have problems with finding their way around, they are guided by the guiding signage system provided by the health care facilities to help them solve such problems. Good spatial planning can reduce the wayfinding problems in a clinic. The final results of this study showed that in the wayfinding task experiment gender had no significant impacts on wayfinding efficiency, while there was a significant impact due to age. The older people needed much more time to complete the wayfinding tasks, which means that they had a poorer performance with regard to wayfinding efficiency. In terms of space syntax analysis, the second-floor outpatient areas of the research field have a tree structure with the most user-friendly route plan for the patients, followed by the first-floor outpatient areas, and the least user-friendly were the route plans of the first basement floor outpatient areas, where patients were easily disoriented due to the interlocking route plans forming a symmetrical ring structure. Therefore, in a symmetrical circular aisle, special attention should be given to the visual concentration areas to guide the patients to their destinations by placing appropriate signage forms and contents that match the characteristics of the space. Meanwhile, the text of the sign should not be too small and should not convey too much information. In addition, different colors should be used on the walls to distinguish the operation properties of the space, and an appropriate wayfinding system planning approach should be applied to provide clear and precise guidance information to the patients. A well-planned wayfinding system can facilitate the public’s awareness of the structure of the map, and thus reduce problems when going to a destination. However, the results of this study show that the planning of the wayfinding system should be based on the minimal signage configuration required to meet the needs of the patients. Too many signs make it difficult for the patients to immediately determine the nearest route to the destination. In areas where it is easy to become lost the text of the signs should not be too small or convey too much information, as this makes it difficult for people to understand them and causes confusion. As a public space, the overall structure and movement of medical buildings must comply with the relevant safety regulations. Therefore, since the structure of the indoor space cannot be changed at will, the spatial characteristics of the space and movement should be strengthened in areas where people easily become lost, so that the patients can reach their destinations quickly.

In order to objectively analyze the impact of the original architectural structure design and planning of the medical building, and the guiding signage system set up later, on the wayfinding behaviors of the general users of the hospital, the experimental object of this study was members of the general public who had never been to the experimental site (CCH/CKB Hospital) before. With regard to the individuals who will come to a hospital, some patients, such as those with dementia, will face greater problems with regard to wayfinding behaviors, and further analysis and research must be carried out for this group. Therefore, this study’s limitations are that it focuses on the general public, and that the experimental field is also limited to the outpatient area (B1 to F2) in the hospital. Future research will thus focus on the wayfinding behaviors of special groups or patients (e.g., dementia patients, etc.) and extend to the ward areas on the other floors.

However, we have achieved the purpose of this paper with our final results, and it is hoped that these will help solve the wayfinding problem in the focal hospital and improve the quality of the hospital environment. The results of this study can also be used as a reference for other health care facilities in the future when planning and constructing related guiding signage systems.

## Author Contributions

Conceptualization, Ming-Shih Chen, Yao-Tsung Ko and Wen-Che Hsieh; data curation, Yao-Tsung Ko and Wen-Che Hsieh; resources, Ming-Shih Chen and Yao-Tsung Ko; funding ac-quisition, Ming-Shih Chen; investigation, Yao-Tsung Ko and Wen-Che Hsieh; methodology, Yao-Tsung Ko and Wen-Che Hsieh; software: Yao-Tsung Ko and Wen-Che Hsieh; visualization, Yao-Tsung Ko and Wen-Che Hsieh; project administration, Ming-Shih Chen; writing—original draft, Ming-Shih Chen, Yao-Tsung Ko and Wen-Che Hsieh; writing—review and editing, Ming-Shih Chen and Yao-Tsung Ko. All authors have read and agreed to the published version of the manuscript.

## Funding

This research was funded by the Ministry of Science and Technology of Taiwan under grant MOST 105-2410-H-029-035.

## Institutional Review Board Statement

Not applicable.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

The data presented in this study are available on request from the corresponding author.

## Conflicts of Interest

The authors declare no conflict of interest.

## References

01. Passini, R. Wayfinding: A conceptual framework. Urban Ecol. **1981**, 5, 17–31. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Wayfinding:+A+conceptual+framework&author=Passini,+R.&publication_year=1981&journal=Urban+Ecol.&volume=5&pages=17%E2%80%9331&doi=10.1016/0304-4009(81)90018-8)\] \[ [CrossRef](http://doi.org/10.1016/0304-4009(81)90018-8)\]
02. Zijlstra, E.; Hagedoorn, M.; Krijnen, W.P.; van der Schans, C.P.; Mobach, M.P. Route complexity and simulated physical ageing negatively influence wayfinding. Appl. Ergon. **2016**, 56, 62–67. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Route+complexity+and+simulated+physical+ageing+negatively+influence+wayfinding&author=Zijlstra,+E.&author=Hagedoorn,+M.&author=Krijnen,+W.P.&author=van+der+Schans,+C.P.&author=Mobach,+M.P.&publication_year=2016&journal=Appl.+Ergon.&volume=56&pages=62%E2%80%9367&doi=10.1016/j.apergo.2016.03.009)\] \[ [CrossRef](http://doi.org/10.1016/j.apergo.2016.03.009)\]
03. Water, T.; Wrapson, J.; Reay, S.; Ford, K. Making space work: Staff socio-spatial practices in a paediatric outpatient department. Health Place. **2018**, 50, 146–153. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Making+space+work:+Staff+socio-spatial+practices+in+a+paediatric+outpatient+department&author=Water,+T.&author=Wrapson,+J.&author=Reay,+S.&author=Ford,+K.&publication_year=2018&journal=Health+Place.&volume=50&pages=146%E2%80%93153&doi=10.1016/j.healthplace.2018.01.007&pmid=29454242)\] \[ [CrossRef](http://doi.org/10.1016/j.healthplace.2018.01.007)\] \[ [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/29454242)\]
04. Blumberg, R.; Devlin, A. Design issues in hospital: The adolescent client. Environ. Behav. **2006**, 38, 293–317. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Design+issues+in+hospital:+The+adolescent+client&author=Blumberg,+R.&author=Devlin,+A.&publication_year=2006&journal=Environ.+Behav.&volume=38&pages=293%E2%80%93317&doi=10.1177/0013916505281575)\] \[ [CrossRef](http://doi.org/10.1177/0013916505281575)\]
05. Chen, K.L. Wayfinding and Marking in Library; Mandarin Library & Information Service Company: Taipei, Taiwan, 2007. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Wayfinding+and+Marking+in+Library&author=Chen,+K.L.&publication_year=2007)\]
06. Baskaya, A.; Wilson, C.; Özcan, Y.Z. Wayfinding in an unfamiliar environment: Different spatial settings of two polyclinics. Environ. Behav. **2004**, 36, 839–867. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Wayfinding+in+an+unfamiliar+environment:+Different+spatial+settings+of+two+polyclinics&author=Baskaya,+A.&author=Wilson,+C.&author=%C3%96zcan,+Y.Z.&publication_year=2004&journal=Environ.+Behav.&volume=36&pages=839%E2%80%93867&doi=10.1177/0013916504265445)\] \[ [CrossRef](http://doi.org/10.1177/0013916504265445)\] \[ [Green Version](http://repository.bilkent.edu.tr/bitstream/11693/48538/1/Wayfinding_in_an_Unfamiliar_Environment.pdf)\]
07. Huang, J.S.; Tzeng, S.Y. A Study of Wayfinding behaviors in Out-Patient Area-Two Single Floor Type for Example. J. Des. **2008**, 13, 43–63. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=A+Study+of+Wayfinding+behaviors+in+Out-Patient+Area-Two+Single+Floor+Type+for+Example&author=Huang,+J.S.&author=Tzeng,+S.Y.&publication_year=2008&journal=J.+Des.&volume=13&pages=43%E2%80%9363)\]
08. Andersson, J.E. Architecture for the silver generation: Exploring the meaning of appropriate space for ageing in a Swedish municipality. Health Place **2011**, 17, 572–587. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Architecture+for+the+silver+generation:+Exploring+the+meaning+of+appropriate+space+for+ageing+in+a+Swedish+municipality&author=Andersson,+J.E.&publication_year=2011&journal=Health+Place&volume=17&pages=572%E2%80%93587&doi=10.1016/j.healthplace.2010.12.015)\] \[ [CrossRef](http://doi.org/10.1016/j.healthplace.2010.12.015)\]
09. Wu, Z.-H.; Han, Y.; Chen, Y.; Liu, K.J.R. A Time-Reversal Paradigm for Indoor Positioning System. IEEE Trans. Veh. Technol. **2015**, 64, 1331–1339. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=A+Time-Reversal+Paradigm+for+Indoor+Positioning+System&author=Wu,+Z.-H.&author=Han,+Y.&author=Chen,+Y.&author=Liu,+K.J.R.&publication_year=2015&journal=IEEE+Trans.+Veh.+Technol.&volume=64&pages=1331%E2%80%931339&doi=10.1109/TVT.2015.2397437)\] \[ [CrossRef](http://doi.org/10.1109/TVT.2015.2397437)\]
10. Carroll, J.B. Human Cognitive Abilities: A Survey of Factor-Analytic Studies; Cambridge University Press: Cambridge, UK, 1993. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Human+Cognitive+Abilities:+A+Survey+of+Factor-Analytic+Studies&author=Carroll,+J.B.&publication_year=1993)\]
11. O’Neill, M.J. Effects of Signage and Floor Plan Configuration on Wayfinding Accuracy. Environ. Behav. **1991**, 23, 553–574. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Effects+of+Signage+and+Floor+Plan+Configuration+on+Wayfinding+Accuracy&author=O%E2%80%99Neill,+M.J.&publication_year=1991&journal=Environ.+Behav.&volume=23&pages=553%E2%80%93574&doi=10.1177/0013916591235002)\] \[ [CrossRef](http://doi.org/10.1177/0013916591235002)\]
12. Best, G. Direction-Finding in Large Buildings. In Architectural Psychology: Proceedings of the Conference, Dalandhui University of Strathclyde, Strathclyde, UK, 28 February–2 March 1969; Canter, D.V., Ed.; RIBA Publications Ltd.: London, UK, 1970; pp. 72–75. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Direction-Finding+in+Large+Buildings&author=Best,+G.&publication_year=1970&pages=72%E2%80%9375)\]
13. Chiu, T.W. The Research of Human Cognition Difference between Plane and Three-Dimensional Guide Map Design in Public Exhibition Space. Master’s Thesis, Tunghai University, Taichung City, Taiwan, 2011. Unpublished work. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=The+Research+of+Human+Cognition+Difference+between+Plane+and+Three-Dimensional+Guide+Map+Design+in+Public+Exhibition+Space&author=Chiu,+T.W.&publication_year=2011)\]
14. Arthur, P.; Passini, R. Wayfinding: People, Signs, and Architecture; McGraw-Hill: New York, NY, USA, 1992. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Wayfinding:+People,+Signs,+and+Architecture&author=Arthur,+P.&author=Passini,+R.&publication_year=1992)\]
15. Morag, I.; Pintelon, L.; Heylighen, A. Evaluating the Inclusivity of hospital wayfinding systems for users with diverse needs and abilities. J. Health Serv. Res. Policy **2016**, 21, 243–248. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Evaluating+the+Inclusivity+of+hospital+wayfinding+systems+for+users+with+diverse+needs+and+abilities&author=Morag,+I.&author=Pintelon,+L.&author=Heylighen,+A.&publication_year=2016&journal=J.+Health+Serv.+Res.+Policy&volume=21&pages=243%E2%80%93248&doi=10.1177/1355819616642257)\] \[ [CrossRef](http://doi.org/10.1177/1355819616642257)\] \[ [Green Version](https://www.mdpi.com/2220-9964/10/8/570)\]
16. Lee, E.; Daugherty, J.; Selga, J.T.; Schmidt, U. Improving Surgical Start Times by Improving Wayfinding. J. PeriAnesthesia Nurs. **2020**, 35, 17–21. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Improving+Surgical+Start+Times+by+Improving+Wayfinding&author=Lee,+E.&author=Daugherty,+J.&author=Selga,+J.T.&author=Schmidt,+U.&publication_year=2020&journal=J.+PeriAnesthesia+Nurs.&volume=35&pages=17%E2%80%9321&doi=10.1016/j.jopan.2019.06.001&pmid=31561964)\] \[ [CrossRef](http://doi.org/10.1016/j.jopan.2019.06.001)\] \[ [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/31561964)\]
17. Peponis, J.; Zimring, C.; Choi, Y.K. Finding the Building in Wayfinding. Environ. Behav. **1990**, 22, 555–590. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Finding+the+Building+in+Wayfinding&author=Peponis,+J.&author=Zimring,+C.&author=Choi,+Y.K.&publication_year=1990&journal=Environ.+Behav.&volume=22&pages=555%E2%80%93590&doi=10.1177/0013916590225001)\] \[ [CrossRef](http://doi.org/10.1177/0013916590225001)\]
18. Morgareidge, D.; Cai, H.; Jia, J. Performance-driven design with the support of digital tools: Applying discrete event simulation and space syntax on the design of the emergency department. Front. Archit. Res. **2014**, 3, 250–264. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Performance-driven+design+with+the+support+of+digital+tools:+Applying+discrete+event+simulation+and+space+syntax+on+the+design+of+the+emergency+department&author=Morgareidge,+D.&author=Cai,+H.&author=Jia,+J.&publication_year=2014&journal=Front.+Archit.+Res.&volume=3&pages=250%E2%80%93264&doi=10.1016/j.foar.2014.04.006)\] \[ [CrossRef](http://doi.org/10.1016/j.foar.2014.04.006)\] \[ [Green Version](https://www.mdpi.com/2220-9964/10/8/570)\]
19. Wang, W.C. The Spatial Logic of Museums—Case Studies on The National Museum of Natural Science and The National Science and Technology Museum. Master’s Thesis, Feng Chia University, Taichung City, Taiwan, 2004. Unpublished work. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=The+Spatial+Logic+of+Museums%E2%80%94Case+Studies+on+The+National+Museum+of+Natural+Science+and+The+National+Science+and+Technology+Museum&author=Wang,+W.C.&publication_year=2004)\]
20. Choudhary, R.; Bafna, S.; Heo, Y.; Hendrich, A.; Chow, M. A predictive model for computing the influence of space layouts on nurses’ movement in hospital units. J. Build. Perform. Simul. **2010**, 3, 171–184. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=A+predictive+model+for+computing+the+influence+of+space+layouts+on+nurses%E2%80%99+movement+in+hospital+units&author=Choudhary,+R.&author=Bafna,+S.&author=Heo,+Y.&author=Hendrich,+A.&author=Chow,+M.&publication_year=2010&journal=J.+Build.+Perform.+Simul.&volume=3&pages=171%E2%80%93184&doi=10.1080/19401490903174280)\] \[ [CrossRef](http://doi.org/10.1080/19401490903174280)\]
21. Haq, S.; Luo, Y. Space Syntax in Healthcare Facilities Research: A Review. HERD Health Environ. Res. Des. J. **2012**, 5, 98–117. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Space+Syntax+in+Healthcare+Facilities+Research:+A+Review&author=Haq,+S.&author=Luo,+Y.&publication_year=2012&journal=HERD+Health+Environ.+Res.+Des.+J.&volume=5&pages=98%E2%80%93117&doi=10.1177/193758671200500409)\] \[ [CrossRef](http://doi.org/10.1177/193758671200500409)\]
22. Lynch, K. The Image of the City; MIT Press: Cambridge, MA, USA, 1960. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=The+Image+of+the+City&author=Lynch,+K.&publication_year=1960)\]
23. Downs, R.M.; Stea, D.; Boulding, K.E. Image and Environment: Cognitive Mapping and Spatial Behavior; Aldine Publishing Company: Chicago, IL, USA, 1973. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Image+and+Environment:+Cognitive+Mapping+and+Spatial+Behavior&author=Downs,+R.M.&author=Stea,+D.&author=Boulding,+K.E.&publication_year=1973)\]
24. Evans, G.; Fellows, J.; Zorn, M.; Doty, K. Cognitive mapping and architecture. J. Appl. Psychol. **1980**, 65, 474–478. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Cognitive+mapping+and+architecture&author=Evans,+G.&author=Fellows,+J.&author=Zorn,+M.&author=Doty,+K.&publication_year=1980&journal=J.+Appl.+Psychol.&volume=65&pages=474%E2%80%93478&doi=10.1037/0021-9010.65.4.474)\] \[ [CrossRef](http://doi.org/10.1037/0021-9010.65.4.474)\]
25. Blades, M. Wayfinding theory and research: The need for a new approach. In Cognitive and Linguistic Aspects of Geographic Space; Mark, D.M., Frank, A.U., Eds.; Kluwer: Dordrecht, The Netherlands, 1991; pp. 137–165. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Wayfinding+theory+and+research:+The+need+for+a+new+approach&author=Blades,+M.&publication_year=1991&pages=137%E2%80%93165)\]
26. Chen, C.-H.; Chang, W.-C. Gender differences in relation to wayfinding strategies, navigational support design, and wayfinding task difficulty. J. Environ. Psychol. **2009**, 29, 220–226. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Gender+differences+in+relation+to+wayfinding+strategies,+navigational+support+design,+and+wayfinding+task+difficulty&author=Chen,+C.-H.&author=Chang,+W.-C.&publication_year=2009&journal=J.+Environ.+Psychol.&volume=29&pages=220%E2%80%93226&doi=10.1016/j.jenvp.2008.07.003)\] \[ [CrossRef](http://doi.org/10.1016/j.jenvp.2008.07.003)\]
27. Iachini, T.; Ruotolo, F.; Ruggiero, G. The effects of familiarity and gender on spatial representation. J. Environ. Psychol. **2009**, 29, 227–234. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=The+effects+of+familiarity+and+gender+on+spatial+representation&author=Iachini,+T.&author=Ruotolo,+F.&author=Ruggiero,+G.&publication_year=2009&journal=J.+Environ.+Psychol.&volume=29&pages=227%E2%80%93234&doi=10.1016/j.jenvp.2008.07.001)\] \[ [CrossRef](http://doi.org/10.1016/j.jenvp.2008.07.001)\]
28. Van der Ham, I.J.M.; Claessen, M.H.G. How age relates to spatial navigation performance: Functional and methodological considerations. Ageing Res. Rev. **2020**, 58, 101020\. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=How+age+relates+to+spatial+navigation+performance:+Functional+and+methodological+considerations&author=Van+der+Ham,+I.J.M.&author=Claessen,+M.H.G.&publication_year=2020&journal=Ageing+Res.+Rev.&volume=58&pages=101020&doi=10.1016/j.arr.2020.101020)\] \[ [CrossRef](http://doi.org/10.1016/j.arr.2020.101020)\]
29. Bosch, S.J.; Gharaveis, A. Flying solo: A review of the literature on wayfinding for older adults experiencing visual or cognitive decline. Appl. Ergon. **2017**, 58, 327–333. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Flying+solo:+A+review+of+the+literature+on+wayfinding+for+older+adults+experiencing+visual+or+cognitive+decline&author=Bosch,+S.J.&author=Gharaveis,+A.&publication_year=2017&journal=Appl.+Ergon.&volume=58&pages=327%E2%80%93333&doi=10.1016/j.apergo.2016.07.010&pmid=27633229)\] \[ [CrossRef](http://doi.org/10.1016/j.apergo.2016.07.010)\] \[ [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/27633229)\]
30. MacMinner, S. Human Perception and Orientation in the Built Environment; Academic Press: New York, NY, USA, 1997. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Human+Perception+and+Orientation+in+the+Built+Environment&author=MacMinner,+S.&publication_year=1997)\]
31. Rousek, J.; Hallbeck, M. The use of simulated visual impairment to identify hospital design elements that contribute to wayfinding difficulties. Int. J. Ind. Ergon. **2011**, 41, 447–458. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=The+use+of+simulated+visual+impairment+to+identify+hospital+design+elements+that+contribute+to+wayfinding+difficulties&author=Rousek,+J.&author=Hallbeck,+M.&publication_year=2011&journal=Int.+J.+Ind.+Ergon.&volume=41&pages=447%E2%80%93458&doi=10.1016/j.ergon.2011.05.002)\] \[ [CrossRef](http://doi.org/10.1016/j.ergon.2011.05.002)\]
32. Koneczny, S.; Rousek, J.B.; Hallbeck, M.S. Simulating visual impairment to detect hospital way-finding difficulties. Stud. Health Technol. Inform. **2009**, 142, 133–135. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Simulating+visual+impairment+to+detect+hospital+way-finding+difficulties&author=Koneczny,+S.&author=Rousek,+J.B.&author=Hallbeck,+M.S.&publication_year=2009&journal=Stud.+Health+Technol.+Inform.&volume=142&pages=133%E2%80%93135&pmid=19377131)\] \[ [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/19377131)\]
33. Liu, P.C. Form Generation from Spatial Configuration—A Design Methodology Based on Space Syntax Analysis and Parametric Design. Ph.D. Thesis, Tunghai University, Taichung City, Taiwan, 2015. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=Form+Generation+from+Spatial+Configuration%E2%80%94A+Design+Methodology+Based+on+Space+Syntax+Analysis+and+Parametric+Design&author=Liu,+P.C.&publication_year=2015)\]
34. Shu, C.F. The Inner Logic of Space Syntax. J. Archit. Dimens. Des. Theory **1999**, 1, 43–53. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=The+Inner+Logic+of+Space+Syntax&author=Shu,+C.F.&publication_year=1999&journal=J.+Archit.+Dimens.+Des.+Theory&volume=1&pages=43%E2%80%9353)\]
35. Hillier, B.; Hanson, J. The Social Logic of Space; Cambridge University Press: Cambridge, UK; New York, NY, USA, 1984. \[ [Google Scholar](http://scholar.google.com/scholar_lookup?title=The+Social+Logic+of+Space&author=Hillier,+B.&author=Hanson,+J.&publication_year=1984)\]

**Figure 1.**
Dynamic space syntax graph \[ [34](https://www.mdpi.com/2220-9964/10/8/570#B34-ijgi-10-00570)\].

**Figure 1.**
Dynamic space syntax graph \[ [34](https://www.mdpi.com/2220-9964/10/8/570#B34-ijgi-10-00570)\].

**Figure 2.**
Analysis of the axial map \[ [34](https://www.mdpi.com/2220-9964/10/8/570#B34-ijgi-10-00570)\].

**Figure 2.**
Analysis of the axial map \[ [34](https://www.mdpi.com/2220-9964/10/8/570#B34-ijgi-10-00570)\].

**Figure 3.**
Classification of the content of the signage in the research field.

**Figure 3.**
Classification of the content of the signage in the research field.

**Figure 4.**
Classification of the forms of the signage in the research field.

**Figure 4.**
Classification of the forms of the signage in the research field.

**Figure 5.**
The signage configuration and distribution of the outpatient areas B1 to 2F in CCH/CKB.

**Figure 5.**
The signage configuration and distribution of the outpatient areas B1 to 2F in CCH/CKB.

**Figure 6.**
The axial mapping analysis of the first floor of the CCH/CKB Building.

**Figure 6.**
The axial mapping analysis of the first floor of the CCH/CKB Building.

**Figure 7.**
The axial mapping analysis of the first basement floor of the CCH/CKB Building.

**Figure 7.**
The axial mapping analysis of the first basement floor of the CCH/CKB Building.

**Figure 8.**
The axial mapping analysis of the second floor of the CCH/CKB Building.

**Figure 8.**
The axial mapping analysis of the second floor of the CCH/CKB Building.

**Figure 9.**
The research recorder observed and recorded the participants performing the wayfinding tasks.

**Figure 9.**
The research recorder observed and recorded the participants performing the wayfinding tasks.

**Figure 10.**
The behavioral annotation diagram and points where participants became lost on the first basement floor of the CCH/CKB Building.

**Figure 10.**
The behavioral annotation diagram and points where participants became lost on the first basement floor of the CCH/CKB Building.

**Figure 11.**
The overlapping map of the signage, axis and route isovist on the first basement floor of the CCH/CKB Building.

**Figure 11.**
The overlapping map of the signage, axis and route isovist on the first basement floor of the CCH/CKB Building.

**Figure 12.**
The visual area of the subject location in the intersection area of route numbers 186, 32, 2, and 8.

**Figure 12.**
The visual area of the subject location in the intersection area of route numbers 186, 32, 2, and 8.

**Table 1.**
Statistics on the number and type distribution of the signage on each floor.

**Table 1.**
Statistics on the number and type distribution of the signage on each floor.

|  | Wall-Mounted | Up Hanging | Protruding |  |
| :-: | :-: | :-: | :-: | :-: |
|  | (A) Identification | (B) Guidance | (C) Direction | (D) Description | (A) Identification | (B) Guidance | (A) Identification | Total |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|  |  |  |  |  |  |  |  |  |
| B1 | 13 | 5 | 4 | 4 | 3 | 16 | 8 | 53 |
| 1F | 2 | 4 | 1 | 1 | 1 | 4 | 2 | 15 |
| 2F | 6 | 0 | 2 | 2 | 0 | 3 | 1 | 14 |
| Sum | 21 | 9 | 7 | 7 | 4 | 23 | 11 | 82 |
| Percentage | 25.61% | 10.97% | 8.54% | 8.54% | 4.88% | 28.05% | 13.41% |  |

**Table 2.**
The quantification of the dynamic syntax of the major and vertical routes on the first floor of the CCH/CKB Building.

**Table 2.**
The quantification of the dynamic syntax of the major and vertical routes on the first floor of the CCH/CKB Building.

| Rank | Line | Route Properties | Rn | CN |
| :-: | :-: | :-: | :-: | :-: |
| 1 | 59 | Passage to 2F Escalator | 1.1866 | 5 |
| 2 | 255 | Staircase a | 1.1432 | 7 |
| 3 | 144 | Escalator 1F to B1 | 1.1209 | 4 |
| 4 | 155 | Lobby routes | 1.1190 | 4 |
| 5 | 221 | Escalator B1 to 1F | 1.1003 | 3 |
| 6 | 62 | Main entrance/exit routes | 1.0645 | 3 |
| 7 | 61 | Lobby route-elevator area | 1.0588 | 8 |
| 8 | 60 | Escalator 1F to 2F | 1.0030 | 2 |
| 8 | 58 | Escalator 2F to 1F | 1.0030 | 2 |
| 10 | 232 | Elevatorhall B-Vertical route\_Elevator d | 0.9659 | 8 |
| 11 | 87 | Elevator hall A—Elevator c | 0.9428 | 2 |
| 12 | 88 | Elevator hall A—Elevator b | 0.9213 | 3 |
| 13 | 145 | Elevator hall A—Elevator a | 0.9207 | 3 |
| 14 | 237 | Vertical Route\_Elevator c | 0.9195 | 4 |
| 15 | 235 | Vertical Route\_Elevator a | 0.8967 | 3 |
| 15 | 236 | Vertical Route\_Elevator b | 0.8967 | 3 |
| 17 | 233 | Elevatorhall B-Vertical route\_Elevator e | 0.8507 | 6 |
| 18 | 234 | Elevator hall B-Vertical route\_Elevator f | 0.8507 | 6 |
| 19 | 55 | Elevator hall B-Staircase b | 0.8242 | 5 |
| 20 | 56 | Aisle-Elevator hall B | 0.8237 | 4 |
| 21 | 246 | Staircase b | 0.7444 | 3 |

(Rn: global integration; CN: connectivity numbers between spaces and axes).

**Table 3.**
The quantification of the dynamic syntax of major routes on the first basement floor of the CCH/CKB Building.

**Table 3.**
The quantification of the dynamic syntax of major routes on the first basement floor of the CCH/CKB Building.

| Rank | Line | Route Properties | Rn | CN |
| :-: | :-: | :-: | :-: | :-: |
| 1 | 34 | Escalator 1F to B1 | 1.2181 | 4 |
| 2 | 33 | Escalator B1 to 1F | 1.2021 | 4 |
| 3 | 32 | Outpatient areas—Physiological examination room (Diagnostics 30) | 1.1557 | 15 |
| 4 | 255 | Staircase a | 1.1432 | 5 |
| 5 | 8 | Radiology counter—Aisle of urodynamic examination room | 1.1038 | 13 |
| 6 | 193 | First basement floor corridor-elevator area | 1.0745 | 8 |
| 7 | 186 | Machine for making an appointment, cashier and taking a number—64-row computed tomography (CT) room | 1.0427 | 17 |
| 8 | 2 | Front passage of extracorporeal shock wave lithotripsy room | 0.9693 | 10 |
| 9 | 232 | Elevator hall B-Vertical route\_Elevator d | 0.9659 | 8 |
| 10 | 191 | Passage—Elevator hall A | 0.9612 | 5 |
| 11 | 187 | Aisle—Elevator hall B | 0.9460 | 7 |
| 11 | 192 | 64-row computed tomography (CT) room—Elevator hall B | 0.9460 | 6 |
| 13 | 237 | Vertical route\_Elevator c | 0.9195 | 4 |
| 14 | 236 | Vertical route\_Elevator b | 0.8973 | 3 |
| 15 | 235 | Vertical route\_Elevator a | 0.8967 | 3 |
| 16 | 188 | Elevator hall A- Elevator c | 0.8679 | 2 |
| 17 | 189 | Elevator hall A- Elevator b | 0.8507 | 2 |
| 17 | 233 | Elevator hall B-Vertical route\_Elevator e | 0.8507 | 6 |
| 17 | 234 | Elevator hall B-Vertical route\_Elevator f | 0.8507 | 6 |
| 20 | 190 | Elevator hall A—Elevator a | 0.8502 | 2 |
| 21 | 57 | Elevator hall B—Staircase b | 0.8372 | 6 |
| 22 | 246 | Staircase b | 0.7444 | 3 |

(Rn: global integration; CN: connectivity numbers between spaces and axes).

**Table 4.**
The quantification of the dynamic syntax of major routes on the second floor of the CCH/CKB Building.

**Table 4.**
The quantification of the dynamic syntax of major routes on the second floor of the CCH/CKB Building.

| Rank | Line | Route Properties | Rn | CN |
| :-: | :-: | :-: | :-: | :-: |
| 1 | 232 | Elevator hall B-Vertical route\_Elevator d | 0.9659 | 8 |
| 2 | 237 | Vertical route\_Elevator c | 0.9195 | 4 |
| 3 | 238 | Vertical route\_Escalator 2F to 1F | 0.9008 | 2 |
| 3 | 239 | Vertical route\_Escalator 1F to 2F | 0.9008 | 2 |
| 5 | 236 | Vertical route\_Elevator b | 0.8973 | 3 |
| 6 | 235 | Vertical route\_Elevator a | 0.8967 | 3 |
| 7 | 53 | Aisle—Elevator hall B | 0.8717 | 6 |
| 8 | 105 | Escalator 1F to 2F | 0.8597 | 3 |
| 8 | 106 | Escalator 2F to 1F | 0.8597 | 3 |
| 10 | 233 | Elevator hall B-Vertical route\_Elevator e | 0.8507 | 6 |
| 10 | 234 | Elevator hall B-Vertical route\_Elevator f | 0.8507 | 6 |
| 12 | 104 | Passage—Elevator hall A | 0.8486 | 8 |
| 13 | 54 | Elevator hall B—Staircase b | 0.8460 | 5 |
| 14 | 102 | Elevator hall A—Elevator b | 0.8164 | 3 |
| 15 | 103 | Elevator hall A—Elevator a | 0.8159 | 2 |
| 16 | 101 | Elevator hall A—Elevator c | 0.8111 | 2 |
| 17 | 100 | Aisle—Neurology | 0.7596 | 8 |
| 18 | 246 | Staircase b | 0.7444 | 3 |
| 19 | 113 | Front aisle of the appointment and cashier counter | 0.6770 | 5 |
| 20 | 107 | Route 113—Otorhinolaryngology clinic | 0.6764 | 5 |
| 21 | 111 | Route 100—Infectious diseases clinic | 0.6711 | 4 |
| 22 | 50 | Common corridor of mental health and dentistry | 0.6058 | 5 |

(Rn: global integration; CN: connectivity numbers between spaces and axes).

**Table 5.**
Wayfinding task contents of the clinic and examination rooms in the different floors of the medical building.

**Table 5.**
Wayfinding task contents of the clinic and examination rooms in the different floors of the medical building.

| Floor | CCH/CKB Building | Degree of Difficulty of the Wayfinding Tasks |
| :-: | :-: | :-: |
| Mean | SD |
| :-: | :-: |
| 1F | Information Station | 2.63 | 0.23 |
| Pharmacy | 1.57 | 0.15 |
| 2F | Registration & Cashier | 1.85 | 0.12 |
| Ultrasonic Room | 2.63 | 0.33 |
| Otorhinolaryngology (Clinic 52) | 2.13 | 0.26 |
| Dentistry | 2.15 | 0.41 |
| Mental Health Clinic | 2.37 | 0.28 |
| B1 | Machine for making an appointment, <br>cashier and taking a number | 2.13 | 0.16 |
| Clinic Room 9 | 2.37 | 0.08 |
| Clinic Room 52 | 2.05 | 0.32 |
| Clinic Room 26 | 2.13 | 0.42 |
| Radiology Counter | 2.37 | 0.06 |
| Physiological Examination Room <br>(Clinic 30) | 3.92 | 0.26 |
| Blood Collection Station | 3.83 | 0.35 |
| Aisle of Urodynamic Examination | 3.87 | 0.22 |
| Extracorporeal Shock Wave Lithotripsy Room | 3.60 | 0.36 |
| MRI Room | 3.43 | 0.15 |
| 64-row Computed Tomography (CT) Room | 3.83 | 0.26 |
| Angiography Room | 3.67 | 0.12 |

**Table 6.**
Statistics and t-test results of the time spent on the wayfinding tasks by different genders.

**Table 6.**
Statistics and t-test results of the time spent on the wayfinding tasks by different genders.

|  |  |  |  |  | Independent Samples t-Test |
| :-: | :-: | :-: | :-: | :-: | :-: |
|  | Gender | Sample | Mean | SD | t | Sig. (p) |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Time spent on wayfinding tasks | Male | 15 | 1697 | 236 | 0.733 | 0.470 |
| Female | 15 | 1621 | 327 |

Compared significance under the 0.05 level is indicated by \*. \* (Unit: Second).

**Table 7.**
Descriptive statistics of the time spent on wayfinding tasks for three different age groups.

**Table 7.**
Descriptive statistics of the time spent on wayfinding tasks for three different age groups.

| Age Range | Sample | Mean | SD | 95% Confidence Interval | Minimum | Maximum |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Lower Bound | Upper Bound |
| :-: | :-: |
| 19–30 | 10 | 1531 | 258 | 1251 | 1886 | 1099 | 2039 |
| 31–44 | 10 | 1687 | 231 | 1374 | 1978 | 1159 | 2165 |
| 45–64 | 10 | 1758 | 282 | 1582 | 2062 | 1470 | 2213 |
| Sum | 30 | 1659 | 257 | 1402 | 1975 | 1243 | 2139 |

(Unit: Second).

**Table 8.**
Homogeneity test of variance of the time spent on wayfinding tasks for three different age groups.

**Table 8.**
Homogeneity test of variance of the time spent on wayfinding tasks for three different age groups.

| Levene Statistics | Freedom Degree of Numerator | Freedom Degree of Denominator | Sig. (p) |
| :-: | :-: | :-: | :-: |
| 0.206 | 2 | 27 | 0.815 |

**Table 9.**
One-way ANOVA of the time spent on wayfinding tasks for three different age groups.

**Table 9.**
One-way ANOVA of the time spent on wayfinding tasks for three different age groups.

| Items | Sum of Square | Freedom Degree | Mean Sum of Squares | F | Sig. (p) |
| :-: | :-: | :-: | :-: | :-: | :-: |
| Between Groups | 269,885.400 | 2 | 134,942.700 | 1.771 | 0.028 \* |
| Within Groups | 2,057,681.400 | 27 | 76,210.422 |  |  |
| Sum | 2,327,566.800 | 29 |  |  |  |

Compared significance under the 0.05 level is indicated by \*.

**Table 10.**
Post-hoc analysis of the time spent on wayfinding tasks for three different age groups.

**Table 10.**
Post-hoc analysis of the time spent on wayfinding tasks for three different age groups.

| (I) Age Range | (J) Age Range | Average Difference (I–J) | Standard Error | F | Sig. (p) |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 19–30 | 31–44 | −156 | 123 | 1.627 | 0.085 |
| 45–64 | −227 | 106 | 1.183 | 0.033 \* |
| 31–44 | 19–30 | 124 | 115 | 0.763 | 0.082 |
| 45–64 | −102 | 128 | 1.272 | 0.106 |
| 45–64 | 19–30 | 258 | 109 | 0.852 | 0.021 \* |
| 31–44 | 118 | 132 | 1.045 | 0.117 |

Compared significance under the 0.05 level is indicated by \*.

|     |     |
| --- | --- |
|  | **Publisher’s Note:** MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations. |

© 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license ( [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)).

## Share and Cite

[Email](mailto:?&subject=From%20MDPI%3A%20%22Exploring%20the%20Planning%20and%20Configuration%20of%20the%20Hospital%20Wayfinding%20System%20by%20Space%20Syntax%3A%20A%20Case%20Study%20of%20Cheng%20Ching%20Hospital%2C%20Chung%20Kang%20Branch%20in%20Taiwan%22&body=https://www.mdpi.com/1239890%3A%0A%0AExploring%20the%20Planning%20and%20Configuration%20of%20the%20Hospital%20Wayfinding%20System%20by%20Space%20Syntax%3A%20A%20Case%20Study%20of%20Cheng%20Ching%20Hospital%2C%20Chung%20Kang%20Branch%20in%20Taiwan%0A%0AAbstract%3A%20With%20regard%20to%20the%20outpatient%20areas%20of%20a%20hospital%2C%20the%20smoothness%20of%20the%20route%20is%20now%20taken%20into%20consideration%20in%20the%20process%20of%20configuring%20the%20wayfinding%20system.%20As%20patients%20often%20spend%20time%20on%20ineffective%20wayfinding%20processes%2C%20and%20there%20is%20limited%20manpower%20at%20hospitals%20and%20a%20lack%20of%20clarity%20in%20the%20information%20provided%20by%20the%20wayfinding%20system%2C%20it%20is%20difficult%20to%20provide%20effective%20and%20timely%20consultation%20services%20for%20patients.%20This%20study%20was%20conducted%20at%20Cheng%20Ching%20Hospital%2C%20Chung%20Kang%20Branch%20%28CCH%2FCKB%29%20in%20Taiwan.%20This%20study%20attempts%20to%20investigate%20the%20relationships%20between%20the%20wayfinding%20system%20of%20the%20outpatient%20areas%20and%20the%20patients%E2%80%99%20behaviors%20in%20the%20hospital.%20Depthmap%20software%20based%20on%20space%20syntax%20is%20adopted%20to%20assist%20in%20the%20route%20analysis%20and%20wayfinding%20behaviors.%20It%20integrates%20axial%20mapping%20analysis%20and%20isovist%20analysis%20and%20gives%20suggestions%20on%20the%20location%2C%20format%20and%20content%20of%20the%20wayfinding%20system.%20The%20final%20results%20of%20the%20study%20show%20that%20in%20the%20wayfinding%20task%20experiment%20gender%20has%20no%20significant%20impact%20on%20the%20effect%20of%20wayfinding[...] "Email")[LinkedIn](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.mdpi.com%2F1239890&title=Exploring%20the%20Planning%20and%20Configuration%20of%20the%20Hospital%20Wayfinding%20System%20by%20Space%20Syntax%3A%20A%20Case%20Study%20of%20Cheng%20Ching%20Hospital%2C%20Chung%20Kang%20Branch%20in%20Taiwan%26source%3Dhttps%3A%2F%2Fwww.mdpi.com%26summary%3DWith%20regard%20to%20the%20outpatient%20areas%20of%20a%20hospital%2C%20the%20smoothness%20of%20the%20route%20is%20now%20taken%20into%20consideration%20in%20the%20process%20of%20configuring%20the%20wayfinding%20system.%20As%20patients%20often%20spend%20time%20on%20ineffective%20wayfinding%20processes%2C%20and%20there%20is%20%5B...%5D "LinkedIn")[facebook](http://www.facebook.com/sharer.php?u=https://www.mdpi.com/1239890 "facebook")[Reddit](http://www.reddit.com/submit?url=https://www.mdpi.com/1239890 "Reddit")[Mendeley](http://www.mendeley.com/import/?url=https://www.mdpi.com/1239890 "Mendeley")

**MDPI and ACS Style**

Chen, M.-S.; Ko, Y.-T.; Hsieh, W.-C.
Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan. _ISPRS Int. J. Geo-Inf._ **2021**, _10_, 570.
https://doi.org/10.3390/ijgi10080570

**AMA Style**

Chen M-S, Ko Y-T, Hsieh W-C.
Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan. _ISPRS International Journal of Geo-Information_. 2021; 10(8):570.
https://doi.org/10.3390/ijgi10080570

**Chicago/Turabian Style**

Chen, Ming-Shih, Yao-Tsung Ko, and Wen-Che Hsieh.
2021\. "Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan" _ISPRS International Journal of Geo-Information_ 10, no. 8: 570.
https://doi.org/10.3390/ijgi10080570

**APA Style**

Chen, M.-S., Ko, Y.-T., & Hsieh, W.-C.

(2021). Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan. _ISPRS International Journal of Geo-Information_, _10_(8), 570.
https://doi.org/10.3390/ijgi10080570

Note that from the first issue of 2016, this journal uses article numbers instead of page numbers. See further details [here](https://www.mdpi.com/about/announcements/784).

## Article Metrics

No

No

### Article Access Statistics

For more information on the journal statistics, click [here](https://www.mdpi.com/journal/ijgi/stats).

Multiple requests from the same IP address are counted as one view.

Zoom\| Orient \| As Lines \| As Sticks \| As Cartoon \| As Surface \|Previous Scene\|Next Scene

## Cite

Export citation file:
BibTeX \|
EndNote \|
RIS

**MDPI and ACS Style**

Chen, M.-S.; Ko, Y.-T.; Hsieh, W.-C.
Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan. _ISPRS Int. J. Geo-Inf._ **2021**, _10_, 570.
https://doi.org/10.3390/ijgi10080570

**AMA Style**

Chen M-S, Ko Y-T, Hsieh W-C.
Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan. _ISPRS International Journal of Geo-Information_. 2021; 10(8):570.
https://doi.org/10.3390/ijgi10080570

**Chicago/Turabian Style**

Chen, Ming-Shih, Yao-Tsung Ko, and Wen-Che Hsieh.
2021\. "Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan" _ISPRS International Journal of Geo-Information_ 10, no. 8: 570.
https://doi.org/10.3390/ijgi10080570

**APA Style**

Chen, M.-S., Ko, Y.-T., & Hsieh, W.-C.

(2021). Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan. _ISPRS International Journal of Geo-Information_, _10_(8), 570.
https://doi.org/10.3390/ijgi10080570

Note that from the first issue of 2016, this journal uses article numbers instead of page numbers. See further details [here](https://www.mdpi.com/about/announcements/784).

_clear_

We use cookies on our website to ensure you get the best experience.

Read more about our cookies [here](https://www.mdpi.com/about/privacy).

[Accept](https://www.mdpi.com/accept_cookies)

## Share Link

[Email](mailto:?&subject=From%20MDPI%3A%20%22Exploring%20the%20Planning%20and%20Configuration%20of%20the%20Hospital%20Wayfinding%20System%20by%20Space%20Syntax%3A%20A%20Case%20Study%20of%20Cheng%20Ching%20Hospital%2C%20Chung%20Kang%20Branch%20in%20Taiwan%22&body=https://www.mdpi.com/1239890%3A%0A%0AExploring%20the%20Planning%20and%20Configuration%20of%20the%20Hospital%20Wayfinding%20System%20by%20Space%20Syntax%3A%20A%20Case%20Study%20of%20Cheng%20Ching%20Hospital%2C%20Chung%20Kang%20Branch%20in%20TaiwanWith%20regard%20to%20the%20outpatient%20areas%20of%20a%20hospital%2C%20the%20smoothness%20of%20the%20route%20is%20now%20taken%20into%20consideration%20in%20the%20process%20of%20configuring%20the%20wayfinding%20system.%20As%20patients%20often%20spend%20time%20on%20ineffective%20wayfinding%20processes%2C%20and%20there%20is%20limited%20manpower%20at%20hospitals%20and%20a%20lack%20of%20clarity%20in%20the%20information%20provided%20by%20the%20wayfinding%20system%2C%20it%20is%20difficult%20to%20provide%20effective%20and%20timely%20consultation%20services%20for%20patients.%20This%20study%20was%20conducted%20at%20Cheng%20Ching%20Hospital%2C%20Chung%20Kang%20Branch%20%28CCH%2FCKB%29%20in%20Taiwan.%20This%20study%20attempts%20to%20investigate%20the%20relationships%20between%20the%20wayfinding%20system%20of%20the%20outpatient%20areas%20and%20the%20patients%E2%80%99%20behaviors%20in%20the%20hospital.%20Depthmap%20software%20based%20on%20space%20syntax%20is%20adopted%20to%20assist%20in%20the%20route%20analysis%20and%20wayfinding%20behaviors.%20It%20integrates%20axial%20mapping%20analysis%20and%20isovist%20analysis%20and%20gives%20suggestions%20on%20the%20location%2C%20format%20and%20content%20of%20the%20wayfinding%20system.%20The%20final%20results%20of%20the%20study%20show%20that%20in%20the%20wayfinding%20task%20experiment%20gender%20has%20no%20significant%20impact%20on%20the%20effect%20of%20wayfinding%20efficiency%2C%20while%20a[...] "Email")[Twitter](https://x.com/intent/tweet?text=Exploring+the+Planning+and+Configuration+of+the+Hospital+Wayfinding+System+by+Space+Syntax%3A+A+Case+Study+of+Cheng+Ching+Hospital%2C+Chung+Kang+Branch+in+Taiwan&hashtags=mdpiijgi&url=https%3A%2F%2Fwww.mdpi.com%2F1239890&via=ISPRS_IJGI "Twitter")[LinkedIn](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.mdpi.com%2F1239890&title=Exploring%20the%20Planning%20and%20Configuration%20of%20the%20Hospital%20Wayfinding%20System%20by%20Space%20Syntax%3A%20A%20Case%20Study%20of%20Cheng%20Ching%20Hospital%2C%20Chung%20Kang%20Branch%20in%20Taiwan%26source%3Dhttps%3A%2F%2Fwww.mdpi.com%26summary%3DWith%20regard%20to%20the%20outpatient%20areas%20of%20a%20hospital%2C%20the%20smoothness%20of%20the%20route%20is%20now%20taken%20into%20consideration%20in%20the%20process%20of%20configuring%20the%20wayfinding%20system.%20As%20patients%20often%20spend%20time%20on%20ineffective%20wayfinding%20processes%2C%20and%20there%20is%20%5B...%5D "LinkedIn")[facebook](http://www.facebook.com/sharer.php?u=https://www.mdpi.com/1239890 "facebook")[Reddit](http://www.reddit.com/submit?url=https://www.mdpi.com/1239890 "Reddit")[Mendeley](http://www.mendeley.com/import/?url=https://www.mdpi.com/1239890 "Mendeley")[CiteULike](http://www.citeulike.org/posturl?url=https://www.mdpi.com/1239890 "CiteULike")

Copy

_clear_

## Share

https://www.mdpi.com/1239890

_clear_

[Back to TopTop](https://www.mdpi.com/2220-9964/10/8/570#)

### 来源 8: http://www.nature.com/articles/s41598-025-20128-0.pdf

- URL: http://www.nature.com/articles/s41598-025-20128-0.pdf
- 精读方法：jina-readerlm-academic

```markdown
The provided draft Markdown does not match the content of the original HTML, which only contains a head tag with no actual body content. Therefore, there is nothing to extract or refine further into Markdown beyond the title "Your Title" if one were present.
```

### 来源 9: Improving wayfinding in hospitals for people with diverse needs and abilities: An exploratory approach based on multi-criteria decision making

- URL: https://www.sciencedirect.com/science/article/abs/pii/S0003687023001874
- 精读方法：jina-readerlm-academic

```markdown
# Improving wayfinding in hospitals for people with diverse needs and abilities: An exploratory approach based on multi-criteria decision making

## Abstract

Hospital [wayfinding](/topics/computer-science/wayfinding) systems that are based solely on signage do not provide adequate solutions for [wayfinding](/topics/computer-science/wayfinding) needs, especially for users with impairments. Moreover, the interaction between user characteristics and the inner space of the building also determines wayfinding efficiency. The aims of this study, therefore, were to identify architectural features that affect spatial orientation and wayfinding behaviors; demonstrate the multicriteria decision-making (MCDM) processes for improved wayfinding; and produce a set of quantitative values (i.e., weights) for each selected architectural feature, based on the individual's preferences.

Doing so could enable the formulating of practical design guidelines for hospital buildings, tailored to the needs and abilities of the users, to minimize disorientation and confusion – as demonstrated in this paper through a [case study](/topics/computer-science/case-study).

## Introduction

The term _wayfinding_ refers to the coordinated and goal-directed movements of an individual while traversing through the environment (Montello and Sas, 2006). Wayfinding employs a range of cognitive processes, such as perception, memory, and problem-solving, and relies on the provision of successive communication cues, such as visual, auditory, tactile, and olfactory elements. When performing indoor wayfinding, users usually draw on locally available information, such as maps and signs, that when combined could be defined as a wayfinding system. This system may also include implicit information from the surrounding architecture features (Passini et al., 2000).

### Hospital Environment Complexity

Wayfinding is particularly challenging in hospitals due to two related factors:
1. The design and layout of hospitals serve a wide range of users, including patients, visitors, and hospital staff.
2. Each group of users has numerous different needs and capabilities.

Henceforth,
- Successful wayfinding is dependent on navigational cues that are beneficial for such user diversity.
- This is particularly important in the light of recent demographic changes in user populations.

For instance,
- In the U.S., the elderly population is expected to increase from 16% of the population (54 million people) in 2019 to 21% by 2040 (Administration for Community Living, 2021).
- Since aging has been linked to decreased spatial cognition and learning capacity, reduced visual acuity, and narrowed visual field.
- Future users are likely to be less adept at navigating within new or familiar environments.
- Users with disabilities are expected to increase from 60.1 million in 2021 to 80.8 million in 2040 (Centers for Disease Control and Prevention, 2022).

### Signage Challenges

Studies indicate that signage should only be recommended as a primary wayfinding support strategy in cases where interior design features are insufficient for providing sufficient information.

### Aim

The aim was threefold:
1. Identify architectural features within a hospital environment that affect users' wayfinding experiences.
2. Demonstrate a methodology for generating ease-of-use rating tools in relation to specific routes within a hospital.
3. Produce a set of quantitative values (i.e., weights) for each selected architectural feature/criterion.

## Highlights

- Summarized the effects of architectural features on wayfinding behaviors.
- Demonstrated multicriteria decision-making processes for improved wayfinding.
- Designed inclusive ways finding systems for a diverse range of users.
- Illustrated a process for generating routes that minimize users' disorientation.

## Abstract

Hospital [wayfinding](/topics/computer-science/wayfinding) systems that are based solely on signage do not provide adequately solutions for [wayfinding](/topics/computer-science/wayfinding) needs. Moreover, interactions between user characteristics and inner space determine wayfinding efficiency.

The aims were:
- To identify architectural features affecting spatial orientation and wayfinding behaviors.
- To implement an MCDM approach for improving wayfinding in diverse user groups.
- To generate routes minimizing disorientation using an MCDM approach.

## Section Snippets

### Modeling the WayFinding Problem

By modeling the relationship between the structure of physical space and individual behavior:

* N*(N−1)/2 comparisons are required.

### Applying Multicriteria Decision-Making Approach

While existing models help clarify role architecture impacts:

| Architectural Features | Impact Description |
|-----------------------|--------------------|
| Visual Affordance       | Enhances visibility |
| Interior Design Features | Supports navigation |

#### Research Contributions

This research aimed at illustrating an applicable process for generating internal routes within a hospital:

* Identifying architectural features impacting user experience.
* Implementing an MCDM approach to assess ease-of-use ratings.
* Producing quantitative values representing user preferences.

## Funding

This research did not receive any specific grant from funding agencies in public or commercial sectors.

## Acknowledgments

The authors acknowledge assistance from Sara Catarina Arez Simões in developing literature reviews regarding architectural factors affecting spatial orientation and wayfinding behavior.

## References (56)

1. Bates *et al.*  
   ### How Cognitive Aging Affects Multisensory Integration Of Navigation Cues  
   **Neurobiol. Aging** (2014)
   
2. Birrell *et al.*  
   ### Urban Air Mobility Infrastructure Design: Using Virtual Reality To Capture User Experience Within The World's First Urban Airport  
   **Appl. Ergon** (2022)
   
3. Bozgeyikli *et al.*  
   ### Locomotion In Virtual Reality For Room Scale Tracked

### 来源 10: 专家观点 - 智慧医院产品观（十一）：适老化设计-中国医院协会信息专业委员会

- URL: https://www.chima.org.cn/Html/News/Articles/15495.html
- 精读方法：firecrawl-scrape

![](https://www.chima.org.cn/Sites/Uploaded/UserUpLoad/20220427/20220427102144.png)![](https://www.chima.org.cn/Sites/Uploaded/Image/2022/04/276378665177626846867181175.png)![](https://www.chima.org.cn/Content/Areas/Common/images/logo/wxShare.jpg)

[![](https://www.chima.org.cn/Sites/Uploaded/UserUpLoad/20200217/20200217152616.png)\\
首 页](https://www.chima.org.cn/)
[CHIMA介绍](https://www.chima.org.cn/Html/News/Main/52.html)

[CHIMA简介](https://www.chima.org.cn/Html/News/Columns/1/Index0.html)
[CHIMA委员](https://www.chima.org.cn/Html/News/Columns/2/Index0.html)
[学术活动](https://www.chima.org.cn/Html/News/Columns/3/Index0.html)
[新闻中心](https://www.chima.org.cn/Html/News/Main/53.html)

[政策法规](https://www.chima.org.cn/Html/News/Columns/4/Index0.html)
[通知公告](https://www.chima.org.cn/Html/News/Columns/5/Index0.html)
[专家观点](https://www.chima.org.cn/Html/News/Columns/6/Index0.html)
[案例分享](https://www.chima.org.cn/Html/News/Columns/34/Index0.html)
[行业动态](https://www.chima.org.cn/Html/News/Columns/7/Index0.html)
[新闻周报](https://www.chima.org.cn/Html/News/Columns/45/Index0.html)
[报告下载](https://www.chima.org.cn/Html/News/Columns/10/Index0.html)
[品牌活动](https://www.chima.org.cn/Html/News/Main/57.html)

[CHIMA CIO班](https://www.chima.org.cn/Html/News/Columns/46/Index0.html)
[CHIMA大会](https://www.chima.org.cn/Html/News/Columns/16/Index0.html)
[走进医院](https://www.chima.org.cn/Html/News/Columns/17/Index0.html)
[西部行](https://www.chima.org.cn/Html/News/Columns/18/Index0.html)
[安全训练营](https://www.chima.org.cn/Html/News/Columns/19/Index0.html)
[CHIMA 2026](https://2026.chima.org.cn/)
[VendorClub](https://www.chima.org.cn/Interactions/Companys/Collect)
[CHIMA大讲堂](https://djt.chima.org.cn/)

- [登录](https://www.chima.org.cn/Account/LogOn)
- \|
- 加入收藏

- 您所在的位置：
- [首页](https://www.chima.org.cn/)
- >> [新闻中心](https://www.chima.org.cn/Html/News/Main/53.html)
- >> [专家观点](https://www.chima.org.cn/Html/News/Columns/6/Index0.html)

- [政策法规](https://www.chima.org.cn/Html/News/Columns/4/Index0.html)
- [通知公告](https://www.chima.org.cn/Html/News/Columns/5/Index0.html)
- [专家观点](https://www.chima.org.cn/Html/News/Columns/6/Index0.html)
- [案例分享](https://www.chima.org.cn/Html/News/Columns/34/Index0.html)
- [行业动态](https://www.chima.org.cn/Html/News/Columns/7/Index0.html)
- [新闻周报](https://www.chima.org.cn/Html/News/Columns/45/Index0.html)

# 智慧医院产品观（十一）：适老化设计

发布时间：2022-04-27

浏览次数：

1619

**前言**

最近，我经常收看一档名为《梦想改造家》的节目。这档以家居装修改造为主题的节目中，经常会提到一种设计理念：适老化设计。

适老化设计，顾名思义，是一种针对老年人群体的人文关怀式设计。通过在商场、医院、学校等公共建筑中，充分考虑到老年人的身体机能及行动特点，做出相应的设计，包括实现无障碍设计，旨在让“建筑更加人性化，适用性更强”。为老人营造一个便利且安全的生活环境。

今年春节，父母来我家过年。我是做技术出身，家里自然少不了智能家居的身影。但是这些给我带来诸多便利的科技产品，却给父母带来了很多麻烦，甚至让他们显得无所适从。为此，我进行了一系列“去智能化”改造，把一些使用率高、便于替换的智能设备，换成了更符合父母操作习惯的传统设备。

这段经历让我认识到，“适老化设计”不仅仅是电视屏幕中的一种高大上的设计理念，它就在身边，关乎每个人的生活。

**1适老化设计的医疗应用场景**

节后，一次去医院的经历让我意识到，适老性设计在医疗场景中的重要性。

以往去医院，我更多是出于参观、办事等目的，心态较为平和。这次不同，当我卸下所有的职场身份，纯粹以一个患者家属的身份，带着焦躁的情绪，在一所陌生的医院里来回奔波时，心态和诉求都变了。

比如，当我手里拿着一堆单据找路时，我完全没有心情去掏出手机，扫二维码，拉起什么小程序，再跳转到院内导航。

相反，我下意识地倾向于选择肉眼可见的指路标识，我觉得这种无需借助任何技术的工具，在紧急情况和焦虑心态下非常好用。

![微信图片_20220426165202.png](https://www.chima.org.cn/Sites/Uploaded/Image/2022/04/276378665177626846867181175.png)

再比如，当我使用各种自助机服务时，总是被一些不规范的设计搞得很困惑，比如下面这台取药自助签到机：看似挺大一块屏幕，近三分之二的内容是与我的流程无关的广告，还占据着主视线。当你带着焦虑的心态站在这样一台“不懂事”的机器面前时，你甚至觉得它就是来给你添堵的，而不是帮你解决问题的。

![微信图片_20220426165204.png](https://www.chima.org.cn/Sites/Uploaded/Image/2022/04/276378665178517514709702542.png)

类似这样的问题还有很多，我就不一一举例了，也不是针对某个具体的医院或者公司。我想要表达的是，如果连我这样的从业者，在医院就诊时，面对各式各样的数字化工具和场景，都免不了困惑，那可想而知，中老年群体在面对所谓的智能化就医场景时，要面对怎样隐形的数字鸿沟，会是怎样的无所适从。

**2老年群体的特点**

个体在进入老年期后，老年群体的生活特征和认知能力会出现不同程度的退行性变化。对此，在《顺丰速运APP适老化体验设计复盘》一文中，作者将老年群体的退行性变化特征分为视觉、操作和认知三个方面，具体如下：

![微信图片_20220426165206.png](https://www.chima.org.cn/Sites/Uploaded/Image/2022/04/276378665179794695188641076.png)

图源自“SFUP Design”公众号

**3对于适老化设计的几点建议**

**一是遵循既有的设计规范。** 在数字医疗诞生之前，传统医疗已经存在很多年，在用色、文案、样式方面，早就形成了一套既有的行业规范。数字化的医疗产品作为一个后来者，更多的应该是去遵守规范，而不是盲目创新。

比如下图是我医院门诊大厅里张贴的一张“取药流程”，与门诊大厅主色调保持一致，有事说事儿，重点突出，没有任何的干扰项和多余信息，一目了然。

![微信图片_20220426165208.png](https://www.chima.org.cn/Sites/Uploaded/Image/2022/04/276378665181958787031385056.png)

没有对比就没有差距，某个门诊自助机界面，一眼看过去，是不是觉得内容“过于丰富”?信息密集度高，文本获取难度大，与患者无关的干扰选项太多，尤其是文字上的图标，既是干扰项，还挤压了文字显示的空间，背景图更是一个与需求毫无相干的整体干扰项。

![微信图片_20220426165209.png](https://www.chima.org.cn/Sites/Uploaded/Image/2022/04/276378665182484246773788961.png)

**二是从真实世界自然引出数字场景。** 在数字场景出现之前，用户对于医疗场景的认识和习惯多来自于真实世界，也就是我们俗称的线下，这个线下世界的既有设计规范和使用习惯，每个人都耳熟能详，都是这样看着过来的。数字化医疗工具和场景的介入，既不应该挤压传统医疗场景的空间和位置，更应该借助传统场景，选择更平滑的方式，在传统世界和数字场景之间，搭建一个平滑的过渡桥梁。

比如，把拉起院内导航的二维码，就放在传统导航里，既保留了传统导航的直观便捷，也预留了数字化工具的入口。

![微信图片_20220426165211.png](https://www.chima.org.cn/Sites/Uploaded/Image/2022/04/276378665183352515071010622.png)

还有个很好的例子，很多医院里都有类似“专家简介”的海报和宣传栏，散落在门诊大厅、科室走廊以及医院的主干道上。仔细留意会发现，尽管随着各类在线业务的上线，类似专家简介、出诊信息等信息已经陆续搬到手机屏幕里，但是，传统的海报和宣传栏前，还是不时的有患者驻足观看，甚至拿出手机拍照。这说明什么呢?

首先，海报和宣传栏，在内容展示的可视性上，确实比手机屏幕要好太多，也更符合中老年群体的阅读习惯。其次，由医院张贴的海报和宣传栏，代表了一种官方背书，更容易获取患者信任。

那么，是不是可以考虑，在海报、宣传内容中增加二维码，通过扫码拉起医院的官方公众号、医生的个人主页、排班信息等等，让用户快速获取自己想要的资源，同时建立真实世界和虚拟场景之间的关联。

**三是尊重患者的心态。** 谁都不希望自己老去，更不愿意别人把他当作老人。有一阵儿我父亲总是丢手机，我妈当着他的面跟我说，给你爸买个老人机算了，省事，丢了也不可惜。我爸一听就不乐意了，我赶紧打圆场说，我爸玩智能手机玩得挺好，还是给他买之前那款智能手机，小心点就是了。

所以，在做适老化设计的时候，不能只考虑产品本身的功能，也不是把字体调大一点、对比度调高一点那么简单，而是要用同理心来觉察老人群体的心理和情感，不能让他们觉得，因为自己老了，我们才设计了这个产品去帮他(她)，而一旦用了这个产品，就意味着被打上了“老人”的标签。就像我刚才提到的例子中的老人机。

在这方面，国家政务平台就做得很好，在“防疫健康信息码”界面底部，采用了“关怀模式”的描述，而不是“老年模式、老人版本”等，技术的温度，就体现在这些细微之处。

![微信图片_20220426165213.png](https://www.chima.org.cn/Sites/Uploaded/Image/2022/04/276378665184524629177290309.png)

再举个很好的例子，很多人都有个习惯，看到不错的科普文章，会顺手转发给自己的父母，我也是这样。但时间久了我发现，科普文章逻辑严密、内容都不短，想要希望父母准确理解其中的意图，多少有点儿难度。我只能在转发的同时，把文中的重点摘录给父母看，提醒他们注意。

最近，在一些医学科普文章中，我发现了积极的变化：在文章的开头或者结尾，用一张图，配上较大的字体，把文章重点罗列总结，父母只需要看这张图，就能掌握精髓。我认为这也是一种适老化设计的体现。

**4结尾**

我常听到一种说法，青年人是引领浪潮的“数字原住民”，中年人是亦步亦趋的“数字移民”，老年人则是被拒之门外的“数字难民”。适老化设计，就是为了消除三种身份之间的割裂感，助力老年人跨越数字鸿沟，帮助老年人更好地融入智能生活。毕竟每个人都会老去，现在以产品设计者的身份进行适老化设计，就是帮助老去后的自己。

作者简介

李楠，CHIMA青年委员。现从事医院管理和信息化工作。作者观点仅代表个人，纯属技术交流，与供职单位无关。

上一篇： [郭扬帆：HIS系统上线宝典｜时间节点，学会倒算](https://www.chima.org.cn/Html/News/Articles/15499.html "郭扬帆：HIS系统上线宝典｜时间节点，学会倒算")

下一篇： [武汉同济医院多院区公立医院医技检查精细化管理实践](https://www.chima.org.cn/Html/News/Articles/15492.html "武汉同济医院多院区公立医院医技检查精细化管理实践")


## 跨源矛盾检测结论

### 检测范围
- 已精读来源数量：9 个
- 检测对象：核心数字、日期、功能描述、因果判断、市场/公司事实
- 检测时间：2026-06-21

### 检测结果
结论：待 Agent 基于精读全文检测。最终报告必须替换为以下二选一：

结论：未检测到跨源矛盾，可进入综合阶段。

或：

结论：检测到 X 处跨源矛盾，综合输出时必须保留双方表述，不得静默合并。

### 矛盾项 1：[简短标题]
- 矛盾描述：[具体什么矛盾]
- 来源 A：[URL]
  - 原文引用：“……”
  - 来源等级：A / B / C / D
  - 发布时间 / 数据日期：YYYY-MM-DD
- 来源 B：[URL]
  - 原文引用：“……”
  - 来源等级：A / B / C / D
  - 发布时间 / 数据日期：YYYY-MM-DD
- 初步判断：
  - 倾向：[来源 A / 来源 B / 暂不倾向]
  - 理由：[官方一手来源优先 / 数据更新 / 方法更透明 / 与中文本地来源一致]
- 综合输出要求：
  - 必须写成“来源 A 说 X，来源 B 说 Y，建议人工核实”
  - 禁止取平均值、合并成第三种说法、只保留其中一方
## 矛盾与不确定性

- 脚本不会自动裁决跨源矛盾。Agent 编译最终报告时，必须比较数字、日期、因果关系和产品能力声明。
- 本证据包中没有 URL 支撑的说法都应视为未验证，不得作为事实写入最终调研报告或 Wiki。

## 工具运行记录

- 候选信源超过 15 个，已使用 Jina Reranker 精选。

## 入库提醒

只有在 Agent 已完成新的中文综合 raw 报告并删除本证据包后，才能询问用户是否入库。若用户确认，按完整 `SCHEMA.md` Ingest 工作流执行。
