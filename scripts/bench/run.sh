#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
BENCHMARK_ID=""
LANGUAGE=""
MODE="baseline"
INPUT_SIZE=""
TRIALS=5
WARMUPS=3

while [[ $# -gt 0 ]]; do
  case "$1" in
    --benchmark) BENCHMARK_ID="$2"; shift 2 ;;
    --language) LANGUAGE="$2"; shift 2 ;;
    --mode) MODE="$2"; shift 2 ;;
    --input-size) INPUT_SIZE="$2"; shift 2 ;;
    --trials) TRIALS="$2"; shift 2 ;;
    --warmups) WARMUPS="$2"; shift 2 ;;
    *) echo "unknown argument: $1" >&2; exit 1 ;;
  esac
done

if [[ -z "$BENCHMARK_ID" || -z "$LANGUAGE" || -z "$INPUT_SIZE" ]]; then
  echo "usage: run.sh --benchmark <id> --language <lang> --input-size <n> [--mode baseline] [--trials 5] [--warmups 3]" >&2
  exit 1
fi

case "$BENCHMARK_ID" in
  cpu-prime-count)
    BENCH_CATEGORY="cpu"
    BENCH_TIER="micro"
    BENCH_ANALOG="pure compute validation engine"
    IMPLEMENTATION_SCRIPT="$ROOT_DIR/languages/$LANGUAGE/cpu-prime-count/run.sh"
    RUN_ARG="$INPUT_SIZE"
    ;;
  mem-large-json-transform)
    BENCH_CATEGORY="memory"
    BENCH_TIER="component"
    BENCH_ANALOG="ETL transform stage / ingestion service"
    IMPLEMENTATION_SCRIPT="$ROOT_DIR/languages/$LANGUAGE/mem-large-json-transform/run.sh"
    RUN_ARG="$INPUT_SIZE"
    ;;
  con-producer-consumer-pipeline)
    BENCH_CATEGORY="concurrency"
    BENCH_TIER="component"
    BENCH_ANALOG="bounded internal pipeline / worker queue"
    IMPLEMENTATION_SCRIPT="$ROOT_DIR/languages/$LANGUAGE/con-producer-consumer-pipeline/run.sh"
    RUN_ARG="$INPUT_SIZE"
    ;;
  io-large-file-streaming)
    BENCH_CATEGORY="io"
    BENCH_TIER="component"
    BENCH_ANALOG="file ingestion / streaming transform stage"
    IMPLEMENTATION_SCRIPT="$ROOT_DIR/languages/$LANGUAGE/io-large-file-streaming/run.sh"
    RUN_ARG="$INPUT_SIZE"
    ;;
  par-parallel-reduction)
    BENCH_CATEGORY="parallelism"
    BENCH_TIER="component"
    BENCH_ANALOG="analytics reduction stage / batch parallel worker reduction"
    IMPLEMENTATION_SCRIPT="$ROOT_DIR/languages/$LANGUAGE/par-parallel-reduction/run.sh"
    RUN_ARG="$INPUT_SIZE"
    ;;
  *)
    echo "unsupported benchmark for current bootstrap: $BENCHMARK_ID" >&2
    exit 1
    ;;
esac

RUN_ID="$(date -u +"%Y%m%dT%H%M%SZ")-${BENCHMARK_ID}-${LANGUAGE}-${MODE}"
RUN_DIR="$ROOT_DIR/results/raw/$RUN_ID"
SAFE_INPUT_TAG="$(printf '%s' "$INPUT_SIZE" | sed 's|.*/||; s|[^A-Za-z0-9._-]|_|g')"
mkdir -p "$RUN_DIR/runs" "$RUN_DIR/logs"
"$ROOT_DIR/scripts/bench/env-capture.sh" "$RUN_DIR/env.json" >/dev/null

if [[ ! -x "$IMPLEMENTATION_SCRIPT" ]]; then
  echo "missing executable implementation: $IMPLEMENTATION_SCRIPT" >&2
  exit 1
fi

for ((i=1;i<=WARMUPS;i++)); do
  "$IMPLEMENTATION_SCRIPT" "$RUN_ARG" > /dev/null
  echo "warmup $i complete"
done

for ((trial=1;trial<=TRIALS;trial++)); do
  STARTED_AT="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  START_EPOCH="$(python3 - <<'PY'
import time
print(time.time())
PY
)"
  TMP_OUT="$RUN_DIR/logs/trial-${trial}.out"
  /usr/bin/time -l "$IMPLEMENTATION_SCRIPT" "$RUN_ARG" > "$TMP_OUT" 2> "$RUN_DIR/logs/trial-${trial}.time"
  EXIT_CODE=$?
  FINISHED_AT="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  END_EPOCH="$(python3 - <<'PY'
import time
print(time.time())
PY
)"
  WALL_TIME_MS="$(python3 - <<PY
start=float("$START_EPOCH")
end=float("$END_EPOCH")
print(round((end-start)*1000, 3))
PY
)"
  MEM_PEAK_MB="$(python3 - <<PY
import re, pathlib
text = pathlib.Path("$RUN_DIR/logs/trial-${trial}.time").read_text()
match = re.search(r"(\d+)\s+maximum resident set size", text)
if match:
    print(round(int(match.group(1))/1024/1024, 3))
else:
    print(0)
PY
)"
  CPU_PERCENT="$(python3 - <<PY
import re, pathlib
text = pathlib.Path("$RUN_DIR/logs/trial-${trial}.time").read_text()
first = text.splitlines()[0] if text.splitlines() else ''
match = re.search(r"\s*([0-9.]+)\s+real\s+([0-9.]+)\s+user\s+([0-9.]+)\s+sys", first)
if match:
    real = float(match.group(1))
    user = float(match.group(2))
    sysv = float(match.group(3))
    print(round(((user + sysv) / real) * 100, 3) if real > 0 else 0)
else:
    print(0)
PY
)"
  RESULT_LINE="$(tail -n1 "$TMP_OUT" | tr -d '\r')"
  CORRECTNESS=true
  case "$BENCHMARK_ID" in
    cpu-prime-count)
      if ! [[ "$RESULT_LINE" =~ ^[0-9]+$ ]]; then
        CORRECTNESS=false
      fi
      ;;
    mem-large-json-transform)
      if ! python3 - <<PY
import json
json.loads('''$RESULT_LINE''')
PY
      then
        CORRECTNESS=false
      fi
      ;;
    con-producer-consumer-pipeline)
      if ! python3 - <<PY
import json
payload = json.loads('''$RESULT_LINE''')
assert 'item_count' in payload and 'value_sum' in payload
PY
      then
        CORRECTNESS=false
      fi
      ;;
    io-large-file-streaming)
      if ! python3 - <<PY
import json
payload = json.loads('''$RESULT_LINE''')
assert 'total_records' in payload and 'categories' in payload
PY
      then
        CORRECTNESS=false
      fi
      ;;
    par-parallel-reduction)
      if ! python3 - <<PY
import json
payload = json.loads('''$RESULT_LINE''')
assert 'item_count' in payload and 'value_sum' in payload
PY
      then
        CORRECTNESS=false
      fi
      ;;
  esac
  INPUT_JSON="$(python3 - <<PY
import json
print(json.dumps("""$INPUT_SIZE"""))
PY
)"
  cat > "$RUN_DIR/runs/${BENCHMARK_ID}.${LANGUAGE}.${MODE}.size-${SAFE_INPUT_TAG}.trial-${trial}.json" <<EOF
{
  "schema_version": "1.0.0",
  "run_id": "$RUN_ID",
  "benchmark": {
    "id": "$BENCHMARK_ID",
    "category": "$BENCH_CATEGORY",
    "benchmark_tier": "$BENCH_TIER",
    "architectural_analog": "$BENCH_ANALOG"
  },
  "implementation": {
    "language": "$LANGUAGE",
    "runtime": "bootstrap-local",
    "mode": "$MODE",
    "implementation_version": "git:$(git -C "$ROOT_DIR" rev-parse --short HEAD 2>/dev/null || echo unknown)"
  },
  "parameters": {
    "input_size": $INPUT_JSON,
    "trial": $trial,
    "warmup_completed": true
  },
  "metrics": {
    "wall_time_ms": $WALL_TIME_MS,
    "cpu_percent_avg": $CPU_PERCENT,
    "cpu_percent_peak": $CPU_PERCENT,
    "mem_peak_mb": $MEM_PEAK_MB,
    "exit_code": $EXIT_CODE
  },
  "quality": {
    "correctness_passed": $CORRECTNESS,
    "warnings": []
  },
  "timestamps": {
    "started_at": "$STARTED_AT",
    "finished_at": "$FINISHED_AT"
  }
}
EOF
  echo "trial $trial complete -> $RUN_DIR"
done

echo "$RUN_DIR"
