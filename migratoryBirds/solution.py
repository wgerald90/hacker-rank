#!/usr/bin/env  python3
import sys
from collections import OrderedDict

HELP = """
solution.py -d[DEBUG] [ARRAY_SIZE] [ARRAY]

"""

DEBUG = False

def debug(*args):
    if DEBUG:
        print(args[:])


def migratoryBirds(arr):
    # get a copy of the array
    arr = [int(i) for i in arr.split(" ")]
    setOfTypes = set(arr[:])
    birds  = {k: 0 for k in setOfTypes}
    for bird in arr:
        birds[bird] += 1

    debug(f"birds dictionary: {[(k, v)  for k, v in birds.items()]}")

    bird, count = 0, 0
    for k, v in birds.items():
        debug(k, v)
        if bird == 0:
            bird, count = k, v
        else:
            if v > count:
                bird, count = k, v
            if v >= count and k < bird:
                bird, count = k, v

        debug(f'Bird: {bird}\nCount: {count}')
    return bird

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 2:
        print(HELP)
        sys.exit(1)

    if len(args) == 3:
        DEBUG = True
        args = args[1:]

    array_size = args[0]
    array = args[1]

    print(migratoryBirds(array))