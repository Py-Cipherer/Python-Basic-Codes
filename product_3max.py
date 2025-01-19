lis=[11,45,34,26,90,37,12]
def prod(l):
    li=[]
    for a in l:
        if a not in li:
            li.append(a)
    for i in range(len(li)-1,0,-1):
        for j in range(i):
            if li[j]>li[j+1]:
                t=li[j]
                li[j]=li[j+1]
                li[j+1]=t
    p=(li[-1]*li[-2])*li[-3]
    print("product= ",p)
    return "UPDATED LIST= ",li
print(prod(lis))
