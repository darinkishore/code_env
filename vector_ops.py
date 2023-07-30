# vector operations with the vector class

from vector_and_matrix_v2 import Vector, Matrix



# vector addition

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(f"{v1} + {v2} = {v1 + v2}")

# matrix multiplication

m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[1, 2], [3, 4], [5, 6]])
print(f"{m1} * {m2} = {m1 * m2}")

# invalid matrix multiplication

m3 = Matrix([[1, 2, 3], [4, 5, 6]])
m4 = Matrix([[1, 2], [3, 4]])
try:
    print(f"{m3} * {m4} = {m3 * m4}")
except ValueError as e:
    print(e)



