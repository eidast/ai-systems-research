#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$DIR/out"
javac -d "$DIR/out" "$DIR/ProducerConsumerPipeline.java"
java -cp "$DIR/out" ProducerConsumerPipeline "${1:-100000}"
