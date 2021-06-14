# type hinting is defining type of arguments in method and also the return type
def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count


if __name__ == '__main__':
    print(list_avg(123))
