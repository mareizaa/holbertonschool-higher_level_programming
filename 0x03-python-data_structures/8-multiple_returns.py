#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l > 0:
        new = (l, sentence[0])
        return(new)
    else:
        new = (l, None)
        return(new)
