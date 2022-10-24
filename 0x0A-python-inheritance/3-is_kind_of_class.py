#!/usr/bin/python3
"""
Method - is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """checks object instance in subclass and superclass

    Args:
    obj: object to check
    a_class: class to check

    Returns:
    True if the object is an instance of, or if the object is an instance of
    a class that inherited from the specified class;
    otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
