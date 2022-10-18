#!/usr/bin/python3
"""
Module add_integer
Adds two integers through main func

"""


def add_integer(a, b=98):
    """returns the sum of two integers
    Raises:TypeError: if a and b are not integers or floats
    """
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
