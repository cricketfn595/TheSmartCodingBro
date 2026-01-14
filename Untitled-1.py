try:
    x = float(input("Enter a number: "))
    x*=2
except ValueError:
    print("Error! Please enter a number")
else:
    print(x)
finally:
    print("Done!")

