#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list) - 1
    for i in range(l, 0, -1):
        print("{:d}".format(my_list[i]))
    print("{:d}".format(my_list[0]))
