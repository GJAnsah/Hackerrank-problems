website: https://bit.ly/34ZyUyr
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
