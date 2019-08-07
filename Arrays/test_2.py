def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


print(parity(11))
print(0XFFFF)


def parity_2(x, n):
    if n == 1:
        return x & 0x1
    n = n // 2
    y = x >> n
    x = x ^ y
    return parity_2(x, n)


print(parity_2(11, 4))

# propagate right most bit
x = 64
y = x & ~(x - 1)
to_shift = y - 1
print(bin(x))
print(bin(x | to_shift))

# mod by bit operation
x = 16
y = 2
print(bin(x))
print(bin(y))
print(x % y)
print(x & (y - 1))

# test if x is power of 2
x = pow(2, 9) - 7
y = 2
print(x)
print(y)
out = True if (x & (y - 1)) == 0 else False
print(out)

x = 73
temp = x
i = 1
j = 6
x_bin = bin(x)
print(x_bin)
ith_pos = x >> i & 0x1
print(bin(ith_pos))
jth_pos = x >> 6 & 0x1
print(bin(jth_pos))
if ith_pos != jth_pos:
    y = 1 << i
    k = i << j
    temp ^= y | k
    print(bin(temp))


def reverseBits(n):
    rev = 0

    # traversing bits of 'n' from the right
    while (n > 0):

        # bitwise left shift 'rev' by 1
        rev = rev << 1

        # if current bit is '1'
        if (n & 1 == 1):
            rev = rev ^ 1

        # bitwise right shift 'n' by 1
        n = n >> 1

    # required number
    return rev


x = 12
print(bin(x))
y = x >> 3
l = 8 >> 2 | y
print(bin(y))
print(bin(l))
print(reverseBits(x))

print(bin(0xc))
print(bin(0x5))


def sum(x, y):
    while y:
        carry = x & y
        print(bin(carry))
        x ^= y
        print(bin(x))
        y = carry << 1
        print(bin(y))
    return x


sum(5, 3)


def compute_product(x, y):
    running_sum = 0
    while x:
        if x & 0x1:
            running_sum = sum(running_sum, y)
        x >>= 1
        y <<= 1
    return running_sum


def subtract(x, y):
    while y:
        borrow = ~x & y
        x ^= y
        y = borrow << 1
    return x


print(sum(6, 3))

print(compute_product(5, 3))


def add_nums(x, y):
    while y:
        carry = x & y
        x ^= y
        y = carry << 1
    return x


def get_pdt(x, y):
    remaining_sum = 0
    while x:
        if x & 0x1:
            remaining_sum = add_nums(remaining_sum, y)
        x >>= 1
        y <<= 1
    return remaining_sum


def get_power(x, y):
    tot_pdt = x
    while y:
        tot_pdt = get_pdt(tot_pdt, x)
        y >>= 1
    return tot_pdt


print(get_power(18, 4))
print(pow(18, 4))


def dutch_flag_partition(pivot_index, A):
    # TODO - you fill in here.

    if len(A) > 1:
        pivot_val = A[pivot_index]
        smaller, equal, larger = 0, 0, len(A)
        while equal < larger:
            if A[equal] < pivot_val:
                A[smaller], A[equal] = A[equal], A[smaller]
                smaller += 1
                equal += 1
            elif A[equal] == pivot_val:
                equal += 1
            elif A[equal] > pivot_val:
                larger -= 1
                A[larger], A[equal] = A[equal], A[larger]

    return A


print(dutch_flag_partition(1, [0, 1, 1, 0, 2, 1, 2]))


def partition_1(arr):
    smaller = 0
    equal = 0
    larger = len(arr)
    vals = set(arr)
    num1, num2, _ = vals
    while equal < larger:
        if arr[equal] == num1:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
            equal += 1
        elif arr[equal] == num2:
            larger -= 1
            arr[larger], arr[equal] = arr[equal], arr[larger]
        else:
            equal += 1

    return arr


print(partition_1([1, 3, 3, 2, 1, 2, 3]))

import random


def partition(arr, l, r):
    smaller = l
    equal = l
    larger = r+1
    pivot_val = arr[r]
    while equal < larger:
        if arr[equal] < pivot_val:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
            equal += 1
        elif arr[equal]> pivot_val:
            larger -= 1
            arr[larger], arr[equal] = arr[equal], arr[larger]
        else:
            equal += 1

    return smaller, larger


def quicksort(arr, l, r):
    if l >=r:
        return
    lesser, greater = partition(arr, l, r)
    quicksort(arr,l,lesser-1)
    quicksort(arr,greater+1,r)


#test_arr = [1, 3, 3, 2, 1, 2, 3]
test_arr = [2,1,3,4,2,2,8,4,4,4,4]
quicksort(test_arr,0, len(test_arr)-1)
print(test_arr)


def add_one(arr):
    res_arr = [0]*(len(arr) + 1)
    to_sum = 1
    for i in range(len(arr)-1, -1, -1):
        sum_val = arr[i]+to_sum
        sum_res = sum_val % 10
        res_arr[i+1] = sum_res
        to_sum = sum_val // 10

    if to_sum != 0:
        res_arr[0] = to_sum
    else:
        res_arr = res_arr[1:]

    print(res_arr)

test_arr = []
add_one(test_arr)


def multiply_nums(arr1, arr2):

    if arr1[0]==0 or arr2[0]==0:
        return [0]
    else:
        res_arr = [0]*(len(arr1)+len(arr2))
        final_sign = 1
        if arr1[0] * arr2[0] < 0:
            final_sign *= -1
        arr1[0] = abs(arr1[0])
        arr2[0] = abs(arr2[0])
        for i, j in enumerate(reversed(arr1)):
            carry = 0
            for k, p in enumerate(reversed(arr2)):
                res_index = (len(res_arr) - 1) - (i + k)
                sum_num = j*p+carry+res_arr[res_index]
                sum_val = sum_num % 10
                carry = sum_num // 10
                res_arr[res_index] = sum_val
                if k == len(arr2)-1 and carry > 0:
                    res_arr[res_index-1] += carry

        if res_arr[0] == 0:
            res_arr = res_arr[1:]

        res_arr[0] = res_arr[0]*final_sign

        return res_arr



#test_arr_1 = [1,9,3,7,0,7,7,2,1]
test_arr_1 = [0]
test_arr_2= [-7,6,1,8,3,8,2,5,7,2,8,7]

print (multiply_nums(test_arr_1, test_arr_2))