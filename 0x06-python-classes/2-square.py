#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square

    Attributes:
    __size (int): private attr - size of side of a square
    """

    def __init__(self, size=0):
        """Initializes a square

        Args:
        size (int): size of a side of a square

        Raises:
        TypeError: If size is not an int
        ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
