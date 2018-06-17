#optimize it
def transpose_mat(mat):
    trans = [[row[i] for row in mat] for i in range(len(mat[0]))]
    return trans

def rotate_mat(mat):
    temp = [[row[i] for row in mat] for i in range(len(mat[1]))]
    rotated = [row[::-1] for row in temp]
    rotated_trans = transpose_mat(rotated)
    print (rotated_trans)

test_mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]

test_mat_2 = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]



transposed_mat = transpose_mat(test_mat_2)
rotate_mat(transposed_mat)