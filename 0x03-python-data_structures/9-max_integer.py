#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    tmp = 0
    for counter in range(len(my_list)):
        if my_list[counter] >= tmp:
            tmp = my_list[counter]
    return tmp
