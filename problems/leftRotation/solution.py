#!/usr/bin/python3


def rotate(arr, num_rot, size):
    lyst = arr[:]
    for index, value in enumerate(arr):
        new_index = index - num_rot
        lyst[new_index] = value
    return lyst



if __name__ == '__main__':
    args = input().split()
    size = int(args[0])
    num_rot = int(args[1])
    arr = list(map(int, input().rstrip().split()))

    [print(i, end = " ") for i in rotate(arr, num_rot, size)]
