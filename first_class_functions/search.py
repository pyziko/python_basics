from operator import itemgetter


def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element

    raise RuntimeError(f"could not find an element with {expected}")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
]


def get_friend_name(friend):
    return friend["name"]


# print(search(friends, "Rolf Smith", get_friend_name))

# print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
# todo we can also use itemgetter
print(search(friends, "Rolf Smith", itemgetter("name")))
