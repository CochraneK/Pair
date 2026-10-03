# 原 protocol 审计

## 值得保留
1. 科学问题清楚。
2. 能与 Shen et al. 直接比较。
3. SIPS P1–P5 结构合理。
4. paired control 是好骨架。
5. 原文已经有研究专用账号、关闭记忆/引用历史、每题新会话、72h、截图、拒答/报错保留。
6. 有盲评、试评分、一致性。
7. 有预注册、R、seed、sessionInfo、分析代码公开意识。

## 必须或强烈建议修改

### P1｜matched controls 可能混入行为风险
最强内部效度问题。修复为 minimal pair。

### P2｜产品 ≠ 底层模型
免费版可能自动路由、限额后降级、调用隐藏 safety/system 层。结论必须是 product snapshot。

### P3｜novelty statement 过强
“中文语境没有任何系统评价”“国内还没有相关实证研究”必须在投稿前重新查新，并把边界收窄。

### P4｜双语不适合作为第二核心创新
可留 secondary / sensitivity analysis。

### P5｜重复采样偏弱
若只做 secondary，建议 stratified 20% + 3–5 次，不必膨胀成全量 10 次。

### P6｜“两评分员中位数并向下取整”需要重审
保存 raw ratings；报告 reliability；主分析用 adjudicated consensus 或显式 rater model。不要仅因前作这样做就机械复制。

### P7｜统计框架应统一
原方案写 proportional odds + GEE + Brant。应让统计人员冻结一个自洽框架，不要机械混用。

### P8｜metadata 还需完整
增加 surface、app/build、model selector、thinking/search、locale、quota/fallback、run_id、retry_count。

### P9｜伦理表述避免绝对化
虽然没有患者参与和真实病历，仍建议取得本机构“非人类受试者/豁免/无需伦理审查”的正式确认。

### P10｜若想长期做 benchmark，需考虑 contamination
第一篇论文可以公开；若做长期 leaderboard，可考虑 public dev + protected test。
