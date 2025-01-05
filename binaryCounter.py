'''
Binary Counter
Ex. n = 3
input: n
output:
000
001
010
011
100
101
110
111
'''

def bcounter(n):
    arr = [0] * n
    for i in range(2**n):
        print(*arr)
        increment(arr)

def increment(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0: break
        arr[i] = 0
    if i >= 0: arr[i] = 1

def bcounterRCS(n: int, k:int = 0, arr: list = None):
    if arr is None: arr = [0] * n 
    if n == k: 
        print(*arr)
    else:
        arr[k] = 0
        bcounterRCS(n, k+1, arr)
        arr[k] = 1 
        bcounterRCS(n, k+1, arr)

print("Binary Counter")
n = int(input("n = "))
bcounterRCS(n)
print("-"*(n*2))
bcounter(n)
