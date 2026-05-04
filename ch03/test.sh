#!/usr/bin/env bash
set -euo pipefail

# ch03/test.sh - Run tests with coverage

if [ ! -d ".venv" ]; then
  echo "Setting up virtual environment..."
  python -m venv .venv
  source .venv/bin/activate
  pip install -e ".[dev]"
else
  source .venv/bin/activate
fi

echo "Running tests with coverage..."
python -m pytest -v --cov=multiply --cov-report=term-missing --cov-fail-under=100

echo "✓ All tests passed with 100% coverage!"
