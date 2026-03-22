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

if [[ "$BENCHMARK_ID" != "cpu-prime-count" ]]; then
  echo "unsupported benchmark for current bootstrap: $BENCHMARK_ID" >&2
  exit 1
fi

RUN_ID="$(date -u +"%Y%m%dT%H%M%SZ")-${BENCHMARK_ID}-${LANGUAGE}-${MODE}"
RUN_DIR="$ROOT_DIR/results/raw/$RUN_ID"
mkdir -p "$RUN_DIR/runs" "$RUN_DIR/logs"
"$ROOT_DIR/scripts/bench/env-capture.sh" "$RUN_DIR/env.json" >/dev/null

IMPLEMENTATION_SCRIPT="$ROOT_DIR/languages/$LANGUAGE/cpu-prime-count/run.sh"
if [[ ! -x "$IMPLEMENTATION_SCRIPT" ]]; then
  echo "missing executable implementation: $IMPLEMENTATION_SCRIPT" >&2
  exit 1
fi

for ((i=1;i<=WARMUPS;i++)); do
  "$IMPLEMENTATION_SCRIPT" "$INPUT_SIZE" > /dev/null
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
  /usr/bin/time -l "$IMPLEMENTATION_SCRIPT" "$INPUT_SIZE" > "$TMP_OUT" 2> "$RUN_DIR/logs/trial-${trial}.time"
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
  PRIME_RESULT="$(tail -n1 "$TMP_OUT" | tr -d '\r')"
  CORRECTNESS=true
  if ! [[ "$PRIME_RESULT" =~ ^[0-9]+$ ]]; then
    CORRECTNESS=false
  fi
  cat > "$RUN_DIR/runs/${BENCHMARK_ID}.${LANGUAGE}.${MODE}.size-${INPUT_SIZE}.trial-${trial}.json" <<EOF
{
  "schema_version": "1.0.0",
  "run_id": "$RUN_ID",
  "benchmark": {
    "id": "$BENCHMARK_ID",
    "category": "cpu",
    "benchmark_tier": "micro",
    "architectural_analog": "pure compute validation engine"
  },
  "implementation": {
    "language": "$LANGUAGE",
    "runtime": "bootstrap-local",
    "mode": "$MODE",
    "implementation_version": "git:$(git -C "$ROOT_DIR" rev-parse --short HEAD 2>/dev/null || echo unknown)"
  },
  "parameters": {
    "input_size": $INPUT_SIZE,
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
