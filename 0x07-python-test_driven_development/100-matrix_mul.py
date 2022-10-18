#!/usr/bin/python3
"""
Module: matrix_mul
Matrix Multiplication
"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices
    Raises TypeErrors and ValueErrors
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for j in m_b:
        if type(j) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for j in row:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")

    row_len = []
    for row in m_a:
        row_len.append(len(row))
    if not all(elem == row_len[0] for elem in row_len):
        raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        row_len.append(len(row))
    if not all(elem == row_len[0] for elem in row_len):
        raise TypeError("each row of m_b must be of the same size")

    num_col = 0
    for col in m_a[0]:
        num_col = num_col + 1
    num_row = 0
    for row in m_b:
        num_row = num_row + 1

    if num_col != num_row:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
