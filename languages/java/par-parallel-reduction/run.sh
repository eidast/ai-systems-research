#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$DIR/out"
javac -d "$DIR/out" "$DIR/ParallelReduction.java"
java -cp "$DIR/out" ParallelReduction "${1:-200000}"
