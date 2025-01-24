"""
a word, phrase, or name formed by rearranging the letters of another, such as "scar", formed from "cars".
"""
a = ["listen", "silent", "enlist", "hello", "world", "lonely", "lone"] #-> sample list for input.

def sortString(str1):
    return ''.join(sorted(str1))

def isSubstring(str1, str2):        #Will check whether both sorted strings are either same or substring of other one. 
    return str1 in str2 or str2 in str1
    
def anagram(a):
    n=[]    #-> temp list for manipulation purpose
    final=[]    #-> final anagram words will be stored here.
    visited = []    #-> reference list for storing words visited during loop.

    for i in range(len(a)):
        temp = []
        for j in range(i+1,len(a)):
            #isAna will store the bool value whether true or false for the currently iterated word.
            isAna = isSubstring(sortString(a[i]),sortString(a[j])) or isSubstring(a[i],a[j])
            if (isAna == True):
                #if the iterated words are not in the visited and temp list, they get appended here.
                if (a[i] not in temp and a[i] not in visited):
                    temp.append(a[i])
                    visited.append(a[i])
                if (a[j] not in temp and a[j] not in visited):
                    temp.append(a[j])
                    visited.append(a[j])
        # if temp is not empty then it gets appended to final list.            
        if temp != []:
            final.append(temp)
    print(final)

anagram(a)
