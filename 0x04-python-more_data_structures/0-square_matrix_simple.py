#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for row in matrix:
        sq_matrix.append([i ** 2 for i in row])
    return sq_matrix
