#Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
x=0
for i in tuple1:
    if i==50:
        x+=1
print(x)

#or

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))