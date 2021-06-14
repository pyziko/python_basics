# List Slicing
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes', 'juice']

print(amazon_cart)

# first and second items
print(amazon_cart[0:2])

# reverse
print(amazon_cart[::-1])

# remove item at index 3
print(amazon_cart.pop(3))
print(amazon_cart)

# Matrix
matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

first_in_first_row = matrix[0][0]
print(first_in_first_row)
Second_in_first_row = matrix[0][1]
print(Second_in_first_row)
first_in_second_row = matrix[1][0]
print(first_in_second_row)
second_in_last_row = matrix[-1][1]
print(second_in_last_row)
last_in_second_row = matrix[1][-1]
print(last_in_second_row)

# List Methods
basket = [1, 2, 3, 4, 5]

# adding
basket.append(100)
new_list = basket
print(new_list)

basket.extend([100, 101])
new_list2 = basket
print(new_list2)

# More Methods
letters = ['a', 'b', 'c', 'd', 'e', 'd']
print("f" in letters)

print(letters.count('d'))

letters.sort()
print(letters)
print(letters.reverse())
print("reverse: ", letters)
letters.sort(reverse=True)
print(letters)

print(sorted(['d', 'f', 'a', str(5)]))

# Common Patterns
print(list(range(101)))

delimiter = " "
new_sentence = delimiter.join(["hi", "my", "name", "is", "ziko"])
print(new_sentence)

# todo info list unpacking

a, b, c, *sliced = [1, 2, 3]
print(a, b, c)

i, j, k, *sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(i, j, k, sliced)

w, x, y, *sliced, z = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(w, x, y, sliced, z)
