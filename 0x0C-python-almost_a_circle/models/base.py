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
