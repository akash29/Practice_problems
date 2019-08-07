def bin_search(arr,l,r,x):
    if len(arr)>0:
        middle = l+((r-l)//2)
        if l > r:
            return -1
        elif arr[middle] == x:
            return middle
        elif x > arr[middle]:
            return bin_search(arr,middle+1,r,x)
        elif x < arr[middle]:
            return bin_search(arr,l,middle-1,x)


def find_relative_order(arr1,arr2):
    sorted_arr = sorted(arr1)
    index = 0
    visited = [0]*len(arr1)
    for j,i in enumerate(arr2):
        search_index = bin_search(sorted_arr,0,len(sorted_arr)-1,i)
        while sorted_arr[search_index] == arr2[j]:
            arr1[index] = sorted_arr[search_index]
            visited[search_index] = 1
            search_index += 1
            index += 1
    for k, i in enumerate(visited):
        if not i:
            arr1[index] = sorted_arr[k]
            index+=1

    return arr1


A1 = [2,1,2,5,7,1,9,3,6,8,8]
A2 = [2,1,8,3]
print(find_relative_order(A1,A2))