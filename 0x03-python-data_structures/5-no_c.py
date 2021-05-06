#!/usr/bin/python3
def no_c(my_string):
    i = 0
    copy = ""
    while i < len(my_string):
        if my_string[i] != "c" and my_string[i] != "C":
            copy += my_string[i]
        i += 1
    return copy
