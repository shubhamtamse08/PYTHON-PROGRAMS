names=["A","B","C","D","E","F","G","H","I","J",]
meno=[0,1,1,1,2,2,1,2,1,2]
salary=[1000,2000,3000,4500,2000,5000,1500,2300,1300,1100]
removed=[]
removed2=[]


data=list(zip(salary,meno,names))
for i in data:
    if i[0]>4000:
        removed.append(i)

remaining=[i for i in data if i[0]<4000]

a.sorted(remaining,key=lambda x:x[0],reverse=True)
index=0
for i in a:
    if i[1]>=2:
        removed2.append(i)
    if(len(removed2>3)):
        break
final=removed+removed2

for i in final:
    print("{}.{} : Meno{} : salary{}".format(index,i[2],i[1],i[0]))
    index+=1





