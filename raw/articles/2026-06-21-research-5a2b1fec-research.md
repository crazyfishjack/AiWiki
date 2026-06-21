---
title: "调研证据包：医院导视 设计逻辑 导视设计 适老化 通用设计"
source-type: article
generated: 2026-06-21
generated-by: wiki-research-skill
research-mode: standard
---

# 调研证据包：医院导视 设计逻辑 导视设计 适老化 通用设计

## 调研问题

医院导视 设计逻辑 导视设计 适老化 通用设计

## 摘要

本文档是四工具检索生成的证据包草稿，不是最终调研报告。Agent 必须先阅读本证据包，执行下方"AI 综合指令"，生成新的中文综合 raw 报告，然后询问用户是否入库。本证据包保留不删除。

- 发现候选信源：25
- 精读信源数量：10
- 精读成功数量：10
- 精读失败数量：0

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
| exa | 1.00 | A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness | https://pmc.ncbi.nlm.nih.gov/articles/PMC9656047/ |
| exa | 1.00 | A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness | https://www.mdpi.com/1660-4601/19/21/13885 |
| exa | 1.00 |  | http://www.nature.com/articles/s41598-025-20128-0.pdf |
| exa | 1.00 | Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan | https://www.mdpi.com/2220-9964/10/8/570 |
| exa | 1.00 | A Comparative Analysis of the Spatial Design Perspective of Wayfinding: The Emergency Room as a Case Study | https://www.mdpi.com/2075-5309/15/4/516 |
| exa | 1.00 | Optimized Wayfinding Signage Positioning in Hospital Built Environment through Medical Data and Flows Simulations | https://www.mdpi.com/2075-5309/12/9/1426 |
| exa | 1.00 | Elderly users’ perceptions of signage systems from tertiary hospitals in Guangzhou | https://pmc.ncbi.nlm.nih.gov/articles/PMC10840000/ |
| exa | 1.00 | Exploring Sign System Design for a Medical Facility: A Virtual Environment Study on Wayfinding Behaviors | https://www.mdpi.com/2075-5309/13/6/1366 |
| exa | 1.00 | Adaptive Aging Safety of Guidance Marks in Rail Transit Connection Systems Based on Eye Movement Data | https://pmc.ncbi.nlm.nih.gov/articles/PMC8775515/ |
| exa | 1.00 | Dementia-Friendly Design: A Set of Design Criteria and Design Typologies Supporting Wayfinding - PMC | https://pmc.ncbi.nlm.nih.gov/articles/PMC8725382/ |
| exa | 1.00 | (De)signs of Confusion: Architectural Environments Causing Confusion for People with Advanced Dementia During Wayfinding | https://www.mdpi.com/3042-4518/3/1/10 |
| exa | 1.00 | Enhancing Wayfinding Experience in Low-Vision Individuals through a Tailored Mobile Guidance Interface | https://www.mdpi.com/2079-9292/12/22/4561 |
| exa | 1.00 | Wayfinding in Complex Medical Facilities: The Indexicality of Directional Arrows | https://pmc.ncbi.nlm.nih.gov/articles/PMC10621024/ |
| exa | 1.00 | Aging Adaptation Transition of Health Care Buildings for Accessibility Optimization for the Elderly | https://www.mdpi.com/2075-5309/15/3/379 |
| exa | 1.00 | Implementing an augmented reality-enabled wayfinding system through studying user experience and requirements in complex environments | https://link.springer.com/article/10.1186/s40327-015-0026-2 |
| tavily | 0.71 | [PDF] 积极老龄化视角下社区公共导视系统适老化设计研究 | https://pdf.hanspub.org/ar_3141153.pdf |
| tavily | 0.68 | [PDF] 基于案例分析的国内外医疗机构导视系统设计现状研究 | https://pdf.hanspub.org/design202496_1871181613.pdf |
| tavily | 0.60 | 筑医台--HCD医养设计--医院导视标识的前世今生 | http://hcd.zhuyitai.com/journals/hcd/article/d2195d017b9249f296ad72725c7ed2f6 |
| tavily | 0.54 | 专家观点 - 智慧医院产品观（十一）：适老化设计-中国医院协会信息专业委员会 | https://www.chima.org.cn/Html/News/Articles/15495.html |
| tavily | 0.54 | 适老化视阙下医院导视设计策略探究 | https://www.hanspub.org/journal/paperinformation?paperid=71956 |
| tavily | 0.53 | Research on Design Strategy of Guided Vision in Hospital for Aging ... | https://www.researchgate.net/publication/373763311_Research_on_Design_Strategy_of_Guided_Vision_in_Hospital_for_Aging_Patients |
| tavily | 0.50 | 微信长辈就医适老化设计规范 \| 微信服务号文档 | https://developers.weixin.qq.com/doc/service/guide/product/elderMedical/elderMedical-designstandards.html |
| tavily | 0.47 | 微信长辈就医适老化设计规范 \| 微信开放文档 | https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/cityservice/elderMedical-designstandards.html |
| tavily | 0.45 | 友善设计——老年医院导视系统的适老化设计实践探究-维普期刊 中文期刊服务平台 | http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688&from=Qikan_Article_Detail |
| tavily | 0.45 | [PDF] 香港垂直居所的适老设计指引* | https://soinnohub.polyujcsoinno.hk/wp-content/uploads/2023/01/Luk-2019-Guide-for-Vertical-Building-Design-for-the-Elderly-in-Hong-Kong.pdf |

## 信源质量门控记录

### 门控规则
- Tavily score < 0.4：剔除
- 已知低质域名：剔除
- 重复 URL：合并保留最高分结果
- Exa 学术/语义结果：默认保留，但进入来源等级评估
- C/D 级来源不得作为唯一结论依据
- 入库映射：A/B → `source-quality: high`；C → `source-quality: medium`；D → `source-quality: low`

### 保留信源
1. [A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness](https://pmc.ncbi.nlm.nih.gov/articles/PMC9656047/)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
2. [A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness](https://www.mdpi.com/1660-4601/19/21/13885)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
3. [http://www.nature.com/articles/s41598-025-20128-0.pdf](http://www.nature.com/articles/s41598-025-20128-0.pdf)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
4. [Exploring the Planning and Configuration of the Hospital Wayfinding System by Space Syntax: A Case Study of Cheng Ching Hospital, Chung Kang Branch in Taiwan](https://www.mdpi.com/2220-9964/10/8/570)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
5. [A Comparative Analysis of the Spatial Design Perspective of Wayfinding: The Emergency Room as a Case Study](https://www.mdpi.com/2075-5309/15/4/516)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
6. [Optimized Wayfinding Signage Positioning in Hospital Built Environment through Medical Data and Flows Simulations](https://www.mdpi.com/2075-5309/12/9/1426)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
7. [Elderly users’ perceptions of signage systems from tertiary hospitals in Guangzhou](https://pmc.ncbi.nlm.nih.gov/articles/PMC10840000/)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
8. [Exploring Sign System Design for a Medical Facility: A Virtual Environment Study on Wayfinding Behaviors](https://www.mdpi.com/2075-5309/13/6/1366)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
9. [Adaptive Aging Safety of Guidance Marks in Rail Transit Connection Systems Based on Eye Movement Data](https://pmc.ncbi.nlm.nih.gov/articles/PMC8775515/)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
10. [Dementia-Friendly Design: A Set of Design Criteria and Design Typologies Supporting Wayfinding - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8725382/)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
11. [(De)signs of Confusion: Architectural Environments Causing Confusion for People with Advanced Dementia During Wayfinding](https://www.mdpi.com/3042-4518/3/1/10)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
12. [Enhancing Wayfinding Experience in Low-Vision Individuals through a Tailored Mobile Guidance Interface](https://www.mdpi.com/2079-9292/12/22/4561)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
13. [Wayfinding in Complex Medical Facilities: The Indexicality of Directional Arrows](https://pmc.ncbi.nlm.nih.gov/articles/PMC10621024/)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
14. [Aging Adaptation Transition of Health Care Buildings for Accessibility Optimization for the Elderly](https://www.mdpi.com/2075-5309/15/3/379)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：Exa 学术/语义结果，默认保留但进入来源等级评估
   - 后续处理：进入 rerank
15. [Implementing an augmented reality-enabled wayfinding system through studying user experience and requirements in complex environments](https://link.springer.com/article/10.1186/s40327-015-0026-2)
   - 工具：exa
   - 分数：Exa 默认保留
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：学术论文
   - 后续处理：进入精读
16. [[PDF] 积极老龄化视角下社区公共导视系统适老化设计研究](https://pdf.hanspub.org/ar_3141153.pdf)
   - 工具：tavily
   - 分数：0.71
   - 来源等级：B
   - 入库映射：`source-quality: high`
   - 保留原因：与主题高度相关
   - 后续处理：进入精读
17. [[PDF] 基于案例分析的国内外医疗机构导视系统设计现状研究](https://pdf.hanspub.org/design202496_1871181613.pdf)
   - 工具：tavily
   - 分数：0.68
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
18. [筑医台--HCD医养设计--医院导视标识的前世今生](http://hcd.zhuyitai.com/journals/hcd/article/d2195d017b9249f296ad72725c7ed2f6)
   - 工具：tavily
   - 分数：0.60
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
19. [专家观点 - 智慧医院产品观（十一）：适老化设计-中国医院协会信息专业委员会](https://www.chima.org.cn/Html/News/Articles/15495.html)
   - 工具：tavily
   - 分数：0.54
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
20. [适老化视阙下医院导视设计策略探究](https://www.hanspub.org/journal/paperinformation?paperid=71956)
   - 工具：tavily
   - 分数：0.54
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
21. [Research on Design Strategy of Guided Vision in Hospital for Aging ...](https://www.researchgate.net/publication/373763311_Research_on_Design_Strategy_of_Guided_Vision_in_Hospital_for_Aging_Patients)
   - 工具：tavily
   - 分数：0.53
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
22. [微信长辈就医适老化设计规范 | 微信服务号文档](https://developers.weixin.qq.com/doc/service/guide/product/elderMedical/elderMedical-designstandards.html)
   - 工具：tavily
   - 分数：0.50
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
23. [微信长辈就医适老化设计规范 | 微信开放文档](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/cityservice/elderMedical-designstandards.html)
   - 工具：tavily
   - 分数：0.47
   - 来源等级：A
   - 入库映射：`source-quality: high`
   - 保留原因：官方文档 / 一手数据
   - 后续处理：进入精读
24. [友善设计——老年医院导视系统的适老化设计实践探究-维普期刊 中文期刊服务平台](http://dianda.cqvip.com/Qikan/Article/Detail?id=7101034688&from=Qikan_Article_Detail)
   - 工具：tavily
   - 分数：0.45
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考
25. [[PDF] 香港垂直居所的适老设计指引*](https://soinnohub.polyujcsoinno.hk/wp-content/uploads/2023/01/Luk-2019-Guide-for-Vertical-Building-Design-for-the-Elderly-in-Hong-Kong.pdf)
   - 工具：tavily
   - 分数：0.45
   - 来源等级：C
   - 入库映射：`source-quality: medium`
   - 保留原因：相关性一般，需交叉验证
   - 后续处理：仅作背景参考

### 剔除信源
1. [医院导视系统](https://www.pinterest.com/ideas/%E5%8C%BB%E9%99%A2%E5%AF%BC%E8%A7%86%E7%B3%BB%E7%BB%9F/948575276788)
   - 工具：tavily
   - 分数：0.36
   - 来源等级：C
   - 剔除原因：score 低于 0.4
2. [[PDF] 《移动互联网应用(APP)适老化通用设计规范》解读](https://www.w3.org/2021/05/29-older-users-and-accessibility/slides/slides-dingliting.pdf)
   - 工具：tavily
   - 分数：0.35
   - 来源等级：C
   - 剔除原因：score 低于 0.4
3. [[PDF] 适老化街道空间的包容性设计策略 - Art and Design](https://api.artdesignp.com/uploads/file/asp/2024051008231869fb26205.pdf)
   - 工具：tavily
   - 分数：0.35
   - 来源等级：C
   - 剔除原因：score 低于 0.4
4. [移动互联网应用（APP）适老化通用设计规范（工业和信息化部）_中国互联网应用适老化及无障碍公共服务平台](http://wza.isc.org.cn/bztx/bzjd/mobile/index.html)
   - 工具：tavily
   - 分数：0.33
   - 来源等级：C
   - 剔除原因：score 低于 0.4
5. [互联网网站适老化通用设计规范 （工业和信息化部）_中国互联网应用适老化及无障碍公共服务平台](http://wza.isc.org.cn/bztx/bzjd/lgf)
   - 工具：tavily
   - 分数：0.31
   - 来源等级：C
   - 剔除原因：score 低于 0.4
6. [[PDF] 上海市既有住宅适老化改造技术导则（正文）](https://zjw.sh.gov.cn/cmsres/aa/aab97b16be89424698acaa58c55f1709/4bc0662f4ca91f897ad38fbad0a0cca1.pdf)
   - 工具：tavily
   - 分数：0.18
   - 来源等级：C
   - 剔除原因：score 低于 0.4
7. [[PDF] 《移动互联网应用(APP)适老化通用设计规范》解读](https://www.w3.org/2021/05/29-older-users-and-accessibility/slides/slides-dingliting.pdf)
   - 工具：tavily
   - 分数：0.37
   - 来源等级：C
   - 剔除原因：score 低于 0.4
8. [国外医院导视设计鉴赏丨理性又温柔，再也不怕在医院里迷路了](https://zhuanlan.zhihu.com/p/313408884)
   - 工具：tavily
   - 分数：0.34
   - 来源等级：C
   - 剔除原因：score 低于 0.4
9. [上海长征医院导视系统设计 :: Behance](https://www.behance.net/gallery/137875995/_?locale=zh_CN)
   - 工具：tavily
   - 分数：0.31
   - 来源等级：C
   - 剔除原因：score 低于 0.4
10. [互联网网站适老化通用设计规范 （工业和信息化部）_中国互联网应用适老化及无障碍公共服务平台](http://wza.isc.org.cn/bztx/bzjd/lgf)
   - 工具：tavily
   - 分数：0.30
   - 来源等级：C
   - 剔除原因：score 低于 0.4
11. [Digital maturity helps hospitals improve care under pressure - MobiHealthNews](https://www.mobihealthnews.com/video/digital-maturity-helps-hospitals-improve-care-under-pressure)
   - 工具：tavily
   - 分数：0.09
   - 来源等级：C
   - 剔除原因：score 低于 0.4
12. [How hospitals are managing Medline, Hologic product shortages - Modern Healthcare](https://www.modernhealthcare.com/medical-devices/mh-medline-hologic-supply-shortages-hospitals/)
   - 工具：tavily
   - 分数：0.08
   - 来源等级：C
   - 剔除原因：score 低于 0.4
13. [Electronic Caregiver and HCUnity Launch Longitudinal Care Intelligence Platform to Advance the Future of Connected Care - Digital Journal](https://www.digitaljournal.com/pr/news/access-newswire/electronic-caregiver-hcunity-launch-longitudinal-1346035092.html)
   - 工具：tavily
   - 分数：0.06
   - 来源等级：C
   - 剔除原因：score 低于 0.4
14. [Opmed and Mayo Clinic Unveil Multimodal AI Platform at ACC.26 to Optimize Surgical Capacity - HIT Consultant](https://hitconsultant.net/2026/06/18/opmed-mayo-clinic-cardiovascular-ai-scheduling/)
   - 工具：tavily
   - 分数：0.06
   - 来源等级：C
   - 剔除原因：score 低于 0.4
15. [‘Everybody will use AI, how do you remain relevant?’: LegalTechTalk 2026 panel explores legal design, legal engineering and the future of legal services - SCC Online](https://www.scconline.com/blog/post/2026/06/21/legal-design-legal-engineering-future-of-law-firms-legaltechtalk-2026/)
   - 工具：tavily
   - 分数：0.05
   - 来源等级：C
   - 剔除原因：score 低于 0.4
16. [More Americans Have a Plan to Age in Place - WSJ](https://www.wsj.com/lifestyle/relationships/americans-aging-housing-0e073f48)
   - 工具：tavily
   - 分数：0.04
   - 来源等级：C
   - 剔除原因：score 低于 0.4
17. [Clinical large language model centered on electronic medical records - Nature](https://www.nature.com/articles/s41746-026-02509-5)
   - 工具：tavily
   - 分数：0.04
   - 来源等级：A
   - 剔除原因：score 低于 0.4
18. [How outpatient surgery is opening the door for robot makers - Modern Healthcare News](https://www.modernhealthcare.com/medical-devices/mh-distalmotion-greg-roche-robotic-surgery-asc/)
   - 工具：tavily
   - 分数：0.04
   - 来源等级：C
   - 剔除原因：score 低于 0.4
19. [Why HaloMD may be the future of the No Surprises Act - Modern Healthcare](https://www.modernhealthcare.com/providers/mh-halomd-no-surprises-act-idr-disputes/)
   - 工具：tavily
   - 分数：0.03
   - 来源等级：C
   - 剔除原因：score 低于 0.4
20. [Renault unveils military SUV prototype as automakers pursue defense opportunities - Automotive News](https://canada.autonews.com/renault/ane-renault-thales-military-vehicle-0615/)
   - 工具：tavily
   - 分数：0.01
   - 来源等级：C
   - 剔除原因：score 低于 0.4
21. [[PDF] 积极老龄化视角下社区公共导视系统适老化设计研究](https://pdf.hanspub.org/ar_3141153.pdf)
   - 工具：tavily
   - 分数：0.58
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
22. [[PDF] 基于案例分析的国内外医疗机构导视系统设计现状研究](https://pdf.hanspub.org/design202496_1871181613.pdf)
   - 工具：tavily
   - 分数：0.53
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
23. [微信长辈就医适老化设计规范 | 微信开放文档](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/cityservice/elderMedical-designstandards.html)
   - 工具：tavily
   - 分数：0.28
   - 来源等级：A
   - 剔除原因：score 低于 0.4
24. [[PDF] 数字产品适老化研究综述:需求挖掘,障碍分析与优化设计](https://jirm.whu.edu.cn/jwk3/xxzyglxb/CN/article/downloadArticleFile.do?attachType=PDF&id=6413)
   - 工具：tavily
   - 分数：0.26
   - 来源等级：C
   - 剔除原因：score 低于 0.4
25. [[PDF] 《移动互联网应用(APP)适老化通用设计规范》解读](https://www.w3.org/2021/05/29-older-users-and-accessibility/slides/slides-dingliting.pdf)
   - 工具：tavily
   - 分数：0.22
   - 来源等级：C
   - 剔除原因：score 低于 0.4
26. [[PDF] 适老化街道空间的包容性设计策略 - Art and Design](https://api.artdesignp.com/uploads/file/asp/2024051008231869fb26205.pdf)
   - 工具：tavily
   - 分数：0.21
   - 来源等级：C
   - 剔除原因：score 低于 0.4
27. [互联网网站适老化通用设计规范 （工业和信息化部）_中国互联网应用适老化及无障碍公共服务平台](http://wza.isc.org.cn/bztx/bzjd/lgf)
   - 工具：tavily
   - 分数：0.21
   - 来源等级：C
   - 剔除原因：score 低于 0.4
28. [[PDF] 既有住宅适老化改造工程技术标准](http://xxgk.jl.gov.cn/zcbm/fgw_98022/xxgkmlqy/202411/P020241126354690280235.pdf)
   - 工具：tavily
   - 分数：0.15
   - 来源等级：C
   - 剔除原因：score 低于 0.4
29. [医院建筑规划与设计 - 在设计过程中助您一臂之力](https://www.draeger.com/zh_cn/Hospital/Planning-Design)
   - 工具：tavily
   - 分数：0.12
   - 来源等级：C
   - 剔除原因：score 低于 0.4
30. [[PDF] 重庆市医院建筑品质提升设计导则](https://zfcxjw.cq.gov.cn/zwgk_166/zfxxgkmls/zcwj/qtwj/202304/W020230410501422372247.pdf)
   - 工具：tavily
   - 分数：0.11
   - 来源等级：C
   - 剔除原因：score 低于 0.4
31. [[PDF] 基于案例分析的国内外医疗机构导视系统设计现状研究](https://pdf.hanspub.org/design202496_1871181613.pdf)
   - 工具：tavily
   - 分数：0.65
   - 来源等级：C
   - 剔除原因：重复 URL，已合并到最高分结果
32. [微信长辈就医适老化设计规范 | 微信服务号文档](https://developers.weixin.qq.com/doc/service/guide/product/elderMedical/elderMedical-designstandards.html)
   - 工具：tavily
   - 分数：0.42
   - 来源等级：A
   - 剔除原因：重复 URL，已合并到最高分结果
33. [[PDF] 全国一体化政务服务平台适老化服务建设指南](https://www.cnis.ac.cn/ynbm/zfglbzhyjzx/bzyjzq/gbyjzq/202508/P020250821330287517937.pdf)
   - 工具：tavily
   - 分数：0.39
   - 来源等级：C
   - 剔除原因：score 低于 0.4
34. [[PDF] 中华人民共和国国家标准家居产品适老化设计指南](http://www.cnlic.org.cn/zhongqingliangonggao/202406/P020240613034653.pdf)
   - 工具：tavily
   - 分数：0.39
   - 来源等级：C
   - 剔除原因：score 低于 0.4
35. [[PDF] 《移动互联网应用(APP)适老化通用设计规范》解读](https://www.w3.org/2021/05/29-older-users-and-accessibility/slides/slides-dingliting.pdf)
   - 工具：tavily
   - 分数：0.39
   - 来源等级：C
   - 剔除原因：score 低于 0.4
36. [[PDF] 适老化街道空间的包容性设计策略 - Art and Design](https://api.artdesignp.com/uploads/file/asp/2024051008231869fb26205.pdf)
   - 工具：tavily
   - 分数：0.37
   - 来源等级：C
   - 剔除原因：score 低于 0.4
37. [移动互联网应用（APP）适老化通用设计规范（工业和信息化部）_中国互联网应用适老化及无障碍公共服务平台](http://wza.isc.org.cn/bztx/bzjd/mobile/index.html)
   - 工具：tavily
   - 分数：0.36
   - 来源等级：C
   - 剔除原因：score 低于 0.4
38. [互联网网站适老化通用设计规范 （工业和信息化部）_中国互联网应用适老化及无障碍公共服务平台](http://wza.isc.org.cn/bztx/bzjd/lgf)
   - 工具：tavily
   - 分数：0.33
   - 来源等级：C
   - 剔除原因：score 低于 0.4
39. [[PDF] 北京市规划和自然资源委员会关于印发《既有住宅适老化改造设计 ...](http://ghzrzyw.beijing.gov.cn/biaozhunguanli/bz/jzsj/202005/P020200514392116575138.pdf)
   - 工具：tavily
   - 分数：0.20
   - 来源等级：C
   - 剔除原因：score 低于 0.4
40. [[PDF] 上海市既有住宅适老化改造技术导则（正文）](https://zjw.sh.gov.cn/cmsres/aa/aab97b16be89424698acaa58c55f1709/4bc0662f4ca91f897ad38fbad0a0cca1.pdf)
   - 工具：tavily
   - 分数：0.18
   - 来源等级：C
   - 剔除原因：score 低于 0.4

## 完整精读结果

### 来源 1: Research on Design Strategy of Guided Vision in Hospital for Aging ...

- URL: https://www.researchgate.net/publication/373763311_Research_on_Design_Strategy_of_Guided_Vision_in_Hospital_for_Aging_Patients
- 精读方法：firecrawl-scrape

- [Home](https://www.researchgate.net/directory/publications)
- [Neurophysiology](https://www.researchgate.net/topic/Neurophysiology/publications)
- [Biological Science](https://www.researchgate.net/topic/Biological-Science/publications)
- [Physiology](https://www.researchgate.net/topic/Physiology/publications)
- [Vision](https://www.researchgate.net/topic/Vision/publications)

ArticlePDF Available

# Research on Design Strategy of Guided Vision in Hospital for Aging Patients

- January 2023
- [Design](https://www.researchgate.net/journal/Design-2476-1524) 08(03):1222-1232

DOI: [10.12677/Design.2023.83148](https://doi.org/10.12677/Design.2023.83148)

Authors:

[![小漫 谢](https://c5.rgstatic.net/m/448675030402/images/icons/icons/author-avatar.svg)](https://www.researchgate.net/scientific-contributions/xiaoman-xie-2260566753)

[小漫 谢](https://www.researchgate.net/scientific-contributions/xiaoman-xie-2260566753)

[小漫 谢](https://www.researchgate.net/scientific-contributions/xiaoman-xie-2260566753)

- This person is not on ResearchGate, or hasn't claimed this research yet.

[Download full-text PDF](https://www.researchgate.net/publication/373763311_Research_on_Design_Strategy_of_Guided_Vision_in_Hospital_for_Aging_Patients/fulltext/6595b5d30bb2c7472b302498/Research-on-Design-Strategy-of-Guided-Vision-in-Hospital-for-Aging-Patients.pdf)

[Read full-text](https://www.researchgate.net/publication/373763311_Research_on_Design_Strategy_of_Guided_Vision_in_Hospital_for_Aging_Patients#read)

[Download citation](https://www.researchgate.net/publication/373763311_Research_on_Design_Strategy_of_Guided_Vision_in_Hospital_for_Aging_Patients/citation/download)

Copy link Link copied

* * *

[Read full-text](https://www.researchgate.net/publication/373763311_Research_on_Design_Strategy_of_Guided_Vision_in_Hospital_for_Aging_Patients#read) [Download citation](https://www.researchgate.net/publication/373763311_Research_on_Design_Strategy_of_Guided_Vision_in_Hospital_for_Aging_Patients/citation/download)
Copy link Link copied

![ResearchGate Logo](https://www.researchgate.net/images/icons/svgicons/researchgate-logo-white.svg)

**Discover the world's research**

- 25+ million members
- 160+ million publication pages
- 2.3+ billion citations

[Join for free](https://www.researchgate.net/signup.SignUp.html)

Available via license: [CC BY 4.0](https://www.researchgate.net/deref/https%3A%2F%2Fcreativecommons.org%2Flicenses%2Fby%2F4.0%2F)

Content may be subject to copyright.

Design设计, 2023, 8(3), 1222-1232

Published Online September 2023 in Hans. https://www.hanspub.org/journal/design

https://doi.org/10.12677/design.2023.83148

文章引用: 谢小漫, 周杨静. 适老化视阙下医院导视设计策略探究\[J\]. 设计,2023, 8(3): 1222-1232.

DOI: 10.12677/design.2023.83148

适老化视阙下医院导视设计策略探究

谢小漫，周杨静\*

南京林业大学艺术设计学院，江苏南京

收稿日期：2023年7月20日；录用日期：2023年8月31日；发布日期：2023年9月7日

摘要

目的：针对国内人口老龄化，探索老年人产生的独立就医困难现象的原因，找出国内医疗导视系统存在

的漏洞，提出具有参考价值的医院导视设计改善策略。方法：系统分析医院导视系统设计的组成部分以

确认其功能性，结合国内江苏省会南京的医院导视系统现状与国外导视设计案例，模拟医院导视系统面

对老年人所适合的情境，总结老年人就医面临的心理及生理需求，对医院导视设计的适老化改善提出建

设性意见。结论：医院导视设计不应只服务于多数人，更应服务于少数人。提高导视系统设计的效率，

在功能性的基础上与时代主题相结合，加强设计的完整性、舒适性、易辩性与安全性，设计具有艺术性、

创造性，具有人情味的医院导视系统，将极大改善国内老年人就医困难现象，增加老年人就医的幸福感。

关键词

老龄化，医院导视，适老化改造

Research on Design Strategy of Guided

Vision in Hospital for Aging Patients

Xiaoman Xie, Yangjing Zhou\*

School of Art and Design, Nanjing Forestry University, Nanjing Jiangsu

Received: Jul. 20th, 2023; accepted:Aug. 31st, 2023; published: Sep. 7th, 2023

Abstract

Objective: To explore the causes of the difficulty of independent medical care for the elderly in

China, to find out the loopholes in the domestic medical population ageing system, and to propose

some useful strategies for improving the design of hospital vision guidance. Methods: The compo-

nents of the design of hospital guided vision system were systematically analyzed to confirm its

functionality, and the current situation of the hospital guided vision system in Nanjing, capital of

\*通讯作者。

谢小漫

DOI:

10.12677/design.2023.83148 1223

设计

Jiangsu Province, and the cases of foreign guided vision design were combined. This paper simu-

lates the situation that the hospital guidance system is suitable for the elderly, summarizes the

psychological and physiological needs of the elderly, and puts forward some constructive sugges-

tions for the aging improvement of the hospital guidance design. Conclusion: Hospital Vision

Guidance Design should not only serve the majority, but also serve the minority. We should im-

prove the efficiency of the design of the guide system, combine with the theme of the times on the

basis of the function, strengthen the integrity, comfort, argumentation and security of the design.

The design is artistic and creative. The humanistic vision guidance system in hospital will greatly

improve the medical difficulties of the elderly in China and increase their happiness in seeking

medical treatment.

Keywords

Aging, Hospital Vision Guidance, Suitable for Aging Reform

Copyright © 2023 by author(s) and Hans PublishersInc.

This work is licensed under the Creative Commons Attribution International License (CC BY4.0).

http://creativecommons.org/licenses/by/4.0/

1\. 引言

当前国内老年人口比例较往年相比不断扩大，且未来呈现不断增加的趋势\[1\]，但中国社会老年人接

受信息的能力落后，“数字鸿沟”问题较为严重。数字鸿沟即信息化在社会人群中表现出接受程度差异

化，进而产生数字信息、通讯技术、互联网在老年人群中接受落后甚至不能的现象，在高度信息化的导

视系统中，也就出现了“数字鸿沟”\[2\]。中国大多数医院存在导视指向不明确、线上与线下诊疗及互联

网医疗系统界面复杂、交互操作困难、高度智能、医疗流程复杂难懂等问题。医院导视系统作为解决医

患沟通障碍的桥梁，在人口构成复杂、人员流动密集、医疗部门众多的医院中，可以达到“无人而治”，

自发引导老年人就医，改善老年人就医的多重困难，但国内医疗导视设计功能性低下，以至于医院极度

依赖人工，有悖于社会服务在信息化时代与新冠疫情背景下的自发性服务目的，这使医院导视系统设计

的适老化改造迫在眉睫。

2\. 医院导视设计构成

2.1.导视设计的室内外功能分类

医院导视设计的最重要组成之一即标识牌的设计。以室内外不同的功能分区的标识牌共同组成了医

院的导视系统。标识作为导视设计的外在表现形式，常以图形与文字符号的“标记”形式，为患者与医

院建立起沟通的桥梁，其本身是一种沟通的方式，承载着至关重要的引导作用。

室外标识牌是导视设计起引导作用的第一步，包括医院总平面布局的图标，为患者初步构建起医院

大致布局的脑海意识；指向急诊科、门诊部、住院部等明确各部门走向的标识牌设计；交通指示明细的

标识牌；长方体、不规则体、交叉分方向指向的落地分流标识牌等等。

室内标识牌细细划分医院各部分的职能分区，为患者结合自身的医疗需求进行详细的指向功能\[3\]。

如以楼层划分的各楼层科室布局、各楼层的平面图展示以及楼层号牌；挂号、药房、收费处各功能指向

标识牌；洗手间与开水间的标识；医院简介、专家介绍、警示宣传等各个不同分工的标识牌。

不同的尺寸、材料、色彩、形状的标识牌设计形成的传达空间，构成了不同的消费者感官尺度，好

Open Access

谢小漫

DOI:

10.12677/design.2023.83148 1224

设计

的标识牌设计不仅使患者轻松找到其指定的功能地，更为患者构建了舒适的医疗环境，给患者带来安全

感，并建立起对医院的信任与依赖。梅田医院作为典型的医院导视设计的成功案例，其成功在于原研哉

对标识材料、颜色等与医院建立紧密联系的别出心裁的设计，当其设计为患者带来安心，柔和，舒适以

及一目了然的感受时，其患者受众就已经涵盖了大部分人群了。

2.2. 导视设计的四级导向组成

医院导视分为四个级别的导向标识，分别为一级导向、二级导向、三级导向和四级导向标识，一级

导向极其简明，常布置于大厅等醒目的位置，在老龄化日益严重的今日，也要考虑到老年人的文化教育

水平进行设计；二级导向主要是局部区域指示，如各楼层或局部区域牌宇；三级导向常常建立于分岔路，

如提示患者楼道方向；四级导向则以小型标识为主，如警示性标识、宣传性标识等等。这四级导向相辅

相成，共构了清晰的医院视觉导向系统。在老年人就医过程中，统一简洁的四级导向也为老年人带来极

高的便利。

3\. 国内老年人就医障碍

3.1. 老年人身体机能的下降

老年人身体机能的下降主要表现在视力与体力两方面。随着年龄的增长，老人白内障，老花，体力

不支，走路变慢等问题接踵而至。

老年人视觉能力的退化主要表现在视觉灵敏度的感知上。其一，辨色能力的下降。他们难以分辨微

妙的颜色区分，尤其是蓝色，所以在对于蓝绿色的视觉辨别度会明显低于红黄色的对比。其二，眩光的

敏感度上升，老年人的眼角膜随着年龄的增加会有很大程度的损耗，遇到强光时会感到强烈的盲性眩光

以至于无法看清物体，适应强光的灵敏度下降而眩光的灵敏度上升，《高年龄者在环境氛围构建下的起

居室照明需求研究》也用数据表明了老年人眩光灵敏度会随年龄的增加而增加，见表1。

Table 1. Study on the living room lighting needs of the elderly under the construction of environmental atmosphere

表1\. 《高年龄者在环境氛围构建下的起居室照明需求研究》①

年龄段相对视力变化(%) 对眩光敏感度变化(%)

20~40 100 100

50~70 70~35 100~200

体力的下降则主要表现在骨质退化与代谢能力的下降，大部分老年人有行动缓慢，弯腰困难，肌肉

无力，体力不支等问题。

针对老年人身体机能的下降，导视设计的可视化、可辨别化、易懂简洁是老年人就医的关键，老人

视觉的不适会造成视觉的盲区和视觉尺度的错乱，导向不明确的医院导视系统也不利于老年人不支的体

力。

南京作为一线城市，虽然医疗水平走在中国前沿，但大部分医院的导视设计也存在中国大部分医院

共通的弊端，字体堆砌、过小，导视标识不易被察觉，引导指向不明确，引导信息错乱没有规划等问题

\[4\]，典型的有南京省中医院、南京医科大学第一附属医院、江苏省中西结合医院等，此类医院已经形成

稳定的业内口碑与就医人流，建筑设施设备的陈旧破旧不会轻易流失病患，尤其处在人口大量流动的市

区，有常驻病患的情况下，建筑结构不能轻易变动。但陈旧的设施与复杂的道路指标使大部分老年人仍

然难以在拥挤的医院与冗杂庞大的信息系统里从容就医，导视系统在此时的改设则可以改变一部分老年

人就医问题，见图1。

谢小漫

DOI:

10.12677/design.2023.83148 1225

设计

Figure 1. Jiangsu provincial hospital of traditional Chinese medicine

图1\. 江苏省省中医院②

3.2. 老年人“技术赋能”的脱节

大多数老年人存在“技术赋能”脱节的问题\[5\]。千禧年代以来，技术的快速进步带来的不仅是便捷

的生活与愈发智能的社会生活，同时也影响了大批老年人口的生活方式。极少数的老年人接受过高等教

育，他们对于新鲜事物的接受能力较高，对于国内医院导向指示往往能够耐心甄别并独立完成就医。但

绝大多数老年人没有经历过系统的文化教育，他们对新鲜事物，如电子产品，时尚文化等容易产生抵触

心理，对于无处不在的信息导视功能往往表现为缺乏兴趣，转而依赖人工服务的现象\[6\]。简洁易辩是导

视系统需要努力的方向之一。

老年人身体机能的下降导致其辨认信息尤其困难。复杂的导视系统，灵活多变、信息冗乱、操作困

难、人口拥挤是国内医院普遍存在的现象，这直接导致了老年人抗拒就医，或就医必须由子女陪同。医

院针对这一现象衍生了层出不穷的人工服务，但这违背了信息社会的初衷，并弱化了医院导视系统的功

能性。在医院紧急遇到人口众多，排队就诊的情况下，人工不可避免的会产生焦躁、不耐烦等情绪，见

图2。“技术赋能”脱节，就医感到困惑、迷茫的老人，在当下往往容易缺乏安全感，丢失尊严。

Figure 2. The first affiliated hospitalof NanjingMedical University

图2\. 南京医科大学附属第一医院③

信息技术重构了医院诊疗过程，尤其后疫情时代的到来，使得医疗程序更加繁琐复杂，人们就医频

繁依赖电子设备，如自助服务，网上预约、扫码消费、广告绑架等等。医院诊疗变得愈加复杂，老年人

的抗拒就医心理难以消灭。

谢小漫

DOI:

10.12677/design.2023.83148 1226

设计

3.3. 医院导视人文情怀的缺失

中国医院导视系统在设计上更注重医院传统，最终医院诊疗氛围显得冰冷而商业化，在导视系统设

计上出现缺乏人情味，千篇一律的现状。在公立医院，导视与产品更注重实用性，缺少人情味。在老人

医疗的过程中，影响其就医体验感表现在方方面面，好的体验不仅可以给老人感受到家的温暖，带来放

松愉悦等情感，同时也会为医院带来附加价值；不好的体验则使其抗拒就医\[7\]。江苏省中西结合医院设

施陈旧，较好的医疗口碑相对于较差的医疗环境体验形成了强烈的对比，医院入口的地标琐碎；导视色

调区分不明，千篇一律；楼梯间的导视标字体过小，字体连绵对接……见图3，糟糕的导视系统与不易

区分的错乱的环境色给老年人就医带来了极其不好的体验，对设计的轻视导致极度依赖人工，医疗人工

服务不会面面俱到，以人为本的理念也难以贯彻到导视的设计中。

Figure 3. Jiangsu provincial hospital of integrated Chinese and western medicine

图3.江苏省中西结合医院④

有人文主义特征的医院考虑到患者的方方面面：色彩带来的心理舒适度，材质带来的导视传达空间

的心理温度，以及触觉带来的身心安全感等。从光线照明、植物绿化、导视标牌视觉主次、主要信息的

视觉大小等细节入手。其收益的不仅是老年人的就医体验，更是全体消费者的就医体验。南京鼓楼医院

在导视设计上采用了有趣而有用的表现形式，导视指向分明，患者可以轻松根据导视标识走到相应位置，

见图4。根据老年人的夜视能力下降，导视标识牌也适当增加夜晚照明的功能。

Figure 4. Nanjingdrum tower hospital

图4\. 鼓楼医院⑤

4\. 适老化导视设计原则

4.1. 整体感与易辨性

为让老年患者就医快速找到所需位置，导视设计的整体与易辩是关键。整体感即导视传达空间的设

谢小漫

DOI:

10.12677/design.2023.83148 1227

设计

计使患者与所处的环境达和谐相融，在患者被导视标识所指引时，其感官不自觉地会追随色调一致，风

格一致，审美一致，触觉一致，字体一致，数字图形符号一致，系统与系统、物与物之间有联系的个体。

设计统一风格的图标，方向箭头，甚至辅助图形，建立系统的标识概念并在相应的场景主观强调，达到

和谐统一的目的。成熟的导视设计不仅注重统一的设计，在完整和谐的基础上增加个性以达到医院风格

易辩的效果，在导视设计中注入自己地方性医院的人文关怀色彩，或医院文化，营造的这种导视环境使

医院和个体、人和设计之间可以隔空对话\[8\]。在整体性的设计过程中，许多国内设计师随大流，设计的

风格几乎完全一致，同时在设计过程中的折中也会使设计的完整性大打折扣。设计的整体性不仅仅是设

计本身的完整，设计材料与技术、结构的完整，更重要的是在独由的设计风格中维护其整体性，使得在

设计师设计的这个导视空间里，患者能够放松自己并在一个统一的审美环境中达到自然统一，创造出独

特性的导视系统以增加品牌效应。如SLK Klinikun医院的标识设计，见图5。标识牌统一为黑色，标识

小标牌则分为不同色系但统一和谐的色牌，以不同色块的标识指引患者走向不同方向，在错综复杂的部

门中，轻易不会迷失方向。同时偶有绿色标识对应相应的部门墙体，色调的完整性使患者增加参与感，

达成与设计师的对话。SLK的导视设计可以轻易在千篇一律的标识牌的设计中脱颖而出，见图5。有特

点的同时保证了整体感，使患者与医院间产生粘性，极大的彰显了其设计的优势。在统一视觉传达系统

中，老年人也不会轻易的受到纷杂信息的干扰，受到统一的视觉领导。

Figure 5. SLK klinikun hospital

图5\. SKL医院⑥

在信息堆砌，规划不明确的导视设计空间里，简洁、易懂的导视设计不仅使导向更加准确，更能增

加导视层级的功能性。国内许多综合医院标识的设计象征性较弱，复杂而难以辨认。易辨认的标识应是

让人眼前一亮，言简意赅的表达了设计师意图，使患者一目了然的、凭借直觉地被导视指引着。单独文

字或标识的设计不宜过于抽象，要具有较强的辨识度，从而避免识别困难。同时易辩性的导视不仅是字

体大小，箭头指向的易辩，更应是以患者的就医情景设想，涉及到方方面面的易辩性。老年人易于认别

的视域范围可以用成年人的视域范围做设想，在眼球最舒适的视阙范围内，最舒适的导视牌位于地平线

往上80~220cm的位置\[8\]，见图6。假设患者从室外走向室内，结合医院地形走向，室外的标识牌是使

用落地式的标识牌更易明确方向。以有趣生动的形式引导患者走向目的地，考虑到老年人的视力延展性，

可以结合医院功能的分区为导视进行配色，并为患者设计有趣的视觉引导线，引得老年患者轻松自然

的由一个阶段转向另外一个阶段，打造设计师与使用者共同就医的体验效果，营造有趣生动的路线体

验。

谢小漫

DOI:

10.12677/design.2023.83148 1228

设计

Figure 6.Guidance plate and eyeball viewing range

图6\. 导视牌与眼球视阙范围⑦

4.2.安全感与舒适性

为了给老人带来舒适的就医体验，导视系统可以从老人心理入手。如夜晚夜功能的标识灯牌设计，

带给老人视觉上温暖的落差，可以极大的增加老人医疗就诊的舒适感；医院导视设计上的空间与距离

的体贴，导视摆放在适宜的位置也会增加老人的好感度及老人生理上的安全感。为老人设计适应的高

度的标牌指示，使其在识别标牌时轻松自然；在不同的功能分区中，使用放大的数字增加视觉集中度，

使其寻找方向时不至于慌乱茫然；坐轮椅双腿不便的老人，采用针对性的导视设计以增加其导视的可

阅读性，如跟据《美国残疾人法案》的标准，双腿不便坐在轮椅上，手臂向上最高摆动距离为122cm，

导视标识指示离地面至少38 cm\[9\]；在标识的设计中，尽量采用直观的图形与数字元素，图像数字与

文字的结合才能增强老年人的记忆力度，在合适的尺寸适当的放大或缩小某些字体\[10\]，使设计更具

功能性与指向性，老人的就医也会更具安全感；导视内容设计应使用积极元素，体贴到老人的就医情

绪，见图7。

Figure 7. Visual graphics and figures

图7\. 直观的图形与数字⑧

谢小漫

DOI:

10.12677/design.2023.83148 1229

设计

4.3.材料与技术

经过反消费设计运动对人们审美即价值观的熏陶，设计的色彩以及趣味性已不再是打动消费者唯一

衡量的标准，设计作品的功能性，创造性，其材料与技术是也当前设计的关键。在室内环境中，人们更

多注重的是设计的整体感受，在医院导视设计则体现在导视整体传感度上，室内传导系统材料的温度，

触觉，肌理，视觉心理都涵盖在内，不同的材料带来不一样的传感温度，产生不一样的心理感受。例如，

原研哉梅田医院导视系统的材质使用的都是纯白洁净的亚麻布，拥有圆润型外观的导视牌常由这样的材

质包裹而成，看起来犹如柔软的云朵，舒适的背枕，呈现出完全的放松状态。

给到国内导视系统设计的启示，设计师要注意导视系统材料的传感温度，导视牌，导视的尺度，导

视的位置。避免锋利尖锐的材料，材料的视觉传感上要避免强光的直射，医院内的任何位置都可以在导

视设计的范畴内。以老人为第一视角，室内墙面导视的高度要适应坐轮椅的老人，导视信息的高度在应

在700~1700毫米的范围内；不同的导视信息之间应把握到十米到三十米的距离，同时保持连续性。医院

导视系统适老化工作不仅要考虑材料的选择，技术人性化的加持，也需要关注老年人的身心健康，与心

理医生，跨专业的综合性人才共同营造舒适的就医环境，改善老年人抗拒就医的现状。

5\. 适老化导视设计设计策略

5.1.医院导视设计的色彩探究

医院导视系统的不同色彩可以为老年患者带来不同的体验感受，结合医院本身的设计风格，自然绿色主

题、清浅的蓝色主题、温暖的木色花香主题等，在标识牌的颜色上追随医院主题风格\[11\]，色调和谐统一。

考虑到老年人就医情绪，可以增加医院的空间形象和情感，空间的识别性，以增加医院的人文关怀情感。

老人身体机能的下降最直接导致的是色彩灵敏度的下降，导视标识中图形的联想、文字的识别和标识含

义的理解，都要基于人的认知才能具有识别性，具有导视的使用价值。低效果甚至无效的导视系统设计没有

考虑老人的实际身体机能，仅将导视直观带入为“显示”，进而忽视其指引作用。老人辨色能力的下降使其

对黄、红色系具有更高的视觉灵敏度，在导视应用中，关键的导视信息可以使用黄色或红色代替。对蓝绿色

辨别灵敏度的下降则可以运用在统一的导视功能分区。老人眩光敏感度的上升使其无法识别强烈光照的设

计。导视系统在设计的过程中则不仅要考虑色彩的分配，更须考虑不同色彩的传递媒介\[12\]。以原研哉的梅

田医院为例，统一的米白色搭配不仅给人带来心里的舒适性，更统一了整个医院的风格，传递了爱、包容、

平静、温暖的信息。没有电子的强光照射完全以色彩、材质为切入，这样的导视设计无疑是成功的。

5.2.医院导视设计的人文关怀

人文关怀是医院导视设计中不可或缺的一部分，导视设计要尊重人的人格和价值，在医院导视设计

中要考虑到不同文化程度对导视设计识别的需求，考虑到社区内具有视觉障碍或听觉障碍的人群对导视

的需求，其中大部分是老年人。医院导视设计中要重视导视标识图形的含义是否通俗易懂，导视箭头的

方向位置是否容易识别等问题，医院导视整体感受，从生理到心理的人文关怀，产生美的设计，是决定

医院导视成功与否的关键。

产生情感与美的设计需要将审美与功能相统一，使导视设计与老人在精神世界达到共鸣。对医院产

生情感需注重导视设计的细节关怀，如导视灯牌舒适、导视色彩温暖等是医院内在的精神力量。美的设

计则是对外的视觉感觉，是人们初次的、直观的印象\[9\]，可在导视设计元素上增贴治愈性元素以产生情

感与美的设计，如植物，花卉等清新的自然元素。导视系统的适老化也要考虑到老人的视听觉，在标识

设计上可以采用触觉突起的设计，见图8。某些特殊的位置甚至可以考虑声音标识，以达到设计不孤立

谢小漫

DOI:

10.12677/design.2023.83148 1230

设计

个体的目的，包容而平等，开放有温度。在导视标牌的特殊空间，用数字符号起强调作用，将电子材质

作为标识材质时，电子光线考虑老人视觉承受能力，温和易区分的光线为老年患者带来轻松愉悦的感受，

让老人直面感受到医院的关怀与爱\[13\]。

Figure 8.The design of haptic protrusions

图8.触觉突起的设计⑨

南京泰康仙林鼓楼医院，见图9，作为南京新设立医院在导视设计上注重了人文关怀，环境干净整

洁，人工挂号缴费处装饰蝴蝶兰，绿色植被与浅绿色粉墙相适应，大厅摆设钢琴与温暖舒适休闲椅，人

工窗口导视字体大小分明，地标字体功能放大，色调区分，是优秀导视设计的典范，有着极好的就医体

验，对老年人就医友好。

Figure 9. Taikang xianlin drum tower hospital

图9\. 泰康仙林鼓楼楼院⑩

国外典型的例子有墨尔本皇家儿童医院的视觉导向系统设计，在该医院中明显感受到功能性逐步被

弱化，艺术的感受逐渐被强调，情感化设计是医院导视设计的重点，功能性虽然要强调，但导视空间的

艺术性、创造性，整体营造下的具有温度的情感化导视设计系统，具有抚慰老年人就医心情的艺术导向，

也是导视系统重点研究的方向。

5.3.医院导视设计的智能化

智能化设计与老年人之间存在壁垒，但我国导视设计必定顺应时代的发展趋势，并完善导视智能化

谢小漫

DOI:

10.12677/design.2023.83148 1231

设计

设计完善软件设施，从而提高信息的传递速度。老年人数据鸿沟并非不能解决，除了硬件软件的改善，

应从各方面入手，他们的认知不仅基于受教育的程度，还在于相关领域的了解；文化程度不仅是他们的

受教育程度，还在于他们的学习程度。大多数老年人迫于时代导致文化程度低，身体机能的下降导致学

习能力减弱，理解能力低。所以基于人文关怀的设计理念，导视设计要尊重人的人格和价值，在医院导

视设计中要考虑到不同文化程度的人对导视设计识别的需求。当今人工智能涉及到各方面，互联网信息

已然引起负荷，不可避免地产生了人与人之间信息的差别与隔离，尤其体现在老年人与年轻人的信息差

\[14\]。技术的控制和资本的力量时刻都在左右人们在互联网上可以接触到的信息。对于老年人自身文化水

平受限所导致的沟通障碍问题，人机的无障碍沟通可以作为切入点引入导视设计当中以解决这一问题。

在科技进步的大趋势下，后疫情时代的到来的社会背景下，人们对高度智能化设备的依赖一定程度

减轻了人与人的沟通障碍，电子交互，人工智能，AR、VR以及元宇宙概念的提出等为现实世界带来了

无限可能性\[15\]。加之后疫情时代重视人与人之间的距离把握，在不依赖人工的前提下，智能化设计也可

以提高人机互动，拉近人与医院的距离感，面对特殊人群如老年人群、具有视觉障碍或听觉障碍的人群，

快速的降低其就医难度并使其对人工的依赖转移到对导视的需求上，这是智能化的优势。

导视系统的智能化要以完善可适用的信息基础为目标，以图文形式传递信息，增加专业技术人员的

参与，尝试多种类型的导视牌设计，以老年人达到无障碍沟通为可利用标准。语音人工智能也是导视设

计专业性赋能的方式之一。它摆脱了老年人的识别障碍，以最直接的方式与老人达成无障碍沟通。除了

语音导向设计，易辩查询信息，实时播报功能等信息化智能导向也应在医院的节点处设计补充\[16\]。医院

导视适老化应考虑到避开硬件软件的缺陷，做到有效沟通，即“消除数字鸿沟，技术赋权的关键问题是

要有一套充足的、可以利用的信息基础设施，可以使所有人有机会通过口头和书面并最终通过多媒体(宽

带服务)获得相关信息和通信技术”\[17\]。

智能化设计与老年人之间存在的壁垒，除了技术的加持，面对老年人技术赋能的脱节问题，根本上

应从社会层面，心理层面入手，加大数字化信息普及性，通过有效宣传降低老年人接触全新且易变事务

的排斥心态。除此之外，医院导视设计也可以融入人工智能。人工智能具有人工不具备的优势。其一，

人工智能可以快速的解决工作量庞大的错综复杂的问题；其二，人工智能可以不知疲倦的工作，没有工

作疲惫期以至于时刻高效的解决问题；其三，人工智能具备人类不具备的计算能力，可以短期内运算高

端的数据。将人工智能引入到导视系统设计当中，不仅可以降低人工成本，也可以降低沟通难度。智能

化设计是未来导视设计发展趋势之一，创新的方式带来全新的变革，综合的改善与创新极可能为适老化

院导视的设计创造新局面。

6\. 结论

只有立足于老年人视角才可以做出真正的适老化导视设计。导视设计作为交叉学科，除了表现在对

材料技术的重视，人文关怀也是不可分割的一部分，为使设计与设计对象无障碍沟通，需要深入的了解

老年人的身心状态，为老年人创造足够舒适的就医环境。在未来中国的医疗系统的构建中，具有人文关

怀的导视系统设计必定能为医疗空间带来新体验，散发新鲜活力，为医院创造前所未有的附加价值。

注释

①表1来源：作者自绘

②图1来源：网页引用，https://www.mafengwo.cn/sales/9242705.html

③图2来源：作者自摄

④图3来源：作者自摄

谢小漫

DOI:

10.12677/design.2023.83148 1232

设计

⑤图4来源：作者自摄

⑥图5来源：来自谷德设计网

⑦图6来源：作者自绘

⑧图7来源：来自谷德设计网

⑨图8来源：来自谷德设计网

⑩图9来源：作者自摄

参考文献

\[1\]白雪锋, 郑婕, 周成玲, 王浩. 基于Citespace知识图谱的中国适老化研究历程与趋势分析\[J\]. 中国老年学杂志,

2021, 41(20): 4561-4566\.

\[2\]杨晨晨, 吴学林. 老年人数字鸿沟的问题及解决办法分析\[J\]. 科技风, 2023(21): 148-150\.

https://doi.org/10.19392/j.cnki.1671-7341.202321050

\[3\]战宁. 童话般的视觉体验——墨尔本皇家儿童医院导视系统设计探析\[J\]. 装饰, 2014(4): 139-140\.

\[4\]郭丽萍, 丛焘. 城市发展中公共景观空间适老化设计研究\[J\]. 现代物业(中旬刊), 2020(6): 70-71\.

\[5\]段莉, 高云峰, 刘亚莉, 田建丽. 乡镇社区老年人居家环境适老化水平的调查研究\[J\]. 护理学杂志, 2019, 34(9):

87-90.

\[6\]王天赋, 王睿. 养老设施适老化产品满意度多层次模糊综合评价\[J\]. 包装工程, 2022, 43(12): 192-198.

\[7\]王杰. 数字产品适老化评估体系研究\[J\]. 老龄科学研究, 2022, 10(4): 9-27\.

\[8\]郭铁军, 王春晓, 高渤. 文化地标导视设计研究\[J\]. 包装工程, 2021, 42(2): 180-185, 194.

\[9\]邓俊, 汤迪欣. 基于人机工程学的城市公共导视设计研究\[J\].包装工程, 2020, 41(24): 46-52, 78\.

\[10\]刘梁. 环境心理学语境下的数字化医院导视系统研究\[J\]. 包装工程, 2020, 41(14): 272-277, 338.

\[11\]李战鹏. 基于色彩视觉心理特征的医院室内设计及导视设计探究\[J\]. 设计, 2020, 33(8): 111-113\.

\[12\]王聪, 朱华. 妇幼保健院视觉导视系统中的情感化设计研究\[J\]. 包装工程, 2020, 41(8): 258-262.

\[13\]陈佳音. 马斯洛理论视角下的老年公寓公共空间环境设计\[J\].文化产业, 2022(10): 157-159.

\[14\]何铨, 张湘笛. 老年人数字鸿沟的影响因素及社会融合策略\[J\]. 浙江工业大学学报(社会科学版), 2017, 16(4):

437-441.

\[15\]高丹阳. 老年人“数字鸿沟”弥合路径探析\[J\]. 新闻研究导刊, 2022, 13(4): 127-129\.

\[16\]徐越, 韵卓敏, 王婧媛, 景荣杰, 黄黎明, 沈勤. 智能化背景下, 老年人数字鸿沟的影响因素及其形成过程分析

\[J\]. 智能计算机与应用, 2020, 10(2): 75-82\.

\[17\]王娟, 张劲松. 数字鸿沟: 人工智能嵌入社会生活对老年人的影响及其治理\[J\]. 湖南社会科学, 2021(5): 123-130\.

ResearchGate has not been able to resolve any citations for this publication.

[Response Measures and Research on the Demand Difference of Financial Products for the Middle-Aged and the Elderly](https://www.researchgate.net/publication/365831249_Response_Measures_and_Research_on_the_Demand_Difference_of_Financial_Products_for_the_Middle-Aged_and_the_Elderly)

Article

Full-text available

- Jan 2022

- [钰欣 王](https://www.researchgate.net/scientific-contributions/yuxin-wang-2237156741)

[View](https://www.researchgate.net/publication/365831249_Response_Measures_and_Research_on_the_Demand_Difference_of_Financial_Products_for_the_Middle-Aged_and_the_Elderly)

[计算机数据挖掘技术的开发及其应用](https://www.researchgate.net/publication/330494545_jisuanjishujuwajuejishudekaifajiqiyingyong)

Article

Full-text available

- Jan 2019

- [建科 徐](https://www.researchgate.net/scientific-contributions/jianke-xu-2152393431)
- [洲 颜](https://www.researchgate.net/scientific-contributions/zhou-yan-2152382953)

我国在计算机数据挖掘技术的应用时间还不是很长，还没有得到有效的发展，但是其应用范围的扩增却是非常迅 速，因为其本身具有较高的实用性。在计算机的功能的不断增加，一些统计学理论也融入其中，在这种情况下出现了 数据挖掘技术，在使用云计算，云存储的今天。数据挖掘技术不断进步，为人们解决众多问题，在计算机网络中查找 筛选出人们想要知道的信息，这就是数据挖掘。因此主要分析了计算机数据挖掘技术的应用前景，并对相关技术进行 介绍。

[View](https://www.researchgate.net/publication/330494545_jisuanjishujuwajuejishudekaifajiqiyingyong)

Show abstract

- Jan 2021
- 4561-4566

- 郑婕 白雪锋
- 王浩 周成玲
- Citespace

白雪锋, 郑婕, 周成玲, 王浩. 基于 Citespace 知识图谱的中国适老化研究历程与趋势分析\[J\]. 中国老年学杂志,
2021, 41(20): 4561-4566.

- Jan 2014
- 139-140

- 战宁
- 童话般的视觉体验--墨尔本皇家儿童医院导视系统设计探析

战宁. 童话般的视觉体验--墨尔本皇家儿童医院导视系统设计探析\[J\]. 装饰, 2014(4): 139-140.

**We and our partners use cookies** ✕

By using this site, you consent to the processing of your personal data, the storing of cookies on your device, and the use of similar technologies for personalization, ads, analytics, etc. For more information or to opt out, see our [Privacy Policy](https://www.researchgate.net/privacy-policy)

### 来源 2: 适老化视阙下医院导视设计策略探究

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

### 来源 3: 友善设计——老年医院导视系统的适老化设计实践探究-维普期刊 中文期刊服务平台

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

### 来源 4: [PDF] 积极老龄化视角下社区公共导视系统适老化设计研究

- URL: https://pdf.hanspub.org/ar_3141153.pdf
- 精读方法：firecrawl-scrape

积极老龄化视角下社区公共导视系统适老化设计研究

朱知秋，范松华

南通大学艺术学院，江苏 南通

收稿日期：2026年1月26日；录用日期：2026年3月18日；发布日期：2026年3月26日

摘 要

随着我国人口老龄化进程加快，积极老龄化已成为国家应对老龄问题的核心理念。社区公共导视系统作为老年群体参与社区生活的“无声向导”，其设计合理性直接影响老年人的社区融入度、出行安全性与生活幸福感。本文基于积极老龄化“科学、主动、有为”的核心内涵，结合老年群体生理心理特征与适老化设计标准，分析当前社区公共导视系统存在的视觉、认知、情感、技术适配问题，提出兼具功能性、多元性、文化性与智能性的设计策略，为构建老年友好型社区导视环境、助力积极老龄化落地提供理论参考与实践路径。

积极老龄化，社区公共空间，导视系统，适老化设计

Abstract

Research on Age-Friendly Design of
Community Public Signage System from the
Perspective of Active Aging

With the acceleration of China’s population aging process, active aging has become the core concept
for the country to address aging issues. As a “silent guide” for the elderly to participate in community

文章引用: 朱知秋, 范松华. 积极老龄化视角下社区公共导视系统适老化设计研究\[J\]. 老龄化研究, 2026, 13(3): 890-
896\. DOI: 10.12677/ar.2026.133110

* * *

朱知秋，范松华

**life, the design rationality of community public signage systems directly affects the elderly’s commu-** **nity integration, travel safety, and sense of happiness. Based on the core connotation of “scientific,** **proactive, and productive” in active aging, this paper combines the physiological and psychological** **characteristics of the elderly with age-friendly design standards to analyze the existing visual, cog-** **nitive, emotional, and technical adaptation issues in current community public signage systems. It** **proposes design strategies that are functional, diverse, cultural, and intelligent, providing theoret-** **ical references and practical paths for building an elderly-friendly community signage environment** **and facilitating the implementation of active aging.**

# Keywords

## Active Aging, Community Public Space, Signage System, Aging-Friendly Design

Copyright © 2026 by author(s) and Hans Publishers Inc. This work is licensed under the Creative Commons Attribution International License (CC BY 4.0). [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/) Open Access

# 1\. 引言

中共中央、国务院先后印发《关于加强新时代老龄工作的意见》《“十四五”国家老龄事业发展和养 老服务体系规划》等政策文件，明确提出将积极老龄观、健康老龄化理念全面融入经济社会发展全过程， 推动构建老年友好型社会。此外，2025 年 12 月，民政部等八部门联合发布《关于培育养老服务经营主体 促进银发经济发展的若干措施》，进一步细化落实路径，明确提出完善社区无障碍设施与智能养老服务 供给，推动社区环境适老化升级。 社区是老年群体生活核心场景，公共导视系统作为空间信息传递载体，对保障老人独立出行、参与 社交至关重要。然而，当前多数社区导视系统仍以通用人群为设计核心，忽视老年群体视觉衰退等生理 心理特征，存在标识模糊、可读性差、布局不合理等问题，制约其社区参与积极性。在此背景下，基于积 极老龄化视域优化社区公共导视系统设计，具有重要的现实意义。

# 2\. 相关概述

2.1. 积极老龄化 1990 年，世界卫生组织提出“健康老龄化”发展战略，又于 2002 年在“健康老龄化”基础上发布 《积极应对人口老龄化政策框架》，提出“积极老龄化”观念及其政策建议\[1\]。积极老龄化区别于强调 “养老负担”的消极老龄观，其核心是将老龄化视为社会进步的标志，通过政策引导、环境优化与社会 支持，让老年人充分发挥自身价值，实现健康、参与、保障的有机统一。

## 2.2. 社区公共导视系统

社区公共导视系统，是指应用于居民社区内部的一套系统化、标准化的视觉体系，主要涵盖标识牌、 区域地图、信息公示栏、安全警示标识等多元载体。其核心目的是通过清晰的视觉符号与文字信息，实 现引导、说明、提示的功能，帮助居民和访客在社区复杂空间中高效、安全、舒适地定位与移动。同时， 该系统并非单纯的功能性设施，还可通过融入社区文化符号、地域特色元素，优化空间视觉秩序，辅助 社区日常管理，进一步增强居民的身份认同感与归属感，营造和谐有序的社区文化氛围，是提升社区空 间治理效能与人文建设水平的重要支撑。

DOI: 10.12677/ar.2026.133110 老龄化研究

* * *

朱知秋，范松华

## 2.3. 适老化设计

适老化设计是一种充分考虑到老年群体各种需求的人性化设计理念，在住宅或在公共建筑如商场、 医院、学校等，从老年视角出发，以老年群体为本，针对老人的生理功能、心理特征或行动特点等对其 进行合理的设计\[2\]。在设计过程中，遵循“通用性、安全性、舒适性、情感性”原则，对产品、环境与 服务进行优化，既满足老年群体的特殊需求，又兼顾其他群体使用体验的设计理念，避免“过度特殊化” 导致的排斥感。

# 3\. 积极老龄化视角下社区公共导视系统设计现状

3.1. 现状概述 当前我国社区导视系统建设在积极老龄化视角下呈现“新旧分化”特征(图 1)：新建社区逐步引入适 老化设计理念，部分配备智能导视设备；而老旧小区受历史条件限制，导视系统普遍存在设施陈旧、设 计不合理等问题。整体来看，社区公共导视系统改造仍处于碎片化阶段，缺乏系统性规划。多数项目仅 注重标识更新，未充分关注老年群体的认知习惯与情感需求。 政策层面，多地已将导视系统适老化改造纳入老旧小区更新计划。例如，在老年人口比例较高的岭 南传统村落明经村，原有导视系统存在标识模糊、功能分区不明、墙面老旧等问题。广州大学美术与设 计学院团队基于积极老龄化理念对该村进行优化改造。此外，2025 年 4 月实施的《城市公共设施适老化 设施服务要求与评价》国家标准，进一步明确了导视系统在字体、色彩、照明等方面的适老化指标，为 系统化改造提供了依据。 尽管如此，我国社区导视系统的适老化水平仍参差不齐，尤其在老旧社区，现有系统难以满足积极 老龄化的多元需求。图源：作者自绘。

**Figure 1. Current situation of “new and old differentiation”**

图 1\. “新旧分化”现状

## 3.2. 核心问题具体分析

1. 视觉设计适配性不足：老年群体普遍存在视力下降、色觉分辨能力衰减、对比度感知能力弱化等问题。然而，现有社区导视系统设计往往未充分考虑以上因素，存在字体规格偏小、色彩搭配缺乏辨识 度、材质易产生反光干扰等缺陷。例如，部分社区采用浅色文字搭配浅色调背景的设计方案，视觉对比 度不足；标识材质多选用光滑塑料，夜间受光线照射时易产生强反光等直接干扰老年群体的视觉识别， 大幅降低导视信息的可及性。

2. 认知信息设计复杂：认知障碍是影响老年人出行效率的主要因素，具体表现为因生理机能衰退，
   导致对复杂的信息标识、平面地图辨识的理解产生困难\[3\]。但当前社区导视标识都存在符号设计繁琐、 文本表述冗余、信息排布无序等问题。部分标识过度追求“一站式信息全覆盖”，在有限的版面内堆砌 大量非必要信息，同时未通过层级划分等方式突出核心内容，导致老年群体在信息接收过程中难以快速

DOI: 10.12677/ar.2026.133110 老龄化研究

* * *

朱知秋，范松华

筛选出关键信息，进而出现信息误读、漏读等问题。

3. 情感关怀与文化赋能不足：对于老年群体而言，社区不仅是基础的居住空间，更是情感归属与文化传承的载体。但当前社区导视系统多采用标准化、同质化的工业风设计，过度侧重导向导航的基础功 能，忽视了与老年群体情感需求、社区文化特质相契合的设计表达。例如，老旧社区的导视标识未融入 地域建筑元素，新建社区的标识缺乏温度感，难以引发老年群体的情感共鸣。

4. 智能技术应用失衡与脱离现实：部分新建社区引入智能导视设备，但普遍存在“技术中心主义”
   倾向，忽视老年群体的技术接受能力与使用习惯。从实际使用场景来看，这些设备多存在语音播报音量 不足、操作流程繁琐等特征，在一定程度上提高了老年群体的使用门槛。同时，部分设计方一味推崇昂 贵的智能终端，忽视二维码、NFC 标签等低成本技术方案的应用，导致智能导视系统的落地性与可持续 性较差，部分设备因维护不当沦为“摆设”。

# 4\. 积极老龄化视角下社区公共导视系统适老化设计原则

4.1. 受众平衡原则 适老化设计并非“特殊化设计”，其核心要义在于兼顾老年群体与其他群体的共同使用需求，实现 “全龄友好”的设计目标。若设计走向过度特殊化，不仅会增加设计与落地实施的成本，还可能通过视 觉符号、功能划分等形成隐性的年龄标签，诱发老年群体的排斥心理从而违背了适老化设计所秉持的人 文关怀初衷。因此，社区导视系统的适老化设计，在满足老年人视觉辨识、认知理解等特殊需求的基础 上，还需避免因设计过度差异化而引发的排斥效应。

## 4.2. 信息认知适配原则

基于老年群体信息认知机能衰退问题，优化导视系统的信息呈现形式。视觉层面，应采用高饱和度 对比色提升辨识度，选用无衬线字体减少视觉干扰，并合理增大标识尺寸与字符之间间距；认知层面， 简化信息内容，统一标识编码逻辑与视觉符号规范，从源头降低老年群体的信息处理成本。同时，可以 通过重复提示、路径强化等方式，帮助老年人建立空间认知，降低记忆负担。

## 4.3. 情感关怀原则

结合情感层次理论，导视语言应避免使用“老人”“残障”等带有歧视色彩的词汇，而是采用更中性 和积极的表达\[4\]。设计层面，可通过色彩、材质与文化元素传递温暖且安全的暗示，这样的设计目标不 仅是减轻由老年居民使用导视系统引起的心理负担，更是为了提升老年群体的心理福祉，增强他们对导 视系统的接受度和满意度，从而促进他们享受社区生活带来的乐趣和便利，进一步提升社区活力\[5\]。

## 4.4. 智能技术简化原则

智能技术在社区老年服务中的应用需严格遵守“简单易用、安全可靠”的核心原则，充分适配老年 群体的认知规律与实际操作能力，避免因技术操作复杂、界面设计繁琐而增加老年群体的使用门槛。同 时，需结合社区现有经济发展水平与管理服务能力，综合考量智能技术的成本投入、日常维护难度及抗 干扰性能，优先选取低成本、易维护、高适配性的技术实施方案，兼顾技术应用的实用性与经济性，最 终实现智能技术在社区老年服务场景中的可持续落地与长效应用。

# 5\. 积极老龄化视角下社区公共导视系统适老化设计具体策略

5.1. 视觉层：适配老年人生理特征

1. 色彩设计：色彩心理学研究表明，不同年龄阶段会产生不同的色彩心理，老年人的色彩意识不再
   DOI: 10.12677/ar.2026.133110 老龄化研究

* * *

像青年人那样强烈，对于颜色的敏感度要较年轻人 25%~40% \[6\]。因此，采用高对比度、低饱和度的色彩搭配方案，如深灰色文字与米黄色背景组合，避免纯红、亮蓝等高饱和度色彩，从源头减少老年群体视觉疲劳的产生。同时，针对色觉减退群体的视觉特性，导视系统设计应避免使用色相相近的色彩区分信息，优先通过色彩明度差异强化信息辨识度，从而确保色觉障碍老年人能清晰区分核心内容。

2. 字体与符号设计：老年用户视觉感知能力衰退，过小的字体、不恰当的字形、过密的行距容易导致信息识别困难\[7\]。因此社区导视系统设计应严格遵循《城市公共设施适老化设施服务要求与评价》的相关标准。首先，字体选用清晰易读的无衬线字体，字号需不小于 36 号，重要标识的字号可提升至 48 号以上，同时将字符间距与行间距适当增大，适配老年群体视觉聚焦能力较弱的特点。其次，符号设计应遵循“简洁化、具象化”原则，优先采用老年群体熟悉的生活场景类符号替代抽象图形，降低认知成本；
   对于复杂信息，可采用“图文结合”的呈现形式，以图形辅助文字解读，从而降低老年群体对纯文字信息的理解难度。

3. 布局与材质：标识的布局设计需要契合老年群体人体工学特征，标识安装高度控制在 1.2~1.5 米范围内，确保老年群体可平视查看，避免弯腰或仰头带来的行动不便与视觉不适。在材质选择上，主体应选取防滑、耐磨、环保的复合型材料，边缘需进行圆角处理，规避尖锐边角引发的磕碰伤害风险。例如 ，日 本 Abeyama 养老院聚焦高龄、行动不便老年人的需求，打造了兼具功能性与人文关怀的导视系统。在细节设计上，房间标牌采用陶土与木材制作，倾斜式角度适配轮椅使用者与弯腰困难的老年人，木质肌理搭配柔和光源，营造温馨氛围(图 2)。

图源： [http://signgoood.com/case/show/510](http://signgoood.com/case/show/510)

Figure 2. Signage system of Abeyama nursing home in Japan
图 2\. 日本 Abeyama 养老院导视系统

2. 引导健康生活：老年人喜欢静态、低强度和高强度的运动，其中散步、静坐和亲子活动最受到欢迎\[9\]。因此结合社区既有空间布局特征，规划环形健康步行步道体系。在步道配套导视标识中，清晰地标注步道全程长度、休憩点与健身设施的具体方位，并在步道沿线途中有序设置“步数提示”“心率提示”等健康指引标识，引导老年群体开展与自身适配的步行锻炼。同时，在步道周边的休憩点、饮水点、卫生间等便民服务区域，设置醒目且易辨识的导视标识，以便于老年群体在锻炼途中解决基本生理

图 2\. 日本 Abeyama 养老院导视系统

5.2. 认知层：降低信息处理成本

* * *

朱知秋，范松华

需求。

3. 完善安全保障：将应急通道、消防设施、社区卫生站、警务室等安全保障类信息作为导视核心内容，提升其视觉与信息优先级。同时沿用“多节点、短距离递进式”指引模式，规避因长距离路径标识缺 失引发的迷路、走失等安全隐患。结合老年群体记忆力衰退的生理特征，在标识设计中增设“当前位置 目标位置”的简易空间示意图，标注大树、雕塑等易辨识的自然与人工地标参照物，借助具象化参照 体系降低老年群体的空间认知负荷，确保老年人可便捷到达各个功能区域，从而营造安全、友好的社区 环境\[10\]。

## 5.3. 情感层：构建人文关怀体验

1. 文化元素融入：结合社区历史文化与老年群体的审美偏好，在导视标识设计中融入传统纹样、地域建筑剪影等元素，进一步深化老年群体对社区文化的理解和认同，同时促使导视系统兼具功能性与人 文关怀。以老旧小区改造场景为例，可提取原有建筑的典型构造、风貌特征融入标识造型，通过视觉符 号唤醒老年群体的社区记忆，强化身份认同与情感归属感。

2. 社区参与式设计：让老年群体从“设计接受者”转变为“设计参与者”。通过居民议事会、老年群体专项访谈等形式，系统收集老年群体对导视标识的位置、内容、形态、辨识度的需求与建议，并将 其贯穿于导视系统的设计、优化全流程。例如，某社区通过访谈发现老年人习惯以“老槐树”“健身器材 区”为参照物，据此调整标识布设位置，在标识中明确标注这些参照物，避免专业化设计与实际使用场 景脱节。 导视系统应该鼓励并促进老年居民的社交活动，通过提供通往社区中心、活动场所和休闲区的清晰 指引，以及展示社区活动信息，来激励老年居民参与社区生活，从而实现社区内的社交互动和情感支持， 这对促进老年居民的社会参与和心理健康至关重要。

## 5.4. 智能层：简化技术并降低成本

1. 简易智能导视设备：对于社区核心区域布设的智能导视终端选用简易化智能终端，该设备需摒弃高端触控屏、人脸识别等非必要功能，仅保留语音播报、触控导览、放大显示等核心功能。同时，针对老 年人生理感官特点进行优化交互体验：采用适中音量、缓慢语速、清晰音色的语音提示适配听觉感知变 化\[11\]。界面采用放大字体设计，适配视觉灵敏度变化。

2. 低成本智能技术：对于社区普通区域，优先采用二维码、NFC 标签等低成本、易维护、高适配的技术方案，替代昂贵的智能终端，实现智能导视的全覆盖，单台设备成本控制在 10 元以内，大幅降低改 造与维护成本。例如，在传统导视标识牌的空白区域印制高清防刮二维码，扫码后可查看社区电子导览 图、设施信息、社区活动通知、健康养生知识等内容，支持语音播报功能，适配老年人的使用习惯。

3. 安全备份与技术适配：为智能导视设备配置备用电源模块，保障突发停电场景下设备正常运行。与此同时，考虑到老年群体技术接受度的差异性，采用“智能 \+ 传统”并行模式，提供多元化选择：既 部署自动化语音导视、触控导视等智能服务，也保留传统指引服务，具备一定技术操作能力与依赖传统 服务的老年群体需求，实现全年龄段、全能力层次的服务覆盖。

# 6\. 结语

社区公共导视系统的适老化设计，是积极老龄化理念从理论走向实践的重要具象载体。其设计的科 学性直接关乎老年群体的出行安全、自主活动能力及生活幸福感，更是保障老年人平等享有公共服务、 促进社会融入的重要环节。未来，需构建社区治理主体、设计专业力量与老年群体的协同联动机制，持

DOI: 10.12677/ar.2026.133110 老龄化研究

* * *

续迭代导视系统，共同打造安全、便捷、有温度的社区环境。

参考文献

\[1\] 刘智勇. 积极应对人口老龄化国家战略: 观念更新、任务定位、实现途径\[J\]. 学习论坛, 2023(1): 81-88.
\[2\] 张笑. 适老化导视系统设计研究与实践\[D\]: \[硕士学位论文\]. 兰州: 西北师范大学, 2025.
\[3\] 刘键, 许泽君, 赵健磊, 等. 老龄化背景下地铁智能导视系统的服务设计\[J\]. 包装工程, 2018, 39(14): 87-94.
\[4\] 周晓丽. 城市公园适老化标识设计研究\[J\]. 丝网印刷, 2025(18): 103-105.
\[5\] 杨静, 吴泽秋. 情感层次理论辅助老旧小区导视系统适老化改造\[J\]. 包装工程, 2025, 46(16): 457-471+532.
\[6\] 赵浩凯. 友善设计óó老年医院导视系统的适老化设计实践探究\[J\]. 艺术与设计(理论), 2020, 2(1): 74-76.
\[7\] 张译匀, 杜洪竹. 基于认知负荷理论的养老机构海报适老化设计研究\[J\]. 工业设计, 2025(11): 73-76.
\[8\] 崔颖. 适老化视阈下我国社区智慧养老服务的数字设计与应用研究\[D\]: \[硕士学位论文\]. 南京: 南京邮电大学,
2024\.
\[9\] 甘伟, 李绳彪, 金天. 积极老龄化视角下的老旧社区运动空间设计策略研究\[J\]. 设计, 2024, 37(9): 68-71.
\[10\] 刘泽萱, 田原. 北京市老旧社区公共空间适老化更新策略研究\[J\]. 城市建筑空间, 2026, 33(1): 73-75.
\[11\] 万云青, 周雅轩. 认知衰退老年人医疗 App 界面适老化设计研究\[J\]. 工业设计, 2025(10): 103-106.

### 来源 5: A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness

- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9656047/
- 精读方法：firecrawl-scrape

Checking your browser before accessing pmc.ncbi.nlm.nih.gov ...

Click [here](https://www.google.com/recaptcha/challengepage/#) if you are not automatically redirected after 5 seconds.

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**

reCAPTCHA

### 来源 6: 筑医台--HCD医养设计--医院导视标识的前世今生

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

### 来源 7: [PDF] 基于案例分析的国内外医疗机构导视系统设计现状研究

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

### 来源 8: http://www.nature.com/articles/s41598-025-20128-0.pdf

- URL: http://www.nature.com/articles/s41598-025-20128-0.pdf
- 精读方法：jina-readerlm-academic

```markdown
The provided draft Markdown does not match the content of the original HTML, which only contains a head tag with no actual body content. Therefore, there is nothing to extract or refine further into Markdown beyond the title "Your Title" if one were present.
```

### 来源 9: A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness

- URL: https://www.mdpi.com/1660-4601/19/21/13885
- 精读方法：firecrawl-scrape

Next Article in Journal

[The Effect of a Sleep Intervention on Sleep Quality in Nursing Students: Study Protocol for a Randomized Controlled Trial](https://www.mdpi.com/1660-4601/19/21/13886)

Next Article in Special Issue

[Global Research Trends on Smart Homes for Older Adults: Bibliometric and Scientometric Analyses](https://www.mdpi.com/1660-4601/19/22/14821)

Previous Article in Journal

[The Waning of BNT162b2 Vaccine Effectiveness for SARS-CoV-2 Infection Prevention over Time: A Test-Negative Study in Health Care Professionals of a Health Department from January 2021 to December 2021](https://www.mdpi.com/1660-4601/19/21/13884)

Previous Article in Special Issue

[How Do Older Adults Process Icons in Visual Search Tasks? The Combined Effects of Icon Type and Cognitive Aging](https://www.mdpi.com/1660-4601/19/8/4525)

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

[![ijerph-logo](https://pub.mdpi-res.com/img/journals/ijerph-logo.png?723264ea56800ef4)](https://www.mdpi.com/journal/ijerph)

[Submit to this Journal](https://susy.mdpi.com/user/manuscripts/upload?form%5Bjournal_id%5D%3D6) [Review for this Journal](https://susy.mdpi.com/volunteer/journals/review) [Propose a Special Issue](https://www.mdpi.com/journalproposal/sendproposalspecialissue/ijerph)

[►▼\\
Article Menu](https://www.mdpi.com/1660-4601/19/21/13885#)

## Article Menu

- [Academic Editors](https://www.mdpi.com/1660-4601/19/21/13885#academic_editors)

[![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Mary Lou Maher](https://sciprofiles.com/profile/1515618?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name)

![](https://pub.mdpi-res.com/bundles/mdpisciprofileslink/img/unknown-user.png?1781764495)Lina Lee

- [Recommended Articles](https://www.mdpi.com/1660-4601/19/21/13885#)
- [Related Info Links](https://www.mdpi.com/1660-4601/19/21/13885#related)

  - [PubMed/Medline](http://www.ncbi.nlm.nih.gov/sites/entrez/36360765)
  - [Google Scholar](http://scholar.google.com/scholar?q=A%20Design%20Framework%20of%20Medical%20Wayfinding%20Signs%20for%20the%20Elderly%3A%20Based%20on%20the%20Situational%20Cognitive%20Commonness)

- [More by Authors Links](https://www.mdpi.com/1660-4601/19/21/13885#authors)

  - on DOAJ

    - [Wu, J.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Jianfeng%20Wu%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)
    - [Liu, X.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Xinyu%20Liu%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)
    - [Lu, C.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Chunfu%20Lu%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)
    - [Yu, S.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Shihan%20Yu%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)
    - [Jiao, D.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Dongfang%20Jiao%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)
    - [Ye, X.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Xinyu%20Ye%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)
    - [Zhu, Y.](http://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22query_string%22%3A%7B%22query%22%3A%22%5C%22Yuqing%20Zhu%5C%22%22%2C%22default_operator%22%3A%22AND%22%2C%22default_field%22%3A%22bibjson.author.name%22%7D%7D%7D)

  - on Google Scholar

    - [Wu, J.](http://scholar.google.com/scholar?q=Jianfeng%20Wu)
    - [Liu, X.](http://scholar.google.com/scholar?q=Xinyu%20Liu)
    - [Lu, C.](http://scholar.google.com/scholar?q=Chunfu%20Lu)
    - [Yu, S.](http://scholar.google.com/scholar?q=Shihan%20Yu)
    - [Jiao, D.](http://scholar.google.com/scholar?q=Dongfang%20Jiao)
    - [Ye, X.](http://scholar.google.com/scholar?q=Xinyu%20Ye)
    - [Zhu, Y.](http://scholar.google.com/scholar?q=Yuqing%20Zhu)

  - on PubMed

    - [Wu, J.](http://www.pubmed.gov/?cmd=Search&term=Jianfeng%20Wu)
    - [Liu, X.](http://www.pubmed.gov/?cmd=Search&term=Xinyu%20Liu)
    - [Lu, C.](http://www.pubmed.gov/?cmd=Search&term=Chunfu%20Lu)
    - [Yu, S.](http://www.pubmed.gov/?cmd=Search&term=Shihan%20Yu)
    - [Jiao, D.](http://www.pubmed.gov/?cmd=Search&term=Dongfang%20Jiao)
    - [Ye, X.](http://www.pubmed.gov/?cmd=Search&term=Xinyu%20Ye)
    - [Zhu, Y.](http://www.pubmed.gov/?cmd=Search&term=Yuqing%20Zhu)

[Article Views](https://www.mdpi.com/1660-4601/19/21/13885#metrics)

[Citations-](https://www.mdpi.com/1660-4601/19/21/13885#metrics)

- [Table of Contents](https://www.mdpi.com/1660-4601/19/21/13885#table_of_contents)

Altmetric[_share_ Share](https://www.mdpi.com/1660-4601/19/21/13885# "Share") [_announcement_ Help](https://www.mdpi.com/1660-4601/19/21/13885# "Help")_format\_quote_ Cite [_question\_answer_ Discuss in SciProfiles](https://sciprofiles.com/discussion-groups/public/10.3390/ijerph192113885?utm_source=mpdi.com&utm_medium=publication&utm_campaign=discuss_in_sciprofiles "Discuss in Sciprofiles")

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

[Download PDF](https://www.mdpi.com/1660-4601/19/21/13885/pdf?version=1667547466)

_settings_

[Order Article Reprints](https://www.mdpi.com/1660-4601/19/21/13885/reprints)

Font Type:

_Arial__Georgia__Verdana_

Font Size:

AaAaAa

Line Spacing:

______

Column Width:

______

Background:

Open AccessArticle

# A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness

by

Jianfeng Wu

![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Jianfeng Wu

[SciProfiles](https://sciprofiles.com/profile/940165?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Jianfeng%20Wu) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Jianfeng+Wu%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Jianfeng+Wu)

1 [![](https://pub.mdpi-res.com/img/design/orcid.png?0465bc3812adeb52?1781764495)](https://orcid.org/0000-0003-3726-2015),

Xinyu Liu

![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Xinyu Liu

[SciProfiles](https://sciprofiles.com/profile/2436270?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Xinyu%20Liu) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Xinyu+Liu%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Xinyu+Liu)

2,

Chunfu Lu

![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Chunfu Lu

[SciProfiles](https://sciprofiles.com/profile/573934?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Chunfu%20Lu) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Chunfu+Lu%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Chunfu+Lu)

1,\*,

Shihan Yu

![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Shihan Yu

[SciProfiles](https://sciprofiles.com/profile/author/ZW1YbHZRbWJrZW5JWjVpS2tiVXN5SURmRmVROGJiVU14bm91MHVhT0RmWT0=?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Shihan%20Yu) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Shihan+Yu%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Shihan+Yu)

2,

Dongfang Jiao

![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Dongfang Jiao

[SciProfiles](https://sciprofiles.com/profile/2080909?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Dongfang%20Jiao) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Dongfang+Jiao%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Dongfang+Jiao)

2,

Xinyu Ye

![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Xinyu Ye

[SciProfiles](https://sciprofiles.com/profile/author/dnMvZ1ZsVmVzMG1mK0w2S2VkR21qcnBQYldNc2pobTZlZ0VUNG1sb2h1TT0=?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Xinyu%20Ye) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Xinyu+Ye%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Xinyu+Ye)

2 and

Yuqing Zhu

![](https://www.mdpi.com/bundles/mdpisciprofileslink/img/unknown-user.png)Yuqing Zhu

[SciProfiles](https://sciprofiles.com/profile/author/cmRBSm4yNnQ1bWhoZTUxbEI5a0tTVUgwby82K2JTU3hZOGxOeE1jSmFXST0=?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name) [Scilit](https://scilit.com/scholars?q=Yuqing%20Zhu) [Preprints.org](https://www.preprints.org/search?condition_blocks=[{%22value%22:%22Yuqing+Zhu%22,%22type%22:%22author%22,%22operator%22:null}]&sort_field=relevance&sort_dir=desc&page=1&exact_match=true) [Google Scholar](https://scholar.google.com/scholar?q=Yuqing+Zhu)

2

1

Industrial Design and Research Institute, Zhejiang University of Technology, Hangzhou 310023, China

2

School of Design and Architecture, Zhejiang University of Technology, Hangzhou 310023, China

\*

Author to whom correspondence should be addressed.

_Int. J. Environ. Res. Public Health_ **2022**, _19_(21), 13885; [https://doi.org/10.3390/ijerph192113885](https://doi.org/10.3390/ijerph192113885)

Submission received: 25 September 2022
/
Revised: 19 October 2022
/
Accepted: 24 October 2022
/
Published: 25 October 2022

(This article belongs to the Special Issue [Age-Friendly Technologies: Interaction Design with and for Older People](https://www.mdpi.com/journal/ijerph/special_issues/Technologies_People))

Download _keyboard\_arrow\_down_

[Download PDF](https://www.mdpi.com/1660-4601/19/21/13885/pdf?version=1667547466)

[Download PDF with Cover](https://www.mdpi.com/1660-4601/19/21/13885#)

[Download XML](https://www.mdpi.com/1660-4601/19/21/13885#)

[Download Epub](https://www.mdpi.com/1660-4601/19/21/13885/epub)

[Browse Figures](https://www.mdpi.com/1660-4601/19/21/13885#)

[\
                        <strong>Figure 1</strong><br/>\
                                                    <p>Symbol design framework based on the situational cognitive commonness.</p>\
                                                ](https://pub.mdpi-res.com/ijerph/ijerph-19-13885/article_deploy/html/images/ijerph-19-13885-g001.png?1667556675 "                         <strong>Figure 1</strong><br/>                                                     <p>Symbol design framework based on the situational cognitive commonness.</p>                                                 ")[\
                        <strong>Figure 2</strong><br/>\
                                                    <p>Healthcare wayfinding signs developed by the National Standard of the People’s Republic of China GB/T 10001.6-2021.</p>\
                                                ](https://pub.mdpi-res.com/ijerph/ijerph-19-13885/article_deploy/html/images/ijerph-19-13885-g002.png?1667556671 "                         <strong>Figure 2</strong><br/>                                                     <p>Healthcare wayfinding signs developed by the National Standard of the People’s Republic of China GB/T 10001.6-2021.</p>                                                 ")[\
                        <strong>Figure 3</strong><br/>\
                                                    <p>Presentation of a representative experimental material. Note: The experimental material for users’ drawing of symbol for the “internal medicine department” was taken as an example.</p>\
                                                ](https://pub.mdpi-res.com/ijerph/ijerph-19-13885/article_deploy/html/images/ijerph-19-13885-g003.png?1667556668 "                         <strong>Figure 3</strong><br/>                                                     <p>Presentation of a representative experimental material. Note: The experimental material for users’ drawing of symbol for the “internal medicine department” was taken as an example.</p>                                                 ")[\
                        <strong>Figure 4</strong><br/>\
                                                    <p>Extraction and prototyping of healthcare symbols for the “internal medicine department” and the development of a design.</p>\
                                                ](https://pub.mdpi-res.com/ijerph/ijerph-19-13885/article_deploy/html/images/ijerph-19-13885-g004.png?1667556662 "                         <strong>Figure 4</strong><br/>                                                     <p>Extraction and prototyping of healthcare symbols for the “internal medicine department” and the development of a design.</p>                                                 ")[\
                        <strong>Figure 5</strong><br/>\
                                                    <p>The designs of healthcare wayfinding signs in this study.</p>\
                                                ](https://pub.mdpi-res.com/ijerph/ijerph-19-13885/article_deploy/html/images/ijerph-19-13885-g005.png?1667556666 "                         <strong>Figure 5</strong><br/>                                                     <p>The designs of healthcare wayfinding signs in this study.</p>                                                 ")[\
                        <strong>Figure 6</strong><br/>\
                                                    <p>Examples of symbol materials for the judgment test. Note: The materials for the “internal medicine department” here are taken as examples.</p>\
                                                ](https://pub.mdpi-res.com/ijerph/ijerph-19-13885/article_deploy/html/images/ijerph-19-13885-g006.png?1667556672 "                         <strong>Figure 6</strong><br/>                                                     <p>Examples of symbol materials for the judgment test. Note: The materials for the “internal medicine department” here are taken as examples.</p>                                                 ")

[Versions Notes](https://www.mdpi.com/1660-4601/19/21/13885/notes)

## Abstract

Older people in China have a poor understanding of hospital signage. To address this problem, in this study, we combined the theories of situated cognition and cognitive commonness in order to introduce the three main factors that affect the generation of situational cognitive commonness: composition of the situation, familiarity, and concreteness. We used these theories to construct a methodological framework for the design of geriatric hospital wayfinding signs that were based on situational cognitive commonness. The design of nine healthcare signs for Chinese national standards were used as examples in the study. First, users who were familiar with medical scenarios were asked to draw concrete cognitive conception graphics for the purposes of individual wayfinding targets from both physical and social situations. Next, we coded and grouped the generated graphics based on their situational features in order to extract groups of representative common graphics. Finally, we reorganized the common graphics and developed concrete designs, which were tested by the judgment test. The wayfinding signs designed according to the methodological framework of this study effectively improved the understanding of hospital signage among older Chinese people. This study took geriatric hospital wayfinding signs as the examples to provide a feasible theoretical basis and research reference for symbol design.

Keywords:

[cognitive commonness](https://www.mdpi.com/search?q=cognitive+commonness); [situation theory](https://www.mdpi.com/search?q=situation+theory); [wayfinding sign](https://www.mdpi.com/search?q=wayfinding+sign); [elderly](https://www.mdpi.com/search?q=elderly); [geriatric hospital](https://www.mdpi.com/search?q=geriatric+hospital); [medical signs](https://www.mdpi.com/search?q=medical+signs); [design framework](https://www.mdpi.com/search?q=design+framework)

## 1\. Introduction

Healthcare signage uses graphics as the primary feature to provide guidance \[ [1](https://www.mdpi.com/1660-4601/19/21/13885#B1-ijerph-19-13885)\]. Older patients use these signs to help them with wayfinding when seeking medical treatments \[ [2](https://www.mdpi.com/1660-4601/19/21/13885#B2-ijerph-19-13885), [3](https://www.mdpi.com/1660-4601/19/21/13885#B3-ijerph-19-13885)\]. In order to enhance the understanding of healthcare signage among older patients, many researchers have constructed in-depth studies on the effective expression of visual features in healthcare signs \[ [4](https://www.mdpi.com/1660-4601/19/21/13885#B4-ijerph-19-13885), [5](https://www.mdpi.com/1660-4601/19/21/13885#B5-ijerph-19-13885), [6](https://www.mdpi.com/1660-4601/19/21/13885#B6-ijerph-19-13885)\] and factors that affect the understanding of graphics among older people \[ [6](https://www.mdpi.com/1660-4601/19/21/13885#B6-ijerph-19-13885), [7](https://www.mdpi.com/1660-4601/19/21/13885#B7-ijerph-19-13885), [8](https://www.mdpi.com/1660-4601/19/21/13885#B8-ijerph-19-13885)\]. Due to differences in understanding and the cognition of symbols between designers and elderly users \[ [2](https://www.mdpi.com/1660-4601/19/21/13885#B2-ijerph-19-13885)\], the existing healthcare and hospital signage is still not friendly to the elderly.

To minimize the cognitive gap between designers and specific user groups, some studies have proposed symbol design methods based on the principle of user participation \[ [2](https://www.mdpi.com/1660-4601/19/21/13885#B2-ijerph-19-13885), [9](https://www.mdpi.com/1660-4601/19/21/13885#B9-ijerph-19-13885), [10](https://www.mdpi.com/1660-4601/19/21/13885#B10-ijerph-19-13885)\]. According to this principle, users can draw on their ideas about the symbols and designers analyze these ideas to extract representing graphics, which have “cognitive commonness”—that is, constrained by the experience of the objective world, the cognitions of a specific group of people share certain characteristics and patterns, which reflect the common cognitive structure of the group \[ [11](https://www.mdpi.com/1660-4601/19/21/13885#B11-ijerph-19-13885), [12](https://www.mdpi.com/1660-4601/19/21/13885#B12-ijerph-19-13885), [13](https://www.mdpi.com/1660-4601/19/21/13885#B13-ijerph-19-13885)\]. Finally, these graphics can be optimized to generate symbols that will best enhance user understanding \[ [14](https://www.mdpi.com/1660-4601/19/21/13885#B14-ijerph-19-13885), [15](https://www.mdpi.com/1660-4601/19/21/13885#B15-ijerph-19-13885), [16](https://www.mdpi.com/1660-4601/19/21/13885#B16-ijerph-19-13885)\]. Although it has been shown that the graphical expression may be affected by multiple factors, such as the users’ ability to present their ideas in graphics \[ [17](https://www.mdpi.com/1660-4601/19/21/13885#B17-ijerph-19-13885)\], education level \[ [18](https://www.mdpi.com/1660-4601/19/21/13885#B18-ijerph-19-13885)\], experience \[ [7](https://www.mdpi.com/1660-4601/19/21/13885#B7-ijerph-19-13885)\], and age \[ [19](https://www.mdpi.com/1660-4601/19/21/13885#B19-ijerph-19-13885)\], users influenced by these factors can still provide valuable ideas for symbol design \[ [17](https://www.mdpi.com/1660-4601/19/21/13885#B17-ijerph-19-13885)\]. These methods have been used extensively for public symbol designs, such as transportation \[ [20](https://www.mdpi.com/1660-4601/19/21/13885#B20-ijerph-19-13885)\], tourism \[ [21](https://www.mdpi.com/1660-4601/19/21/13885#B21-ijerph-19-13885)\], and healthcare \[ [22](https://www.mdpi.com/1660-4601/19/21/13885#B22-ijerph-19-13885)\]. When these methods are used, the degree that cognitive commonness is generated is generally determined by the ratio of the number of common graphics to the total number of graphics drawn by users. The graphic category with the highest number of common ideas represents the users’ cognitive commonness, which is also the chief source of the graphics used for symbol design \[ [23](https://www.mdpi.com/1660-4601/19/21/13885#B23-ijerph-19-13885)\]. However, it is not enough to take “the number of similar graphics” as the standard to obtain users’ cognitive commonness, due to the fact that there is no way to ensure that these graphics are common and representative for a specific population. In addition, the lack of constraints on the semantics of the graphics when extracting common ideas may limit the comprehensibility of the redesigned symbols \[ [7](https://www.mdpi.com/1660-4601/19/21/13885#B7-ijerph-19-13885)\]. Thus, further research is needed to summarize the common ideas in order to extract users’ cognitive commonness.

Some researchers have studied the comprehension of symbols from the perspective of situated cognition \[ [24](https://www.mdpi.com/1660-4601/19/21/13885#B24-ijerph-19-13885), [25](https://www.mdpi.com/1660-4601/19/21/13885#B25-ijerph-19-13885)\]. The findings indicated that users have a better understanding of symbols that represent a complete application situation \[ [26](https://www.mdpi.com/1660-4601/19/21/13885#B26-ijerph-19-13885)\], suggesting a new perspective for the interpretation of accurately extracting cognitive commonness. In this study, we introduced the theory of situated cognition in order to construct a methodological framework for symbol design based on the situational cognitive commonness. We also selected signs used for Chinese geriatric hospital wayfinding in order to carry out the design and to evaluate and discuss the methods.

## 2\. Related Research

### 2.1. Symbol Design Based on Cognitive Commonness

Previous studies have shown that cognitive convergence exists between groups. This convergence is not only reflected in the form of information storage and processing, but also has an important impact on the output of cognitive activities. Some researchers have used the concept of cognitive commonness to describe this phenomenon \[ [11](https://www.mdpi.com/1660-4601/19/21/13885#B11-ijerph-19-13885), [12](https://www.mdpi.com/1660-4601/19/21/13885#B12-ijerph-19-13885), [13](https://www.mdpi.com/1660-4601/19/21/13885#B13-ijerph-19-13885)\]. Further, this theory of cognitive commonness has raised significant attention in the field of graphic design \[ [10](https://www.mdpi.com/1660-4601/19/21/13885#B10-ijerph-19-13885), [15](https://www.mdpi.com/1660-4601/19/21/13885#B15-ijerph-19-13885), [27](https://www.mdpi.com/1660-4601/19/21/13885#B27-ijerph-19-13885)\]. First, it has been used to visualize cognitive expression by graphics in order to eliminate the cognitive friction that exists between designers and users and also to reduce the perceived challenge in design tasks and design expression. Second, the expected preferences for specific symbols are inferred by illustrating the common ideas of the users, providing references for the design of the symbols. For example, Ng \[ [17](https://www.mdpi.com/1660-4601/19/21/13885#B17-ijerph-19-13885)\] explored the cognitive commonness of older people and collected their ideas on the signage used in public. They then summarized and evaluated the common ideas of the older people. Green \[ [15](https://www.mdpi.com/1660-4601/19/21/13885#B15-ijerph-19-13885)\] guided users to draw graphics that symbolize the functions of automotive instrument panels, and then extracted the common graphics to create a candidate set of automotive symbols. The question of how to accurately obtain and extract the cognitive commonness of users, however, remains a core challenge when applying these methods. Existing research has mainly adopted the measurement of an absolute number of common ideas and considered the category of ideas that accounts for the largest proportion of ideas of a user group as cognitive commonness \[ [23](https://www.mdpi.com/1660-4601/19/21/13885#B23-ijerph-19-13885), [28](https://www.mdpi.com/1660-4601/19/21/13885#B28-ijerph-19-13885)\]. Although using an absolute number of common ideas to determine cognitive commonness is simple and easy to implement, this approach can also be affected by many factors, such as the users’ drawing ability, object imagery preference \[ [17](https://www.mdpi.com/1660-4601/19/21/13885#B17-ijerph-19-13885)\], gender, and age \[ [7](https://www.mdpi.com/1660-4601/19/21/13885#B7-ijerph-19-13885), [19](https://www.mdpi.com/1660-4601/19/21/13885#B19-ijerph-19-13885)\]. These user factors may result in deviations in these ideas. Therefore, further research is required to ensure the accuracy and perfection of the graphics used to describe and represent cognition and ideas.

### 2.2. The Theory of Situated Cognition and Cognitive Commonness

According to the theory of situated cognition, cognition occurs in complex social contexts involving people, actions, and situations \[ [29](https://www.mdpi.com/1660-4601/19/21/13885#B29-ijerph-19-13885), [30](https://www.mdpi.com/1660-4601/19/21/13885#B30-ijerph-19-13885)\]. Rambusch \[ [31](https://www.mdpi.com/1660-4601/19/21/13885#B31-ijerph-19-13885)\] and Echterhoff \[ [32](https://www.mdpi.com/1660-4601/19/21/13885#B32-ijerph-19-13885)\] showed that information that presents situational features is more likely to be transmitted among groups and tends to develop a cognitive commonness among groups. The more specific the situational features, the better the ability of individuals to imagine and remember the relevant information, which leads to higher cognitive similarity of the shared information \[ [33](https://www.mdpi.com/1660-4601/19/21/13885#B33-ijerph-19-13885)\]. For example, Lesch \[ [24](https://www.mdpi.com/1660-4601/19/21/13885#B24-ijerph-19-13885)\] showed that scenario training not only improved the cognitive levels and understanding of warning symbols among older people, but also strengthened the ability of older people to correctly respond to the hazards indicated by the warning symbols. The results of Lesch’s study provided a new idea for drawing graphics representing cognitive commonness—that is, the use of situational elements as the basis for drawing and extracting common ideas based on cognitive commonness.

The findings of the above studies suggest that three main factors affect the situational cognitive commonness:

- Composition of the situation. The human cognitive system is suprapersonal; cognition is constructed and stored in the brain and affected by physical activities and the environment of social interaction \[ [31](https://www.mdpi.com/1660-4601/19/21/13885#B31-ijerph-19-13885), [34](https://www.mdpi.com/1660-4601/19/21/13885#B34-ijerph-19-13885)\]. Hutchins \[ [35](https://www.mdpi.com/1660-4601/19/21/13885#B35-ijerph-19-13885)\] showed that completion of a flight required information processing in the brain of pilots, their usage of physical tools in the cockpit to store the information, and thus researchers explain pilots’ behavioral attributes through their situational representation of tool use. Rizzolatti \[ [36](https://www.mdpi.com/1660-4601/19/21/13885#B36-ijerph-19-13885)\] proposed that human cognition and behaviors are affected by a matching system that exists between action execution and action observation in social situations. In a specific situation, human cognition originates from perceptual activities, depending on the contact with physical equipment and physical structures in the environment as well as in the social interactions (behaviors, language, and other communication methods) held with other people. Both are important components in situated cognition.

- Familiarity. Cognitive commonness is affected by familiarity \[ [37](https://www.mdpi.com/1660-4601/19/21/13885#B37-ijerph-19-13885)\], which promotes the generation of more information related to situated cognition. Increasing evidence has supported the idea that individuals who are more familiar with the items and events they need to describe are capable of constructing a richer situational model \[ [38](https://www.mdpi.com/1660-4601/19/21/13885#B38-ijerph-19-13885)\]. The theory of situated cognition suggests that the more familiar an individual is with the target information, the more likely it is that he/she can process the situational representations based on memory \[ [30](https://www.mdpi.com/1660-4601/19/21/13885#B30-ijerph-19-13885)\]. A study by Shen \[ [37](https://www.mdpi.com/1660-4601/19/21/13885#B37-ijerph-19-13885)\] showed that people who are familiar with a restaurant, for example, could retrieve the situational information of the restaurant’s service from their memory, which directly affected their perception of the restaurant’s service. Another study by Shen \[ [39](https://www.mdpi.com/1660-4601/19/21/13885#B39-ijerph-19-13885)\] showed that a user’s familiarity with the objects depicted in a symbol affected their understanding of that symbol, suggesting that designers should use patterns and elements that are familiar to the users. Green \[ [15](https://www.mdpi.com/1660-4601/19/21/13885#B15-ijerph-19-13885)\] believed that it was difficult for individuals to draw symbols to represent unfamiliar situations during graphic generation. Selecting individuals who were more familiar with the target information to draw the symbols improved the efficiency of graphic design. In other words, the more familiar the users are with a specific interaction and scenario, the easier it is to recall their relatively complete memory of that situation. These users can build a rich situational-cognitive model by recalling the situational features in the brain, so that they can produce more situational information that is common. As a result, designers can extract the ideas of situational cognitive commonness among the users.

- Concreteness. When the ideas that symbols represent are more specific and simpler, the semantics are clearer and easier to understand \[ [40](https://www.mdpi.com/1660-4601/19/21/13885#B40-ijerph-19-13885)\]. It is easier for people to generate concrete graphics of cognitive commonness \[ [17](https://www.mdpi.com/1660-4601/19/21/13885#B17-ijerph-19-13885)\] and to actively use concrete elements to create patterns. For example, Picard \[ [41](https://www.mdpi.com/1660-4601/19/21/13885#B41-ijerph-19-13885)\] believed that children’s drawings conveyed information about objects or scenes in concrete forms. Jones \[ [42](https://www.mdpi.com/1660-4601/19/21/13885#B42-ijerph-19-13885)\] showed that older people tended to show concrete elements with less complexity in cognition and visual processing in their drawings and that they are good at drawing concrete graphics. Hence, selection of specific and authentic situational information that represents a familiar environment is needed when designing symbols. In addition, the visual elements should be simplified but should not be too abstractive in order to allow users to have a consistent understanding.

## 3\. Methodological Framework for Symbol Design and Operating Procedures Based on the Situational Cognitive Commonness

### 3.1. Framework for Symbol Design

As mentioned above, situated cognition reflects the cognitive commonness of users. As such, this study proposed a symbol design framework that is based on situational cognitive commonness ( [Figure 1](https://www.mdpi.com/1660-4601/19/21/13885#ijerph-19-13885-f001)). This framework was based mainly on a previous report by Green \[ [15](https://www.mdpi.com/1660-4601/19/21/13885#B15-ijerph-19-13885)\]. We embedded the theory of situated cognition into the symbol design framework, which is based on situational cognitive commonness. At both the user and designer levels, we introduced the three factors (i.e., composition of the situation, familiarity, and concreteness) that affect situational cognitive commonness into all three graphic design stages (i.e., creation, extraction, and prototyping). The study focused on how to establish cognitive commonness that is based on situational measures for the purposes of the better design of symbols.

At the user’s level, all three factors (i.e., composition of the situation, familiarity, and concreteness) were fully utilized. Familiarity with the situation enabled users to build a rich situational-cognitive model, thereby improving the creation of the ideas for situational cognitive commonness. The brain recalled the situational features experienced by the users and presented them in concrete forms. During the first stage (i.e., creation) of symbol design, researchers screened representative users who were familiar with the wayfinding target situations. For example, people who visited a place several times in a certain period of time were familiar with the situation of this space, and therefore had advantages in their situated cognition when conceiving graphics. As such, the designers promoted them to draw graphics from both social and physical situations and requested the users to use concrete expressions in order to create cognitive conception graphics.

At the designer’s level, the two factors of composition of the situation and concreteness were introduced. The second (extraction) stage involved the composition of the situation. Situational elements, as the bases for extracting common ideas and the references for the prototyping stage, affected the effectiveness of the proposed designs. Designers encoded the graphics generated by the users and grouped the graphics based on their physical and social situational elements. The designers subsequently screened groups of common graphics based on the graphics of the groups and the number of common ideas. Both composition of the situation and concreteness were introduced during the prototyping stage of symbol design. Situational information triggers the cognitive commonness of specific events and items in humans. The concrete expression of ideas helped users to easily understand the graphics. Therefore, concrete expression was regarded as a tool to assist situational design. At the prototyping stage, designers may prioritize the elements of common graphic groups, and screen the graphics with higher importance for design. The designers supplemented the physical and social situational elements that had been missing in the groups of common graphics, which was followed by the development of the symbols in a concrete form according to the design criteria.

### 3.2. Operating Procedures

During the first stage (i.e., creation), cognitive conception graphics of optimized symbols were created by the users. First, for symbols that were not easily understood by the target users, experimental materials (e.g., title, meaning, and drawing region) were generated in the designated area. Second, users who were familiar with the application situation of the symbols were invited to participate in graphing and were guided to imagine the personnel, objects, environments, and human interaction scenarios. It should be noted that the researchers instructed the participants to recall the wayfinding target situations rather than the wayfinding symbols in order to simulate situational cognition. The symbol names were given to the users as textual stimuli, and the users were required to draw concrete graphics. The users were interviewed about their drawing ideas during or after they had completed drawing.

During the second stage (i.e., extraction), the graphics created by the users were extracted in order to form graphics of cognitive commonness for subsequent design use. First, the designers needed to eliminate the drawing papers that possessed no responses or only plain text responses. Further, the designers then carefully followed the principle of extracting cognitive commonness with situational features by encoding the user-drawn graphics that were based on situational features, such as interaction scenarios and related devices. Subsequently, they divided the graphics into groups, then screened and selected the groups that met the situational features, and that also had a relatively large number of responses, in order to form groups of the common graphics. As the participants’ graphics may not be intuitive enough, designers in this stage were required to be aware of the wayfinding target location beforehand in order to increase their familiarity with the surroundings. They were required to know exactly what each idea was meant to represent and to interact with the participants more.

During the third stage (i.e., prototyping), the symbols were designed and tested according to the groups of common graphics. The designers were required to follow the requirements of concreteness and situationalization in order to extract and reorganize the representative graphics from the groups of common graphics. The key to this link was such that the scene represented by the graphics should be easy to understand in order to reveal the intent of the application of the symbols in the actual scenario. Various graphics were integrated in order to express the key elements and interactions in the scenario. Designers prioritized the graphic elements of each group according to their importance, and then extracted the elements that met the method standards and were easy to express as representative graphics. Designers used had rich experience in wayfinding target situations, so that they could supplement the situational elements that the users might have missed, and to also aid the users through drawing design sketches. Standard symbols, design specifications, and users’ visual habits and cognitive rules were subsequently combined to form standardized symbol designs. Then, the designs were reviewed and revised by experts in order to form symbols that were based on the users’ situational cognitive commonness. Finally, participants who were not involved in the design were invited to complete the judgement test developed by the International Organization for Standardization \[ [43](https://www.mdpi.com/1660-4601/19/21/13885#B43-ijerph-19-13885)\] in order to examine differences in the user’s understanding of the symbols before and after the design. The two symbol variants with the same meaning from before and after the optimization were placed in one group in a random order and labeled. The symbols in each group were arranged from top to bottom and were printed on a piece of white paper as experimental materials. According to the judgment test criteria, the comprehension of each symbol variant was determined by estimating the percentage of the total population who understood the correct meaning of the symbol variant \[ [2](https://www.mdpi.com/1660-4601/19/21/13885#B2-ijerph-19-13885), [44](https://www.mdpi.com/1660-4601/19/21/13885#B44-ijerph-19-13885)\]. All participants were required to write a judgment value in the blank space next to each symbol variant.

## 4\. Application of Symbol Design Method Based on the Situational Cognitive Commonness

To test the effectiveness of the symbol design framework (which was based on the users’ situational cognitive commonness), we carried out a design practice for geriatric hospital wayfinding signs in China. Although healthcare signs are widely used, they are not universally understood by older people. Hence, redesigning these healthcare symbols may help improve the problem of symbol cognition among older people. This design method was also evaluated and improved in this practice. The steps associated with the symbol design approach, based on situational cognitive commonness, are discussed in the following sections.

### 4.1. Design Preparation

The symbols for medical treatment and healthcare regulated by the National Standard of the People’s Republic of China \[ [45](https://www.mdpi.com/1660-4601/19/21/13885#B45-ijerph-19-13885)\] were implemented only in October 2021. As there was no report on public identification and testing, we selected nine wayfinding signs for healthcare as experimental materials in this study. These signs showed basic information about some of the major departments in a healthcare environment, including “internal medicine department”, “surgery department”, “radiology department”, “nurse”, “observation room”, “ultrasound department”, “gynecology department”, “western pharmacy”, and “traditional Chinese medicine (TCM) pharmacy”. [Figure 2](https://www.mdpi.com/1660-4601/19/21/13885#ijerph-19-13885-f002) shows the specific symbols and names selected in this study. [Figure 3](https://www.mdpi.com/1660-4601/19/21/13885#ijerph-19-13885-f003) shows an example of the experimental materials, including a drawing paper for users at the first (creation) stage that contains a title, a description of the title, and a drawing area of 8 × 8 cm2. The drawing area is divided into 2 × 2 squares by the central axes.

### 4.2. Obtaining Ideas from the Users

This study recruited participants from several communities in Hangzhou City, Zhejiang Province, China, and all of the research protocol for this study was approved by the Ethics Committee of the Institute of Industrial Design of Zhejiang University of Technology (Zhejiang Province, China). All participants gave their verbal informed consent before participating the experiment.

In order to obtain, relatively, enough common ideas, we used the information saturation sampling principle for reference \[ [46](https://www.mdpi.com/1660-4601/19/21/13885#B46-ijerph-19-13885)\]. As such, a sequential participant experiment format was adopted. The first stage of graphic design (i.e., creation) enrolled a total of 24 older people, which included 14 men and 10 women, aged 73 ± 9.7 years on average (mean ± standard deviation). All participants had elementary school education or above, and their backgrounds were in cities. These 24 participants were told that this part of the experiment would last for 20–30 min, and that they would receive a material reward at the end of the experiments. These participants had received medical treatments frequently and had also visited hospitals more than five times in the past year. They also had a high degree of familiarity with healthcare environments in general and were representative of the population.

During the experiments, these participants were provided paper materials and a pencil. They were then instructed to read each title (e.g., medical department, service, etc.) and to imagine each situation. They were then asked to draw a picture of the situation described and to complete the drawing independently. Participants were allowed to write or draw in the drawing area, without a right or wrong answer. Participants were encouraged to verbally describe their drawing ideas during the drawing task. Their thoughts were recorded by the researchers. All participants were interviewed by the researchers after they had completed their drawing. Participants who were not able to complete the drawing task were allowed to withdraw from the study, and their experimental data were not used for subsequent analysis.

### 4.3. Extracting the Common Graphics

After eliminating the drawing papers with no responses or only plain text responses, a total of 174 graphics for the nine symbols were obtained at the end of the first stage (i.e., creation). Both pure graphics and graphics marked with a small amount of text were defined as valid responses. [Figure 4](https://www.mdpi.com/1660-4601/19/21/13885#ijerph-19-13885-f004) shows the process of extracting the common graphics for a healthcare symbol, specifically for a “internal medicine department”, and the developing of the designs. The designers had to accurately extract the common graphics. They combined the recorded ideas of the individual users with their drawings in order to encode the graphics that were based on physical situations (e.g., characters involved in the situations, medical equipment, and medical environments) as well as social situations (e.g., doctor–patient interaction scenarios) and subsequently divided the drawings into six groups. Among these six groups of drawings, the “stethoscope” group and “scene of a patient visiting a doctor” group contained obvious situational features and had many graphic responses. Therefore, these two groups were extracted from the six groups to form a group of common ideas under the title of the “internal medicine department”.

### 4.4. Output of Symbol Design

In this study, the output was a symbol design that represented the cognitive commonness of the users. The designers restored the scenario of interaction based on both the physical and social situations, and then explored which situational elements the users may encounter. Subsequently, they extracted the representative graphic elements (e.g., doctor, patient, and stethoscope) from the groups of common graphics (e.g., “scene of a patient visiting a doctor” and “stethoscope”). The designers reorganized the graphics and supplemented the situational elements that the users might have missed, and then sketched the designs. A person wearing a surgical scrub cap and carrying a stethoscope represented a doctor, and a commonly used human pattern was used to represent a general patient. The stethoscope was drawn in the form of circles and arcs and the characteristics of the stethoscope were properly amplified to draw users’ attention and facilitate understanding. In addition, the symbol featured the scenario information of a doctor using the stethoscope to examine a patient who was in a seated position. After finishing the sketch, we used Adobe Illustrator and Adobe XD to develop the actual symbols based on these sketches.

After all designs were developed, three experts were invited to comment on the designed symbols. After several rounds of revisions based on the experts’ opinions, the final “internal medicine department” design was obtained. [Figure 5](https://www.mdpi.com/1660-4601/19/21/13885#ijerph-19-13885-f005) shows the designs of the nine healthcare symbols that were developed in this study.

### 4.5. Design Test and Statistical Analysis

To verify the effectiveness of the symbol design methods based on situational cognitive commonness, we verified the differences in understanding the healthcare wayfinding signs before and after optimization of the designs by the judgment test.

This study recruited 77 Chinese older men (44) and women (33), who were all older than 60 years old, from several communities in Hangzhou City to participate in the design test. All representative participants had an education level of elementary school or above, and all grew up and lived in the city. None of them had severe cognitive or visual impairment, nor participated in the graphic drawing task (experiments listed in [Section 4.2](https://www.mdpi.com/1660-4601/19/21/13885#sec4dot2-ijerph-19-13885)). All were non-medical-related professionals who received a monetary reward at the end of the experiments.

The experimental materials included printed paper materials containing nine groups of healthcare symbols before and after optimization (representative examples are shown in [Figure 2](https://www.mdpi.com/1660-4601/19/21/13885#ijerph-19-13885-f002) and [Figure 5](https://www.mdpi.com/1660-4601/19/21/13885#ijerph-19-13885-f005)), with the symbol titles and descriptions marked on the top of the papers ( [Figure 6](https://www.mdpi.com/1660-4601/19/21/13885#ijerph-19-13885-f006)). Two symbol variants (with the same meaning) before and after optimization were put in the same group and were randomly arranged in the left and right columns. According to the judgment test criteria, these 77 participants were required to estimate the percentage of the total population (0–100%) that may understand each symbol variant correctly \[ [2](https://www.mdpi.com/1660-4601/19/21/13885#B2-ijerph-19-13885), [44](https://www.mdpi.com/1660-4601/19/21/13885#B44-ijerph-19-13885)\], followed by writing the judgment value (estimated percentage of the total population) in the blank space next to each symbol variant.

To test whether the design method based on the situational cognitive commonness could improve symbol understanding among older users, this study used a paired t-test to analyze the data and to compare the understanding before and after optimization of the designs. An alpha of 0.05 was used to test significance in this study.

The results of the paired t-test showed that the average understanding of six out of nine optimized symbols was significantly higher than that of the existing designs, including the “internal medicine department”, “surgery department”, “radiology department”, “nurse”, “observation room”, and “gynecology department” ( [Table 1](https://www.mdpi.com/1660-4601/19/21/13885#ijerph-19-13885-t001)). Among the remaining three schemes, no significant difference was found before and after optimization for the “western pharmacy” and “TCM pharmacy” symbols, whereas the average understanding of the optimized symbol for “ultrasound department” was slightly reduced. Therefore, among the nine design schemes, a total of six symbols provided better understanding to the users, compared with the existing national standard graphic symbols. This result suggested that our symbol design method based on the situational cognitive commonness was effective in improving the understanding of graphic symbols among older Chinese people.

## 5\. Discussion

### 5.1. Major Findings

#### 5.1.1. Role of Situated Cognition in Symbol Design

This study integrated the theory of situated cognition in a symbol design method based on situational cognitive commonness. Users and designers were guided to use situational representation in the physical and social situations during three different stages of graphic design: creation of cognitive graphics, extraction of common graphics, and design output. Among the nine new healthcare symbols with situational elements in the assessments, six of them (i.e., “internal medicine department”, “surgery department”, “radiology department”, “nurse”, “observation room”, and “gynecology department”) achieved significantly better user understanding after optimization, indicating the necessity of introducing situated cognition into symbol design. As mentioned earlier, when extracting common ideas from a user group, the category with the highest percentage of cognitive ideas was typically used to determine cognitive commonness \[ [23](https://www.mdpi.com/1660-4601/19/21/13885#B23-ijerph-19-13885), [28](https://www.mdpi.com/1660-4601/19/21/13885#B28-ijerph-19-13885)\], which may, however, lack constraint on graphic semantics when extracting common ideas \[ [7](https://www.mdpi.com/1660-4601/19/21/13885#B7-ijerph-19-13885)\]. In this study, designers used users’ high cognitive similarity to medical situational features in order to direct users in the generation and evaluation of symbols \[ [33](https://www.mdpi.com/1660-4601/19/21/13885#B33-ijerph-19-13885)\]. The users’ cognition of healthcare symbols was associated with users’ spatial interaction with medical treatment, and their memories of healthcare scenarios were stimulated by situational visual representations. The commonness and uniformity of healthcare scenarios led to cognitive convergence in older people. In accordance with cognitive theories, they created graphs with the same or with similar semantics; with this approach, then, the understanding of the optimized medical symbols can be improved.

This finding was also supported in a study by Patel \[ [22](https://www.mdpi.com/1660-4601/19/21/13885#B22-ijerph-19-13885)\], which used the Snellen eye chart, ophthalmologist graphics, and eye graphics in order to redesign the ophthalmologist icon for hospitals in central India. By fully presenting the characters, equipment, and elements of the ophthalmology clinic, they effectively improved the users’ understanding of the icons.

In addition, our study also showed that older people’s judgments of symbols were not only determined by their specific representations of the situation, but were also influenced by long-term aesthetic preferences and stereotypes. For example, the symbol of “gynecology department” was composed of elements for a woman and a heart (love). Although this symbol did not present the medical situation of a gynecology clinical, it still evoked a high level of understanding by the older user, which was consistent with the finding of Smith \[ [47](https://www.mdpi.com/1660-4601/19/21/13885#B47-ijerph-19-13885)\]. This result also confirmed the report of Schwarz \[ [30](https://www.mdpi.com/1660-4601/19/21/13885#B30-ijerph-19-13885)\] that people relied on general knowledge of items and events and tended to form judgments in a top-down manner. In this study, old Chinese people already had deep-rooted cognitive standards for the symbol of the “gynecology department”. Even if the situational features were not obvious in this circumstance, older Chinese people still made judgments based on their cognition.

#### 5.1.2. Roles of Familiarity and Concreteness in Symbol Design

Familiarity was the starting point for the application of the framework of symbol design methods based on situational cognitive commonness. It was also an important factor in the formation of cognitive commonness. Among the national standard healthcare symbols in China, some symbols include professional medical tools as the main elements. For example, a single element, a stethoscope, was used to represent the symbol of the “internal medicine department”. As patients in healthcare scenarios, however, older people were generally less familiar with professional medical tools and had a hard time identifying these pictures with a high degree of completeness in their minds. This increased the difficulties in generating the cognitive commonness, resulting in a poor understanding of the existing symbols. In the design practice for healthcare symbols, this study recruited older people with a high familiarity with the healthcare environment as participants to draw the common graphics. Their drawing ideas focused on familiar physical and social situations. For example, the common ideas about the “internal medicine department” obtained by older Chinese people included “stethoscope” and “scene of a patient visiting a doctor” ( [Figure 4](https://www.mdpi.com/1660-4601/19/21/13885#ijerph-19-13885-f004)). From the perspective of situated cognition, the designers put “a doctor using stethoscope to examine a patient” into the symbol for the “internal medicine department”. The users were highly familiar with this scenario. Thus, the designed symbol effectively overcame the problem of poor understanding of medical tools (which were used as design elements in the national standard healthcare symbols in China) among older Chinese people. In addition, a poor understanding of the symbols was improved after partial optimization of the symbols, suggesting the role of familiarity was important in symbol design. For example, our optimized symbol for “ultrasound department” consisted of fewer components (which included only an ultrasound screen, a patient, and a bed; see [Figure 5](https://www.mdpi.com/1660-4601/19/21/13885#ijerph-19-13885-f005) for details) than the national standard healthcare symbols in China (which included an ultrasound screen, a patient, a bed, and a radiologist; see [Figure 2](https://www.mdpi.com/1660-4601/19/21/13885#ijerph-19-13885-f002) for details). The lack of key elements in the scene may result in the poor understanding of the users. A study by Shen \[ [39](https://www.mdpi.com/1660-4601/19/21/13885#B39-ijerph-19-13885)\] showed that icons that were highly comprehensible tended to represent events and items that the users were familiar with. In the present study, the older patients had a single perception perspective in the limited healthcare scenario. As cognitive commonness generated by high familiarity was amplified, this led to the neglect of other situational elements and resulted in the usage of fewer symbolic elements and a poorer understanding among older users. This finding also suggests that it is necessary to recruit different user populations for a situation when designing a symbol based on situational cognitive commonness in order to enrich the cognitive commonness of specific situations.

Moreover, concrete expression played a key role in acquiring the cognitive commonness of older people and also the design output. The drawings of older people when generating cognitive conception graphics mostly contained concrete elements. For example, the symbols prepared by our participants for “scene of a patient visiting a doctor” in the “internal medicine department” included the drawings of “a doctor”, “patient”, and “table”. This phenomenon of concrete representation was also shown in other graphic drawings, which verified the findings of Ng \[ [17](https://www.mdpi.com/1660-4601/19/21/13885#B17-ijerph-19-13885)\] that people were more likely to create concrete graphics of cognitive commonness. Designers of our study also adopted concrete expression when processing and designing the common graphics. The final test results verified that the understanding of the symbols among older people was improved, which was consistent with the findings of the report by Jones \[ [42](https://www.mdpi.com/1660-4601/19/21/13885#B42-ijerph-19-13885)\] that the concrete design method directly reflected the cognitive commonness of the users.

### 5.2. Application Suggestions

First, we suggest incorporating situated cognition into symbol design processes. Based on the cognitive commonness of specific users to symbols, the optimized symbols may effectively improve the users’ understanding of the symbols. Compared with the previous symbol design methods based on the principle of user participation, the composition of the situation is more conducive to users’ memory of the real scene that the graphics and wayfinding signs are meant to represent. Familiarity can make users provide comprehensive information when generating graphics, and the use of concreteness in the design of the graphics can intuitively express the symbol semantics that the designers wish users to acquire. This method can better obtain the users’ more real and common ideas. It can also help designers implement their ideas more effectively, and therefore make it easier for users to understand symbols. The cognition of each healthcare department among older people generally stems from the physical and social situations with which they interact. Thus, it is necessary to make the composition of symbols align with their understanding by restoring the characters, physical equipment, healthcare environment, and interaction between the patients and the doctors. When designing symbols for complex scenarios, the drawings from users may not completely present all scenarios, as such designers should supplement the situational features in order to prepare symbols that best fit with the actual scenarios.

Second, we suggest selecting participants who are familiar with the target information when applying the framework of symbol design methods that are based on situational cognitive commonness. This should improve the efficiency and quality of common graphic creation and lay a solid foundation for designers to extract common graphics, thereby effectively improving understanding of designed symbols.

Third, designers should try their best to guide users to draw concrete graphics and to process and enhance the concreteness of the design in order to minimize the difficulties of understanding among users. Designers may have operational differences in the extraction and prototyping stages, which may lead to different design results. Designers are required to be familiar with wayfinding target situations in advance; further they must try to understand users’ real drawing ideas in depth and to carry out design practice as well.

### 5.3. Limitations and Future Research

This study does also have some limitations: (1) This study focused on the current situation that older Chinese people have a poor understanding of healthcare wayfinding signs in China. The design practice using the framework of this study was based on healthcare wayfinding signs and the older population. Therefore, the application is most suitable for the healthcare symbol design field targeting the older population. More in-depth research in the future should be conducted on symbols from different fields or that integrate multiple fields. (2) This research paid little attention to the effects of user factors on the generation of cognitive commonness. Older people from different age groups and having different characteristics may have different cognitive patterns. Future studies should include participants from different backgrounds and education level and age groups and with different characteristics in order to improve the generality of the symbols. (3) This study incorporated familiarity and concreteness into the design framework and design practice. We did not, however, evaluate users’ familiarity with the target information or objects that are included in the National Standard of the People’s Republic of China \[ [45](https://www.mdpi.com/1660-4601/19/21/13885#B45-ijerph-19-13885)\] regulating of medical wayfinding symbols, which may have influenced the judgment of participants who had knowledge of these symbols. The degrees of concreteness in the user-drawn graphics or the designers’ designs were also not objectively evaluated. Therefore, a future study should introduce questionnaires to verify the role of familiarity and concreteness through the users’ scoring. (4) This study only compared the changes in the comprehension of medical wayfinding symbols before and after the redesign, without integrating the medical department symbols and other public symbols within the hospital. Therefore, future studies should test the comprehension of medical symbols and general-purpose symbols within the hospital to verify whether users can accurately recognize the medical symbol design scheme among many symbols.

## 6\. Conclusions

This study incorporated the theory of situated cognition and cognitive commonness into symbol design. We proposed a design framework for signage in geriatric hospitals based on older users’ situational cognitive commonness in order to improve the understanding of healthcare and hospital signage among older Chinese people. Using the design practice of nine national standard healthcare wayfinding signs, the design approach in this study further developed the previous symbolic design approach that was based on the principle of user participation. Further, this approach then incorporated new design methods in the design framework in order to address its shortcomings in the interpretation of accurately extracting cognitive commonness with: the composition of the situation that enhanced the real common ideas, the familiarity that promoted users to recall situations comprehensively, and the concreteness that expressed the semantics of symbols intuitively, which all improved the understanding of the medical wayfinding symbols among older people. This study provided a feasible theoretical basis that can be used to improve the graphic design of wayfinding signs for older people in a healthcare environment. It can also serve as a research reference in the graphic design for public environments in order to improve the understanding of signs.

## Author Contributions

Conceptualization, J.W.; methodology, Y.Z. and X.L.; formal analysis, X.L. and D.J.; investigation, S.Y. and X.Y.; resources, C.L.; writing—original draft preparation, Y.Z.; writing—review and editing, X.L.; supervision, J.W. All authors have read and agreed to the published version of the manuscript.

## Funding

This research was funded by the Philosophy and Social Science Planning Fund Project of Zhejiang Province, grant number: 21NDJC038YB; additionally, the Zhejiang Provincial Natural Science Foundation of China also provided funding, grant number: LQ18E050008.

## Institutional Review Board Statement

The study was conducted in accordance with the Declaration of Helsinki and approved by the Ethics Committee of the Industrial Design Institute of Zhejiang University of Technology (protocol code 1101/2021/20211115).

## Informed Consent Statement

Informed consent was obtained from all subjects who were involved in this study.

## Data Availability Statement

Not applicable.

## Conflicts of Interest

The authors declare no conflict of interest.

## References

01. Heires, M. The international organization for standardization (ISO). New Polit. Econ. **2008**, 13, 357–367. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=The+international+organization+for+standardization+(ISO)&author=Heires,+M.&publication_year=2008&journal=New+Polit.+Econ.&volume=13&pages=357%E2%80%93367&doi=10.1080/13563460802302693)\] \[ [CrossRef](https://doi.org/10.1080/13563460802302693)\]
02. Lee, S.; Dazkir, S.S.; Paik, H.S.; Coskun, A. Comprehensibility of universal healthcare symbols for wayfinding in healthcare facilities. Appl. Ergon. **2014**, 45, 878–885. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Comprehensibility+of+universal+healthcare+symbols+for+wayfinding+in+healthcare+facilities&author=Lee,+S.&author=Dazkir,+S.S.&author=Paik,+H.S.&author=Coskun,+A.&publication_year=2014&journal=Appl.+Ergon.&volume=45&pages=878%E2%80%93885&doi=10.1016/j.apergo.2013.11.003&pmid=24290906)\] \[ [CrossRef](https://doi.org/10.1016/j.apergo.2013.11.003)\] \[ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/24290906)\]
03. Hashim, M.J.; Alkaabi, M.S.K.M.; Bharwani, S. Interpretation of way-finding healthcare symbols by a multicultural population: Navigation signage design for global health. Appl. Ergon. **2014**, 45, 503–509. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Interpretation+of+way-finding+healthcare+symbols+by+a+multicultural+population:+Navigation+signage+design+for+global+health&author=Hashim,+M.J.&author=Alkaabi,+M.S.K.M.&author=Bharwani,+S.&publication_year=2014&journal=Appl.+Ergon.&volume=45&pages=503%E2%80%93509&doi=10.1016/j.apergo.2013.07.002&pmid=23932379)\] \[ [CrossRef](https://doi.org/10.1016/j.apergo.2013.07.002)\] \[ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/23932379)\]
04. Shinar, D.; Vogelzang, M. Comprehension of traffic signs with symbolic versus text displays. Transp. Res. Part F Traffic Psychol. Behav. **2013**, 18, 72–82. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Comprehension+of+traffic+signs+with+symbolic+versus+text+displays&author=Shinar,+D.&author=Vogelzang,+M.&publication_year=2013&journal=Transp.+Res.+Part+F+Traffic+Psychol.+Behav.&volume=18&pages=72%E2%80%9382&doi=10.1016/j.trf.2012.12.012)\] \[ [CrossRef](https://doi.org/10.1016/j.trf.2012.12.012)\]
05. Rousek, J.B.; Hallbeck, M.S. Improving and analyzing signage within a healthcare setting. Appl. Ergon. **2011**, 42, 771–784. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Improving+and+analyzing+signage+within+a+healthcare+setting&author=Rousek,+J.B.&author=Hallbeck,+M.S.&publication_year=2011&journal=Appl.+Ergon.&volume=42&pages=771%E2%80%93784&doi=10.1016/j.apergo.2010.12.004&pmid=21281930)\] \[ [CrossRef](https://doi.org/10.1016/j.apergo.2010.12.004)\] \[ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/21281930)\]
06. Ng, A.W.Y.; Chan, A.H.S. Visual and cognitive features on icon effectiveness. In Proceedings of the International Multiconference of Engineers and Computer Scientists, Newswood Limited, Hong Kong, China, 19–21 March 2008; pp. 19–21. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Visual+and+cognitive+features+on+icon+effectiveness&conference=Proceedings+of+the+International+Multiconference+of+Engineers+and+Computer+Scientists,+Newswood+Limited&author=Ng,+A.W.Y.&author=Chan,+A.H.S.&publication_year=2008&pages=19%E2%80%9321)\]
07. Chan, A.H.S.; Ng, A.W.Y. Investigation of guessability of industrial safety signs: Effects of prospective-user factors and cognitive sign features. Int. J. Ind. Ergon. **2010**, 40, 689–697. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Investigation+of+guessability+of+industrial+safety+signs:+Effects+of+prospective-user+factors+and+cognitive+sign+features&author=Chan,+A.H.S.&author=Ng,+A.W.Y.&publication_year=2010&journal=Int.+J.+Ind.+Ergon.&volume=40&pages=689%E2%80%93697&doi=10.1016/j.ergon.2010.05.002)\] \[ [CrossRef](https://doi.org/10.1016/j.ergon.2010.05.002)\]
08. McDougall, S.J.P.; De Bruijn, O.; Curry, M.B. Exploring the effects of icon characteristics on user performance: The role of icon concreteness, complexity, and distinctiveness. J. Exp. Psychol. Appl. **2000**, 6, 291\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Exploring+the+effects+of+icon+characteristics+on+user+performance:+The+role+of+icon+concreteness,+complexity,+and+distinctiveness&author=McDougall,+S.J.P.&author=De+Bruijn,+O.&author=Curry,+M.B.&publication_year=2000&journal=J.+Exp.+Psychol.+Appl.&volume=6&pages=291&doi=10.1037/1076-898X.6.4.291)\] \[ [CrossRef](https://doi.org/10.1037/1076-898X.6.4.291)\]
09. Ng, A.W.Y.; Chan, A.H.S. Participatory environmentally friendly message design: Influence of message features and user characteristics. Int. J. Environ. Res. Public Health **2020**, 17, 1353\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Participatory+environmentally+friendly+message+design:+Influence+of+message+features+and+user+characteristics&author=Ng,+A.W.Y.&author=Chan,+A.H.S.&publication_year=2020&journal=Int.+J.+Environ.+Res.+Public+Health&volume=17&pages=1353&doi=10.3390/ijerph17041353)\] \[ [CrossRef](https://doi.org/10.3390/ijerph17041353)\]
10. Chong, M. Development of candidate symbols for automobile functions. Final Rep. **1990**, 25, 1–32. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Development+of+candidate+symbols+for+automobile+functions&author=Chong,+M.&publication_year=1990&journal=Final+Rep.&volume=25&pages=1%E2%80%9332)\]
11. Westergren, A.J. Predicting Window Size Preferences: Commonness or Cognitive Evaluation? Honors Thesis, Ball State University, Muncie, IN, USA, 1988. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Predicting+Window+Size+Preferences:+Commonness+or+Cognitive+Evaluation?&author=Westergren,+A.J.&publication_year=1988)\]
12. Pariasa, I.G.; Rajeg, I.M.; Sosiowati, I.G.A.G. The Application of Metaphor Identification Procedure (Mip) And Conceptual Metaphor in Japanese Poetry. Doctoral Dissertation, Udayana University, Bali, Indonesia, 2017. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=The+Application+of+Metaphor+Identification+Procedure+(Mip)+And+Conceptual+Metaphor+in+Japanese+Poetry&author=Pariasa,+I.G.&author=Rajeg,+I.M.&author=Sosiowati,+I.G.A.G.&publication_year=2017)\]
13. Yan, W. Psychological Analysis of User Interface Design in Computer Software. J. Phys. Conf. Ser. **2020**, 1533, 022040\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Psychological+Analysis+of+User+Interface+Design+in+Computer+Software&author=Yan,+W.&publication_year=2020&journal=J.+Phys.+Conf.+Ser.&volume=1533&pages=022040&doi=10.1088/1742-6596/1533/2/022040)\] \[ [CrossRef](https://doi.org/10.1088/1742-6596/1533/2/022040)\]
14. Siswandari, Y.; Kim, W.; Xiong, S. Comprehension and redesign of recently introduced water-sport prohibitive symbols in South Korea. Int. J. Ind. Ergon. **2015**, 50, 196–205. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Comprehension+and+redesign+of+recently+introduced+water-sport+prohibitive+symbols+in+South+Korea&author=Siswandari,+Y.&author=Kim,+W.&author=Xiong,+S.&publication_year=2015&journal=Int.+J.+Ind.+Ergon.&volume=50&pages=196%E2%80%93205&doi=10.1016/j.ergon.2015.09.018)\] \[ [CrossRef](https://doi.org/10.1016/j.ergon.2015.09.018)\]
15. Green, P. Displays for automotive instrument panels: Production and rating symbols. HSRI Res. Rev. **1981**, 12, 1–12. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Displays+for+automotive+instrument+panels:+Production+and+rating+symbols&author=Green,+P.&publication_year=1981&journal=HSRI+Res.+Rev.&volume=12&pages=1%E2%80%9312)\]
16. Green, P. Debugging a symbol set for identifying displays: Production and screening studies. Final Rep. **1980**, 64, 1–116. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Debugging+a+symbol+set+for+identifying+displays:+Production+and+screening+studies&author=Green,+P.&publication_year=1980&journal=Final+Rep.&volume=64&pages=1%E2%80%93116)\]
17. Ng, A.W.Y.; Siu, K.W.M.; Chan, C.C.H. The effects of user factors and symbol referents on public symbol design using the stereotype production method. Appl. Ergon. **2012**, 43, 230–238. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=The+effects+of+user+factors+and+symbol+referents+on+public+symbol+design+using+the+stereotype+production+method&author=Ng,+A.W.Y.&author=Siu,+K.W.M.&author=Chan,+C.C.H.&publication_year=2012&journal=Appl.+Ergon.&volume=43&pages=230%E2%80%93238&doi=10.1016/j.apergo.2011.05.007&pmid=21621745)\] \[ [CrossRef](https://doi.org/10.1016/j.apergo.2011.05.007)\] \[ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/21621745)\]
18. Al-Madani, H.; Al-Janahi, A.R. Role of drivers’ personal characteristics in understanding traffic sign symbols. Accid. Anal. Prev. **2002**, 34, 185–196. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Role+of+drivers%E2%80%99+personal+characteristics+in+understanding+traffic+sign+symbols&author=Al-Madani,+H.&author=Al-Janahi,+A.R.&publication_year=2002&journal=Accid.+Anal.+Prev.&volume=34&pages=185%E2%80%93196&doi=10.1016/S0001-4575(01)00012-4)\] \[ [CrossRef](https://doi.org/10.1016/S0001-4575(01)00012-4)\]
19. Shorr, D.J.; Ezer, N.; Fisk, A.D.; Rogers, W.A. Comprehension of warning symbols by younger and older adults: Effects of visual degradation. In Proceedings of the Human Factors and Ergonomics Society Annual Meeting, San Antonio, TX, USA, 19–23 October 2009; SAGE Publications: Los Angeles, CA, USA; pp. 1598–1602.
20. Kim, S.; Ulfarsson, G.F.; Anton, K.R. Traffic sign comprehensibility in an aging society: A study of “photo-enforced traffic signal ahead” signage. Transp. Res. Rec. **2009**, 2096, 81–88. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Traffic+sign+comprehensibility+in+an+aging+society:+A+study+of+%E2%80%9Cphoto-enforced+traffic+signal+ahead%E2%80%9D+signage&author=Kim,+S.&author=Ulfarsson,+G.F.&author=Anton,+K.R.&publication_year=2009&journal=Transp.+Res.+Rec.&volume=2096&pages=81%E2%80%9388&doi=10.3141/2096-11)\] \[ [CrossRef](https://doi.org/10.3141/2096-11)\]
21. Ng, A.W.Y.; Siu, K.W.M.; Chan, C.C.H. Perspectives toward the stereotype production method for public symbol design: A case study of novice designers. Appl. Ergon. **2013**, 44, 65–72. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Perspectives+toward+the+stereotype+production+method+for+public+symbol+design:+A+case+study+of+novice+designers&author=Ng,+A.W.Y.&author=Siu,+K.W.M.&author=Chan,+C.C.H.&publication_year=2013&journal=Appl.+Ergon.&volume=44&pages=65%E2%80%9372&doi=10.1016/j.apergo.2012.04.011)\] \[ [CrossRef](https://doi.org/10.1016/j.apergo.2012.04.011)\]
22. Patel, G.; Mukhopadhyay, P. Ergonomic analysis and design intervention in symbols used in hospitals in central India. Appl. Ergon. **2021**, 94, 103410\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Ergonomic+analysis+and+design+intervention+in+symbols+used+in+hospitals+in+central+India&author=Patel,+G.&author=Mukhopadhyay,+P.&publication_year=2021&journal=Appl.+Ergon.&volume=94&pages=103410&doi=10.1016/j.apergo.2021.103410)\] \[ [CrossRef](https://doi.org/10.1016/j.apergo.2021.103410)\]
23. Ng, A.W.Y.; Chan, A.H.S. Mental models of construction workers for safety-sign representation. J. Constr. Eng. Manag. **2017**, 143, 04016091\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Mental+models+of+construction+workers+for+safety-sign+representation&author=Ng,+A.W.Y.&author=Chan,+A.H.S.&publication_year=2017&journal=J.+Constr.+Eng.+Manag.&volume=143&pages=04016091&doi=10.1061/(ASCE)CO.1943-7862.0001221)\] \[ [CrossRef](https://doi.org/10.1061/(ASCE)CO.1943-7862.0001221)\]
24. Lesch, M.F. A comparison of two training methods for improving warning symbol comprehension. Appl. Ergon. **2008**, 39, 135–143. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=A+comparison+of+two+training+methods+for+improving+warning+symbol+comprehension&author=Lesch,+M.F.&publication_year=2008&journal=Appl.+Ergon.&volume=39&pages=135%E2%80%93143&doi=10.1016/j.apergo.2007.07.002)\] \[ [CrossRef](https://doi.org/10.1016/j.apergo.2007.07.002)\]
25. Lesch, M.F.; Powell, W.R.; Horrey, W.J.; Wogalter, M.S. The use of contextual cues to improve warning symbol comprehension: Making the connection for older adults. Ergonomics **2013**, 56, 1264–1279. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=The+use+of+contextual+cues+to+improve+warning+symbol+comprehension:+Making+the+connection+for+older+adults&author=Lesch,+M.F.&author=Powell,+W.R.&author=Horrey,+W.J.&author=Wogalter,+M.S.&publication_year=2013&journal=Ergonomics&volume=56&pages=1264%E2%80%931279&doi=10.1080/00140139.2013.802019&pmid=23767856)\] \[ [CrossRef](https://doi.org/10.1080/00140139.2013.802019)\] \[ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/23767856)\]
26. Wisniewski, E.C.; Isaacson, J.J.; Hall, S.M. Techniques for assessing safety symbol comprehension: Web-based vs. in-person questionnaire administration. In Proceedings of the Human Factors and Ergonomics Society Annual Meeting, San Francisco, CA, USA, 16–20 October 2006; SAGE Publications: Los Angeles, CA, USA; pp. 2207–2211.
27. Kowalewski, S.; Kluge, J.; Ziefle, M. Integrating potential users into the development of a medical wrist watch in four steps. In Proceedings of the International Conference on Human-Computer Interaction, Las Vegas, NV, USA, 21–26 July 2013; Springer: Berlin/Heidelberg, Germany; pp. 183–186.
28. Salman, Y.B.; Kim, Y.H.; Cheng, H.I. Senior—Friendly icon design for the mobile phone. In Proceedings of the 6th International Conference on Digital Content, Multimedia Technology and Its Applications, Seoul, Korea, 16–18 August 2010; IEEE: Piscataway, NJ, USA; pp. 103–108.
29. Semin, G.R.; Smith, E.R. Socially situated cognition in perspective. Soc. Cogn. **2013**, 31, 125\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Socially+situated+cognition+in+perspective&author=Semin,+G.R.&author=Smith,+E.R.&publication_year=2013&journal=Soc.+Cogn.&volume=31&pages=125&doi=10.1521/soco.2013.31.2.125)\] \[ [CrossRef](https://doi.org/10.1521/soco.2013.31.2.125)\]
30. Schwarz, N. Situated cognition and the wisdom of feelings: Cognitive tuning. Wisdom Feel. **2002**, 1, 144–166. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Situated+cognition+and+the+wisdom+of+feelings:+Cognitive+tuning&author=Schwarz,+N.&publication_year=2002&journal=Wisdom+Feel.&volume=1&pages=144%E2%80%93166)\]
31. Rambusch, J.; Ziemke, T. The role of embodiment in situated learning. In Proceedings of the 27th Annual Conference of the Cognitive Science Society, Stresa, Italy, 21–23 July 2005; Lawrence Erlbaum: Mahwah, NJ, USA; pp. 1803–1808.
32. Echterhoff, G.; Kopietz, R.; Higgins, E.T. Adjusting shared reality: Communicators’ memory changes as their connection with their audience changes. Soc. Cogn. **2013**, 31, 162\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Adjusting+shared+reality:+Communicators%E2%80%99+memory+changes+as+their+connection+with+their+audience+changes&author=Echterhoff,+G.&author=Kopietz,+R.&author=Higgins,+E.T.&publication_year=2013&journal=Soc.+Cogn.&volume=31&pages=162&doi=10.1521/soco.2013.31.2.162)\] \[ [CrossRef](https://doi.org/10.1521/soco.2013.31.2.162)\]
33. Wilson, R.A.; Clark, A. How to situate cognition: Letting nature take its course. Camb. Handb. Situated Cogn. **2008**, 55–77. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=How+to+situate+cognition:+Letting+nature+take+its+course&author=Wilson,+R.A.&author=Clark,+A.&publication_year=2008&journal=Camb.+Handb.+Situated+Cogn.&pages=55%E2%80%9377)\]
34. Stanton, N.A.; Salmon, P.M.; Walker, G.H.; Jenkins, D.P. Is situation awareness all in the mind? Theor. Issues Ergon. Sci. **2010**, 11, 29–40. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Is+situation+awareness+all+in+the+mind?&author=Stanton,+N.A.&author=Salmon,+P.M.&author=Walker,+G.H.&author=Jenkins,+D.P.&publication_year=2010&journal=Theor.+Issues+Ergon.+Sci.&volume=11&pages=29%E2%80%9340&doi=10.1080/14639220903009938)\] \[ [CrossRef](https://doi.org/10.1080/14639220903009938)\]
35. Hutchins, E. How a cockpit remembers its speeds. Cogn. Sci. **1995**, 19, 265–288. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=How+a+cockpit+remembers+its+speeds&author=Hutchins,+E.&publication_year=1995&journal=Cogn.+Sci.&volume=19&pages=265%E2%80%93288&doi=10.1207/s15516709cog1903_1)\] \[ [CrossRef](https://doi.org/10.1207/s15516709cog1903_1)\]
36. Rizzolatti, G.; Fadiga, L.; Fogassi, L.; Gallese, V. 14 from mirror neurons to imitation: Facts and speculations. Imitative Mind Dev. Evol. Brain Bases **2002**, 6, 247–266. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=14+from+mirror+neurons+to+imitation:+Facts+and+speculations&author=Rizzolatti,+G.&author=Fadiga,+L.&author=Fogassi,+L.&author=Gallese,+V.&publication_year=2002&journal=Imitative+Mind+Dev.+Evol.+Brain+Bases&volume=6&pages=247%E2%80%93266)\]
37. Shen, Y.C.; Lin, H.Y.; Chou, C.Y.; Wu, P.H.; Yang, W.H. “Yes, I know you”: The role of source familiarity in the relationship between service adaptive behavior and customer satisfaction. J. Serv. Theory Pract. **2022**. ahead of print. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=%E2%80%9CYes,+I+know+you%E2%80%9D:+The+role+of+source+familiarity+in+the+relationship+between+service+adaptive+behavior+and+customer+satisfaction&author=Shen,+Y.C.&author=Lin,+H.Y.&author=Chou,+C.Y.&author=Wu,+P.H.&author=Yang,+W.H.&publication_year=2022&journal=J.+Serv.+Theory+Pract.&doi=10.1108/JSTP-01-2022-0017)\] \[ [CrossRef](https://doi.org/10.1108/JSTP-01-2022-0017)\]
38. Zwaan, R.A. Embodied cognition, perceptual symbols, and situation models. Discourse Process. **1999**, 28, 81–88. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Embodied+cognition,+perceptual+symbols,+and+situation+models&author=Zwaan,+R.A.&publication_year=1999&journal=Discourse+Process.&volume=28&pages=81%E2%80%9388&doi=10.1080/01638539909545070)\] \[ [CrossRef](https://doi.org/10.1080/01638539909545070)\]
39. Shen, Z.; Xue, C.; Wang, H. Effects of users’ familiarity with the objects depicted in icons on the cognitive performance of icon identification. I-Perception **2018**, 9, 2041669518780807\. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Effects+of+users%E2%80%99+familiarity+with+the+objects+depicted+in+icons+on+the+cognitive+performance+of+icon+identification&author=Shen,+Z.&author=Xue,+C.&author=Wang,+H.&publication_year=2018&journal=I-Perception&volume=9&pages=2041669518780807&doi=10.1177/2041669518780807&pmid=29977490)\] \[ [CrossRef](https://doi.org/10.1177/2041669518780807)\] \[ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/29977490)\]
40. Schröder, S.; Ziefle, M. Effects of icon concreteness and complexity on semantic transparency: Younger vs. older users. In Proceedings of the International Conference on Computers for Handicapped Persons, Linz, Austria, 9–11 July 2008; Springer: Berlin/Heidelberg, Germany; pp. 90–97.
41. Picard, D.; Boulhais, M. Sex differences in expressive drawing. Personal. Individ. Differ. **2011**, 51, 850–855. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Sex+differences+in+expressive+drawing&author=Picard,+D.&author=Boulhais,+M.&publication_year=2011&journal=Personal.+Individ.+Differ.&volume=51&pages=850%E2%80%93855&doi=10.1016/j.paid.2011.07.017)\] \[ [CrossRef](https://doi.org/10.1016/j.paid.2011.07.017)\]
42. Jones, J.E. A Descriptive Study of Elderly art Students and Implications for Art Education. Ph.D. Thesis, University of Oregon, Eugene, OR, USA, 1976. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=A+Descriptive+Study+of+Elderly+art+Students+and+Implications+for+Art+Education&author=Jones,+J.E.&publication_year=1976)\]
43. ISO 9186; Graphical Symbols—Test Methods for Judged Comprehensibility and for Comprehension. International Organization for Standardization: Geneva, Switzerland, 2001.
44. Foster, J.J.; Afzalnia, M.R. International assessment of judged symbol comprehensibility. Int. J. Psychol. **2005**, 40, 169–175. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=International+assessment+of+judged+symbol+comprehensibility&author=Foster,+J.J.&author=Afzalnia,+M.R.&publication_year=2005&journal=Int.+J.+Psychol.&volume=40&pages=169%E2%80%93175&doi=10.1080/00207590444000258)\] \[ [CrossRef](https://doi.org/10.1080/00207590444000258)\]
45. GB/T 10001.6-2021; Public Information Graphical Symbols. China National Institute of Standardization: Beijing, China, 2021.
46. Malterud, K.; Siersma, V.D.; Guassora, A.D. Sample Size in Qualitative Interview Studies: Guided by Information Power. Qual. Health Res. **2016**, 26, 1753–1760. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Sample+Size+in+Qualitative+Interview+Studies:+Guided+by+Information+Power&author=Malterud,+K.&author=Siersma,+V.D.&author=Guassora,+A.D.&publication_year=2016&journal=Qual.+Health+Res.&volume=26&pages=1753%E2%80%931760&doi=10.1177/1049732315617444)\] \[ [CrossRef](https://doi.org/10.1177/1049732315617444)\]
47. Smith, E.R.; Collins, E. Situated cognition. Mind Context **2010**, 7, 126–145. \[ [Google Scholar](https://scholar.google.com/scholar_lookup?title=Situated+cognition&author=Smith,+E.R.&author=Collins,+E.&publication_year=2010&journal=Mind+Context&volume=7&pages=126%E2%80%93145)\]

**Figure 1.**
Symbol design framework based on the situational cognitive commonness.

**Figure 1.**
Symbol design framework based on the situational cognitive commonness.

**Figure 2.**
Healthcare wayfinding signs developed by the National Standard of the People’s Republic of China GB/T 10001.6-2021.

**Figure 2.**
Healthcare wayfinding signs developed by the National Standard of the People’s Republic of China GB/T 10001.6-2021.

**Figure 3.**
Presentation of a representative experimental material. Note: The experimental material for users’ drawing of symbol for the “internal medicine department” was taken as an example.

**Figure 3.**
Presentation of a representative experimental material. Note: The experimental material for users’ drawing of symbol for the “internal medicine department” was taken as an example.

**Figure 4.**
Extraction and prototyping of healthcare symbols for the “internal medicine department” and the development of a design.

**Figure 4.**
Extraction and prototyping of healthcare symbols for the “internal medicine department” and the development of a design.

**Figure 5.**
The designs of healthcare wayfinding signs in this study.

**Figure 5.**
The designs of healthcare wayfinding signs in this study.

**Figure 6.**
Examples of symbol materials for the judgment test. Note: The materials for the “internal medicine department” here are taken as examples.

**Figure 6.**
Examples of symbol materials for the judgment test. Note: The materials for the “internal medicine department” here are taken as examples.

**Table 1.**
Paired t-test results of symbols.

**Table 1.**
Paired t-test results of symbols.

| Symbol | Degree of Understanding (Mean ± Standard Deviation) | Difference | t |
| :-: | :-: | :-: | :-: |
| Design | Existing |
| :-: | :-: |
| Internal medicine department | 73.14 ± 20.95 | 53.26 ± 24.96 | 19.88 | 6.033 \*\*\* |
| Surgery department | 65.82 ± 21.15 | 50.38 ± 21.68 | 15.44 | 6.010 \*\*\* |
| Radiology department | 66.62 ± 24.55 | 50.60 ± 25.19 | 16.03 | 4.093 \*\*\* |
| Nurse | 64.09 ± 27.02 | 50.69 ± 24.79 | 13.4 | 3.212 \*\* |
| Observation room | 70.25 ± 23.60 | 55.55 ± 25.07 | 14.7 | 3.976 \*\*\* |
| Gynecology department | 61.64 ± 24.50 | 55.30 ± 22.16 | 6.34 | 2.039 \* |
| Western pharmacy | 64.47 ± 21.82 | 63.30 ± 25.29 | 1.17 | 0.363 |
| TCM pharmacy | 63.82 ± 22.30 | 63.82 ± 23.48 | 0 | 0 |
| Ultrasound room | 59.87 ± 24.13 | 65.09 ± 26.62 | −5.22 | −1.295 |

\\* p < 0.05, \*\* p < 0.01, and \*\*\* p < 0.001 significance differences.

|     |     |
| --- | --- |
|  | **Publisher’s Note:** MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations. |

© 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license ( [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)).

## Share and Cite

[Email](mailto:?&subject=From%20MDPI%3A%20%22A%20Design%20Framework%20of%20Medical%20Wayfinding%20Signs%20for%20the%20Elderly%3A%20Based%20on%20the%20Situational%20Cognitive%20Commonness%22&body=https://www.mdpi.com/1906194%3A%0A%0AA%20Design%20Framework%20of%20Medical%20Wayfinding%20Signs%20for%20the%20Elderly%3A%20Based%20on%20the%20Situational%20Cognitive%20Commonness%0A%0AAbstract%3A%20Older%20people%20in%20China%20have%20a%20poor%20understanding%20of%20hospital%20signage.%20To%20address%20this%20problem%2C%20in%20this%20study%2C%20we%20combined%20the%20theories%20of%20situated%20cognition%20and%20cognitive%20commonness%20in%20order%20to%20introduce%20the%20three%20main%20factors%20that%20affect%20the%20generation%20of%20situational%20cognitive%20commonness%3A%20composition%20of%20the%20situation%2C%20familiarity%2C%20and%20concreteness.%20We%20used%20these%20theories%20to%20construct%20a%20methodological%20framework%20for%20the%20design%20of%20geriatric%20hospital%20wayfinding%20signs%20that%20were%20based%20on%20situational%20cognitive%20commonness.%20The%20design%20of%20nine%20healthcare%20signs%20for%20Chinese%20national%20standards%20were%20used%20as%20examples%20in%20the%20study.%20First%2C%20users%20who%20were%20familiar%20with%20medical%20scenarios%20were%20asked%20to%20draw%20concrete%20cognitive%20conception%20graphics%20for%20the%20purposes%20of%20individual%20wayfinding%20targets%20from%20both%20physical%20and%20social%20situations.%20Next%2C%20we%20coded%20and%20grouped%20the%20generated%20graphics%20based%20on%20their%20situational%20features%20in%20order%20to%20extract%20groups%20of%20representative%20common%20graphics.%20Finally%2C%20we%20reorganized%20the%20common%20graphics%20and%20developed%20concrete%20designs%2C%20which%20were%20tested%20by%20the%20judgment%20test.%20The%20wayfinding%20signs%20designed%20according%20to%20the%20methodological%20framework%20of%20this%20study%20effectively[...] "Email")[LinkedIn](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.mdpi.com%2F1906194&title=A%20Design%20Framework%20of%20Medical%20Wayfinding%20Signs%20for%20the%20Elderly%3A%20Based%20on%20the%20Situational%20Cognitive%20Commonness%26source%3Dhttps%3A%2F%2Fwww.mdpi.com%26summary%3DOlder%20people%20in%20China%20have%20a%20poor%20understanding%20of%20hospital%20signage.%20To%20address%20this%20problem%2C%20in%20this%20study%2C%20we%20combined%20the%20theories%20of%20situated%20cognition%20and%20cognitive%20commonness%20in%20order%20to%20introduce%20the%20three%20main%20factors%20that%20affect%20the%20%5B...%5D "LinkedIn")[facebook](http://www.facebook.com/sharer.php?u=https://www.mdpi.com/1906194 "facebook")[Reddit](http://www.reddit.com/submit?url=https://www.mdpi.com/1906194 "Reddit")[Mendeley](http://www.mendeley.com/import/?url=https://www.mdpi.com/1906194 "Mendeley")

**MDPI and ACS Style**

Wu, J.; Liu, X.; Lu, C.; Yu, S.; Jiao, D.; Ye, X.; Zhu, Y.
A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness. _Int. J. Environ. Res. Public Health_ **2022**, _19_, 13885.
https://doi.org/10.3390/ijerph192113885

**AMA Style**

Wu J, Liu X, Lu C, Yu S, Jiao D, Ye X, Zhu Y.
A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness. _International Journal of Environmental Research and Public Health_. 2022; 19(21):13885.
https://doi.org/10.3390/ijerph192113885

**Chicago/Turabian Style**

Wu, Jianfeng, Xinyu Liu, Chunfu Lu, Shihan Yu, Dongfang Jiao, Xinyu Ye, and Yuqing Zhu.
2022\. "A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness" _International Journal of Environmental Research and Public Health_ 19, no. 21: 13885.
https://doi.org/10.3390/ijerph192113885

**APA Style**

Wu, J., Liu, X., Lu, C., Yu, S., Jiao, D., Ye, X., & Zhu, Y.

(2022). A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness. _International Journal of Environmental Research and Public Health_, _19_(21), 13885.
https://doi.org/10.3390/ijerph192113885

Note that from the first issue of 2016, this journal uses article numbers instead of page numbers. See further details [here](https://www.mdpi.com/about/announcements/784).

## Article Metrics

No

No

### Article Access Statistics

For more information on the journal statistics, click [here](https://www.mdpi.com/journal/ijerph/stats).

Multiple requests from the same IP address are counted as one view.

Zoom\| Orient \| As Lines \| As Sticks \| As Cartoon \| As Surface \|Previous Scene\|Next Scene

## Cite

Export citation file:
BibTeX \|
EndNote \|
RIS

**MDPI and ACS Style**

Wu, J.; Liu, X.; Lu, C.; Yu, S.; Jiao, D.; Ye, X.; Zhu, Y.
A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness. _Int. J. Environ. Res. Public Health_ **2022**, _19_, 13885.
https://doi.org/10.3390/ijerph192113885

**AMA Style**

Wu J, Liu X, Lu C, Yu S, Jiao D, Ye X, Zhu Y.
A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness. _International Journal of Environmental Research and Public Health_. 2022; 19(21):13885.
https://doi.org/10.3390/ijerph192113885

**Chicago/Turabian Style**

Wu, Jianfeng, Xinyu Liu, Chunfu Lu, Shihan Yu, Dongfang Jiao, Xinyu Ye, and Yuqing Zhu.
2022\. "A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness" _International Journal of Environmental Research and Public Health_ 19, no. 21: 13885.
https://doi.org/10.3390/ijerph192113885

**APA Style**

Wu, J., Liu, X., Lu, C., Yu, S., Jiao, D., Ye, X., & Zhu, Y.

(2022). A Design Framework of Medical Wayfinding Signs for the Elderly: Based on the Situational Cognitive Commonness. _International Journal of Environmental Research and Public Health_, _19_(21), 13885.
https://doi.org/10.3390/ijerph192113885

Note that from the first issue of 2016, this journal uses article numbers instead of page numbers. See further details [here](https://www.mdpi.com/about/announcements/784).

_clear_

We use cookies on our website to ensure you get the best experience.

Read more about our cookies [here](https://www.mdpi.com/about/privacy).

[Accept](https://www.mdpi.com/accept_cookies)

## Share Link

[Email](mailto:?&subject=From%20MDPI%3A%20%22A%20Design%20Framework%20of%20Medical%20Wayfinding%20Signs%20for%20the%20Elderly%3A%20Based%20on%20the%20Situational%20Cognitive%20Commonness%22&body=https://www.mdpi.com/1906194%3A%0A%0AA%20Design%20Framework%20of%20Medical%20Wayfinding%20Signs%20for%20the%20Elderly%3A%20Based%20on%20the%20Situational%20Cognitive%20CommonnessOlder%20people%20in%20China%20have%20a%20poor%20understanding%20of%20hospital%20signage.%20To%20address%20this%20problem%2C%20in%20this%20study%2C%20we%20combined%20the%20theories%20of%20situated%20cognition%20and%20cognitive%20commonness%20in%20order%20to%20introduce%20the%20three%20main%20factors%20that%20affect%20the%20generation%20of%20situational%20cognitive%20commonness%3A%20composition%20of%20the%20situation%2C%20familiarity%2C%20and%20concreteness.%20We%20used%20these%20theories%20to%20construct%20a%20methodological%20framework%20for%20the%20design%20of%20geriatric%20hospital%20wayfinding%20signs%20that%20were%20based%20on%20situational%20cognitive%20commonness.%20The%20design%20of%20nine%20healthcare%20signs%20for%20Chinese%20national%20standards%20were%20used%20as%20examples%20in%20the%20study.%20First%2C%20users%20who%20were%20familiar%20with%20medical%20scenarios%20were%20asked%20to%20draw%20concrete%20cognitive%20conception%20graphics%20for%20the%20purposes%20of%20individual%20wayfinding%20targets%20from%20both%20physical%20and%20social%20situations.%20Next%2C%20we%20coded%20and%20grouped%20the%20generated%20graphics%20based%20on%20their%20situational%20features%20in%20order%20to%20extract%20groups%20of%20representative%20common%20graphics.%20Finally%2C%20we%20reorganized%20the%20common%20graphics%20and%20developed%20concrete%20designs%2C%20which%20were%20tested%20by%20the%20judgment%20test.%20The%20wayfinding%20signs%20designed%20according%20to%20the%20methodological%20framework%20of%20this%20study%20effectively%20improved%20the[...] "Email")[Twitter](https://x.com/intent/tweet?text=A+Design+Framework+of+Medical+Wayfinding+Signs+for+the+Elderly%3A+Based+on+the+Situational+Cognitive+Commonness&hashtags=mdpiijerph&url=https%3A%2F%2Fwww.mdpi.com%2F1906194&via=IJERPH_MDPI "Twitter")[LinkedIn](http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.mdpi.com%2F1906194&title=A%20Design%20Framework%20of%20Medical%20Wayfinding%20Signs%20for%20the%20Elderly%3A%20Based%20on%20the%20Situational%20Cognitive%20Commonness%26source%3Dhttps%3A%2F%2Fwww.mdpi.com%26summary%3DOlder%20people%20in%20China%20have%20a%20poor%20understanding%20of%20hospital%20signage.%20To%20address%20this%20problem%2C%20in%20this%20study%2C%20we%20combined%20the%20theories%20of%20situated%20cognition%20and%20cognitive%20commonness%20in%20order%20to%20introduce%20the%20three%20main%20factors%20that%20affect%20the%20%5B...%5D "LinkedIn")[facebook](http://www.facebook.com/sharer.php?u=https://www.mdpi.com/1906194 "facebook")[Reddit](http://www.reddit.com/submit?url=https://www.mdpi.com/1906194 "Reddit")[Mendeley](http://www.mendeley.com/import/?url=https://www.mdpi.com/1906194 "Mendeley")[CiteULike](http://www.citeulike.org/posturl?url=https://www.mdpi.com/1906194 "CiteULike")

Copy

_clear_

## Share

https://www.mdpi.com/1906194

_clear_

[Back to TopTop](https://www.mdpi.com/1660-4601/19/21/13885#)

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
- 已精读来源数量：10 个
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
