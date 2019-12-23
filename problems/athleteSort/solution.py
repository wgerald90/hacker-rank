#!/usr/bin/python3


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())

    ##################
    # code below
    sorted_table = sorted(arr,key = lambda x: x[k])
    for item in sorted_table:
        print(' '.join(str(i) for i in item)
