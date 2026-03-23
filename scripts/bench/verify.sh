#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

required_paths=(
  "$ROOT_DIR/configs/benchmark-matrix.yaml"
  "$ROOT_DIR/schemas/benchmark-definition.schema.json"
  "$ROOT_DIR/schemas/benchmark-run.schema.json"
  "$ROOT_DIR/benchmarks/definitions/cpu/cpu-prime-count.yaml"
  "$ROOT_DIR/benchmarks/definitions/memory/mem-large-json-transform.yaml"
  "$ROOT_DIR/benchmarks/datasets/generated/mem-large-json-transform-medium.json"
  "$ROOT_DIR/languages/python/cpu-prime-count/run.sh"
  "$ROOT_DIR/languages/typescript/cpu-prime-count/run.sh"
  "$ROOT_DIR/languages/go/cpu-prime-count/run.sh"
  "$ROOT_DIR/languages/rust/cpu-prime-count/run.sh"
  "$ROOT_DIR/languages/java/cpu-prime-count/run.sh"
  "$ROOT_DIR/languages/csharp/cpu-prime-count/run.sh"
  "$ROOT_DIR/languages/python/mem-large-json-transform/run.sh"
  "$ROOT_DIR/languages/typescript/mem-large-json-transform/run.sh"
  "$ROOT_DIR/languages/go/mem-large-json-transform/run.sh"
  "$ROOT_DIR/languages/rust/mem-large-json-transform/run.sh"
  "$ROOT_DIR/languages/java/mem-large-json-transform/run.sh"
  "$ROOT_DIR/languages/csharp/mem-large-json-transform/run.sh"
  "$ROOT_DIR/benchmarks/definitions/concurrency/con-producer-consumer-pipeline.yaml"
  "$ROOT_DIR/languages/python/con-producer-consumer-pipeline/run.sh"
  "$ROOT_DIR/languages/typescript/con-producer-consumer-pipeline/run.sh"
  "$ROOT_DIR/benchmarks/definitions/io/io-large-file-streaming.yaml"
  "$ROOT_DIR/scripts/data/generate_io_large_file.py"
  "$ROOT_DIR/languages/python/io-large-file-streaming/run.sh"
  "$ROOT_DIR/languages/typescript/io-large-file-streaming/run.sh"
  "$ROOT_DIR/languages/go/io-large-file-streaming/run.sh"
  "$ROOT_DIR/languages/rust/io-large-file-streaming/run.sh"
  "$ROOT_DIR/languages/java/io-large-file-streaming/run.sh"
  "$ROOT_DIR/languages/csharp/io-large-file-streaming/run.sh"
  "$ROOT_DIR/benchmarks/definitions/parallelism/par-parallel-reduction.yaml"
  "$ROOT_DIR/languages/python/par-parallel-reduction/run.sh"
  "$ROOT_DIR/languages/typescript/par-parallel-reduction/run.sh"
  "$ROOT_DIR/languages/go/par-parallel-reduction/run.sh"
  "$ROOT_DIR/languages/rust/par-parallel-reduction/run.sh"
  "$ROOT_DIR/languages/java/par-parallel-reduction/run.sh"
  "$ROOT_DIR/languages/csharp/par-parallel-reduction/run.sh"
)

for p in "${required_paths[@]}"; do
  if [[ ! -f "$p" ]]; then
    echo "missing required file: $p" >&2
    exit 1
  fi
done

for tool in python3 git; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "missing required tool: $tool" >&2
    exit 1
  fi
done

echo "verification ok"
