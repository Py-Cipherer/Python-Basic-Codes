def primetest(a):
    if a<2:
        return "Enter any greater value than 1."
    for i in range(2,int(a/2)+1):
        if a%i==0:
            return "Not a prime"
    return "It's a prime."
print(primetest(55))
print(primetest(67))
