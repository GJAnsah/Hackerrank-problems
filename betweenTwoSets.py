https://www.hackerrank.com/challenges/between-two-sets/problem

#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

r=[]
for i in range (1,101):
    if all(i%x==0 for x in a):
        if all(y%i==0 for y in b):
            r.append(i)
print(len(r))
