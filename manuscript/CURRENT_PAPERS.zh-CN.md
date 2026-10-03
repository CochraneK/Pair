# 当前论文状态

[English](CURRENT_PAPERS.md) | [简体中文](CURRENT_PAPERS.zh-CN.md)

更新：2026-10-03

## Paper 1 — A+B

**当前 canonical working version：** A+B Master v4

- 英文主稿：[`PAIR_AB_MASTER_v4_EN.md`](PAIR_AB_MASTER_v4_EN.md)
- 中文主稿：[`PAIR_AB_MASTER_v4_ZH.md`](PAIR_AB_MASTER_v4_ZH.md)

科学定位：
- Aim 1：confirmatory matched psychosis-related vs matched-control consumer-product audit；
- Aim 2：预先规定的 exploratory response-policy calibration 子研究。

已经纳入设计状态的 Reviewer #2 修正：
- 评分者可对产品身份盲法，但不声称对 prompt condition 盲法；
- 预设排除 P5 disorganized communication 的敏感性分析；
- 要求预先定义 consumer-product sampling frame 与 version-break rule；
- 要求 brand-leakage audit；
- Aim 2 因只有 6 个 scenario families，始终保持探索性定位。

## Paper 2 — C

**当前 canonical working version：** PAIR-C Master v2

- 英文主稿：[`PAIR_C_MASTER_v2_EN.md`](PAIR_C_MASTER_v2_EN.md)
- 中文主稿：[`PAIR_C_MASTER_v2_ZH.md`](PAIR_C_MASTER_v2_ZH.md)

科学定位：
- 开发和试点评价 psychosis-specific conversational response-policy calibration；
- 一次只改变一个临床 cue 的 minimal contrasts；
- 医生定义可接受 intervention interval `[L,U]`；
- 医生直接标注 pair-level target direction（`-1/0/+1`）；
- under-response 与 over-response 分开；
- 重复生成只用于估计 stochasticity，不扩充临床样本量。

关键修正：
- 64 题 pilot **不**声称精确 threshold/boundary-location estimation；
- 0–5 是 ordinal escalation-intensity scale，而不是等距临床严重度量尺；
- URS/ORS 是 ordinal step distance，必须同时报告 categorical/binary summaries；
- evidence/plausibility 是临床相关变量，不是 nuisance；
- 当前 64 题 pilot 不估计 Nuisance Invariance。

## 双语公开规则

公开 README、当前论文 Master、HTML 仪表盘和 GitHub Pages 均需英文与简体中文同步维护。详见 [`../BILINGUAL_POLICY.md`](../BILINGUAL_POLICY.md)。

## 实证结果边界

当前仓库中**没有真实模型表现结果**。Synthetic 与 dry-run 输出仅用于工程、分析与论文演练，不得作为实证结果报告。

## 投稿 Gate

两篇论文都不能在以下事项真实完成前投稿：伦理认定、预注册状态、精确 product/model manifest、真实医生审核/评分、真实模型输出、冻结统计、Data/Code Availability、作者贡献/资助/COI，以及最终 CHART 审核。