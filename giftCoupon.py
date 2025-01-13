A = [ 69, 82, 134, 92, 76 ]
P = 200
res, ans = [], []
counter = 1

def backtrack(arr, target, k):
    global res
    global ans
    global counter
    if sum(res) >= target:
        ans.append(res.copy())
        return
    if len(arr) <= k: return
      
    backtrack(arr, target, k+1)
    res.append(arr[k])
    counter += 1
    backtrack(arr, target, k+1)
    res.pop()
    return ans

x = backtrack(A, P, 0)
print(f"counter: {counter}")
ans = sorted(x, key=lambda x: sum(x))[0]
print(f"answer is", sum(ans), ans)
for i in range(len(x)):
    print(i+1, sum(x[i]), x[i])
