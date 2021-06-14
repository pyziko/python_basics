from datetime import date

birth_year = input('what year were you born?  ')
if birth_year.isdigit():
    print("yes you can continue")
age = date.today().year - int(birth_year)
print(f"You are {age} years old")


# password checker

username = input("Enter your username: ")
password = input("Enter your password: ")

starred = '*' * len(password)

print(f'Hey {username} password {starred} is {len(password)} letters long')
