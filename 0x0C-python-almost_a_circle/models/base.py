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
        if list_objs is None:
            list_objs = []
        new = []
        for entry in list_objs:
            new.append(cls.to_dictionary(entry))
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """from json string method"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create method"""
        if cls.__name__ == "Square":
            temp = cls(1)
        else:
            temp = cls(1, 1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """load from file method"""
        pass
