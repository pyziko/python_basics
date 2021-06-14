# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat("Zimmy", 2)
cat2 = Cat("Hulu", 3)
cat3 = Cat("Boner", 5)


# 2 Create a function that finds the oldest cat

def oldestCat(*args) -> int:
    ageHolder = 0
    for cat in args:
        if cat.age > ageHolder:
            ageHolder = cat.age
    return ageHolder


def oldestCat2(*args):
    return max(cat.age for cat in args)


oldest = oldestCat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest} years old.")
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
