#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list.copy()
    if my_list is None:
        return
    if idx < 0 and idx > len(my_list):
        return cpy_list
    for counter in range(len(cpy_list)):
        if idx == counter:
            cpy_list[counter] = element
    return cpy_list
