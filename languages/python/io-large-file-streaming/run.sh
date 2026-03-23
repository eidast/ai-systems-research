#!/usr/bin/env bash
set -euo pipefail
python3 "$(dirname "$0")/stream.py" "${1:?dataset path required}"
