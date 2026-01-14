#- Prompt the user for two numbers and divide them. Handle both ValueError (invalid input) and ZeroDivisionError.
try:
    try:
        str1 = input("Enter a number: ")
        str2 = input("Enter another number: ")
        num1 = int(str1)
        num2 = int(str2)
    except ValueError:
        print("Invalid input. Please enter numbers.")

    res = num1/num2
except ZeroDivisionError:
    print("Error! Cannot divide by 0")
else:
    print(res)
