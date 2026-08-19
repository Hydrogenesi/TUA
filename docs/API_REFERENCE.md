# API Reference

All public functions live in `matriun.py`.

---

## `create_zero_matrix(num_rows, num_cols)`

Return a matrix of zeros with the given dimensions.

**Parameters**
- `num_rows` (`int`) — Number of rows.
- `num_cols` (`int`) — Number of columns.

**Returns** `list[list[int]]` — A `num_rows × num_cols` matrix filled with `0`.

```python
create_zero_matrix(2, 3)
# [[0, 0, 0], [0, 0, 0]]
```

---

## `create_identity_matrix(size)`

Return a square identity matrix of the given size.

**Parameters**
- `size` (`int`) — Number of rows and columns.

**Returns** `list[list[int]]` — A `size × size` matrix with `1` on the main diagonal and `0` elsewhere.

```python
create_identity_matrix(3)
# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

---

## `get_matrix_dimensions(matrix)`

Return the dimensions of a matrix.

**Parameters**
- `matrix` (`list[list]`) — The matrix to inspect. May be empty (`[]`).

**Returns** `tuple[int, int]` — `(num_rows, num_cols)`. Returns `(0, 0)` for an empty matrix.

```python
get_matrix_dimensions([[1, 2, 3], [4, 5, 6]])
# (2, 3)
```

---

## `add_matrices(first_matrix, second_matrix)`

Return the element-wise sum of two matrices with identical dimensions.

**Parameters**
- `first_matrix` (`list[list[number]]`) — The first operand.
- `second_matrix` (`list[list[number]]`) — The second operand (must match dimensions).

**Returns** `list[list[number]]` — A new matrix where each element is the sum of the corresponding elements.

```python
add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
# [[6, 8], [10, 12]]
```

---

## `multiply_matrices(left_matrix, right_matrix)`

Return the matrix product of two matrices.

**Parameters**
- `left_matrix` (`list[list[number]]`) — The left operand (`m × k`).
- `right_matrix` (`list[list[number]]`) — The right operand (`k × n`).

**Returns** `list[list[number]]` — A new `m × n` matrix.

**Raises** `ValueError` — If `left_matrix` columns ≠ `right_matrix` rows.

```python
multiply_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
# [[19, 22], [43, 50]]
```

---

## `transpose_matrix(matrix)`

Return the transpose of the given matrix (rows become columns).

**Parameters**
- `matrix` (`list[list[number]]`) — The matrix to transpose (`m × n`).

**Returns** `list[list[number]]` — A new `n × m` matrix.

```python
transpose_matrix([[1, 2, 3], [4, 5, 6]])
# [[1, 4], [2, 5], [3, 6]]
```

---

## `scale_matrix(matrix, scalar_factor)`

Return a new matrix with every element multiplied by a scalar.

**Parameters**
- `matrix` (`list[list[number]]`) — The matrix to scale.
- `scalar_factor` (`number`) — The value to multiply each element by.

**Returns** `list[list[number]]` — A new matrix of the same dimensions.

```python
scale_matrix([[1, 2], [3, 4]], scalar_factor=3)
# [[3, 6], [9, 12]]
```

---

## `apply_wildcard_mask(matrix, wildcard_value)`

Replace every element equal to `wildcard_value` with `None`.

Cells matching the wildcard are treated as unset rather than as a numeric value. The original matrix is not modified.

**Parameters**
- `matrix` (`list[list[number]]`) — The source matrix.
- `wildcard_value` (`number`) — The sentinel value to replace.

**Returns** `list[list[number | None]]` — A new matrix with matching cells set to `None`.

```python
apply_wildcard_mask([[1, 0, 3], [0, 5, 0]], wildcard_value=0)
# [[1, None, 3], [None, 5, None]]
```
