# DECISIONS LOG

## D-001｜前期必须充分 brainstorm
**状态：Frozen principle**

发散是优势，不是缺陷。禁止用 scope control 过早杀死 idea generation。

流程：Diverge → Preserve → Falsify → Prioritize → Freeze。

## D-002｜未进入当前主线的好 idea 必须保留
**状态：Frozen principle**

落点：`IDEA_POOL.md`。

## D-003｜APP 定义为 consumer chatbot product audit
**状态：Frozen for current execution candidate**

禁止把 APP 结果直接表述为固定底模属性。

## D-004｜APP 使用研究专用干净账号
**状态：Frozen**

- 新研究账号
- 不做其他聊天
- 关闭 memory / 引用历史
- custom instructions 为空
- 每题新会话

## D-005｜不统一注入自定义 system prompt
**状态：Frozen**

若研究目标是普通用户的真实产品体验，hidden system/safety/routing 是产品本身。

## D-006｜APP 与 API 共用 benchmark schema，但分开解释
**状态：Frozen**

APP = product layer  
API = model/config layer

## D-007｜Evolvent/BenchRouter 可用于工程化，不视为 scientific novelty
**状态：Frozen principle**

## D-008｜原学生 RQ 本身可以发表
**状态：Current assessment**

不能把“有更高级方案”误写成“原方案不能发”。

## D-009｜原题继续时最优先修 matched-control confounding
**状态：Implemented in A-v0.1**

minimal pair：只改变 psychotic component；风险、金额、行动、语气、长度尽量不变。

## D-010｜“中国版/中文”不再作为主要 novelty
**状态：Current literature-based assessment**

可作为 setting / external validity / cultural context。

## D-011｜路线执行结构
**状态：Operationally frozen candidate**

- A：主 product-audit paper
- B：A 中的 nested active enhancement
- C：独立 fixed-API benchmark track

## D-012｜判断“改进”还是“新项目”
**状态：Frozen heuristic**

> 如果拿掉这个建议，原 RQ 还一样吗？

Yes → protocol improvement  
No → extension / substudy / new study

## D-013｜公开仓库内容边界
**状态：Frozen boundary**

`CochraneK/Pair` 可公开展示协作安全的研究材料，但不提交账号凭据、原始截图、潜在患者/受试者数据、以及已明确要求个人保留的方向。第三方原始文档在未确认再分发权限前不直接公开二进制副本。

## D-014｜Assumption Mode：默认临床审题可接受并继续推进
**日期：2026-10-03**  
**状态：User-authorized workflow assumption**

用户明确要求：默认医生审核没有问题，继续推进。

执行含义：
- 不再让临床审题阻塞题库冻结、预注册草案、runner、随机化、评分和统计工具开发；
- A/B/C 均推进到 collection-ready candidate。

证据边界：
- 这不是“真实精神科医生已经签字”的证据；
- 不得在论文/伦理/注册材料中伪造 clinician validation；
- 若以后获得真实临床复核，单独保存并升级版本。

详见 `ASSUMPTION_MODE_2026-10-03.md`。

## D-015｜当前执行规模冻结
**日期：2026-10-03**  
**状态：Candidate execution freeze**

- A：5 consumer products；160 primary prompts + 16 psychosis stability subset × 2 additional repeats → 960 outputs
- B：3 consumer products × 36 prompts × 3 runs → 324 outputs
- C：3 fixed API configs × 64 prompts × 3 runs → 576 outputs
- 全部执行合计：1,860 outputs

随机种子、产品/config ID 与 schedule 规则写入 `execution/EXECUTION_PLAN_v0.1.md` 和 `scripts/build_collection_schedules.py`。

## D-016｜C 的固定 API candidate set
**日期：2026-10-03**  
**状态：Candidate freeze; reverify immediately before run**

- DeepSeek: `deepseek-flash` / V4.1-Flash
- Qwen: `qwen3.8-max-0902`
- Doubao: `doubao-seed-2-1-pro-260915`

统一原则：单轮、无 system prompt、关闭 tools/web、reasoning-enabled high candidate；保存 exact request JSON hash 与 provider response metadata。

## D-017｜停止继续扩题，进入真实执行
**状态：Frozen stop rule**

除非发现 validity-breaking error，否则现在不再新增核心维度、题目家族、模型或评分指标。

新的好 idea → `IDEA_POOL.md` / future work。

下一阶段只允许：
1. 伦理/预注册；
2. technical smoke pilot；
3. frozen collection；
4. blind rating；
5. frozen statistics；
6. reporting/reviewer audit。
