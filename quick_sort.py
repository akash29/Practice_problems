def partition(A,start,end):
    pivot = A[end]
    part_index = start
    for i in range(start,end):
        if A[i]<=pivot:
            A[i],A[part_index] = A[part_index],A[i]
            part_index += 1
    A[part_index],A[end]= A[end],A[part_index]
    return part_index

def quick_sort(A,start,end):
    if start<end:
        partition_index = partition(A,start,end)
        quick_sort(A,start,partition_index-1)
        quick_sort(A,partition_index+1,end)



A = [1,3,2,4,6,5,8,9,7]
quick_sort(A,0,8)
print(A)


