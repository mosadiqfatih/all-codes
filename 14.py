class BankAccount:
    def __init__(self, account_number, balance):
        self.__accno = account_number
        self.__balance = balance
        
    def deposit(self, amount):
        balance = self.__balance + amount
        self.__balance = balance
        return self.__balance
    
    def withdraw(self, amount):
        balance = self.__balance - amount
        self.__balance = balance
        return self.__balance
    
    def check_balance(self):
        return self.__balance
    
    
acc1 = BankAccount(17, 100000)
print(acc1.check_balance())
print(acc1.deposit(700))
print(acc1.withdraw(1000))
