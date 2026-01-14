#Palindrome Checker
def check_palindrome(word):
    word=word.lower()
    reverseword=word[::-1]
    if reverseword==word:
        return "Yes"
    else:
        return "No"
    
Word=input("Enter a word: ")
print("Is the word a palindrome: ",check_palindrome(Word))
