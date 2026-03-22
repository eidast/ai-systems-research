# Project Operating Rules

This document defines the operational rules for this research repository.

## Repository location rule

Canonical local location:
- `~/Projects/ai-systems-research`

Workspace access may use a symlink, but the project source of truth lives under `~/Projects/`.

## Documentation-first rule

Every meaningful contribution must:
1. update the relevant documentation,
2. add technical information required to execute or interpret the work,
3. preserve cross-references where useful.

## Versioning rule

Every meaningful contribution should end with:
1. `git add`
2. `git commit`
3. `git push`

The repository should reflect the current state of the research, not a backlog of uncommitted local changes.

## Technical evidence rule

When adding a benchmark, script, schema, or result artifact, also add the supporting technical documentation required to:
- execute it,
- validate it,
- interpret it,
- reproduce it.

## Evidence over opinion rule

Claims should be backed by:
- benchmark results,
- methodology,
- explicit assumptions,
- or architectural reasoning with stated limits.

## Cross-reference rule

When creating a new technical document, link it to related methodology, architecture, and benchmark documents when helpful.

## Output quality rule

No benchmark result should be treated as decision-grade unless it has:
- correctness validation,
- metadata completeness,
- repeatable execution,
- bounded interpretation.

## Cross-references

- [README](../README.md)
- [Documentation Index](./index.md)
- [Methodology](./methodology.md)
