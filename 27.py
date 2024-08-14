class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def getter(self):
        return self.name, self.price
        
class ShoppingCart(Item):
    cart = []
    def add_item(self):
        ShoppingCart.cart.append(Item.getter(self))
        
    def remove_item(self):
        ShoppingCart.cart.remove(Item.getter(self))
    
    @staticmethod    
    def dis_item():
        print(ShoppingCart.cart)
        

item1 = Item('Vaccum', 1000)
item2 = Item('Toothpaste', 50)

print(type(item2))

ShoppingCart.add_item(item1)
ShoppingCart.add_item(item2)

ShoppingCart.dis_item()