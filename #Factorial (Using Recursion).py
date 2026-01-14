#Factorial (Using Recursion)
def facto(n):
    factprod=1
    if n==0:
        return factprod
    else:
        factprod*=n
        return factprod*facto(n-1)
    
N=int(input("Enter an integer: "))
print("The factorial of",N,"is",facto(N))
