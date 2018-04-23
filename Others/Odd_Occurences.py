def solution (A):
    result = 0
    for i in A:
        result ^= i
    return result

print (solution([9,1,1,2,2]))