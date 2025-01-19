for i in range(6):
    for j in range(i):
        if j%2==0:
            print("@",end="")
        else:
            print("#",end="")
    print()
