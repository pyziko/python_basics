import sys


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"Person[name- {self._name}, age - {self._age}]"

    def __repr__(self):
        return f"<Person('{self._name}', {self._age})>"

    def toString(self):
        return self.__str__()


bob = Person("Bob", 35)
print(bob.toString())

print(sys.path)


