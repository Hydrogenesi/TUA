# MATRIUN

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-16_passing-brightgreen.svg)](#testing)

**MATRIUN** is a lightweight, pure-Python matrix utility library designed for simplicity and clarity.

- ✨ **Pure Python** — No external dependencies for core operations
- 📝 **Descriptive Code** — Every variable and function name is a full English word
- ✅ **Well-Tested** — Comprehensive test suite with 16 unit tests
- 🎯 **Single-Purpose** — Each function does one thing well
- 📊 **Future-Ready** — Foundation for visualization and advanced features via Plate71

## Features

### Matrix Operations

- `create_zero_matrix(rows, cols)` — Create a zero-filled matrix
- `create_identity_matrix(size)` — Create an identity matrix
- `get_matrix_dimensions(matrix)` — Get matrix dimensions
- `add_matrices(A, B)` — Element-wise addition
- `multiply_matrices(A, B)` — Standard matrix multiplication
- `transpose_matrix(matrix)` — Transpose rows ↔ columns
- `scale_matrix(matrix, factor)` — Scalar multiplication
- `apply_wildcard_mask(matrix, value)` — Replace values with `None`

### CLI Demo

```bash
$ matriun demo
$ matriun demo --size 5  # Show 5×5 matrix operations
```

## Installation

### From Source

```bash
git clone https://github.com/Hydrogenesi/TUA.git
cd TUA
pip install .
```

### Development Installation

For contributing or experimenting:

```bash
pip install -e .
pip install -r requirements.txt  # Includes pytest
```

## Quick Start

### Python Usage

```python
from matriun import (
    create_identity_matrix,
    multiply_matrices,
    transpose_matrix,
    add_matrices,
    scale_matrix
)

# Create matrices
identity = create_identity_matrix(2)
matrix_a = [[1, 2], [3, 4]]

# Operations
result = multiply_matrices(identity, matrix_a)
scaled = scale_matrix(matrix_a, 2)
transposed = transpose_matrix(matrix_a)

print(result)  # [[1, 2], [3, 4]]
print(scaled)  # [[2, 4], [6, 8]]
print(transposed)  # [[1, 3], [2, 4]]
```

### Using the CLI

```bash
# Run the demo with a 3×3 matrix
$ matriun demo
MATRIUN demo
Matrix size: 3x3

Identity matrix:
  [1, 0, 0]
  [0, 1, 0]
  [0, 0, 1]

Zero matrix:
  [0, 0, 0]
  [0, 0, 0]
  [0, 0, 0]

# ... more operations ...
```

## Documentation

| Document | Purpose |
|---|---|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Module structure and design decisions |
| [docs/API_REFERENCE.md](docs/API_REFERENCE.md) | Complete API reference with examples |
| [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) | Setup, testing, and contribution guide |
| [docs/CHANGELOG.md](docs/CHANGELOG.md) | Version history and notable changes |
| [docs/PLATE71_RENDERER_SPEC.md](docs/plate71_renderer_spec.md) | **[PLANNED]** Visualization system for rendering matrices |

## Roadmap

### Current (v0.1.0)
- ✅ Core matrix operations
- ✅ Pure Python implementation
- ✅ CLI demo interface
- ✅ Comprehensive test suite
- ✅ Full documentation

### Planned (v0.2.0+)
- 🎨 **Plate71 Visualization** — Render matrices as interactive SVG/HTML plates
- 🔄 **Animation** — Visualize matrix transformations in real-time
- 📈 **Performance** — NumPy integration for large matrices
- 🌐 **Export** — PNG, PDF, LaTeX export formats
- 🎯 **Interactive** — Click to select cells, copy operations

See [docs/plate71_renderer_spec.md](docs/plate71_renderer_spec.md) for technical details on the visualization system.

## Testing

```bash
# Run all tests
pytest test_matriun.py

# Run with verbose output
pytest -v test_matriun.py

# Run a specific test
pytest test_matriun.py::test_multiply_matrices_produces_correct_product
```

**Current Status:** All 16 tests passing ✓

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines:

1. Open an issue to describe your change
2. Fork and create a feature branch
3. Write code following our conventions (descriptive names, no abbreviations)
4. Add tests for any new functionality
5. Run `pytest` to verify all tests pass
6. Open a pull request

## Code Style

- **Python 3.9+** — Modern Python with type hints where helpful
- **Descriptive naming** — `row_index` not `i`, `cell_width` not `w`
- **Immutability** — Functions return new matrices, never modify inputs
- **Single responsibility** — Each function does one thing well

## License

MIT License — See [LICENSE](LICENSE) for details.

## Author

Created by [Hydrogenesi](https://github.com/Hydrogenesi)

---

**Quick Links:**
- 📚 [Documentation Hub](docs/)
- 🐛 [Report Issues](https://github.com/Hydrogenesi/TUA/issues)
- 🤝 [Contributing Guide](CONTRIBUTING.md)
- 📝 [Changelog](docs/CHANGELOG.md)
