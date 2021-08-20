#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    length = len(list_of_integers)

    if length <= 1:
        return None

    for i in range(1, length - 1):
        if (list_of_integers[i] >= list_of_integers[i - 1] and
                list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]
