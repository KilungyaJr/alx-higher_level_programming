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
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

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

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args or len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.width, self.width, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            if kwargs or len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(self.width, self.width,
                                          self.x, self.y)
                        else:
                            self.id = value
                    if key == "size":
                        self.width = value
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
