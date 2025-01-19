def palindrome(a):
    s=str(a)
    if (a>10) and (s==s[::-1]):
        return "This number is a palindrome."
    else:
        return "This number is not a palindrome."
print(palindrome(11))
print(palindrome(23))
