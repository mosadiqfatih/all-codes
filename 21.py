class FileManager:
# -----------first approach----------
#     def _read(self):
#         with open('neuro.txt', 'r') as file:
#             print(file.read())
            
#     def _write(self, text):
#         with open('neuro.txt', 'w') as file:
#             print(file.write(text))
            
            
# f1 = FileManager()
# f1._read()

# f1._write('What is dead may never die?')

    def reading(self):
        file = open('neuro.txt', 'r')
        print(file.read())
    
    def writing(self):
        file = open('neuro.txt', 'w+')
        file.write('New text inserted..')
        file.seek(0)
        print(file.read())
        
f1 = FileManager()
f1.writing()