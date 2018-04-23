
def getright_positions(arr,l,r,key):

    while r-l >1:
        m = int(l+(r-l)/2)
        if arr[m] <=key:
            l = m
        else:
            r = m
    return l


def getleft_positions(arr,l,r,key):

    while r-l >1:
        m= int(l+(r-l)/2)
        if arr[m] >=key:
            r = m
        else:
            l = m
    return r

def count_positions(arr,size,key):
    right  = getright_positions(arr,-1,size-1,key)
    left = getleft_positions(arr,0,size-1,key)

    if arr[left] == key and arr[right] == key:
        return (right-left)+1
    else:
        return 0


input_arr = [1,2,3,4,4,4,5,6,6,7]
key = 2
num = count_positions(input_arr,len(input_arr),key)
print ("Num of entries : {0}".format(num))