# PLAN B｜原题 + 嵌套 Clinical Boundary Substudy（推荐）

## 为什么平衡最好
- 不抢走学生原项目
- Aim 1 能独立发表
- AI 合作者不是只“帮忙跑模型”
- 增加新的科学故事
- Aim 2 失败也不毁 Aim 1

## Aim 1
完整按 Plan A。

## Aim 2
问题：
> 当同一个 psychosis-relevant scenario 中，一个临床重要 cue 改变时，AI 是否以正确方向调整回应策略？

### 第一版只选 3 个轴
1. conviction：低 vs 高
2. insight：保留 vs 缺失
3. behavioral risk：低 vs 高

### 设计
从 Aim 1 抽 15–20 个基础 scenario families。
每个 family 生成 minimal variants。
除目标 cue 外，其余信息尽量不变。

### Clinician ground truth
不写唯一标准文本。
医生标：
- 可继续支持性交流
- 应进一步 clarification
- 应 non-reinforcement / reality-oriented response
- 应 risk assessment
- 应 professional referral
- 应 urgent escalation

可保留专家分歧。

### 探索指标
- Counterfactual sensitivity
- Appropriate policy shift
- Under-response
- Over-response / over-pathologization
- Monotonicity（若有有序强度）

### 先 pilot
5–8 scenario families × 3 axes × 2 levels × 2–3 products。
确认可评分性和效应后再扩。

## 什么时候把 Aim 2 升级为 headline
如果 pilot 显示：
- 对关键 cue 系统性不敏感
- 产品 response threshold 差异明显
- 过早/过晚升级明显

否则保留 exploratory/substudy。

## 项目边界
会议上明确：
> Aim 1 是原 protocol 精修；Aim 2 是新增共同方法学扩展。
