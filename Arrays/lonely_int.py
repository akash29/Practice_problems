def find_num(arr):
    answer = 0
    for i in arr:
        answer ^=i
    return answer


a = [1,2,3,3,1]
print(find_num(a))