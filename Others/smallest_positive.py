def solution(A):

    if len(A)==1:
        if A[0]-1 >1:
            return A[0]+1
        else:
            return 1
    sorted_A = sorted(A)
    start_pointer = 0
    end_pointer = len(sorted_A)-1
    while start_pointer < end_pointer:
        next_num = sorted_A[start_pointer+1]
        if next_num - sorted_A[start_pointer] >1:
            result = sorted_A[start_pointer]+1
            if result > 0:
                return result
            else:
                return 1
        else:
            start_pointer+=1
    if start_pointer == end_pointer:
        result = sorted_A[end_pointer]+1
        if result >0:
            return result
        else:
            return 1



print(solution([2]))