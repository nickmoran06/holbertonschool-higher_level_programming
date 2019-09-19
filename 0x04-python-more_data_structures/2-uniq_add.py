#!/usr/bin/python3
def uniq_add(my_list=[]):

    redu_sum = 0

    for counter in set(my_list):
        redu_sum += counter

    return redu_sum
