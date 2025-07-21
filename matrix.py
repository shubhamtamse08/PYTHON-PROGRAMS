matrix=[
    [1,2,3,10]
    ,[4,5,6,20]
    ,[7,8,9,30]
]
rows=len(matrix)
cols=len(matrix[0])

top=0
botton=rows-1
left=0
right=cols-1

while(top<=botton and left<=right):
    for i in range(left,right):
        print(matrix[top][i],end=" ")
    top+=1

    for i in range(top,botton):
        print(matrix[i][right],end=" ")
    right-=1

    if(top<=botton):
        for i in range(right,left-1,-1):
            print(matrix[botton][i],end=" ")
        botton-=1
    if(left<=right):
        for i in range(botton,top-1,-1):
            print(matrix[i][left],end=" ")
        left+=1