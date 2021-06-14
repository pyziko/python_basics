# while loop
i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('done with all the work')

# else is only used when we want to be sure that the while loop runs successfully
# but it requires a break
# note, the break, goes entirely out of the while loop hence the else won't be called


while True:
    response = input('say something: ')
    if response == 'bye':
        break

# Pass  used where an empty code is not allowed

for i in [1, 2, 3]:
    pass

# Exercise
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0]
]

# is_friend = True
# can_message = "message allowed" if is_friend else "not allowed to message"
collector = ""
for sublist in picture:
    for item in sublist:
        collector += " " if item == 0 else "$"
    print(collector)
    collector = ""


# Exercise check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = {"dummy"}
duplicates.clear()
for char in some_list:
    if some_list.count(char) > 1:
        duplicates.add(char)
print(duplicates)