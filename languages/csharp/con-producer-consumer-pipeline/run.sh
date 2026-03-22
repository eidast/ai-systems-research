#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
dotnet run --project "$DIR/ProducerConsumerPipeline.csproj" -- "${1:-100000}"
