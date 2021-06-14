# 3D ARRAY
print("\n********************\n")
Colors = [[['Blue', 'Green', 'White', 'Black']], [['Green', 'Blue', 'White', 'Yellow']],
          [['White', 'Blue', 'Red', 'Green']]]

print(Colors[2][0][2])

matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
    for val in submatrix:
        matrix2.append(val)

print(matrix2[2])

print("\n*****************\n")

for submatrix in matrix:
    for val in submatrix:
        matrix2.append(val)

print(matrix2[2][2])
