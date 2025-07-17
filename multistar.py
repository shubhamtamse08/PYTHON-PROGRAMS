b=int(input("enter the numbers of block"))
l=int(input("enter numbers of lines"))
s=int(input("enter numbers of star"))
sum=0

for i in range(b):
    print(f"-----{i+1}------")
    count=0
    for j in range(l-i):
        for k in range(s):
            print("*",end="")
            count=count+1
        print()
    print(count)
    sum+=count
print(f"total{sum}")
