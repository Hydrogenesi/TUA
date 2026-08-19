# MATRIUN Architecture

## Overview

MATRIUN is a single-module Python library with a companion CLI module. It has no external runtime dependencies.

```
TUA/
├── matriun.py        # Core matrix operations library
├── matriun_cli.py    # Command-line interface (argparse)
├── test_matriun.py   # Unit tests (pytest)
├── pyproject.toml    # Package metadata and build config
├── requirements.txt  # Development dependencies
├── README.md
├── CONTRIBUTING.md
└── docs/
    ├── ARCHITECTURE.md   (this file)
    ├── API_REFERENCE.md
    ├── CHANGELOG.md
    └── DEVELOPMENT.md
```

## Module Descriptions

### `matriun.py`

The core library. All public functions accept and return standard Python lists-of-lists (`list[list[int | float | None]]`) so no external numeric library is required.

Key design decisions:
- **Pure Python** — no NumPy or other dependencies; easy to embed anywhere.
- **Descriptive naming** — every variable and parameter uses full words to keep code self-documenting.
- **Immutability** — functions return new matrices and never mutate their inputs.

### `matriun_cli.py`

A thin `argparse` wrapper that exposes the `matriun demo` subcommand. The `main()` function accepts an optional `argv` list for testability.

### `test_matriun.py`

Unit tests written with `pytest`. Each public function has dedicated test cases covering normal usage and edge/error paths.

## Data Model

Matrices are represented as `list[list[number]]` — a list of rows, where each row is a list of numeric values. This matches the standard Python convention for 2-D arrays.

```python
matrix = [
    [1, 2, 3],  # row 0
    [4, 5, 6],  # row 1
]
```

An empty matrix is represented as `[]` (zero rows). The `get_matrix_dimensions` function handles this edge case by returning `(0, 0)`.
