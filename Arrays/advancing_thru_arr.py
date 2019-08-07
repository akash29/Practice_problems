import numpy as np

def advance_thru_arr(A):
    if len(A) > 0:
        i = 0
        while i < len(A):
            if A[i]+i < len(A) - 1:
                new_arr = A[i+1:A[i]+i+1]
                min_index = np.argmax(new_arr)+1
                max_value = max(new_arr)
                if max_value <= 0:
                    return False
                else:
                    i += min_index
            elif A[i]+i >= len(A)-1:
                return True
    else:
        return True

#test_arr = [3,3,1,0,2,0,1]
#test_arr = [3,2,0,0,2,0,1]
#test_arr= [4,1,3,0,1,0,2]
#test_arr=[3,3,-1,0,-2,0,1]
test_arr = [2,4,1,1,0,2,3]
print(advance_thru_arr(test_arr))