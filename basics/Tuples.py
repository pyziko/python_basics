# Tuples
empty_tuples = ()

print(empty_tuples)

my_tuple = (1, 2, 3, 4, 5)
print(5 in my_tuple)

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 55
}

print(user.items())

new_tuple = (1, 2, 3, 4, 5, 5)
x, y, z, *other = new_tuple

print(x)
print(other)

print(new_tuple.count(5))
print(new_tuple.index(5))
print(len(new_tuple))
