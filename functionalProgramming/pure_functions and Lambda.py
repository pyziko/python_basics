# given the same input, it will always give the same output
# it should not interact with the outside world (i.e its scope)
# the idea is we would never have a bug since it doesn't depend on
# any data from the outside world (outside its scope) which is subject to change

# pure functions leads to less buggy code
from functools import reduce


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


# todo info map, filter, zip and reduce

print("\n*********** MAP *************\n")
# todo map -> transforming data
# takes the function without "()" so that it does not execute then takes in the data

my_list = [1, 2, 3]


def timesBy2(item):
    return item * 2


print(list(map(timesBy2, my_list)))
print(my_list)


#
#
#
print("\n*********** FILTER *************\n")
# todo filter -> checks predicate passed

def only_dd(item):
    return item % 2 != 0


print(list(filter(only_dd, my_list)))
print(my_list)

#
#
#
#
print("\n*********** ZIP *************\n")
# todo zip -> use case, grouping some data together, say email, names, phoneNumber
# todo info note if one is longer it ignores the extras
email = ("test@test.com", "test@test1.com", "test@test2.com")
name = ("Ezekiel", "Ziko", "Zikozee")
number = ("07066616366", "08055573668", "08176569549", "08037672979")

print(list(zip(email, name, number)))

#
#
#
#
print("\n*********** REDUCE *************\n")


# todo reduce -> import from functools
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))


print("\n*********** LAMBDA *************\n")
# todo lambda expressions
# lambda param: action(param)

print("LAMBDA FOR MULTiPLY BY 2: ==> ", list(map(lambda item: item * 2, my_list)))
print("LAMBDA FOR FILTER  ==> ", list(filter(lambda item: item % 2 != 0, my_list)))
print("LAMBDA FOR REDUCE  ==> ", reduce(lambda acc, item: acc + item, my_list, 0))
