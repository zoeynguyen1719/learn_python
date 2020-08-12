import os
import sys
import numpy
import numpy as np

A = [[m for m in range(3)] for n in range(2)]
A = np.array(A)
print(A)

print(A.transpose())

D = [[h for h in range(3)] for k in range(2)]
D = np.array(D)
E = A + D
print(E)

B = [[i for i in range(2)] for j in range(3)]
B = np.array(B)
C = A.dot(B)
print(C)

F = [[l for l in range(4)] for p in range(4)]
F = np.array(F)
print numpy.linalg.det(F)