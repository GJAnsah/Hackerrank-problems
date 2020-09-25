#Challenge:https://www.hackerrank.com/challenges/strange-advertising/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    x=2
    a=2
    for i in range (n-1):
        x=math.floor(x*1.5)
        a+=x
    return(a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
