#!/usr/bin/python3
"""
Module: append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string

    Args:
    search_string:
    new_string
    """
    with open(filename, encoding="utf-8") as my_file:
        read_text = my_file.readlines()

    with open(filename, mode="w", encoding="utf-8") as my_file:
        s = ""
        for a_line in read_text:
            s += a_line
            if search_string in a_line:
                s += new_string
        my_file.write(s)
