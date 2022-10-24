#!/usr/bin/python3
"""
defines a class MyList that inherits from list
"""


class MyList(list):
    """a class MyList that inherits from list"""

    def print_sorted(self):
        """prints a sorted list in ascending order"""
        print(sorted(self))
