'''
HACKERRANK CHALLENGES
    https://goo.gl/zwk3Yj
    https://goo.gl/5gwabg
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#-------------SOLUTIONS-----------
#1
def reverse_array(arr):
    arr=arr[: :-1]
    return (" ".join(str(a) for a in arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(reverse_array(arr))
    
#------------------------------------------------
#2
def plusMinus(arr):
    positive=negative=zero=0
    for a in arr:
        if a>0:
            positive+=1
        elif a<0:
            negative+=1
        else:
            zero+=1
    positive/=len(arr)
    negative/=len(arr)
    zero/=len(arr)
    return([positive,negative,zero])
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    count=plusMinus(arr)
    for a in count:
        print (a)
