def solution(A):
    # write your code in Python 3.6
    maj_index = 0
    count=1
    for i in range(len(A)):
        if A[i]==A[maj_index]:
            count+=1
        else:
            count-=1
        if count == 0:
            maj_index = i
            count = 1
    print (maj_index)

solution([1,2,3,4,4,4,4,4])