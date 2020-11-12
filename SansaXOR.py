#website: https://www.hackerrank.com/challenges/sansa-and-xor/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&isFullScreen=true

#solution


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sansaXor function below.
def sansaXor(arr,n):
    x=0
    if n%2==0:
        return x
    else:
        for i in range(n):
            if i%2==0:
                x=x^arr[i]
        return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr,n)

        fptr.write(str(result) + '\n')

    fptr.close()
