#BinarySearch with sorted num array
sortedData = [2,3,5,9,11,20,25,39,44,49,52,79]

def binarySearch(numArr, searchNum):
    left = 0 
    right = len(numArr)
    while left <= right:
        mid = (left + right) // 2
        if numArr[mid] == searchNum: return mid
        if numArr[mid] > searchNum:
            right = mid - 1
        else:
            left = mid + 1 
    return -1

result = binarySearch(sortedData, 11)
print(result)
