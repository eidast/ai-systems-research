# Methodology

## Objective

Produce benchmark evidence that is reproducible, fair enough to be informative, and useful for architectural decision-making.

## Methodological Principles

### 1. Same problem, equivalent intent
Each implementation must solve the same benchmark objective with comparable semantics.

### 2. Hardware and runtime disclosure
All measurements must record environment details:
- machine
- CPU
- memory
- OS
- runtime versions
- compiler settings

### 3. Multiple runs
Each benchmark must run multiple times in order to capture:
- mean
- median
- standard deviation
- outliers

### 4. Warmup awareness
JIT-based runtimes such as Java and C# may require warmup runs before stable measurement.

### 5. Raw data preservation
Raw outputs must be stored before any derived interpretation or chart generation.

### 6. Interpretation discipline
Do not infer universal truth from narrow benchmark cases.
Treat results as workload-sensitive evidence, not ideology.

## Measurement Categories

### Performance
- execution time
- throughput
- latency (avg, p95, p99 when relevant)

### Resource Consumption
- peak memory
- average memory
- peak CPU
- average CPU

### Delivery/Engineering Cost
- implementation complexity
- build complexity
- runtime footprint
- dependency profile

## Data Outputs

### Raw
- CSV
- JSON
- benchmark logs

### Processed
- normalized tables
- comparative datasets
- chart inputs

### Visual
- bar charts
- line charts
- heatmaps
- radar charts
- scatter plots

## Related Docs

- [Research Design v1](./research-design.md)
- [Benchmark Suite v1](./benchmark-suite.md)
- [Architecture Overview](./architecture-overview.md)
