# list, set, dictionary

# var = [param for param in iterable]
# var = [expression for param in iterable conditional]

print("\n****** LIST COMPREHENSION *******\n")
my_list = [*'hello']
my_list2 = [char for char in 'hello']
print(my_list)
print(my_list2)
my_list3 = [num for num in range(0, 100)]
print(my_list3)

# doubling my_list3
my_list4 = list(map(lambda x: x * 2, [num for num in range(0, 100)]))
# doubling my_list3 simpler way
my_list5 = [num ** 2 for num in range(0, 100)]
# only even numbers
# todo info var = [expression for param in iterable conditional]
my_list6 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

print("DOUBLING =", my_list4)
print("SQUARING =", my_list5)
print("EVEN NUMBERS =", my_list6)

print("\n****** SET COMPREHENSION *******\n")
#
#
# todo ==> Set Dictionary Comprehension
# doubling my_list3 simpler way
my_set2 = {num ** 2 for num in range(0, 100)}
# only even numbers
# todo info var = [expression for param in iterable conditional]
my_set3 = {num ** 2 for num in range(0, 100) if num % 2 == 0}

print("SQUARING =", my_set2)
print("EVEN NUMBERS =", my_set3)

print("\n****** DICT COMPREHENSION *******\n")
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

# var = [expression for param in iterable conditional]
my_dict = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
some_dict = {num: num * 2 for num in [1, 2, 3]}

print("DICTOO",my_dict)
print(some_dict)

student_attendance = {"Rold": 96, "Box": 85}
for t in student_attendance.items():
    print(t)
    i, x = t
    print(f"{i} : {x}")

sequence = [1, 2, 3, 4, 5, 6]

print(list(x * 2 for x in sequence))


users = [
    (0, "Bob", "Password"),
    (1, "Bobs", "Password"),
    (2, "Bobd", "Password")

]

# making username as key
user_dict = {user[1]: user for user in users}
print(user_dict.values())
print(user_dict)