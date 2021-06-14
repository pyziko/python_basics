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

    def check_arrows(self):
        print(f"attaching with arrows: arrows left - {self._num_arrows}")

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('borgie', 50, 100)
hb1.run()
hb1.check_arrows()
hb1.attack()
hb1.signIn()