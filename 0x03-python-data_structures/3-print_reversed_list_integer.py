#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list)
    i = l
    while i:
        i -= 1
        print("{:d}".format(my_list[i]))
