#Implement __str__ and __repr__ in a Book class to format output nicely.
class Books:
    def __init__(self, name, type, author):
        self.name = name
        self.type = type
        self.author = author

    def __str__(self):
        return f"{self.name} is a {self.type} by {self.author}"

    def __repr__(self):
        return f"Books({self.name}, {self.type}, {self.author})"

b1 = Books("The Room On The Roof", "Novel","Ruskin Bond" )
print(str(b1))
print(repr(b1))  
