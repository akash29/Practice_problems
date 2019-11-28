# Given a list of possibly overlapping intervals, 
# return a new list of intervals where all overlapping intervals have been merged.
# given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)]

def heapify(arr, i , n):
    smallest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[left][0] < arr[smallest][0]:
        smallest = left
    if right < n and arr[right][0] < arr[smallest][0]:
        smallest = right
    
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, smallest, n)

def construct_heap(arr):
    n = len(arr)
    for i in range(len(arr)-1,-1,-1):
        heapify(arr,i, n)
    return arr

def extract_min(arr,res_arr,current_max=float('-inf'),current_min=float('-inf')):
    if len(arr) > 0 :
        val = arr[0]
        arr[0] = arr[-1]
        arr.pop()
        n = len(arr) 
        heapify(arr,0, n)
        if val[0] > current_min and val[1] > current_max:
            current_max = val[1]
            current_min = val[0]
            res_arr.append((val[0],val[1]))
            extract_min(arr,res_arr,current_max,current_min)
        else:
            extract_min(arr, res_arr, current_max, current_min)
    else:
        return


current_max = float('-inf')
current_min = float('-inf')
res_list = []
test_arr = [(1, 3), (5, 8), (4, 10), (20, 25)]
heap_arr = construct_heap(test_arr)
extract_min(heap_arr,res_list)
print (res_list)