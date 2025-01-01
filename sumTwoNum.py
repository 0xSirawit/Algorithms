data = [9,2,4,3,7,5,0]
data2 = [9,2,4,3,7,5,6]

def binarySearch(data, n):
    left = 0
    right = len(data)
    while left <= right:
       mid = (left+right) // 2 
       if data[mid] == n:
           return mid
       if data[mid] > n:
           right = mid - 1
       else:
           left = mid + 1
    return -1 

def sum2(numArr, k):
    lengthArr = len(numArr)
    for i in range(lengthArr):
        for j in range(i+1,lengthArr):
            if numArr[i] + numArr[j] == k:
                return [numArr[i], numArr[j]]
    return -1, -1
    
def sum2BinarySearch(numArr,k): 
    lengthArr = len(numArr)
    for i in range(lengthArr):
        delta = k - numArr[i]
        result = binarySearch(numArr[i+1:], delta)
        if result > -1:
            return [numArr[i], numArr[i+1+result]]
    return -1,-1 

print(sum2(data, 7))
print(sum2BinarySearch(sorted(data2), 9))
