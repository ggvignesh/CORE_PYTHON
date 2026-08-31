#9. LibraryMember — Borrowing Limit + Title Validation
class LibraryMember:
    total_members = 0
    borrowing_limit = 3

    def __init__(self, name):
        self.name = name
        self.books_borrowed = 0
        LibraryMember.total_members = LibraryMember.total_members + 1

    def borrow_book(self, title):
        if LibraryMember.is_valid_title(title):
            if self.books_borrowed < LibraryMember.borrowing_limit:
                self.books_borrowed = self.books_borrowed + 1
                print(self.name, "borrowed", title)
            else:
                print(self.name, "reached borrowing limit")
        else:
            print("Invalid book title")

    @classmethod
    def update_borrowing_limit(cls, new_limit):
        cls.borrowing_limit = new_limit

    @staticmethod
    def is_valid_title(title):
        if type(title) == str and len(title.strip()) >= 3 and len(title) <= 100:
            return True
        else:
            return False

    def display(self):
        print(f"name = {self.name}")
        print(f"books_borrowed = {self.books_borrowed}")

M1 = LibraryMember("Rajesh")
M2 = LibraryMember("Ramesh")

M1.borrow_book("Python")
M1.borrow_book("Data Science")
M1.borrow_book("Machine Learning")
M1.borrow_book("SQL")

M2.borrow_book("Java")
M2.borrow_book("C++")

print("\nMember Details:")

M1.display()
M2.display()

print("\nTotal active members =", LibraryMember.total_members)

print("\nTitle Validation:")

print("Python =", LibraryMember.is_valid_title("Python"))
print("AB =", LibraryMember.is_valid_title("AB"))
print("Empty =", LibraryMember.is_valid_title(""))

LibraryMember.update_borrowing_limit(5)

print("\nAfter changing borrowing limit:")

M1.borrow_book("SQL")
M1.display()