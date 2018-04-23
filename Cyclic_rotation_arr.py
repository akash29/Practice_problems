def rotation(arr,n, k):
    new_arr = []
    for i, j in enumerate(arr):
        temp_index = i+k
        if temp_index < n:
            new_arr.insert(temp_index,j)
        else:
            temp_index = temp_index % n
            new_arr.insert(temp_index,j)
    return new_arr

print(rotation([1,2,3,4,5],5,4))