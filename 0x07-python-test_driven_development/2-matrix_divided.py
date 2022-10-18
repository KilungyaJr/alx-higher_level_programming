#!/usr/bin/python3
"""
Module: matrix_divided
divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """divides each element of a matrix, rounded to 2 decimals.
    Raises: Exceptions as in the func.
    Returns: A new division matrix
    """
    mat_typ_err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError(mat_typ_err)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(mat_typ_err)
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError(mat_typ_err)

    row_len = []
    for row in matrix:
        row_len.append(len(row))
    if not all(elem == row_len[0] for elem in row_len):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    div_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return div_matrix
