#!/usr/bin/python3
"""
Module - lookup
Finds list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Args:
    obj: object to look into

    Returns:
    a list object
    """
    return dir(obj)
