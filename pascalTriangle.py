import numpy as np

def pascal(n):
    C = np.zeros((n+1, n+1), dtype=int)
    C[0, 0] = 1
    for i in range(1, n+1):
        for j in range(i+1):
            if i == j or j == 0:
                C[i, j] = 1
            else:
                C[i, j] = C[i-1, j-1] + C[i-1, j]
    return C

n = int(input('n = '))
C = pascal(n)
print(F'Print Pascal Triangle (n = {n})')
for i in range(n+1):
    for j in range(i+1):
        print(F'{C[i, j]:<3d}', end=' ')
    print()
