#!/usr/bin/env python3
import sys

HELP = """
jumpingOnTheClouds [-d] [ARRAY_LENGTH] [ARRAY]

Given an array of 1's and 0's return the shortest path

"""

DEBUG = False

def debug(*args):
    if DEBUG:
        print(args[:])


def jumpingOnClouds(arr):
    arr = [int(i) for i in arr]
    jumped, nJumps = False, 0
    for index, i in enumerate(arr):
        if index != 0:
            if i == 0:
                if jumped:
                    nJumps += 1
                    jumped = False
                else:
                    if len(arr) - 1 == index:
                        nJumps += 1
                    jumped = True
            elif i == 1:
                if jumped:
                    nJumps += 1
                else:
                    jumped = True

    return nJumps

def init():
    try:
        nArgs = len(sys.argv[1:])
        if nArgs <= 1:
            print(HELP)
            sys.exit(1)
    except IndexError:
        print(HELP)
        sys.exit(1)

    if nArgs == 3:
        return sys.argv[1], sys.argv[2], sys.argv[3]

    # array_length, array
    return sys.argv[1], sys.argv[2]

if __name__ == '__main__':
    args = init()

    if len(args) == 3:
        DEBUG = True
        arrayLength, array = args[1], args[2]
    else:
        arrayLength, array = args[0], args[1]

    nJumps = jumpingOnClouds(array.split(" "))

    print(nJumps)