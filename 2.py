class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f'Hello Mr.{self.name}')
        

p1 = Person('ali ahmad', 15)

p1.greeting()