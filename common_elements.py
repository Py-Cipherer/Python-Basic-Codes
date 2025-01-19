l1 = [1, 2, 3, 4, 5]
l2 = [3, 5, 7, 9, 11]

def common(l1,l2):
    l3=[]
    newl=l2.copy()
    for i in l1:
        for j in newl:
            if i==j:
                l3.append(i)
                newl.remove(j)
    return l3


def common_new(l1,l2):
    set_l2 = set(l2)
    c=[com for com in l1 if com in set_l2]
    return c

print(common(l1,l2))
print(common_new(l1,l2))
