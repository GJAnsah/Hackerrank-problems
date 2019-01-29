#Series of solved leetcode problems.

'''
1. Compute and return the square root of x, where x is guaranteed to be a non-negative integer. 
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
'''
class Solution:
    def mySqrt(self, x): 
        if x>=0:
            return(int(math.sqrt(x)))
            
            
#---------------------------------------------------------------------------------------
'''
2.Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution:
    def majorityElement(self, nums):
        for x in nums:
            if nums.count(x)>len(nums)/2:
                return x
      
#---------------------------------------------------------------------------------------
'''
3.Given a non-empty array of integers, every element appears twice except for one. Find that single one.
'''
class Solution:
    def singleNumber(self, nums):
        for x in nums:
            if nums.count(x)==1:
                return x
