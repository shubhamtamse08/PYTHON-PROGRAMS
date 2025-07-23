a=int(input("enter a"))
b=int(input("enter b"))
if(a>b):
    big=a
else:
    big=b

step=big
while True:
    if(big%a==0 and big%b==0):
        print(big)
    else:
        big=big+1