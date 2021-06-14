# a class that has many of other class
# Inheritance : a book is a book self
# Composition: A bookshelf has many books

class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

    def to_string(self):
        return self.__str__()


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("Python 101")

shelf = BookShelf(book, book2)

print(shelf.to_string())
print([book.name for book in shelf.books])
