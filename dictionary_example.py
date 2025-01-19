def student_result():
    d={}
    n=int(input("Enter No. of values to enter= "))
    for i in range(n):
        print("Entry number ",i+1,":- ")
        nm=input("Enter name = ")
        roll=int(input("Enter roll no.= "))
        marks= int(input("Enter marks = "))
        d[roll]=[nm,marks]
    print([x for x in d.items()])
student_result()
