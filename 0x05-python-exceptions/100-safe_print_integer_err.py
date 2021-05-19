#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return 1
    except Exception as e:
        print("Exeption: {:}".format(e), file=sys.stderr)
