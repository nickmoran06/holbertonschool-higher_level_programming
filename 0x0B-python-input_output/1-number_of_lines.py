#!/usr/bin/python3
def number_of_lines(filename=""):
    """Function that returns the number of line a text file"""
    lines = 0
    with open(filename, encoding="utf-8") as TxtFile:
        for i in TxtFile:
            lines += 1
        return lines
