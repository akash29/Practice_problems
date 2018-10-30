def find_contiguous_largest_sum(num_list):
    sum_list = [0]*len(num_list)
    sum_list[0] = num_list[0]
    res_list = []
    for i in range(1,len(num_list)):
        if num_list[i]+sum_list[i-1] > num_list[i]:
            sum_list[i] = num_list[i]+sum_list[i-1]
            res_list.append(num_list[i-1])
        else:
            res_list = []
            sum_list[i] = num_list[i]
    if sum_list[-1]>sum_list[-2]:
        res_list.append(num_list[-1])
    return res_list, max(sum_list)


test_list = [2, -8, 3, -2, 4, -10]
seq, max_num = find_contiguous_largest_sum(test_list)
print(max_num)
print(seq)