
a = ["listen", "silent", "enlist", "hello", "world", "lonely", "lone"]
def anagram(a):
    n=[]
    final=[]
    visited = []

    for i in range(len(a)):
        temp = []
        for j in range(i+1,len(a)):
            
            isAna = isSubstring(sortString(a[i]),sortString(a[j])) or isSubstring(a[i],a[j])
            if (isAna == True):
                if (a[i] not in temp and a[i] not in visited):
                    temp.append(a[i])
                    visited.append(a[i])
                if (a[j] not in temp and a[j] not in visited):
                    temp.append(a[j])
                    visited.append(a[j])
                    
        if temp != []:
            final.append(temp)

    print(final)

def sortString(str1):
    return ''.join(sorted(str1))

def isSubstring(str1, str2):
    return str1 in str2 or str2 in str1

anagram(a)
