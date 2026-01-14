n1=int(input("Enter limit of asterisks that can be printed: "))
s_n1=n1
x=1
while n1>0:
    print('*'*x)
    x+=1
    n1-=1

n2=s_n1-1

for i in range(n2,0,-1):
    print('*'*i)
