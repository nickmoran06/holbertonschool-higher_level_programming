#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda counter: counter if counter != search else replace, my_list))
