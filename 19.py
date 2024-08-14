class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []
        
    def add_employee(self):
        self.employees.append(self.name)
        print('employee added successfully..')
        print(self.employees)
    def remove_employee(self):
        self.employees.remove(self.name)
        print('employee removed successfully..')
        print(self.employees)
        
        
hasan = Company('Hasan')
hasan.add_employee()