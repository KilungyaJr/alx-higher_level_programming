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
        if type(width) is not int:
            raise TypeError("must be an integer")
        if width <= 0:
            raise ValueError("must be > 0")
        self.width = width
        if type(height) is not int:
            raise TypeError("must be an integer")
        if height <= 0:
            raise ValueError("must be > 0")
        self.height = height
        if type(x) is not int:
            raise TypeError("must be an integer")
        if x < 0:
            raise ValueError("must be >= 0")
        self.x = x
        if type(y) is not int:
            raise TypeError("must be an integer")
        if y < 0:
            raise ValueError("must be >= 0")
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError("must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError("must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
