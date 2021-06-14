usernames = {"Ezekiel": "zikana", "max": [1, 2, 3, 4]}

print(usernames["max"])

disordered = {2: "zikana", "max": [1, 2, 3, 4], False : "Zibana"}
for key in disordered.keys():
    print(str(key) + "-" + str(disordered[key]))

#UPDATING
disordered["ziko"] = "Gbana"
disordered.update({"bashi": "Kpolaka"})
print(disordered)
print(disordered[False])

#DELETING
del disordered["bashi"]
print(disordered)

#REMOVE LAST ITEM
disordered.popitem()
print(disordered)


#CLEAR
disordered.clear()
print(disordered)



print("\n**************\n")
values = usernames.values()
print("Yoo", values)
for i in values:
    print(i)

print("\n**************\n")
keys = usernames.keys()
print("Yaa", values)
for i in keys:
    print(i)

print(usernames.items())