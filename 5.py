class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def area(self):
        print(self.width * self.length)
        
    def perimeter(self):
        print(2*(self.width + self.length))
        
        
r1 = Rectangle(15, 7)

r1.area()
r1.perimeter()