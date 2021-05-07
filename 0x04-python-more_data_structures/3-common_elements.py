#!/usr/bin/python3
def common_elements(set_1, set_2):
    aux = []
    comun = []
    for i in set_1:
        if i not in set_2:
            comun.append(i)
        else:
            aux.append(i)
    return aux
