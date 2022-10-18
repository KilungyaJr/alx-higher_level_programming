#!/usr/bin/python3
"""
Module: text_indentation
prints a text with 2 new lines after a set of characters
"""


def text_indentation(text):
    """prints text with 2 added lines after each of these chars: ., ? and :
    Raises:
    TypeError if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if flag == 0:
            if char == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if char == "." or char == "?" or char == ":":
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")
