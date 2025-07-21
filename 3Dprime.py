def prime(i):
    if(i==1):
        return False
    else:
        for j in range(i):
            if (i%j == 0):
                return False
            return True


def sod(i):
    d=list(str(i))
    x=sum([int(i) for i in d])
    if(prime(x)):
        return True
    else:
        return False


    while(i>0):
        d=i%10
        if( not prime(d)):
            return False
        i=i//10
    return True




for i in range(100,1000):
    if prime(i) and sod(i) and dig(i):
        print(i,end=" ")