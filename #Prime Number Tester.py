#Prime Number Tester
import math
def prime_number_checker(n):
    toggler=""
    for i in range(2,math.trunc(math.sqrt(n))+1):
        if n%i==0:
            return "Not Prime"
            toggler="Yes"
        else:
            continue
        
    if toggler != "Yes":
        return "Prime"
    
N=int(input("Enter a number: "))
print("Is the number prime: ",prime_number_checker(N))
