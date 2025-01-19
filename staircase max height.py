#staircase max height
blocks=125

def height(n):
    c=0
    s=0
    for steps in range(1,n+1):
        s+=steps
        if s<=n:
            c+=1
        else:
            return c
n=height(blocks)
print("Max Height= ",n)
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

