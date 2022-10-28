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
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id, self.x, self.y, self.height)
