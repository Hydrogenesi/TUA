# TUA · MATRIUN

MATRIUN is a small, pure-Python matrix utility library with a command-line demo.
No external runtime dependencies. Python 3.9+.

## Install

```bash
pip install .            # library + `matriun` CLI
pip install -e ".[dev]"  # editable install with pytest
```

## Quick start

```python
from matriun import create_identity_matrix, multiply_matrices, transpose_matrix

identity = create_identity_matrix(3)
data = [[2, 1, 0], [0, 3, 0], [0, 0, 4]]

print(multiply_matrices(identity, data))   # [[2, 1, 0], [0, 3, 0], [0, 0, 4]]
print(transpose_matrix([[1, 2, 3]]))       # [[1], [2], [3]]
```

## API at a glance

All functions take and return `list[list[Number]]` and never mutate their inputs.
Full signatures, shape rules, and error conditions: [docs/API_REFERENCE.md](docs/API_REFERENCE.md).

| Function | Shape rule | Raises |
|---|---|---|
| `create_zero_matrix(rows, cols)` | `→ (rows, cols)` | `ValueError` if negative |
| `create_identity_matrix(size)` | `→ (size, size)` | `ValueError` if negative |
| `get_matrix_dimensions(m)` | `(m, n) → (m, n)` tuple | — |
| `add_matrices(a, b)` | `(m, n) + (m, n) → (m, n)` | `ValueError` on mismatch |
| `multiply_matrices(a, b)` | `(m, k) × (k, n) → (m, n)` | `ValueError` on mismatch |
| `transpose_matrix(m)` | `(m, n) → (n, m)` | — |
| `scale_matrix(m, k)` | `(m, n) → (m, n)` | — |
| `apply_wildcard_mask(m, v)` | `(m, n) → (m, n)`, matches → `None` | — |

## CLI

```bash
matriun                 # same as `matriun demo`
matriun demo            # 3x3 walkthrough
matriun demo --size 4   # NxN walkthrough, N >= 1
matriun --help
```

Exit code `0` on success, `2` on argument errors (e.g. `--size 0`).
The demo prints: identity, zero, scaled identity, an asymmetric matrix A, its
transpose, `A + Aᵀ`, and `A × I`.

## Testing

```bash
python -m pytest
```

Tests are the source of truth for behaviour; documentation follows the tests.

## Documentation

| Document | Status | Contents |
|---|---|---|
| [docs/index.md](docs/index.md) | current | Documentation hub |
| [docs/API_REFERENCE.md](docs/API_REFERENCE.md) | current | Every function: signature, shape rule, errors, example |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | current | Module layout and design constraints |
| [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) | current | Setup, testing, conventions, release |
| [docs/plate71_renderer_spec.md](docs/plate71_renderer_spec.md) | **planned** | Plate71 SVG renderer for MATRIUN matrices — spec only, no code yet |
| [docs/plate71_v3_unified_visualization.md](docs/plate71_v3_unified_visualization.md) | **planned** | Plate71 v3 crest visualization — spec only |
| [docs/71_ORDER_CREST_FRAMEWORK.md](docs/71_ORDER_CREST_FRAMEWORK.md) | **planned** | 71-order magnitude ladder framework — conceptual, not implemented |
| [CHANGELOG.md](CHANGELOG.md) | current | Release history |

## Roadmap

Documents marked **planned** describe future work. Nothing under `docs/plate71*`
or `docs/71_ORDER*` is implemented in this repository; the only code is
`matriun.py`, `matriun_cli.py`, and `test_matriun.py`.

## License

MIT — see [LICENSE](LICENSE).
