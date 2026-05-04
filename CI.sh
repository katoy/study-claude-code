#!/usr/bin/env bash
set -euo pipefail

# CI.sh - Run complete CI pipeline

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR/ch03"

echo "=== GitHub Copilot Study - CI Pipeline ==="
echo

# Setup
if [ ! -d ".venv" ]; then
  echo "📦 Setting up virtual environment..."
  python -m venv .venv
  source .venv/bin/activate
  pip install -e ".[dev]" -q
else
  source .venv/bin/activate
fi

# Linting
echo "🔍 Running linter (ruff)..."
python -m ruff check .

# Type checking
echo "🔍 Running type checker (mypy)..."
python -m mypy .

# Tests
echo "🧪 Running tests with coverage..."
python -m pytest --cov=multiply --cov-report=term-missing --cov-fail-under=100

echo
echo "✅ All checks passed!"
