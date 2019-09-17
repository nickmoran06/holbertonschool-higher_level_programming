#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    my_list = list(my_string)
    for counter in range(len(my_list)):
        if my_list[counter] is "c" or my_list[counter] is "C":
            my_list[counter] = ""
    return(''.join(my_list))
