#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    aux = list(set(my_list))
    for i in aux:
        add += i
    return add
