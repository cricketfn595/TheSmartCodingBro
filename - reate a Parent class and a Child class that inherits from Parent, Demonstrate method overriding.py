#- Create a Parent class and a Child class that inherits from Parent. Demonstrate method overriding.

class Books:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def printfeatures(self):
        print("Name:", self.name, "Length:", self.length, )

class Dictionaries(Books):
    def __init__(self, no_of_words, language):
        self.no_of_words = no_of_words
        self.language = language

    def printattributes(self):
        print("No. of words:", self.no_of_words,",", "Languages:", self.language, )

d1 = Dictionaries(20000,"English")
d1.printattributes()