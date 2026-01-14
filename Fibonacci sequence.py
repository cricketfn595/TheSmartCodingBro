#Program to print the Fibonacci sequence
c=0
p=1
pp=1

i=0

n=int(input("Enter the number of terms that should be printed in the Fibonacci sequence: "))
while i<n:
    print(c,end=' ')
    pp=p
    p=c
    c=pp+p
    i+=1

