#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    hidden = dir(hidden_4)
    for i in range(0, len(hidden)):
        if hidden[i][0] != '_':
            print("{:}".format(hidden[i]))
