#!/usr/bin/python3
"""
Module: print_square
prints a square with the character #
"""


def print_square(size):
    """prints a square
    Raises:
    TypeError: if size is not an integer, if size is float and < 0
    ValueError: if size is < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is float and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
