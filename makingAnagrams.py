'''
https://www.hackerrank.com/challenges/making-anagrams/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    minDel=0
    s3=set(s1+s2)
    for alphabet in s3:
        minDel+=abs(s1.count(alphabet)-s2.count(alphabet))
    return (minDel)
        
s1 = input()
s2 = input()

print(makingAnagrams(s1, s2))
