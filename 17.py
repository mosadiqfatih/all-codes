class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        
    def add_student(self, name):
        self.students.append(name)
        print('Student added successfully..')
        print(self.students)
    def remove_student(self, name):
        self.students.remove(name)
        print('Student removed successfully..')
        print(self.students)
        
        
ali = School('ali')
ali.add_student('ali')