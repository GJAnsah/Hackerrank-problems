'''
HACKERRANK CHALLENGE:https://goo.gl/zwk3Yj
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def reverse_array(arr):
    arr=arr[: :-1]
    return (" ".join(str(a) for a in arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(reverse_array(arr))
