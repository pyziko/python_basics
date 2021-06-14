# Decorator Pattern-> superboost our function by adding extra functionality

def my_decorator(func):
    def wrap_func(*args, **kwargs):  # this now takes unlimited arguments and/or unlimited keyword arguments
        print("**********")  # some extra functionality
        func(*args, **kwargs)
        print("##########")  # some other extra functionality

    return wrap_func  # notice we are not calling it i.e ()


# under the hood, this is how decorared works
# hello2 = my_decorator(hello)
# hello2()
# OR
#  my_decorator(hello)()

@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)


hello("Hi", "EMOJ")


@my_decorator
def sayYo(yo="zoom"):
    print(f"{yo} away")


sayYo()
