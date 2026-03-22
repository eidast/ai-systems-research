# Language Layout and Required Files

This document defines the minimum file layout expected for each language implementation in the repository.

## Objective

Keep implementations consistent, reviewable, and reproducible across languages.

## Minimum per-language benchmark layout

For each benchmark implementation, prefer this structure:

```text
languages/<language>/<benchmark-id>/
  run.sh
  README.md
  src-or-main-files...
  optional project manifest/build file
  optional fixtures/
  optional meta.json
```

## Required files

### 1. `run.sh`
Required.
Provides a stable execution entrypoint for the benchmark runner.

### 2. Source files
Required.
Examples:
- Python: `prime_count.py`
- Go: `prime_count.go`
- Rust: `Cargo.toml` + `src/main.rs`
- Java: `PrimeCount.java`
- C#: `PrimeCount.csproj` + `Program.cs`
- TypeScript/Node: `prime_count.mjs` or package-based source

### 3. Local `README.md`
Strongly recommended.
Should explain:
- how the implementation is built/run,
- which runtime/toolchain it depends on,
- any implementation-specific caveats,
- whether build artifacts are intentionally excluded from version control.

### 4. `meta.json`
Recommended.
Useful for AI trace metadata, optimization stage notes, implementation authoring notes, and language-specific caveats.

## Recommended additional repository files by language

### Python
- `requirements.txt` or `pyproject.toml` when dependencies appear

### TypeScript/Node
- `package.json` once we need dependencies or scripts
- `package-lock.json` if package-managed

### Go
- `go.mod` if the implementation grows beyond a single-file standard-library example

### Rust
- `Cargo.toml`
- `Cargo.lock` for reproducibility

### Java
- Keep it simple for now with raw `javac`, but move to a small build file if complexity grows

### C#
- `.csproj` required
- avoid committing `bin/` and `obj/`

## Rule on build artifacts

Generated artifacts must not be committed unless they are part of the measured evidence under `results/`.

## Cross-references

- [Project Operating Rules](./project-operating-rules.md)
- [Execution Protocol](./execution-protocol.md)
- [Toolchain Versions](./toolchain-versions.md)
