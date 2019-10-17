#!/usr/bin/python3
class Student:
    """Student representation"""
    def __init__(self, first_name, last_name, age):
        """Initilize the atributess"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Show as dictionary the instance with the specified atributes"""
        if attrs is None:
            return self.__dict__
        expec_dict = {}
        for keys in attrs:
            try:
                expec_dict[keys] = self.__dict__[keys]
            except:
                """Ignore the keys that not are in the dictionary"""
                continue
        return expec_dict

    def reload_from_json(self, json):
        """Method that replaces all atributes of the Student instance"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__.update({key: value})
