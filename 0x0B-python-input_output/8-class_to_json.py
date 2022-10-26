#!/usr/bin/python3
"""
Module: class_to_json
"""


def class_to_json(obj):
    """
    Attributes:
    obj: instance of a class, serializable

    Returns:
    the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    return obj.__dict__
