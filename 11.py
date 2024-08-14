class Account:
    def __init__(self, balance):
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount
    
    def get_balance(self):
        return self.__balance
        
acc1 = Account(1900)
acc1.deposit(100)
print(acc1.get_balance())     

acc1.withdraw(500)
print(acc1.get_balance()) 