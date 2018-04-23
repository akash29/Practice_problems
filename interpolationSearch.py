

def interpolationSearch(arr,start,end):

    if len(arr)>=1:
        if start == end or end < start:
            return -1
        pos = int(start + (numToFind - arr[start])*(end-start)/(arr[end]-arr[start]))
        if arr[pos] < numToFind:
            start = pos+1
            return interpolationSearch(arr,start,end)
        elif arr[pos] > numToFind:
            end = pos-1
            return interpolationSearch(arr,start,end)
        elif arr[pos] == numToFind:
            return pos
    elif arr[0] == numToFind:
        return 0
    else:
        return -1


if __name__ == "__main__":
    inputArr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23,
                  24, 33, 35, 42, 47]
    startPos = 0
    endPos = len(inputArr)-1
    numToFind = 16
    index = interpolationSearch(inputArr,startPos,endPos)
    print("index of "+str(numToFind)+":",index)