try:
    num1=int(input("Enter any value: "))
    num2=int(input("Enter any value: "))
    num3=num1//num2
    print("The quotient is= ",num3)
except NameError:print("Variable not present.")
except ZeroDivisionError:print("Division by zero not allowed.")
else:
    if num3%2==0:
        raise ValueError ("You should not get an even number.")
    else:
        print("Congo!!,You got an odd number")
