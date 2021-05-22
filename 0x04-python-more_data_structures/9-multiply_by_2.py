#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = a_dictionary.keys()
    vl = a_dictionary.values()
    new_v = []
    for i in vl:
        new_v.append(i * 2)
    new_dic = dict(zip(keys, new_v))
    return new_dic
