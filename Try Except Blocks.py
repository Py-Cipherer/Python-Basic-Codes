#Sample code to raise custom Error Messages while Expection Handling.
try:       #write the code in try block in which we want to find/handle the errors.
    num1=int(input("Enter any value: "))
    num2=int(input("Enter any value: "))
    num3=num1//num2
    print("The quotient is= ",num3)
#Except block is used to handle predefined Errors in Python.
except NameError:print("Variable not present.")
# "NameError" is one of Predefined Errors in Python that occurs when no such variable name is found.
except ZeroDivisionError:print("Division by zero not allowed.")
else:
    if num3%2==0:
        raise ValueError ("You should not get an even number.") 
        # "Raise" is used to raise or return Error statements without interruption in code execution.
        #Here ValueError is a custom error msg for this code according to the code logic.
    else:
        print("Congo!!,You got an odd number")
