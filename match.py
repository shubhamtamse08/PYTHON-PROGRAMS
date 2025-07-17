n=int(input("enter the numbers of team"))
teams=[]
matches=[]
for i in range(n):
    t=input("enter the team")
    teams.append(t)
meet=int(input("enter number of meeting"))
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(meet):
            matches.append([teams[i],teams[j]])
index=1
for i in matches:
    print("match {}:{} Vs {}".format(index,i[0],i[1]))
    index+=1
