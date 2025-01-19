def fibo(n):
    L=[0,1]
    x=0
    y=1
    for i in range(3,n+1):
        s=x+y
        L.append(s)
        x=y
        y=s
    return L
