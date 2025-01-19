
def prime(a):
    if a==2:
        return 2
    for i in range(2,int(a/2)+1):
        if a%i==0:
            break
    return a

def primelist(n):
    pl=[]
    for i in range(n):
        if prime(i):
            pl.append(i)
    return pl

def factorlist():
    n=int(input("Enter number to find it's factors= "))
    l=[]
    for i in (primelist(n)):
        if n%i==0:
            l.append(i)
    return l

print(factorlist())