# PAIR execution plan v0.1

**Prepared:** 2026-10-03  
**Status:** candidate execution freeze under Assumption Mode.

## Plan A — consumer APP main audit
Products:
1. DeepSeek
2. 豆包
3. Kimi
4. 通义千问
5. 腾讯元宝

Main bank:
- 160 prompts per product
- 5 products
- 800 primary outputs

Stability subset:
- 16 psychosis prompts = 20% of the 80 psychosis prompts
- stratified allocation: P1=4, P2=3, P3=3, P4=3, P5=3
- each selected item receives two additional fresh-chat runs per product
- 32 additional outputs per product
- 160 additional outputs total

**Plan A total: 960 outputs.**

Randomization:
- repeat-subset seed: `202610031`
- product primary order base seed: `202610100 + product_index`
- repeat passes use distinct deterministic seeds.

## Plan B — nested product pilot
Representative consumer products:
1. DeepSeek
2. 豆包
3. 通义千问

Design:
- 36 prompts
- 3 independent runs per prompt/product
- 3 products

**Plan B total: 324 outputs.**

Order seed base: `202610200` with product/replicate-specific offsets.

## Plan C — fixed API pilot
Configurations:
1. `C-DS-V41F-20260910`
2. `C-QWEN38MAX-0902`
3. `C-DOUBAO21PRO-260915`

Design:
- 64 prompts
- 3 independent runs per prompt/configuration
- 3 model configurations

**Plan C total: 576 outputs.**

Order seed base: `202610300` with configuration/replicate-specific offsets.

## Overall volume
If all routes are executed as currently frozen:

`960 + 324 + 576 = 1,860 outputs`

## Data separation
Never pool these as one undifferentiated benchmark:
- A = consumer product audit
- B = consumer product clinical-boundary pilot
- C = fixed API/model configuration benchmark pilot

## Real vs dry-run
Only responses actually collected from the frozen products/configurations count as empirical outputs. Synthetic fixtures and engineering defaults must remain labelled dry-run.

## Schedule generation
Canonical deterministic generator: `scripts/build_collection_schedules.py`.

The generated CSV schedules may be regenerated from frozen case files and seeds; schedule files themselves need not be manually edited.
