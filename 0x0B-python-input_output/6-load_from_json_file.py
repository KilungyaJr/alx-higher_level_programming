#!/usr/bin/python3
"""
Module: load_from_json_file
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, encoding="utf-8") as my_file:
        read_data = my_file.read()
        return json.loads(read_data)
    # this single line works too - return json.load(my_file)
