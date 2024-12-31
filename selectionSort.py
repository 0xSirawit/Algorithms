#selectionSort
data = [29,10,14,37,14]

def findMinIndex(numArr, k):
    minIndex = k
    for i in range(k+1, len(numArr)):
        if numArr[i] < numArr[minIndex]:
            minIndex = i
    return minIndex

def selectionSort(numArr):
    lengthArr = len(numArr)
    for i in range(lengthArr-1):
        minIndex = findMinIndex(numArr, i)
        numArr[i], numArr[minIndex] = numArr[minIndex], numArr[i]

print("Raw data:", data)

selectionSort(data)
print("Sorted data:", data)
