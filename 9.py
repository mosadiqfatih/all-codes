class Vehicle:
    def drive(self):
        pass
    
    
class Bike(Vehicle):
    def drive(self):
        print('Bike on the way🚲')
        
        
class Truck(Vehicle):
    def drive(self):
        print('Truck on the way🚚')
        

b1 = Bike()
b1.drive()

t1 = Truck()
t1.drive()