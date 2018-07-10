def pair_positive_negative(lst):
    num_list = {}
    result_list = []
    for i,j in enumerate(lst):
        if abs(j) not in num_list:
            num_list[abs(j)]=1
        else:
            num_list[abs(j)]+=1
            if num_list[abs(j)] == 2:
                result_list.append(-abs(j))
                result_list.append(abs(j))

    print(result_list)

pair_positive_negative([-1,2,-3,4,-5,-6,7])
pair_positive_negative([1,2,-2,3,4,-4,-3])