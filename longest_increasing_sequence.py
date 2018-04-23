def lis(arr,n):
    L = [1 for i in range(n)]

    for i in range(1,n):
        for j in range(i):
            if arr[i] > arr[j] \
                    and L[i] < L[j] +1:
                L[i] = L[j] +1

    print ("LIS is:", max(L))


if __name__=="__main__":
    test_arr = [10,9,20,12,21,30,22,40,1]
    len_arr = len(test_arr)
    lis(test_arr,len_arr)