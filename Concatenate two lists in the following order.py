#Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res=[]
for i in list2:
    for j in list1:
        res.append(j+i)
print(res)
