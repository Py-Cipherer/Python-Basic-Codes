s='abba'
def palindrome_str_counter(s):
    c=0
    for i in range(int(len(s)/2)):
        for j in range(len(s),0,-1):
            st=s[i:j]
            if st==st[::-1] and st!='':
                c+=1
                print(st)
    return c
print(palindrome_str_counter(s))
