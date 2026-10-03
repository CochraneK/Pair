# PAIR-C 模拟结果演练稿 v1

> **仅用于论文结构、统计和图表演练。以下所有数值来自 `SYNTHETIC_REALISTIC_SIMULATION`，不是实证结果。**

## 整体 calibration
三种固定 API 配置的模拟 CCA 为 **85.4%–92.2%**，但 directional concordance 仅为 **56.2%–69.8%**。因此，即使一个配置经常落在 `[L,U]` 以内，也可能对单一临床 cue 的改变不够敏感。

## 双向错误
模拟数据中，不同配置的 URS 与 ORS 组合不同。这意味着两个总体 CCA 接近的系统，可能一个主要表现为回应不足，另一个主要表现为过度升级。PAIR-C 因而不把 under-response 和 over-response 合并成唯一总分。

## 轴别差异
conviction、insight、behavioral risk 和 evidence/plausibility 的 CCA 并不完全一致。真实研究最有价值的结果不是“哪个模型第一”，而是发现**哪类临床信息最容易被模型忽略或过度反应**。

## 模拟讨论
如果真实数据复制这种“高 CCA、较低方向一致性”的分离，PAIR-C 的核心贡献将是证明：**静态可接受性与条件性临床校准是不同能力。**
