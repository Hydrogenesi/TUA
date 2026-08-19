# Documentation Hub

## MATRIUN

MATRIUN provides small, focused matrix helpers for Python and includes a CLI demo.

## Navigation

| Document | Description |
|---|---|
| [Plate71 Renderer Specification](./plate71_renderer_spec.md) | Technical specification for rendering MATRIUN matrices as interactive SVG/HTML visual plates (feature preview). |

## Installation

```bash
pip install .
```

## CLI

Run the demo:

```bash
matriun demo
```

Run a larger demo:

```bash
matriun demo --size 4
```

Show help:

```bash
matriun --help
```

## Library Example

```python
from matriun import create_identity_matrix, multiply_matrices

identity = create_identity_matrix(2)
data = [[2, 1], [0, 3]]
print(multiply_matrices(identity, data))
```
