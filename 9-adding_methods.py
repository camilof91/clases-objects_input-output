# Modify the Book class from Exercise 1 and add the describe_book method

class Book:

    def __init__(self, title =0, author = 0):
        self.title = title
        self.author = author

    # Call the describe_book method here
    def describe_book(self):
        print(f"Title: {f_book.author}, Author: {f_book.author}")


# Create an instance of Book here   
f_book = Book( "Python Basics", "John Doe")
f_book.describe_book()



