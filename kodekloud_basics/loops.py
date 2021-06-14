counter = 0
while counter < 4:
    print("yoga")
    counter += 1

print("**********************\n\n", 0o7)
i = 2
while True:
    if i % 3 == 0:
        break
    print(i)
    i += 2

print("**********************\n\n", 0o7)
i = 5
while True:
    if i % 0o11 == 0:
        break
    print(i)
    i += 1

print("**********************\n\n", 0o7, "\n\n")
someList = [5, 10, 15, 30]
for i in range(len(someList)):
    print(someList[i])

print("**********************\n\n")
for num in range(0, 11):
    if(num % 2 == 0):continue
    print(num)

print("**********************\n\n")

x = 'abcd'
for i in range(len(x)):
    print("hello")

print("**********************\n\n")

x = 'zikozee'
for i in x:
    print(i.upper())
