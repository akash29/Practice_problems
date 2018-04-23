def find_product(arr,pdt):

    sorted_arr = sorted(arr)
    start_ptr = 0
    end_ptr = len(arr)-1

    while start_ptr <= end_ptr:
        temp_pdt = sorted_arr[start_ptr]*sorted_arr[end_ptr]
        if temp_pdt == pdt:
            return [sorted_arr[start_ptr],sorted_arr[end_ptr]]
        elif temp_pdt > pdt:
            end_ptr-=1
        elif temp_pdt < pdt:
            start_ptr+=1

    return []

result = find_product([2,4,1,6,5,40,-1],12)
print (result)