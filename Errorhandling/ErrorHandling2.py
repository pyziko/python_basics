# Error Handling

def add(num1, num2):
    try:
        return num1/num2
    except TypeError as err:
        print(f"check inputted numbers: {err}")
    except (ZeroDivisionError, ValueError) as err:
        print(err)
        raise


print(add(5, 'str'))
