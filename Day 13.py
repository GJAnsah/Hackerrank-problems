'''
Hacker Rank Challenge: https://www.hackerrank.com/challenges/diagonal-difference/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''

#Solution
import math
import os
import random
import re
import sys

#diagonalDifference function
def diagonalDifference(arr,n):
    p=0
    q=0
    for a in range(n):
        p+=arr[a][a]
    for a in range(0,n,1):
        q+=arr[a][n-1]
        n-=1
        if n<0:
            break
    return (abs(q-p))

#main program here
n = int(input())

arr = []

for _ in range(n):
     arr.append(list(map(int, input().rstrip().split())))

print(diagonalDifference(arr,n))
