#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a = len(tuple_a)
    b = len(tuple_a)
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    if a is 2 and b is 2:
        pos_0 = tuple_a[0] + tuple_b[0]
        pos_1 = tuple_a[1] + tuple_b[1]
        tuple_c = (pos_0, pos_1)
        return tuple_c
    elif a < 2:
        tuple_a[1] = 0
    elif b < 2:
        tuple_b[1] = 0
    elif a < 2 and b is 2:
        return tuple_b
    elif b < 2 and a is 2:
        return tuple_a
    elif a is 0 and b is 0:
        return tuple_a
    elif a < 2 and b < 2:
        return (tuple_a[0] + tuple_b[0], 0)
