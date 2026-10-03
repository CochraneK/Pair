# Evolvent / BenchRouter 接入说明

Evolvent BenchRouter 更适合未来 **API/local model** benchmark，不适合直接替代消费 APP 的 UI 采集。

最小接入：
- `benchmark.yaml`
- `task.yaml`
- 一个读取 model endpoint/env 并输出 `result.json` 的脚本

能解决：
- benchmark registration
- endpoint routing
- containerized reproducibility
- batch execution
- compare results

不能解决：
- clinical case validity
- clinical rubric
- clinician ground truth
- APP hidden system/routing
- publication novelty

**Evolvent = engineering shell；精神科团队 = scientific validity。**
