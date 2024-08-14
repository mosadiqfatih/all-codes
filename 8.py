class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        
        
m1 = Manager('Abas', 300000000, 'IT')

print(m1.name, m1.salary, m1.department)

        
        
    