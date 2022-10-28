#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Reprsents the class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor - initializes the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints in formatted output"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        if type(value) is not int:
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError("must be > 0")
        self.width = value
        self.height = value
