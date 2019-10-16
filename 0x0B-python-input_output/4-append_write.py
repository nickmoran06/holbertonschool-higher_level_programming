#!/usr/bin/python3
def append_write(filename="", text=""):
    """Function that appends a string to a text file"""
    with open(filename, "a", encoding="utf=8") as TxtFile:
        return TxtFile.write(text)
