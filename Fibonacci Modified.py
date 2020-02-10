https://www.hackerrank.com/challenges/fibonacci-modified/submissions/code/142077993

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    seq = [t1,t2]
    if n==1:
        return (t1)
    elif n<=2:
        return (t2)
    else:
        for i in range (2,n):
            seq.append(seq[i-2]+(seq[i-1]*seq[i-1]))
    return (seq[n-1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
