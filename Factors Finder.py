"""
Finding factors of given number such as :-
12=[1,2,3,4,6]
22=[1,2,11]

"""
#user defined non-parameterised-with-return-type function to find factors.
def factorlist():
    n=int(input("Enter number to find it's factors= "))
    if n==0:
        return "0 has infinite factors."
    l=[]
    for i in range(1,int(n/2)+1):                    #<--loop will iterate till half of the number.
        if n%i==0:
            l.append(i)
    return l

print(factorlist())                                  #calling the function and printing its returned value.
