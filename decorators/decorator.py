# Decorator -> superboost our function by adding extra functionality

def my_decorator(func):
    def wrap_func():  # todo  remember to use functools and  make sure u pass *args and **kwargs
        print("**********")  # some extra functionality
        func()
        print("##########")  # some other extra functionality

    return wrap_func  # notice we are not calling it i.e ()


# under the hood, this is how decorared works
# hello2 = my_decorator(hello)
# hello2()
# OR
#  my_decorator(hello)()

@my_decorator
def hello():
    print('helloooo')


hello()


@my_decorator
def bye():
    print("see ya Later")


bye()
