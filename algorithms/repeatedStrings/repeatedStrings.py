#!/usr/bin/python3


def init():
    arg1, arg2 = sys.argv[1:]
    try:
        depth = int(arg1)
        string = arg2
    except TypeError:
        string, depth = arg1, int(arg2)

    return string, depth


def repeatedString(s, n):
    subOccur = s.count("a")
    numberOfWholeStrings = int(n / len(s))
    remainder = n - (len(s) * numberOfWholeStrings)
    return (subOccur * numberOfWholeStrings) + s[:remainder].count("a")
    

if __name__ == '__main__':
    string, n = init()
    totalOccurences = repeatedString(string, n)
    print(totalOccurences)
