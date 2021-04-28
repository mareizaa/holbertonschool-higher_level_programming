#!/usr/bin/python3
for i in range(0, 10):
    for c in range(0, 10):
        if i < c and (i * 10) + c < 89:
            print('{:}{:}'.format(i, c), end=', ')
        elif i == 8 and c == 9:
            print('{:}{:}'.format(i, c))
