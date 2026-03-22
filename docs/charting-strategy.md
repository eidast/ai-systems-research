# Charting Strategy v1

This document defines the visual outputs generated from measured data.

## Principles

- charts must be generated from curated data only
- charts must be reproducible from scripts
- every chart must answer an architectural question
- avoid visuals that imply universal rankings without context

## Required chart families

## 1. Bar charts
Use for:
- total execution time by language
- peak memory by language
- startup time by runtime

## 2. Line charts
Use for:
- scaling by worker/core count
- throughput under increasing load
- latency under increasing concurrency

## 3. Scatter plots
Use for:
- performance vs memory
- performance vs engineering effort
- throughput vs p99 latency

## 4. Heatmaps
Use for:
- language vs benchmark vs metric
- workload class vs runtime fit

## 5. Radar charts
Use for normalized comparative views of:
- performance
- memory
- operability
- maintainability
- implementation effort

## 6. Decision matrix visuals
Use for:
- best fit by workload class
- conditional fit by organizational constraints
- architecture guidance summaries

## Output rules

- generate both `PNG` and `SVG`
- include chart title, metric units, benchmark ID, environment profile
- never chart mixed cold/warm data as a single series
- annotate if a chart is exploratory or decision-grade

## Source directories

- raw data: `results/raw/`
- curated data: `results/curated/latest/`
- generated charts: `results/charts/latest/`
- report outputs: `results/reports/latest/`

## Cross-references

- [Metrics Schema](./metrics-schema.md)
- [Decision Framework](./decision-framework.md)
- [Tooling Plan](./tooling-plan-forge.md)
