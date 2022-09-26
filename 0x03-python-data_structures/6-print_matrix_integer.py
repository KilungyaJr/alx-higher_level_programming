#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print('\n'.join([' '.join(['{:d}'.format(item) for item in row])]))
