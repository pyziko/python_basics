import random as oulala
import sys

from utility import multiply, divide
from shopping.more_shopping import shoopingcart


def randomTesting():
    print(oulala.randint(1, 8))
    print(oulala.choice(list(range(0, 5))))
    my_list = list(range(1, 6))
    oulala.shuffle(my_list)
    print(my_list)


def sysTesting():
    print(sys)


print(__name__)
if __name__ == '__main__':
    print(divide(4, 3))
    print(multiply(4, 5))
    print(shoopingcart.buy('apple'))
    print("please run this")
    randomTesting()
