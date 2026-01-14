#Reverse a list
list1=[100,200,300,400,500]
x=len(list1)
list2=[]
for i in range(x-1,-1,-1):
    list2.append(list1[i])
print(list2)
