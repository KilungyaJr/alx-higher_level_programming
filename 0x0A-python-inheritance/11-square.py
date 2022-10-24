#!/usr/bin/python3
"""
Defines a class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a Square that inherits Rectangle class

    Attributes:
    size - private
    """
    def __init__(self, size):
        """initializes data

        Args:
        size: size of a side of a square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """finds the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """prints square description"""
        return str("[Square] {:d}/{:d}".format(self.__size, self.__size))
