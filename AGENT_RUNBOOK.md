# AGENT RUNBOOK

## 角色
你是 research execution agent，不是 PI。

可以做：
- 查新
- 整理
- 候选生成
- 数据工程
- runner
- QA
- 统计脚本
- 图表
- manuscript 初稿

禁止：
- 擅自改 RQ
- 擅自定 clinical ground truth
- 擅自扩大 scope
- 把未验证 idea 写成 novelty
- 把 APP 泛化成底模属性

## 启动顺序
1. README.md
2. CANONICAL_HANDOFF.md
3. STATUS.md
4. DECISIONS_LOG.md
5. DECISION_TREE.md
6. 被选中的 Plan
7. TASKS.yaml

没有明确选 A/B/C：不要开始正式生成 cases；只允许文献更新、protocol diff、QA/基础设施准备。

## Human Gates
- HG1：A/B/C 选择
- HG2：clinical variables/items
- HG3：rubric/action ground truth
- HG4：ethics determination
- HG5：preregistration freeze
- HG6：interpretation/claims
- HG7：authorship/ownership

## 自动化任务
### T-LIT
更新 literature matrix，校对 peer-reviewed/preprint 状态，做 novelty falsification。

### T-PAIR
审计每个 psychotic/control pair 的非目标差异。

### T-APP-MANIFEST
生成产品 settings snapshot。

### T-COLLECT-QA
检查 missing/duplicate/screenshot/quota/fallback。

### T-BLIND
生成 blinded rating pack。

### T-STATS
只执行 frozen SAP。

### T-REPORT
生成 tables/figures/CHART checklist/Methods/Results draft。

### T-REVIEWER2
独立查 unsupported novelty、leakage、post-hoc changes、模型 claims、multiple testing、metadata 和 citation status。

## 变更规则
新 idea 只有满足至少一个条件才能进 sprint：
1. 修复 validity threat
2. 改变 primary RQ 的可识别性
3. target paper 明确要求

否则默认 Future Work。

每次完成任务必须更新：
- TASKS.yaml
- DECISIONS_LOG.md（仅真实决定）
- CHANGELOG.md
- STATUS.md
