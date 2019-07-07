#!/usr/bin/env python3.6

import argparse

DOCUMENTATION = """

Problem Statement:
    Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares 
    has an integer on it. She decides to share a contiguous segment of the bar selected such that the 
    length of the segment matches Ron's birth month and the sum of the integers on the squares is 
    equal to his birth day. You must determine how many ways she can divide the chocolate.

    Considerthe chocolate bar as an array of squares, s = [2, 2, 1, 3, 2]. She wants to find segments 
    summing to Rons Birthday, d = 4 with a length equaling his birth month, m = 2. In this case there 
    are two segments meeting her criteria: [2, 2] and [1, 3].

Function Description:
    Complete the birthday function. It should return an integer denoting the number of ways lily can 
    divide the chocolate bar.
"""



def birthday(s, d, m):
    """
    args:
        s: {list: int}  numbers on each of the squares of chocolate.
        d: {int}        Rons Birthday
        m: {int}        Rons Birth Month
    """
    nways = 0
    for index, _ in enumerate(s):
        try:
            sublist = s[index: (index+m)]
            if sum(sublist) == d and len(sublist) == m:
                nways += 1
        except IndexError:
            break
    return nways


def init():
    parser = argparse.ArgumentParser()
    parser.add_argument("s", help="Array of integers denoting the numbers on the bar of chocolate")
    parser.add_argument("d", type=int, help="Birth day")
    parser.add_argument("m", type=int, help="Birth Month")

    return parser.parse_args()


if __name__ == '__main__':
    args= init()
    array = [int(i) for i in args.s]
    print(birthday(array, int(args.d), int(args.m)))
