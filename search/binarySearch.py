import numpy as np


def binarySearch(arr, left, right):
    if len(arr) >= 1:
        middleIndex = int(left + (right - left) / 2)
        if left > right:
            return -1
        elif arr[middleIndex] < numToFind:
            middleIndex += 1
            return binarySearch(arr, middleIndex, right)
        elif arr[middleIndex] > numToFind:
            middleIndex -= 1
            return binarySearch(arr, left, middleIndex)
        elif arr[middleIndex] == numToFind:
            return middleIndex
    elif arr[0] == numToFind:
        return 0


if __name__=="__main__":
    inputArr = [3,1]
    print (inputArr)
    numToFind = 1
    startIndex = 0
    endIndex = len(inputArr)-1
    index = binarySearch(inputArr,startIndex,endIndex)
    print(index)
