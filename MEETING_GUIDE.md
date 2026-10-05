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

# GitHub Pages 会议叙事规则（v11 冻结）

GitHub Pages 是正式会议讲解主界面。v11 起，首页不是“给项目负责人看的操作手册”，而是**给老师、同学共同阅读和讨论的研究文本**。

## 公开页面的语言规则
- 中文页面以自然中文为主。英文术语只在第一次出现、确有必要时括号说明；后续优先使用中文。
- 不在中文正文大量堆叠 `prompt / control / psychosis-specific penalty / validity / publication ceiling / ground truth / cue / snapshot` 等词。
- 常用中文统一：提示词/情境、匹配对照、精神病性相关内容、产品快照、临床校准、回应不足、过度回应、方向一致性、临床审核。
- 缩写如 CCA / URS / ORS / CDC 只在指标解释部分集中出现，不作为普通讨论语言。

## 公开页面的内容边界
主页面只保留：
- 研究问题；
- 原始方案；
- 方法学问题与修订；
- 病例如何改进；
- 消费产品与固定 API 的研究边界；
- 文献与创新边界；
- 两篇论文结构；
- 当前准备程度与真实工作量；
- 医生具体需要做什么；
- 统计指标的临床含义；
- 对话样例、模拟图和论文全文；
- 伦理/证据边界；
- 本次会议真正需要决定的执行事项。

以下内容属于内部元认知/项目管理信息，不放在公开会议主页：
- “我应该怎么说服”“怎么开场”；
- “Agent 以后不能删什么”；
- 对用户个人的操作提醒；
- Git canonical 管理规则的细节；
- 为避免遗忘而写给助手的幕后说明。

这些内容可以继续保留在 `MEETING_GUIDE.md`、`CANONICAL_HANDOFF.md`、`STATUS.md` 等内部协作文档中。

## v11 推荐主叙事
1. **研究问题**：两层科学问题及其关系。
2. **原始方案**：80+80、SIPS P1–P5、消费产品、医生评分、重复生成。
3. **为什么需要修订**：混杂、产品层解释、创新边界、评分信息损失、统计预先冻结。
4. **病例如何改进**：至少展示 2–3 个 before → confound → revision 实例。
5. **产品与接口分层**：A/B consumer product；C fixed API/configuration。
6. **文献与创新边界**：已有方向 vs PAIR 的具体贡献。
7. **两篇论文结构**：Paper 1=A+B；Paper 2=PAIR-C。
8. **当前准备程度**：A 960；B 324；C 576；总计 1,860 outputs，并说明已准备与待完成事项。
9. **医生需要做什么**：prompt/case validation、`[L,U]`、target direction、output rating。
10. **指标怎么解释**：A ordinal appropriateness；B/C CCA/URS/ORS/CDC 的临床意义与限制。
11. **对话 + 模拟结果**：模拟内容必须显著标为 rehearsal；正式对话样例按冻结规则选择。
12. **论文全文**：中英双语直接嵌入 Page。
13. **伦理与证据边界**：fictional prompts、非患者结局、文化审查、正式伦理/预注册仍待真实完成。
14. **会议决策**：A+B、产品集合、临床分工、C、下一真实步骤。

## 详细程度原则
- 可以详细讲科学内容，不要用“项目管理说明”填充篇幅。
- 病例改造、APP/API、医生评分、统计指标应比 v10 更详细，因为这些最值得团队讨论。
- 技术实现细节（脚本文件名、hash、seed、Agent 规则）留在 dashboard/Git，不占主会议叙事。
- 首页风格继续保持纸张感、章节式长文本和对照表，少圆角、少 dashboard 感。

## 数据与伦理边界
- 当前 prompt banks 是 fictional/synthetic research prompts，不使用原始患者临床记录。
- A/B 消费产品结论只限定到 tested product/date/configuration；不能外推为稳定 base-model trait。
- 工程默认 `[L,U]`、synthetic model performance、mock clinician rating 都不得视觉上伪装成真实结果。
- 真实伦理 determination、真实 preregistration、真实 clinician sign-off、真实模型输出和真实评分必须与 assumption/mock/synthetic 层严格分开。

## 手机端 / 响应式规则（2026-10-05 起冻结）
GitHub Pages 是会议现场入口，手机端不是附带适配，而是一等展示环境。

必须满足：
- 竖屏宽度约 360–430px 时正文不横向溢出；
- 顶部导航可横向滑动或自然换行，不能用固定高度压住正文；
- 表格允许横向滑动，不能把三列表压到不可读；
- 图表在手机端自动单列并占满可用宽度；
- 长链接、代码和英文标识可以断行，不撑破页面；
- 对话样例在窄屏下由“角色 + 内容”双列改成上下排列；
- 会议决策 radio/button 触控区域至少约 40–44px；
- 论文 iframe 在手机竖屏下使用视口相关高度，且仍可单独打开论文全文；
- 兼容横屏会议展示，并考虑 iOS/Android 安全区域（safe-area inset）；
- 每次大改 `docs/index*`、`paper_*.html`、临床审题页后，都要检查桌面 + 手机布局。

## 页面组件
- 会议主页：`docs/index.html`
- 论文全文：`docs/papers.html`
- 临床审题：`docs/PAIR_C_CLINICIAN_REVIEW.html`
- 技术索引：`docs/dashboard.html`
- README、论文、Pages 继续中英双语同步维护。
