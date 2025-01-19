def contiguous(l):
    add=int(input("Enter the sum limit of subarray= "))
    li=[]
    final_li=[]
    for i in range(len(l)):
        c=0
        for j in range(i,len(l)):
            end=j
            k=l[j]
            c+=k
            if c>add:
                break
            if c==add:
                li.append((i,end))
    for i in li:
        start=i[0]
        khtm=i[1]+1
        sub=l[start:khtm]
        khtm2=khtm+(len(sub))
        subrev=l[khtm:khtm2]
        if sub==subrev[::-1]:
            final_li.append((start,khtm2-1))
            print("contiguous subarray= ",l[start:khtm2],end=" ")
            print("and its index= ",(start,khtm2-1))
    print("List of all indexes of contiguous subarrays= ",final_li)
l=[3, 1, 4, 2, 2, 4, 1, 3]
contiguous(l)
