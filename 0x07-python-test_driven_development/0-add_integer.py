#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)
    return int(a + b)
