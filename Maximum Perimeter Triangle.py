''' problem:
https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''

''' formula for degenerate triangles: https://www.quora.com/What-is-a-degenerate-triangle?share=1 '''

#Solution

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    sticks.sort()
    a=[]
    for i in range(len(sticks)-2):
        if sticks[i]+sticks[i+1]>sticks[i+2]:
            a.append(sticks[i:i+3])
    if not a:
        return ([-1])
    b=[sum(i) for i in a]
    return (a[(b.index(max(b)))])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
