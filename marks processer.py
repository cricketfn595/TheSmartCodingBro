#Program to accept marks of 5 subjects, print average and percentage
print("This is the marks processer.")
tm=int(input("Enter the total marks: "))
s=0
for i in range(5):
    i=float(input("Enter an exam's marks: "))
    p=(i/tm)*100
    s+=i
    print("The percentage you got in this exam is",p,"%")

avg=s/5
print("The average marks you got is",avg)


