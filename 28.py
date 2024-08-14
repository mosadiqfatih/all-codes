class Restaurant:
    def __init__(self, name, menu=None):
        self.name = name
        if menu == None:
            self.menu = []
        else:
            self.menu = menu
            
    def add(self, item):
        self.menu.append(item)
        print(self.menu)
    def remove(self, item):
        self.menu.remove(item)
        print(self.menu)
        

r1 = Restaurant('Abas Qoli Special', ['Chips', 'Jigar', 'Palaw', 'Kabab', 'Chainaki'])

r1.add('Karayi')
r1.remove('Chips')
