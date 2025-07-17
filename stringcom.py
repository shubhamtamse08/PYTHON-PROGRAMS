ben="aaabbcccccaa"
c=1
res=""

for i in range(len(ben) ):
    if(ben[i]==ben(i+1)):
        c=c+1
    else:
        res=res+ben[i]
        res=res+str(c)
        c=1
print(res)
