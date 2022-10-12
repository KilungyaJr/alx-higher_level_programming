#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square

    Attributes:
    __size (int): private attr - size of side of a square

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
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Finds the area of a square

        Returns:
        the current square area
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Defines the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison to a Square."""
        return self.area() >= other.area()
