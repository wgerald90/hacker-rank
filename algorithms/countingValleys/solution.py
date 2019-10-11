#!/usr/bin/python3
import sys

def init():
    arg1, arg2 = sys.argv[1:]
    return int(arg1), arg2


def countingValleys(n, s):
    seaLevel, valleys = 0, 0
    values = {"D": -1, "U": 1}
    
    for item in s:
        seaLevel += values[item]
        if seaLevel == 0 and item == "U":
            valleys += 1

    return valleys


if __name__ == '__main__':
    nsteps, data = init()

    nValleys = countingValleys(nsteps, data)
    print(nValleys)
