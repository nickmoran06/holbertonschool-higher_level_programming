#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    for arguments in argv[1:]:
        result += int(arguments)
    print("{:d}".format(result))
