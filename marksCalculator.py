def calculate_marks():
    a=input("Enter Student's Name= ")
    eng=int(input("Enter english marks= "))
    math=int(input("Enter maths marks= "))
    chem=int(input("Enter chemistry marks= "))
    phy=int(input("Enter physics marks= "))
    comp=int(input("Enter computer marks= "))
    print(a,"has scored:\n",eng,"in English\n",math,"in Mathematics\n",chem,"in Chemistry\n",phy,"in Physics\n",comp,"in Computer")
    mTotal=eng+math+chem+phy+comp
    print("Total marks obtained= ",mTotal)
    p=(mTotal/5)
    print("Percentage scored= ",p)
    if p>=90:
        print("Grade: A")
    if (90>p>=80):
        print("Grade: B")
    if (80>p>=70):
        print("Grade: C")
    if (70>p>=60):
        print("Grade: D")
    if (60>p>=50):
        print("Grade: E")
    if (p<40):
        print("Grade: RETEST")
calculate_marks()
