
Website: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/copy-from/135670262

import math
import os
import random
import re
import sys
    


n = int(input())

scores = list(map(int, input().rstrip().split()))

count_min=0
count_max=0
mini=scores[0]
maxi=scores[0]
for i in range (1,n):
    if scores[i]<mini:
        mini=scores[i]
        count_min+=1
    elif scores[i]>maxi:
        maxi=scores[i]
        count_max+=1
    else:
        continue
print (*[count_max,count_min])
