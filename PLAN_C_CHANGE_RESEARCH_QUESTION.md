# PLAN C｜正式改变研究问题

## 新 RQ
> 当精神病谱系体验中的 clinically relevant information 发生最小变化、其他条件不变时，LLM 能否在正确时点和方向调整 conversational response policy？

不再主要问：
“psychotic prompt 比 control 差多少？”

而问：
“什么时候应该继续聊、澄清、现实导向、风险评估、转诊或紧急升级，AI 的切换边界是否正确？”

## Signature
### Minimal counterfactual scenario families
候选轴：
- evidence / plausibility
- conviction
- insight
- behavioral risk
- cultural formulation

### 两个核心性质
- Relevant sensitivity：该变的时候变
- Nuisance invariance：不该变的时候不变

## Ground truth
Clinician-defined acceptable action range，而不是唯一文本答案。

actions：
- normal supportive conversation
- clarification
- emotional validation
- maintain epistemic uncertainty
- reality-oriented reflection
- risk assessment
- routine referral
- urgent escalation

contraindicated：
- delusion confirmation
- 帮助在异常信念框架中搜证
- ridicule/confrontation
- premature diagnostic labeling
- dangerous under-triage

## Outcomes
- Counterfactual Sensitivity
- Appropriate Policy Shift
- Monotonicity
- Under-response
- Over-pathologization / over-escalation
- calibration against clinician-rated intervention need

## Cultural formulation
中国不再是“换语言/换模型”，而是操纵 clinical context：
无文化说明 vs culturally sanctioned vs idiosyncratic + impairment/risk。

## 执行
主 benchmark 优先 API/open-weight/fixed configuration。
APP 作为 secondary product audit。

## 最大风险
- Safe-Psych / K-Bench 已进入 calibration territory
- 抢先速度很快
- ground truth 工作量大
- 这是新项目，会改变原学生项目边界

## 进入 Plan C 前必须
- 正式 systematic novelty search
- 团队确认改题
- 贡献/作者边界重谈
- protocol 重冻结
- pilot 证明 variants 能被医生稳定区分
