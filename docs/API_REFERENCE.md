# MATRIUN API Reference

Module: `matriun`. Every function returns a **new** matrix; inputs are never mutated.

## Types

```python
Number = int | float
Matrix = list[list[Number]]
```

A matrix is a list of equal-length rows. `[]` is the 0×0 matrix. Dimensions are
always `(num_rows, num_cols)`. Functions do not validate that rows are
equal-length; ragged input is undefined behaviour.

---

### `create_zero_matrix(num_rows: int, num_cols: int) -> Matrix`

Shape: `→ (num_rows, num_cols)`, all cells `0`.

Raises `ValueError` if either dimension is negative.

```python
>>> create_zero_matrix(2, 3)
[[0, 0, 0], [0, 0, 0]]
>>> create_zero_matrix(0, 5)
[]
```

### `create_identity_matrix(size: int) -> Matrix`

Shape: `→ (size, size)`, `1` on the diagonal, `0` elsewhere.

Raises `ValueError` if `size` is negative.

```python
>>> create_identity_matrix(3)
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

### `get_matrix_dimensions(matrix) -> tuple[int, int]`

Returns `(num_rows, num_cols)`. Column count comes from the first row; `[]`
reports `(0, 0)`. Never raises.

```python
>>> get_matrix_dimensions([[1, 2, 3], [4, 5, 6]])
(2, 3)
```

### `add_matrices(first_matrix: Matrix, second_matrix: Matrix) -> Matrix`

Shape: `(m, n) + (m, n) → (m, n)`, element-wise.

Raises `ValueError("Cannot add: …")` if dimensions differ.

```python
>>> add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
[[6, 8], [10, 12]]
>>> add_matrices([[1, 2]], [[1], [2]])
ValueError: Cannot add: first matrix is 1x2 but second matrix is 2x1.
```

### `multiply_matrices(left_matrix: Matrix, right_matrix: Matrix) -> Matrix`

Shape: `(m, k) × (k, n) → (m, n)`, standard matrix product.

Raises `ValueError("Cannot multiply: …")` if `k` does not match.

```python
>>> multiply_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
[[19, 22], [43, 50]]
>>> multiply_matrices([[1, 2, 3]], [[1, 2], [3, 4]])
ValueError: Cannot multiply: left matrix has 3 columns but right matrix has 2 rows.
```

### `transpose_matrix(matrix: Matrix) -> Matrix`

Shape: `(m, n) → (n, m)`. Never raises.

```python
>>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
[[1, 4], [2, 5], [3, 6]]
```

### `scale_matrix(matrix: Matrix, scalar_factor: Number) -> Matrix`

Shape: `(m, n) → (m, n)`, every cell multiplied by `scalar_factor`. Never raises.

```python
>>> scale_matrix([[1, 2], [3, 4]], 3)
[[3, 6], [9, 12]]
```

### `apply_wildcard_mask(matrix: list[list[T]], wildcard_value: T) -> list[list[T | None]]`

Shape: `(m, n) → (m, n)`. Every cell equal to `wildcard_value` becomes `None`;
all others are copied unchanged. Never raises.

```python
>>> apply_wildcard_mask([[1, 0, 3], [0, 5, 0]], wildcard_value=0)
[[1, None, 3], [None, 5, None]]
```

---

## CLI: `matriun_cli.main(argv=None) -> int`

| Invocation | Behaviour | Exit |
|---|---|---|
| `matriun` | runs the 3×3 demo | 0 |
| `matriun demo` | runs the 3×3 demo | 0 |
| `matriun demo --size N` | runs the N×N demo (N ≥ 1) | 0 |
| `matriun demo --size 0` | argparse error | 2 |
| `matriun --help` | usage text | 0 |

Demo output sections, in order: `Identity matrix`, `Zero matrix`,
`Scaled identity (x3)`, `Matrix A` (where `A[i][j] = i*N + j`),
`Matrix B (transpose of A)`, `A + B`, `A * I`.
