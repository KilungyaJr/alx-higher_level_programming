#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square

    Attributes:
    __size (int): private attr - size of side of square
    """

    def __init__(self, size):
        """Initializes a square

        Args:
        size (int): size of a side of a new square.
        """
        self.__size = size
