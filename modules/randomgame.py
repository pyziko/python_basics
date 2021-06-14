import random
import sys

# cd to the path of this file and then run: python randomgame.py 1 10

# remember sys.argv[0] is file name
firstNumber = sys.argv[1]
secondNumber = sys.argv[2]
rand = random.randint(int(firstNumber), int(secondNumber))

while True:
    print(f"Guess a number from {firstNumber} to {secondNumber}")
    try:
        entered = int(input("Enter number: "))
        if entered < 1 or entered > 10:
            print("it must be a number between 1 and 10")
            print("\n*******************\n")
            continue

        if entered == rand:
            print("You are a Genius")
            break
        else:
            print("Try again")
    except ValueError:
        print("Please Enter a valid number")
        print("\n*******************\n")
