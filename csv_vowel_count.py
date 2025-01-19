def countvowel():
    f=open("C://Users//Administrator//Desktop//names.csv","r")
    r=f.read()
    print(r)
    c=0
    for i in r:
        if i in "aeiouAEIOU" :
            c+=1
    return "No. of vowels= ",c
print(countvowel())
