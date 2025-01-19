def case_counter(s):
    if type(s)==str:
        up=0
        lo=0
        for i in s:
            if i.isupper():
                up+=1
            if i.islower():
                lo+=1
        return "No. of uppecase letters= ",up, "No. of lowercase letters= ",lo
    else:
        return "Only string values accepted."
print(case_counter("AlexNeverFailedCS"))

