#!/usr/bin/python3
""" Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """json string method"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file method"""
        pass

    @staticmethod
    def from_json_string(json_string):
        """from json string method"""
        if json_string is None:
            return []
        return json.dumps(json_string)
