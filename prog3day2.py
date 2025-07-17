import time
s=input("enter sentence")
c=0
for i in range(len(s)):
    if (s[i]==" " and s[i+1]!=" "):
        c=c+1
time.sleep(2)
print("number of words in sentence",c+1)       