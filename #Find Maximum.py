#Find Maximum
def findmax(Largelist):
    largest=0
    for i in Largelist:
        if i>largest:
            largest=i
        else:
            continue
    return largest

Largelist=eval(input("Enter a list of three numbers: "))
print("The largest number is: ",findmax(Largelist))