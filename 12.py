class Book:
    def __init__(self, title, author, pages):
        self.__title = 0
        self.__author = 0
        self.__pages = 0
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        self.__title = value
        
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, value):
        self.__author = value
        
    @property
    def pages(self):
        return self.__pages
    
    @pages.setter
    def pages(self, value):
        self.__pages = value
        
        
b1 = Book('Alchemist', 'Paulo Coehlo', 210)
b1.author = 'Paulo the Magician'
print(b1.author)