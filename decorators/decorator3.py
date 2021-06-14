# Decorator
from time import time


def performance(func):
    def wrap_func(*args, **kwargs):# todo  remember to use functools
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"time taken: {end - start} s")
        return result

    return wrap_func  # notice we are not calling it i.e ()


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()
