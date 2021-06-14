# Dictionary
some_dict = {}

print(some_dict)
dictionary = {'a': 1, 'b': 2, 'x': True, 5: 2.0}

print(dictionary['a'])
print(dictionary)

my_list = [{'a': [1, 2, 3], 'b': 2, 'x': True}, {'a': [4, 5, 6], 'b': 2, 'x': True}]

# Keyz - keys mus be immutable
# hence keys cannot be lists.
# since tuples are immutable, they can be keys
dictionary = {
    (1, 2): True
}
print(dictionary)

# unique keys are
unique_key_dict = {
    '123': True,
    '123': [1, 2, 3, 4]
}

print(unique_key_dict)

# todo Methods -> creation

user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}

print(user.get('age', 55))  # incase age does not exist use 55
print(user)

user2 = dict(name='John', age=55)
print("create new dict", user2)

# todo Update
some_dict.update({'a': 1})
# another Update
some_dict['b'] = True

# todo methods -> in, keys, values, items(tuples)

some_user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 55
}

print('size' in some_user)
print('greet' in some_user)

# todo keys
keys = some_user.keys()
print("keys: ", keys)
print('greet' in some_user.keys())

# todo values
values = some_user.values()
print("values: ", values)
print(55 in some_user.values())

# todo items -> tuples
items = some_user.items()
print("items: ", items)

print(('basket', [1, 2, 3]) in some_user.items())
print('basket' in some_user.items())

# todo pop
print("Popping: ", some_user.pop('age'))
print(some_user)
print("Popping some Item as dict is unordered: ", some_user.popitem())

# todo copy
some_user2 = some_user.copy()
print(some_user2)
# todo clear
some_user.clear()
print(some_user)
print(some_user2)





