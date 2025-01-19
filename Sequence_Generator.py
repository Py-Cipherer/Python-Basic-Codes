def sequence(n):
    alph="0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n>26:
        n=n%26
    if n==0:
        seq=(alph[26]*26)
    else:
        seq=(alph[n]*n)+alph[n+1::]
    return seq
print(sequence(392366))