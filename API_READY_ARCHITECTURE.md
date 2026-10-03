# API-ready Benchmark Architecture

## 原则
现在做 APP，也从第一天使用 provider-agnostic schema。

## 目录建议
```text
benchmark/
├── cases/
├── rubric/
├── runners/app_capture/
├── runners/api/
├── raw/app/
├── raw/api/
├── blinded/
├── ratings/
├── analysis/
├── configs/
└── reports/
```

## 公共字段
run_id / case_id / condition / language / response / timestamp / source_type / source_id / config_id

## APP metadata
product / surface / subscription / displayed model / UI mode / memory/history / search/tool / screenshot

## API metadata
provider / exact model_id / endpoint / system-prompt hash / temperature / top_p / max tokens / reasoning / seed / tools/web / retries / token use / latency

## 分析原则
1. APP within-product
2. API within-model/config
3. 再做 exploratory interface-gap

不要直接混成一个排行榜。

## RAG / system prompt intervention
不混 baseline。
未来可作为明确 experimental arms。

## Release
若只为第一篇论文：可全量公开。
若要长期 leaderboard：考虑 public dev + protected test + versioned refresh。

# Evolvent / BenchRouter
BenchRouter 适合 API/local：
- benchmark.yaml
- task.yaml
- 一个读取 endpoint/model/env 并写 result.json 的脚本

它不直接解决 APP UI，也不提供 clinical ground truth。
**Evolvent = engineering shell；精神科团队 = scientific validity。**
