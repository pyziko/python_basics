class PlayerCharacter:
    # Class Object Attribute. does not change
    membership = True

    # __init__ constructor
    # self is class PlayerCharacter same as "this" in Java
    def __init__(self, name, age):
        if self.membership:  # same as PlayerCharacter.membership
            self.name = name  # attributes that is dynamic (changes)
            self.age = age  # attributes

    def shout(self):
        return f'my name is {self.name}'

    def run(self, hello):
        return f'{hello} my name is {self.name}'


player1 = PlayerCharacter('Cindy', 54)
player2 = PlayerCharacter('Tom', 22)

print(player1.name)
print(player2.age, player2.shout())
print("RUN METHOD: ", player2.run("Hi"))

print(player2.membership)

print("\n**********\n")


# to see blueprint of PlayerCharacter
# help(PlayerCharacter)


class MustBe18:

    def __init__(self, name="anonymous", age=0):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        return f'my name is {self.name}'


user = MustBe18("Ziko", 23)

print(user.shout())
