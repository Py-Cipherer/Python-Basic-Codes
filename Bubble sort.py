l=[12,75,8,36,4,98,52,14,]
def bubble_sort(l):
    for i in range(len(l)):
        for j in range(0,len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
print(bubble_sort(l))
