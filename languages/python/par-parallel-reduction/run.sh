#!/usr/bin/env bash
set -euo pipefail
python3 "$(dirname "$0")/parallel_reduction.py" "${1:-200000}"
