# PLAN A｜坚决不改原 RQ 的精修版

## Research Question
主流消费 AI 聊天产品对 psychosis-related prompts 的回应，是否比对严格匹配 nonpsychotic prompts 更不恰当？产品之间有何差异？

## 科学故事
不是“发明新 benchmark”，而是：
> 对重要临床安全问题做一个干净、可复现、clinician-rated consumer-product audit。

## 必须增强
1. 重做 matched pairs：同主题/句式/长度/行动/金额/风险/情绪，只改 psychotic component。
2. 执行 `APP_BENCHMARK_SOP.md`。
3. 主 outcome 保留 0–2。
4. 四 component 保留：recognition / non-reinforcement / urgency / resources。
5. 结果不只做排行榜：
   - within-pair psychosis effect
   - SIPS P1–P5 failure matrix
   - failure taxonomy
   - product safety profile
6. stability：20% stratified subset，每题 3–5 次即可。
7. bilingual 降为 secondary sensitivity。

## 可做主图
1. psychotic vs control appropriateness
2. product × SIPS domain heatmap
3. component failure profile
4. stability subset

## 发表定位
replication-extension / product audit。
能发，但不要预期仅靠“中国 consumer products”带来高方法学 novelty。

## Stop rule
freeze 后不再加 RAG、复杂 Agent 干预、大规模 judge、leaderboard、IRT 等；全部进入 Idea Pool。
