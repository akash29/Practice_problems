def find_inflection(lst):
    lst = sorted(lst)
    middle_index = len(lst)//2
    neg_arr = lst[:middle_index][::-1]
    pos_arr = lst[middle_index:]
    out_lst=[]
    for i,j in zip(neg_arr,pos_arr):
        out_lst.append(i)
        out_lst.append(j)
    print(out_lst)

my_lst = [-1,2,-3,4,-5,6]
test_2 = [0,-1,2,4,5,-7,-8,9,-10,-11]

find_inflection(my_lst)
find_inflection(test_2)