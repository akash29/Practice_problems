def compare_triplets(A, B):
    A_score = 0
    B_score = 0
    for i,j in zip(A, B):
        if i < j:
            B_score += 1
        elif i > j:
            A_score += 1
    return [A_score, B_score]

a = [17,28,30]
b = [99,16,8]
print(compare_triplets(a,b))
