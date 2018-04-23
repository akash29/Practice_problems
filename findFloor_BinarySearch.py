def floor(arr,l,r,key):

    while r-l >1:
        m = int(l+(r-l)/2)
        if arr[m] <= key:
            l = m
        else:
            r = m
    if key < arr[0]:
        return -1
    else:
        return arr[l]

arr = [1,2,3,4,6,8]
key = 7
val = floor(arr,0,len(arr)-1,key)
print ("Floor: ",val)