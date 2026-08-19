# Changelog

All notable changes to MATRIUN are documented here.

## [0.1.0] — Initial Release

### Added

- `create_zero_matrix(num_rows, num_cols)` — Returns a matrix of zeros.
- `create_identity_matrix(size)` — Returns a square identity matrix.
- `get_matrix_dimensions(matrix)` — Returns `(num_rows, num_cols)` tuple.
- `add_matrices(first_matrix, second_matrix)` — Element-wise addition.
- `multiply_matrices(left_matrix, right_matrix)` — Standard matrix product.
- `transpose_matrix(matrix)` — Rows become columns.
- `scale_matrix(matrix, scalar_factor)` — Multiplies every element by a scalar.
- `apply_wildcard_mask(matrix, wildcard_value)` — Replaces matching cells with `None`.
- CLI entry point `matriun demo [--size N]`.
- Full pytest suite covering all public functions and the CLI.
