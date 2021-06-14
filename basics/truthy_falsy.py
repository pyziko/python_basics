is_old = True
is_licensed = True

if is_old and is_licensed:
    print("ziko")

# Falsy VALUES  --- anything outside this is truthy

# None
# False
# 0
# 0.0
# 0j
# Decimal(0)
# Fraction(0, 1)
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# '' - an empty str
# b'' - an empty bytes
# set() - an empty set
# an empty range, like range(0)
# objects for which
# obj.__bool__() returns False
# obj.__len__() returns 0


print(bool('hello'))
print(bool(5))

print(bool(""))
print(bool(0))
print(bool(-1))
