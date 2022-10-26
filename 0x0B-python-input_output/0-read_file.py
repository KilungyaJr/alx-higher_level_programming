#!/usr/bin/python3
"""
Module: read_file
"""


def read_file(filename=""):
    """reads a text file and prints it to stdout"""
    with open("my_file_0.txt", encoding="utf-8") as filename:
        read_data = filename.read()
