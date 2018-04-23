def solution(A):
    start_point = len(A)//2
    left_sum =  sum(A[:start_point])
    right_sum = sum(A[start_point:])
    print (left_sum)
    print(right_sum)
    min_value = abs(left_sum-right_sum)
    while start_point < len(A)-1:
        start_point+=1
        temp_min = abs(sum(A[:start_point])-sum(A[start_point:]))
        if temp_min < min_value:
            min_value = temp_min
    return min_value
print(solution([-100,100]))