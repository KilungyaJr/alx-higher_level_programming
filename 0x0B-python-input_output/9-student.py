#!/usr/bin/python3
"""
Defines a class Student
"""


class Student():
    """a student class

    Attributes:
    first_name: student's first name, public
    last_name: student's last name, public
    age: student's age, public
    """
    def __init__(self, first_name, last_name, age):
        """initializes the data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """etrieves a dictionary representation of a Student instance"""
        return self.__dict__
