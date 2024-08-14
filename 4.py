import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        print(math.pi * self.radius**2)
        
        
c1 = Circle(5)
c1.area()