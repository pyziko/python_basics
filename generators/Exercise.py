# fibonacci number

# using range or generator
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(21):
    print(x)


# using list
def fib(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result
