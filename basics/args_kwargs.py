# *args **kwargs

# todo info *args  --> arguments
def func(*args):
    print(args)  # a tuple
    return sum(args)


print(func(1, 2, 3, 4, 5))


# todo info **kwargs  --> keyword arguments

def anotherFunc(*args, **kwargs):
    print(args)  # a tuple
    print(kwargs)  # returns a dictionary
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total


print(anotherFunc(1, 2, 3, 4, 5, num=5, num2=10))


# todo Rule: params, *args, default params, **kwargs
def orderOfRule(name, *args, i=15, **kwargs):
    pass


# Exercise return highest even number in

def highest_even(a_list):
    a_list.sort(reverse=True)
    for item in a_list:
        if item % 2 == 0:
            return item


# print(highest_even([10, 2, 3, 4, 8, 11, 50]))
