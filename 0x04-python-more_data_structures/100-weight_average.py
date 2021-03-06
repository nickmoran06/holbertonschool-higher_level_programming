#!/usr/bin/python3
def weight_average(my_list=[]):

    num = 0
    den = 0

    if not my_list:
        return 0

    for tuple in my_list:
        num += (tuple[0] * tuple[1])
        den += tuple[1]

    return num / den
