# Extend the Book class definition if necessary

class Book:

    def __init__(self, title =0, author = 0):
        self.title = title
        self.author = author

    # Call the describe_book method here
    def describe_book(self):
        print(f"Title: {f_book.title}, Author: {f_book.author}")
    

def ask_book():
    n_title=input("Title book: ")
    n_author=input("Author book: ")
    return n_title, n_author



#def main ():
title, author = ask_book()
f_book = Book( title, author)
f_book.describe_book()



#main()
# Write a script that takes input and creates an instance of Book

