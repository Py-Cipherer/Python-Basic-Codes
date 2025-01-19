l=[12,75,8,36,4,98,52,14]
def insertion_sort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and key < l[j]:
               l[j+1]=l[j]
               j=j-1
        else:
            l[j+1]=key
    return l
print(insertion_sort(l))
