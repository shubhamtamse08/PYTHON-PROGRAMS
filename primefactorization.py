def primefact(n):
    i=2
    while(n%i!=0):
        i=i+1
    print(i, end=' ')
    primefact(n//i)




n=int(input("Enter a number: "))
primefact(n)