#- Implement a base class Animal with a speak() method and subclasses Dog and Cat with their own speak() implementations
class Animal:
    def speak(self):
        print("Hello!")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

Bruno = Dog()
Kitty = Cat()

for x in (Bruno, Kitty):
    x.speak()