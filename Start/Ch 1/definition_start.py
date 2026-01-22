# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# create a basic class
class Book:
    """A class representing a book with a title and an author."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

# create instances of the class
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# print the class and property
print(f"Book 1: {book1.title} by {book1.author}")
print(f"Book 2: {book2.title} by {book2.author}")
