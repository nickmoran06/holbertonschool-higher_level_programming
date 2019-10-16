#!/usr/bin/python3
def inherits_from(obj, a_class):
    """returns boolean if obj is a subclass of a_class"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
