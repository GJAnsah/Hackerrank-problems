'''
HackerRank Conditionals (Day 3 of 30 days of code)
Task 
Given an integer, n , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.
'''

def wierd_or_not(N):
    
    if N%2==1:                  #check if n is odd
        return ("Weird")
    else:
        if ((N>=2) & (N<=5))|(N>20): #check if n is an even number between 2 and 5 inclusive, or above 20
            return("Not Weird")
        else:
            return("Weird")

N = int(input())
print(wierd_or_not(N))
