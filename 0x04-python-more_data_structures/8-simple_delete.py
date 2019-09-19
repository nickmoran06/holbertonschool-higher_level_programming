#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        for counter in a_dictionary:
            if counter is key:
                del a_dictionary[counter]
                return a_dictionary
    return a_dictionary
