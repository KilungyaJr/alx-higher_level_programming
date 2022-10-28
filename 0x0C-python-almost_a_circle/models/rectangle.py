#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """Represents a class Rectangle

    Attributes:
    __width: width of the rectangle
    __height: height of rectangle
    __x:
    __y:
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor - initializes the data"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        self.__y = value
