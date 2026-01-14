#- Define a static method calculate_area() in a Rectangle class that calculates the area using width and height
class Rectangle:
    @staticmethod
    def calculate_area(length, breadth):
       print(length*breadth , "sq.units")



    
rec1 = Rectangle()
rec1.calculate_area(4,5)


