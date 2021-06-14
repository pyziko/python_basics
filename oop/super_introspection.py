class User:
    def __init__(self, email):
        self.email = email

    def signIn(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self._name = name
        self._power = power

    def attack(self):
        print(f"attaching with power of {self._power}")


wizard1 = Wizard("Merlin", 60, "merlin@gmail.com")
print(wizard1.email)

# todo info ->> introspection
print(dir(wizard1))
