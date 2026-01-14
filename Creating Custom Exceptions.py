class InvalidAgeError(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
    
def process_age(age):
    if age<0 or age>120:
        raise InvalidAgeError("Age must be between the inclusive range of 0 and 120!")
    else:
        print("Valid input!")
    
process_age(int(input("Enter an age: ")))