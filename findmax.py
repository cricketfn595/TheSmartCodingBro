list1=[5,3,2,10,7,11]
x=list1[0]
y=list1[0]
for i in list1:
    if i>x:
        y=x
        x=i
    elif i>y:
        y=i

print(y)