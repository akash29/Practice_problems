
def merge(left,right,A,mid):
    nl = len(left)
    nr = len(right)
    i=0
    j=0;k=0;insertion_count=0
    while i < nl and j < nr:
        if left[i]<=right[j]:
            A[k] = left[i]
            i+=1
        else:
            A[k] = right[j]
            j+=1
            insertion_count+=mid-i

        k+=1

    while i< nl:
        A[k] = left[i]
        i+=1
        k+=1

    while j < nr:
        A[k] = right[j]
        j+=1
        k+=1

    return insertion_count


def merge_sort(A):
    n = len(A)
    if n>=2:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        count_0=merge_sort(left)
        count_1=merge_sort(right)
        count_2=merge(left,right,A,mid)
        print (A)
        return count_0+count_1+count_2
    else:
        return 0

print(merge_sort([4,3,2,1]))