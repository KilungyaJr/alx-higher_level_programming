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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as my_file:
                list_ins = Base.from_json_string(my_file.read())
                return [cls.create(**d) for d in list_ins]
        except IOError:
            return "[]"

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write the CSV serialization of
         a list of objects to a file"""
        filename = cls.__name__ + ".csv"
        if filename == "Rectangle.csv":
            header = ["id", "width", "height", "x", "y"]
        else:
            header = ["id", "size", "x", "y"]

        with open(filename, "w", newline="") as csv_file:
            if list_objs == [] or list_objs is None:
                csv_file.write("[]")
            else:
                writer = csv.DictWriter(csv_file, fieldnames=header)
                for objs in list_objs:
                    writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes instantiated
        from a CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as csv_file:
                if cls.__name__ == "Rectangle":
                    header = ["id", "width", "height", "x", "y"]
                else:
                    header = ["id", "size", "x", "y"]
                list_objs = csv.DictReader(csv_file, fieldnames=header)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_objs]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
