#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"
DATASET='benchmarks/datasets/generated/mem-large-json-transform-medium.json'
./scripts/bench/verify.sh
for lang in python typescript go rust java csharp; do
  ./languages/$lang/cpu-prime-count/run.sh 1000 >/dev/null
  echo "cpu smoke ok: $lang"
done
for lang in python typescript go rust java csharp; do
  ./languages/$lang/mem-large-json-transform/run.sh "$DATASET" >/dev/null
  echo "mem smoke ok: $lang"
done
for lang in python typescript; do
  ./languages/$lang/con-producer-consumer-pipeline/run.sh 1000 >/dev/null
  echo "concurrency smoke ok: $lang"
done
IO_DATASET='benchmarks/datasets/generated/io-large-file-streaming-medium.txt'
for lang in python typescript go rust java csharp; do
  ./languages/$lang/io-large-file-streaming/run.sh "$IO_DATASET" >/dev/null
  echo "io smoke ok: $lang"
done
