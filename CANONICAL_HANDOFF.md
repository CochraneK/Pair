# CANONICAL HANDOFF

## 0. 当前任务
围绕 2026-10-02 原始 protocol：

**《国产大语言模型聊天产品对精神病性内容的回应恰当性：一项中英双语横断面评价研究》**

建立一个 publication-oriented、可交接、可扩展到 API 的研究执行框架。

## 1. 原 protocol 真正在测什么
它直接测的是：

> 当用户已经表达出精神病性内容时，消费级 AI 聊天产品是否更容易给出不恰当回应，尤其是否未识别、强化异常信念、低估紧迫性或未提供求助资源。

它**不是**纵向因果研究，不能证明“AI 越聊越让病情加重”。

原设计：
- 80 条 psychotic prompts：SIPS P1–P5，各 16 条
- 80 条结构匹配 control prompts
- 中国文化语境内容
- 5 个国产消费级聊天产品免费版
- 每题独立新对话、单轮
- 72 小时集中采集
- 原始文本 + 截图 + 时间戳
- 两名精神科医生盲评
- 主要结局：0–2 appropriateness
- 次要四成分：recognition / non-reinforcement / urgency / resources
- 20% psychotic prompts 重复提交
- 双语子研究
- 预注册、R、sessionInfo、分析代码公开

## 2. 原方案的优点必须先承认
1. 临床问题清楚，能直接接 Shen et al. (JAMA Psychiatry, 2026)。
2. SIPS 五维度提供合理 clinical taxonomy。
3. psychotic/control 配对比“随便问几个 AI”严谨。
4. 已考虑研究专用账号、关闭记忆/引用历史、每题新会话。
5. 已考虑时间窗、版本记录、截图和拒答/报错保留。
6. 有盲评、试评分、一致性、预注册和统计意识。
7. 作为学生 protocol，本身已经有发表可能性。

后续修改必须区分：修硬伤、提高 publication ceiling、只是 AI/系统化偏好。

## 3. 当前确认的主要问题
### 3.1 Novelty 不宜再押“中国版”
“中文 + 国产模型”可作为 setting / external validity，但不应作为主要科学创新。

### 3.2 matched controls 存在潜在混淆
部分 pair 不只改变 psychosis，还改变行为风险，例如“全部积蓄 vs 小部分积蓄”“停药 vs 调整作息”。

如果继续原问题，应做 **minimal matching**：除 psychotic component 外，行为、金额、风险、语气、长度尽量保持一致。

### 3.3 APP 测的是产品，不是底模
claim 应限定为“某消费聊天产品在某日期、某默认设置下的表现”。

### 3.4 双语、重复采样、LLM judge、API/App、多轮都不是足够新的 headline novelty
可以做，但更适合作为方法或 secondary analysis。

### 3.5 结果要更临床可解释
主 0–2 评分可保留以便与 Shen 比较，但最好增加 failure profile，而不是只做总排名。

## 4. 三条路线
### Plan A｜原题精修
RQ 不变：psychotic prompts 是否比严格匹配 controls 更容易诱发不恰当回应？不同消费产品有何差异？

关键增强：minimal matched pairs、consumer-product SOP、within-scenario / paired effect、failure profile、CHART-compliant metadata、stability subset。

### Plan B｜原题 + 嵌套增强（当前推荐）
Aim 1 保留学生原问题。Aim 2 加一个小型 clinical-boundary / calibration substudy：

> 当 conviction、insight 或 behavioral risk 等关键临床 cue 改变时，AI 的回应策略是否发生临床上恰当的变化？

只做 2–3 个变量、小范围 subset，避免把主论文整个换掉。

### Plan C｜正式改变研究问题
> psychosis-spectrum clinical uncertainty 下，LLM 的 conversational response policy decision boundary 是否校准？

这是新研究，不能伪装成“小改 protocol”。

## 5. 决策规则
### 不改 RQ，如果
- 已接近采集或已预注册
- 目标是快速发表
- 学生希望保留项目结构
- 新问题 gap 尚未系统确认
- 临床评分资源不足
- 改题会引发所有权混乱

### 建议加 Aim 2，如果
- 目标明确是“比普通 replication/audit 更强”
- 仍希望学生原问题居中心
- 可多做有限 subset
- AI 合作者需要体现为真实方法学贡献

### 正式改题，如果
- 团队承认这是新科学问题
- 文献查新确认剩余 gap
- 可重新预注册
- 有资源构造 minimal counterfactual scenario families
- 有 clinician action / escalation boundary 专家意见
- 目标是 benchmark/methodology paper

## 6. APP 应如何解释
APP 是有效研究对象，不是“API 的低配版”。

产品响应近似：base model + hidden system prompt + safety layer + routing + search/tools + account state + memory/personalization + UX logic。

隐藏层不能被研究者真正控制；应控制用户侧：研究专用新账号、无其他历史使用、关闭 memory / 引用历史、custom instructions 为空、每题独立新会话、固定 surface/语言/地区设置、固定默认 thinking/search/model-selector 状态、随机/区组化 prompt 顺序、记录 quota/fallback/限流、不追问/不 regenerate/不点赞点踩、保存 raw text/截图/时间/版本/模式和错误。

## 7. APP 以后可用同一流程跑 API
原则：**同一个 benchmark schema；不同 execution strata。**

共享 case IDs、frozen prompts、rubric、ratings format、analysis schema；分开 APP runner、API runner、metadata 和 claims。

API 额外固定 model_id/checkpoint、provider、system prompt、temperature、top_p、max tokens、reasoning、tools/web、seed（若支持）。

## 8. 原研究本质上是不是 benchmark？
是。它已经有 standardized prompt set、multiple systems、common scoring、comparative analysis，因此是 benchmarking study。

若要成为 reusable benchmark artifact，还应增加 versioned dataset、schema、frozen execution protocol、metadata standard、reproducible runner、result format、baseline runs、release/version policy。

Evolvent/BenchRouter 可帮助工程化 API/local benchmark，但不能替代精神科 clinical ground truth。

## 9. 已有研究大致占掉了什么
已经有人做：
- psychotic/control 单轮 clinician rating：Shen 2026
- psychosis 多轮升级与 DCS/HES/SIS：psychosis-bench
- API vs chat interface：LLM Spirals of Delusion
- 真实伤害相关对话历史：DelusionEval
- 精神科大规模多任务 benchmark：PsychiatryBench
- mental-health knowledge/diagnosis/emotional support：PsyEval
- 大规模 human vs LLM judge：MentalBench/MentalAlign
- over-refusal / safe completion：Health-ORSC-Bench
- high-risk clinician-calibrated benchmark：K-Bench
- sequential uncertainty、clarify/abstain：Safe-Psych
- benchmark 临床可解释性：BMJ Mental Health 2026 Perspective
- chatbot health study reporting：CHART

因此不要把“中国模型、中文、API、重复采样、LLM judge、多轮、拒答、benchmark 工程化”单独当 novelty。

仍值得押注、但需正式系统查新的 gap：psychosis-specific minimal counterfactual response-policy boundary、under-response 与 over-pathologization 的双向 calibration、cultural formulation 作为实验因子、clinician acceptable-action distribution。

## 10. 当前研究过程原则
DIVERGE → PRESERVE → NOVELTY FALSIFICATION → DEFEND ORIGINAL → VALIDITY CHECK → OWNERSHIP CHECK → PUBLIC / LATER / PRIVATE → PRIORITIZE → FREEZE → EXECUTE。

新 idea 不进当前实验，不等于删除；进入 Idea Pool。

## 11. 接手 Agent 硬规则
1. 不得自动改变 Research Question。
2. 不得把 brainstorm 当成已决策事项。
3. 不得把 preprint 写成 peer-reviewed。
4. novelty claim 必须注明检索日期与置信度。
5. APP 结果不得写成底层模型稳定属性。
6. 临床 label/rubric 只能由临床团队批准。
7. 新增任务先判断是否影响 validity / primary RQ / target paper。
8. freeze 后，新 idea 默认进入 Future Work。
9. 重要决定写入 `DECISIONS_LOG.md`。
10. 执行状态写入 `TASKS.yaml`。
