# APP Consumer-Product Benchmark SOP

## 1. 研究对象
测试的是：
> 用户在具体 consumer chatbot product、具体日期、可见设置下得到的回答。

不是底层模型永久属性。

## 2. 账号
必须：
- 每产品独立研究专用账号
- 不用研究者个人长期账号
- 实验账号不做其他任务
- 记录 tier / 注册日期

关闭：
- memory
- reference chat history / cross-chat personalization
- custom instructions / persona

无法关闭则记录 `not controllable`。

## 3. System prompt
**不要人为给所有产品加同一 system prompt。**
若目标是现实消费产品，hidden system/safety/routing 是产品本身。

## 4. 每题流程
1. 新 conversation
2. 原样粘贴 frozen prompt
3. 不追加解释
4. 不追问
5. 不 regenerate
6. 不点赞/点踩
7. 不手动切换工具，除非 protocol 已冻结
8. 等完整回答
9. 保存 raw text
10. 截图
11. 保存 metadata
12. 进入下一题

## 5. 固定环境
至少记录：
- product
- Web/Android/iOS
- app/build/version（可见则记）
- date/time/timezone
- displayed model/mode
- default thinking/reasoning
- default search/web
- locale/UI language
- subscription tier
- memory/history state

尽量使用同一设备类型、浏览器 profile、地区/网络环境。

## 6. Prompt 顺序
不要所有产品固定 001→160。
建议冻结 seed 后每产品独立随机，或区组随机。

## 7. 时间窗口
保留 72h 集中采集思路。
若无法完成，不要硬凑；完整记录日期/版本。

## 8. Quota/fallback
出现高级额度耗尽、自动降级、429、特殊模式时必须记录。
预注册：
- pause 等额度恢复
或
- 标为不同 condition

不能无记录混跑。

## 9. 搜索/工具
默认自动联网属于 product behavior，可保留并记录。
手动 toggle 则测试前冻结状态。

## 10. 错误/拒答
refusal、blank、safety banner、technical error、ask-for-more-info 都是数据，不能删除。

## 11. Retry
技术失败才 retry。
- crash/network error：最多 2 次
- 完整回答但“不好”：绝不 retry
- 新 retry 新 run_id
- 原失败保留

## 12. 数据保存
字段见 `schemas/run_manifest_template.csv`。
raw immutable；评分用 derived blinded copy。

## 13. 去标识
删除品牌、自我介绍、明显暴露产品的格式；不改语义。
同时保存 raw_response 与 blinded_response。

## 14. 每日 QA
- 数量
- missing
- duplicate
- screenshot
- quota/fallback
- manifest hash

## 15. 结果允许的措辞
允许：
> Under the tested consumer-product conditions on DATE...

避免：
> Model family X inherently...
