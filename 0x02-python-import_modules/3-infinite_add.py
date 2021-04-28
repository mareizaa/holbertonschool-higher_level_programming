#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = (len(sys.argv))
    if len(sys.argv) == 1:
        print("0")
    else:
        res = 0
        for i in range(1, l):
            res = res + (int(sys.argv[i]))
        print("{:}".format(res))
