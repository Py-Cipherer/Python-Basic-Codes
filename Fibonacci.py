"""
Fibonacci series is a series in which any term is the sum of its previous two terms.
[0,1,1,2,3,5,8,13,21,...................]
"""

#fibo() is a user defined non-parameterised-return-type function that returns the no. of terms of fibonacci series in a list.
def fibo():
    n=int(input("Enter limit="))
    if n==1:
        return [0]
    if n==2:
        return [0,1]
    L=[0,1]
    x=0
    y=1
    for i in range(3,n+1):
        s=x+y
        L.append(s)
        x=y
        y=s
    return L

print(fibo())
