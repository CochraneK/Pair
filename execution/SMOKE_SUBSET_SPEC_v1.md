# Real technical smoke subset specification v1

**Date frozen:** 2026-10-03

This specification defines the real smoke collection to run before the full 1,860-output execution.

## Plan A — 100 APP outputs
Select 20 unique Aim-1 prompts:
- P1–P5: 4 prompts/domain
- within each domain: 2 psychotic + 2 matched controls

Run the same 20 prompts on all 5 APP products:
- DeepSeek
- 豆包
- Kimi
- 通义千问
- 腾讯元宝

Total: `20 × 5 = 100`.

Purpose: verify fresh-chat procedure, visible settings capture, raw response capture, screenshots, quota/fallback handling and manifest integrity. These outputs are not used to modify prompts based on model quality.

## Plan B — 36 APP outputs
Use the first 2 frozen scenario families (`B01`, `B02`):
- 3 axes
- 2 levels/axis
- 12 prompts total

Run replicate 1 on:
- DeepSeek
- 豆包
- 通义千问

Total: `12 × 3 = 36`.

Purpose: verify minimal-pair execution, run IDs, capture fields and later boundary scoring.

## Plan C — 48 API outputs
Use the first 2 frozen C families (`C01`, `C02`):
- conviction
- insight
- behavioral risk
- evidence/plausibility
- 2 levels/axis
- 16 prompts total

Run replicate 1 on all 3 fixed API configurations.

Total: `16 × 3 = 48`.

Important correction:
- all four axes are clinically relevant in this pilot;
- `evidence/plausibility` may imply a negative policy shift (less inappropriate psychiatric escalation when evidence becomes more externally plausible);
- no Nuisance Invariance estimate is produced from the 64-item C pilot unless a dedicated nuisance module is separately frozen.

## Total real smoke volume
`100 + 36 + 48 = 184 outputs`.

## Pass criteria
Before full collection:
- no unresolved account/session contamination;
- no systematic prompt truncation/corruption;
- raw responses persist with correct case/run IDs;
- APP screenshots and metadata can be captured consistently;
- quota/fallback events are detectable and flagged;
- API authentication and request schema work for all fixed configs;
- blind-pack generation succeeds without brand/model leakage;
- no validity-breaking schema bug remains.

## Stop rule
A smoke failure may justify an engineering/configuration fix. It must **not** justify changing a prompt or primary metric merely because a product/model performed poorly.
