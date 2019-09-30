#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as Error:
        print("Exception: {:s}".format(str(Error)), file=sys.stderr)
        return False
    return True
