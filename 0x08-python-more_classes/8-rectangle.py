#!/usr/bin/python3
"""A Class Rectangle."""


class Rectangle:
    """Represents a rectangle

    Attributes:
    __width (int): private attr
    __height (int): private attr
    number_of_instances: public attr
    print_symbol: public attr used as symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the data

        Args:
        height (int): height of rect
        width (int): width of rect
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """prints a rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rec_str = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rec_str += str(self.print_symbol)
                rec_str += "\n"
            return rec_str[:-1]

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """deletes an instance of rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """compares the areas of rectangles

        Raises:
        TypeError: if instance is not a rectangle

        Returns:
        the biggest rectangle based on the area
        rect_1 if both have the same area value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
