'''
Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        x=str(x)        #cast from integer to string
        if x[0]=='-':
            x=x[1::1]   #cutting out '-'
            x=x[::-1]   #reversing string
            x=int(x)
            x=0-x
        else:
            x=x[::-1]
            x=int(x)
        if x>2**31-1:
            return 0
        elif x<-2**31:
            return 0
        else:
            return x
