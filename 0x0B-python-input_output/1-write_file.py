#!/usr/bin/python3
"""
Module: write_file
"""


def write_file(filename="", text=""):
    """writes a string to a text file

    Returns:
    number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(text)
