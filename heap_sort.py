def heapify(arr,n,id):
    largest = id
    left = id*2+1
    right = id*2+2

    if left<n and arr[id]<arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right

    if id!=largest:
        arr[id],arr[largest] = arr[largest], arr[id]
        heapify(arr,n,largest)

def heap_sort(arr):
    n = len(arr)
    count = 0

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap

        heapify(arr, i, 0)
        count += 1
    print (count)


arr = [3,2,4,1]
heap_sort(arr)
print(arr)