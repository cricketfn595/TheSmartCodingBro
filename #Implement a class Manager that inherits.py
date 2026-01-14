#Implement a class Manager that inherits from both Employee and Person.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe_person(self):
        return f"Name: {self.name} , Age: {self.age}"
    
class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def describe_employee(self):
        return f"Employee ID: {self.employee_id} , Salary: {self.salary}"
    
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)
        self.department = department

    def describe_manager(self):
        return f"{self.describe_person()} , {self.describe_employee()}, Department:{self.department}"
    
m1 = Manager("Riku",12, "AB555", 100000, "IT")
print(m1.describe_manager())