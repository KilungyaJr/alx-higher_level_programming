#!/usr/bin/python3
"""A Class Rectangle."""


class Rectangle:
    """Represents a rectangle

    Attributes:
    __width (int): private attr
    __height (int): private attr
    """

    def __init__(self, width=0, height=0):
        """initializes the data"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter

        Args:
        value (int): width of a rectangle

        Raises:
        TypeError: if width is not an integer
        ValueError: if width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter

        Args:
        value (int): height of the rectangle

        Raises:
        TypeError: if height is not an int
        ValueError: if height < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
