#!/usr/bin/python3
"""
Module: read_file
"""


def read_file(filename=""):
    """reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as my_file:
        read_data = my_file.read()
        print(read_data, end="")
