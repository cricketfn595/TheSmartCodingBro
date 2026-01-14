#- Create a class Person with a default constructor that initializes name and age. Print an object’s attributes.
class Person:
    def __init__(self, name = "", age =0):
        self.name = name
        self.age = age

person1 = Person("Riku", 12)
print(person1.name)
print(person1.age)

