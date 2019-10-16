#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file and prints it to stdout"""
    lines = 0
    with open(filename, "r", encoding="utf-8") as TxtFile:
        if nb_lines <= 0:
            print(TxtFile.read(), end="")
        else:
            for line in TxtFile:
                print(line, end='')
                lines += 1
                if lines == nb_lines:
                    break
