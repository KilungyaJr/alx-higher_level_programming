#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    sq_matrix = []
    for x in matrix:
        sq_matrix.append(list(map(lambda x: x ** 2, x)))
    return sq_matrix
