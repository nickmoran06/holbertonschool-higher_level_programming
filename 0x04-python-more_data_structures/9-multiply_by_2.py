#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for counter in b_dictionary:
        b_dictionary[counter] *= 2
    return b_dictionary
