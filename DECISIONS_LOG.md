# DECISIONS LOG

## D-001｜前期必须充分 brainstorm
**状态：Frozen principle**

发散是优势，不是缺陷。禁止用 scope control 过早杀死 idea generation。

流程：Diverge → Preserve → Falsify → Prioritize → Freeze。

## D-002｜未进入当前主线的好 idea 必须保留
**状态：Frozen principle**

落点：`IDEA_POOL.md`。

## D-003｜APP 定义为 consumer chatbot product audit
**状态：Recommended / data collection 前冻结**

禁止把 APP 结果直接表述为固定底模属性。

## D-004｜APP 使用研究专用干净账号
**状态：原 protocol 已有，继续保留**

- 新研究账号
- 不做其他聊天
- 关闭 memory / 引用历史
- custom instructions 为空
- 每题新会话

## D-005｜不统一注入自定义 system prompt
**状态：Recommended**

若研究目标是普通用户的真实产品体验，hidden system/safety/routing 是产品本身。

## D-006｜APP 与 API 共用 benchmark schema，但分开解释
**状态：Recommended**

APP = product layer  
API = model/config layer

## D-007｜Evolvent/BenchRouter 可用于工程化，不视为 scientific novelty
**状态：Recommended**

API/local 阶段可接；APP 需独立 capture pipeline。

## D-008｜原学生 RQ 本身可以发表
**状态：Current assessment**

不能把“有更高级方案”误写成“原方案不能发”。

## D-009｜原题继续时最优先修 matched-control confounding
**状态：High priority**

minimal pair：只改变 psychotic component；风险、金额、行动、语气、长度尽量不变。

## D-010｜“中国版/中文”不再作为主要 novelty
**状态：Current literature-based assessment**

可作为 setting / external validity / cultural context。

## D-011｜三条路线并存
**状态：Pending team decision**

- A：原题精修
- B：原题 + 嵌套增强（当前默认推荐）
- C：正式换题

## D-012｜判断“改进”还是“新项目”
**状态：Frozen heuristic**

> 如果拿掉这个建议，原 RQ 还一样吗？

Yes → protocol improvement  
No → extension / substudy / new study

## D-013｜公开仓库内容边界
**状态：Frozen boundary**

`CochraneK/Pair` 可公开展示协作安全的研究材料，但不提交账号凭据、原始截图、潜在患者/受试者数据、以及已明确要求个人保留的方向。第三方原始文档在未确认再分发权限前不直接公开二进制副本。
