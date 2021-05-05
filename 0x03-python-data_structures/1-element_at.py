#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    i = 0
    while i < len(my_list):
        if i == idx:
            return (my_list[idx])
        i += 1
