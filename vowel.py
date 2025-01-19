s=input("Enter Any String= ")
n=""
for i in s:
    if i in "AEIOUaeiou":
        n=n+"@"
    else:
        n=n+i
print(s)
print(n)
