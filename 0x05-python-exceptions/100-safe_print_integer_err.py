#!/usr/bin/python3


def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exeption: {}".format(e), file=sys.stderr)
        return False
