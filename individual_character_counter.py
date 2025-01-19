def character(s):
    a=''
    for i in range(len(s)):
        c=0
        for j in s:
            if s[i]==j:
                c+=1
        print("Repetition of ",s[i],"=",c)
s=input("Enter any string= ")
character(s)
