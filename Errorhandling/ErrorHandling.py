# Error Handling
age = ""
condition = True
while True:
    try:
        age = input("What is your age? ")
        print(int(age))
        10/int(age)
        break
    except ValueError:
        print(f"inputted data: '{age}' is not a valid number")
    except ZeroDivisionError:
        print(f"inputted data: '{age}', must be greater than zero")
