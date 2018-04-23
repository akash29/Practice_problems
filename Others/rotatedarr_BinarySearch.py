def searchIndex_rotatedarr(arr,l,r):
    if arr[l] < arr[r]:
        return l

    while l<=r:
        m = int(l+(r-l)/2)

        if arr[m] < arr[r]:
            r = m
        elif arr[m] > arr[r]:
            l = m+1
        else:
            return l
    return -1

input_arr = [7,8,9,10,1,2,3,4,5]
min_index = searchIndex_rotatedarr(input_arr,0,len(input_arr)-1)
print ("Min index:",min_index)
