# 与原 protocol 作者沟通的建议顺序

## 1. 先确认原方案成立
明确说：
- SIPS 五维度好
- paired controls 有价值
- APP 有真实世界意义
- dedicated accounts / new chat / 72h / blind rating 都是优点
- 即使不大改，也是一篇可做研究

## 2. 只指出硬伤
优先顺序：
1. controls 同时改变 psychosis 与行为风险
2. APP 结论要定义为 product snapshot
3. novelty claim 要更新，不能只靠中文/国产

## 3. 说明“benchmark 化”不等于改题
可以表达：
> 你原来其实已经在做 benchmark-style study，只是还没有把 dataset、metadata、runner、versioning 做成 reusable benchmark artifact。

## 4. 再问 publication goal
> 如果目标只是稳妥发一篇，把设计做干净已经够；如果目标是明显提高 publication ceiling，我们是否愿意在原 Aim 外加一个真正新的科学问题？

## 5. 若对方愿意，再展示 Plan B
一句话：
> 原 Aim 完整保留，再抽少量场景，测试 conviction/insight/risk 改变时 AI 是否正确改变回应策略。

强调：
- 原论文不消失
- Aim 2 失败不影响 Aim 1
- 这是新增共同贡献

## 6. 什么时候谈 Plan C
只有团队明确说：
> 我们就是想冲方法学/benchmark 论文，工作量可以增加。

## 7. 会上不要展开
- 远期硬件
- 完整持续 leaderboard
- 大规模 RAG/Agent intervention
- IRT
- 所有 future idea
- 任何个人保留方向

---

# GitHub Pages 会议叙事规则（v9 起冻结）

GitHub Pages 是正式会议讲解主界面，不能从“A+B / C 已经定了”直接开始。默认顺序必须保留完整的推理过渡：

1. **为什么开这个会**：不是证明原方案不行，而是区分 validity、publication ceiling 和额外偏好。
2. **学生原始方案到底在问什么**：准确复述研究问题、题目、产品、评分与统计。
3. **先替原方案做最强辩护**：明确哪些设计已经成立、为什么原方案本来就有发表机会。
4. **审稿人真正会问什么**：matched-control confounding、consumer-product snapshot、novelty、评分 disagreement、单次生成稳定性等。
5. **原版 vs 升级版**：逐维度说明哪些是保留，哪些是 validity improvement，哪些已经改变研究问题。
6. **别人已经做到哪里**：用文献比较剥掉虚假的 novelty，不能用“中国/中文”“APP vs API”“response policy”等单点做首创新颖性。
7. **怎么说服而不是推翻**：用保护原项目主体性的表达，把“旧方案错 → 换新方案”改成“旧方案成立 → 修 validity → 新问题明确标 extension”。
8. **A / B / C 是怎么长出来的**：A=原题精修；B=原题上嵌套探索性最小临床对照；C=独立第二篇方法学/benchmark-development paper。
9. **再讲当前两篇论文**：Paper 1=A+B；Paper 2=PAIR-C。
10. **再进入模拟图、对话样例与论文全文**：模拟内容必须显著标注为 rehearsal；论文必须包含按冻结规则选取的对话样例。
11. **会议最后才拍板真实事项**：产品集合、医生审核角色、C 定位、真实采集窗口、伦理与预注册。

## 首页风格规则
- 首页优先是“讨论手册 / 共同推理”，不是项目 dashboard。
- 少卡片、少圆角、少 AI 产品感；保留纸张感、章节编号、长文本推理和对照表。
- 技术索引单独放在 `docs/dashboard.html`。
- 论文全文通过 `docs/papers.html` 嵌入首页或单独打开。
- README、论文、Pages 中英双语同步维护。
