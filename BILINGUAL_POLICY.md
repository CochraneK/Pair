# PAIR bilingual maintenance policy / PAIR 双语维护规则

## English

PAIR public-facing research materials are bilingual by default.

The following artifacts must be maintained in synchronized **English + Simplified Chinese** versions:

1. repository README;
2. current manuscript masters for Paper 1 (A+B) and Paper 2 (C);
3. public HTML dashboards and GitHub Pages navigation/content;
4. manuscript-state / public handoff pages where a language-specific version materially improves usability;
5. public-facing protocol summaries or clinician-facing pages when they are intended for both Chinese- and English-speaking collaborators.

### Canonical naming

- `README.md` = English
- `README.zh-CN.md` = Simplified Chinese
- `manuscript/*_EN.md` = English manuscript
- `manuscript/*_ZH.md` = Simplified Chinese manuscript

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
- warnings about synthetic/dry-run data;
- submission gates.

Translation may adapt sentence structure for natural academic Chinese/English, but it must not change scientific claims.

### HTML / GitHub Pages

`docs/index.html` must offer an obvious English/中文 switch or bilingual presentation and link to both language versions of each current paper and README.

When GitHub Pages is enabled, the deployed page must not become single-language through later edits.

## 中文

PAIR 的对外研究材料默认采用**英文 + 简体中文双语同步维护**。

以下内容必须保持中英双版：

1. 仓库 README；
2. Paper 1（A+B）和 Paper 2（C）的当前论文 Master；
3. 对外 HTML 仪表盘与 GitHub Pages 的导航和核心内容；
4. 面向公开协作的论文状态/交接页面（在双语能明显提高可用性时）；
5. 同时面向中英文协作者的公开 protocol summary 或 clinician-facing 页面。

### 规范命名

- `README.md` = 英文
- `README.zh-CN.md` = 简体中文
- `manuscript/*_EN.md` = 英文论文
- `manuscript/*_ZH.md` = 中文论文

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
- synthetic/dry-run 警示；
- 投稿 gate。

翻译可以为符合学术中文/英文习惯而调整句法，但不能改变科学主张。

### HTML / GitHub Pages

`docs/index.html` 必须提供明显的 English / 中文切换或等价的双语呈现，并同时链接当前 README 和两篇论文的中英文版本。

GitHub Pages 启用后，后续修改也不得退化成单语页面。