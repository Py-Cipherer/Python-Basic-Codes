def First_run_up(a,b,c,d,e):
    tup=(a,b,c,d,e)
    l=list(tup)
    b=len(l)
    for i in range(b-1):
        for j in range(b-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print("Original Tuple= ",tup)
    print("Sorted tuple= ",tuple(l))
    print("2nd Largest value= ",l[-2])
First_run_up(5,62,6,781,112)
