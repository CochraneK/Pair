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

# GitHub Pages 会议叙事规则（v10 冻结）

GitHub Pages 是正式会议讲解主界面。它必须让第一次接触项目的老师/同学能够从“学生原始方案”一路跟到“为什么形成两篇论文”，不能只展示最终结论或技术 dashboard。

默认顺序：

1. **为什么开会**：区分 validity、publication ceiling 和真正新增研究问题。
2. **学生原始方案**：准确复述研究问题、题目、产品、评分、重复与统计。
3. **先替原方案做最强辩护**：明确原设计为什么已经有发表价值。
4. **真正硬伤**：matched-control confounding、consumer-product snapshot、novelty、评分 disagreement、统计框架。
5. **病例如何从原始版本改成 minimal pair**：必须展示 before → confound → revised pair → QA/clinician review，而不是让人以为题库只是 AI 批量生成。
6. **APP vs API**：A/B 是 consumer-product snapshot；C 是 fixed API/configuration。两者不能混成“模型能力”。
7. **文献版图**：剥掉虚假 novelty，说明已有研究做到哪里。
8. **怎么说服，而不是推翻**：旧方案成立 → 修 validity → 新问题明确标 extension。
9. **A/B/C 如何演化**：A=原题精修；B=A 上的 prespecified exploratory substudy；C=独立 benchmark-development pilot。
10. **为什么拆成两篇**：Paper 1=A+B；Paper 2=PAIR-C。
11. **当前已完成资产与真实工作量**：A 160 prompts / 960 outputs；B 36 / 324；C 64 / 576；总 1,860；展示 runner、schema、rating、analysis、manuscript 已经落地。
12. **医生到底要做什么**：A 的 prompt validity + 0–2/output components；B/C 的 manipulation success、`[L,U]`、target direction、clinically relevant change、output-policy rating。
13. **从一条 raw response 到论文图**：prompt → raw response → blinded raw ratings → structured row → CLMM/CCA/URS/ORS/CDC → estimate/CI/family pattern → Table/Figure/exemplar。
14. **模拟图与对话样例**：必须显著标 `SYNTHETIC REHEARSAL`；真实论文的对话例子按冻结规则选择，防止 cherry-picking。
15. **论文全文嵌入**：A+B / C、中文 / English 可在 Page 内直接切换阅读。
16. **什么结果也算研究成功**：不把“必须显著”“必须有最差产品”当成功标准；A 看主效应估计，B 看 cue/family/stability，C 看 static calibration 与 directional sensitivity 的分离或可解释 failure signatures。
17. **会议决策板 + Parking lot**：会议最后才点选产品集合、A/B 边界、临床分工、C 定位、下一真实步骤；未来方向保留但不重新塞回当前 protocol。

## 状态标签规则
Page 必须持续区分：
- `FROZEN / PROVISIONAL DESIGN`：设计已经冻结或暂定冻结；
- `ENGINEERING DEFAULT`：仅供 pipeline 使用，不是医生 ground truth；
- `SYNTHETIC REHEARSAL`：模拟结果/模拟回应，不是实证发现；
- `REAL EMPIRICAL`：只有真实采集并完成真实评分后才能使用。

任何 `[L,U]` 工程默认、synthetic model performance、mock clinician rating 都不得视觉上伪装成真实结果。

## 会议交互规则
- `docs/index.html` 必须保留浏览器内 localStorage 决策板。
- 会议选择应能生成可复制的 `Meeting Decision Summary`，供会议纪要和 Git 决策日志使用。
- 不需要把 Page 做成复杂项目管理后台；交互只服务现场讨论和拍板。

## 首页风格规则
- 首页优先是“讨论手册 / 共同推理”，不是项目 dashboard。
- 少卡片、少圆角、少 AI 产品感；保留纸张感、章节编号、长文本推理和对照表。
- 技术索引单独放在 `docs/dashboard.html`。
- 临床审题工具放在 `docs/PAIR_C_CLINICIAN_REVIEW.html`。
- 论文全文通过 `docs/papers.html` 嵌入首页或单独打开。
- README、论文、Pages 中英双语同步维护。

## 明确的数据与伦理边界
- 当前 prompt banks 是 fictional/synthetic research prompts，不使用原始患者临床记录。
- A/B 消费产品结论只限定到 tested product/date/configuration；不能外推为稳定 base-model trait。
- 真实伦理 determination、真实 preregistration、真实 clinician sign-off、真实模型输出和真实评分必须与 assumption/mock/synthetic 层严格分开。
