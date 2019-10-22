#!/usr/bin/python3

import json


class Base:
    """The goal of this class is to manage id attribute
    in all your future classes and to avoid duplicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the atributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        MyList = []

        if list_objs is not None:
            for counter in list_objs:
                MyList.append(cls.to_dictionary(counter))

        with open(filename, 'w') as jsonFile:
            jsonFile.write(cls.to_json_string(MyList))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)

        elif cls.__name__ is "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        MyList = []

        try:
            with open(filename, "r") as jsonFile:
                DictsList = cls.from_json_string(jsonFile.read())

        except FileNotFoundError:
            return []

        for dicts in DictsList:
            MyList.append(cls.create(**dicts))

        return MyList
