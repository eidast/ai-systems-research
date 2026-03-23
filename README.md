# AI Systems Research: Multi-Language Performance, Architecture, and Optimization

> A research-driven benchmark suite and technical article exploring how modern AI changes software engineering decisions across languages, runtimes, and architectural tradeoffs.

## Objective

This repository exists to support a high-rigor technical investigation on a central question:

**How does modern AI change the way senior engineers and architects design, implement, optimize, and compare solutions across multiple programming languages?**

The focus is not just code generation speed. The real interest is whether AI makes it economically viable to:

- prototype the same solution in multiple languages,
- compare CPU and memory tradeoffs with more rigor,
- reason about concurrency, parallelism, and I/O models,
- evaluate architectural decisions with empirical evidence,
- and choose the right stack for the right problem domain.

## Research Scope

Initial language matrix:

- Python
- Go
- Rust
- TypeScript / Node.js
- Java
- C#
- Assembly (selected benchmarks only)

Initial benchmark domains:

- CPU-bound workloads
- Memory-bound workloads
- Parallelism
- Concurrency
- I/O-bound workloads

## Expected Outputs

- Reproducible benchmark implementations
- Structured raw and processed results
- Visualizations and comparative charts
- Methodology documentation
- Architectural interpretation of results
- A publishable long-form technical article

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── index.md
│   ├── research-design.md
│   ├── benchmark-suite.md
│   ├── methodology.md
│   ├── architecture-overview.md
│   ├── diagrams/
│   │   ├── research-workflow.md
│   │   └── benchmark-pipeline.md
│   └── mindmaps/
│       └── research-map.md
├── benchmarks/
│   ├── cpu-bound/
│   ├── memory-bound/
│   ├── parallelism/
│   ├── concurrency/
│   └── io-bound/
├── languages/
│   ├── python/
│   ├── go/
│   ├── rust/
│   ├── typescript/
│   ├── java/
│   ├── csharp/
│   └── assembly/
├── results/
│   ├── raw/
│   ├── processed/
│   └── charts/
├── scripts/
└── article/
```

## Documentation Guide

Start here:

- [Documentation Index](docs/index.md)
- [Research Design v1](docs/research-design.md)
- [Benchmark Suite v1](docs/benchmark-suite.md)
- [Methodology](docs/methodology.md)
- [Active Observability](docs/active-observability.md)
- [Architecture Overview](docs/architecture-overview.md)
- [Benchmark Catalog v1](docs/benchmark-catalog.md)
- [Metrics Schema v1](docs/metrics-schema.md)
- [Execution Protocol v1](docs/execution-protocol.md)
- [Decision Framework v1](docs/decision-framework.md)
- [Project Operating Rules](docs/project-operating-rules.md)
- [Language Runtime Availability](docs/language-runtime-availability.md)
- [Intermediate Findings v1](docs/intermediate-findings-v1.md)

Visual references:

- [Research Workflow Diagram](docs/diagrams/research-workflow.md)
- [Benchmark Pipeline Diagram](docs/diagrams/benchmark-pipeline.md)
- [Research Governance Diagram](docs/diagrams/research-governance.md)
- [Research Mind Map](docs/mindmaps/research-map.md)

## Principles

1. **Fair comparisons over flashy claims**
2. **Same problem, same algorithm, same measurement intent**
3. **Empirical results before architectural conclusions**
4. **Reproducibility over anecdotal benchmarking**
5. **Architectural usefulness over language tribalism**

## Manual execution guide

Run from the repository root:

### 1. Verify toolchains and repository prerequisites

```bash
./scripts/setup/verify-toolchains.sh
./scripts/bench/verify.sh
```

### 2. Run automated validation

```bash
./scripts/test/run_all.sh
./scripts/test/smoke_benchmarks.sh
```

### 3. Execute benchmarks manually

#### CPU — prime count

Single-language direct entrypoint examples:

```bash
./languages/python/cpu-prime-count/run.sh 300000
./languages/typescript/cpu-prime-count/run.sh 300000
./languages/go/cpu-prime-count/run.sh 300000
./languages/rust/cpu-prime-count/run.sh 300000
./languages/java/cpu-prime-count/run.sh 300000
./languages/csharp/cpu-prime-count/run.sh 300000
```

Measured run through the common benchmark runner:

```bash
./scripts/bench/run.sh --benchmark cpu-prime-count --language python --input-size 300000 --trials 3 --warmups 1
```

#### Memory — large JSON transform

First ensure dataset exists:

```bash
python3 scripts/data/generate_mem_large_json.py
```

Direct entrypoint examples:

```bash
./languages/python/mem-large-json-transform/run.sh benchmarks/datasets/generated/mem-large-json-transform-medium.json
./languages/typescript/mem-large-json-transform/run.sh benchmarks/datasets/generated/mem-large-json-transform-medium.json
./languages/go/mem-large-json-transform/run.sh benchmarks/datasets/generated/mem-large-json-transform-medium.json
./languages/rust/mem-large-json-transform/run.sh benchmarks/datasets/generated/mem-large-json-transform-medium.json
./languages/java/mem-large-json-transform/run.sh benchmarks/datasets/generated/mem-large-json-transform-medium.json
./languages/csharp/mem-large-json-transform/run.sh benchmarks/datasets/generated/mem-large-json-transform-medium.json
```

Measured run through the common benchmark runner:

```bash
./scripts/bench/run.sh --benchmark mem-large-json-transform --language python --input-size benchmarks/datasets/generated/mem-large-json-transform-medium.json --trials 3 --warmups 1
```

#### Concurrency — producer consumer pipeline

Direct entrypoint examples:

```bash
./languages/python/con-producer-consumer-pipeline/run.sh 100000
./languages/typescript/con-producer-consumer-pipeline/run.sh 100000
./languages/go/con-producer-consumer-pipeline/run.sh 100000
./languages/rust/con-producer-consumer-pipeline/run.sh 100000
./languages/java/con-producer-consumer-pipeline/run.sh 100000
./languages/csharp/con-producer-consumer-pipeline/run.sh 100000
```

Measured run through the common benchmark runner:

```bash
./scripts/bench/run.sh --benchmark con-producer-consumer-pipeline --language python --input-size 100000 --trials 3 --warmups 1
```

#### I/O — large file streaming

First ensure dataset exists:

```bash
python3 scripts/data/generate_io_large_file.py
```

Direct entrypoint examples:

```bash
./languages/python/io-large-file-streaming/run.sh benchmarks/datasets/generated/io-large-file-streaming-medium.txt
./languages/typescript/io-large-file-streaming/run.sh benchmarks/datasets/generated/io-large-file-streaming-medium.txt
./languages/go/io-large-file-streaming/run.sh benchmarks/datasets/generated/io-large-file-streaming-medium.txt
./languages/rust/io-large-file-streaming/run.sh benchmarks/datasets/generated/io-large-file-streaming-medium.txt
./languages/java/io-large-file-streaming/run.sh benchmarks/datasets/generated/io-large-file-streaming-medium.txt
./languages/csharp/io-large-file-streaming/run.sh benchmarks/datasets/generated/io-large-file-streaming-medium.txt
```

Measured run through the common benchmark runner:

```bash
./scripts/bench/run.sh --benchmark io-large-file-streaming --language python --input-size benchmarks/datasets/generated/io-large-file-streaming-medium.txt --trials 3 --warmups 1
```

#### Parallelism — parallel reduction

Direct entrypoint examples:

```bash
./languages/python/par-parallel-reduction/run.sh 200000
./languages/typescript/par-parallel-reduction/run.sh 200000
./languages/go/par-parallel-reduction/run.sh 200000
./languages/rust/par-parallel-reduction/run.sh 200000
./languages/java/par-parallel-reduction/run.sh 200000
./languages/csharp/par-parallel-reduction/run.sh 200000
```

Measured run through the common benchmark runner:

```bash
./scripts/bench/run.sh --benchmark par-parallel-reduction --language python --input-size 200000 --trials 3 --warmups 1
```

### 4. Regenerate summaries, charts, and reports

```bash
python3 scripts/report/aggregate.py results/raw results/curated/latest
python3 scripts/report/build_charts.py results/curated/latest/result-summary.json results/charts/latest
python3 scripts/report/build_mem_charts.py results/curated/latest/result-summary.json results/charts/latest
python3 scripts/report/build_concurrency_charts.py results/curated/latest/result-summary.json results/charts/latest
python3 scripts/report/render_report.py results/curated/latest/result-summary.json results/charts/latest results/reports/latest/cpu-prime-count-report.md
python3 scripts/report/render_mem_report.py results/curated/latest/result-summary.json results/charts/latest results/reports/latest/mem-large-json-transform-report.md
python3 scripts/report/render_concurrency_report.py results/curated/latest/result-summary.json results/charts/latest results/reports/latest/con-producer-consumer-pipeline-report.md
```

## Status

Current phase: **Execution Pack v1 + CPU/Memory/Concurrency bootstrap**

## Current recommended workstream

1. complete concurrency coverage across the main language set
2. add the next benchmark family after concurrency stabilizes
3. keep tests, smoke validation, raw evidence, and reports in sync
4. commit and push every meaningful contribution

---

If this repository is later published, the public README should remain concise and point to the deeper documents under `docs/`.
