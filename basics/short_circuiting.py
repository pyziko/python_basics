# short circuiting
from functions_docstrings import checkDriverAge

is_friend = True
is_user = False

if is_friend or is_user:
    print("best friends for ever")

if is_friend and is_user:
    print("best friends for ever")

# Logical Operators

# lowercase letter is of higher precedence than uppercase version
print('a' > 'b')
print('a' > 'A')

is_magician = True
is_expert = False

# check if magician and expert: "You are a master magician"

# check if magician but not expert: "at least you're getting there"

# if you're not a magician: "You need magic powers"

if not is_magician:
    print("You need magic powers")
elif is_magician and not is_expert:
    print("at least you're getting there")
else:
    print("You are a master magician")

# == checks for equality hence there is conversion
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# is checks location in memory where they are stored. if they are the same
# not data structures are created in different location
# but same types like int, str, bool with same value are same
print("\n*************\n")

print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)


data = checkDriverAge(50)
print(data)