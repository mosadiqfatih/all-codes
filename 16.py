class Library:
    books = []
    def __init__(self, name, book):
        self.name = name
        self.book = book
        
    def add_books(self):
        Library.books.append(self.book)
        print('one book added..')
        print(Library.books)
    
    def remove_books(self):
        Library.books.remove(self.book)
        print('one book removed..')
        print(Library.books)
    
    
    
book1 = Library('roman', 'Alchemist')

book1.add_books()

book1.remove_books()