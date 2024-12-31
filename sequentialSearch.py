#SequentialSearch
Data = [2,3,5,9,11,20,25,39,44,49,52,79]

def sequentialSearch(numArr, searchNum):
    lengthArr = len(numArr)
    for i in range(lengthArr):
        if numArr[i] == searchNum:
            return i
    return -1

result = sequentialSearch(Data, 20)
print(result)
