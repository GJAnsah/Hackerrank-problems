#----Hacker Rank Challenge----https://goo.gl/vzhYfy

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
