# Development Guide

## Prerequisites

- Python 3.9 or later
- `pip`

## Setup

Clone the repository and install in editable mode with development dependencies:

```bash
git clone https://github.com/Hydrogenesi/TUA.git
cd TUA
pip install -e .
pip install -r requirements.txt
```

## Running Tests

Tests are written with [pytest](https://pytest.org).

```bash
pytest test_matriun.py
```

To see verbose output:

```bash
pytest -v test_matriun.py
```

## Project Layout

```
matriun.py        — Core library (pure Python, no external deps)
matriun_cli.py    — CLI entry point (argparse)
test_matriun.py   — Unit tests
pyproject.toml    — Package metadata
requirements.txt  — Dev dependencies (pytest)
```

## Making Changes

1. Fork the repository and create a feature branch.
2. Keep all public functions in `matriun.py` and their signatures stable unless there is a documented reason to change them.
3. Add or update tests in `test_matriun.py` for any changed behaviour.
4. Run `pytest` to confirm all tests pass before opening a pull request.
5. Follow existing naming conventions: full English words, no abbreviations.

## Coding Conventions

- All functions return new matrices — never mutate the input.
- Use descriptive variable names (`row_index`, not `i`).
- Keep functions short and single-purpose.

## Submitting a Pull Request

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full checklist.
