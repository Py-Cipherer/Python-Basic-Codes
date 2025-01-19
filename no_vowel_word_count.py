def no_vowel_count():
    f=open("C://Users//Administrator//Desktop//story11.txt","r")
    d=f.read()
    c=0
    for i in (d.split()):
        i=i.lower()
        if "a" in i or "e" in i or "i" in i or "o" in i or "u" in i:
            continue
        c+=1
    return "No. of non vowel words= ",c
print(no_vowel_count())
