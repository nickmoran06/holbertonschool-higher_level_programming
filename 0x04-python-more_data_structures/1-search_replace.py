#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def counter_selec(counter):
        if counter != search:
            return counter
        return replace
    return list(map(counter_selec, my_list))
