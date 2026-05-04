#!/usr/bin/env bash
set -euo pipefail

# ch03/test.sh - Run tests with coverage using uv

cd "$(dirname "$0")"

# Ensure all dependencies including dev tools are synced
uv sync --quiet

echo "Running tests with coverage..."
uv run pytest -v --cov=multiply --cov-report=term-missing --cov-fail-under=100

echo "✓ All tests passed with 100% coverage!"

