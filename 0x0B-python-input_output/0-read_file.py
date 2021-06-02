#!/usr/bin/python3
""" reads a text file (UTF8) and prints it"""


def read_file(filename=""):
    with open(filename) as f:
        print(f.read(), end="")
