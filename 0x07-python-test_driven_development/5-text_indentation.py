#!/usr/bin/python3
def text_indentation(text):
    sym = [".", "?", ":"]
    ch = 0

    if type(text) is not str:
        raise TypeError("text must be a string")

    while ch in range(len(text)):
        if text[ch] is sym[0] or text[ch] is sym[1] or text[ch] is sym[2]:
            print("{:s}".format(text[ch]) + "\n")
            ch += 1
            while ch in range(len(text)):
                if text[ch] is not " ":
                    break
                else:
                    ch += 1
        else:
            print("{:s}".format(text[ch]), end="")
            ch += 1
