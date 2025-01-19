def tribonacci(signature,n):
    if n>0:
        if n>=3:
            for i in range(3,n):
                signature.append(sum(signature[i-3:i+1]))
            return signature
        return signature[0:n]
    return "Enter a positive number."
print(tribonacci([1,1,1],10))
