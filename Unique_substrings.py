s = "abc"
def unique_substrings(s):
    sub=[]
    for i in range(len(s)+1):
        for j in range(i):
            sliced=s[j:i]
            if sliced not in sub:
                sub.append(sliced)
    return "Unique substrings are = ",sub


print(unique_substrings(s))
