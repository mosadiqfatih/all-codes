class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        
    def add_animal(self):
        self.animals.append(self.name)
        print('animal added successfully..')
        print(self.animals)
    def remove_animal(self):
        self.animals.remove(self.name)
        print('animal removed successfully..')
        print(self.animals)
        
        
lion1 = Zoo('Zeus')
lion1.add_animal()
lion1.remove_animal()