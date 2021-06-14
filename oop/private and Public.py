class Player:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f"my name is {self._name}, and I am {self._age} years old")


player1 = Player("Ezekiel", 100)

# there's really no privacy in python we can still override it ::: see below
# but for convention sake, we still use underscore
player1.speak = 500

print(player1.speak)
