#Copy specific elements from one tuple to a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
list1=[]
for i in tuple1:
    if i==44 or i==55:
       list1.append(i)
print(list1)

