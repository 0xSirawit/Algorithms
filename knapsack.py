import numpy as np

'''
1/0 Knapsack Problem with Bottom-up approach (Tabulation)
input:
values = 60 100 120
weights = 10 20 30
max weights = 50

output:
Knapsack problem
n = 2
v = [60, 100, 120]
w = [10, 20, 30]
W = 50
Max value = 220
'''

def knapsack(v, w, W):
    m = len(v)
    V = np.zeros((m, W+1), dtype=int)
    for i in range(1, m):
        for j in range(1, W+1):
            take = 0
            notake = V[i-1, j]
            if w[i] <= j:
                take = v[i] + V[i-1, j-w[i]]
            V[i,j] = max(take, notake)
    return V[i,j]

v = [int(x) for x in input("values = ").split()]
w = [int(x) for x in input("weights = ").split()]
W  = int(input("max weights = "))
print('Knapsack problem')
print('n =', len(v)-1)
print('v =', v)
print('w =', w)
print('W =', W)
mxvalue = knapsack(v,w,W)
print("Max value =", mxvalue)
