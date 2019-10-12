# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    output, count = dict(), 0
    n = list(range(n))
    while len(n)-1 >= 0:
        index = n.pop(0)
        for i , v in enumerate(ar):
            if index != i and i >= index:
                if (v+ ar[index]) % k == 0:
                    try:
                        if i not in output[index]:
                            output[index].append(i)
                            count += 1
                    except KeyError:
                        output[index] = [i]
                        count += 1
    return count