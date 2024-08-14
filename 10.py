class Bird:
    def fly(self):
        print('Flying...')
    
class Penguin(Bird):
    def fly(self):
        print('🐧 cannot fly!')
        
class Eagle(Bird):
    pass


p1 = Penguin()
p1.fly()

e1 = Eagle()
e1.fly()