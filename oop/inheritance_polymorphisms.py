# todo info ->> INHERITANCE

class User:

    def signIn(self):
        print("Logged ib")

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def accessParentAttack(self):
        # i can access User(parent here)
        User.attack(self)

    def attack(self):
        print(f"attaching with power of {self._power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):

        print(f"attaching with arrows: arrows left - {self._num_arrows}")


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
wizard1.attack()
archer1.attack()

# checking instances
print(isinstance(wizard1, User))
print(isinstance(archer1, User))
print(isinstance(archer1, object))


print("\n*****************\n")

# todo info ->> POLYMORPHISM
wizard1 = Wizard("Merlin", 60)
archer1 = Archer("Robin", 30)


# now this guy can take anything that inherits user or rather anything that has attack method
# sample1
def player_attack(character):
    character.attack()


player_attack(wizard1)
player_attack(archer1)

# sample2
for char in [wizard1, archer1]:
    char.attack()
