# PAIR

[English](README.md) | [简体中文](README.zh-CN.md)

**PAIR = Psychosis AI Response（精神病性内容 AI 回应研究）**

这是一个以论文发表为导向、采用版本控制的研究工作区，用于评估消费级 AI 聊天产品以及固定 API 模型配置如何回应精神病性相关内容。

> **双语规则：** 对外公开的 README、论文主稿、HTML 仪表盘和 GitHub Pages 必须同步维护英文与简体中文版本。详见 [`BILINGUAL_POLICY.md`](BILINGUAL_POLICY.md)。

## 当前状态

截至 2026-10-03，**研究设计与工程准备已基本完成**。

当前研究结构：
- **Plan A** —— 消费级产品主审计；80 对匹配提示词 / 160 条提示词；已达到真实采集候选状态。
- **Plan B** —— 嵌入第一篇论文中的预设探索性临床对照子研究；36 条提示词 / 18 个最小对照对。
- **Plan C** —— 独立的精神病性场景 response-policy calibration 论文；64 条提示词的固定 API 试点。

当前论文主稿：
- **Paper 1 — A+B：** [`English`](manuscript/PAIR_AB_MASTER_v4_EN.md) | [`简体中文`](manuscript/PAIR_AB_MASTER_v4_ZH.md)
- **Paper 2 — C：** [`English`](manuscript/PAIR_C_MASTER_v2_EN.md) | [`简体中文`](manuscript/PAIR_C_MASTER_v2_ZH.md)

根据 [`ASSUMPTION_MODE_2026-10-03.md`](ASSUMPTION_MODE_2026-10-03.md)，临床题目/量规审核可以在**工作流执行层面暂按可接受处理**，但这不代表真实医生已经完成审核或签字。

## 建议从这里开始

1. [`STATUS.md`](STATUS.md)
2. [`CANONICAL_HANDOFF.md`](CANONICAL_HANDOFF.md)
3. [`TASKS.yaml`](TASKS.yaml)
4. [`DECISIONS_LOG.md`](DECISIONS_LOG.md)
5. [`execution/COLLECTION_READINESS_2026-10-03.md`](execution/COLLECTION_READINESS_2026-10-03.md)
6. [`execution/EXECUTION_PLAN_v0.1.md`](execution/EXECUTION_PLAN_v0.1.md)
7. [`manuscript/CURRENT_PAPERS.md`](manuscript/CURRENT_PAPERS.md)

## 论文

### Paper 1 — A+B
**消费级 AI 产品精神病性内容审计 + 探索性临床最小对照子研究**

- 英文主稿：[`manuscript/PAIR_AB_MASTER_v4_EN.md`](manuscript/PAIR_AB_MASTER_v4_EN.md)
- 中文主稿：[`manuscript/PAIR_AB_MASTER_v4_ZH.md`](manuscript/PAIR_AB_MASTER_v4_ZH.md)
- Reviewer #2 压力测试：[`manuscript/REVIEWER2_AB_v1.md`](manuscript/REVIEWER2_AB_v1.md)

### Paper 2 — C
**基于最小临床对照的精神病性场景 response-policy calibration**

- 英文主稿：[`manuscript/PAIR_C_MASTER_v2_EN.md`](manuscript/PAIR_C_MASTER_v2_EN.md)
- 中文主稿：[`manuscript/PAIR_C_MASTER_v2_ZH.md`](manuscript/PAIR_C_MASTER_v2_ZH.md)
- Reviewer #2 压力测试：[`manuscript/REVIEWER2_C_v1.md`](manuscript/REVIEWER2_C_v1.md)

## 已冻结/候选研究资产

### Plan A
- `benchmark/A_CASES_v0.1/`
- `routes/A/PROTOCOL_READY.md`
- `routes/A/SAP_AND_RESULTS_TEMPLATE.md`
- `analysis/plan_a_analysis.R`

### Plan B
- `benchmark/B_PILOT_v0.1/`
- `routes/B/PROTOCOL_AND_PILOT_READY.md`
- `routes/B/SAP_AND_RESULTS_TEMPLATE.md`
- `scripts/boundary_metrics.py`

### Plan C
- `routes/C/PILOT_BLUEPRINTS_64.csv`
- `routes/C/BENCHMARK_AND_PILOT_READY.md`
- `routes/C/METRICS_AND_RESULTS_TEMPLATE.md`
- `configs/C_API_PILOT_REQUESTS_v0.1.json`
- `scripts/api_pilot_runner.py`

## HTML / GitHub Pages

双语项目仪表盘源码位于 [`docs/index.html`](docs/index.html)。启用 GitHub Pages 后，应从 `main` → `/docs` 部署。

Page 必须同时提供英文和中文的 README、论文和研究状态入口。上一次仓库核查时 GitHub Pages 尚未启用，但页面源码会持续保持可发布状态。

## 预注册 / 伦理

目前已准备：
- [`preregistration/PLAN_AB_PREREGISTRATION_DRAFT_v0.1.md`](preregistration/PLAN_AB_PREREGISTRATION_DRAFT_v0.1.md)
- [`ethics/ETHICS_DETERMINATION_REQUEST_DRAFT.md`](ethics/ETHICS_DETERMINATION_REQUEST_DRAFT.md)

这些都仍是草稿。在真实机构或注册平台正式出具结果之前，不应声称已获伦理认定或已完成预注册。

## 执行规模

当前候选冻结计划：
- Plan A：**960** 条输出
- Plan B：**324** 条输出
- Plan C：**576** 条输出
- 全部运行时合计：**1,860** 条输出

采集计划由 `scripts/build_collection_schedules.py` 使用固定随机种子生成。

## 评分

统一盲评手册：
- `rating/RATER_MANUAL_v0.1.md`

盲评包生成器：
- `scripts/build_blinded_rating_pack.py`

## 研究原则

- APP 结果代表**特定日期和配置下的消费级产品快照**，不能直接等同于底层模型的稳定属性。
- APP 和 API 必须作为不同执行层分开处理。
- AI 执行者不能伪造临床 ground truth。
- 先发散保存想法，再检验新颖性、排序、冻结、执行。
- 冻结后禁止静默修改：任何实质性变化都要新版本并保留 diff。
- README、论文、HTML 和 Pages 默认中英双语同步。
- 不向公开仓库提交密码、API Key、账户标识、私密截图或可识别临床数据。

## 公开仓库规则

仓库可以公开，但原始或敏感运行材料不应默认进入 Git。

默认不进入公开 Git 的内容包括：
- API Key / token
- 账户标识
- 原始私密截图
- 受限或可识别临床材料
- 无再分发许可的第三方来源文档

详见 [`DATA_POLICY.md`](DATA_POLICY.md)。

## 仍需真实完成的步骤

项目目前已经不是被设计问题卡住，而是等待真实执行：
1. 获得机构伦理认定；
2. 正式提交并时间戳预注册；
3. 固定并记录消费级产品设置/账户状态；
4. 运行 A/B APP 真实 smoke pilot 与完整采集；
5. 为 C 提供真实 API 凭证并运行 smoke/full pilot；
6. 若论文要声称临床验证或 ground truth，获得真实医生审核与评分；
7. 在真实数据上运行冻结统计分析；
8. 完成最终 CHART、Reviewer #2 与文献更新检查。

目前仓库中**没有真实模型表现结果**；现有 synthetic / dry-run 内容仅用于软件、结构、分析和论文演练。