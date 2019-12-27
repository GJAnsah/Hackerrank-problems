https://www.hackerrank.com/challenges/the-hurdle-race/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=30-day-campaign&isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys


nk = input().split()

n = int(nk[0])

k = int(nk[1])

height = list(map(int, input().rstrip().split()))

if max(height)>k:
    print (max(height)-k)
else:
    print(0)
