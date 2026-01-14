#- Define a class Employee with a class variable company_name and instance variables name and salary. Demonstrate the difference between class and instance variables.
class Employee:
    company_name = "Renewo"

    def __init__(self, name = "", salary = 0):
        self.name = name
        self.salary = salary

e1 = Employee("Bob", 4500000)
print(e1.name)
print(e1.salary)
