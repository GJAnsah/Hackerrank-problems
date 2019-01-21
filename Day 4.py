#Multiples of numbers from 1 to 12
num=1
while a<13:
    for x in range(1,13):
        x=str(x)
        print (num ,"*", x, "=", num*int(x))
    num+=1
    print("\n")
