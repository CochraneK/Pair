# PAIR-C：基于最小临床对照的精神病性场景对话回应政策校准 benchmark——开发与试点评价

[English](PAIR_C_MASTER_v2_EN.md) | [简体中文](PAIR_C_MASTER_v2_ZH.md)

**目标期刊：** npj Digital Medicine  
**版本：** PAIR-C Master v2  
**内部状态：** 含真实数据占位符的正式论文主稿。本论文报告的是一个 64 题的“最小临床对照下 response-policy calibration”试点，不声称能够精确定位临床 threshold/boundary；真正的阈值定位至少需要每个轴 ≥3 个有序水平和更多场景家族。任何 synthetic 演练数值都不得作为真实实证结果写入论文。

## 摘要

### 背景
大型语言模型（LLM）可能以具有临床后果的方式回应精神病性相关披露。既往工作已经发现异常信念强化、过早下结论、不恰当升级及过度病理化等问题，但总体安全分数或总体恰当性分数并不能告诉我们：当一个临床关键信息发生变化时，模型是否会成比例地调整它的对话回应政策。当风险上升时，回应可能太弱；当异常体验仍高度不确定，或存在合理普通解释时，回应也可能太强。

### 方法
我们开发了 PAIR-C，一个基于“一次只改变一个临床 cue”的最小对照设计、用于精神病性场景 response-policy calibration 的 benchmark。64 题试点由 8 个 scenario families、4 个临床相关轴（conviction、insight/接受替代解释、behavioral risk、evidence/plausibility）和每轴 2 个水平组成，共形成 32 个最小对照对。临床医生独立评价操纵成功、自然度、无意混杂，并在一个六级 escalation-intensity 量尺上为每个变体给出可接受干预区间 `[L,U]`，同时在 pair level 直接标注目标变化方向（`decrease`、`no material change`、`increase`）。3 个固定、版本可识别的 API/model configuration 每题独立查询 3 次，共计划 576 条输出。对 configuration 身份盲法的评分者将每条回应映射为实际传达出的 escalation-intensity policy level，并独立标记 contraindicated behaviors。主要指标包括 Clinical Calibration Accuracy（CCA）、基于有序等级步长的 under-response severity（URS）、over-response severity（ORS）、Clinical-Cue Directional Concordance（CDC）和 Relevant Sensitivity。本 64 题试点不估计 Nuisance Invariance，因为尚未包含独立的 nuisance module。

### 结果
[[REAL RESULTS：报告 benchmark validation、医生 interval/direction 一致性、精确 configuration ID、完成 run 数、CCA/URS/ORS/CDC/Relevant Sensitivity 及其不确定性、axis-specific pattern、violation rate 和重复生成不稳定性。不得使用 synthetic 数值。]]

### 结论
[[REAL CONCLUSION：说明试点是否识别出可解释的精神病性场景 response-policy calibration 失败，以及结果是否支持扩展至 PAIR-C v1.0。避免使用全局“最好/最安全模型”主张。]]

## 引言

通用 AI 聊天机器人越来越多地接触情绪困扰、异常信念、怀疑/被害体验、感知异常及其他心理健康问题。在精神病性相关场景中，“看起来友善”与“临床上安全”并不总是一致。一个显得共情的回答可能强化缺乏依据的解释；相反，一个过度精神科化、过度急诊化的回应，又可能把模糊、文化上可理解或本身具有普通解释的体验过度病理化。因此，真正重要的评价问题，并不只是系统是否“支持用户”“足够谨慎”或“愿不愿意拒答”，而是：**回应政策的强度和方向，是否与实际出现的临床信息相校准。**

既有精神病性相关 chatbot 研究已经表明，这确实是一个独立的评价领域。Shen 等人发现，多个 ChatGPT 产品版本对精神病性提示词给出较不恰当回应的概率明显高于匹配对照 [1]。Psychosis-bench 进一步在多轮妄想轨迹中测量 delusion confirmation、harm enablement 和 safety intervention [2]。Kirgis 等人则发现，即使底层能力看起来相近，API 与消费级聊天界面的精神病性相关行为也可能不同，并且会随对话轮次发生变化 [3]。这些研究证明精神病性对话安全具有特异性，但它们主要比较 prompt 类别、模型、界面或纵向轨迹，并未系统隔离“一个预定义临床 cue 发生改变”所带来的回应政策变化。

更广泛的 mental-health safety 文献则揭示了第二个问题：平均 benchmark 表现可能掩盖 calibration 错误。SIM-VAIL 显示，表面上支持性的 chatbot 行为在多轮交流中也可能放大特定精神脆弱机制 [4]。Safe-Psych 说明，更强的精神科能力并不自动带来不确定情境下更好的 calibration：模型可能过早给出结论，而 safety prompting 又可能把错误推向过度 abstention [5]。ClinDet-Bench 同样把 premature conclusion 和 excessive abstention 视为相反方向的错误 [6]。K-Bench 通过临床医生校准的高风险心理健康场景，显示即使强模型之间也存在 configuration-level 差异 [7]。近期针对脆弱对话中 AI companion 的研究也明确使用 **response policy** 这一概念进行审计，因此 PAIR-C 不会把“response policy”这个术语本身当作创新点 [15]。

这种双向 calibration 问题在精神病性体验中尤其重要，因为异常体验本身并非单一维度。妄想相关体验可在 conviction、preoccupation、disruption、distress 和 attribution 等方面变化 [8]。Insight 也是多维构念，涉及对问题的觉察、对症状来源的归因以及对是否需要帮助的理解 [9]。即时 behavioral risk 会改变合理回应，但风险必须在具体情境中评估，不能由“存在精神病性体验”本身推导。与此同时，可核实的外部证据可能使一个听起来异常的报告更符合普通解释。已有 LLM 精神病风险评估研究也发现，对非临床体验进行 over-pathologization 是一个重要错误模式 [10]。文化表述又进一步影响体验是否具有合理性及如何被理解 [11]。

这些临床事实意味着，benchmark ground truth 不应总是唯一“理想回答”。对于同一披露，可能存在多种临床上可接受的对话策略，只要它既没有保护不足，也没有无必要地把体验病理化。PAIR-C 因而将临床 ground truth 表示为**可接受 escalation/intervention 区间 `[L,U]`**，并要求医生直接标注 pair-level 目标变化方向。这样可以对 under-response 与 over-response 做对称测量，也避免从有序量尺的 interval midpoint 人为推导“正确方向”。

PAIR-C 的核心问题是：当场景其他信息尽量不变、只改变一个临床有意义的 cue 时，模型是否会做出临床上合适的政策调整。试点操纵 4 个轴：conviction、insight/接受替代解释、即时 behavioral risk 和 evidence/plausibility。我们使用 3 个固定 API/model configuration、重复生成和盲化的 response-policy rating。主要目标是估计回应落入医生可接受区间的绝对 calibration，并区分两个方向的错误；第二个目标是估计模型政策变化的符号，是否与医生在采集前直接标注的目标方向一致。由于每个轴只有 2 个水平，本试点只能评价 directional sensitivity 和 contrast 下的 calibration，**不能**精确定位临床 threshold。我们在当前 targeted scoping search 中未发现一个与“psychosis-specific one-cue minimal contrasts + acceptable interval + direct target direction + symmetric under/over scoring”完全相同的既有 benchmark，但在投稿前仍须更新正式 novelty search，因此不作“全球首个”主张。

## 方法

### 研究设计与报告范围
PAIR-C 是一项 benchmark-development 与 pilot-evaluation 研究，使用虚构、单轮、精神病性相关披露以及固定、版本可识别的 LLM configuration。64 题试点主要用于检验构念效度、临床可评分性、指标行为以及是否能够产生可解释的失败模式，为后续更大 benchmark 版本提供依据。它不是诊断工具、患者风险预测工具，也不替代真实临床评估。报告在适用范围内遵循 CHART 的模型身份、prompt 来源、query strategy、human reference standard、分析与可重复性原则 [13,14]。

### Benchmark ontology
PAIR-C 所定义的是**受控实验维度**，而不是宣称真实精神病理构念彼此正交。

**Conviction。** 指个体对异常解释的确信程度。低水平变体仍保留怀疑并能接受替代解释；高水平变体接近确定。该轴来源于妄想现象的多维研究 [8]。

**Insight / 接受替代解释。** 指说话者能否考虑压力、睡眠、知觉、认知或其他内部/情境解释。该操作化比全局 illness insight 更狭义；后者本身是多维构念 [9]。

**Behavioral risk。** 指异常体验/信念是否已经推动个体准备采取近期、具体、并可能带来明显社会、职业、经济、治疗或安全后果的行动。该轴用于测试回应比例性，不意味着精神病性体验本身等同于危险性。

**Evidence / plausibility。** 指是否存在可独立核查的信息，使普通、非精神病性解释更可信。与其他轴不同，更强的普通证据有时应当导致精神科升级程度**下降**。该轴直接测试 over-pathologization 风险 [10]。

文化表述挑战集留待后续，不属于当前 64 题核心试点。

### Scenario families 与最小对照构建
试点包含 8 个精神病性相关 scenario families，覆盖 referential interpretation、suspiciousness/persecutory ideas、grandiosity、perceptual abnormalities、thought interference 与 thought broadcasting 等。每个 family 为 4 个轴各构造一个最小对照对，因此总计 8 families × 4 axes × 2 levels = 64 prompts（32 对）。

同一 pair 内尽量保持主题、第一人称叙述者、请求任务、情绪语气、近似长度及非目标临床信息不变。配对设计避免无必要地引入药物变化、自杀/暴力、大额经济风险或其他会独立改变合理回应的 cue。由于 conviction 与 insight 在临床上本来就相关，PAIR-C 不假设它们完美正交；如果一个操纵必然显著改变第二个轴，该 pair 应由临床医生拒绝。

### Prompt 来源与生成式 AI 辅助
所有 scenario 都为 PAIR-C 新构造的虚构材料，不复制公开病例或受版权保护的访谈原文。研究者先定义 ontology、pair constraint、目标轴与禁止混杂。生成式 AI 可以在这些约束下辅助候选措辞与语言自然化；研究人员再人工核查语义等价性、临床连贯性、意外 cue 改变以及模板化痕迹。

[[REAL DEVELOPMENT RECORD：说明谁制定 ontology、哪些 AI 系统参与辅助、生成多少候选、临床审核前修改/淘汰多少。]]

### 临床医生验证
在任何模型输出可见之前，临床医生独立审核每个变体。必填 item-level annotation 包括：目标轴操纵成功与否、domain fit、自然度/真实感、重大非目标混杂、无意 second-axis change、可接受 `[L,U]`、contraindicated behaviors 和自由文本意见。**Pair level** 还需直接标注预期政策变化方向（`-1`=降低，`0`=无实质变化，`+1`=提高），以及该变化是否足够具有临床意义，可以进入 Relevant Sensitivity。

一个 pair 只有在以下条件满足后才能保留：目标操纵具有临床意义；修订后不存在重大无意混杂；两个变体均可分配合理区间；所有关键分歧都可以在看不到模型输出的情况下透明解决。

[[REAL CLINICIAN VALIDATION：填写医生人数/资历、独立审核流程、manipulation-success threshold、confound threshold、原始一致性、`[L,U]` 和 target_direction 分歧如何裁决、修改/删除题目数量，以及最终 pilot version/hash。共识前必须保留每位医生的原始标注。]]

### 可接受 escalation/intervention 区间
医生在 0–5 六级 **escalation-intensity** 量尺上，分别标注最低可接受水平 `L` 与最高可接受水平 `U`：

0. 一般支持性交流已足够；  
1. 应进行澄清/进一步探索；  
2. 应明确保持认识论不确定性/避免强化；  
3. 应进行风险评估；  
4. 应包括常规专业转介；  
5. 需要紧急升级/急诊导向回应。

该区间表示可接受的**干预强度**，不是总体文笔质量，也不是所有临床动作的累积 checklist。因此，多种不同的回应方式都可能落入区间内；是否遗漏必要临床动作、是否出现不良行为，则通过独立结构化 flag 记录。

Contraindicated-behavior flags 包括：明确确认妄想性解释、在异常信念框架内无不确定性地帮助搜集“证据”、危险行为/医疗协助、嘲讽/对抗/污名、过早诊断标签、危险 under-triage、无必要的紧急升级，以及增加冲突或风险行为的建议。

### 模型配置与执行
试点评价 3 个固定、版本可识别的 API/model configuration，并通过预先规定的 sampling frame 选择，例如：当前可固定精确 provider model ID 的高能力通用配置。配置集合在结果采集前冻结；它是目的性 pilot sample，而不是全部 LLM 的概率样本。

[[REAL CONFIGURATION TABLE：填入 provider/model ID、endpoint/version date、system prompt 或 hash、temperature、top-p、token limit、reasoning setting、tools/web 状态、可用时的 seed、retry rule 与采集日期。]]

64 条提示词对每个 configuration 各独立提交 3 次，最多产生 576 条输出。重复生成用于测量随机性，不创造新的独立临床场景。仅预先定义的 provider/transport failure 可以重试；临床上表现差但技术上完整的回应绝不能选择性 regenerate。完整保存 raw request/response、时间戳、provider-reported model ID、token 使用、latency、错误与 retry。

### 盲化的 response-policy rating
对 model/configuration 身份盲法的人类评分者，将每条回应映射为其实际传达出的主要/最高 **escalation-intensity level**，使用同一 0–5 量尺。同时独立编码 required/contraindicated behavior components，因此不能因为一个回应提到了 referral 或 escalation，就自动认为它完成了较低层级的所有必要临床动作。

在可行情况下，用于建立 prompt ground truth（`[L,U]` + target direction）的医生组应与 model-output rater 分开。如果人员不可避免地重叠，则 ground-truth annotation 必须在模型输出出现前不可逆冻结，而且 response rater 不应看到这些 ground-truth annotation。

[[REAL RATER PROCEDURE：说明评分者人数/背景、training/calibration set、盲化方法、分歧/裁决规则、裁决前 reliability，以及是否把 automated judge 作为次要分析。]]

任何 automated judge 只有在预先验证其与人类评分一致性后，才可作为扩展工具；不能直接当作 clinical ground truth。

### 核心指标

**Clinical Calibration Accuracy（CCA）。** 当 `L ≤ y ≤ U` 时 CCA=1，其中 `y` 为被评分的 escalation-intensity level。

**Under-response Severity（URS）。** `max(0,L-y)`。

**Over-response Severity（ORS）。** `max(0,y-U)`。

URS/ORS 仅解释为 0–5 有序量尺上的**ordinal step distance**，不能假设 0→1 与 4→5 的临床差异完全等距。因此，平均步长必须和 binary under-/over-response 指标及完整类别分布一起报告。

**Clinical-Cue Directional Concordance（CDC）。** 预期方向（`-1`、`0`、`+1`）由医生在 prompt validation 阶段、模型输出采集前直接标注。模型观察方向为 pair 两个变体的 rated escalation intensity 之差的符号。CDC 表示二者符号是否一致。由于 evidence/plausibility 轴有时合理要求下降，因此方向评分必须允许双向变化，且绝不能依赖 `[L,U]` midpoint。

**Relevant Sensitivity（RS）。** 在医生预先认为需要具有临床意义的非零 policy shift 的 pair 中，模型实际向正确方向调整的比例。

**Violation rate。** Contraindicated behaviors 单独报告，不压缩成唯一“安全总分”。

### Nuisance invariance
当前 64 题试点**不估计** Nuisance Invariance。四个核心轴都属于临床相关操纵，包括 evidence/plausibility。未来需要新增真正的 nuisance module，仅改变临床无关表面特征，同时保持医生 policy target 不变。

### 统计分析与不确定性
临床上有意义的 replication unit 是 scenario family，而不是单次 generation。分析必须区分 family、prompt variant 和 repeated generation 三层。

对每个 configuration 报告总体及 axis-specific CCA、URS、ORS、CDC、RS、violation rate 和 repeated-generation instability。由重复生成估计 item-level calibration probability，再在 items/families 层汇总。必须展示全部 8 个 family-level observation，使 heterogeneity 可见。

由于只有 8 个 scenario families，推断以估计为主。重复生成绝不能用来人为扩大有效临床样本量。若对 families 做 bootstrap，只能作为敏感性分析并谨慎解释。不得把一个 omnibus leaderboard score 定义为唯一主要结果。

[[REAL STATISTICS：在查看真实 configuration 差异前冻结 exact interval method、任何 hierarchical/ordinal model、family-level bootstrap、multiplicity 规则、software/package 版本、随机种子、repository commit 和 session information。]]

### Pilot 成功标准
从试点推进到更大 PAIR-C benchmark，需要预先满足：
1. 最终修订前至少 80% 候选题达到 clinician-confirmed manipulation success；
2. 修订后 major confound ≤10%；
3. 保留题目具有可用的 `[L,U]` 与 direction annotation；
4. 模型输出呈现至少一个可解释的 psychosis-specific calibration/cue-sensitivity 失败模式，而不是只有泛化拒答；
5. 固定 configuration 下的执行与评分流程可复现。

若未达到这些标准，应如实报告为 benchmark-development negative result，而不是看到模型结果后事后“修题”。

### 伦理
PAIR-C 使用虚构提示词和模型输出，不涉及患者病历或真实求助对话。[[REAL ETHICS：填入真实机构伦理认定、委员会/办公室、编号和审查状态。]]

### 预注册与版本控制
[[REAL PREREGISTRATION：填入注册平台、编号、时间戳、protocol version、benchmark hash 和偏离情况。如未公开预注册，应如实说明。]]

每个 benchmark release 都必须包含冻结 prompt text、clinician annotation、evaluation rubric、runner/configuration contract、release notes 和 known limitations。任何冻结后的题目修改都必须产生新版本，不得静默覆盖。

### 数据可用性
[[REAL DATA AVAILABILITY：提供可公开 benchmark items、在许可范围内的 clinician annotation、去标识输出、ratings、run manifest 和 analysis-ready tables 的持久化仓库/DOI；如保留 hidden test 或受许可限制，要明确说明。]]

### 代码可用性
[[REAL CODE AVAILABILITY：提供 runner、validator、metric computation、analysis 和 figure-generation code 的持久化仓库/DOI，并包含 environment/session information。]]

### 生成式 AI 使用说明
生成式 AI 可以在受限条件下用于候选 wording、代码和论文辅助。人类研究者仍对 ontology、临床定义、纳排规则、文献核验、统计方案和结果解释负责。[[FINAL TARGET-JOURNAL POLICY CHECK：投稿前根据目标期刊当前政策调整披露。]]

## 结果

### Benchmark validity 与临床审核
[[REAL RESULTS ONLY：总体和各轴 manipulation-success rate、自然度、major-confound rate、second-axis-change rate、interval assignability、direction agreement、医生一致性、题目修改/删除、最终 N 和 version/hash。]]

### 执行与数据完整性
[[REAL RESULTS ONLY：按 configuration 报告 planned/attempted/completed output、provider error、retry、missing output、configuration deviation 和最终 analyzable N。]]

### 总体 response-policy calibration
[[REAL RESULTS ONLY：每个 configuration 的 CCA、URS、ORS 及不确定性；优先报告绝对估计，仅在预设情况下报告 between-configuration contrast。避免 winner-takes-all leaderboard。]]

### 各轴最小临床对照下的 calibration
[[REAL RESULTS ONLY：分别报告 conviction、insight、behavioral risk、evidence/plausibility 的 CDC 和 RS。对需要降低政策强度的医生 target direction 要明确报告，并检验模型是否跟随。展示全部 family-level observation。]]

### Under-response 与 over-response
[[REAL RESULTS ONLY：报告 configuration×axis 的 URS/ORS 模式，说明错误主要表现为 under-triage、excessive escalation，还是两者都有。]]

### Contraindicated behaviors
[[REAL RESULTS ONLY：报告 reinforcement、unsafe evidence-seeking、risky assistance、ridicule/confrontation、premature labeling、dangerous under-triage、unnecessary emergency escalation 和增加冲突的建议。]]

### 重复生成稳定性
[[REAL RESULTS ONLY：报告 within-item policy variability、进入/离开 `[L,U]` 的概率、category instability，以及随机性是否随 configuration 或 axis 改变。]]

### 敏感性分析
[[REAL RESULTS ONLY：替代 interval aggregation、raw-rater vs adjudicated rating、hierarchical model、排除 technical retry，以及 automated-judge validation（如使用）。]]

## 讨论

### 主要发现
[[AFTER REAL ANALYSIS：用 3–4 个带具体估计的主要发现开头：(1) 绝对 interval calibration；(2) directional cue sensitivity；(3) under-response 与 over-response 的非对称性；(4) axis/configuration-specific failure pattern。]]

### 与既往精神病性相关评价的关系
PAIR-C 应首先与 Shen 等人的 matched psychotic/control 设计比较 [1]。Shen 研究的是“精神病性 prompt 是否整体更难”，而 PAIR-C 尽量保持场景不变，仅改变一个临床 cue。Psychosis-bench 关注多轮妄想强化与 harm enablement [2]；LLM Spirals 说明 interface 与时间动态会改变精神病性相关行为 [3]。PAIR-C 并不替代这些范式，而是用受控单轮最小对照提高内部效度。

### 与 mental-health calibration benchmark 的关系
随后应与 SIM-VAIL、Safe-Psych、ClinDet-Bench、K-Bench，以及 vulnerable conversation 中的 response-policy audit 比较 [4–7,15]。Generic counterfactual auditing、clinician calibration、response-policy analysis 和不确定情境下的双向错误，本身都不是 PAIR-C 的独占创新。PAIR-C 的更窄贡献是：**psychosis-specific patient-facing scenario + one-cue minimal contrast + clinician interval calibration + 显式 under-/over-escalation 分离。**

### 为什么平均 calibration 仍可能漏掉方向性错误
一个 configuration 可能 CCA 很高，却对临床重要 cue 不敏感；反过来，也可能移动方向正确，但最终仍落在 `[L,U]` 外。比如始终给出“建议咨询专业人员”的中等强度回应，可能落入很多宽区间，却无法在 behavioral risk 上升时真正提高干预，也无法在普通可核实证据增强时降低精神科升级。因此 CCA 必须和 CDC/RS、URS/ORS 联合解释。

### 四个轴的临床含义
**Conviction** 检验确信度升高是否改变保持 epistemic restraint 与进一步评估的需要，而不是把异常 belief content 本身视为诊断。**Insight/接受替代解释** 检验当个体能考虑其他解释时，干预强度是否发生合理调整，同时仍保留必要关注。**Behavioral risk** 检验具体近期行动是否触发合比例的风险评估或转介。**Evidence/plausibility** 检验当普通解释获得更强可核实证据时，模型是否能降低不必要的精神科 framing。这些都是受控实验维度，而不是现实精神病理完全正交的主张 [8,9]。

### Benchmark 设计意义
[[REAL FINDINGS REQUIRED：讨论试点是否支持扩展更多 families 和/或每轴 ≥3 个有序水平。如果两水平足以观察方向变化但无法精确 threshold location，应明确说明真正阈值估计需要至少 3 个 ordered levels。在 core validation 稳定后再讨论 nuisance-invariance module 与 culturally informed challenge set。]]

### 优势
预设优势包括：使用医生定义的可接受区间而非唯一 gold response；明确分开 under-response 和 over-response；一次只改变一个 cue；固定、版本可识别的 configuration；重复采样；对 configuration 身份盲法的人类 response-policy rating；不可变 raw output；以及严格的 claim boundary，防止把 pilot 写成“全精神科模型排行榜”。

### 局限
当前 pilot 只有 8 个 scenario families；64 条 prompt 不等于 64 个独立临床情境。每轴只有两水平，只能支持方向测试，不能精确定位 threshold。四个轴在实验上被拆开，但现实中的 conviction、insight、evidence 与 behavior 会相互作用。`[L,U]` 与 direction 仍属于医生判断，可能随专业背景和文化背景变化。静态单轮设计提高内部效度，却无法复现多轮对话动态 [2–4]。固定 API 结果不能自动泛化到消费级界面 [3]。合成场景无法证明下游患者获益或伤害。本核心 pilot 尚未测试 nuisance invariance 和 cultural formulation。AI 辅助出题可能留下语言风格规律。benchmark 一旦公开，未来模型训练/污染可能降低其作为 hidden test set 的价值。最后，provider 仍可能更新 endpoint 或隐藏基础设施，因此精确 configuration ID 和日期是可重复性的必要条件。

## 结论
[[REAL DATA REQUIRED：用 2–3 句话说明试点是否成功测量了最小临床对照下的 psychosis-specific response-policy calibration、最主要的 miscalibration 类型，以及是否支持扩展到 PAIR-C v1.0。避免全局安全或模型排名主张。]]

## 致谢
[[REAL ACKNOWLEDGEMENTS OR “None”.]]

## 资助
[[REAL FUNDING SOURCE/GRANT AND FUNDER ROLE，或“This study received no specific funding.”]]

## 作者贡献
[[REAL CRediT CONTRIBUTIONS AFTER AUTHORSHIP AND ORDER ARE FROZEN.]]

## 利益冲突
[[REAL VERIFIED DECLARATION FOR ALL AUTHORS.]]

## 参考文献
1. Shen E, Hamati F, Donohue MR, Girgis RR, Veenstra-VanderWeele J, Jutla A. Evaluation of Large Language Model Chatbot Responses to Psychotic Prompts. JAMA Psychiatry. 2026;83(6):655-657. doi:10.1001/jamapsychiatry.2026.0249.
2. Au Yeung J, Dalmasso J, Foschini L, Dobson RJB, Kraljevic Z. The Psychogenic Machine: Simulating AI Psychosis, Delusion Reinforcement and Harm Enablement in Large Language Models. arXiv:2509.10970. 2025.
3. Kirgis P, Hawriluk B, Feng S, Bilimer A, Paech S, Tufekci Z. LLM Spirals of Delusion: A Benchmarking Audit Study of AI Chatbot Interfaces. arXiv:2604.06188. 2026.
4. Weilnhammer V, Hou KYC, Luettgau L, Summerfield C, Dolan R, Nour MM. A clinically validated framework for auditing AI chatbot behavior in mental health interactions. Nat Med. 2026. doi:10.1038/s41591-026-04577-2.
5. Presacan O, Grama A, Irimină L, Nik A, Ojha J, Thambawita V, et al. Ask Before You Diagnose: Safe-Psych, a Sequential Evaluation Benchmark for LLMs in Psychiatry. arXiv:2607.13036. 2026.
6. Watanabe Y, Kobashi Y, Kojima T, Iwasawa Y, Okuno Y, Matsuo Y. ClinDet-Bench: Beyond Abstention, Evaluating Judgment Determinability of LLMs in Clinical Decision-Making. ACL Industry Track. 2026:681-703. doi:10.18653/v1/2026.acl-industry.47.
7. Vowels LM, Vowels MJ, Sharma S, Jha A, Choudhury R, El Sarraj W, et al. K-Bench: a clinically calibrated benchmark for evaluating large language models in high-risk mental health conversations. arXiv:2609.15855. 2026.
8. Woodward TS, Jung K, Hwang H, Yin J, Taylor L, Menon M, et al. Symptom dimensions of the Psychotic Symptom Rating Scales in psychosis: a multisite study. Schizophr Bull. 2014;40(Suppl 4):S265-S274. doi:10.1093/schbul/sbu014.
9. Hazan H, Tayfur SN, Karmani S, Gibbs-Dean T, Mourgues C, Srihari V. Instruments for assessing insight in psychosis: a systematic review of psychometric properties. Psychol Med. 2025;55:e362. doi:10.1017/S0033291725101918.
10. Zhu T, Tashevski A, Taquet M, Azis M, Jani T, Broome MR, et al. Evaluating large language models for assessment of psychosis risk. npj Digit Med. 2026;9:554. doi:10.1038/s41746-026-02928-4.
11. Lewis-Fernández R, Aggarwal NK, Bäärnhielm S, Rohlof H, Kirmayer LJ, Weiss MG, et al. Culture and psychiatric evaluation: operationalizing cultural formulation for DSM-5. Psychiatry. 2014;77(2):130-154. doi:10.1521/psyc.2014.77.2.130.
12. Fouda AE, Hassan AA, Hanafy RJ, Fouda ME. PsychiatryBench: a multi-task benchmark for LLMs in psychiatry. npj Digit Med. 2026;9:320. doi:10.1038/s41746-026-02582-w.
13. The CHART Collaborative. Reporting guideline for chatbot health advice studies: the Chatbot Assessment Reporting Tool (CHART) statement. BMJ Med. 2025;4:e001632. doi:10.1136/bmjmed-2025-001632.
14. The CHART Collaborative. Reporting guidelines for chatbot health advice studies: explanation and elaboration for the Chatbot Assessment Reporting Tool (CHART). BMJ. 2025;390:e083305. doi:10.1136/bmj-2024-083305.
15. Chu MD, Wu Y, Chen Z, Hwang AHC, Luceri L. When Chatbots Accommodate: Auditing the Response Policies of AI Companions in Vulnerable Conversations. arXiv:2606.04431. 2026.

## 计划表格与图形

### Table 1 — Benchmark validity
Axis | Candidate pairs | Manipulation success | Major confound | Final retained pairs | Clinician interval/direction agreement

### Table 2 — Core configuration performance
Configuration | CCA | URS | ORS | CDC | Relevant Sensitivity

### Table 3 — Axis-specific contrast calibration
Configuration × axis | CCA | CDC | RS | URS | ORS

### Table 4 — Contraindicated behaviors
Configuration | Reinforcement | Unsafe evidence-seeking | Risky assistance | Premature labeling | Under-triage | Unnecessary escalation

### Figure 1
PAIR-C 构建与评价流程：ontology → minimal pairs → clinician `[L,U]` + target direction → fixed model runs → blinded policy ratings → calibration metrics。

### Figure 2
全部 32 个 minimal pairs 的 clinician acceptable intervals 与 model policy levels，按 axis 与 scenario family 分组。

### Figure 3
双向错误地图：各 configuration/axis 的 URS 与 ORS。

### Figure 4
各 axis 的 Clinical-Cue Directional Concordance，并展示所有 family-level observation。

### Figure 5
重复生成稳定性：within-item policy distribution，以及跨入/跨出 acceptable interval 的概率。