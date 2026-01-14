#- Define a class Car with attributes brand and color. Create an object and print its attributes.
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

print(f"Name: {car1.name}, Brand: {car1.brand}, Color: {car1.color}, Value: {car1.value}, Seats: {car1.seats} ")