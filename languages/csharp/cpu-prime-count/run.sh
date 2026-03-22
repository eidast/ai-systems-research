#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
dotnet run --project "$DIR/PrimeCount.csproj" -- "${1:-100000}"
