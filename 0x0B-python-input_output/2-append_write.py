#!/usr/bin/python3
"""
Module: append_write
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file

    Returns:
    number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
