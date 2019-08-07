def find_max_contiguous(arr):
    sum_arr = [0]*len(arr)
    sum_arr[0] = arr[0]
    for i in range(1, len(arr)):
        if arr[i]+sum_arr[i-1] >= arr[i]:
            sum_arr[i] = sum_arr[i-1]+arr[i]
        else:
            sum_arr[i] = arr[i]

    return max(sum_arr)


#test_arr = [1,2,3,-2,5]
# test_arr=[-2,-3,4,-1,-2,1,5,-3]
# test_arr = [-1,-2,-3,-4]
test_arr=[-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print(find_max_contiguous(test_arr))