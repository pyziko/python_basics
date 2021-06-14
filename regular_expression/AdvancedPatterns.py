import re

# https://www.w3schools.com/python/python_regex.asp
pattern = re.compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
pattern2 = re.compile(
    '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')

email = 'eze.eromosei@gmail.com'

print(bool(re.search(pattern2, email)))

# at least eight characters wrong
# The password is at least 8 characters long (?=.{8,}).
# The password has at least one uppercase letter (?=.*[A-Z]).
# The password has at least one lowercase letter (?=.*[a-z]).
# The password has at least one digit (?=.*[0-9]).
# The password has at least one special character ([^A-Za-z0-9]).

passwordPattern = re.compile("(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,})")

password = 'PythonGuru2#@'

print(bool(re.match(passwordPattern, password)))
print(bool(re.search(passwordPattern, password)))

