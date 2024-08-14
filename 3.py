class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def printing(self):
        print(self.make, self.model, self.year)
        
        
bugatti = Car('Bugatti', 'Veyron', 2045)
bugatti.printing()    