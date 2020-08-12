m = int(input("fill the row number"))
n = int(input("fill the column number"))
i = int(input("fill the index number"))
mat = [[1*i for n in range(2)] for m in range(3)]

def matrix(m, n):
    mat = [[1*i for n in range(2)] for m in range(3)]
    return mat
  
print(mat)

a = len(mat[0])
b = len(mat)
trans = [[1*i for b in range(3)] for a in range(2)]

def transpose(trans): 
    for a in range(len(mat)):
        for b in range(len(mat[0])):
            trans[b][a] = mat[a][b]

for t in trans:
    print(t)


A = [[1*i for n in range(2)] for m in range(3)]
B = [[2*i for n in range(2)] for m in range(3)]
print(A)
print(B)

def addition(sum):
    for c in range(len(A)):
        for d in range(len(A[0])):
            sum[c][d] = A[c][d] + B[c][d]

mul = []
def multiply(mul):
    mul = [] 
    for e in range(0, len(A)): 
        mul.append(A[e] * B[e]) 
print(mul)
