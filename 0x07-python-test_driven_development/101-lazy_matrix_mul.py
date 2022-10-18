#!/usr/bin/python3
"""
Module: lazy_matrix_mul
Matrix Multiplication using NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices
    using matmul function of NumPy
    """
    return numpy.matmul(m_a, m_b)
