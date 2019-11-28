# Given an array of integers, 
# write a function to determine whether the array could become non-decreasing by
#  modifying at most 1 element.

# For example, given the array [10, 5, 7], you should return true,
#  since we can modify the 10 into a 1 to make the array non-decreasing.

# Given the array [10, 5, 1], you should return false, 
# since we can't modify any one element to get a non-decreasing array.
import numpy as np

def check_non_decreasing(arr):
    p = None

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            if p is not None:
                return False
            p = i
    
    return (p==0 or p==len(arr)-2 or arr[p-1] <= arr[p+1] or arr[p] <= arr[p+2])


test_arr = [1]
# test_arr = np.arange(10)[::-1]
print (test_arr)
print(check_non_decreasing(test_arr))