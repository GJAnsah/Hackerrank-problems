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
        
        
        
        
 '''
 HackerRank big sum: https://goo.gl/5a1Qtj
 '''
#solution
def aVeryBigSum(count,ar):
    result = 0
    i=0
    while i<count:
        result+=ar[i]
        i+=1 
    return (result)


if __name__ =='__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar_count,ar)


    print(result)
