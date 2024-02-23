# Define the FileManager class here
class FileManager:
    def __init__(self, filename):
        self.filename
    
    def write_content(self, content):
        file = open("prueba.txt","x")
        #text = input("text: ")
        file.write(content)
        file.close()
    
    def read_content(self):
        file = file = open("prueba.txt","r")
        file.read()
        file.close()

# Demonstrate using FileManager to write and read from a file
n_file = FileManager("prueba.txt")
n_file.write_content("hola")
n_file.read_content()