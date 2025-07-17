import random
name1=input("player1")
name2=input("player2")
print("comp has fixed 5 nums")
print("you guys have to guess it")

num=[]
while(len(num!=5)):
    d=random.randint(1,10)
    if(d not in num):
        num.append(d)

print("-----------")

s1=0
s2=0
player1=[]
player2=[]
for i in range(3):
    print("------ROUND-------".format(i+1))
    print("Dear {} guss ur choice ".format(name1))
    ch=int(input())
    while(ch in player1 or ch in player2):
        ch=int(input("it is already taken choose anyother"))
    player1.append(ch)
    if(ch in num):
        print("----> correct")
        s1=s1+1
    else:
        print("---->wrong")

    print("Dear {} guss ur choice ".format(name2))
    ch = int(input())
    while (ch in player1 or ch in player2):
        ch = int(input("it is already taken choose anyother"))
    player1.append(ch)
    if (ch in num):
        print("----> correct")
        s1 = s1 + 1
    else:
        print("---->wrong")

print("------------")
print("let ")
print()
