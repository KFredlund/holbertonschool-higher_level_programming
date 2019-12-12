#!/usr/bin/python3
from sys import argv
for i in range(0, len(argv)):
    if len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
        break
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(i + 1, argv[1]))
        break
    else:
        print("0 arguments.")
