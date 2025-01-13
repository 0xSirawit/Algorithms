def insertionSort(arrNum):
    for i in range(1,len(arrNum)):
        t = arrNum[i]
        for j in range(i-1,-1,-1):
            if t > arrNum[j]: break
            arrNum[j+1] = arrNum[j]
            arrNum[j] = t
        print(arrNum)
    return arrNum

testCase = [4,1,3,2,5]
print(insertionSort(testCase))
