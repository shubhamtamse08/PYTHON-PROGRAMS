rows=int(input("enter the rows"))
num=1
for i in range(1,rows+1):
    if(i%2==1):
        for j in range(1,i+1):
            print(num,end=" ")
            if(j<i):
                print("*",end=" ")
            num=num+1
    else:
        temp=num+i-1
        for j in range(1,i+1):
            print(temp,end=" ")
            if(j<i):
                print("*",end=" ")
            temp=temp-1
            num=num+1
    print()
