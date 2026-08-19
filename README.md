# MATRIUN

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

MATRIUN is a lightweight Python matrix utility library with a small command-line demo. It provides clear, descriptive functions for common matrix operations with no external dependencies.

## Features

- Create zero and identity matrices
- Add, multiply, transpose, and scale matrices
- Apply wildcard masking to matrix cells
- Simple CLI demo to explore operations interactively

## Install

Install from the project root:

```bash
pip install .
```

For editable development installs:

```bash
pip install -e .
```

## Python Usage

```python
from matriun import (
    create_identity_matrix,
    create_zero_matrix,
    add_matrices,
    multiply_matrices,
    transpose_matrix,
    scale_matrix,
    apply_wildcard_mask,
)

# Create a 3x3 identity matrix
identity = create_identity_matrix(3)

# Multiply two matrices
result = multiply_matrices(identity, [[2, 1, 0], [0, 3, 0], [0, 0, 4]])
print(result)
# [[2, 1, 0], [0, 3, 0], [0, 0, 4]]

# Scale a matrix by a scalar
scaled = scale_matrix([[1, 2], [3, 4]], scalar_factor=2)
print(scaled)
# [[2, 4], [6, 8]]

# Mask wildcard values
masked = apply_wildcard_mask([[1, 0, 3], [0, 5, 0]], wildcard_value=0)
print(masked)
# [[1, None, 3], [None, 5, None]]
```

## CLI Demo

After installation, run:

```bash
matriun demo
```

Specify the demo matrix size:

```bash
matriun demo --size 4
```

Show help:

```bash
matriun --help
```

## Documentation

| Document | Description |
| --- | --- |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Module structure and design decisions |
| [docs/API_REFERENCE.md](docs/API_REFERENCE.md) | Full function signatures and descriptions |
| [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) | Contributing and testing guide |
| [docs/CHANGELOG.md](docs/CHANGELOG.md) | Version history |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE).