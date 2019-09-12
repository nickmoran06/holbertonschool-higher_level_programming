#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_arg = len(argv)

    if len_arg == 1:
        print("{:d} {:s}{:s}".format(len_arg - 1, "argument", "."))
    elif len_arg == 2:
        print("{:d} {:s}{:s}".format(len_arg - 1, "argument", ":"))
    else:
        print("{:d} {:s}{:s}".format(len_arg - 1, "arguments", ":"))

    for i, j in enumerate(argv):
        if i > 0:
            print("{}: {}".format(i, j))
