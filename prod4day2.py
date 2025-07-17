h=int(input("enter numbers of heads"))
l=int(input("enter numbers of legs"))
flag=False
for hen in range(h):
    cow=h-hen
    if(cow*4 + hen*2 == l):
        print("cows",cow)
        print("hens",hen)
        flag=True
        break
if(not flag):
    print("No solution")
    
        
        

