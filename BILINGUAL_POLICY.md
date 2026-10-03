# PAIR bilingual maintenance policy / PAIR 双语维护规则

## English

PAIR public-facing research materials are bilingual by default.

The following artifacts must be maintained in synchronized **English + Simplified Chinese** versions:

1. repository README;
2. current manuscript masters for Paper 1 (A+B) and Paper 2 (C);
3. manuscript conversation-exemplar modules and their selection rules;
4. public HTML discussion pages and GitHub Pages navigation/content;
5. manuscript-state / public handoff pages where a language-specific version materially improves usability;
6. public-facing protocol summaries or clinician-facing pages when they are intended for both Chinese- and English-speaking collaborators.

### Canonical naming

- `README.md` = English
- `README.zh-CN.md` = Simplified Chinese
- `manuscript/*_EN.md` = English manuscript or manuscript module
- `manuscript/*_ZH.md` = Simplified Chinese manuscript or manuscript module

### Synchronization rule

A substantive scientific change is not considered publicly complete until both language versions are updated.

The two versions must preserve the same:
- study design;
- sample/output counts;
- hypotheses and estimands;
- statistical definitions;
- evidence boundaries;
- ethics/preregistration status;
- manuscript version number;
- conversation-exemplar selection rule;
- warnings about synthetic/dry-run data;
- submission gates.

Translation may adapt sentence structure for natural academic Chinese/English, but it must not change scientific claims.

### Conversation exemplars in papers

Both manuscripts must include representative prompt-response examples rather than reporting only numerical metrics.

- Paper 1 (A+B): at least one matched psychosis/control example and one minimal clinical-contrast example.
- Paper 2 (C): at least one minimal clinical-contrast pair linked to the principal empirical finding.
- Additional examples may move to the Supplement.
- Example selection must follow a frozen rule and must not be based on which response is most dramatic or narratively convenient.
- Synthetic examples are permitted only in clearly labeled rehearsal materials; the empirical manuscript must use real collected outputs and clinician-frozen ground truth.

### HTML / GitHub Pages

GitHub Pages is the intended meeting/presentation interface, not merely a repository landing page.

- `docs/index.html` = meeting discussion handbook;
- `docs/papers.html` = embedded bilingual full-paper reader for A+B and C;
- embedded papers must append the corresponding conversation-exemplar module;
- `docs/dashboard.html` = technical project index;
- `docs/index.html` and `docs/papers.html` must retain obvious English/中文 switching.

When GitHub Pages is enabled, later edits must not degrade the meeting interface into a single-language or purely technical dashboard.

## 中文

PAIR 的对外研究材料默认采用**英文 + 简体中文双语同步维护**。

以下内容必须保持中英双版：

1. 仓库 README；
2. Paper 1（A+B）和 Paper 2（C）的当前论文 Master；
3. 论文中的对话样例模块及其样例选择规则；
4. 对外 HTML 讨论页与 GitHub Pages 的导航和核心内容；
5. 面向公开协作的论文状态/交接页面（在双语能明显提高可用性时）；
6. 同时面向中英文协作者的公开 protocol summary 或 clinician-facing 页面。

### 规范命名

- `README.md` = 英文
- `README.zh-CN.md` = 简体中文
- `manuscript/*_EN.md` = 英文论文或论文模块
- `manuscript/*_ZH.md` = 中文论文或论文模块

### 同步规则

任何实质性科学修改，在中英文两版均完成同步之前，都不能视为“公开版本已经更新完毕”。

两版必须严格保持一致的：
- 研究设计；
- 样本量/输出量；
- 假设和 estimand；
- 统计定义；
- 证据边界；
- 伦理/预注册状态；
- 论文版本号；
- 对话样例选择规则；
- synthetic/dry-run 警示；
- 投稿 gate。

翻译可以为符合学术中文/英文习惯而调整句法，但不能改变科学主张。

### 论文中的对话样例

两篇论文都必须展示代表性的 prompt-response 对话，而不能只报告统计数字。

- Paper 1（A+B）：至少 1 组 psychosis/control matched pair + 1 组 minimal clinical contrast；
- Paper 2（C）：至少 1 组与主要实证发现对应的 minimal clinical-contrast pair；
- 更多样例可进入 Supplement；
- 样例必须按预先冻结的规则选择，不能因为“更戏剧化、更好讲故事”而 cherry-pick；
- Synthetic 例子只能出现在明确标注的 rehearsal 材料里；实证论文必须换成真实采集输出和医生冻结后的 ground truth。

### HTML / GitHub Pages

GitHub Pages 是会议/讲解的主界面，而不是普通仓库首页。

- `docs/index.html` = 会议讨论手册；
- `docs/papers.html` = A+B 与 C 的双语论文全文内嵌阅读器；
- 内嵌论文后必须自动附上对应的对话样例模块；
- `docs/dashboard.html` = 技术项目索引；
- `docs/index.html` 和 `docs/papers.html` 必须持续提供明显的 English / 中文切换。

GitHub Pages 启用后，后续修改不得退化成单语页面，也不得重新变成只有技术导航的 AI-dashboard 风格。