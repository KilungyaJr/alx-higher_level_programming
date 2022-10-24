#!/usr/bin/python3
"""
Method - inherits_from
"""


def inherits_from(obj, a_class):
    """checks object instance in subclass and superclass

    Args:
    obj: object to check
    a_class: class to check

    Returns:
    True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class;
    otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
