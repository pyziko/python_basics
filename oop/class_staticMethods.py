class Character:
    membership = True

    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age

    def instance_method(self): # used to manipulate method
        return f'my name is {self.name}'

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    # with this, we still need it to be part of the class and we use its start i.e attributes. However
    # no need to instantiate class on usage
    # todo this is used to create a function that requires access to the class object via cls (note cls can be any name)
    # todo Hence a new object of type Character can be created here
    @classmethod
    def class_method(cls, num1, num2):
        print(cls.membership) # accessible
        return cls('Teddy', num1 + num2)

    # todo this is just an ordinary function that lives in a class
    @staticmethod   # we don't care about the class state. i.e attributes (i.s static in JAVA)
    def static_method(num1, num2):
        return num1 + num2


# we can access adding things directly
print(Character.adding_things(2, 3))

playerK = Character.class_method(5, 3)
print(playerK.age)

print(Character.static_method(10, 3))
