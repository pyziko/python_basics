from CustomError import NotNumberException

age = ""
while True:
    try:
        age = input("What is your age? ")
        if age == "0":
            raise ZeroDivisionError("Numerator cannot be zero-based")
        10/int(age)
    except ValueError:
        print(f"inputted data: '{age}' is not a valid number")
        raise NotNumberException("This is not a valid number").message()
    except ZeroDivisionError as e:
        print(f"{age} >>> {e}")
    else:  # todo place code here that should run if no errors occurred
        print("Thank you")
        break
    finally: # todo place code here that should run regardless if there are errors or not
        print("Ok, i am finally done")