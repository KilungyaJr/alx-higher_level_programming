#!/usr/bin/python3
"""
Module - is_same_class
"""


def is_same_class(obj, a_class):
    """checks instance of the specified class

    Args:
    obj: object to check
    a_class: class to check

    Returns:
    True if the object is exactly an instance of the specified class;
    otherwise False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
