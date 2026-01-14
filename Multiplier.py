n=int(input("Enter a number of even numbers: "))

s=0

for i in range(1,n*2+1):
    if i%2==0:
        s=s+i

print(s)
