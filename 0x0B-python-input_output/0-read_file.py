#!/usr/bin/python3
def read_file(filename=""):
    """Function to read a text file nad prints in stdout"""
    with open(filename, "r", encoding="utf-8") as TxtFile:
        print(TxtFile.read(), end="")
