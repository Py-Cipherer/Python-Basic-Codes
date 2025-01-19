def multiple():
    t=()
    for i in range(1,11):
        m=n*i
        t+=(m,)
    print(t)
n=int(input("Enter number to find multiples= "))
multiple()
