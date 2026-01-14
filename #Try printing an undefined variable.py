#Try printing an undefined variable. Catch the exception and print a custom message.
try:
    print(x)
except NameError:
    print("Error! This variable is not defined.")