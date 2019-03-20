#----Hacker Rank Challenge
'''
https://goo.gl/vzhYfy
https://goo.gl/cNkTYu
https://goo.gl/1419Tu
https://goo.gl/wjEkFm
'''

#----------------------------------------------------------------------------------------------------------------------------------------
from sys import stdin

def query(dict,key):
    if key in dict.keys(): 
        print(key,"=",dict[key],sep="") 
    else: 
        print("Not found")


phonebook={}
no_of_entries=int(input())
for x in range(no_of_entries):
    entry=input()
    entry=list(entry.split(" "))
    phonebook[entry[0]]=entry[1]


 
lines = stdin.read().splitlines() 
for name in lines:
    query(phonebook,name)

    
#-----------------------------------------------------------------------------------------------------------------------
def staircase(n):
    for x in range(1,n+1):
        stair="#"*x
        print(stair.rjust(n))

if __name__ == '__main__':
    n = int(input())
    staircase(n)
    
#--------------------------------------------------------------------------------------------------------------------
def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return (n*factorial(n-1))
    
n = int(input())
print(factorial(n))

#---------------------------------------------------------------------------------------------------------------------------------
n = str(bin(int(input())))
n=n.strip("0b")
n=n.split("0")
print(len(max(n)))
