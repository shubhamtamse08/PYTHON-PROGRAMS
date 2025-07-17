from datetime import datetime
a=input("enter first date")
b=input(("enter second date"))
d1=datetime.strptime(a,"%y-%m-%d")
d2=datetime.strptime(b,"%y-%m-%d")
diff=d2-d1
print(" Differnce",abs(diff.months),"days")
