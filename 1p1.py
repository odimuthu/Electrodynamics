from sympy.physics.vector import *

N = ReferenceFrame('N')

print(N.x, N.y, N.z)

print(N.x == N.x)
print(N.y == N.y)
print(N.z == N.z)

