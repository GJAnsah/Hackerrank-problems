#Modified Day 2 program. The sum is of only multiples of 3
name = str.title(input("Enter your name to proceed: "))
userNum= int(input("\nHello, "+name+". \n\nEnter an integer and let me give you the sum of all multiples of 3 from 1 to your number.\nEnter your number here: "))

newList=[]
for x in range(1,userNum+1):
	if x%3==0:
		newList.append(x)

print(sum(newList))
