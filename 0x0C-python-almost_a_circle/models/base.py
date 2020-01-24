#!/usr/bin/python3
import json
""" Base class"""


class Base:
    """Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Method def"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """json string method"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
