# PAIR dialogue-example reporting rule / 对话样例报告规则

Updated: 2026-10-03

## English
Both PAIR papers must include interpretable prompt-response examples in the main manuscript, not only aggregate statistics.

The example-selection rule is frozen before product/configuration-level results are interpreted to reduce cherry-picking:

### Paper 1 — A+B
Include in the main text:
1. one psychosis / matched-control pair;
2. one clinically important under-response, reinforcement, or other insufficient-response example;
3. where present, one opposite-direction error such as over-pathologization or unnecessary escalation.

Report prompt excerpt, response excerpt, product/configuration, raw rating, adjudicated rating, and the rubric component driving the judgment. Put complete examples in the Supplement where permitted.

### Paper 2 — PAIR-C
Include:
1. one minimal pair in which policy moves in the clinician-required direction and remains acceptably calibrated;
2. one under-response pair;
3. where present, one over-response / premature-escalation example.

Report both prompt variants, response excerpts, clinician `[L,U]`, direct pair-level `target_direction`, rated policy level `y`, URS/ORS, and contraindicated-behavior flags.

Synthetic examples may be used on the meeting Page or in rehearsal manuscripts only when prominently labeled `SIMULATION REHEARSAL`. They must never be presented as empirical findings.

## 中文
两篇 PAIR 论文的正文都必须包含能够直接阅读和理解的 prompt-response 对话样例，不能只有汇总统计。

为减少 cherry-picking，样例选择规则必须在解释产品/配置层面的结果之前冻结。

### Paper 1 — A+B
正文至少包括：
1. 一组 psychosis / matched-control pair；
2. 一个具有临床意义的 under-response、reinforcement 或其他回应不足案例；
3. 若真实数据中存在，再展示一个相反方向错误，例如 over-pathologization 或 unnecessary escalation。

每个案例报告 prompt 摘录、回应摘录、产品/配置、原始评分、裁决评分和导致该判断的 rubric component。许可范围内将完整案例放入 Supplement。

### Paper 2 — PAIR-C
正文至少包括：
1. 一组模型沿医生要求方向移动且 calibration 合格的 minimal pair；
2. 一组 under-response pair；
3. 若存在，再展示一个 over-response / premature escalation 案例。

每个案例报告两条 prompt、回应摘录、医生 `[L,U]`、直接标注的 `target_direction`、模型 policy level `y`、URS/ORS 和 contraindicated-behavior flags。

会议 Page / rehearsal manuscript 可以展示模拟案例，但必须显著标注 `SIMULATION REHEARSAL`，绝不能作为真实实证结果。
