# generator is a subset of an iterable
from time import time


def generator_fn(num):
    for i in range(num):
        yield i  # yield only keeps only value in memeory per time


g = generator_fn(10)

print(next(g))
print(next(g))
print(next(g))
print(next(g))

#
#
#
print("\n******** GENERATOR PERFORMANCE ********\n")


def performance(func):
    def wrap_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"time taken: {end - start} s")
        return result

    return wrap_func  # notice we are not calling it i.e ()


@performance
def long_time():
    for i in range(1000000):
        i * 5


@performance
def long_time2():
    for i in list(range(1000000)):
        i * 5


long_time()
long_time2()
