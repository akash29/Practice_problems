
def binarySearch(arr,left,right):
    if len(arr) >=1:
        middleIndex = int(left + (right-left)/2)
        if left > right:
            return -1
        elif arr[middleIndex] < numToFind:
           middleIndex += 1
           return binarySearch(arr,middleIndex,right)
        elif arr[middleIndex] > numToFind:
            middleIndex -= 1
            return binarySearch(arr,left,middleIndex)
        elif arr[middleIndex] == numToFind:
            return middleIndex
    elif arr[0] == numToFind:
        return 0


def exponentialSearch(arr,endIndex):
    if len(arr) >=1:

        if arr[endIndex] < numToFind:
            endIndex *= 2
            if endIndex > len(arr) - 1:
                endIndex = len(arr) - 1
            return exponentialSearch(arr,endIndex)
        elif arr[endIndex] > numToFind:
            return binarySearch(arr,endIndex/2,endIndex)
        elif arr[endIndex] == numToFind:
            return endIndex
    elif arr[0] == numToFind:
        return 0
    else:
        return -1


if __name__=="__main__":
    inputArr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23,
                  24, 33, 35, 42, 47]
    numToFind = -1
    start = 1
    index = exponentialSearch(inputArr,start)
    print("index of "+str(numToFind)+":",index)