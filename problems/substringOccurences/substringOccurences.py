#!/usr/bin/python3

import sys


def init():
    arg1, arg2 = sys.argv[1:]
    if len(arg1) > len(arg2):
        string, substring = arg1, arg2
    else:
        string, substring = arg2, arg1

    return string, substring

def get_substring_occurences(string, substring):
    count = 0
    for index, char in enumerate(string):
        try:
            if char == substring[0] and string[index: (len(substring) + index)] == substring:
                count += 1
        except IndexError:
            break

    return count


if __name__ == '__main__':
    string, substring = init()
    nOccurences = get_substring_occurences(string, substring)
    print(nOccurences)
