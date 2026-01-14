print("This is the Collatz conjecture sequence finder")
n=int(input("Enter a number: "))
print(n)
if n>0:
    if n==1:
        print("Enter a number other than 1")
    while n>1:
        if n%2==0:
            n=n/2
            print(n)
        else:
            n=3*n+1
            print(n)
