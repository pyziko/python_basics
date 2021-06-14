def say_hello(name="Ezekiel", emoji="😁"):
    print(f'Hello {name} {emoji}')


say_hello("Eromosei", "😄")
say_hello()

# keyword arguments
say_hello(emoji="😋", name="Bomba")


def add(num, num2):
    return num + num2


print(add(5, 6))


def summation(num1, num2):
    def another_func(a1, a2):
        return a1 + a2

    return another_func(num1, num2)


print(summation(5, 9))


# Exercise

# 1.Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.

def _checkDriverAge(age=0):
    """
    examples \n
    checkDriverAge(32)  return "Powering On. Enjoy the ride!"\n
    checkDriverAge(18)  return "Congratulations on your first year of driving. Enjoy the ride!"\n
    :param age: age of intending driver in int\n
    :return: a comment suitable to driving age
    """
    if int(age) < 18:
        return "Sorry, you are too young to drive this car. Powering off"
    elif int(age) > 18:
        return "Powering On. Enjoy the ride!"
    else:
        return "Congratulations on your first year of driving. Enjoy the ride!"


response = _checkDriverAge()
print(response)

print(help(_checkDriverAge))
print(_checkDriverAge.__doc__)
