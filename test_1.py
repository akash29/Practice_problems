def solution(A):
    A_len = len(A)
    candidate = -1
    candidate_count = 0
    candidate_index = -1

    for index in range(A_len):
        if candidate_count == 0:
            candidate = A[index]
            candidate_index = index
            candidate_count += 1
        else:
            if A[index] == candidate:
                candidate_count += 1
            else:
                candidate_count -= 1

    if len([number for number in A if number == candidate]) <= A_len // 2:
        return -1
    else:
        return candidate_index

print(solution([3,4,3,5,3,7,3,8,3]))