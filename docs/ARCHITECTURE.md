# Architecture

MATRIUN is deliberately small: three flat modules at the repository root,
packaged with setuptools via `pyproject.toml`.

```
TUA/
├── matriun.py          # library: 8 pure functions on list[list[Number]]
├── matriun_cli.py      # argparse CLI; `matriun` console script → main()
├── test_matriun.py     # pytest suite — the behavioural source of truth
├── pyproject.toml      # build metadata, console script, [dev] extras
└── docs/               # this folder; see README "Documentation" table
```

## Design constraints

- **Pure Python, no runtime dependencies.** Matrices are plain nested lists so the
  library works anywhere Python 3.9+ runs.
- **No mutation.** Every function allocates and returns a new matrix.
- **Fail loudly on shape errors.** `add_matrices` and `multiply_matrices` raise
  `ValueError` with the offending dimensions; constructors reject negative sizes.
- **Column count from row 0.** `get_matrix_dimensions` trusts the first row;
  ragged input is not validated (see API_REFERENCE.md).
- **CLI is a thin shell.** `matriun_cli` only formats and prints; all math lives
  in `matriun`.

## Data flow

```
user code / CLI ──▶ matriun.<function>(matrix, ...) ──▶ new Matrix
```

## Planned, not implemented

`docs/plate71_renderer_spec.md`, `docs/plate71_v3_unified_visualization.md`, and
`docs/71_ORDER_CREST_FRAMEWORK.md` describe a future SVG renderer and a
conceptual magnitude framework. They reference MATRIUN matrices as input but no
renderer module exists in this repository.
