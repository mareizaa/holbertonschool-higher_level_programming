#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if (len(sys.argv) - 1) is not 3 or len(sys.argv) == 0:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    elif sys.argv[2] == '+':
        print("{:} + {:} = {:}".format(a, b, add(a, b)))
    elif sys.argv[2] == '-':
        print("{:} - {:} = {:}".format(a, b, sub(a, b)))
    elif sys.argv[2] == '*':
        print("{:} * {:} = {:}".format(a, b, mul(a, b)))
    elif sys.argv[2] == '/':
        print("{:} / {:} = {:}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
