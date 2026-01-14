#- Modify the Car class to include a method describe() that prints the car's brand and color.
class Car:
    name = ""
    brand = ""
    color = ""
    value = 0
    seats = 0

car1 = Car()
car1.name = "Baleno"
car1.brand = "Maruti Suzuki"
car1.color = "Blue, Red, White, Brown etc"
car1.value = 80000
car1.seats = 5

def describe(obj):
    print(f"Name: {obj.name}, Brand: {obj.brand}, Color: {obj.color}, Value: {obj.value}, Seats: {obj.seats} ")

describe(car1)