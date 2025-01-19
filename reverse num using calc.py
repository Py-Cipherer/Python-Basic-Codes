def revNum(num):
    rev=0
    rem=0
    while num>0:
        print("num=",num)
        rem=num%10
        print("rem",rem)
        rev=rev*10+rem
        print("rev",rev)
        num=num//10
        print("finalnum=",num)
    return rev
print(revNum(1234))
