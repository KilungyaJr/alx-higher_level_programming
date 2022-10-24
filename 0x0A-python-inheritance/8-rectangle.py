#!/usr/bin/python3
"""
Defines a class BaseGeometry
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
