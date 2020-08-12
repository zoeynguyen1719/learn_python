import os, sys


def fseri(a):
    if a<=1: 
        return a
    else:
        return (fseri(a - 1) + fseri(a - 2))
n = int(input("fill the number"))
print("fibonacci:")
for i in range(n):
    print(fseri(i))
    
