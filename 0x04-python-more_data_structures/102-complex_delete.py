#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    if not a_dictionary:
        return a_dictionary

    value_del = []

    for key_value in a_dictionary:
        if a_dictionary[key_value] is value:
            value_del.append(key_value)

    for key_value in value_del:
        del a_dictionary[key_value]

    return a_dictionary
