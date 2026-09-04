# MATRIUN Documentation Hub

MATRIUN is a pure-Python matrix utility library with a CLI demo. Python 3.9+, no runtime dependencies.

## Guides

| Document | Status | What it covers |
|---|---|---|
| [API Reference](API_REFERENCE.md) | current | Every function: signature, shape rule, errors, example; CLI behaviour and exit codes |
| [Architecture](ARCHITECTURE.md) | current | Module layout and design constraints |
| [Development](DEVELOPMENT.md) | current | Setup, testing, conventions, release steps |
| [Plate71 Renderer Spec](plate71_renderer_spec.md) | **planned** | SVG/HTML renderer for MATRIUN matrices — specification only |
| [Plate71 v3 Unified Visualization](plate71_v3_unified_visualization.md) | **planned** | Crest visualization layer on top of Plate71 — specification only |
| [71-Order Crest Framework](71_ORDER_CREST_FRAMEWORK.md) | **planned** | Conceptual magnitude-ladder framework — not implemented |

## Install

```bash
pip install .            # library + CLI
pip install -e ".[dev]"  # editable, with pytest
```

## CLI

```bash
matriun                 # 3x3 demo
matriun demo --size 4   # 4x4 demo
matriun --help
```

## Library example

```python
from matriun import add_matrices, create_identity_matrix, multiply_matrices

identity = create_identity_matrix(2)
data = [[2, 1], [0, 3]]
print(multiply_matrices(identity, data))   # [[2, 1], [0, 3]]
print(add_matrices(data, identity))        # [[3, 1], [0, 4]]
```
