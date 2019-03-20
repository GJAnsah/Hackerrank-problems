#----Hacker Rank Challenge
'''
https://goo.gl/vzhYfy
https://goo.gl/cNkTYu
'''

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
