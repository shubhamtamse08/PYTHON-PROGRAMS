a=[10,20,"sahil","om",232,22,34,"anuj",20,34,"rock"]
a1=[]
a2=[]
a3=[]
for i in a:
    if(type(i)==str):
        a3.append(i)
    elif(i%2==1):
        a1.append(i)
    elif(i%2==0):
        a2.append(i)

    a1.sort()
    a2.sort()
    a3.sort()
print(a1+a2+a3)