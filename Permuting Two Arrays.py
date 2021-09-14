'''
https://www.hackerrank.com/challenges/two-arrays/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B

def twoArrays(k, A, B):
    A.sort(reverse=True)
    B.sort()
    
    sums=[x+y for x,y in zip(A,B)]
    
    if all(ele >=k  for ele in sums):
        return ('YES')
    else:
        return ('NO')
    


q = int(input().strip())

for q_itr in range(q):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))
    
    print(twoArrays(k, A, B))

