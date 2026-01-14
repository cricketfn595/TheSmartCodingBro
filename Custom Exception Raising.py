def checkpos(num):
    try:
        if num<0:
            raise ValueError("Entered number is negative!")
        else:
            print("Valid input")
    except ValueError as ve:
        print("Error: ",ve)

num=int(input("Enter a number: "))
checkpos(num)
         