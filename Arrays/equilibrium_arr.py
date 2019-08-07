def find_equilibrium_pt(arr):
    sum_arr_1 = [0]*len(arr)
    sum_arr_1[0] = arr[0]
    sum_arr_2 = [0]*len(arr)
    sum_arr_2[-1] = arr[-1]
    for i in range(1,len(arr)):
        sum_arr_1[i] = sum_arr_1[i-1]+arr[i]
    for i in range(len(arr)-2,-1,-1):
        sum_arr_2[i] = sum_arr_2[i+1]+arr[i]

    for j, k in enumerate(zip(sum_arr_1,sum_arr_2)):
        if k[0] == k[1]:
            return j

#test_arr = [1,3,5,2,2]
test_arr = [9,9,4,3,2]
print(find_equilibrium_pt(test_arr))
