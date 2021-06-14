from typing import List  # , Tuple, Set etc...


class Book:
    pass


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"ddddddddddd {len(self.books)}"


class Duty:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, duty_type: str, weight: int):
        self.name = name
        self.duty_type = duty_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Duty {self.name}, {self.duty_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Duty":   # if different return Class Type, no need for quotes
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Duty":
        return cls(name, cls.TYPES[1], page_weight)
