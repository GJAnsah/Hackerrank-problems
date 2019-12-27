task:https://www.hackerrank.com/challenges/library-fine/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign&isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys


d1M1Y1 = input().split()

d1 = int(d1M1Y1[0])

m1 = int(d1M1Y1[1])

y1 = int(d1M1Y1[2])

d2M2Y2 = input().split()

d2 = int(d2M2Y2[0])

m2 = int(d2M2Y2[1])

y2 = int(d2M2Y2[2])

if y1<y2:
    print (0)
elif y1>y2:
    print(10000)
else:
    if m1>m2:
        print(500*(m1-m2))
    elif m1<m2:
        print (0)
    else:
        if d1<d2:
            print(0)
        elif d1>d2:
            print(15*(d1-d2))
        else:
            print(0)
    
