#!/usr/bin/python3
"""Python class MagicClass from a given ByteCode."""
import math


class MagicClass:
    """Represents the MagicClass"""

    def __init__(self, radius=0):
        """Initializes the operation

        Args:
        radius (int or float): radius of the MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculates the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calculates the circumference"""
        return 2 * math.pi * self.__radius
