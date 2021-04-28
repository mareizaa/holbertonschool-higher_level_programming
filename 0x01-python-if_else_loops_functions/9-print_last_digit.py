#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last = number % 10
        print('{:}'.format(last), end='')
        return last
    else:
        last = number % -10
        print('{:}'.format(last * -1), end='')
        return last * -1
