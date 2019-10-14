#!/usr/bin/python3


def hourglass_sum(arr):
    largest_sum = None
    for rindex, row in enumerate(arr):
        for cindex, _ in enumerate(row):
            try:
                total = 0
                # top row
                total += sum(arr[rindex][cindex:cindex+3])
                # middle row
                total += arr[rindex+1][cindex+1]
                # bottom row
                total += sum(arr[rindex+2][cindex:cindex+3])
                if largest_sum == None:
                    largest_sum = total
                elif total > largest_sum:
                    largest_sum = total
            except IndexError:
                break
    return largest_sum


