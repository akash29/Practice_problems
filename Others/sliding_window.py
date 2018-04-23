

def sliding_window(arr,win):
    val = [max(arr[i:i+win]) for i in range(len(arr)) if i <=len(arr)-win]
    print(val)


input_arr = [1,3,-1,-3,5,3,6,7]
k = 3
sliding_window(input_arr,k)