import random

def makeCostMatrix(n,m):
    return [[random.randint(100, 200) for row in range(n)] for column in range(m)]

print(makeCostMatrix(3,2))
