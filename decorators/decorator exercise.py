# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):   # todo  remember to use functools and  make sure u pass *args and **kwargs
        if args[0]['valid']:  # first argument, key valid
            fn(*args, **kwargs)
        else:
            print("user is not authenticated")
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
