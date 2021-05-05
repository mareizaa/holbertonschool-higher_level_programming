#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list)
    while l:
        l -= 1
        print("{:d}".format(my_list[l]))
