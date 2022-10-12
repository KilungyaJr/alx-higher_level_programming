#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square

    Attributes:
    __size (int): private attr - size of side of a square

    property def size(self): to retrieve it
    property setter def size(self, value): to set it
    area: public instance method
    """

    def __init__(self, size=0):
        """Initializes a square

        Args:
        size (int): size of a side of a square
        """
        self.__size = size

    @property
    def size(self):
        """property getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter

        Args:
        value (int): size of a side of a square

        Raises:
        TypeError: If size is not an int
        ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Finds the area of a square

        Returns:
        the current square area
        """
        return self.__size ** 2
