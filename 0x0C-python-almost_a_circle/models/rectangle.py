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
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for i in range(self.height):
            for j in range(self.width + self.x):
                if j < self.x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

    def __str__(self):
        """prints in formatted output"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__, self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args or len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            if kwargs or len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id =value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
