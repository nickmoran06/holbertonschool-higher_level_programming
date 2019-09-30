#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as Error:
        sys.stderr.write("Exception: {:s}".format(str(Error)))
        return False
    return True
