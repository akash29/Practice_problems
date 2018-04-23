def solution(A):
    sorted_A = sorted(A)
    if len(sorted_A)>=3:
        R_index = len(sorted_A)-1
        Q_index = len(sorted_A)-2
        P_index = len(sorted_A)-3
        while P_index >=0:
            R = sorted_A[R_index]
            Q = sorted_A[Q_index]
            P = sorted_A[P_index]
            if P>=0 and Q>=0 and R>=0:
                if R>Q>P and Q+P > R:
                    return 1
                else:
                    R_index-=1
                    Q_index-=1
                    P_index-=1
            else:
                return 0
        return 0
    else:
        return 0

print(solution([10,2,5,1,8,20]))
