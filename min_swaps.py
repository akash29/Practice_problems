def find_min_swaps(arr):

    sorted_arr = sorted(arr)
    arr_map={}
    for i,j in enumerate(arr):
        arr_map[j]=i

    swaps = 0
    for i,j in enumerate(arr):
        if j!=sorted_arr[i]:
            swaps+=1
            sort_index = arr_map[sorted_arr[i]]
            actual_index = arr_map[j]
            arr[sort_index],arr[actual_index] = arr[actual_index],arr[sort_index]
            arr_map[j] = sort_index
    return swaps



A = [1,5,4,3,2]
print(find_min_swaps(A))