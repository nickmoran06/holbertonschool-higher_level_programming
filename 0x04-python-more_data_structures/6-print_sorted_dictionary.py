#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for counter in sorted(a_dictionary):
        print("{:s}: {}".format(counter, a_dictionary[counter]))
