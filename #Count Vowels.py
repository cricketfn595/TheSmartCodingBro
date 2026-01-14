#Count Vowels
def countvowels(string):
    no_of_vowels=0
    for i in string.lower():
        if i in "aeiou":
            no_of_vowels+=1
        else:
            continue
    return no_of_vowels

String=input("Enter the string: ")
print("The number of vowels in the tring is: ",countvowels(String))
