def fact(n):
    s=""
    c=1
    l=[i for i in range(1,n+1)]
    for j in l:
        s+=str(j)+"x"
        c=c*j
    print(s,"1 =",c)
(fact(6))