class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': "yoyo",
            'hasPets': False
        }

    # our own implementation of str
    def __str__(self):
        return f"{self.color}"

    # our own implementation of len
    def __len__(self):
        return 5

    # our own implementation of delete
    def __del__(self):
        print('deleted!')

    # our own implementation of call
    def __call__(self):
        return 'yes??'

    # our own implementation of getitem in dict
    def __getitem__(self, i):
        return self.my_dict[i]


actionFigure = Toy('red', 0)
print(actionFigure.__str__())
print(str(actionFigure))
print(len(actionFigure))
# del actionFigure
print(actionFigure())
print(actionFigure['name'])
