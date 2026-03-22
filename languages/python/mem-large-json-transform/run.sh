#!/usr/bin/env bash
set -euo pipefail
DATASET="${1:?dataset path required}"
python3 "$(dirname "$0")/transform.py" "$DATASET"
