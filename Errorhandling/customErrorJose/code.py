class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __str__(self):
        return f"Book {self.name}"

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only have {self.page_count} pages."
            )
        self.pages_read += pages
        print(f"You have read now read {self.pages_read} pages out of {self.page_count}")


python101 = Book("Python101", 50)
try:
    python101.read(35)
    python101.read(50)
except TooManyPagesReadError as e:
    print(e)