#----Hacker Rank Array challenge : shorturl.at/egrw5


if __name__ == '__main__':
    a= []

    for _ in range(6):
        a.append(list(map(int, input().rstrip().split())))

hourGlassSums=[]
total=[]  
x=0
i=0
count=0
while count<4:
    for j in range(x,x+4):
        if(x+3)<7:
            total.append(a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2])
            if(len(total)==4):
                hourGlassSums+=total
                total=[]
                i+=1
                x=0
            else:
                x+=1 
    count+=1
print(max(hourGlassSums))
