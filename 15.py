class Student:
    def __init__(self, name, grade, age):
        self.__name = name
        self.__grade = grade
        self.__age = age
        
    def getter(self):
        return self.__name, self.__grade, self.__age
    
    def _setter(self, name, grade, age):
        self.__name = name
        self.__grade = grade
        self.__age = age
    

ali = Student('ali', 10, 17)    
print(ali.getter())
ali._setter('ali reza', 12, 19)
print(ali.getter())
