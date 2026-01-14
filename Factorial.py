#Program to find the factorial of a number
num=int(input("Enter a number to find the factorial of: "))
if num<0:
    print("Factorial for negative numbers is undefined.")
elif num==0:
    print("Factorial of 0 is 1.")
else:
    product=1
    for i in range(1,num+1):
        product=product*i
        print("The factorial of",num,"is",product)
    




    























               
