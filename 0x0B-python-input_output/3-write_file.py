#!/usr/bin/python3
def write_file(filename="", text=""):
    """Function that write a text to a file"""
    with open(filename, "w", encoding="utf=8") as TxtFile:
        return TxtFile.write(text)
