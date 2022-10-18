#!/usr/bin/python3
"""
Module: say_my_name
prints formatted first and last names
"""


def say_my_name(first_name, last_name=""):
    """Returns formated output of a name
    Raises: TypeError if first and last names are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
