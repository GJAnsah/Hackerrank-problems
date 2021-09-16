'''
https://www.hackerrank.com/challenges/priyanka-and-toys/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''

#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w,n):
    w.sort()
    m=0
    count=1
    for i in range(n):
        if w[i]>w[m]+4:
            count+=1
            m=i
    return(count)


if __name__ == '__main__':

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    print(toys(w,n))
