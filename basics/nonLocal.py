# Scope - what variables do I have access to?
def outer():
    x = "local"

    def inner():
        nonlocal x  # comment out and see difference
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
x = int(5)
print(x)

print("Hello"[0])

print("Hello".upper().replace())
b = "  Hello            ".strip()


