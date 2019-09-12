#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        str_without_n = str[:n] + str[n + 1:]
        return (str_without_n)
    else:
        return (str)
