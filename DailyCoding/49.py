def max_contiguous_sum(arr):
    n = len(arr)
    sum_arr = [0]*n
    sum_arr[0] = arr[0]
    i = 1
    max_val = 0
    while i < n:
        sum_val = sum_arr[i-1]+arr[i]
        if sum_val < 0:
            sum_arr[i]=0
        else:
            max_val = sum_val if sum_val > max_val else max_val
            sum_arr[i] = sum_val
        i+=1
    return max_val

test_arr_1 = [34,-50,42,14,-5,86]
test_arr_2 = [1,100,200,-200,500,-500]
test_arr_3 = [-1,-2,-3,-4,-5,-6]
test_arr_4 = [-1,-2,-3,-6,-10,9]
test_arr_5 = [-2,-3,4,-1,-2,1,5,-3]
test_arr = [test_arr_1,test_arr_2,test_arr_3,test_arr_4,test_arr_5]
for i in test_arr:
    print(max_contiguous_sum(i))
# max_contiguous_sum([34, -50, 42, 14, -5, 86])