#!/bin/python3

import math


# Complete the encryption function below.
def encryption(s):
    sqrt = math.sqrt(len(s))
    columns = math.ceil(sqrt)
    
    starting_point, last = 0, 0
    answer = ""
    for i in range(len(s)):
        if i == 0:
            answer += s[i]
        else:
            calc = last + int(columns)
            if calc > len(s)-1:
                starting_point += 1
                last = starting_point
                answer += " {}".format(s[last])
            else:
                last = calc
                answer += s[last]
    
    return answer

