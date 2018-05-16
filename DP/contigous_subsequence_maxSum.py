def Contiguous_Subsequence(arr):
    if len(arr)<1:
        return arr[0]

    L_arr = arr[:]
    for i in range(1,len(arr)):
        if L_arr[i]+L_arr[i-1] > L_arr[i]:
            L_arr[i] = L_arr[i]+L_arr[i-1]
        else:
            L_arr[i] = L_arr[i]

    return max(L_arr)


test = [5,15,-30,10,-5,40,10]
test2 = [5,-2,-1,8,-5,14,12]
test3 = [5,-2,-30,8,-40,14,12]
print(Contiguous_Subsequence(test))
print(Contiguous_Subsequence(test2))
print(Contiguous_Subsequence(test3))


