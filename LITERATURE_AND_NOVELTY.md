# 文献版图与创新性评估

**检索更新时间：2026-10-03**

这是一份 publication-oriented landscape，不是 PRISMA 系统综述。任何“首次/无人做过”在投稿前必须再次查新。

## 1. 与原方案最直接的前作

### Shen et al., JAMA Psychiatry, 2026
- 79 psychotic + 79 matched control prompts
- 3 个 ChatGPT product versions
- 单轮 isolated sessions
- clinician 0–2 appropriateness
- proportional odds

**含义：**原学生方案明显属于 replication/extension。换成中国消费产品可以发表，但方法学首创有限。

## 2. psychosis/delusion safety 已经有人做的部分

### psychosis-bench / The Psychogenic Machine (2025 preprint)
- 16 个 12-turn scenarios
- explicit / implicit
- DCS / HES / SIS
- 8 个模型

已占：多轮升级、强化妄想、伤害支持、安全介入这些核心 benchmark 思路。

### LLM Spirals of Delusion (2026)
- API vs chat interface
- 20-turn conversations
- human + LLM graders
- 时间漂移/接口差异

已占：“APP vs API 本身就是创新”。

### DelusionEval (2026 preprint)
- 589 unique conversation histories
- 12,591 messages
- harm-derived/naturalistic context

已占：真实伤害相关 histories / context-length risk。

## 3. 泛精神卫生 benchmark

- **PsyEval**, npj Mental Health Research, 2026
- **PsychiatryBench**, npj Digital Medicine, 2026 — 5,188 expert-annotated items / 11 tasks
- **MentalBench-100k / MentalAlign-70k**, EACL 2026
- **Health-ORSC-Bench**, Findings ACL 2026 — 31,920 boundary prompts / 30 models
- **PsychEthicsBench**, Findings ACL 2026
- **Safe-Psych**, 2026 preprint — sequential evidence / DIAGNOSE-CLARIFY-ABSTAIN
- **K-Bench**, 2026 preprint — clinician-calibrated high-risk benchmark

**结论：**“精神科 benchmark”“临床校准”“自动 judge”“多轮”“高风险”“拒答”都不是空白。

## 4. Benchmark 报告方式的新趋势

### BMJ Mental Health, 2026-09-28 Perspective
主张：
- domain/subdomain
- failure modes
- uncertainty
- clinically meaningful anchors
- reproducible/versioned analysis

同时指出 psychosis 在 HealthBench mental-health subset 中覆盖很少，支持 psychosis-specific evaluation 的必要性。

### CHART, 2025
要求透明报告：
- model/chatbot identity/version/date
- APP/API access route
- prompt source/engineering
- query strategy
- ground truth
- sample size
- analysis
- data availability

建议从采集第一天就按 CHART 建 metadata。

## 5. 与原设计很接近的现实参照

### Late-life depression blinded benchmark, Frontiers in Psychiatry, 2026
- 90 questions
- ChatGPT / Gemini / Doubao consumer products
- low/moderate/high risk
- 每题新对话
- repeated subset
- psychiatrists + adjudication

**含义：**consumer product + clinical questions + psychiatrists + repeat subset 已经是成熟且可发表的范式。把原学生 protocol “benchmark 化”会提高质量，但不会自动把 publication ceiling 抬到最高。

## 6. 不要再单独当创新点
- 中国模型
- 中文
- APP
- API
- APP vs API
- repeated sampling
- LLM-as-a-judge
- clinician gold standard
- multi-turn
- refusal / over-refusal
- generic mental-health benchmark
- reasoning on/off
- benchmark runner / leaderboard

## 7. 仍值得押注、但需正式系统查新的空间

### A. Psychosis-specific minimal counterfactual response boundary
同一 scenario 只改变一个 clinically relevant cue：conviction / insight / evidence / behavioral risk / cultural context。

### B. 双向 calibration
同时测 under-response/reinforcement 与 over-pathologization/over-escalation。

### C. Cultural formulation 作为实验变量
不是加“中国元素”，而是改变 culturally sanctioned context，看模型是否正确使用背景。

### D. Clinician acceptable-action distribution
不把精神科不确定性强行压成唯一 gold answer。

## 8. 抢先风险
很高。K-Bench 与 BMJ Mental Health benchmark perspective 都在 2026 年 9 月出现。

### 防抢先
1. 不等完整平台建完再开始。
2. 尽快冻结最小可发表 protocol。
3. Git + preregistration 建立时间戳。
4. freeze 前、投稿前、revision 前都查新。
5. signature 设计要具体，不要泛称“clinical calibration”。

## 9. 当前创新性结论
- **Plan A：**中等偏低 novelty；临床价值中等；正常可发表。
- **Plan B：**中等 novelty；风险/工作量平衡最好。
- **Plan C：**潜力最高，但也是新项目，必须重做查新和贡献边界。
