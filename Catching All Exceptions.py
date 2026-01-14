def divide(x,y):
    try:
        res=x/y
        print(res)
    except Exception as e:
        print("Error: ",e)

x=float(input("Enter a number: "))
y=float(input("Enter another number: "))
divide(x,y)