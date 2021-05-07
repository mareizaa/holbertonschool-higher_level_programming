#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    aux = {key : value}
    a_dictionary.update(aux)
    return a_dictionary
