#Check Even or Odd
def is_even(n):
    return True if n%2==0 else False

N=int(input("Enter an integer: "))
print("Integer is even: ",is_even(N))