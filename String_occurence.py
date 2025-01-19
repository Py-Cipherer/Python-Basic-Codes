def Occurence():
    A=input("Enter String= ")
    S=""
    for i in A:
        c=0
        for j in A:
            if i==j:
                c+=1
        if i not in S:
            print(i,"has occured ",c,"times in inputted string.")
        S+=i
Occurence()
