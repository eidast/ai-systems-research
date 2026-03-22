# Decision Framework v1

This document translates benchmark outputs into architectural guidance.

## Core principle

The repository is not designed to answer "which language wins?".
It is designed to answer:

**Under which workload, runtime, and organizational conditions does a language/runtime become the rational architectural choice?**

## Decision layers

## 1. Workload profile
Describe the problem shape:
- dominant stressor: CPU, memory, I/O, concurrency, mixed
- latency sensitivity
- throughput target
- burstiness
- statefulness
- payload size
- failure tolerance

## 2. Runtime profile
Evaluate:
- steady-state throughput
- tail behavior
- startup cost
- memory efficiency
- multicore scaling
- backpressure behavior
- observability/tooling maturity

## 3. Delivery system profile
Evaluate:
- maintainability
- debugging ergonomics
- implementation effort
- AI leverage
- ecosystem maturity
- deployment complexity
- hiring/onboarding cost

## 4. Outcome language
Recommendations should use:
- recommended fit
- conditional fit
- avoid for this context
- strong technical fit / weak organizational fit
- requires specialist capability

## Decision output template

For every important result family, the interpretation should answer:
1. what happened?
2. why did it likely happen?
3. when does it matter architecturally?
4. when should it not drive a decision?

## Cross-references

- [Architecture Overview](./architecture-overview.md)
- [Benchmark Catalog](./benchmark-catalog.md)
- [Charting Strategy](./charting-strategy.md)
