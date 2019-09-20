#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda c: c if c != search else replace, my_list))
