'''
Author AvmnuSng
Difficulty Easy

HackerRank Loop Challenge: https://goo.gl/MtUAaN

Task 
Given an integer,n, print its first 10 multiples in the form: n x i = result, where i is an integer between 1 and 10 inclusive.
'''

#Solution
if __name__ == '__main__':
    n = int(input())
    for i in range(1,11,1):
        print(n,"x",i,"=",n*i)
