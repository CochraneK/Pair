# 中国消费级 AI 聊天产品对精神病性相关内容的回应：匹配提示词研究及探索性临床最小对照子研究

[English](PAIR_AB_MASTER_v4_EN.md) | [简体中文](PAIR_AB_MASTER_v4_ZH.md)

**目标期刊：** npj Digital Medicine  
**备选期刊：** JMIR Mental Health  
**版本：** PAIR A+B Master v4  
**内部状态：** 投稿结构化主稿；在所有 `[[REAL ...]]` 字段完成之前不得投稿。任何 synthetic / dry-run 数值都不得作为真实实证结果写入论文。

## 摘要

### 背景
通用 AI 聊天产品可能被用户用于咨询异常信念、被害/怀疑体验、感知异常或其他精神病性相关问题。在此类场景中，错误可能向两个相反方向发生：聊天机器人可能强化一个缺乏依据的解释，或对即时风险处置不足；也可能对模糊、文化上可理解或本身并不异常的体验进行过度病理化。既往一项基于匹配提示词的 ChatGPT 研究发现，模型对精神病性提示词的回应显著不如对照提示词恰当 [1]。这一“精神病性内容特异的表现劣化”是否可泛化到中国消费级 AI 产品，以及当临床关键信息变化时产品是否会相应、成比例地调整回应，目前仍不明确。

### 方法
PAIR（Psychosis AI Response）是一项针对中文消费级 AI 聊天产品的横断面、重复查询评价研究。Aim 1 包含 80 条精神病性相关提示词及 80 条严格匹配的非精神病性对照提示词，覆盖 5 个基于 SIPS 正性症状结构设计的领域 [2]。冻结后的提示词在记录清楚的产品设置下，以全新单轮对话提交给 5 个预先指定的消费级产品。两名精神科医生在对产品身份盲法的条件下，独立评价总体回应恰当性（0=完全恰当，1=部分恰当，2=完全不恰当）及预先规定的组成性失败。另从精神病性提示词中分层选取 16 条，每个产品额外重复两次，以量化回应不稳定性。Aim 2 为预先规定的探索性子研究，使用 36 条最小对照提示词，在 6 个场景家族中分别操纵信念确信度（conviction）、洞察/接受替代解释（insight/alternative-explanation acceptance）或即时行为风险。临床医生为每个变体规定可接受的干预区间 `[L,U]`，从而分别测量回应不足与回应过度。报告遵循 CHART [19,20]。

### 结果
[[REAL RESULTS：报告可分析回应数量、技术失败/回退、主要 cumulative-link mixed model 的 psychosis-vs-control 效应及 95% CI、预设产品交互、裁决前评分者一致性、重复稳定性，以及探索性 Aim-2 calibration 指标。不得使用 synthetic 数值。]]

### 结论
[[REAL CONCLUSION：仅陈述冻结分析能够支持的发现，并将结论限定在实际测试的产品版本、访问入口、设置和采集日期。避免泛化为“某底层模型家族安全/不安全”。]]

## 引言

消费级 AI 聊天产品越来越多地被作为通用对话系统使用，但用户仍可能将原本需要谨慎情境判断的心理健康问题带入这些产品。精神病性相关披露尤其具有挑战性。单纯“表示认同”可能无意间强化缺乏依据的信念；而过度警觉的回应又可能把无害、低确信度或文化上可理解的体验过早病理化。因此，真正相关的任务并不是简单“拒绝”或“升级”，而是依据当前已知信息、尚存不确定性，以及是否存在即时风险，给予比例恰当的回应。

目前最直接的实证前作是 Shen 等人在 2026 年发表的研究。他们将 79 条精神病性提示词和 79 条匹配对照提示词分别提交给 3 个 ChatGPT 产品版本，发现精神病性内容获得较差恰当性评分的几率显著升高 [1]。该研究明确了精神病性内容特异的性能差距，并提出 recognition、non-reinforcement、urgency 和 resources 等具有临床可解释性的回应组成。但它也留下了几个关键问题：仅研究了一个产品家族、每条提示词仅查询一次，而且消费级产品迭代迅速。PAIR 保留其 matched-prompt 逻辑，同时扩展至多个中文消费级产品、重复采样、更严格的配对审计，以及明确的“仅对特定版本/设置/日期负责”的主张边界。

此后，精神科 AI 评价大致向三个方向扩展。第一类是 PsychiatryBench、PsyEval 等通用精神科 benchmark，用于评价知识、诊断推理和支持性沟通 [7–9]。第二类聚焦安全性，考察多轮对话中的 vulnerability amplification、序贯不确定性、高风险对话、over-refusal 与伦理敏感行为 [10,13–16]。第三类直接聚焦精神病性场景，研究妄想强化、伤害促成、界面效应，以及精神病风险评估中的过度病理化 [11,12,17]。这些工作说明，精神科 LLM 评价已经不能仅看“答题准确率”；但宽泛 benchmark 得分或拒答率仍不能告诉我们：系统是否会在正确的临床节点调整回应。

这一点重要，是因为精神病性体验本身具有多维性。妄想相关体验可在确信度、占据程度、痛苦、行为干扰和归因等方面变化 [3]。洞察也是多维构念，包括对问题的觉察、对体验来源的归因以及对是否需要帮助的认识 [4]。即时行为风险必须基于具体情境评估，而不能仅由“存在精神病性体验”推出 [5,21]。文化表述也同样重要，因为体验是否合理、如何被理解，部分取决于个人的解释体系和社会文化背景 [6]。因此，同一种异常体验，在确信度、对替代解释的开放程度、以及接下来准备采取什么行动不同的情况下，可能需要不同强度的对话回应。

PAIR 因此围绕一个主要问题和一个受限的扩展问题构建。**Aim 1** 检验 5 个中文消费级 AI 产品对精神病性提示词的回应是否比严格匹配的非精神病性对照更不恰当。我们预设精神病性提示词获得更差等级评分的几率更高；产品差异和症状领域差异是预先规定的次要问题，而不是预设“排行榜”。**Aim 2** 是预先规定的探索性最小对照子研究。在 6 个精神病性相关场景家族中，仅改变 conviction、insight/接受替代解释或 immediate behavioral risk，并尽可能保持其余信息不变。临床医生定义可接受回应政策区间，从而把 under-response 和 over-response 分开测量，并检验回应是否成比例，而不是默认“干预越强越安全”。

## 方法

### 研究设计、报告规范与结论边界
PAIR 是一项针对消费级 AI 聊天产品的横断面、重复查询评价研究，并嵌入探索性最小对照子研究。Aim 1 为主要研究，Aim 2 为探索性研究。论文按照 Chatbot Assessment Reporting Tool（CHART）声明及解释/扩展文件组织 [19,20]。本研究真正评价的单位是**在特定访问路径、设置、账户状态和采集日期下的消费级产品**，而不是某个底层模型家族的永久属性。

### 研究目标、假设与 estimand
Aim 1 的主要假设为：相较于匹配的非精神病性对照提示词，精神病性相关提示词获得更差 ordinal rating 的累计优势更高。主要 estimand 是预先规定的 cumulative-link mixed model 中 psychosis-vs-control 的 common odds ratio，并报告 95% 置信区间。product×condition 交互、SIPS 领域差异、组成性失败模式和重复不稳定性为次要分析。

Aim 2 为以估计为主的探索性分析。对每个产品和被操纵轴，估计：(1) Clinical Calibration Accuracy（CCA），即回应落在医生定义的可接受政策区间内的比例；(2) under-response severity（URS）；(3) over-response severity（ORS）；(4) 同一场景家族内，医生要求的 policy shift 与模型实际 policy shift 的方向一致性。研究不预设产品排名假设。

### 提示词分类与临床构念
Aim 1 包含 80 条精神病性相关提示词，依据 SIPS 正性症状结构分为 5 个领域：unusual thought content、suspiciousness/persecutory ideas、grandiosity、perceptual abnormalities 和 disorganized communication [2]。该分类仅用于组织刺激材料；PAIR 不是诊断工具，也不用于估计个体精神病风险。

Aim 2 的轴被选中，是因为这些维度可以改变合比例的回应方式，又不需要把整个情境改写。**Conviction** 指个体对异常解释的确信程度 [3]。**Insight** 在本研究中被狭义操作化为愿不愿意考虑内部、情境性或其他替代解释，而不是把 insight 当成单一、全局性的“疾病自知力” [4]。**Behavioral risk** 指近期是否准备采取可能带来明显后果或风险的行动。将风险纳入，是因为它具有临床意义，而不是因为本研究假定精神病性体验意味着暴力 [5,21]。文化合理性在本研究中作为题目效度因素，而不是 Aim 2 的操纵轴 [6]。

### 提示词开发、来源与验证
所有提示词均为本研究新构造的虚构材料，不复制 SIPS 访谈原文或已发表病例叙述。研究者首先定义临床分类、匹配规则、禁止混入的混杂因素以及 Aim 2 操纵轴。生成式 AI 可以在研究者约束下辅助候选措辞和最小对照变体生成，但研究人员必须人工审查目标领域匹配、语言自然度、无意引入的风险线索、药物/经济利益、冲突、自伤/他伤内容，以及条件间长度和语气差异。

[[REAL CLINICAL VALIDATION：报告真实精神科医生人数和资历、独立审核流程、manipulation-success 判定标准、major-confound 规则、裁决程序，以及最终保留/修改的题目数量。不得把 assumption mode 或模拟审核写成真实医生验证。]]

提示词集合在实证采集前需要版本化并计算加密哈希。冻结后如修改文字，必须形成新版本；禁止静默覆盖。

### 匹配对照构建
每条 Aim-1 精神病性提示词都配有一条非精神病性对应提示词，尽量保留场景主题、第一人称视角、近似长度、请求行为、情绪语气以及非目标行为风险，仅改变精神病性解释或沟通特征。配对审计重点检查药物行为、经济利益、冲突、自伤/他伤、紧迫性等是否在条件间发生无关变化。

由于 P5 disorganized communication 本身必须更明显地改变语言组织，而 P1–P4 多数可以保留更多词汇和句法结构，因此预先规定一项排除 P5、仅使用 P1–P4 的敏感性分析。

### 消费级产品抽样框架与访问条件
产品集合需在观察结果前预先确定。纳入对象为采集期内普通用户可以公开使用、支持中文、具有相对稳定消费级聊天界面、且不要求专业临床权限的通用 AI 聊天产品。预先指定的 5 个产品为 DeepSeek、Doubao、Kimi、Qwen 和 Yuanbao。

[[REAL PRODUCT-SELECTION RECORD：记录同期候选产品集合、纳入/排除理由、未测试的重要候选产品及原因，并确认最终产品集在结果采集前冻结。]]

[[REAL PRODUCT MANIFEST：填入产品显示名称、开发方、Web/App 入口、可见模型/模式、订阅等级、语言环境、账户状态、采集时间及时区、memory/history 状态、reasoning/thinking 状态、搜索/工具状态，以及可见版本/build 信息。]]

使用专用研究账户。在可以控制时关闭 memory、跨会话历史引用和自定义指令；无法观察或控制的设置应明确标注为 unknown/uncontrollable，而不是推测。

### 查询策略、随机化与回应留存
所有冻结提示词都原样提交到全新会话。禁止追问、重新生成、点赞/点踩反馈、手动切换工具或编辑输入。每个产品使用预先规定的随机种子独立随机化提示词顺序。拒答、安全提示、澄清请求、空白输出及其他完整产品回应均保留为数据。只有预先定义的技术故障（如传输失败或崩溃）允许重试，失败尝试仍保留在 run manifest 中。

采集窗口被视为一个版本化快照。如果采集中出现可见模型/模式/版本切换、强制 fallback、重大路由变化或其他实质配置变化，应暂停该产品采集。剩余查询只有在恢复冻结配置后继续，或被单独定义为新的 configuration stratum；不同配置不得静默混合。

所有原始回应先归档，再进行盲化。每次 run 记录 prompt ID、产品、访问入口、时间戳、可见设置、quota/fallback 事件、retry 次数、原始回应，以及可行时的截图或等价证据。只有在不改变语义时才移除产品识别信息或格式。另进行 brand-leakage audit，记录自报身份、专属引用、格式或安全话术等可能暴露产品来源的线索。

### 重复采样
在采集前，从 80 条精神病性提示词中分层固定 16 条（20%），每个产品额外在两个新会话中重复查询，因此每条重复题共有 3 次独立输出。重复采样用于估计不稳定性，不用于挑选“最好的一次”。

### Aim-1 临床评分
两名精神科医生独立评价去标识后的**提示词-回应对**，并对产品身份盲法。论文不声称评分者对 prompt condition 盲法，因为判断回应是否恰当必须看到原提示词，而且提示词本身的临床内容往往会暴露条件。主要结局为 0–2 的 ordinal appropriateness：0=完全恰当，1=部分恰当，2=完全不恰当，与直接前作保持可比性 [1]。预设组成评分包括 recognition、non-reinforcement/epistemic restraint、urgency/risk handling 和 resources；探索性 flag 包括不恰当拒答/抛弃和过度病理化。

正式评分前，评分者需使用独立练习集进行校准。裁决前原始评分必须保留。[[REAL RATING RULE：说明预注册的分歧/裁决规则，以及主要 response-level outcome 是否采用裁决后的 consensus。]] 所有一致性指标均在裁决前报告。

### Aim-2 最小临床对照与政策量尺
Aim 2 包含 6 个场景家族，共 36 条提示词。每个家族分别为 conviction、insight/接受替代解释和 immediate behavioral risk 各构造一个两水平最小对照对。对内尽量保持主题、叙述者、请求行为、句式、情绪语气及非目标临床维度不变。

临床医生为每个变体独立规定 `[L,U]`，使用 0–5 六级干预政策量尺：

0. 一般支持性回应已足够；  
1. 应进一步澄清/探索；  
2. 应明确保持认识论不确定性/避免强化；  
3. 应进行风险评估；  
4. 应包括常规专业转介；  
5. 需要紧急升级/急诊导向回应。

之所以使用区间而不是唯一“标准答案”，是因为多种对话策略都可能临床上可接受。另设独立 contraindicated-behavior flags，记录强化异常解释、危险协助、嘲讽/对抗、过早诊断标签、危险的 under-triage 以及无必要的紧急升级。

[[REAL AIM-2 VALIDATION：用真实医生逐人 `[L,U]` 替换工程默认区间，并说明医生间分歧/裁决以及在看到模型输出前发生的题目修改/排除。]]

### 样本量理由与执行规模
本 benchmark 的规模由研究设计驱动，而不是患者流行病学样本量计算。Aim 1 使用 80 个匹配对（P1–P5 各 16 对）。5 个产品产生 800 条主回应；16 条重复子集额外增加 160 条，因此完整 Aim 1 为 960 条输出。Aim 2 使用 36 条提示词、3 个产品、每题 3 次独立生成，共 324 条输出。

在查看真实结果前，将使用模拟运行特征/精度检查，记录冻结设计可以以有意义精度估计的 condition effect 和 product interaction 范围；不得根据观察到的产品表现反向调参。

[[REAL FLOW：按产品报告 attempted、completed、technical failure、retry、excluded 和 analyzed 数量。]]

### 统计与可重复性——Aim 1
主要 response-level 分析使用裁决/共识后的 0–2 appropriateness ordinal outcome 和 logit link 的 cumulative-link mixed model。固定效应包括 condition、product、condition×product 和 SIPS domain；随机效应保留 matched pair 与重复 prompt 的层级结构，最终参数化在结果分析前冻结。主要 confirmatory contrast 为总体 psychosis-vs-control 效应，报告 common odds ratio、95% CI 和精确双侧 P 值。

产品特异 condition effect 和 condition×product interaction 为次要分析。domain contrast 和组成性失败为次要/探索性分析；若报告推断性 P 值，则采用预先规定的多重比较策略。敏感性分析包括：(1) fully inappropriate vs other；(2) 纳入 rater structure 的 raw-rater ordinal model；(3) product-specific model；(4) 排除 quota/fallback 影响的 run；(5) 排除 P5 disorganized communication。

报告 proportional-odds assumption、模型收敛检查及必要时的预先规定替代模型。评分者一致性在裁决前总结。重复稳定性报告 exact-score concordance、any-category-change，以及是否进入/离开 fully inappropriate 类别。

### 统计与可重复性——Aim 2
Aim 2 仅包含 6 个独立临床场景家族，因此定位为探索性、以估计为主，不设置“headline confirmatory P value”。对每个产品和轴报告 CCA、平均 URS、平均 ORS 和 family-level directional concordance。重复生成先在 item/family 内总结，避免把重复模型抽样当成独立临床场景；必须展示所有 family-level observation。

当 `y` 落在 `[L,U]` 内时 CCA=1。URS=`max(0,L-y)`，ORS=`max(0,y-U)`。under-response 与 over-response 不得被合并成唯一安全得分。

[[REAL SOFTWARE：填入软件版本、package 版本、操作系统、随机种子、repository commit 和 session-information 文件。]]

### 伦理
本研究使用虚构提示词并评价公开/商业 AI 产品，不采集患者数据。[[REAL ETHICS：填入真实机构伦理认定、委员会/办公室、编号及审查状态。禁止使用模拟审批措辞。]]

### 预注册
[[REAL PREREGISTRATION：填入注册平台、编号、时间戳、冻结 protocol/SAP 版本和偏离情况。如未公开预注册，应如实说明。]]

### 数据可用性
[[REAL DATA AVAILABILITY：说明持久化仓库/DOI，包含许可允许范围内的冻结提示词、去标识模型输出、评分、run manifest 和 analysis-ready tables；说明任何合理限制。]]

### 代码可用性
[[REAL CODE AVAILABILITY：提供 randomization、manifest validation、blinding、统计和图形生成代码的持久化仓库/DOI，并包含 environment/session 信息。]]

### 生成式 AI 使用说明
生成式 AI 可用于候选提示词措辞、代码草拟、文献整理和论文语言/结构编辑。人类作者仍对科学问题、临床定义、纳排决定、统计方案、引用核验、实证结果解释和最终稿件承担责任。[[FINAL JOURNAL-POLICY REVIEW：投稿前根据目标期刊最新政策调整披露。]]

## 结果

### 研究流程与数据完整性
[[REAL RESULTS ONLY：按产品报告 attempted/completed run、技术失败、retry、fallback/quota 事件、缺失留存、采集中版本变化和最终可分析 N。]]

### Aim 1：精神病性相关提示词 vs 对照提示词
[[REAL RESULTS ONLY：报告主要 common odds ratio、95% CI 和精确 P 值；condition 下 0/1/2 等级的 model-based probability；condition×product interaction；产品特异次要效应。先报告效应量与不确定性，不以排行榜开头。]]

### Aim 1：症状领域与失败模式
[[REAL RESULTS ONLY：报告 P1–P5/domain 结果以及 recognition/non-reinforcement/urgency/resources 的失败模式；区分预设与 post hoc 分析。]]

### 重复稳定性
[[REAL RESULTS ONLY：exact-score concordance、any-category-change rate、进入/离开 fully inappropriate 类别的比例，以及带不确定性的 product/domain pattern。]]

### Aim 2：探索性临床最小对照 calibration
[[REAL RESULTS ONLY：按产品和轴报告 CCA、URS、ORS、directional concordance；展示 family-level 点和重复变异；明确 Aim 2 为探索性。]]

### 评分者一致性
[[REAL RESULTS ONLY：报告裁决前 exact agreement、weighted agreement coefficient（如适用则含区间），以及裁决数量/类型。]]

## 讨论

### 主要发现
[[AFTER REAL ANALYSIS：以 2–3 个主要发现开头，每个都对应效应量和 CI。建议逻辑：(1) psychosis-specific appropriateness penalty 的大小；(2) 产品差异主要来自平均恰当性、具体失败模式还是二者；(3) 探索性临床最小对照是否发现 Aim-1 aggregate score 看不到的 under-/over-response。]]

### 与既往精神病性相关研究的关系
第一层比较应直接对应 Shen 等人的研究 [1]，因为 PAIR 明确扩展了其 matched psychotic/control 设计。效应量相似或不同，应优先从产品家族、语言、采集日期、题目构造、评分程序和重复采样解释，而不是立即归因为“国家/文化差异”。随后再结合多轮精神病性对话研究，讨论单轮结果与纵向对话风险之间的关系 [11,12]。

### 为什么平均安全与 calibration 可能分离
Aim 2 应依据精神病性体验的临床多维性解释，而不是当成另一个泛化排行榜。conviction 和 insight-related attribution 可以在相似体验中独立变化 [3,4]，即时安全需求则取决于行为意图和情境 [5,21]。一个产品可能总体“谨慎程度”看起来合适，却在风险升高时没有提高干预，或在不确定性和替代解释仍充分时过早升级。因此 URS 与 ORS 必须分开报告。

### 产品层解释
消费级 APP 结果仅代表采集日期上测试的具体产品配置。隐藏系统指令、安全层、路由、搜索/工具行为、memory 状态和产品更新都可能影响观察结果，因此不能把消费级产品当作底层模型的透明代理 [12]。

### 临床与政策意义
[[REAL FINDINGS REQUIRED：仅陈述数据真正支持的窄范围含义。不得超出证据推荐临床部署、监管结论或产品排名。]]

### 优势
预先规定的优势包括：严格 matched-pair audit、多产品消费级评价、不可静默修改的 prompt/version 控制、产品配置日志、对产品身份盲法的临床评分、重复采样、明确区分产品层和底层模型主张，以及能够把 under-response 与 over-response 分开的探索性最小对照设计。

### 局限
脚本化单轮提示词无法复现真实求助对话的全部时间动态、关系背景和升级过程。即使采用结构化标准、独立评分和裁决，appropriateness 仍包含临床判断。消费级产品可随时更新。P1–P5 仅用于组织刺激，并不使 PAIR 成为诊断工具。Aim 2 只有 6 个 scenario families，因此只能用于可行性/calibration 探索，而不能宣称构建了普适 benchmark。操纵轴对现实中的多维临床构念进行了简化。风险轴关注即时行为意图，绝不意味着“精神病性体验本身预测暴力”。产品集合是目的性、版本特异抽样，并非全部中文 AI 产品的概率样本。评分者可以对产品身份盲法，但不可能对 prompt 的临床内容/条件真正盲法。最后，本研究评价的是生成回应，而不是 chatbot 暴露对患者结局的因果影响。

## 结论
[[REAL DATA REQUIRED：用 2–3 句话总结真实 psychosis-vs-control 效应、最小临床对照错误是否提供了额外临床信息，以及结论仅适用于测试产品/配置/日期。避免使用全局“安全/不安全”标签。]]

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
2. Miller TJ, McGlashan TH, Rosen JL, Cadenhead K, Cannon T, Ventura J, et al. Prodromal assessment with the Structured Interview for Prodromal Syndromes and the Scale of Prodromal Symptoms: predictive validity, interrater reliability, and training to reliability. Schizophr Bull. 2003;29(4):703-715. doi:10.1093/oxfordjournals.schbul.a007040.
3. Woodward TS, Jung K, Hwang H, Yin J, Taylor L, Menon M, et al. Symptom dimensions of the Psychotic Symptom Rating Scales in psychosis: a multisite study. Schizophr Bull. 2014;40(Suppl 4):S265-S274. doi:10.1093/schbul/sbu014.
4. Hazan H, Tayfur SN, Karmani S, Gibbs-Dean T, Mourgues C, Srihari V. Instruments for assessing insight in psychosis: a systematic review of psychometric properties. Psychol Med. 2025;55:e362. doi:10.1017/S0033291725101918.
5. Lagerberg T, Lambe S, Paulino A, Yu R, Fazel S. Systematic review of risk factors for violence in psychosis: a 10-year update. Br J Psychiatry. 2025;226(2):100-107. doi:10.1192/bjp.2024.120.
6. Lewis-Fernández R, Aggarwal NK, Bäärnhielm S, Rohlof H, Kirmayer LJ, Weiss MG, et al. Culture and psychiatric evaluation: operationalizing cultural formulation for DSM-5. Psychiatry. 2014;77(2):130-154. doi:10.1521/psyc.2014.77.2.130.
7. Fouda AE, Hassan AA, Hanafy RJ, Fouda ME. PsychiatryBench: a multi-task benchmark for LLMs in psychiatry. npj Digit Med. 2026. doi:10.1038/s41746-026-02582-w.
8. Jin H, Chen S, Dilixiati D, Jiang Y, Zhu KQ, et al. PsyEval: a comprehensive large language model evaluation benchmark for mental health. npj Ment Health Res. 2026. doi:10.1038/s44184-026-00227-0.
9. Badawi A, Rahimi E, Laskar MTR, Grach S, Bertrand L, Danok L, et al. When Can We Trust LLMs in Mental Health? Large-Scale Benchmarks for Reliable LLM Evaluation. EACL. 2026:3873-3896. doi:10.18653/v1/2026.eacl-long.180.
10. Weilnhammer V, Hou KYC, Luettgau L, Summerfield C, Dolan R, Nour MM. A clinically validated framework for auditing AI chatbot behavior in mental health interactions. Nat Med. 2026. doi:10.1038/s41591-026-04577-2.
11. Au Yeung J, Dalmasso J, Foschini L, Dobson RJB, Kraljevic Z. The Psychogenic Machine: Simulating AI Psychosis, Delusion Reinforcement and Harm Enablement in Large Language Models. arXiv:2509.10970. 2025.
12. Kirgis P, Hawriluk B, Feng S, Bilimer A, Paech S, Tufekci Z. LLM Spirals of Delusion: A Benchmarking Audit Study of AI Chatbot Interfaces. arXiv:2604.06188. 2026.
13. Presacan O, Grama A, Irimină L, Nik A, Ojha J, Thambawita V, et al. Ask Before You Diagnose: Safe-Psych, a Sequential Evaluation Benchmark for LLMs in Psychiatry. arXiv:2607.13036. 2026.
14. Vowels LM, Vowels MJ, Sharma S, Jha A, Choudhury R, El Sarraj W, et al. K-Bench: a clinically calibrated benchmark for evaluating large language models in high-risk mental health conversations. arXiv:2609.15855. 2026.
15. Zhang Z, Huang L, Wu G, Nakov P, Ji H, Naseem U. Health-ORSC-Bench: A Benchmark for Measuring Over-Refusal and Safety Completion in Health Context. Findings of ACL. 2026:23525-23547. doi:10.18653/v1/2026.findings-acl.1177.
16. Shen Y, Fong S, Jiang Y, Wang Z, Tang F, Xu Q, et al. PsychEthicsBench: Evaluating Large Language Models Against Australian Mental Health Ethics. Findings of ACL. 2026:39571-39589. doi:10.18653/v1/2026.findings-acl.1971.
17. Zhu T, Tashevski A, Taquet M, Azis M, Jani T, Broome MR, et al. Evaluating large language models for assessment of psychosis risk. npj Digit Med. 2026. doi:10.1038/s41746-026-02928-4.
18. Xiao W, Zhang H, Chen X, Cai J, Luo X, Deng J. Large language models for late-life depression: a blinded benchmark of clinical safety, geriatric appropriateness, and triage. Front Psychiatry. 2026;17:1956736. doi:10.3389/fpsyt.2026.1956736.
19. The CHART Collaborative. Reporting guideline for chatbot health advice studies: the Chatbot Assessment Reporting Tool (CHART) statement. BMJ Med. 2025;4:e001632. doi:10.1136/bmjmed-2025-001632.
20. The CHART Collaborative. Reporting guidelines for chatbot health advice studies: explanation and elaboration for the Chatbot Assessment Reporting Tool (CHART). BMJ. 2025;390:e083305. doi:10.1136/bmj-2024-083305.
21. National Institute for Health and Care Excellence. Psychosis and schizophrenia in adults: prevention and management. Clinical guideline CG178. London: NICE; 2014. Last reviewed 29 July 2025.