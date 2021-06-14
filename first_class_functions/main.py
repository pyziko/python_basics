
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


# todo notice here we don't add parenthesis meaning we are not calling/executing "divide"
result = calculate(20, 4, operator=divide)

if __name__ == '__main__':
    print(result)

