# Sets

my_set = {1, 2, 3, 4, 5, 6, 6}

print(my_set)

# todo Adding
my_set.add(100)
my_set.add(2)

print(my_set)

# todo convert list to set
my_list = [1, 2, 3, 4, 5, 5]

new_set = set(my_list)
print(new_set)

# todo convert set to list
new_list = list(new_set)
print(new_list)
# todo len of set
print(len(new_set))

# todo METHODS

# todo update
my_set = {1, 2, 3, 4, 5, }
your_set = [4, 5, 6, 7, 8, 9, 10]
my_set.update(your_set)
print("update ", my_set)

# todo difference
my_set = {1, 2, 3, 4, 5, }
your_set = {4, 5, 6, 7, 8, 9, 10}
my_set.difference(your_set)
print("difference ", your_set.difference(my_set))


# todo difference update:::: removes all element of another set from this set
my_set = {1, 2, 3, 4, 5, }
your_set = {4, 5, 6, 7, 8, 9, 10}
# my_set.difference_update(your_set)
# print("difference update", my_set)
your_set.difference_update(my_set)
print("difference update", your_set)

# todo discard
my_set.discard(5)
print(my_set)

# todo intersection
my_set = {1, 2, 3, 4, 5, }
your_set = {4, 5, 6, 7, 8, 9, 10}
print("intersection", my_set.intersection(your_set))
print("intersection alternative", my_set & your_set )

# todo disjoint
my_set = {1, 2, 3, 4, 5, }
your_set = {4, 5, 6, 7, 8, 9, 10}
print("isdisjoint: ", my_set.isdisjoint(your_set))


# todo disjoint
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print("isdisjoint: ", my_set.isdisjoint(your_set))
my_set = {1, 2, 3}
your_set = {4, 5, 6, 7, 8, 9, 10}
print("isdisjoint: ", my_set.isdisjoint(your_set))

# todo union
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print("union: ", my_set.union(your_set))
print("union alternative : ", my_set | your_set)

# todo subset
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print("subset: ", my_set.issubset(your_set))
my_set = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print("subset2: ", my_set.issubset(your_set))


# todo superset
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print("superset: ", my_set.issuperset(your_set))
my_set = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print("superset2: ", your_set.issuperset(my_set))

