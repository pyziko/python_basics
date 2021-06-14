countries = ["USA", "Canada", "India"]
# get items
b = countries[0]
b_same = countries[-3]
print(b, b_same)  ### same as countries[-3]

# deleting
del countries[1]

print(countries)

#### CHANGING DATA

countries.append("Nigeria")
print(countries)
countries.insert(2, "Brazil")

print(countries)

##SWAPPING DATA   -- instead of using temporary data
countries[0], countries[1] = countries[1], countries[0]
print(countries)

print("POPPING \n")
countries.pop(2)
print(countries)

print("SORT \n")
countries.sort()
print(countries)

print("REVERSE \n")
countries.reverse()
print(countries)

print("MAX \n")
print(max(countries))

##ITERATING DATA
list1 = [4, 0, 7, 1]
print(list1[::-1])

# ITERATING WITHOUT INCREMENTING as loop position "i" and value of list provided "j"
for i, j in enumerate(list1):
    print(i, j)

list1 = [[1, 2, 3, 2, 5], [4, 5, 6, 7], [8, 9, 10]]
for i in list1:
    if len(i) == 3:
        print(i)

list1 = [] * 2
print(list1)

# SLICING        list[start:end]
letters = ["A", "B", "C", "D", "E"]

print(letters[0:2])
print(letters[1:])
print(letters[:4])

print(letters[1:-1])

# This assist to copy over the list so the original is not manipulated
letter_copy = letters[:]

print(letter_copy)

del letters[1:3]
print(letters)

# FINDING list
letters = ["A", "B", "C", "D", "E"]

print("B" in letters)

print("C" not in letters)



