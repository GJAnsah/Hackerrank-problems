#Modified Day 2 program. The sum is of only multiples of 3
newList=[]
print(newList)
for x in range(1,16):
	if x%3==0:
		newList.append(x)
print (newList)
print(sum(newList))
