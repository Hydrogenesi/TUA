# Contributing to MATRIUN

Thank you for your interest in contributing!

## How to Contribute

1. **Open an issue** — Describe the bug or feature before starting work.
2. **Fork and branch** — Create a branch from `main` with a descriptive name.
3. **Write code** — Follow the conventions described in [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md).
4. **Add tests** — Every new function or bug fix should have a corresponding test in `test_matriun.py`.
5. **Run tests** — `pytest test_matriun.py` must pass with no failures.
6. **Open a pull request** — Describe what changed and reference the related issue.

## Code Style

Follow the conventions in [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md#coding-conventions). In summary: Python 3.9+, descriptive names, no external runtime dependencies, and functions must never mutate their inputs.

## Reporting Bugs

Please include:
- Python version
- Steps to reproduce
- Expected vs. actual output

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
