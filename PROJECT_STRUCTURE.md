# Project Structure

```
study-claude-code/
├── CI.sh                          # CI pipeline runner (linting, type check, tests)
├── LICENSE                        # MIT License
├── README.md                      # Root documentation (if any)
├── .git/                          # Git repository
├── .github/
│   └── workflows/
│       └── lint.yml              # GitHub Actions workflow
├── .githooks/
│   └── pre-push                  # Pre-push hook (runs CI checks)
├── .gitignore                    # Global ignore patterns
├── .claude/                      # Claude IDE configuration
│   └── settings.local.json
├── .vscode/                      # VS Code settings
│   └── mcp.json
├── .mcp.json                     # MCP configuration
└── ch03/                         # Chapter 3: Python Testing & Type Safety
    ├── multiply.py              # Main module (14 LOC)
    ├── conftest.py              # Pytest configuration
    ├── pyproject.toml           # Project metadata & dependencies
    ├── pytest.ini               # Pytest settings (100% coverage required)
    ├── uv.lock                  # Dependency lock file
    ├── README.md                # Module documentation
    ├── run.sh                   # Execute multiply.py with auto venv setup
    ├── test.sh                  # Run tests with coverage verification
    ├── .gitignore               # Module-specific ignore patterns
    └── tests/
        ├── __init__.py
        └── test_multiply.py     # 8 comprehensive test cases (100% coverage)
```

## Quick Start

### Run Application
```bash
./ch03/run.sh 3 4  # Output: 3.0 × 4.0 = 12.0
```

### Run Tests
```bash
./ch03/test.sh  # Tests + 100% coverage verification
```

### Run Full CI Pipeline
```bash
./CI.sh  # Linting + Type checking + Tests
```

## Key Features

- ✅ **100% Test Coverage**: `multiply.py` with 8 test cases
- ✅ **Type Safety**: mypy type checking
- ✅ **Code Quality**: ruff linter
- ✅ **CI Automation**: GitHub Actions workflow + pre-push hooks
- ✅ **Reproducible Environment**: uv-managed dependencies

## Technologies

- **Python 3.11+** - Core language
- **pytest** - Test framework with coverage
- **mypy** - Type checker
- **ruff** - Fast Python linter
- **uv** - Dependency manager

## Development Dependencies

```
pytest>=8.0
pytest-cov>=5.0
mypy>=1.0
ruff>=0.4
```

See `ch03/pyproject.toml` for full configuration.
