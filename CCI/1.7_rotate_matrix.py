#optimize it
def transpose_mat(mat):
    transposed = [[row[i] for row in mat] for i in range(len(mat))]
    print(transposed)
    return transposed

def rotate_mat(mat,transposed):
    reversed_trans = [transposed[i] for i in range(len(mat) - 1, -1, -1)]
    return reversed_trans

test_mat = [[1,2],
            [3,4]]

test_mat_2 = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]



transposed_mat = transpose_mat(test_mat)
print(rotate_mat(test_mat,transposed_mat))