#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolean_list = []
    for counter in range(len(my_list)):
        if my_list[counter] % 2 == 0:
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    return boolean_list
