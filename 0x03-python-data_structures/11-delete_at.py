#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    for counter in range(len(my_list)):
        if idx is counter:
            del(my_list[counter])
    return my_list
