def majority(l):
    d={}
    for i in l:
        c=l.count(i)
        d[i]=[c]
    m=(max(list(zip(d.values(),d.keys())))[1])
    mv=(max(list(zip(d.values(),d.keys())))[0])[0]
    if (mv)>(len(l)/2) or (mv)==(len(l)/2):
        print(m,"is the majority number.")
    else:
        print("No match found.")   
li=[1,1,1,1,1,1,12,2,2,2]
majority(li)
