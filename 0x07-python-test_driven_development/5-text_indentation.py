#!/usr/bin/python3
"""
prints a text with 2 new lines
fter each of these characters: 
., ? and :
"""


def text_indentation(text):
    """
    prints a text with 2 new lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    new = text.replace(". ",".\n\n").replace("? ","?\n\n").replace(": ",":\n\n")
    print(new, end="")
