def delete_duplicates(A):
    if len(A) > 1:
        i = 1
        j = i-1
        N = len(A)
        while i < N:
            if i-j == 1 and A[i] == A[j]:
                i += 1
            elif i-j == 1 and A[i] != A[j]:
                i += 1
                j += 1
            elif i-j > 1 and A[i] == A[j]:
                i += 1
            elif i-j > 1 and A[i] != A[j]:
                j += 1
                A[j] = A[i]
                i += 1
        return A[:j+1]
    elif len(A) == 1:
        return A
    else:
        return []

test_arr = [2,3,5,5,7,11,11,11,13]
print(delete_duplicates(test_arr))