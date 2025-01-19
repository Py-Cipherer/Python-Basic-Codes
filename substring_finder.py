def count_occurence(slist,substr):
    c=0
    for i in slist:
        if (substr.lower()) in (i.lower()):
            c+=1
            print(i)
    return "Occurence= ",c
st=["apple", "banana", "Orange", "orange juice", "apple pie", "banana split"]
sub="orange"
print(count_occurence(st,sub))
