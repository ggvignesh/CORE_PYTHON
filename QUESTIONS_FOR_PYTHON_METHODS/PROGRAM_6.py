#6. Book — Constructor + Class Method + Static Method
class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books = Book.total_books + 1

    def display(self):
        print(f"title = {self.title}")
        print(f"author = {self.author}")

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title, author)

    @staticmethod
    def is_valid_title(title):
        if len(title) >= 3:
            return True
        else:
            return False

# Creating book using constructor
B1 = Book("Python", "Guido")

# Validating title before creating book
title = "Java"

if Book.is_valid_title(title):
    B2 = Book(title, "James")
else:
    print("Invalid title")

# Creating book using class method
B3 = Book.from_string("C++-Bjarne")

B1.display()
B2.display()
B3.display()

print(f"Total books = {Book.total_books}")