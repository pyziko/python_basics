# Scope - what variables fo I have acces to

x = 1


def confusion():
    a = 5
    global x
    return a + x


def usingGlobal():
    a = 5
    b = x
    return a + b


print(confusion())
print(usingGlobal())
print(x)

# 1 - start with local
# 2 - Parent local
# 3 - Global
# 4 - built in python functions.
