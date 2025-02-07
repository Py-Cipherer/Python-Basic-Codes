"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace
the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
* "ncyabciiuscygc" => ['nc', 'ya', 'bc', 'ii', 'us', 'cy', 'gc']

"""

def pair_maker():
    s=int(input("Enter any string= "))
    l=[]
    while(len(s)>=2):
        l.append(s[0:2])
        s=s[2:]
    if (len(s)==1):
        s+="_"
        l.append(s)
    return l
print(pair_maker())
