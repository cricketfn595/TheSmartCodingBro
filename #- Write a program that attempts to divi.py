#- Write a program that attempts to divide a number by zero and catches the ZeroDivisionError
x = int(input("Enter a number: "))
try:
    y = x/0
except ZeroDivisionError:
    print("Error! -  Division by 0 is undefined")

else:
    print("Result: ", y)


