#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    characters = 0
    for counter in range(x):
        try:
            print("{}".format(my_list[counter]), end="")
            characters += 1
        except:
            break
    print()
    return characters
