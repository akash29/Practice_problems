
def heapify(arr,i,n):
    left = 2*i+1
    right = 2*i+2
    smallest = i
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        heapify(arr,smallest,n)


def __extract_min(arr):
    if len(arr) > 1:
        min_value = arr[0]
        last_value = arr.pop()
        arr[0] = last_value
        heapify(arr, 0, len(arr))
        return min_value
    else:
        return arr.pop()


def extract_k_min(arr,k):
    result_list = []
    k = k if k < len(arr) else len(arr)
    for _ in range(k):
        result_list.append(__extract_min(arr))
    return result_list


temp_arr = [3,8,2,7,1,0,5,22,11]
n = len(temp_arr)
for i in range(n,-1,-1):
    heapify(temp_arr,i,n)
print(extract_k_min(temp_arr,6))



