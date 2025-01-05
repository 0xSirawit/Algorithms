def sumSubset(arr, t, k):
    print(arr, t, k)
    if t == 0: return True    
    if k < 0: return False
    return sumSubset(arr, t-arr[k], k-1) or sumSubset(arr, t, k-1) 

arrNum = [3, 9, 7]
target = 10
print(sumSubset(arrNum, target, len(arrNum)-1))
