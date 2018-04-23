import numpy as np


def jumpSearch(arr,startIndex,endIndex):
    if len(arr) >=1:
        if arr[endIndex] < numToFind:
            startIndex = endIndex
            endIndex = endIndex + numToJump
            return jumpSearch(arr,startIndex,endIndex)
        elif arr[endIndex] > numToFind:
            for j in range(startIndex,endIndex):
                if arr[j] == numToFind:
                    return j
            return -1
        elif arr[endIndex] == numToFind:
            return endIndex
    else:
        if arr[0] == numToFind:
            return 0
        else:
            return -1

if __name__ =="__main__":
    inputArr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    numToFind = 377
    numToJump = int(np.sqrt(len(inputArr)))-1
    index = jumpSearch(inputArr,0,numToJump)
    print("index of "+str(numToFind)+":",index)