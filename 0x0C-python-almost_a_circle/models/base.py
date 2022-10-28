#!/usr/bin/python3
"""
Defines a class Base
"""
import json


class Base:
    """ represents the base class
    Attributes:
    __nb_objects: private attr
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor - initializes a new object with a given id"""
        if id is not None:
            self.id = id
        else:
           self.__class__.__nb_objects += 1
           self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf=8") as json_file:
            if list_objs is None or list_objs is []:
                json_file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string is []:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(10, 5)
            else:
                instance = cls(10)
            instance.update(**dictionary)
            return instance
