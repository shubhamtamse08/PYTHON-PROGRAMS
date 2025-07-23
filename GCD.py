a=int(input("enter a"))
b=int(input("enter b"))
c=0
while(b!=0):
    c=a%b
    a=b
    b=c
print(a)
