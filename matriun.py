"""
MATRIUN - Matrix utility module for TUA.

Pure-Python matrix helpers operating on ``list[list[Number]]``. No external
dependencies. Every function returns a new matrix; inputs are never mutated.

Shape conventions
-----------------
A matrix is a list of equal-length row lists. ``[]`` is the 0x0 matrix.
Dimensions are reported as ``(num_rows, num_cols)``.
"""

from __future__ import annotations

from typing import Any, List, Optional, Sequence, Tuple, TypeVar, Union

Number = Union[int, float]
Matrix = List[List[Number]]
T = TypeVar("T")


def create_zero_matrix(num_rows: int, num_cols: int) -> Matrix:
    """Return a ``num_rows x num_cols`` matrix filled with ``0``.

    Shape: ``(num_rows, num_cols)``.

    Raises:
        ValueError: if either dimension is negative.

    Example:
        >>> create_zero_matrix(2, 3)
        [[0, 0, 0], [0, 0, 0]]
    """
    if num_rows < 0 or num_cols < 0:
        raise ValueError(
            f"Matrix dimensions must be non-negative, got {num_rows}x{num_cols}."
        )
    return [[0] * num_cols for _ in range(num_rows)]


def create_identity_matrix(size: int) -> Matrix:
    """Return the ``size x size`` identity matrix.

    Shape: ``(size, size)``.

    Raises:
        ValueError: if ``size`` is negative.

    Example:
        >>> create_identity_matrix(3)
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    identity = create_zero_matrix(size, size)
    for diagonal_index in range(size):
        identity[diagonal_index][diagonal_index] = 1
    return identity


def get_matrix_dimensions(matrix: Sequence[Sequence[Any]]) -> Tuple[int, int]:
    """Return ``(num_rows, num_cols)`` for ``matrix``.

    The column count is taken from the first row; ``[]`` reports ``(0, 0)``.

    Example:
        >>> get_matrix_dimensions([[1, 2, 3], [4, 5, 6]])
        (2, 3)
        >>> get_matrix_dimensions([])
        (0, 0)
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    return num_rows, num_cols


def add_matrices(first_matrix: Matrix, second_matrix: Matrix) -> Matrix:
    """Return the element-wise sum of two matrices.

    Shape rule: both inputs must be ``(m, n)``; the result is ``(m, n)``.

    Raises:
        ValueError: if the two matrices have different dimensions.

    Example:
        >>> add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[6, 8], [10, 12]]
    """
    num_rows, num_cols = get_matrix_dimensions(first_matrix)
    other_rows, other_cols = get_matrix_dimensions(second_matrix)
    if (num_rows, num_cols) != (other_rows, other_cols):
        raise ValueError(
            f"Cannot add: first matrix is {num_rows}x{num_cols} "
            f"but second matrix is {other_rows}x{other_cols}."
        )

    result_matrix = create_zero_matrix(num_rows, num_cols)
    for row_index in range(num_rows):
        for col_index in range(num_cols):
            result_matrix[row_index][col_index] = (
                first_matrix[row_index][col_index]
                + second_matrix[row_index][col_index]
            )
    return result_matrix


def multiply_matrices(left_matrix: Matrix, right_matrix: Matrix) -> Matrix:
    """Return the matrix product ``left_matrix @ right_matrix``.

    Shape rule: ``(m, k) x (k, n) -> (m, n)``.

    Raises:
        ValueError: if ``left_matrix`` column count != ``right_matrix`` row count.

    Example:
        >>> multiply_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
    """
    left_rows, left_cols = get_matrix_dimensions(left_matrix)
    right_rows, right_cols = get_matrix_dimensions(right_matrix)

    if left_cols != right_rows:
        raise ValueError(
            f"Cannot multiply: left matrix has {left_cols} columns "
            f"but right matrix has {right_rows} rows."
        )

    product_matrix = create_zero_matrix(left_rows, right_cols)
    for row_index in range(left_rows):
        for col_index in range(right_cols):
            dot_product = 0
            for shared_index in range(left_cols):
                dot_product += (
                    left_matrix[row_index][shared_index]
                    * right_matrix[shared_index][col_index]
                )
            product_matrix[row_index][col_index] = dot_product
    return product_matrix


def transpose_matrix(matrix: Matrix) -> Matrix:
    """Return the transpose of ``matrix`` (rows become columns).

    Shape rule: ``(m, n) -> (n, m)``. Never raises.

    Example:
        >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    num_rows, num_cols = get_matrix_dimensions(matrix)
    transposed_matrix = create_zero_matrix(num_cols, num_rows)
    for row_index in range(num_rows):
        for col_index in range(num_cols):
            transposed_matrix[col_index][row_index] = matrix[row_index][col_index]
    return transposed_matrix


def scale_matrix(matrix: Matrix, scalar_factor: Number) -> Matrix:
    """Return a new matrix with every element multiplied by ``scalar_factor``.

    Shape rule: ``(m, n) -> (m, n)``. Never raises.

    Example:
        >>> scale_matrix([[1, 2], [3, 4]], 3)
        [[3, 6], [9, 12]]
    """
    num_rows, num_cols = get_matrix_dimensions(matrix)
    scaled_matrix = create_zero_matrix(num_rows, num_cols)
    for row_index in range(num_rows):
        for col_index in range(num_cols):
            scaled_matrix[row_index][col_index] = (
                matrix[row_index][col_index] * scalar_factor
            )
    return scaled_matrix


def apply_wildcard_mask(
    matrix: List[List[T]], wildcard_value: T
) -> List[List[Optional[T]]]:
    """Return a copy of ``matrix`` with every cell equal to ``wildcard_value`` set to ``None``.

    Cells matching the wildcard are treated as unset rather than as a value.
    The input is not mutated.

    Shape rule: ``(m, n) -> (m, n)``. Never raises.

    Example:
        >>> apply_wildcard_mask([[1, 0, 3], [0, 5, 0]], wildcard_value=0)
        [[1, None, 3], [None, 5, None]]
    """
    num_rows, num_cols = get_matrix_dimensions(matrix)
    masked_matrix: List[List[Optional[T]]] = [list(row) for row in matrix]
    for row_index in range(num_rows):
        for col_index in range(num_cols):
            if masked_matrix[row_index][col_index] == wildcard_value:
                masked_matrix[row_index][col_index] = None
    return masked_matrix
