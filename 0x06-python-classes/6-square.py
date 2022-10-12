#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square

    Attributes:
    __size (int): private attr - size of side of a square
    __position (tuple): private attr - 2 positive integers

    property def size(self): to retrieve it
    property def position(self): to retrieve it
    property setter def size(self, value): to set it
    property setter def position(self, value): to set it

    area: public instance method
    my_print: public instance method
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square

        Args:
        size (int): size of a side of a square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieves the size attr."""
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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieves the position attr."""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter

        Args:
        value (tuple): of two integers

        Raises:
        TypeError: if not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Finds the area of a square

        Returns:
        the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #."""
        if self.__size == 0:
            print()

        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
