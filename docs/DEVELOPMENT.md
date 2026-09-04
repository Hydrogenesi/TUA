# Development

## Setup

```bash
git clone https://github.com/Hydrogenesi/TUA.git
cd TUA
pip install -e ".[dev]"
```

`pytest` is the only dev dependency (declared in `pyproject.toml` under
`[project.optional-dependencies] dev` and mirrored in `requirements.txt`).

## Run tests

```bash
python -m pytest            # from the repo root
python -m pytest -v -k cli  # just the CLI tests
```

Use `python -m pytest` rather than bare `pytest` so the interpreter that owns
the editable install is the one running the suite.

## Conventions

- Descriptive names throughout (`num_rows`, `row_index`, `scalar_factor`) —
  no single-letter loop variables.
- Full type hints on public functions; `Matrix` / `Number` aliases from `matriun`.
- Docstrings state the shape rule, the error conditions, and one example.
- **Tests define truth.** A behaviour change lands with a test in
  `test_matriun.py` first; docs are updated to match the test.
- New shape or validation errors use `ValueError` with the concrete dimensions
  in the message.

## Adding a function

1. Implement in `matriun.py` with a docstring (shape rule, raises, example).
2. Add tests to `test_matriun.py` covering the happy path and each error.
3. Add a row to the README "API at a glance" table and a section to
   `docs/API_REFERENCE.md`.
4. Export it in `matriun_cli.py` only if the demo uses it.

## Release

1. Bump `version` in `pyproject.toml`.
2. Add an entry to `CHANGELOG.md`.
3. `python -m build` (requires `pip install build`) → `dist/`.
