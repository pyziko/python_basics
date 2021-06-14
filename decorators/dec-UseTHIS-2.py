import functools

user = {"username": "jose", "access_level": "admin"}


# todo always pass *arg and **kwargs so that is resuable by fns that take in arguments
# todo info::::: functools this ensures that function passed name and documentation is not lost
def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


@make_secure
def get_admin_password():
    return "1234"

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secured_password"


# print(get_admin_password.__name__)  # try this without functools and you'll see name is lost

print(get_admin_password())

