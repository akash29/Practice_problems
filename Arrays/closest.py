def ClosestXdestinations(numDestinations, allLocations, numDeliveries):
    # WRITE YOUR CODE HERE
    sum_arr = [(i,abs(k[0])+abs(k[1])) for i,k in enumerate(allLocations)]
    cord_map = {}
    for i,k in enumerate(allLocations):
        cord_map[i] = k
    sorted_arr = mergeSort(sum_arr)
    i = 0
    out_result = []
    while numDeliveries >0 and i < numDestinations:
        out_result.append(cord_map[sorted_arr[i][0]])
        i+=1
        numDeliveries-=1
    print(out_result)

def mergeSort(len_arr):
    n = len(len_arr)
    if n > 1:
        mid = len(len_arr) // 2
        left = len_arr[:mid]
        right = len_arr[mid:]
        mergeSort(left)
        mergeSort(right)
        sorted_arr = merge(left, right, len_arr, mid)
        return sorted_arr


def merge(left, right, A, mid):
    nl = len(left)
    nr = len(right)
    i = 0
    j = 0
    k = 0
    insertion_count = 0
    while i < nl and j < nr:
        if left[i][1] <= right[j][1]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
            insertion_count += mid - i

        k += 1

    while i < nl:
        A[k] = left[i]
        i += 1
        k += 1

    while j < nr:
        A[k] = right[j]
        j += 1
        k += 1

    return A







num_dest = 6
all_loc = [[3,6],[2,4],[5,3],[2,7],[1,8],[7,9]]
num_deli = 3
ClosestXdestinations(num_dest,all_loc, num_deli)