#!/usr/bin/python3
"""
Defines a class BaseGeometry
"""


class BaseGeometry():
    """public instance method: area, integer validator"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """represents a rectangle that inherits from BaseGeometry class

    Attributes:
    width, height - all private
    """
    def __init__(self, width, height):
        """initializes data"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
