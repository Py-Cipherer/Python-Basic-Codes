n=11
for i in range(n,0,-2):
    for space in range((n-i)//2):
        print(" ",end="")
    for j in range(i):
        print("$",end="")
    for space in range ((n-i)//2):
        print(" ",end="")
    print()
for a in range(1,n+1,2):
    if a==1:
        continue
    for space in range((n-a)//2):
        print(" ",end="")
    for j in range(a):
        print("$",end="")
    for space in range ((n-a)//2):
        print(" ",end="")
    print()