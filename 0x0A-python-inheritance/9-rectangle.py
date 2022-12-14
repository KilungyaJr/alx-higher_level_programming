#!/usr/bin/python3
"""
Defines a class Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents a rectangle that inherits BaseGeometry class

    Attributes:
    width, height - all private
    """
    def __init__(self, width, height):
        """initializes data

        Args:
        width: width of rectangle
        height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """finds the rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """prints rectangle description"""
        return str("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
