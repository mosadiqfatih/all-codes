class Animal:
    def speak(self):
        pass
        
        
class Dog(Animal):
    def speak(self):
        print('Bark!')
        
        
class Cat(Animal):
    def speak(self):
        print('Meow!')
        

c1 = Cat()
c1.speak()

d1 = Dog()
d1.speak()