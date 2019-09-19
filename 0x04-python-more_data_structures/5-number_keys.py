#!/usr/bin/python3
def number_keys(a_dictionary):
    num_keys = 0

    for counter in set(a_dictionary):
        num_keys += 1

    return num_keys
