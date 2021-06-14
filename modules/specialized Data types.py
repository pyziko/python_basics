from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7]

sentence = 'blah blah blah thinking about python'
print(Counter(li))
print(Counter(sentence))

# TODO DEFAULT DICT
# using default dict we can set a value for non-existent keys
# dictionary = defaultdict(lambda: bool(), {'a': 1, 'b': 2})
dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})

print(dictionary['c'])


# TODO INFO: ORDERED DICTIONARY
# TODO DICTIONARY BY DEFAULT ARE NOW ORDERED SO NO NEED FOR THIS
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)






