def check_contiguous(lst):
    sorted_lst = sorted(set(lst))
    sub_lst = [(sorted_lst[i]-sorted_lst[0])+1 for i in range(len(sorted_lst))]
    sum_lst = sum(sub_lst)
    lst_len = len(sorted_lst)
    expected_len = (lst_len*(lst_len+1))//2
    if expected_len==sum_lst:
        return 'Yes'
    return 'No'

print(check_contiguous([1,2,3,4,5,4,4,6,6]))
print(check_contiguous([2,1,5,6,8]))
print(check_contiguous([5,2,3,6,4,4,6,6]))
print(check_contiguous([10,14,10,12,12,13,15]))