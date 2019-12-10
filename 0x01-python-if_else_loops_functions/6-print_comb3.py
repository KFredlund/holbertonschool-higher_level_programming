#!/usr/bin/python3
for first in range(0, 10):
    for second in range(0, 10):
        if first < second:
            if first == 8 and second == 9:
                print("{:d}".format(89))
            else:
                print("{:d}{:d}".format(first, second), end=", ")
