def array_left_rotation(a, n, k):
    new_arr = a[k:]+a[:k]
    print (new_arr)

array_left_rotation([1,2,3,4,5],5,4)