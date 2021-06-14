# 2D ARRAY
classroom = [
    ["Sam", "Max", "Joe", "Anne"],
    ["Sofie", "Lisa", "Tim", "Sasha"],
    ["Claire", "Sara", "Leo", "Kim"],
    ["Zoe", "Guy", "Anna", "Eve"]
]

student = classroom[2][1]
print(student)

print("\n********************\n")
# check if Eve exists in nested list1 without modifying original list
classroom_copy = [item for students in classroom for item in students]
# same as above
# classroom_copy = []
# for students in classroom:
#   for item in students:
#        classroom_copy.append(item)


print(classroom_copy)

eveExists = "Eve" in classroom_copy
print(eveExists)

print("\n********************\n")
countries = [['Egypt', 'USA', 'India'],
             ['Dubai', 'America', 'Spain'],
             ['London', 'England', 'France']]
countries2 = [country for sublist in countries for country in sublist if len(country) < 6]
print(countries2)

matrix = [[j for j in range(4)] for i in range(4)]
print(matrix)