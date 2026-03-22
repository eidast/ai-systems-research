# Testing and Validation

This document defines the minimum automated validation expected for the repository.

## Objectives

- catch functional regressions after code changes
- verify cross-language correctness invariants
- validate benchmark scripts still execute correctly
- keep benchmark results trustworthy after refactors

## Test layers

### 1. Unit tests
Validate language-local logic for known values and shape invariants.

Current scope:
- Python `cpu-prime-count`
- Python `mem-large-json-transform`

### 2. Cross-language consistency tests
Validate that equivalent implementations produce equivalent outputs.

Current scope:
- `cpu-prime-count` across Python, TypeScript, Go, Rust, Java, C#
- `mem-large-json-transform` across Python, TypeScript, Go, Rust, Java, C#
- `con-producer-consumer-pipeline` across Python and TypeScript

### 3. Runner validation
`verify.sh` ensures required files and base tools exist before benchmark execution.

### 4. Post-change rule
After meaningful changes to benchmark code, runner code, schemas, or datasets:
1. run automated tests
2. run smoke validation for affected benchmark entrypoints
3. rerun affected measured benchmarks if needed
4. only then commit and push

## Current test commands

```bash
./scripts/test/run_all.sh
./scripts/test/smoke_benchmarks.sh
```

Both commands rely only on the standard Python and shell environment already used by the project.

## QA specialist guidance incorporated

This repository also keeps a specialist QA note from Cesar in:
- [Testing Strategy (Cesar)](./testing-strategy-cesar.md)

The current lightweight test suite and smoke gates are aligned with that guidance, especially around correctness, cross-language equivalence, and post-change validation.

## Cross-references

- [Methodology](./methodology.md)
- [Execution Protocol](./execution-protocol.md)
- [Project Operating Rules](./project-operating-rules.md)
