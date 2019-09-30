#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    characters = 0
    for counter in range(x):
        try:
            print("{:d}".format(my_list[counter]), end="")
            characters += 1
        except (TypeError, ValueError):
            continue
    print()
    return characters
