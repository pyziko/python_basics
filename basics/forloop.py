# enumerates

for counter, item in enumerate('Zero to MasteryV2'):
    if item == 'o':
        continue
    if item.isdigit():
        value = int(item) + 5
        print(value)

    print(counter, item)

# iterables -> object that can be iterated over. list, dictionary, tuple, set, string
# iterate -> one by one check each item

print("\n***********\n")

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
print("\n***********\n")

for key in user.keys():
    print(key)
print("\n***********\n")

for value in user.values():
    print(value)
print("\n***********\n")

for item in user.items():
    key, value = item
    print(key, value)
print("\n***********\n")

for key, value in user.items():
    print(key, value)

print("\n***********\n")
# counter
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = sum(some_list)
print(total)

total2 = 0
for i in some_list:
    total2 += i
print(total2)


# range
print("\n***********\n")

# for i in range(51):
#     print(i)
#
# for i in range(0, 51):
#     print(i)
#
for i in range(0, 51, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

print(list(range(10)))

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f"index of 50 is  {i}")
        break
