def solution(N,A):
    counter = [0]*N
    for i in A:
        if N >= i >= 1:
            temp_val = counter[i-1]
            counter[i-1] = temp_val+1
        elif i == N+1:
            max_val = max(counter)
            counter  = [max_val]*N

    return counter

solution(5,[3,4,4,6,1,4,4])

