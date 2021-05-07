#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    aux = key
    if key in a_dictionary:
        a_dictionary.pop(aux)
        return a_dictionary
    return a_dictionary
