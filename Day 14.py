'''
HACKERRANK CHALLENGE:https://www.hackerrank.com/challenges/30-arrays/problem?h_r=email&unlock_token=4ed89be48f0e732068fc31bce053fe7810d7aab4&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
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
