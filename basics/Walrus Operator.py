# Walrus Operator

a = 'hellooooooooooooooooooooo'

if len(a) > 10:
    print(f"too long {len(a)} elements")

# Walrus style
if (n := len(a)) > 10:
    print(f"too long {n} elements")

# another Walrus example
while (n := len(a)) > 1:
    print(n)
    a = a[:-1]


print(a)