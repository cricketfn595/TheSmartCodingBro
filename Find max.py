import sys

list1=[15,13,12,20,17,21]
x=-sys.maxsize-1
y=-sys.maxsize-1
z=-sys.maxsize-1
t=-sys.maxsize-1
for i in list1:
    if i>x:
        t=z
        z=y
        y=x
        x=i
    elif i>y:
        t=z
        z=y
        y=i
    elif i>z:
        t=z
        z=i
    elif i>t:
        t=i
    print(x,y,z,t)