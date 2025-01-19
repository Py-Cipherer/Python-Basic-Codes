s='Saloni   is  Dabbu'
def str_rev(s):
    st=''
    c=0
    for i in s.split():
        if c>0:
            for j in range(c):
                st+=' '
        st+=i[::-1]
        c=c*0
        for k in (s[len(st):len(s)]):
            if k.isspace():
                c+=1
            else:
                break
    print(st)
str_rev(s)
