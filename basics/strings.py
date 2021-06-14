name = 'hello "bomba" bee'
print(type(name))

long_string = '''
se am ooo
'''

print(long_string)
print('hello ' + str(55))
if type('hello ' + str(55)) is str:
    print("you got it mehn")

escape_me = 'zikozee \" is a nigga'

print(escape_me)

weather = "It's \"kind of\" sunny"
print(weather)

# FORMATTED STRING
name = 'Johnny'
age = 55

# 1
print(f'hi {name}. You are {age} years old')

# 2
total_string = 'hi {}. You are {} years old'
total_string = total_string.format(name, age)

# 3
some_String = 'hi {1}. You are {0} years old'
some_String = some_String.format(55, 'Sally')
print(some_String)

# 4
zee_string = 'hi {new_name}. You are {age} years old'
zee_string = zee_string.format(new_name="Zikozee", age=30)
print(zee_string)

# Indexes
selfish = 'me me me'
for i in selfish:
    print(i)

print(len(selfish))

# [start:stop:stepOver]
print(selfish[0:-1:2])
print(selfish[::-1])

# convert string to list then assihn then convert back
data = []
for i in selfish:
    data.append(i)

print(data)
data[0] = "Youghurt:::"
print(data)

data = "".join(data)
print(data)

some_input = input("enter your age: ")
try:
    data = int(some_input)
except ValueError:
    print(some_input + " cannot be converted  to a number")

someData = input("enter your age: ")
checker = someData.isdigit()
if not checker:
    print(someData + " is not a number")

data = "fibonacci"
print(data.find('co'))
