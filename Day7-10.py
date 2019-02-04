#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.



class Solution(object):
    def generate(self, numRows):
        triangle=[]
        x=1
        for i in range(numRows):
            triangle.append([])
            for j in range (x):
                triangle[i].append(0)
            triangle[i][0]=1
            triangle[i][-1]=1
            for h in range (len(triangle[i])):
                if triangle[i][h]==0:
                    triangle[i][h]=triangle[i-1][h-1]+triangle[i-1][h]
            x+=1
        return(triangle)
