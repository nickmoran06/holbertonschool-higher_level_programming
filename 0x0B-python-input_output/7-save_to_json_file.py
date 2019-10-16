#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, using a JSON represent"""
    with open(filename, "w", encoding="utf-8") as TxtFile:
        json.dump(my_obj, TxtFile)
