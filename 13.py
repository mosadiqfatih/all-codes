class Laptop:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price
        
        
    def Brand(self):
        return self.__brand
        
    def Model(self):
        return self.__model    
        
    def Price(self):
        return self.__price
    
    def discount_calculating(self, discount_rate):
        discount = self.__price * discount_rate
        return f'Discount amount: {discount}'
    
    
l = Laptop('DELL', 'Latitude E7250', 15000)
print(l.Brand())
print(l.Model())     
print(l.Price())
print(l.discount_calculating(.20))