def RomanTranslator(s):
    #initialising the values of roman numerals in a dictionary.
    roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    value=0
    #setting an iteration loop on Roman numeral.
    for i in range(0,len(s)):
        if i==len(s)-1:
            value+=roman[s[-1]]
        elif roman[s[i]]>roman[s[i+1]]:
            value+=roman[s[i]]
        elif roman[s[i]]<roman[s[i+1]]:
            value-=roman[s[i]]
    return value

print(RomanTranslator("MMMDCCXC"))
